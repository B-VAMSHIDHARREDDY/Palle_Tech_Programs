print("----------------- Example 1 ----------------")
def sample(**m):
    print(m)
sample(name="vamshi")
print("----------------- Example 2 ----------------")
def sample(**n):
    print(n)
sample(samsung="10k",apple="20k",vivo="15k")
print("----------------- Example 3 ----------------")
def sample(**x):
    for i in x:
        print(i,end="   ") # ======> print keys
        print(x[i]) # =====>print values
sample(samsung="10k",apple="20k",vivo="15k")

