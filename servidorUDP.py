import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket Criado com sucesso")

host = 'localhost'
porta = 5543

s.bind((host, porta))
mensagem = '\nServidor: Olá cliente.'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print("Servidor enviando mensagem")
        s.sendto(dados + (mensagem.encode()), end)