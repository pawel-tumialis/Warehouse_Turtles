import matplotlib.pyplot as plt

from container.container import EPAL

class Plotter():

    def __init__(self, ) -> None:
        pass
    def _plot_container(self, ax, container):
        x,y,z = 0,0,0
        dx, dy, dz = container.WIDTH, container.HEIGHT, container.DEPTH
        xx = [x, x, x+dx, x+dx, x]
        yy = [y, y+dy, y+dy, y, y]

        kwargs = {'alpha': 1, 'color': 'black','linewidth':1}
 
        ax.plot3D(xx, yy, [z]*5, **kwargs)
        ax.plot3D(xx, yy, [z+dz]*5, **kwargs)
        ax.plot3D([x, x], [y, y], [z, z+dz], **kwargs)
        ax.plot3D([x, x], [y+dy, y+dy], [z, z+dz], **kwargs)
        ax.plot3D([x+dx, x+dx], [y+dy, y+dy], [z, z+dz], **kwargs)
        ax.plot3D([x+dx, x+dx], [y, y], [z, z+dz], **kwargs)

    def _plot_box(self, ax, x, y, z, dx, dy, dz):
        ax.bar3d(x, y, z, dx, dy, dz, alpha=0.8)


    def prepare_plot(self, container:EPAL):

        # fig = plt.figure()
        axGlob = plt.axes(projection='3d')
        self._plot_container(axGlob, container)

        for box in container.boxes:
            x,y,z = box.position
            w,h,d = box.get_dimension()
            self._plot_box(axGlob, x,y,z,w,h,d)

        return plt