import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 创建数据集
data = pd.read_csv('dataset_for_assignment_2.csv')
df = pd.DataFrame(data)

# 设置Seaborn风格
sns.set_theme(style="whitegrid")

# 创建箱线图：应用使用次数 vs. 所在地区
plt.figure(figsize=(8, 5))
sns.boxplot(x="Location", y="App Sessions", data=df, palette="Set2")
plt.title("Distribution of App Sessions by Location")
plt.xlabel("Location")
plt.ylabel("App Sessions")
plt.show()

