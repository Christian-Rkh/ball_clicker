import pygame
import sys
import random

# 초기 설정
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("공 잡기 게임")
clock = pygame.time.Clock()

# 색상 설정
WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 30
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)

ball_speed_x = 3
ball_speed_y = 3

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 닫기 이벤트
            running = False

    screen.fill(WHITE)  # 배경 색상을 흰색으로 설정

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        ball_speed_y = -ball_speed_y

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.flip()  # 화면 업데이트
    clock.tick(60)# 초당 프임 수

pygame.quit()
sys.exit()