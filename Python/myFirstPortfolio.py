import pygame
import random

# pygame 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("벽돌깨기 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# 게임 객체 설정
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
BALL_SIZE = 10
BRICK_WIDTH = 80
BRICK_HEIGHT = 30
BRICK_ROWS = 5
BRICK_COLS = 10

# 패들 설정
paddle_x = SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = SCREEN_HEIGHT - 50
paddle_speed = 7

# 공 설정
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT - 100
ball_dx = 5
ball_dy = -5

# 벽돌 생성
bricks = []
brick_colors = [RED, ORANGE, YELLOW, GREEN, BLUE]

for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick_x = col * (BRICK_WIDTH + 2) + 1
        brick_y = row * (BRICK_HEIGHT + 2) + 50
        bricks.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))

# 게임 상태
score = 0
lives = 3
game_over = False
game_won = False

# 폰트 설정
font = pygame.font.Font(None, 36)

def draw_objects():
    # 패들 그리기
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    
    # 공 그리기
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_SIZE)
    
    # 벽돌 그리기
    for i, brick in enumerate(bricks):
        color_index = i // BRICK_COLS
        pygame.draw.rect(screen, brick_colors[color_index], brick)
        pygame.draw.rect(screen, BLACK, brick, 2)

def update_ball():
    global ball_x, ball_y, ball_dx, ball_dy, lives, game_over
    
    # 공 이동
    ball_x += ball_dx
    ball_y += ball_dy
    
    # 벽 충돌 체크
    if ball_x <= BALL_SIZE or ball_x >= SCREEN_WIDTH - BALL_SIZE:
        ball_dx *= -1
    if ball_y <= BALL_SIZE:
        ball_dy *= -1
    
    # 바닥에 떨어졌을 때
    if ball_y >= SCREEN_HEIGHT:
        lives -= 1
        if lives <= 0:
            game_over = True
        else:
            # 공 리셋
            ball_x = SCREEN_WIDTH // 2
            ball_y = SCREEN_HEIGHT - 100
            ball_dx = 5
            ball_dy = -5

def check_collisions():
    global ball_dx, ball_dy, score
    
    # 패들 충돌 체크
    paddle_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    if paddle_rect.collidepoint(ball_x, ball_y + BALL_SIZE):
        ball_dy *= -1
        # 패들 위치에 따른 공 방향 조정
        relative_x = (ball_x - paddle_x) / PADDLE_WIDTH
        ball_dx = (relative_x - 0.5) * 10
    
    # 벽돌 충돌 체크
    for brick in bricks[:]:
        if brick.collidepoint(ball_x, ball_y):
            bricks.remove(brick)
            ball_dy *= -1
            score += 10
            break

def draw_ui():
    # 점수 표시
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # 생명 표시
    lives_text = font.render(f"Health: {lives}", True, WHITE)
    screen.blit(lives_text, (10, 40))

def draw_game_over():
    if game_over:
        game_over_text = font.render("Game Over", True, RED)
        screen.blit(game_over_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2))
    elif game_won:
        win_text = font.render("You Win", True, GREEN)
        screen.blit(win_text, (SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2))

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and (game_over or game_won):
                # 게임 재시작
                bricks.clear()
                for row in range(BRICK_ROWS):
                    for col in range(BRICK_COLS):
                        brick_x = col * (BRICK_WIDTH + 2) + 1
                        brick_y = row * (BRICK_HEIGHT + 2) + 50
                        bricks.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))
                score = 0
                lives = 3
                game_over = False
                game_won = False
                ball_x = SCREEN_WIDTH // 2
                ball_y = SCREEN_HEIGHT - 100
                ball_dx = 5
                ball_dy = -5
    
    if not game_over and not game_won:
        # 패들 이동
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < SCREEN_WIDTH - PADDLE_WIDTH:
            paddle_x += paddle_speed
        
        # 공 업데이트
        update_ball()
        check_collisions()
        
        # 승리 조건 체크
        if len(bricks) == 0:
            game_won = True
    
    # 화면 그리기
    screen.fill(BLACK)
    draw_objects()
    draw_ui()
    draw_game_over()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit() 