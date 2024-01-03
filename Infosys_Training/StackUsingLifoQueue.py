# Stack implementation using queue module 

from queue import LifoQueue 

# Initializing a stack 
stack = LifoQueue(maxsize = 10) 

# qsize() give the maxsize of the stack 
print(stack.qsize()) 

# put() function to push  
stack.put('a') 
stack.put('b') 
stack.put('c') 

print("Full: ", stack.full()) 
print("Size: ", stack.qsize()) 

# get() fucntion to pop in LIFO order 
print('\nElements poped from the stack') 
print(stack.get()) 
print(stack.get()) 
print(stack.get()) 

print("\nEmpty: ", stack.empty())