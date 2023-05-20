from queue1 import Queue1


queuelist1 = Queue1()

closinglist = [")", "]",  "}"]
openinglist = ["(", "[", "{"] 


def split1(value):
   
    for i in value:
      if i != " ":
         queuelist1.enqueue(i)
      else: 
         continue
    

split1("{}()(){}")
print(queuelist1)


def validate_brackets():
    temp = queuelist1.linkedlist.head 
    current =queuelist1.linkedlist.head 

    if  current.value== closinglist[0] or closinglist[1] or closinglist[2] :

        return False
    else:
          
   
        while current is not None:
                
            if current.value == openinglist[0] or openinglist[1] or openinglist[2] :
            
                if current.next.value == closinglist[0] or closinglist[1] or closinglist[2]:
                        print(queuelist1.peek())
                        print(queuelist1.dequeue())
                        queuelist1.dequeue()
                        # print(queuelist1.peek())
                        current= temp

                else:
                    current = current.next

    if queuelist1.isEmpty():
        return True
    else:
        return False
        
print(validate_brackets())
print(queuelist1)




       
       
   

