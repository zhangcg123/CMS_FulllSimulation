# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Date:   2021-03-15 23:05:35
# @Last Modified by:   ramkrishna
# @Last Modified time: 2021-03-19 00:58:24

import argparse

parser = argparse.ArgumentParser(description='Process Full CMSSW Simulation.')
parser.add_argument('--eospath', 
                    type=str, 
                    default="/eos/user/r/rasharma/post_doc_ihep/H4LStudies/FullSim/", 
                    help='Add the eos path for output'
                    )
parser.add_argument('--json',
                    type=str,
                    default='FullSimInfo.json',
                    help='Name of json file having info for each steps to be performed.')
parser.add_argument('--suffix',
                    type=str,
                    default='TEST',
                    help='Suffix to be added in the output directory')

args = parser.parse_args()
# print(args)

import subprocess
import os
import sys

sys.path.append("Utils/python_utils/.")
from color_style import style


StringToChange = args.suffix
condor_file_name = StringToChange
output_log_path = StringToChange
storeAreaPath = args.eospath
storeAreaPathWithEOSString = storeAreaPath
EOSOutPutPathWithEOSRedirector = 'root://cmseos.fnal.gov/'+storeAreaPath+os.sep+StringToChange

import condorJobHelper
listOfFilesToTransfer = 'B2G-RunIISummer20UL17DIGIPremix-00001_1_cfg.py,  B2G-RunIISummer20UL17MiniAODv2-00068_1_cfg.py,  B2G-RunIISummer20UL17SIM-00001_1_cfg.py, B2G-RunIISummer20UL17HLT-00001_1_cfg.py, B2G-RunIISummer20UL17RECO-00001_1_cfg.py, B2G-RunIISummer20UL17wmLHEGEN-00005_1_cfg.py'
condorJobHelper = condorJobHelper.condorJobHelper(condor_file_name,
                                                  listOfFilesToTransfer,
                                                  12000,    # request_memory 12000
                                                  8,    # request_cpus 8
                                                  output_log_path,
                                                  'test',   # logFileName
                                                  "",   # Arguments
                                                  50 # Queue
                                                  )

# jdlFile = condorJobHelper.jdlFileHeaderCreater()
# print '==> jdlfile name: ',jdlFile

outScript = open(condor_file_name+".sh","w");

outScript.write('#!/bin/bash')
outScript.write('\n'+'echo "Starting job on " `date`')
outScript.write('\n'+'echo "Running on: `uname -a`"')
outScript.write('\n'+'echo "System software: `cat /etc/redhat-release`"')
outScript.write('\n'+'source /cvmfs/cms.cern.ch/cmsset_default.sh')
outScript.write('\n'+'echo "'+'#'*51+'"')
outScript.write('\n'+'echo "#    List of Input Arguments: "')
outScript.write('\n'+'echo "'+'#'*51+'"')
outScript.write('\n'+'echo "Input Arguments: $1"')
outScript.write('\n'+'echo "Input Arguments: $2"')
outScript.write('\n'+'echo "Input Arguments: $3"')
outScript.write('\n'+'echo "Input Arguments: $4"')
outScript.write('\n'+'echo "Input Arguments: $5"')
outScript.write('\n'+'echo "'+'#'*51+'"')
outScript.write('\n'+'')
outScript.write('\n'+'OUTDIR='+EOSOutPutPathWithEOSRedirector)
outScript.write('\n'+'')
outScript.write('\n'+'echo "================================================="')
outScript.write('\n'+'echo $PWD')
outScript.write('\n'+'ls')
outScript.write('\n'+'echo "================================================="')
outScript.write('\n'+'')
########################################################################
##
##  Read JSON FILE and as per the info of json file do each steps
##  
########################################################################
import json
from collections import OrderedDict
# with open(args.json) as json_file:
# JSON file 
f = open (args.json, "r") 
data = json.loads(f.read(),object_pairs_hook=OrderedDict)
for steps in data['steps']:
    # print(steps['RandomSeed'])
    outScript.write('\n'+'echo "'+'#'*51+'"')
    outScript.write('\n'+'echo "##"')
    outScript.write('\n'+'echo "##\t STEP: '+steps['step']+'"')
    outScript.write('\n'+'echo "##"')
    outScript.write('\n'+'echo "'+'#'*51+'"')
    outScript.write('\n'+'eval `scramv1 project CMSSW '+steps['CMSSWVersion']+'`')
    outScript.write('\n'+'cd '+steps['CMSSWVersion']+'/src/')
    outScript.write('\n'+'# set cmssw environment')
    outScript.write('\n'+'eval `scram runtime -sh`')
    outScript.write('\n'+'cd -')
    if (steps['step']=="wmLHEGEN"): 
        outScript.write("\n"+'sed -i "s|args = cms.vstring.*|args = cms.vstring(\\"${1}\\"),|g" '+steps['PythonConfig']+' ')
        outScript.write('\n'+'echo "+============================================================"')
        outScript.write('\n'+'cat   '+steps['PythonConfig'])    
        outScript.write('\n'+'echo "+============================================================"')
    outScript.write('\n'+'cmsRun  '+steps['PythonConfig'])
    outScript.write('\n'+'echo "+============================================================"')
    outScript.write('\n'+'echo "List all root files = "')
    outScript.write('\n'+'ls *.root')
    outScript.write('\n'+'echo "+============================================================"')

########################################################################
outScript.close();

