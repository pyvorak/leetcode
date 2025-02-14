class ProductOfNumbers:
    def __init__(self):
        self.s = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.s = [1]
        else:
            self.s.append(self.s[-1]*num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.s):
            return 0
        else: 
            return self.s[-1] // self.s[-k-1]
