INPUT_list = []
file = open('nono_board.txt','r')

for line in file:
    line.strip()
    line = line.split()
    INPUT_list.append(list(map(int, line)))

n = INPUT_list[0][0]
m = INPUT_list[0][1]

row = INPUT_list[1:m + 1]
column = INPUT_list[m + 1:n + m + 1]




