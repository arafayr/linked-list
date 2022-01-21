#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.noofnodes = 0
        self.head = None
    def insert(self,data):
        
        #new node is the variable jis me object ka reference hai 
        newNode = Node(data)
        self.noofnodes = self.noofnodes+1
        
        if self.head is None:
            
            #THIS LINE MEANS self.head  = Node(data)
            
            
            #jo reference tha self.newNode me wo self.head me agya
            self.head = newNode
            
            
            
        else:
            
            
            
            
            #jo reference self.head me already tha wo age barh gya
            # #pichle wale ka reference matlab ke indirectly
            # self.next = Node(data)
            
            newNode.next = self.head
            
            
            
            #or phir self.head me jo reference tha us ko update kardia self.head me new reference dal dia
            
            self.head = newNode
            
            
           

            
    def insert_between_bydata(self, data, newdata):
        actualnode = self.head
        if actualnode.data == data:
            self.noofnodes = self.noofnodes+1
            
            newnode = Node(newdata)
            newnode.next = actualnode
            actualnode = newnode
        else:
            while actualnode.next and actualnode.data != data:
                prevnode = actualnode
                actualnode = actualnode.next


            if actualnode is not None:
                self.noofnodes = self.noofnodes+1
                newnode = Node(newdata)
                newnode.next = prevnode.next
                prevnode.next = newnode
            else:
                print("The node u r trying to target doesnot exist")

        
            
            
        
             
    def insert_end(self,data):
        self.noofnodes = self.noofnodes+1
        newnode = Node(data)
        actualnode = self.head
        while actualnode.next is not None:
            
            actualnode = actualnode.next
        
        actualnode = newnode
        
        
    def middle_node(self):
        totalnodes = self.noofnodes
        middle = totalnodes//2
        
        actualnode = self.head
        for i in range(middle):
                actualnode = actualnode.next
        print("Middle node is: ",actualnode.data) 
        
    def middlenode_mem_efficient(self):
        fasternode = self.head
        slowernode = self.head
        while fasternode.next and fasternode.next.next:
            fasternode = fasternode.next.next
            slowernode= slowernode.next
        print(slowernode.data)
    
    def reverse(self):
        
        currentnode = self.head
        prevnode= None
        nextnode = None
        
        while currentnode:
            
            
            nextnode = currentnode.next
            currentnode.next = prevnode
            prevnode = currentnode
            currentnode = nextnode
            
        self.head = prevnode
            
      
        
    def show(self):
        currentnode = self.head
        while currentnode:
            print(currentnode.data)
            #print(self.head.next)
            currentnode = currentnode.next
        #print(currentnode)
    
    def delete(self,data):
        
        thisnode = self.head
        if thisnode and thisnode.data == data :
            self.noofnodes = self.noofnodes-1
            
            self.head = thisnode.next
            thisnode = None
            
            
        previousnode = None
        
        while thisnode and thisnode.data != data:
            previousnode = thisnode
            thisnode = thisnode.next
            
        if thisnode == None:
            print("The node doesnt exist")
        else:
            self.noofnodes = self.noofnodes-1
            
            previousnode.next = thisnode.next
            thisnode = None
          
    def lenght(self):
        print(self.noofnodes)
        
        

obj = LinkedList()

obj.insert(1)
obj.insert(3)
obj.insert(4)




obj.insert_between_bydata(1,2)
obj.show()



print("---------------------------")

obj.reverse()
obj.show()


# In[ ]:




