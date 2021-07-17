import turtle
from random import randint


def principal() :
    xc1 = float(input('Digite o valor da coordenada x para o canto superior esquerdo do primeiro quadrado: '))
    yc1 = float(input('Digite o valor da coordenada y para o canto superior esquerdo do primeiro quadrado: '))
    lc1 = float(input('Digite o valor da largura do primeiro quadrado: '))
    ac1 = float(input('Digite o valor da altura do primeiro quadrado: '))
    xc2 = float(input('Digite o valor da coordenada x para o canto superior esquerdo do segundo quadrado: '))
    yc2 = float(input('Digite o valor da coordenada y para o canto superior esquerdo do segundo quadrado: '))
    lc2 = float(input('Digite o valor da largura do segundo quadrado: '))
    ac2 = float(input('Digite o valor da altura do segundo quadrado: '))
    print(testaColisao(xc1, yc1, lc1, ac1, xc2, yc2, lc2, ac2))
    desenhaCaixa(xc1, yc1, lc1, ac1)
    desenhaCaixa(xc2, yc2, lc2, ac2)


def testaColisao(x1, y1, l1, a1, x2, y2, l2, a2):
    if (x2 > x1 and x1 < x2 - l2) or (x1 > x2 and x1 - l1 > x2):
        if y1 < y2 - a2 or y1 - a1 > y2:
            return 'Não Colide'
    else:
        return 'Colide'


def desenhaCaixa(xc, yc, lc, ac) :
    t = turtle.Turtle()
    t.penup()
    t.goto(xc, yc)
    t.pendown()
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    t.right(90)
    for i in range(2) :
        t.forward(ac)
        t.right(90)
        t.forward(lc)
        t.right(90)
principal()
