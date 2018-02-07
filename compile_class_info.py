import glob
import os
import csv
import json
import pandas as pd
from collections import defaultdict

def main():
    filtered_list = collect_csv_files()
    holder = read_csv(filtered_list)
    write_csv(holder)
    check_no_spaces()
    count_camel_case()
    write_json()

def collect_csv_files():
    all_csv = glob.glob('*.csv')
    all_csv.remove('mlp6.csv')
    all_csv.remove('everyone.csv')
    return all_csv

def read_csv(filtered_list):
    holder = []
    for filename in filtered_list:
        reader = pd.read_csv(filename,header=None)
        holder.append(reader)
    return holder
#Based on: https://youtu.be/KoRT-v0SzMs (Accessed: 2/6/18)

def write_csv(holder):
    header = ['First Name','Last Name','Net ID','GitHub Name','Teamname']
    con_val = pd.concat(holder,axis=0, ignore_index=True)
    con_val.columns=header
    con_val.to_csv('everyone.csv', index=None)
#Based on: https://youtu.be/KoRT-v0SzMs (Accessed: 2/6/18)

def check_no_spaces():
    columns = defaultdict(list)
    with open('everyone.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (m,n) in row.items():
                columns[m].append(n)
    z = columns['Teamname']
#Source: https://stackoverflow.com/a/16503661 (Accessed: 2/6/18)
    for y in z:
        if ' ' in y[0] and ' ' in y[1:len(z)]:
            print('Yes Siree Bob')
            break
        if y[0].isalpha and ' ' in y[1:len(z)]:
            print('Yes Siree Bob')
            break
        if y[0].isdigit and ' ' in y[1:len(z)]:
            print('Yes Siree Bob')
            break
    else:
        print('No spaces found in Teamname','\n---------------------------')

def count_camel_case():
    columns = defaultdict(list)
    with open('everyone.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (m,n) in row.items():
                columns[m].append(n)
    z = columns['Teamname']
#Source: https://stackoverflow.com/a/16503661 (Accessed: 2/6/18)
    count = [0]
    for y in z:
        if y[0].isupper():
            if y[1].islower():
                count = [x+1 for x in count] #Based on https://stackoverflow.com/a/21823813 (Accessed: 2/6/18)
        if ' ' in y[0]:
            if y[1].isupper():
                if y[2].islower():
                    count = [x+1 for x in count]
    print('Instances of CamelCase:',count)

def write_json():
    unfilt = glob.glob('*.csv')
    unfilt.remove('everyone.csv')
    for filename in unfilt:
        csv_file = open(filename, 'r')
        change = filename
        ext = change.replace('.csv', '.json')
        json_file = open(ext, 'w')
        header = ('First Name','Last Name','Net ID','GitHub Name','Teamname')
        reader = csv.DictReader(csv_file,header)
        for row in reader:
            json.dump(row, json_file)
            json_file.write('\n')
#Based on: https://stackoverflow.com/a/19706994 (Accessed: 2/6/18) and https://stackoverflow.com/a/34960394 (Accessed: 2/6/18)

if __name__ == '__main__':
    main()
