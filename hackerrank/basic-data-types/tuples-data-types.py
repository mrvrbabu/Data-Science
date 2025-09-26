if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(integer_list)
    tup = tuple(integer_list)
    print(tup)
    print(hash(tup))
