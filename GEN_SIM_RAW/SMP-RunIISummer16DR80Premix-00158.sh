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
#cmsDriver.py step1 --fileout file:SMP-RunIISummer16DR80Premix-00158_step1.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISpring15PrePremix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v2-v2/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016 --nThreads 4 --datamix PreMix --era Run2_2016 --python_filename SMP-RunIISummer16DR80Premix-00158_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10 || exit $? ; 
cmsDriver.py step1 --fileout file:SMP-RunIISummer16DR80Premix-00158_step1.root  --pileup_input  file:001EB167-3781-E611-BE3C-0CC47A4D75F4.root --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016 --nThreads 4 --datamix PreMix --era Run2_2016 --python_filename SMP-RunIISummer16DR80Premix-00158_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10 || exit $? ; 
cmsRun -e -j SMP-RunIISummer16DR80Premix-00158_rt.xml SMP-RunIISummer16DR80Premix-00158_1_cfg.py || exit $? ; 
echo 10 events were ran 
grep "TotalEvents" SMP-RunIISummer16DR80Premix-00158_rt.xml 
grep "Timing-tstoragefile-write-totalMegabytes" SMP-RunIISummer16DR80Premix-00158_rt.xml 
grep "PeakValueRss" SMP-RunIISummer16DR80Premix-00158_rt.xml 
grep "AvgEventTime" SMP-RunIISummer16DR80Premix-00158_rt.xml 
grep "AvgEventCPU" SMP-RunIISummer16DR80Premix-00158_rt.xml 
grep "TotalJobCPU" SMP-RunIISummer16DR80Premix-00158_rt.xml 
grep "EventThroughput" SMP-RunIISummer16DR80Premix-00158_rt.xml 

cmsDriver.py step2 --filein file:SMP-RunIISummer16DR80Premix-00158_step1.root --fileout file:SMP-RunIISummer16DR80Premix-00158.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,RECO,EI --nThreads 4 --era Run2_2016 --python_filename SMP-RunIISummer16DR80Premix-00158_2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10 || exit $? ; 
cmsRun -e -j SMP-RunIISummer16DR80Premix-00158_2_rt.xml SMP-RunIISummer16DR80Premix-00158_2_cfg.py || exit $? ; 
echo 10 events were ran 
grep "TotalEvents" SMP-RunIISummer16DR80Premix-00158_2_rt.xml 
grep "Timing-tstoragefile-write-totalMegabytes" SMP-RunIISummer16DR80Premix-00158_2_rt.xml 
grep "PeakValueRss" SMP-RunIISummer16DR80Premix-00158_2_rt.xml 
grep "AvgEventTime" SMP-RunIISummer16DR80Premix-00158_2_rt.xml 
grep "AvgEventCPU" SMP-RunIISummer16DR80Premix-00158_2_rt.xml 
grep "TotalJobCPU" SMP-RunIISummer16DR80Premix-00158_2_rt.xml 
grep "EventThroughput" SMP-RunIISummer16DR80Premix-00158_2_rt.xml 

