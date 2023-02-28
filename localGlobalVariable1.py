def myFunc1():
    
    # defining a local variable one
    # a local variable changes the value of one within
    # the method myFunc1(), but does not change the value
    # of the global variable, one, value
    one = -1;
    
    # this will print the local value of variable one and
    # the value of the global variable two
    print(one,two);


# one and two are global varaibles
one = 1;
two = 2;

# this will print the global varaibles, one and two
print(one,two);

# calling myFunc1() method which will print the local
# variable one and the global variable two
myFunc1();

# this will print the global variables, one and two
print(one,two);

'''
Output:
1 2
-1 2
1 2
'''