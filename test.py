from re import match
import pytest
from py_csv_util import PyCsvUtil


class TestPyCsvUtil:
    def test_default_delimiter_type(self):
        """ デフォルトの範囲区切り文字が文字列型であること """
        csv_util = PyCsvUtil()
        assert isinstance(csv_util._range_delimiter, str)

    def test_default_delimiter_val(self):
        """ デフォルトの範囲区切り文字が'-'であること """
        csv_util = PyCsvUtil()
        assert csv_util._range_delimiter == '-'

    def test_delimiter_typec_check(self):
        """ 引数のデリミタの型チェック """
        with pytest.raises(TypeError):
            csv_util = PyCsvUtil(1)

    
    def test_list_to_str_arg_type(self):
        """ 配列→文字列変換メソッドの引数テスト """
        csv_util = PyCsvUtil()
        not_list_arg = ''
        with pytest.raises(TypeError):
            csv_util.list_to_str(not_list_arg)

    def test_list_to_str_return_type(self):
        """ 配列→文字列変換メソッドの戻り値テスト """
        csv_util = PyCsvUtil()
        test_list = [1, 2, 3]
        assert isinstance(csv_util.list_to_str(test_list), str)

    def test_str_to_list_arg_type(self):
        """ 文字列→配列変換メソッドの引数テスト """
        csv_util = PyCsvUtil()
        not_str_arg = []
        with pytest.raises(TypeError):
            csv_util.str_to_list(not_str_arg)

    def test_str_to_list_return_type(self):
        """ 文字列→配列変換メソッドのテスト """
        csv_util = PyCsvUtil()
        str_arg = '1,2,6-9,16'
        assert isinstance(csv_util.str_to_list(str_arg), list)
