## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

# turn on when running on MC
runOnMC = True

# AK5 sequence with pileup substraction is the default
# the other sequences can be turned off with the following flags.
## True -> run also sequence without PU subtraction
runAK5NoPUSub = True 

### enable PU correction ##########
doJetPileUpCorrection = True
##################################

#add the L2L3Residual corrections only for data
if runOnMC:#MC
    jetCorrections=['L1FastJet','L2Relative','L3Absolute']
else:#Data
    jetCorrections=['L1FastJet','L2Relative','L3Absolute','L2L3Residual']

############ general options ####################
process.options.wantSummary = True
process.maxEvents.input = 400
process.MessageLogger.cerr.FwkReport.reportEvery = 100
########### global tag ############################
#from CMGTools.Common.Tools.getGlobalTag import getGlobalTag
#process.GlobalTag.globaltag = cms.string(getGlobalTag(runOnMC))
process.GlobalTag.globaltag = 'START52_V11B::All'
##################################################

############ PRINTOUT ###################

sep_line = "-" * 50
print sep_line
print 'running the following PFBRECO+PAT sequences:'
print '\tAK5'
if runAK5NoPUSub: print '\tAK5NoPUSub'
#print 'embedding in taus: ', doEmbedPFCandidatesInTaus
#print 'HPS taus         : ', hpsTaus
#print 'produce CMG tuple: ', runCMG
print 'run on MC        : ', runOnMC
print sep_line
print 'Global tag       : ', process.GlobalTag.globaltag
print sep_line

######################################################
    
### INPUT COLLECTIONS ##########

process.source.fileNames = [
    'file:/data3/scratch/cms/mc/Summer12/PU_S7_START52_V5-v2/DYJetsToLL_M-50/FE123555-F27A-E111-8E40-003048D46046.root'
#    'file:/data3/scratch/cms/mc/Summer12/TTJets_TuneZ2star_8TeV/FEDDBC6A-9290-E111-B7FD-0018F3D09628.root'
#    '/store/mc/Summer12/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S7_START52_V5-v2/0000/FE123555-F27A-E111-8E40-003048D46046.root',
#    '/store/mc/Summer12/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S7_START52_V5-v2/0000/FA178E3B-CB7A-E111-88E9-003048D460B6.root',
#    '/store/mc/Summer12/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S7_START52_V5-v2/0000/FA28D4A9-D37A-E111-B990-001A64789E00.root',
#    '/store/mc/Summer12/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S7_START52_V5-v2/0000/FAB6476C-D37A-E111-81A2-0025B3E063EA.root',
#    '/store/mc/Summer12/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S7_START52_V5-v2/0000/FC6345EE-D17A-E111-9656-001A64789D8C.root',
#    '/store/mc/Summer12/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S7_START52_V5-v2/0000/FE123555-F27A-E111-8E40-003048D46046.root'
]

### DEFINITION OF THE PFBRECO+PAT SEQUENCES ##########
# load the PAT config
process.load("PhysicsTools.PatAlgos.patSequences_cff")
from PhysicsTools.PatAlgos.tools.coreTools import *

# Configure PAT to use PFBRECO instead of AOD sources
# this function will modify the PAT sequences.
from PhysicsTools.PatAlgos.tools.pfTools import *

# ---------------- rho calculation for JEC ----------------------

from RecoJets.JetProducers.kt4PFJets_cfi import kt4PFJets

process.kt6PFJets = kt4PFJets.clone(
    rParam = cms.double(0.6),
    doAreaFastjet = cms.bool(True),
    doRhoFastjet = cms.bool(True),
)

#compute rho correction for lepton isolation
process.kt6PFJetsCHS = process.kt6PFJets.clone(
    src = cms.InputTag("pfNoElectronAK5") )
process.kt6PFJetsForIso = process.kt6PFJets.clone(
    Rho_EtaMax = cms.double(2.5),
    Ghost_EtaMax = cms.double(2.5) )
process.kt6PFJetsCHSForIso = process.kt6PFJets.clone(
    Rho_EtaMax = cms.double(2.5),
    Ghost_EtaMax = cms.double(2.5),
    src = cms.InputTag("pfNoElectronAK5") )

# ---------------- Sequence AK5 ----------------------

# PFBRECO+PAT sequence 1:
# no lepton cleaning, AK5PFJets

postfixAK5 ="AK5"
jetAlgoAK5 ="AK5"

usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgoAK5, runOnMC=runOnMC, postfix=postfixAK5, jetCorrections=('AK5PFchs', jetCorrections))

removeSpecificPATObjects(process, ['Taus'], postfix = "AK5")
removeSpecificPATObjects(process, ['Muons'], postfix = "AK5")
removeSpecificPATObjects(process, ['Electrons'], postfix = "AK5")

############### remove useless modules ####################
def removeUseless( modName ):
    getattr(process,"patDefaultSequence"+postfixAK5).remove(
        getattr(process, modName+postfixAK5)
        )

removeUseless( "produceCaloMETCorrections" )
removeUseless( "pfCandsNotInJet" )
removeUseless( "pfJetMETcorr" )
removeUseless( "pfCandMETcorr" )
removeUseless( "pfchsMETcorr" )
removeUseless( "pfType1CorrectedMet" )
removeUseless( "pfType1p2CorrectedMet" )
#########################################################

# removing default cuts on muons 
getattr(process,"pfMuonsFromVertexAK5").dzCut = 99
getattr(process,"pfMuonsFromVertexAK5").d0Cut = 99
getattr(process,"pfSelectedMuonsAK5").cut="pt()>3"

# removing default cuts on electrons 
getattr(process,"pfElectronsFromVertexAK5").dzCut = 99
getattr(process,"pfElectronsFromVertexAK5").d0Cut = 99
getattr(process,"pfSelectedElectronsAK5").cut="pt()>5"

############ recipe for PU correction ##########################

if doJetPileUpCorrection:
    from CommonTools.ParticleFlow.Tools.enablePileUpCorrection import enablePileUpCorrection
    enablePileUpCorrection( process, postfix=postfixAK5 )
    # avoid double calculation of rho (introduced by jetTools in PAT)
    getattr(process,'patDefaultSequence'+postfixAK5).remove(getattr(process,'ak5PFJets'+postfixAK5))
    getattr(process,'patDefaultSequence'+postfixAK5).remove(getattr(process,'kt6PFJets'+postfixAK5))
    getattr(process,'patDefaultSequence'+postfixAK5).remove(getattr(process,'kt6PFJets'+postfixAK5))
    getattr(process,"patJetCorrFactors"+postfixAK5).rho = cms.InputTag("kt6PFJets", "rho")

################################################################

# curing a weird bug in PAT..
from CMGTools.Common.PAT.removePhotonMatching import removePhotonMatching
removePhotonMatching( process, postfixAK5 )

getattr(process,"pfNoMuon"+postfixAK5).enable = False 
getattr(process,"pfNoElectron"+postfixAK5).enable = False 
getattr(process,"pfNoTau"+postfixAK5).enable = False 
getattr(process,"pfNoJet"+postfixAK5).enable = True
getattr(process,"pfIsolatedMuons"+postfixAK5).isolationCut = 999999
getattr(process,"pfIsolatedElectrons"+postfixAK5).isolationCut = 999999

########## insert the PFMET significance calculation #############
from CMGTools.Common.PAT.addMETSignificance_cff import addMETSig
addMETSig( process, postfixAK5 )
####################################################################

########## add specific configuration for pat Jets ##############

getattr(process,"patJets"+postfixAK5).addTagInfos = True
getattr(process,"patJets"+postfixAK5).tagInfoSources  = cms.VInputTag(
    cms.InputTag("secondaryVertexTagInfosAODAK5"),
    cms.InputTag("impactParameterTagInfosAODAK5")
    )
### non default embedding of AOD items for default patJets
getattr(process,"patJets"+postfixAK5).embedCaloTowers = False
getattr(process,"patJets"+postfixAK5).embedPFCandidates = True


##############################################################
#add user variables to PAT-jets 
process.qglAK5PFCHS   = cms.EDProducer(
    "QuarkGluonTagger",
    jets     = cms.InputTag("selectedPatJetsAK5"),
    rho      = cms.InputTag("kt6PFJetsForIso:rho"),
    jec      = cms.string('ak5PFL1FastL2L3'),
    isPatJet = cms.bool(True),
    )

process.customPFJets = cms.EDProducer(
    'PFJetUserData',
    JetInputCollection=cms.untracked.InputTag("selectedPatJetsAK5"),
    is2012Data=cms.untracked.bool(True),
    qgMap=cms.untracked.InputTag("qglAK5PFCHS"),
    Verbosity=cms.untracked.bool(False)
    )

