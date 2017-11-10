"""
Algorithm design
Date - 11/05/2017
Topic - Linked list
"""

import os
import sys
import cv2
import numpy as np
import ast

def help_message():
  print("create a linked list for numbers")
  print("Usage: [which_method]")
  print("1 - singly_linked_list")
  print("Example usages: " + sys.argv[0] + " 1")

class Node():
  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node

  def get_data(self):
    return self.data

  def get_next(self):
    return self.next_node

  def set_next(self, next_node=None):
    self.next_node = next_node

class SinglyLinkedList():
  def __init__(self):
    self.head = None
    self.last = None

  def fix_last_pointer(self):
    if self.last != None:
      while self.last.get_next() != None:
        self.last = self.last.get_next()
    else:
      current = self.head
      previous = None
      while current:
        previous = current
        current = current.get_next()

      self.last = previous
    return True

  def insertAtFirst(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.last = new_node
    else:
      new_node.set_next(self.head)
      self.head = new_node 

    self.fix_last_pointer()

  def insertAtLast(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.last = new_node
    else:
      self.last.set_next(new_node)
      self.last = new_node

    self.fix_last_pointer()

  def insertAtIndex(self, value, index):
    sz = self.size()
    if index > sz:
      print "insertAtIndex: Index is out of bounds"
      return
    elif index == 0:
      self.insertAtFirst(value)
      return
    elif index == sz:
      self.insertAtLast(value)
      return

    previous = None
    current = self.head
    while index != 0:
      previous = current
      current = current.get_next()
      index -= 1

    new_node = Node(value)
    previous.set_next(new_node)
    new_node.set_next(current)
    return True

  def insert_sorted(self, value):
    sz = self.size()
    ret, order = self.is_sorted()
    if ret == False and sz > 0:
      print "cannot insert, list is not sorted"
      return False
    
    if sz == 0:
      new_node = Node(value)
      self.head = new_node
    elif order == 'ascending':
      new_node = Node(value)
      current = self.head
      previous = None
      while current and value > current.get_data():
        previous = current
        current = current.get_next()

      if previous == None:
        self.head = new_node
        new_node.set_next(current)
      else:
        previous.set_next(new_node)
        new_node.set_next(current)
    elif order == 'descending':
      new_node = Node(value)
      current = self.head
      previous = None
      while current and value < current.get_data():
        previous = current
        current = current.get_next()

      if previous == None:
        self.head = new_node
        new_node.set_next(current)
      else:
        previous.set_next(new_node)


    self.fix_last_pointer()

    return True

  def is_sorted(self):
    ret = self.is_sorted_ascending()
    if ret == False:
      ret = self.is_sorted_descending()
      return ret, 'descending'
    else:
      return ret, 'ascending'

  def is_sorted_descending(self):
    sz = self.size()
    if sz == 1:
      print "List is sorted in ascending order"
      return True
    elif sz == 0:
      print "List is empty"
      return False

    current = self.head
    while current and current.get_next():
      if current.get_data() < (current.get_next()).get_data():
        print "List is not sorted in ascending order"
        return False
      current = current.get_next()

    print "This List is sorted in ascending order"
    return True

  def is_sorted_ascending(self):
    sz = self.size()
    if sz == 1:
      print "List is sorted in ascending order"
      return True
    elif sz == 0:
      print "List is empty"
      return False

    current = self.head
    while current and current.get_next():
      if current.get_data() > (current.get_next()).get_data():
        print "List is not sorted in ascending order"
        return False
      current = current.get_next()

    print "This List is sorted in ascending order"
    return True

  def find(self, value):
    current = self.head
    while current:
      if current.get_data() == value:
        return True
      else:
        current = current.get_next()

    print "Find failed :", "value ", value, " is not present"
    return False

  def remove(self, value):
    previous = None
    current = self.head
    while current:
      if current.get_data() == value:
        if previous == None:
          self.head = current.get_next()
          del current
          return True
        else:
          previous.set_next(current.get_next())
          del current
          return True
      else:
        previous = current
        current = current.get_next()

    print "Find failed :", "value ", value, " is not present"
    return False

  def sort(self):
    pass

  def size(self):
    current = self.head
    #print "ids of current and head", id(current), id(self.head)
    count = 0
    while current:
      count = count + 1
      current = current.get_next()
      #print "ids of current and head", id(current), id(self.head)
    return count

  def print_elements(self):
    current = self.head
    print "Elements of Singly linked list\t",
    while current:
      print current.get_data(), " ->",
      current = current.get_next()
    print "NULL"

    if self.head != None and self.last != None:
      print "first and last elements are", self.head.get_data(), self.last.get_data()

  def delete_list(self):
    current = self.head
    previous = None
    while current:
      previous = current
      current = current.get_next()
      self.head = current
      print "deleted value", previous.get_data()
      del previous

    self.head = None
    self.last = None
    return True
   
def singly_linked_list():
  linked_list = SinglyLinkedList()
  linked_list.insertAtFirst(1)
  linked_list.insertAtFirst(2)
  linked_list.insertAtFirst(3)
  linked_list.insertAtLast(4)
  linked_list.insertAtLast(5)
  linked_list.print_elements()
  linked_list.insertAtIndex(6, 0)
  linked_list.print_elements()
  linked_list.insertAtIndex(7, 6)
  linked_list.print_elements()
  linked_list.insertAtIndex(8, 4)
  linked_list.print_elements()
  linked_list.remove(2)
  linked_list.print_elements()
  linked_list.find(10)
  linked_list.print_elements()
  linked_list.is_sorted()
  linked_list.delete_list()
  linked_list.print_elements()

  linked_list.insert_sorted(8)
  linked_list.insert_sorted(4)
  linked_list.insert_sorted(9)
  linked_list.insert_sorted(3)
  linked_list.insert_sorted(6)
  linked_list.print_elements()

if __name__ == '__main__':
  which_method = -1

  # Validate the input arguments
  if (len(sys.argv) != 2):
    help_message()
    sys.exit()
  else:
    which_method = int(sys.argv[1])

  function_launch = {
  1 : singly_linked_list,
  }

  # Call the function
  output = function_launch[which_method]()
 