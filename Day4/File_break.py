fo1 = open('C:/Users/vsingh326/Documents/python/chunk', 'wb')
for i in range(0, 5761):
    fo2 = open('C:/Users/vsingh326/Documents/python/chunk' + str(i) + '.jpg', 'rb')
    for line in fo2:
        line.read()
fo1.close()
