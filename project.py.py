import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns



# Rainfall data, yearly for timeseries plots

def main():

    df_1 = pd.read_csv("C:\\Users\DELL\Desktop\python_project\DATA_SET\Rainfall_yearly.csv")
    df_1 = df_1.rename(columns = {'SUBDIVISION':'State', 'JAN': 'Jan', 'FEB': 'Feb', 'MAR': 'Mar', 
                            'APR': 'Apr' , 'MAY': 'May', 'JUN': 'Jun', 'JUL': 'Jul', 'AUG': 'Aug', 'SEP': 'Sep', 'OCT': 'Oct'
                        , 'NOV': 'Nov', 'DEC': 'Dec', 'ANNUAL': 'Annual', 'YEAR': 'Year'})

    #df_1.head()
    df_1_year = df_1.groupby("Year")
    df_1_state = df_1.groupby("State")



    df_2 = pd.read_csv("C:\\Users\DELL\Desktop\python_project\DATA_SET\Rainfall_Districtwise.csv")
    df_2 = df_2.rename(columns= {'STATE_UT_NAME' : "State",'JAN': 'Jan', 'FEB': 'Feb', 'MAR': 'Mar', 
                        'APR': 'Apr' , 'MAY': 'May', 'JUN': 'Jun', 'JUL': 'Jul', 'AUG': 'Aug', 'SEP': 'Sep', 'OCT': 'Oct'
                        , 'NOV': 'Nov', 'DEC': 'Dec', 'ANNUAL': 'Annual'})

    dic = {
    'NORTH': ['JAMMU AND KASHMIR', 'HIMACHAL PRADESH', 'PUNJAB', 'CHANDIGARH', 'UTTARANCHAL', 'HARYANA', 'DELHI', 'UTTAR PRADESH', 'RAJASTHAN'],
    'WEST': ['GUJARAT', 'DAMAN AND DIU', 'DADRA AND NAGAR HAVELI', 'MAHARASHTRA', 'GOA'],
    'SOUTH': ['KARNATAKA', 'ANDHRA PRADESH', 'TAMIL NADU', 'KERALA', 'PUDUCHERRY', 'TELANGANA','LAKSHADWEEP', 'ANDAMAN And NICOBAR ISLANDS'],
    'EAST': ['ODISHA', 'WEST BENGAL', 'JHARKHAND', 'BIHAR'],
    'NORTHEAST': ['ARUNACHAL PRADESH', 'ASSAM', 'MANIPUR', 'MEGHALAYA', 'MIZORAM', 'NAGALAND', 'SIKKIM', 'TRIPURA'],
    'CENTRAL': ['MADHYA PRADESH', 'CHHATTISGARH']
    }

    # Create a new column 'Region' in the existing DataFrame and map the states/union territories with their regions
    #df_2['Region'] = df_2['State'].map({state: region for region, states in regions.items() for state in states})
    df_2["Region"] = df_2["State"].map({state: region for region, states in dic.items() for state in states})
    df_2["Region"]

    plot_yearly_rainfall(df_1)
    plot_annual_rainfall_by_state(df_1,lst)
    plot_top_rainfall_states(df_1)
    plot_avg_annual_rainfall(df_2)
    plot_bottom_rainfall_states(df_1)
    plot_avg_monthly_rainfall(df_2)
    plot_annual_rainfall_by_region(df_2,dic)
    


# df_1 = pd.read_csv("C:\\Users\DELL\Desktop\python_project\DATA_SET\Rainfall_yearly.csv")
# df_1 = df_1.rename(columns = {'SUBDIVISION':'State', 'JAN': 'Jan', 'FEB': 'Feb', 'MAR': 'Mar', 
#                         'APR': 'Apr' , 'MAY': 'May', 'JUN': 'Jun', 'JUL': 'Jul', 'AUG': 'Aug', 'SEP': 'Sep', 'OCT': 'Oct'
#                     , 'NOV': 'Nov', 'DEC': 'Dec', 'ANNUAL': 'Annual', 'YEAR': 'Year'})

# #df_1.head()
# df_1_year = df_1.groupby("Year")
# df_1_state = df_1.groupby("State")



# df_2 = pd.read_csv("C:\\Users\DELL\Desktop\python_project\DATA_SET\Rainfall_Districtwise.csv")
# df_2 = df_2.rename(columns= {'STATE_UT_NAME' : "State",'JAN': 'Jan', 'FEB': 'Feb', 'MAR': 'Mar', 
#                     'APR': 'Apr' , 'MAY': 'May', 'JUN': 'Jun', 'JUL': 'Jul', 'AUG': 'Aug', 'SEP': 'Sep', 'OCT': 'Oct'
#                     , 'NOV': 'Nov', 'DEC': 'Dec', 'ANNUAL': 'Annual'})

