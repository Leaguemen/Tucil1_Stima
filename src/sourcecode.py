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

#main
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


print(buffer_size)
print(matrix_width, matrix_height)
print(matrix)
print(num_of_sequence)
print(array_of_points)
print(array_of_sequence)