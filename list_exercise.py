
d = [
    {'name':'Todd','phone':'555-1414','email':'todd@mail.net'},
    {'name':'Helga','phone':'555-1618','email':'helga@mail.net'},
    {'name':'Princess','phone':'555-3141','email':''},
    {'name':'LJ','phone':'555-2718','email':'lj@mail.net'}
]

# Function to get name of users whose phone number ends in 8.
def number(d):
    user = []
    for i in d:
        if i['phone'][-1] == str(8):
            user.append(i['name'])

    return user

# Function to get name of users whose email is blank.
def eid(d):
    username = []
    for i in d:
        if i['email'] == '':
            username.append(i['name'])

    return username

print(number(d))
print(eid(d))







