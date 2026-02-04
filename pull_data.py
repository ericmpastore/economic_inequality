import pandas as pd
from fredapi import Fred
import matplotlib.pyplot as plt

def get_data():

    fred = Fred(api_key='d924e2e442ebd00887e0ad5687fdd531')

    gini_data = fred.get_series('SIPOVGINIUSA')
    gini_frame = gini_data.reset_index()
    gini_frame.columns = ['observation_date', 'SIPOVGINIUSA']

    gini_frame.to_csv('GINIUSA.csv', index=False)

    return gini_frame

def main():
    print(get_data().head())

if __name__ == '__main__':
    main()