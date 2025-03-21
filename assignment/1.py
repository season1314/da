import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 读取数据
data = pd.read_csv('dataset_for_assignment_2.csv')
df = pd.DataFrame(data)

# 设置 Seaborn 风格
sns.set_theme(style="whitegrid")

# 绘制柱状图：用户活动水平 vs. 应用使用次数
plt.figure(figsize=(8, 5))
sns.barplot(x="Activity Level", y="App Sessions", data=df, hue="Activity Level", palette="Blues", estimator=sum, legend=False)

# 设置标题和标签
plt.title("App Sessions by Activity Level")
plt.xlabel("Activity Level")
plt.ylabel("Total App Sessions")

# 显示图表
plt.show()
