import pygame
from constants import GIF_CREATION_IMAGES, IMAGES
from os.path import join
from pygame.time import Clock

clock = Clock()

pygame.init()

WW, WH = 200, 50

RR = 5
window = pygame.display.set_mode((WW, WH))
image_name = "kda-explorer.png"
image = pygame.image.load(join(IMAGES, image_name)).convert_alpha()
IR = image.get_rect()
centerx, centery = WW / 2, WH / 2
start_x = 0
IR.centerx = centerx
IR.centery = centery
IXV = 1

pink = (255, 25, 179)
black = (0, 0, 0, 0)
white = (255, 255, 255)
frame = 0
frame_rate = int(1000 / 50)

num_images = 1
min_images = 0
max_images = 25
num_increment = 1


def events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()


running = True
window.set_alpha(0)
window.set_colorkey(black)
while running:
    events()
    window.fill(black)
    for i in range(num_images):
        window.blit(image, IR)

    pygame.display.update()
    pygame.image.save(
        window.convert_alpha(),
        join(
            GIF_CREATION_IMAGES,
            f"Frame {frame} ({50}ms) (replace).png",
        ),
    )
    num_images += num_increment
    if num_images > max_images:
        num_increment *= -1
        num_images += num_increment
    elif num_images < min_images:
        running = False
    frame += 1
    clock.tick(10)


pygame.quit()
