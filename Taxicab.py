# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/10/2022
# Description: A class with three data members that hold x and y coordinates, as well as one that
# represents odometer reading.

class Taxicab:
    """
    Represents a taxi cab's position with x and y coordinates along with its distance traveled
    represented by an odometer.
    """
    def __init__(self, get_x_coord, get_y_coord):
        """Initializes the x and y coordinates as well as setting the odometer to 0 at the start."""
        self._get_x_coord = get_x_coord
        self._get_y_coord = get_y_coord
        self._get_odometer = 0

    def get_x_coord(self):
        """Returns the x-coordinate."""
        return self._get_x_coord

    def get_y_cord(self):
        """Returns the y-coordinate."""
        return self._get_y_coord

    def get_odometer(self):
        """Returns the odometer reading of the taxi cab."""
        return self._get_odometer

    def move_x(self, distance):
        """Returns the direction of the taxi cab in the x-coordinates and adds distance traveled to the odometer."""
        self._get_x_coord += distance
        self._get_odometer += abs(distance)

    def move_y(self, distance):
        """Returns the direction of the taxi cab in the y-coordinates and adds distance traveled to the odometer."""
        self._get_y_coord += distance
        self._get_odometer += abs(distance)

