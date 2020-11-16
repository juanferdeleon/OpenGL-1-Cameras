'''

        OpenGL 1: Cameras

Juan Fernando De Leon Quezada

'''

import pygame
from pygame.locals import *

from gl import Renderer
import shaders



deltaTime = 0.0

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

r = Renderer(screen)
# Set Shaders
r.setShaders(shaders.vertex_shader, shaders.fragment_shader)
r.createObjects()


cubeX = 0
cubeZ = 0

wantsToContinue = True
while wantsToContinue:
    '''Game Loop'''

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        cubeX += 2 * deltaTime
    if keys[pygame.K_d]:
        cubeX -= 2 * deltaTime
    if keys[pygame.K_w]:
        cubeZ += 2 * deltaTime
    if keys[pygame.K_s]:
        cubeZ -= 2 * deltaTime

    # On key down
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            wantsToContinue = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode()
            elif ev.key == pygame.K_ESCAPE:
                wantsToContinue = False


    r.translateCube(cubeX, 0, cubeZ)

    # Render
    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000


pygame.quit()
