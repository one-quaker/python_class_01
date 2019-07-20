import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('-m', '--msg', type=str)
parser.add_argument('-n', '--first-name', type=str)
parser.add_argument('--range', type=int, default=20)


ARG = parser.parse_args()


for i in range(ARG.range):
    # name = '{}_test'.format(i)
    name = '{0:02d}_test'.format(i)
    print(name)
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.mkdir(name)
