# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:30:36 2019

@author: Savithri K. B.
"""

from copy import deepcopy

ALL_NUMS = "123456789"

class Grid:
    def __init__(self,num):
        self.grid = []
      
        for i in range(9):
            self.grid.append([])
        
        self.neighbor_dict = {}
        
        for i in range(9):
            for j in range(9):
                if num[i * 9 + j] == ".":
                    self.grid[i].append(ALL_NUMS)
                else:
                    self.grid[i].append(num[i * 9 + j])
                
                self.find_neighbors_of_elem(i, j)
        
    #The display method is used to show the grid   
    def display(self):
        for row in self.grid:
            for elem in row:
                print("{0: <9}".format(elem), end=" ")
            print("")

    #Takes a copy of old grid, calls the other methods remove_            
    def update(self):
        old_grid = self.get_copy()
        self.remove_elements_in_neighbors()
        
        while not old_grid.is_equal(self):
            old_grid = self.get_copy()
            self.remove_elements_in_neighbors()
            self.place_element_with_no_other_option()
    
    def remove_elements_in_neighbors(self):
        for i in range(len(self.grid)):
            row = self.grid[i]

            for j in range(len(row)):
                if len(row[j]) != 1:
                    continue
                
                neighbors = self.neighbor_dict[(i, j)]
                
                for neighbor in neighbors:
                    k = neighbor[0]
                    l = neighbor[1]
                    self.grid[k][l] = self.grid[k][l].replace(row[j], "")
    
    def place_element_with_no_other_option(self):
        for i in range(len(self.grid)):
            for num in ALL_NUMS:
                possible_places = []
                
                for j in range(len(self.grid[i])):
                    if num in self.grid[i][j]:
                        possible_places.append(j)
                
                if len(possible_places) == 1:
                    self.grid[i][possible_places[0]] = num
        
        for j in range(len(self.grid[0])):
            for num in ALL_NUMS:
                possible_places = []
                
                for i in range(len(self.grid)):
                    if num in self.grid[i][j]:
                        possible_places.append(i)
                
                if len(possible_places) == 1:
                    self.grid[possible_places[0]][j] = num

    def get_copy(self):
        return deepcopy(self)
    
    def is_equal(self, other):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != other.grid[i][j]:
                    return False
        
        return True
    
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

grid = Grid("4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......")
grid.update()
grid.display()