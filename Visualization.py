import pandas as pd
import matplotlib.pyplot as plt

# 读取数据文件
data = pd.read_csv("taobao.csv")
# 查看数据概况
print(data.info())
# 查看数据前五行
print(data.head())

# 数据清洗
# 去除重复数据
data.drop_duplicates(inplace=True)
# 去除缺失值
data.dropna(inplace=True)
# 去除异常值
data = data[data["price"] > 0]
data = data[data["sales"] > 0]

# 数据转换
# 将价格和销量转换为数值类型
data["price"] = data["price"].astype(float)
data["sales"] = data["sales"].astype(int)
# 提取商品品牌
data["brand"] = data["title"].str.split(" ").str[0]
# 提取商品折扣
data["discount"] = data["price"] / data["original_price"]

# 数据分析
# 按品牌分组，计算平均折扣
brand_discount = data.groupby("brand")["discount"].mean().sort_values()
# 按价格区间分组，计算平均折扣
bins = [0, 100, 200, 300, 400, 500, 1000, 2000, 3000, 4000, 5000]
labels = ["0-100", "100-200", "200-300", "300-400", "400-500", "500-1000", "1000-2000", "2000-3000", "3000-4000", "4000-5000"]
data["price_range"] = pd.cut(data["price"], bins=bins, labels=labels)
price_discount = data.groupby("price_range")["discount"].mean().sort_index()

# 数据可视化
# 设置中文显示
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 绘制品牌折扣柱状图
plt.figure(figsize=(20, 8))
plt.bar(brand_discount.index, 1 - brand_discount, color="#FF6902")
plt.xlabel("品牌")
plt.ylabel("折扣率")
plt.title("淘宝商品品牌折扣分析")
plt.show()
# 绘制价格折扣折线图
plt.figure(figsize=(20, 8))
plt.plot(price_discount.index, 1 - price_discount, color="#FF6902", marker="o")
plt.xlabel("价格区间")
plt.ylabel("折扣率")
plt.title("淘宝商品价格折扣分析")
plt.show()
