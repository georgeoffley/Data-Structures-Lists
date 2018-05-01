# Firstpart, the basics

#Basic Lists
list = [1,2,3]

print (list)

# Here we are adding things to a list using a CSV file
avengers = ['Iron Man','Captain America','Black Widow','The Hulk','Hawkeye','Thor', 'Falcon']

print (avengers)

# Add to end of list
avengers.append('Black Panther')

print (avengers)

# Remove from
avengers.remove('Captain America')

print (avengers)

# Insert at given position
avengers.insert(0, 'Spider Man')

print (avengers)

# Remove from the last position
avengers.pop()

print (avengers)

# Count the number of values
how_many_spider_mans = avengers.count('Spider Man')

print (how_many_spider_mans)

# Nest Lists
gotg = ['Star Lord', 'Rocket', 'Groot', 'Drax', 'Gamora']

avengers.append(gotg)

print (avengers)

# Removes all the values from the Lists
avengers.clear()

print (avengers)
