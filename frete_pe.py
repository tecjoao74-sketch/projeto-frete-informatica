<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Sistema de Frete PE</title>
</head>

<body>

<h2>Consulta de Frete</h2>

<label>Digite o CEP:</label>
<input type="text" id="cep">
<button onclick="buscarCEP()">Buscar</button>

<h3 id="endereco"></h3>
<h3 id="frete"></h3>

<script>

async function buscarCEP() {

    let cep = document.getElementById("cep").value

    let url = "https://viacep.com.br/ws/" + cep + "/json/"

    let resposta = await fetch(url)
    let dados = await resposta.json()

    if(dados.erro){
        alert("CEP não encontrado")
        return
    }

    let cidade = dados.localidade
    let estado = dados.uf
    let rua = dados.logradouro

    document.getElementById("endereco").innerHTML =
    "Cidade: " + cidade + "<br>Estado: " + estado + "<br>Rua: " + rua

    let resultado = ""

    if(estado != "PE"){
        resultado = "Não realizamos entregas para este estado"
    }
    else if(cidade.toLowerCase() == "jaboatão dos guararapes"){
        resultado = "Frete GRÁTIS"
    }
    else{
        resultado = "Frete: R$ 10,00"
    }

    document.getElementById("frete").innerHTML = resultado

}

</script>

</body>
</html>
