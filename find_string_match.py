"""
Algorithm design
Date - 11/01/2017
Topic - String matching
"""

import os
import sys
import cv2
import numpy as np
import ast

def help_message():
  print("Find string_p in string_s")
  print("Usage: [method] [string_p] [string_s]")
  print("[method]   - 1 - perform a naive search")
  print("[string_p] - input string")
  print("[string_s] - sentence")
  print("Example usages: " + sys.argv[0] + " 1 " + "\"naveen\"" + " \"my name is naveen\"")
   
"""
===================================================
============= String matching algorithm ===========
===================================================
Time complexity - O(mn)
"""
def naive_search(string_p, string_s):
  for i in range(len(string_s) - len(string_p) + 1):
    j = 0
    while j < len(string_p) and string_s[i+j] == string_p[j]:
      j = j + 1
    if j == len(string_p):
      return i
  return 0

if __name__ == '__main__':
  which_method = -1

  # Validate the input arguments
  if (len(sys.argv) != 4):
    help_message()
    sys.exit()
  else:
    which_method = int(sys.argv[1])
    string_p = sys.argv[2]
    string_s = sys.argv[3]

  function_launch = {
  1 : naive_search,
  }

  # Call the function
  print "string_p - ", string_p
  print "string_s - ", string_s
  output = function_launch[which_method](string_p, string_s)
  print "found match at index (starting from 0)", output
 