from  CMGTools.External.pujetidsequence_cff import puJetId, puJetMva
process.puJetIdAK5 = puJetId.clone( jets = 'customPFJets')
process.puJetMvaAK5= puJetMva.clone(
    jetids = cms.InputTag("puJetIdAK5"),
    jets = 'customPFJets',
    )

process.puJetIdSequenceAK5 = cms.Sequence(process.puJetIdAK5*process.puJetMvaAK5)

# central jets for filtering and Z->jj candidates
process.customPFJetsCentral = cms.EDFilter(
    "PATJetSelector",
    src = cms.InputTag("customPFJets"),
    cut = cms.string("abs(eta) < 2.4")
    )

############## "Classic" PAT Muons and Electrons ########################
# (made from all reco muons, and all gsf electrons, respectively)
process.patMuons.embedTcMETMuonCorrs = False
process.patMuons.embedCaloMETMuonCorrs = False
process.patMuons.embedTrack = True

process.patElectrons.embedTrack = True
process.patElectrons.pfElectronSource = 'particleFlow'

# use PFIsolation
process.eleIsoSequence = setupPFElectronIso(process, 'gsfElectrons', 'PFIso')
process.muIsoSequence = setupPFMuonIso(process, 'muons', 'PFIso')
adaptPFIsoMuons( process, applyPostfix(process,"patMuons",""), 'PFIso')
adaptPFIsoElectrons( process, applyPostfix(process,"patElectrons",""), 'PFIso')


# setup recommended 0.3 cone for electron PF isolation
process.pfIsolatedElectrons.isolationValueMapsCharged = cms.VInputTag(cms.InputTag("elPFIsoValueCharged03PFIdPFIso"))
process.pfIsolatedElectrons.deltaBetaIsolationValueMap = cms.InputTag("elPFIsoValuePU03PFIdPFIso")
process.pfIsolatedElectrons.isolationValueMapsNeutral = cms.VInputTag(cms.InputTag("elPFIsoValueNeutral03PFIdPFIso"), cms.InputTag("elPFIsoValueGamma03PFIdPFIso"))
process.patElectrons.isolationValues = cms.PSet(
        pfChargedHadrons = cms.InputTag("elPFIsoValueCharged03PFIdPFIso"),
        pfChargedAll = cms.InputTag("elPFIsoValueChargedAll03PFIdPFIso"),
        pfPUChargedHadrons = cms.InputTag("elPFIsoValuePU03PFIdPFIso"),
        pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral03PFIdPFIso"),
        pfPhotons = cms.InputTag("elPFIsoValueGamma03PFIdPFIso")
        )

process.stdMuonSeq = cms.Sequence(
    process.pfParticleSelectionSequence +
    process.muIsoSequence +
    process.makePatMuons +
    process.selectedPatMuons
    )
process.stdElectronSeq = cms.Sequence(
    process.pfParticleSelectionSequence +
    process.eleIsoSequence +
    process.makePatElectrons +
    process.selectedPatElectrons
    )

if not runOnMC:
    process.stdMuonSeq.remove( process.muonMatch )
    process.stdElectronSeq.remove( process.electronMatch )
    process.patMuons.embedGenMatch = False
    process.patElectrons.embedGenMatch = False

# Modules for Electron ID
# MVA Electron ID
process.load("EGamma.EGammaAnalysisTools.electronIdMVAProducer_cfi")
process.mvaeIdSequence = cms.Sequence(
    process.mvaTrigV0 +
    process.mvaNonTrigV0
)
# ElectronID in the VBTF prescription
#import ElectroWeakAnalysis.WENu.simpleCutBasedElectronIDSpring10_cfi as vbtfid
# Switch to the official Electron VBTF Selection for 2011 Data (relax H/E cut in the Endcap):
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/VbtfEleID2011
import HiggsAnalysis.Higgs2l2b.simpleCutBasedElectronIDSummer11_cfi as vbtfid
process.eidVBTFRel95 = vbtfid.simpleCutBasedElectronID.clone( electronQuality = '95relIso' )
process.eidVBTFRel80 = vbtfid.simpleCutBasedElectronID.clone( electronQuality = '80relIso' )
process.eidVBTFCom95 = vbtfid.simpleCutBasedElectronID.clone( electronQuality = '95cIso'   )
process.eidVBTFCom80 = vbtfid.simpleCutBasedElectronID.clone( electronQuality = '80cIso'   )
        
process.vbtfeIdSequence = cms.Sequence(
        process.eidVBTFRel95 +
        process.eidVBTFRel80 +
        process.eidVBTFCom95 +
        process.eidVBTFCom80
)

