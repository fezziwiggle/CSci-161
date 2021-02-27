'''
Maezy Haldeman: maezy.haldeman@und.edu
CS 161: CompSci II
Lab 5a
ID#: 1325352

This program tests all the functionality of the class Priority Queue by enqueuing and dequeuing
both valid and invalid arguments. 

'''

from PriorityQueue import *

def main():
    
    queue1 = PriorityQueue(5) #testing a queue of size 5
    
    print('Max size of queue:', queue1.maxSize())

    print()
    
    try:
        queue1.enqueue('a', 90) #expand these tests, don't miss anything
        queue1.enqueue('b', 100)
        queue1.enqueue('c', 100)
        queue1.enqueue('d')
        queue1.enqueue('e', 50)
        queue1.enqueue('f', 80) #should raise exception, can't add to a full queue
        
    except PriorityQueueException as e:
        print('Caught an enqueue error')
    except Exception as e:
        print('Error from something other than PriorityQueue')
        
    print()
    
    print('Items in queue (priority order)', queue1)
    
    print()
    
    print('Is the queue full?', queue1.isFull())
    print('Is the queue empty?', queue1.isEmpty())  
    
    print()
    
    try:
        while not queue1.isEmpty():
            temp1 = queue1.dequeue()
            print('Dequeuing', temp1)
    except PriorityQueueException as e:
        print('Caught a dequeue error')
    except Exception as e:
        print('Error from something other than PriorityQueue')
        
    print()
        
    print('Items in queue (priority order)', queue1)
    
    print()
    
    print('Is the queue full?', queue1.isFull())
    print('Is the queue empty?', queue1.isEmpty())
    
    
    
    queue2 = PriorityQueue() #testing queue with default size 100
    
    print('Max size of queue:', queue2.maxSize())

    print()
    
    try:
        queue2.enqueue('a', 100) #expand these tests, don't miss anything
        queue2.enqueue('b', 90)
        queue2.enqueue('c', 100)
        queue2.enqueue('d')
        queue2.enqueue('e', 50)
        queue2.enqueue('f', 80)
        queue2.enqueue('g', 60)
        queue2.enqueue('h', 70)
        queue2.enqueue('i', 30)
        queue2.enqueue('j', 40)
        queue2.enqueue('k', 20)
        queue2.enqueue('l', 10)
        queue2.enqueue('m', 0) #should raise exception, 0 outside of priority range
        
    except PriorityQueueException as e:
        print('Caught an enqueue error')
    except Exception as e:
        print('Error from something other than PriorityQueue')
        
    print()
    
    print('Items in queue (priority order)', queue2)
    
    print()
    
    print('Is the queue full?', queue2.isFull())
    print('Is the queue empty?', queue2.isEmpty())  
    
    print()
    
    try:
        while not queue2.isEmpty():
            temp2 = queue2.dequeue()
            print('Dequeuing', temp2)
        queue2.dequeue() #should raise an error, can't dequeue from an empty queue
    except PriorityQueueException as e:
        print('Caught a dequeue error')
    except Exception as e:
        print('Error from something other than PriorityQueue')
        
    print()
        
    print('Items in queue (priority order)', queue2)
    
    print()
    
    print('Is the queue full?', queue2.isFull())
    print('Is the queue empty?', queue2.isEmpty())    
    
    
main()