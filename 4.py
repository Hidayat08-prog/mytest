def sort_array(data):
    k=1
    for i in range(0,len(data)):
        array1=data[i]
        for j in range(i,len(data)):
            array2=data[j]
            if len(data[i])>len(data[j]):
                data[i]=array2
                data[j]=array1
                array1=data[i]

    for i in range(0,len(data)):
        data[i].sort()
    return data
