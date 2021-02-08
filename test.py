from os import name
import numpy as np
import pandas as pd 

change_stock = np.random.normal(0,1,(10,5))

#行索引
stock_label = ["股票{}".format(i) for i in range(10)]

data2 = pd.DataFrame({
    "year":[2020,2021,2022,2023],
    "day":["3.1","3.2","3.3","3.4"],
})

#列索引
date = pd.date_range(start="20210208",periods=5,freq="B")

data = pd.DataFrame(change_stock,index=stock_label,columns=date)

#DataFrame属性
data.shape
data.values
data.index
data.columns
#DataFrame方法(默认显示5行)
data.head()
data.tail()

#设置新的索引
new_df = data2.set_index(["year","day"])
new_df.index.names #levels的名称
new_df.index.levels #每个level的元组值