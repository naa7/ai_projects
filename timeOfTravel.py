import matplotlib.pyplot as plt
import numpy as np

def timeOfTravel(speed, distance):
    time = speed*distance;
    return time;

def plot(speed,distance):
    xpoints = np.array(speed);
    ypoints = np.array(distance);
    
    font1 = {'family':'serif', 'color':'blue', 'size':20};
    font2 = {'family':'serif', 'color':'darkred', 'size':15};
    plt.title("Speed vs. Distance", fontdict=font1);
    plt.xlabel("Speed", fontdict=font2);
    plt.ylabel("Distance", fontdict=font2);
    plt.plot(xpoints,ypoints, 'o:r');
    plt.show();
#speed = int(input("Speed: "));
#distance = int(input("Distance: "));
#print(timeOfTravel(speed, distance));

def main():
    speed = list(range(1, 51, 10));
    distance = list(range(1, 501, 100));
    plot(speed,distance);

if __name__ == "__main__":
    main()