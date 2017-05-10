import os
import time
CRED = '\033[91m'
CEND = '\033[0m'
CGREEN  = '\33[32m'
CBLUE   = '\33[34m'
count = 1
while (count > 0):
	os.system('date')
	print 'Run = ',count
	print 'crab status crab_projects/crab_WPlepWMhadJJ_EWK_LO_aQGC-FT-FS-FM_mjj100VJpT10_Pythia8CUEP8M1_13TeV_Madgraph'
	os.system("crab status crab_projects/crab_WPlepWMhadJJ_EWK_LO_aQGC-FT-FS-FM_mjj100VJpT10_Pythia8CUEP8M1_13TeV_Madgraph | tee status.log") 
	os.system('cat status.log | grep "failed"')
	if 'failed' in open('status.log').read():
		print(CRED+"There are filed jobs. Resubmit them."+CEND)
		os.system("crab resubmit crab_projects/crab_WPlepWMhadJJ_EWK_LO_aQGC-FT-FS-FM_mjj100VJpT10_Pythia8CUEP8M1_13TeV_Madgraph | tee status.log") 
	else:
		print(CGREEN+"All jobs running fine..."+CEND)
	count += 1
	os.system('date')
	print(CBLUE+'\n\n\n=======> Sleep for  15 minute\n\n\n'+CEND)
	time.sleep(900)
	os.system('date')
