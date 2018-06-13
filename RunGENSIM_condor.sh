#!/bin/bash
echo "Starting job on " `date`
echo "Running on: `uname -a`"
echo "System software: `cat /etc/redhat-release`"
source /cvmfs/cms.cern.ch/cmsset_default.sh

### copy CMSSW tar file from store area 
xrdcp -s root://cmseos.fnal.gov//store/user/rasharma/aashaqTemp/CMS_FulllSimulation.tar .
tar -xf CMS_FulllSimulation.tar 
rm CMS_FulllSimulation.tar 
cd CMS_FulllSimulation
echo "======="
ls
echo "======"

# copy gridpack in pwd
xrdcp -s root://cmseos.fnal.gov//store/user/rasharma/aashaqTemp/ggh01_M125_Toa01a01_M20_Tomumubb_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz .

echo $PWD
eval `scramv1 project CMSSW CMSSW_7_1_25_patch3`
cd CMSSW_7_1_25_patch3/src/
# set cmssw environment
eval `scram runtime -sh`
cd -

a=$PWD
echo $a
b=$(echo $a | perl -pe 's/\//\\\//g')
echo $b

perl -pe "s/aashaqPATH/"$b"/g" HIG-RunIISummer15wmLHEGS-00157_1_cfg.py.bkup > HIG-RunIISummer15wmLHEGS-00157_1_cfg.py 
echo "========================="
cat HIG-RunIISummer15wmLHEGS-00157_1_cfg.py
echo "========================="
echo "========================="
echo "========================="
echo "========================="
cmsRun HIG-RunIISummer15wmLHEGS-00157_1_cfg.py $*
echo "List all root files = "
ls *.root
echo "List all files"
ls 
OUTDIR=root://cmseos.fnal.gov//store/user/rasharma/aashaqTemp/
echo "xrdcp output for condor"
for FILE in *inLHE*.root
do
  echo "xrdcp -f ${FILE} ${OUTDIR}/${FILE}"
  xrdcp -f ${FILE} ${OUTDIR}/${FILE} 2>&1
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

echo "Loading CMSSW env"

# as LHE and DR/MINIAOD are in different CMSSW reelase so change CMSSW environment
eval `scramv1 project CMSSW CMSSW_8_0_21`
cd CMSSW_8_0_21/src
echo $PWD
eval `scram runtime -sh`
cd -
cmsRun HIG-RunIISummer16DR80Premix-01616_1_cfg.py $*
cmsRun HIG-RunIISummer16DR80Premix-01616_2_cfg.py $*
cmsRun HIG-RunIISummer16MiniAODv2-01613_1_cfg.py $*
echo "List all root files = "
ls *.root
echo "List all files"
ls 
echo "+=============================="

# copy output to eos
#OUTDIR=root://cmseos.fnal.gov//store/user/lnujj/WpWm_aQGC_Ntuples_Ram/condor_test/
#OUTDIR=root://cmseos.fnal.gov//store/user/rasharma/condortest/
OUTDIR=root://cmseos.fnal.gov//store/user/rasharma/aashaqTemp/
echo "xrdcp output for condor"
for FILE in HIG-RunIISummer16MiniAODv2-*.root 
do
  echo "xrdcp -f ${FILE} ${OUTDIR}/${FILE}"
  xrdcp -f ${FILE} ${OUTDIR}/${FILE} 2>&1
  XRDEXIT=$?
  if [[ $XRDEXIT -ne 0 ]]; then
    rm *.root
    echo "exit code $XRDEXIT, failure in xrdcp"
    exit $XRDEXIT
  fi
  rm ${FILE}
done
date
