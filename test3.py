def MatrixSpiral(strArr):
    # Convert ["[1,2]", "[10,14]"] → [[1,2], [10,14]]
    matrix = []
    for s in strArr:
        # Remove brackets and spaces
        s = s.replace('[', '').replace(']', '').strip()
        # Split by comma and convert to int
        row = [int(x.strip()) for x in s.split(',') if x.strip() != '']
        matrix.append(row)

    result = []

    # Spiral traversal
    while len(matrix) > 0:
        # 1️⃣ Top row
        result.extend(matrix[0])
        del matrix[0]

        # 2️⃣ Right column
        for r in range(len(matrix)):
            if len(matrix[r]) > 0:
                result.append(matrix[r][-1])
                del matrix[r][-1]

        # 3️⃣ Bottom row (reversed)
        if len(matrix) > 0:
            result.extend(matrix[-1][::-1])
            del matrix[-1]

        # 4️⃣ Left column (bottom to top)
        for r in range(len(matrix) - 1, -1, -1):
            if len(matrix[r]) > 0:
                result.append(matrix[r][0])
                del matrix[r][0]

    return result


# Example usage:
print(MatrixSpiral(["[1,2,3]", "[4,5,6]", "[7,8,9]"]))       # [1,2,3,6,9,8,7,4,5]
print(MatrixSpiral(["[1,2]", "[10,14]"]))                   # [1,2,14,10]
print(MatrixSpiral(["[4,5,6,5]", "[1,1,2,2]", "[5,4,2,9]"]))

def test(strArr):
    matrix = []
    for s in strArr:
        s = s.replace('[','').replace(']', '')
        row = s.strip().split(',')
        row = [int(e) for e in row]
        matrix.append(row)

    result = []
    while len(matrix) >0:
        result.extend(matrix[0])
        del matrix[0]

        for r in range(len(matrix)):
            if len(matrix)>0:
                result.append(matrix[r][-1])
                del matrix[r][-1]

        if len(matrix)>0:
            result.extend(matrix[-1][::-1])
            del matrix[-1]

        for r in range(len(matrix)-1, -1, -1):
            if len(matrix) >0:
                result.append(matrix[r][0])
                del matrix[r][0]
        print("matrix: ", matrix)

    return result


print(test(["[1,2,3]", "[4,5,6]", "[7,8,9]"]))  
print(test(["[1,2]", "[10,14]"]))                   # [1,2,14,10]
print(test(["[4,5,6,5]", "[1,1,2,2]", "[5,4,2,9]"])) # [4,5,6,5,2,9,2,4,5,1,1,2]