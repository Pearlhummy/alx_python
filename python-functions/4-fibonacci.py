def fibonacci_sequence(n):
    t=[]
    if n<=0:
        t=[]
    elif n==1:
        t=[0]
    else:
        t=[0,1]
        for i in range(1, n-1):
            t.append(t[i-1]+t[i])
    return(t)