# #df_2.columns
# #df_2 = df_2.rename(columns="ST")


    



def plot_yearly_rainfall(df):
    """
    Plots the yearly rainfall and adds a horizontal line for the mean annual rainfall.

    Parameters:
    - df: DataFrame containing the necessary columns ('Year' and 'Annual').
    """
    plt.figure(figsize=(15, 5))

    # Group by year, sum the annual rainfall, and plot a line chart
    df.groupby(['Year'])['Annual'].sum().plot(kind='line', color='b')

    # Adding labels and title
    plt.ylabel('Yearly Rainfall')
    plt.xlabel('Year')
    plt.title('Yearly Rainfall (Overall)')

    # Add a horizontal line for the mean annual rainfall
    mean_rainfall = df.groupby(['Year'])['Annual'].sum().mean()
    plt.axhline(mean_rainfall, color='red', linestyle='--', label='Mean')

    # Add legend
    plt.legend()

    # Display the plot
    plt.show()

# Example usage:
# Replace 'your_dataframe' with the actual variable name of your DataFrame
# plot_yearly_rainfall(your_dataframe)

#plot_yearly_rainfall(df_1)








def plot_annual_rainfall_by_state(df, states_list):
    """
    Plots the annual rainfall for specified states and adds a horizontal line for the mean annual rainfall.

    Parameters:
    - df: DataFrame containing the necessary columns ('Year', 'Annual', 'State').
    - states_list: List of states for which the annual rainfall should be plotted.
    """
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 15))

    for ax, state in zip(axes.flatten(), states_list):
        # Select only the data for the current state
        data = df[df["State"] == state]
        ax = data.groupby(['Year'])['Annual'].sum().plot(kind='line', color='b', ax=ax)
        ax.axhline(data.groupby(['Year'])['Annual'].sum().mean(), color='gray', linestyle='--', label='Mean')
        ax.set_title(state, fontsize=12)
        ax.set_xlabel("Year")
        ax.set_ylabel("Yearly Rainfall (mm)")
        ax.legend()

    fig.suptitle("Annual Rainfall Region Wise over the Years", fontsize=18)

    # adjust the position of the main title
    fig.subplots_adjust(top=0.9)
    plt.tight_layout()
    plt.show()

# Example usage:
# Replace 'your_dataframe' with the actual variable name of your DataFrame
# Replace 'your_states_list' with the list of states you want to plot
# plot_annual_rainfall_by_state(your_dataframe, your_states_list)

lst = ["BIHAR","HARYANA DELHI & CHANDIGARH","PUNJAB","WEST UTTAR PRADESH"]
#lst = ["KERALA","HARYANA DELHI & CHANDIGARH","PUNJAB","WEST UTTAR PRADESH"]
#plot_annual_rainfall_by_state(df_1,lst)






def plot_top_rainfall_states(df, top_n=5):
    """
    Plots the top N states with the highest total annual rainfall over the years.

    Parameters:
    - df: DataFrame containing the necessary columns ('State', 'Annual').
    - top_n: Number of top states to display (default is 5).
    """
    plt.figure(figsize=(8, 4))

    # Group by state, sum the annual rainfall, sort in descending order, and select the top N states
    top_states = df.groupby(['State'])['Annual'].sum().sort_values(ascending=False).head(top_n)

    # Plotting the bar chart
    top_states.plot(kind='bar', color='g')

    # Adding labels and title
    plt.ylabel('Total Rainfall (mm)')
    plt.xlabel('Regions')
    plt.title(f'Top {top_n} Rain Receiving Regions Over the Years')

    # Display the plot
    plt.show()

# Example usage:
# Replace 'your_dataframe' with the actual variable name of your DataFrame
# plot_top_rainfall_states(your_dataframe)
    
#plot_top_rainfall_states(df_1)

        
    

def plot_avg_annual_rainfall(df):
    """
    Plots the average annual rainfall in all States and UT using Seaborn barplot.

    Parameters:
    - df: DataFrame containing the necessary columns ('State', 'Annual').
    """
    fig = plt.figure(figsize=(18, 28))
    ax = plt.subplot(2,1,1)
    ax = plt.xticks(rotation=90)
    ax = plt.title('Avg Annual rainfall in all States and UT')
    ax = sns.barplot(x='State', y='Annual', data=df) 

#plot_avg_annual_rainfall(df_2)






