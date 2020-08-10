import pytest
import yaml

from pythoncode.calc import Calculator

# 创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
@pytest.fixture(scope='function')
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")


with open("./dates/calc.yml", encoding='utf-8') as f:
    dates = yaml.safe_load(f)
    add_dates = dates['add']['dates']
    # print(add_dates)
    my_id = dates['add']['myid']
    # print(my_id)

    div_dates = dates['div']['dates']
    print(div_dates)
    my_id1 = dates['div']['myid']
    print(my_id1)

    sub_dates = dates['sub']['dates']
    print(div_dates)
    my_id2 = dates['sub']['myid']
    print(my_id2)

    mul_dates = dates['mul']['dates']
    print(mul_dates)
    my_id3 = dates['mul']['myid']
    print(my_id3)

@pytest.fixture(params=add_dates,ids=my_id)
def get_dates(request):
    date = request.param
    print(f"request.param的测试数据是:{date}")
    return date

@pytest.fixture(params=div_dates,ids=my_id1)
def get_dates1(request):
    date = request.param
    print(f"request.param的测试数据是:{date}")
    return date
@pytest.fixture(params=sub_dates,ids=my_id2)
def get_dates2(request):
    date = request.param
    print(f"request.param的测试数据是:{date}")
    return date
@pytest.fixture(params=mul_dates,ids=my_id3)
def get_dates3(request):
    date = request.param
    print(f"request.param的测试数据是:{date}")
    return date