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
    plt.title('GINI Coefficient 1963-2023')
    
    # Label once per N years (adjust interval as needed)
    label_interval = 5  # Change to 10 for every 10 years
    for i in range(len(x)):
        year = x.iloc[i].year
        if year % label_interval == 0:  # Label years divisible by interval
            plt.annotate(f'{y.iloc[i]:.1f}', xy=(x.iloc[i], y.iloc[i]),
                     xytext=(0, 5), textcoords='offset points',
                     ha='center', fontsize=8)
            
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)

    # Remove y axis scale completely
    plt.yticks([])
    plt.tight_layout()
    plt.show()
    


def main():
    render_plot()

if __name__ == "__main__":
    main()