process.eidSequence = cms.Sequence(
    process.mvaeIdSequence +
    process.vbtfeIdSequence
)

process.patElectrons.electronIDSources = cms.PSet(
        eidVBTFRel95 = cms.InputTag("eidVBTFRel95"),
        eidVBTFRel80 = cms.InputTag("eidVBTFRel80"),
        eidVBTFCom95 = cms.InputTag("eidVBTFCom95"),
        eidVBTFCom80 = cms.InputTag("eidVBTFCom80"),
        #MVA 
        mvaTrigV0 = cms.InputTag("mvaTrigV0"),
        mvaNonTrigV0 = cms.InputTag("mvaNonTrigV0")
)

process.stdLeptonSequence = cms.Sequence(
    process.stdMuonSeq +
    process.eidSequence +
    process.stdElectronSeq 
    )

# Classic Electrons with UserData

process.userDataSelectedElectrons = cms.EDProducer(
    "Higgs2l2bElectronUserData",
    src = cms.InputTag("selectedPatElectrons"),
    rho = cms.InputTag("kt6PFJetsForIso:rho"),
    primaryVertices=cms.InputTag("offlinePrimaryVertices")
)

# ID+Isolated electrons: select electrons passing VETO
process.selectedIsoElectrons = cms.EDFilter(
    "PATElectronSelector",
    src = cms.InputTag("userDataSelectedElectrons"),
    cut = cms.string("(userFloat('cutIDCode') > 0) && (userFloat('passTriggerTight') > 0)")
#    src = cms.InputTag("selectedIDElectrons"),
#    cut = cms.string("electronID('eidVBTFCom95') == 7")
)

# Classic Muons with UserData
process.userDataSelectedMuons = cms.EDProducer(
    "Higgs2l2bMuonUserData",
    src = cms.InputTag("selectedPatMuons"),
    rho = cms.InputTag("kt6PFJetsForIso:rho"),
    primaryVertices=cms.InputTag("offlinePrimaryVertices")
)

# ID-selected muons
process.selectedIDMuons = cms.EDFilter(
    "PATMuonSelector",
    src = cms.InputTag("userDataSelectedMuons"),
    cut = cms.string(
            "isGlobalMuon && isTrackerMuon && isPFMuon && globalTrack().normalizedChi2 < 10 && " +
            "globalTrack().hitPattern().numberOfValidMuonHits > 0 && "              +
            "numberOfMatchedStations > 1 && abs( userFloat('dzVtx') ) < 0.5 && "    +
            "innerTrack().hitPattern().numberOfValidPixelHits > 0 && "              +
            "track().hitPattern().trackerLayersWithMeasurement > 5 && abs(dB) < 0.2" )
)

# Isolated muons: standard isolation
process.selectedIsoMuons = cms.EDFilter(
    "PATMuonSelector",
    src = cms.InputTag("selectedIDMuons"),
#    cut = cms.string("trackIso + caloIso < 0.15 * pt")
# using DeltaBeta correction
    cut = cms.string("( max(0., (neutralHadronIso + photonIso - 0.5*puChargedHadronIso) ) + chargedHadronIso) < 0.12 * pt")
)

process.userDataStandardLeptonSequence = cms.Sequence(
    process.userDataSelectedMuons *
    process.userDataSelectedElectrons *
    process.selectedIDMuons *
#    process.selectedIDElectrons *
    process.selectedIsoMuons *
    process.selectedIsoElectrons 
    )


# Jet cleaning for patJets
process.cleanPatJetsIsoLept = cms.EDProducer(
    "PATJetCleaner",
    src = cms.InputTag("customPFJetsCentral"),
    preselection = cms.string(''),
    checkOverlaps = cms.PSet(
    muons = cms.PSet(
    src = cms.InputTag("selectedIsoMuons"),
    algorithm = cms.string("byDeltaR"),
    preselection = cms.string(""),
    deltaR = cms.double(0.5),
    checkRecoComponents = cms.bool(False),
    pairCut = cms.string(""),
    requireNoOverlaps = cms.bool(True),
    ),
    electrons = cms.PSet(
    src = cms.InputTag("selectedIsoElectrons"),
    algorithm = cms.string("byDeltaR"),
    preselection = cms.string(""),
    deltaR = cms.double(0.5),
    checkRecoComponents = cms.bool(False),
    pairCut = cms.string(""),
    requireNoOverlaps = cms.bool(True),
    )
    ),
    finalCut = cms.string('')
    )


