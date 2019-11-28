import os.path
import re

li=os.listdir("C:\\Users\\vsingh326\\Documents\\python\\demo")

for i in li:

    net=os.path.splitext(i)
    if(net[1]==".log"):
        print(i)
        f=open("C:\\Users\\vsingh326\\Documents\\python\\demo"+i,"rb")
        data = f.read().decode()
        pattern="\S+@\S+"
        matches=re.findall(pattern,data)
        print(matches)


        f.close()
