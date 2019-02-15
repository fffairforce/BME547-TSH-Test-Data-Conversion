import pytest

"""
Just don't know how keep warning wrong pep8
when putting right below def test_diagnosis_tsh(test_list, expected):
import diagnose func to test the function
:param test_list: TSH results
:param expected: Diagnosis results
:return True or False of the expectation
"""


@pytest.mark.parametrize("test_list, expected",
                         [([2.0, 1.5, 3.1, 2.5,
                            1.1, 3.0, 1.9, 0.3,
                            0.7, 1.8, 2.2, 3.7],
                             "Hyperthyroidism"),
                          ([2.8, 3.6, 3.3, 4.5,
                            5.5, 5.0, 6.6, 3.5,
                            2.7, 4.4, 4.1, 4.8],
                             "Hyperthyroidism"),
                          ([3.5, 1.2, 2.3, 2.8,
                            2.9, 2.6, 3.5, 1.3],
                             "normal thyroid function"),
                          ([0.5], "Hyperthyroidism")
                          ])
def test_diagnosis_tsh(test_list, expected):
    from dictionary import diagnose
    answer = diagnose(test_list)
    assert answer == expected