# ---------------- Sequence AK5NoPUSub, pfNoPileUp switched off ---------------

# PFBRECO+PAT sequence 2:
# pfNoPileUp switched off, AK5PFJets. This sequence is a clone of the AK5 sequence defined previously.

if runAK5NoPUSub:
    print 'Preparing AK5NoPUSub sequence...',

    postfixNoPUSub = 'NoPUSub'
    postfixAK5NoPUSub = postfixAK5+postfixNoPUSub

    from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet
    cloneProcessingSnippet(process, getattr(process, 'patPF2PATSequence'+postfixAK5), postfixNoPUSub)

    getattr(process,"pfNoPileUp"+postfixAK5NoPUSub).enable = False
    getattr(process,"patJetCorrFactors"+postfixAK5NoPUSub).payload = "AK5PF"

    getattr(process,"patJets"+postfixAK5NoPUSub).tagInfoSources  = cms.VInputTag(
        cms.InputTag("secondaryVertexTagInfosAODAK5NoPUSub"),
        cms.InputTag("impactParameterTagInfosAODAK5NoPUSub")
        )

    # disable embedding of genjets in PAT jets to avoid duplication of the genjet collection
    if runOnMC:
        process.patJetsAK5.embedGenJetMatch=False
        process.patJetsAK5NoPUSub.embedGenJetMatch=False
        process.patJetGenJetMatchAK5NoPUSub.matched=cms.InputTag("ak5GenJetsNoNu")
        getattr(process,"patDefaultSequence"+postfixAK5NoPUSub).remove(getattr(process,"genForPF2PATSequence"+postfixNoPUSub))
    # disable embedding of PFparticles in PAT jets to avoid duplication of the PFparticles collection
#    process.pfJetsAK5NoPUSub.src=cms.InputTag("particleFlow")
#    process.pfNoJetAK5NoPUSub.bottomCollection=cms.InputTag("particleFlow")
#    process.pfTauPFJets08RegionAK5NoPUSub.pfSrc=cms.InputTag("particleFlow")
#    process.pfTauTagInfoProducerAK5NoPUSub.PFCandidateProducer=cms.InputTag("particleFlow")
#    process.pfTausBaseAK5NoPUSub.builders[0].pfCandSrc=cms.InputTag("particleFlow")
#    process.patJetsAK5.embedPFCandidates=False
#    process.patJetsAK5NoPUSub.embedPFCandidates=False


    # do not rereconstruct standard ak5PFJets if available in PFAOD
#    if not runOnV4:
#    process.PFBRECOAK5NoPUSub.remove(process.pfJetSequenceAK5NoPUSub)
#    process.patJetsAK5NoPUSub.jetSource = cms.InputTag("ak5PFJets")
#    process.patJetCorrFactorsAK5NoPUSub.src = cms.InputTag("ak5PFJets")
#    process.jetTracksAssociatorAtVertexAK5NoPUSub.jets = cms.InputTag("ak5PFJets")
#    process.pfJetsForHPSTauAK5NoPUSub.src = cms.InputTag("ak5PFJets")
#    process.pfMETAK5NoPUSub.jets = cms.InputTag("ak5PFJets")
#    process.softMuonTagInfosAODAK5NoPUSub.jets = cms.InputTag("ak5PFJets")
#    process.PFMETSignificanceAK5NoPUSub.inputPFJets = cms.InputTag("ak5PFJets")
#    if runOnMC:
#        process.patJetGenJetMatchAK5NoPUSub.src = cms.InputTag("ak5PFJets")
#        process.patJetPartonMatchAK5NoPUSub.src = cms.InputTag("ak5PFJets")
#        process.patJetPartonAssociationAK5NoPUSub.jets = cms.InputTag("ak5PFJets")

    print 'Done'

    process.qglAK5PF   = cms.EDProducer(
        "QuarkGluonTagger",
        jets     = cms.InputTag("selectedPatJetsAK5NoPUSub"),
        rho      = cms.InputTag("kt6PFJetsForIso:rho"),
        jec      = cms.string('ak5PFL1FastL2L3'),
        isPatJet = cms.bool(True),
        )

    process.customPFJetsNoPUSub = cms.EDProducer(
        'PFJetUserData',
        JetInputCollection=cms.untracked.InputTag("selectedPatJetsAK5NoPUSub"),
        is2012Data=cms.untracked.bool(True),
        qgMap=cms.untracked.InputTag("qglAK5PF"),
        Verbosity=cms.untracked.bool(False)
        )


    process.puJetIdAK5NoPUSub = puJetId.clone( jets = 'customPFJetsNoPUSub')
    process.puJetMvaAK5NoPUSub= puJetMva.clone(
        jetids = cms.InputTag("puJetIdAK5NoPUSub"),
        jets = 'customPFJetsNoPUSub',
        )

    process.puJetIdSequenceAK5NoPUSub = cms.Sequence(process.puJetIdAK5NoPUSub*process.puJetMvaAK5NoPUSub)

    process.customPFJetsNoPUSubCentral = cms.EDFilter(
        "PATJetSelector",
        src = cms.InputTag("customPFJetsNoPUSub"),
        cut = cms.string("abs(eta) < 2.4")
        )

