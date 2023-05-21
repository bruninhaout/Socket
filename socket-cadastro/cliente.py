import socket

HOST = 'localhost'  # Endereço IP do servidor de cadastro
PORT = 8000  # Porta do servidor de cadastro

# Cria o socket do cliente
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Estabelece conexão com o servidor
s.connect((HOST, PORT))

# Envia os dados do paciente para o servidor
nome = input('Digite o nome do paciente: ')
idade = input('Digite a idade do paciente: ')
sexo = input('Digite o sexo do paciente: ')

data = f'{nome},{idade},{sexo}'
s.sendall(data.encode())

# Recebe a resposta do servidor e imprime na tela
response = s.recv(1024).decode()
print(response)

# Fecha a conexão
s.close()
