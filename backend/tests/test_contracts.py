import pytest
from app import create_app
from db import db

@pytest.fixture
def app():
    app = create_app(testing=True)
    with app.app_context():
        db.create_all()
    yield app
    # Cleanup
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_contract_success(client):
    data = {
        "title": "Contrato Teste",
        "client": "Cliente A",
        "supplier": "Fornecedor X",
        "category": "TI",
        "status": "ativo",
        "amount": 1500.50,
        "start_date": "2024-01-01",
        "end_date": "2024-12-31"
    }

    response = client.post("/contracts", json=data)
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["title"] == "Contrato Teste"
    assert json_data["amount"] == 1500.50

def test_create_contract_missing_fields(client):
    data = {"title": "Faltando campos"}
    response = client.post("/contracts", json=data)
    assert response.status_code == 400
    json_data = response.get_json()
    assert "Campos obrigatórios ausentes" in json_data["error"]

def test_create_contract_invalid_amount(client):
    data = {
        "title": "Contrato",
        "client": "Cliente",
        "supplier": "Fornecedor",
        "category": "TI",
        "status": "ativo",
        "amount": "inválido"
    }
    response = client.post("/contracts", json=data)
    assert response.status_code == 400
    assert "Campo 'amount' deve ser um número válido" in response.get_json()["error"]

def test_get_contracts_with_pagination(client):
    # Criar 15 contratos
    for i in range(15):
        client.post("/contracts", json={
            "title": f"Contrato {i+1}",
            "client": f"Cliente {i+1}",
            "supplier": "Fornecedor",
            "category": "TI",
            "status": "ativo",
            "amount": 1000 + i
        })

    # Página 1
    response = client.get("/contracts")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["page"] == 1
    assert len(json_data["items"]) == 10  # per_page fixo
    assert json_data["has_next"] is True

    # Página 2
    response = client.get("/contracts?page=2")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["page"] == 2
    assert len(json_data["items"]) == 5
    assert json_data["has_prev"] is True
    assert json_data["has_next"] is False

def test_filter_contracts_by_supplier(client):
    client.post("/contracts", json={
        "title": "C1",
        "client": "X",
        "supplier": "Fornecedor 1",
        "category": "TI",
        "status": "ativo",
        "amount": 1000
    })
    client.post("/contracts", json={
        "title": "C2",
        "client": "Y",
        "supplier": "Fornecedor 2",
        "category": "TI",
        "status": "ativo",
        "amount": 2000
    })

    response = client.get("/contracts?supplier=Fornecedor 1")
    json_data = response.get_json()
    assert len(json_data["items"]) == 1
    assert json_data["items"][0]["supplier"] == "Fornecedor 1"

def test_get_contract_by_id(client):
    post = client.post("/contracts", json={
        "title": "Contrato Único",
        "client": "Cliente",
        "supplier": "Fornecedor",
        "category": "RH",
        "status": "ativo",
        "amount": 3000
    })
    cid = post.get_json()["id"]

    response = client.get(f"/contracts/{cid}")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["title"] == "Contrato Único"

def test_update_contract_partial(client):
    post = client.post("/contracts", json={
        "title": "Antigo",
        "client": "Cliente",
        "supplier": "Fornecedor",
        "category": "TI",
        "status": "ativo",
        "amount": 500
    })
    cid = post.get_json()["id"]

    response = client.put(f"/contracts/{cid}", json={
        "title": "Novo Título",
        "amount": 999.99
    })
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["title"] == "Novo Título"
    assert json_data["amount"] == 999.99

def test_update_contract_invalid_amount(client):
    post = client.post("/contracts", json={
        "title": "Contrato",
        "client": "Cliente",
        "supplier": "Fornecedor",
        "category": "TI",
        "status": "ativo",
        "amount": 100
    })
    cid = post.get_json()["id"]

    response = client.put(f"/contracts/{cid}", json={"amount": "inválido"})
    assert response.status_code == 400
    assert "Campo 'amount' deve ser um número válido" in response.get_json()["error"]

def test_delete_contract(client):
    post = client.post("/contracts", json={
        "title": "A deletar",
        "client": "c",
        "supplier": "s",
        "category": "cat",
        "status": "ativo",
        "amount": 123
    })
    cid = post.get_json()["id"]

    response = client.delete(f"/contracts/{cid}")
    assert response.status_code == 200

    response = client.get(f"/contracts/{cid}")
    assert response.status_code == 404
