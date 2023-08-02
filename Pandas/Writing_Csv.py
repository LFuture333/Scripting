import pandas as pd 
import numpy as np

technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python"],
    'Fee' :[22000,25000,np.nan,24000],
    'Duration':['30day',None,'55days',np.nan],
    'Discount':[1000,2300,1000,np.nan]
          }

df = pd.DataFrame(technologies)

df.to_csv("courses.csv", header=True, sep=',')