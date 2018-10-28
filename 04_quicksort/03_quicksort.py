def quicksort(array):
    if len(array) < 2:
        return array # base case. 원소의 개수가 0 또는 1이면 이미 정렬된 상태
    else:
        pivot = array[0] # recursive case
        less = [i for i in array[1:] if i <= pivot] # 기준 원소보다 작거나 모든 원소로 이루어진 하위 배열
        greater = [i for i in array[1:] if i > pivot] # 기준 원소보다 큰 모든 원소로 이루어진 하위 배열
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))
