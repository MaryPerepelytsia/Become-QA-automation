def test_lists():
    assert [1, 2, 3] == [1, 2, 3]


def test_lists_fail():
    assert ["asfA", 2, 3] != [1, 2, 3]