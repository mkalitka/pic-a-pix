import sys
import pygame

n = 40
m = 30

scale = 18

Width = 1080
Height = 720

BWdh = n*20+8
BHgt = m*20+7

X = Width/2-20*n/2
Y = Height/2-20*m/2

MoveX = (n-2)*2
MoveY = (m-2)*2

NNY = n // 2 + n % 2 + 1
NNX = m // 2 + m % 2 + 1

if NNY > 6:
    HorizontalTable = X + MoveX - 25 - 10 // 2 * 20 + 20 * ((n + 1) % 2)
else:
    HorizontalTable = X + MoveX - 25 - n // 2 * 20 + 20 * ((n + 1) % 2)
if NNX > 6:
    VerticalTable = Y + MoveY - 30 - 10 // 2 * 20 + 20 * ((m + 1) % 2)
else:
    VerticalTable = Y + MoveY - 30 - m // 2 * 20 + 20 * ((m + 1) % 2)


pygame.init()
screen = pygame.display.set_mode((Width, Height))
T = pygame.font.SysFont('A', 35)
text = T.render('X', True, (244, 174, 63))
arrowU = T.render('^', True, (244, 174, 63))
arrowD = T.render('v', True, (244, 174, 63))
arrowR = T.render('>', True, (244, 174, 63))
arrowL = T.render('<', True, (244, 174, 63))


pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(X+MoveX-5, Y+MoveY-5, BWdh, BHgt))
pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(HorizontalTable, Y+MoveY-5, 5, BHgt))
pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(X+MoveX-5, VerticalTable, BWdh, 5))

for i in range(0, n+1):
    if i == 0:
        pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(X + MoveX - 5 + i * 20, VerticalTable, 5, BHgt))
        screen.blit(arrowU, (X+MoveX-20, Y+MoveY-50))
        screen.blit(arrowD, (X+MoveX-20, Y+MoveY-40))
    if i == n:
        pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(X + MoveX - 2 + i * 20, VerticalTable, 5, BHgt))
    if i < n:
        for j in range(1, NNX):
            if j <= 5:
                screen.blit(text, (i * 20 + X + MoveX + 1, -j * 20 + Y+MoveY - 6, 18, 18))
    pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(X + MoveX - 2 + i * 20, VerticalTable, 2, BHgt))

for i in range(0, m+1):
    if i == 0:
        pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(HorizontalTable, Y + MoveY - 5 + i * 20, BWdh - 5, 5))
        screen.blit(arrowL, (X+MoveX-50, Y+MoveY-27))
        screen.blit(arrowR, (X+MoveX-35, Y+MoveY-27))
    if i == m:
        pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(HorizontalTable, Y + MoveY - 3 + i * 20, BWdh - 5, 5))
    if i < m:
        for j in range(1, NNY):
            if j <= 5:
                screen.blit(text, (-j * 20 + X + MoveX - 1, i * 20 + Y + MoveY - 2, 18, 18))
    pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(HorizontalTable, Y + MoveY - 2 + i * 20, BWdh, 2))

for i in range(0, n):
    for j in range(0, m):
        pygame.draw.rect(screen, (240, 230, 215), pygame.Rect(i * 20 + X + MoveX, j * 20 + Y+MoveY, scale, scale))

Check = [[2]*m for i in range(n)]

while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(0, n):
                for j in range(0, m):
                    if i * 20 + X + MoveX <= mouse[0] <= i * 20 + X + MoveX + 18 and j * 20 + Y+MoveY <= mouse[1] <= j * 20 + Y+MoveY+18:
                        Check[i][j] = Check[i][j]+1
                        if Check[i][j] > 2:
                            Check[i][j] = 0
                        if Check[i][j] == 0:
                            pygame.draw.rect(screen, (240, 230, 215), pygame.Rect(i * 20 + X + MoveX, j * 20 + Y+MoveY, scale, scale))
                            screen.blit(text, (i * 20 + X + MoveX + 1, j * 20 + Y+MoveY - 2, scale, scale))
                            break
                        elif Check[i][j] == 1:
                            pygame.draw.rect(screen, (33, 48, 88), pygame.Rect(i * 20 + X + MoveX, j * 20 + Y+MoveY, scale, scale))
                            break
                        elif Check[i][j] == 2:
                            pygame.draw.rect(screen, (240, 230, 215), pygame.Rect(i * 20 + X + MoveX, j * 20 + Y+MoveY, scale, scale))
                            break

            if X+MoveX-15 <= mouse[0] <= X+MoveX-10 and Y+MoveY-50 <= mouse[1] <= Y+MoveY-35:
                print("X")
            elif X+MoveX-15 <= mouse[0] <= X+MoveX-10 and Y+MoveY-35 <= mouse[1] <= Y+MoveY-20:
                print("Y")
            elif X+MoveX-50 <= mouse[0] <= X+MoveX-35 and Y+MoveY-27 <= mouse[1] <= Y+MoveY-12:
                print("A")
            elif X+MoveX-35 <= mouse[0] <= X+MoveX-20 and Y+MoveY-27 <= mouse[1] <= Y+MoveY-12:
                print("B")
        if event.type == pygame.QUIT:
            sys.exit(0)
    pygame.display.flip()
