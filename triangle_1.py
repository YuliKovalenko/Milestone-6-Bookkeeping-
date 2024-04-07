def get_triangle(rows: int) -> list[list[int]]:
    triangle = []
    triangle.append([1])
 
    for i in range(1, rows):
        previous_row = triangle[i-1]  
        current_row = [1]  
   
        for j in range(1, len(previous_row)):
            current_row.append(previous_row[j-1] + previous_row[j])

        current_row.append(1)
        triangle.append(current_row)

    return triangle


def print_centered_triangle(triangle: list[list[int]]):
    max_row_length = len(triangle[-1]) * 2 - 1
    for row in triangle:
        print(" " * ((max_row_length - len(row) * 2) // 2), end="")
        print(*row, sep=" ")


while True:
    try:
        rows = int(input("Enter the desired number of rows for Pascal's Triangle: "))
        if rows > 0:
            break 
        else:
            print("Please enter a positive number of rows.")
    except ValueError:
        print("Please enter a valid integer number of rows.")


triangle = get_triangle(rows)
print_centered_triangle(triangle)