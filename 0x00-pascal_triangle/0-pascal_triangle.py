#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        # Previous row is the last row in the triangle
        prev_row = triangle[-1]
        # Initialize the new row with a leading 1
        new_row = [1]

        # Populate the middle values
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        # End the row with a trailing 1
        new_row.append(1)

        # Append the new row to the triangle
        triangle.append(new_row)

    return triangle
