import array
class Stack:
    def __init__(self):
        self.mystack=array.array('i',[])
        self.top=-1
    
    def is_empty(self):
        if len(self.mystack):
            return False
        else:
            return True

    def display_details(self,task):
        print("Operation performed: ",task)
        print("Stack===>",self.mystack)
        print("Stack Top: ",self.top,"\n")

    def push(self,element):
        self.mystack.append(element)
        self.top=len(self.mystack)-1
        self.display_details("Push")

    def pop(self):
        if self.is_empty():
            print("There are no elemnets in stack to Pop/remove")
        else:
            self.mystack.pop()
            self.top=len(self.mystack)-1
            self.display_details("POP")

            
    
if __name__=='__main__':
    stack1=Stack()
    stack1.push(10)
    stack1.push(11)
    
    stack1.pop()
    stack1.push(14)
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    
                       



    