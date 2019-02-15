import pytest
"""
Just don't know how keep warning wrong pep8
when putting right below def test_diagnosis_tsh(test_list, expected):
import diagnose func to test the function
:param test_list: TSH results
:param expected: Diagnosis results
:return True or False of the expectation
"""


@pytest.mark.parametrize("a, expected", [

    ("TSH,3.5,3.6,1.8,2.8,1.9,3.4,3,3.6,3,4", 'Normal thyroid function'),

    ("TSH,2.7,1.4,2.5,3.1,0.4,1.8,3.1,3,3.8,0.9,2.3", 'Hyperthyroidism'),

    ("TSH,6.3,6.7,6.3,7.6,2.1,6.9,7.1,4.1,7.2,3.5,2.9", 'Hypothyroidism'),

])
def test_diagnose_parametrize(a, expected):

    """
    The function of diagnose() is tested with three input conditons using
    the paramertrize decorator.
    Returns:
        Passed if answer == expected
    """
    from dictionary import diagnose
    answer = diagnose(a)
    assert answer[1] == expected
