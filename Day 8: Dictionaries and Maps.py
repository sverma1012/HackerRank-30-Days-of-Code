# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
phonebook = dict()

# Get the input of names and numbers
for i in range(n):
    name, number = str(input()).split()
    phonebook[name] = number

# Get input of the names that the user is trying to search for.
val = str(input())

while val != None:
    try:
        if val in phonebook:
            print(val, '=', phonebook[val], sep='')
        else:
            print('Not found')

        val = str(input())
    except (EOFError):
        break