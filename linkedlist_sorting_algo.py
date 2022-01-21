#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0
        
        
    def add(self,value):
        newnode = node(value)
        if self.head == None:
            self.head = newnode
            self.size +=1
            #print("head ",self.size)
        else:
            prev = None
            curr = self.head
            while curr and curr.data < value:
                self.size +=1
                #print("looop ",self.size)
                prev = curr
                curr = curr.next
                
            if curr !=None:
                if prev == None:
                    newnode.next = self.head
                    self.head = newnode
                #temp = prev
                  #  print("rpev = none ",self.size)
                    self.size +=1
                else:
                    
                    newnode.next = curr
                    prev.next = newnode

                 #   print("middle",self.size)
                    self.size +=1
            elif curr == None:
                prev.next = newnode
                #print("last",self.size)
                self.size +=1
                
                
                
    def __contains__(self,data):
        cur = self.head
        
        while cur.next and cur.data != data:
            cur = cur.next
            
        print (cur.data == data)
    def remove(self,data):
        curr  = self.head
        if curr== None:
            return False
        
        else:
            if self.size == 1:
                
                
                self.head = None
                return 1
            elif curr.data == data:
                
                
                    
                    self.head = curr.next 
                    return 1
                    
                
            else:   
                prev = None
                curr = self.head
                
                while curr and curr.data != data:
                    prev = curr
                    curr = curr.next
                    
                if curr == None:
                    prev = None
                    return 1
                else:
                    prev.next = curr.next
                    return 1
            

    def removeallbeta(self,data):
        curr  = self.head
        if curr== None:
            return False
        
        else:
            if self.size == 1:
                
                
                self.head = None
                return 1
            elif curr.data == data:
                
                
                    while curr.data == data:
                        curr = curr.next
                        
                    self.head = curr
                    return 1
                    
                
            else:   
                prev = None
                curr = self.head
                count = 0
                actuallast = None
                actual = None
                while curr:
                    
                    
                    if curr.data == data:
                        if count == 0:
                            #actualprev = curr
                   #         print("prev ",prev.data)
                            actual = prev
                            count+=1
                        actuallast = curr
                        
                        #if curr.data != data:
                            
                    prev = curr
                    curr = curr.next
                    
                if curr == None and actuallast == None:
                    #print("hola")
                    #print("actual", actual.data)
                    actual.next = None
                    curr = None
                    return 1
                
                
                else:
                    
                     #   print("hello")
                        actual.next = actuallast.next
                        return 1
            

                
    def traverse(self):
        curr = self.head
        
        while curr:
            print(curr.data)
            curr=curr.next
                
                
obj = linkedlist()
obj.add(3)
obj.add(2)
obj.add(2)
obj.add(2)
obj.add(2)
obj.add(2)
obj.add(2)
obj.add(1)
obj.add(1)
obj.add(5)
obj.add(30)
obj.add(30)
obj.add(4)
obj.add(5)
obj.traverse()

print("---------------------------------------")

obj.removeallbeta(2)
obj.traverse()
            

