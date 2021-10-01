#calculator.py

def sum(m, n):
    result = m

    if n<0:
        for i in range(abs(n)):
            result -= 1
    else:
        for i in range(n):
            result += 1
    
    return result



def divide(m, n):
    #to do
    if n == 0:
        print("ERROR: cannot divide by 0")
        return 0

    isNeg_n = 0
    isNeg_m = 0
    if n < 0:
        isNeg_n = 1
        n = -n

    if m < 0:
        isNeg_m = 1
        m = -m

    i = 0
    while m > 0:
        m = m - n
        if(m >= 0):
            i = i + 1
    
    if (isNeg_n == 0 and isNeg_m == 1) or (isNeg_n == 1 and isNeg_m == 0):
        return -i
    else:
        return i



def multiply(m,n):
    if n == 0 or m == 0:
        return 0
    
    tmp_sum = 0
    for i in range(abs(n)):
        tmp_sum = tmp_sum + abs(m)
    
    if (n < 0 and m < 0) or (n>0 and m>0):
        return abs(tmp_sum)
    elif (n < 0 and m > 0) or (n > 0  and m < 0):
        return -abs(tmp_sum)



def MCD(m,n):
    while n != 0:
        m, n = n, m % n
    return m

