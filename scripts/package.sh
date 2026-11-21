#!/usr/bin/env bash
# Validate the skills, then zip each one into dist/<skill>.zip for uploading to Claude.
# Each zip contains the skill's folder at its top level, e.g. time-entry-drafting/SKILL.md.
set -euo pipefail

cd "$(dirname "$0")/.."
python3 scripts/validate.py

rm -rf dist
mkdir -p dist
cd skills
for dir in */; do
  name="${dir%/}"
  zip -qr "../dist/${name}.zip" "$name" -x '*.DS_Store'
  echo "dist/${name}.zip"
done
