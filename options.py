# -*- coding: utf-8 -*-
"""Functions dealing with the options and their file."""
# TODO:
# put all os-specific stuff in here?

from sys import stderr
from os import path, stat
from StringIO import StringIO

defaults = {
    'ballimit': 9999, # minmax limit for balance in search
    'branch': 1,
    # calendar colours
    'cal_col_op': 'lightred',
    'cal_col_cons': 'lightblue',
    'cal_disp': 0, # calendar display mode: 0 week  1 day  2 month
    'cal_res': 1, # minutes per appointment: 0->60  1->30  2->15
    'starttime': '7:30', # time of day from which to show in calendar
    'ccode': 'uk',
    'contime': 1800,  # set to 0 to disable autocon checking
    'currency': 8356, # currency symbol ['$', £: 8356, €: 8364, ...]
    'dbhost': None,   # host to connect to for gnuvet db
    'dbhostport': 5432, # port to connect for postgres
    'dobwarn': True,  # warn if dob hasn't been changed on adding patient
    'lang': 'en',
    'maxwinnum': 3, # max open client/patient windows
    'nolabels': False,
    'srchdetails': True,
    'stdfind': 0, # 0 all  1 live  2 rip
    'stdmark': 1,
    'usemark': True, # False for D,AT; True for UK, ...
    'usestock': False,
    'usesymp': True,
    # clinhist colours
    'other_col': 'darkRed',
    'med_col':   'darkBlue',
    'serv_col':  'darkGreen',
    'good_col':  'darkMagenta',
    'food_col':  'darkYellow',
    'cons_col':  'darkCyan',
    'hist_col':  'black',
    # alternatively always use black (delete or comment out above options)
    # and setAlternatingRowColors()
    }

def readopt(s):
    """Simple test for values read from config files."""
    if s == 'True':  return True
    if s == 'False':  return False
    try:
        return int(s)
    except ValueError:
        return s

def read_options(user=None):
    """Set options according to options file if it exists, is readable
    and not suspiciously large.  Otherwise return defaults."""
    if not 'sysinfo' in locals():
        from util import sysinfo
    syspath, userdir, optfile = sysinfo()
    if not optfile:
        stderr.write(syspath + '\n')
        return
    if not 'os_path' in locals():
        from os import path as os_path
    if user:
        optfile = os_path.join(os_path.expanduser('~'+user), userdir, optfile)
    else:
        optfile = os_path.join(syspath, os_path.split(optfile)[-1])
    if not path.exists(optfile):
        return defaults
    if stat(optfile).st_size > 2048:
        stderr.write('Warn: options file "{}" too big, using defaults.\n'
                     .format(optfile))
        return defaults
    try:
        with open(optfile, 'r', 1) as f:
            of = StringIO(f.read())
    except IOError:
        stderr.write("Couldn't open options file, using defaults.\n")
        return defaults
    for line in of:
        if (not (line or line.__contains__('=')) or
            line.startswith('#') or line.startswith(';')):
            continue
        line = line.rstrip()
        tmp = line[:79]
        option, setting = tmp.split('=')
        if option in defaults:
            defaults[option] = readopt(setting)
    return defaults

def write_options(user=None):
    """Write customised options to file."""
    # hierwei: implement
    gvdir = '.'
    if 'workdir' in defaults:
        gvdir=defaults['workdir']
    pass
