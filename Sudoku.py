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
        
        self.neighbor_dict = {}
        
        for i in range(9):
            for j in range(9):
                if num[ i * 9 + j] == ".":
                    self.grid[i].append("123456789")
                else:
                    self.grid[i].append(num[ i * 9 + j])
                
                self.find_neighbors_of_elem(i, j)
        
    
    def display(self):
        for row in self.grid:
            for elem in row:
                print("{0: <9}".format(elem), end=" ")
            print("")
    
    def get_copy(self):
        return deepcopy(self)
    
    def find_neighbors_of_elem(self, i, j):
        elem = (i, j)

        list_tuple = []
        for k in range(0,9):
            list_tuple.append((i, k))
            list_tuple.append((k, j))

        square_neighbors = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]

        rows_in_square = square_neighbors[i // 3]
        cols_in_square = square_neighbors[j // 3]

        for row in rows_in_square:
            for col in cols_in_square:
                list_tuple.append((row, col))

        list_tuple = list(set(list_tuple))
        list_tuple.remove(elem)

        self.neighbor_dict[elem] = list_tuple

grid = Grid(".2.4...7..145.832..75.23.9..5281.................4758..6.38.95..396.281..4...1.3.")
grid.display()
