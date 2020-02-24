import numpy as np
import matplotlib.pyplot as plt
import json
import sys
import time
import os
import glob
import shutil
import datetime
from optparse import OptionParser

if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--dir", dest="dir",default="./")
    parser.add_option("--file", dest="file", default="Note")
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    print(datetime.date.today())
    datenm = "{0:%Y%m%d}".format(datetime.date.today())
    cp_dir = opt.dir
    cp_num = len(glob.glob(cp_dir + opt.file + "_" + datenm + "*.pdf"))
    cpname = "{}/{}_{}{:03}.pdf".format(cp_dir, opt.file, datenm, cp_num)
    print(cpname)

    shutil.copyfile(opt.file + ".pdf", cpname)
