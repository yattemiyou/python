# エージェント指示書 (Agent Instructions)

## プロジェクト概要 (Project Context)

- **開発言語**: Python 3.12+
- **実行環境**: Linux
- **環境・依存関係管理**: uv (Astral)
- **静的解析・フォーマッタ**: Ruff
- **テストフレームワーク**: pytest
- **ロギングライブラリ**: loguru

## ディレクトリ構成

```
project/
│
├── .venv/
├── src/
├── tests/
├── docs/
├── config/
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

## セットアップおよび開発コマンド (Setup & Development Commands)

- **Pythonのインストール**: `uv python install`
- **環境の初期化・構築**: `uv venv`
- **依存関係の同期**: `uv sync`
- **新規パッケージの追加**: `uv add <パッケージ名>`
- **Pythonスクリプトの実行**: `uv run <スクリプト名.py>`
- **リンターの実行（チェック）**: `uv run ruff check`
- **フォーマッタの実行（修正）**: `uv run ruff format`
- **テストの実行**: `uv run pytest`

## コーディング規約 (Code Guidelines)

- 可読性を最優先にする
- 保守しやすい設計にする
- 必要以上に複雑なコードを書かない
- DRY・YAGNI・SOLIDを意識する
- 1関数1責務
- 50行以内を目安にする
- 深いネストを避ける
- 早期returnを活用する
- Ruffのルールを遵守し、PEP 8に準拠したクリーンなPythonコードを書くこと。
- すべての関数の引数と戻り値に、明示的な型ヒント（Type Hints）を記述すること。
- 新機能やユーティリティ関数を追加する際は、必ず `pytest` を用いたユニットテストを合わせて作成すること。
- 新たな依存パッケージの追加は、最小限にとどめること。
- セキュリティ上のベストプラクティスを考慮する
- コードは省略せず、完成版を提示する

## ログ (Log)

- **ロギング**: すべてのログ出力には `loguru` を使用すること。標準の `logging` モジュールや、デバッグ目的の `print()` は使用禁止とする。
- ログレベル（DEBUG、INFO、WARNING、ERROR）を適切に使い分ける。

## テスト (Test)

以下のテストケースを作成する。

- 正常系
- 異常系
- 境界値

## ガードレール / 厳守事項 (Guardrails - Strict Rules)

- **最重要**: グローバル環境のPythonや、標準の `pip` (`python -m pip`) は絶対に使用しないこと。必ず `uv` を使用し、依存関係はすべてプロジェクト内で管理すること。
- **最重要**: コマンドを実行する際は、必ず `uv run` を頭に付け、`uv` が管理する仮想環境内で実行させること。
- **最重要**: タスクを完了とする前に、必ず `uv run ruff check` と `uv run pytest` を実行し、エラーがないことを確認すること。
- **最重要**: ロギングを実装する際は、必ず `from loguru import logger` を使用すること。
- 仮想環境ディレクトリ（`.venv`）やRuffのキャッシュ（`.ruff_cache`）をGitにコミットしないこと。
- `requirements.txt` や `pyproject.toml` を手動で直接編集しないこと。変更が必要な場合は、必ず `uv` のコマンドを介して更新すること。
- 仕様が曖昧な場合は、実装前に確認すること。
