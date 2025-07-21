import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import mplcursors
import pandas as pd
from matplotlib.lines import Line2D
from scipy.stats import linregress 
from scipy.fft import fft, rfft,fftshift
from scipy.fft import fftfreq, rfftfreq
import scipy.signal as sig
from scipy.fft import fft, rfft,fftshift
from scipy.fft import fftfreq, rfftfreq
import sys
import pickle
import json
import cloudpickle


def show(nparray,title=" "):
    plt.figure()
    plt.title(title)
    plt.plot(nparray)
    plt.show()

def showall(List):
    plt.figure()
    for l in List:
        plt.plot(l)
    plt.show()

def findalpha(sequence):
    return 1/np.std(sequence)

def findbeta(sequence):
    return -np.mean(sequence)/np.std(sequence)

def normalize(series:np.ndarray):
    return findalpha(series)*series+findbeta(series)

def noholes(selectedpositions,shapletlength):
    if(len(selectedpositions)==0):   #NEED TO THINK ABOUT THE CASE WHERE I HAVE ONLY ONE ELEMENT
        return False
            
    condition=1
    selectedpositions=sorted(selectedpositions)
    for i in range(len(selectedpositions)-1):
        position= selectedpositions[i]
        nextposition=selectedpositions[i+1]
        if(abs((position+shapletlength-nextposition))/shapletlength > condition):
   #         print(position/8," ",nextposition/8)
           #     print(abs((position-nextposition))/len(shaplet))
            return False
    return True    

def chi2dist(shaplet,Signal):
    #/ (16*mean_*len(shaplet))
    """
    Returns: the chi2 list measure of the shaplet and the signal difference
    """
    lengthShaplet=len(shaplet)
    d=[]
    for i in range(0,len(Signal)-lengthShaplet):
        diff=np.sum(np.power(Signal[i:i+lengthShaplet]-shaplet,2))
        d.append(diff)
    return np.array(d) / (16*np.mean(shaplet)*len(shaplet))

def get_minimas_coordinates(difference,order=300):
    return sig.argrelmin(difference,order=order,mode="wrap")[0]

def draw(shaplet,difference,signal,txt="",xlim=None,minimasposition=None):
    if(minimasposition is None):
        newList=get_minimas_coordinates(shaplet,difference)
    else:
        newList=minimasposition
    plt.figure()
    plt.plot(np.array(range(len(signal)))/8,signal,color='b')
    
    if(xlim is not None):
        plt.xlim(np.array(xlim)/8)
        
    if(txt!=""):
        plt.title(txt)
        
    # Add legend
    #plt.legend(loc="best", fontsize=10)

    for el in newList:
        index=el
        plt.plot(np.array(range(index,index+len(shaplet)))/8,shaplet,color='r',alpha=0.5)
    #plt.xlim(10_000,len(signal))
    #
    """
    plt.axvline(x=2932/8, color='r', linestyle='--', label=f'x = {2932/8:0.2f}')
    plt.text(2932/8, 0, f'{2932/8:0.2f}', horizontalalignment='center', verticalalignment='bottom')
    plt.xlabel("time in s")
    plt.ylabel("intensity count /s ")
    """
    plt.xlabel("time in s")
    plt.ylabel("intensity count /s")
    #

    plt.show()

def loadpickle(filename):
    """
    need to define this function
    """
    with open(filename+".pkl", "rb") as f:
        loaded = cloudpickle.load(f)
    return loaded

def savepickle(filename,data):
    """
    need to define this function too
    args: filename,data
    """
    with open(filename+".pkl", "wb") as f:
        cloudpickle.dump(data, f)

import json


def loadjson(filename):
    """
    Loads data from a JSON file.
    :param filename: Name of the JSON file to read from.
    :return: Parsed JSON data as a Python object.
    """
    with open(filename+".json", 'r', encoding='utf-8') as file:
        return json.load(file)

def savejson(filename, data):
    """
    Saves data to a JSON file.
    :param filename: Name of the JSON file to write to.
    :param data: The Python object to be saved as JSON.
    """
    with open(filename+".json", 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def get_low(lcnumber):
    df=df=pd.read_csv("classified_lcs\grs1915_lc"+str(lcnumber)+".txt",sep="	",skiprows=[0, 1], header=None)
    df.columns = ['time', 'total','low','mid','high']
    return df["low"]