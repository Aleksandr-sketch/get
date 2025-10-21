import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title("График зависимости напряжения на входе АЦП от времени")
    plt.xlim(0, 3)
    plt.ylim(0, 3.5)
    plt.grid()
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.show()