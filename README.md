# time-series-basics
Time Series basics - importing, cleaning, printing to csv

Note date files are synthetic data. 


data-import.py

    # The function init is used to import times and values from teh the csv file
    # The word low will be replaced with the value 40 and the word high will be replaced with the value 300
    
    # The function linear search is used to search the datafile for a key_time and then return the list of associated values
    
    # Added a binary search option. Could not get code to work to benchmark speed differences between linear search and binary search
    
    # The function roundTimeArray is used to round times to the nearest minute
    
    # printLargeArray function developed to create a csv which aligns the data in the zip objects based on key_file
    
    # Main function pulls in csv files, then creates two rounded versions. One is rounded to the nearest 5 minutes. The other is rounded to the nearest 15 minutes. Then the data is combined into two new csv files, one for the 5 min rounding, one for the 15 min rounding. 
    