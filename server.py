import socket
import time
main_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind(("localhost", 10000))
main_socket.setblocking(False)  # Непрерывность, не ждём ответа
main_socket.listen(5)  # Прослушка входящих соединений, 5 одновременных подключений
print("Сокет создался")
players=[]
while True:
    try:
        # проверяем желающих войти в игру
        new_socket, addr = main_socket.accept()  # принимаем входящие
        new_socket.setblocking(False)
        print('Подключился', addr)
        players.append(new_socket)

    except BlockingIOError:
        pass
    for sock in players:
        try:
            data= sock.recv(1024).decode()
            print('получил', data)
        except:
            pass
    time.sleep(1)
    for sock in players:
        try:
            sock.send('lol'.encode())
        except:
            players.remove(sock)
            sock.close()
            print('сокет закрыт')

