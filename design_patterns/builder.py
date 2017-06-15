class CarBuilder():

	def __init__(self):
		self.car = []

	def buildExhaust(self):
		self.car.append('Exhaust')

	def buildTires(self):
		self.car.append('Tires')

	def buildSteeringWheel(self):
		self.car.append('Steering Wheel')

	def returnCar(self):
		return self.car

	def clearCar(self):
		self.car = []


class ShowRoom():

	def __init__(self, builder):
		self.cars = []
		self.builder = builder

	def buildCarAudi(self):
		self.builder.buildExhaust()
		self.builder.buildSteeringWheel()
		self.builder.buildTires()
		self.cars.append(self.builder.returnCar())
		self.builder.clearCar()
	
	def buildCarBMW(self):
		self.builder.buildExhaust()
		self.builder.buildSteeringWheel()
		self.builder.buildTires()
		self.builder.buildTires()
		self.builder.buildTires()
		self.builder.buildTires()
		self.cars.append(self.builder.returnCar())
		self.builder.clearCar()

	def print(self):
		for car in self.cars:
			for part in car:
				print(part, end=' ')

			print()


class RallyRace():

	def __init__(self, builder):
		self.cars = []
		self.builder = builder
		for x in range(20):
			self.buildRaceCar()

	def buildRaceCar(self):
		self.builder.buildExhaust()
		self.builder.buildExhaust()
		self.builder.buildExhaust()
		self.builder.buildExhaust()

		self.cars.append(self.builder.returnCar())
		self.builder.clearCar()

	def print(self):
		for car in self.cars:
			for part in car:
				print(part, end = ' ')

			print()

carBuilder = CarBuilder()
showRoom = ShowRoom(carBuilder)
rallyRace = RallyRace(carBuilder)

showRoom.buildCarBMW()
showRoom.buildCarAudi()
showRoom.print()

print('*' * 100)
rallyRace.print()