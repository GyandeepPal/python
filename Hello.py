# lst=[7,-4,-2,9,0,11,17,8,19,10]
# # print(lst[:-5:10])
# # print(lst[:-5:-10])

# # lst.append("Hello, World!")
# lst.insert(-9,74)
# lst1=[45,75,93]
# lst.extend(lst1)
# lst=lst+lst1
# print(lst)


# lst_sum=0
# lst = [5,3,2,1,4,8]
# for i in lst:
#    lst_sum +=i
#    ans=[]
# for i in lst:
#  ans.append(lst_sum-i)
# print(ans)
# print(lst)

lst=[[5,3,2,1,4,8],[1,2,3,4,5,6],[7,8,9,10,11,12]]
# ans = [23,21,57]
ans =[]
for i in lst:
     ans.append(sum(i))

print(ans)

# list=[[1,2,7,3,4,7],[2,9,4,7,5,7],[9,6,7,6,8,5,6],[7,5,3,7,8,5,4]]
# ans=[]
# for i in range(len(lst)):
#     if((i%2)==0):{

#         print()
#         }


# lst = [[3,2,1,8],[50,3,7,9],[2,3,7,8]]

# for i in range(len(lst)):
#     for j in range(len(lst[i])):
        
#         if lst[i][j] % 2 == 0:   # even
#             lst[i][j] -= 1
#         else:                    # odd
#             lst[i][j] += 1

# print(lst)
