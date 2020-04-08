#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_16_patch2/src ] ; then 
 echo release CMSSW_10_2_16_patch2 already exists
else
scram p CMSSW CMSSW_10_2_16_patch2
fi
cd CMSSW_10_2_16_patch2/src
eval `scram runtime -sh`

curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/B2G-RunIIFall18wmLHEGS-01725 --retry 2 --create-dirs -o Configuration/GenProduction/python/B2G-RunIIFall18wmLHEGS-01725-fragment.py 
[ -s Configuration/GenProduction/python/B2G-RunIIFall18wmLHEGS-01725-fragment.py ] || exit $?;

scram b
cd ../../
#seed=$(($(date +%s) % 100 + 1))
#cmsDriver.py Configuration/GenProduction/python/B2G-RunIIFall18wmLHEGS-01725-fragment.py --fileout file:B2G-RunIIFall18wmLHEGS-01725.root --mc --eventcontent RAWSIM,LHE,DQM --datatier GEN-SIM,LHE,DQMIO --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step LHE,GEN,SIM,VALIDATION:genvalid_all --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename B2G-RunIIFall18wmLHEGS-01725_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${seed})" -n 317 || exit $? ; 
cmsDriver.py Configuration/GenProduction/python/B2G-RunIIFall18wmLHEGS-01725-fragment.py --fileout file:B2G-RunIIFall18wmLHEGS-01725.root --mc --eventcontent RAWSIM,LHE,DQM --datatier GEN-SIM,LHE,DQMIO --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step LHE,GEN,SIM,VALIDATION:genvalid_all --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename B2G-RunIIFall18wmLHEGS-01725_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring  -n 51 || exit $? ; 
