my_set = {3,4,5}
print("my_set = ",my_set)

my_set2 = {"Hola", 23.3, False, True}
print("my_set2 = ",my_set2)

my_set3 = {3,3,2}
print("my_set3 = ",my_set3)

# my_set4 = {[1,2,3],4}
# print("my_set4 = ",my_set4)
    # 'Error'

# TYPES SETS
my_set4 = {(21,12,3),4}
print("my_set4 = ",my_set4)

empty_set = {}
print(type(empty_set))

empty_set = set()
print(type(empty_set))


# CASTING SETS
my_list = [1,1,2,3,4,4,5]
my_set_cast = set(my_list)
print(my_set_cast)

my_tuple = ("Hola", "Hola", "Hola", 1)
my_set_cast2 = set(my_tuple)
print(my_set_cast2)