f = open("read2.txt", "r")
all_lines = f.readlines()

i = 1.0
for line in all_lines:
    print(f'{line} {round(i,1)}')
    i = i + 0.1




