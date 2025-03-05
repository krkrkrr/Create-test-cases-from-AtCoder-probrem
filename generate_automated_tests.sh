#!/bin/bash

# 引数のチェック
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <contest_name>"
    exit 1
fi

CONTEST_NAME=$1
CONTEST_URL="https://atcoder.jp/contests/${CONTEST_NAME}"

# 現在のディレクトリを保存
ORIGINAL_DIR=$(pwd)

# スクリプトの場所にディレクトリを変更
cd "$(dirname "$0")"

# 仮想環境の作成
python -m venv .venv --upgrade-deps

# 仮想環境のアクティベート
source .venv/bin/activate

# パッケージのインストール
python -m pip install .

# 必要なファイルの作成
cd "$ORIGINAL_DIR"
python "$(dirname "$0")/src/initialize_environment.py" ${CONTEST_URL}

# 仮想環境のディアクティベート
deactivate

echo "Quick Start completed successfully."