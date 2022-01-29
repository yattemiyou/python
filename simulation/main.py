import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import sys

from Excavator import Excavator_V1, Excavator_V2, Excavator_V3
from Field import Field

field = Field()

excavator = [
    Excavator_V1(field),
    Excavator_V2(Field(field)),
    Excavator_V3(Field(field))
]

fig, ax = plt.subplots(nrows=1, ncols=3)


def show(i, excavator):
    target = np.zeros((Field.ROW, Field.COLUMN))
    target[excavator.x][excavator.y] = 100
    target[excavator.xt][excavator.yt] = 0

    mask = np.full((Field.ROW, Field.COLUMN), True)
    mask[excavator.x][excavator.y] = False
    mask[excavator.xt][excavator.yt] = False

    count = np.count_nonzero(excavator.field.sediment == excavator.field.mean)
    total = Field.ROW * Field.COLUMN

    ax[i].set_title(f'Ver.{i+1} {count}/{total}')

    sns.heatmap(target, cmap='bwr_r', cbar=False,
                mask=mask, square=True, ax=ax[i])

    sns.heatmap(excavator.field.sediment, cmap='Oranges', cbar=False, vmin=0, vmax=Field.RANGE,
                mask=np.logical_not(mask), square=True, ax=ax[i])

    if count == total:
        sys.exit


def initialize():
    global excavator

    for i, e in enumerate(excavator):
        show(i, e)


def simulate(t):
    global excavator

    for i, e in enumerate(excavator):
        e.next()

        show(i, e)


if __name__ == '__main__':
    ani = FuncAnimation(
        fig, simulate, init_func=initialize, interval=200, repeat=False
    )

    ani.save("simulation.gif", writer='imagemagick')
