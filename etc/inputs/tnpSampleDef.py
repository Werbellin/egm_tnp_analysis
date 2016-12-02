from libPython.tnpClassUtils import tnpSample

cernBox = 'root://eosuser.cern.ch//eos/user/p/ppigard/electron_trees/' 
cernBox = '/Users/pigard/data/eID/'

Moriond17_v1 = {
    #'DY_NLO' : tnpSample('DY_NLO', cernBox + 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_v1_slim.root', 
    #                          isMC = True, nEvts = 33584160 ),
    'DY_madgraph' : tnpSample('DY_madgraph', '/Users/pigard/data/electron_trees/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v2_slim.root', 
                              isMC = True, nEvts = 33584160 ),

    'sum_rerecoBDEFG_promptHv23' : tnpSample('data_v1', '/Users/pigard/data/electron_trees/sum_rerecoBDEFG_promptHv23_slim.root', lumi = 36),
#    'data_Run2016B' : tnpSample('data_Run2016B' , cernBox + 'rereco_RunB_v1_slim.root' , lumi = 5.349 ),
#    'data_Run2016C' : tnpSample('data_Run2016C' , cernBox + '' , lumi = 2.363 ),
#    'data_Run2016D' : tnpSample('data_Run2016D' , cernBox + '' , lumi = 4.256 ),
#    'data_Run2016E' : tnpSample('data_Run2016E' , cernBox + '' , lumi = 3.981 ),
#    'data_Run2016F' : tnpSample('data_Run2016F' , cernBox + '' , lumi = 3.105 ),
#    'data_Run2016G' : tnpSample('data_Run2016G' , cernBox + 'rereco_RunG_v1_slim.root' , lumi = 7.544 ),
#    'data_Run2016H' : tnpSample('data_Run2016H' , cernBox + '' , lumi = 6.105 ),
    }




### qll stat
eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
Moriond17_80X = {
    'DY_madgraph' : tnpSample('DY_madgraph', eosDir1 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_DYToLL_madgraph.root', 
                              isMC = True, nEvts = 33584160 ),
    'data_Run2016B' : tnpSample('data_Run2016B' , eosDir2 + 'data/TnPTree_SingleElectron_2016rereco_RunB.root' , lumi = 5.349 ),
    'data_Run2016C' : tnpSample('data_Run2016C' , eosDir2 + 'data/TnPTree_SingleElectron_2016rereco_RunC.root' , lumi = 2.363 ),
    'data_Run2016D' : tnpSample('data_Run2016D' , eosDir2 + 'data/TnPTree_SingleElectron_2016rereco_RunD.root' , lumi = 4.256 ),
    'data_Run2016E' : tnpSample('data_Run2016E' , eosDir2 + 'data/TnPTree_SingleElectron_2016rereco_RunE.root' , lumi = 3.981 ),
    'data_Run2016F' : tnpSample('data_Run2016F' , eosDir2 + 'data/TnPTree_SingleElectron_2016rereco_RunF.root' , lumi = 3.105 ),
    'data_Run2016G' : tnpSample('data_Run2016G' , eosDir2 + 'data/TnPTree_SingleElectron_2016rereco_RunG.root' , lumi = 7.544 ),
    'data_Run2016H' : tnpSample('data_Run2016H' , eosDir2 + 'data/TnPTree_SingleElectron_2016prompt_RunH.root' , lumi = 6.105 ),
    }

Moriond17_80X_prompt = {
    'DY_madgraph' : tnpSample('DY_madgraph', eosDir1 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_DYToLL_madgraph.root', 
                              isMC = True, nEvts = 33584160 ),
    'data_Run2016B' : tnpSample('data_Run2016B' , eosDir2 + 'data/TnPTree_SingleElectron_2016prompt_RunB.root' , lumi = -1 ),
    'data_Run2016C' : tnpSample('data_Run2016C' , eosDir2 + 'data/TnPTree_SingleElectron_2016prompt_RunC.root' , lumi = -1 ),
    'data_Run2016D' : tnpSample('data_Run2016D' , eosDir2 + 'data/TnPTree_SingleElectron_2016prompt_RunD.root' , lumi = -1 ),
    'data_Run2016F' : tnpSample('data_Run2016F' , eosDir2 + 'data/TnPTree_SingleElectron_2016prompt_RunF.root' , lumi = -1 ),
    'data_Run2016G' : tnpSample('data_Run2016G' , eosDir2 + 'data/TnPTree_SingleElectron_2016prompt_RunG.root' , lumi = -1 ),
    'data_Run2016H' : tnpSample('data_Run2016H' , eosDir2 + 'data/TnPTree_SingleElectron_2016prompt_RunH.root' , lumi = -1 ),
    }



