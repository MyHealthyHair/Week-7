class User():
	
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		
	def describe_user(self):
		print(self.first_name.title() + ' ' + self.last_name.title() + 'is ' + str(self.age) +' years old.')
		
	def greet_user(self):
		print('Hello, ' + self.first_name.title() + ' ' + self.last_name.title() + '.')
		
amy = User('amy', 'brone' ,17)


amy.describe_user()
amy.greet_user()


