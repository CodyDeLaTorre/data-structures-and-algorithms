def mergesort(arr):
    n = len(arr)

    if n > 1:
      mid = n//2
      left = arr[:mid]
      right = arr[mid:]
      # // sort the left side
      mergesort(left)
      # // sort the right side
      mergesort(right)
      # // merge the sorted left an right sides together
      merge(left, right, arr)
    return arr

def merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
          arr[k] = left[i]
          i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1

        k = k + 1

    if i == len(left):
       # set remaining entries in arr to remaining values in right
      arr[k:] = right[j:]
    else:
       # set remaining entries in arr to remaining values in left
      arr[k:] = left[i:]
    return arr

new_list = [8,4,23,42,16,15]

print(mergesort(new_list))
