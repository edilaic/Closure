#!/usr/bin/env python

from os import chdir
from logging import error
from subprocess import call

inst = ["iristestofalonglogin"]
full = ["iristest"]
all = full + inst

WORKDIR = "test/work/var/yp/src"



def closeamdmapentry(i):
    pass

def closeautomapentry(i):
    pass

def closeexportsentry(i):
    pass
    
def closegroupentry(i):
    pass

def closenetgroupentry(i):
    pass

def checkout(files, user):
    chdir(WORKDIR)
    try:
        for i in files:
            program = ['co', '-l', i]
            if call(program):
                raise Exception(program)
    except Exception as ex:
        error('Exception in %s while closing account %s.' % (ex, user))
        raise ex
    
def checkin(files, user):
    call('ci -u thingy')
    
files = ["automaps/auto.home.eecs", "amdmaps/amd.home.eecs",
         "exports", "group", "netgroup"]
user = full[0]
checkout(files, user)
for i in all:
    closeautomapentry(i)
    closeamdmapentry(i)
    closeexportsentry(i)
    closegroupentry(i)
    closenetgroupentry(i)
checkin()

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
