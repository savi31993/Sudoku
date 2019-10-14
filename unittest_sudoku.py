# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:45:06 2019

@author: Savithri K. B.
"""

import Sudoku

val = "1................................................................................"

def init_test():
    grid = Sudoku.Grid(val)
    
    assert(grid.grid[0][0] == "1")
    
    for i in range(1, 9):
        assert(grid.grid[0][i] == Sudoku.ALL_NUMS)
        
        for j in range(9):
            assert(grid.grid[i][j] == Sudoku.ALL_NUMS)
    #grid.display()
    print("__init__ test passed")

def neighbors_test():
    grid = Sudoku.Grid(val)
    
    grid.find_neighbors_of_elem(2, 1)
    
    neighbor_list = grid.neighbor_dict[(2, 1)]
    
    for i in range(9):
        if i == 1:
            continue
        
        assert((2, i) in neighbor_list)
    
    for i in range(9):
        if i == 2:
            continue
        
        assert((i, 1) in neighbor_list)
    
    assert((0, 0) in neighbor_list)
    assert((1, 0) in neighbor_list)
    assert((0, 2) in neighbor_list)
    assert((1, 2) in neighbor_list)
    
    assert((2, 1) not in neighbor_list)
    
    
    print("find_neighbors_of_elem test passed")

def remove_test():
    grid = Sudoku.Grid(val)
    
    grid.remove_elements_in_neighbors()
    
    assert(grid.grid[0][0] == "1")
    
    for i in range(1, 9):
        assert(grid.grid[0][i] == "23456789")
        assert(grid.grid[i][0] == "23456789")
    
    assert(grid.grid[1][1] == "23456789")
    assert(grid.grid[2][1] == "23456789")
    assert(grid.grid[1][2] == "23456789")
    assert(grid.grid[2][2] == "23456789")
    
    for i in range(1, 9):
        for j in range(3, 9):
            assert(grid.grid[i][j] == Sudoku.ALL_NUMS)
    
    for i in range(3, 9):
        assert(grid.grid[i][1] == Sudoku.ALL_NUMS)
        assert(grid.grid[i][2] == Sudoku.ALL_NUMS)
    
    print("remove_elements_in_neighbors test passed")
    
def place_test():
    grid = Sudoku.Grid(val)
    
    grid.remove_elements_in_neighbors()
    
    for i in range(1, len(grid.grid[0]) - 1):
        grid.grid[0][i] = grid.grid[0][i].replace('2', '')
    
    grid.place_element_with_no_other_option()
    
    assert(grid.grid[0][-1] == '2')
    
    print("place_element_with_no_other_option test passed")

init_test()
neighbors_test()
remove_test()
place_test()