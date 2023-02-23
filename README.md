# md chatter

markdownファイルの集積に対してgpt-indexでクエリできないかを試す

## 判明していること（23/2/23）

- markdownをそのまま読み込ませるのはあまりよくない（とはいえllama indexはちゃんとパースしてくれる）
- markdownのheaderによる検索はほぼ機能しない
- 英語でないとindexがうまく機能しない
- embeddingを経由することで費用を削減できる
- 普通に誤答することもある