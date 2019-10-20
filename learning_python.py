filename = 'learning_python.txt'

#1
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

#2
print('\n')
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#3
print("\n")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
