# wap which will create a list all ellement divisible by 3 between 4and 25
lst=[]
for i in range(4,26):
    if((i%3)==0):
        lst.append(i)
print(lst)