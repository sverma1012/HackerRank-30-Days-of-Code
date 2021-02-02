# Goal: Let's Review

# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

# Iterate through each inputted string

for i in range(T):
    even = ''
    odd = ''
    s = str(input())

    for i in range(len(s)):
        if (i % 2 == 0):
            even = even + s[i]
        else:
            odd = odd + s[i]

    print(even, odd)