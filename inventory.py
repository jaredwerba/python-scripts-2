inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Steps 01 // 02 // 03
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
# Steps 04 // 05
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

#Think of Inventory as a book, your key's are the chapters and the contents are the pages contained. You must refer to each chapter of the book when calling a function or making changes.

print inventory
