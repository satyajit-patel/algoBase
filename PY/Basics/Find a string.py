def count_substring(string, sub_string):
    init = 0;
    n = len(string)
    m = len(sub_string)
    count = 0
    
    for i in range(n):
        if(i-init+1 == m):
            substr = string[init:i+1]
            if(substr == sub_string):
                count += 1
            init += 1
    
    return count

# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)