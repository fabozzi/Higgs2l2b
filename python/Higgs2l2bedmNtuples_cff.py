
import FWCore.ParameterSet.Config as cms
import copy

### HIGGS variables


higgs =  cms.EDProducer(
    "CandViewNtpProducer",
    src=cms.InputTag("h2l2b"),
    lazyParser=cms.untracked.bool(True),
    prefix=cms.untracked.string("H"),
    eventInfo=cms.untracked.bool(True),
    variables = cms.VPSet(
    cms.PSet(
    tag = cms.untracked.string("Mass"),
    quantity = cms.untracked.string("mass")
    ),
    cms.PSet(
    tag = cms.untracked.string("Pt"),
    quantity = cms.untracked.string("pt")
    ),
    cms.PSet(
    tag = cms.untracked.string("Eta"),
    quantity = cms.untracked.string("eta")
    ),
    cms.PSet(
    tag = cms.untracked.string("Y"),
    quantity = cms.untracked.string("y")
    ),
    cms.PSet(
    tag = cms.untracked.string("Phi"),
    quantity = cms.untracked.string("phi")
    ),
    cms.PSet(
    tag = cms.untracked.string("En"),
    quantity = cms.untracked.string("energy")
    ),
    cms.PSet(
    tag = cms.untracked.string("jminbmatch"),
    quantity = cms.untracked.string("userFloat('jminbmatch')")
    ),
    cms.PSet(
    tag = cms.untracked.string("jmincmatch"),
    quantity = cms.untracked.string("userFloat('jmincmatch')")
    ),
    cms.PSet(
    tag = cms.untracked.string("jmaxbmatch"),
    quantity = cms.untracked.string("userFloat('jmaxbmatch')")
    ),
    cms.PSet(
    tag = cms.untracked.string("jmaxcmatch"),
    quantity = cms.untracked.string("userFloat('jmaxcmatch')")
    ),
    cms.PSet(
    tag = cms.untracked.string("zzdPhi"),
    quantity = cms.untracked.string("userFloat('zzdPhi')")
    ),
    cms.PSet(
    tag = cms.untracked.string("zzdEta"),
    quantity = cms.untracked.string("userFloat('zzdEta')")
    ),
    cms.PSet(
    tag = cms.untracked.string("zzdr"),
    quantity = cms.untracked.string("userFloat('zzdr')")
    ),
    cms.PSet(
    tag = cms.untracked.string("lldPhi"),
    quantity = cms.untracked.string("userFloat('lldPhi')")
    ),
    cms.PSet(
    tag = cms.untracked.string("lldEta"),
    quantity = cms.untracked.string("userFloat('lldEta')")
    ),
    cms.PSet(
    tag = cms.untracked.string("lldr"),
    quantity = cms.untracked.string("userFloat('lldr')")
    ),
    cms.PSet(
    tag = cms.untracked.string("jjdPhi"),
    quantity = cms.untracked.string("userFloat('jjdPhi')")
    ),
    cms.PSet(
    tag = cms.untracked.string("jjdEta"),
    quantity = cms.untracked.string("userFloat('jjdEta')")
    ),
    cms.PSet(
    tag = cms.untracked.string("jjdr"),
    quantity = cms.untracked.string("userFloat('jjdr')")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau1LooseID"),
    quantity = cms.untracked.string("userFloat('jet1LooseID')")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau2LooseID"),
    quantity = cms.untracked.string("userFloat('jet2LooseID')")
    ),
    cms.PSet(
    tag = cms.untracked.string("costhetaNT1"),
    quantity = cms.untracked.string("userFloat('costhetaNT1')")
    ),
    cms.PSet(
    tag = cms.untracked.string("costhetaNT2"),
    quantity = cms.untracked.string("userFloat('costhetaNT2')")
    ),
    cms.PSet(
    tag = cms.untracked.string("phiNT"),
    quantity = cms.untracked.string("userFloat('phiNT')")
    ),
    cms.PSet(
    tag = cms.untracked.string("phiNT1"),
    quantity = cms.untracked.string("userFloat('phiNT1')")
    ),
    cms.PSet(
    tag = cms.untracked.string("costhetastarNT"),
    quantity = cms.untracked.string("userFloat('costhetastarNT')")
    ),
    cms.PSet(
    tag = cms.untracked.string("costhetaNT1Refit"),
    quantity = cms.untracked.string("userFloat('costhetaNT1Refit')")
    ),
    cms.PSet(
    tag = cms.untracked.string("costhetaNT2Refit"),
    quantity = cms.untracked.string("userFloat('costhetaNT2Refit')")
    ),
    cms.PSet(
    tag = cms.untracked.string("phiNTRefit"),
    quantity = cms.untracked.string("userFloat('phiNTRefit')")
    ),
    cms.PSet(
    tag = cms.untracked.string("phiNT1Refit"),
    quantity = cms.untracked.string("userFloat('phiNT1Refit')")
    ),
    cms.PSet(
    tag = cms.untracked.string("costhetastarNTRefit"),
    quantity = cms.untracked.string("userFloat('costhetastarNTRefit')")
    ),
    cms.PSet(
    tag = cms.untracked.string("RefitMass"),
    quantity = cms.untracked.string("userFloat('HZZRefitMass')")
    ),
    cms.PSet(
    tag = cms.untracked.string("zjjRefitMass"),
    quantity = cms.untracked.string("userFloat('ZjjRefitMass')")
    ),
    cms.PSet(
    tag = cms.untracked.string("RefitChi2"),
    quantity = cms.untracked.string("userFloat('KFchiSquare')")
    ),
    cms.PSet(
    tag = cms.untracked.string("RefitChi2Prob"),
    quantity = cms.untracked.string("userFloat('KFchiSquareProb')")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau1RefitPt"),
    quantity = cms.untracked.string("userFloat('j1RefitPt')")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau2RefitPt"),
    quantity = cms.untracked.string("userFloat('j2RefitPt')")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau1RefitEta"),
    quantity = cms.untracked.string("userFloat('j1RefitEta')")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau2RefitEta"),
    quantity = cms.untracked.string("userFloat('j2RefitEta')")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau1RefitPhi"),
    quantity = cms.untracked.string("userFloat('j1RefitPhi')")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau2RefitPhi"),
    quantity = cms.untracked.string("userFloat('j2RefitPhi')")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau1RefitE"),
    quantity = cms.untracked.string("userFloat('j1RefitE')")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau2RefitE"),
    quantity = cms.untracked.string("userFloat('j2RefitE')")
    ),
    cms.PSet(
    tag = cms.untracked.string("HelyLD"),
    quantity = cms.untracked.string("userFloat('helyLD')")
    ),
    cms.PSet(
    tag = cms.untracked.string("ldSig"),
    quantity = cms.untracked.string("userFloat('ldSig')")
    ),
    cms.PSet(
    tag = cms.untracked.string("ldBkg"),
    quantity = cms.untracked.string("userFloat('ldBkg')")
    ),
    cms.PSet(
    tag = cms.untracked.string("HelyLDRefit"),
    quantity = cms.untracked.string("userFloat('helyLDRefit')")
    ),
    cms.PSet(
    tag = cms.untracked.string("ldSigRefit"),
    quantity = cms.untracked.string("userFloat('ldSigRefit')")
    ),
    cms.PSet(
    tag = cms.untracked.string("ldBkgRefit"),
    quantity = cms.untracked.string("userFloat('ldBkgRefit')")
    ),
# new met variables
    cms.PSet(
    tag = cms.untracked.string("trkMetX"),
    quantity = cms.untracked.string("userFloat('trkMetX')")
    ),
    cms.PSet(
    tag = cms.untracked.string("trkMetY"),
    quantity = cms.untracked.string("userFloat('trkMetY')")
    ),
    cms.PSet(
    tag = cms.untracked.string("trkCorrectedMetX"),
    quantity = cms.untracked.string("userFloat('trkCorrectedMetX')")
    ),
    cms.PSet(
    tag = cms.untracked.string("trkCorrectedMetY"),
    quantity = cms.untracked.string("userFloat('trkCorrectedMetY')")
    ),
    cms.PSet(
    tag = cms.untracked.string("trkMet"),
    quantity = cms.untracked.string("userFloat('trkMet')")
    ),
    cms.PSet(
    tag = cms.untracked.string("trkPlusNeuMet"),
    quantity = cms.untracked.string("userFloat('trkPlusNeuMet')")
    ),
    )
    )

