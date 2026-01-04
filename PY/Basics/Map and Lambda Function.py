cube = lambda x: x**3

# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

def fibonacci(n):
    # return a list of fibonacci numbers
    if(n == 0):
        return []
    if n == 1:
        return [0]
    l = [0] * n
    l[0] = 0
    l[1] = 1
    """
    n = 5
    [0, 1, 1, 2, 3]
    """
    for i in range(2, n):
        l[i] = l[i-1] + l[i-2]
    return l;

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))