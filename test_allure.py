import allure

@allure.step('start')
def test_give_back_one():
    print('yes')
    return 1
