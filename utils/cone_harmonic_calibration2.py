import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import os


def get_csv_column(csv_path, col_name, sort_by=None, exclude_from=None):
    df = pd.read_csv(csv_path, delimiter=';')
    col = df[col_name].tolist()
    col = np.array(col)
    if sort_by is not None:
        sort_val = get_csv_column(csv_path, sort_by)
        sort_idxs = np.argsort(sort_val)
        col = col[sort_idxs]
    if exclude_from is not None:
        sort_val = sort_val[sort_idxs]
        col = col[sort_val >= exclude_from]
    return col


include_svm = True

folder_paths = ['/share/wandell/data/reith/coneMosaik/sanity_sensor_data/', '/share/wandell/data/reith/coneMosaik/sensor_sanity_point5_rounded/']

fig = plt.figure()
# plt.grid(which='both')
plt.xscale('log')
plt.xlabel('contrast')
plt.ylabel('dprime')
plt.title(f"Contrast calibration for cone mosaic")
plt.title(f"Sensor data - rounded to rounded point 5 mean comparison")
for i, p in enumerate(folder_paths):
    if i == 0:
        appendix = ' rounded mean'
    elif i == 1:
        appendix = ' rounded to .5 mean'
    csv1 = os.path.join(p, 'results.csv')
    csv_svm = os.path.join(p, 'svm_results.csv')
    fname = 'cone_mosaic_contrasts_calibration_exclude_lower_vals_updated'
    fname = 'sensor_data_point5_mean_to_rounded_mean'

    oo = get_csv_column(csv1, 'optimal_observer_d_index', sort_by='contrast', exclude_from=10**-6)
    nn = get_csv_column(csv1, 'nn_dprime', sort_by='contrast', exclude_from=10**-6)
    contrasts = get_csv_column(csv1, 'contrast', sort_by='contrast', exclude_from=10**-6)

    plt.plot(contrasts, oo, label='Ideal Observer'+appendix)
    plt.plot(contrasts, nn, label='ResNet18'+appendix)
    epsilon = 0.001
    if include_svm:
        svm = get_csv_column(csv_svm, 'dprime_accuracy', sort_by='contrast', exclude_from=10**-6)
        svm[svm >= (svm.max()-epsilon)] = oo.max()
        plt.plot(contrasts, svm, label='Support Vector Machine'+appendix)

plt.legend(frameon=True, loc='upper left', fontsize='x-small')
out_path = p
fig.savefig(os.path.join(out_path, f'{fname}.png'), dpi=200)
# fig.show()
print('done!')
