class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length=len(matrix)
        for index in range(length):
            for jindex in range(len(matrix[index])):
                if target==matrix[index][jindex]:
                    return True
        return False
            


        