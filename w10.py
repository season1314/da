import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd


tips = pd.read_csv('week10/Sample_Data_for_Activity.csv')
tips.head()
tips.info()
sns.displot(tips['Normal_Distribution'], kde=True)

sns.displot(tips['Normal_Distribution'], kind="hist", kde=True, bins=20)
sns.rugplot(tips['Normal_Distribution'], color="r")

