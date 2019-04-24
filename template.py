from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# screen resolution
import ctypes                            #######

user32 = ctypes.windll.user32            #######


def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, 1, 1, 70)
    gluLookAt(8, 9, 10,
              0, 0, 0,
              0, 1, 0)

    glClearColor(1, 1, 1, 1)


    # Enable light 1 and set position
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLight(GL_LIGHT0, GL_POSITION,  (0.5, 2.5, 3))
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)


def draw():

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)
    glClearColor(51 / 255, 164 / 255, 1,1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	
	
	### START CODE HERE ###                                       #######
    glColor(0,0,1)
    glutSolidTorus(0.125, 0.5, 20, 20)
	### END CODE HERE ### 

	
	
	
    glutSwapBuffers()


def specialKeyHandler(key, x, y):
    global car_z
    if key == GLUT_KEY_RIGHT:
        quit()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))    #########
glutCreateWindow(b"Moving Car")
glutFullScreen()                                                              #########
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(specialKeyHandler)
glutMainLoop()
