board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCDE"
y = ''
p = 0

for i in range(len(board)):
    for j in range(len(board[0])):
        l = board[i][j]
        if p< len(word) and l == word[p] :
            y += l
            p += 1
        else:
            
            
