a=[]
b = int(input('ввести число критериев:'))#Ввод

for i in range(b):#создание таблицы
    a.append([])
    for j in range(b):
        a[i].append(0)
        
        
for i in range(b):#заполнение диагонали
    a[i][i]=1
    
    
for i in range(b):#ввод сравнения критериев
    for j in range(b):
        if a[i][j]==0:
            print('ввести число для сравнения ', i+1,' и ', j+1)
            a[i][j] =float(input())
            a[i][j] = round(a[i][j],2)
            a[j][i] = round(1/a[i][j],2)#заполнение обратной ячейки
            
print(a)

summ=[]
d=0

for i in range(b):#сумма строк
    summ.append(0)
    for j in range(b):
        summ[i]+=a[i][j]
        summ[i]=round(summ[i],2)

for i in range(b):
    d+=summ[i]
    d=round(d,2)


print(summ,"суммы по строкам")
print( d,"общая сумма")
weight=[]
for i in range(b):#расчет весовых коэффициентов
    weight.append(round(summ[i]/d,2))
    
print(weight, "веcовые коэффиценты")