import os
import datetime

# デフォルトの保存先ファイル
DEFAULT_OUTPUT_FILE = "output.txt"

def save_transcript(text: str, 
                    output_file: str = DEFAULT_OUTPUT_FILE) -> None:
    """
    文字起こしされたテキストを、タイムスタンプ付きで指定ファイルに追記（append）する。

    Args:
        text (str): 保存する文字列。
        output_file (str): 保存先のファイルパス。
                           親ディレクトリが存在しない場合は作成を試みる。
    """
    
    # 保存先ディレクトリの確認・作成
    output_dir = os.path.dirname(output_file)
    if output_dir: # ルートディレクトリへの保存（''）でない場合
        os.makedirs(output_dir, exist_ok=True)
        
    # 追記するエントリの作成
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"[{timestamp}]\n{text}\n\n" # タイムスタンプと本文、間に空行
    
    # ファイルに追記
    try:
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(log_entry)
        print(f"Transcript saved to {output_file}")
    except IOError as e:
        print(f"Error: Failed to write to file {output_file}: {e}")