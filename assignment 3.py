from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# Camera-related variables
camera_pos = (0, 500, 500)
look_at_target = (0, 0, 0)
player_x = 0
player_y = 0
player_z = 0
player_r = 0
x_r = 0
y_r = 0
z_r = 1
camera_angle = 0
enemy_list = []
enemy_z = 0
enemy_rad = 20
for i in range(5):
    enemy_x = random.uniform(-550, 500)
    enemy_y = random.uniform(-550, 500)
    enemy_list.append([enemy_x, enemy_y])

fovY = 120
rand_var = 423
bullet_list = []
bullet_c = 1
missed_bullet = 0
scored = 0
player_life = 5
game_over = False
fpp = False
cheat_mode = False




def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()

    # Set up an orthographic projection that matches window coordinates
    gluOrtho2D(0, 1000, 0, 800)  # left, right, bottom, top

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    # Draw text at (x, y) in screen coordinates
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))

    # Restore original projection and modelview matrices
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def draw_shapes():
    global player_x, player_y, player_z, x_r, y_r, z_r, game_over

    glPushMatrix()
    glTranslatef(player_x, player_y, player_z)
    if game_over:
        glRotate(90, 1, 0, 0)
    else:
        glRotatef(player_r, x_r, y_r, z_r)
    glTranslatef(-20, 0, 0)
    glColor3f(0, 0, 1)
    gluCylinder(gluNewQuadric(), 5, 12, 20, 10, 10)
    glTranslatef(  40, 0, 0)
    gluCylinder(gluNewQuadric(), 5, 12, 20, 10, 10)
    glTranslatef(-20, 0, 40)
    glColor3f(0.3, 0.6, 0)
    glutSolidCube(40)
    glTranslatef( 0, 0,  38)
    glColor3f(0, 0, 0)
    gluSphere(gluNewQuadric(), 16, 10, 10)
    glTranslatef( 25,  40,  - 30)
    glColor3f(1,0.8,0.6)
    glRotatef(90, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 5, 12, 40, 10, 10)
    glTranslatef( - 50, 0, 0)
    glColor3f(1,0.8,0.6)
    gluCylinder(gluNewQuadric(), 5, 12, 40, 10, 10)
    glTranslatef(25 , 0, -20)
    glColor3f(0.87,0.87,0.87)
    gluCylinder(gluNewQuadric(), 1, 12, 60, 10, 10)
    glPopMatrix()


def enemy():
    global  enemy_list,enemy_z,enemy_rad
    for val in enemy_list:
        glPushMatrix()
        glColor3f(1,0,0)
        glTranslatef(0,0,0)
        glTranslatef(val[0], val[1], enemy_z)
        gluSphere(gluNewQuadric(), enemy_rad, 10, 10)
        glColor3f(0, 0, 0)
        enemy_rad1 = enemy_rad - 10
        glTranslatef(0, 0, 20)
        gluSphere(gluNewQuadric(), enemy_rad1, 10, 10)
        glPopMatrix()


def bullet():
    global bullet_list, bullet_c
    for bullet in bullet_list:
        glPushMatrix()
        glColor3f(bullet_c,0,0)
        glTranslatef(bullet[0],bullet[1],bullet[2])
        glutSolidCube(10)
        glPopMatrix()

def restart_game():
    global fpp,look_at_target, camera_pos, player_x,  player_y, player_z, player_r, x_r ,y_r, z_r, game_over, camera_angle,enemy_z,enemy_rad,enemy_list,enemy_x,enemy_y,fovY,missed_bullet,bullet_list, bullet_c, scored,player_life
    camera_pos = (0, 500, 500)
    look_at_target = (0, 0, 0)
    player_x = 0
    player_y = 0
    player_z = 0
    player_r = 0
    x_r = 0
    y_r = 0
    z_r = 1
    camera_angle = 0
    enemy_list = []
    enemy_z = 0
    enemy_rad = 20
    for i in range(5):
        enemy_x = random.uniform(-550, 500)
        enemy_y = random.uniform(-550, 500)
        enemy_list.append([enemy_x, enemy_y])

    fovY = 120
    bullet_list = []
    bullet_c = 1
    missed_bullet = 0
    scored = 0
    player_life = 5
    game_over = False
    fpp = False





