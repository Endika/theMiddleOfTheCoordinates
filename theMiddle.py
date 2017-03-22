# -*- encoding: utf-8 -*-

import math


class MiddleCoordinates():
    """The middle of the coordinates."""

    coordinates_lts = []

    def __init__(self, coordinates_lts):
        """It is obvious."""
        self.coordinates_lts = coordinates_lts

    def get_distance(self, coor1, coor2):
        """Get distance."""
        result = (coor2[0] - coor1[0]) ** 2 + (coor2[1] - coor1[1]) ** 2
        if result < 0:
            result *= -1
        return math.sqrt(result)

    def get_middle_point(self, coor1, coor2):
        """Get the middle coordinates."""
        return (coor1[0] + coor2[0]) / 2.0, (coor1[1] + coor2[1]) / 2.0

    def get_middle_multi_points(self, point_lts):
        """Get the middle multi coordinates."""
        result = {}
        for point in point_lts:
            new_points = []
            for subpoint in point_lts:
                if subpoint != point:
                    new_points.append(
                        self.get_middle_point(point, subpoint))
            middle = self.get_middle_point(new_points[0], new_points[1])
            result[middle] = 0.0
            for subpoint in point_lts:
                result[middle] += self.get_distance(subpoint, middle)
            result[middle] /= 3
        coor_result = False
        for key in result.keys():
            if not coor_result:
                coor_result = key
            if result[key] < result[coor_result]:
                coor_result = key
        return coor_result

    def _filter_all_coordinates(self):
        """Easy, get all possition points from X and Y."""
        top = self.coordinates_lts[0]
        bottom = self.coordinates_lts[0]
        right = self.coordinates_lts[0]
        left = self.coordinates_lts[0]
        for coordinates in self.coordinates_lts:
            if coordinates[1] > top[1]:
                top = coordinates
            if coordinates[1] < bottom[1]:
                bottom = coordinates
            if coordinates[0] > right[0]:
                right = coordinates
            if coordinates[0] < left[0]:
                left = coordinates
        return top, bottom, right, left

    def _prepare_points(self, top, bottom, right, left):
        point_lts = [top, bottom]
        if top != right and bottom != right:
            point_lts.append(right)
        if top != left and bottom != left:
            point_lts.append(left)
        return point_lts

    def _far_point(self, point_lts):
        x_max = point_lts[0]
        y_max = point_lts[1]
        for coor in point_lts:
            if coor[0] > x_max[0]:
                x_max = coor
            if coor[1] > y_max[1]:
                y_max = coor
        if x_max != y_max and x_max[0] < y_max[1]:
            return y_max
        return x_max

    def the_middle(self):
        """Get the middle coordinate."""
        top, bottom, right, left = self._filter_all_coordinates()
        point_lts = self._prepare_points(top, bottom, right, left)
        len_total = len(point_lts)
        if len_total == 2:
            return self.get_middle_point(point_lts[0], point_lts[1])
        elif len_total == 3:
            return self.get_middle_multi_points(point_lts)
        elif len_total == 4:
            firts = self.get_middle_point(point_lts[0], point_lts[1])
            second = self.get_middle_point(point_lts[2], point_lts[3])
            if firts != second:
                return self.get_middle_point(firts, second)
            return firts
