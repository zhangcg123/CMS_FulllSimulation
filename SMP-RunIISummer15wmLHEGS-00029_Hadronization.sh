#!/bin/bash
#source  /afs/cern.ch/cms/cmsset_default.sh
if [ -r CMSSW_8_0_12/src ] ; then 
 echo release CMSSW_8_0_12 already exists
else
scram p CMSSW CMSSW_8_0_12
fi
cd CMSSW_8_0_12/src
eval `scram runtime -sh`

export X509_USER_PROXY=$HOME/private/personal/voms_proxy.cert
curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/SMP-RunIISummer15wmLHEGS-00029 --retry 2 --create-dirs -o Configuration/GenProduction/python/SMP-RunIISummer15wmLHEGS-00029-fragment.py 
[ -s Configuration/GenProduction/python/SMP-RunIISummer15wmLHEGS-00029-fragment.py ] || exit $?;

scram b
cd ../../
cmsDriver.py Configuration/GenProduction/python/SMP-RunIISummer15wmLHEGS-00029-fragment.py --fileout file:SMP-RunIISummer15wmLHEGS-00029_Hadronize.root --mc --eventcontent RAWSIM,LHE --datatier GEN,LHE --conditions auto:mc --beamspot Realistic50ns13TeVCollision --step LHE,GEN --magField 38T_PostLS1 --python_filename SMP-RunIISummer15wmLHEGS-00029_Hadronization_1_cfg.py --no_exec -n 51 || exit $? ; 
cmsRun -e -j SMP-RunIISummer15wmLHEGS-00029_rt.xml SMP-RunIISummer15wmLHEGS-00029_Hadronization_1_cfg.py || exit $? ; 
echo 51 events were ran 
grep "TotalEvents" SMP-RunIISummer15wmLHEGS-00029_rt.xml 
grep "Timing-tstoragefile-write-totalMegabytes" SMP-RunIISummer15wmLHEGS-00029_rt.xml 
grep "PeakValueRss" SMP-RunIISummer15wmLHEGS-00029_rt.xml 
grep "AvgEventTime" SMP-RunIISummer15wmLHEGS-00029_rt.xml 
grep "AvgEventCPU" SMP-RunIISummer15wmLHEGS-00029_rt.xml 
grep "TotalJobCPU" SMP-RunIISummer15wmLHEGS-00029_rt.xml 
