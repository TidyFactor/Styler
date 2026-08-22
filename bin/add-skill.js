#!/usr/bin/env node
/**
 * bin/add-skill.js — CLI installer wrapper for tidyfactor-styler
 */

const fs = require("fs");
const path = require("path");

const SKILL_NAME = "tidyfactor-styler";
const SOURCE_DIR = path.resolve(__dirname, "..");
const HOME = process.env.USERPROFILE || process.env.HOME;
const GLOBAL_CONFIG_SKILL = path.join(HOME, ".gemini", "config", "skills", SKILL_NAME);

function log(msg) {
  console.log(`[${SKILL_NAME}] ${msg}`);
}

function syncDirectory(src, dest) {
  if (!fs.existsSync(src)) return;
  fs.mkdirSync(dest, { recursive: true });
  fs.cpSync(src, dest, { recursive: true });
  log(`✓ Synchronized to: ${dest}`);
}

log(`Installing/updating ${SKILL_NAME}...`);
syncDirectory(SOURCE_DIR, GLOBAL_CONFIG_SKILL);
log(`Successfully registered ${SKILL_NAME}.`);
