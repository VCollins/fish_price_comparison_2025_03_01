#import relevant libraries
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

#Alter filepath as necessary
#path = #Set path as needed
path = "/home/gw83523/Software_Projects/fish_price_comparison_2025_03_01/"

#Create temporary dataframe for csv to beloaded
temp_df = pd.read_csv(path + 'fish_price_comparison_2025_03_01.csv', header=None)