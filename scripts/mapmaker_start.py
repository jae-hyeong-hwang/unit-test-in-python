class Point():
  def __init__(self, name, latitude, longitutde)
    if not isinstance(name, str):
      raise ValueError("City name provided must be a string")
    self._name = name
    
    if not(-90 <= latitude <= 90) or not (-180 <= longitude <= 180)
        raise ValueError("Invalude latitude, longitude")
    self._longitude = longitude
    self._latitude = latitude

  def get_lat_long(self):
    return (self._latitude, self._longitude)

  
