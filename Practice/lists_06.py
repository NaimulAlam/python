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
