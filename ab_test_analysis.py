
# coding: utf-8

get_ipython().magic(u'matplotlib inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read dataset Data format:
# date, variation, session id, total minutes watched
dt = pd.read_csv('experiment_granular.csv',sep=',',header=0)
dt.head()

# mean, SD, N per variation
dt_all = dt.groupby('v.variation')
dt_all.describe()

# mean, SD, N per variation after filtering out outliers
no_outl = dt[dt.minute_view_cnt <= 720]
no_outl_var = no_outl.groupby('v.variation')
no_outl_var.describe()

# plotting entire distrubution of min views
no_outl.minute_view_cnt.hist(bins=30)

# Examining distribution in sessions with less than 100 minutes watched
no_outl[(no_outl.minute_view_cnt <= 100)].minute_view_cnt.hist(bins=30)

# Examining sessions with less than 100 minutes watched
# but without the skew due to the ones who didn't watch anything at all
no_outl[(no_outl.minute_view_cnt <= 100) & (no_outl.minute_view_cnt >0)].minute_view_cnt.hist(bins=30)
