m = 1
n = 0
p = 0
for i in range(4) :
    p = n
    n = m
    m = n+p
    print("Month",i,":",m,"pair(s) of rabbits")
    
