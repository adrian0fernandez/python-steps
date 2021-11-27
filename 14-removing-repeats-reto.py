# [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6] -> [1,2,3,4,5,6]

def remove_duplicates(some_list):
    my_set = set(some_list)
    return my_set

def run():
    random_list = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()