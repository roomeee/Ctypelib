import ctypes


class MyList:
    def __init__(self):
        self.size = 1  # maximum items to be stored
        self.n = 0  # item stored
        #  Create a c type array with size
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __str__(self):
        result= ''
        for i in range(self.n):
            result= result + str(self.A[i])+ ','

        return '['+result[:-1] +']'

    def __getitem__(self, index):
        if 0<= index <self.n:
            return self.A[index]
        else:
            return 'Index out of range'


    def __make_array(self, capacity):
        # static array which is referential array
        return (capacity * ctypes.py_object)()

    def append(self, item):
        if self.n== self.size:
            self.__resize(self.size*2)

        self.A[self.n]= item
        self.n= self.n+1

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        self.size= new_capacity
        for i in range(self.n):
            B[i]= self.A[i]
        self.A=B

    def pop




L = MyList()
L.append('hell0')
L.append(100)
L.append(3.4)
L.append(True)
print(len(L))
print(L)
print(L[2])
