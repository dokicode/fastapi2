import pandas as pd
import numpy as np

class DataService():

    def __init__(self) -> None:
        pass

    def generateData():
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        return df
    
    def read_csv(filename):
        df = pd.read_csv(filename)
        return df