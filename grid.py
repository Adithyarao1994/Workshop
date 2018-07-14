width = int(input("How wide?"))
height = int(input("How high?"))
grid = []
row = []
bak = "."
for i in range(width):
    row.append(bak)
for i in range(height):
    grid.append(row)
print (len(grid))
for i in range(len(grid)):
	print(grid[i])
n=len(grid)
N=2*len(grid)
fact=1
fact2=1

for i in range(1,n+1):
	fact=fact*i
for i in range(1,N+1):	
	fact2=fact2*i

print("The Number of Routes are") 
result=fact2/(fact*fact)
print(result)


