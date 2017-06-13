class AbstractFactory():
	
	def createProduct1(self):
		raise NotImplementedError

	def createProduct2(self):
		raise NotImplementedError


class ConcreteFactoryAudi(AbstractFactory):

	def createProduct1(self):
		return ConcreteProductAudi().product1()

	def createProduct2(self):
		return ConcreteProductAudi().product2()


class ConcreteFactoryBMW(AbstractFactory):

	def createProduct1(self):
		return ConcreteProductBMW().product1()

	def createProduct2(self):
		return ConcreteProductBMW().product2()


class AbstractProduct():

	def eat(self):
		raise NotImplementedError

	def sleep(self):
		raise NotImplementedError


class ConcreteProductBMW(AbstractProduct):

	def product1(self):
		return 'BMW > Audi'

	def product2(self):
		return 'BMW > Audi2'


class ConcreteProductAudi(AbstractProduct):

	def product1(self):
		return 'Audi > BMW'

	def product2(self):
		return 'Audi > BMW2'



def makeItEasier():
	print(CONCRETE.createProduct1())
	print(CONCRETE.createProduct2())


CONCRETE = ConcreteFactoryAudi()
makeItEasier()

CONCRETE = ConcreteFactoryBMW()
makeItEasier()
