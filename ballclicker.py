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
BLUE = (0, 0, 255)

ball_radius = 30
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)

ball_speed_x = 3
ball_speed_y = 3
score = 0
time_limit = 30
start_ticks = pygame.time.get_ticks()

font = pygame.font.Font(None, 36)
# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 닫기 이벤트
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            distance = ((mouse_x - ball_x) ** 2 + (mouse_y - ball_y) ** 2) ** 0.5
            if distance < ball_radius:
                score += 1
                ball_x = random.randint(ball_radius, WIDTH - ball_radius)
                ball_y = random.randint(ball_radius, HEIGHT - ball_radius)
                ball_speed_x = random.choice([2, 6]) * 0.5
                ball_speed_y += random.choice([2, 6])
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    if elapsed_time > time_limit:
        running = False

    screen.fill(WHITE)  # 배경 색상을 흰색으로 설정

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        ball_speed_y = -ball_speed_y

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    time_text = font.render(f"Time: {max(0, int(time_limit - elapsed_time))}", True, BLUE)
    screen.blit(time_text, (WIDTH - 150, 10))

    pygame.display.flip()  # 화면 업데이트
    clock.tick(60)# 초당 프임 수
game_over = True
while game_over:
    screen.fill(WHITE)  # 화면을 흰색으로 초기화
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Game Over!", True, (0, 0, 0))
    final_score_text = font.render(f"Your Score: {score}", True, (0, 0, 0))
    screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
    screen.blit(final_score_text, (WIDTH // 2 - 200, HEIGHT // 2 + 20))

    pygame.display.flip()  # 화면 업데이트

    for event in pygame.event.get():  # 종료 화면에서 이벤트 처리
        if event.type == pygame.QUIT:  # 창 닫기 버튼 클릭 시
            game_over = False

pygame.quit()  # pygame 종료
sys.exit()  # 시스템 종료

pygame.quit()
sys.exit()