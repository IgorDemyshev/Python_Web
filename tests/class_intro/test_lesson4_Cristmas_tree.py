import random
 #    *
 #   ***
 #  *****
 #    |

# height_of_tree = 3
# print(' ' * 3 + '*')
# print(' ' * 2 + '*' * 3)
# print(' ' + '*' * 5)

def make_tree(height_of_tree: int = random.randint(2,12), symbol: str = '&'):
    for branch in range(height_of_tree):
        print(' ' * (height_of_tree - branch) + symbol * (1 + (branch * 2)))
      #   max = height_of_tree * 2
      #   print(' ' * (height_of_tree - branch) + '*' * (max - (max - branch * 2 - 1)))
    print(' ' * height_of_tree + '|')

make_tree()
make_tree(7, '$')
make_tree(random.randint(3,10), '%')


#arg -  argument(you put * before arg, fe *other);  kwargs - key, value pair(fe **other)

def register(name, gender=None, race='', *other, **stuff):
    print(f"Hello {name}!")
    if gender:
        print(f"You are a {gender}")
    if race:
        print(f"Your race is '{race}'")
    for i in other:
        print(f"... and you are {i}")

    for (k, v) in stuff.items():
        print(f"... you {k} is {v}")

    #or
    # for item in stuff.items():
    #     print(f"... your {item[0]} is {item[1]}")


# register('Jane')
# register('Bob', 'male')
# register('Jessice', None, 21, 170, 'white', '408-888-1111')
# register('Jessice', None, 'hispanic', 21, 'white', height=170, cell='408-888-1111')
register(
    race='white',
    gender='male',
    address='123 Apple Ln. Tree, CA',
    name='Steve'
)
register(
    race=123,
    gender=True,
    name='Steve'
)