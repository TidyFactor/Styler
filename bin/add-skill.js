#!/usr/bin/env node
/**
 * bin/add-skill.js — CLI installer wrapper for tidyfactor-styler
 */

const fs = require('fs');
const path = require('path');

const targetDir = process.cwd();
const skillSource = path.resolve(__dirname, '..');
const agentSkillsDir = path.join(targetDir, '.agents', 'skills', 'tidyfactor-styler');

fs.mkdirSync(agentSkillsDir, { recursive: true });

function copyRecursive(src, dest) {
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (['.git', 'node_modules', 'dist'].includes(entry.name)) continue;
    if (entry.isDirectory()) {
      fs.mkdirSync(destPath, { recursive: true });
      copyRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

copyRecursive(skillSource, agentSkillsDir);
console.log('✓ Successfully injected tidyfactor-styler skill into .agents/skills/tidyfactor-styler');
