import math
def powerset(set,size):
    powersetsize=(int) (math.pow(2,size))
    outer=0
    inner=0
    for outer in range (0,powersetsize):
        for inner in range(0,size):
            if ((outer&(1<<inner))>0):
                print(set[inner],end="")
        print("")
size=int(input("Enter array size:"))
set=[]
for i in range(0,size):
    n=int(input("Enter element:"))
    set.append(n)
powerset(set,len(set))