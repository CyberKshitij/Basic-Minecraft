from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController



app = Ursina()

block = 0
white_color = load_texture('Kshitij/Exam/Grass.png')


def update():
    if held_keys['1']:
        block = 1 


class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_color',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.cyan
        )


    def input(self, key):
        update()
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal )

                if block == 1:
                    voxel = Voxel(position=self.position + mouse.normal , colour= color.color(0,1 , random.uniform(.9 , 1.0)))
            

            if key == 'right mouse down':
                destroy(self)

        

for z in range(50):
    for x in range(50):
        voxel = Voxel(position=(x,0,z))
        

player = FirstPersonController()
app.run()