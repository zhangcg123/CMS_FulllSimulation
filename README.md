# CMSSW Full Simulation

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
