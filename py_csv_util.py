import re
import itertools

class PyCsvUtil:
    def __init__(self, delimiter='-'):
        """
        コンストラクタ

        Parameters
        --------
        delimiter: str, default '-'
            範囲として扱う文字列のデリミタ（区切り文字）
        """
        if isinstance(delimiter, str):
            self._range_delimiter = delimiter
        else:
            raise TypeError("invalid delimiter type")

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
            _converted_list = [self._make_list(str_item) for str_item in str_arg.split(',')]
            return list(itertools.chain.from_iterable(_converted_list))
        else:
            raise TypeError


    def _make_list(self, str_arg):
        # should be rename '_match_pattern'
        _match_pattern = r'\d+'+self._range_delimiter+r'\d+'
        if re.match(_match_pattern, str_arg):
                    # should be rename '_range_list'
                    _range_list = str_arg.split(self._range_delimiter)
                    _generated_list = [i for i in range(int(_range_list[0]), int(_range_list[1])+1)]
                    return _generated_list
        return [int(str_arg)]
