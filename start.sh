#!/bin/bash

# Verifica se está rodando com bash
if [ -z "$BASH_VERSION" ]; then
    echo "❌ Este script precisa ser executado com bash, não sh."
    echo "   Use: bash start.sh  ou  ./start.sh"
    exit 1
fi

echo "🚀 Iniciando o projeto..."

cleanup() {
    echo ""
    echo "🛑 Parando backend e frontend..."
    if [ ! -z "$BACKEND_PID" ]; then
        kill "$BACKEND_PID" 2>/dev/null
    fi
    if [ ! -z "$FRONTEND_PID" ]; then
        kill "$FRONTEND_PID" 2>/dev/null
    fi
    # Para docker compose do backend
    if [ -d "backend" ]; then
        cd backend
        docker compose down
        cd ..
    fi
    echo "✅ Todos os processos parados."
    exit 0
}

trap cleanup SIGINT SIGTERM

# Backend
if [ -d "backend" ]; then
    echo "🐳 Iniciando backend com Docker Compose..."
    cd backend
    docker compose up --build 2>&1 | sed "s/^/[BACKEND] /" &
    BACKEND_PID=$!
    cd ..
else
    echo "⚠️ Pasta 'backend' não encontrada. Pulei o backend."
fi

# Frontend
if [ -d "frontend" ]; then
    echo "📦 Iniciando frontend com npm..."
    cd frontend
    npm start 2>&1 | sed "s/^/[FRONTEND] /" &
    FRONTEND_PID=$!
    cd ..
else
    echo "⚠️ Pasta 'frontend' não encontrada. Pulei o frontend."
fi

echo "🎉 Backend e frontend iniciados! Pressione Ctrl+C para parar."

# Espera pelos processos
wait $BACKEND_PID $FRONTEND_PID
