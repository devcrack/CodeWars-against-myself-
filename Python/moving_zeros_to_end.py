"""
Instructions:
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


#Clever solution 
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

# My solution 
def move_zeros(array):    
    zeros = [k for k in array if not k]
    array = [k for k in array if k]
    array += zeros    

    return array

if __name__ == "__main__":
    _array = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
    print(move_zeros(_array))

    
