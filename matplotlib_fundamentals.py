import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#data visualization with matplotlib course :
#create line charts , bar charts , histograms , scatter plots and more
#u can customize the charts with different colors , markers and styles

#plots, style, lapeling, title and grid
def lesson_1():
    pass
    x = np.array([2023,2024,2025,2026])
    y = np.array([1,10,20,4])

    style = dict(color = "#700000"
            , marker = "."
            , markersize = 15
            , markerfacecolor = "#ff0000" 
            , markeredgecolor = "#ff0000"
            , linestyle = "solid"
            , linewidth = 3) #pack of style properties
            #for unpack use ** before style 

    plt.plot(x,y, **style) 
    # this for creating line chart x axis and y axis
    plt.title("first line chart",
             fontsize = 20,
             family = "arial",
             fontweight = "bold") # this for adding title to the chart
    plt.xlabel("year") # this for adding label to x axis
    plt.ylabel("value") # this for adding label to y axis
    plt.grid(axis="y",
            linewidth = 2) # this for adding grid to the chart
    plt.show() # this for displaying the chart
 

#bar charts 
def lesson_2():
    pass
    courses = np.array(["data structures","logic","diffrential"
                       ," comunication ","human rights","propabilty"])
    grades = np.array([(100-92),5,(100-97),1,0.5,6])

    barstyle = dict(color = "#168ab8")  

    plt.bar(courses,grades, **barstyle) #vertical bar chart
    #plt.barh(courses,grades, **barstyle) #horizontal bar chart
    plt.title("grades bar chart",
               fontsize = 20,
               family = "arial",
               fontweight = "bold")

    plt.xlabel("courses",
               fontsize = 20,
               family = "arial",
               fontweight = "bold")
    plt.ylabel("grades",
               fontsize = 20,
               family = "arial",
               fontweight = "bold")           

    plt.show()           

#pie charts
def lesson_3():
    pass
    colleges = np.array(["engineering","medicine",
                         "computer scince","teeth"])
    students = np.array([8,8,6,4])                     
    
    
    plt.pie(students, labels=colleges,
                      autopct="%1.1f%%",
                       explode = (0,0,0.2,0),
                       shadow = True)

    plt.title("louisville intern",
               fontsize = 20,
               family = "arial",
               fontweight = "bold",
               )

    plt.show()


#scatter graph
def lesson_4():
    pass
    x = np.array([1,2,3,4,5])
    y = np.array([2,3,5,7,11])
    plt.scatter(x,y, color = "#168ab8", marker = "o", s = 200) #s for size of the marker
    plt.title("scatter plot",
               fontsize = 20,
               family = "arial",
               fontweight = "bold",
               )
    plt.xlabel("x axis",
               fontsize = 20,
                family = "arial",
                fontweight = "bold",
                )
    plt.ylabel("y axis",        
               fontsize = 20,
                family = "arial",
                fontweight = "bold",
                )
    plt.grid() # this for adding grid to the chart
    plt.show()



#histogram
def lesson_5():
    pass
    scores = np.random.normal(loc = 80, scale = 10, size = 100)
    scores = np.clip(scores, 0, 100) # scores between 0 and 100
    
    plt.hist(scores, bins = 20,
             color = "#53f594",
             edgecolor = "black")


    plt.title("scores histogram",
               fontsize = 20,
               family = "arial",
               fontweight = "bold",
               )
    plt.xlabel("scores",
               fontsize = 20,
                family = "arial",
                fontweight = "bold",
                )
   
 
    plt.show()


#supblots
def lesson_6():
    pass
    x = np.array([1,2,3,4,5])
    y1 = np.array([1,4,9,16,25])
    

    figure, axes = plt.subplots(1,2, figsize=(10,5)) # 1 row , 2 columns , first plot
    axes[0].plot(x,y1, color = "#168ab8")
    axes[0].set_title("NUMBER 1",
                         fontsize = 20,
                         family = "arial",
                         fontweight = "bold",
                         )
    axes[1].plot(x,x**2, color = "#ff0000") 
    axes[1].set_title("NUMBER 2",
                         fontsize = 20,
                         family = "arial",
                         fontweight = "bold",
                         )
   
  
   
    plt.tight_layout()
    plt.show()  


  
