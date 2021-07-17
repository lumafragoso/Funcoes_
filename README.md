# Funcoes_
Assessment activity of the 1º period of IT Bachelor on Functions in Python / Atividade avaliativa do 1º periodo do Bacharelado em TI sobre Funções em Python

## Caixas Envoltórias

### Goal / Objetivo
In the Envoltoria Box problem, we saw how it is possible to identify the collision between a box and a point, however, in practice the problem always involves two boxes.
Boxes collide when any point (any of the 4) in one box meets inside the other box.
Thus, write a function testColisao, which receives 8 parameters: xc1,yc1,lc1,ac1 and xc2,yc2,lc2,ac2 representing the upper left corner of each box with its respective width and height. When box 1 collides with box 2 the function must print "Collide", otherwise "Does not collide".
Also write a function to draw the boxes, the function should take only 4 parameters: xc,yc,lc,ac and should draw a box with a random color (use turtle.color(randint(0,255), randint(0,255), randint (0.255))).
Your program should ask the user for the coordinates of each box, draw them and test the collision using the functions you have made.

No problema Caixa Envoltoria, vimos como é possível identificar a colisão entre uma caixa e um ponto, porém, na prática o problema sempre envolve duas caixas.
As caixas se colidem quando algum ponto (qualquer um dos 4) de uma caixa se encontrar dentro da outra caixa.
Assim, escreva uma função testaColisao, que recebe 8 parâmetros: xc1,yc1,lc1,ac1 e xc2,yc2,lc2,ac2 representando o canto superior esquerdo de cada caixa com sua respectiva largura e altura. Quando a caixa 1 colide com a caixa 2 a função deve imprimir "Colide", caso contrário "Não colide".
Escreva também uma função para desenhar as caixas, a função deve receber apenas 4 parâmetros: xc,yc,lc,ac e deve desenhar uma caixa com uma cor aleatória (use turtle.color(randint(0,255), randint(0,255), randint(0,255))).
Seu programa deve pedir ao usuário as coordenadas de cada caixa, desenhá-las e testar a colisão usando as funções feitas.
