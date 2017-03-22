The Middle of the coordinates
===

Simple script to calculate the central coordinate of a list


# How to run

```
from theMiddle import MiddleCoordinates
my_coordinates = [[43.267422, -2.934732],
                  [43.269466, -2.935319],
                  [43.268189, -2.931603]]
print('My coordinates {}'.format(my_coordinates))
m = MiddleCoordinates(my_coordinates)
print("The middle coordinates is {}".format(m.the_middle()))
```

