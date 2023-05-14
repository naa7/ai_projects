def farenheit(temp_celcius):
    temp_farenheit = temp_celcius * (9/5) + 32;
    return temp_farenheit;

def celcius(temp_farenheit):
    temp_celcius = round((temp_farenheit - 32) * (5/9));
    return temp_celcius;

def userInput():
    print("Celcius & Farenheit Temperature Converter");
    temperature = input("Enter [temperature] [C/F], 32 C: ").split();
    temperatureValue = int(temperature[0]);
    temperatureUnit = str(temperature[1]);
    if temperatureUnit == 'C' or temperatureUnit == 'c':
        temp = farenheit(temperatureValue);
        print("Temperature:", str(temperatureValue) + str(temperatureUnit) + " =", str(temp) + "F");    
    elif temperatureUnit == 'F' or temperatureUnit == 'f':
        temp = celcius(temperatureValue);
        print("Temperature:", str(temperatureValue) + str(temperatureUnit) + " =", str(temp) + "C");    
   
def main():
    userInput();
if __name__ == "__main__":
    main();