from utilities import cnst     

class Box():
    def __init__(self, id, depth, width, height):
        self.id = id
        self.width = width
        self.height = height
        self.depth = depth

        self.rotation_type = cnst.RotationType.RT_WHD
        self.position = cnst.START_POSITION

    def __repr__(self):
        return f"[BOX]: {self.id=}, {self.position=}, {self.width=}, {self.depth=}, {self.height=}"

    def get_volume(self):
        return self.width * self.height * self.depth

    def get_dimension(self):
        dimension = ()

        if self.rotation_type == cnst.RotationType.RT_WHD:
            dimension = (self.width, self.height, self.depth)
        elif self.rotation_type == cnst.RotationType.RT_HWD:
            dimension = (self.height, self.width, self.depth)
        elif self.rotation_type == cnst.RotationType.RT_HDW:
            dimension = (self.height, self.depth, self.width)
        elif self.rotation_type == cnst.RotationType.RT_DHW:
            dimension = (self.depth, self.height, self.width)
        elif self.rotation_type == cnst.RotationType.RT_DWH:
            dimension = (self.depth, self.width, self.height)
        elif self.rotation_type == cnst.RotationType.RT_WDH:
            dimension = (self.width, self.depth, self.height)
            
        return dimension