def plot_bottom_rainfall_states(df_1, n=8):
    plt.figure(figsize=(15,5))
    df_1.groupby(['State'])['Annual'].sum().sort_values(ascending=False).tail(8).plot(kind='bar', color = 'r')
    plt.ylabel('Total Rainfall')
    plt.title('Bottom 8 Rain Receiving States')

#plot_bottom_rainfall_states(df_1)





def plot_avg_monthly_rainfall(df):
    """
    Plots the average monthly rainfall for the specified DataFrame.

    Parameters:
    - df: DataFrame containing columns for each month ('Jan', 'Feb', ..., 'Dec').
    """
    plt.figure(figsize=(10, 5))

    # Calculate the mean for each month and plot the bar chart
    df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
        'Sep', 'Oct', 'Nov', 'Dec']].mean().plot(kind='bar')

    # Adding labels and title
    plt.xlabel('Months')
    plt.ylabel('Avg. Rainfall')
    plt.title('Avg. Monthly Rainfall Data')

    # Display the plot
    plt.show()

# Example usage:
# Replace 'your_dataframe' with the actual variable name of your DataFrame
# plot_avg_monthly_rainfall(your_dataframe)

#plot_avg_monthly_rainfall(df_2)




    # dic = {
    # 'NORTH': ['JAMMU AND KASHMIR', 'HIMACHAL PRADESH', 'PUNJAB', 'CHANDIGARH', 'UTTARANCHAL', 'HARYANA', 'DELHI', 'UTTAR PRADESH', 'RAJASTHAN'],
    # 'WEST': ['GUJARAT', 'DAMAN AND DIU', 'DADRA AND NAGAR HAVELI', 'MAHARASHTRA', 'GOA'],
    # 'SOUTH': ['KARNATAKA', 'ANDHRA PRADESH', 'TAMIL NADU', 'KERALA', 'PUDUCHERRY', 'TELANGANA','LAKSHADWEEP', 'ANDAMAN And NICOBAR ISLANDS'],
    # 'EAST': ['ODISHA', 'WEST BENGAL', 'JHARKHAND', 'BIHAR'],
    # 'NORTHEAST': ['ARUNACHAL PRADESH', 'ASSAM', 'MANIPUR', 'MEGHALAYA', 'MIZORAM', 'NAGALAND', 'SIKKIM', 'TRIPURA'],
    # 'CENTRAL': ['MADHYA PRADESH', 'CHHATTISGARH']
    # }

    # # Create a new column 'Region' in the existing DataFrame and map the states/union territories with their regions
    # #df_2['Region'] = df_2['State'].map({state: region for region, states in regions.items() for state in states})
    # df_2["Region"] = df_2["State"].map({state: region for region, states in dic.items() for state in states})
    # df_2["Region"]


def plot_annual_rainfall_by_region(df, region_dict):
    """
    Plots annual rainfall for each state in different regions.

    Parameters:
    - df: DataFrame containing the necessary columns ('State', 'Annual').
    - region_dict: Dictionary mapping states to their respective regions.
    """
    # Create a new column 'Region' in the existing DataFrame and map the states/union territories with their regions
    df["Region"] = df["State"].map({state: region for region, states in region_dict.items() for state in states})

    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 15))

    for ax, region in zip(axes.flatten(), region_dict.keys()):
        # Plotting the bar chart for each region
        ax = sns.barplot(x='State', y='Annual', data=df[df["Region"] == region], ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='center')
        ax.set_title(region, fontsize=12)
        ax.set_xlabel("States/UTs")
        ax.set_ylabel("Annual Rainfall (in mm)")

    fig.suptitle("Annual Rainfall Region Wise", fontsize=18)

    # Adjust the position of the main title
    fig.subplots_adjust(top=0.9) 
    plt.tight_layout()
    plt.show()

# Example usage:
# Replace 'your_dataframe' with the actual variable name of your DataFrame
# Replace 'your_region_dict' with the actual region dictionary
# plot_annual_rainfall_by_region(your_dataframe, your_region_dict)
#plot_annual_rainfall_by_region(df_2,dic)




if __name__ == "__main__":
    # print("hello")
    # plot_yearly_rainfall(df_1)
    # plot_annual_rainfall_by_state(df_1,lst)
    # plot_top_rainfall_states(df_1)
    # plot_avg_annual_rainfall(df_2)
    # plot_bottom_rainfall_states(df_1)
    # plot_avg_monthly_rainfall(df_2)
    # plot_annual_rainfall_by_region(df_2,dic)
    # print("HELLo000")
    main()







