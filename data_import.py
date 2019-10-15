import csv
import dateutil.parser
from os import listdir
from os.path import isfile, join
import argparse
import datetime


class Import Data

"Function retrieves times and values from csv file"
def __init__(self, data_csv):
        self._time = []
        self._value = []
        self._roundtime = []
        self._roundtimeStr = []
        with open(data_csv, "r") as fhandle:
            reader = csv.DictReader(fhandle)
            for row in reader:
                try:
                    self._time.append(dateutil.parser.parse(row['time']))
                except ValueError:
                    print('Bad input format for time')
                    print(row['time'])
                self._value.append(row['value'])
            
            fhandle.close()
        
        "Added a function to replace the word low with the value 40 and the word high with the value 300"
             with open(data_csv, "r") as: replacement:
                replacement = reader\.replace("low", 40)
                replacement = reader\.replace("high", 300)            
            fhandle.close()
        
   
# linear search function to search for key_time and return associated value
    def linear_search_value(self, key_time):
        for i in range(len(self._roundtimeStr)):
            curr =  self._roundtimeStr[i]
            if key_time == curr:
                return self._value[i]

        print('invalid time')

        return -1
        
        
        
        # return list of value(s) associated with key_time
        # if none, return -1 and error message

    def binary_search_value(self,key_time):
        # optional extra credit
        # return list of value(s) associated with key_time
        # if none, return -1 and error message

# creation of a round Time Array to round times to nearest minute
def roundTimeArray(obj, res):
            for times in self._time:
            minminus = datetime.timedelta(minutes = (times.minute % resolution))
            minplus = datetime.timedelta(minutes=resolution) - minminus
            if (times.minute % resolution) <= resolution/2:
                newtime = times - minminus
            else:
                newtime=times + minplus        
               
                
            self._roundtime.append(newtime)
            self._roundtimeStr.append(newtime.strftime("%m/%d/%Y %H:%M"))


def printArray(data_list, annotation_list, base_name, key_file):

def printLargeArray(data_list, annotation_list, base_name, key_file):
    base_data = []
    key_idx = 0
    for i in range(len(annotation_list)):
        if annotation_list[i] == key_file:
            base_data = zip(data_list[i]._roundtimeStr, data_list[i]._value)
            print('base data is: '+annotation_list[i])
            key_idx = i
            break            
        if i == len(annotation_list):
            print('Key not found')            

    file=open(base_name+'.csv','w')
    file.write('time,')
    
    file.write(annotation_list[key_idx][0:-4]+', ')

    non_key = list(range(len(annotation_list)))
    non_key.remove(key_idx)

    for idx in non_key:
        file.write(annotation_list[idx][0:-4]+', ')
    file.write('\n')

    for time, value in base_data:
        file.write(time+', '+value+', ')
        for n in non_key:
            if time in data_list[n]._roundtimeStr:
                file.write(str(data_list[n].linear_search_value(time))+', ')
            else:
                file.write('0, ')
        file.write('\n')
    file.close()



if __name__ == '__main__':

    #adding arguments
    parser = argparse.ArgumentParser(description= 'A class to import, combine, and print data from a folder.',
    prog= 'dataImport')

    parser.add_argument('folder_name', type = str, help = 'Name of the folder')

    parser.add_argument('output_file', type=str, help = 'Name of Output file')

    parser.add_argument('sort_key', type = str, help = 'File to sort on')

    parser.add_argument('--number_of_files', type = int,
    help = "Number of Files", required = False)

    args = parser.parse_args()


    #pull all the folders in the file
    files_lst = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]


    #import all the files into a list of ImportData objects (in a loop!)
    data_lst = []
    for files in files_lst:
        data_lst.append(ImportData(folder_path+files))

    #create two new lists of zip objects
    # do this in a loop, where you loop through the data_lst
    data_5 = [] # a list with time rounded to 5min
    data_15 = [] # a list with time rounded to 15min

    #print to a csv file
    printLargeArray(data_5,files_lst,args.output_file+'_5',args.sort_key)
    printLargeArray(data_15, files_lst,args.output_file+'_15',args.sort_key)
