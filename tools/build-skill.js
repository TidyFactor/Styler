#!/usr/bin/env node
/**
 * build-skill.js — packages the distributable Claude Skill (.skill file)
 * for tidyfactor-styler from the repo's single source of truth,
 * and synchronizes across all target agent locations.
 */

const fs = require("fs");
const path = require("path");
const { execFileSync, spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const SKILL_NAME = "tidyfactor-styler";
const DIST_DIR = path.join(ROOT, "dist");
const STAGE_DIR = path.join(DIST_DIR, SKILL_NAME);

const HOME = process.env.USERPROFILE || process.env.HOME;
const AGENTS_SKILL = path.resolve(ROOT, "..", ".agents", "skills", SKILL_NAME);
const GLOBAL_CONFIG_SKILL = path.join(HOME, ".gemini", "config", "skills", SKILL_NAME);

const args = process.argv.slice(2);
const outFlagIdx = args.indexOf("--out");
const OUT_FILE =
  outFlagIdx !== -1 && args[outFlagIdx + 1]
    ? path.resolve(ROOT, args[outFlagIdx + 1])
    : path.join(DIST_DIR, `${SKILL_NAME}.skill`);

const ROOT_COPIES = [
  "SKILL.md",
  "references",
  "scripts",
  "tools",
  "bin",
  "assets",
  "brand.json",
  ".tidyfactor",
  "package.json",
  "AGENTS.md",
  "README.md",
  "README.ar.md",
  "README.fa.md",
  "README.es.md",
  "README.pt.md",
  "README.zh.md",
  "README.de.md",
  "README.fr.md",
  "LICENSE",
  "CHANGELOG.md",
];

const EXCLUDED_PATTERNS = [
  /__pycache__/,
  /\.pyc$/,
  /\.DS_Store$/,
  /Thumbs\.db$/,
  /\.git/,
];

function log(msg) {
  console.log(`[build-skill] ${msg}`);
}

function rmrf(p) {
  if (fs.existsSync(p)) fs.rmSync(p, { recursive: true, force: true });
}

function shouldExclude(filePath) {
  return EXCLUDED_PATTERNS.some((pattern) => pattern.test(filePath));
}

function copyFiltered(src, dest) {
  if (!fs.existsSync(src)) return;
  const stat = fs.statSync(src);
  if (stat.isDirectory()) {
    if (shouldExclude(src)) return;
    fs.mkdirSync(dest, { recursive: true });
    for (const file of fs.readdirSync(src)) {
      copyFiltered(path.join(src, file), path.join(dest, file));
    }
  } else {
    if (shouldExclude(src)) return;
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.copyFileSync(src, dest);
  }
}

function zipArchive(stagePath, outFile, cwdDir) {
  log("zipping Claude skill archive...");
  if (fs.existsSync(outFile)) fs.rmSync(outFile);

  const stageBasename = path.basename(stagePath);

  // 1. Try native zip
  try {
    execFileSync("zip", ["-r", "-q", outFile, stageBasename], {
      cwd: cwdDir,
      stdio: "inherit",
    });
    return;
  } catch (err) {}

  // 2. Try Python built-in zipfile module
  try {
    const pythonCmd = process.platform === "win32" ? "python" : "python3";
    execFileSync(pythonCmd, ["-m", "zipfile", "-c", outFile, stageBasename], {
      cwd: cwdDir,
      stdio: "inherit",
    });
    return;
  } catch (pyErr) {}

  // 3. Try PowerShell Compress-Archive
  try {
    const tmpZip = outFile.replace(/\.(skill|zip)$/, ".zip");
    if (fs.existsSync(tmpZip)) fs.rmSync(tmpZip);
    const result = spawnSync(
      "powershell",
      [
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        `Compress-Archive -Path "${stagePath}" -DestinationPath "${tmpZip}" -Force`,
      ],
      { stdio: "inherit" }
    );
    if (result.status === 0) {
      if (tmpZip !== outFile) {
        fs.renameSync(tmpZip, outFile);
      }
      return;
    }
  } catch (winErr) {}

  throw new Error("Failed to create zip archive via zip, Python, or PowerShell.");
}

function syncToTargetLocation(targetDir) {
  log(`synchronizing to target location: ${targetDir}`);
  rmrf(targetDir);
  fs.mkdirSync(targetDir, { recursive: true });
  for (const item of ROOT_COPIES) {
    const src = path.join(ROOT, item);
    const dest = path.join(targetDir, item);
    if (fs.existsSync(src)) {
      copyFiltered(src, dest);
    }
  }
}

function runIntegrityValidation() {
  log("running release validation checks...");
  const validatorScript = path.join(ROOT, "tools", "validate_skill.py");
  if (fs.existsSync(validatorScript)) {
    const pythonCmd = process.platform === "win32" ? "python" : "python3";
    const res = spawnSync(pythonCmd, [validatorScript], { stdio: "inherit" });
    if (res.status !== 0) {
      throw new Error("Validation checks failed. Build aborted.");
    }
  }
}

function main() {
  log(`repo root: ${ROOT}`);
  
  // 1. Run Pre-Build Validation
  runIntegrityValidation();

  log("cleaning previous build...");
  rmrf(STAGE_DIR);
  fs.mkdirSync(STAGE_DIR, { recursive: true });

  log("staging single-source-of-truth files from repo root (filtered)...");
  for (const name of ROOT_COPIES) {
    const src = path.join(ROOT, name);
    const dest = path.join(STAGE_DIR, name);
    copyFiltered(src, dest);
    log(`  + ${name}`);
  }

  const pkg = JSON.parse(fs.readFileSync(path.join(ROOT, "package.json"), "utf8"));
  const versionedOutFile = path.join(DIST_DIR, `${SKILL_NAME}-v${pkg.version}.skill`);

  fs.mkdirSync(path.dirname(OUT_FILE), { recursive: true });
  zipArchive(STAGE_DIR, OUT_FILE, DIST_DIR);
  fs.copyFileSync(OUT_FILE, versionedOutFile);

  const sizeKb = (fs.statSync(OUT_FILE).size / 1024).toFixed(1);
  log(`done → ${path.relative(ROOT, OUT_FILE)} (${sizeKb} KB)`);
  log(`✓ Created versioned archive → ${path.relative(ROOT, versionedOutFile)}`);

  // Auto-sync to Skills-LAB root if located inside Skills-LAB
  const skillLabRoot = path.resolve(ROOT, "..");
  if (path.basename(skillLabRoot) === "Skills-LAB") {
    const skillLabTarget = path.join(skillLabRoot, `${SKILL_NAME}.skill`);
    const skillLabVersionedTarget = path.join(skillLabRoot, `${SKILL_NAME}-v${pkg.version}.skill`);
    fs.copyFileSync(OUT_FILE, skillLabTarget);
    fs.copyFileSync(OUT_FILE, skillLabVersionedTarget);
    log(`✓ Updated Skills-LAB root archives → ${SKILL_NAME}.skill & ${SKILL_NAME}-v${pkg.version}.skill`);
  }

  // Cross-Agent Synchronization
  syncToTargetLocation(AGENTS_SKILL);
  syncToTargetLocation(GLOBAL_CONFIG_SKILL);
  log(`✓ Completed 4-way cross-agent synchronization across all target locations.`);
}

main();
