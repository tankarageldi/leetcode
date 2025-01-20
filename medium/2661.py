class Solution:
    def firstCompleteIndex(self, arr, mat):
        num_to_index = {}
        for i in range(len(arr)):
            num_to_index[arr[i]] = i

        result = float("inf")
        num_rows, num_cols = len(mat), len(mat[0])

        for row in range(num_rows):
            last_element_index = float("-inf")
            for col in range(num_cols):
                index_val = num_to_index[mat[row][col]]
                last_element_index = max(last_element_index, index_val)

            result = min(result, last_element_index)

        for col in range(num_cols):
            last_element_index = float("-inf")
            for row in range(num_rows):
                index_val = num_to_index[mat[row][col]]
                last_element_index = max(last_element_index, index_val)

            result = min(result, last_element_index)

        return result