import pytest  # motor/ engine
import requests  # biblioteca para comunicar com APIs

base_url = 'https://petstore.swagger.io/v2' #endereço da API
headers = {'Content-Type': 'application/json'} #os dados serão no formato json

def testar_incluir_pet ():
# Configura
    # Dados de entrada: virão do pet1.json
    # Resultado Esperado
    status_code_esperado = 200
    nome_pet_esperado = 'Emma'
    tag_esperada = 'vacinado'


# Executa
    resultado_obtido = requests.post (url=base_url + '/pet',
                   data=open('C:\\Users\\Géssica Oliveira\\PycharmProjects\\133pets\\vendors\json\pet1.json', 'rb'),
                   headers=headers
                   )


# Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()  # estrai o json da respose
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    # assert corpo_da_resposta['tags.name'] == tag_esperada <-- assim funciona se for java
    assert corpo_da_resposta ['tags'] [0] ['name'] == tag_esperada  # posição zero, pois a contagem das compostas é por zero sempre


def testar_consultar_pet():
    #  Configura
    # Dados de Entrada
    pet_id = '175201'

    # Resultado Esperado
    status_code_esperado = 200
    nome_pet_esperado = 'Emma'
    tag_esperada = 'vacinado'

    # Executa
    resultado_obtido = requests.get(
        url = base_url +'/pet/' + pet_id,
        headers=headers

    )


    # Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    assert corpo_da_resposta['tags'][0]['name'] == tag_esperada


def testar_alterar_pet():
    status_code_esperado = 200
    nome_pet_esperado = 'Emma'
    status_esperado = 'solded'

    resultado_obtido = requests.put(
        url=f'{base_url}/pet',
        data=open('C:\\Users\\Géssica Oliveira\\PycharmProjects\\133pets\\vendors\\json\\pet2.json', 'rb'),
        headers=headers)


    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_respota = resultado_obtido.json()
    assert corpo_da_respota['name'] == nome_pet_esperado
    assert corpo_da_respota['status'] == status_esperado


def testar_excluir_pet():
    pet_id = '175201'
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'



    resultado_obtido = requests.delete(
        url=base_url + '/pet/' + pet_id,
        headers=headers
    )


    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta ['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == pet_id

