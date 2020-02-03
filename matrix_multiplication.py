X = [[1,2,3],
     [4,5,6],
     [7,8,9]]
Y = [[1,2,3],
     [4,5,6],
     [7,8,9]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

##for i in range(len(X)):
##    
##    for j in range(len(Y[0])):
##        
##        for k in range(len(Y)):
##
##            result[i][j] = result[i][j] + X[i][k] * Y[k][j]

result = [[sum(a*b for a,b in zip(x_row,y_col)) for y_col in zip(*Y)] for x_row in X]

for r in result:

    print(r)

                       