def keyboardListener(key, x, y):
    global player_x, player_y, player_z, player_r, x_r, y_r, z_r, game_over, fovY, cheat_mode
    rad1 = math.radians(player_r + 90)
    # # Move forward (W key)
    if key == b'w':
        if not game_over:
            if -600 <= (player_x + 15 *math.cos(rad1)) <= 570 and -600 <= (player_y + 15 *math.sin(rad1)) <= 570:
                player_x += 15 *math.cos(rad1)
                player_y += 15 *math.sin(rad1)

    # # Move backward (S key)
    if key == b's':
        if not game_over:
            if -600 <= (player_x - 15 *math.cos(rad1)) <= 570 and -600 <= (player_y - 15 *math.sin(rad1)) <= 570:
                player_x -= 15 *math.cos(rad1)
                player_y -= 15 *math.sin(rad1)
    # # Rotate gun left (A key)
    if key == b'a':
        if not game_over:
            player_r += 5

    # # Rotate gun right (D key)
    if key == b'd':
        if not game_over:
            player_r -= 5


    # # Toggle cheat mode (C key)
    if key == b'c':
        cheat_mode = not cheat_mode
    # # Toggle cheat vision (V key)
    # if key == b'v':

    # # Reset the game if R key is pressed
    if key == b'r':
        restart_game()
    if key == b'n':
        fovY -= 10
    if key == b'm':
        fovY += 10


def specialKeyListener(key, x, y):

    global camera_pos, camera_angle
    rad = math.radians(camera_angle)
    cam_x, cam_y, cam_z = camera_pos
    d = (cam_x ** 2 + cam_y ** 2) ** 0.5

    # # Move camera up (UP arrow key)
    if key == GLUT_KEY_UP:
        cam_z += 10

    # # # Move camera down (DOWN arrow key)
    if key == GLUT_KEY_DOWN:
        cam_z -=10

    # # moving camera left (LEFT arrow key)
    if key == GLUT_KEY_LEFT:
        camera_angle -= 5
        rad = math.radians(camera_angle)
        cam_x = d * math.cos(rad)
        cam_y = d * math.sin(rad)
        # Small angle decrement for smooth movement
    #
    # # moving camera right (RIGHT arrow key)
    if key == GLUT_KEY_RIGHT:
        camera_angle += 5
        rad = math.radians(camera_angle)
        cam_x = d * math.cos(rad)
        cam_y = d * math.sin(rad)
    # Small angle increment for smooth movement
    #
    camera_pos = (cam_x, cam_y, cam_z)


def mouseListener(button, state, x, y):
    global fovY, player_z, player_r, player_x, player_y, player_z, bullet_list, game_over,camera_pos,look_at_target, fpp
    # # Left mouse button fires a bullet
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if not game_over:
            bullet_x = player_x
            bullet_y = player_y
            bullet_z = player_z
            bullet_r = math.radians(player_r + 90)
            bullet_dx = math.cos(bullet_r)
            bullet_dy = math.sin(bullet_r)
            bullet_list.append([bullet_x, bullet_y, bullet_z ,bullet_dx, bullet_dy])

        # # Right mouse button toggles camera tracking mode
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        fpp = not fpp



def setupCamera():
    global camera_pos,look_at_target
    glMatrixMode(GL_PROJECTION)  # Switch to projection matrix mode
    glLoadIdentity()  # Reset the projection matrix
    # Set up a perspective projection (field of view, aspect ratio, near clip, far clip)
    gluPerspective(fovY, 1.25, 0.1, 1500)  # Think why aspect ration is 1.25?
    glMatrixMode(GL_MODELVIEW)  # Switch to model-view matrix mode
    glLoadIdentity()  # Reset the model-view matrix

    # Extract camera position and look-at target
    if not fpp:
        x, y, z = camera_pos
        d,e,f = look_at_target
    else:
        rad = math.radians(player_r+ 90)
        x = player_x + 10 * math.cos(rad)
        y = player_y + 10 * math.sin(rad)
        z = 99
        d = player_x + 50 * math.cos(rad)
        e = player_y + 50 * math.sin(rad)
        f = 99
    # Position the camera and set its orientation
    gluLookAt(x, y, z,  # Camera position
              d, e, f,  # Look-at target
              0, 0, 1)  # Up vector (z-axis)


