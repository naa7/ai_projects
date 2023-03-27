def add_it_up(num):
    if type(num) == int:
        i = 0;
        sum = 0;
        while i <= num:
            sum = sum + i;
            i = i + 1;
    else:
        sum = 0;
    return(sum);
 
print(add_it_up(3));
print(add_it_up(5));
print(add_it_up(7));
print(add_it_up('a'));
print(add_it_up("hi"));
print(add_it_up(-1));

