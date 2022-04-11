import pytest
import requests

base_url = 'https://petstore.swagger.io/v2' #endereço da API
headers = {'Content-Type': 'application/json'} #os dados serão no formato json

def testar_incluir_usuario():
    # dados de entrada vem de user1.json
    status_code_esperado = 200  # se a comunicação teve ida e volta
    code_esperado = 200         # se fez o que pediu (inclusão do usuário)
    type_esperado = 'unknown'
    message_esperada = '5201094'

    resultado_obtido = requests.post(
        url=base_url + '/user',
        data=open('C:\\Users\\Géssica Oliveira\\PycharmProjects\\133pets\\vendors\\json\\user1.json', 'rb'),
        headers=headers
    )

    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperada


def testar_consultar_usuario():
    #  Configura
    # Dados de Entrada
    user_name = 'Jose'


    # Resultado Esperadoc
    status_code_esperado = 200
    id_user = '5201094'
    firstName = user_name
    lastName = 'Amarildo'

    # Executa
    resultado_obtido = requests.get(
        url=base_url + '/user/' + user_name,
        headers=headers
    )


    # Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert corpo_da_resposta['firstName'] == user_name
    assert corpo_da_resposta['lastName'] == lastName


def testar_alterar_usuario():
    status_code_esperado = 200
    user_name = 'Jose'
    status_user = 5


    resultado_obtido = requests.put(
        url=f'{base_url}/user',
        data=open('C:\\Users\\Géssica Oliveira\\PycharmProjects\\133pets\\vendors\\json\\user2.json', 'rb'),
        headers=headers
    )

    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_respota = resultado_obtido.json()
    assert corpo_da_respota['username'] == user_name
    assert corpo_da_respota['userStatus'] == status_user
