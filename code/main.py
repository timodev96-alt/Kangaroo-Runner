import raylib as rl
from pyray import *

init_window(1280,720,'Kangaroo Runner')
x_pos = 100
y_pos = 100

while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)
    draw_circle(int(x_pos),int(y_pos),50,RED)
    if is_key_down(rl.KEY_D):
        x_pos += 0.1
    if is_key_down(rl.KEY_A):
        x_pos -= 0.1
    if is_key_down(rl.KEY_S):
        y_pos += 0.1
    if is_key_down(rl.KEY_W):
        y_pos -= 0.1
    if is_key_pressed(rl.KEY_SPACE):
        close_window()
    end_drawing()