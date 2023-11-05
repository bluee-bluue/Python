from flask import Flask, jsonify, request

app = Flask(__name__)
users_tarefas = {}


@app.route("/")
def bem_vindo():
    return "Gerenciador de Tarefas"


@app.route("/cadastro/usuario", methods=['POST'])
def cadastro_usuario():
    dic_pessoa = request.json
    user_id = dic_pessoa['usuario_id']
    nome_usuario = dic_pessoa['nome']

    if user_id in users_tarefas:
        return "Usuário já cadastrado"

    users_tarefas[user_id] = []

    if 'titulo' in dic_pessoa:
        titulo_tarefa = dic_pessoa['titulo']
        users_tarefas[user_id].append(titulo_tarefa)
        return f"Usuário cadastrado com sucesso: {nome_usuario} e Tarefa cadastrada com sucesso: {titulo_tarefa}"
    else:
        return f"Usuário cadastrado com sucesso: {nome_usuario}"


'''
{
    "usuario_id": 1,
    "nome": "Caique",
    "titulo": "Tarefa 1"
}
'''


@app.route("/cadastro/tarefa", methods=['POST'])
def cadastro_tarefa():
    dic_tarefa = request.json
    user_id = dic_tarefa['usuario_id']
    titulo_tarefa = dic_tarefa['titulo']

    if titulo_tarefa in users_tarefas[user_id]:
        return "Tarefa já cadastrada"

    if user_id in users_tarefas:
        users_tarefas[user_id].append(titulo_tarefa)
        return f"Tarefa cadastrada com sucesso: {titulo_tarefa}"
    else:
        return "Usuário não encontrado"


'''
{
    "usuario_id": 1,
    "titulo": "Tarefa 1"
}
'''


@app.route("/usuarios", methods=['GET'])
def todos_usuarios():
    return jsonify(users_tarefas)


@app.route("/tarefas/<int:id_usuario>", methods=['GET'])
def tarefas_por_id(id_usuario):
    if id_usuario in users_tarefas:
        return jsonify(users_tarefas[id_usuario])
    else:
        return "Usuário não encontrado"


@app.route("/tarefas/remover", methods=['POST'])
def remove_tarefa():
    dados = request.json
    user_id = dados['usuario_id']
    titulo_tarefa = dados['titulo']

    if user_id in users_tarefas:
        if titulo_tarefa in users_tarefas[user_id]:
            users_tarefas[user_id].remove(titulo_tarefa)
            return f"Tarefa removida com sucesso: {titulo_tarefa}"
        else:
            return "Tarefa não encontrada"
    else:
        return "Usuário não encontrado"


'''
{
    "usuario_id": 1,
    "titulo": "Tarefa 1"
}
'''


@app.route("/tarefas/alterar", methods=['POST'])
def altera_tarefa():
    dados = request.json
    user_id = dados['usuario_id']
    titulo_tarefa = dados['titulo']
    novo_titulo_tarefa = dados['novo_titulo']

    if user_id in users_tarefas:
        if titulo_tarefa in users_tarefas[user_id]:
            users_tarefas[user_id].remove(titulo_tarefa)
            users_tarefas[user_id].append(novo_titulo_tarefa)
            return f"Tarefa alterada com sucesso: {titulo_tarefa} -> {novo_titulo_tarefa}"
        else:
            return "Tarefa não encontrada"
    else:
        return "Usuário não encontrado"


'''
{
    "usuario_id": 1,
    "titulo": "Tarefa 1",
    "novo_titulo": "Tarefa 2"
}
'''

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
