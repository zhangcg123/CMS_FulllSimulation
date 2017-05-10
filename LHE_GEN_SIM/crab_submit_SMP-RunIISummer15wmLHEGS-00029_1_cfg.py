from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'WPlepWMhadJJ_EWK_LO_aQGC-FT-FS-FM_mjj100VJpT10_Pythia8CUEP8M1_13TeV_Madgraph'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00090_1_cfg.py'
config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_mjj100pt10_tarball.tar.xz']
config.Data.outputPrimaryDataset = 'WPlepWMhadJJ_EWK_LO_aQGC-FT-FS-FM_mjj100VJpT10_Pythia8CUEP8M1_13TeV_Madgraph'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 600
NJOBS = 10000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/lnujj/WpWm_aQGC_Ntuples_Ram/CMSSW_FullSimulation/'
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS-MCRUN2_71_V1-v1'
config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.whitelist = ['T2_CH_CERN','T3_US_FNALLPC']
