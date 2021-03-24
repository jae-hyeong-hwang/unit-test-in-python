from scripts.mapmaker_start import Point

# in order to prevent minor bug add blank line
def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)
# in order to prevent minor bug add blank line    
