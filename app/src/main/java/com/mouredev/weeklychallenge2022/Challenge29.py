def sortNumbers(arr,cond):
    if cond.lower()=="asc":
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i]<arr[j]:
                    aux=arr[i]
                    arr[i]=arr[j]
                    arr[j]=aux
    elif cond.lower()=="desc":
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i]>arr[j]:
                    aux=arr[i]
                    arr[i]=arr[j]
                    arr[j]=aux
    else:
        return "Error, se ingreso una condición incorrecta"
    return arr
print(sortNumbers([2, 3, 1, 8, 9],'Asc'))
print(sortNumbers([1, 8, 7, 1, 9],'Desc'))
print(sortNumbers([1, 8, 7, 1, 9],'Dasc'))
