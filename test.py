import pandas as pd
import numpy as np

df= pd.DataFrame(np.random.randint(1, 100, size=(100, 4)), columns=list('ABCD'))
print(df)
