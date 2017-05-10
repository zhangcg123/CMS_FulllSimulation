#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc481
if [ -r CMSSW_7_1_21_patch2/src ] ; then 
 echo release CMSSW_7_1_21_patch2 already exists
else
scram p CMSSW CMSSW_7_1_21_patch2
fi
cd CMSSW_7_1_21_patch2/src
eval `scram runtime -sh`

export X509_USER_PROXY=$HOME/private/personal/voms_proxy.cert
curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/SMP-RunIISummer15wmLHEGS-00090 --retry 2 --create-dirs -o Configuration/GenProduction/python/SMP-RunIISummer15wmLHEGS-00090-fragment.py 
[ -s Configuration/GenProduction/python/SMP-RunIISummer15wmLHEGS-00090-fragment.py ] || exit $?;

scram b
cd ../../
cmsDriver.py Configuration/GenProduction/python/SMP-RunIISummer15wmLHEGS-00090-fragment.py --fileout file:SMP-RunIISummer15wmLHEGS-00090.root --mc --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN,SIM --magField 38T_PostLS1 --python_filename SMP-RunIISummer15wmLHEGS-00090_1_cfg.py --no_exec -n 41 || exit $? ; 
cmsRun -e -j SMP-RunIISummer15wmLHEGS-00090_rt.xml SMP-RunIISummer15wmLHEGS-00090_1_cfg.py || exit $? ; 
echo 41 events were ran 
grep "TotalEvents" SMP-RunIISummer15wmLHEGS-00090_rt.xml 
grep "Timing-tstoragefile-write-totalMegabytes" SMP-RunIISummer15wmLHEGS-00090_rt.xml 
grep "PeakValueRss" SMP-RunIISummer15wmLHEGS-00090_rt.xml 
grep "AvgEventTime" SMP-RunIISummer15wmLHEGS-00090_rt.xml 
grep "AvgEventCPU" SMP-RunIISummer15wmLHEGS-00090_rt.xml 
grep "TotalJobCPU" SMP-RunIISummer15wmLHEGS-00090_rt.xml 
grep "EventThroughput" SMP-RunIISummer15wmLHEGS-00090_rt.xml 
