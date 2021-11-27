def adding():
    print("ADDING")

    my_set = {1,2,3}
    print(my_set)

    # Adding element
    my_set.add(4)
    print(my_set)

    # Updating multiple elements
    my_set.update([1,2,5])
    print(my_set)

    # Updating multiple elements
    my_set.update((1,7,2), {6,8})
    print(my_set) 


def removing():
    print("\n")
    print("DELETING")

    my_set = {1,2,3,4,5,6,7} 
    print(my_set)

    # deleting existing element
    my_set.discard(1)
    print(my_set)
    
    # deleting existing element
    my_set.remove(2)
    print(my_set)
    
    # deleting an unexisting element
    my_set.discard(10)
    print(my_set)
    
    # deleting an unexisting element
    my_set.discard(12)
    print(my_set)

def pop():
    print("\n")
    print("DELETING")

    my_set = {1,2,3,4,5,6,7} 
    print(my_set)

    # deleting a random element
    my_set.pop() 
    print(my_set)

    # cleaning set
    my_set.clear()
    print(my_set)

# adding()
# removing()
pop()


