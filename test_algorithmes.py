import algorithmes

def test_naive_algorithm():
    points = [(0, 0), (1, 1), (2, 2), (0, 2), (2, 0)]
    expected_enveloppe = [(0, 0), (2, 0), (2, 2), (0, 2)]
    result = algorithmes.naive_algorithm(points)
    assert set(result) == set(expected_enveloppe)


def test_divide_and_conquer():
    points = [(0, 0), (1, 1), (2, 2), (0, 2), (2, 0)]
    expected_enveloppe = [(0, 0), (2, 0), (2, 2), (0, 2)]
    result = algorithmes.divide_and_conquer(points)
    assert set(result) == set(expected_enveloppe)

def test_jarvis():
    points = [(0, 0), (1, 1), (2, 2), (0, 2), (2, 0)]
    expected_enveloppe = [(0, 0), (2, 0), (2, 2), (0, 2)]
    result = algorithmes.jarvis(points)
    assert set(result) == set(expected_enveloppe)

def test_sklansky():
    points = [(0, 0), (1, 1), (2, 2), (0, 2), (2, 0)]
    expected_enveloppe = [(0, 0), (2, 0), (2, 2), (0, 2)]
    result = algorithmes.sklansky(points)
    assert set(result) == set(expected_enveloppe)