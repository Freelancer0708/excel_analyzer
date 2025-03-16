import os

# ローカルのExcelファイルをユーザーが選択するので固定化しない
OUTPUT_FOLDER = "output/"

# CSVファイルの保存パス
CSV_OUTPUT_PATH = os.path.join(OUTPUT_FOLDER, "analysis_report.csv")

# グラフ画像の保存パス
PLOT_OUTPUT_PATH = os.path.join(OUTPUT_FOLDER, "sales_trend.png")

# 出力フォルダがなければ作成
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