def idle():
    global enemy_rad,enemy_list, player_x, player_y, player_z,player_r, bullet_list,enemy_x, enemy_y, missed_bullet,scored,player_life, game_over, cheat_mode
    if cheat_mode:
        player_r += 5
        for enemies in enemy_list:
            e_x = player_x - enemies[0]
            e_y = player_y - enemies[1]
    #start from here


    for c_r in enemy_list:
        dx = c_r[0] - player_x
        dy = c_r[1] - player_y
        c_r[0] -= dx* 0.001
        c_r[1] -= dy * 0.001
        dis = math.sqrt((player_x - c_r[0])**2 + (player_y - c_r[1])**2)
        if dis < enemy_rad:
            player_life -= 1
            enemy_list.remove(c_r)
            enemy_x = random.uniform(-550, 500)
            enemy_y = random.uniform(-550, 500)
            enemy_list.append([enemy_x, enemy_y])
            if player_life == 0:
                game_over = True

    if 20 <= enemy_rad <= 40:
        enemy_rad += 0.25
    elif enemy_rad> 40:
        enemy_rad = 20
    bullet_speed = 10
    for bullet in bullet_list:
        if -610 <=(bullet[0]) <= 590 and -610 <=(bullet[1]) <= 590:
            bullet[0] += bullet[3] * bullet_speed
            bullet[1] += bullet[4] * bullet_speed
            for enemy in enemy_list:
                d = math.sqrt((bullet[0] - enemy[0])**2 + (bullet[1] - enemy[1])**2)
                if d < enemy_rad:
                     scored += 1
                     enemy_list.remove(enemy)
                     enemy_x = random.uniform(-550, 500)
                     enemy_y = random.uniform(-550, 500)
                     enemy_list.append([enemy_x, enemy_y])
                     bullet_list.remove(bullet)
                     print(f"scored: {scored}")
        else:
            missed_bullet +=1
            bullet_list.remove(bullet)
            print(f"missed bullet: {missed_bullet}")
            if missed_bullet >= 5:
                game_over = True

    # Ensure the screen updates with the latest changes
    glutPostRedisplay()


def showScreen():
    """
    Display function to render the game scene:
    - Clears the screen and sets up the camera.
    - Draws everything of the screen
    """
    # Clear color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset modelview matrix
    glViewport(0, 0, 1000, 800)  # Set viewport size

    setupCamera()# Configure camera perspective
    grid_y = 600
    # Draw the grid (game floor)
    glBegin(GL_QUADS)
    for i in range(13):
        grid_x = -600
        for j in range(13):
            if (i+j) %2 != 0:
                glColor3f(0.7, 0.5, 0.95)
            else:
                glColor3f(1, 1, 1)

            x_1 = grid_x
            y_1  = grid_y
            x_2 = x_1+ 90
            y_2 = y_1 - 90
            glVertex3f(x_1, y_1, 0)
            glVertex3f(x_2, y_1, 0)
            glVertex3f(x_2, y_2, 0)
            glVertex3f(x_1, y_2, 0)
            grid_x += 90
        grid_y -=90
    glEnd()


    glBegin(GL_QUADS)
    for i in range(2):
        if i % 2 == 0:
            glColor3f(0, 0, 1)
            y1 = 600
            z1 = 0
            y2 = -570
            z2 = 50
            glVertex3f(-600, y1, z1)
            glVertex3f(-600, y2, z1)
            glVertex3f(-600, y2, z2)
            glVertex3f(-600, y1, z2)

            glColor3f(0, 1, 1)
            glVertex3f(570, y1, z1)
            glVertex3f(570, y2, z1)
            glVertex3f(570, y2, z2)
            glVertex3f(570, y1, z2)
        else:
            glColor3f(0, 1, 0)
            x1 = -600
            z1 = 0
            x2 = 570
            z2 = 50
            glVertex3f(x1, -570, z1)
            glVertex3f(x2, -570, z1)
            glVertex3f(x2, -570, z2)
            glVertex3f(x1, -570, z2)

            glColor3f(1, 1, 1)
            glVertex3f(x1, 600, z1)
            glVertex3f(x2, 600, z1)
            glVertex3f(x2, 600, z2)
            glVertex3f(x1, 600, z2)
    glEnd()
    if not game_over:
        enemy()
        draw_text(10, 770, f"Player Life Remaining: {player_life}")
        draw_text(10, 740, f"Game Score: {scored}")
        draw_text(10, 710, f"Player Bullet Missed: {missed_bullet}")
        bullet()
    else:
        draw_text(10, 770, f"Game is Over. Your Score is {scored}.")
        draw_text(10, 740, f"Press "R" to Restart the Game.")

    draw_shapes()
    glutSwapBuffers()


# Main function to set up OpenGL window and loop
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # Double buffering, RGB color, depth test
    glutInitWindowSize(1000, 800)  # Window size
    glutInitWindowPosition(0, 0)  # Window position
    wind = glutCreateWindow(b"3D OpenGL Intro")  # Create the window

    glutDisplayFunc(showScreen)  # Register display function
    glutKeyboardFunc(keyboardListener)  # Register keyboard listener
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)  # Register the idle function to move the bullet automatically

    glutMainLoop()  # Enter the GLUT main loop


if __name__ == "__main__":
    main()
