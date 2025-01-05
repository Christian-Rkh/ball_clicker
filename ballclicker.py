import pygame
import sys

# 초기 설정
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("공 잡기 게임")

# 색상 설정
WHITE = (255, 255, 255)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 닫기 이벤트
            running = False

    screen.fill(WHITE)  # 배경 색상을 흰색으로 설정
    pygame.display.flip()  # 화면 업데이트

pygame.quit()
sys.exit()