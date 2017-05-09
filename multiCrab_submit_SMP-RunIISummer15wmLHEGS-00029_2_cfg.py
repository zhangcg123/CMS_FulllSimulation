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
#config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_tarball_MadDefCard.tar.xz']
config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 600
NJOBS = 1998  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/CMSSW_FullSimulation_April2017/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'
#config.Data.additional_input_files = '/afs/cern.ch/user/r/rasharma/work/aQGC_Studies/MC_SampleGeneration/LHEproduction/WlvWjjVBF2jets_EWK_LO_tarball.tar.xz'
config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.whitelist = ['T2_CH_CERN', 'T2_IT_Pisa', 'T2_RU_JINR','T2_DE_RWTH']

#NB: SAMPLES HAVE TO BE UPDATED!

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand

    #Make sure you set this parameter (here or above in the config it does not matter)
    config.General.workArea = 'Crab_Project_25Feb'

    def submit(config):
        res = crabCommand('submit', config = config)

    #########    From now on that's what users should modify: this is the a-la-CRAB2 configuration part.

    #config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_SM_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_1_cfg.py'
    #config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_SM_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_SM_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    #config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_SM_mjj200_Pythia8CUEP8M1_13TeV_Madgraph'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_2_cfg.py'
    #config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_SM_RunCardChanged_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_SM_mjj200_Pythia8CUEP8M1_13TeV_Madgraph'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    #config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_3_cfg.py'
    #config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_DefaultRunCard_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    #config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_mjj200_Pythia8CUEP8M1_13TeV_Madgraph'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_4_cfg.py'
    #config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_RunCardChanged_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_mjj200_Pythia8CUEP8M1_13TeV_Madgraph'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    #config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_SMNoDecay_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_5_cfg.py'
    #config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_SM_WithoutDecay_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_LO_SMNoDecay_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    #config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_SMNoDecay_mjj200_Pythia8CUEP8M1_13TeV_Madgraph'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_6_cfg.py'
    #config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_SM_WithoutDecay_mjj200_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_LO_SMNoDecay_mjj200_Pythia8CUEP8M1_13TeV_Madgraph'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    #config.General.requestName = 'aQGC_ENuQQJJ_EWK_LO_SM_Pythia8CUEP8M1_13TeV_Madgraph'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_7_cfg.py'
    ##config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_ENuQQJJ_EWK_LO_SM_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_ENuQQJJ_EWK_LO_SM_Pythia8CUEP8M1_13TeV_Madgraph'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    #config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_RunCardChanged_InitilaizeAllaQGCPar_Pythia8CUEP8M1_13TeV_Madgraph'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_8_cfg.py'
    #config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_RunCardChanged_aQGCSetAllPar_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_RunCardChanged_InitilaizeAllaQGCPar_Pythia8CUEP8M1_13TeV_Madgraph'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    #config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_mjj100VJpT10_Pythia8CUEP8M1_13TeV_Madgraph'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_9_cfg.py'
    #config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_mjj100pt10_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_mjj100VJpT10_Pythia8CUEP8M1_13TeV_Madgraph'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()


    #config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_FT010e12_Pythia8CUEP8M1_13TeV_Madgraph'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_10_cfg.py'
    #config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_RunCardChanged_FT010e12_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_FT010e12_Pythia8CUEP8M1_13TeV_Madgraph'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    #config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_FT08e12_Pythia8CUEP8M1_13TeV_Madgraph'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_11_cfg.py'
    #config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_RunCardChanged_FT08e12_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_FT08e12_Pythia8CUEP8M1_13TeV_Madgraph'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    #config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_FT014e12_Pythia8CUEP8M1_13TeV_Madgraph'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_12_cfg.py'
    #config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_RunCardChanged_FT014e12_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_FT014e12_Pythia8CUEP8M1_13TeV_Madgraph'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    #config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_FT06e12_Pythia8CUEP8M1_13TeV_Madgraph_v2'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_13_cfg.py'
    #config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_RunCardChanged_FT06e12_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_FT06e12_Pythia8CUEP8M1_13TeV_Madgraph_v2'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    #config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_FT016e12_Pythia8CUEP8M1_13TeV_Madgraph'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_14_cfg.py'
    #config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_RunCardChanged_FT016e12_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_FT016e12_Pythia8CUEP8M1_13TeV_Madgraph'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    #config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_SM_Pythia8CUEP8M1_13TeV_Madgraph_RwgtValidation_v2'
    #config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_15_cfg.py'
    #config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_SM_RwgtValidation_tarball.tar.xz']
    #config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_LO_SM_Pythia8CUEP8M1_13TeV_Madgraph_RwgtValidation_v2'
    #from multiprocessing import Process
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    config.General.requestName = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_Pythia8CUEP8M1_13TeV_Madgraph_RwgtValidation'
    config.JobType.psetName =  'SMP-RunIISummer15wmLHEGS-00029_Hadronization_16_cfg.py'
    config.JobType.inputFiles = ['/afs/cern.ch/user/r/rasharma/work/public/GridPacks/New/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_RwgtValidation_tarball.tar.xz']
    config.Data.outputPrimaryDataset = 'aQGC_WPlepWMhadJJ_EWK_LO_NPle1_Pythia8CUEP8M1_13TeV_Madgraph_RwgtValidation'
    from multiprocessing import Process
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
