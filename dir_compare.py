#!/usr/bin/python
# -*-coding:utf-8 -*-

import os
import sys
import shutil


def get_dir_content(dir):
    dir_list = []
    dir_files = os.listdir(dir)
    for dir_file in dir_files:
        if not dir_file.startswith('.'):
            dir_list.append(dir_file)
    return dir_list


def compare_dir(dir1, dir2):
    parent_dirs = get_dir_content(dir1)
    child_dirs = get_dir_content(dir2)
    for child_dir in child_dirs:
        if os.path.isfile(child_dir):
            os.system("cp %s/%s %s" % (dir2, child_dir, dir1))
        elif child_dir in parent_dirs:
            os.system("cp -r %s/%s/* %s/%s/" % (dir2, child_dir, dir1, child_dir))
        else:
            os.system("cp -r %s/%s %s/" % (dir2, child_dir, dir1))
    return True


def help(param="-h"):
    if param in ["--help", "-h"]:
        print '''
        dir_compare.py [parent_dir] [child_dir]
                       parent_dir is move the following directory
                       child_dir is move the previous directory
        dir_compare.py [-h or --help]
                       get help
        '''
        sys.exit()
    else:
        print "Re-enter the parameter incorrectly"
        sys.exit()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        help()
    elif len(sys.argv) != 3:
        help(sys.argv[1])
    else:
        compare_dir(sys.argv[1], sys.argv[2])
        shutil.rmtree(sys.argv[2])
