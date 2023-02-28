def readList():
    List = input("Enter list values: ").split();
    List = list(map(int,List));
    return List;
    
def selectionSort(List):
    listSize = len(List);
    for i in range(listSize - 1):
        minimum = i;
        for j in range(i + 1, listSize):
            if List[j] < List[minimum]:
                minimum = j;
        List[i], List[minimum] = List[minimum], List[i];
    
    

def main():
    #List = readList();
    List = [5, 6,1, 2, 8, 9, 12, 18, 7, 10];
    sortedList = list(List);
    selectionSort(sortedList);
    print("Original list:", List);
    print("Sorted list:", sortedList);
    
if __name__ == "__main__":
    main();