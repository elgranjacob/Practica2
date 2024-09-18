
import random
import time
matrix = []
inicio = time.time()
filas = int(input("Proporcione el número de fila:"))
columnas = int(input("Proporcione el número de columnas: "))

for i in range(filas):
    row = []
    for j in range(columnas):
        
        row.append(random.randrange(0,100,1))
    matrix.append(row)
        
for row in matrix:
    print(" | ".join(f"{num:02d}" for num in row))

 

fin = time.time()


print(matrix[321][5])
print(fin-inicio)










