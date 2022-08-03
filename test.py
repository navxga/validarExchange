from time import sleep
import sys
import pyautogui
import json

# Socket
import socket 
host = 'https://api-integra-private.impacta.adv.br/api/private/v1/cliente/integracao/pendente/execucao' 
port = 7000
addr = (host, port) 
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serv_socket.bind(addr) 
serv_socket.listen(10) 
print('aguardando conexao')
con, cliente = serv_socket.accept() 
print('conectado') 
print('aguardando mensagem') 
recebe = con.recv(1024) 
print('mensagem recebida: '+ recebe.serv_socket.close())


# Declarações
p = pyautogui
def openExchange():
    p.hotkey('win', 'r')
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
