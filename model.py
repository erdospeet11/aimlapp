import numpy as np
from sklearn.linear_model import LinearRegression

# Fit y = 2x on a few points. The model learns that line.
_x = np.array([[0.0], [1.0], [2.0], [3.0]])
_y = np.array([0.0, 2.0, 4.0, 6.0])

model = LinearRegression()
model.fit(_x, _y)


def predict(value: float) -> float:
    return float(model.predict(np.array([[value]]))[0])
