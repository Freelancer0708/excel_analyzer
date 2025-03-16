import pandas as pd
import config

def analyze_data(file_path):
    """選択したExcelデータを分析し、統計情報をCSVに保存"""
    df = pd.read_excel(file_path)

    # 統計情報を取得
    summary = df.describe()
    print("📊 データの基本統計情報:")
    print(summary)

    # CSVに保存
    summary.to_csv(config.CSV_OUTPUT_PATH)
    print(f"✅ 分析結果を {config.CSV_OUTPUT_PATH} に保存しました！")
    return summary

if __name__ == "__main__":
    file_path = input("Excelファイルのパスを入力してください: ")
    analyze_data(file_path)
