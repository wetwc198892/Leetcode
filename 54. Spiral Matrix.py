class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        result = []
        left = 0
        right = len(matrix[0])-1
        up = 0
        down = len(matrix)-1
        i,j=0,0
        flag = 1
        while(True):
            if len(matrix)>1 and matrix[i][j]==-111:
                break
            if flag == 1:
                for k in range(left,right+1):
                    result.append(matrix[up][k])
                    matrix[up][k] = -111
                i,j=i+1,right
                up += 1
                flag = 2
                if len(matrix)==1:
                    break
            elif flag == 2:
                for k in range(up,down+1):
                    result.append(matrix[k][right])
                    matrix[k][right] = -111
                i,j=down,right-1
                right -= 1
                flag = 3
            elif flag == 3:
                for k in range(right,-1+left,-1):
                    result.append(matrix[down][k])
                    matrix[down][k] = -111
                i,j=down-1,left
                down -= 1
                flag = 4
            elif flag == 4:
                for k in range(down,-1+up,-1):
                    result.append(matrix[k][left])
                    matrix[k][left] = -111
                i,j=up,left+1
                left += 1
                flag = 1
        return result