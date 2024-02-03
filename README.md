# Youtube 動画 -> MP3 変換

コマンドラインインターフェースによる、YouTube 動画を MP3 形式へ変換する簡易的ツール。

<img src="./docs/nyan_cat.webp">

## 開発環境

 * python v3.11
 * pyinstaller v

## 対応OS

 * Windows 10/11

## 環境構築手順

<ol>
    <li>
        PowerShellを管理者権限で開き、<code>ffmpeg</code>と<code>ffprobe</code>をインストール
        <ol>
            <li>Chocolateyというパッケージマネージャをインストール</li>
                <code>Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iwr -useb https://chocolatey.org/install.ps1 | iex</code>
            <li>インストールの確認</li>
                <code>choco -v</code>
            <li>ffmpegをインストール</li>
                <code>choco install ffmpeg</code>
            <li>ffmpegがインストールされたことを確認</li>
                <code>ffmpeg -version</code>
        </ol>
    </li>
    <li>ユーザーフォルダに<code>Youtube-MP3</code>をクローン</li>
    <li>コントロールパネルを開き、システムとセキュリティ > システム > システムの詳細を選択</li>
    <li>「詳細設定」タブを選択し、「環境変数」を選択</li>
    <li>「システム環境変数」の中から <code>Path</code>を選択し、「編集」ボタンを選択</li>
    <li>「新規」をクリックし、実行ファイルが存在するフォルダのパス（C:\Users\<ユーザー名>\Youtube-MP3\exe\windows-64bit\dist</li>
    <li>次のコマンドでpython環境を構築(構築済みでv3.11が入っている場合は、スキップ) <code>choco install -y python3 --version=3.11</code></li>
    <li><code>python</code>コマンドが有効ではない場合、システム環境変数から<code>Path</code>を編集</li>
    <li><code>pip install -r requirements.txt</code></li>を実行し、依存ライブラリーをインストール
    <li><code>transfer</code>の<code>libs</code>内にある<code>define.py</code>を開き、<code>SOUND_FOLDER_PATH</code>変数の値「<user-name>」を自身のユーザー名に修正して保存
    <li><code>windows.build.bat</code> を実行</li>
</ol>

## 利用手順

「PowerShell」または「コマンドプロンプト」を開き、youtubeコマンドを入力し引数には動画URLを指定。

<code>youtube "https://youtube.be/another_example"</code>

また、引数に複数のリンクを指定することで一括ダウンロードも可能。

<code>youtube "https://youtube.be/another_example_1" "https://youtube.be/another_example_2"</code>

変換後、ダウンロードされたMP3は<code>Youtube-MP3</code>内の<code>music</code>フォルダに格納されます。