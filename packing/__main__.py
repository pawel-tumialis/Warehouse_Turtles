from packer.packer import Packer
from plotter.plotter import Plotter
from box.box import Box
import pandas as pd

packer = Packer()

# data = pd.read_csv("C:\\dev\\hest_hackaton\\Pakowanie.csv")
# sizes = data["Wymiary (mm)"]
# for index, row in data.iterrows():
#     sizes = row["Wymiary (mm)"]
#     Z_axis = sizes.split("x")[2]
#     Y_axis = sizes.split("x")[1]
#     X_axis = sizes.split("x")[0]
#     packer.add_box(Box(index, int(X_axis), int(Y_axis), int(Z_axis)))



# packer.add_boxes([Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160)])
# packer.add_boxes([Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200)])
packer.pack()

print('\n')
print(packer)
# print(packer.containers[0].boxes)

ploter = Plotter()
fig = ploter.prepare_animated_plot(packer.containers[0])
fig = ploter.prepare_plot(packer.containers[0])
fig.show()
