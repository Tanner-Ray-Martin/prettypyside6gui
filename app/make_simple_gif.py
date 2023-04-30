import pygame
from constants import GIF_CREATION_IMAGES
from os.path import join

pygame.init()

WW, WH = 500, 500
RR = 100
window = pygame.display.set_mode((WW, WH))

pink = (255, 25, 179)
black = (0, 0, 0)
white = (255, 255, 255)
import time


def draw_rect(r_type=None):
    if r_type == "round":
        pygame.draw.rect(
            window,
            black,
            pygame.Rect(0, 0, WW, WH),
            border_bottom_left_radius=RR,
            border_bottom_right_radius=RR,
            border_top_left_radius=RR,
            border_top_right_radius=RR,
        )
    else:
        pygame.draw.rect(window, black, pygame.Rect(0, 0, WW, WH))


def events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


class Animation:
    def __init__(self, color, x, y, x_v, y_v):
        self.color = color
        self.radius = 20
        self.x = x
        self.y = y
        self.w = self.radius * 2
        self.h = self.radius * 2
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.y_velocity = y_v
        self.x_velocity = x_v

    def move(self):
        self.rect.centerx += self.x_velocity
        self.rect.centery += self.y_velocity
        if self.rect.right > WW:
            self.rect.right = WW
            self.x_velocity = 0
            self.y_velocity = speed
        elif self.rect.bottom > WH:
            self.rect.bottom = WH
            self.x_velocity = speed * -1
            self.y_velocity = 0
        elif self.rect.left < 0:
            self.rect.left = 0
            self.y_velocity = speed * -1
            self.x_velocity = 0
        elif self.rect.top < 0:
            self.rect.top = 0
            self.x_velocity = 5
            self.y_velocity = 0

    def draw(self):
        pygame.draw.circle(window, self.color, self.rect.center, self.radius)


running = True
num_animations = 150
num_per_side = int(num_animations / 4)
x_diff = int(WW / num_per_side)
y_diff = int(WH / num_per_side)
start_x = 0
start_y = 0
color = black
animations = []
direction = "right"
speed = 1
x_v, y_v = speed, 0
frame = 0
max_frames = 200
for i in range(4):
    for num in range(num_per_side):
        if color == black:
            color = pink
        else:
            color = black
        animations.append(Animation(color, start_x, start_y, x_v, y_v))
        if direction == "right":
            start_x += x_diff
        elif direction == "down":
            start_y += y_diff
        elif direction == "left":
            start_x -= x_diff
        elif direction == "up":
            start_y -= y_diff
    if direction == "right":
        direction = "down"
        x_v = 0
        y_v = speed
    elif direction == "down":
        direction = "left"
        x_v = speed * -1
        y_v = 0
    elif direction == "left":
        direction = "up"
        x_v = 0
        y_v = speed * -1


window.fill(white)
draw_rect()
while running:
    for animation in animations:
        animation.move()
        animation.draw()
    pygame.display.update()
    running = events()
    pygame.image.save(window, join(GIF_CREATION_IMAGES, f"{frame}.png"))
    frame += 1
    if frame > max_frames:
        running = False
    time.sleep(0.02)

pygame.quit()
