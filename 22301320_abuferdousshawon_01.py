# #TASK1
#
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import random
#
#
# rain_drops_points = []
# number_of_rains = 700
# move_x = 0.0
# animate_x = 0.0
# animate_y = 10.0
# bg_change = 0.0
# for i in range(number_of_rains):
#     x = random.randint(0, 500)
#     y = random.randint(0, 500)
#     rain_drops_points.append([x, y])
#
# def make_rains():
#     global raindrops,move_x
#     for i in rain_drops_points:
#         x = i[0]
#         y = i[1]
#         glBegin(GL_LINES)
#         colour = random.choice([0.75,0.2])
#         if colour == 0.75:
#             glColor3f(0.75, 0.75, 0.75)
#         else:
#             glColor3f(0.2, 0.6, 1.0)
#         glVertex2f(x,y)
#         glVertex2f(x+move_x,y-20)
#         glEnd()
#
# def myhouse():
#
#     glColor3f(1.0, 0.8, 0.6)
#     glBegin(GL_TRIANGLES)
#     glVertex2d(0, 0)
#     glVertex2d(500, 0)
#     glVertex2d(500, 310)
#
#     glVertex2d(0, 0)
#     glVertex2d(500, 310)
#     glVertex2d(0, 310)
#     glEnd()
#
#
#     glColor3f(0.2, 1.0, 0.6)
#     x=0
#     y= 240
#     for i in range(13):
#         glBegin(GL_TRIANGLES)
#         glVertex2d(x, y)
#         glVertex2d(x+40, y)
#         glVertex2d(x+20, y+50)
#         x=x+40
#         glEnd()
#
#     glColor3f(1.0, 0.4, 0.4)
#     glBegin(GL_TRIANGLES)
#     glVertex2d(150, 250)
#     glVertex2d(250, 325)
#     glVertex2d(350, 250)
#     glEnd()
#
#     glColor3f(1.0, 0.8, 1.0)
#     glBegin(GL_TRIANGLES)
#     glVertex2d(170, 160)
#     glVertex2d(330, 160)
#     glVertex2d(330, 250)
#
#     glVertex2d(170, 160)
#     glVertex2d(330, 250)
#     glVertex2d(170, 250)
#     glEnd()
#
#
#     glColor3f(0.0, 0.6, 0.6)
#     glBegin(GL_TRIANGLES)
#     glVertex2d(230, 160)
#     glVertex2d(270, 160)
#     glVertex2d(270, 220)
#
#     glVertex2d(230, 160)
#     glVertex2d(270, 220)
#     glVertex2d(230, 220)
#     glEnd()
#
#     glColor3f(0.0, 0.0, 0.0)
#     glPointSize(5)
#     glBegin(GL_POINTS)
#     glVertex2f(260,190)
#     glEnd()
#
#
#     glColor3f(0.0, 0.0, 0.0)
#     glBegin(GL_TRIANGLES)
#     glVertex2d(185, 190)
#     glVertex2d(215, 190)
#     glVertex2d(215, 220)
#
#     glVertex2d(185, 190)
#     glVertex2d(215, 220)
#     glVertex2d(185, 220)
#     glEnd()
#
#     glColor3f(1.0, 1.0, 1.0)
#     glBegin(GL_LINES)
#     glVertex2f(200,220)
#     glVertex2f(200,190)
#
#     glVertex2f(185,205)
#     glVertex2f(215,205)
#     glEnd()
#
#     glColor3f(0.0, 0.0, 0.0)
#     glBegin(GL_TRIANGLES)
#     glVertex2d(285, 190)
#     glVertex2d(315, 190)
#     glVertex2d(315, 220)
#
#     glVertex2d(285, 190)
#     glVertex2d(315, 220)
#     glVertex2d(285, 220)
#     glEnd()
#
#     glColor3f(1.0, 1.0, 1.0)
#     glBegin(GL_LINES)
#     glVertex2f(300,220)
#     glVertex2f(300,190)
#
#     glVertex2f(285,205)
#     glVertex2f(315,205)
#     glEnd()
#
# def iterate():
#     glViewport(0, 0, 500, 500)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
#     glMatrixMode (GL_MODELVIEW)
#     glLoadIdentity()
#
# def specialKeyListener(key, x, y):
#     global rain_drops_points,move_x,animate_x,animate_y
#     if key == GLUT_KEY_RIGHT:
#         move_x+=2
#         animate_x+=0.8
#         animate_y-=0.8
#         print(animate_x,animate_y, move_x)
#         print("rightward")
#
#     if key == GLUT_KEY_LEFT:
#         move_x -= 2
#         animate_y+=0.8
#         animate_x-=0.8
#         print(animate_x,animate_y, move_x)
#         print("leftward")
#
#
#
# def animate():
#     global rain_drops_points,move_x,animate_x,animate_y
#     for rain in rain_drops_points:
#         rain[1] -=animate_y
#         rain[0] += animate_x
#         if rain[1]<0 or rain[1]>500:
#             rain[0]= random.randint(0,500)
#             rain[1]= random.randint(0,500)
#     glutPostRedisplay()
#
#
# def keyboardListener(key, x, y):
#     global bg_change
#     if key == b'w':
#         bg_change+=0.25
#         glClearColor(bg_change, bg_change, bg_change, bg_change)
#         print('Its going to be morning')
#     if key == b's':
#         bg_change -= 0.25
#         glClearColor(bg_change, bg_change, bg_change, bg_change)
#         print('Its going to be night')
#
# def showScreen():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     myhouse()
#     make_rains()
#     glutSwapBuffers()
#
#
# def init():
#     glClearColor(0, 0, 0, 0)  # black background
#
#
#
# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(500, 500)
# glutInitWindowPosition(0, 0)
# wind = glutCreateWindow(b"Task1")
# init()
# glutDisplayFunc(showScreen)
# glutIdleFunc(animate)
# glutSpecialFunc(specialKeyListener)
# glutKeyboardFunc(keyboardListener)
# glutMainLoop()



