
##Important! You shouldn't use statistics library! ("import statistics" is not allowed)

import math
class MinHeap: #Please store and implement MinHeap data structure with an array
    def __init__(self):
        self.array = []
        self.size = 0
    def getSize(self):
        return self.size    
    def getLchild(self, index):
        return 2 * index + 1
    def getRchild(self, index):
        return 2 * index + 2
    def getparent(self, index):
        return (index - 1) // 2
    def hasLChild(self,index):
        return self.getLchild(index) < self.size
    def hasRChild(self,index):
        return self.getRchild(index) < self.size
    def hasParent(self,index):
        return self.getparent(index) >= 0
    def leftChild(self,index):
        return self.array[self.getLchild(index)]
    def rightChild(self,index):
        return self.array[self.getRchild(index)]
    def Parent(self,index):
        return self.array[self.getparent(index)]
    def swap(self,index1,index2):
        temp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = temp

    def insert(self, item): #insert new item
    ### TODO ### 
    ### input: a value ###
    ### You need not return or print anything with this function. ###
        self.array.append(item)
        self.size += 1
        self.heapifyUp(self.size - 1)
    def heapifyUp(self,index):
        if(self.hasParent(index) and self.Parent(index) > self.array[index]): 
            self.swap(index,self.getparent(index))
            self.heapifyUp(self.getparent(index))

    def peek(self):  #Find Minimum item
    #  non-leaf node cannot be the minimum element as its child node has a lower value.
        if self.size == 0:
            return
        else:
            return self.array[0]
    def removeMin(self):
    ### TODO ###
    ### You need not return or print anything with this function. ###
        if(self.size == 0):
            raise("Empty Heap")
        self.array[0] = self.array[self.size - 1]
        self.array.pop()
        self.size -= 1
        self.heapifyDown(0)
    def heapifyDown(self,index):
        smallest = index
        if(self.hasLChild(index) and self.array[smallest] > self.leftChild(index)):
            smallest = self.getLchild(index)
        if(self.hasRChild(index) and self.array[smallest] > self.rightChild(index)):
            smallest = self.getRchild(index)
        if(smallest != index):
            self.swap(index,smallest)
            self.heapifyDown(smallest)

    def showMinHeap(self):  #Show MinHeap with array
        return self.array

class MaxHeap: #Please store and implement MinHeap data structure with an array
    def __init__(self):
        self.array = []
        self.size = 0
    def getSize(self):
        return self.size
    def getLchild(self, index):
        return 2 * index + 1
    def getRchild(self, index):
        return 2 * index + 2
    def getparent(self, index):
        return (index - 1) // 2
    def hasLChild(self,index):
        return self.getLchild(index) < self.size
    def hasRChild(self,index):
        return self.getRchild(index) < self.size
    def hasParent(self,index):
        return self.getparent(index) >= 0
    def leftChild(self,index):
        return self.array[self.getLchild(index)]
    def rightChild(self,index):
        return self.array[self.getRchild(index)]
    def Parent(self,index):
        return self.array[self.getparent(index)]
    def swap(self,index1,index2):
        temp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = temp

    def insert(self, item): #insert new item
    ### TODO ###
    ### input: a value ###
    ### You need not return or print anything with this function. ###
        self.array.append(item)
        self.size += 1
        self.heapifyup(self.size - 1)
    def heapifyup(self,index):
        if(self.hasParent(index) and self.Parent(index) < self.array[index]): 
            self.swap(index,self.getparent(index))
            self.heapifyup(self.getparent(index))

    def peek(self):    #Find Maximum item
        if self.size == 0:
            return
        else:
            return self.array[0]
    def removeMax(self):   #Find Maximum item
    ### TODO ###
    ### You need not return or print anything with this function. ###
        if(self.size == 0):
            raise("Empty Heap")
        self.array[0] = self.array[self.size - 1]
        self.array.pop()
        self.size -= 1
        self.heapifyDown(0)
    def heapifyDown(self,index):
        largest = index
        if(self.hasLChild(index) and self.array[largest] < self.leftChild(index)):
            largest = self.getLchild(index)
        if(self.hasRChild(index) and self.array[largest] < self.rightChild(index)):
            largest = self.getRchild(index)
        if(largest != index):
            self.swap(index,largest)
            self.heapifyDown(largest)

    def showMaxHeap(self):   #Show MaxHeap with array
        return self.array

class FindMedian(): 
    def __init__(self):
    ### TODO ###
    ### Your own data structure. Implementing with heap structure is highly recommended. ###
        self.small = MaxHeap()
        self.large = MinHeap()
        self.median = 0

    def AddNewValues(self, NewValues):  # Add NewValues(a list of items) into your data structure
    ### TODO ### 
    ### input: a list of values ###
    ### You need not return or print anything with this function. ###
        for i in NewValues:
            if i <= self.median:
                self.small.insert(i)
            else:
                self.large.insert(i)
            if len(self.small.showMaxHeap()) - len(self.large.showMinHeap()) > 1:
                self.large.insert(self.small.showMaxHeap()[0])
                self.small.removeMax()
            elif len(self.large.showMinHeap()) - len(self.small.showMaxHeap()) > 1:
                self.small.insert(self.large.showMinHeap()[0])
                self.large.removeMin()


    def ShowMedian(self):  # Show Median of your data structure
    ### TODO ### 
    ### You need not print anything but "return Median". ###
        if len(self.small.showMaxHeap()) > len(self.large.showMinHeap()):
            self.median = self.small.showMaxHeap()[0]
        elif len(self.large.showMinHeap()) > len(self.small.showMaxHeap()):
            self.median = self.large.showMinHeap()[0]
        else:
            self.median = (self.small.showMaxHeap()[0] + self.large.showMinHeap()[0])/2
                
        return float(self.median)

    def RemoveMedian(self): # Remove median
    ### TODO ###
    ### You need not return or print anything with this function. ###
        if len(self.small.showMaxHeap()) > len(self.large.showMinHeap()):
            self.small.removeMax()
            return self.ShowMedian()
        elif len(self.small.showMaxHeap()) < len(self.large.showMinHeap()):
            self.large.removeMin()
            return self.ShowMedian()
