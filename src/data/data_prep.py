import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import os

df = pd.DataFrame({"A":[1,2,3], "B":[1,2,3]})

df2 = pd.DataFrame({"C":[2,3,5], "B":[3,4,5]})

#New features added
df3 = pd.DataFrame({"C":[2,3,5, 8], "B":[3,4,5]})
df2.head()
 
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

api_key = os.getenv("apikey")