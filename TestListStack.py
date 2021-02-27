from LimitedStack import *

def main():
   stack = LimitedStack (5)
   stack.push ("a")
   stack.push ("b")
   stack.push ("c")
   print ("Top item ", stack.peek())
   print (stack)
   
   stack.push ("d")
   print (stack)

   stack.push ("e")
   while not stack.isEmpty():
      print (stack.peek())
      stack.top()
      print (stack)
   
   stack.push ("a")
   stack.push ("b")
   stack.push ("c")
   stack.push ("d")
   stack.push ("e")
   stack.push ("f")


   print ("Is the stack full? ", stack.isFull() )      
   print ("Is the stack empty? ", stack.isEmpty() )      
   while not stack.isEmpty():
      print (stack.peek(), end = ' ' )
      stack.top()
   print ()   

   print ("Is the stack full? ", stack.isFull() )      
   print ("Is the stack empty? ", stack.isEmpty() )      
      
      
      
   
   
   

main()   