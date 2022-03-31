import numpy as np
import matplotlib.pyplot as plt
import json
import sys
import time
import os
import glob
import shutil
import datetime
import argparse

if __name__ == '__main__':
    argvs = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", dest="dir", default="./")
    parser.add_argument("--file", dest="file", default="Note")
    opt = parser.parse_args()
    print(opt, argvs)

    print(datetime.date.today())
    datenm = "{0:%Y%m%d}".format(datetime.date.today())
    cp_dir = opt.dir
    cp_num = len(glob.glob(cp_dir + opt.file + "_" + datenm + "*.pdf"))
    cpname = "{}/{}_{}{:03}.pdf".format(cp_dir, opt.file, datenm, cp_num)
    print(cpname)

    shutil.copyfile(opt.file + ".pdf", cpname)
