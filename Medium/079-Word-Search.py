"""
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


class Solution(object):

    def dfs(self, r, c, word, board):
        if len(word) == 0:
            return True
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return False
        if board[r][c] != word[0]:
            return False
        val = board[r][c]
        board[r][c] = '#'
        if self.dfs(r + 1, c, word[1:], board) or self.dfs(r - 1, c, word[1:], board) or self.dfs(r, c + 1, word[1:], board) or self.dfs(r, c - 1, word[1:], board):
            return True
        board[r][c] = val
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(r, c, word, board):
                    return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(Solution().erist(board, word))
