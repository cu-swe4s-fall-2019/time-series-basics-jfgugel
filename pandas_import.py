import numpy as np
import pandas as pd
from functools import reduce
import datetime as dt

#import data from csv files to pandas dataframes
activity_small = pd.read_csv('./data/activity_small.csv')
basal_small = pd.read_csv('./basal_small.csv')
bolus_small = pd.read_csv('./data/bolus_small.csv')
cgm_small = pd.read_csv('./data/cgm_small.csv')
hr_small = pd.read_csv('./data/hr_small.csv')
meal_small = pd.read_csv('./data/meall_small.csv')
smbg_small = pd.read_csv('./data/smbg_small.csv')



#join the frames together with an inner join (left join default)
joinFrame = cgm_small([activity_small, basal_small, bolus_small, 
                      hr_small, meal_small, smbg_small], how='inner')

#rename columns
activity_small.rename(columns={"value":"activity_small"},inplace=True)
basal_small.rename(columns={"value":"basal_small"},inplace=True)
bolus_small.rename(columns={"value":"bolus_small"},inplace=True)
cgm_small.rename(columns={"value":"cgm_small"},inplace=True)
hr_small.rename(columns={"value":"hr_small"},inplace=True)
meal_small.rename(columns={"value":"meal_small"},inplace=True)
smbg_small.rename(columns={"value":"smbg_small"},inplace=True)


#fill in any nan values with 0
joinFrame.fillna(0,inplace=True)


#time stamps
cgm_small.index = pd.to_datetime(cgm.index)
#add a new column
cgm_small.insert(len(cgm_small.columns),'DT',cgm_small.index)
#get the difference between values, and add it as a new column
cgm_small.insert(len(cgm_small.columns),'DT_diff',cgm_small.DT.diff())

#make a column that rounds to nearest 15minute interval
cgm_small.insert(len(cgm_small.columns),'15min',cgm_small['DT'].dt.round('15min'))

#make a column that rounds to nearest 5minute interval
cgm_small.insert(len(cgm_small.columns),'5min',cgm_small['DT'].dt.round('5min'))

# group by new times, and get the means
rounded_cgm_small_15mins = cgm_Small.groupby('15min')['cgm_small'].mean()
rounded_cgm_small_5mins = cgm_Small.groupby('5min')['cgm_small'].mean()
