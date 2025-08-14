quad_size = GRID_LENGTH * 2 / 13  # size of each square
start_x = -GRID_LENGTH
start_y = GRID_LENGTH

glBegin(GL_QUADS)
for row in range(13):
    for col in range(13):
        # Alternate colors like a chessboard
        if (row + col) % 2 == 0:
            glColor3f(1, 1, 1)  # White
        else:
            glColor3f(0.7, 0.5, 0.95)  # Purple

        x1 = start_x + col * quad_size
        y1 = start_y - row * quad_size
        x2 = x1 + quad_size
        y2 = y1 - quad_size

        glVertex3f(x1, y1, 0)
        glVertex3f(x2, y1, 0)
        glVertex3f(x2, y2, 0)
        glVertex3f(x1, y2, 0)
glEnd()


glBegin(GL_QUADS)
for i in range(13):

    for j in range(13):
        if (i + j) % 2 != 0:
            glColor3f(0.7, 0.5, 0.95)
        else:
            glColor3f(1, 1, 1)

        x_1 = (-grid_x) + j * 60
        y_1 = grid_x - i * 60
        x_2 = x_1 + 60
        y_2 = y_1 - 60
        glVertex3f(x_1, y_1, 0)
        glVertex3f(x_2, y_1, 0)
        glVertex3f(x_2, y_2, 0)
        glVertex3f(x_1, y_2, 0)

glEnd()


# glColor3f(0, 0, 1)
    # glBegin(GL_QUADS)
    # y1 = 600
    # z1 = 0
    # y2 = -480
    # z2 = 50
    # glVertex3f(-600, y1, z1)
    # glVertex3f(-600, y2, z1)
    # glVertex3f(-600, y2, z2)
    # glVertex3f(-600, y1, z2)
    # glEnd()
    # glColor3f(0, 1, 0)
    # glBegin(GL_QUADS)
    # x1 = -600
    # z1 = 0
    # x2 = 570
    # z2 = 50
    # glVertex3f(x1, -480, z1)
    # glVertex3f(x2, -480, z1)
    # glVertex3f(x2, -480, z2)
    # glVertex3f(x1, -480, z2)
    # glEnd()
    # glColor3f(0, 1, 1)
    # glBegin(GL_QUADS)
    # y1 = 600
    # z1 = 0
    # y2 = -480
    # z2 = 50
    # glVertex3f(570, y1, z1)
    # glVertex3f(570, y2, z1)
    # glVertex3f(570, y2, z2)
    # glVertex3f(570, y1, z2)
    # glEnd()
    # glColor3f(1, 1, 1)
    # glBegin(GL_QUADS)
    # x1 = -600
    # z1 = 0
    # x2 = 570
    # z2 = 50
    # glVertex3f(x1, 600, z1)
    # glVertex3f(x2, 600, z1)
    # glVertex3f(x2, 600, z2)
    # glVertex3f(x1, 600, z2)
    # glEnd()

# glPushMatrix()
    # glColor3f(0.3, 0.6, 0)
    # glTranslatef(player_x, player_y, player_z)
    # glRotatef(player_r, x_r, y_r, z_r)
    # glTranslatef(0, 0, 10)
    # gluCylinder(gluNewQuadric(), 18, 18, 50, 5, 2)
    # glColor3f(0, 0, 1)
    # glTranslatef(-20, 0, -10)
    # gluCylinder(gluNewQuadric(), 5, 12, 20, 10, 10)
    # glTranslatef(  40, 0, 0)
    # gluCylinder(gluNewQuadric(), 5, 12, 20, 10, 10)
    # glTranslatef( - 20, 0,  72)
    # glColor3f(0, 0, 0)
    # gluSphere(gluNewQuadric(), 16, 10, 10)
    # glTranslatef( 25,  25,  - 30)
    # glColor3f(1,0.8,0.6)
    # glRotatef(90, 1, 0, 0)
    # gluCylinder(gluNewQuadric(), 5, 12, 30, 10, 10)
    # glTranslatef( - 50, 0, 0)
    # glColor3f(1,0.8,0.6)
    # gluCylinder(gluNewQuadric(), 5, 12, 30, 10, 10)
    # glTranslatef(25 , 0, -10)
    # glColor3f(0.87,0.87,0.87)
    # gluCylinder(gluNewQuadric(), 4, 12, 40, 10, 10)
    # glPopMatrix()  # Restore the previous matrix state