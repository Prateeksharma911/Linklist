class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkList:
    def __init__(self):
        self.head=None
    def insertbegning(self,data):
        node=Node(data,self.head)
        self.head=node
    def insertend(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data)
        return

    def newlist(self,listdata):
        self.head=None
        self.head=Node(listdata[0])
        itr=self.head
        for i in range(1,len(listdata)):
            itr.next=Node(listdata[i])
            itr=itr.next
    
    def getlength(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        return count

    def removeat(self,index):
        if index<0 or index>=self.getlength():
            raise Exception("Invalid index")
        
        if index==0:
            self.head=self.head.next
            return
        
        count=0
        itr=self.head
        while itr.next:
            count+=1
            if count==index:
                itr.next=itr.next.next
                return
            itr=itr.next
    def insertat(self,point,value):
        count=0
        if point<0 or point>self.getlength():
            raise Exception("Invalid index")
        if point==0:
            self.insertbegning(value)
            return
        while itr:
            count+=1
            print("as")
            if count==point:
                node=Node(value)
                node.next=itr.next
                itr.next=node
                return




    def printlist(self):
        if self.head is None:
            print('Empty')
            return
        itr=self.head
        listr=''
        while itr:
            listr+=str(itr.data)+'-->'
            itr=itr.next
        print(listr)

if __name__ == '__main__':
    ll=LinkList()
    # ll.insertbegning([5,4,7,1,3,9])
    # ll.insertbegning(2)
    # ll.insertbegning(3)
    # ll.insertend(99)
    ll.newlist([5,4,7,1,3,9])
    ll.getlength()
    ll.printlist()
    # ll.removeat(2)
    ll.insertat(0,619)
    ll.printlist()