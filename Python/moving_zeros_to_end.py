def move_zeros(array):
    new_array =[]
    for k in array:    
        if k == 0:
            new_array.insert(len(new_array), k)
        else:
            new_array.append(k)
    return new_array

if __name__ == "__main__":
    _array = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
    print(move_zeros(_array))