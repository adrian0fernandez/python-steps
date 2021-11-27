def union():
    my_set1 = {3,4,5}
    my_set2 = {5,6,7}

    my_set3 = my_set1 | my_set2
    print("Union result is: ", my_set3)


def intersction():
    my_set1 = {3,4,5}
    my_set2 = {5,6,7}

    my_set3 = my_set1 & my_set2
    print("Intersection result is: ", my_set3)


def difference():
    my_set1 = {3,4,5}
    my_set2 = {5,6,7}

    my_set3 = my_set1 - my_set2
    print("Difference result is: ", my_set3)

def simetric_difference():
    my_set1 = {3,4,5}
    my_set2 = {5,6,7}

    my_set3 = my_set1 ^ my_set2
    print("Simetric Diference result is: ", my_set3)


union()
intersction()
difference()
simetric_difference()