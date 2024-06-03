import pandas as pd

# series data
""" series_data = [10, 15, 20, 25]
ser = pd.Series(series_data)

print(ser) """

# dataframe data
""" dataframe_data = ([
    [100, "a", True],
    [200, "b", False],
    [150, "d", False],
    [550, "c", True]
])

df = pd.DataFrame(dataframe_data)

df.index = ["01", "02", "03", "04"]
df.columns = ["A", "B", "C"]

print(df[["A", "B"]]) """

# ファイル開き
df = pd.read_csv("./python_module/titanic.csv")

# 不k数の名を指定
""" 
print(df.loc[[2, 5]])
print(df.loc[:, ["Age", "Name"]])
print(df.loc[[2, 5], ["Age", "Name"]]) 
"""

# 複数のIndex指定
""" 
print(df.iloc[1])
print(df.iloc[:, 0:2])
print(df.iloc[1:3, 1:3]) 
"""

# 一つの結果のみ取得する
""" 
print(df.at[0, "Age"])
print(df.iat[0, 1])
 """

#比較演算子で範囲を指定
""" 
print(df["Age"] >= 30)
print(df[df["Age"] >= 30])
print(df[df["Age"].isin([20, 30, 40])])
 """

# 列を基準にソートする
""" 
print(df.sort_values("Age", ascending=False))
 """

# Null処理
"""
print(df.dropna(how="any")) # nullが一つでもあったら行を削除
df.dropna(how="all") # 行の全体がnullだったら行を削除
print(df.fillna(value=0)) #★ Nullを0に変換する 
print(df.isna()) # nullだったらTrueをreturnする
"""

# Grouping
""" 
print(df.groupby("Gender")[["Gender"]].count())
print(df["Gender"].value_counts()) # print(df.groupby("Gender")[["Gender"]].count())と同じ意味
print(df.groupby(["Gender", "Survived"])["Survived"].count())
print(df.groupby(["Gender"])[["Age"]].mean()) # グループ別の年齢の平均値
 """

# DataFrameをループさせる
""" 
for i, r in df.iterrows(): # iterrows()を使えばDataFrameを行単位に変換できる。
    print(i, r)

for age, pclass in zip(df["Age"], df["Pclass"]): # zip()を使えば列のデータをtupleに変換する。(iterrows()より早い)
    print(age, pclass)
 """

