# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Date:   2021-03-15 23:05:35
# @Last Modified by:   ramkrishna
# @Last Modified time: 2021-03-19 00:58:24

import argparse

parser = argparse.ArgumentParser(description='Process Full CMSSW Simulation.')
parser.add_argument('--json',
                    type=str,
                    default='FullSimInfo.json',
                    help='Name of json file having info for each steps to be performed.')
parser.add_argument('--dirname',
                    type=str,
                    default='TEST',
                    help='Directory under EOS condor outputs')
parser.add_argument('--filename',
		    type=str,
		    default='TEST',
		    help='Condor excutable name')
parser.add_argument('--jobflavour',
		    type=str,
		    default='longlunch',
		    help='Specify the condor job flavour')


args = parser.parse_args()

import subprocess
import os
import sys

sys.path.append("./python_utils/")
from color_style import style

os.system('voms-proxy-init --voms cms --out /afs/cern.ch/user/c/chenguan/private/voms_proxy.txt --hours 4')

DirName = args.dirname
EOSPath = '/eos/user/c/chenguan/CondorOutputs/'+DirName + '/'

os.mkdir( '/eos/user/c/chenguan/CondorOutputs/'+DirName )
for subd in ['errors','outs']:
	os.mkdir( '/eos/user/c/chenguan/CondorOutputs/'+DirName+'/'+subd )
condor_file_name = args.filename

import condorJobHelper
listOfFilesToTransfer = 'EGM-RunIISummer20UL18wmLHEGEN-00001_1_cfg.py, EGM-RunIISummer20UL18SIM-00002_1_cfg.py, EGM-RunIISummer20UL18DIGIPremix-00002_1_cfg.py, EGM-RunIISummer20UL18HLT-00002_1_cfg.py, EGM-RunIISummer20UL18RECO-00002_1_cfg.py'

condorJobHelper = condorJobHelper.condorJobHelper(condor_file_name,
                                                  listOfFilesToTransfer,
                                                  12000,	# request_memory 12000
                                                  8,		# request_cpus 8
                                                  EOSPath,	# destination
						  "",   	# Arguments
                                                  3, 		# Queue
						  args.jobflavour,	# condor job flavour
                                                  )

jdlFile = condorJobHelper.jdlFileHeaderCreater()
condorJobHelper.jdlFileAppendLogInfo()
print '==> jdlfile name: ',jdlFile

outScript = open(condor_file_name+".sh","w")
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
outScript.write('\n'+'OUTDIR='+EOSPath)
outScript.write('\n'+'')
outScript.write('\n'+'echo "================================================="')
outScript.write('\n'+'echo $PWD')
outScript.write('\n'+'ls')
outScript.write('\n'+'echo "================================================="')
outScript.write('\n'+'')
outScript.write('\n'+'export X509_USER_PROXY=${1}')
outScript.write('\n'+'voms-proxy-info -all')
outScript.write('\n'+'voms-proxy-info -all -file ${1}')
outScript.write('\n'+'')
outScript.write('\n'+'echo "================================================="')
outScript.write('\n'+'')
outScript.write('\n'+'export SCRAM_ARCH=slc7_amd64_gcc700')
outScript.write('\n'+'')
########################################################################
##
##  Read JSON FILE and as per the info of json file do each steps
##  
########################################################################
import json
# with open(args.json) as json_file:
# JSON file 
f = open (args.json, "r") 
data = json.load(f)
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
    outScript.write('\n'+'cmsRun  '+steps['PythonConfig'])
    if steps['step'] == 'RECO':
	    outScript.write('\n'+'mv EGM-RunIISummer20UL18RECO-00002.root out_${2}_${3}.root')

########################################################################
outScript.close()

os.system('chmod 755 ' + condor_file_name + '.sh')
