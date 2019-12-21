import numpy as np


def prime_number(n):
    '''
    cek apakah prime number, return Boolean
    '''
    k = 0
    for i in range(2,n):
        if n % i == 0:
            k+=1
            break
    if k==1:
        return False
    elif k==0:
        return True

def bilang(cols,rows):
    n = 2
    mylist=[]

    for row in range(1,rows+1):
        rowlist=[]
        i=1
        while i<= cols:
            while True:
                if prime_number(n):
                    break
                else:
                    n+=1

            rowlist.append(n)
            i += 1
            n+=1

        mylist.append(rowlist)

    return np.array(mylist)
