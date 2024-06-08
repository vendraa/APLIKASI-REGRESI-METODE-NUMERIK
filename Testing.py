import math
import matplotlib.pyplot as plt
from MetodeLinier import regresi_linier, predict_linier, galat_rms
from MetodeEksponensial import regresi_eksponensial, predict_eksponensial,galat_rms


NL = [6, 5, 0, 2, 6, 0, 3, 1, 1, 4, 4, 6, 6, 1, 7, 7, 9, 5, 7, 2]
NT = [61.0, 84.0, 69.0, 27.0, 73.0, 85.0, 74.0, 36.0, 47.0, 74.0, 25.0, 34.0, 57.0, 76.0, 83.0, 31.0, 58.0, 49.0, 73.0, 54.0]

#Testing Regresi Linier
a_linier, b_linier = regresi_linier(NL, NT)
NT_pred_linier = predict_linier(NL, a_linier, b_linier)
galat_rms_linear = galat_rms(NT, NT_pred_linier)
print(f'Galat RMS (Linear): {galat_rms_linear}')

#Testing Regresi Eksponensial
a_eksponensial, b_eksponensial = regresi_eksponensial(NL, NT)
NT_pred_eksponensial = predict_eksponensial(NL, a_eksponensial, b_eksponensial)
galat_rms_eksponennsial = galat_rms(NT, NT_pred_eksponensial)
print(f'Galat RMS (Exponential): {galat_rms_eksponennsial}')

