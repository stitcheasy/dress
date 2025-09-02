import numpy as np
import matplotlib.pyplot as plt

def curve(point1_x=1, point1_y=1, point2_x=5, point2_y=5, controlPt_x = 3, controlPt_y=6,typeofline='-', colorline='blue', curvelabel='Bezier Curve'):

        # Define the start and end points
        p0 = np.array([point1_x, point1_y])   # Start point
        p2 = np.array([point2_x, point2_y])   # End point

        # Define a control point
        p1 = np.array([controlPt_x, controlPt_y])  # Control point (adjust to change the shape of the curve)

        # Generate points along the Bezier curve
        t = np.linspace(0, 1, 100)

      

        # Compute the curve using the correct parentheses
        curve = ((1 - t)**2)[:, None] * p0 + 2 * ((1 - t) * t)[:, None] * p1 + (t**2)[:, None] * p2

        # Plot the curve
        plt.plot(curve[:, 0], curve[:, 1], linestyle=typeofline, color=colorline, ms=3, label=curvelabel, linewidth=4)
        #plt.plot(*zip(p0, p1, p2), label='Control Points')  # Show control points
          
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        #plt.title("Quadratic Bezier Curve between Two Points")
        #plt.show()

#curve(2,2,6,6,3,5, '--', 'pink',"curve label")