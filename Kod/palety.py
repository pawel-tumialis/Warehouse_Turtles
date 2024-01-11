from packer.packer import Packer
from plotter.plotter import Plotter
from box.box import Box
import pandas as pd

class palety_marcel:
    def __init__(self, df) -> None:
        self.data = df
        self.sizes = self.data["Wymiary (mm)"]
        
        self.packer = Packer()
        
        for index, row in self.data.iterrows():
            it = row["Ilosc"]

            sizes = row["Wymiary (mm)"]
            Z_axis = sizes.split("x")[2]
            Y_axis = sizes.split("x")[1]
            X_axis = sizes.split("x")[0]
            for _ in range(it):
                self.packer.add_box(Box(0, int(X_axis), int(Y_axis), int(Z_axis)))

        self.packer.pack()

        print('\n')
        print(self.packer)
    
    def get_palety(self):
        return len(self.packer.containers)

    def show(self, index):
        ploter = Plotter()
        fig = ploter.prepare_animated_plot(self.packer.containers[index])
        fig = ploter.prepare_plot(self.packer.containers[index])
        fig.show()




# packer.add_boxes([Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(4,360, 240, 160)])
# packer.add_boxes([Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200), Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200),Box(1,600, 400, 300), Box(2,360, 240, 160), Box(3,440,320, 200)])


