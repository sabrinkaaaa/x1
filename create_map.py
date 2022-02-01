import os

import pygame
import requests

pygame.init()


def map_create():
    api_server = "http://static-maps.yandex.ru/1.x/"

    lon = a
    lat = b
    delta = c

    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    response = requests.get(api_server, params=params)
    file = open("1.png", 'wb')
    for i in response:
        file.write(i)


a = ''
b = ''
c = ''
flag = 'a'
run = True
map = False
while run:
    screen = pygame.display.set_mode((600, 450))
    if map:
        screen.blit(pygame.image.load('1.png'), (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.unicode in '0987654321.':
                if flag == 'a':
                    a += event.unicode
                elif flag == 'b':
                    b += event.unicode
                else:
                    c += event.unicode
            if event.unicode == ' ':
                if flag == 'a':
                    flag = 'b'
                elif flag == 'b':
                    flag = 'c'
                else:
                    print(12121)
                    map_create()
                    map = True
                    flag = 'a'
    pygame.display.flip()

