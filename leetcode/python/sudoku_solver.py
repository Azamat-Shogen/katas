 #TODO: valid sudoku - leetcode

class Solution:
  def isValidSudoku(self, board):
    #TODO: filter horizontal numbers
    horiz_list = [[ char for char in list(filter(lambda x: x != '.', el))] for el in board]
    # create a set of these numbers
    horiz_set = [set(el) for el in horiz_list]
  
    # create 2 lists to hold the length of each element in horiz_set and horiz_pass
    horiz_list_length_elements = list(map(lambda x: len(x), horiz_list))
    horiz_set_length_elements = list(map(lambda x: len(x), horiz_set))
    # compare the two elements and return a list of boolean values
    horiz_boolean_list = [horiz_list_length_elements[i] == horiz_set_length_elements[i] for i in range(len(horiz_set_length_elements))]

    # RETURN True if All values are True , else False
    horiz_pass = False not in horiz_boolean_list
    

    #TODO: create a list to hold all vertical lines
    vert_temp = []
    vert_index = 0

    while vert_index < len(board):
      temp = []
      for el in board:
        temp.append(el[vert_index])
        
      vert_temp.append(temp)
      vert_index += 1
    
    #TODO: filter horizontal numbers
    vert_list = [[ char for char in list(filter(lambda x: x != '.', el))] for el in vert_temp]
    # create a set of these numbers
    vert_set = [set(el) for el in vert_list]
   
    # create 2 lists to hold the length of each element in vert_set and vert_pass
    vert_list_length_elements = list(map(lambda x: len(x), vert_list))
    vert_set_length_elements = list(map(lambda x: len(x), vert_set))
    # compare the two elements and return a list of boolean values
    vert_boolean_list = [vert_list_length_elements[i] == vert_set_length_elements[i] for i in range(len(vert_set_length_elements))]

    # RETURN True if All values are True , else False
    vert_pass = False not in vert_boolean_list
     

    #TODO: cubes lists
    
    cubes = []
    temp_col = 0
    for _ in range(3):
      x = 0
      for _ in range(3):
        temp = []
        for i in range(x, x+3):
          y = temp_col
          for j in range(y, y+3):
            temp.append(board[i][j])
        
        x += 3
        cubes.append(temp)
      temp_col += 3

     #TODO: filter cube numbers
    cube_list = [[ char for char in list(filter(lambda x: x != '.', el))] for el in cubes]
    # create a set of these numbers
    cube_set = [set(el) for el in cube_list]
   
    # create 2 lists to hold the length of each element in cube_set and cube_pass
    cube_list_length_elements = list(map(lambda x: len(x), cube_list))
    cube_set_length_elements = list(map(lambda x: len(x), cube_set))
    # compare the two elements and return a list of boolean values
    cube_boolean_list = [cube_list_length_elements[i] == cube_set_length_elements[i] for i in range(len(cube_set_length_elements))]

    # RETURN True if All values are True , else False
    cube_pass = False not in cube_boolean_list

    # RETURN TRUE IF ALL CASES ARE TRUE (HORISONTAL, VERTICAL, CUBICAL)
    return (horiz_pass and vert_pass) and cube_pass
     



b1 = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]


b2 = [["8","3",".",".","7",".",".",".","."]
      ,["6",".",".","1","9","5",".",".","."]
      ,[".","9","8",".",".",".",".","6","."]
      ,["8",".",".",".","6",".",".",".","3"]
      ,["4",".",".","8",".","3",".",".","1"]
      ,["7",".",".",".","2",".",".",".","6"]
      ,[".","6",".",".",".",".","2","8","."]
      ,[".",".",".","4","1","9",".",".","5"]
      ,[".",".",".",".","8",".",".","7","9"]]



solution = Solution()
result1 = solution.isValidSudoku(b1)
result2 = solution.isValidSudoku(b2)

print(result1) # output True
print(result2) # output False

