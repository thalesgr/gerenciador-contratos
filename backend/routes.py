from flask import request, jsonify
from db import db
from models import Contract
from utils import update_model_from_dict
from errors import InvalidUsage

def register_routes(app):
    @app.route("/contracts", methods=["GET"])
    def get_contracts():
        query = Contract.query
        search = request.args.get("search")
        supplier = request.args.get("supplier")
        category = request.args.get("category")
        status = request.args.get("status")
        min_amount = request.args.get("min_amount")
        max_amount = request.args.get("max_amount")
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")

        if search:
            query = query.filter(
                Contract.title.contains(search) |
                Contract.client.contains(search)
            )
        if supplier:
            query = query.filter(Contract.supplier == supplier)
        if category:
            query = query.filter(Contract.category == category)
        if status:
            query = query.filter(Contract.status == status)
        if min_amount:
            try:
                query = query.filter(Contract.amount >= float(min_amount))
            except ValueError:
                from errors import InvalidUsage
                raise InvalidUsage("Parâmetro min_amount inválido")
        if max_amount:
            try:
                query = query.filter(Contract.amount <= float(max_amount))
            except ValueError:
                from errors import InvalidUsage
                raise InvalidUsage("Parâmetro max_amount inválido")
        if start_date:
            query = query.filter(Contract.start_date >= start_date)
        if end_date:
            query = query.filter(Contract.end_date <= end_date)

        try:
            page = int(request.args.get("page", 1))
            if page < 1:
                page = 1
        except ValueError:
            from errors import InvalidUsage
            raise InvalidUsage("Parâmetro page inválido")

        per_page = 10  # fixo

        pagination = query.order_by(Contract.id.desc()).paginate(page=page, per_page=per_page, error_out=False)

        results = [c.to_dict() for c in pagination.items]

        response = {
            "total": pagination.total,
            "page": pagination.page,
            "per_page": per_page,
            "pages": pagination.pages,
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev,
            "items": results
        }

        return jsonify(response)

    @app.route("/contracts/<int:id>", methods=["GET"])
    def get_contract(id):
        contract = Contract.query.get_or_404(id)
        return jsonify(contract.to_dict())

    @app.route("/contracts", methods=["POST"])
    def create_contract():
        data = request.get_json()
        
        if not data:
            raise InvalidUsage("Corpo da requisição vazio ou inválido")

        required_fields = ["title", "client", "supplier", "category", "status", "amount"]
        missing_fields = [f for f in required_fields if f not in data]

        if missing_fields:
            raise InvalidUsage(f"Campos obrigatórios ausentes: {', '.join(missing_fields)}")

        try:
            amount = float(data["amount"])
        except (ValueError, TypeError):
            raise InvalidUsage("Campo 'amount' deve ser um número válido")


        contract = Contract(
            title=data["title"],
            client=data["client"],
            supplier=data["supplier"],
            category=data["category"],
            status=data["status"],
            amount=data["amount"],
            start_date=data.get("start_date"),
            end_date=data.get("end_date"),
        )
        db.session.add(contract)
        db.session.commit()
        return jsonify(contract.to_dict()), 201

    @app.route("/contracts/<int:id>", methods=["PUT"])
    def update_contract(id):
        contract = Contract.query.get_or_404(id)
        data = request.get_json()
        
        if not data:
            raise InvalidUsage("Corpo da requisição vazio ou inválido")

        update_model_from_dict(contract, data, numeric_fields=["amount"])
        
        db.session.commit()
        return jsonify(contract.to_dict())

    @app.route("/contracts/<int:id>", methods=["DELETE"])
    def delete_contract(id):
        contract = Contract.query.get_or_404(id)
        db.session.delete(contract)
        db.session.commit()
        return jsonify({"message": "Contrato excluído com sucesso"})
