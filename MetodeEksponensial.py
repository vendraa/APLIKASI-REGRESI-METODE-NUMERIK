import math
import matplotlib.pyplot as plt


NL = [6, 5, 0, 2, 6, 0, 3, 1, 1, 4, 4, 6, 6, 1, 7, 7, 9, 5, 7, 2]
NT = [61.0, 84.0, 69.0, 27.0, 73.0, 85.0, 74.0, 36.0, 47.0, 74.0, 25.0, 34.0, 57.0, 76.0, 83.0, 31.0, 58.0, 49.0, 73.0, 54.0]


def regresi_eksponensial(x, y):
    n = len(x)
    log_y = [math.log(yi) for yi in y]
    x_mean = sum(x) / n
    log_y_mean = sum(log_y) / n
    b = sum((x[i] - x_mean) * (log_y[i] - log_y_mean) for i in range(n)) / sum((x[i] - x_mean) ** 2 for i in range(n))
    a = log_y_mean - b * x_mean
    return math.exp(a), b

def predict_eksponensial(x, a, b):
    return [a * math.exp(b * xi) for xi in x]

a_eksponensial, b_eksponensial = regresi_eksponensial(NL, NT)
NT_pred_eksponensial = predict_eksponensial(NL, a_eksponensial, b_eksponensial)

def galat_rms(y_true, y_pred):
    n = len(y_true)
    return (sum((y_true[i] - y_pred[i]) ** 2 for i in range(n)) / n) ** 0.5

galat_rms_eksponensial = galat_rms (NT, NT_pred_eksponensial)
print(f'Galat RMS (Exponential): {galat_rms_eksponensial}')

plt.scatter(NL, NT, color='blue', label='Data')
plt.plot(NL, NT_pred_eksponensial, color='green', label='Exponential Fit')
plt.title('Regresi Eksponensial')
plt.xlabel('Jumlah Latihan Soal')
plt.ylabel('Nilai Ujian')
plt.legend()
plt.show()