### Zll variables

zll = (

    cms.PSet(
    tag = cms.untracked.string("zllMass"),
    quantity = cms.untracked.string("daughter(0).mass")
    ),
    cms.PSet(
    tag = cms.untracked.string("zllPt"),
    quantity = cms.untracked.string("daughter(0).pt")
    ),
    cms.PSet(
    tag = cms.untracked.string("zllEta"),
    quantity = cms.untracked.string("daughter(0).eta")
    ),
    cms.PSet(
    tag = cms.untracked.string("zllY"),
    quantity = cms.untracked.string("daughter(0).y")
    ),
    cms.PSet(
    tag = cms.untracked.string("zllPhi"),
    quantity = cms.untracked.string("daughter(0).phi")
    ),
    cms.PSet(
    tag = cms.untracked.string("zllEn"),
    quantity = cms.untracked.string("daughter(0).energy")
    ),
    cms.PSet(
    tag = cms.untracked.string("zllCharge"),
    quantity = cms.untracked.string("daughter(0).charge")
    ),
    ## pt
    cms.PSet(
    tag = cms.untracked.string("LeptDau1Charge"),
    quantity = cms.untracked.string("daughter(0).daughter(0).charge ")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2Charge"),
    quantity = cms.untracked.string("daughter(0).daughter(1).charge")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1Pt"),
    quantity = cms.untracked.string("daughter(0).daughter(0).pt ")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2Pt"),
    quantity = cms.untracked.string("daughter(0).daughter(1).pt")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1Px"),
    quantity = cms.untracked.string("daughter(0).daughter(0).px ")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2Px"),
    quantity = cms.untracked.string("daughter(0).daughter(1).px")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1Py"),
    quantity = cms.untracked.string("daughter(0).daughter(0).py ")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2Py"),
    quantity = cms.untracked.string("daughter(0).daughter(1).py")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1Pz"),
    quantity = cms.untracked.string("daughter(0).daughter(0).pz ")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2Pz"),
    quantity = cms.untracked.string("daughter(0).daughter(1).pz")
    ),
## eta
    cms.PSet(
    tag = cms.untracked.string("LeptDau1Eta"),
    quantity = cms.untracked.string("daughter(0).daughter(0).eta ")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2Eta"),
    quantity = cms.untracked.string("daughter(0).daughter(1).eta ")
    ),
    ## phi
    cms.PSet(
    tag = cms.untracked.string("LeptDau1Phi"),
    quantity = cms.untracked.string("daughter(0).daughter(0).phi ")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2Phi"),
    quantity = cms.untracked.string("daughter(0).daughter(1).phi ")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1En"),
    quantity = cms.untracked.string("daughter(0).daughter(0).energy ")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2En"),
    quantity = cms.untracked.string("daughter(0).daughter(1).energy ")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1GlobalMuonBit"),
    quantity = cms.untracked.string("daughter(0).daughter(0).isGlobalMuon")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2GlobalMuonBit"),
    quantity = cms.untracked.string("daughter(0).daughter(1).isGlobalMuon")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1StandAloneBit"),
    quantity = cms.untracked.string("daughter(0).daughter(0).isStandAloneMuon")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2StandAloneBit"),
    quantity = cms.untracked.string("daughter(0).daughter(1).isStandAloneMuon")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1TrackerMuonBit"),
    quantity = cms.untracked.string("daughter(0).daughter(0).isTrackerMuon")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2TrackerMuonBit"),
    quantity = cms.untracked.string("daughter(0).daughter(1).isTrackerMuon")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1NofMuonHits"),
    quantity = cms.untracked.string("?daughter(0).daughter(0).isGlobalMuon?daughter(0).daughter(0).masterClone.globalTrack.hitPattern.numberOfValidMuonHits: -1")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2NofMuonHits"),
    quantity = cms.untracked.string("?daughter(0).daughter(1).isGlobalMuon?daughter(0).daughter(1).masterClone.globalTrack.hitPattern.numberOfValidMuonHits: -1")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1NofStripHits"),
    quantity = cms.untracked.string("?daughter(0).daughter(0).isGlobalMuon?daughter(0).daughter(0).masterClone.globalTrack.hitPattern.numberOfValidStripHits: -1")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2NofStripHits"),
    quantity = cms.untracked.string("?daughter(0).daughter(1).isGlobalMuon?daughter(0).daughter(1).masterClone.globalTrack.hitPattern.numberOfValidStripHits: -1")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1NofPixelHits"),
    quantity = cms.untracked.string("?daughter(0).daughter(0).isGlobalMuon?daughter(0).daughter(0).masterClone.globalTrack.hitPattern.numberOfValidPixelHits: -1")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2NofPixelHits"),
    quantity = cms.untracked.string("?daughter(0).daughter(1).isGlobalMuon?daughter(0).daughter(1).masterClone.globalTrack.hitPattern.numberOfValidPixelHits: -1")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1NormChi2"),
    quantity = cms.untracked.string("?daughter(0).daughter(0).isGlobalMuon?daughter(0).daughter(0).masterClone.globalTrack.normalizedChi2: -1")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2NormChi2"),
    quantity = cms.untracked.string("?daughter(0).daughter(1).isGlobalMuon?daughter(0).daughter(1).masterClone.globalTrack.normalizedChi2: -1")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1NofChambers"),
    quantity = cms.untracked.string("?daughter(0).daughter(0).isGlobalMuon?daughter(0).daughter(0).masterClone.numberOfChambers: -1")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2NofChambers"),
    quantity = cms.untracked.string("?daughter(0).daughter(1).isGlobalMuon?daughter(0).daughter(1).masterClone.numberOfChambers: -1")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1dB"),
    quantity = cms.untracked.string("daughter(0).daughter(0).masterClone.dB")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2dB"),
    quantity = cms.untracked.string("daughter(0).daughter(1).masterClone.dB")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1TrkIso"),
    quantity = cms.untracked.string("daughter(0).daughter(0).masterClone.trackIso")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2TrkIso"),
    quantity = cms.untracked.string("daughter(0).daughter(1).masterClone.trackIso")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1EcalIso"),
    quantity = cms.untracked.string("daughter(0).daughter(0).masterClone.ecalIso")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2EcalIso"),
    quantity = cms.untracked.string("daughter(0).daughter(1).masterClone.ecalIso")
    ),
      cms.PSet(
    tag = cms.untracked.string("LeptDau1HcalIso"),
    quantity = cms.untracked.string("daughter(0).daughter(0).masterClone.hcalIso")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2HcalIso"),
    quantity = cms.untracked.string("daughter(0).daughter(1).masterClone.hcalIso")
    ),
     cms.PSet(
    tag = cms.untracked.string("LeptDau1CombRelIso"),
    quantity = cms.untracked.string("(daughter(0).daughter(0).masterClone.hcalIso + daughter(0).daughter(0).masterClone.ecalIso + daughter(0).daughter(0).masterClone.trackIso )/ daughter(0).daughter(0).pt")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2CombRelIso"),
    quantity = cms.untracked.string("(daughter(0).daughter(1).masterClone.hcalIso + daughter(0).daughter(1).masterClone.ecalIso + daughter(0).daughter(1).masterClone.trackIso )/ daughter(0).daughter(1).pt")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1AbsCombIsoPUCorr"),
    quantity = cms.untracked.string("daughter(0).daughter(0).masterClone.userFloat('absCombIsoPUCorrected')")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2AbsCombIsoPUCorr"),
    quantity = cms.untracked.string("daughter(0).daughter(1).masterClone.userFloat('absCombIsoPUCorrected')")
    ),

    )

