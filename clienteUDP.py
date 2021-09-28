import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Criente socket criado com sucesso")

host = 'localhost'
porta = 5542
mensagem = 'Ola servidor!'

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5543))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("Cliente: " + dados)
finally:
    print('Cliente: Fechando a conexão')
    s.close()