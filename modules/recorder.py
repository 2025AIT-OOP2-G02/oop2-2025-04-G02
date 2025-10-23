"""modules.recorder

シンプルな録音スクリプト。

目的:
    マイクから音声を録音してプロジェクト内の `files/input.wav` に保存します。

依存:
    - システムに ffmpeg バイナリがインストールされていること（macOS: brew install ffmpeg 推奨）。
    - Python パッケージ `ffmpeg-python`（pip install ffmpeg-python）が必要です。

使い方:
    - モジュールを直接実行すると、デフォルトで `files/input.wav` に 10 秒間録音します::

        python modules/recorder.py

    - このスクリプトは教育用の簡易スクリプトです。より柔軟に使いたい場合は関数化やコマンドライン引数の追加を検討してください。
"""

import ffmpeg
import time

# 録音時間（秒）
duration = 10
# 出力ファイル名
output_file = 'files/input.wav'

try:
    print(f"{duration}秒間、マイクからの録音を開始します...")
    # FFmpegコマンドを実行
    # -f <デバイス入力形式>: OSに応じたデバイス入力形式を指定
    #   - Windows: 'dshow' または 'gdigrab'
    #   - macOS: 'avfoundation'
    #   - Linux: 'alsa'
    # -i <入力デバイス名>: デバイス名を指定
    (
        ffmpeg
        .input(':0', format='avfoundation', t=duration) # macOS
        .output(output_file, acodec='pcm_s16le', ar='44100', ac=1)
        .run(overwrite_output=True)
    )
    print(f"録音が完了しました。{output_file}に保存されました。")

except ffmpeg.Error as e:
    print(f"エラーが発生しました: {e.stderr.decode()}")
except Exception as e:
    print(f"予期せぬエラー: {e}")