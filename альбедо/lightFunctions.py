import numpy as np
import matplotlib.pyplot as plt
import imageio
from cycler import cycler


def readIntensity(photoName, plotName, lamp, surface):
    photo = imageio.v2.imread(photoName)
    background = photo[350:550, 490:600, 0:3].swapaxes(0, 1)

    cut = photo[350:550, 380:600, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig = plt.figure(figsize=(10, 5), dpi=200)

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')

    plt.plot(rgb, label=['r', 'g', 'b'])
    plt.plot(luma, 'w', label='I')
    plt.legend()

    plt.imshow(background, origin='lower')

    plt.savefig(plotName)
    plt.close()
    return luma


white = readIntensity("white1.jpg", "spektr_white_mercury", "ртутная_лампа", "белый")
red = readIntensity('red1.jpg', 'spektr_red', 'лампа накаливания', 'красный')
blue = readIntensity('blue.jpg', 'spektr_blue', 'лампа накаливания', 'синий')
yellow = readIntensity('yellow.jpg', 'spektr_yellow', 'лампа накаливания', 'желтый')
green = readIntensity('green1.jpg', 'spektr_green', 'лампа накаливания', 'зеленая')
white_lamp = readIntensity('white2.jpg', 'spektr_white_warm', 'лампа накаливания', 'белый')
