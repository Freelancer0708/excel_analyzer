import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import config

def plot_revenue_trend(file_path):
    """選択したExcelファイルの売上データを可視化"""
    df = pd.read_excel(file_path)

    plt.figure(figsize=(10,5))
    sns.lineplot(x=df["Date"], y=df["Revenue ($)"], marker="o")
    plt.title("Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=45)
    plt.savefig(config.PLOT_OUTPUT_PATH)  # 画像として保存
    plt.show()
    print(f"✅ 売上トレンドグラフを {config.PLOT_OUTPUT_PATH} に保存しました！")

if __name__ == "__main__":
    file_path = input("Excelファイルのパスを入力してください: ")
    plot_revenue_trend(file_path)
