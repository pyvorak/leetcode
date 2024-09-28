class MyCircularDeque:
    def __init__(self, k: int):
        self.max_size = k
        self.v = []

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.v = [value] + self.v
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.v.append(value)
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.v.pop(0)
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.v.pop()
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.v[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.v[-1]

    def isEmpty(self) -> bool:
        return len(self.v) == 0

    def isFull(self) -> bool:
        return len(self.v) == self.max_size
