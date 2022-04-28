# alkaline earth metals

earth_metals = ["Beryllium", "Magnesium", "Calcium", "Stronium", "Barium", "Radium"]

# to sort them alphabetically in ascending order
earth_metals.sort()

# to sort them in the descending order
earth_metals.sort(reverse=True)
earth_metals 

# lest put the elements in a tuple instead of a list
earth_metals = ("Beryllium", "Magnesium", "Calcium", "Stronium", "Barium", "Radium")
# since tuples are immutable objects, they cannot be changed and sorting changes things, so they cannot be sorted this way.

planets = [
	("Mercury", 2440, 5.43, 0.395)
	("Venus", 6052, 5.24, 0.723)
	("Earth", 6378, 5.52, 1.000)
	("Mars", 3396, 3.93, 1.530)
]
# to sort the planets based on their sizes, the second element in the planets list
size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)

density = lambda planet: planet[2]]
planets.sort(key=density)

# list.sort method changes the list, but what about tuples
# we can use the built-in function sorted()
earth_metals = ("Beryllium", "Magnesium", "Calcium", "Stronium", "Barium", "Radium")
sorted_earth_metals = sorted(earth_metals)
# creates a new list

sorted("Alphabetical") # sorts the characters of this string

