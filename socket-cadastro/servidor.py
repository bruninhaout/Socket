import socket

HOST = ''  # Endereço IP do servidor
PORT = 8000  # Porta do servidor

# Cria o socket do servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o bind do socket com o endereço e porta definidos
s.bind((HOST, PORT))

# Define o número máximo de conexões simultâneas
s.listen(5)

print(f'Servidor de cadastro de pacientes iniciado em {HOST}:{PORT}')

while True:
    # Espera por uma nova conexão
    conn, addr = s.accept()
    print(f'Conexão estabelecida com {addr}')

    # Recebe os dados enviados pelo cliente
    data = conn.recv(1024).decode()

    # Processa os dados recebidos (aqui, apenas imprimimos na tela)
    print(f'Dados recebidos: {data}')

    # Fecha a conexão
    conn.close()
    
