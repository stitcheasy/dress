import matplotlib.pyplot as plt


# Create a  grid  with a custom size and DPI 
def drawgridM(l=33.1, w=23.6, dpi=150, shift=0.8,linewidth=0.8, fontsize=6):
        l=l
        w=w


        
        fig = plt.figure(figsize=(l, w), dpi=150) # Default size, higher DPI
        ax = fig.add_subplot(111)
        plt.rc('legend',fontsize=20,  loc='upper right')
        plt.yticks(fontsize=25, rotation=0)
        plt.xticks(fontsize=25, rotation=0)

        for x in range(int(l)+1):
                xpos = x
                ax.axvline(x=xpos, color='lightgray', linewidth=linewidth)
                ax.text(xpos, 0 - shift, f"{x}\"", rotation=90, fontsize=fontsize)
                
        for y in range(int(w)+1):
                ypos = y
                ax.axhline(y=ypos, color='lightblue', linewidth=linewidth)
                ax.text(0-shift, ypos, f"{y}\"", fontsize=fontsize) 

        plt.title("Figure size in inches | " + "L " + str(l) + " inch" + " | " + "W " + str(w) + " inch", fontsize=fontsize*2)
        
        #plt.show()
        return fig,ax
      
       

#drawgridM(50, 30, 150, 0.6, 0.7, 7)

#drawgrid() for A1 size figure 
