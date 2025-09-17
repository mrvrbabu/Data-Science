# Enter your code here. Read inpfrom STDIN. Print output to STDOUT


ss = set(map(int, input().split()))
n = int(input())
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

if ss.issuperset(s1)  and ss.issuperset(s2):
	print(True)
else:
	print(False)
