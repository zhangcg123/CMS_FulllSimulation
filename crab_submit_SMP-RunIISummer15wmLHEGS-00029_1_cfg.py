from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_MadDefCard'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'SMP-RunIISummer15wmLHEGS-00029_Hadronization_1_cfg.py'
config.JobType.inputFiles = ['/uscms_data/d3/rasharma/aQGC_analysis/CMS_FulllSimulation/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_tarball_MadDefCard.tar.xz']

config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_MadDefCard'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
NJOBS = 200  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/CMSSW_FullSimulation/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'
#config.Data.additional_input_files = '/afs/cern.ch/user/r/rasharma/work/aQGC_Studies/MC_SampleGeneration/LHEproduction/WlvWjjVBF2jets_EWK_LO_tarball.tar.xz'
config.Site.storageSite = 'T3_US_FNALLPC'
