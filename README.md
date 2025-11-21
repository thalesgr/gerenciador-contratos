# Gerenciador de Contratos

Uma aplicação web para gerenciar contratos de serviços e fornecedores de forma eficiente.  
Atualmente, os contratos são gerenciados através de planilhas e documentos espalhados, causando dificuldades para:

- Acompanhar o status dos contratos ativos  
- Identificar contratos próximos do vencimento  
- Manter histórico de alterações  
- Gerar relatórios consolidados  
- Controlar responsabilidades e categorias  

Esta aplicação centraliza essas informações e permite que a equipe gerencie todo o ciclo de vida dos contratos de forma organizada e acessível.

---

## Tecnologias Utilizadas

### Backend
- **Linguagem / Framework**: Python + Flask  
- **Banco de Dados**: SQLite  
- **Principais dependências**:
  - Flask  
  - Flask-Cors  
  - Flask-SQLAlchemy  
  - Flask-Migrate  
  - SQLAlchemy9  
  - python-dotenv  
  - pytest  
  - pytest-flask  

### Frontend
- **Framework**: React.js + JavaScript  
- **Bibliotecas**:
  - react-bootstrap, bootstrap  
  - axios  
  - react-router-dom  
  - react-scripts  
  - @testing-library/react e demais relacionadas a testes  

### Docker
- Backend e banco de dados podem ser levantados via Docker para facilitar a execução local.


## Configuração e execução do Ambiente Local

### Passo 1: Configurar o projeto
Execute o script `setup.sh` para instalar dependências e configurar o ambiente:
```bash
bash setup.sh
```

### Passo 2: Ativar o ambiente vitual
```bash
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```
### Passo 3: Rodar a aplicação
```bash
bash start.sh
```

O projeto já deve abrir a página contendo o conteúdo do projeto.

## Testes

Para rodar os testes da aplicação é apenas necessário um comando: 
```bash
pytest -v
```
## Contato

- Desenvolvedor: Thales Rangel
- GitHub: thalesgr
- LinkedIn: /in/thalesgr

