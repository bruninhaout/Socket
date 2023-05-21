import socket

HOST = 'localhost'  # endereço IP ou nome do servidor
PORT = 5000  # porta usada pelo servidor

# cria o socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conecta ao servidor
c.connect((HOST, PORT))

nome_arquivo = input('Digite o nome do arquivo que deseja receber: ')

# envia o nome do arquivo em bytes
c.send(nome_arquivo.encode())

#data = s.recv(102400)

# abre o arquivo
with open(f'copiado_{nome_arquivo}', 'wb') as file:
    while True:
        data = c.recv(4096)
        if not data:
            break
        file.write(data)

print(f'{nome_arquivo} recebido \n')
 
# fecha a conexão
c.close()
