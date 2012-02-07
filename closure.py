#!/usr/bin/env python

from os import chdir, getlogin
from logging import error
from shutil import copyfile
from subprocess import call

inst = ["iristestofalonglogin"]
full = ["iristest"]
all = full + inst

WORKDIR = "test/work/var/yp/src"
#SED = "/usr/sww/bin/sed"
SED = "/bin/sed"
#RCSDIFF = "/usr/local/bin/rcsdiff"
RCSDIFF = "/usr/bin/rcsdiff"

def sed(exp, target):
    call([SED, "-i", exp, target])
    return

def rcsdiff(target):
    pass

def confirmchanges(target):
    pass

def closeamdmapentry(user, target):
    target = "amdmaps/amd.home.eecs"
    copyfile(target, target + ".backup")
    sed("/^" + user + "\b/d", target)
    rcsdiff(target)
    confirmchanges(target)
    return

def closeautomapentry(user):
    
    pass

def closeexportsentry(user):
    pass
    
def closegroupentry(user):
    pass

def closenetgroupentry(user):
    pass

def checkout(files, user):
    try:
        for i in files:
            program = ['co', '-l', i]
            if call(program):
                raise Exception(program)
    except Exception as ex:
        error('Exception in %s with file %s while closing account %s.' % (ex, i, user))
        raise ex
    
def checkin(files, user):
    try:
        for i in files:
            program = ['ci', '-u', '-m"Closing ' + user + '. (' + getlogin() +')"', i]
            if call(program):
                raise Exception(program)
    except Exception as ex:
        error('Exception in %s with file %s while closing account %s.' % (ex, i, user))
        raise ex
    
files = ["automaps/auto.home.eecs", "amdmaps/amd.home.eecs",
         "exports", "group", "netgroup"]
chdir(WORKDIR)
for i in all:
    checkout(files, i)
    closeautomapentry(i)
    closeamdmapentry(i)
    closeexportsentry(i)
    closegroupentry(i)
    closenetgroupentry(i)
    checkin(files, i)

# for i in $all; do  $i;  $i;  $i; done

# for i in $inst; do  $i;  $i; done

# for i in $inst; do co -l passwd.closed; ypmatch $i passwd >> passwd.closed; ci -u -m"closing $i ($USER)" passwd.closed; done

# for i in $inst; do sed -i "/^$i:/d" $PASSWD; done


# # iffy
# def foo():
#     ret = fun()
#     if ret:
#         ret2 = bar(ret)
#         if ret2:
#             ret3 = baz(ret2)
#     print ret

# # exceptional!
# def foo():
#     try:
#         baz(bar(fun))
#     except:
#        asdflkajs df
#     print ret
