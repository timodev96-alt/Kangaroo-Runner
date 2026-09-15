import raylib
import pyray

pyray.init_window(1280,720,'Kangaroo Runner')

while not raylib.WinndoSouldClose():
    raylib.BeginDrawing()
    raylib.DrawCircle(100,200,50,raylib.RED)
    if raylib.IsKeyPressed(raylib.KEY_SPACE):
        print('Space')
    raylib.EndDrawing()