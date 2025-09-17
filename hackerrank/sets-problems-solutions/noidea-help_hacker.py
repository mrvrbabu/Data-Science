# Read inputs
n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# Compute happiness
happiness = sum((i in A) - (i in B) for i in arr)

# Print result
print(happiness)
