from flask import Flask, request, jsonify
from flask_cors import CORS
from db import db
from errors import register_error_handlers
from routes import register_routes
import os

def create_app(testing=False):
    app = Flask(__name__)
    CORS(app)

    if testing:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["TESTING"] = True
    else:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        DB_DIR = os.path.join(BASE_DIR, "data")
        os.makedirs(DB_DIR, exist_ok=True)
        DB_PATH = os.path.join(DB_DIR, "database.db")
        print(f"[APP] Usando DB em: {DB_PATH}")
        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    register_error_handlers(app)
    register_routes(app)
   
    # Garantir que as tabelas existam ao iniciar
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
