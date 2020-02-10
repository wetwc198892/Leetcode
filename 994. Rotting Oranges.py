class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        list_two = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    temp_list = [i,j]
                    list_two.append(temp_list)
        temp_list = [-1,-1]
        list_two.append(temp_list)
        while(list_two):
            i,j = list_two.pop(0)
            if i == -1 and j == -1:
                mins += 1
                if len(list_two) > 0:
                    temp_list = [-1,-1]
                    list_two.append(temp_list)
                continue
            if j-1>=0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                temp_list = [i,j-1]
                list_two.append(temp_list)
            if j+1<len(grid[0]) and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                temp_list = [i,j+1]
                list_two.append(temp_list)
            if i-1>=0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                temp_list = [i-1,j]
                list_two.append(temp_list)
            if i+1<len(grid) and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                temp_list = [i+1,j]
                list_two.append(temp_list)
        for i in grid:
            if i.count(1)>0:
                return -1
        return mins-1
                    