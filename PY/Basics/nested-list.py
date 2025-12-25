if __name__ == '__main__':
    nums = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nums.append([name, score])
        
    grades = sorted(set([it[1] for it in nums]))
    secondLowVal = grades[1]
    ans = sorted([it[0] for it in nums if it[1] == secondLowVal])
    for it in ans:
        print(it)
# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true