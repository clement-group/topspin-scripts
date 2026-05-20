#$COMMENT=Combines the fids from two half experiments in the data folder

# default first experiment to current experiment 
open_exp = CURDATA()

if open_exp is None:
	ERRMSG("A dataset must be open in the directory you'd like to perform the operation in.")
	EXIT()

s_name = open_exp[0]
s_init_exp = open_exp[1]
s_init_proc = open_exp[2]
s_dir = open_exp[3]

result = INPUT_DIALOG(
	title="concat_pseudo2D",
	header="Will concatenate rows of first experiment with rows from second "
    			"experiment.\n Ensure that destination and temp exp nums are not "
					"occupied!",
	items=["First exp num", "Second exp num", "Destination exp num", "Temp exp num"],
	values=[s_init_exp, "", "", "9900"])
if result == None:
	EXIT()

s_exp1 = result[0]
s_exp2 = result[1]
s_dest = result[2]
s_temp = result[3]

# Get exp1 and copy to temp1
RE([s_name, s_exp1, "1", s_dir])
i_rows1 = int(GETPAR("1s TD"))
i_dim = GETACQUDIM()
if i_dim != 2:
	ERRMSG("Dimension of acquisition data must be 2.", "concat_pseudo2D")
	EXIT()
WR([s_name, s_dest, "1", s_dir], "n") 

# Get exp2
RE([s_name, s_exp2, "1", s_dir])
i_rows2 = int(GETPAR("1s TD"))
i_dim = GETACQUDIM()
if i_dim != 2:
	ERRMSG("Dimension of acquisition data must be 2.", "concat_pseudo2D")
	EXIT()

# Prep dest to receive more fids
RE([s_name, s_dest, "1", s_dir], show="n")
i_total_rows = i_rows1 + i_rows2
PUTPAR("1 TD", str(i_total_rows))
PUTPAR("1s TD", str(i_total_rows))
PUTPAR("1 SI", str(i_total_rows))

# Copy temp fids to dest
for i in range(i_rows2):
	RE([s_name, s_exp2, "1", s_dir], show="y")
	RSER(fidnum=str(i+1), expno=s_temp, show="y")
	SLEEP(0.2)
	XCMD("wser " + str(i_rows1+i+1) + " " + s_dest, wait=WAIT_TILL_DONE)
	SLEEP(0.2)
	XCMD("close", wait=WAIT_TILL_DONE) 
	SLEEP(0.2)
	
# Reprocess dest
RE([s_name, s_dest, "1", s_dir], show="y")
ct = XCMD("xf2")

if ct.getResult() == -1:
	ERRMSG("Something went wrong! Processing failed.", "concat_pseudo2D")
	EXIT()

MSG(title="concat_pseudo2D",
		message="Copying complete. You can now delete the temporary "
						"experiment #" + s_temp)