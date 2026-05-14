#!/bin/bash

set -e

echo "🔧 Updating system..."
sudo apt-get update

echo "🔧 Fixing Yarn key issue..."
curl -fsSL https://dl.yarnpkg.com/debian/pubkey.gpg \
  | sudo gpg --dearmor -o /usr/share/keyrings/yarnkey.gpg

echo "deb [signed-by=/usr/share/keyrings/yarnkey.gpg] https://dl.yarnpkg.com/debian/ stable main" \
  | sudo tee /etc/apt/sources.list.d/yarn.list

sudo apt-get update

echo "🐍 Installing Python dependencies..."
pip install --upgrade pip

if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi

echo "🎭 Installing Playwright..."
pip install playwright

echo "📦 Installing OS dependencies (this fixes your error)..."
python -m playwright install-deps

echo "🌐 Installing browsers..."
python -m playwright install

echo "✅ Setup complete!"