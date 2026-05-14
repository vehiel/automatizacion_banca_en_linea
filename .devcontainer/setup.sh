#!/bin/bash

set -e

echo "🔧 Configurando Yarn (fix key error)..."

curl -fsSL https://dl.yarnpkg.com/debian/pubkey.gpg \
  | sudo gpg --dearmor -o /usr/share/keyrings/yarnkey.gpg

echo "deb [signed-by=/usr/share/keyrings/yarnkey.gpg] https://dl.yarnpkg.com/debian/ stable main" \
  | sudo tee /etc/apt/sources.list.d/yarn.list

sudo apt-get update

echo "🐍 Instalando dependencias Python..."
pip install --upgrade pip

if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi

echo "🎭 Instalando Playwright..."
pip install playwright

echo "📦 Instalando dependencias del sistema (Playwright)..."
sudo playwright install-deps

echo "🌐 Instalando navegadores..."
playwright install

echo "✅ Setup completo!"
