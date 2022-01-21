#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
        
class doublylinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.noofnodes = 0
    def insert_end(self,data):
        newnode = Node(data)
        if self.head == None:
            self.noofnodes +=1
            self.head = newnode
            self.tail = newnode
            
            
            
        else:
            self.noofnodes +=1
            newnode.previous = self.tail
            self.tail.next = newnode
            self.tail = newnode
            
    def show_forward(self):
        actualnode = self.head
        while actualnode is not None:
            print(actualnode.data)
            actualnode = actualnode.next
    def show_backward(self):
        actualnode = self.tail
        while actualnode is not None:
            print(actualnode.data)
            actualnode = actualnode.previous
        
            
            
            
obj = doublylinkedlist()
obj.insert_end("damn1")
obj.insert_end("damn2")
obj.insert_end("damn3")
obj.show_backward()
        


# In[ ]:




