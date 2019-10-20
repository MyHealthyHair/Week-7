#1
filename = 'programming.txt'

with open(filename,'w') as file_object:
	file_object.write('I love programming.\n')
	file_object.write('I love creating new games.\n')

#2
filename = 'programming.txt'

with open(filename,'a') as file_object:
	file_object.write('I also love sth.\n')
	file_object.write('I love creating apps.\n')
