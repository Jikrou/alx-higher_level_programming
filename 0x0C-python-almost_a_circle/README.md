# Module Package "models" README

This package contains modules for representing geometric shapes, including rectangles and squares.

## Modules

### `rectangle.py`

This module defines the `Rectangle` class, which represents a rectangle shape. 
It includes methods for calculating area, displaying the shape, 
converting to a dictionary, updating attributes, and more.

#### Example Usage:

```python
from models.rectangle import Rectangle

# Create a rectangle instance
rectangle = Rectangle(3, 4, 1, 2)

# Calculate the area
area = rectangle.area()
print("Area:", area)

# Display the rectangle
rectangle.display()

# Convert to dictionary
rectangle_dict = rectangle.to_dictionary()
print("Dictionary:", rectangle_dict)

# Update attributes
rectangle.update(5, 6, 7, 8, 9)
print("Updated Rectangle:", rectangle)
