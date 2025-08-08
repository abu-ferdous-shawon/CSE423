from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random



top_left_x = -50
top_left_y = -210
top_right_x = 50
top_right_y = -210
bottom_left_x = -30
bottom_left_y = -230
bottom_right_x = 30
bottom_right_y = -230
r,g,b = 1,1,1
diamond_x = random.randint(-235,235)
diamond_y = 195
red_c = random.uniform(0, 1)
green_c = random.uniform(0, 1)
blue_c = random.uniform(0, 1)
animate_y= 1
pause = False
score = 0
x_v = 10


def new_coordinates(x_axis, y_axis):
    a = x_axis - (500/2)
    b = (500/2) - y_axis
    return a,b


def zone_0(a,b):
    if abs(a) >= abs(b):
        if a>0 and b>0:
            return (a,b)
        elif a<0 and b>0:
            return "zone3"
        elif a<0 and b<0:
            return 'zone4'
        elif a>0 and b<0:
            return (a,-b)
    else:
        if a>0 and b>0:
            return "zone1"
        elif a < 0 and b > 0:
            return "zone2"
        elif a < 0 and b < 0:
            return "zone5"
        elif a > 0 and b < 0:
            return "zone6"

def zone_actual(c,d,zone):
    if zone == "zone1":
        return (d,c)
    elif zone == "zone2":
        return (-d,c)
    elif zone == "zone3":
        return (-c,d)
    elif zone == "zone4":
        return (-c,-d)
    elif zone == "zone5":
        return (-d,-c)
    elif zone == "zone6":
        return (d,-c)
    elif zone == "zone7":
        return (c,-d)
    elif zone == "zone0":
        return (c,d)


