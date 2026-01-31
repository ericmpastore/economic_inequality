import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def render_plot(csv_file='GINIUSA.csv'):
    """
    Docstring for render_plot

    EPastore 01/30/26, Render plot reads data from csv file, parses, and shows plot
    
    :param csv_file: Parameter identifies file to read source data
    """
    # read csv parameter into dataframe, EPastore 01/30/26
    gini_frame = pd.read_csv(csv_file)

    # convert dates to full dates, EPastore 01/31/26
    gini_frame['observation_date'] = pd.to_datetime(gini_frame['observation_date'])

    x = gini_frame['observation_date']
    y = gini_frame['SIPOVGINIUSA']

    plt.plot(x,y)
    plt.ylim(bottom=0)
    plt.tight_layout()
    # for i in range(len(x)):
    #     plt.annotate(str(int(y.iloc[i])), xy=(x.iloc[i], y.iloc[i]), 
    #              xytext=(0, 5), textcoords='offset points', 
    #              ha='center', fontsize=9)
    plt.show()
    


def main():
    render_plot()

if __name__ == "__main__":
    main()