# Jet cleaning for patJets NoPUSub
    process.cleanPatJetsNoPUIsoLept = cms.EDProducer(
        "PATJetCleaner",
        src = cms.InputTag("customPFJetsNoPUSubCentral"),
        preselection = cms.string(''),
        checkOverlaps = cms.PSet(
        muons = cms.PSet(
        src = cms.InputTag("selectedIsoMuons"),
        algorithm = cms.string("byDeltaR"),
        preselection = cms.string(""),
        deltaR = cms.double(0.5),
        checkRecoComponents = cms.bool(False),
        pairCut = cms.string(""),
        requireNoOverlaps = cms.bool(True),
        ),
        electrons = cms.PSet(
        src = cms.InputTag("selectedIsoElectrons"),
        algorithm = cms.string("byDeltaR"),
        preselection = cms.string(""),
        deltaR = cms.double(0.5),
        checkRecoComponents = cms.bool(False),
        pairCut = cms.string(""),
        requireNoOverlaps = cms.bool(True),
        )
        ),
        finalCut = cms.string('')
        )
    

# ---------------- Common stuff ---------------

### PATH DEFINITION #############################################

# counters that can be used at analysis level to know the processed events
process.prePathCounter = cms.EDProducer("EventCountProducer")
process.postPathCounter = cms.EDProducer("EventCountProducer")

# trigger information (no selection)

process.p = cms.Path( process.prePathCounter )

#process.p += process.kt6PFJets

# PFBRECO+PAT ---

process.p += getattr(process,"patPF2PATSequence"+postfixAK5)

process.p += process.kt6PFJetsCHS
process.p += process.kt6PFJetsForIso
process.p += process.kt6PFJetsCHSForIso

process.p += process.qglAK5PFCHS
process.p += process.customPFJets
process.p += process.puJetIdSequenceAK5
process.p += process.customPFJetsCentral

process.p += process.stdLeptonSequence

#process.p += process.patTriggerSequence

process.p += process.userDataStandardLeptonSequence
process.p += process.cleanPatJetsIsoLept


if runAK5NoPUSub:
    process.p += getattr(process,"patPF2PATSequence"+postfixAK5NoPUSub)
    process.p += process.qglAK5PF 
    process.p += process.customPFJetsNoPUSub
    process.p += process.puJetIdSequenceAK5NoPUSub
    process.p += process.customPFJetsNoPUSubCentral
    process.p += process.cleanPatJetsNoPUIsoLept


# Select leptons
process.selectedPatMuons.cut = (
    "pt > 8.0 && abs(eta) < 2.4"
        )
process.selectedPatElectrons.cut = (
    "pt > 8.0 && abs(eta) < 2.5"
    )
# Select jets
process.selectedPatJetsAK5.cut = cms.string('pt > 15.0')
process.selectedPatJetsAK5NoPUSub.cut = cms.string('pt > 15.0')

################# COMBINATORIAL ANALYSIS ###########################

process.zee = cms.EDProducer("CandViewShallowCloneCombiner",
                                 checkCharge = cms.bool(False),
                                 cut = cms.string('mass > 12 && max(daughter(0).pt, daughter(1).pt) > 17'),
                                 decay = cms.string("userDataSelectedElectrons@+ userDataSelectedElectrons@-")
                             )

process.zmm = cms.EDProducer("CandViewShallowCloneCombiner",
                                 checkCharge = cms.bool(False),
                                 cut = cms.string('mass > 12 && max(daughter(0).pt, daughter(1).pt) > 17'),
                                 decay = cms.string("userDataSelectedMuons@+ userDataSelectedMuons@-")
                             )

