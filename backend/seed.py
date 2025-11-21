import os
from app import create_app
from db import db
from models import Contract

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DB_DIR, exist_ok=True)
SEED_MARKER = os.path.join(DB_DIR, ".seeded")

def run_seed():
    if os.path.exists(SEED_MARKER):
        print("[SEED] Seed já executado. Pulando.")
        return

    app = create_app()

    with app.app_context():
        print("[SEED] Criando tabelas...")
        db.create_all()

        if Contract.query.first():
            print("[SEED] Registros já existem. Criando marker...")
            with open(SEED_MARKER, "w") as f:
                f.write("seeded")
            return

        print("[SEED] Inserindo registros iniciais...")
        contracts = [
            Contract(
                title="Contrato de TI",
                client="Empresa XPTO",
                supplier="Tech Solutions",
                category="Tecnologia",
                status="Ativo",
                amount=15000.00,
                start_date="2024-01-10",
                end_date="2024-12-31"
            ),
            Contract(
                title="Consultoria Financeira",
                client="Banco Central",
                supplier="Alpha Consultoria",
                category="Consultoria",
                status="Ativo",
                amount=88000.00,
                start_date="2024-02-20",
                end_date="2025-02-20"
            ),
            Contract(
                title="Contrato de Desenvolvimento Web",
                client="Empresa Gamma",
                supplier="Web Solutions",
                category="Tecnologia",
                status="Ativo",
                amount=12000.00,
                start_date="2024-02-01",
                end_date="2024-12-31"
            ),
            Contract(
                title="Contrato de Suporte Técnico",
                client="Empresa Delta",
                supplier="IT Support Ltda",
                category="Tecnologia",
                status="Ativo",
                amount=9000.75,
                start_date="2024-03-10",
                end_date="2025-03-09"
            ),
            Contract(
                title="Contrato de Consultoria em TI",
                client="Empresa Epsilon",
                supplier="Tech Advisors",
                category="Tecnologia",
                status="Ativo",
                amount=17500.00,
                start_date="2024-01-20",
                end_date="2024-12-20"
            ),
            Contract(
                title="Contrato de Infraestrutura de Rede",
                client="Empresa Zeta",
                supplier="Net Solutions",
                category="Tecnologia",
                status="Ativo",
                amount=22000.50,
                start_date="2024-04-01",
                end_date="2025-03-31"
            ),
            Contract(
                title="Contrato de Licenciamento de Software",
                client="Empresa Eta",
                supplier="Soft Licensing",
                category="Tecnologia",
                status="Ativo",
                amount=15000.00,
                start_date="2024-05-05",
                end_date="2025-05-04"
            ),
            Contract(
                title="Contrato de Desenvolvimento Mobile",
                client="Empresa Theta",
                supplier="App Creators",
                category="Tecnologia",
                status="Ativo",
                amount=28000.25,
                start_date="2024-06-10",
                end_date="2025-06-09"
            ),
            Contract(
                title="Contrato de Migração de Sistemas",
                client="Empresa Iota",
                supplier="System Movers",
                category="Tecnologia",
                status="Ativo",
                amount=19500.00,
                start_date="2024-07-01",
                end_date="2025-06-30"
            ),
            Contract(
                title="Contrato de Segurança da Informação",
                client="Empresa Kappa",
                supplier="Cyber Safe",
                category="Tecnologia",
                status="Ativo",
                amount=25000.75,
                start_date="2024-08-15",
                end_date="2025-08-14"
            ),
            Contract(
                title="Contrato de Suporte a Banco de Dados",
                client="Empresa Lambda",
                supplier="DB Masters",
                category="Tecnologia",
                status="Ativo",
                amount=13500.00,
                start_date="2024-09-01",
                end_date="2025-08-31"
            ),
            Contract(
                title="Contrato de Treinamento em TI",
                client="Empresa Mu",
                supplier="Tech Academy",
                category="Tecnologia",
                status="Ativo",
                amount=11000.50,
                start_date="2024-10-01",
                end_date="2025-09-30"
            )
        ]

        db.session.bulk_save_objects(contracts)
        db.session.commit()

        with open(SEED_MARKER, "w") as f:
            f.write("seeded")

        print("[SEED] Seed executado com sucesso.")

if __name__ == "__main__":
    run_seed()
