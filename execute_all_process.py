#!/usr/env/bin/python.3.6.9
from process_datasets.process_data_apic_controller import execute_function
from decorators.decorators import decorator_os

# ======================================
#  This environment, execute all process
#   Author : Bryan Alonso
#   Position : Support Engineer
# ======================================


@decorator_os
def main():
    execute_function()


if __name__ == '__main__':
    main()
