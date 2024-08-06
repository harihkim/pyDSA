def search(matrix: list[list[int]], to_find: int) -> tuple[int,int]:
    row_index = 0
    col_index = len(matrix[0]) - 1

    while(row_index < len(matrix) and col_index >= 0):
        found = matrix[row_index][col_index]
        if(found==to_find):
            return (row_index,col_index)
        elif(found > to_find):
            col_index -= 1
        else:
            row_index += 1
    return (-1,-1)

arr = [
    [10,20,30,40],
    [15,25,35,45],
    [28,29,37,49],
    [33,34,38,50]
]

print(search(arr,57))
