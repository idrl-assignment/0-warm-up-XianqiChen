import numpy as np
import matplotlib.pyplot as plt


def generate_random_matrix(m, n):
    return np.random.randint(2, size=(m, n))


def save_matrix(matrix, file_name):
    plt.imshow(matrix)
    plt.savefig(file_name)


if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    save_matrix(matrix, "example.jpg")
