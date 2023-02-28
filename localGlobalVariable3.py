def myFunc3(one, two, three):
    
    # declaring variable sum which is given
    # by the addition of variables one and two
    # and subtracting that from three
    sum = (one + two) - three;
    
    # returning the variable sum to back to where the method
    # myFunc3() was called
    return sum;

def main():
    
    # declaring local variables
    one = 1;
    two = 2;
    three = 3;
    
    # declaring variable result which is the
    # returned value from myFunc3() method.
    # myFunc3() method is given three parameters.
    # the first parameter is the value of variable two.
    # the second parameter is the value of variable three.
    # the third parameter is the value of variable one
    result = myFunc3(two, three, one);
    
    # this will print the value of variable result which
    # should be 4 ((3+2)-1))
    print(result);

if __name__ == "__main__":
    main();
    
'''
Ouptput:
4
'''