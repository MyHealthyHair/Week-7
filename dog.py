#1
class Dog():
	"""一次模拟小狗的尝试"""
	
	def __init__(self, name, age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age
		
	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + ' is now sitting.')
		
	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title() + ' rolled over!')
	
my_dog = Dog('wille',6)
my_dog.sit()
my_dog.roll_over()

#2
class Dog():
	"""一次模拟小狗的尝试"""
	
	def __init__(self, name, age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age
		
	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + ' is now sitting.')
		
	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title() + ' rolled over!')
	
my_dog = Dog('wille',6)
your_dog = Dog('lucy',3)

print('\n')
print("my dog's name is " + my_dog.name.title() + '.')
print("my dog is " + str(my_dog.age) + ' years old.')
my_dog.sit()

print("\nyour dog's name is " + your_dog.name.title() + '.')
print("your dog is " + str(your_dog.age) + ' years old.')
your_dog.sit()
my_dog.roll_over()
