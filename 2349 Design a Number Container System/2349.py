class NumberContainers:
    def __init__(self):
        self.idx = {}
        self.num = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.idx[index] = number
        heappush(self.num[number], index)

    def find(self, number: int) -> int:
        while self.num[number] and self.idx[self.num[number][0]] != number:
            heappop(self.num[number])

        if self.num[number]:
            return self.num[number][0]
        else:
            return -1
