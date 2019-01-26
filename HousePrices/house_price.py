# -*- coding: utf-8 -*-

import pandas as pd


train_path='D:/KaggleData/House Prices/train.csv'
test_path='D:/KaggleData/House Prices/test.csv'

#%%
train_data=pd.read_csv(train_path)

#%%
train_data.shape
train_data.count() 
#%%统计每一列的数据的缺失情况
#统计每一列的缺失值
#train_data.count()
#缺失百分比排序 
(train_data.count()/train_data.shape[0]).sort_values()
#有效数据占比小于50%，直接删除？
#PoolQC           0.004795
#MiscFeature      0.036986
#Alley            0.062329
#Fence            0.192466  枚举，NAN为No fence
#FireplaceQu      0.527397  枚举型，与fireplaces相关的值，Fireplaces为0时，该值为空。将空值转换为另一个枚举值
#LotFrontage      0.822603  数值
#GarageYrBlt      0.944521  数值
#GarageType       0.944521  枚举
#GarageFinish     0.944521  枚举
#GarageQual       0.944521  枚举
#GarageCond       0.944521  枚举
#BsmtExposure     0.973973 枚举
#BsmtFinType2     0.973973 枚举
#BsmtFinType1     0.974658 枚举
#BsmtCond         0.974658 枚举
#BsmtQual         0.974658 枚举
#MasVnrArea       0.994521 数值
#MasVnrType       0.994521 枚举
#Electrical       0.999315 枚举
#%%
#证明Fireplaces为0的时候，FireplaceQu为NAN，可以将FireplaceQu中的NAN转为一个值
fireplace_qu_isna=train_data['FireplaceQu'].isnull()
no_fireplace=train_data['Fireplaces']==0
not_nan_num=0
for i in range(len(fireplace_qu_isna)):
    if fireplace_qu_isna[i] and no_fireplace[i]:
        not_nan_num+=1

print(not_nan_num/len(fireplace_qu_isna)+ 
      (train_data.count()/train_data.shape[0]).sort_values()['FireplaceQu'])
#%% 填充缺失值
