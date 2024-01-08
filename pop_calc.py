"""
Urban Population Calculator
•	import both pandas as pd and matplotlib.pyplot as plt
•	Read in the .csv with pandas and assign the dataframe as df_pop
•	avg_age = median of the [‘Median Age’] column
•	Filter your dataframe, creating two new dataframes df_older and df_younger where df_older is any countries where [‘Median Age’] > avg_age and df_younger contains countries where [‘Median Age’] < avg_age
•	Calculate the mean Urban Population %    [‘Urban Pop %’] for both the younger and older countries and compare with a graph in matplotlib.
"""
def age_urban(file_name):
    import pandas as pd
    import matplotlib.pyplot as plt
    df_pop = pd.read_csv(file_name)
    # print(df_pop)  
        
    avg_age = df_pop['Median Age'].median()

    df_older = df_pop[df_pop['Median Age'] > avg_age]
    df_younger= df_pop[df_pop['Median Age'] < avg_age]

    # print(len(df_younger))
    # print(len(df_older))
        
    x_val = "Younger", "Older"
    y_val = [df_younger['Urban Pop %'].mean(), df_older['Urban Pop %'].mean()]

    fig1 = plt.figure()
    plt.bar(x_val, y_val, color ='green', width = 0.7)    
    plt.xlabel("Countries")
    plt.ylabel("Urban Population Percentage")
    plt.title("City living for older vs. younger countries")
    plt.show()