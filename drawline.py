import matplotlib.pyplot as plt
import numpy as np


def line(point1_x=0.0, point1_y=0.0, point2_x=1.0, point2_y=1.0, typeofline='-', colorline='blue'):

        # Define the coordinates of the two points
        p1x=point1_x
        p1y=point1_y
        p2x=point2_x
        p2y=point2_y

        # Create arrays for x and y coordinates
        x_coords = np.array([p1x, p2x])
        y_coords = np.array([p1y, p2y])


        # Plot the line
        plt.plot(x_coords, y_coords, marker='o', linestyle=typeofline, color=colorline, ms=3, linewidth=4)
        

        #plt.show()

#line(point1_x=2, point1_y=2, point2_x=5, point2_y=5,typeofline="--", color='pink')
