import pytest
from code_challenges.insertion import insertion

sort_list = [8,4,23,42,16,15]
# @pytest.mark.skip("TODO")
def test_first(sort_list):
   insertion(sort_list)
   actual = insertion(sort_list)
   expected = [4,8,15,16,23,42]
   assert actual == expected
