"""
Algorithm design
Date - 11/02/2017
Topic - Calculate power
"""

import os
import sys
import cv2
import numpy as np
import ast

def help_message():
  print("Calculate a power n")
  print("Usage: [method] [a] [n]")
  print("[method]   - 1 - perform a naive multiplication")
  print("[a] - base \"a\"")
  print("[n] - power \"n\"")
  print("Example usages: " + sys.argv[0] + " 1 " + "[a] " + "[n]")
   
"""
===================================================
=============== direct multiplication =============
===================================================
Time complexity - O(n)
Space complexity - O(1)
"""
def direct_multiplication(a, n):
  out = 1
  for i in range(n):
    if a < 0:
      out = out / a
    else:
      out = out * a
  return out

"""
===================================================
============== recursive multiplication ===========
===================================================
Time complexity - O(n)
Space complexity - O(1)
Divide and conquer
"""
def recursive_method(a, n):
  if n == 0:
    return 1
  elif n%2 == 0:
    return recursive_method(a, n/2) * recursive_method(a, n/2)
  else:
    if a < 0:
      return recursive_method(a, n/2) * recursive_method(a, n/2) / a
    else:
      return recursive_method(a, n/2) * recursive_method(a, n/2) * a

"""
===================================================
======= optimized recursive multiplication ========
===================================================
Time complexity - O(logn)
Space complexity - O(1)
Divide and conquer
"""
def optimized_recursive_method(a, n):
  if n == 0:
    return 1
  temp = recursive_method(a, n/2)
  if n%2 == 0:
    return temp * temp
  else:
    if a < 0:
      return temp * temp / a
    else:
      return temp * temp * a


if __name__ == '__main__':
  which_method = -1

  # Validate the input arguments
  if (len(sys.argv) != 4):
    help_message()
    sys.exit()
  else:
    which_method = int(sys.argv[1])
    a = float(sys.argv[2])
    n = int(sys.argv[3])

  function_launch = {
  1 : direct_multiplication,
  2 : recursive_method,
  3 : optimized_recursive_method,
  }

  # Call the function
  output = function_launch[which_method](a, n)
  print "Output -", a, "power", n, "is", output
 