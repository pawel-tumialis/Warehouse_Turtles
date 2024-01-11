import utilities.cnst as cnst
from itertools import count
from box.box import Box

def rect_intersect(box1, box2, x, y):
    d1 = box1.get_dimension()
    d2 = box2.get_dimension()

    cx1 = box1.position[x] + d1[x]/2
    cy1 = box1.position[y] + d1[y]/2
    cx2 = box2.position[x] + d2[x]/2
    cy2 = box2.position[y] + d2[y]/2

    ix = max(cx1, cx2) - min(cx1, cx2)
    iy = max(cy1, cy2) - min(cy1, cy2)

    return ix < (d1[x]+d2[x])/2 and iy < (d1[y]+d2[y])/2

def intersect(box1, box2):
    return (
        rect_intersect(box1, box2, cnst.Axis.WIDTH, cnst.Axis.HEIGHT) and
        rect_intersect(box1, box2, cnst.Axis.HEIGHT, cnst.Axis.DEPTH) and
        rect_intersect(box1, box2, cnst.Axis.WIDTH, cnst.Axis.DEPTH)
    )

class EPAL:
    _instance_count = count(start=1)

    WIDTH = 800
    HEIGHT= 1200
    EPAL_HEIGHT = 144
    DEPTH = 2000 - EPAL_HEIGHT

    def __init__(self):
        self.id = next(self._instance_count)
        self.boxes = []
    
    def __repr__(self):
        return f"[EPAL]: {self.id=}"
    
    def _gravity(self, new_box: Box, pivot):

        while True:
            new_box.position[2] -= 1
            box_dimension = new_box.get_dimension()
            if not self.is_inside(pivot, box_dimension):
                new_box.position[2] += 1
                return new_box
            for box_in_container in self.boxes:
                if intersect(box_in_container, new_box):
                    new_box.position[2] += 1
                    return new_box
        new_box.position[2] += 1
        return new_box
        
    def is_empty(self):
        return len(self.boxes) == 0
    
    def is_inside(self, pivot, box_dimension):
        return not (EPAL.WIDTH  < pivot[0] + box_dimension[0] or 
                    EPAL.HEIGHT < pivot[1] + box_dimension[1] or 
                    EPAL.DEPTH  < pivot[2] + box_dimension[2] or 
                    0 >= pivot[0] + box_dimension[0] or
                    0 >= pivot[1] + box_dimension[1] or 
                    0 >= pivot[2] + box_dimension[2])


    def get_volume(self):
        return EPAL.WIDTH * EPAL.HEIGHT * EPAL.DEPTH

    def put_box(self, new_box, pivot):
        fit = False
        valid_item_position = new_box.position
        new_box.position = pivot

        for rotation_type in cnst.RotationType.ALL:
            new_box.rotation_type = rotation_type
            box_dimension = new_box.get_dimension()

            if not self.is_inside(pivot, box_dimension):
                continue

            fit = True
            for box_in_container in self.boxes:
                if intersect(box_in_container, new_box):
                    fit = False
                    break

            if fit:
                self.boxes.append(new_box)
                return fit

        if not fit:
            new_box.position = valid_item_position

        return fit
        

        

        

