import numpy as np
class Solution(object):
    def exist(self, board, word):

        def dfs(x, y, idx):
            if idx == len(word) - 1:
                return True
            
            visited[x][y] = True
            
            for x_id, y_id in directions:
                nx, ny = x + x_id, y + y_id
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and board[nx][ny] == word[idx + 1]:
                    if dfs(nx, ny, idx + 1):
                        return True
            
            visited[x][y] = False
            return False
        
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False



board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"

board2 = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
word2 = "AAAAAAAAAAAAAAa"

s = Solution()
print(s.exist(board1,word1))
print(s.exist(board2,word2))




# # Second approach
# def check(arr, word, x, y,word_idx):
#     if x < 0 or y < 0 or x >= len(arr) or y >= len(arr[0]) or word_idx > len(word):
#         return False

#     if arr[x][y] != word[word_idx]:
#         return False
    
#     if word_idx == len(word) - 1:
#         return True
        
#     temp = arr[x][y]
#     arr[x][y] = '*'
    
#     found = (check(arr, word, x+1, y, word_idx+1) or
#                 check(arr, word, x-1, y, word_idx+1) or
#                 check(arr, word, x, y+1, word_idx+1) or
#                 check(arr, word, x, y-1, word_idx+1))
    
#     arr[x][y] = temp
    
#     return found

# np_arr = np.array(board)

# row = len(board)
# column = len(board[0])

# for i in range(row):
#     for j in range(column):
#         if board[i][j] == word[0] and check(np_arr, word, i, j, 0):
#             return True

# return False