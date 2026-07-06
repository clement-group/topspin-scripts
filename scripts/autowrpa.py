import string
curdat = CURDATA()
expno = INPUT_DIALOG("autowrpa script","", ["First# = ", "Last# = ", "Destination = "], ["", "", ""], ["", "", ""], ["1", "1", "1"])

if expno <> None:
  i = int(expno[0])
  while i < (int(expno[1])+1):
                XCMD("re " + str(i), wait = WAIT_TILL_DONE)
              	WR([expno[2], str(i), "1", curdat[3],])
              	
                i += 1