process.zem = cms.EDProducer("CandViewShallowCloneCombiner",
                                 checkCharge = cms.bool(False),
                                 cut = cms.string('mass > 12 && max(daughter(0).pt, daughter(1).pt) > 17'),
                                 decay = cms.string("userDataSelectedElectrons@+ userDataSelectedMuons@-")
                             )

process.zjj = cms.EDProducer("CandViewShallowCloneCombiner",
                             checkCharge = cms.bool(False),
                             checkOverlap = cms.bool(False),
                             cut = cms.string(''),
                             decay = cms.string("cleanPatJetsNoPUIsoLept cleanPatJetsNoPUIsoLept")
)

process.hzzeejjBaseColl = cms.EDProducer("CandViewCombiner",
                                             checkCharge = cms.bool(False),
                                             cut = cms.string(''),
                                             decay = cms.string("zee zjj")
                                         )

process.hzzmmjjBaseColl = cms.EDProducer("CandViewCombiner",
                                             checkCharge = cms.bool(False),
                                             cut = cms.string(''),
                                             decay = cms.string("zmm zjj")
                                         )

process.hzzemjjBaseColl = cms.EDProducer("CandViewCombiner",
                                             checkCharge = cms.bool(False),
                                             cut = cms.string(''),
                                             decay = cms.string("zem zjj")
                                         )

process.hzzeejj = cms.EDProducer("Higgs2l2bUserData",
                                     higgs = cms.InputTag("hzzeejjBaseColl"),
                                     gensTag = cms.InputTag("genParticles"),
                                     PFCandidates = cms.InputTag("particleFlow"),
                                     primaryVertices = cms.InputTag("offlinePrimaryVertices"),
                                     dzCut = cms.double(0.1)
                                 )

process.hzzmmjj = cms.EDProducer("Higgs2l2bUserData",
                                     higgs = cms.InputTag("hzzmmjjBaseColl"),
                                     gensTag = cms.InputTag("genParticles"),
                                     PFCandidates = cms.InputTag("particleFlow"),
                                     primaryVertices = cms.InputTag("offlinePrimaryVertices"),
                                     dzCut = cms.double(0.1)
                                     )

process.hzzemjj = cms.EDProducer("Higgs2l2bUserData",
                                     higgs = cms.InputTag("hzzemjjBaseColl"),
                                     gensTag = cms.InputTag("genParticles"),
                                     PFCandidates = cms.InputTag("particleFlow"),
                                     primaryVertices = cms.InputTag("offlinePrimaryVertices"),
                                     dzCut = cms.double(0.1)
                                     )

process.combinatorialSequence = cms.Sequence(
    process.zee +
    process.zmm +
    process.zem +
    process.zjj +
    process.hzzeejjBaseColl +
    process.hzzmmjjBaseColl +
    process.hzzemjjBaseColl +
    process.hzzeejj +
    process.hzzmmjj +
    process.hzzemjj
)

process.p += process.combinatorialSequence

process.p += getattr(process,"postPathCounter") 
 
# Setup for a basic filtering
process.zll = cms.EDProducer("CandViewMerger",
                             src = cms.VInputTag("zee", "zmm", "zem")
)

process.zllFilter = cms.EDFilter("CandViewCountFilter",
                                 src = cms.InputTag("zll"),
                                 minNumber = cms.uint32(1),
)

process.jetFilter = cms.EDFilter("CandViewCountFilter",
                                 src = cms.InputTag("customPFJetsCentral"),
                                 minNumber = cms.uint32(2),
)

process.jetFilterNoPUSub = cms.EDFilter("CandViewCountFilter",
                                 src = cms.InputTag("customPFJetsNoPUSubCentral"),
                                 minNumber = cms.uint32(2),
)

process.filterPath1 = cms.Path(
    process.zll *
    process.zllFilter *
    process.jetFilter
)

process.filterPath2= cms.Path(
    process.zll *
    process.zllFilter *
    process.jetFilterNoPUSub
)


# event cleaning (in tagging mode, no event rejected)
process.load('CMGTools.Common.PAT.addFilterPaths_cff')
### if you have a tag which contains rev >=1.3 of addFilterPaths_cff.py,
### you can use the paths currently commented
process.fullPath = cms.Schedule(
    process.p,
    process.filterPath1,
    process.filterPath2,
    process.EcalDeadCellBoundaryEnergyFilterPath,
    process.simpleDRfilterPath,
############# ->
    process.EcalDeadCellTriggerPrimitiveFilterPath,
    process.greedyMuonPFCandidateFilterPath,
############# <-
    process.hcalLaserEventFilterPath,
    process.inconsistentMuonPFCandidateFilterPath,
    process.trackingFailureFilterPath,
############# ->
    process.CSCTightHaloFilterPath,
############# <-
    process.HBHENoiseFilterPath,
    process.primaryVertexFilterPath,
    process.noscrapingFilterPath
    )

