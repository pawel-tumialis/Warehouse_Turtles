import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.axes_grid1
import matplotlib.widgets

from container.container import EPAL

class Player(FuncAnimation):
    def __init__(self, fig, func, frames=None, init_func=None, fargs=None,
                 save_count=None, mini=0, maxi=100, pos=(0.125, 0.92), **kwargs):
        self.i = 0
        self.min=mini
        self.max=maxi
        self.runs = True
        self.forwards = True
        self.fig = fig
        self.func = func
        self.setup(pos)
        
        FuncAnimation.__init__(self,self.fig, func=func, frames=frames, 
                                           init_func=init_func, fargs=fargs,
                                           save_count=save_count, **kwargs )    

    def play(self):
        while self.runs:
            self.i = self.i+self.forwards-(not self.forwards)
            if self.i > self.min and self.i < self.max:
                yield self.i
            else:
                self.stop()
                yield self.i

    def start(self):
        self.runs=True
        self.event_source.start()

    def stop(self, event=None):
        self.runs = False
        self.event_source.stop()

    def forward(self, event=None):
        self.forwards = True
        self.start()
    def backward(self, event=None):
        self.forwards = False
        self.start()
    def oneforward(self, event=None):
        self.forwards = True
        self.onestep()
    def onebackward(self, event=None):
        self.forwards = False
        self.onestep()

    def onestep(self):
        if self.i > self.min and self.i < self.max:
            self.i = self.i+self.forwards-(not self.forwards)
        elif self.i == self.min and self.forwards:
            self.i+=1
        elif self.i == self.max and not self.forwards:
            self.i-=1
        self.func(self.i, *self._args)
        self.slider.set_val(self.i)
        self.fig.canvas.draw_idle()

    def setup(self, pos):
        playerax = self.fig.add_axes([pos[0],pos[1], 0.64, 0.04])
        divider = mpl_toolkits.axes_grid1.make_axes_locatable(playerax)
        # bax = divider.append_axes("right", size="80%", pad=0.05)
        sax = divider.append_axes("right", size="80%", pad=0.05)
        # fax = divider.append_axes("right", size="80%", pad=0.05)
        ofax = divider.append_axes("right", size="100%", pad=0.05)
        sliderax = divider.append_axes("right", size="500%", pad=0.07)
        self.button_oneback = matplotlib.widgets.Button(playerax, label='$\u29CF$')
        # self.button_back = matplotlib.widgets.Button(bax, label='$\u25C0$')
        self.button_stop = matplotlib.widgets.Button(sax, label='$\u25A0$')
        # self.button_forward = matplotlib.widgets.Button(fax, label='$\u25B6$')
        self.button_oneforward = matplotlib.widgets.Button(ofax, label='$\u29D0$')
        self.button_oneback.on_clicked(self.onebackward)
        # self.button_back.on_clicked(self.backward)
        self.button_stop.on_clicked(self.stop)
        # self.button_forward.on_clicked(self.forward)
        self.button_oneforward.on_clicked(self.oneforward)
        self.slider = matplotlib.widgets.Slider(sliderax, '', 
                                                self.min, self.max, valinit=self.i)
        self.slider.on_changed(self.set_pos)

    def set_pos(self,i):
        self.i = int(self.slider.val)
        self.func(self.i, *self._args)

    def update(self,i):
        self.slider.set_val(i)

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
    
    def _animation_update(self, frame, ax, container:EPAL):
        # frame = frame - 2
        ax.clear()
        self._plot_container(ax, container)
        for box in container.boxes[:frame]:
            # pass
            # box = container.boxes[frame]
            x,y,z = box.position
            w,h,d = box.get_dimension()
            self._plot_box(ax, x,y,z,w,h,d)
        return ax

    def prepare_animated_plot(self, container:EPAL):

        fig = plt.figure()
        axGlob = plt.axes(projection='3d')

        self._plot_container(axGlob, container)
        # ani = animation.FuncAnimation(fig=fig, func=self._animation_update, fargs=(axGlob, container), frames=len(container.boxes), interval=1000/len(container.boxes))
        ani = Player(fig=fig, func=self._animation_update, fargs=(axGlob, container), maxi=len(container.boxes), frames=len(container.boxes))
        ani.pause()
        
        axGlob.clear()
        self._plot_container(axGlob, container)

        for box in container.boxes:
            x,y,z = box.position
            w,h,d = box.get_dimension()
            self._plot_box(axGlob, x,y,z,w,h,d)

        return plt
    
    def prepare_plot(self, container:EPAL):
        fig = plt.figure()
        axGlob = plt.axes(projection='3d')

        self._plot_container(axGlob, container)
        self._plot_container(axGlob, container)

        for box in container.boxes:
            x,y,z = box.position
            w,h,d = box.get_dimension()
            self._plot_box(axGlob, x,y,z,w,h,d)

        return plt