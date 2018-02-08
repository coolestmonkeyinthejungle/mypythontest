a=[]
for i in range(int(input("Введите размер массива: "))):
    a.append(int(input("Введите значения элемента a: ")))
for x in range(len(a)):
    for y in range (len(a)-x-1):
        if(a[y]>a[y+1]):
            a[y],a[y+1]=a[y+1],a[y]
print(a)

