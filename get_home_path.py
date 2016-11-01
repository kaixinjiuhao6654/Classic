#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os


class get_home_path(object):
    def __init__(self, username='root'):
        self.username = username
        self.user_dict = {}

    def read_passwd(self):
        with open("/etc/passwd", "r") as user_info:
            for f in user_info.readlines():
                f_list = f.strip('\n').split(':')
                self.user_dict[f_list[0]] = f_list[5]
        return self.user_dict

    def get_home_dir(self):
        user_dict = self.read_passwd()
        try:
            home_dir = user_dict[self.username]
            return home_dir
        except Exception, e:
            print "%s user not exist!" % e
            sys.exit()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print os.path.expanduser('~')
    elif len(sys.argv) == 2:
        username = sys.argv[1]
        get_path = get_home_path(username)
        print get_path.get_home_dir()
    else:
        print "Parameter input is incorrect,more than one."
