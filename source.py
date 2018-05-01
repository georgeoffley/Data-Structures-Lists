# Firstpart, the basics

#Basic Lists # List example
list = [1,2,3]

print (list)

# Here we are creating our list. # Hero List
avengers = ['Iron Man','Captain America','Black Widow','The Hulk','Hawkeye','Thor', 'Falcon']

print ("Hero List example: ")
print (avengers)

# Print in loop # For Loop
print ("For Loop Example: ")
for x in avengers:
    print (x)

# Add to end of list #Stacking #Append example
avengers.append('Black Panther')

print ("Append Example: ")
for x in avengers:
    print (x)

# Remove from the last position # Pop example
avengers.pop()

print ("Pop Example: ")
for x in avengers:
    print (x)

# Remove from the last position # Pop index example
avengers.pop(2)

print ("Pop Index Example: ")
for x in avengers:
    print (x)

# Remove from
avengers.remove('Captain America')

print ("Remove Example: ")
for x in avengers:
    print (x)

# Insert at given position
avengers.insert(0, 'Spider Man')

print ("Insert Example: ")
for x in avengers:
    print (x)

# Count the number of values
how_many_spider_mans = avengers.count('Spider Man')

print ("Count Example Example: How Manny Spider Men are there?")
print (how_many_spider_mans)

# Nest Lists
gotg = ['Star Lord', 'Rocket', 'Groot', 'Drax', 'Gamora']

avengers.append(gotg)

print ("Append Nested List Example: ")
for x in avengers:
    print (x)

# Removes all the values from the Lists
avengers.clear()

print ("Clear Example: ")
print (avengers)
