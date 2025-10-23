# oop2-2025-04-G02

## 📖 プロジェクト概要

このプロジェクトは、音声録音 → 文字起こし → 保存を行うプログラムを
グループで分担して開発するものです。

---

## 実行手順

main.py を実行してください。

```bash
python main.py
```

### Python バージョン

- Python 3.13 以上  

### requirements.txt

mlx>=0.11\
numba\
numpy\
torch\
tqdm\
more-itertools\
tiktoken\
huggingface_hub\
scipy

### インストール方法

```bash
pip install -r requirements.txt
```

---

## 📝 命名規則

### ファイル名

- 小文字 + アンダースコア `_` を使用
- 統合用スクリプトは `main.py`

### 関数名

- 小文字 + アンダースコア `_` で記述（snake_case）
- 処理内容がわかる名前にする  
  例: `record_audio()`, `transcribe_audio()`, `save_transcription()`

### 変数名

- 小文字 + アンダースコア `_`（snake_case）  
  意味がわかる名前にする  
  例: `audio_path`, `output_file`, `duration_sec`

### 出力ファイル名

- WAVファイル: `input.wav`
- 文字起こし結果: `output.txt`

---

## 🚀 実行手順

1. `main.py` を実行

```bash
python main.py
