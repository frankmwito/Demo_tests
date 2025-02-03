import pytest
import math

# test cases using two parametrize decorators
@pytest.mark.parametrize("shape", ["rectangle", "circle"])
@pytest.mark.parametrize("dimensions, expected_area", [((5, 10), 50), ((10,), round(math.pi * 10**2, 2))])
def test_areas(shape, dimensions, expected_area):
    if shape == "rectangle":
        area = dimensions[0] * dimensions[1]  # width * height
    elif shape == "circle":
        area = round(math.pi * (dimensions[0] ** 2), 2)  # π * r^2
    else:
        raise ValueError("Invalid shape")
    
    assert area == expected_area, f"Expected {expected_area}, but got {area}"
