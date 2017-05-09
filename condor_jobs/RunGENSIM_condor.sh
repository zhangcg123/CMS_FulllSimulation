#!/bin/bash
cd  /uscms_data/d3/rasharma/aQGC_analysis/CMS_FulllSimulation/CMSSW_8_0_12/src/
eval `scram runtime -sh`
cd -
a=$PWD
echo $a
b=$(echo $a | perl -pe 's/\//\\\//g')
echo $b
perl -pe "s/RAMPATH/"$b"/g" SMP-RunIISummer15wmLHEGS-00029_Hadronization_1_cfg.py.bkup > SMP-RunIISummer15wmLHEGS-00029_Hadronization_1_cfg.py
cmsRun SMP-RunIISummer15wmLHEGS-00029_Hadronization_1_cfg.py
