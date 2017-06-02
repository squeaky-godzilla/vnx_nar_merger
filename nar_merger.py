#!/usr/bin/env python

import os
import glob
import shutil
import time

def narmerge(file1,file2,fileout):
    os.system('naviseccli.exe analyzer -archivemerge -data ' + file1 + ' ' + file2 + ' -out ' + fileout + ' -overwrite n')

start_time = time.clock()
narlist_initial = glob.glob('*.nar')
narlist = glob.glob('*.nar')
outname_base = narlist[0].split('_')[0]
cycle_count = 0
while True:
    narlist = glob.glob('*.nar')
    print "nar files left ... %s" % (len(glob.glob('*.nar')))
    # outname_base = narlist[0].split('.')[0]
    if len(glob.glob('*.nar')) > 1:
        narlist1 = narlist[::2]
        narlist2 = narlist[1::2]
        for i in range(0,len(narlist1)):
            try:
                cycle_count += 1
                print "merging %s AND %s ..." % (narlist1[i],narlist2[i])
                narmerge(narlist1[i],narlist2[i],outname_base + '_' + str(cycle_count) + '_in_progress.nar')
                # os.rename(narlist1[i],narlist1[i] + '.processed')
                # os.rename(narlist2[i],narlist2[i] + '.processed')
                os.remove(narlist1[i])
                os.remove(narlist2[i])
            except IndexError:
                pass
    elif len(glob.glob('*.nar')) <= 1:
        try:
            os.rename(narlist[0],outname_base + '_final.nar')
        except IndexError:
            pass
        print "done, processed %s files in %s seconds" % (len(narlist_initial),time.clock() - start_time)
        break
