class mystack:
    def __init__(self):
        self.stack_list =  []

    def  is_empty(self):
        return self.stack_size = 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size
