from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_MadDefCard_Test'
config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.JobType.pluginName = 'Analysis'
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'SMP-RunIISummer15wmLHEGS-00029_Hadronization_1_cfg.py'
config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_tarball_MadDefCard.tar.xz']
config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 2000
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/CMSSW_FullSimulation/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'
#config.Data.additional_input_files = '/afs/cern.ch/user/r/rasharma/work/aQGC_Studies/MC_SampleGeneration/LHEproduction/WlvWjjVBF2jets_EWK_LO_tarball.tar.xz'
config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.whitelist = ['T2_CH_CERN', 'T2_IT_Pisa', 'T2_RU_JINR','T2_DE_RWTH']

#NB: SAMPLES HAVE TO BE UPDATED!

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand

    #Make sure you set this parameter (here or above in the config it does not matter)
    config.General.workArea = 'Crab_Project_25Feb'

    def submit(config):
        res = crabCommand('submit', config = config)

    #########    From now on that's what users should modify: this is the a-la-CRAB2 configuration part.

    config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_CutssWW_Pythia8CUEP8M1_13TeV_Madgraph'
    config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_2c_cfg.py'
    config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_tarball_RunCard_ssWW.tar.xz']
    config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_CutssWW_Pythia8CUEP8M1_13TeV_Madgraph'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()


    config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_CutssWWVBF_Pythia8CUEP8M1_13TeV_Madgraph'
    config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_3c_cfg.py'
    config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_tarball_RunCard_ssWW_VBFcut.tar.xz']
    config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_CutssWWVBF_Pythia8CUEP8M1_13TeV_Madgraph'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()


    config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_CutssWWTighterVBF_Pythia8CUEP8M1_13TeV_Madgraph'
    config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_4c_cfg.py'
    config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_tarball_RunCard_ssWW_tigherVBFcut.tar.xz']
    config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_CutssWWTighterVBF_Pythia8CUEP8M1_13TeV_Madgraph'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
