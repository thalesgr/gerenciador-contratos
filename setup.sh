#!/bin/bash

echo "🔧 Iniciando configuração do ambiente..."

# Verifica se python3-full e python3-venv estão instalados
echo "📦 Verificando pacotes necessários..."
sudo apt update -y
sudo apt install -y python3-full python3-venv

# Cria o ambiente virtual
echo "🐍 Criando ambiente virtual (venv)..."
python3 -m venv venv

# Ativa o ambiente virtual
echo "🚀 Ativando ambiente virtual..."
source venv/bin/activate

# Instala dependências
echo "📚 Instalando dependências do projeto..."
pip install --upgrade pip
pip install flask flask_sqlalchemy flask_wtf wtforms

echo "✅ Ambiente configurado com sucesso!"
echo ""
echo "👉 Para ativar novamente o ambiente, use:"
echo "   source venv/bin/activate"
echo ""
echo "👉 Para rodar sua aplicação Flask, use:"
echo "   python app.py"
echo ""
echo "🎉 Tudo pronto!"
