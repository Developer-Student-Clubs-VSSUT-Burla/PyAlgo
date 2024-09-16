class dQueue:
    def __init__(self):
        self.d_queue = []
    def is_empty(self):
        return len(self.d_queue) == 0
    def add_at_front(self , item):
        self.d_queue.insert(0 , item)
    def add_at_rear(self, item):
        self.d_queue.append(item)
    def del_at_front(self):
        self.d_queue.pop(0)
    def del_at_rear(self):
        self.d_queue.pop()
    def size(self):
        return len(self.d_queue)

# """  d-queue = front-> [2,3,4,5,6,6,8] <- rear
# front at 0
# rear at 6
#  """                        