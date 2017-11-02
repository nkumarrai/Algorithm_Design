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
================ Calculate a power n ==============
===================================================
Time complexity - O(mn) ??
"""
def direct_multiplication(a, n):
  out = 1
  for i in range(n):
    out = out * a
  return out

def advanced_multiplication(a, n):
  pass

if __name__ == '__main__':
  which_method = -1

  # Validate the input arguments
  if (len(sys.argv) != 4):
    help_message()
    sys.exit()
  else:
    which_method = int(sys.argv[1])
    a = int(sys.argv[2])
    n = int(sys.argv[3])

  function_launch = {
  1 : direct_multiplication,
  2 : advanced_multiplication,
  }

  # Call the function
  output = function_launch[which_method](a, n)
  print "Output -", a, "power", n, "is", output
 