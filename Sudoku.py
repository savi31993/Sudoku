# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:30:36 2019

@author: Savithri K. B.
"""

from copy import deepcopy

class Grid:
    def __init__(self,num):
        self.grid = []
      
        for i in range(9):
            self.grid.append([])
      
        for i in range(9):
            for j in range(9):
                if num[ i * 9 + j] == ".":
                    self.grid[i].append("123456789")
                else:
                    self.grid[i].append(num[ i * 9 + j])
    
    def display(self):
        for row in self.grid:
            for elem in row:
                print("{0: <9}".format(elem), end=" ")
            print("")
    
    def get_copy(self):
        return deepcopy(self)

grid = Grid(".2.4...7..145.832..75.23.9..5281.................4758..6.38.95..396.281..4...1.3.")
grid.display()