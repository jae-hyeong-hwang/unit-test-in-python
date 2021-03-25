from scripts.mapmaker_start import Point
import pytest

# in order to prevent minor bug add blank line
def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)
# in order to prevent minor bug add blank line 

def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Buenos Aires", 12.11386, -555.08269)
    #breakpoint()
    assert str(exp.value) == 'Invalid latitude, longitude combination'
    
    with pytest.raises(ValueError) as exp:
        Point(5, 12.11386, -55.08269)
    assert str(exp.value) == 'City name provided must be a string'
