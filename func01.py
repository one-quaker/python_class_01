import json


def save_hero(user_id, name='Spiderman'):
    if not user_id:
        print('User id can\'t be empty')
        return dict()
    if type(user_id) != int:
        print('User id must be integer')
        return dict()
    if not name:  # if name == '' or None or False or [] or {} or ()
        print('Name is empty, please specify some name')
        return dict()
    return dict(id=user_id, name=name)


# h0 = save_hero() # fails here
h1 = save_hero(name='Batman', user_id=5)
h2 = save_hero(1, name='Superman')
h3 = save_hero(user_id=10, name='Iron man')
h4 = save_hero(2, 'Hulk')


print(h1)
print(h2)
print(h3)
print(h4)


# save result of h1, h2, h3, h4 to file
# use json.dump or json.dumps
