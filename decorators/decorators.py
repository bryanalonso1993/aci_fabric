#!/usr/env/bin/python3.6.9
import sys
import os

# =================================================
#      Decorators .... :)
#
#
# =================================================


# validate os
def decorator_os(my_fn):
    def validate_os():
        if sys.platform.startswith('li'):
            return my_fn
        else:
            print("Bad OS , this script supported in Linux , your OS is : {}".format(sys.platform))
            sys.exit(0)
    return validate_os()


# validate file process exist
def decorator_file(my_fn):
    def validate_exists_file(file):
        if not os.path.isfile(file):
            os.mknod(file)
        return my_fn(file)
    return validate_exists_file
