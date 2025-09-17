# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())
ss = set(map(int, input().split()))

n = int(input())

user_input_act1 = input()
s1 = set(map(int, input().split()))
ss.intersection_update(s1)

user_input_act2 = input()
s2 = set(map(int, input().split()))
ss.update(s2)

user_input_act3 = input()
s3 = set(map(int, input().split()))
ss.symmetric_difference_update(s3)

user_input_act4 = input()
s4 = set(map(int, input().split()))
ss.difference_update(s4)

print(sum(ss))

# # Read input
# len_A = int(input())        # size of set A (not really needed in code)
# A = set(map(int, input().split()))

# N = int(input())            # number of operations

# for _ in range(N):
#     operation, size = input().split()
#     other_set = set(map(int, input().split()))

#     if operation == "update":
#         A.update(other_set)
#     elif operation == "intersection_update":
#         A.intersection_update(other_set)
#     elif operation == "difference_update":
#         A.difference_update(other_set)
#     elif operation == "symmetric_difference_update":
#         A.symmetric_difference_update(other_set)

# print(sum(A))
