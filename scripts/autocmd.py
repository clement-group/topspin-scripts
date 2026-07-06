import string
expno = INPUT_DIALOG("autocmd script","Input first/last expts on which to execute given cmd, with increment", ["First# = ", "Last# = ", "cmd: ", "Inc ="], ["", "", "", "1"], ["", "", "", ""], ["1", "1", "1", "1"])
if expno <> None:
	i = int(expno[0])
	while i < (int(expno[1])+1):
		newcmd = string.replace(expno[2],"$i",str(i))
		#XCMD("re 3622")
		XCMD("re " + str(i) + " 1", wait = WAIT_TILL_DONE)
		if ";" in newcmd:
			cmdlist = newcmd.split(';')
			for cmd in cmdlist:
				XCMD(cmd)
		else:
			XCMD(newcmd)
		#XCMD("phc0 -208.673", wait = WAIT_TILL_DONE)
		#XCMD("phc1 2302.400", wait = WAIT_TILL_DONE)
		#XCMD("efp", wait = WAIT_TILL_DONE)
		i += int(expno[3])