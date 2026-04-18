class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Initialize 3 lists of hash sets to track the used numbers in rows, columns, and sub-grids
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # Each sub-grid is tracked by a unique box index
        
        # Iterate over the entire board
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                
                # Skip empty cells
                if num == ".":
                    continue
                
                # Calculate the box index for the current cell
                box_index = (row // 3) * 3 + (col // 3)
                
                # Check for duplicates in the row, column, or sub-grid
                if num in rows[row] or num in cols[col] or num in boxes[box_index]:
                    return False
                
                # Add the number to the respective row, column, and sub-grid sets
                rows[row].add(num)
                cols[col].add(num)
                boxes[box_index].add(num)
        
        # If no duplicates are found, the Sudoku board is valid
        return True
