"""
Algorithm design
Date - 11/12/2017
Topic - Binary search
"""

import os
import sys
import cv2
import numpy as np
import ast

# Only works for sorted arrays in ascending order

# Iterative method
def binary_search_iterative(input_array, value):
  left = 0
  right = len(input_array) - 1
  while left <= right:
    mid = (left + right)/2
    print "mid value", left, right, mid
    if value == input_array[mid]:
      return mid
    elif value < input_array[mid]:
      right = mid - 1
    else:
      left = mid + 1
  return -1

# Recursive method
def bs_recursive(input_array, left, right, value):
  if left > right:
    return -1

  mid = (left + right)/2
  print "mid value", left, right, mid
  if value == input_array[mid]:
    return mid
  elif value < input_array[mid]:
    return bs_recursive(input_array, left, mid-1, value)
  else:
    return bs_recursive(input_array, mid+1, right, value)

def binary_search_recursive(input_array, value):
  index = bs_recursive(input_array, 0, len(input_array)-1, value)
  return index

if __name__ == '__main__':
  value = 8
  input_array = [1,2,3,4,5,6,8]
  index = binary_search_iterative(input_array, value)
  print "Iterative index found", index, "value", input_array[index]
  index = binary_search_recursive(input_array, value)
  print "Recursive index found", index, "value", input_array[index]