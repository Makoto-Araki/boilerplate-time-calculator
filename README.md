# 関数作成

引数に開始時刻と経過時間と曜日(オプション)を指定して開始時刻から経過時間後の時刻を求める関数を作成

## 1. 実行準備

リモートリポジトリから取得後に Python を対話モードで起動

```
$ git clone https://github.com/Makoto-Araki/boilerplate-time-calculator.git
$ cd boilerplate-time-calculator
$ python (対話モードで起動)
```

## 2. 関数実行(1)

引数に開始時刻と経過時間を指定して実行

```
>>> from time_calculator import add_time
>>> print(add_time('11:00 AM', '0:05'))
11:05 AM
```

## 3. 関数実行(2)

経過時間により午前・午後の表示を入れ替える

```
>>> from time_calculator import add_time
>>> print(add_time('11:00 AM', '0:65'))
12:05 AM
```

## 4. 関数実行(3)

経過時間により日付を跨ぎ翌日となる場合は (next day) と表示する

```
>>> from time_calculator import add_time
>>> print(add_time('11:00 PM', '10:05'))
9:05 AM (next day)
```

## 5. 関数実行(4)

経過時間により日付を跨ぎN日後になる場合は (N days later) と表示する

```
>>> from time_calculator import add_time
>>> print(add_time("6:30 PM", "205:12"))
7:42 AM (9 days later)
```

## 6. 関数実行(5)

曜日指定の場合は実行結果に曜日も表示する

```
>>> from time_calculator import add_time
>>> print(add_time('11:00 PM', '0:65', 'Monday'))
12:05 PM, Tuesday (next day)
```