from flask import Flask, request, jsonify
import idcontador
import conexao

app = Flask(__name__)

@app.route('/alunos', methods=['POST'])
def adicionar_aluno():
    data = request.get_json()
    nome = data['nome']
    idade = data['idade']
    curso = data['curso']
    
    novoId = idcontador.ProximoId('contadorId')
    novoAluno = {
        'id': novoId,
        'nome': nome,
        'idade': idade,
        'curso': curso,
        'ativo': True
    }
    
    alunoRef = conexao.db.reference('Alunos')
    alunoRef.child(str(novoId)).set(novoAluno)
    
    return jsonify({"message": f"Aluno {nome}, {idade}, {curso} adicionado com sucesso."}), 201

if __name__ == '__main__':
    app.run(debug=True)
    
    
@app.route('/alunos/<int:id>', methods=['GET'])
def obter_aluno(id):
    alunoRef = conexao.db.reference('Alunos')
    aluno = alunoRef.child(str(id)).get()
    
    if aluno:
        return jsonify(aluno), 200
    else:
        return jsonify({"error": "Aluno não encontrado"}), 404
    
    
@app.route('/alunos', methods=['GET'])
def obter_todos_alunos():
    alunoRef = conexao.db.reference('Alunos')
    alunos = alunoRef.get()

    if alunos:
        alunos_lista = []
        for id, aluno in alunos.items():
            aluno['id'] = id  # Adiciona o ID ao objeto do aluno
            alunos_lista.append(aluno)
        return jsonify(alunos_lista), 200
    else:
        return jsonify({"error": "Nenhum aluno encontrado"}), 404
    
