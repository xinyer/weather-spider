class weather:

    def __init__(self, city, date, phenomenon, temperature, wind_direction, wind_power):
        self.city = city
        self.date = date
        self.phenomenon = phenomenon
        self.temperature = temperature
        self.wind_direction = wind_direction
        self.wind_power = wind_power

    def tostring(self):
        print(self.city, self.date, self.phenomenon, self.temperature, self.wind_direction, self.wind_power)
        pass

    def tostring(self):
        return self.city + ' ' + self.date + ' ' + self.phenomenon + ' ' + self.temperature + ' ' + self.wind_direction + ' ' + self.wind_power
