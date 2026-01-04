import numpy as np 
from numpy import random
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])


print(f"the element in the third row and first column:{arr[2,0]}")
print("="*50)


print(f"Elements in the second column:{arr[0,1]} {arr[1,1]} {arr[2,1]}")
print("="*50)


print( f"data type of array element:{arr.dtype} ")
print("="*50)


new_arr=arr.copy()
new_arr[0,0]=100
if new_arr.base==None:
    print("the original array not affected \n")
else:
    print("the original array affected \n")
print("="*50)

new_arr2=arr.view()
new_arr2[0,0]=100
if new_arr2.base.all()!=arr.all():
    print("the original array not affected \n")
else:
    print("the original array affected \n")
print("="*50)

print(f"the shape of the array is:{arr.shape}")
print("="*50)

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
for x in range(len(arr)):
    for y in range(len(arr)):
        print(f"the element in the row number ({x}) and column number ({y}) is:{arr[x,y]}")
print("="*50)

print("joining 2 arrays virtically:")
v_arr=[[100,110,120],[130,140,150],[160,170,180]]
virtical_array=np.vstack((arr,v_arr))
print(virtical_array)
print("\n")
print("joining 2 arrays horizontally:")
h_arr=[[100,110,120],[130,140,150],[160,170,180]]
horizontal_array=np.hstack((arr,h_arr))
print(horizontal_array)
print("="*50)

col_split=np.hsplit(arr,3)
print(f"array after split by column (horizontally):\nthe first arry :\n{col_split[0]}\nthe second array:\n{col_split[1]}\nthe third array:\n{col_split[2]}") 
print("="*50)

search_for_60=np.where(arr==60)
print(f"the element 60 is in position:{search_for_60}")
print("="*50)

row1_sort_ascending= np.sort(arr[0])
print(f"row number 1 sorted ascending:{row1_sort_ascending}")
row2_sort_ascending=np.sort(arr[1])
print(f"row number 2 sorted ascending:{row2_sort_ascending}")
row3_sort_ascending=np.sort(arr[2])
print(f"row number 3 sorted ascending:{row3_sort_ascending}")
print("="*50)

greater=arr>50
new_array=arr[greater]
print(f"new array with element greater than 50:{new_array}")
print("="*50)

rand_array = random.randint(100, size=(2, 3))
print(f"array with random entries:\n{rand_array}")
print("="*50)

sqrt_array=np.sqrt(arr)
print(f"sqrt array:{sqrt_array}")



