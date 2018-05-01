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

# Index example
print (avengers.index('Black Widow'))

# Remove from # Remove example
avengers.remove('Captain America')

print ("Remove Example: ")
for x in avengers:
    print (x)

# Insert at given position # insert example
avengers.insert(0, 'Spider Man')

print ("Insert Example: ")
for x in avengers:
    print (x)

# Count the number of values # Count example
how_many_spider_mans = avengers.count('Spider Man')

print ("Count Example Example: How Manny Spider Men are there?")
print (how_many_spider_mans)

# Nest Lists # GoTG list
gotg = ['Star Lord', 'Rocket', 'Groot', 'Drax', 'Gamora']

# Nested lists example
avengers.append(gotg)

print ("Append Nested List Example: ")
for x in avengers:
    print (x)

# Removes all the values from the Lists # Clear example
avengers.clear()

print ("Clear Example: ")
print (avengers)
