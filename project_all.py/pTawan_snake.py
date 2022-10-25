from typing_extensions import Self
import pygame
from pygame.math import Vector2
import sys
import os
import random


class Snake:
    def __init__(self) -> None:
        self.body = [Vector2(5, 10), Vector2(6, 10)]
        self.direction = Vector2(1, 0)
        self.extendable = False

    def draw_snack(self):
        for index,block in enumerate(self.body):
            pos_x = int(block.x * cell_size)
            pos_y = int(block.y * cell_size)
            block_rect = pygame.Rect(pos_x, pos_y, cell_size, cell_size)
            if index == 0:
                pygame.draw.rect(screen, (0, 0, 0), block_rect)
            else:
                pygame.draw.rect(screen, (0, 0, 165), block_rect)

    def move_snake(self):
        if self.extendable:
            body_tail = self.body[:]
            body_tail.insert(0, body_tail[0] + self.direction)
            self.body = body_tail[:]
            self.extendable = False
        else:
            body_tail = self.body[:-1]
            body_tail.insert(0, body_tail[0] + self.direction)
            self.body = body_tail[:]

    def extend_snake(self):
        self.extendable = True

    # def reset(self):
	#     self.body = [Vector2(5, 10), Vector2(6, 10)]
    #     self.direction = Vector2(0,0)

    def reset(self):
        self.body = [Vector2(5,10), Vector2(6,10)]
        self.direction = Vector2(0,0)

class Fruit:
    def __init__(self) -> None:
        self.create_fruit()

    def draw_fruit(self):
        pos_x = int(self.pos.x * cell_size)
        pos_y = int(self.pos.y * cell_size)
        fruit_rect = pygame.Rect(pos_x, pos_y, cell_size, cell_size)
        pygame.draw.rect(screen, (200, 0, 0), fruit_rect)

    def create_fruit(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)


class Engine:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update_object(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_game_over()

    def draw_object(self):
        self.draw_grass()
        self.snake.draw_snack()
        self.fruit.draw_fruit()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.create_fruit()
            self.snake.extend_snake()

    def check_game_over(self):
        # hit the wall
        if not 0 <= self.snake.body[0].x <= cell_number or not 0 <= self.snake.body[0].y <= cell_number:
            self.game_over()

        # hit itself
        for body in self.snake.body[1:]:
            if body == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167, 210, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(
                            col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                            grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size,cell_size)
                            pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 2)
        score_surface = font.render(score_text,True,(0,0,0))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_number + 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        screen.blit(score_surface,score_rect)


pygame.init()

cell_size = 20
cell_number = 20

pygame.display.set_caption("Py Snake")
screen = pygame.display.set_mode(
    (cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()
font = pygame.font.Font(os.path.join('Font','Pixeboy-z8XGD.ttf'), 35)

engine = Engine()

SURFACE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SURFACE_UPDATE, 160)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SURFACE_UPDATE:
            engine.update_object()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if engine.snake.direction.y != 1:
                    engine.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if engine.snake.direction.y != -1:
                    engine.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if engine.snake.direction.x != -1:
                    engine.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if engine.snake.direction.x != 1:
                    engine.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_r:
                engine.snake.reset()

    screen.fill((175, 215, 70))
    engine.draw_object()
    pygame.display.update()
    clock.tick(60)
