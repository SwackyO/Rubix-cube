from ursina import *

app = Ursina()

cube_size = 0.95
gap = 0.05
cubies = []

face_colors = {
    'front': color.red,
    'back': color.orange,
    'left': color.blue,
    'right': color.green,
    'top': color.white,
    'bottom': color.yellow
}

class Cubie(Entity):
    def __init__(self, position):
        super().__init__(
            model='cube',
            color=color.black,               # darker body to contrast stickers
            position=position,
            scale=Vec3(cube_size, cube_size, cube_size)
        )
        self.add_stickers()

    def add_stickers(self):
        offset = (cube_size / 2) + 0.01
        th = 0.06                          # sticker thickness
        sz = cube_size * 0.9              # sticker height/width

        x, y, z = self.position

        # right face
        if x > 0.9:
            Entity(parent=self,
                   model='cube',
                   color=face_colors['right'],
                   scale=(th, sz, sz),
                   position=( offset, 0,    0   ))
        # left face
        if x < -0.9:
            Entity(parent=self,
                   model='cube',
                   color=face_colors['left'],
                   scale=(th, sz, sz),
                   position=(-offset, 0,    0   ))
        # top face
        if y > 0.9:
            Entity(parent=self,
                   model='cube',
                   color=face_colors['top'],
                   scale=(sz, th, sz),
                   position=(0,    offset, 0   ))
        # bottom face
        if y < -0.9:
            Entity(parent=self,
                   model='cube',
                   color=face_colors['bottom'],
                   scale=(sz, th, sz),
                   position=(0,   -offset, 0   ))
        # front face
        if z > 0.9:
            Entity(parent=self,
                   model='cube',
                   color=face_colors['front'],
                   scale=(sz, sz, th),
                   position=(0,    0,    offset))
        # back face
        if z < -0.9:
            Entity(parent=self,
                   model='cube',
                   color=face_colors['back'],
                   scale=(sz, sz, th),
                   position=(0,    0,   -offset))

def make_cube():
    for x in range(3):
        for y in range(3):
            for z in range(3):
                pos = Vec3(x - 1, y - 1, z - 1) * (cube_size + gap)
                cubies.append(Cubie(pos))

make_cube()

# camera + light
EditorCamera()
DirectionalLight()

camera.position = (0, 0, -10)
camera.look_at(Vec3(0, 0, 0))

app.run()
