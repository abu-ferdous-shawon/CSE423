from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
pos_x = 0
pos_y = 0
size = 4
point_blink = False
point_blink_stop = True
time = 0
ball_coordinates = []
space = False
ball_speed = 0.8



def new_coordinates(x_axis, y_axis):
    a = x_axis - (500/2)
    b = (500/2) - y_axis
    return a,b


def keyboardListener(key, x, y):
    global space
    if key == b' ':
        space = not space
    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global ball_speed
    if key==GLUT_KEY_UP:
        ball_speed *= 2.4
        print("Speed Increased")
    if key== GLUT_KEY_DOWN:		#// up arrow key
        ball_speed /= 2.4
        print("Speed Decreased")
    glutPostRedisplay()

def mouseListener(button, state, x, y):
    global ball_coordinates,size,point_blink
    if button==GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            point_blink = not point_blink
            print(point_blink)
    if button==GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            a,b = new_coordinates(x, y)
            red_c = random.uniform(0.2, 1)
            green_c = random.uniform(0.2, 1)
            blue_c = random.uniform(0.2, 1)
            diagonal_x = random.choice([1, -1])
            diagonal_y = random.choice([1, -1])
            ball_coordinates.append([a, b,[red_c,green_c,blue_c],[diagonal_x,diagonal_y]])
            print(a,b)
    glutPostRedisplay()

def animate():
    global ball_coordinates,size, point_blink,time,point_blink_stop,ball_speed
    if not space:
        for i in ball_coordinates:
            if point_blink:
                time+=1
                if time>100:
                    point_blink_stop = not point_blink_stop
                    time = 0
            i[0] += i[3][0]*ball_speed
            i[1] += i[3][1]*ball_speed
            if i[0] > 250 :
                i[3][0] *= -1
            elif i[0] <-250:
                i[3][0] *= -1
            elif i[1] > 250:
                i[3][1] *= -1
            elif i[1] <-250:
                i[3][1] *= -1
        glutPostRedisplay()



def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250, 250, -250, 250, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    global pos_x,pos_y,size,ball_coordinates,point_blink,point_blink_stop
    for i in ball_coordinates:
        x=i[0]
        y=i[1]
        if point_blink_stop or not point_blink:
            glColor3f(i[2][0], i[2][1], i[2][2])
        else:
            glColor3f(0, 0, 0)
        glPointSize(size)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

    glutSwapBuffers()


def init():
    glClearColor(0, 0, 0, 0)  # black background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,	1,	1,	1000.0)

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()
glutDisplayFunc(display)
glutMouseFunc(mouseListener)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)

glutMainLoop()