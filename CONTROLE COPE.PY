<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Dashboard COPE - Governo BA</title>
<style>
body {
    font-family: Arial;
    background-color: #f0f2f5;
}
header {
    background-color: #003366;
    color: white;
    padding: 15px;
    text-align: center;
}
.container {
    width: 80%;
    margin: auto;
    margin-top: 30px;
}
.card {
    background: white;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
}
button {
    background-color: #0055A4;
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
}
</style>
</head>

<body>

<header>
<h2>Dashboard Controle COPE - Bahia</h2>
</header>

<div class="container">

<div class="card">
<h3>Cadastrar COPE</h3>
<input type="text" id="nome" placeholder="Nome do COPE">
<input type="number" id="qtd" placeholder="Quantidade">
<button onclick="cadastrar()">Cadastrar</button>
</div>

<div class="card">
<h3>Nova Autorização</h3>
<input type="text" id="nomeAut" placeholder="Nome do COPE">
<button onclick="autorizar()">Subtrair 1 vaga</button>
</div>

<div class="card">
<h3>Saldos</h3>
<ul id="lista"></ul>
</div>

</div>

<script>
let copes = {};

function cadastrar() {
    let nome = document.getElementById("nome").value.toUpperCase();
    let qtd = parseInt(document.getElementById("qtd").value);

    if(!copes[nome]) copes[nome] = 0;
    copes[nome] += qtd;
    atualizar();
}

function autorizar() {
    let nome = document.getElementById("nomeAut").value.toUpperCase();
    if(copes[nome] && copes[nome] > 0) {
        copes[nome] -= 1;
        atualizar();
    } else {
        alert("COPE sem saldo ou não encontrado");
    }
}

function atualizar() {
    let lista = document.getElementById("lista");
    lista.innerHTML = "";
    for(let nome in copes) {
        lista.innerHTML += `<li>${nome}: ${copes[nome]} vagas</li>`;
    }
}
</script>

</body>
</html>