def findSmallest(arr):
    smallest = arr[0] # 가장 작은 정수를 저장
    smallest_index = 0 # 가장 작은 정수의 인덱스를 저장
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallext = arr[i]
    return smallest_index

def selectionSort(arr): # 배열을 정렬
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr) # 배열에서 가장 작은 정수를 찾아서
        newArr.append(arr.pop(smallest)) # 새로운 배열에 추가
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
