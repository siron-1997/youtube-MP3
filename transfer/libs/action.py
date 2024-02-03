import sys, json, os
from yt_dlp import YoutubeDL
from transfer.libs import define

def movie_to_music():
    # コマンドライン引数からURLを取得
    urls: list[str] = sys.argv[1:]

    # 引数が指定されていない場合、メッセージを表示して終了
    if not urls:
        print("Error: ダウンロードする動画のURLが指定されていません。")
        print("       ダウンロードを開始するには引数にURLを指定してください。")
        print("")
        print('    youtube "https://youtu.be/<another_example>"')
        print("")
        return
    # 引数に指定されたURLをダウンロード
    else:
        ydl_opts = {
            "format": "mp3/bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192" # 音質設定
                }
            ],
            "outtmpl": f"{define.SOUND_FOLDER_PATH}" + "/" + "%(title)s.%(ext)s" # 保存先
        }

        with YoutubeDL(ydl_opts) as ydl:
            result = ydl.download(urls)
            print(result)