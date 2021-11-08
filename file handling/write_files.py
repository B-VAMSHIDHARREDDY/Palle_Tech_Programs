f = open("C:\\Users\\B.Vamshidhar Reddy\\OneDrive\\Desktop\\data.txt",'w')

# f.write("one") # remove all data in file and write "one" on file

n = int(input("enter lines we have: "))
for i in range(1,n):
    f.write(f"line number {i}")
    f.write("\n")

f.write(input("enter text: "))
f.close()