### for this round eleIDs, phoIDs, trigger trees are included in the same file
eosDir = 'eos/cms/store/group/phys_egamma/tnp/80X/76Xids/AllIDs_v0/'
Ichep2016_80X = {
    'DY_amcatnlo' : tnpSample('DY_amcatnlo', eosDir+'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_DYToLL_mcAtNLO.root', isMC = True, nEvts = 28696958 ),
    'DY_madgraph' : tnpSample('DY_madgraph', eosDir+'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root'           , isMC = True, nEvts = 44716638 ),
    'Wjets'       : tnpSample('Wjets'      , eosDir+'mc/TnPTree_WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_WJets_madgraph.root' , isMC = True, nEvts = 28062407 ),
    'ttbar'       : tnpSample('ttbar'      , eosDir+'mc/TnPTree_TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ttbar_madgraph.root'     , isMC = True, nEvts = 10215131 ),
    'data_Run2016B' : tnpSample('data_Run2016B' , eosDir+'data/TnPTree_SingleElectron_Run2016B.root' , lumi = 5.884 ),
    'data_Run2016C' : tnpSample('data_Run2016C' , eosDir+'data/TnPTree_SingleElectron_Run2016C.root' , lumi = 2.646 ),
    'data_Run2016D' : tnpSample('data_Run2016D' , eosDir+'data/TnPTree_SingleElectron_Run2016D.root' , lumi = 4.353 ),
}

eosDir_v0 = 'eos/cms/store/group/phys_egamma/tnp/80X/'
ICHEP2016 = {
    'mc_DY_madgraph_ele' : tnpSample('mc_DY_madgraph_ele', eosDir_v0 + 'Photons_76Xids/elev2/mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root' ,
                                     isMC = True, nEvts = 36311064 ),
    'mc_DY_amcatnlo_ele' : tnpSample('mc_DY_amcatnlo_ele', eosDir_v0 + 'Photons_76Xids/elev2/mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root',
                                     isMC = True, nEvts = 28696958 ),
    'mc_DY_madgraph_pho' : tnpSample('mc_DY_madgraph_pho', eosDir_v0 + 'Photons_76Xids/phov2/mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root' ,
                                     isMC = True, nEvts = 41253879 ),
    'mc_DY_amcatnlo_pho' : tnpSample('mc_DY_amcatnlo_pho', eosDir_v0 + 'Photons_76Xids/phov2/mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root',
                                     isMC = True, nEvts = 28696958 ),
    'mc_Wjets_madgraph_pho' : tnpSample('mc_Wjets_madgraph_pho', eosDir_v0 + 'Photons_76Xids/phov2/mc/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root'        , 
                                        isMC = True, nEvts = 999 ),
    'mc_DY_madgraph_rec' : tnpSample('mc_DY_madgraph_rec', eosDir_v0 + 'RecoSF/RECOv3/mc//TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root'       ,
                                     isMC = True, nEvts = 49877138 ),
    'mc_DY_amcatnlo_rec' : tnpSample('mc_DY_amcatnlo_rec', eosDir_v0 + 'RecoSF/RECOv3/mc//TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root'      , 
                                     isMC = True, nEvts = 28328619 ),
    'data_2016_runB_ele' :  tnpSample('data_2016_runB_ele', eosDir_v0 + 'Photons_76Xids/elev2/data/TnPTree_SingleElectron_2016_RunB.root' , lumi = 5.709 ),
    'data_2016_runC_ele' :  tnpSample('data_2016_runC_ele', eosDir_v0 + 'Photons_76Xids/elev3/data/TnPTree_SingleElectron_2016_RunC.root' , lumi = 2.646 ),
    'data_2016_runD_ele' :  tnpSample('data_2016_runD_ele', eosDir_v0 + 'Photons_76Xids/elev3/data/TnPTree_SingleElectron_2016_RunD.root' , lumi = 4.330 ),
    'data_2016_runB_pho' :  tnpSample('data_2016_runB_pho', eosDir_v0 + 'Photons_76Xids/phov2/data/TnPTree_SingleElectron_2016_RunB.root' , lumi = 5.900 ),
    'data_2016_runC_pho' :  tnpSample('data_2016_runC_pho', eosDir_v0 + 'Photons_76Xids/phov3/data/TnPTree_SingleElectron_2016_RunC.root' , lumi = 2.646 ),
    'data_2016_runD_pho' :  tnpSample('data_2016_runD_pho', eosDir_v0 + 'Photons_76Xids/phov3/data/TnPTree_SingleElectron_2016_RunD.root' , lumi = 4.330 ),
    'data_2016_runB_rec' :  tnpSample('data_2016_runB_rec', eosDir_v0 + 'RecoSF/RECOv3/data//TnPTree_SingleElectron_2016_RunB.root'       , lumi = 5.237 ),
    'data_2016_runC_rec' :  tnpSample('data_2016_runC_rec', eosDir_v0 + 'RecoSF/RECOv4/data//TnPTree_SingleElectron_2016_RunC.root'       , lumi = 2.646 ),
    'data_2016_runD_rec' :  tnpSample('data_2016_runD_rec', eosDir_v0 + 'RecoSF/RECOv5/data//TnPTree_SingleElectron_2016_RunD.root'       , lumi = 4.313 ),
}
