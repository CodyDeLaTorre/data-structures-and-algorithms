def insertion(list):
  if list is None:
    return []
  for i in range(1, len(list)):
    j = i -1
    temp = list[i]
    while j >= 0 and temp < list[j]:
      list[j + 1] = list[j]
      j = j - 1
    list[j + 1] = temp
  return list
