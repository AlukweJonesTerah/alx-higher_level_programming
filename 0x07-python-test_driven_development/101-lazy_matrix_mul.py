#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    # Validate m_a and m_b using NumPy
    try:
        np_m_a = np.array(m_a, dtype=np.int64)
        np_m_b = np.array(m_b, dtype=np.int64)
    except (TypeError, ValueError) as e:
        raise TypeError(f"Error converting matrices to NumPy arrays: {e}")

    # Check if matrices can be multiplied
    if np_m_a.shape[1] != np_m_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication using NumPy
    result_matrix = np.dot(np_m_a, np_m_b)

    return result_matrix