#!/bin/bash

# Verifica se o script está rodando com bash
if [ -z "$BASH_VERSION" ]; then
    echo "❌ Este script precisa ser executado com bash, não sh."
    echo "   Use: bash start.sh  ou  ./start.sh"
    exit 1
fi

echo "🚀 Iniciando o projeto..."

# Rodando backend via Docker Compose
if [ -d "backend" ]; then
    echo "🐳 Iniciando backend com Docker Compose..."
    cd backend
    docker compose up --build -d
    cd ..
else
    echo "⚠️ Pasta 'backend' não encontrada. Pulei o backend."
fi

# Rodando frontend via npm
if [ -d "frontend" ]; then
    echo "📦 Iniciando frontend com npm..."
    cd frontend
    npm start
else
    echo "⚠️ Pasta 'frontend' não encontrada. Pulei o frontend."
fi

echo "🎉 Projeto iniciado!"
