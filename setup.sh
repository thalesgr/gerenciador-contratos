#!/bin/bash

# Verifica se o script está rodando com bash
if [ -z "$BASH_VERSION" ]; then
    echo "❌ Este script precisa ser executado com bash, não sh."
    echo "   Use: bash setup.sh  ou  ./setup.sh"
    exit 1
fi

echo "🔧 Iniciando configuração do ambiente..."

# Verifica pacotes Python
echo "📦 Verificando pacotes necessários..."
sudo apt update -y
sudo apt install -y python3-full python3-venv

# Verifica se Docker está instalado
if ! command -v docker &> /dev/null
then
    echo "⚠️  Docker não está instalado. Por favor, instale o Docker antes de continuar."
    echo "   https://docs.docker.com/get-docker/"
else
    echo "🐳 Docker encontrado!"
fi

# Cria venv
echo "🐍 Criando ambiente virtual (venv)..."
python3 -m venv --upgrade-deps venv

# Ativa venv
echo "🚀 Ativando ambiente virtual..."
source venv/bin/activate

# Instala dependências backend
echo "📚 Instalando dependências do backend..."
pip install --upgrade pip setuptools wheel
pip install -r backend/requirements.txt

echo "✅ Backend configurado com sucesso!"

# Setup do frontend
if ! command -v npm &> /dev/null
then
    echo "⚠️  npm não está instalado. Por favor, instale Node.js e npm para continuar."
    echo "   https://nodejs.org/"
else
    echo "📦 Instalando dependências do frontend..."
    if [ -d "frontend" ]; then
        cd frontend
        npm install
        cd ..
        echo "✅ Frontend configurado com sucesso!"
    else
        echo "⚠️  Pasta 'frontend' não encontrada. Pulei o setup do frontend."
    fi
fi

echo ""
echo "👉 Para ativar novamente o ambiente backend, use:"
echo "   source venv/bin/activate"
echo ""
echo "💡 Para rodar testes com pytest, ative o ambiente virtual primeiro:"
echo "   source venv/bin/activate"
echo "   pytest -v"
echo ""
echo "👉 Para rodar sua aplicação, use o script start.sh:"
echo "   ./start.sh"
echo ""
echo "🎉 Tudo pronto!"
