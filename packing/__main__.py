from packer.packer import Packer
from box.box import Box

packer = Packer()

packer.add_boxes([Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160)])
packer.pack()

print('\n')
print(packer)
print(packer.containers[0].boxes)


"""
[0,0,0]     - Box(1,600, 400, 300)
[400, 0, 0] - Box(2,360, 240, 160)
[0, 300, 0] - Box(3,440,320, 200)
[640, 0, 0] - Box(4,360, 240, 160)

"""