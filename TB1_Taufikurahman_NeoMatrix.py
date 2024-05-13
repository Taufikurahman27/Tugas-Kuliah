#Big task 1 is to create a neo matrix program
print("===================================")
print("            Taufikurahman          ")
print("             41823010025           ")
print("       TB1-Advanced Programming    ")
print("===================================")

#Class to decode the matrix
def decode_matrix(input_matrix):
    # Takes the number of rows and columns from the input
    rows, cols = map(int, input_matrix[0].split())

    # Declare an empty matrix
    matrix = []

    # Fills the matrix with input
    for row in input_matrix[1:]:
        matrix.append(list(row))

    # Decoding text from the matrix
    decoded_text = ''
    for col in range(cols):
        for row in range(rows):
            # If the character is not alphanumeric,replace it with a space
            if not matrix[row][col].isalnum():
                decoded_text += ' '
            else:
                decoded_text += matrix[row][col]

    return decoded_text

# Example input
input_matrix = [
    '7 3',
    'Tsi',
    'h%x',
    'i #',
    'sM ',
    '$a ',
    '#t%',
    'ir!'
]

# Decoding and printing results
print(decode_matrix(input_matrix))
