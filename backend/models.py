from db import db

class Contract(db.Model):
    __tablename__ = "contracts"

    id = db.Column(db.Integer, primary_key=True)

    # Título ou nome do contrato
    title = db.Column(db.String(150), nullable=False)

    # Cliente ou responsável
    client = db.Column(db.String(150), nullable=False)

    # Fornecedor do contrato
    supplier = db.Column(db.String(150), nullable=False)

    # Categoria (ex.: manutenção, software, consultoria…)
    category = db.Column(db.String(100), nullable=False)

    # Status (ex.: ativo, encerrado, suspenso, em negociação…)
    status = db.Column(db.String(50), nullable=False)

    # Valor monetário do contrato
    amount = db.Column(db.Float, nullable=False)

    # Período
    start_date = db.Column(db.String(20))
    end_date = db.Column(db.String(20))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "client": self.client,
            "supplier": self.supplier,
            "category": self.category,
            "status": self.status,
            "amount": self.amount,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
