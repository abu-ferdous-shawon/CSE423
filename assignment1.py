from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random
rain_drops_points = []
number_of_rains = 700
move_x = 0.0
animate_x = 0.0
animate_y = 10.0
bg_change = 0.0
for i in range(number_of_rains):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    rain_drops_points.append([x, y])

def make_rains():
    global raindrops,move_x
    for i in rain_drops_points:
        x = i[0]
        y = i[1]
        glBegin(GL_LINES)
        colour = random.choice([0.75,0.2])
        if colour == 0.75:
            glColor3f(0.75, 0.75, 0.75)
        else:
            glColor3f(0.2, 0.6, 1.0)
        glVertex2f(x,y)
        glVertex2f(x+move_x,y-20)
        glEnd()

def myhouse():
    #background
    glColor3f(1.0, 0.8, 0.6)
    glBegin(GL_TRIANGLES)
    glVertex2d(0, 0)
    glVertex2d(500, 0)
    glVertex2d(500, 310)

    glVertex2d(0, 0)
    glVertex2d(500, 310)
    glVertex2d(0, 310)
    glEnd()

    #grass
    glColor3f(0.2, 1.0, 0.6)
    x=0
    y= 240
    for i in range(13):
        glBegin(GL_TRIANGLES)
        glVertex2d(x, y)
        glVertex2d(x+40, y)
        glVertex2d(x+20, y+50)
        x=x+40
        glEnd()

    #roof
    glColor3f(1.0, 0.4, 0.4)
    glBegin(GL_TRIANGLES)
    glVertex2d(150, 250)
    glVertex2d(250, 325)
    glVertex2d(350, 250)
    glEnd()

    #body
    glColor3f(1.0, 0.8, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(170, 160)
    glVertex2d(330, 160)
    glVertex2d(330, 250)

    glVertex2d(170, 160)
    glVertex2d(330, 250)
    glVertex2d(170, 250)
    glEnd()


    #door
    glColor3f(0.0, 0.6, 0.6)
    glBegin(GL_TRIANGLES)
    glVertex2d(230, 160)
    glVertex2d(270, 160)
    glVertex2d(270, 220)

    glVertex2d(230, 160)
    glVertex2d(270, 220)
    glVertex2d(230, 220)
    glEnd()

    #door point
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(260,190)
    glEnd()

    #windows
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(185, 190)
    glVertex2d(215, 190)
    glVertex2d(215, 220)

    glVertex2d(185, 190)
    glVertex2d(215, 220)
    glVertex2d(185, 220)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(200,220)
    glVertex2f(200,190)

    glVertex2f(185,205)
    glVertex2f(215,205)
    glEnd()

    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(285, 190)
    glVertex2d(315, 190)
    glVertex2d(315, 220)

    glVertex2d(285, 190)
    glVertex2d(315, 220)
    glVertex2d(285, 220)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(300,220)
    glVertex2f(300,190)

    glVertex2f(285,205)
    glVertex2f(315,205)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def specialKeyListener(key, x, y):
    global rain_drops_points,move_x,animate_x,animate_y
    if key == GLUT_KEY_RIGHT:
        move_x+=2
        animate_x+=0.8
        animate_y-=0.8
        print(animate_x,animate_y, move_x)
        print("rightward")

    if key == GLUT_KEY_LEFT:
        move_x -= 2
        animate_y+=0.8
        animate_x-=0.8
        print(animate_x,animate_y, move_x)
        print("leftward")



def animate():
    global rain_drops_points,move_x,animate_x,animate_y
    for rain in rain_drops_points:
        rain[1] -=animate_y
        rain[0] += animate_x
        if rain[1]<0 or rain[1]>500:
            rain[0]= random.randint(0,500)
            rain[1]= random.randint(0,500)
    glutPostRedisplay()


def keyboardListener(key, x, y):
    global bg_change
    if key == b'w':
        bg_change+=0.25
        glClearColor(bg_change, bg_change, bg_change, bg_change)
        print('Its going to be morning')
    if key == b's':
        bg_change -= 0.25
        glClearColor(bg_change, bg_change, bg_change, bg_change)
        print('Its going to be night')

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    myhouse()
    make_rains()
    glutSwapBuffers()


def init():
    glClearColor(0, 0, 0, 0)  # black background



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task1")
init()
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMainLoop()