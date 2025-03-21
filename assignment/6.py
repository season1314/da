import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 创建数据
data = pd.read_csv('dataset_for_assignment_2.csv')

# 转换为DataFrame
df = pd.DataFrame(data)

# 打印列名，检查是否正确
print("列名:", df.columns)

# 替换列名中的空格为下划线
df.columns = df.columns.str.replace(' ', '_')

# 打印替换后的列名，确认修改
print("修改后的列名:", df.columns)

# 绘制散点图
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Distance_Travelled_(km)', y='App_Sessions', hue='Activity_Level', data=df, palette='viridis')

# 添加标题和标签
plt.title('Relationship Between Distance Traveled and User Engagement (Activity Level)', fontsize=14)
plt.xlabel('Distance Traveled (km)', fontsize=12)
plt.ylabel('App Sessions (User Engagement)', fontsize=12)

# 显示图形
plt.show()
