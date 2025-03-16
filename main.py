import tkinter as tk
from tkinter import filedialog, messagebox
import data_handler
import analysis
import visualization
import config
import os

# `output/` フォルダを自動作成
if not os.path.exists(config.OUTPUT_FOLDER):
    os.makedirs(config.OUTPUT_FOLDER)

def select_file_and_analyze():
    """ユーザーがExcelファイルを選択し、データ分析を実行"""
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    
    if not file_path:
        messagebox.showwarning("Warning", "No file selected!")
        return

    df = data_handler.load_local_excel(file_path)
    if df is not None:
        analysis.analyze_data(file_path)
        visualization.plot_revenue_trend(file_path)
        messagebox.showinfo("Complete", "Data analysis finished!")

# GUIの作成
root = tk.Tk()
root.title("Excel Analyzer")
root.geometry("300x200")

btn_select = tk.Button(root, text="Select Excel File", command=select_file_and_analyze)
btn_select.pack(pady=20)

root.mainloop()
