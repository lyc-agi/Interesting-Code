
def test_fun(a, **b):
    print(a, b)

num = 'hhh'
eval(f'test_fun(1, {num}=3)')
