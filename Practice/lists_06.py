users = ['Naim', 'Alam', 'Nisa']

data = ['Naim', 20, True]

emptylist = []

print("Naim" in emptylist)

print(users[0])
print(users[-2])

print(users.index('Nisa'))

print(users[0:2])
print(users[0:])
print(users[-3:-1])

print(len(data))

users.append('NewName')
print(users)

users += ["Abul"]
print(users)

users.extend(['Hello', 'Hi'])
print(users)

users.insert(1, 'Kalam')
print(users)

users[2:2] = ['Jhon', 'Snow']
print(users)

users[1:3] = ['Kal', 'Al']
print(users)

users.remove('NewName')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['adam']
print(users)
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Nisa", True])
print(mylist)

# Tuples

myTuple = tuple(("ahmed", 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(myTuple)
print(type(myTuple))
print(type(anothertuple))

newlist = list(myTuple)
newlist.append("Alam")
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
