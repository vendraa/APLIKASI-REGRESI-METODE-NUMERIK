import matplotlib.pyplot as plt


NL = [6, 5, 0, 2, 6, 0, 3, 1, 1, 4, 4, 6, 6, 1, 7, 7, 9, 5, 7, 2]
NT = [61.0, 84.0, 69.0, 27.0, 73.0, 85.0, 74.0, 36.0, 47.0, 74.0, 25.0, 34.0, 57.0, 76.0, 83.0, 31.0, 58.0, 49.0, 73.0, 54.0]

def regresi_linier(x, y):
    n = len(x)
    x_mean = sum(x) / n
    y_mean = sum(y) / n
    b = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n)) / sum((x[i] - x_mean) ** 2 for i in range(n))
    a = y_mean - b * x_mean
    return a, b

def predict_linier(x, a, b):
    return [a + b * xi for xi in x]

a_linier, b_linier = regresi_linier(NL, NT)
NT_pred_linier = predict_linier(NL, a_linier, b_linier)

def galat_rms(y_true, y_pred):
    n = len(y_true)
    return (sum((y_true[i] - y_pred[i]) ** 2 for i in range(n)) / n) ** 0.5

galat_rms_linier = galat_rms(NT, NT_pred_linier)
print(f'Galat RMS (Linier): {galat_rms_linier}')

plt.scatter(NL, NT, color='blue', label='Data')
plt.plot(NL, NT_pred_linier, color='red', label='Linier Fit')
plt.title('Regresi Linier')
plt.xlabel('Jumlah Latihan Soal')
plt.ylabel('Nilai Ujian')
plt.legend()
plt.show()
