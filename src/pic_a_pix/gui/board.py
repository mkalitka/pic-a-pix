import sys
import pygame

def create_board(n, m, left_num, up_num):

    list_len_left = [len(i) for i in left_num]
    longest_left = max(list_len_left)
    print(longest_left)

    list_len_up = [len(i) for i in up_num]
    longest_up = max(list_len_up)
    print(longest_up)

    scale = 18

    Width = 1480
    Height = 820

    BWdh = n*20+8
    BHgt = m*20+7

    X = Width/2-20*n/2
    Y = Height/2-20*m/2

    MoveX = (n-2)*2
    MoveY = (m-2)*2

    NNY = longest_left+1
    NNX = longest_up+1

    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

    HorizontalTable = X + MoveX - 25 - (longest_left) * 20 + 20 * ((n + 1) % 2)
    VerticalTable = Y + MoveY - 30 - (longest_up) * 20 + 20 * ((m + 1) % 2)


    pygame.init()
    screen = pygame.display.set_mode((Width, Height))
    T = pygame.font.SysFont('A', 30)
    iks = pygame.font.SysFont('A', 35)
    block_x = iks.render('X', True, (244, 174, 63))


    pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(X+MoveX-5, Y+MoveY-5, BWdh, BHgt))
    pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(HorizontalTable, Y+MoveY-5, 5, BHgt))
    pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(X+MoveX-5, VerticalTable, BWdh, 5))

    for i in range(0, n+1):
        if i == 0:
            pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(X + MoveX - 5 + i * 20, VerticalTable, 5, BHgt))
        if i == n:
            pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(X + MoveX - 2 + i * 20, VerticalTable, 5, BHgt))
        if i < n:
            for j in range(1, NNX):
                if(j-1 < len(up_num[i])):
                    if( up_num[i][j - 1] // 10 > 0):
                        T = pygame.font.SysFont('A', 22)
                    else:
                        T = pygame.font.SysFont('A', 28)
                    text = T.render(str(up_num[i][j - 1]), True, (244, 174, 63))
                    screen.blit(text, (i * 20 + X + MoveX + 1, -j * 20 + Y+MoveY - 6, 18, 18))
        pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(X + MoveX - 2 + i * 20, VerticalTable, 2, BHgt))

    for i in range(0, m+1):
        if i == 0:
            pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(HorizontalTable, Y + MoveY - 5 + i * 20, BWdh - 5, 5))
        if i == m:
            pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(HorizontalTable, Y + MoveY - 3 + i * 20, BWdh - 5, 5))
        if i < m:
            for j in range(1, NNY):
                if j-1 < len(left_num[i]):
                    if left_num[i][j - 1] // 10 > 0:
                        T = pygame.font.SysFont('A', 22)
                    else:
                        T = pygame.font.SysFont('A', 28)
                    text = T.render(str(left_num[i][j-1]), True, (244, 174, 63))
                    screen.blit(text, (-j * 20 + X + MoveX - 1, i * 20 + Y + MoveY - 2, 18, 18))
        pygame.draw.rect(screen, (40, 105, 106), pygame.Rect(HorizontalTable, Y + MoveY - 2 + i * 20, BWdh, 2))

    for i in range(0, n):
        for j in range(0, m):
            pygame.draw.rect(screen, (240, 230, 215), pygame.Rect(i * 20 + X + MoveX, j * 20 + Y+MoveY, scale, scale))

    check = [[2]*m for i in range(n)]

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                for i in range(n):
                    for j in range(m):
                        if i * 20 + X + MoveX <= mouse[0] <= i * 20 + X + MoveX + 18 and j * 20 + Y + MoveY <= mouse[1] <= j * 20 + Y + MoveY + 18:

                            if event.button == LEFT and check[i][j] == 1:
                                check[i][j] = 2
                                pygame.draw.rect(screen, (240, 230, 215),
                                                 pygame.Rect(i * 20 + X + MoveX, j * 20 + Y + MoveY, scale, scale))
                                break
                            elif event.button == RIGHT and check[i][j] == 0:
                                check[i][j] = 2
                                pygame.draw.rect(screen, (240, 230, 215),
                                                 pygame.Rect(i * 20 + X + MoveX, j * 20 + Y + MoveY, scale, scale))
                                break

                            if event.button == RIGHT:
                                check[i][j] = 0
                                pygame.draw.rect(screen, (240, 230, 215),
                                                 pygame.Rect(i * 20 + X + MoveX, j * 20 + Y + MoveY, scale, scale))
                                screen.blit(block_x, (i * 20 + X + MoveX + 1, j * 20 + Y + MoveY - 2, scale, scale))
                            if event.button == LEFT:
                                check[i][j] = 1
                                pygame.draw.rect(screen, (33, 48, 88),
                                                 pygame.Rect(i * 20 + X + MoveX, j * 20 + Y + MoveY, scale, scale))

            if event.type == pygame.QUIT:
                sys.exit(0)
        pygame.display.flip()

# left_num=[[1], [12], [1, 1], [1, 1], [1], [2, 1], [1], [1, 1], [1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [3, 1], [1, 1], [1, 1], [2, 1], [4]]
# up_num=[[2], [1, 2], [1, 2, 1], [10, 1, 10], [1, 3], [1, 1, 1], [1, 1, 3, 1], [1, 1], [6, 6], [1]]
#
# create_board(10, 20, left_num, up_num)