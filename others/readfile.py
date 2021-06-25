filename = 'test.txt'

with open(filename) as file_object:
    # file_object.write('I love programming')
    for line in file_object:
        print(line.rstrip())

