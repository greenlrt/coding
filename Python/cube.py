import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

verticies= (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    pygame.init()
    width = 800
    height = 600
    display = (width, height)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    drag = False
    dX = 0
    dy = 0
    THETA = 0
    PHI = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5, 0, 0)

                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drag = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drag = True
                    old_x, old_y = pygame.mouse.get_pos()
                if event.button == 4:
                    glTranslate(0, 0, 1.0)
                
                if event.button == 5:
                    glTranslate(0, 0, -1.0)

            if event.type == pygame.MOUSEMOTION:
                if drag:
                    #print(pygame.mouse.get_pos())
                    x, y = pygame.mouse.get_pos()
                    dX = (x - old_x) * 2 * math.pi / width
                    dY = (y - old_y) * 2 * math.pi / height
                    THETA += dX
                    PHI += dY
                    old_x = x
                    old_y = y
                    glRotatef(THETA, 0, 1, 0)
                    glRotatef(PHI, 1, 0, 0)

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
