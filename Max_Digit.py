def returnLargestDigit(n):
    max=0
    for i in str(n):
        if int(i)>max:
            max=int(i)
    return max

print(returnLargestDigit(579))