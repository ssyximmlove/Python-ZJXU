import matplotlib.pyplot as plt
import pandas as pd

# a) 使用 pandas 读取文件 data.csv 中的数据创建 DataFrame 对象，并删除其中所有缺失值
data = pd.read_csv('data.csv')
data = data.dropna()

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 400
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

# b) 使用 matplotlib 生成折线图，反应该饭店每天的营业额情况，并把图形保存为本地文件 first.jpg
data['日期'] = pd.to_datetime(data['日期'])

plt.figure(figsize=(12, 6))
plt.plot(data['日期'], data['销量'])
plt.title('饭店每天的营业额情况')
plt.xlabel('日期')
plt.ylabel('营业额')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('first.jpg')
plt.close()

# c) 按月份进行统计，使用 matplotlib 绘制柱状图显示每个月份的营业额，并把图形保存为本地文件 second.jpg
monthly_data = data.groupby(data['日期'].dt.to_period('M'))['销量'].sum()
plt.figure(figsize=(12, 6))
monthly_data.plot(kind='bar')
plt.title('每个月份的营业额')
plt.xlabel('月份')
plt.ylabel('营业额')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('second.jpg')
plt.close()

# d) 按月份进行统计，找出相邻两个月最大涨幅，并把涨幅最大的月份写入文件 maxMonth.txt
monthly_percentage_change = monthly_data.pct_change()
max_increase = monthly_percentage_change.max()
max_increase_month = monthly_percentage_change.idxmax()
with open('maxMonth.txt', 'w') as f:
    f.write(str(max_increase_month))

# e) 按季度统计该饭店 2017 年的营业额数据，使用 matplotlib 生成饼状图显示 2017 年 4 个季度的营业额分布情况，并把图形保存为本地文件 third.jpg
quarterly_data = data.groupby(data['日期'].dt.to_period('Q'))['销量'].sum()
plt.figure(figsize=(8, 8))
quarterly_data.plot(kind='pie', autopct='%1.1f%%')
plt.title('2017 年 4 个季度的营业额分布情况')
plt.ylabel('')
plt.tight_layout()
plt.savefig('third.jpg')
plt.close()
