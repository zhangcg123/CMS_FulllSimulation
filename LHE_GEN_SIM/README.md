# How to run

	cmsRun -e -j SMP-RunIISummer15wmLHEGS-00090_rt.xml SMP-RunIISummer15wmLHEGS-00090_1_cfg.py || exit $? ; 
	echo 41 events were ran 
	grep "TotalEvents" SMP-RunIISummer15wmLHEGS-00090_rt.xml 
	grep "Timing-tstoragefile-write-totalMegabytes" SMP-RunIISummer15wmLHEGS-00090_rt.xml 
	grep "PeakValueRss" SMP-RunIISummer15wmLHEGS-00090_rt.xml 
	grep "AvgEventTime" SMP-RunIISummer15wmLHEGS-00090_rt.xml 
	grep "AvgEventCPU" SMP-RunIISummer15wmLHEGS-00090_rt.xml 
	grep "TotalJobCPU" SMP-RunIISummer15wmLHEGS-00090_rt.xml 
	grep "EventThroughput" SMP-RunIISummer15wmLHEGS-00090_rt.xml

# Crab Commands:

	voms-proxy-init --voms cms --valid 168:00
	source /cvmfs/cms.cern.ch/crab3/crab.sh
	crab status <dir>
	crab submit <dir>
	crab report <dir>

## Script for crab job

The failure rate is quite high (1 success after several 100s failure, this is because it is unable to find the input tar file). So, for this we can use the screen command and submit a script having infinite loop of resubmit after every 15min. There exits a python file named (Crab_Resubmit_infLoop.py)[]. 

How to use this:

	screen -L # -L is for log file
	#load cmssw environment
	voms-proxy-init
	source /cvmfs/cms.cern.ch/crab3/crab.csh
	python Crab_Resubmit_infLoop.py
	#type CTRL+D to detatch the terminal.

To see the status you can attach the screen using **screen -r**, or you can just see the file **screenlog.0**. Before attach the screen you have to be in same node from where you submited the script.


# DASGOCLIENT

	dasgoclient -query="summary dataset=/WPlepWMhadJJ_EWK_LO_aQGC-FT-FS-FM_mjj100VJpT10_Pythia8CUEP8M1_13TeV_Madgraph/rasharma-RunIISummer15wmLHEGS-MCRUN2_71_V1-v1_RAWSIMoutput-99cbbb113e4c1b1300a43d8e69b2780b/USER instance=prod/phys03"
