import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14


def test_soma():
    # given a num1 of 10 and a num2 of 5
    num1 = 10
    num2 = 5

    # when we calculate the soma
    output = methods.soma(num1, num2)

    # then the area should be 15
    assert output == 15

def test_subtracao():
    # given a num1 of 20 and a num2 of 10
    num1 = 20
    num2 = 10

    # when we calculate the subtracao
    output = methods.subtracao(num1, num2)

    # then the area should be 10
    assert output == 10

def test_multiplicacao():
    # given a num1 of 5 and a num2 of 10
    num1 = 5
    num2 = 10

    # when we calculate the multiplicacao
    output = methods.multiplicacao(num1, num2)

    # then the area should be 50
    assert output == 50

def test_divisao():
    # given a num1 of 10 and a num2 of 2
    num1 = 10
    num2 = 2

    # when we calculate the divisao
    output = methods.divisao(num1, num2)

    # then the area should be 5
    assert output == 5