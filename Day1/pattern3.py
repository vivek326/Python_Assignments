num=int(input("Enter Number of rows: "))

for i in range(num,0,-1):
    print(" "*(num-i),"*"*i)

def sayhi(name1,name2,name3="Dhoni"):
    print("Hello "+name1+" "+name2+" "+name3)

sayhi(name1="Sachin",name2="Saurav")