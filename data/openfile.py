import zipfile
import os

def unzip_file(zip_file_path):
    # ZIPファイルのディレクトリを取得
    zip_dir = os.path.dirname(zip_file_path)
    
    # ZIPファイルを開く
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # 全てのファイルを解凍する
        zip_ref.extractall(zip_dir)
        print(f"Unzipped files to {zip_dir}")

# 使用例
zip_file_path = 'valid.zip'  # ここにZIPファイルのパスを指定
unzip_file(zip_file_path)
