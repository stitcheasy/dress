import matplotlib.pyplot as plt


# Create a  grid  with a custom size and DPI 
def drawgrid(l=33.1, w=23.6, dpi=150):
        l=l
        w=w
        
        fig = plt.figure(figsize=(l, w), dpi=150) # Default size, higher DPI
        ax = fig.add_subplot(111)

        

        for x in range(int(l)+1):
                xpos = x
                ax.axvline(x=xpos, color='lightgray', linewidth=6)
                ax.text(xpos, 0 - 0.8, f"{x}\"", rotation=90, fontsize=18)

        for y in range(int(w)+1):
                ypos = y
                ax.axhline(y=ypos, color='lightblue', linewidth=6)
                ax.text(0-0.8, ypos, f"{y}\"", fontsize=18) 

        plt.title("Figure size in inches | " + "L " + str(l) + " inch" + " | " + "W " + str(w) + " inch", fontsize=38)
        
        return fig,ax
        #plt.show()
       

#drawgrid(50, 30, 150)
#drawgrid() for A1 size figure 