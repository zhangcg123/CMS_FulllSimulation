#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_18/src ] ; then 
 echo release CMSSW_10_2_18 already exists
 else
 scram p CMSSW CMSSW_10_2_18
 fi
 cd CMSSW_10_2_18/src
 eval `scram runtime -sh`


 scram b
 cd ../../
 cmsDriver.py step1 --filein "dbs:/RadionTohh_narrow_M-5000_TuneCP2_PSWeights_13TeV-madgraph-pythia/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM" --fileout file:B2G-RunIIAutumn18NanoAODv6-01916.root --mc --eventcontent NANOEDMAODSIM --datatier NANOAODSIM --conditions 102X_upgrade2018_realistic_v20 --step NANO --nThreads 2 --era Run2_2018,run2_nanoAOD_102Xv1 --python_filename B2G-RunIIAutumn18NanoAODv6-01916_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10 || exit $? ; 

