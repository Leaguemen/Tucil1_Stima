import random
import time

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

def compare_sequence(compared,reference):
    length_compared = len(compared)
    length_reference = len(reference)
    if length_reference > length_compared:
        return False
    else:
        c= 0
        r = 0
        while c < length_compared:
            if compared[c].symbol == reference[r]:
                r += 1
                if r == length_reference:
                    return True  
            else:
                r = 0  
            c += 1
        return False
    
def enumerate_sequence(matrix: Matrix, n:int):
    def backtrack(path, visited, last_i, last_j, last_movement):
        if len(path) == n:
            sequence.append(path)
            return
        last_char = path[-1] if path else None
        for i in range(len(matrix.data)):
            for j in range(len(matrix.data[0])):
                if matrix.data[i][j] != last_char and not visited[i][j]:
                    if last_i != -1 and last_movement == "vertical" and i != last_i:
                        continue
                    if last_j != -1 and last_movement == "horizontal" and j != last_j:
                        continue
                    visited[i][j] = True
                    next_movement = "vertical" if last_movement == "horizontal" else "horizontal"
                    backtrack(path + [matrix.data[i][j]], visited, i, j, next_movement)
                    visited[i][j] = False

    sequence = []
    while n >=2:
        visited = [[False for _ in range(len(matrix.data[0]))] for _ in range(len(matrix.data))]
        for j in range(len(matrix.data[0])):
            visited[0][j] = True
            backtrack([matrix.data[0][j]], visited, 0, j, "horizontal")
            visited[0][j] = False
        n -=1
    return sequence

def find_idx(lis : list, elmt : int):
    found = False
    i = 0
    while not found and i < len(lis):
        if lis[i] == elmt:
            found = True
        i += 1
    if not found:
        return -1
    else:
        return i

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
sequence_combination = []
result_point_array = []
max_points = 0
idx_of_max = -1
seq_result = []
result_pos = []
executionTime = 0

#main
option = input("How would you want to input the data ? \n 1. file \n 2. command line \n >> ")
while option not in ['1','2']:
    print("Invalid option, please only write 1 or 2")
    option = input("How would you want to input the data ? \n 1. file \n 2. command line \n >> ")

if option == '1':
    file_open=input(str("Apa nama file yang ingin dibaca ? "))
    data = open("input/"+file_open)
    data_contents = clean_data(data.read())
    buffer_size= int(data_contents[0])
    matrix_width = int(data_contents[2])
    matrix_height = int(data_contents[3])
    matrix = Matrix(matrix_height,matrix_width)
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
                matrix.data[curr_row-1][curr_col-1] = temp
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
    data.close()
else:
    jumlah_token_unik = int(input("Masukkan jumlah token yang ingin diinput: "))
    input_string= input("Masukkan token - token unik tersebut dengan tiap token dipisah dengan spasi (e.g. BD 1C 7A ): ")
    token_selection = input_string.split()
    if jumlah_token_unik != len(token_selection):
        print("Jumlah token unik tidak sama dengan jumlah token unik yang diinput")
    else:
        buffer_size= int(input("Masukkan besar buffer : "))
        matrix_size = input("Masukkan dimensi matrix (e.g. 6 6) : ").split()
        matrix_width= int(matrix_size[0])
        matrix_height = int(matrix_size[1])
        matrix = Matrix(matrix_height,matrix_width)
        for i in range(matrix_height):
            for j in range(matrix_width):
                temp = Token(random.choice(token_selection),j+1,i+1)
                matrix.data[i][j] = temp
        print("Membuat matrix secara acak ... ")
        time.sleep(2)
        print("Inilah matrix yang digunakan: ")
        print(matrix)
        num_of_sequence = int(input("Masukkan berapa jumlah sequence yang akan dibuat : "))
        max_sequence_size = int(input("Masukkan panjang maksimal sequence tersebut : "))
        for i in range(num_of_sequence):
            array_of_points.append(random.randint(10,100))
            temp = []
            for j in range(random.randint(2,max_sequence_size)):
                temp.append(random.choice(token_selection))
            array_of_sequence.append(temp)
        print("Membuat sequence secara acak ... ")
        time.sleep(2)
        for i in range(len(array_of_sequence)):
            print(array_of_sequence[i], "@", array_of_points[i], "Points")
start = time.time()
sequence_combination = enumerate_sequence(matrix,buffer_size)
if sequence_combination == []:
    print("Tidak ada sekuens yang bisa digenerate ... ")
    out= input(("Ketik apapun untuk keluar dari program ... "))
else:
    for i in range(len(sequence_combination)):
        points = 0
        for j in range(len(array_of_sequence)):
            if compare_sequence(sequence_combination[i],array_of_sequence[j]):
                points += array_of_points[j]
        result_point_array.append(points)

    max_points = max(result_point_array)
    idx_of_max = find_idx(result_point_array,max_points)

    if idx_of_max != -1:
        result_temp = sequence_combination[idx_of_max]
        for i in range(len(result_temp)):
            seq_result.append(result_temp[i].symbol)
            result_pos.append([result_temp[i].x,result_temp[i].y])
    end = time.time()
    executionTime = (end - start)*1000


    print("Poin maksimal yang bisa didapat adalah :", max_points)
    print('\n')
    print("Dengan sequence sebagai berikut :",seq_result)
    print('\n')
    print("Berikut adalah koordinat tiap simbol pada sequence tersebut : ")
    for i in range(len(result_pos)):
        print(result_pos[i])

    print("execution time :",executionTime,"ms")

    option_save = str(input("Apakah Anda ingin menyimpan hasil program ? (y/n) "))
    while option_save not in ["y","n"]:
        print("Bukan pilihan valid, tolong ketik hanya y untuk yes atau n untuk no !")
        option_save=str(input("Apakah Anda ingin menyimpan hasil program ? (y/n) "))
    if option_save == "y":
        file_name = str(input("Apa nama filenya ? "))
        save = open("../test/"+file_name,'w')
        save.write(str(max_points))
        save.write('\n')
        save.write(str(seq_result))
        save.write('\n')
        for i in range(len(result_pos)):
            save.write(str(result_pos[i]))
            save.write('\n')
        save.write(str(executionTime))
        save.close()
    out= input(("Ketik apapun untuk keluar dari program ... "))