"""

outScript.write('\n'+'echo "List all root files = "')
outScript.write('\n'+'ls *.root')
outScript.write('\n'+'echo "List all files"')
outScript.write('\n'+'ls ')
outScript.write('\n'+'cp B2G-RunIIFall18wmLHEGS-01725.root out_inLHE_${1}_${2}.root')
outScript.write('\n'+'echo "========================="')
outScript.write('\n'+'echo "==> List all files..."')
outScript.write('\n'+'ls *.root ')
outScript.write('\n'+'echo "+=============================="')
outScript.write('\n'+'echo "xrdcp output for condor"')
outScript.write('\n'+'xrdcp -f out_inLHE_${1}_${2}.root ${OUTDIR}/out_inLHE_${1}_${2}.root')
outScript.write('\n'+'echo "========================="')
outScript.write('\n'+'echo "==> List all files..."')
outScript.write('\n'+'ls *.root ')
outScript.write('\n'+'echo "+=============================="')
outScript.write('\n'+'date')
outScript.write('\n'+'echo "+=============================="')
outScript.write('\n'+'')
outScript.write('\n'+'echo "Loading CMSSW env DR1, DR2 and MiniAOD"')
outScript.write('\n'+'')
outScript.write('\n'+'# as LHE and DR/MINIAOD are in different CMSSW reelase so change CMSSW environment')
outScript.write('\n'+'eval `scramv1 project CMSSW CMSSW_10_2_5`')
outScript.write('\n'+'cd CMSSW_10_2_5/src')
outScript.write('\n'+'echo "pwd : ${PWD}"')
outScript.write('\n'+'eval `scram runtime -sh`')
outScript.write('\n'+'cd -')
outScript.write('\n'+'echo "========================="')
outScript.write('\n'+'echo "==> List all files..."')
outScript.write('\n'+'echo "pwd : ${PWD}"')
outScript.write('\n'+'ls ')
outScript.write('\n'+'echo "+=============================="')
outScript.write('\n'+'echo "==> cmsRun B2G-RunIIAutumn18DRPremix-02890_1_cfg.py" ')
outScript.write('\n'+'cmsRun B2G-RunIIAutumn18DRPremix-02890_1_cfg.py  ')
outScript.write('\n'+'echo "==> cmsRun B2G-RunIIAutumn18DRPremix-02890_2_cfg.py"')
outScript.write('\n'+'cmsRun B2G-RunIIAutumn18DRPremix-02890_2_cfg.py ')
outScript.write('\n'+'echo "==> cmsRun B2G-RunIIAutumn18MiniAOD-02887_1_cfg.py"')
outScript.write('\n'+'cmsRun B2G-RunIIAutumn18MiniAOD-02887_1_cfg.py')
outScript.write('\n'+'echo "========================="')
outScript.write('\n'+'echo "==> List all files..."')
outScript.write('\n'+'echo "pwd : ${PWD}"')
outScript.write('\n'+'ls ')
outScript.write('\n'+'echo "+=============================="')
outScript.write('\n'+'echo "List all root files = "')
outScript.write('\n'+'ls *.root')
outScript.write('\n'+'echo "List all files"')
outScript.write('\n'+'ls ')
outScript.write('\n'+'echo "+=============================="')
outScript.write('\n'+'')
outScript.write('\n'+'# copy output to eos')
outScript.write('\n'+'echo "xrdcp output for condor"')
outScript.write('\n'+'cp B2G-RunIIAutumn18MiniAOD-02887.root out_MiniAOD_${1}_${2}.root')
outScript.write('\n'+'echo "========================="')
outScript.write('\n'+'echo "==> List all files..."')
outScript.write('\n'+'ls *.root ')
outScript.write('\n'+'echo "+=============================="')
outScript.write('\n'+'echo "xrdcp output for condor"')
outScript.write('\n'+'xrdcp -f out_MiniAOD_${1}_${2}.root ${OUTDIR}/out_MiniAOD_${1}_${2}.root')
outScript.write('\n'+'echo "========================="')
outScript.write('\n'+'echo "==> List all files..."')
outScript.write('\n'+'ls *.root ')
outScript.write('\n'+'echo "+=============================="')
outScript.write('\n'+'date')
outScript.write('\n'+'')
outScript.write('\n'+'')
outScript.write('\n'+'echo "+=============================="')
outScript.write('\n'+'echo "==> Running NanoAOD..."')
outScript.write('\n'+'eval `scramv1 project CMSSW CMSSW_10_2_18`')
outScript.write('\n'+'cd CMSSW_10_2_18/src')
outScript.write('\n'+'echo $PWD')
outScript.write('\n'+'eval `scram runtime -sh`')
outScript.write('\n'+'cd -')
outScript.write('\n'+'cmsRun B2G-RunIIAutumn18NanoAODv6-01916_1_cfg.py')
outScript.write('\n'+'echo "List all root files = "')
outScript.write('\n'+'ls *.root')
outScript.write('\n'+'echo "+=============================="')
outScript.write('\n'+'# copy output to eos')
outScript.write('\n'+'echo "xrdcp output for condor"')
outScript.write('\n'+'echo "xrdcp -f B2G-RunIIAutumn18NanoAODv6-01916.root ${OUTDIR}/out_NanoAOD_${1}_${2}.root"')
outScript.write('\n'+'echo "+=============================="')
outScript.write('\n'+'xrdcp -f B2G-RunIIAutumn18NanoAODv6-01916.root ${OUTDIR}/out_NanoAOD_${1}_${2}.root')
outScript.write('\n'+'echo "+=============================="')
outScript.write('\n'+'echo "Done."')
outScript.write('\n'+'date')

outScript.close();

os.system("chmod 777 "+condor_file_name+".sh");

print "===> Set Proxy Using:";
print "\tvoms-proxy-init --voms cms --valid 168:00";
print "\"condor_submit "+condor_file_name+".jdl\" to submit";

"""