def readList():
    List = [];
    while True:
        userInput = int(input("Enter numbers: "));
        if userInput >= 0:
            List.append(userInput);
        else:
            break;

    return List;

def main():
    List = readList();
    print(List);
    
if __name__ == "__main__":
    main();