from CMGTools.Common.Tools.cmsswRelease import cmsswIs52X
if cmsswIs52X():
    process.fullPath.append(process.hcalLaserFilterFromAODPath)
else:
    print 'NO hcalLaserFilterFromAOD available for releases < 5.2'
    
#this is needed only for Madgraph MC:
if runOnMC:
    process.fullPath.append(process.totalKinematicsFilterPath)
else:
    del process.totalKinematicsFilterPath

### OUTPUT DEFINITION #############################################

# PFBRECO+PAT ---

# Add PFBRECO output to the created file
#from PhysicsTools.PatAlgos.patEventContent_cff import patEventContentNoCleaning, patTriggerEventContent, patTriggerStandAloneEventContent


process.out = cms.OutputModule("PoolOutputModule",
                 fileName = cms.untracked.string('h2l2qSkimData.root'),
                 SelectEvents = cms.untracked.PSet(
                    SelectEvents = cms.vstring(
                        'filterPath1',
                        'filterPath2')
                 ),
                 outputCommands =  cms.untracked.vstring(
                  'drop *_*_*_*',
                  ),
)

process.out.dropMetaData = cms.untracked.string("DROPPED")

# add trigger information to the pat-tuple
##process.out.outputCommands += patEventContentNoCleaning
#process.out.outputCommands += patTriggerEventContent
#process.out.outputCommands += patTriggerStandAloneEventContent

process.out.outputCommands.extend([
    'keep *_userDataSelectedElectrons_*_PAT',
    'keep *_userDataSelectedMuons_*_PAT',
    'keep *_customPFJets_*_PAT',
    'keep *_customPFJetsNoPUSub_*_PAT',
    'keep *_cleanPatJetsNoPUIsoLept_*_PAT',
    # rho variables
    'keep *_*_rho_PAT',
    'keep *_kt6PFJetsCentralNeutral_rho_*',
    'keep *_kt6PFJets*_rho_*',
    # PU jetID maps
    "keep *_puJetId*_*_*", # input variables
    "keep *_puJetMva*_*_*", # final MVAs and working point flags
    # ll, jj, lljj candidates
    'keep *_zee_*_PAT',
    'keep *_zmm_*_PAT',
    'keep *_zem_*_PAT',
    'keep *_zjj_*_PAT',
    'keep *_hzzeejj_*_PAT',
    'keep *_hzzmmjj_*_PAT',
    'keep *_hzzemjj_*_PAT',
    ####
    'keep *_offlineBeamSpot_*_*',
    'keep *_offlinePrimaryVertices_*_*',
    'keep *_secondaryVertexTagInfos*_*_*',
    'keep *_impactParameterTagInfos*_*_*',
    'keep *_*_*tagInfo*_*',
    # additional collections from AOD   
    'keep *_generalTracks_*_*',
    'keep *_electronGsfTracks_*_*',
    'keep *_muons_*_*',
    'keep *_globalMuons_*_*',
    'keep *_standAloneMuons_*_*',
    'keep recoPFCandidates_particleFlow_*_*',
    # genParticles & genJets
    'keep *_genParticles_*_*',
    'keep recoGenJets_ak5GenJets_*_*',
    'keep recoGenJets_kt6GenJets_*_*',
    # gen Info
    'keep PileupSummaryInfos_*_*_*',
    'keep GenEventInfoProduct_*_*_*',
    'keep GenRunInfoProduct_*_*_*',
    'keep LHEEventProduct_*_*_*',
    'keep *_genEventScale_*_*',
    ###### MET products
    'keep *_patMETs*_*_*',
#    'keep *_patType1CorrectedPFMet_*_*', # NOT included for the moment
    ### for HLT selection
    'keep edmTriggerResults_TriggerResults_*_HLT'])

# additional products for event cleaning
process.out.outputCommands.extend([
    'keep *_TriggerResults_*_PAT',
    ])

process.out.outputCommands.extend(['keep edmMergeableCounter_*_*_*'])

process.outPath = cms.EndPath(process.out)
