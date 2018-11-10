import numpy as np

if __name__ == "__main__":
    print(np.__version__)
    vec2 = np.array([4, 5, 6])
    vec = np.linalg.norm(vec2)
    print(vec)
