# Python応用研修

## 1. Git復習
- git init → git add → git commit -m "message" → git push -u origin main

## 2. pipコマンド
-  pipのバージョン確認 : pip --version
- pipをアップデート: pip install 
- パッケージのインストール一覧 : pip list
- パッケージのインストール : pip install [package_name]
- パッケージアンインストール : pip uninsatall [package_name]

## 3. Pandas
### 1. pandasとは
- データ解析を容易にする機能を提供するPythonのータ分析ライブラリ
### 2. pandasのデータ型
1. Series : 1次元データ、列や業として使われる
2. DataFrame : 2次元データ、Seriesで列と行が構成されているテーブル
### 3. 列名、行名の変更
1. 行名：df.index = ["行名①","行名②"]
2. 列名：df.columns = ["列名①","列名②"]
### 4. データの範囲を指定
1. 列の指定：df["列名①", "列名②"]
2. 行の指定：df[行番号:行番号]
3. 行数を指定：df.head(行数)