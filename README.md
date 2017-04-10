# Pythia8Hadronization

1. Run the script **SMP-RunIISummer15wmLHEGS-00029_Hadronization.sh**
	* This will load the CMSSW environment and a configuration file that can hadronize using pythia8.
2. From python configuration file created by script remove lhe output from schedule other wise it will just generate two root file once containg only lhe information and another lhe with genparticle and othere collaction as well.
3. Then you can run it using crab job.
	* **For each gridpack you need to create seperate configuration file and put the path of corresponding gridpack.**
	* **Input gridpack should be placed in the public area of lxplus**
	* **Input path of gridpack in crab configuration and in pythia8 configuration file should be identical**
