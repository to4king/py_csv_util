# py_csv_util

## About

CSV 文字列とリストの変換を行うモジュールです。

リストへの変換元文字列はカンマ区切り数字文字列を想定しています。
コンストラクタ引数に”区切り文字”を指定することができ、CSV 文字列中に範囲を示すカラムがあれば”区切り文字”の左辺、右辺を開始値/終了値として扱います。

## Requirements

- pytest
  - Use in test.py

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

- **_`__init__([range_delimiter])`_**

  - コンストラクタ
  - Parameters
    - delimiter: 範囲区切り文字
    - Type: String
    - optional: true
    - Default: -(hyphen)

- **_`list_to_str(list_arg)`_**

  - リストをカンマ区切り文字列に変換する
  - Parameters
    - list_arg: 変換対象リスト
    - Type: List
  - Returns
    - return_value: カンマ区切り文字列
    - Type: String
  - Raises
    - TypeError: 引数に List 以外を与えると発生

- **_`str_to_list(str_arg)`_**
  - カンマ区切り文字列をリストに変換する
  - デリミタに指定された範囲区切り文字が含まれる場合、デリミタの左辺/右辺を開始値/終了値として扱う
  - Parameters
    - str_arg: 変換対象文字列
    - Type: String
  - Returns
    - return_value: カンマごとに分割した値を要素に持つリスト
    - Type: List
  - Raises
    - TypeError: 引数に String 以外を与えると発生

## Feature tasks

- [ ] PyPI モジュール化