#TASK2

# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import random
# pos_x = 0
# pos_y = 0
# size = 4
# point_blink = False
# point_blink_stop = True
# time = 0
# ball_coordinates = []
# space = False
# ball_speed = 0.8
#
#
#
# def new_coordinates(x_axis, y_axis):
#     a = x_axis - (500/2)
#     b = (500/2) - y_axis
#     return a,b
#
#
# def keyboardListener(key, x, y):
#     global space
#     if key == b' ':
#         space = not space
#     glutPostRedisplay()
#
#
# def specialKeyListener(key, x, y):
#     global ball_speed
#     if key==GLUT_KEY_UP:
#         ball_speed *= 2.4
#         print("Speed Increased")
#     if key== GLUT_KEY_DOWN:		#// up arrow key
#         ball_speed /= 2.4
#         print("Speed Decreased")
#     glutPostRedisplay()
#
# def mouseListener(button, state, x, y):
#     global ball_coordinates,size,point_blink
#     if button==GLUT_LEFT_BUTTON:
#         if state == GLUT_DOWN:
#             point_blink = not point_blink
#             print(point_blink)
#     if button==GLUT_RIGHT_BUTTON:
#         if state == GLUT_DOWN:
#             a,b = new_coordinates(x, y)
#             red_c = random.uniform(0.2, 1)
#             green_c = random.uniform(0.2, 1)
#             blue_c = random.uniform(0.2, 1)
#             diagonal_x = random.choice([1, -1])
#             diagonal_y = random.choice([1, -1])
#             ball_coordinates.append([a, b,[red_c,green_c,blue_c],[diagonal_x,diagonal_y]])
#             print(a,b)
#     glutPostRedisplay()
#
# def animate():
#     global ball_coordinates,size, point_blink,time,point_blink_stop,ball_speed
#     if not space:
#         for i in ball_coordinates:
#             if point_blink:
#                 time+=1
#                 if time>100:
#                     point_blink_stop = not point_blink_stop
#                     time = 0
#             i[0] += i[3][0]*ball_speed
#             i[1] += i[3][1]*ball_speed
#             if i[0] > 250 :
#                 i[3][0] *= -1
#             elif i[0] <-250:
#                 i[3][0] *= -1
#             elif i[1] > 250:
#                 i[3][1] *= -1
#             elif i[1] <-250:
#                 i[3][1] *= -1
#         glutPostRedisplay()
#
#
#
# def iterate():
#     glViewport(0, 0, 500, 500)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(-250, 250, -250, 250, 0.0, 1.0)
#     glMatrixMode (GL_MODELVIEW)
#     glLoadIdentity()
#
# def display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     global pos_x,pos_y,size,ball_coordinates,point_blink,point_blink_stop
#     for i in ball_coordinates:
#         x=i[0]
#         y=i[1]
#         if point_blink_stop or not point_blink:
#             glColor3f(i[2][0], i[2][1], i[2][2])
#         else:
#             glColor3f(0, 0, 0)
#         glPointSize(size)
#         glBegin(GL_POINTS)
#         glVertex2f(x, y)
#         glEnd()
#
#     glutSwapBuffers()
#
#
# def init():
#     glClearColor(0, 0, 0, 0)  # black background
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     gluPerspective(104,	1,	1,	1000.0)
#
# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(500, 500)
# glutInitWindowPosition(0, 0)
# wind = glutCreateWindow(b"OpenGL Coding Practice")
# init()
# glutDisplayFunc(display)
# glutMouseFunc(mouseListener)
# glutIdleFunc(animate)
# glutKeyboardFunc(keyboardListener)
# glutSpecialFunc(specialKeyListener)
#
# glutMainLoop()


diamond_width = (((diamond_x + 15) - (diamond_x - 15)) ** 2 + ((diamond_y - 20) - (diamond_y - 20)) ** 2) ** 1 / 2
diamond_height = (((diamond_x + 15) - (diamond_x + 15)) ** 2 + ((diamond_y - 20) - (diamond_y - 40)) ** 2) ** 1 / 2
box_width = (((top_right_x) - (top_left_x)) ** 2 + ((top_right_y) - (top_left_y)) ** 2) ** 1 / 2
box_height = (((top_right_x) - (top_right_x)) ** 2 + ((top_right_y) - (bottom_right_y)) ** 2) ** 1 / 2


if (diamond_x-15)<(top_left_x + box_width) and ((diamond_x-15)+diamond_width) > top_left_x and (diamond_y-40) < (bottom_left_y+ box_height and ((diamond_y-40)+diamond_height)) > bottom_left_y: