#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
if [ -r CMSSW_8_0_21/src ] ; then 
 echo release CMSSW_8_0_21 already exists
else
scram p CMSSW CMSSW_8_0_21
fi
cd CMSSW_8_0_21/src
eval `scram runtime -sh`

export X509_USER_PROXY=$HOME/private/personal/voms_proxy.cert

scram b
cd ../../
cmsDriver.py step1 --fileout file:SMP-RunIISummer16MiniAODv2-00156.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step PAT --nThreads 4 --era Run2_2016 --python_filename SMP-RunIISummer16MiniAODv2-00156_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1920 || exit $? ; 
cmsRun -e -j SMP-RunIISummer16MiniAODv2-00156_rt.xml SMP-RunIISummer16MiniAODv2-00156_1_cfg.py || exit $? ; 
echo 1920 events were ran 
grep "TotalEvents" SMP-RunIISummer16MiniAODv2-00156_rt.xml 
grep "AvgEventTime" SMP-RunIISummer16MiniAODv2-00156_rt.xml 
if [ $? -eq 0 ]; then
  var1=$(grep "AvgEventTime" SMP-RunIISummer16MiniAODv2-00156_rt.xml | sed "s/.* Value=\"\(.*\)\".*/\1/")
  bc -l <<< "scale=4; $var1/4"
fi
grep "EventThroughput" SMP-RunIISummer16MiniAODv2-00156_rt.xml 
if [ $? -eq 0 ]; then
  var1=$(grep "EventThroughput" SMP-RunIISummer16MiniAODv2-00156_rt.xml | sed "s/.* Value=\"\(.*\)\".*/\1/")
  bc -l <<< "scale=4; 1/$var1"
fi
