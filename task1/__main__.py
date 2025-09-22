#!/usr/bin/env python

import logging
from . import USVehicleFactory, EUVehicleFactory


def main():
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()
    vehicles = [
        us_factory.create_car("Ford", "Mustang"),
        us_factory.create_motorcycle("Harley-Davidson", "Street 750"),
        eu_factory.create_car("BMW", "3 Series"),
        eu_factory.create_motorcycle("Ducati", "Monster"),
    ]
    for vehicle in vehicles:
        vehicle.start_engine()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
