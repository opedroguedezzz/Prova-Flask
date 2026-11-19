import os
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename

# Cria o Blueprint das rotas
produtos_bp = Blueprint("produtos", __name__)

# Cria uma lista para armazenar os produtos temporariamente
produtos_temp = []
contador_id = 1

# Abre a página inicial e mostra os produtos cadastrados
@produtos_bp.route("/")
def index():
    busca = request.args.get("busca", "").strip()
    return render_template("index.html", produtos=produtos_temp, busca=busca)

# Recebe os dados do formulário e salva um novo produto
@produtos_bp.route("/salvar", methods=["POST"])
def salvar():
    global contador_id

    nome = request.form.get("nome", "").strip()
    preco = float(request.form.get("preco", 0))

    # Recebe a foto enviada pelo usuário e define uma imagem padrão
    arquivo = request.files.get("foto")
    nome_imagem = "padrao.png"

    # Verifica se uma foto foi enviada e salva ela na pasta de imagens
    if arquivo and arquivo.filename != "":
        nome_imagem = secure_filename(arquivo.filename)
        arquivo.save(os.path.join("static/uploads", nome_imagem))

    # Cria um dicionário com os dados do produto
    novo = {
        "id": contador_id,
        "nome": nome,
        "preco": preco,
        "imagem": nome_imagem
    }

    # Adiciona o produto na lista e aumenta o contador do ID
    produtos_temp.append(novo)
    contador_id += 1

    # Exibe uma mensagem de confirmação e volta para a página inicial
    flash("Salvo temporariamente na memória!", "success")
    return redirect("/")

# Recebe o ID e exclui o produto correspondente da lista
@produtos_bp.route("/excluir/<int:id>", methods=["GET"])
def excluir(id):
    global produtos_temp
    produtos_temp = [p for p in produtos_temp if p["id"] != id]
    return redirect("/")
