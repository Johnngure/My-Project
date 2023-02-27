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

f __name__ == "__main__" :
    stack_obj = MyStack()
    print("is_empty(): " + str(stack_obj.is_empty()))
    print("peek(): " + str(stack_obj.peek()))
    print("size(): " + str(stack_obj.size()))