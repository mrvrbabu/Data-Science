# Enter your code here. Read input from STDIN. Print output to STDOUT

s1 = int(input())
m = set(map(int, input().split()))
s2 = int(input())
n = set(map(int, input().split()))

myset = m.difference(n)
myset.update(n.difference(m))
print(myset)
sorter_list = sorted(myset)
for i in sorter_list:
    print(i)
