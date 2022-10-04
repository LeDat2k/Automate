import pyautogui 
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyperclip
import seaborn as sns


df = pd.read_csv('Thongtin.csv', sep=',') 

def input_person(person, input_locations):
    # them moi button
    # pyautogui.click(x=1772, y=175)
    # time.sleep(4)

    # input form
    for i in range(len(person)):
        pyautogui.click(input_locations[i])
        pyperclip.copy(person[i])
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)

    # save button
    # pyautogui.click(x=1764, y=1021)
    # time.sleep(5)


if __name__=="__main__":
    # k - 1
    k = 38
    persons = df.iloc[k].values
    persons[6] = '0' +str(persons[6])[:-1]

    input_locations = [(1601, 844), (177, 378), (1343, 193), (546, 57), (1026, 48), (223, 172), (1647, 13), (1709, 695)]

    input_person(persons, input_locations)
