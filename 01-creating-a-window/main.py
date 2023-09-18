import ctypes
import sdl2
from OpenGL import GL

window = None
context = None

windowWidth = 1024
windowHeight = 600

def init():
    global window, context

    if sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING) != 0:
        print("Unable to initialise SDL!")
        return -1

    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 4)
    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 6)
    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)

    window = sdl2.SDL_CreateWindow(b"Lesson 01 - Creating a Window", sdl2.SDL_WINDOWPOS_UNDEFINED, sdl2.SDL_WINDOWPOS_UNDEFINED, windowWidth, windowHeight, sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_OPENGL)
    if not window:
        print("Unable to create a window!")
        return -1

    context = sdl2.SDL_GL_CreateContext(window)
    if not context:
        print("Unable to create an OpenGL context!")
        return -1

    majorVersion = ctypes.c_int32()
    minorVersion = ctypes.c_int32()
    sdl2.SDL_GL_GetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, ctypes.pointer(majorVersion))
    sdl2.SDL_GL_GetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, ctypes.pointer(minorVersion))
    if majorVersion.value < 4 or (majorVersion.value == 4 and minorVersion.value < 5):
        print("Unable to get a recent OpenGL version!")
        return -1

    print(GL.glGetString(GL.GL_VERSION).decode())

    GL.glClearColor(0.04, 0.23, 0.51, 1.0)

    return 0

def close():

    sdl2.SDL_GL_DeleteContext(context)
    sdl2.SDL_DestroyWindow(window)
    sdl2.SDL_Quit()

def draw():

    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    sdl2.SDL_GL_SwapWindow(window)

def main():

    if init() != 0:
        return

    draw()

    import time
    time.sleep(2)

    close()

if __name__ == "__main__":
    main()
