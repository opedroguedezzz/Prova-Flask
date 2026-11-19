import os
from flask import Flask
from database import db
from models import Categoria
from routes import produtos_bp

app = Flask(__name__)

# Configurações do sistema
app.config["SECRET_KEY"] = "chave_avaliacao_ds1"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///produtos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "static", "uploads")
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Inicialização do banco de dados
db.init_app(app)
app.register_blueprint(produtos_bp)


from flask import Flask
from routes import produtos_bp

app = Flask(__name__)

app.secret_key = "123"
app.config["UPLOAD_FOLDER"] = "static/uploads"

app.register_blueprint(produtos_bp)

if __name__ == "__main__":
    app.run(debug=True)
