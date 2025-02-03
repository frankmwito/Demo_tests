import pytest



class Test_Match:
    #Pass    
    @pytest.mark.xfail(run=True)
    def test_number_square(self):
        num = 10
        result = num * num # 10 * 10 = 100
        assert result == num ** 2
    # Fail
    def test_divide_number(self):
        pytest.xfail("Need To Investigate")
        num = 10
        result = num + num
        assert result == num / num
       
    # Fail 
    @pytest.mark.xfail(reason="Result Add Numbers & Not Multiply Numbers")
    def test_square_number(self):
        num = 10
        result = num + num # 10 * 10 = 100
        assert result == num ** 2
        
    #Pass
    @pytest.mark.xfail(reason="Result and Assert Are Correct")
    def test_cube_number(self):
        num = 10
        result = num * num * num # 10 * 10 * 10 = 1000
        assert result == num ** 3

        