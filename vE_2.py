from time import sleep
import pyautogui
import json

# Declarações
p = pyautogui
def openExchange():
    p.hotkey('win', 'r')
    '''
    p.write('C:\\Users\\lnavega\\Projetos\\integra\\src\\Integra.ExchangeService\\bin\\Debug\\netcoreapp3.1\\Integra.ExchangeService.exe')
    '''
    p.write('cmd')
    p.press('enter')

def execute():
    p.write('execute ')
    p.write(id)
    p.press('enter')

# Entrada do Json
with open("listaId.json", encoding = "UTF-8") as jsn:
    ids = json.load(jsn)

# Execução
openExchange()
sleep(1)

for i in ids:
    print(i['Cliente'])
    if i['Cliente'] != 'DAYCOVAL':
        id = i['Id']
        execute()
        sleep(4)

print('Fim da Execução!')
