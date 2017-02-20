# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/SMP-RunIISummer15wmLHEGS-00029-fragment.py --fileout file:SMP-RunIISummer15wmLHEGS-00029_Hadronize.root --mc --eventcontent RAWSIM,LHE --datatier GEN,LHE --conditions auto:mc --beamspot Realistic50ns13TeVCollision --step LHE,GEN --magField 38T_PostLS1 --python_filename SMP-RunIISummer15wmLHEGS-00029_Hadronization_1_cfg.py --no_exec -n 51
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(51)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/SMP-RunIISummer15wmLHEGS-00029-fragment.py nevts:51'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:SMP-RunIISummer15wmLHEGS-00029_Hadronize.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.LHEoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('LHE'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:SMP-RunIISummer15wmLHEGS-00029_Hadronize_inLHE.root'),
    outputCommands = process.LHEEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings',
	    'processParameters'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'),
	processParameters = cms.vstring(
	    #'24:onMode = off',
	    #'24:onIfAny = 11 13 15'
	    #'24:oneChannel = 1 0.5 100 11 12 13'
	    #'-24:onMode = off',
	    #'-24:onIfAny = 1 2 3 4 5'
	    #'-24:oneChannel = 1 0.5 100 1 2 3 4 5'
	    'JetMatching:setMad = off',	# Ref: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookGeneration
            'JetMatching:scheme = 1',
            'JetMatching:merge = on',
	    'JetMatching:jetAlgorithm = 2',
	    'JetMatching:etaJetMax = 5.',
	    'JetMatching:coneRadius = 1.',
	    'JetMatching:slowJetPower = 1',
	    'JetMatching:qCut = 30.', #this is the actual merging scale
	    'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
	    'JetMatching:nJetMax = 4', #number of partons in born matrix element for highest multiplicity
	    'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
	)
    ),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    #args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.4.2/VVJJ_tests/WlvWjjVBF2jets_EWK_LO_tarball.tar.xz'),
    args = cms.vstring('/uscms_data/d3/rasharma/aQGC_analysis/CMS_FulllSimulation/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_tarball_MadDefCard.tar.xz'),
    #args = cms.vstring('/afs/cern.ch/user/r/rasharma/public/GridPacks/WlvWjjVBF2jets_EWK_LO_tarball_WithoutDecay.tar.xz'),
    nEvents = cms.untracked.uint32(51),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)
process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
#process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step,process.LHEoutput_step)
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	if path in ['lhe_step']: continue
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 


