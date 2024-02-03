from transfer.libs import action

if __name__ == "__main__":
    try:
        # Youtube動画ファイル変換
        action.movie_to_music()
    except Exception as e:
        print(e)