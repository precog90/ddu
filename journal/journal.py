import os


def load(name):
    """
    :param name: Journal name to load
    :return: Journal requested
    """
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    print("Saving to {0}".format(filename))


#    fout = open(filename, 'w')
    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    pathname = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return pathname


#    fout.close()




def add_entry(text, data):
    return None