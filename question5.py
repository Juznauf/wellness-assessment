"""
implement the reshape function of numpy.
Given an array A = (1,2,3...L), this is a 1D array.
Implement the reshape function to reshape this array into a multi dimensional array.
"""
import math

class threeD_array(object):

    def __init__(self,A,L1,L2,L3):
        """
        A is a 1D array, eg. A = (1,2,3,....L)
        L = L1*L2*L3

        index is from 1 to L
        """
        self.original_array = A
        self.ndim = 3
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3
        self.L = L1*L2*L3
        self.newArray = []
        counter = 0
        for _ in range(L1):
            temp1 = []
            for _ in range(L2):
                temp2 = []
                for k in range(L3):
                    temp2.append(A[counter+k])
                temp1.append(temp2)
                counter += L3
            self.newArray.append(temp1)


    def __repr__(self):
        return {'array':self.original_array, 'new_array':self.newArray}

        
    def get(self,x,y,z):
        """
        will get the value at x,y,z coordinate location
        """        
        return self.newArray[x-1][y-1][z-1]

    def index(self,x,y,z):
        """
        will give the corresponding index in of this element in A
        """
        return self.original_array.index(self.get(x,y,z),(x-1)*(y-1)*(z-1)) + 1

    def coordinates(self,index):
        """
        will give the x,y,z coordinate in this 3D array
        """

        # find x coord
        x = 1
        y = 1
        z = 1
        temp_index = index


        while temp_index > self.L2 * self.L3:
            temp_index -= (self.L2 * self.L3)
            x += 1

        while temp_index > self.L3:
            temp_index -= self.L3
            y += 1
        if temp_index > 0:
            z = temp_index
        return x,y,z

class fiveD_array(object):

    def __init__(self,A,L1,L2,L3,L4,L5):
        """
        A is a 1D array, eg. A = (1,2,3....L)
        L = L1*L2*L3*L4*L5
        """    
        self.original_array = A
        self.ndim = 3
        self.newArray = []
        counter = 0
        
        self.original_array = A
        self.ndim = 5
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3
        self.L4 = L4
        self.L5 = L5
        self.L = L1*L2*L3*L4*L5
        
        self.newArray = []
        
        counter = 0
        for _ in range(L1):
            temp1 = []
            for _ in range(L2):
                temp2 = []
                for _ in range(L3):
                    temp3 = []
                    for _ in range(L4):
                        temp4 = []
                        for n in range(L5):
                            temp4.append(A[counter+n])
                        temp3.append(temp4)
                        counter += L5
                    temp2.append(temp3)
                temp1.append(temp2)
            self.newArray.append(temp1)

    def __repr__(self):
        return {'array':self.original_array, 'new_array':self.newArray}

    def get(self,u,w,x,y,z):
        """
        will get the value at u,w,x,y,z coordinate location
        """
        return self.newArray[u-1][w-1][x-1][y-1][z-1]
        

    def index(self,u,w,x,y,z):
        """
        will give the corresponding index in of this element in A
        """
        return self.original_array.find(self.get(u,w,x,y,z), (u-1)*(w-1)*(x-1)*(y-1)*(z-1)) + 1


    def coordinates(self,index):
        """
        will give the u,w,x,y,z coordinates in this 5D array
        """
        u = 1
        w = 1
        x = 1
        y = 1
        z = 1

        temp_index = index

        while temp_index > (self.L2 * self.L3 * self.L4 * self.L5):
            temp_index -= (self.L2 * self.L3 * self.L4 * self.L5)
            u += 1

        while temp_index > (self.L3 * self.L4 * self.L5):
            temp_index -= (self.L3 * self.L4 * self.L5)
            w += 1
        
        while temp_index > (self.L4 * self.L5):
            temp_index -= (self.L4 * self.L5)
            x += 1

        while temp_index > self.L5:
            temp_index -= self.L5
            y += 1

        if temp_index > 0:
            z = temp_index

        return u,w,x,y,z
        

if __name__ == "__main__":
    # checker
    new3d = threeD_array(list(range(10000)),5,10,10000//(5*10))
    new5d = fiveD_array(list(range(10000)),3,4,2,20,10000//(5*4*2*20))
    index = 19
    x,y,z = new3d.coordinates(index)
    v3 = new3d.get(x,y,z)
    idx3 = new3d.index(x,y,z)
    print(x,y,z)
    print("index is {}".format(index))
    print("v3 is {}".format(v3))
    print("idx3 is {}".format(idx3))

    print("show that idx3 = index")
    print(idx3==index)

    print()

    u5,w5,x5,y5,z5 = new5d.coordinates(idx3)
    print(u5,w5,x5,y5,z5)
    print("index is {}".format(index))
    v5 = new5d.get(u5,w5,x5,y5,z5)
    print("v5 is {}".format(v5))
    print("show that v3 = v5")
    print(v3==v5)

