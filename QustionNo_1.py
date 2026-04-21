lst=[[1,2,3],[3,5,4,3],[4,5,3,2]]
max=[]


for i in lst:
     lst1=sorted(i)
     max.append(lst1[- 1])
print(sum(max))