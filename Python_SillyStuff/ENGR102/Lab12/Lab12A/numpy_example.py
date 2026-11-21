# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
#               Zachary Adams 637008110
#               Harshil Patel 838007668
# Section:      555
# Assignment:   numpy_example
# Date:         17 November 2026

# As a team, we have gone through all required sections of the
# tutorial and each team member understands the material

# Import
import numpy as np

# Creating and printing matrices
matrixA = np.array(np.arange(12)).reshape(3, 4); print(f"Matrix A: \n{matrixA}\n")
matrixB = np.array(np.arange(8)).reshape(4, 2); print(f"Matrix B: \n{matrixB}\n")
matrixC = np.array(np.arange(6)).reshape(2, 3); print(f"Matrix C: \n{matrixC}\n")

# Compute: D = ABC (matrix multiplication)
matrixD = matrixA @ matrixB @ matrixC; print(f"Matrix D: \n{matrixD}\n")

# Print D as a transposed matrix
matrixDTrans = matrixD.T; print(f"Matrix D^T: \n{matrixDTrans}\n")

# Compute: E = sqrt(D) / 2
matrixE = np.sqrt(matrixD) / 2; print(f"Matrix E: \n{matrixE}\n")
