#!/usr/bin/env node
/**
 * bin/add-skill.js — Multi-Agent Skill Installer Wrapper for tidyfactor-styler
 * Supports Trae, Cursor, Windsurf, Antigravity, GitHub Copilot, RooCode, OpenCode, KiloCode, Warp, and Universal.
 *
 * @license Apache-2.0
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

const targetDir = process.cwd();
const skillSource = path.resolve(__dirname, '..');
const skillName = 'tidyfactor-styler';

const AGENT_MAP = [
  { name: 'Trae AI IDE',               dir: path.join(targetDir, '.trae', 'skills', skillName),        test: path.join(targetDir, '.trae') },
  { name: 'Cursor IDE',                dir: path.join(targetDir, '.cursor', 'skills', skillName),      test: path.join(targetDir, '.cursor') },
  { name: 'Windsurf Cascade',          dir: path.join(targetDir, '.windsurf', 'skills', skillName),    test: path.join(targetDir, '.windsurf') },
  { name: 'GitHub Copilot',            dir: path.join(targetDir, '.github', 'prompts', skillName),     test: path.join(targetDir, '.github') },
  { name: 'RooCode',                   dir: path.join(targetDir, '.roo', 'skills', skillName),         test: path.join(targetDir, '.roo') },
  { name: 'OpenCode / Zen',            dir: path.join(targetDir, '.opencode', 'skills', skillName),    test: path.join(targetDir, '.opencode') },
  { name: 'KiloCode',                  dir: path.join(targetDir, '.kilocode', 'skills', skillName),    test: path.join(targetDir, '.kilocode') },
  { name: 'Warp Terminal',             dir: path.join(targetDir, '.warp', 'skills', skillName),        test: path.join(targetDir, '.warp') },
  { name: 'Kiro Spec IDE',             dir: path.join(targetDir, '.kiro', 'skills', skillName),        test: path.join(targetDir, '.kiro') },
  { name: 'Claude Code',               dir: path.join(targetDir, '.claude', 'skills', skillName),      test: path.join(targetDir, '.claude') },
  { name: 'Zed AI Agent',              dir: path.join(targetDir, '.zed', 'skills', skillName),         test: path.join(targetDir, '.zed') },
  { name: 'Google Antigravity/Gemini', dir: path.join(targetDir, '.agents', 'skills', skillName),      test: path.join(targetDir, '.agents') },
];

function copyRecursive(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (['.git', 'node_modules', 'dist'].includes(entry.name)) continue;
    if (entry.isDirectory()) {
      copyRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

// Determine installation targets
let mountedTargets = [];

for (const agent of AGENT_MAP) {
  if (fs.existsSync(agent.test)) {
    copyRecursive(skillSource, agent.dir);
    mountedTargets.push(agent.name + ' (' + path.relative(targetDir, agent.dir) + ')');
  }
}

// Always ensure universal fallback in .agents/skills/
const defaultDir = path.join(targetDir, '.agents', 'skills', skillName);
copyRecursive(skillSource, defaultDir);
if (!mountedTargets.some(t => t.includes('.agents'))) {
  mountedTargets.push('Universal Default (.agents/skills/' + skillName + ')');
}

console.log('✨ Successfully injected ' + skillName + ' into:');
mountedTargets.forEach(t => console.log('  • ' + t));
