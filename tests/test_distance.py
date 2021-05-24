from mlproject.distance import haversine

def test_type_of_distance():
    assert type(haversine(48.865070, 2.380009, 37.9686695, 23.7076324)) == float
    
def test_value_of_distance():
    assert round(haversine(48.865070, 2.380009, 48.235070, 2.393409),2) == round(70.00789153218594, 2)