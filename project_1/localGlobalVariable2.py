def myFunc2 (one, two, three):
    # this will print the values of the variables
    # called from outside the method myFunc2. In this
    # case, the values called are global variables.
    # the global variable two will print first.
    # the global variable three will print second.
    # the global variable one will print last.
    print (one, two, three);

# declaring global variables, one, two and three
one = 1;
two = 2;
three = 3;

# this will print the values of the global variables
print (one, two, three);

# calling myFunc2 method using the global variables as
# method parameters. In this case, the global variable
# two will be used as the method's first parameter.
# three will be used as the method's second parameter.
# one will be used as the method's third parameter.
myFunc2 (two, three, one);

# this will print the values of the global variables
print (one, two, three);

'''
Output:
1 2 3
2 3 1
1 2 3
'''