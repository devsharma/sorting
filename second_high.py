#!/usr/bin/python
import sys
if __name__ == '__main__':
  n = int(input('Length of array : ').strip())
  arr = input('Content of array : ').strip().split(" ")

  if len(arr) != n:
    print('Incorrect #no of content of array. Exiting')
    sys.exit(1)
  max = 0
  for i in range(0, n):
    max = i

    for j in range(i+1, n):
      if int(arr[max]) < int(arr[j]):
        max = j

    arr[i], arr[max] = arr[max], arr[i]
    sec = 0
    max = arr[0]
    for i in range(1, n):
        if arr[i] < max:
            sec = i
            break

  print(arr[sec])
