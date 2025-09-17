
def average(array):
    # your code goes here
    hgt = set(arr)
    n = len(hgt)
    total = sum(hgt)
    avg = total / n 
    return avg 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
   # print(set(arr))
