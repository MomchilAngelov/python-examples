class AbstractFactory():
	
	def createProductDoor(self, price, quallity):
		raise NotImplementedError

	def createProductWindow(self, price, quallity):
		raise NotImplementedError


class ConcreteFactoryAudi(AbstractFactory):

	def createProductDoor(self, price, quallity):
		return ConcreteProductAudi().door(price, quallity)

	def createProductWindow(self, price, quallity):
		return ConcreteProductAudi().window(price, quallity)


class ConcreteFactoryBMW(AbstractFactory):

	def createProductDoor(self, price, quallity):
		return ConcreteProductBMW().door(price, quallity)

	def createProductWindow(self, price, quallity):
		return ConcreteProductBMW().window(price, quallity)


class AbstractProduct():

	def door(self, price, quallity):
		raise NotImplementedError

	def window(self, price, quallity):
		raise NotImplementedError

	def printProduct(self):
		print("Price: {0}\tQuallity: {1}".format(self.price, self.quallity))



class ConcreteProductBMW(AbstractProduct):

	def door(self, price, quallity):
		return BMWDoor(price, quallity)

	def window(self, price, quallity):
		return BMWWindow(price, quallity)


class ConcreteProductAudi(AbstractProduct):

	def door(self, price, quallity):
		return AudiDoor(price, quallity)

	def window(self, price, quallity):
		return AudoWindow(price, quallity)




class AudiDoor(AbstractProduct):
	def __init__(self, price, quallity):
		self.price = price
		self.quallity = quallity


class AudoWindow(AbstractProduct):
	def __init__(self, price, quallity):
		self.price = price
		self.quallity = quallity


class BMWDoor(AbstractProduct):
	def __init__(self, price, quallity):
		self.price = price
		self.quallity = quallity


class BMWWindow(AbstractProduct):
	def __init__(self, price, quallity):
		self.price = price
		self.quallity = quallity


def makeItEasier(pFactor, qFactor):
	CONCRETE.createProductDoor(pFactor * 10, qFactor * 20).printProduct()
	CONCRETE.createProductWindow(pFactor * 20, qFactor * 20).printProduct()

CONCRETE = ConcreteFactoryAudi()
makeItEasier(10, 1)

CONCRETE = ConcreteFactoryBMW()
makeItEasier(30, 5)
