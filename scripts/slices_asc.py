#$COMMENT=Extracts fids from a sr file, stores them in increasing PROCNOs, and converts the processed data to asc files.

serData = CURDATA()
dim = GETACQUDIM()
if dim < 2:
	ERRMSG("Dimension of acquisition data must be >=2.", "splitsr")
	EXIT()
td1 = int(GETPAR("1s TD"))
td2 = 1
td3 = 1
td4 = 1
if dim == 3:
	td2 = int(GETPAR("2s TD"))
if dim == 4:
	td2 = int(GETPAR("2s TD"))
	td3 = int(GETPAR("3s TD"))
if dim == 5:
	td2 = int(GETPAR("2s TD"))
	td3 = int(GETPAR("3s TD"))
	td4 = int(GETPAR("4s TD"))
	
nFids = td1 * td2 * td3 * td4
result = INPUT_DIALOG("splitsr", "",\
   ["Starting slice", "Number of fids", "First Destination PROCNO = "],\
   ["1", str(nFids), "901"])
if result == None:
	EXIT()
	
startIndex = int(result[0])
nFids = int(result[1])
destinationStart = int(result[2])

for i in range(nFids):
	SHOW_STATUS("fid = " + str(i+1) + ", expno = " + str(destinationStart + i))
	RE(serData, "n") # make it the current dataset	
	# Read fid, do not display it. Fid is now current dataset.
	RSR(str(startIndex+i), str(destinationStart + i), "y")
	XCMD("convbin2asc")
	i = i+1
