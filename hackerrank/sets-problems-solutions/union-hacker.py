# Enter your code here. Read input from STDN. Print output to STDOUT 

n = int(input())
eng = set(map(int, input().split()))
m = int(input())
fre = set(map(int, input().split()))
s = eng.union(fre)
print(len(s))
