#ivan = ['пушене', 'пиене', 'тия три неща', 'коли', 'facebook', 'игри', 'разходки по плажа', 'скандинавска поезия']
#maria = ['пиене', 'мода', 'facebook', 'игри', 'лов със соколи', 'шопинг', 'кино']
#for val in [set(ivan) & set(maria)]:
#	print(val)

people = [
    {
        'name': "Мария",
        'interests': ['пътуване', 'танци', 'плуване', 'кино'],
        'age': 24,
        'gender': "female",
        "ex": ["Кирил", "Петър", "Андрей"],
    },
    {
        'name': "Диана",
        'interests': ['мода', 'спортна стрелба', 'четене', 'скандинавска поезия'],
        'age': 21,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Дарина",
        'interests': ['танци', 'покер', 'история', 'софтуер'],
        'age': 34,
        'gender': "female",
        "ex": ["Борис"],
    },
    {
        'name': "Лилия",
        'interests': ['покер', 'автомобили', 'танци', 'кино'],
        'age': 36,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Галя",
        'interests': ['пътуване', 'автомобили', 'плуване', 'баскетбол'],
        'age': 18,
        'gender': "female",
        "ex": ['Димитър'],
    },
    {
        'name': "Валерия",
        'interests': ['плуване', 'покер', 'наука', 'скандинавска поезия'],
        'age': 27,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Ина",
        'interests': ['кино', 'лов със соколи', 'пътуване', 'мода'],
        'age': 20,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Кирил",
        'interests': ['баскетбол', 'автомобили', 'кино', 'наука'],
        'age': 19,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Георги",
        'interests': ['автомобили', 'футбол', 'плуване', 'танци'],
        'age': 32,
        'gender': "male",
        'ex': [],
    },
    {
        'name': "Андрей",
        'interests': ['футбол', 'скандинавска поезия', 'история', 'танци'],
        'age': 26,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Емил",
        'interests': ['летене', 'баскетбол', 'софтуер', 'наука'],
        'age': 34,
        'gender': "male",
        'ex': ['Дарина'],
    },
    {
        'name': "Димитър",
        'interests': ['футбол', 'лов със соколи', 'автомобили', 'баскетбол'],
        'age': 22,
        'gender': "male",
        'ex': ['Галя'],
    },
    {
        'name': "Петър",
        'interests': ['пътуване', 'покер', 'баскетбол', 'лов със соколи'],
        'age': 23,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Калоян",
        'interests': ['кино', 'покер', 'пътуване', 'автомобили'],
        'age': 29,
        'gender': "male",
        'ex': [],
    },
]

class Human():
	def __init__(self, age, name, exes, interests, gender):
		self.age = age 
		self.name = name
		self.exes = exes
		self.interests = interests
		self.gender = gender

	def get_exes_count(self, other):
		return len(self.exes & other.exes)

	def get_common_interests(self, other):
		return self.interests & other.interests

	def age_difference(self, other):
		return abs(self.age - other.age)

	def different_gender(self, other):
		return not self.gender is other.gender

	def print_result(self, other):
		print("Влюбихме " + self.name + " и " + other.name + " на база това, че имат " + str(self.age_difference(other)) +
		" години разлика, и че те харесват ", end="")
		for key in self.get_common_interests(other):
			print(key, end=", ")
		print("")

def conditions(human1, human2):
	if not human1.age_difference(human2) < 7:
		return False
	if not human1.different_gender(human2):
		return False
	if not len(human1.get_common_interests(human2)) > 0:
		return False
	if not human1.get_exes_count(human2) == 0:
		return False
	return True

for human in people:
	this_human = Human(human.get('age'), human.get('name'), set(human.get('ex')), set(human.get('interests')), human.get('gender'))

	for other_humans in people:
		other_human = Human(other_humans.get('age'), other_humans.get('name'), 
		set(other_humans.get('ex')), set(other_humans.get('interests')), other_humans.get('gender'))
		
		if conditions(this_human, other_human):
			this_human.print_result(other_human)