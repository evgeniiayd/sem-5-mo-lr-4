import pygame
import sys

# Инициализация Pygame
pygame.init()

# Параметры окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Размеры персонажа и объектов
PLAYER_SIZE = 50
PLAYER_BORDER_THICKNESS = 2
OBJECT_SIZE = 50
WALL_THICKNESS = 5

# Скорость движения персонажа
PLAYER_SPEED = 5

# Инициализация окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Базовая заготовка 2D-игры")
clock = pygame.time.Clock()

# Переменные персонажа
player_pos = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
player_velocity = [0, 0]  # Скорость по X и Y

# Неподвижные объекты
objects = [
    pygame.Rect(200, 150, OBJECT_SIZE, OBJECT_SIZE),
    pygame.Rect(400, 300, OBJECT_SIZE, OBJECT_SIZE),
    pygame.Rect(600, 450, OBJECT_SIZE, OBJECT_SIZE)
]

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_velocity[0] = -PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                player_velocity[0] = PLAYER_SPEED
            elif event.key == pygame.K_UP:
                player_velocity[1] = -PLAYER_SPEED
            elif event.key == pygame.K_DOWN:
                player_velocity[1] = PLAYER_SPEED
        elif event.type == pygame.KEYUP:
            if event.key in {pygame.K_LEFT, pygame.K_RIGHT}:
                player_velocity[0] = 0
            elif event.key in {pygame.K_UP, pygame.K_DOWN}:
                player_velocity[1] = 0

    # Обновление позиции персонажа
    player_pos[0] += player_velocity[0]
    player_pos[1] += player_velocity[1]

    # Ограничение движения персонажа внутри игрового окна с учётом стен
    player_pos[0] = max(WALL_THICKNESS, min(player_pos[0], WINDOW_WIDTH - PLAYER_SIZE - WALL_THICKNESS))
    player_pos[1] = max(WALL_THICKNESS, min(player_pos[1], WINDOW_HEIGHT - PLAYER_SIZE - WALL_THICKNESS))

    # Рендеринг объектов
    screen.fill(WHITE)

    # Отрисовка стен
    pygame.draw.rect(screen, BLACK, (0, 0, WINDOW_WIDTH, WALL_THICKNESS))  # Верхняя стена
    pygame.draw.rect(screen, BLACK, (0, 0, WALL_THICKNESS, WINDOW_HEIGHT))  # Левая стена
    pygame.draw.rect(screen, BLACK, (0, WINDOW_HEIGHT - WALL_THICKNESS, WINDOW_WIDTH, WALL_THICKNESS))  # Нижняя стена
    pygame.draw.rect(screen, BLACK, (WINDOW_WIDTH - WALL_THICKNESS, 0, WALL_THICKNESS, WINDOW_HEIGHT))  # Правая стена

    # Отрисовка персонажа с перекрестием
    pygame.draw.rect(screen, BLUE, (*player_pos, PLAYER_SIZE, PLAYER_SIZE), PLAYER_BORDER_THICKNESS)  # Рамка
    pygame.draw.line(screen, BLUE,
                     (player_pos[0], player_pos[1]),
                     (player_pos[0] + PLAYER_SIZE, player_pos[1] + PLAYER_SIZE),
                     2)  # Диагональная линия

    pygame.draw.line(screen, BLUE,
                     (player_pos[0] + PLAYER_SIZE, player_pos[1]),
                     (player_pos[0], player_pos[1] + PLAYER_SIZE),
                     2)  # Обратная диагональ

    # Отрисовка неподвижных объектов
    for obj in objects:
        pygame.draw.rect(screen, RED, obj)

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

