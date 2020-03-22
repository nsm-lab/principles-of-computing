# unit tests for Mini-project 7 (The Fifteen Puzzle), by k., 08/02/2014

import unittest
from mini_project7 import Puzzle


class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass
    def test_lower_row_invariant(self):
        state = Puzzle(4, 4, [[4, 2, 3, 7], [8, 5, 6, 10], [9, 1, 0, 11], [12, 13, 14, 15]])
        self.assertTrue(state.lower_row_invariant(2, 2))
        self.assertIs(type(state.lower_row_invariant(2, 2)), bool)
        state = Puzzle(4, 4, [[4, 2, 3, 7], [8, 5, 6, 10], [9, 1, 11, 0], [12, 13, 14, 15]])
        self.assertFalse(state.lower_row_invariant(2, 2))
        state = Puzzle(4, 4, [[4, 2, 3, 7], [8, 5, 6, 10], [9, 0, 1, 11], [12, 13, 14, 15]])
        self.assertFalse(state.lower_row_invariant(2, 2))
        state = Puzzle(4, 4, [[4, 2, 3, 7], [8, 5, 6, 10], [9, 1, 0, 12], [11, 13, 14, 15]])
        self.assertFalse(state.lower_row_invariant(2, 2))
        state = Puzzle(4, 4, [[4, 2, 3, 7], [8, 5, 6, 1], [9, 0, 10, 11], [12, 13, 14, 15]])
        self.assertTrue(state.lower_row_invariant(2, 1))
        state = Puzzle(4, 4, [[4, 2, 3, 7], [8, 5, 6, 1], [9, 0, 10, 11], [13, 12, 14, 15]])
        self.assertFalse(state.lower_row_invariant(2, 1))
        state = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
        self.assertTrue(state.lower_row_invariant(2, 2))
        state = Puzzle(3, 3, [[2, 3, 4], [1, 0, 5], [6, 7, 8]])
        self.assertTrue(state.lower_row_invariant(1, 1))
        state = Puzzle(3, 3, [[2, 3, 4], [5, 0, 1], [6, 7, 8]])
        self.assertFalse(state.lower_row_invariant(1, 1))
        state = Puzzle(3, 5, [[13, 1, 2, 3, 11], [5, 6, 7, 8, 10], [11, 12, 4, 0, 14]])
        self.assertTrue(state.lower_row_invariant(2, 3))
        state = Puzzle(4, 4, [[1, 2, 3, 7], [5, 0, 6, 4], [8, 9, 10, 11], [12, 13, 14, 15]])
        self.assertFalse(state.lower_row_invariant(1, 1))
    def test_solve_interior_tile(self):
        state = Puzzle(4, 4, [[4, 13, 1, 3], [5, 10, 2, 7], [8, 12, 6, 11], [9, 0, 14, 15]])
        self.assertIs(type(state.solve_interior_tile(3, 1)), str)
        state = Puzzle(4, 4, [[4, 13, 1, 3], [5, 10, 2, 7], [8, 12, 6, 11], [9, 0, 14, 15]])
        self.assertEqual(state.solve_interior_tile(3, 1), 'uuulddrulddruld')
        state = Puzzle(4, 4, [[1, 2, 3, 7], [5, 4, 9, 6], [8, 0, 10, 11], [12, 13, 14, 15]])
        self.assertEqual(state.solve_interior_tile(2, 1), 'urullddruld')
        state = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
        self.assertEqual(state.solve_interior_tile(2, 2) , 'uulldrruldrulddruld')
        state = Puzzle(3, 3, [[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        self.assertEqual(state.solve_interior_tile(2, 1) , 'l')
        state =  Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 10, 7], [8, 9, 0, 11], [12, 13, 14, 15]])
        self.assertEqual(state.solve_interior_tile(2, 2) , 'uld')
        state = Puzzle(3, 5, [[13, 2, 3, 4, 5], [6, 7, 8, 9, 11], [10, 12, 1, 0, 14]])
        self.assertEqual(state.solve_interior_tile(2, 3) , 'uullldrruldrruldrulddruld')
        state = Puzzle(4, 4, [[1, 2, 3, 4], [5, 6, 7, 9], [8, 0, 10, 11], [12, 13, 14, 15]])
        self.assertEqual(state.solve_interior_tile(2, 1) , 'urrulldrullddruld')
        state = Puzzle(3, 3, [[1, 2, 3], [4, 5, 7], [6, 0, 8]])
        self.assertEqual(state.solve_interior_tile(2, 1) , 'urullddruld')
        state = Puzzle(4, 5, [[15, 16, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 0, 17, 18, 19]])
        self.assertEqual(state.solve_interior_tile(3, 1), 'uuulddrulddruld')
    def test_solve_col0_tile(self):
        state = Puzzle(3, 3, [[1, 2, 3], [6, 4, 5], [0, 7, 8]])
        self.assertIs(type(state.solve_col0_tile(2)), str)
        state = Puzzle(3, 3, [[1, 2, 3], [6, 4, 5], [0, 7, 8]])
        self.assertEqual(state.solve_col0_tile(2), 'urr')
        state = Puzzle(3, 3, [[2, 3, 6], [1, 4, 5], [0, 7, 8]])
        self.assertEqual(state.solve_col0_tile(2), 'ururdlludruldruldrdlurdluurddlurr')
        state = Puzzle(3, 3, [[2, 6, 1], [3, 4, 5], [0, 7, 8]])
        self.assertEqual(state.solve_col0_tile(2), 'uruldruldrdlurdluurddlurr')
        state = Puzzle(3, 3, [[6, 2, 1], [3, 4, 5], [0, 7, 8]])
        self.assertEqual(state.solve_col0_tile(2), 'uruldruldruldrdlurdluurddlurr')
        state = Puzzle(3, 5, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [0, 11, 12, 13, 14]])
        self.assertEqual(state.solve_col0_tile(2), 'urrrrulldrulldrulldruldrdlurdluurddlurrrr')
        state = Puzzle(3, 5, [[10, 2, 3, 4, 5], [6, 7, 8, 9, 1], [0, 11, 12, 13, 14]])
        self.assertEqual(state.solve_col0_tile(2), 'uruldruldruldrdlurdluurddlurrrr')
        state = Puzzle(3, 5, [[1, 2, 10, 4, 5], [6, 7, 8, 9, 3], [0, 11, 12, 13, 14]])
        self.assertEqual(state.solve_col0_tile(2), 'ururdlludruldruldrdlurdluurddlurrrr')
    def test_invariant_row0(self):
        state = Puzzle(3, 3, [[2, 0, 1], [3, 4, 5], [6, 7, 8]])
        self.assertFalse(state.row0_invariant(1))
        self.assertIs(type(state.row0_invariant(1)), bool)
        state = Puzzle(4, 4, [[1, 0, 3, 2], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
        self.assertFalse(state.row0_invariant(1))
        state = Puzzle(3, 3, [[1, 0, 2], [3, 4, 5], [6, 7, 8]])
        self.assertTrue(state.row0_invariant(1))
        state = Puzzle(4, 4, [[1, 0, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
        self.assertTrue(state.row0_invariant(1))
        state = Puzzle(3, 5, [[1, 2, 3, 4, 0], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]])
        self.assertTrue(state.row0_invariant(4))
        state = Puzzle(3, 5, [[2, 4, 1, 0, 3], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]])
        self.assertFalse(state.row0_invariant(3))
        state = Puzzle(4, 4, [[4, 2, 0, 3], [5, 1, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
        self.assertTrue(state.row0_invariant(2))
        # from the grader
        state = Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]])
        self.assertFalse(state.row0_invariant(2))
    def test_invariant_row1(self):
        state = Puzzle(3, 3, [[2, 3, 4], [1, 0, 5], [6, 7, 8]])
        self.assertTrue(state.row1_invariant(1))
        self.assertIs(type(state.row1_invariant(1)), bool)
        state = Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]])
        self.assertTrue(state.row1_invariant(1))
        state = Puzzle(3, 3, [[2, 3, 4], [5, 1, 0], [6, 7, 8]])
        self.assertTrue(state.row1_invariant(2))
        state = Puzzle(4, 4, [[1, 3, 4, 2], [0, 6, 5, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
        self.assertFalse(state.row1_invariant(0))
        state = Puzzle(3, 5, [[1, 2, 3, 4, 5], [8, 9, 0, 6, 7], [10, 11, 12, 13, 14]])
        self.assertFalse(state.row1_invariant(2))
        state = Puzzle(3, 5, [[1, 5, 2, 3, 4], [7, 6, 0, 8, 9], [10, 11, 12, 13, 14]])
        self.assertTrue(state.row1_invariant(2))
        state = Puzzle(3, 5, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [10, 11, 12, 13, 14]])
        self.assertTrue(state.row1_invariant(4))
        state = Puzzle(4, 4, [[4, 6, 1, 3], [5, 2, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
        self.assertTrue(state.row1_invariant(2))
        # from the grader
        state = Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]])
        self.assertFalse(state.row1_invariant(0))
        self.assertIs(type(state.row1_invariant(1)), bool)
        state = Puzzle(4, 5, [[15, 6, 5, 3, 4], [2, 1, 0, 8, 9], [10, 11, 12, 13, 14], [7, 16, 17, 18, 19]])
        self.assertFalse(state.row1_invariant(2))
    def test_solve_row0(self):
        state = Puzzle(3, 3, [[1, 2, 0], [3, 4, 5], [6, 7, 8]])
        self.assertEqual(state.solve_row0_tile(2), 'ld')
        state = Puzzle(4, 4, [[2, 4, 5, 0], [3, 6, 1, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
        self.assertEqual(state.solve_row0_tile(3), 'ldllurrdlurdlurrdluldrruld')
        state = Puzzle(4, 4, [[1, 3, 5, 0], [2, 6, 4, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
        self.assertEqual(state.solve_row0_tile(3), 'lduldruldurdlurrdluldrruld')        
        state = Puzzle(4, 5, [[1, 5, 6, 0, 4], [7, 2, 3, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
        self.assertEqual(state.solve_row0_tile(3), 'lduldurdlurrdluldrruld')    
    def test_solve_row1(self):
        state = Puzzle(3, 3, [[2, 5, 4], [1, 3, 0], [6, 7, 8]])
        self.assertEqual(state.solve_row1_tile(2), 'uldruldur')
        self.assertIs(type(state.solve_row1_tile(2)), str)
        state = Puzzle(3, 3, [[1, 4, 2], [3, 5, 0], [6, 7, 8]])
        self.assertEqual(state.solve_row1_tile(2), 'lur')
        state = Puzzle(3, 5, [[1, 2, 7, 3, 4], [6, 5, 0, 8, 9], [10, 11, 12, 13, 14]])
        self.assertEqual(state.solve_row1_tile(2), 'uldur')
        state = puzzle = Puzzle(4, 4, [[1, 2, 6, 3], [7, 4, 5, 0], [8, 9, 10, 11], [12, 13, 14, 15]])
        self.assertEqual(state.solve_row1_tile(3), 'lllurrdlurrdlur')
        state = Puzzle(4, 4, [[1, 7, 4, 2], [3, 5, 6, 0], [8, 9, 10, 11], [12, 13, 14, 15]])
        self.assertEqual(state.solve_row1_tile(3), 'ulldrruldruldur')
        state = Puzzle(3, 5, [[1, 7, 2, 3, 4], [6, 5, 0, 8, 9], [10, 11, 12, 13, 14]])
        self.assertEqual(state.solve_row1_tile(2), 'uldruldur')
        state = Puzzle(3, 5, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [10, 11, 12, 13, 14]])
        self.assertEqual(state.solve_row1_tile(4), 'lur')
    def test_two_by_two(self):
        state = Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]])
        self.assertEqual(state.solve_2x2(), 'uldrul')
        self.assertIs(type(state.solve_2x2()), str)
        state = Puzzle(3, 5, [[5, 1, 2, 3, 4], [6, 0, 7, 8, 9], [10, 11, 12, 13, 14]])
        self.assertEqual(state.solve_2x2(), 'ulrdlu')
        state = Puzzle(2, 2, [[3, 2], [1, 0]])
        self.assertEqual(state.solve_2x2(), 'uldrul')
        state = Puzzle(2, 2, [[1, 3], [2, 0]])
        self.assertEqual(state.solve_2x2(), 'ul')
        state = Puzzle(2, 2, [[0, 1], [2, 3]])
        self.assertEqual(state.solve_2x2(), '')
    def test_finale(self):
        state = Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]])
        self.assertEqual(state.solve_puzzle(), 'rrdddulduldulduuulddrulddrulduruulddruldruldrdlurdluurddlurrrrulduldulduldurlruldrdlurdluurddlurrrruldurlduldurlduldurlduldurdlurrdluldrrulduldrul')
        state = Puzzle(4, 4, [[14, 12, 8, 5], [0, 2, 15, 6], [4, 13, 7, 9], [10, 11, 3, 1]])
        self.assertEqual(state.solve_puzzle(), 'rrrdduullurrdldrulddrulduuulldrruldrulddrulddrulduurullddrulddrulduruuldrulddruldruldrdlurdluurddlurrrllurrdlllurrdluulddruldururdlludruldruldrdlurdluurddlurrrulldrruldruldurldlurdlurrdluldrruldlurldulrdlu')
        state = Puzzle(4,4,[[2,11,12,13],[9,4,6,1],[5,7,8,3],[10,0,14,15]])
        self.assertEqual(state.solve_puzzle(), 'rrlluuurrdllurdlludrulddrulddruldururullddruldruldrdlurdluurddlurrruldruldllurrdluulddruldurrulldruldrdlurdluurddlurrrlllurrdlurrdlurldulldrruldruldurlduldurdlurrdluldrrulduldrul')
        
              
# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)
