class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lengthi = len(grid)
        if not lengthi:
            return 0
        lengthj = len(grid[0])
        result = 0
        for i in range(lengthi):
            for j in range(lengthj):
                if grid[i][j] == '1':
                    result += 1
                    self.findisland(i,j,grid)
        return result
    
    def findisland(self,i:int,j:int,grid:List[List[str]]):
        lengthi = len(grid)
        lengthj = len(grid[0])
        grid[i][j] = '0'
        if i>0 and grid[i-1][j] == '1':
            self.findisland(i-1,j,grid)
        if j>0 and grid[i][j-1] == '1':
            self.findisland(i,j-1,grid)
        if i<lengthi-1 and grid[i+1][j]=='1':
            self.findisland(i+1,j,grid)
        if j< lengthj-1 and grid[i][j+1]=='1':
            self.findisland(i,j+1,grid)
                                              
            