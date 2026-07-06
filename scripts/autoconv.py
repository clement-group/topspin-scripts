import string
expno = INPUT_DIALOG("autoconv script","Input first/last expts on which to do the convdta etc. sequence", ["First# = ", "Last# = "], ["", ""], ["", ""], ["1", "1"])
if expno <> None:
  i = int(expno[0])
  while i < (int(expno[1])+1):
                XCMD("re " + str(i), wait = WAIT_TILL_DONE)
                XCMD("convdta 99" + str(i), wait = WAIT_TILL_DONE)
                XCMD("phc0 0", wait = WAIT_TILL_DONE)
                XCMD("phc1 0", wait = WAIT_TILL_DONE)
                XCMD("datmod raw", wait = WAIT_TILL_DONE)
                XCMD("f1p 0", wait = WAIT_TILL_DONE)
                XCMD("f2p 5.19508e-004", wait = WAIT_TILL_DONE)
                XCMD("nsp 0", wait = WAIT_TILL_DONE)
                XCMD("ls", wait = WAIT_TILL_DONE)
                XCMD("mc", wait = WAIT_TILL_DONE)
                #XCMD("efp", wait = WAIT_TILL_DONE)
                i += 1
