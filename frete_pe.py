import requests

def buscar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao consultar API")
        return None

    data = response.json()

    if "erro" in data:
        print("CEP não encontrado")
        return None

    return data


def calcular_frete(cidade, estado):

    if estado != "PE":
        return "Não realizamos entregas para este estado."

    if cidade.lower() == "jaboatão dos guararapes":
        return "Frete grátis!"

    return "Frete: R$ 10,00"


cep = input("Digite o CEP: ")

endereco = buscar_endereco(cep)

if endereco:

    cidade = endereco["localidade"]
    estado = endereco["uf"]
    rua = endereco["logradouro"]

    print("\nEndereço encontrado:")
    print("Cidade:", cidade)
    print("Estado:", estado)
    print("Rua:", rua)

    resultado = calcular_frete(cidade, estado)

    print("\nResultado do frete:")
    print(resultado)
