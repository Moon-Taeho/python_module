import pandas as pd

df = pd.read_csv("./python_module/titanic.csv")

# 練習①
print(df.loc[:, ["Age", "Gender", "Pclass", "Fare", "Survived"]])

# 練習②
print(df.dropna(how="any"))

# 練習③
print("Max Fare:", df["Fare"].max())
print("Min Fare:", df["Fare"].min())

# 練習④
print("Count : ", df[df["Age"] <= 30]["Gender"].count())

# 練習⑤
print(df.loc[:, ["Age", "Gender", "Pclass", "Fare", "Survived"]].sort_values("Pclass", ascending=False))

# 練習⑥
print(df[df["Survived"] == 1].groupby("Gender")["Gender"].count())

# 練習⑦
print(df.groupby(["Gender"])[["Age"]].mean())