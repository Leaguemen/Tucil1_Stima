import random

class Token:
    def __init__(self, symbol:str,x:int,y:int):
        self.symbol = symbol
        self.x = x
        self.y = y

    def __str__(self):
        return self.symbol

class Matrix:
    def __init__(self, rows:int, cols:int):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    

def clean_data(data : str):
    result = []
    buffer =""
    for i in range(len(data)):
        if data[i] == " " :
            result.append(buffer)
            buffer=""
        elif data[i] == '\n':
            result.append(buffer)
            result.append(data[i])
            buffer=""
        elif i == len(data)- 1 :
            result.append(buffer + data[i])
            buffer=""
        else:
            buffer+= data[i]
    return result

def enumerate_sequence(matrix: Matrix, n:int):
    def backtrack(path, visited, last_i, last_j, last_movement):
        if len(path) == n: #base case, complete sequence has been formed
            strings.append(path)
            return
        last_char = path[-1] if path else None
        for i in range(len(matrix.data)): #len baris
            for j in range(len(matrix.data[0])): #len kolom
                if matrix.data[i][j] != last_char and not visited[i][j]:
                    if last_i != -1 and last_movement == "horizontal" and i != last_i:
                        continue
                    if last_j != -1 and last_movement == "vertical" and j != last_j:
                        continue
                    visited[i][j] = True
                    next_movement = "horizontal" if last_movement == "vertical" else "vertical"
                    backtrack(path + [matrix.data[i][j]], visited, i, j, next_movement)
                    visited[i][j] = False

    strings = [] #array to store all possible string
    visited = [[False for _ in range(len(matrix.data[0]))] for _ in range(len(matrix.data))] #boolean array to track cell yang belum di visit
    for i in range(len(matrix.data)):
        for j in range(len(matrix.data[0])):
            visited[i][j] = True
            # Start by going horizontal
            backtrack([matrix.data[i][j]], visited, i, j, "horizontal")
            # Start by going vertical
            backtrack([matrix.data[i][j]], visited, i, j, "vertical")
            visited[i][j] = False
    return strings

#kamus global
jumlah_token_unik = -1
token_selection = []
buffer_size = -1
matrix_width = -1
matrix_height = -1
matrix = Matrix(0,0)
num_of_sequence = -1
array_of_points = []
array_of_sequence = []

#main
option = input("How would you want to input the data ? \n 1. file \n 2. command line \n >> ")
while option not in ['1','2']:
    print("Invalid option, please only write 1 or 2")
    option = input("How would you want to input the data ? \n 1. file \n 2. command line \n >> ")

if option == '1':
    data = open("input.txt")
    data_contents = clean_data(data.read())
    buffer_size= int(data_contents[0])
    matrix_width = int(data_contents[2])
    matrix_height = int(data_contents[3])
    matrix = Matrix(matrix_width,matrix_height)
    i = 0
    n_ent = 0
    curr_col = 1
    curr_row = 1
    #fill matrix
    while n_ent < 2+matrix_height:
        if n_ent < 2:
            if data_contents[i]== '\n':
                n_ent +=1
        else:
            if data_contents[i]== '\n':
                curr_col = 1
                n_ent +=1
                curr_row +=1
            else:
                temp = Token(data_contents[i],curr_col,curr_row)
                matrix.data[curr_col-1][curr_row-1] = temp
                curr_col +=1
        i +=1
    array_of_sequence = []
    array_of_points = []
    num_of_sequence = data_contents[i]
    i +=2
    isPoint = False
    seq_buf = []
    while i < len(data_contents):
        if not isPoint:
            if data_contents[i] == '\n':
                array_of_sequence.append(seq_buf)
                seq_buf = []
                isPoint = not isPoint
            else:
                seq_buf.append(data_contents[i])
        else:
            if data_contents[i] != '\n':
                array_of_points.append(int(data_contents[i]))
            else:
                isPoint = not isPoint
        i+=1 
else:
    jumlah_token_unik = int(input())
    input_string= input()
    token_selection = input_string.split()
    if jumlah_token_unik != len(token_selection):
        print("Jumlah token unik tidak sama dengan jumlah token unik yang diinput")
    else:
        buffer_size= int(input())
        matrix_size = input().split()
        matrix_width= int(matrix_size[0])
        matrix_height = int(matrix_size[1])
        matrix = Matrix(matrix_width,matrix_height)
        for i in range(matrix_width):
            for j in range(matrix_width):
                temp = Token(random.choice(token_selection),i+1,j+1)
                matrix.data[i][j] = temp
        num_of_sequence = int(input())
        max_sequence_size = int(input())
        for i in range(num_of_sequence):
            array_of_points.append(random.randint(10,100))
            temp = []
            for j in range(random.randint(1,max_sequence_size)):
                temp.append(random.choice(token_selection))
            array_of_sequence.append(temp)
