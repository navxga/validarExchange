from time import sleep
import pyautogui
import json

# Declarações
p = pyautogui
def openExchange():
    p.hotkey('win', 'r')
    p.write('C:\\Users\\lnavega\\Projetos\\integra\\src\\Integra.ExchangeService\\bin\\Debug\\netcoreapp3.1\\Integra.ExchangeService.exe')
    p.press('enter')
def execute():
    p.write('execute ')
    p.write(id)
    p.press('enter')
execute 
# Entrada do Json
with open("listaId.json", encoding = "UTF-8") as jsn:
    ids = json.load(jsn)

# Execução
openExchange()
sleep(1)

executados = 1

for i in ids:
    print(executados, i['Cliente'], end = ' ')
    if i['Cliente'] != 'DAYCOVAL':
        id = i['Id']
        execute()
        print('executando')
        executados += 1
        sleep(15)

print('Fim da Execução!')
print(f'{executados} Ids foram executados.')
