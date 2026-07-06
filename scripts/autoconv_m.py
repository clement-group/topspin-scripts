import string
from shutil import copyfile
expno = INPUT_DIALOG("autoconv script","Input first/last expts on which to do the convdta etc. sequence", ["First# = ", "Last# = "], ["", ""], ["", ""], ["1", "1"])
curdat=CURDATA()
if expno <> None:
  i = int(expno[0])
  while i < (int(expno[1])+1):
                XCMD("re " + str(i), wait = WAIT_TILL_DONE)
                if i<10:
                	XCMD("convdta 90" + str(i), wait = WAIT_TILL_DONE)
                else:
                	XCMD("convdta 9" + str(i), wait = WAIT_TILL_DONE)
                XCMD("phc1 0", wait = WAIT_TILL_DONE)
                XCMD("datmod raw", wait = WAIT_TILL_DONE)
                XCMD("f1p 0", wait = WAIT_TILL_DONE)
                XCMD("f2p 9.19508e-005", wait = WAIT_TILL_DONE)
                XCMD("nsp 0", wait = WAIT_TILL_DONE)
                XCMD("ls", wait = WAIT_TILL_DONE)
                XCMD("mc", wait = WAIT_TILL_DONE)
                if i<10:
                	copyfile(curdat[3]+"/"+curdat[0]+"/"+str(i)+"/pdata/1/title",curdat[3]+"/"+curdat[0]+"/"+str(900+i)+"/pdata/1/title")
                else:
                	copyfile(curdat[3]+"/"+curdat[0]+"/"+str(i)+"/pdata/1/title",curdat[3]+"/"+curdat[0]+"/9"+str(i)+"/pdata/1/title")
                i += 1
