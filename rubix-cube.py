from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

# Config
cube_size = 0.95
gap = 0.05

# Create a 3x3x3 grid of cubes
cubies = []

class Cubie(Entity):
    def __init__(self, position):
        super().__init__(
            model='cube',
            color=color.white,
            position=position,
            scale=Vec3(cube_size, cube_size, cube_size),
            collider='box'
        )

def make_cube():
    for x in range(3):
        for y in range(3):
            for z in range(3):
                pos = Vec3(x - 1, y - 1, z - 1) * (cube_size + gap)
                cubie = Cubie(pos)
                cubies.append(cubie)

make_cube()

# Mouse controls
selected_axis = 'y'
rotation_angle = 0
is_rotating = False
layer = []

def input(key):
    global selected_axis, is_rotating, rotation_angle, layer

    if is_rotating:
        return

    if key == 'left mouse down':
        hit_info = mouse.hovered_entity
        if hit_info:
            layer = [c for c in cubies if abs(c.world_position.y - hit_info.world_position.y) < 0.1]
            is_rotating = True
            rotation_angle = 0

def update():
    global rotation_angle, is_rotating

    if is_rotating:
        angle_step = 5
        for c in layer:
            c.rotation_y += angle_step
        rotation_angle += angle_step
        if rotation_angle >= 90:
            is_rotating = False
            rotation_angle = 0

EditorCamera()  # Allows orbiting with right-click drag
app.run()
