fin = open("C:/Users/vsingh326/PycharmProjects/function/demo", "rt")
fout = open("out.txt", "wt")
li = ["Sachin", "Saurav", "Rahul"]
for line in fin:
    fout.write(line.replace('Dhoni', '******'))

fin.close()
fout.close()
