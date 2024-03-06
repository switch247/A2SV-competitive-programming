class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows ,n_columns =  len(matrix),  len(matrix[0])
        l, r = 0, n_rows* n_columns -1
        while l<=r:
            cell_number = (l+r)//2
            row_number = cell_number // n_columns
            column_number = cell_number % n_columns
            if matrix[row_number][column_number] == target:
                return True
            elif matrix[row_number][column_number] < target:
                l = cell_number +1
            else:
                r = cell_number -1
        return False
        # 1d->2d matrix
        # cell_number = row_number*n_columns + column_number
        # row_number = cell_number // n_columns
        # column_number = cell_number % n_columns




        # method 2
        # def BinarySearch(resCol, low, high, target):
        #     while low <= high:
        #         mid = (low+high) // 2
        #         if resCol[mid] == target:
        #             return True
        #         elif resCol[mid] > target:
        #             high = mid -1
        #         else:
        #             low = mid + 1
        #     return False

        # l, r = 0, len(matrix) - 1
        # while l <= r:
        #     mid = (l+r) // 2
        #     if matrix[mid][0] <= target and matrix[mid][-1] >= target:
        #         resCol = matrix[mid]
        #         return BinarySearch(resCol, 0, len(resCol), target)
        #     elif matrix[mid][0] > target:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return False
