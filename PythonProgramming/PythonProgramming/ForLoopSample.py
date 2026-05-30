limit =5

for i in range(limit):
    print("index -> ",i)

print("*"*50)
for i in range(limit,0,-1):
    print("Step -1 : reverse index -> ",i)

print("*"*50)
for i in range(0,limit,2):
    print("Step 2 : index -> ",i)


print("*"*50)
for i in range(0,limit,3):
    print("Step 3 : index -> ",i)


print("*"*50)
for i in range(0,limit):
    print("No step : index -> ",i)
