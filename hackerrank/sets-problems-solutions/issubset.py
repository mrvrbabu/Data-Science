# Enter your code here. Read input from STDIN. Print output to STDOUT
# Test if given set is a subset of another set

T = int(input())
#T = int(input("Enter the number of test cases "))
#a_num = int(input("Enter number of elements of set A : "))
#print(a_num)
i = 0 
for i in range(0, T):
    a_num = int(input())
    A = set(map(int, input().split()))
    #print(A)
    #b_num = int(input("Enter the number of elements of set B: "))
    b_num = int(input())
    B = set(map(int, input().split()))

    Z = A.issubset(B)
    if Z == True:
        #print("True, Set A is subset of Set B")
        print(True)
    else:
        #print("False, Set A is not a subset of Set B")
        print(False)
