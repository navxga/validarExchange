from time import sleep
import pyautogui
# import requests
import json

# Declarações
p = pyautogui
def openExchange():
    p.hotkey('win', 'r')
    p.write('cmd')
    # p.write('C:\\Users\\lnavega\\Projetos\\integra\\src\\Integra.ExchangeService\\bin\\Debug\\netcoreapp3.1\\Integra.ExchangeService.exe')
    p.press('enter')
def execute():
    p.write('execute ')
    p.write(id)
    p.press('enter')

# # API
# endpoint = 'https://api-integra-private.impacta.adv.br/api/private/v1/cliente/integracao/pendente/execucao'

# requisicao = requests.get(endpoint)

# print('Start')
# print(requisicao)
# print('End')


# Entrada do Json
with open("listaId.json", encoding = "UTF-8") as jsn:
    ids = json.load(jsn)

# Execução
openExchange()
sleep(1)

executados = 1

for i in ids:
    if i['Cliente'] != 'DAYCOVAL':
        print(executados, i['Cliente'], end = ' ')

        id = i['Id']
        execute()
        print('executado.')
        executados += 1
        sleep(15)
    else:
        print(executados, i['Cliente'])

print('Fim da Execução!')
print(f'{executados} Ids foram executados.')