zee =(

    cms.PSet(
    tag = cms.untracked.string("EleDau1VBTF80CombID"),
    quantity = cms.untracked.string("daughter(0).daughter(0).masterClone.electronID(\"eidVBTFCom80\")")
    ),
    cms.PSet(
    tag = cms.untracked.string("EleDau2VBTF80CombID"),
    quantity = cms.untracked.string("daughter(0).daughter(1).masterClone.electronID(\"eidVBTFCom80\")")
    ),
    cms.PSet(
    tag = cms.untracked.string("EleDau1VBTF95CombID"),
    quantity = cms.untracked.string("daughter(0).daughter(0).masterClone.electronID(\"eidVBTFCom95\")")
    ),
    cms.PSet(
    tag = cms.untracked.string("EleDau2VBTF95CombID"),
    quantity = cms.untracked.string("daughter(0).daughter(1).masterClone.electronID(\"eidVBTFCom95\")")
    ),
###### variables useful for custom electron selection
    cms.PSet(
    tag = cms.untracked.string("LeptDau1isEB"),
    quantity = cms.untracked.string("daughter(0).daughter(0).masterClone.isEB")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2isEB"),
    quantity = cms.untracked.string("daughter(0).daughter(1).masterClone.isEB")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1isEE"),
    quantity = cms.untracked.string("daughter(0).daughter(0).masterClone.isEE")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2isEE"),
    quantity = cms.untracked.string("daughter(0).daughter(1).masterClone.isEE")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1DeltaPhiAtVtx"),
    quantity = cms.untracked.string("daughter(0).daughter(0).masterClone.deltaPhiSuperClusterTrackAtVtx")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2DeltaPhiAtVtx"),
    quantity = cms.untracked.string("daughter(0).daughter(1).masterClone.deltaPhiSuperClusterTrackAtVtx")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau1HOverE"),
    quantity = cms.untracked.string("daughter(0).daughter(0).masterClone.hcalOverEcal")
    ),
    cms.PSet(
    tag = cms.untracked.string("LeptDau2HOverE"),
    quantity = cms.untracked.string("daughter(0).daughter(1).masterClone.hcalOverEcal")
    )    
    )

