set i=1
set red='\e[0;31m'
set blue='\e[0;34m'
set NC='\e[0m'
while ($i >= 0) 
	echo "${blue} crab status Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_SM_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph | tee status.log ${NC}"
	crab status Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_SM_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph | tee status.log
	cat status.log | grep "failed"
	if (`grep -q "failed" status.log`) then
		echo "No jobs failed"
	else 
		echo "Severla jobs failed"
		crab resubmit Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_SM_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph
	endif
	echo "${blue} crab status Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_SM_mjj200_Pythia8CUEP8M1_13TeV_Madgraph | tee status.log ${NC}"
	crab status Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_SM_mjj200_Pythia8CUEP8M1_13TeV_Madgraph | tee status.log
	cat status.log | grep "failed"
	if (`grep -q "failed" status.log`) then
		echo "No jobs failed"
	else 
		echo "Severla jobs failed"
		crab resubmit Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_SM_mjj200_Pythia8CUEP8M1_13TeV_Madgraph
	endif
	echo "${blue} crab status Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_LO_SMNoDecay_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph | tee status.log ${NC}"
	crab status Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_LO_SMNoDecay_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph | tee status.log
	cat status.log | grep "failed"
	if (`grep -q "failed" status.log`) then
		echo "No jobs failed"
	else 
		echo "Severla jobs failed"
		crab resubmit Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_LO_SMNoDecay_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph
	endif
	echo "${blue} crab status Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_LO_SMNoDecay_mjj200_Pythia8CUEP8M1_13TeV_Madgraph | tee status.log ${NC}"
	crab status Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_LO_SMNoDecay_mjj200_Pythia8CUEP8M1_13TeV_Madgraph | tee status.log
	cat status.log | grep "failed"
	if (`grep -q "failed" status.log`) then
		echo "No jobs failed"
	else 
		echo "Severla jobs failed"
		crab resubmit Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_LO_SMNoDecay_mjj200_Pythia8CUEP8M1_13TeV_Madgraph
	endif
	echo "${blue} crab status Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_LO_NPle1_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph | tee status.log ${NC}"
	crab status Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_LO_NPle1_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph | tee status.log
	cat status.log | grep "failed"
	if (`grep -q "failed" status.log`) then
		echo "No jobs failed"
	else 
		echo "Severla jobs failed"
		crab resubmit Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_LO_NPle1_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph
	endif
	echo "${blue} crab status Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_LO_NPle1_mjj200_Pythia8CUEP8M1_13TeV_Madgraph | tee status.log ${NC}"
	crab status Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_LO_NPle1_mjj200_Pythia8CUEP8M1_13TeV_Madgraph | tee status.log
	cat status.log | grep "failed"
	if (`grep -q "failed" status.log`) then
		echo "No jobs failed"
	else 
		echo "Severla jobs failed"
		crab resubmit Crab_Project_25Feb/crab_aQGC_WPlepWMhadJJ_EWK_LO_NPle1_mjj200_Pythia8CUEP8M1_13TeV_Madgraph
	endif
	date
	echo "${red}Run Number = $i${NC}"
	sleep 30m
	@ i++
end