def mid_point(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0:
        while True:
            if y2 >= y1:
                return
            else:
                y1-=1
                draw_points(x1,y1)
    elif dy == 0:
        while True:
            if x2 >= x1:
                return
            else:
                x1-=1
                draw_points(x1,y1)

    zone = zone_0(dx,dy)
    if zone == "zone1":
        x1_prime = y1
        y1_prime = x1
        x2_prime = y2
        y2_prime = x2
    elif zone == "zone2":
        x1_prime = y1
        y1_prime = -x1
        x2_prime = y2
        y2_prime = -x2
    elif zone == "zone3":
        x1_prime = -x1
        y1_prime = y1
        x2_prime = -x2
        y2_prime = y2
    elif zone == "zone4":
        x1_prime = -x1
        y1_prime = -y1
        x2_prime = -x2
        y2_prime = -y2
    elif zone == "zone5":
        x1_prime = -y1
        y1_prime = -x1
        x2_prime = -y2
        y2_prime = -x2
    elif zone == "zone6":
        x1_prime = -y1
        y1_prime = x1
        x2_prime = -y2
        y2_prime = x2
    elif zone == "zone7":
        x1_prime = x1
        y1_prime = -y1
        x2_prime = x2
        y2_prime = -y2
    elif zone == "zone0":
        x1_prime = x1
        y1_prime = y1
        x2_prime = x2
        y2_prime = y2
    dx_prime = x2_prime - x1_prime
    dy_prime = y2_prime - y1_prime

    d_init = 2*dy_prime - dx_prime
    dne = 2*(dy_prime-dx_prime)
    de = 2*dy_prime

    x1,y1 = zone_actual(x1_prime,y1_prime,zone)
    x2,y2 = zone_actual(x2_prime,y2_prime,zone)
    draw_points(x1,y1)

    while True:
        if x1 == x2 and y1 == y2:
            return
        if x1_prime> x2_prime or y1_prime>y2_prime:
            if d_init > 0:
                d_init += dne
                x1_prime -= 1
                y1_prime -= 1
                x1,y1 = zone_actual(x1_prime,y1_prime,zone)
                draw_points(x1,y1)
            else:
                d_init += de
                x1_prime -= 1
                x1,y1 = zone_actual(x1_prime,y1_prime,zone)
                draw_points(x1,y1)
        else:
            if d_init > 0:
                d_init += dne
                x1_prime += 1
                y1_prime += 1
                x1,y1 = zone_actual(x1_prime,y1_prime,zone)
                draw_points(x1,y1)
            else:
                d_init += de
                x1_prime += 1
                x1,y1 = zone_actual(x1_prime,y1_prime,zone)
                draw_points(x1,y1)


def left_arrow():
    glColor3f(0.2, 0.6, 1.0)
    mid_point(-216, 245, -240,220)
    mid_point(-200, 220, -240, 220)
    mid_point(-240, 220, -216, 195)


def pause_button():
    global pause
    if pause == False:
        glColor3f(1, 1, 0.0)
        mid_point(-10, 245,-10,195)
        mid_point(10, 245, 10, 195)
    else:
        glColor3f(1, 1, 0.0)
        mid_point(-15, 245, -15, 195)
        mid_point(15, 220, -15, 245)
        mid_point(15, 220 , -15, 195)



def exit():
    glColor3f(1, 0.0, 0.0)
    mid_point(210,245,240,195)
    mid_point(240, 245, 210, 195)


def box():
    global top_left_x, top_right_x, bottom_left_x, bottom_right_x, top_left_y, top_right_y, bottom_left_y, bottom_right_y,r,g,b
    glColor3f(r,g,b)
    mid_point(top_right_x, top_right_y, top_left_x, top_left_y)
    mid_point(top_right_x, top_right_y, bottom_right_x, bottom_right_y)
    mid_point( bottom_left_x, bottom_left_y,top_left_x, top_left_y)
    mid_point( bottom_right_x, bottom_right_y, bottom_left_x, bottom_left_y)


def diamond():
    global diamond_x, diamond_y,red_c,green_c,blue_c
    glColor3f(red_c, green_c, blue_c)
    mid_point(diamond_x+15, diamond_y-20, diamond_x, diamond_y)
    mid_point(diamond_x, diamond_y, diamond_x - 15, diamond_y - 20)
    mid_point(diamond_x-15, diamond_y-20, diamond_x, diamond_y - 40)
    mid_point(diamond_x + 15, diamond_y - 20, diamond_x, diamond_y - 40)


def animate():
    global diamond_y,animate_y,diamond_x,red_c,green_c,blue_c, r, g, b,top_left_y,top_left_x,top_right_x,top_right_y,bottom_left_y,bottom_right_y,score,over,pause,x_v
    if pause == False:
        r, g, b = 1, 1, 1
        diamond_y -= animate_y
        if( (top_left_x <= (diamond_x) <= top_right_x) or (top_left_x <= (diamond_x-15) <= top_right_x) or (top_left_x <= (diamond_x+15) <= top_right_x) ) and (bottom_left_y<(diamond_y-40) < top_left_y):
            score += 1
            animate_y += 0.25
            print("score:", score)
            diamond_x = random.randint(-235, 235)
            diamond_y = 195
            red_c = random.uniform(0, 1)
            green_c = random.uniform(0, 1)
            blue_c = random.uniform(0, 1)

        elif diamond_y <= -250:
            pause= True
            animate_y =0
            x_v = 10
            r, g, b = 1, 0, 0
            print(f"Game over! score:{score}")
            score = 0

    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global top_left_x, top_left_y, top_right_x, top_right_y, bottom_left_x, bottom_left_y, bottom_right_x,bottom_right_y,pause,x_v
    if pause == False:
        if key == GLUT_KEY_RIGHT:
            if (top_right_x + x_v) <=240:
                top_left_x += x_v
                top_right_x += x_v
                bottom_left_x += x_v
                bottom_right_x += x_v
        if key == GLUT_KEY_LEFT:
            if (top_left_x + x_v) >= -230:
                top_left_x -= x_v
                top_right_x -= x_v
                bottom_left_x -= x_v
                bottom_right_x -= x_v

def mouseListener(button, state, x, y):
    global diamond_x,diamond_y,red_c,green_c,blue_c,pause,score,animate_y,x_v
    if button==GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            a, b = new_coordinates(x, y)
            if -240<=a<=-200 and 195<= b <= 245:
                pause = False
                print("StartOver!")
                score = 0
                animate_y = 1
                x_v = 10
                diamond_x = random.randint(-235, 235)
                diamond_y = 195
                red_c = random.uniform(0, 1)
                green_c = random.uniform(0, 1)
                blue_c = random.uniform(0, 1)
            elif -10<=a<=10 and 195<= b <= 245:
                pause = not pause
            elif 210<=a<=240 and 195<= b <= 245:
                print("Exit")
                score = 0
                animate_y = 1
                x_v = 10
                glutLeaveMainLoop()




def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    return


def init():
    glClearColor(0, 0, 0, 0)  # black background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,	1,	1,	1000.0)


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
    left_arrow()
    pause_button()
    exit()
    box()
    diamond()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"ASSIGNMENT2")
init()
glutDisplayFunc(display)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()