# Youtube 動画 -> MP3 変換

コマンドラインインターフェースによる、YouTube 動画を MP3 形式へ変換する簡易的ツール。

## 開発環境

 * python3.11

## 環境構築

以下の OS のみ対応

 * Windows 10/11
 * Linux (Ubuntu)

### 環境構築手順 (Windows)

 1. ユーザーフォルダに<code>Youtube-MP3</code>をクローン
 2. コントロールパネルを開き、システムとセキュリティ > システム > システムの詳細を選択
 3. 「詳細設定」タブを選択し、「環境変数」を選択
 4. 「システム環境変数」の中から <code>Path</code>を選択し、「編集」ボタンを選択
 5. 「新規」をクリックし、実行ファイルが存在するフォルダのパス（C:\Users\<ユーザー名>\Youtube-MP3\exe\windows-64bit\dist
 6. 設定完了後、全てのダイアログを閉じる

### 利用手順

「PowerShell」または「コマンドプロンプト」を開き、youtubeコマンドの引数に動画のurlを設定。

※複数のリンクを設定した一括返還も可能

<code>youtube "https://youtube.be/another_example"</code>
<code>youtube "https://youtube.be/another_example_1" "https://youtube.be/another_example_2"</code>

変換後、ダウンロードされたMP3は<code>Youtube-MP3</code>内の<code>music</code>フォルダに格納されます。