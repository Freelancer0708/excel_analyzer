import pandas as pd

def load_local_excel(file_path):
    """ユーザーが選択したExcelファイルを読み込む"""
    try:
        df = pd.read_excel(file_path)
        print(f"✅ {file_path} を正常に読み込みました！")
        print(df.head())  # 先頭5行を表示
        return df
    except FileNotFoundError:
        print(f"❌ エラー: ファイル {file_path} が見つかりません！")
        return None
    except Exception as e:
        print(f"❌ エラー: {e}")
        return None

if __name__ == "__main__":
    file_path = input("Excelファイルのパスを入力してください: ")
    load_local_excel(file_path)
