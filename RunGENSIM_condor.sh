#!/bin/bash
echo "Starting job on " `date`
echo "Running on: `uname -a`"
echo "System software: `cat /etc/redhat-release`"
source /cvmfs/cms.cern.ch/cmsset_default.sh

OUTDIR=root://cmseos.fnal.gov//store/user/rasharma/double-higgs/SignalSample/GF_HH_Benchmark1/

echo "======="
ls
echo "======"

echo $PWD
eval `scramv1 project CMSSW CMSSW_10_2_16_patch2`
cd CMSSW_10_2_16_patch2/src/
# set cmssw environment
eval `scram runtime -sh`
cd -
echo "========================="
echo "==> Running GEN-SIM step (1001 events will be generated)"
cmsRun B2G-RunIIFall18wmLHEGS-01725_1_cfg.py 
echo "List all root files = "
ls *.root
echo "List all files"
ls 
echo "xrdcp output for condor"
for FILE in *LHEGS-01725.root
do
  echo "xrdcp -f ${FILE} ${OUTDIR}/out_inLHE_${1}_${2}.root"
  xrdcp -f ${FILE} ${OUTDIR}/out_inLHE_${1}_${2}.root 2>&1
  XRDEXIT=$?
  if [[ $XRDEXIT -ne 0 ]]; then
    rm *.root
    echo "exit code $XRDEXIT, failure in xrdcp"
    exit $XRDEXIT
  fi
  rm ${FILE}
done
date
echo "+=============================="

echo "Loading CMSSW env for DR1, DR2 and MiniAOD"

# as LHE and DR/MINIAOD are in different CMSSW reelase so change CMSSW environment
eval `scramv1 project CMSSW CMSSW_10_2_5`
cd CMSSW_10_2_5/src
echo $PWD
eval `scram runtime -sh`
cd -
cmsRun B2G-RunIIAutumn18DRPremix-02890_1_cfg.py  
cmsRun B2G-RunIIAutumn18DRPremix-02890_2_cfg.py 
cmsRun B2G-RunIIAutumn18MiniAOD-02887_1_cfg.py
echo "List all root files = "
ls *.root
echo "List all files"
ls 
echo "+=============================="

# copy output to eos
echo "xrdcp output for condor"
for FILE in B2G*MiniAOD*.root 
do
  echo "xrdcp -f ${FILE} ${OUTDIR}/out_miniAOD_${1}_${2}.root"
  xrdcp -f ${FILE} ${OUTDIR}/out_miniAOD_${1}_${2}.root 2>&1
  XRDEXIT=$?
  if [[ $XRDEXIT -ne 0 ]]; then
    rm *.root
    echo "exit code $XRDEXIT, failure in xrdcp"
    exit $XRDEXIT
  fi
  rm ${FILE}
done
date


echo "+=============================="
echo "==> Running NanoAOD..."
eval `scramv1 project CMSSW CMSSW_10_2_18`
cd CMSSW_10_2_18/src
echo $PWD
eval `scram runtime -sh`
cd -
cmsRun B2G-RunIIAutumn18NanoAODv6-01916_1_cfg.py
echo "List all root files = "
ls *.root
echo "+=============================="
# copy output to eos
echo "xrdcp output for condor"
for FILE in B2G*NanoAOD*.root 
do
  echo "xrdcp -f ${FILE} ${OUTDIR}/out_miniAOD_${1}_${2}.root"
  xrdcp -f ${FILE} ${OUTDIR}/out_nanoAOD_${1}_${2}.root 2>&1
  XRDEXIT=$?
  if [[ $XRDEXIT -ne 0 ]]; then
    rm *.root
    echo "exit code $XRDEXIT, failure in xrdcp"
    exit $XRDEXIT
  fi
  rm ${FILE}
done
date
