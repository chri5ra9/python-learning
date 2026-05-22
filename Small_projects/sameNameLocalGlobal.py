def spam():
    global eggs
    eggs = 'spam' # This is a global variable.

def bacon():
    eggs = 'bacon' #this is a local variable

def ham():
    print(eggs) #this is a global variable

eggs = 'global' #This is a global variable

spam()
print(eggs)
