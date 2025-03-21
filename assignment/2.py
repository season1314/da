import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Creating a dataset
data = pd.read_csv('dataset_for_assignment_2.csv')

df = pd.DataFrame(data)

# Seaborn style
sns.set_theme(style="whitegrid")

# Create scatter plot: app usage vs. calories burned
plt.figure(figsize=(8, 5))
sns.scatterplot(x="App Sessions", y="Calories Burned", hue="Activity Level", data=df, palette="coolwarm", s=100)
plt.title("App Sessions vs. Calories Burned")
plt.xlabel("App Sessions")
plt.ylabel("Calories Burned")
plt.show()
