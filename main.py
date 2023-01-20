import math
import numpy as np
from scipy import constants


def wave_length_to_freq(wave_length):
    return 2 * math.pi * constants.c / wave_length


def main():
    l: float = float(input('Длина волны: '))
    w = wave_length_to_freq(l)

    l1 = 0.0684043e-6
    l2 = 0.1162414e-6
    l3 = 9.896161e-6
    w1 = wave_length_to_freq(l1)
    w2 = wave_length_to_freq(l2)
    w3 = wave_length_to_freq(l3)
    B1 = 0.696163
    B2 = 0.4079426
    B3 = 0.8374794

    w2 = w ** 2
    w12 = w1 ** 2
    w22 = w2 ** 2
    w32 = w3 ** 2

    B1w12 = B1 * w12
    B2w22 = B2 * w22
    B3w32 = B3 * w32
    w12_w2 = w12 - w2
    w22_w2 = w22 - w2
    w32_w2 = w32 - w2

    J1 = B1w12 / w12_w2
    J2 = B2w22 / w22_w2
    J3 = B3w32 / w32_w2
    J12 = B1w12 / w12_w2 ** 2
    J22 = B2w22 / w22_w2 ** 2
    J32 = B3w32 / w32_w2 ** 2

    kk = w3 ** 2

    b1 = w * (J12 + J22 + J32) / np.sqrt(J1 + J2 + J3 + 1)

    b2 = ((J1 + J2 + J3 + 1)
          * (
                  (B1 * (3 * w2 + w12) * w12) / w12_w2 ** 3 +
                  (B2 * (3 * w2 + w22) * w22) / w22_w2 ** 3 +
                  (B3 * (3 * w2 + w32) * w32) / w32_w2 ** 3
          ) -
          w2 * (J12 + J22 + J32) ** 2
          ) / ((J1 + J2 + J3 + 1) ** (3 / 2))

    print(b1, b2)


if __name__ == '__main__':
    main()
