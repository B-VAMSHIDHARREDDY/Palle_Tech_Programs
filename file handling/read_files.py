# Read data from a file

f = open("C:\\Users\\B.Vamshidhar Reddy\\OneDrive\\Desktop\\data.txt",'r')

# res = f.read() # it is read the total text in the file
#
# print(res)
# print("***********")
#
# print(f.readline()) # it is read first line only
# print(f.readline(14))
#
# res2 = f.readlines() # read all lines and store list
# print(res2)
# print("\n",res2[1])
# print(res2[4])

for i in f:  # using for we print the line by line
    print(i)


f.close()

