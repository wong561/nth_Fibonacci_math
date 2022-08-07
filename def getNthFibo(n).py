

def getNthFibo(n):
   
    if n==1:
        return 0

    elif n==2:
        return 1

    else:
        
        x=5**.5
        p=((1+x)/2)**(n-1)
        q=((1-x)/2)**(n-1)
        a=(p+q)/x.round()
        

    return a


    
     
