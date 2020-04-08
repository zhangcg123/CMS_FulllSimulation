# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/RadionTohh_narrow_M-5000_TuneCP2_PSWeights_13TeV-madgraph-pythia/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM --fileout file:B2G-RunIIAutumn18NanoAODv6-01916.root --mc --eventcontent NANOEDMAODSIM --datatier NANOAODSIM --conditions 102X_upgrade2018_realistic_v20 --step NANO --nThreads 2 --era Run2_2018,run2_nanoAOD_102Xv1 --python_filename B2G-RunIIAutumn18NanoAODv6-01916_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1001
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('NANO',eras.Run2_2018,eras.run2_nanoAOD_102Xv1)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1001)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:B2G-RunIIAutumn18MiniAOD-02887.root'
        #'/store/mc/RunIIAutumn18MiniAOD/RadionTohh_narrow_M-5000_TuneCP2_PSWeights_13TeV-madgraph-pythia/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/6C35DB53-492E-5141-AFC6-1BA93E4C7E77.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/RadionTohh_narrow_M-5000_TuneCP2_PSWeights_13TeV-madgraph-pythia/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/FBFB9CD2-39EE-644D-8368-8FE169D0E4C8.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/RadionTohh_narrow_M-5000_TuneCP2_PSWeights_13TeV-madgraph-pythia/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/E49B4E97-88A3-5A46-9F14-561860C25DE4.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/RadionTohh_narrow_M-5000_TuneCP2_PSWeights_13TeV-madgraph-pythia/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/FB09BA62-3889-6346-8558-B3710CA1A745.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/RadionTohh_narrow_M-5000_TuneCP2_PSWeights_13TeV-madgraph-pythia/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/39FAA23D-DA83-164B-B01F-83D7A4600203.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/RadionTohh_narrow_M-5000_TuneCP2_PSWeights_13TeV-madgraph-pythia/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/B0AB5644-7179-AE4E-B9FA-953E309E5E6C.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/RadionTohh_narrow_M-5000_TuneCP2_PSWeights_13TeV-madgraph-pythia/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/878D43DB-625A-B542-9982-9F319E9A0CA7.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/RadionTohh_narrow_M-5000_TuneCP2_PSWeights_13TeV-madgraph-pythia/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/523064FD-0D69-AA4F-84F0-EC439C04E836.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/RadionTohh_narrow_M-5000_TuneCP2_PSWeights_13TeV-madgraph-pythia/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/8BA16351-0D82-5C44-94B7-7B7BDD3D8ED1.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/RadionTohh_narrow_M-5000_TuneCP2_PSWeights_13TeV-madgraph-pythia/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/AF9B95D4-AA63-404C-853A-5CCB7C3DEB49.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/RadionTohh_narrow_M-5000_TuneCP2_PSWeights_13TeV-madgraph-pythia/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/DFA49513-A4D7-CF43-BD33-39E7285BF6A4.root', 
        #'/store/mc/RunIIAutumn18MiniAOD/RadionTohh_narrow_M-5000_TuneCP2_PSWeights_13TeV-madgraph-pythia/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/283CD336-85AB-214E-AC7C-0D194084E397.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:1001'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOEDMAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:B2G-RunIIAutumn18NanoAODv6-01916.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v20', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOEDMAODSIMoutput_step = cms.EndPath(process.NANOEDMAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOEDMAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
