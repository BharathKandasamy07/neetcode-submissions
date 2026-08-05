class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j].isdigit() and board[i][j] in seen:
                    print('a')
                    return False
                seen.add(board[i][j])
        
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i].isdigit() and board[j][i] in seen:
                    print('b')
                    return False
                seen.add(board[j][i])
        
        for i in (0,3,6):
            for j in (0,3,6):
                seen = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l].isdigit() and board[i+k][j+l] in seen:
                            print('c')
                            return False
                        seen.add(board[i+k][j+l])
        
        return True


