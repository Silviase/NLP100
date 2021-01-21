# 言語処理100本ノック #2

## 10. 行数のカウント

```wc```はファイルの行数/単語数/文字数を表示する.

```bash
wc popular-names.txt // 2780 11120 55026
```

## 11. タブをスペースに変換

```Ctrl+H```でいいじゃんと思ったけどそういう問題ではない.

```bash
sed -e 's/\t/ /g' popular-names.txt --in-place
```

## 12. 1列目をcol1.txtに，2列目をcol2.txtに保存

ワンライナーを諦めた. 早すぎる妥協である.

```bash
cat popular-names.txt | cut -d " " -f 1 > col1.txt
cat popular-names.txt | cut -d " " -f 2 > col2.txt
```

ここで"これはpythonでやったものをUNIXコマンドで確認するものである"ということに気付いてしまう. えー. とりあえずやる.

## 13. マージ

マージする.

```bash
paste col1.txt col2.txt --delimiters=" " > merged.txt
```

## 14. 先頭N行

```bash
cat popular-names.txt | head -N
```

## 15. 末尾N行

```bash
cat popular-names.txt | tail -N
```

## 16. N分割

```bash
split -n 3 popular-names.txt
```