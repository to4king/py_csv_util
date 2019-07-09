# py_csv_util

## About

CSV文字列とリストの変換を行うモジュールです。

リストへの変換元文字列はカンマ区切り数字文字列を想定しています。
コンストラクタ引数に”区切り文字”を指定することができ、CSV文字列中に範囲を示すカラムがあれば”区切り文字”の左辺、右辺を開始値/終了値として扱います。

## Useage

```Python

# Initialize
>>> from py_csv_util import PyCsvUtil
>>> util_obj = PyCsvUtil()

# Convert list to str
>>> list = [1, 2, 3, 4]
>>> csv_str = util_obj.list_to_str(list)
>>> print(csv_str)
    "1,2,3,4"

# Convert str to list
>>> str = "1,2,3,8-11,13"
>>> list = util_obj.str_to_list(str)
>>> print(list)
    [1, 2, 3, 8, 9, 10, 11, 13]
```

## Reference

- ***`__init__([range_delimiter])`***
  - コンストラクタ
  - Parameters
    - range_delimiter: 範囲区切り文字
    - Type: String
    - Default: -(hyphen)

- ***`list_to_str(list_arg)`***
  - リストをカンマ区切り文字列に変換する
  - Parameters
    - list_arg: 変換対象リスト
    - Type: List
  - Returns
    - return_value: カンマ区切り文字列
    - Type: String
  - Raises
    - TypeError: 引数にList以外を与えると発生

- ***`str_to_list(str_arg)`***
  - カンマ区切り文字列をリストに変換する
  - デリミタに指定された範囲区切り文字が含まれる場合、デリミタの左辺/右辺を開始値/終了値として扱う
  - Parameters
    - str_arg: 変換対象文字列
    - Type: String
  - Returns
    - return_value: カンマごとに分割した値を要素に持つリスト
    - Type: List
  - Raises
    - TypeError: 引数にString以外を与えると発生

## Feature tasks

- [ ] PyPIモジュール化