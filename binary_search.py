def binary_oxtarish(list, item):
    low = 0 
    high = len(list)-1

    while low <= high:
        mid = (low+high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high =mid -1
        else:
            high = mid +1
    return None

mani_listm = [1,3,4,6,7,9,10,15,20]

print(binary_oxtarish(mani_listm, 20))
print(binary_oxtarish(mani_listm, 4))
print(binary_oxtarish(mani_listm, -1))
print(binary_oxtarish(mani_listm, 7))
print(binary_oxtarish(mani_listm, 9))
    