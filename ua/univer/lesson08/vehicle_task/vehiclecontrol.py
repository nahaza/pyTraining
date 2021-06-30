from ua.univer.lesson08.vehicle_task.vehicle import Car, Plane
from ua.univer.lesson08.vehicle_task.vehicle_ables import SwimAble


class VehicleControl:
    def __init__(self, vehicle_list):
        self.vehicle_list = vehicle_list

    def print_max_price_vehicle(self):
        max_price_vehicle = self.vehicle_list[0]
        for vehicle in self.vehicle_list:
            if vehicle.price > max_price_vehicle.price:
                max_price_vehicle = vehicle
        print(max_price_vehicle)

    def get_list_between_year(self, year_begin, year_end):
        vehicles_between_year = []
        for vehicle in self.vehicle_list:
            if year_begin < vehicle.year < year_end:
                vehicles_between_year.append(vehicle)
        return vehicles_between_year

    def print_count_Car_Plane(self):
        count_car = 0
        count_plane = 0
        count_swim = 0
        for vehicle in self.vehicle_list:
            if isinstance(vehicle, Car):
                count_car += 1
            if isinstance(vehicle, Plane):
                count_plane += 1
            if isinstance(vehicle, SwimAble):
                count_swim += 1
        print("Count car = ", count_car)
        print("Count plane passenger = ", count_plane)
        print("Count swim = ", count_swim)


