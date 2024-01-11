from container.container import EPAL
import utilities.cnst as cnst


class Packer:
    def __init__(self):
        self.containers = [EPAL()]
        self.boxes = []

    def __repr__(self) -> str:
        return f"[PACKER]: {len(self.containers)=}, {len(self.boxes)=}"
        

    def _add_container(self):
        return self.containers.append(EPAL())

    def add_box(self, box):
        return self.boxes.append(box)
    
    def add_boxes(self, boxes):
        for box in boxes:
            self.add_box(box)

    def _remove_box(self, box):
        self.boxes.remove(box)

    def _pack2container(self, container, box):
        if container.is_empty():
            if container.put_box(box, cnst.START_POSITION):
                return True
            
            raise Exception(f"Empty container didn't put item, {container.id=}")

        for axis in cnst.Axis.ALL:       
            for con_box in container.boxes:
                pivot = cnst.START_POSITION
                w, h, d = con_box.get_dimension()

                if axis == cnst.Axis.WIDTH:
                    pivot = [con_box.position[0] + w, con_box.position[1], con_box.position[2]]
                elif axis == cnst.Axis.HEIGHT:
                    pivot = [con_box.position[0], con_box.position[1] + h, con_box.position[2]]
                elif axis == cnst.Axis.DEPTH:
                    pivot = [con_box.position[0], con_box.position[1], con_box.position[2] + d]

                if container.put_box(box, pivot):
                    return True
        return False
       
            
    def pack(self, bigger_first=True):
        self.boxes.sort( key=lambda item: item.get_volume(), reverse=bigger_first)

        while len(self.boxes) > 0:
            fitted = False
            for container in self.containers:
                for box in self.boxes:
                    if self._pack2container(container, box):
                        self._remove_box(box)
                        fitted = True
                

            if not fitted:
                self._add_container()
