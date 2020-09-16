# _*_ coding:utf-8 _*_
#
import pytest
def add_caculator(num1,num2):
    sum = num1 + num2
    return sum

@pytest.mark.parametrize("num1,num2,result", [[1, 2, 3],
                                              [3, 12, 15],
                                              [6, -2, 4], [1.8, 2, 3.8]],
                         ids=["10以内", "10以外", "负数", "小数"])
def test_add_caculator(num1,num2,result):
    sum = add_caculator(num1,num2)
    assert sum == result
