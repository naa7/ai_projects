import matplotlib.pyplot as plt;
import numpy as np;
import random;

def farenheit(temp_c):
    temp_f = [];
    for i in temp_c:
        farenheit = round((i * (9/5) + 32),1);
        temp_f.append(farenheit);
    return temp_f;


def plot(temp_c, temp_f):
    x_points = np.array(temp_c)
    y_points = np.array(temp_f);
    
    font1 = {'family':'serif', 'color':'blue', 'size':20};
    font2 = {'family':'serif', 'color':'darkred', 'size':15};
    plt.title("Fahrenheit vs. Celcius", fontdict=font1);
    plt.xlabel("Celcius", fontdict=font2);
    plt.ylabel("Fahrenheit", fontdict=font2);
    plt.plot(x_points, y_points, 'og');
    plt.show();
    
def main():
    temp_c = [];
    while len(temp_c) < 11:
        tmp = random.randint(1,100);
        if tmp not in temp_c:
            temp_c.append(tmp);
    
    temp_f = farenheit(temp_c);
    print("Celcius:", temp_c);
    print("Farenheit:", temp_f);
    plot(temp_c, temp_f);

if __name__ == "__main__":
    main();