"""
Algorithm design
Date - 11/01/2017
Topic - Insertion sort
"""

import os
import sys
import cv2
import numpy as np
import ast

def help_message():
  print("Usage: ")
  print("[sorting algorithm]")
  print("1 - Insertion sort")
  print("2 - Selection sort")
  print("[input array]")
  print("Pass an input array to sort")
  print("Example usages: " + sys.argv[0] + " 1 " + "\"[3,4,2,1]\"")
   
def swap(input_array, i, j):
  temp = input_array[i]
  input_array[i] = input_array[j]
  input_array[j] = temp
  return input_array

#https://stackoverflow.com/questions/15799034/insertion-sort-vs-selection-sort
"""
===================================================
======== Sorting algorithm : Insertion sort =======
===================================================
Time complexity - O(n^2)
If the list is almost sorted, it takes O(n)
"""
def insertion_sort(input_array):
  for i in range(len(input_array)):
    j = i
    while j > 0 and input_array[j] < input_array[j-1]:
      swap(input_array, j, j-1)
    j = j -1
  return input_array

"""
===================================================
======== Sorting algorithm : Selection sort =======
===================================================
Time complexity - O(n^2)
"""
def selection_sort(input_array):
  for i in range(len(input_array)):
    index_min_value = i
    found_any_min_value = False
    for j in range(i+1, len(input_array)):
      if input_array[index_min_value] > input_array[j]:
        index_min_value = j
        found_any_min_value = True

    if found_any_min_value:
      swap(input_array, i, index_min_value)

  return input_array

if __name__ == '__main__':
  which_sort = -1
   
  # Validate the input arguments
  if (len(sys.argv) != 3):
    help_message()
    sys.exit()
  else:
    which_sort = int(sys.argv[1])
    input_array = sys.argv[2]

  function_launch = {
  1 : insertion_sort,
  2 : selection_sort,
  }

  # Call the function
  input_array = ast.literal_eval(input_array)
  print "Input array", input_array
  output = function_launch[which_sort](input_array)
  print "Sorted array", output
 