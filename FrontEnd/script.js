document.getElementById(id="adicionardados").addEventListener("click", function() {
    var nome = document.getElementById("nome").value;
    var idade = document.getElementById("idade").value;
    var email = document.getElementById("curso").value;

    if (nome === "" || idade === "" || email === "") {
        alert("Preencha todos os campos!");
    }

    let dados = {
        nome: nome,
        idade: idade,
        curso: email
    };

    fetch("http://localhost:5000/alunos", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
    })
    .then(response => response.json())
    .then(data => {
        console.log("Dados enviados com sucesso:", data);
        alert("Dados enviados com sucesso!");
    })
    .catch(error => {
        console.error("Erro ao enviar dados:", error);
        
    });
});

function obterAlunos() {
    fetch("http://localhost:5000/alunos")
        .then(response => response.json())
        .then(data => {
            let tabela = document.getElementById("tabela-alunos").getElementsByTagName('tbody')[0];
            tabela.innerHTML = ""; // Limpa a tabela antes de adicionar novos dados
            data.forEach(aluno => {
                let linha = tabela.insertRow();
                let celulaId = linha.insertCell(0);
                let celulaNome = linha.insertCell(1);
                let celulaIdade = linha.insertCell(2);
                let celulaCurso = linha.insertCell(3);
                let celulaAcoes = linha.insertCell(4);

                celulaId.innerHTML = aluno.id;
                celulaNome.innerHTML = aluno.nome;
                celulaIdade.innerHTML = aluno.idade;
                celulaCurso.innerHTML = aluno.curso;
                celulaAcoes.innerHTML = '<button onclick="obterAluno('+ aluno.id +')">Editar</button> <button>Excluir</button>';
            });
        })
        .catch(error => {
            console.error("Erro ao obter dados:", error);
        });
}

window.onload = function() {
    obterAlunos();
  };