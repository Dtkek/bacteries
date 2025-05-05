import socket
import pygame
import math
import time
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect(("localhost", 10000))
pygame.init()
WIDTH=800
HEIGHT=600
cc=(WIDTH//2, HEIGHT//2)
old=(0,0)
radius=50
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('бактерии')
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if pygame.mouse.get_focused():
            pos=pygame.mouse.get_pos()
            vector = pos[0]-cc[0], pos[1]-cc[1]
            Lenv= math.sqrt(vector[0]**2+vector[1]**2)
            vector=vector[0]/Lenv, vector[1]/Lenv
            if Lenv<radius:
                vector=0,0
            if vector!= old:
                old=vector
                msg=f'<{vector[0]},{vector[1]}>'
                sock.send(msg.encode())


    data = sock.recv(1024).decode()
    print('получил', data)
    screen.fill('gray')
    pygame.draw.circle(screen,(255,0,0),cc,radius)
    pygame.display.update()
pygame.quit()
