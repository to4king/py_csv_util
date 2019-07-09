import re


class PyCsvUtil:
    def __init__(self, range_delimiter='-'):
        """
        コンストラクタ

        Parameters
        --------
        range_delimiter: str, default '-'
            範囲として扱う文字列のデリミタ（区切り文字）
        """
        self._range_delimiter = range_delimiter

    def list_to_str(self, list_arg):
        """
        リストの要素をCSV文字列に変換する

        Parameters
        --------
        list_arg: list
            変換対象のリスト

        Returns
        --------
        string: str
            引数で受けたリストの要素を結合した文字列
        
        Raises
        --------
        TypeError
            リスト以外を引数に渡すと発生
        """
        if isinstance(list_arg, list):
            str_list = [str(item) for item in list_arg]
            return ','.join(str_list)
        else:
            raise TypeError

    def str_to_list(self, str_arg):
        """
        数字（っぽい値）のCSV文字列を数値のリストに変換する
        
        Parameters
        --------
        str_arg: str
            変換対象の文字列（カンマ区切り）

        Returns
        --------
        list: list
            デリミタで分割した文字列それぞれを要素にしたリスト

        Raises
        --------
        TypeError
            文字列以外を引数に渡すと発生
        """
        if isinstance(str_arg, str):
            _match_pattern = r'\d+'+self._range_delimiter+r'\d+'
            _converted_list = []
            for str_item in str_arg.split(','):
                if re.match(_match_pattern, str_item):
                    _range_list = str_item.split(self._range_delimiter)
                    _range_start = int(_range_list[0])
                    _range_end = int(_range_list[1])
                    for i in range(_range_start, _range_end+1):
                        _converted_list.append(i)
                else:
                    if len(str_item):
                        _converted_list.append(int(str_item))
            return _converted_list
        else:
            raise TypeError
