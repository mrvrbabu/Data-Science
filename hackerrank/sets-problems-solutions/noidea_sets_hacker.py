# # Enter your code here. Read input from STDIN. Print output to STDOUT 

# nlist = list()
# nlist = input() 
# nset = set(map(int, input().split()))
# nint = list()
# nint = list(map(int, input().split())) 

# mint = list()
# mint = list(map(int, input().split()))


# happiness = sum((i in nint) - (i in mint) for i in nset) 

# print(happiness)
# # for i in range(0,len(nint)):
# #         if nint[i] in nset:
# #                 happiness += 1
# # mint = list()
# # mint = list(map(int, input().split())) 
# # j = 0
# # nothappy = 0 
# # for j in range(0, len(mint)):
# # 	#print(mint[j])
# # 	if mint[j] in nset:
# # 		nothappy += 1 
# # print(happiness - nothappy)



m, n = map(int, input().split())
arr = list(map(int, input().split()))
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

happiness = sum((i in s1) - (i in s2) for i in arr)
print(happiness)