zem =(

    cms.PSet(
    tag = cms.untracked.string("EleDau1VBTF80CombID"),
    quantity = cms.untracked.string("daughter(0).daughter(0).masterClone.electronID(\"eidVBTFCom80\")")
    ),
    cms.PSet(
    tag = cms.untracked.string("EleDau2VBTF80CombID"),
    quantity = cms.untracked.string("-1")
    ),    
    cms.PSet(
    tag = cms.untracked.string("EleDau1VBTF95CombID"),
    quantity = cms.untracked.string("daughter(0).daughter(0).masterClone.electronID(\"eidVBTFCom95\")")
    ),
    cms.PSet(
    tag = cms.untracked.string("EleDau2VBTF95CombID"),
    quantity = cms.untracked.string("-1")
    ),    
    )

###  zjj standard and bDiscriminator variables

zjj = (
    
    cms.PSet(
    tag = cms.untracked.string("zjjMass"),
    quantity = cms.untracked.string("daughter(1).mass")
    ),
    cms.PSet(
    tag = cms.untracked.string("zjjPt"),
    quantity = cms.untracked.string("daughter(1).pt")
    ),
    cms.PSet(
    tag = cms.untracked.string("zjjEta"),
    quantity = cms.untracked.string("daughter(1).eta")
    ),
    cms.PSet(
    tag = cms.untracked.string("zjjY"),
    quantity = cms.untracked.string("daughter(1).y")
    ),
    cms.PSet(
    tag = cms.untracked.string("zjjPhi"),
    quantity = cms.untracked.string("daughter(1).phi")
    ),
    cms.PSet(
    tag = cms.untracked.string("zjjEn"),
    quantity = cms.untracked.string("daughter(1).energy")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau1Pt"),
    quantity = cms.untracked.string("daughter(1).daughter(0).pt ")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau2Pt"),
    quantity = cms.untracked.string("daughter(1).daughter(1).pt")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau1Px"),
    quantity = cms.untracked.string("daughter(1).daughter(0).px ")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau2Px"),
    quantity = cms.untracked.string("daughter(1).daughter(1).px")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau1Py"),
    quantity = cms.untracked.string("daughter(1).daughter(0).py ")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau2Py"),
    quantity = cms.untracked.string("daughter(1).daughter(1).py")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau1Pz"),
    quantity = cms.untracked.string("daughter(1).daughter(0).pz ")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau2Pz"),
    quantity = cms.untracked.string("daughter(1).daughter(1).pz")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau1Eta"),
    quantity = cms.untracked.string("daughter(1).daughter(0).eta ")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau2Eta"),
    quantity = cms.untracked.string("daughter(1).daughter(1).eta ")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau1Phi"),
    quantity = cms.untracked.string("daughter(1).daughter(0).phi ")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau2Phi"),
    quantity = cms.untracked.string("daughter(1).daughter(1).phi ")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau1En"),
    quantity = cms.untracked.string("daughter(1).daughter(0).energy ")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau2En"),
    quantity = cms.untracked.string("daughter(1).daughter(1).energy ")
    ),
    ### MC parton flavour ###
    cms.PSet(
    tag = cms.untracked.string("JetDau1PartonFlavour"),
    quantity = cms.untracked.string("daughter(1).daughter(0).masterClone.partonFlavour")
    ),
    cms.PSet(
    tag = cms.untracked.string("JetDau2PartonFlavour"),
    quantity = cms.untracked.string("daughter(1).daughter(1).masterClone.partonFlavour")
    ),

    ### b tagging ###

    cms.PSet(
    tag = cms.untracked.string("Jet1CSV"),
    quantity = cms.untracked.string("daughter(1).daughter(0).masterClone.bDiscriminator(\"combinedSecondaryVertexBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet2CSV"),
    quantity = cms.untracked.string("daughter(1).daughter(1).masterClone.bDiscriminator(\"combinedSecondaryVertexBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet1CSVMVA"),
    quantity = cms.untracked.string("daughter(1).daughter(0).masterClone.bDiscriminator(\"combinedSecondaryVertexMVABJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet2CSVMVA"),
    quantity = cms.untracked.string("daughter(1).daughter(1).masterClone.bDiscriminator(\"combinedSecondaryVertexMVABJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet1JProb"),
    quantity = cms.untracked.string("daughter(1).daughter(0).masterClone.bDiscriminator(\"jetProbabilityBJetTags\")")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet2JProb"),
    quantity = cms.untracked.string(" daughter(1).daughter(1).masterClone.bDiscriminator(\"jetProbabilityBJetTags\")")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet1JbProb"),
    quantity = cms.untracked.string(" daughter(1).daughter(0).masterClone.bDiscriminator(\"jetBProbabilityBJetTags\")")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet2JbProb"),
    quantity = cms.untracked.string(" daughter(1).daughter(1).masterClone.bDiscriminator(\"jetBProbabilityBJetTags\")")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet1SSVHE"),
    quantity = cms.untracked.string("daughter(1).daughter(0).masterClone.bDiscriminator(\"simpleSecondaryVertexHighEffBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet2SSVHE"),
    quantity = cms.untracked.string("daughter(1).daughter(1).masterClone.bDiscriminator(\"simpleSecondaryVertexHighEffBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet1SSVHP"),
    quantity = cms.untracked.string(" daughter(1).daughter(0).masterClone.bDiscriminator(\"simpleSecondaryVertexHighPurBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet2SSVHP"),
    quantity = cms.untracked.string("daughter(1).daughter(1).masterClone.bDiscriminator(\"simpleSecondaryVertexHighPurBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet1ElPt"),
    quantity = cms.untracked.string("daughter(1).daughter(0).masterClone.bDiscriminator(\"softElectronByPtBJetTags\")")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet2ElPt"),
    quantity = cms.untracked.string("daughter(1).daughter(1).masterClone.bDiscriminator(\"softElectronByPtBJetTags\") ")
    ),
        cms.PSet(
    tag = cms.untracked.string("Jet1ElIp"),
    quantity = cms.untracked.string("daughter(1).daughter(0).masterClone.bDiscriminator(\"softElectronByIP3dBJetTags\")")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet2ElIp"),
    quantity = cms.untracked.string("daughter(1).daughter(1).masterClone.bDiscriminator(\"softElectronByIP3dBJetTags\") ")
    ),
        cms.PSet(
    tag = cms.untracked.string("Jet1Mu"),
    quantity = cms.untracked.string("daughter(1).daughter(0).masterClone.bDiscriminator(\"softMuonBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet2Mu"),
    quantity = cms.untracked.string("daughter(1).daughter(1).masterClone.bDiscriminator(\"softMuonBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet1MuPt"),
    quantity = cms.untracked.string("daughter(1).daughter(0).masterClone.bDiscriminator(\"softMuonByPtBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet2MuPt"),
    quantity = cms.untracked.string("daughter(1).daughter(1).masterClone.bDiscriminator(\"softMuonByPtBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet1MuIp"),
    quantity = cms.untracked.string("daughter(1).daughter(0).masterClone.bDiscriminator(\"softMuonByIP3dBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet2MuIp"),
    quantity = cms.untracked.string("daughter(1).daughter(1).masterClone.bDiscriminator(\"softMuonByIP3dBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet1TKHE"),
    quantity = cms.untracked.string("daughter(1).daughter(0).masterClone.bDiscriminator(\"trackCountingHighEffBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet2TKHE"),
    quantity = cms.untracked.string("daughter(1).daughter(1).masterClone.bDiscriminator(\"trackCountingHighEffBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet1TKHP"),
    quantity = cms.untracked.string("daughter(1).daughter(0).masterClone.bDiscriminator(\"trackCountingHighPurBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("Jet2TKHP"),
    quantity = cms.untracked.string("daughter(1).daughter(1).masterClone.bDiscriminator(\"trackCountingHighPurBJetTags\") ")
    ),
    )


## zll.variables += baseKinematics


Higgs2mu2bEdmNtuple = copy.deepcopy(higgs)
Higgs2mu2bEdmNtuple.variables += zll
Higgs2mu2bEdmNtuple.variables += zjj
Higgs2mu2bEdmNtuple.src = cms.InputTag("hzzmmjj:h")
Higgs2mu2bEdmNtuple.prefix = cms.untracked.string("muHiggs")


Higgs2e2bEdmNtuple = copy.deepcopy(Higgs2mu2bEdmNtuple)
Higgs2e2bEdmNtuple.variables += zee
Higgs2e2bEdmNtuple.src = cms.InputTag("hzzeejj:h")
Higgs2e2bEdmNtuple.prefix = cms.untracked.string("elHiggs")

Higgsemu2bEdmNtuple = copy.deepcopy(Higgs2mu2bEdmNtuple)
Higgsemu2bEdmNtuple.variables += zem
Higgsemu2bEdmNtuple.src = cms.InputTag("hzzemjj:h")
Higgsemu2bEdmNtuple.prefix = cms.untracked.string("elmuHiggs")


## jet variables 
jetinfos =  cms.EDProducer(
    "CandViewNtpProducer",
    src=cms.InputTag("cleanPatJetsIsoLept"),
    lazyParser=cms.untracked.bool(True),
    prefix=cms.untracked.string("CleanJet"),
    eventInfo=cms.untracked.bool(True),
    variables = cms.VPSet(
    cms.PSet(
    tag = cms.untracked.string("Pt"),
    quantity = cms.untracked.string("pt")
    ),
    cms.PSet(
    tag = cms.untracked.string("Eta"),
    quantity = cms.untracked.string("eta")
    ),
    cms.PSet(
    tag = cms.untracked.string("Phi"),
    quantity = cms.untracked.string("phi")
    ),
    cms.PSet(
    tag = cms.untracked.string("En"),
    quantity = cms.untracked.string("energy")
    ),
    cms.PSet(
    tag = cms.untracked.string("PartonFlavour"),
    quantity = cms.untracked.string("partonFlavour")
    ),
    cms.PSet(
    tag = cms.untracked.string("CSVtag"),
    quantity = cms.untracked.string("bDiscriminator(\"combinedSecondaryVertexBJetTags\") ")
    ),
    cms.PSet(
    tag = cms.untracked.string("JPtag"),
    quantity = cms.untracked.string("bDiscriminator(\"jetProbabilityBJetTags\")")
    ),
)
)


eventVtxInfoNtuple = cms.EDProducer(
    "EventVtxInfoNtupleDumper",
    primaryVertices=cms.InputTag("offlinePrimaryVertices")
)


edmNtuplesOut = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('Higgs2l2bEdmNtuples.root'),
    outputCommands = cms.untracked.vstring(
    "drop *",
    "keep *_eventVtxInfoNtuple_*_*",
    "keep *_metInfoProducer_*_*",
    "keep *_kt6PFJets_rho_PAT",
    "keep *_Higgs2e2bEdmNtuple_*_*",
    "keep *_Higgs2mu2bEdmNtuple_*_*",
    "keep *_Higgsemu2bEdmNtuple_*_*"
    
    )
    )
