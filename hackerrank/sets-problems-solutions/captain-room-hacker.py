# Enter your code here. Read input from STDIN. Print output to STDOUT

# n = int(input())
# l = list(map(int, input().split()))
# # s = set(map(int, input().split()))
# print(l)
# s = set(l)
# print(len(l))
# print(s)
# # m = (len(s))
# # print(m)
# i = 0 
# for i in range(0, len(l)):
#     if s[i] in l: 
#         s.discard(i)
#         print(s)
# # for i in :
# # 	if item not in res:
# # 		res.discard(item)
# # print(res)

# # #print(s)

from collections import Counter
k = int(input().strip())

rooms = list(map(int, input().split()))

cnt = Counter(rooms)
print(cnt)
for room, freq in cnt.items():
    if freq == 1:
        print(room)
        break 
