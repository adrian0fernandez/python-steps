# local scope
def my_example_local_scope():
    y = 5
    print(y)

my_example_local_scope()


# Global scope
x = 6
def my_fuc():
    print(x)

def my_other_fuc():
    print(x)
my_fuc()
my_other_fuc()


# both scopes
z = 2
def both_fuc():
    z = 3
    print(z)
both_fuc()

print(z)

# complex scopes
a = 9
def my_scope():
    a = 8

    def my_another_scope():
        a = 7
        print(a)

    my_another_scope()

    print(a)
my_scope()
print(a)
