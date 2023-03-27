#Farmer must move his items from one side of river (a) to the other side of river (b)
#His boat can only take one an at a time
#He cannot leave the fox and goose unattended and cannot leave
#goose and grain unattended
#he starts the process in a

def Move_a2b_with_item (item):
    a.remove (item)
    b.append (item)
    a.remove ("farmer")
    b.append ("farmer")

def Move_b2a_with_item(item):
    b.remove (item)
    a.append (item)
    b.remove ("farmer")
    a.append ("farmer")

def Move_a2b_alone ():
    a.remove ("farmer")
    b.append ("farmer")

def Move_b2a_alone ():
    b.remove ("farmer")
    a.append ("farmer")
    
def Mova2b ():

    if ("farmer" in a and "goose" in a and "fox" not in a and "grain" not in a):
        Move_a2b_with_item ("goose")
        print (a)
        print (b)
        print ("farmer has arrived with goose to b")

    elif ("farmer" in a and "fox" in a and "grain" in a and "goose" not in a):
        Move_a2b_with_item ("fox")
        print (a)
        print (b)
        print ("farmer has arrived with fox to b")
    
    elif ("farmer" in a and "goose" in a and "grain" in a and "fox" not in a):
        Move_a2b_with_item ("grain")
        print (a)
        print (b)
        print ("farmer has arrived with grain to b")
        
    elif ("farmer" in a and "fox" in a and "goose" in a and "grain" in a):
        Move_a2b_with_item ("goose")
        print (a)
        print (b)
        print ("farmer has arrived with goose to b")


def Movb2a ():
    
    if ("farmer" in b and "goose" in b and "fox" in b and "grain" not in b):
        Move_b2a_with_item ("goose")
        print (a)
        print (b)
        print ("farmer has arrived back to a with goose")
        
    elif ("farmer" in b and "fox" in b and "grain" in b and "goose" not in b):
        Move_b2a_alone ()
        print (a)
        print (b)
        print ("farmer has arrived back to a alone")
    
    elif ("farmer" in b and "goose" in b and "fox" not in b and "grain" not in b):
        Move_b2a_alone ()
        print (a)
        print (b)
        print ("farmer has arrived back to a alone")

            
#initial state is where farmer and his position are on a and nothing on b
a = ["farmer", "fox", "goose", "grain"]
b=[]
print (a)
print (b)

#Start process by farmer moving an item from a to b
#then coming back to get more items
#continue until no more items left in a

while len (a) !=0:
    Mova2b ()
    Movb2a ()
print ("farmer has transferred all items from a to b intact")   
    
       


#while len (a) != 0:
#   b.append ('farmer')
#   b.extend ('goose')
#   a.clear()

#   a.remove ("farmer")
#   a.remove ("goose")
 #  print (a)
 #  print (b)
#   b.remove ("farmer")
#   a.extend ("farmer")
#   print (a)
#   print (b)
#   b.extend ("farmer", "fox")
#   a.remove ("farmer", "fox")
#   print (a)
#   print (b)
#   a.extend ("farmer", "goose")
#   b.remove ("farmer", "goose")
#   print (a)
#   print (b)
#   b.extend ("farmer", "fox")
#   a.remove ("farmer", "fox")
   
 
print (a)
print (b)
