#!/bin/sh

# Garantir diretório de dados
mkdir -p /app/data
chmod 0777 /app/data

echo "[ENTRYPOINT] Executando seed se necessário..."
DB_FILE="/app/data/database.db"

if [ ! -f "$DB_FILE" ]; then
    echo "[ENTRYPOINT] Banco não existe, rodando seed..."
    python /app/seed.py
else
    echo "[ENTRYPOINT] Banco já existe, pulando seed."
fi

echo "[ENTRYPOINT] Iniciando aplicação..."
python /app/app.py
