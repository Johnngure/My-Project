def delete(self, val):
    if val < self.val:  # val is in the left subtree
        pass
    elif val > self.val:  # val is in the right subtree
        pass
    else:  # val was found
        if self.righchild  and self.leftchild is None:
            self = None
            return None
        elif self.leftchild is None:
            tmp = self.rightchild
            self = None
            return tmp
        else:
            current = self.rightchild
            # loop down to find the leftmost leaf
            while (current.leftchild is not None):
                current = current.leftchild
                self.val = current.val
                self.rightchild = self.rightchild.delete(current.val)

return self


