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


echo "☕ Installing Java..."
sudo apt-get install -y default-jre

echo "📊 Installing Allure..."
ALLURE_VERSION=2.45.0

wget https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz

tar -zxvf allure-${ALLURE_VERSION}.tgz

sudo mv allure-${ALLURE_VERSION} /opt/allure
sudo rm allure-${ALLURE_VERSION}.tgz

sudo ln -sf /opt/allure/bin/allure /usr/bin/allure

echo "✅ Verifying Allure installation..."
allure --version || exit 1

echo "🐍 Installing Python dependencies..."
pip install --upgrade pip
pip install pytest
pip install allure-pytest

if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi

echo "🎭 Installing Playwright..."
pip install playwright

echo "📦 Installing OS dependencies (this fixes your error)..."
yes | python -m playwright install-deps

echo "🌐 Installing browsers..."
python -m playwright install

echo "✅ Setup complete!"