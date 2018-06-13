# CMSSW Full Simulation

1. Copy scripts form McM
	1. Total three scripts for all sequence from gridpack to MiniAOD
1. Run the scripts to get `.py` files. When you run the three shell script you will get 4 `.py` files.
1. Modify python files for command line inputs.
1. Alongwith in the first script where the input is gridpack there we have to modify few things:
	1. Modify python files for command line inputs.
	2. make sure number of events is same at all three places.
	3. add random generator. [link](https://github.com/ram1123/CMS_FulllSimulation/blob/master/FullSim/SMP-RunIISummer15wmLHEGS-00029_Hadronization_1_cfg.py.bkup#L110-L114)
	1. also change the number of parameters.
	1. See this patch: [link](https://github.com/ram1123/CMS_FulllSimulation/blob/master/FullSim/SMP-RunIISummer15wmLHEGS-00029_Hadronization_1_cfg.py.bkup#L110-L123)
	1. In line (here: [link](https://github.com/ram1123/CMS_FulllSimulation/blob/master/FullSim/SMP-RunIISummer15wmLHEGS-00029_Hadronization_1_cfg.py.bkup#L122) ) the second parameter is totoal number of events and third parameters is the random number.
	1. Also, add `.bkup` at last in the name of first `.py` file.
	1. Make sure that input and output file names remain consistent in going from one step to another.
1. run all `*.py` files as `cmsRun <configure-file-name>.py inputFiles=_0` 

# How to Run Locally

## Step1: release CMSSW 7X and 8X version

	cmsrel CMSSW_7_1_21_patch2
	cd CMSSW_7_1_21_patch2/src
	cmsenv
	cd ../../
	cmsrel CMSSW_8_0_21
	cd CMSSW_8_0_21/src
	cmsenv
	cd ../../
	cd FullSim

## Step2:

1. copy file `HIG-RunIISummer15wmLHEGS-00157_1_cfg.py.bkup` to `HIG-RunIISummer15wmLHEGS-00157_1_cfg.py`.
2. Modify the gridpack path in file `HIG-RunIISummer15wmLHEGS-00157_1_cfg.py.bkup`
3. Run it using `cmsRun HIG-RunIISummer15wmLHEGS-00157_1_cfg.py inputFiles=_0`

## Step2: Submit CMS Full sim production using condor

1. Copy here the gridpack 
2. Modify cmssw 7x and 8x path in RunFullSIM_condor.sh
3. Add gridpack name in RunFullSIM_condor.jdl 
4. Modify gridpack name in SMP-RunIISummer15wmLHEGS-00029_Hadronization_1_cfg.py.bkup
5. Modify store area path where the output will be saved in file: RunFullSIM_condor.sh. You have to add path at two places. One for saving LHE (edm format) files and another for MiniAOD files.
5. Submit condor jobs using command:

		condor_submit RunFullSIM_condor.jdl
	

# Some Important commands

1. Find all files larger than 30 MB and delete it.

	find . -type f -size +30M -exec rm {} \;
	
2. To ask for each file before delete:

	find . -type f -size +30M -exec rm -i {} \;

## Condor commands

1. To submit condor jobs:

		condor_submit <FileName>.jdl
2. To check how the condor job is proceeding:

		condor_tail <ProcessID>.<jobID> -f
3. To check status of condor jobs:

		condor_q -submitter <username>
4. To kill the condor jobs:

		condor_rm <ProcessID>.<jobID>
	

## Crab Commands:

	voms-proxy-init
	source /cvmfs/cms.cern.ch/crab3/crab.sh
	crab status <dir>
	crab submit <dir>
	crab report <dir>

# Full sim chain Ref:

	https://cms-pdmv.cern.ch/mcm/chained_requests?contains=SMP-RunIISummer15wmLHEGS-00090&page=0&shown=15
