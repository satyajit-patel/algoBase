

def split_and_join(line):
    """
    join  - separator.join(iterable) - returns single string
    split - iterable.split(separator) - returns list of strings
    """
    splited = line.split(" ") # ["this", "is" , "a", "string"]
    joined = "-".join(splited) # "this-is-a-string"
    return joined

# https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)