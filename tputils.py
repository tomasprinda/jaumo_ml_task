import codecs
import os
import pickle
import re

import numpy as np
import matplotlib.pyplot as plt
import itertools


def json_load(filename):
    import json
    with open(filename, "r") as f:
        return json.load(f)


def json_dump(d, filename):
    import json
    with open(filename, "w") as f:
        json.dump(d, f)


def pickle_load(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)


def pickle_dump(d, filename):
    with open(filename, "wb") as f:
        pickle.dump(d, f)


def csv_dump(rows, filename, append=False, delimiter=";"):
    import csv
    open_param = 'a' if append else 'w'
    with open(filename, open_param) as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter, quotechar=str('"'), quoting=csv.QUOTE_MINIMAL)
        rows = [list(row) for row in rows]  # Like copy, but converts inner tuples to lists
        writer.writerows(rows)


def csv_load(filename, delimiter=";", n=-1):
    import csv
    rows = []
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar=str('"'), quoting=csv.QUOTE_MINIMAL)
        for row in reader:

            if 0 <= n < len(rows):
                break

            rows.append(row)

    return rows


def txt_dump(rows, filename, append=False, add_new_line=True):
    open_param = 'a' if append else 'w'
    if add_new_line:
        rows = [row + "\n" for row in rows]
    with codecs.open(filename, open_param, encoding="utf-8") as f:
        f.writelines(rows)


def txt_load(filename):
    with codecs.open(filename, "r", encoding="utf-8") as f:
        return [row.strip() for row in f]


def make_sure_path_exists(path):
    try:
        os.makedirs(os.path.dirname(path))
    except OSError as exception:
        import errno
        if exception.errno != errno.EEXIST:
            raise


def silent_remove(filename):
    try:
        os.remove(filename)
    except OSError as e:  # this would be "except OSError, e:" before Python 2.6
        import errno
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occurred


def print_info(var, name="var", output=False):
    """
    Print variable information.
    :type var: any
    :type name: str
    :return:
    """
    if isinstance(var, np.ndarray):
        out = "{}: type:{}, shape:{}, dtype:{}".format(name, type(var), var.shape, var.dtype)
    elif isinstance(var, list) or isinstance(var, tuple):
        out = "{}: type:{}, len:{}, type[0]:{}".format(name, type(var), len(var), type(var[0]) if len(var) > 0 else "")
    else:
        out = "{}: val:{}, type:{}".format(name, var, type(var))
    if output:
        return out
    else:
        print(out)


def strip_extension(filename):
    arr = filename.split(".")
    if len(arr) == 1:
        return arr[0]
    return ".".join(arr[:-1])


def extension(filename):
    arr = filename.split(".")
    return arr[-1]


def tokenize(s):
    return list(filter(None, re.split("[,._ \-!?:\(\)|@/=]+", s)))


def dir_path(file):
    """
    Get the path to a dir where file is located.
    Use der_path(__file__) to get dir where source file is located.
    :param str file:
    :return:
    """
    return os.path.dirname(os.path.abspath(file))


def undefaultdict(d):
    return {k: v for k, v in d.items()}


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        # print("Normalized confusion matrix")
    else:
        # print('Confusion matrix, without normalization')
        pass

    # print(cm)
    plt.figure()
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
