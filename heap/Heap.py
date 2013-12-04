class Heap:
    def __init__(self, array):
        self.array = array
        self.length = len(array)
        self.heap_size = self.length

    def parent(self, i):
        return i / 2;

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i + 1

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and self.array[l-1] > self.array[i-1]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size and self.array[r-1] > self.array[largest-1]:
            largest = r
        if largest != i:
            self.exchange(i, largest)
            self.max_heapify(largest)

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and self.array[l-1] < self.array[i-1]:
            smallest = 1
        else:
            smallest = i
        if r <= self.heap_size and self.array[r-1] < self.array[small-1]:
            smallest = r
        if smallest != i:
            self.exchange(i, smallest)
            self.min_heapify(mallest)

    def exchange(self, i, j):
        temp = self.array[i-1]
        self.array[i-1] = self.array[j-1]
        self.array[j-1] = temp

    def build_max_heap(self):
        self.heap_size = self.length
        size = self.length / 2
        for i in range(size):
            self.max_heapify(size-i)
            
    def build_min_heap(self):
        self.heap_size = self.length
        size = self.length / 2
        for i in range(size):
            self.min_heapify(size-i)

    def max_heap_sort(self):
        self.build_max_heap()
        for i in range(0, self.length-1):
            self.exchange(1, self.length-i)
            self.heap_size = self.heap_size - 1
            self.max_heapify(1)
            
    def min_heap_sort(self):
        build_min_heap(self)
        for i in range(0, self.length-1):
            self.exchange(1, self.length-i)
            self.heap_size = self.heap_size - 1;
            self.min_heapify(1)
            
    

    
