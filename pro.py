#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy
from IPython.display import clear_output

df = pd.read_csv('Bitcoin.csv')

def main_menu():
    clear_output
    print('''--------MAIN MENU--------
    1.Bitcoin Values as dataframe
    2.Bitcoin Analysis Using Visuals
    3.Exit''')
    time.sleep(1)
    main = int(input('<mainM> '))
    if main == 1:
        submenu_1()
    elif main == 2:
        submenu_2()
    elif main == 3:
        exit()
    else:
        print('Input a Valid Choice.')
        time.sleep(1)
        main_menu()

def exit():
    clear_output()
    print('~Thanks~')
    time.sleep(5)
    clear_output()

def submenu_1():
    print('''                 1.View records(Custom) from start
                 2.View records(Custom) from end 
                 3.Check out available columns 
                 4. View data from selected column
                 5.Mathematical Analysis of data
                 6. Attributes of the csv taken
                 7.Return To Main Menu
                 8.Exit''')

    x = int(input('<subM1> '))
    
    if x == 1:
        clear_output()
        numb_rec = int(input('Number Of Records You Want To View: '))
        print(df.head(numb_rec))
        submenu_1()

    elif x == 2:
        clear_output()
        numb_rec = int(input('Number Of Records You Want To View: '))
        print(df.tail(numb_rec))
        submenu_1()

    elif x == 3:
        clear_output()
        print(df.columns)
        submenu_1()

    elif x == 4:
        clear_output()
        columns_data()

    elif x == 5:
        clear_output()
        pass #abhi mereko pata ni isme krna kya
        submenu_1()

    elif x == 6:
        clear_output()
        attributes_csv()

    elif x == 7:
        clear_output()
        main_menu()

    elif x == 8:
        clear_output()
        exit()

def submenu_2():
    main_menu()
    pass #mn nhi kra mera lol, krdunga lekin aj
    

def columns_data():
    clear_output()
    print('''Columns Are:           
             ->Date
             ->Open
             ->High
             ->Low
             ->Close
             ->Volume
         ''')          # !!! It lacks that, if user wish to return to submenu he cannot !!!

   
    inp1 = str(input('Enter The Column Name: '))
    low = inp1.lower() #This makes every word small
    inp2 = low.capitalize() #This makes the first letter of the word capital

    if inp2 in df.columns:
        column_data = df[inp2]
        print(column_data)

    else:
        print(f"Column '{inp2}' not found in the DataFrame.") 
        time.sleep(1)
        columns_data()

    submenu_1()

def attributes_csv():             # !!! It lacks that, if user wish to return to submenu he cannot !!!

    clear_output()
    print('''
        
        1.Diplay the [transpose]
        2.Display [indexes] of the DataFrame
        3.Display the [shape] of the DataFrame
        4.Display the [axes] of the DataFrame
        5.Display the [dimension] of the DataFrame
        6.Display the [data types] of all the columns
        7.Display the [size] of the DataFrame
        ''')
    
    try:
        inp = int(input("Enter Your Choice:"))
        if inp == 1:
            clear_output()
            print(df.T)
        elif inp == 2:
            clear_output()
            print(df.index)
        elif inp ==3:
            clear_output()
            print(df.shape)
        elif inp == 4:
            clear_output()
            print(df.axes)
        elif inp ==5:
            clear_output()
            print(df.ndim)           
        elif inp ==6:
            clear_output()
            print(df.dtypes)            
        elif inp ==7:
            clear_output()
            print(df.size)
        else:
            clear_output()
            print("Please Enter A Input From The Given.")
            time.sleep(1)
            attributes_csv()
    except:
        print("Please Enter A valid Input.")
        time.sleep(1)
        attributes_csv()
    submenu_1()
              

main_menu()  #165 lines ka code less goooooooooooooooo!!!


# # 
