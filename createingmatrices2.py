#trying matrices

def creatematrix():
    r=int(input('ENTER NUMBER OF ROWS'))
    c=int(input('ENTER NUMBER OF COLUMNS'))
    matrix=[]


    for i in range(r):
        row=[]
        for j in range(c):
            item=int(input('ENTER element'))
            row.append(item)
        matrix.append(row)

    #print(matrix)
    return matrix

    #for row in matrix:
    #   f=''
    #    for element in row:
    #        f=f+str(element)
    #    print(f)

"""
#Matrix multiplication
for row in matrix1:
    sum=0
    newrow=[]
    for j in range(len(matrix2)):
        for i in range(len(matrix1)):
            sum+= matrix1[i][]*matrix2[j][i]
        newrow.append(sum)
        sum=0   
    print(newrow)
"""
'''
#Matrix multiplication
matrix1=[[1,2],[3,4]]
matrix2=[[1,2,3],[4,5,6]]
newmatrix=[]
newrow=[]
r=0
c=0
for row in matrix1:
    sum=0
    try:
        for i in row:
            sum=sum+i*matrix2[r][c]
            r+=1
            newrow.append(sum)
        print(sum)
        sum=0
        c+=1
        newmatrix.append(newrow)
        print(newrow)
        newrow=[]
    except IndexError:
        print('Index Error')

print(newmatrix)
'''
matrix1=creatematrix()
#print(Mat1)
matrix2=creatematrix()

#CHeck feasibility to multiply 

noofrowmatrix1=len(matrix1)
print('Matrix 1 row:', noofrowmatrix1)
noofcolumnmatrix1=len(matrix1[0])
print('Matrix 1 coloumn:', noofcolumnmatrix1)
noofrowmatrix2=len(matrix2)
print('Matrix 2 row:', noofrowmatrix2)
noofcolumnmatrix2=len(matrix2[0])
print('Matrix 2 coloumn:', noofcolumnmatrix2)

if noofcolumnmatrix1==noofrowmatrix2:
    print('Matrix multiplication feasible')
    #RESULTANT SIZE
    print('Resultant size of matrix',noofrowmatrix1 ,'X',noofcolumnmatrix2)
    print('TOTAL MULTIPLICATIONS TO BE PERFORMED:', noofrowmatrix1*noofcolumnmatrix1*noofcolumnmatrix2)
    print('TOTAL ADDITIONS TO BE PERFORMED:',noofrowmatrix1*(noofcolumnmatrix1-1)*noofcolumnmatrix2)

    answer=input('Do you want to proceed with multiplication? (yes/no): ')
    if answer.lower()=='yes':
        #Matrix multiplication
        MATRIX2=[]
        for i in range(len(matrix2[0])):
            coloumn=[]
            for j in range(len(matrix2)):
                coloumn.append(matrix2[j][i])
            MATRIX2.append(coloumn)
        print('MATRIX2:', MATRIX2)
        MULTIPLIEDMATRIX=[]
        for coloumn in MATRIX2:
            newrow=[]
            for row in matrix1:
                sum=0
                for i in range(len(coloumn)):
                    sum+=row[i]*coloumn[i]
                newrow.append(sum)
            MULTIPLIEDMATRIX.append(newrow)
        print('MULTIPLIEDMATRIX:', MULTIPLIEDMATRIX)
        REALMULTIPLIEDMATRIX=[]
        for i in range(len(MULTIPLIEDMATRIX[0])):
            newrow=[]
            for coloumn in MULTIPLIEDMATRIX:
                newrow.append(coloumn[i])
            REALMULTIPLIEDMATRIX.append(newrow)
        print('REALMULTIPLIEDMATRIX:', REALMULTIPLIEDMATRIX)
    else:
        print('Multiplication cancelled')
else:
    print('Matrix multiplication not feasible')

'''
#Matrix multiplication using the coulumn method
matrix1=[[1,2],[3,4]]
matrix2=[[1,2,3],[4,5,6]]

for i in range(len(matrix2[0])):
    coloumn=[]
    for j in range(len(matrix2)):
        coloumn.append(matrix2[j][i])
    MATRIX2.append(coloumn)
print('MATRIX2:', MATRIX2)

MULTIPLIEDMATRIX=[]

for coloumn in MATRIX2:
    newrow=[]
    for row in matrix1:
        sum=0
        for i in range(len(coloumn)):
            sum+=row[i]*coloumn[i]
        newrow.append(sum)
    MULTIPLIEDMATRIX.append(newrow)
print('MULTIPLIEDMATRIX:', MULTIPLIEDMATRIX)

REALMULTIPLIEDMATRIX=[]
for i in range(len(MULTIPLIEDMATRIX[0])):
    newrow=[]
    for coloumn in MULTIPLIEDMATRIX:
        newrow.append(coloumn[i])
    REALMULTIPLIEDMATRIX.append(newrow)
print('REALMULTIPLIEDMATRIX:', REALMULTIPLIEDMATRIX)
'''