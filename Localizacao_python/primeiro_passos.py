def localizarua():
    from geopy import Nominatim
    geolocator = Nominatim(user_agent="AIzaSyB4CU7hUNOfQpXn2zfy5IJqI2uJlhgGsPY")
    location = geolocator.geocode("1618, Rua duque de caxias, Ourinhos - SP")
    print((location.latitude, location.longitude))
    #print(location.address)
    #print(location.raw)


def localizaLocLat():
    from geopy import Nominatim
    geolocator = Nominatim(user_agent="AIzaSyB4CU7hUNOfQpXn2zfy5IJqI2uJlhgGsPY")
    location = geolocator.reverse("-22.9623683, -49.8681423")
    print(location.address)
    #print((location.latitude, location.longitude))
    #print(location.raw)

localizarua()

localizaLocLat()