import socket

HOST = 'localhost'  # endereço IP do servidor, vazio significa todos os IPs disponíveis
PORT = 5000  # porta para escutar as conexões

# cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# liga o socket ao endereço e porta especificados
s.bind((HOST, PORT))

# espera por conexões
s.listen(1)

print('Servidor aguardando conexões...')

# aceita uma conexão
conn, addr = s.accept()
print('Conectado por', addr)

# recebe o nome do arquivo
nome_arquivo = conn.recv(2048).decode('UTF-8')

print(f'Recebendo arquivo {nome_arquivo}...')

# abre o arquivo
with open(nome_arquivo, 'rb') as file:
    for data in iter(lambda: file.read(4096), b""):
        conn.sendall(data)


print('Arquivo enviado', addr)

#fecha a conexão e arquivo
file.close()
conn.close()
    
