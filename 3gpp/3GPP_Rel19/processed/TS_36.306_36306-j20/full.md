3GPP TS 36.306 V19.2.0 (2026-03)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

Evolved Universal Terrestrial Radio Access (E-UTRA);
User Equipment (UE) radio access capabilities

(Release 19)



![](media/image1.emf) ![](media/image2.emf)

The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP.
The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented.
This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification.
Specifications and reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices.


Keywords

LTE, E-UTRAN, radio

3GPP

Postal address

3GPP support office address

## 650 Route des Lucioles – Sophia Antipolis

Valbonne – France

Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16

Internet

http://www.3gpp.org

Copyright Notification

No part may be reproduced except as authorized by written permission.
The copyright and the foregoing restriction extend to reproduction in all media.

© 2026, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

Bluetooth® is a Trade Mark of the Bluetooth SIG registered for the benefit of its members


Contents

Foreword 21

1 Scope 22

2 References 22

3 Definitions, symbols and abbreviations 24

3.1 Definitions 24

3.2 Symbols 24

3.3 Abbreviations 24

4 UE radio access capability parameters 26

4.1 ue-Category 30

4.1A ue-CategoryDL and ue-CategoryUL 33

4.1B ue-CategorySL-C-RX, ue-CategorySL-C-TX and ue-CategorySL-D 54

4.1C ue-Category-NB 55

4.2 Parameters set by the field ue-Category and ue-CategoryDL / ue-CategoryUL 56

4.2.1 Transport channel parameters in downlink 56

4.2.1.1 Maximum number of DL-SCH transport block bits received within a TTI 56

4.2.1.2 Maximum number of bits of a DL-SCH transport block received within a TTI 57

4.2.1.3 Total number of DL-SCH soft channel bits 57

4.2.1.4 Maximum number of bits of a MCH transport block received within a TTI 57

4.2.2 Transport channel parameters in uplink 57

4.2.2.1 Maximum number of bits of an UL-SCH transport block transmitted within a TTI 57

4.2.2.2 Maximum number of UL-SCH transport block bits transmitted within a TTI 57

4.2.3 Physical channel parameters in downlink (DL) 57

4.2.3.1 Maximum number of supported layers for spatial multiplexing in DL 57

4.2.4 Physical channel parameters in uplink (UL) 57

4.2.4.1 Support for 64QAM in UL 57

4.2.5 Total layer 2 buffer size 57

4.2.6 Half-duplex FDD operation type 58

4.2.7 RF parameters 58

4.2.7.1 Maximum UE channel bandwidth 58

4.2A Parameters set by ue-CategorySL-C / ue-CategorySL-D 58

4.2A.1 Transport channel parameters in sidelink (SL) 58

4.2A.1.1 Maximum number of SL-SCH transport block bits received within a TTI 58

4.2A.1.2 Maximum number of bits of a SL-SCH transport block received within a TTI 58

4.2A.1.3 Maximum number of SL-DCH transport block bits received within a TTI 58

4.2A.1.4 Maximum number of bits of a SL-DCH transport block received within a TTI 58

4.2A.1.5 Maximum number of bits of a SL-SCH transport block transmitted within a TTI 58

4.2A.1.6 Maximum number of SL-SCH transport block bits transmitted within a TTI 58

4.2A.1.7 Maximum number of bits of a SL-DCH transport block transmitted within a TTI 58

4.2A.1.8 Maximum number of SL-DCH transport block bits transmitted within a TTI 59

4.2A.2 Physical channel parameters in sidelink (SL) 59

4.2A.2.1 Maximum number of supported layers for spatial multiplexing in SL-C 59

4.2A.2.2 Maximum number of supported layers for spatial multiplexing in SL-D 59

4.3 Parameters independent of the field ue-Category and ue-CategoryDL / ue-CategoryUL 59

4.3.1 PDCP Parameters 59

4.3.1.1 supportedROHC-Profiles 59

4.3.1.1A supportedROHC-Profiles-r13 59

4.3.1.2 maxNumberROHC-ContextSessions 60

4.3.1.2A maxNumberROHC-ContextSessions-r13 60

4.3.1.3 pdcp-SN-Extension 60

4.3.1.4 supportRohcContextContinue 60

4.3.1.5 pdcp-SN-Extension-18bits-r13 60

4.3.1.6 supportedUplinkOnlyROHC-Profiles 60

4.3.1.7 supportedUDC-r15 60

4.3.1.8 supportedStandardDic-r15 60

4.3.1.9 supportedOperatorDic-r15 61

4.3.1.10 pdcp-Duplication-r15 61

4.3.1.11 pdcp-VersionChangeWithoutHO-r16 61

4.3.1.12 ehc-r16 61

4.3.1.13 maxNumberEHC-Contexts-r16 61

4.3.1.14 continueEHC-Context-r16 61

4.3.1.15 jointEHC-ROHC-Config-r16 61

4.3.1A NR PDCP Parameters 61

4.3.2 RLC parameters 62

4.3.2.1 Void 62

4.3.2.2 extended-RLC-LI-Field-r12 62

4.3.2.3 extendedRLC-SN-SO-Field-r13 62

4.3.2.4 extendedPollByte-r14 62

4.3.2.5 rlc-UM-r15 62

4.3.2.6 rlc-AM-Ooo-Delivery-r15 62

4.3.2.7 rlc-UM-Ooo-Delivery-r15 62

4.3.2.8 flexibleUM-AM-Combinations-r15 62

4.3.3 Void 62

4.3.4 Physical layer parameters 62

4.3.4.1 ue-TxAntennaSelectionSupported 62

4.3.4.2 ue-SpecificRefSigsSupported 62

4.3.4.3 Void 62

4.3.4.4 enhancedDualLayerFDD 62

4.3.4.5 enhancedDualLayerTDD 63

4.3.4.6 supportedMIMO-CapabilityUL-r10 63

4.3.4.7 supportedMIMO-CapabilityDL-r10 63

4.3.4.8 two-AntennaPortsForPUCCH-r10 63

4.3.4.9 tm9-With-8Tx-FDD-r10 63

4.3.4.10 pmi-Disabling-r10 63

4.3.4.11 crossCarrierScheduling-r10 63

4.3.4.12 simultaneousPUCCH-PUSCH-r10 63

4.3.4.13 multiClusterPUSCH-WithinCC-r10 64

4.3.4.14 nonContiguousUL-RA-WithinCC-Info-r10 64

4.3.4.15 crs-InterfHandl-r11 64

4.3.4.16 Void 64

4.3.4.17 Void 64

4.3.4.18 ePDCCH-r11 64

4.3.4.19 multiACK-CSI-Reporting-r11 64

4.3.4.20 ss-CCH-InterfHandl-r11 64

4.3.4.21 tdd-SpecialSubframe-r11 64

4.3.4.21A tdd-SpecialSubframe-r14 64

4.3.4.21B ssp10-TDD-Only-r14 64

4.3.4.22 txDiv-PUCCH1b-ChSelect-r11 65

4.3.4.23 ul-CoMP-r11 65

4.3.4.24 tm5-FDD 65

4.3.4.25 tm5-TDD 65

4.3.4.26 interBandTDD-CA-WithDifferentConfig-r11 65

4.3.4.27 e-HARQ-Pattern-FDD-r12 65

4.3.4.28 tdd-FDD-CA-PCellDuplex-r12 65

4.3.4.29 csi-SubframeSet-r12 65

4.3.4.30 phy-TDD-ReConfig-FDD-PCell-r12 65

4.3.4.31 phy-TDD-ReConfig-TDD-PCell-r12 65

4.3.4.32 pusch-SRS-PowerControl-SubframeSet-r12 66

4.3.4.33 enhanced-4TxCodebook-r12 66

4.3.4.34 pusch-FeedbackMode-r12 66

4.3.4.35 naics-Capability-List-r12 66

4.3.4.36 noResourceRestrictionForTTIBundling-r12 66

4.3.4.37 Void 66

4.3.4.38 discoverySignalsInDeactSCell-r12 66

4.3.4.39 ul-64QAM-r12 66

4.3.4.40 supportedMIMO-CapabilityDL-r12 66

4.3.4.41 alternativeTBS-Indices-r12 66

4.3.4.42 codebook-HARQ-ACK-r13 66

4.3.4.43 fdd-HARQ-TimingTDD-r13 67

4.3.4.44 maxNumberUpdatedCSI-Proc-r13 67

4.3.4.45 pucch-Format4-r13 67

4.3.4.46 pucch-Format5-r13 67

4.3.4.47 pucch-SCell-r13 67

4.3.4.48 supportedBlindDecoding-r13 67

4.3.4.48.1 maxNumberDecoding-r13 67

4.3.4.48.2 pdcch-CandidateReductions-r13 67

4.3.4.48.3 skipMonitoringDCI-Format0-1A-r13 67

4.3.4.49 crs-InterfMitigationTM10-r13 67

4.3.4.49a crs-InterfMitigationTM1toTM9-r13 68

4.3.4.50 pdsch-CollisionHandling-r13 68

4.3.4.51 aperiodicCSI-Reporting-r13 68

4.3.4.52 crossCarrierScheduling-B5C-r13 68

4.3.4.53 spatialBundling-HARQ-ACK-r13 68

4.3.4.54 uci-PUSCH-Ext-r13 68

4.3.4.55 multiTone-r13 68

4.3.4.56 multiCarrier-r13 69

4.3.4.57 cch-InterfMitigation-RefRecTypeA-r13 69

4.3.4.58 cch-InterfMitigation-RefRecTypeB-r13 69

4.3.4.59 cch-InterfMitigation-MaxNumCCs-r13 69

4.3.4.60 tdd-TTI-Bundling-r14 69

4.3.4.61 dmrs-LessUpPTS-r14 69

4.3.4.62 twoHARQ-Processes-r14 69

4.3.4.63 ce-PUSCH-NB-MaxTBS-r14 69

4.3.4.64 ce-PDSCH-PUSCH-MaxBandwidth-r14 69

4.3.4.65 ce-HARQ-AckBundling-r14 70

4.3.4.66 ce-PDSCH-TenProcesses-r14 70

4.3.4.67 ce-RetuningSymbols-r14 70

4.3.4.68 ce-PDSCH-PUSCH-Enhancement-r14 70

4.3.4.69 ce-SchedulingEnhancement-r14 70

4.3.4.70 ce-SRS-Enhancement-r14 70

4.3.4.70A ce-SRS-EnhancementWithoutComb4-r14 70

4.3.4.71 ce-PUCCH-Enhancement-r14 70

4.3.4.72 ce-ClosedLoopTxAntennaSelection-r14 70

4.3.4.73 ul-256QAM-r14 71

4.3.4.73A ul-256QAM-r15 71

4.3.4.74 alternativeTBS-Index-r14 71

4.3.4.75 multiCarrier-NPRACH-r14 71

4.3.4.76 multiCarrierPaging-r14 71

4.3.4.77 ul-256QAM-perCC-InfoListr14 71

4.3.4.78 unicast-fembmsMixedSCell-r14 71

4.3.4.79 emptyUnicastRegion-r14 71

4.3.4.80 interferenceRandomisation-r14 71

4.3.4.81 must-CapabilityPerBand-r14 71

4.3.4.81.1 must-TM234-UpTo2Tx-r14 71

4.3.4.81.2 must-TM89-UpToOneInterferingLayer-r14 72

4.3.4.81.3 must-TM10-UpToOneInterferingLayer-r14 72

4.3.4.81.4 must-TM89-UpToThreeInterferingLayers-r14 72

4.3.4.81.5 must-TM10-UpToThreeInterferingLayers-r14 72

4.3.4.82 crs-LessDwPTS-r14 72

4.3.4.83 dl-1024QAM-Slot-r15 72

4.3.4.84 dl-1024QAM-SubslotTA-1-r15 72

4.3.4.85 dl-1024QAM-SubslotTA-2-r15 72

4.3.4.86 dmrs-PositionPattern-r15 72

4.3.4.87 dmrs-RepetitionSubslotPDSCH-r15 72

4.3.4.88 dmrs-SharingSubslotPDSCH-r15 72

4.3.4.89 epdcch-SPT-differentCells-r15 72

4.3.4.90 epdcch-STTI-differentCells-r15 72

4.3.4.91 maxLayersSlotOrSubslotPUSCH-r15 73

4.3.4.92 maxNumberUpdatedCSI-Proc-SPT-r15 73

4.3.4.93 Void 73

4.3.4.94 numberOfBlindDecodesUSS-r15 73

4.3.4.95 pdsch-SlotSubslotPDSCH-Decoding-r15 73

4.3.4.96 simultaneousTx-differentTx-duration-r15 73

4.3.4.97 slotPDSCH-TxDiv-TM8-r15 73

4.3.4.98 slotPDSCH-TxDiv-TM9and10-r15 73

4.3.4.99 spdcch-differentRS-types-r15 73

4.3.4.100 spt-Parameters-r15 73

4.3.4.101 sps-CyclicShift-r15 73

4.3.4.102 subslotPDSCH-TxDiv-TM9and10-r15 73

4.3.4.103 sTTI-SupportedCombinations-r15 74

4.3.4.104 Void 74

4.3.4.105 sTTI-SPT-BandParameters-r15 74

4.3.4.106 sTTI-SupportedCSI-Proc-r15 74

4.3.4.107 txDiv-SPUCCH-r15 74

4.3.4.108 ul-256QAM-Slot-r15 74

4.3.4.109 ul-256QAM-Subslot-r15 74

4.3.4.110 ue-TxAntennaSelection-SRS-1T4R-r15 74

4.3.4.111 ue-TxAntennaSelection-SRS-2T4R-2Pairs-r15 74

4.3.4.112 ue-TxAntennaSelection-SRS-2T4R-3Pairs-r15 74

4.3.4.113 wakeUpSignal-r15 75

4.3.4.114 wakeUpSignalMinGap-eDRX-r15 75

4.3.4.115 mixedOperationMode-r15 75

4.3.4.116 void 75

4.3.4.117 sr-WithHARQ-ACK-r15 75

4.3.4.118 sr-WithoutHARQ-ACK-r15 75

4.3.4.119 nprach-Format2-r15 75

4.3.4.120 ce-UL-HARQ-ACK-Feedback-r15 75

4.3.4.121 ce-PDSCH-FlexibleStartPRB-CE-ModeA-r15 75

4.3.4.122 ce-PDSCH-FlexibleStartPRB-CE-ModeB-r15 75

4.3.4.123 ce-PUSCH-FlexibleStartPRB-CE-ModeA-r15 75

4.3.4.124 ce-PUSCH-FlexibleStartPRB-CE-ModeB-r15 76

4.3.4.125 ce-CRS-IntfMitig-r15 76

4.3.4.126 ce-PDSCH-64QAM-r15 76

4.3.4.127 ce-CQI-AlternativeTable-r15 76

4.3.4.128 ce-PUSCH-SubPRB-Allocation-r15 76

4.3.4.129 wakeUpSignal-TDD-r15 76

4.3.4.130 wakeUpSignalMinGap-eDRX-TDD-r15 76

4.3.4.131 shortCqi-ForSCellActivation-r15 76

4.3.4.132 crs-IntfMitig-r15 76

4.3.4.133 srs-UpPTS-6sym-r14 76

4.3.4.134 multiCarrierPagingTDD-r15 77

4.3.4.135 altMCS-Table-r15 77

4.3.4.136 ul-PowerControlEnhancements-r15 77

4.3.4.137 additionalTransmissionSIB1-r15 77

4.3.4.138 aperiodicCsi-ReportingSTTI-r15 77

4.3.4.139 dmrs-BasedSPDCCH-MBSFN-r15 77

4.3.4.140 dmrs-BasedSPDCCH-nonMBSFN -r15 77

4.3.4.141 maxNumberUpdatedCSI-Proc-STTI-Comb77-r15 77

4.3.4.142 maxNumberUpdatedCSI-Proc-STTI-Comb27-r15 77

4.3.4.143 maxNumberUpdatedCSI-Proc-STTI-Comb22-Set1-r15 77

4.3.4.144 maxNumberUpdatedCSI-Proc-STTI-Comb22-Set2-r15 77

4.3.4.145 powerUCI-SlotPUSCH-r15 78

4.3.4.146 powerUCI-SubslotPUSCH-r15 78

4.3.4.147 spdcch-Reuse-r15 78

4.3.4.148 sps-STTI-r15 78

4.3.4.149 sTTI-FD-MIMO-Coexistence-r15 78

4.3.4.150 sTTI-SPT-Supported-r15 78

4.3.4.151 tm8-slotPDSCH-r15 78

4.3.4.152 tm9-slotSubslot-r15 78

4.3.4.153 tm9-slotSubslotMBSFN-r15 78

4.3.4.154 tm10-slotSubslot-r15 78

4.3.4.155 tm10-slotSubslotMBSFN-r15 78

4.3.4.156 ul-AsyncHarqSharingDiff-TTI-Lengths-r15 79

4.3.4.157 semiStaticCFI-r15 79

4.3.4.158 semiStaticCFI-Pattern-r15 79

4.3.4.159 pdsch-RepSubframe-r15 79

4.3.4.160 pdsch-RepSlot-r15 79

4.3.4.161 pdsch-RepSubslot-r15 79

4.3.4.162 pusch-SPS-SubframeRepPCell-r15 79

4.3.4.163 pusch-SPS-SubframeRepPSCell-r15 79

4.3.4.164 pusch-SPS-SubframeRepSCell-r15 79

4.3.4.165 pusch-SPS-SlotRepPCell-r15 79

4.3.4.166 pusch-SPS-SlotRepPSCell-r15 79

4.3.4.167 pusch-SPS-SlotRepSCell-r15 80

4.3.4.168 pusch-SPS-SubslotRepPCell-r15 80

4.3.4.169 pusch-SPS-SubslotRepPSCell-r15 80

4.3.4.170 pusch-SPS-SubslotRepSCell-r15 80

4.3.4.171 pusch-SPS-MaxConfigSubframe-r15 80

4.3.4.172 pusch-SPS-MultiConfigSubframe-r15 80

4.3.4.173 pusch-SPS-MaxConfigSlot-r15 80

4.3.4.174 pusch-SPS-MultiConfigSlot-r15 80

4.3.4.175 pusch-SPS-MaxConfigSubslot-r15 80

4.3.4.176 pusch-SPS-MultiConfigSubslot-r15 80

4.3.4.177 npusch-3dot75kHz-SCS-TDD-r15 81

4.3.4.178 crs-IM-TM1-toTM9-OneRX-Port 81

4.3.4.179 cch-IM-RefRecTypeA-OneRX-Port 81

4.3.4.180 dmrs-OverheadReduction-r15 81

4.3.4.181 srs-DCI7-TriggeringFS2-r15 81

4.3.4.182 npusch-MultiTB-r16 81

4.3.4.183 npdsch-MultiTB-r16 81

4.3.4.184 pusch-MultiTB-CE-ModeA-r16 81

4.3.4.185 pdsch-MultiTB-CE-ModeA-r16 82

4.3.4.186 pusch-MultiTB-CE-ModeB-r16 82

4.3.4.187 pdsch-MultiTB-CE-ModeB-r16 82

4.3.4.188 ce-CSI-RS-Feedback-r16 82

4.3.4.188a ce-CSI-RS-FeedbackCodebookRestriction-r16 82

4.3.4.189 mpdcch-InLteControlRegionCE-ModeA-r16 82

4.3.4.189a mpdcch-InLteControlRegionCE-ModeB-r16 82

4.3.4.189b pdsch-InLteControlRegionCE-ModeA-r16 82

4.3.4.189c pdsch-InLteControlRegionCE-ModeB-r16 82

4.3.4.190 crs-ChEstMPDCCH-CE-ModeA-r16 83

4.3.4.190a crs-ChEstMPDCCH-CE-ModeB-r16 83

4.3.4.190b crs-ChEstMPDCCH-CSI-r16 83

4.3.4.190c crs-ChEstMPDCCH-ReciprocityTDD-r16 83

4.3.4.191 widebandPRG-Slot-r16, widebandPRG-Subslot-r16, widebandPRG-Subframe-r16 83

4.3.4.192 npusch-MultiTB-Interleaving-r16 83

4.3.4.193 npdsch-MultiTB-Interleaving-r16 83

4.3.4.194 multiTB-HARQ-AckBundling-r16 83

4.3.4.195 groupWakeUpSignal-r16 83

4.3.4.196 groupWakeUpSignalAlternation-r16 84

4.3.4.197 subframeResourceResvUL-r16 84

4.3.4.198 subframeResourceResvDL-r16 84

4.3.4.199 slotSymbolResourceResvUL-r16 84

4.3.4.200 slotSymbolResourceResvDL-r16 84

4.3.4.201 groupWakeUpSignalTDD-r16 84

4.3.4.202 groupWakeUpSignalAlternationTDD-r16 84

4.3.4.203 subframeResourceResvUL-CE-ModeA-r16 84

4.3.4.204 subframeResourceResvUL-CE-ModeB-r16 84

4.3.4.205 subframeResourceResvDL-CE-ModeA-r16 85

4.3.4.206 subframeResourceResvDL-CE-ModeB-r16 85

4.3.4.207 slotSymbolResourceResvUL-CE-ModeA-r16 85

4.3.4.208 slotSymbolResourceResvUL-CE-ModeB-r16 85

4.3.4.209 slotSymbolResourceResvDL-CE-ModeA-r16 85

4.3.4.210 slotSymbolResourceResvDL-CE-ModeB-r16 85

4.3.4.211 subcarrierPuncturingCE-ModeA-r16 85

4.3.4.212 subcarrierPuncturingCE-ModeB-r16 85

4.3.4.213 ce-MultiTB-Interleaving-r16 85

4.3.4.214 ce-MultiTB-HARQ-AckBundling-r16 85

4.3.4.215 ce-MultiTB-SubPRB-r16 86

4.3.4.216 ce-MultiTB-EarlyTermination-r16 86

4.3.4.217 ce-MultiTB-64QAM-r16 86

4.3.4.218 ce-MultiTB-FrequencyHopping-r16 86

4.3.4.219 Void 86

4.3.4.220 virtualCellID-BasicSRS-r16 86

4.3.4.221 addSRS-r16 86

4.3.4.221.1 addSRS-1T2R-r16 86

4.3.4.221.2 addSRS-1T4R-r16 86

4.3.4.221.3 addSRS-2T4R-2Pairs-r16 86

4.3.4.221.4 addSRS-2T4R-3Pairs-r16 87

4.3.4.221.5 addSRS-AntennaSwitching-r16 87

4.3.4.221.6 addSRS-CarrierSwitching-r16 87

4.3.4.221.7 addSRS-FrequencyHopping-r16 87

4.3.4.221.8 virtualCellID-AddSRS-r16 87

4.3.4.222 npdsch-16QAM-r17 87

4.3.4.223 npusch-16QAM-r17 87

4.3.4.224 ce-PDSCH-MaxTBS-r17 87

4.3.4.225 ce-PDSCH-14HARQProcesses-r17 88

4.3.4.226 ce-PDSCH-14HARQProcesses-Alt2-r17 88

4.3.4.227 csi-SubframeSet2ForDormantSCell-r17 88

4.3.5 RF parameters 88

4.3.5.1 supportedBandListEUTRA 88

4.3.5.1.1 ue-PowerClass-N-r13, ue-PowerClass-5-r13 88

4.3.5.1.2 intraFreq-CE-NeedForGaps-r13 88

4.3.5.1.3 ue-CA-PowerClass-N 88

4.3.5.1.4 lowerMSD-MRDC-r18 88

4.3.5.1A supportedBandList-r13 88

4.3.5.1A.1 powerClassNB-20dBm-r13 88

4.3.5.1A.2 powerClassNB-14dBm-r14 89

4.3.5.1A.3 powerBoostingNB-r19 89

4.3.5.2 supportedBandCombination 89

4.3.5.2.1 supportedBandCombinationReduced-r13 90

4.3.5.3 multipleTimingAdvance 90

4.3.5.4 simultaneousRx-Tx 90

4.3.5.5 supportedCSI-Proc-r11 90

4.3.5.6 freqBandRetrieval-r11 90

4.3.5.7 dl-256QAM-r12 90

4.3.5.8 supportedNAICS-2CRS-AP-r12 91

4.3.5.9 dc-Support-r12 91

4.3.5.9.1 asynchronous-r12 91

4.3.5.9.2 supportedCellGrouping-r12 91

4.3.5.10 modifiedMPR-Behavior-r10 91

4.3.5.11 freqBandPriorityAdjustment-r12 91

4.3.5.12 commSupportedBandsPerBC-r12 91

4.3.5.13 supportedCSI-Proc-r12 91

4.3.5.14 fourLayerTM3-TM4-r10 91

4.3.5.15 fourLayerTM3-TM4-perCC-r12 91

4.3.5.16 multiNS-Pmax-r10 92

4.3.5.16A multiNS-Pmax-r13 92

4.3.5.17 differentFallbackSupported-r13 92

4.3.5.18 maximumCCsRetrieval-r13 92

4.3.5.19 skipFallbackCombinations-r13 92

4.3.5.20 Void 92

4.3.5.21 reducedIntNonContComb-r13 92

4.3.5.22 additionalRx-Tx-PerformanceReq-r13 92

4.3.5.23 maxLayersMIMO-Indication-r12 92

4.3.5.24 rf-RetuningTimeDL-r14 93

4.3.5.25 rf-RetuningTimeUL-r14 93

4.3.5.26 diffFallbackCombReport-r14 93

4.3.5.27 v2x-SupportedTxBandCombListPerBC-r14, v2x-SupportedRxBandCombListPerBC-r14 93

4.3.5.28 txAntennaSwitchDL-r13 93

4.3.5.29 txAntennaSwitchUL-r13 93

4.3.5.30 supportedMIMO-CapabilityDL-r15 93

4.3.5.31 dl-1024QAM-r15 93

4.3.5.32 srs-MaxSimultaneousCCs-r14 94

4.3.5.33 powerClass-14dBm-r15 94

4.3.5.34 supportedMIMO-CapabilityDL-MRDC-r15 94

4.3.5.35 srs-FlexibleTiming-r14 94

4.3.5.36 srs-HARQ-ReferenceConfig-r14 94

4.3.5.37 fourLayerTM3-TM4-r15 94

4.3.5.38 supportedCSI-Proc-r15 94

4.3.5.39 intraFreqAsyncDAPS-r16 95

4.3.5.40 intraFreqDAPS-r16 95

4.3.5.41 Void 95

4.3.5.42 interFreqAsyncDAPS-r16 95

4.3.5.43 interFreqDAPS-r16 95

4.3.5.44 interFreqMultiUL-TransmissionDAPS-r16 95

4.3.5.45 intraFreqTwoTAGs-DAPS-r16 95

4.3.5.46 v2x-SupportedTxBandCombListPerBC-v1630, v2x-SupportedRxBandCombListPerBC-v1630 95

4.3.5.47 scalingFactorTxSidelink-r16, scalingFactorRxSidelink-r16 95

4.3.5.48 interBandPowerSharingSyncDAPS-r16 96

4.3.5.49 interBandPowerSharingAsyncDAPS-r16 96

4.3.5.50 multiNS-PmaxAerial-r18 96

4.3.5.51 sl-A2X-SupportedBandCombinationList-r18 96

4.3.6 Measurement parameters 96

4.3.6.1 interFreqNeedForGaps and interRAT-NeedForGaps 96

4.3.6.2 rsrqMeasWideband 96

4.3.6.3 timerT312-r12 96

4.3.6.4 alternativeTimeToTrigger-r12 96

4.3.6.5 benefitsFromInterruption-r11 96

4.3.6.6 incMonEUTRA-r12 97

4.3.6.7 incMonUTRA-r12 97

4.3.6.8 extendedMaxMeasId-r12 97

4.3.6.9 crs-DiscoverySignalsMeas-r12 97

4.3.6.10 csi-RS-DiscoverySignalsMeas-r12 97

4.3.6.11 extendedRSRQ-LowerRange-r12 97

4.3.6.12 rsrq-OnAllSymbols-r12 97

4.3.6.13 rs-SINR-Meas-r13 97

4.3.6.14 allowedCellList-r13 97

4.3.6.15 extendedFreqPriorities-r13 98

4.3.6.16 extendedMaxObjectId-r13 98

4.3.6.17 ul-PDCP-Delay-r13 98

4.3.6.18 Void 98

4.3.6.19 rssi-AndChannelOccupancyReporting-r13 98

4.3.6.20 multiBandInfoReport-r13 98

4.3.6.21 Void 98

4.3.6.22 Void 98

4.3.6.23 ceMeasurements-r14 98

4.3.6.24 ncsg-r14 98

4.3.6.25 perServingCellMeasurementGap-r14 98

4.3.6.26 shortMeasurementGap-r14 99

4.3.6.27 nonUniformGap-r14 99

4.3.6.28 rlm-ReportSupport-r14 99

4.3.6.29 Void 99

4.3.6.30 qoe-MeasReport-r15 99

4.3.6.31 ca-IdleModeMeasurements-r15 99

4.3.6.32 ca-IdleModeValidityArea-r15 99

4.3.6.33 qoe-MTSI-MeasReport-r15 99

4.3.6.34 multipleCellsMeasExtension-r15 99

4.3.6.35 heightMeas-r15 99

4.3.6.36 measGapPatterns-r15 99

4.3.6.37 dl-ChannelQualityReporting-r16 99

4.3.6.37a ce-DL-ChannelQualityReporting-r16 100

4.3.6.38 interRAT-NeedForGapsNR-r16 100

4.3.6.39 ce-MeasRSS-Dedicated-r16 100

4.3.6.39a ce-MeasRSS-DedicatedSameRBs-r16 100

4.3.6.40 eutra-IdleInactiveMeasurements-r16 100

4.3.6.41 nr-IdleInactiveMeasFR1-r16 100

4.3.6.42 nr-IdleInactiveMeasFR2-r16 100

4.3.6.43 idleInactiveValidityAreaList-r16 100

4.3.6.44 measGapPatterns-NRonly-r16 101

4.3.6.45 measGapPatterns-NRonly-ENDC-r16 101

4.3.6.46 nr-IdleInactiveBeamMeasFR1-r16 101

4.3.6.47 nr-IdleInactiveBeamMeasFR2-r16 101

4.3.6.48 nr-RSSI-ChannelOccupancyReporting-r17 101

4.3.6.49 connModeMeasIntraFreq-r17 101

4.3.6.50 connModeMeasInterFreq-r17 101

4.3.6.51 nr-CellIndividualOffset-r16 101

4.3.6.52 gaplessMeas-FR2-maxCC-r17 101

4.3.6.53 interRAT-NeedForInterruptionNR-r18 102

4.3.6.54 simultaneousRxDataSSB-DiffNumerology-FR1-r18 102

4.3.6.55 a4-a5-ReportOnLeaveSupport-r15 102

4.3.7 Inter-RAT parameters 102

4.3.7.1 utraFDD 102

4.3.7.2 supportedBandListUTRA-FDD 102

4.3.7.3 utraTDD128 102

4.3.7.4 supportedBandListUTRA-TDD128 102

4.3.7.5 utraTDD384 102

4.3.7.6 supportedBandListUTRA-TDD384 102

4.3.7.7 utraTDD768 102

4.3.7.8 supportedBandListUTRA-TDD768 103

4.3.7.9 geran 103

4.3.7.10 supportedBandListGERAN 103

4.3.7.11 interRAT-PS-HO-ToGERAN 103

4.3.7.12 cdma2000-HRPD 103

4.3.7.13 supportedBandListHRPD 103

4.3.7.14 tx-ConfigHRPD 103

4.3.7.15 rx-ConfigHRPD 103

4.3.7.16 cdma2000-1xRTT 103

4.3.7.17 supportedBandList1XRTT 103

4.3.7.18 tx-Config1XRTT 103

4.3.7.19 rx-Config1XRTT 103

4.3.7.20 e-CSFB-1XRTT 104

4.3.7.21 e-CSFB-ConcPS-Mob1XRTT 104

4.3.7.22 e-RedirectionUTRA 104

4.3.7.23 e-RedirectionGERAN 104

4.3.7.24 dtm 104

4.3.7.25 e-CSFB-dual-1XRTT 104

4.3.7.26 e-RedirectionUTRA-TDD 104

4.3.7.27 cdma2000-NW-Sharing-r11 104

4.3.7.28 mfbi-UTRA 104

4.3.7.29 supportedBandListWLAN 104

4.3.7.30 supportedBandListNB-r19 104

4.3.8 General parameters 105

4.3.8.1 accessStratumRelease 105

4.3.8.1A accessStratumRelease-r13 105

4.3.8.2 deviceType 105

4.3.8.3 Void 105

4.3.8.4 Void 105

4.3.8.5 multipleDRB-r13 105

4.3.8.6 Void 105

4.3.8.7 earlyData-UP-r15 105

4.3.8.8 void 105

4.3.8.9 extendedNumberOfDRBs-r15 105

4.3.8.10 reducedCP-Latency-r15 105

4.3.8.11 earlySecurityReactivation-r16 105

4.3.8.12 Void 106

4.3.8.13 Void 106

4.3.8.14 dl-DedicatedMessageSegmentation-r16 106

4.3.8.15 altFreqPriority-r16 106

4.3.8.16 coverageBasedPaging-r17 106

4.3.8.17 pws-Support-r19 106

4.3.9 Void 106

4.3.10 CSG Proximity Indication parameters 106

4.3.10.1 intraFreqProximityIndication 106

4.3.10.2 interFreqProximityIndication 106

4.3.10.3 utran-ProximityIndication 106

4.3.11 Neighbour cell SI acquisition parameters 106

4.3.11.1 intraFreqSI-AcquisitionForHO 106

4.3.11.2 interFreqSI-AcquisitionForHO 106

4.3.11.3 utran-SI-AcquisitionForHO 107

4.3.11.4 reportCGI-NR-EN-DC-r15 107

4.3.11.5 reportCGI-NR-NoEN-DC-r15 107

4.3.11.6 eutra-CGI-Reporting-ENDC 107

4.3.11.7 utra-GERAN-CGI-Reporting-ENDC 107

4.3.11.8 eutra-SI-AcquisitionForHO-ENDC-r16 107

4.3.11.9 nr-AutonomousGaps-ENDC-FR1-r16 108

4.3.11.10 nr-AutonomousGaps-ENDC-FR2-r16 108

4.3.11.11 nr-AutonomousGaps-FR1-r16 108

4.3.11.12 nr-AutonomousGaps-FR2-r16 108

4.3.11.13 eutra-CGI-Reporting-NEDC-r15 108

4.3.11.14 gNB-ID-Length-Reporting-NR-EN-DC-r17 108

4.3.11.15 gNB-ID-Length-Reporting-NR-NoEN-DC-r17 108

4.3.11.16 eutra-reportCGI-HSDN-r19 108

4.3.11.17 nr-reportCGI-HSDN-r19 109

4.3.12 SON parameters 109

4.3.12.1 rach-Report 109

4.3.12.2 anr-Report-r16 109

4.3.12.3 rach-Report-r16 109

4.3.12.4 rach-ReportForNR-r18 109

4.3.12.5 locationInfo-r16 109

4.3.13 UE-based network performance measurement parameters 109

4.3.13.1 loggedMeasurementsIdle 109

4.3.13.2 standaloneGNSS-Location 109

4.3.13.3 Void 109

4.3.13.4 loggedMBSFNMeasurements-r12 109

4.3.13.5 locationReport-r14 109

4.3.13.6 loggedMeasBT-r15 110

4.3.13.7 loggedMeasWLAN-r15 110

4.3.13.8 immMeasBT-r15 110

4.3.13.9 immMeasWLAN-r15 110

4.3.13.10 ul-PDCP-AvgDelay-r16 110

4.3.13.11 loggedMeasIdleEventL1-r17 110

4.3.13.12 loggedMeasIdleEventOutOfCoverage-r17 110

4.3.13.13 loggedMeasUncomBarPre-r17 110

4.3.13.14 immMeasUncomBarPre-r17 110

4.3.13.15 sigBasedEUTRA-LoggedMeasOverrideProtect-r18 110

4.3.14 IMS Voice parameters 110

4.3.14.1 voiceOver-PS-HS-UTRA-FDD 110

4.3.14.2 voiceOver-PS-HS-UTRA-TDD128 111

4.3.14.3 srvcc-FromUTRA-FDD-ToGERAN 111

4.3.14.4 srvcc-FromUTRA-FDD-ToUTRA-FDD 111

4.3.14.5 srvcc-FromUTRA-TDD128-ToGERAN 111

4.3.14.6 srvcc-FromUTRA-TDD128-ToUTRA-TDD128 111

4.3.15 Other parameters 111

4.3.15.1 Void 111

4.3.15.2 inDeviceCoexInd-r11 111

4.3.15.3 powerPrefInd-r11 111

4.3.15.4 ue-Rx-TxTimeDiffMeasurements-r11 111

4.3.15.5 Void 111

4.3.15.6 Void 111

4.3.15.7 Void 111

4.3.15.8 inDeviceCoexInd-UL-CA-r11 111

4.3.15.9 bwPrefInd-r14 112

4.3.15.10 inDeviceCoexInd-HardwareSharingInd-r13 112

4.3.15.11 overheatingInd-r14 112

4.3.15.12 assistInfoBitForLC-r15 112

4.3.15.13 timeReferenceProvision-r15 112

4.3.15.14 flightPathPlan-r15 112

4.3.15.15 inDeviceCoexInd-ENDC-r15 112

4.3.15.16 nonCSG-SI-Reporting-r14 112

4.3.15.17 resumeWithStoredMCG-SCells-r16 112

4.3.15.18 resumeWithMCG-SCellConfig-r16 112

4.3.15.19 resumeWithStoredSCG-r16 112

4.3.15.20 resumeWithSCG-Config-r16 113

4.3.15.21 mcgRLF-RecoveryViaSCG-r16 113

4.3.15.22 overheatingIndForSCG-r16 113

4.3.15.23 mpsPriorityIndication-r16 113

4.3.15.24 ul-RRC-Segmentation-r16 113

4.3.15.25 ul-RRC-MaxCapaSegments-r17 113

4.3.15.26 ntn-Redirection-r19 113

4.3.15.27 ntn-Redirection-NB-r19 113

4.3.16 Positioning parameters 113

4.3.16.1 otdoa-UE-assisted 113

4.3.16.2 interFreqRSTDmeasurement 113

4.3.17 MBMS parameters 114

4.3.17.1 mbms-SCell-r11 114

4.3.17.2 mbms-NonServingCell-r11 114

4.3.17.3 mbms-AsyncDC-r12 114

4.3.17.4 fembmsMixedCell-r14 114

4.3.17.5 fembmsDedicatedCell-r14 114

4.3.17.6 subcarrierSpacingMBMS-khz1dot25-r14, subcarrierSpacingMBMS-khz7dot5-r14 114

4.3.17.6a subcarrierSpacingMBMS-khz0dot37-r16, subcarrierSpacingMBMS-khz2dot5-r16 114

4.3.17.7 mbms-MaxBW-r14 114

4.3.17.8 mbms-ScalingFactor1dot25-r14, mbms-ScalingFactor7dot5-r14 115

4.3.17.9 mbms-ScalingFactor0dot37-r16, mbms-ScalingFactor2dot5-r16 115

4.3.17.10 timeSeparationSlot2-r16, timeSeparationSlot4-r16 115

4.3.17.11 pmch-Bandwidth-n40-r17, pmch-Bandwidth-n35-r17, pmch-Bandwidth-n30-r17 115

4.3.17.12 cas-Muting-5GB-r19 115

4.3.17.13 timeInterleavingKhz15-r19, timeInterleavingKhz7dot5-r19, timeInterleavingKhz2dot5-r19, timeInterleavingKhz1dot25-r19 115

4.3.17.14 pmch-CyclicShiftAlpha1-r19 116

4.3.17.15 pmch-CyclicShiftAlpha2-r19 116

4.3.17.16 pmch-CyclicShiftAlpha3-r19 116

4.3.17.17 freqInterleavingKhz15-r19, freqInterleavingKhz7dot5-r19, freqInterleavingKhz2dot5-r19, freqInterleavingKhz1dot25-r19 116

4.3.18 RAN-assisted WLAN interworking parameters 116

4.3.18.1 wlan-IW-RAN-Rules-r12 116

4.3.18.2 wlan-IW-ANDSF-Policies-r12 116

4.3.18.3 rclwi-r13 116

4.3.19 MAC parameters 116

4.3.19.1 longDRX-Command-r12 116

4.3.19.2 logicalChannelSR-ProhibitTimer-r12 116

4.3.19.3 extendedMAC-LengthField-r13 117

4.3.19.4 extendedLongDRX-r13 117

4.3.19.5 shortSPS-IntervalFDD-r14 117

4.3.19.6 shortSPS-IntervalTDD-r14 117

4.3.19.7 skipUplinkDynamic-r14 117

4.3.19.8 skipUplinkSPS-r14 117

4.3.19.9 dataInactMon-r14 117

4.3.19.10 rai-Support-r14 117

4.3.19.11 multipleUplinkSPS-r14 117

4.3.19.12 min-Proc-TimelineSubslot-r15 117

4.3.19.13 skipSubframeProcessing-r15 118

4.3.19.14 earlyContentionResolution-r14 118

4.3.19.15 sr-SPS-BSR-r15 118

4.3.19.16 dormantSCellState-r15 118

4.3.19.17 directSCellActivation-r15 118

4.3.19.18 directSCellHibernation-r15 118

4.3.19.19 sps-ServingCell-r15 118

4.3.19.20 extendedLCID-Duplication-r15 118

4.3.19.21 eLCID-Support-r15 118

4.3.19.22 rai-SupportEnh-r16 118

4.3.19.23 directMCG-SCellActivationResume-r16 119

4.3.19.24 directSCG-SCellActivationResume-r16 119

4.3.19.25 directSCG-SCellActivationNEDC-r16 119

4.3.20 Dual Connectivity parameters 119

4.3.20.1 drb-TypeSplit-r12 119

4.3.20.2 drb-TypeSCG-r12 119

4.3.20.3 pdcp-TransferSplitUL-r13 119

4.3.20.4 ue-SSTD-Meas-r13 119

4.3.21 Sidelink parameters 119

4.3.21.1 commSupportedBands-r12 119

4.3.21.2 commSimultaneousTx-r12 120

4.3.21.3 discSupportedBands-r12 120

4.3.21.4 discScheduledResourceAlloc-r12 120

4.3.21.5 disc-UE-SelectedResourceAlloc-r12 120

4.3.21.6 disc-SLSS-r12 120

4.3.21.7 discSupportedProc-r12 120

4.3.21.8 commMultipleTx-r13 120

4.3.21.9 discInterFreqTx-r13 120

4.3.21.10 discPeriodicSLSS-r13 120

4.3.21.11 discSysInfoReporting-r13 120

4.3.21.12 zoneBasedPoolSelection-r14 121

4.3.21.13 v2x-HighReception-r14 121

4.3.21.14 v2x-eNB-Scheduled-r14 121

4.3.21.15 ue-AutonomousWithFullSensing-r14 121

4.3.21.16 ue-AutonomousWithPartialSensing-r14 121

4.3.21.17 slss-TxRx-r14 121

4.3.21.18 sl-CongestionControl-r14 121

4.3.21.19 v2x-TxWithShortResvInterval-r14 121

4.3.21.20 v2x-numberTxRxTiming-r14 121

4.3.21.21 v2x-nonAdjacentPSCCH-PSSCH-r14 121

4.3.21.22 v2x-HighPower-r14 121

4.3.21.23 v2x-SupportedBandCombinationList-r14 122

4.3.21.24 slss-SupportedTxFreq-r15 122

4.3.21.25 sl-64QAM-Tx-r15 122

4.3.21.26 sl-TxDiversity-r15 122

4.3.21.27 v2x-EnhancedHighReception-r15 122

4.3.21.28 sl-64QAM-Rx-r15 122

4.3.21.29 sl-RateMatchingTBSScaling-r15 122

4.3.21.30 sl-LowT2min-r15 122

4.3.21.31 v2x-SensingReportingMode3-r15 122

4.3.21.32 v2x-SupportedBandCombinationListEUTRA-NR-r16 122

4.3.21.33 Void 123

4.3.21.34 tx-Sidelink-r16, rx-Sidelink-r16 123

4.3.21.35 sl-A2X-Service-r18 123

4.3.22 SC-PTM parameters 123

4.3.22.1 scptm-ParallelReception-r13 123

4.3.22.2 Void 123

4.3.22.3 scptm-SCell-r13 123

4.3.22.4 scptm-NonServingCell-r13 123

4.3.22.5 scptm-AsyncDC-r13 123

4.3.23 LAA parameters 124

4.3.23.1 downlinkLAA-r13 124

4.3.23.2 crossCarrierSchedulingLAA-DL-r13 124

4.3.23.3 csi-RS-DRS-RRM-MeasurementsLAA-r13 124

4.3.23.4 endingDwPTS-r13 124

4.3.23.5 secondSlotStartingPosition-r13 124

4.3.23.6 tm9-LAA-r13 124

4.3.23.7 tm10-LAA-r13 124

4.3.23.8 uplinkLAA-r14 124

4.3.23.9 crossCarrierSchedulingLAA-UL-r14 124

4.3.23.10 twoStepSchedulingTimingInfo-r14 124

4.3.23.11 uss-BlindDecodingAdjustment-r14 125

4.3.23.12 uss-BlindDecodingReduction-r14 125

4.3.23.13 outOfSequenceGrantHandling-r14 125

4.3.23.14 aul-r15 125

4.3.23.15 laa-PUSCH-Mode1-r15 125

4.3.23.16 laa-PUSCH-Mode2-r15 125

4.3.23.17 laa-PUSCH-Mode3-r15 125

4.3.24 LWIP parameters 125

4.3.24.1 lwip-r13 125

4.3.24.2 lwip-Aggregation-UL-r14 125

4.3.24.3 lwip-Aggregation-DL-r14 125

4.3.25 LWA parameters 126

4.3.25.1 lwa-r13 126

4.3.25.2 lwa-SplitBearer-r13 126

4.3.25.3 lwa-BufferSize-r13 126

4.3.25.4 wlan-MAC-Address-r13 126

4.3.25.5 lwa-HO-WithoutWT-Change-r14 126

4.3.25.6 lwa-UL-r14 126

4.3.25.7 Void 126

4.3.25.8 wlan-SupportedDataRate-r14 126

4.3.25.9 lwa-RLC-UM-r14 126

4.3.26 Void 126

4.3.26.1 Void 126

4.3.27 Inter-RAT parameters WLAN 126

4.3.27.1 supportedBandListWLAN-r13 126

4.3.28 EBF FD-MIMO parameters 127

4.3.28.1 beamformed-r13 127

4.3.28.2 channelMeasRestriction-r13 127

4.3.28.3 csi-RS-EnhancementsTDD-r13 127

4.3.28.4 dmrs-Enhancements-r13 127

4.3.28.5 interferenceMeasRestriction-r13 127

4.3.28.6 nonPrecoded-r13 127

4.3.28.7 srs-Enhancements-r13 128

4.3.28.8 srs-EnhancementsTDD-r13 128

4.3.28.9 csi-ReportingAdvanced-r14, csi-ReportingAdvancedMaxPorts-r14 128

4.3.28.10 mimo-CBSR-AdvancedCSI-r15 128

4.3.28.11 csi-ReportingNP-r14 128

4.3.28.12 relWeightTwoLayers-r13, relWeightFourLayers-r13, relWeightEightLayers-r13 128

4.3.28.13 totalWeightedLayers-r13 128

4.3.28.14 zp-CSI-RS-AperiodicInfo-r14 129

4.3.28.15 ul-dmrs-Enhancements-r14 129

4.3.28.16 densityReductionNP-r14, densityReductionBF-r14 129

4.3.28.17 hybridCSI-r14 129

4.3.28.18 semiOL-r14 129

4.3.28.19 nzp-CSI-RS-AperiodicInfo-r14 129

4.3.28.20 nzp-CSI-RS-PeriodicInfo-r14 129

4.3.29 CE parameters 129

4.3.29.1 ce-ModeA-r13 129

4.3.29.2 ce-ModeB-r13 130

4.3.29.3 intraFreqA3-CE-ModeA-r13 130

4.3.29.4 intraFreqA3-CE-ModeB-r13 130

4.3.29.5 intraFreqHO-CE-ModeA-r13 130

4.3.29.6 intraFreqHO-CE-ModeB-r13 130

4.3.29.7 ue-CE-NeedULGaps-r13 130

4.3.29.8 unicastFrequencyHopping-r13 130

4.3.29.9 ce-SwitchWithoutHO-r14 130

4.3.29.10 tm9-CE-ModeA-r13 130

4.3.29.11 tm9-CE-ModeB-r13 130

4.3.29.12 tm6-CE-ModeA-r13 131

4.3.29.13 etws-CMAS-RxInConnCE-ModeA-r16 131

4.3.29.14 etws-CMAS-RxInConnCE-ModeB-r16 131

4.3.30 Mobility enhancement parameters 131

4.3.30.1 makeBeforeBreak-r14 131

4.3.30.2 rach-Less-r14 131

4.3.30.3 cho-r16 131

4.3.30.4 cho-Failure-r16 131

4.3.30.5 cho-FDD-TDD-r16 131

4.3.30.6 cho-TwoTriggerEvents-r16 131

4.3.31 Void 132

4.3.31.1 Void 132

4.3.31.2 Void 132

4.3.32 MMTEL parameters 132

4.3.32.1 delayBudgetReporting-r14 132

4.3.32.2 pusch-Enhancements-r14 132

4.3.32.3 recommendedBitRate-r14 132

4.3.32.4 recommendedBitRateQuery-r14 132

4.3.32.5 recommendedBitRateMultiplier-r16 132

4.3.33 High speed enhancement parameters 132

4.3.33.1 measurementEnhancements-r14 132

4.3.33.2 demodulationEnhancements-r14 132

4.3.33.3 prach-Enhancements-r14 132

4.3.33.4 measurementEnhancements2-r16 132

4.3.33.5 demodulationEnhancements2-r16 133

4.3.33.6 measurementEnhancementsSCell-r16 133

4.3.33.7 interRAT-enhancementNR-r16 133

4.3.34 Inter-RAT Parameters NR 133

4.3.34.1 en-DC-r15 133

4.3.34.2 supportedBandListEN-DC-r15 133

4.3.34.3 supportedBandListNR-SA-r15 133

4.3.34.4 eutra-5GC-HO-ToNR-FDD-FR1-r15 133

4.3.34.5 eutra-5GC-HO-ToNR-TDD-FR1-r15 133

4.3.34.6 eutra-5GC-HO-ToNR-FDD-FR2-r15 133

4.3.34.7 eutra-5GC-HO-ToNR-TDD-FR2-r15 133

4.3.34.8 eutra-EPC-HO-ToNR-FDD-FR1-r15 134

4.3.34.9 eutra-EPC-HO-ToNR-TDD-FR1-r15 134

4.3.34.10 eutra-EPC-HO-ToNR-FDD-FR2-r15 134

4.3.34.11 eutra-EPC-HO-ToNR-TDD-FR2-r15 134

4.3.34.12 sa-NR-r15 134

4.3.34.13 ims-VoiceOverNR-FR1-r15 134

4.3.34.14 ims-VoiceOverNR-FR2-r15 134

4.3.34.15 eventB2-r15 134

4.3.34.16 ss-SINR-Meas-NR-FR1-r15 134

4.3.34.17 ss-SINR-Meas-NR-FR2-r15 134

4.3.34.18 ng-EN-DC-r15 134

4.3.34.19 nr-HO-ToEN-DC-r16 134

4.3.34.20 ce-EUTRA-5GC-HO-ToNR-FDD-FR1-r16 135

4.3.34.21 ce-EUTRA-5GC-HO-ToNR-TDD-FR1-r16 135

4.3.34.22 ce-EUTRA-5GC-HO-ToNR-FDD-FR2-r16 135

4.3.34.23 ce-EUTRA-5GC-HO-ToNR-TDD-FR2-r16 135

4.3.34.24 extendedBand-n77-r16 135

4.3.34.25 eutra-5GC-HO-ToNR-TDD-FR2-2-r17 135

4.3.34.26 eutra-EPC-HO-ToNR-TDD-FR2-2-r17 135

4.3.34.27 ims-VoiceOverNR-FR2-2-r17 135

4.3.34.28 ce-EUTRA-5GC-HO-ToNR-TDD-FR2-2-r17 135

4.3.34.29 extendedBand-n77-2-r17 135

4.3.34.30 ntn-IdleMobilityForNR-r19 136

4.3.35 FeCoMP Parameters 136

4.3.35.1 qcl-CRI-BasedCSI-Reporting-r15 136

4.3.35.2 qcl-TypeC-Operation-r15 136

4.3.36 E-UTRA/5GC Parameters 136

4.3.36.1 eutra-5GC-r15 136

4.3.36.2 eutra-EPC-HO-EUTRA-5GC-r15 136

4.3.36.3 Void 136

4.3.36.4 ho-EUTRA-5GC-FDD-TDD-r15 136

4.3.36.5 ho-InterfreqEUTRA-5GC-r15 136

4.3.36.6 IMS-VoiceOverMCG-BearerEUTRA-5GC-r15 136

4.3.36.7 inactiveState-r15 136

4.3.36.8 reflectiveQoS-r15 137

4.3.36.9 earlyData-UP-5GC-r16 137

4.3.36.10 ce-InactiveState-r16 137

4.3.36.11 ce-EUTRA-5GC-r16 137

4.3.36.12 inactiveStatePO-Determination-r17 137

4.3.37 PUR parameters 137

4.3.37.1 pur-CP-EPC-r16 137

4.3.37.2 pur-UP-EPC-r16 137

4.3.37.3 pur-CP-5GC-r16 137

4.3.37.4 pur-UP-5GC-r16 137

4.3.37.5 pur-CP-L1Ack-r16 137

4.3.37.6 pur-NRSRP-Validation-r16 138

4.3.37.7 pur-CP-EPC-CE-ModeA-r16 138

4.3.37.8 pur-CP-EPC-CE-ModeB-r16 138

4.3.37.9 pur-UP-EPC-CE-ModeA-r16 138

4.3.37.10 pur-UP-EPC-CE-ModeB-r16 138

4.3.37.11 pur-CP-5GC-CE-ModeA-r16 138

4.3.37.12 pur-CP-5GC-CE-ModeB-r16 138

4.3.37.13 pur-UP-5GC-CE-ModeA-r16 138

4.3.37.14 pur-UP-5GC-CE-ModeB-r16 138

4.3.37.15 pur-PUSCH-NB-MaxTBS-r16 139

4.3.37.16 pur-SubPRB-CE-ModeA-r16 139

4.3.37.17 pur-SubPRB-CE-ModeB-r16 139

4.3.37.18 pur-RSRP-Validation-r16 139

4.3.37.19 pur-FrequencyHopping-r16 139

4.3.38 IoT NTN parameters 139

4.3.38.1 ntn-Connectivity-EPC-r17 139

4.3.38.2 ntn-TA-Report-r17 140

4.3.38.3 ntn-PUR-TimerDelay-r17 140

4.3.38.4 ntn-OffsetTimingEnh-r17 140

4.3.38.5 ntn-ScenarioSupport-r17 140

4.3.38.6 ntn-SegmentedPrecompensationGaps-r17 141

4.3.38.7 ntn-EventA4BasedCHO-r18 141

4.3.38.8 ntn-LocationBasedCHO-EFC-r18 141

4.3.38.9 ntn-LocationBasedCHO-EMC-r18 141

4.3.38.10 ntn-TimeBasedCHO-r18 141

4.3.38.11 ntn-LocationBasedMeasTrigger-EFC-r18 141

4.3.38.12 ntn-LocationBasedMeasTrigger-EMC-r18 141

4.3.38.13 ntn-TimeBasedMeasTrigger-r18 141

4.3.38.14 ntn-RRC-HarqDisableSingleTB-r18 141

4.3.38.15 ntn-OverriddenHarqDisableSingleTB-r18 141

4.3.38.16 ntn-DCI-HarqDisableSingleTB-r18 142

4.3.38.17 ntn-RRC-HarqDisableMultiTB-r18 142

4.3.38.18 ntn-OverriddenHarqDisableMultiTB-r18 142

4.3.38.19 ntn-DCI-HarqDisableMultiTB-r18 142

4.3.38.20 ntn-RRC-HarqDisableSingleTB-CE-ModeA-r18 142

4.3.38.21 ntn-RRC-HarqDisableSingleTB-CE-ModeB-r18 142

4.3.38.22 ntn-OverriddenHarqDisableSingleTB-CE-ModeB-r18 142

4.3.38.23 ntn-DCI-HarqDisableSingleTB-CE-ModeB-r18 142

4.3.38.24 ntn-RRC-HarqDisableMultiTB-CE-ModeA-r18 142

4.3.38.25 ntn-RRC-HarqDisableMultiTB-CE-ModeB-r18 143

4.3.38.26 ntn-OverriddenHarqDisableMultiTB-CE-ModeB-r18 143

4.3.38.27 ntn-DCI-HarqDisableMultiTB-CE-ModeB-r18 143

4.3.38.28 ntn-SemiStaticHarqDisableSPS-r18 143

4.3.38.29 ntn-UplinkHarq-ModeB-SingleTB-r18 143

4.3.38.30 ntn-HarqEnhScenarioSupport-r18 143

4.3.38.31 ntn-Triggered-GNSS-Fix-r18 143

4.3.38.32 ntn-Autonomous-GNSS-Fix-r18 144

4.3.38.33 ntn-UplinkTxExtension-r18 144

4.3.38.34 ntn-GNSS-EnhScenarioSupport-r18 144

4.3.38.35 ntn-UplinkHarq-ModeB-MultiTB-r18 144

4.3.38.36 eventD1-MeasReportTrigger-r18 144

4.3.38.37 eventD2-MeasReportTrigger-r18 144

4.3.38.38 satelliteInfoConfigDedicated-r18 145

4.3.38.39 ntn-MO-CB-Msg3-EDT-UP-r19 145

4.3.38.40 ntn-OCC-SingleTone-khz3dot75-r19 145

4.3.38.41 ntn-OCC-SingleTone-khz15-r19 145

4.3.38.42 ntn-OCC-EnhScenarioSupport-r19 145

4.3.38.43 ntn-SF-Mode-r19 145

5 Void 145

6 Optional features without UE radio access capability parameters 146

6.1 CSG features 146

6.2 PWS features 146

6.2.1 ETWS 146

6.2.2 CMAS 146

6.2.3 KPAS 146

6.2.4 EU-Alert 146

6.3 MBMS features 146

6.3.1 MBMS Service Continuity 146

6.3.2 MBMS reception with 256QAM 146

6.3.3 PBCH repetition in CAS 146

6.3.4 PDCCH AL16 for CAS in MBMS-dedicated cell 147

6.3.5 Semi-static CFI indication in MIB 147

6.3.6 MBMS reception using Receive Only Mode 147

6.4 Void 147

6.5 Positioning features 147

6.5.0 Void 147

6.5.1 Void 147

6.6 UE receiver features 147

6.6.1 MMSE with IRC receiver 147

6.6.2 MMSE with IRC receiver for PDSCH transmission mode 9 147

6.6.3 Single-user MIMO interference mitigation advanced receiver for UEs with 2 receiver antenna ports 147

6.6.4 Single-user MIMO interference mitigation advanced receiver for UEs with 4 receiver antenna ports 147

6.6.5 MMSE-IRC DL Control Channel interference mitigation receiver for UEs with 4 receiver antenna ports 148

6.7 RRC Connection 148

6.7.1 RRC Connection Reject with deprioritisation 148

6.7.2 RRC Connection Establishment Failure Temporary Qoffset 148

6.7.3 mo-VoiceCall establishment cause for mobile originating MMTEL video 148

6.7.4 mo-VoiceCall establishment cause for mobile originating MMTEL voice 148

6.7.5 RRC Connection Re-establishment for the Control Plane CIoT EPS Optimization 148

6.7.6 Void 148

6.8 Other features 148

6.8.1 System Information Block Type 16 148

6.8.2 QCI1 indication in Radio Link Failure Report 148

6.8.3 Enhanced random access power control 148

6.8.4 MO-EDT for Control Plane CIoT EPS Optimization 149

6.8.5 Void 149

6.8.6 Enhanced PHR 149

6.8.7 void 149

6.8.8 Resynchronization Signals 149

6.8.9 Measurement gaps for higher UE velocity 149

6.8.10 MT-EDT for Control Plane CIoT EPS Optimisation 149

6.8.11 MT-EDT for User Plane CIoT EPS Optimisation 149

6.8.12 Void 149

6.8.13 Reduced MIB/SIB1-BR acquisition time 149

6.8.14 High speed dedicated network features 149

6.8.15 Carrier specific NRSRP thresholds for NPRACH resource selection 149

6.8.16 Protection against improper reselection to GERAN/UTRAN 150

6.8.17 Inter-RAT cell reselection of an NR mobile IAB cell 150

6.8.18 Inter-RAT measurement on an NR NTN cell 150

6.8.19 Minimization of service interruption in EPS 150

6.9 Void 150

6.10 SON features 150

6.10.1 Radio Link Failure Report for inter-RAT MRO 150

6.10.2 Radio Link Failure Report for NB-IoT 150

6.10.3 Radio Link Failure Report for inter-RAT MRO NR 150

6.10.4 LTE RLF report for voice fallback in LTE 150

6.10.5 SCG failure information for EN-DC MRO 150

6.11 Mobility state features 151

6.11.1 Mobility history information storage 151

6.12 Void 151

6.13 Sidelink features 151

6.13.1 Sidelink Relay UE operation 151

6.13.2 Sidelink Remote UE operation 151

6.13.3 Sidelink discovery gap 151

6.13.4 Enhanced sidelink resource selection 151

6.13.5 Short-term time-scale TDM for in-device coexistence 151

6.14 DRX features 151

6.14.1 Extended DRX in RRC_IDLE 151

6.15 Load balancing features 151

6.15.1 Redistribution in RRC_IDLE 151

6.16 SC-PTM features 152

6.16.1 SC-PTM in Idle mode 152

6.16.2 Multiple TB scheduling for SC-PTM in Idle mode for NB-IoT 152

6.16.3 Multiple TB scheduling for SC-PTM in Idle mode for CE Mode A 152

6.16.4 Multiple TB scheduling for SC-PTM in Idle mode for CE Mode B 152

6.17 Idle mode measurements 152

6.17.1 Relaxed monitoring 152

6.17.2 DL channel quality reporting in Msg3 for the anchor carrier 152

6.17.3 Serving cell idle mode measurements reporting 152

6.17.4 NSSS-Based RRM measurements 152

6.17.5 NPBCH-Based RRM measurements 152

6.17.6 RRM measurements on non-anchor paging carriers 153

6.17.7 NRS presence on non-anchor paging carriers 153

6.17.8 DL channel quality reporting in Msg3 for non-anchor carrier 153

6.17.9 Assistance information for inter-RAT cell selection to/from NB-IoT 153

6.17.10 DL channel quality reporting in Msg3 153

6.17.11 Relaxed RRM measurements 153

6.17.12 RSS based measurement improvement 153

6.17.13 RSS based measurement in paging MPDCCH narrowband 153

6.18 E-UTRA/5GC features 154

6.18.1 Void 154

6.18.2 Void 154

6.18.3 RRC Connection Re-establishment for the Control Plane CIoT 5GS Optimisation 154

6.18.4 NB-IoT/5GC 154

6.18.5 MO-EDT for Control Plane CIoT 5GS Optimisation 154

6.18.6 AS RAI 154

6.18.7 Minimization of service interruption 154

6.19 IoT NTN Features 154

6.19.1 Cell reselection measurements triggering based on service time 154

6.19.2 Discontinuous coverage 154

6.19.3 Early RLF triggering based on service time 155

6.19.4 Neighbour cell measurements based on service start time of the neighbour cell 155

6.19.5 UE autonomous release based on service time 155

6.19.6 Cell reselection measurements triggering based on location for (quasi-)fixed cell 155

6.19.7 Cell reselection measurements triggering based on location for earth moving cell 155

6.19.8 GNSS measurements during inactive time 155

6.19.9 SystemInformationBlockType33(-NB) reception in a TN cell 155

6.19.10 Inband operation with NR NTN 155

6.19.11 MO-CB-Msg3-EDT for Control Plane CIoT EPS Optimization 155

6.19.12 MT-CB-Msg3-EDT for Control Plane CIoT EPS Optimization 156

6.19.13 MT-CB-Msg3-EDT for User Plane CIoT EPS Optimization 156

6.19.14 Geofencing of PWS message 156

6.19.15 Inter-RAT cell selection to NB-IoT NTN 156

6.19.16 Inter-RAT cell selection to NR NTN 156

7 Conditionally Mandatory features 156

7.1 Access control features 156

7.1.1 SSAC 156

7.1.2 CSFB Access Barring Control 156

7.1.3 Extended Access Barring 156

7.1.4 ACDC 156

7.1.5 EAB per RSRP 157

7.2 Emergency call features 157

7.2.1 IMS emergency call 157

7.3 MAC features 157

7.3.1 SR mask 157

7.3.2 Power Management Indicator in PHR 157

7.4 Inter-RAT Mobility features 157

7.4.1 High Priority CSFB redirection 157

7.4.2 GERAN A/Gb mode to E-UTRAN Inter RAT handover (PS Handover) 157

7.4.3 SRVCC to E-UTRAN from GERAN 157

7.4.4 Inter-RAT configuration for less than 5 MHz in SystemInformationBlockType24 157

7.5 Delay Tolerant Access Features 158

7.5.1 extendedWaitTime 158

7.6 RRC Connection 158

7.6.1 Void 158

7.7 Physical layer features 158

7.7.1 Different UL/ DL configuration for TDD inter-band carrier aggregation 158

7.7.2 Full duplex for TDD and FDD carrier aggregation 158

7.7.3 Simultaneous transmission of PUCCH and PUSCH across PUCCH groups 158

7.7.4 Simultaneous transmission of PUCCH in licensed spectrum and PUSCH in LAA SCells 158

7.8 Positioning features 158

7.8.1 OTDOA Inter-frequency RSTD measurement indication 158

7.8.2 Acquisition of positioning SI message with 80ms offset 158

7.9 Void 159

7.10 Other features 159

7.10.1 Logged MDT measurement suspension due to IDC interference 159

7.10.2 Support of extended reporting of WLAN measurements 159

7.10.3 wlan-ReportAnyWLAN-r14 159

7.10.4 wlan-PeriodicMeas-r14 159

7.10.5 TA Reporting during Initial Access for NTN 159

7.10.6 IoT NTN TDD mode 159

7.11 E-UTRA/5GC Parameters 160

7.11.1 Downlink SDAP header 160

Annex A (informative): Guideline on maximum number of DL PDCP SDUs per TTI 161

Annex B (informative): Change history 162

# Foreword

This Technical Specification has been produced by the 3rd Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

x the first digit:

## 1 presented to TSG for information;

## 2 presented to TSG for approval;

## 3 or greater indicates TSG approved document under change control.

y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.

z the third digit is incremented when editorial only changes have been incorporated in the document.

# 1 Scope

The present document defines the E-UTRA UE Radio Access Capability Parameters.

# 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or non specific.

- For a specific reference, subsequent revisions do not apply.

- For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1] 3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[2] 3GPP TS 36.323: "Evolved Universal Terrestrial Radio Access (E-UTRA) Packet Data Convergence Protocol (PDCP) specification".

[3] 3GPP TS 36.322: "Evolved Universal Terrestrial Radio Access (E-UTRA) Radio Link Control (RLC) specification".

[4] 3GPP TS 36.321: "Evolved Universal Terrestrial Radio Access (E-UTRA) Medium Access Control (MAC) specification".

[5] 3GPP TS 36.331: "Evolved Universal Terrestrial Radio Access (E-UTRA) Radio Resource Control (RRC) specification".

[6] 3GPP TS 36.101: "Evolved Universal Terrestrial Radio Access (E-UTRA) radio transmission and reception".

[7] IETF RFC 5795: "The RObust Header Compression (ROHC) Framework".

[8] IETF RFC 6846: "RObust Header Compression (ROHC): A Profile for TCP/IP (ROHC-TCP)".

[9] IETF RFC 3095: "RObust Header Compression (RoHC): Framework and four profiles: RTP, UDP, ESP and uncompressed".

[10] IETF RFC 3843: "RObust Header Compression (RoHC): A Compression Profile for IP".

[11] IETF RFC 4815: "RObust Header Compression (ROHC): Corrections and Clarifications to RFC 3095".

[12] IETF RFC 5225: "RObust Header Compression (ROHC) Version 2: Profiles for RTP, UDP, IP, ESP and UDP Lite".

[13] 3GPP TS 36.355: "Evolved Universal Terrestrial Radio Access (E-UTRA) LTE Positioning Protocol (LPP)".

[14] 3GPP TS 36.304: "Evolved Universal Terrestrial Radio Access (E-UTRA); UE Procedures in Idle Mode".

[15] 3GPP TS 37.320: "Universal Terrestrial Radio Access (UTRA) and Evolved Universal Terrestrial Radio Access (E-UTRA); Radio measurement collection for Minimization of Drive Tests (MDT); Overall description; Stage 2".

[16] 3GPP TS 36.133: "Evolved Universal Terrestrial Radio Access (E-UTRA); Requirements for support of radio resource management".

[17] 3GPP TS 36.211: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical Channels and Modulation".

[18] 3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access".

[19] 3GPP TS 23.216: "Single Radio Voice Call Continuity (SRVCC)".

[20] 3GPP TS 25.307: "Requirement on User Equipments (UEs) supporting a release-independent frequency band".

[21] 3GPP TS 24.312: "Access Network Discovery and Selection Function (ANDSF) Management Object (MO)".

[22] 3GPP TS 36.213: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer procedures".

[23] 3GPP TS 36.214: "Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer - Measurements".

[24] 3GPP TS 23.303: "Proximity-based services (ProSe); Stage 2".

[25] 3GPP TS 36.314: "Evolved Universal Terrestrial Radio Access (E-UTRA); Layer 2- Measurements".

[26] 3GPP TS 36.212: "Evolved Universal Terrestrial Radio Access (E-UTRA); Multiplexing and channel coding".

[27] 3GPP TS 36.307: "Evolved Universal Terrestrial Radio Access (E-UTRA); Requirements on User Equipments (UEs) supporting a release-independent frequency band".

[28] 3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for Evolved Packet System (EPS); Stage 3".

[29] 3GPP TS 23.285: "Technical Specification Group Services and System Aspects; Architecture enhancements for V2X services".

[30] 3GPP TS 36.300: "Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Universal Terrestrial Radio Access (E-UTRAN); Overall description; Stage 2".

[31] 3GPP TS 23.246: "Multimedia Broadcast/Multicast Service (MBMS); Architecture and functional description".

[32] 3GPP TS 38.306: "NR; UE Radio Access Capabilities".

[33] 3GPP TS 38.101-1: "NR User Equipment (UE) radio transmission and reception Part 1: Range 1 Standalone".

[34] 3GPP TS 38.101-2: "NR User Equipment (UE) radio transmission and reception Part 2: Range 2 Standalone".

[35] 3GPP TS 38.331: "NR; Radio Resource Control (RRC) protocol specification".

[36] 3GPP TS 38.215: "NR; Physical layer measurements".

[37] 3GPP TS 38.133: "NR; Requirements for support of radio resource management".

[38] 3GPP TS 37.340: "Evolved Universal Terrestrial Radio Access (E-UTRA) and NR; Multi-connectivity".

[39] 3GPP TS 24.501: "Non-Access-Stratum (NAS) protocol for 5G System (5GS); Stage 3".

[40] 3GPP TS 38.323: "NR; Packet Data Convergence Protocol (PDCP) specification".

[41] 3GPP TS 38.314: "NR; Layer 2 Measurements".

[42] 3GPP TS 23.287: "Technical Specification Group Services and System Aspects; Architecture enhancements for 5G System (5GS) to support Vehicle-to-Everything (V2X) services".

[43] 3GPP TS 36.102: "Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) radio transmission and reception for satellite access".

[44] 3GPP TS 38.101-3: "NR User Equipment (UE) radio transmission and reception Part 3: Range 1 and Range 2 Interworking operation with other radios".

[45] 3GPP TS 38.101-5: "NR User Equipment (UE) radio transmission and reception Part 5: Satellite access Radio Frequency (RF) and performance requirements".

# 3 Definitions, symbols and abbreviations

## 3.1 Definitions

For the purposes of the present document, the terms and definitions given in TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in TR 21.905 [1].

Fallback band combination: A band combination that would result from another band combination (parent band combination) by releasing at least one SCell or uplink configuration of SCell. A fallback band combination supports the same channel bandwidths for each carrier as its parent band combination. An intra-band non-contiguous band combination is not considered to be a fallback band combination of an intra-band contiguous band combination.

NB-IoT: NB-IoT allows access to network services via E-UTRA with a channel bandwidth limited to 200 kHz (corresponding to one PRB).

Primary Cell: The cell, operating on the primary frequency, in which the UE either performs the initial connection establishment procedure or initiates the connection re-establishment procedure, or the cell indicated as the primary cell in the handover procedure. In this specification, Primary Cell also refers to PSCell defined in TS 36.331 [5] unless explicitly stated otherwise.

Sidelink: UE to UE interface for sidelink communication, V2X sidelink communication and sidelink discovery. The Sidelink corresponds to the PC5 interface as defined in TS 23.303 [24].

Sidelink communication: AS functionality enabling ProSe Direct Communication as defined in TS 23.303 [24], between two or more nearby UEs, using E-UTRA technology but not traversing any network node. In this version, the terminology "sidelink communication" without "V2X" prefix only concerns PS unless specifically stated otherwise.

Sidelink discovery: AS functionality enabling ProSe Direct Discovery as defined in TS 23.303 [24], using E-UTRA technology but not traversing any network node.

V2X sidelink communication: AS functionality enabling V2X Communication as defined in TS 23.285 [29], between nearby UEs, using E-UTRA technology but not traversing any network node.

## 3.2 Symbols

For the purposes of the present document, the following symbols apply:

<symbol> <Explanation>

## 3.3 Abbreviations

For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1].

1xRTT CDMA2000 1x Radio Transmission Technology

ACK Acknowledgement

ACDC Application specific Congestion control for Data Communication

ANDSF Access Network Discovery and Selection Function

ANR Automatic Neighbour Relation

BCCH Broadcast Control Channel

CAS Cell Acquisition Subframes

CFI Control Format Indicator

CG Cell Group

CRS Cell-specific Reference Signal

CSG Closed Subscriber Group

CSI Channel State Information

DC Dual Connectivity

DCI Downlink Control Information

DL-SCH Downlink Shared Channel

EHC Ethernet Header Compression

E-UTRA Evolved Universal Terrestrial Radio Access

E-UTRAN Evolved Universal Terrestrial Radio Access Network

FDD Frequency Division Duplex

GERAN GSM/EDGE Radio Access Network

HARQ Hybrid Automatic Repeat Request

HRPD High Rate Packet Data

HSDN High Speed Dedicated Network

IRC Interference Rejection Combining

MAC Medium Access Control

MMSE Minimum Mean Squared Error

MO-EDT Mobile Originated Early Data Transmission

MRO Mobility Robustness Optimisation

MT-EDT Mobile Terminated Early Data Transmission

MTSI Multimedia Telephony Service for IMS

MUST MultiUser Superposition Transmission

NAICS Network Assisted Interference Cancellation/Suppression

NB-IoT Narrow Band Internet of Things

NTN Non-Terrestrial Network

OS OFDM Symbol

PCell Primary Cell

PDCCH Physical Downlink Control Channel

PDCP Packet Data Convergence Protocol

PDSCH Physical Downlink Shared Channel

PHR Power Headroom Reporting

ProSe Proximity-based Services

PUCCH Physical Uplink Control Channel

PUR Preconfigured Uplink Resource

PUSCH Physical Uplink Shared Channel

QoE Quality of Experience

RACH Random Access CHannel

RAI Release Assistance Indication

RAT Radio Access Technology

RLC Radio Link Control

RLF Radio Link Failure

ROHC RObust Header Compression

RRC Radio Resource Control

SC-PTM Single Cell Point to Multipoint

SCC Secondary Component Carrier

SCell Secondary Cell

SI System Information

SL Sidelink

SL-DCH Sidelink Discovery CHannel

SL-SCH Sidelink Shared CHannel

SON Self Organizing Networks

SPT Short Processing Time

SR Scheduling Request

SSAC Service Specific Access Control

SSTD SFN and Subframe Timing Difference

STTI Short TTI

TDD Time Division Duplex

TTI Transmission Time Interval

UCI Uplink Control Information

UDC Uplink Data Compression

UE User Equipment

UL-SCH Uplink Shared Channel

UMTS Universal Mobile Telecommunications System

UTRA UMTS Terrestrial Radio Access

V2X Vehicle-to-Everything

WLAN Wireless Local Area Network

# 4 UE radio access capability parameters

The following clauses define the UE radio access capability parameters and minimum capabilities for MBMS capable UE. Only parameters for which there is the possibility for UEs to signal different values are considered as UE radio access capability parameters. Therefore, mandatory features without capability parameters that are the same for all UEs are not listed here. Also capabilities which are optional or conditionally mandatory for UEs to implement but do not have UE radio access capability parameter are listed in this specification.

E-UTRAN needs to respect the signalled UE radio access capability parameters when configuring the UE and when scheduling the UE.

All parameters shown in italics are signalled and correspond to a field defined in TS 36.331 [5].

For optional features, the UE radio access capability parameter indicates whether the feature has been implemented and successfully tested. For mandatory features with the UE radio access capability parameter, the parameter indicates whether the feature has been successfully tested.

The mandatory features required to be supported by a UE are the same for all UE categories unless explicitly specified elsewhere in the specifications.

Unless otherwise stated, the requirements on the maximum number of transport block bits are applicable for a TTI length of 1 ms. For other TTI lengths, the requirements shall be scaled according to clause 7.1.7 or 11.1 in TS 36.213 [22] in order to get the corresponding requirement.

The following UE radio access capability parameters specified in clause 4 are applicable in NB-IoT:

- ue-Category-NB in NB-IoT (clause 4.1C)

- supportedROHC-Profiles-r13 (clause 4.3.1.1A)

- maxNumberROHC-ContextSessions-r13 (clause 4.3.1.2A)

- rlc-UM-r15 (clause 4.3.2.5)

- multiTone-r13 (clause 4.3.4.55)

- multiCarrier-r13 (clause 4.3.4.56)

- twoHARQ-Processes-r14 (clause 4.3.4.62)

- multiCarrier-NPRACH-r14 (clause 4.3.4.75)

- multiCarrierPaging-r14 (clause 4.3.4.76)

- interferenceRandomisation-r14 (clause 4.3.4.80)

- wakeUpSignal-r15 (clause 4.3.4.113)

- wakeUpSignalMinGap-eDRX-r15 (clause 4.3.4.114)

- mixedOperationMode-r15 (clause 4.3.4.115)

- sr-WithHARQ-ACK-r15 (clause 4.3.4.117)

- sr-WithoutHARQ-ACK-r15 (clause 4.3.4.118)

- nprach-Format2-r15 (clause 4.3.4.119)

- multiCarrierPagingTDD-r15 (clause 4.3.4.134)

- additionalTransmissionSIB1-r15 (clause 4.3.4.137)

- npusch-3dot75kHz-SCS-TDD-r15 (clause 4.3.4.177)

- npusch-MultiTB-r16 (clause 4.3.4.182)

- npdsch-MultiTB-r16 (clause 4.3.4.183)

- npusch-MultiTB-Interleaving-r16 (clause 4.3.4.192)

- npdsch-MultiTB-Interleaving-r16 (clause 4.3.4.193)

- multiTB-HARQ-AckBundling-r16 (clause 4.3.4.194)

- groupWakeUpSignal-r16 (clause 4.3.4.195)

- groupWakeUpSignalAlternation-r16 (clause 4.3.4.196)

- subframeResourceResvUL-r16 (clause 4.3.4.197)

- subframeResourceResvDL-r16 (clause 4.3.4.198)

- slotSymbolResourceResvUL-r16 (clause 4.3.4.199)

- slotSymbolResourceResvDL-r16 (clause 4.3.4.200)

- npdsch-16QAM-r17 (clause 4.3.4.222)

- npusch-16QAM-r17 (clause 4.3.4.223)

- supportedBandList-r13 (clause 4.3.5.1A)

- multiNS-Pmax-r13 (clause 4.3.5.16A)

- powerClassNB-20dBm-r13 (clause 4.3.5.1A.1)

- powerClassNB-14dBm-r14 (clause 4.3.5.1A.2)

- powerBoostingNB-r19 (clause 4.3.5.1A.3)

- dl-ChannelQualityReporting-r16 (clause 4.3.6.37)

- connModeMeasIntraFreq-r17 (clause 4.3.6.49)

- connModeMeasInterFreq-r17 (clause 4.3.6.50)

- accessStratumRelease-r13 (clause 4.3.8.1A)

- multipleDRB-r13 (clause 4.3.8.5)

- earlyData-UP-r15 (clause 4.3.8.7)

- earlySecurityReactivation-r16 (clause 4.3.8.11)

- coverageBasedPaging-r17 (clause 4.3.8.16)

- pws-Support-r19 (clause 4.3.8.17)

- anr-Report-r16 (clause 4.3.12.2)

- rach-Report-r16 (clause 4.3.12.3)

- locationInfo-r16 (clause 4.3.12.5)

- ntn-Redirection-r19 (clause 4.3.15.26)

- logicalChannelSR-ProhibitTimer (clause 4.3.19.2)

- dataInactMon-r14 (clause 4.3.19.9)

- rai-Support-r14 (clause 4.3.19.10)

- earlyContentionResolution-r14 (clause 4.3.19.14)

- sr-SPS-BSR-r15 (clause 4.3.19.15)

- rai-SupportEnh-r16 (clause 4.3.19.22)

- earlyData-UP-5GC-r16 (clause 4.3.36.9)

- pur-CP-EPC-r16 (clause 4.3.37.1)

- pur-UP-EPC-r16 (clause 4.3.37.2)

- pur-CP-5GC-r16 (clause 4.3.37.3)

- pur-UP-5GC-r16 (clause 4.3.37.4)

- pur-CP-L1Ack-r16 (clause 4.3.37.5)

- pur-NRSRP-Validation-r16 (clause 4.3.37.6)

- ntn-Connectivity-EPC-r17 (clause 4.3.38.1)

- ntn-TA-Report-r17 (clause 4.3.38.2)

- ntn-PUR-TimerDelay-r17 (clause 4.3.38.3)

- ntn-OffsetTimingEnh-r17 (clause 4.3.38.4)

- ntn-ScenarioSupport-r17 (clause 4.3.38.5)

- ntn-SegmentedPrecompensationGaps-r17 (clause 4.3.38.6)

- ntn-LocationBasedMeasTrigger-EFC-r18 (clause 4.3.38.11)

- ntn-LocationBasedMeasTrigger-EMC-r18 (clause 4.3.38.12)

- ntn-TimeBasedMeasTrigger-r18 (clause 4.3.38.13)

- ntn-RRC-HarqDisableSingleTB-r18 (clause 4.3.38.14)

- ntn-OverriddenHarqDisableSingleTB-r18 (clause 4.3.38.15)

- ntn-DCI-HarqDisableSingleTB-r18 (clause 4.3.38.16)

- ntn-RRC-HarqDisableMultiTB-r18 (clause 4.3.38.17)

- ntn-OverriddenHarqDisableMultiTB-r18 (clause 4.3.38.18)

- ntn-DCI-HarqDisableMultiTB-r18 (clause 4.3.38.19)

- ntn-UplinkHarq-ModeB-SingleTB-r18 (clause 4.3.38.29)

- ntn-HarqEnhScenarioSupport-r18 (clause 4.3.38.30)

- ntn-Triggered-GNSS-Fix-r18 (clause 4.3.38.31)

- ntn-Autonomous-GNSS-Fix-r18 (clause 4.3.38.32)

- ntn-UplinkTxExtension-r18 (clause 4.3.38.33)

- ntn-GNSS-EnhScenarioSupport-r18 (clause 4.3.38.34)

- ntn-UplinkHarq-ModeB-MultiTB-r18 (clause 4.3.38.35)

- ntn-MO-CB-Msg3-EDT-UP-r19 (clause 4.3.38.39)

- ntn-OCC-SingleTone-khz3dot75-r19 (clause 4.3.38.40)

- ntn-OCC-SingleTone-khz15-r19 (clause 4.3.38.41)

- ntn-OCC-EnhScenarioSupport-r19 (clause 4.3.38.42)

- ntn-SF-Mode-r19 (clause 4.3.38.43)

The UE radio access capabilities specified in clause 4 are not applicable in NB-IoT, unless they are listed above.

The following optional features without UE radio access capability parameters specified in clause 6 are applicable in NB-IoT:

- RRC Connection Re-establishment for the Control Plane CIoT EPS Optimization (clause 6.7.5)

- System Information Block Type 16 (clause 6.8.1)

- Enhanced random access power control (clause 6.8.3)

- MT-EDT for Control Plane CIoT EPS Optimisation (clause 6.8.10)

- MT-EDT for User Plane CIoT EPS Optimisation (clause 6.8.11)

- EDT for Control Plane CIoT EPS Optimization (clause 6.8.4)

- Enhanced PHR (clause 6.8.6)

- Carrier specific NRSRP thresholds for NPRACH resource selection (clause 6.8.15)

- Radio Link Failure Report for NB-IoT (clause 6.10.2)

- SC-PTM in Idle mode (clause 6.16.1)

- Multiple TB scheduling for SC-PTM in Idle mode for NB-IoT (clause 6.16.2)

- Relaxed monitoring (clause 6.17.1)

- DL channel quality reporting in Msg3 for the anchor carrier (clause 6.17.2)

- Serving cell idle mode measurements reporting (clause 6.17.3)

- NSSS-Based RRM measurements (clause 6.17.4)

- NPBCH-Based RRM measurements (clause 6.17.5)

- RRM measurements on non-anchor paging carriers (clause 6.17.6)

- NRS presence on non-anchor paging carriers (clause 6.17.7)

- DL channel quality reporting in Msg3 for non-anchor carrier (clause 6.17.8)

- Assistance information for inter-RAT cell selection to/from NB-IoT (clause 6.17.9)

- RRC Connection Re-establishment for the Control Plane CIoT 5GS Optimisation (clause 6.18.3)

- NB-IoT/5GC (clause 6.18.4)

- MO-EDT for Control Plane CIoT 5GS Optimisation (clause 6.18.5)

- AS RAI (clause 6.18.6)

- Cell reselection measurements triggering based on service time (clause 6.19.1)

- Discontinuous coverage (clause 6.19.2).

- Early RLF triggering based on service time (clause 6.19.3).

- Neighbour cell measurements based on service start time of the neighbour cell (clause 6.19.4).

- UE autonomous release based on service time (clause 6.19.5).

- Cell reselection measurements triggering based on location for (quasi-)fixed cell (clause 6.19.6).

- Cell reselection measurements triggering based on location for earth moving cell (clause 6.19.7).

- GNSS measurements during inactive time (clause 6.19.8).

- SystemInformationBlockType33(-NB) reception in a TN cell (clause 6.19.9).

- Inband operation with NR NTN (6.19.10).

- MO-CB-Msg3-EDT for Control Plane CIoT EPS Optimization (clause 6.19.11).

- MT-CB-Msg3-EDT for Control Plane CIoT EPS Optimization (clause 6.19.12).

- MT-CB-Msg3-EDT for User Plane CIoT EPS Optimization (clause 6.19.13).

- Geofencing of PWS message (6.19.14).

- Inter-RAT cell selection to NB-IoT NTN (clause 6.19.15).

The optional features without UE radio access capability parameters specified in clause 6 are not applicable in NB-IoT, unless they are listed above.

## 4.1 ue-Category

The field ue-Category defines a combined uplink and downlink capability. The parameters set by the UE Category are defined in clause 4.2. Tables 4.1-1 and 4.1-2 define the downlink and, respectively, uplink physical layer parameter values for each UE Category. A UE indicating category 6 or 7 shall also indicate category 4. A UE indicating category 8 shall also indicate category 5. A UE indicating category 9 shall also indicate category 6 and 4. A UE indicating category 10 shall also indicate category 7 and 4. A UE indicating category 11 shall also indicate category 9, 6 and 4. A UE indicating category 12 shall also indicate category 10, 7 and 4. Table 4.1-4 defines the minimum capability for the maximum number of bits of a MCH transport block received within a TTI for an MBMS capable UE capable of reception via MBSFN.

Table 4.1-1: Downlink physical layer parameter values set by the field ue-Category

| UE Category | Maximum number of DL-SCH transport block bits received within a TTI (Note 1) | Maximum number of bits of a DL-SCH transport block received within a TTI | Total number of soft channel bits | Maximum number of supported layers for spatial multiplexing in DL |
| --- | --- | --- | --- | --- |
| Category 1 | 10296 | 10296 | 250368 | 1 |
| Category 2 | 51024 | 51024 | 1237248 | 2 |
| Category 3 | 102048 | 75376 | 1237248 | 2 |
| Category 4 | 150752 | 75376 | 1827072 | 2 |
| Category 5 | 299552 | 149776 | 3667200 | 4 |
| Category 6 | 301504 | 149776 (4 layers, 64QAM)75376 (2 layers, 64QAM) | 3654144 | 2 or 4 |
| Category 7 | 301504 | 149776 (4 layers, 64QAM)75376 (2 layers, 64QAM) | 3654144 | 2 or 4 |
| Category 8 | 2998560 | 299856 | 35982720 | 8 |
| Category 9 | 452256 | 149776 (4 layers, 64QAM)75376 (2 layers, 64QAM) | 5481216 | 2 or 4 |
| Category 10 | 452256 | 149776 (4 layers, 64QAM)75376 (2 layers, 64QAM) | 5481216 | 2 or 4 |
| Category 11 | 603008 | 149776 (4 layers, 64QAM)195816 (4 layers, 256QAM)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM) | 7308288 | 2 or 4 |
| Category 12 | 603008 | 149776 (4 layers, 64QAM)195816 (4 layers, 256QAM)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM) | 7308288 | 2 or 4 |
| NOTE 1: In carrier aggregation operation, the DL-SCH processing capability can be shared by the UE with that of MCH received from a serving cell. If the total eNB scheduling for DL-SCH and an MCH in one serving cell at a given TTI is larger than the defined processing capability, the prioritization between DL-SCH and MCH is left up to UE implementation. |  |  |  |  |

Table 4.1-2: Uplink physical layer parameter values set by the field ue-Category

| UE Category | Maximum number of UL-SCH transport block bits transmitted within a TTI | Maximum number of bits of an UL-SCH transport block transmitted within a TTI | Support for 64QAM in UL |
| --- | --- | --- | --- |
| Category 1 | 5160 | 5160 | No |
| Category 2 | 25456 | 25456 | No |
| Category 3 | 51024 | 51024 | No |
| Category 4 | 51024 | 51024 | No |
| Category 5 | 75376 | 75376 | Yes |
| Category 6 | 51024 | 51024 | No |
| Category 7 | 102048 | 51024 | No |
| Category 8 | 1497760 | 149776 | Yes |
| Category 9 | 51024 | 51024 | No |
| Category 10 | 102048 | 51024 | No |
| Category 11 | 51024 | 51024 | No |
| Category 12 | 102048 | 51024 | No |

Table 4.1-3: Total layer 2 buffer sizes set by the field ue-Category

| UE Category | Total layer 2 buffer size [bytes] | With support for split bearers |
| --- | --- | --- |
| Category 1 | 150 000 | 230 000 |
| Category 2 | 700 000 | 1 100 000 |
| Category 3 | 1 400 000 | 2 300 000 |
| Category 4 | 1 900 000 | 3 100 000 |
| Category 5 | 3 500 000 | 5 900 000 |
| Category 6 | 3 300 000 | 5 800 000 |
| Category 7 | 3 800 000 | 6 200 000 |
| Category 8 | 42 200 000 | 61 600 000 |
| Category 9 | 4 800 000 | 7 200 000 |
| Category 10 | 5 200 000 | 7 600 000 |
| Category 11 | 6 200 000 | 11 000 000 |
| Category 12 | 6 700 000 | 11 500 000 |

Table 4.1-4: Maximum number of bits of a MCH transport block received within a TTI set by the field ue-Category for an MBMS capable UE capable of reception via MBSFN

| UE Category | Maximum number of bits of a MCH transport block received within a TTI |
| --- | --- |
| Category 1 | 10296 |
| Category 2 | 51024 |
| Category 3 | 75376 |
| Category 4 | 75376 |
| Category 5 | 75376 |
| Category 6 | 75376 |
| Category 7 | 75376 |
| Category 8 | 75376 |
| Category 9 | 75376 |
| Category 10 | 75376 |
| Category 11 | 75376 (64QAM)97896 (256QAM) |
| Category 12 | 75376 (64QAM)97896 (256QAM) |

Table 4.1-5: Half-duplex FDD operation type set by the field ue-Category for a half-duplex FDD capable UE

| UE Category | Half-duplex FDD operation type |
| --- | --- |
| Category 1 | Type A |
| Category 2 | Type A |
| Category 3 | Type A |
| Category 4 | Type A |
| Category 5 | Type A |
| Category 6 | Type A |
| Category 7 | Type A |
| Category 8 | Type A |
| Category 9 | Type A |
| Category 10 | Type A |
| Category 11 | Type A |
| Category 12 | Type A |

## 4.1A ue-CategoryDL and ue-CategoryUL

The fields ue-CategoryDL and ue-CategoryUL define downlink/uplink capability respectively. The parameters set by the UE DL/UL Categories are defined in clause 4.2. Tables 4.1A-1 and 4.1A-2 define the downlink and, respectively, uplink physical layer parameter values for each UE DL/UL Category. Table 4.1A-4 defines the minimum capability for the maximum number of bits of a MCH transport block received within a TTI for an MBMS capable UE capable of reception via MBSFN. Table 4.1A-6 defines the only combinations for UE UL and DL Categories that are allowed to be signalled with ue-CategoryDL and ue-CategoryUL. Table 4.1A-6 also defines which UE Categories a UE shall indicate in addition to the combinations for UE UL and DL Categories. For a BL UE, Table 4.1A-7 defines the only combinations for UE UL and DL Categories that are allowed to be signalled with ue-CategoryDL and ue-CategoryUL, and which UE Categories a UE shall indicate in addition to the combinations for UE UL and DL Categories. A UE indicating DL category 13 may indicate category 9 or 10 in ue-Category-v1170. A UE indicating Category M2 shall also indicate Category M1.

Table 4.1A-1: Downlink physical layer parameter values set by the field ue-CategoryDL

| UE DL Category | Maximum number of DL-SCH transport block bits received within a TTI (Note 1) | Maximum number of bits of a DL-SCH transport block received within a TTI | Total number of soft channel bits | Maximum number of supported layers for spatial multiplexing in DL |
| --- | --- | --- | --- | --- |
| DL Category M1 (Note 4) | 1000 or 1736 | 1000 or 1736 | 25344 or 43008 | 1 |
| DL Category M2 | 4008 | 4008 | 73152 | 1 |
| DL Category 0 (Note 2) | 1000 | 1000 | 25344 | 1 |
| DL Category 1bis | 10296 | 10296 | 250368 | 1 |
| DL Category 4 | 150752 | 75376 | 1827072 | 2 |
| DL Category 6 | 301504 | 149776 (4 layers, 64QAM)75376 (2 layers, 64QAM) | 3654144 | 2 or 4 |
| DL Category 7 | 301504 | 149776 (4 layers, 64QAM)75376 (2 layers, 64QAM) | 3654144 | 2 or 4 |
| DL Category 9 | 452256 | 149776 (4 layers, 64QAM)75376 (2 layers, 64QAM) | 5481216 | 2 or 4 |
| DL Category 10 | 452256 | 149776 (4 layers, 64QAM)75376 (2 layers, 64QAM) | 5481216 | 2 or 4 |
| DL Category 11 | 603008 | 149776 (4 layers, 64QAM)195816 (4 layers, 256QAM)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM) | 7308288 | 2 or 4 |
| DL Category 12 | 603008 | 149776 (4 layers, 64QAM)195816 (4 layers, 256QAM)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM) | 7308288 | 2 or 4 |
| DL Category 13 | 391632 | 195816 (4 layers, 256QAM)97896 (2 layers, 256QAM) | 3654144 | 2 or 4 |
| DL Category 14 | 3916560 | 391656 (8 layers, 256QAM) | 47431680 | 8 |
| DL Category 15 | 749856-807744 (Note 3) | 149776 (4 layers, 64QAM)195816 (4 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)201936 (4 layers, 256QAM, if alternativeTBS-Index-r14 is supported)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)100752 (2 layers, 256QAM, if alternativeTBS-Index-r14 is supported) | 9744384 | 2 or 4 |
| DL Category 16 | 978960 -1051360 (Note 3) | 149776 (4 layers, 64QAM)195816 (4 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)201936 (4 layers, 256QAM, if alternativeTBS-Index-r14 is supported)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)100752 (2 layers, 256QAM, if alternativeTBS-Index-r14 is supported) | 12789504 | 2 or 4 |
| DL Category 17 | 25065984 | 391656 (8 layers, 256QAM) | 303562752 | 8 |
| DL Category 18 | 1174752-1211616 (Note 3) | 299856 (8 layers, 64QAM)391656 (8 layers, 256QAM)149776 (4 layers, 64QAM)195816 (4 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)201936 (4 layers, 256QAM, if alternativeTBS-Index-r14 is supported)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)100752 (2 layers, 256QAM, if alternativeTBS-Index-r14 is supported) | 14616576 | 2 or 4 or 8 |
| DL Category 19 | 1566336 -1658272 (Note 3) | 299856 (8 layers, 64QAM)391656 (8 layers, 256QAM)149776 (4 layers, 64QAM)195816 (4 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)201936 (4 layers, 256QAM, if alternativeTBS-Index-r14 is supported)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)100752 (2 layers, 256QAM, if alternativeTBS-Index-r14 is supported) | 19488768 | 2 or 4 or 8 |
| DL Category 20 | 1948064 - 2019360 (Note 3) | 299856 (8 layers, 64QAM)391656 (8 layers, 256QAM),502624 (8 layers, 1024QAM)149776 (4 layers, 64QAM)195816 (4 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)201936 (4 layers, 256QAM, if alternativeTBS-Index-r14 is supported)251640 (4 layers, 1024QAM)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)100752 (2 layers, 256QAM, if alternativeTBS-Index-r14 is supported)125808 (2 layers, 1024QAM) | 24360960 | 2 or 4 or 8 |
| DL Category 21 | 1348960 - 1413120 (Note 3) | 149776 (4 layers, 64QAM)195816 (4 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)201936 (4 layers, 256QAM, if alternativeTBS-Index-r14 is supported)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)100752 (2 layers, 256QAM, if alternativeTBS-Index-r14 is supported) | 17052672 | 2 or 4 |
| DL Category 22 | 2349504 – 2562784 | 299856 (8 layers, 64QAM)391656 (8 layers, 256QAM)502624 (8 layers, 1024QAM)149776 (4 layers, 64QAM)195816 (4 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)201936 (4 layers, 256QAM, if alternativeTBS-Index-r14 is supported)251640 (4 layers, 1024QAM)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)100752 (2 layers, 256QAM, if alternativeTBS-Index-r14 is supported)125808 (2 layers, 1024QAM) | 29233152 | 2 or 4 or 8 |
| DL Category 23 | 2695968 – 2869920 | 299856 (8 layers, 64QAM)391656 (8 layers, 256QAM)502624 (8 layers, 1024QAM)149776 (4 layers, 64QAM)195816 (4 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)201936 (4 layers, 256QAM, if alternativeTBS-Index-r14 is supported)251640 (4 layers, 1024QAM)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)100752 (2 layers, 256QAM, if alternativeTBS-Index-r14 is supported)125808 (2 layers, 1024QAM) | 34105344 | 2 or 4 or 8 |
| DL Category 24 | 2936880 – 3028608 | 299856 (8 layers, 64QAM)391656 (8 layers, 256QAM)502624 (8 layers, 1024QAM)149776 (4 layers, 64QAM)195816 (4 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)201936 (4 layers, 256QAM, if alternativeTBS-Index-r14 is supported)251640 (4 layers, 1024QAM)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)100752 (2 layers, 256QAM, if alternativeTBS-Index-r14 is supported)125808 (2 layers, 1024QAM) | 36541440 | 2 or 4 or 8 |
| DL Category 25 | 3132672 – 3316544 | 299856 (8 layers, 64QAM)391656 (8 layers, 256QAM)502624 (8 layers, 1024QAM)149776 (4 layers, 64QAM)195816 (4 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)201936 (4 layers, 256QAM, if alternativeTBS-Index-r14 is supported)251640 (4 layers, 1024QAM)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)100752 (2 layers, 256QAM, if alternativeTBS-Index-r14 is supported)125808 (2 layers, 1024QAM) | 38977536 | 2 or 4 or 8 |
| DL Category 26 | 3422400– 3531888 | 299856 (8 layers, 64QAM)391656 (8 layers, 256QAM)502624 (8 layers, 1024QAM)149776 (4 layers, 64QAM)195816 (4 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)201936 (4 layers, 256QAM, if alternativeTBS-Index-r14 is supported)251640 (4 layers, 1024QAM)75376 (2 layers, 64QAM)97896 (2 layers, 256QAM, if alternativeTBS-Index-r14 is not supported)100752 (2 layers, 256QAM, if alternativeTBS-Index-r14 is supported)125808 (2 layers, 1024QAM) | 42631680 | 2 or 4 or 8 |
| NOTE 1: In carrier aggregation operation, the DL-SCH processing capability can be shared by the UE with that of MCH received from a serving cell. If the total eNB scheduling for DL-SCH and an MCH in one serving cell at a given TTI is larger than the defined processing capability, the prioritization between DL-SCH and MCH is left up to UE implementation.NOTE 2: Within one TTI, a UE indicating category 0 shall be able to receive up to 1000 bits for a transport block associated with C-RNTI/Semi-Persistent Scheduling C-RNTI/P-RNTI/SI-RNTI/RA-RNTI and up to 2216 bits for another transport block associated with P-RNTI/SI-RNTI/RA-RNTI.NOTE 3: The UE indicating category x shall reach the value within the defined range indicated by "Maximum number of DL-SCH transport block bits received within a TTI" of category x. The UE shall determine the required value within the defined range indicated by "Maximum number of DL-SCH transport block bits received within a TTI" of the corresponding category, based on its capabilities (i.e. CA band combination, MIMO, Modulation scheme). If the UE capability of CA band combination, MIMO and modulation scheme supported can exceed the upper limit of the defined range, the UE shall support the maximum value of the defined range indicated by "Maximum number of DL-SCH transport block bits received within a TTI" of the corresponding category.NOTE 4: The UE supports "Maximum number of DL-SCH transport block bits received within a TTI" and "Maximum number of bits of a DL-SCH transport block received within a TTI" of 1736 bits and "Total number of soft channel bits" of 43008 bits if the UE indicates support of ce-PDSCH-MaxTBS-r17. Otherwise the UE supports "Maximum number of DL-SCH transport block bits received within a TTI" and "Maximum number of bits of a DL-SCH transport block received within a TTI" of 1000 bits and "Total number of soft channel bits" of 25344 bits. |  |  |  |  |

Table 4.1A-2: Uplink physical layer parameter values set by the field ue-CategoryUL

| UE UL Category | Maximum number of UL-SCH transport block bits transmitted within a TTI | Maximum number of bits of an UL-SCH transport block transmitted within a TTI | Support for 64QAM in UL | Support for 256QAM in UL |
| --- | --- | --- | --- | --- |
| UL Category M1(Note 1) | 1000 or 2984 | 1000 or 2984 | No | No |
| UL Category M2 | 6968 | 6968 | No | No |
| UL Category 0 | 1000 | 1000 | No | No |
| UL Category 1bis | 5160 | 5160 | No | No |
| UL Category 3 | 51024 | 51024 | No | No |
| UL Category 5 | 75376 | 75376 | Yes | No |
| UL Category 7 | 102048 | 51024 | No | No |
| UL Category 8 | 1497760 | 149776 | Yes | No |
| UL Category 13 | 150752 | 75376 | Yes | No |
| UL Category 14 | 9585664 | 149776 | Yes | No |
| UL Category 15 | 226128 | 75376 | Yes | No |
| UL Category 16 | 105528 | 105528 | Yes | Yes |
| UL Category 17 | 2119360 | 211936 | Yes | Yes |
| UL Category 18 | 211056 | 105528 | Yes | Yes |
| UL Category 19 | 13563904 | 211936 | Yes | Yes |
| UL Category 20 | 316584 | 105528 | Yes | Yes |
| UL Category 21 | 301504 | 75376 | Yes | No |
| UL Category 22 | 422112 | 105528 | Yes | Yes |
| UL Category 23 | 527640 | 105528 | Yes | Yes |
| UL Category 24 | 633168 | 105528 | Yes | Yes |
| UL Category 25 | 738696 | 105528 | Yes | Yes |
| UL Category 26 | 844224 | 105528 | Yes | Yes |
| NOTE 1: The UE supports "Maximum number of UL-SCH transport block bits transmitted within a TTI" and "Maximum number of bits of an UL-SCH transport block transmitted within a TTI" of 2984 bits if the UE indicates support of ce-PUSCH-NB-MaxTBS-r14. Otherwise the UE supports 1000 bits. |  |  |  |  |

Table 4.1A-3: Total layer 2 buffer sizes set by the fields ue-CategoryDL and ue-CategoryUL

| UE DL Category | UE UL Category | Total layer 2 buffer size [bytes] | With support for split bearers [bytes] |
| --- | --- | --- | --- |
| DL Category M1 (Note 1) | UL Category M1 | 20 000 or 40 000 | N/A |
| DL Category M2 | UL Category M2 | 100 000 | N/A |
| DL Category 0 | UL Category 0 | 20 000 | N/A |
| DL Category 1bis | UL Category 1bis | 150 000 | 230 000 |
| DL Category 4 | UL Category 5 | 2 200 000 | 3 300 000 |
| DL Category 6 | UL Category 5 | 3 500 000 | 6 000 000 |
| DL Category 6 | UL Category 16 | 3 800 000 | 6 300 000 |
| DL Category 7 | UL Category 13 | 4 200 000 | 6 700 000 |
| DL Category 7 | UL Category 18 | 4 800 000 | 7 300 000 |
| DL Category 9 | UL Category 5 | 5 000 000 | 7 400 000 |
| DL Category 9 | UL Category 16 | 5 200 000 | 7 700 000 |
| DL Category 10 | UL Category 13 | 5 700 000 | 8 100 000 |
| DL Category 10 | UL Category 18 | 6 200 000 | 8 700 000 |
| DL Category 11 | UL Category 5 | 6 400 000 | 11 300 000 |
| DL Category 11 | UL Category 16 | 6 600 000 | 11 500 000 |
| DL Category 12 | UL Category 13 | 7 100 000 | 12 000 000 |
| DL Category 12 | UL Category 15 | 7 700 000 | 12 600 000 |
| DL Category 12 | UL Category 18 | 7 600 000 | 12 500 000 |
| DL Category 12 | UL Category 20 | 8 600 000 | 13 500 000 |
| DL Category 13 | UL Category 3 | 4 200 000 | 7 300 000 |
| DL Category 13 | UL Category 5 | 4 400 000 | 7 600 000 |
| DL Category 13 | UL Category 7 | 4 700 000 | 7 800 000 |
| DL Category 13 | UL Category 13 | 5 100 000 | 8 300 000 |
| DL Category 13 | UL Category 16 | 4 700 000 | 7 800 000 |
| DL Category 13 | UL Category 18 | 5 700 000 | 8 800 000 |
| DL Category 14 | UL Category 8 | 50 800 000 | 76 200 000 |
| DL Category 14 | UL Category 17 | 56 600 000 | 82 000 000 |
| DL Category 15 | UL Category 3 | 8 000 000 | 13 000 000 |
| DL Category 15 | UL Category 5 | 8 200 000 | 13 400 000 |
| DL Category 15 | UL Category 7 | 8 500 000 | 13 600 000 |
| DL Category 15 | UL Category 13 | 8 900 000 | 14 100 000 |
| DL Category 15 | UL Category 16 | 8 500 000 | 13 700 000 |
| DL Category 15 | UL Category 18 | 9 500 000 | 14 700 000 |
| DL Category 16 | UL Category 3 | 10 000 000 | 17 000 000 |
| DL Category 16 | UL Category 5 | 10 600 000 | 17 400 000 |
| DL Category 16 | UL Category 7 | 10 800 000 | 17 600 000 |
| DL Category 16 | UL Category 13 | 11 000 000 | 18 100 000 |
| DL Category 16 | UL Category 15 | 12 000 000 | 18 800 000 |
| DL Category 16 | UL Category 16 | 8 500 000 | 13 700 000 |
| DL Category 16 | UL Category 18 | 11 800 000 | 18 700 000 |
| DL Category 16 | UL Category 20 | 12 800 000 | 19 700 000 |
| DL Category 17 | UL Category 14 | 330 000 000 | 530 000 000 |
| DL Category 17 | UL Category 19 | 360 000 000 | 530 000 000 |
| DL Category 18 | UL Category 3 | 11 800 000 | 21 600 000 |
| DL Category 18 | UL Category 5 | 12 000 000 | 21 800 000 |
| DL Category 18 | UL Category 7 | 12 300 000 | 22 100 000 |
| DL Category 18 | UL Category 13 | 12 700 000 | 22 500 000 |
| DL Category 18 | UL Category 15 | 13 400 000 | 23 200 000 |
| DL Category 18 | UL Category 16 | 12 300 000 | 22 100 000 |
| DL Category 18 | UL Category 18 | 13 300 000 | 23 100 000 |
| DL Category 18 | UL Category 20 | 14 300 000 | 24 100 000 |
| DL Category 19 | UL Category 3 | 16 000 000 | 28 300 000 |
| DL Category 19 | UL Category 5 | 16 300 000 | 28 500 000 |
| DL Category 19 | UL Category 7 | 16 500 000 | 28 800 000 |
| DL Category 19 | UL Category 13 | 17 000 000 | 29 200 000 |
| DL Category 19 | UL Category 15 | 17 700 000 | 29 900 000 |
| DL Category 19 | UL Category 16 | 16 500 000 | 28 800 000 |
| DL Category 19 | UL Category 18 | 17 500 000 | 29 800 000 |
| DL Category 19 | UL Category 20 | 18 500 000 | 30 800 000 |
| DL Category 19 | UL Category 21 | 18 400 000 | 30 600 000 |
| DL Category 20 | UL Category 3 | 19 400 000 | 35 800 000 |
| DL Category 20 | UL Category 5 | 19 600 000 | 36 000 000 |
| DL Category 20 | UL Category 7 | 19 900 000 | 36 300 000 |
| DL Category 20 | UL Category 13 | 20 300 000 | 36 800 000 |
| DL Category 20 | UL Category 15 | 21 100 000 | 37 500 000 |
| DL Category 20 | UL Category 16 | 19 900 000 | 36 300 000 |
| DL Category 20 | UL Category 18 | 20 900 000 | 37 300 000 |
| DL Category 20 | UL Category 20 | 21 900 000 | 38 300 000 |
| DL Category 20 | UL Category 21 | 21 800 000 | 38 200 000 |
| DL Category 21 | UL Category 3 | 13 700 000 | 23 500 000 |
| DL Category 21 | UL Category 5 | 13 900 000 | 23 700 000 |
| DL Category 21 | UL Category 7 | 14 200 000 | 24 000 000 |
| DL Category 21 | UL Category 13 | 14 600 000 | 24 400 000 |
| DL Category 21 | UL Category 15 | 15 300 000 | 25 200 000 |
| DL Category 21 | UL Category 16 | 14 200 000 | 24 000 000 |
| DL Category 21 | UL Category 18 | 15 200 000 | 25 000 000 |
| DL Category 21 | UL Category 20 | 16 200 000 | 26 000 000 |
| DL Category 22 | UL Category 20 | 26 600 000 | 47 000 000 |
| DL Category 22 | UL Category 22 | 27 500 000 | 48 000 000 |
| DL Category 22 | UL Category 23 | 30 500 000 | 51 300 000 |
| DL Category 22 | UL Category 24 | 32 400 000 | 57 000 000 |
| DL Category 22 | UL Category 25 | 35 000 000 | 59 900 000 |
| DL Category 22 | UL Category 26 | 38 000 000 | 67 600 000 |
| DL Category 23 | UL Category 20 | 29 500 000 | 50 400 000 |
| DL Category 23 | UL Category 22 | 28 500 000 | 49 000 000 |
| DL Category 23 | UL Category 23 | 31 500 000 | 52 300 000 |
| DL Category 23 | UL Category 24 | 33 300 000 | 57 900 000 |
| DL Category 23 | UL Category 25 | 36 000 000 | 60 900 000 |
| DL Category 23 | UL Category 26 | 39 000 000 | 68 600 000 |
| DL Category 24 | UL Category 20 | 31 400 000 | 56 000 000 |
| DL Category 24 | UL Category 22 | 29 500 000 | 50 000 000 |
| DL Category 24 | UL Category 23 | 32 400 000 | 53 300 000 |
| DL Category 24 | UL Category 24 | 34 300 000 | 58 900 000 |
| DL Category 24 | UL Category 25 | 37 000 000 | 61 900 000 |
| DL Category 24 | UL Category 26 | 40 000 000 | 69 500 000 |
| DL Category 25 | UL Category 20 | 34 100 000 | 58 900 000 |
| DL Category 25 | UL Category 22 | 30 500 000 | 51 000 000 |
| DL Category 25 | UL Category 23 | 33 400 000 | 54 300 000 |
| DL Category 25 | UL Category 24 | 35 300 000 | 59 900 000 |
| DL Category 25 | UL Category 25 | 38 000 000 | 62 900 000 |
| DL Category 25 | UL Category 26 | 41 000 000 | 70 500 000 |
| DL Category 26 | UL Category 20 | 37 000 000 | 66 600 000 |
| DL Category 26 | UL Category 22 | 31 500 000 | 52 000 000 |
| DL Category 26 | UL Category 23 | 34 400 000 | 55 300 000 |
| DL Category 26 | UL Category 24 | 36 300 000 | 60 900 000 |
| DL Category 26 | UL Category 25 | 39 000 000 | 63 900 000 |
| DL Category 26 | UL Category 26 | 42 000 000 | 71 500 000 |
| NOTE 1: The UE supports "Total layer 2 buffer size" of 40 000 bytes if the UE indicates support of ce-PUSCH-NB-MaxTBS-r14. Otherwise the UE supports 20 000 bytes. |  |  |  |

Table 4.1A-4: Maximum number of bits of a MCH transport block received within a TTI set by the field ue-CategoryDL for an MBMS capable UE capable of reception via MBSFN

| UE DL Category | Maximum number of bits of a MCH transport block received within a TTI |
| --- | --- |
| DL Category M1 | NA |
| DL Category M2 | NA |
| DL Category 0 | 4584 |
| DL Category 1bis | 10296 |
| DL Category 4 | 75376 |
| DL Category 6 | 75376 |
| DL Category 7 | 75376 |
| DL Category 9 | 75376 |
| DL Category 10 | 75376 |
| DL Category 11 | 75376 (64QAM)97896 (256QAM) |
| DL Category 12 | 75376 (64QAM)97896 (256QAM) |
| DL Category 13 | 75376 (64QAM)97896 (256QAM) |
| DL Category 14 | 75376 (64QAM)97896 (256QAM) |
| DL Category 15 | 75376 (64QAM)97896 (256QAM) |
| DL Category 16 | 75376 (64QAM)97896 (256QAM) |
| DL Category 17 | 75376 (64QAM)97896 (256QAM) |
| DL Category 18 | 75376 (64QAM)97896 (256QAM) |
| DL Category 19 | 75376 (64QAM)97896 (256QAM) |
| DL Category 20 | 75376 (64QAM)97896 (256QAM) |
| DL Category 21 | 75376 (64QAM)97896 (256QAM) |

Table 4.1A-5: Half-duplex FDD operation type set by the field ue-CategoryDL for a half-duplex FDD capable UE

| UE DL Category | Half-duplex FDD operation type |
| --- | --- |
| DL Category M1 | Type B |
| DL Category M2 | Type B |
| DL Category 0 | Type B |
| DL Category 1bis | Type A |
| DL Category 4 | Type A |
| DL Category 6 | Type A |
| DL Category 7 | Type A |
| DL Category 9 | Type A |
| DL Category 10 | Type A |
| DL Category 11 | Type A |
| DL Category 12 | Type A |
| DL Category 13 | Type A |
| DL Category 14 | Type A |
| DL Category 15 | Type A |
| DL Category 16 | Type A |
| DL Category 17 | Type A |
| DL Category 18 | Type A |
| DL Category 19 | Type A |
| DL Category 20 | Type A |
| DL Category 21 | Type A |

Table 4.1A-6: supported DL/UL Categories combinations and maximum UE channel bandwidth set by the fields ue-CategoryDL and ue-CategoryUL and UE categories to be indicated by UEs other than Category M

| UE DL Category | UE UL Category | UE categories | Maximum UE channel bandwidth [MHz] |
| --- | --- | --- | --- |
| DL Category 0 | UL Category 0 | N/A | According to maximum channel bandwidth specified per band in TS 36.101 [6]. |
| DL Category 1bis | UL Category 1bis | Category 1 (NOTE 1) |  |
| DL Category 4 | UL Category 5 | Category 4 |  |
| DL Category 6 | UL Category 5 | Category 6, 4 |  |
| DL Category 6 | UL Category 16 | Category 6, 4DL Category 6 and UL Category 5 |  |
| DL Category 7 | UL Category 13 | Category 7, 4 |  |
| DL Category 7 | UL Category 18 | Category 7, 4DL Category 7 and UL Category 13 |  |
| DL Category 9 | UL Category 5 | Category 9, 6, 4 |  |
| DL Category 9 | UL Category 16 | Category 9, 6, 4DL Category 9 and UL Category 5 |  |
| DL Category 10 | UL Category 13 | Category 10, 7, 4 |  |
| DL Category 10 | UL Category 18 | Category 10, 7, 4DL Category 10 and UL Category 13 |  |
| DL Category 11 | UL Category 5 | Category 11, 9, 6, 4 |  |
| DL Category 11 | UL Category 16 | Category 11, 9, 6, 4DL Category 11 and UL Category 5 |  |
| DL Category 12 | UL Category 13 | Category 12, 10, 7, 4 |  |
| DL Category 12 | UL Category 15 | Category 12, 10, 7, 4DL Category 12 and UL Category 13 |  |
| DL Category 12 | UL Category 18 | Category 12, 10, 7, 4DL Category 12 and UL Category 13 |  |
| DL Category 12 | UL Category 20 | Category 12, 10, 7, 4DL Category 12 and UL Category 13DL Category 12 and UL Category 15 |  |
| DL Category 13 | UL Category 3 | Category 6, 4Category 9 (if supported) |  |
| DL Category 13 | UL Category 5 | Category 6, 4Category 9 (if supported) |  |
| DL Category 13 | UL Category 7 | Category 7, 4Category 10 (if supported) |  |
| DL Category 13 | UL Category 13 | Category 7, 4Category 10 (if supported) |  |
| DL Category 13 | UL Category 16 | Category 6, 4DL Category 13 and UL Category 5 |  |
| DL Category 13 | UL Category 18 | Category 7, 4DL Category 13 and UL Category 13 |  |
| DL Category 14 | UL Category 8 | Category 8, 5 |  |
| DL Category 14 | UL Category 17 | Category 8, 5DL Category 14 and UL Category 8 |  |
| DL Category 15 | UL Category 3 | Category 11, 9, 6, 4 |  |
| DL Category 15 | UL Category 5 | Category 11, 9, 6, 4DL Category 11 and UL Category 5 |  |
| DL Category 15 | UL Category 7 | Category 12, 10, 7, 4 |  |
| DL Category 15 | UL Category 13 | Category 12, 10, 7, 4DL Category 12 and UL Category 13 |  |
| DL Category 15 | UL Category 16 | Category 11, 9, 6, 4DL Category 11 and UL Category 5DL Category 15 and UL Category 5 |  |
| DL Category 15 | UL Category 18 | Category 12, 10, 7, 4DL Category 12 and UL Category 13DL Category 15 and UL Category 13 |  |
| DL Category 16 | UL Category 3 | Category 11, 9, 6, 4 |  |
| DL Category 16 | UL Category 5 | Category 11, 9, 6, 4DL Category 11 and UL Category 5 |  |
| DL Category 16 | UL Category 7 | Category 12, 10, 7, 4 |  |
| DL Category 16 | UL Category 13 | Category 12, 10, 7, 4DL Category 12 and UL Category 13 |  |
| DL Category 16 | UL Category 15 | Category 12, 10, 7, 4DL Category 16,12 and UL Category 13 |  |
| DL Category 16 | UL Category 16 | Category 11, 9, 6, 4DL Category 11 and UL Category 5DL Category 16 and UL Category 5 |  |
| DL Category 16 | UL Category 18 | Category 12, 10, 7, 4DL Category 12 and UL Category 13DL Category 16 and UL Category 13 |  |
| DL Category 16 | UL Category 20 | Category 12, 10, 7, 4DL Category 12 and UL Category 13DL Category 16 and UL Category 13DL Category 16 and UL Category 15 |  |
| DL Category 17 | UL Category 14 | Category 8, 5DL Category 14 and UL Category 8 |  |
| DL Category 17 | UL Category 19 | Category 8, 5DL Category 14 and UL Category 8DL Category 17 and UL Category 14 |  |
| DL Category 18 | UL Category 3 | Category 11, 9, 6, 4DL Category 16 and UL Category 3 |  |
| DL Category 18 | UL Category 5 | Category 11, 9, 6, 4DL Category 16, 11 and UL Category 5 |  |
| DL Category 18 | UL Category 7 | Category 12, 10, 7, 4DL Category 16 and UL Category 7 |  |
| DL Category 18 | UL Category 13 | Category 12, 10, 7, 4DL Category 16, 12 and UL Category 13 |  |
| DL Category 18 | UL Category 15 | Category 12, 10, 7, 4DL Category 16,12 and UL Category 13 |  |
| DL Category 18 | UL Category 16 | Category 11, 9, 6, 4DL Category 11 and UL Category 5DL Category 16 and UL Category 5DL Category 18 and UL Category 5 |  |
| DL Category 18 | UL Category 18 | Category 12, 10, 7, 4DL Category 12 and UL Category 13DL Category 16 and UL Category 13 |  |
| DL Category 18 | UL Category 20 | Category 12, 10, 7, 4DL Category 12 and UL Category 13DL Category 16 and UL Category 13DL Category 18 and UL Category 15 |  |
| DL Category 19 | UL Category 3 | Category 11, 9, 6, 4DL Category 16 and UL Category 3 |  |
| DL Category 19 | UL Category 5 | Category 11, 9, 6, 4DL Category 16, 11 and UL Category 5 |  |
| DL Category 19 | UL Category 7 | Category 12, 10, 7, 4DL Category 16 and UL Category 7 |  |
| DL Category 19 | UL Category 13 | Category 12, 10, 7, 4DL Category 16, 12 and UL Category 13 |  |
| DL Category 19 | UL Category 15 | Category 12, 10, 7, 4DL Category 16,12 and UL Category 13 |  |
| DL Category 19 | UL Category 16 | Category 11, 9, 6, 4DL Category 11 and UL Category 5DL Category 16 and UL Category 5DL Category 19 and UL Category 5 |  |
| DL Category 19 | UL Category 18 | Category 12, 10, 7, 4DL Category 12 and UL Category 13DL Category 16 and UL Category 13DL Category 19 and UL Category 13 |  |
| DL Category 19 | UL Category 20 | Category 12, 10, 7, 4DL Category 12 and UL Category 13DL Category 16 and UL Category 13DL Category 19 and UL Category 15 |  |
| DL Category 19 | UL Category 21 | Category 12, 10, 7, 4DL Category 12 and UL Category 13DL Category 16 and UL Category 13DL Category 19 and UL Category 15 |  |
| DL Category 20 | UL Category 3 | Category 11, 9, 6, 4DL Category 16 and UL Category 3DL Category 19 and UL Category 3 |  |
| DL Category 20 | UL Category 5 | Category 11, 9, 6, 4DL Category 16, 11 and UL Category 5DL Category 19 and UL Category 5 |  |
| DL Category 20 | UL Category 7 | Category 12, 10, 7, 4DL Category 16 and UL Category 7DL Category 19 and UL Category 7 |  |
| DL Category 20 | UL Category 13 | Category 12, 10, 7, 4DL Category 16, 12 and UL Category 13DL Category 19 and UL Category 13 |  |
| DL Category 20 | UL Category 15 | Category 12, 10, 7, 4DL Category 16,12 and UL Category 13DL Category 19 and UL Category 13DL Category 19 and UL Category 15 |  |
| DL Category 20 | UL Category 16 | Category 11, 9, 6, 4DL Category 11 and UL Category 5DL Category 16 and UL Category 5DL Category 19 and UL Category 5DL Category 19 and UL Category 16 |  |
| DL Category 20 | UL Category 18 | Category 12, 10, 7, 4DL Category 12 and UL Category 13DL Category 16 and UL Category 13DL Category 19 and UL Category 13DL Category 19 and UL Category 18 |  |
| DL Category 20 | UL Category 20 | Category 12, 10, 7, 4DL Category 12 and UL Category 13DL Category 16 and UL Category 13DL Category 19 and UL Category 15DL Category 19 and UL Category 20 |  |
| DL Category 20 | UL Category 21 | Category 12, 10, 7, 4DL Category 12 and UL Category 13DL Category 16 and UL Category 13DL Category 19 and UL Category 15DL Category 19 and UL Category 21 |  |
| DL Category 21 | UL Category 3 | Category 11, 9, 6, 4DL Category 16 and UL Category 3DL Category 18 and UL Category 3 |  |
| DL Category 21 | UL Category 5 | Category 11, 9, 6, 4DL Category 16, 11 and UL Category 5DL Category 18 and UL Category 5 |  |
| DL Category 21 | UL Category 7 | Category 12, 10, 7, 4DL Category 16 and UL Category 7DL Category 18 and UL Category 7 |  |
| DL Category 21 | UL Category 13 | Category 12, 10, 7, 4DL Category 16, 12 and UL Category 13DL Category 18 and UL Category 13 |  |
| DL Category 21 | UL Category 15 | Category 12, 10, 7, 4DL Category 16,12 and UL Category 13DL Category 18 and UL Category 13DL Category 18 and UL Category 15 |  |
| DL Category 21 | UL Category 16 | Category 11, 9, 6, 4DL Category 11 and UL Category 5DL Category 16 and UL Category 5DL Category 18 and UL Category 5DL Category 18 and UL Category 16 |  |
| DL Category 21 | UL Category 18 | Category 12, 10, 7, 4DL Category 12 and UL Category 13DL Category 16 and UL Category 13DL Category 18 and UL Category 13DL Category 18 and UL Category 18 |  |
| DL Category 21 | UL Category 20 | Category 12, 10, 7, 4DL Category 12 and UL Category 13DL Category 16 and UL Category 13DL Category 18 and UL Category 15DL Category 18 and UL Category 20 |  |
| DL Category 22 | UL Category 20 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 22 | UL Category 22 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 22 | UL Category 22 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 22 | UL Category 23 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 22 | UL Category 24 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 22 | UL Category 25 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 22 | UL Category 26 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 23 | UL Category 20 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 23 | UL Category 22 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 23 | UL Category 23 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 23 | UL Category 24 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 23 | UL Category 25 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 23 | UL Category 26 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 24 | UL Category 20 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 24 | UL Category 22 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 24 | UL Category 23 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 24 | UL Category 24 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 24 | UL Category 25 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 24 | UL Category 26 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 25 | UL Category 20 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 25 | UL Category 22 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 25 | UL Category 23 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 25 | UL Category 24 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 25 | UL Category 25 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 25 | UL Category 26 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 26 | UL Category 20 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 26 | UL Category 22 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 26 | UL Category 23 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 26 | UL Category 24 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 26 | UL Category 25 | DL Category 20 and UL Category 20 (NOTE3) |  |
| DL Category 26 | UL Category 26 | DL Category 20 and UL Category 20 (NOTE3) |  |
| NOTE 1: The UE indicating DL category 1bis is only required to support 1Rx antenna even though the UE indicates UE category 1 for legacy compatibility.NOTE 2: Void.NOTE 3: The UE indicating DL Category 20 and UL Category 20 also indicates Category 12, 10, 7, 4, DL Category 12 and UL Category 13, DL Category 16 and UL Category 13, DL Category 19 and UL Category 15, DL Category 19 and UL Category 20. |  |  |  |

Table 4.1A-7: supported DL/UL Categories combinations and maximum UE channel bandwidth set by the fields ue-CategoryDL and ue-CategoryUL and UE categories to be indicated by UEs of Category M

| UE DL Category | UE UL Category | UE categories | Maximum UE channel bandwidth [MHz] |
| --- | --- | --- | --- |
| DL Category M1 | UL Category M1 | N/A | 1.4 |
| DL Category M2 | UL Category M2 | DL Category M1 and UL Category M1 | 5(NOTE) |
| NOTE: The minimum of 5 MHz and the maximum channel bandwidth specified per band in TS 36.101 [6]. |  |  |  |

## 4.1B ue-CategorySL-C-RX, ue-CategorySL-C-TX and ue-CategorySL-D

The ue-CategorySL-C-RX, ue-CategorySL-C-TX and ue-CategorySL-D define reception and transmission capabilities for sidelink communication, V2X sidelink communication and sidelink discovery respectively. The parameters set by the UE SL-C-RX, UE SL-C-TX (sidelink communication and V2X sidelink communication) category and UE SL-D (sidelink discovery) category are defined in clause 4.2A. Table 4.1B-1 and Table 4.1B-2 defines the reception and transmission physical layer parameter values for each SL-C-RX and each SL-C-TX Category, respectively. Table 4.1B-3 defines physical layer parameter values for each SL-D Category. If a UE of this release supports sidelink communication, the UE shall support SL-C-RX Category 1 and SL-C-TX Category 1. If a UE of this release supports V2X sidelink communication, the UE shall support SL-C-RX Category 2 to 4 for reception, and SL-C-TX category 2 to 5 for transmission. If a UE of this release supports sidelink discovery, the UE shall support SL-D Category 1.

Table 4.1B-1: Reception physical parameter values set by ue-CategorySL-C-RX

| UE SL-C-RX Category | Maximum number of SL-SCH transport block bits received within a TTI | Maximum number of bits of a SL-SCH transport block received within a TTI | Total number of soft channel bits |
| --- | --- | --- | --- |
| SL-C-RX Category 1 | 25456 | 25456 |  |
| SL-C-RX Category 2 | 31704 | 31704 | 737280 |
| SL-C-RX Category 3 | 48936 | 48936 | 995328 |
| SL-C-RX Category 4 | 73488 | 48936 | 1492992 |

Table 4.1B-2: Transmission physical parameter values set by ue-CategorySL-C-TX

| UE SL-C-TX Category | Maximum number of SL-SCH transport block bits transmitted within a TTI | Maximum number of bits of a SL-SCH transport block transmitted within a TTI | Maximum number of supported layers for spatial multiplexing in SL-C-TX |
| --- | --- | --- | --- |
| SL-C-TX Category 1 | 25456 | 25456 | 1 |
| SL-C-TX Category 2 | 31704 | 31704 | 1 |
| SL-C-TX Category 3 | 49272 | 32856 | 1 |
| SL-C-TX Category 4 | 48936 | 48936 | 1 |
| SL-C-TX Category 5 | 73488 | 48936 | 1 |

Table 4.1B-3: Reception and transmission physical parameter values set by ue-CategorySL-D

| UE SL-D Category | Maximum number of SL-DCH transport block bits received within a TTI | Maximum number of bits of a SL-DCH transport block received within a TTI | Maximum number of SL-DCH transport block bits transmitted within a TTI | Maximum number of bits of a SL-DCH transport block transmitted within a TTI | Maximum number of supported layers for spatial multiplexing in SL-D |
| --- | --- | --- | --- | --- | --- |
| SL-D Category 1 | 11600 | 232 | 232 | 232 | 1 |

## 4.1C ue-Category-NB

The field ue-Category-NB defines a combined uplink and downlink capability in NB-IoT. The parameters set by the UE Category are defined in clause 4.2. Tables 4.1C-1 and 4.1C-2 define the downlink and, respectively, uplink physical layer parameter values for each UE Category. A UE indicating Category NB2 shall also indicate Category NB1.

Table 4.1C-1: Downlink physical layer parameter values set by the field ue-Category-NB

| UE Category | Maximum number of DL-SCH transport block bits received within a TTI | Maximum number of bits of a DL-SCH transport block received within a TTI | Total number of soft channel bits |
| --- | --- | --- | --- |
| Category NB1 | 680 | 680 | 2112 |
| Category NB2 (Note 1) | 2536 or 4968 | 2536 or 4968 | 6400 or 12800 |
| NOTE 1: The UE supports "Maximum number of DL-SCH transport block bits received within a TTI" and "Maximum number of bits of a DL-SCH transport block received within a TTI" of 4968 bits and "Total number of soft channel bits" of 12800 bits if the UE indicates support of npdsch-16QAM-r17. Otherwise the UE supports "Maximum number of DL-SCH transport block bits received within a TTI" and "Maximum number of bits of a DL-SCH transport block received within a TTI" of 2536 bits and "Total number of soft channel bits" of 6400 bits. |  |  |  |

Table 4.1C-2: Uplink physical layer parameter values set by the field ue-Category-NB

| UE Category | Maximum number of UL-SCH transport block bits transmitted within a TTI | Maximum number of bits of an UL-SCH transport block transmitted within a TTI |
| --- | --- | --- |
| Category NB1 | 1000 | 1000 |
| Category NB2 | 2536 | 2536 |

Table 4.1C-3: Total layer 2 buffer sizes set by the field ue-Category-NB

| UE Category | Total layer 2 buffer size [bytes] |
| --- | --- |
| Category NB1 | 4000 |
| Category NB2 (Note 1) | 8000 or 12000 |
| NOTE 1: The UE supports "Total layer 2 buffer size" of 12000 bytes if the UE indicates support of npdsch-16QAM-r17. Otherwise the UE supports 8000 bytes. |  |

Table 4.1C-5: Half-duplex FDD operation type set by the field ue-Category-NB for a half-duplex FDD capable UE

| UE Category | Half-duplex FDD operation type |
| --- | --- |
| Category NB1 | Type B |
| Category NB2 | Type B |

## 4.2 Parameters set by the field ue-Category and ue-CategoryDL / ue-CategoryUL

### 4.2.1 Transport channel parameters in downlink

#### 4.2.1.1 Maximum number of DL-SCH transport block bits received within a TTI

Defines the maximum number of DL-SCH transport blocks bits that the UE is capable of receiving within a DL-SCH TTI.

This number does not include the bits of a DL-SCH transport block carrying BCCH in the same subframe.

#### 4.2.1.2 Maximum number of bits of a DL-SCH transport block received within a TTI

Defines the maximum number of DL-SCH transport block bits that the UE is capable of receiving in a single transport block within a DL-SCH TTI per cell.

#### 4.2.1.3 Total number of DL-SCH soft channel bits

Defines the total number of soft channel bits available for HARQ processing.

This number does not include the soft channel bits required by the dedicated broadcast HARQ process for the decoding of system information.

#### 4.2.1.4 Maximum number of bits of a MCH transport block received within a TTI

Defines the maximum number of MCH transport block bits that the UE is capable of receiving within a MCH TTI.

### 4.2.2 Transport channel parameters in uplink

#### 4.2.2.1 Maximum number of bits of an UL-SCH transport block transmitted within a TTI

Defines the maximum number of UL-SCH transport block bits that the UE is capable of transmitting in a single transport block within an UL-SCH TTI.

#### 4.2.2.2 Maximum number of UL-SCH transport block bits transmitted within a TTI

Defines the maximum number of UL-SCH transport blocks bits that the UE is capable of transmitting within an UL-SCH TTI.

### 4.2.3 Physical channel parameters in downlink (DL)

#### 4.2.3.1 Maximum number of supported layers for spatial multiplexing in DL

This field defines the maximum number of supported layers for spatial multiplexing per UE. The UE shall support the number of layers according to its Rel-8/9 category (Cat. 1-5) in all non-CA band combinations. Further requirements on the number of supported layers for spatial multiplexing are provided in clause 4.3.5.2.

For each bandwidth class per band per band combination specified in supportedBandCombination, the UE provides the corresponding MIMO capability.

### 4.2.4 Physical channel parameters in uplink (UL)

#### 4.2.4.1 Support for 64QAM in UL

Defines if 64QAM is supported in UL.

### 4.2.5 Total layer 2 buffer size

This parameter defines the total layer 2 buffer size. The total layer 2 buffer size is defined as the sum of the number of bytes that the UE is capable of storing in the RLC transmission windows and RLC reception and reordering windows for all radio bearers, and for UEs capable of split bearers, also in PDCP reordering windows for all split radio bearers.

### 4.2.6 Half-duplex FDD operation type

This parameter defines the type of half-duplex FDD operation for a half-duplex FDD capable UE. The half-duplex FDD operation type applies whenever the UE is in half-duplex FDD operation. The different types of half-duplex FDD operation are specified in TS 36.211 [17].

### 4.2.7 RF parameters

#### 4.2.7.1 Maximum UE channel bandwidth

Defines the maximum channel bandwidth supported by the UE.

## 4.2A Parameters set by ue-CategorySL-C / ue-CategorySL-D

### 4.2A.1 Transport channel parameters in sidelink (SL)

#### 4.2A.1.1 Maximum number of SL-SCH transport block bits received within a TTI

Defines the maximum number of SL-SCH transport block bits that the UE is capable of receiving within a SL-SCH TTI.

#### 4.2A.1.2 Maximum number of bits of a SL-SCH transport block received within a TTI

Defines the maximum number of SL-SCH transport block bits that the UE is capable of receiving in a single transport block within a SL-SCH TTI.

#### 4.2A.1.3 Maximum number of SL-DCH transport block bits received within a TTI

Defines the maximum number of SL-DCH transport block bits that the UE is capable of receiving within a SL-DCH TTI.

#### 4.2A.1.4 Maximum number of bits of a SL-DCH transport block received within a TTI

Defines the maximum number of SL-DCH transport block bits that the UE is capable of receiving in a single transport block within a SL-DCH TTI.

#### 4.2A.1.5 Maximum number of bits of a SL-SCH transport block transmitted within a TTI

Defines the maximum number of SL-SCH transport block bits that the UE is capable of transmitting in a single transport block within a SL-SCH TTI.

#### 4.2A.1.6 Maximum number of SL-SCH transport block bits transmitted within a TTI

Defines the maximum number of SL-SCH transport block bits that the UE is capable of transmitting within a SL-SCH TTI.

#### 4.2A.1.7 Maximum number of bits of a SL-DCH transport block transmitted within a TTI

Defines the maximum number of SL-DCH transport block bits that the UE is capable of transmitting in a single transport block within a SL-DCH TTI.

#### 4.2A.1.8 Maximum number of SL-DCH transport block bits transmitted within a TTI

Defines the maximum number of SL-DCH transport block bits that the UE is capable of transmitting within a SL-DCH TTI.

### 4.2A.2 Physical channel parameters in sidelink (SL)

#### 4.2A.2.1 Maximum number of supported layers for spatial multiplexing in SL-C

This field defines the maximum number of supported layers for spatial multiplexing per UE in sidelink communication or V2X sidelink communication.

#### 4.2A.2.2 Maximum number of supported layers for spatial multiplexing in SL-D

This field defines the maximum number of supported layers for spatial multiplexing per UE in sidelink discovery.

## 4.3 Parameters independent of the field ue-Category and ue-CategoryDL / ue-CategoryUL

### 4.3.1 PDCP Parameters

#### 4.3.1.1 supportedROHC-Profiles

This field defines which ROHC profiles from the list below are supported by the UE.

- 0x0000 ROHC uncompressed (RFC 5795)

- 0x0001 ROHC RTP (RFC 3095, RFC 4815)

- 0x0002 ROHC UDP (RFC 3095, RFC 4815)

- 0x0003 ROHC ESP (RFC 3095, RFC 4815)

- 0x0004 ROHC IP (RFC 3843, RFC 4815)

- 0x0006 ROHC TCP (RFC 6846)

- 0x0101 ROHCv2 RTP (RFC 5225)

- 0x0102 ROHCv2 UDP (RFC 5225)

- 0x0103 ROHCv2 ESP (RFC 5225)

- 0x0104 ROHCv2 IP (RFC 5225)

A UE that supports one or more of the listed ROHC profiles shall support ROHC profile 0x0000 ROHC uncompressed (RFC 5795).

'IMS capable UEs supporting voice' shall support ROHC profiles 0x0000, 0x0001, 0x0002 and be able to compress and decompress headers of PDCP SDUs at a PDCP SDU rate corresponding to supported IMS voice codecs.

#### 4.3.1.1A supportedROHC-Profiles-r13

This field defines which ROHC profiles from the list below are supported by the UE:

- 0x0000 ROHC uncompressed (RFC 5795)

- 0x0002 ROHC UDP (RFC 3095, RFC 4815)

- 0x0003 ROHC ESP (RFC 3095, RFC 4815)

- 0x0004 ROHC IP (RFC 3843, RFC 4815)

- 0x0006 ROHC TCP (RFC 6846)

- 0x0102 ROHCv2 UDP (RFC 5225)

- 0x0103 ROHCv2 ESP (RFC 5225)

- 0x0104 ROHCv2 IP (RFC 5225)

A UE that supports one or more of the listed ROHC profiles shall support ROHC profile 0x0000 ROHC uncompressed (RFC 5795). This field is only applicable if the UE supports S1-U data transfer or User plane CIoT EPS Optimisation, see TS 36.331 [5], and any ue-Category-NB.

#### 4.3.1.2 maxNumberROHC-ContextSessions

This field defines the maximum number of header compression context sessions supported by the UE, excluding context sessions that leave all headers uncompressed.

#### 4.3.1.2A maxNumberROHC-ContextSessions-r13

This field defines the maximum number of header compression context sessions supported by the UE, excluding context sessions that leave all headers uncompressed. This field is only applicable if the UE supports S1-U data transfer or User plane CIoT EPS Optimisation, see TS 36.331 [5], and any ue-Category-NB.

#### 4.3.1.3 pdcp-SN-Extension

This field defines whether the UE supports 15 bit length of PDCP sequence number as specified in TS 36.323 [2]. It is mandatory for UEs supporting split bearers and UEs supporting 18 bit length of PDCP sequence number.

#### 4.3.1.4 supportRohcContextContinue

This field defines whether the UE supports ROHC context continuation operation where the UE does not reset the current ROHC context upon handover.

#### 4.3.1.5 pdcp-SN-Extension-18bits-r13

This field defines whether the UE supports 18 bit length of PDCP sequence number as specified in TS 36.323 [2].

#### 4.3.1.6 supportedUplinkOnlyROHC-Profiles

This field defines which ROHC profile(s) from the list below are supported in uplink-only ROHC operation by the UE.

- 0x0006 ROHC TCP (RFC 6846)

A UE that supports uplink-only ROHC profile(s) shall support ROHC profile 0x0000 ROHC uncompressed (RFC 5795).

#### 4.3.1.7 supportedUDC-r15

This field defines whether the UE supports the uplink data compression operation as specified in TS 36.323 [2].

A UE that supports the uplink data compression operation shall support 8192 bytes for compression buffer per UDC DRB and support up to 2 UDC DRBs.

#### 4.3.1.8 supportedStandardDic-r15

This field defines whether the UE supports UL data compression with SIP static dictionary as defined in TS 36.323 [2].

#### 4.3.1.9 supportedOperatorDic-r15

This field defines whether the UE supports UL data compression with operator defined dictionary. If UE supports operator defined dictionary, the UE shall report versionOfDictionary, the version number of the dictionary, and associatedPLMN-ID, the associated PLMN ID of this operator defined dictionary as defined in TS 36.331 [5]. Note this parameter is not required to be present if the UE is in VPLMN. In this release of specification, UE can only support one operator defined dictionary.

#### 4.3.1.10 pdcp-Duplication-r15

This field defines whether the UE supports PDCP duplication.

#### 4.3.1.11 pdcp-VersionChangeWithoutHO-r16

This field defines whether the UE supports changing the PDCP version of DRBs, from LTE PDCP to NR PDCP and vice versa, without handover.

#### 4.3.1.12 ehc-r16

Indicates that the UE supports Ethernet header compression and decompression using EHC protocol, as specified in TS 36.323 [2] and in Annex A of TS 38.323 [40]. The UE indicating this capability and indicating support for at least one ROHC profile, shall support simultaneous configuration of EHC and ROHC on different DRBs.

#### 4.3.1.13 maxNumberEHC-Contexts-r16

Defines the maximum number of Ethernet header compression contexts supported by the UE across all DRBs and across UE's EHC compressor and EHC decompressor. The indicated number defines the number of contexts in addition to CID = "all zeros" as specified in Annex A of TS 38.323 [40].

#### 4.3.1.14 continueEHC-Context-r16

Indicates that the UE supports EHC context continuation operation where the UE keeps the established EHC context(s) upon PDCP re-establishment, as specified in TS 36.323 [2].

#### 4.3.1.15 jointEHC-ROHC-Config-r16

Indicates whether the UE supports simultaneous configuration of EHC and ROHC protocols for the same DRB.

### 4.3.1A NR PDCP Parameters

NR PDCP capabilities: the definition of rohc-Profiles-r15, rohc-ContextMaxSessions-r15, rohc-ProfilesUL-Only-r15, rohc-ContextContinue-r15, outOfOrderDelivery-r15 and sn-SizeLo-r15 are the same as supportedROHC-Profiles, maxNumberROHC-ContextSessions, uplinkOnlyROHC-Profiles, continueROHC-Context, outOfOrderDelivery and shortSN defined in TS 38.306 [32].

ims-VoiceOverNR-PDCP-MCG-Bearer-r15 indicates whether the UE supports IMS voice over NR PDCP with only MCG RLC bearer.

ims-VoiceOverNR-PDCP-SCG-Bearer-r15 indicates whether the UE supports IMS voice over NR PDCP with only SCG RLC bearer when configured with EN-DC.

ims-VoNR-PDCP-SCG-NGENDC-r15 indicates whether the UE supports IMS voice over NR PDCP with only SCG RLC bearer when configured with NGEN-DC.

NOTE: In this release of specification, IMS voice over split bearer is not supported for (NG)EN-DC.

### 4.3.2 RLC parameters

#### 4.3.2.1 Void

#### 4.3.2.2 extended-RLC-LI-Field-r12

This field defines whether the UE supports 15 bit RLC Length Indicator (LI) as specified in TS 36.322 [3].

#### 4.3.2.3 extendedRLC-SN-SO-Field-r13

This field defines whether the UE supports 16 bit length of RLC sequence number and 16 bit length of RLC Segment Offset (SO) as specified in TS 36.322 [3]. It is mandatory for UEs supporting 16 bit length of MAC L field.

#### 4.3.2.4 extendedPollByte-r14

This field defines whether the UE supports extended pollByte values as defined by pollByte-r14 in TS 36.331 [5].

#### 4.3.2.5 rlc-UM-r15

This field defines whether the UE supports RLC UM as specified in TS 36.322 [3]. This field is only applicable for UEs of any ue-Category-NB.

#### 4.3.2.6 rlc-AM-Ooo-Delivery-r15

This field defines whether the UE supports out-of-order delivery from RLC to PDCP for RLC AM.

#### 4.3.2.7 rlc-UM-Ooo-Delivery-r15

This field defines whether the UE supports out-of-order delivery from RLC to PDCP for RLC UM.

#### 4.3.2.8 flexibleUM-AM-Combinations-r15

This field defines whether the UE supports any combination of RLC UM and RLC AM DRBs as long as the total number of DRBs is at most 8, regardless of what FGI20 indicates.

### 4.3.3 Void

### 4.3.4 Physical layer parameters

#### 4.3.4.1 ue-TxAntennaSelectionSupported

This field defines whether the UE supports transmit antenna selection.

#### 4.3.4.2 ue-SpecificRefSigsSupported

This field defines whether the UE supports PDSCH transmission mode 7 for FDD.

#### 4.3.4.3 Void

#### 4.3.4.4 enhancedDualLayerFDD

This field defines whether the UE supports enhanced dual layer (PDSCH transmission mode 8) for FDD.

#### 4.3.4.5 enhancedDualLayerTDD

This field defines whether the UE supports enhanced dual layer (PDSCH transmission mode 8) for TDD. Enhanced dual layer shall be supported by UEs of this version of the specification supporting TDD.

#### 4.3.4.6 supportedMIMO-CapabilityUL-r10

This field defines the maximum number of spatial multiplexing layers in the uplink direction for a certain band and bandwidth class in a supportedBandCombination supported by the UE.

#### 4.3.4.7 supportedMIMO-CapabilityDL-r10

This field defines the maximum number of spatial multiplexing layers in the downlink direction for a certain band and bandwidth class in a supportedBandCombination supported by the UE. For bandwidth classes that include multiple component carriers (i.e. bandwidth classes B, C, D and so on), the field defines the maximum number of spatial multiplexing layers supported by the UE on all component carriers in the corresponding bandwidth class.

The support for more layers in supportedMIMO-CapabilityDL than given by the "maximum number of supported layers for spatial multiplexing in DL" derived from the ue-Category (without suffix) in the UE-EUTRA-Capability IE is only applicable to transmission mode 9 and transmission mode 10.

#### 4.3.4.8 two-AntennaPortsForPUCCH-r10


This field defines whether the UE supports transmit diversity for PUCCH formats 1/1a/1b/2/2a/2b, and if the UE supports PUCCH format 3, transmit diversity for PUCCH format 3.

#### 4.3.4.9 tm9-With-8Tx-FDD-r10


This field defines whether the UE supports PDSCH transmission mode 9 with 8 CSI reference signal ports for FDD when not operating in CE mode.

#### 4.3.4.10 pmi-Disabling-r10


This field defines whether the UE supports PMI disabling.

#### 4.3.4.11 crossCarrierScheduling-r10


This field defines whether the UE supports cross carrier scheduling operation for carrier aggregation, including (if the UE supports carrier aggregation in UL) the use of PCell as the pathloss reference for an SCell when pathlossReference-r10 within UplinkPowerControlDedicatedSCell-r10 is configured as "pCell". The UE supports PDCCH DCI formats with CIF if the UE indicates support for cross carrier scheduling.

NOTE: Regardless of whether the UE supports cross carrier scheduling operation or not, it is mandatory for a UE supporting carrier aggregation in UL to support the configuration where pathlossReference-r10 within UplinkPowerControlDedicatedSCell-r10 is set to "sCell".

#### 4.3.4.12 simultaneousPUCCH-PUSCH-r10


This field defines whether the UE baseband supports simultaneous transmission of PUCCH and PUSCH, and is band agnostic. If the UE indicates support of baseband capability for simultaneous transmission of PUCCH and PUSCH using this field, and if the UE indicates support of RF capability for non-contiguous UL resource allocation within a component carrier for a particular E-UTRA radio frequency band, then the UE supports simultaneous transmission of PUCCH and PUSCH within each component carrier of the band. If the UE indicates support of baseband capability for simultaneous transmission of PUCCH and PUSCH using this field, and if the UE indicates support of carrier aggregation in UL, then the UE supports simultaneous transmission of PUCCH and PUSCH across any UL component carriers which the UE can aggregate. If the UE supports uplink LAA, this field is only applicable for non-LAA cells. For LAA SCells, see clause 7.7.4. If the UE supports DC, this field is applicable within a CG. If the UE supports PUCCH on SCell, this field is applicable within a PUCCH group as defined in TS 36.213 [22].

#### 4.3.4.13 multiClusterPUSCH-WithinCC-r10


This field defines whether the UE baseband supports multi-cluster PUSCH transmission within a component carrier (i.e. PUSCH resource allocation type 1), and is band agnostic. If the UE indicates support of baseband capability for multi-cluster PUSCH transmission within a component carrier using this field, and if the UE indicates support of RF capability for non-contiguous UL resource allocation within a component carrier for a particular E-UTRA radio frequency band, then the UE supports multi-cluster PUSCH transmission within each component carrier of the band.

NOTE: If the UE indicates support of carrier aggregation in UL, then the UE supports PUSCH transmissions over non-contiguous resource blocks across any UL component carriers which the UE can aggregate, regardless of whether or not the UE indicates support of baseband capability for multi-cluster PUSCH transmission within a component carrier using this field..

#### 4.3.4.14 nonContiguousUL-RA-WithinCC-Info-r10


This field defines whether the UE RF supports non-contiguous UL resource allocations within a component carrier, and is signalled per E-UTRA radio frequency band which the UE supports.

#### 4.3.4.15 crs-InterfHandl-r11

This field defines whether the UE supports CRS interference handling. It is mandatory for UEs of this release of the specification, except for Category 0, M1, 1bis and M2 UEs.

#### 4.3.4.16 Void

#### 4.3.4.17 Void

#### 4.3.4.18 ePDCCH-r11

This field defines whether the UE can receive DCI on UE specific search space on Enhanced PDCCH.

#### 4.3.4.19 multiACK-CSI-Reporting-r11

This field defines whether the UE supports multi-cell HARQ ACK and periodic CSI reporting and SR on PUCCH format 3 if the UE supports FDD carrier aggregation with more than two DL component carriers or TDD carrier aggregation.

#### 4.3.4.20 ss-CCH-InterfHandl-r11

This field defines whether the UE supports synchronisation signal and common channel interference handling if the UE supports crs-InterfHandl-r11. It is mandatory for UEs of this release of the specification to support this feature for TDD bands, except for Category 0, M1, 1bis and M2 UEs.

#### 4.3.4.21 tdd-SpecialSubframe-r11

This field defines whether the UE supports TDD special subframe as specified in TS 36.211 [17]. It is mandatory for UEs of this release of the specification.

#### 4.3.4.21A tdd-SpecialSubframe-r14

This field defines whether the UE supports TDD special subframe configuration 10 as specified in TS 36.211 [17]. A UE indicating support of tdd-SpecialSubframe-r14 shall not indicate support of ssp10-TDD-Only-r14.

#### 4.3.4.21B ssp10-TDD-Only-r14

This field defines whether the UE supports TDD special subframe configuration 10 when operating only in TDD carriers (i.e., not in TDD/FDD CA or TDD/FS3 CA) as specified in TS 36.211 [17]. A UE indicating support of ssp10-TDD-Only-r14 shall not indicate support of tdd-SpecialSubframe-r14.

#### 4.3.4.22 txDiv-PUCCH1b-ChSelect-r11

This field defines whether the UE supports transmit diversity for PUCCH format 1b with channel selection if the UE supports carrier aggregation and two-AntennaPortsForPUCCH-r10. UE supporting txDiv-PUCCH1b-ChSelect shall support configuration of PUCCH-ConfigDedicated-v13c0.

#### 4.3.4.23 ul-CoMP-r11

This field defines whether the UE supports UL Coordinated Multi-Point operation. It is mandatory for UEs of this release of the specification.

#### 4.3.4.24 tm5-FDD

This field defines whether the UE supports PDSCH transmission mode 5 for FDD.

#### 4.3.4.25 tm5-TDD

This field defines whether the UE supports PDSCH transmission mode 5 for TDD.

#### 4.3.4.26 interBandTDD-CA-WithDifferentConfig-r11

This field defines whether the UE supports inter-band TDD carrier aggregation with different UL/DL configuration combinations. It is mandatory for UEs of this release of the specification if inter-band TDD carrier aggregation is supported.

#### 4.3.4.27 e-HARQ-Pattern-FDD-r12

This field defines whether the UE supports enhanced HARQ pattern for TTI bundling operation for FDD.

#### 4.3.4.28 tdd-FDD-CA-PCellDuplex-r12

The presence of this field indicates that the UE supports TDD/FDD CA in any supported band combination including at least one FDD band with bandParametersUL and at least one TDD band with bandParametersUL. The first bit is set to "1" if UE supports the TDD PCell. The second bit is set to "1" if UE supports FDD PCell. This field is included only if the UE supports band combination including at least one FDD band with bandParametersUL and at least one TDD band with bandParametersUL. If this field is included, the UE shall set at least one of the bits as "1". If this field is included with DC, then it is applicable within a CG, and the presence of this field indicates the capability of the UE to support TDD/FDD CA with at least one FDD band and at least one TDD band in the same CG, with the value indicating the support for TDD/FDD PCell (PSCell).

#### 4.3.4.29 csi-SubframeSet-r12

This field defines whether the UE supports Rel-12 DL CSI subframe set configuration, Rel-12 DL CSI subframe set dependent CSI measurement/feedback, configuration of up to 2 CSI-IM resources for a CSI process with no more than 4 CSI-IM resources for all CSI processes of one frequency if the UE supports tm10, configuration of two ZP-CSI-RS for tm1-tm9, PDSCH RE mapping with two ZP-CSI-RS configurations, and EPDCCH RE mapping with two ZP-CSI-RS configurations if the UE supports EPDCCH. This field is only applicable for UEs supporting TDD.

#### 4.3.4.30 phy-TDD-ReConfig-FDD-PCell-r12

This field defines whether the UE supports TDD UL/DL reconfiguration for TDD serving cell(s) via monitoring PDCCH with eIMTA-RNTI on a FDD PCell, and HARQ feedback according to UL and DL HARQ reference configurations.

#### 4.3.4.31 phy-TDD-ReConfig-TDD-PCell-r12

This field defines whether the UE supports TDD UL/DL reconfiguration for TDD serving cell(s) via monitoring PDCCH with eIMTA-RNTI on a TDD PCell, and HARQ feedback according to UL and DL HARQ reference configurations.

#### 4.3.4.32 pusch-SRS-PowerControl-SubframeSet-r12

This field defines whether the UE supports subframe set dependent UL power control for PUSCH and SRS. This field is only applicable for UEs supporting TDD.

#### 4.3.4.33 enhanced-4TxCodebook-r12

This field defines whether the UE supports enhanced 4Tx codebook as specified in TS 36.211 [17].

#### 4.3.4.34 pusch-FeedbackMode-r12

This field defines whether the UE supports PUSCH feedback mode 3-2 as specified in TS 36.213 [22].

#### 4.3.4.35 naics-Capability-List-r12

This field indicates that the UE supports NAICS, i.e. receiving assistance information from serving cell and using it to cancel or suppress interference of a neighbouring cell for at least one band combination. For each entry of the list, the NAICS capability for a band combination is indicated as a combination of numberOfNAICSCapableCC and numberOfAggregatedPRB.

#### 4.3.4.36 noResourceRestrictionForTTIBundling-r12

This field defines whether the UE supports TTI bundling operation without resource allocation restriction. It is mandatory for UEs of this release of the specification except for Category M1 and Category M2 UEs.

#### 4.3.4.37 Void

#### 4.3.4.38 discoverySignalsInDeactSCell-r12

This field defines whether the UE supports the behaviour on DL signals and physical channels when SCell is deactivated and discovery signals measurement is configured as specified in TS 36.211 [17]. A UE that supports this feature shall also support carrier aggregation and crs-DiscoverySignalsMeas-r12.

#### 4.3.4.39 ul-64QAM-r12

This field defines whether the UE supports UL 64QAM. A UE that supports 64QAM in UL shall support 64QAM in UL in all supported frequency bands.

#### 4.3.4.40 supportedMIMO-CapabilityDL-r12

This field defines the maximum number of spatial multiplexing layers in the downlink direction supported by the UE on a single component carrier for bandwidth classes that include multiple component carriers (i.e. bandwidth classes B, C, D and so on).

The support for more layers in supportedMIMO-CapabilityDL-12 than given by the "maximum number of supported layers for spatial multiplexing in DL" derived from the ue-Category or ue-CategoryDL in the UE-EUTRA-Capability IE is only applicable to transmission mode 9 and transmission mode 10.

#### 4.3.4.41 alternativeTBS-Indices-r12

This field defines whether alternative TBS indices ITBS 26A and 33A as specified in TS 36.213 [22] are supported by the UE which is capable of transmission mode 9 or 10. Support of the alternative TBS index ITBS 33A is applied for the UE supporting 256QAM in DL.

#### 4.3.4.42 codebook-HARQ-ACK-r13

The first bit of this bitmap defines whether HARQ ACK codebook size determination based on the DAI-based solution as specified in TS 36.213 [22] is supported by the UE. If the UE supports carrier aggregation with more than 5 DL component carriers, it is mandatory to support HARQ ACK codebook size determination based on the DAI-based solution.

The second bit of this bitmap defines whether HARQ ACK codebook size determination based on the number of configured CCs as specified in TS 36.213 [22] is supported by the UE. If the UE supports carrier aggregation with more than 5 DL component carriers, it is mandatory to support HARQ ACK codebook size determination based on the number of configured CCs.

#### 4.3.4.43 fdd-HARQ-TimingTDD-r13

This field defines whether FDD HARQ timing for TDD SCell when configured with TDD PCell as specified in TS 36.213 [22] is supported by the UE.

#### 4.3.4.44 maxNumberUpdatedCSI-Proc-r13

This field defines the maximum number of CSI processes to be updated per UE for which aperiodic CSI is requested for CA with more than 5CCs as specified in TS 36.213 [22] which is supported by the UE.

#### 4.3.4.45 pucch-Format4-r13

This field defines whether PUCCH format 4 as specified in TS 36.213 [22] is supported by the UE. It is mandatory for UEs of this release of the specification if TDD carrier aggregation with more than 5 DL component carriers is supported. It is mandatory for UEs of this release of the specification if FDD carrier aggregation with more than [FFS] DL component carriers is supported.

#### 4.3.4.46 pucch-Format5-r13

This field defines whether PUCCH format 5 as specified in TS 36.213 [22] is supported by the UE.

#### 4.3.4.47 pucch-SCell-r13

This field defines whether PUCCH transmission on SCell in CA is supported by the UE.

#### 4.3.4.48 supportedBlindDecoding-r13

This field defines blind decoding capabilities supported by the UE as specified in TS 36.213 [22].

##### 4.3.4.48.1 maxNumberDecoding-r13

This field defines the maximum number of blind decodes in the UE specific search space per UE in one subframe for CA with more than 5CCs as specified in TS 36.213 [22] which is supported by the UE. The number of blind decodes supported by the UE is the field value * 32. The UE indicating the maximum number of blind decodes in this field shall also support pdcch-CandidateReduction-r13 and/or skipMonitoringDCI-Format0-1A-r13.

##### 4.3.4.48.2 pdcch-CandidateReductions-r13

This field defines whether the UE supports PDCCH candidate reduction on UE specific search space as specified in TS 36.213 [22], clause 9.1.1.

##### 4.3.4.48.3 skipMonitoringDCI-Format0-1A-r13

This field defines whether the UE supports blind decoding reduction on UE specific search space by not monitoring DCI Format 0 and 1A as specified in TS 36.213 [22], clause 9.1.1.

#### 4.3.4.49 crs-InterfMitigationTM10-r13

The field defines whether the UE supports CRS interference mitigation in transmission mode 10. The UE supporting the crs-InterfMitigationTM10-r13 capability shall also support the crs-InterfHandl-r11 capability.

#### 4.3.4.49a crs-InterfMitigationTM1toTM9-r13

The field defines whether the UE supports CRS interference mitigation (CRS-IM) while operating in the following transmission modes (TM): TM 1, TM 2, …, TM 8 and TM 9. The UE shall not include the field if it does not support CRS IM in TMs 1-9. If the field is present, the UE supports CRS-IM on at least one arbitrary downlink CC for up to crs-InterfMitigationTM1toTM9-r13 downlink CC CA configuration. The UE signals crs-InterfMitigationTM1toTM9-r13 value to indicate the maximum crs-InterfMitigationTM1toTM9-r13 downlink CC CA configuration where UE may apply CRS IM. For example, the UE sets "crs-InterfMitigationTM1toTM9-r13 = 3" to indicate that the UE supports CRS-IM on at least one DL CC for supported non-CA, 2DL CA and 3DL CA configurations. The UE supporting the crs-InterfMitigationTM1toTM9-r13 capability shall also support the crs-InterfHandl-r11 capability.

If this field is present, UE supports any of the following features:

1) CRS-IM with 2 CRS antenna ports for PDSCH for UEs with 2 receiver antenna ports (as specified in the TS 36.101 [6])

2) CRS-IM with 4 CRS antenna ports for PDSCH for UEs with 2 receiver antenna ports (as specified in the TS 36.101 [6])

3) CRS-IM with 2 CRS antenna ports for PDSCH for UEs with 4 receiver antenna ports (as specified in the TS 36.101 [6])

4) CRS-IM with 4 CRS antenna ports for PDSCH for UEs with 4 receiver antenna ports (as specified in the TS 36.101 [6])

#### 4.3.4.50 pdsch-CollisionHandling-r13

This field defines whether PDSCH collision handling as specified in TS 36.213 [22] is supported by the UE.

#### 4.3.4.51 aperiodicCSI-Reporting-r13

This field defines whether the UE supports aperiodic CSI reporting with 3 bits of the CSI request field size as specified in TS 36.213 [22], clause 7.2.1 and/or aperiodic CSI reporting mode 1-0 and mode 1-1 as specified in TS 36.213 [22], clause 7.2.1.

#### 4.3.4.52 crossCarrierScheduling-B5C-r13

This field defines whether the UE supports cross carrier scheduling beyond 5 DL component carriers. If supported, the UE shall also support crossCarrierScheduling-r10, i.e., cross carrier scheduling up to 5 DL component carriers.

#### 4.3.4.53 spatialBundling-HARQ-ACK-r13

This field defines whether the UE supports HARQ-ACK spatial bundling on PUCCH or PUSCH as specified in TS 36.213 [22], clauses 7.3.1 and 7.3.2.

#### 4.3.4.54 uci-PUSCH-Ext-r13

This field defines whether the UE supports an extension of UCI delivering more than 22 HARQ-ACK bits on PUSCH as specified in TS 36.212 [26], clause 5.2.2.6 and TS 36.213 [22], clause 8.6.3. It is mandatory for UEs of this release of the specification if TDD carrier aggregation with more than 5 DL component carriers is supported. It is mandatory for UEs of this release of the specification if FDD carrier aggregation with more than [FFS] DL component carriers is supported.

#### 4.3.4.55 multiTone-r13

This field defines whether the UE supports UL multi-tone transmissions on NPUSCH. This field is only applicable for UEs of any ue-Category-NB. It is mandatory for UEs of this release of the specification.

#### 4.3.4.56 multiCarrier-r13

This field defines whether the UE supports multi-carrier operation. This field is only applicable for UEs of any ue-Category-NB. It is mandatory for UEs of this release of the specification.

#### 4.3.4.57 cch-InterfMitigation-RefRecTypeA-r13

This field defines whether the UE supports Type A downlink control channel interference mitigation receiver "LMMSE-IRC + CRS-IC" for PDCCH/PCFICH/PHICH/EPDCCH receive processing (Enhanced downlink control channel performance requirements Type A in the TS 36.101 [6]).

If this field is present, the UE supports at least one the following features:

1) Enhanced downlink control channel interference mitigation Type A receiver for 2 CRS antenna ports for UEs with 2 receiver antenna ports (Enhanced downlink control channel performance requirements Type A in the TS 36.101 [6]).

2) Enhanced downlink control channel interference mitigation Type A receiver for 4 CRS antenna ports for UEs with 2 receiver antenna ports (Enhanced downlink control channel performance requirements Type A in the TS 36.101 [6]).

#### 4.3.4.58 cch-InterfMitigation-RefRecTypeB-r13

This field defines whether the UE supports Type B downlink control channel interference mitigation receiver "E-LMMSE-IRC + CRS-IC" for PDCCH/PCFICH/PHICH receive processing in synchronous networks (Enhanced downlink control channel performance requirements Type B in the TS 36.101 [6]). The UE supporting the capability defined by cch-InterfMitigation-RefRecTypeB-r13 shall also support the capability defined by cch-InterfMitigation-RefRecTypeA-r13.

#### 4.3.4.59 cch-InterfMitigation-MaxNumCCs-r13

This field indicates that the UE supports downlink control channel interference mitigation on at least one arbitrary downlink CC for up to cch-InterfMitigation-MaxNumCCs downlink CC CA configuration.

#### 4.3.4.60 tdd-TTI-Bundling-r14

This field defines whether the UE supporting TDD special subframe configuration 10 also supports TTI bundling for TDD configuration 2 and 3 when ssp10 is configured as specified in TS 36.331 [5].

#### 4.3.4.61 dmrs-LessUpPTS-r14

This field defines whether the UE supports not to transmit DMRS for PUSCH in UpPTS as specified in TS 36.211 [17].

#### 4.3.4.62 twoHARQ-Processes-r14

This field defines whether the UE supports 2 HARQ processes in DL and UL. This field is only applicable for UEs that support category NB2.

#### 4.3.4.63 ce-PUSCH-NB-MaxTBS-r14

This field indicates whether the UE supports the maximum UL TBS size of 2984 bits in 1.4 MHz when operating in coverage enhancement mode A, as specified in TS 36.212 [26] and TS 36.213 [22]. A UE indicating support of ce-PUSCH-NB-MaxTBS-r14 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.64 ce-PDSCH-PUSCH-MaxBandwidth-r14

This field indicates support of a maximum PDSCH/PUSCH channel bandwidth larger than 1.4 MHz when the UE is operating in coverage enhancement mode A and B, as specified in TS 36.212 [26] and TS 36.213 [22]. The maximum supported PDSCH channel bandwidth in coverage enhancement mode A and B is indicated by ce-PDSCH-PUSCH-MaxBandwidth-r14. The maximum supported PUSCH channel bandwidth is 5 MHz in coverage enhancement mode A and 1.4 MHz in coverage enhancement mode B. This field is not applicable for UEs of Category M1. This field is mandatory for UEs of Category M2. A UE indicating support of ce-PDSCH-PUSCH-MaxBandwidth-r14 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.65 ce-HARQ-AckBundling-r14

This field indicates whether the UE supports HARQ-ACK bundling in FDD when operating in coverage enhancement mode A, as specified in TS 36.212 [26] and TS 36.213 [22]. A UE indicating support of ce-HARQ-AckBundling-r14 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.66 ce-PDSCH-TenProcesses-r14

This field indicates whether the UE supports 10 DL HARQ processes in FDD when operating in coverage enhancement mode A, as specified in TS 36.212 [26] and TS 36.213 [22]. A UE indicating support of ce-PDSCH-TenProcesses-r14 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.67 ce-RetuningSymbols-r14

This field indicates the number of retuning symbols used by the UE when operating in coverage enhancement mode A and B, as specified in TS 36.211 [17]. A UE indicating support of ce-RetuningSymbols-r14 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.68 ce-PDSCH-PUSCH-Enhancement-r14

This field indicates whether the UE supports new numbers of repetitions for PUSCH and modulation restriction for PDSCH and PUSCH in coverage enhancement mode A, as specified in TS 36.212 [26] and TS 36.213 [22]. A UE indicating support of ce-PDSCH-PUSCH-Enhancement-r14 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.69 ce-SchedulingEnhancement-r14

This field indicates whether the UE supports dynamic HARQ-ACK delay for HD-FDD in coverage enhancement mode A, as specified in TS 36.212 [26] and TS 36.213 [22]. A UE indicating support of ce-SchedulingEnhancement-r14 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.70 ce-SRS-Enhancement-r14

This field indicates whether the UE supports SRS coverage enhancement with support of SRS combs 2 and 4, as specified in TS 36.213 [22]. A UE indicating support of ce-SRS-Enhancement-r14 shall also indicate support of ce-ModeA-r13 and shall not indicate support of ce-SRS-EnhancementWithoutComb4-r14.

#### 4.3.4.70A ce-SRS-EnhancementWithoutComb4-r14

This field indicates whether the UE supports SRS coverage enhancement with support of SRS comb 2 but without support of SRS comb 4, as specified in TS 36.213 [22]. A UE indicating support of ce-SRS-EnhancementWithoutComb4-r14 shall also indicate support of ce-ModeA-r13 and shall not indicate support of ce-SRS-Enhancement-r14.

#### 4.3.4.71 ce-PUCCH-Enhancement-r14

This field indicates whether the UE supports repetition levels 64 and 128 for PUCCH in CE Mode B, as specified in TS 36.211 [17] and in TS 36.213 [22]. A UE indicating support of ce-PUCCH-Enhancement-r14 shall also indicate support of ce-ModeB-r13.

#### 4.3.4.72 ce-ClosedLoopTxAntennaSelection-r14

This field indicates whether the UE supports UL closed-loop Tx antenna selection in coverage enhancement mode A, as specified in TS 36.212 [26]. A UE indicating support of ce-ClosedLoopTxAntennaSelection-r14 shall also indicate support of ce-ModeA-r13 and ue-TxAntennaSelectionSupported.

#### 4.3.4.73 ul-256QAM-r14

This field indicates UL 256QAM support by the UE on a single component carrier within a band combination (i.e. bandwith class A).

#### 4.3.4.73A ul-256QAM-r15

This field indicates whether the UE supports UL 256QAM for MR-DC within the indicated feature set. This field is reported per component carrier in a bandwidth class (A,B, C, D and so on) for a band in a given band combination.

#### 4.3.4.74 alternativeTBS-Index-r14

This field defines whether alternative TBS index ITBS 33B as specified in TS 36.213 [22] is supported by the UE. Support of the alternative TBS index ITBS 33B is applied for the UE supporting 256QAM in DL.

#### 4.3.4.75 multiCarrier-NPRACH-r14

This field defines whether the UE supports NPRACH on non-anchor carrier, as specified in TS 36.321 [4] and TS 36.331 [5]. This field is only applicable for UEs of any ue-Category-NB. It is mandatory for UEs of this release of the specification.

#### 4.3.4.76 multiCarrierPaging-r14

This field defines whether the UE supports paging on non-anchor carriers for FDD, as specified in TS 36.331 [5] and TS 36.304 [14]. This field is only applicable for UEs of any ue-Category-NB. It is mandatory for UEs of this release of the specification.

#### 4.3.4.77 ul-256QAM-perCC-InfoListr14

This field indicates UL 256QAM support by the UE on a single component carrier within a band combination, which the corresponding bandwidth class includes multiple serving carriers (i.e. bandwidth class B, C, D and so on).

#### 4.3.4.78 unicast-fembmsMixedSCell-r14

This field defines whether unicast reception from FeMBMS/Unicast mixed cell is supported by the UE. This field is included only if UE supports carrier aggregation.

#### 4.3.4.79 emptyUnicastRegion-r14

This field defines whether the UE supports unicast reception in subframes with empty unicast control region as described in TS 36.213 [22], clause 12. This field is included only if UE supports unicast reception from FeMBMS/Unicast mixed cell.

#### 4.3.4.80 interferenceRandomisation-r14

This field indicates whether the UE supports interference randomisation in connected mode for FDD as specified in TS 36.211 [17]. This field is only applicable for UEs of any ue-Category-NB. It is mandatory for UEs of this release of the specification.

#### 4.3.4.81 must-CapabilityPerBand-r14

This field indicates that the UE supports multi-user superposition transmission operation for the corresponding frequency band as specified in 36.212 [26], clause 5.3.3.1. UE indicates the support of the different MUST features per band.

##### 4.3.4.81.1 must-TM234-UpTo2Tx-r14

This field indicates that the UE supports MUST operation for TM2/3/4 using up to 2Tx.

##### 4.3.4.81.2 must-TM89-UpToOneInterferingLayer-r14

This field indicates that the UE supports MUST operation for TM8/9 with assistance information for up to 1 interfering layer.

##### 4.3.4.81.3 must-TM10-UpToOneInterferingLayer-r14

This field indicates that the UE supports MUST operation for TM10 with assistance information for up to 1 interfering layer.

##### 4.3.4.81.4 must-TM89-UpToThreeInterferingLayers-r14

This field indicates that the UE supports MUST operation for TM8/9 with assistance information for up to 3 interfering layers.

##### 4.3.4.81.5 must-TM10-UpToThreeInterferingLayers-r14

This field indicates that the UE supports MUST operation for TM10 with assistance information for up to 3 interfering layers.

#### 4.3.4.82 crs-LessDwPTS-r14

This field defines whether the UE supports TDD special subframe configuration 10 without CRS transmission on the 5th symbol of DwPTS (i.e. ssp10-CRS-LessDwPTS) as specified in TS 36.211 [17] and TS 36.331 [5].

#### 4.3.4.83 dl-1024QAM-Slot-r15

This field indicates whether the UE supports 1024QAM in DL on the band for slot TTI operation.

#### 4.3.4.84 dl-1024QAM-SubslotTA-1-r15

This field indicates whether the UE supports 1024QAM in DL on the band for subslot TTI operation with TA set 1.

#### 4.3.4.85 dl-1024QAM-SubslotTA-2-r15

This field indicates whether the UE supports 1024QAM in DL on the band for subslot TTI operation with TA set 2.

#### 4.3.4.86 dmrs-PositionPattern-r15

This field indicates whether the UE supports uplink DMRS position pattern 'D D D' in subslot #5 with application of the 1/6 as the TBS scaling factor.

#### 4.3.4.87 dmrs-RepetitionSubslotPDSCH-r15

This field indicates whether the UE supports back-to-back 3/4-layer DMRS reception in two consecutive subslots across subframe boundary for subslot-PDSCH.

#### 4.3.4.88 dmrs-SharingSubslotPDSCH-r15

This field indicates whether the UE supports DMRS sharing in two consecutive subslots across subframe boundary for subslot-PDSCH.

#### 4.3.4.89 epdcch-SPT-differentCells-r15

This field indicates whether the UE supports EPDCCH and short processing time on different serving cells.

#### 4.3.4.90 epdcch-STTI-differentCells-r15

This field indicates whether the UE supports EPDCCH and sTTI on different serving cells.

#### 4.3.4.91 maxLayersSlotOrSubslotPUSCH-r15

This field indicates the maxiumum number of layers for slot-PUSCH or subslot-PUSCH transmission. If the UE reports maximum number of layers for UL in sTTI for a band combination using the IE CA-MIMO-ParametersUL-r15, the reported maximum number of layers shall not exceed the value indicated by this field.

#### 4.3.4.92 maxNumberUpdatedCSI-Proc-SPT-r15

This field defines, if short processing time is supported, the maximum number of CSI processes to be updated per UE which aperiodic CSI is requested for CA with more than 5CCs as specified in TS 36.213 [22] which is supported by the UE.

#### 4.3.4.93 Void

#### 4.3.4.94 numberOfBlindDecodesUSS-r15

This field defines the maximum number of blind decodes in UE specific search space in one subframe for CCs configured with sTTI operation, supported by the UE. The number of blind decodes supported by the UE is the field value X*68.

#### 4.3.4.95 pdsch-SlotSubslotPDSCH-Decoding-r15

This field defines whether the UE supports decoding of PDSCH and slot-PDSCH/subslot-PDSCH assigned with C-RNTI/SPS C-RNTI in the same subframe for a given carrier.

#### 4.3.4.96 simultaneousTx-differentTx-duration-r15

This field defines whether the UE supports simultaneous transmission of different transmission durations over different carriers. The different transmission duration can be of subframe, slot or subslot duration. A common capability is used regardless of combination of different UL transmission duration over different carriers. The capability is reported per band/band combination.

#### 4.3.4.97 slotPDSCH-TxDiv-TM8-r15

This field indicates whether the UE supports TX diversity transmission using ports 7 and 8 for TM8 for slot PDSCH.

#### 4.3.4.98 slotPDSCH-TxDiv-TM9and10-r15

This field indicates whether the UE supports TX diversity transmission using ports 7 and 8 for TM9/10 for slot PDSCH.

#### 4.3.4.99 spdcch-differentRS-types-r15

This field indicates whether the UE supports monitoring of sPDCCH on RB sets with different RS types within a TTI.

#### 4.3.4.100 spt-Parameters-r15

This field indicates the maximum number of supported CCs and the corresponding supported frame structure for short processing time. The UE capability is reported per band combination. The reported number of carriers maxNumberCCs-SPT-r15 applies to all the FS-type(s) frameStructureType-SPT-r15 supported in a given band combination.

#### 4.3.4.101 sps-CyclicShift-r15

This field indicates whether the UE supports different cyclic shift for DMRS for UL SPS using 1ms TTI.

#### 4.3.4.102 subslotPDSCH-TxDiv-TM9and10-r15

This field indicates whether the UE supports TX diversity transmission using ports 7 and 8 for TM9/10 for subslot PDSCH.

#### 4.3.4.103 sTTI-SupportedCombinations-r15

This field indicates the different combinations of sTTI lengths (slot or subslot) that the UE supports in a single PUCCH group or in two PUCCH groups. A TTI length combination is reported for DL first followed by UL. In case of two PUCCH groups the support for the primary PUCCH group is indicated first. The capability is reported per band per band combination. This field is also used to report the sTTI capabilities for non-CA bands.

#### 4.3.4.104 Void

#### 4.3.4.105 sTTI-SPT-BandParameters-r15

This field indicates the different sTTI/sPT capabilities for each band of the reported band combinations using supportedBandCombination. The UE reports these capabilities in the same order in which the band combinations are reported. The UE is allowed to report the same band combination more than once, if the corresponding sTTI/sPT capabilities are different. If any of the fields sTTI-CA-MIMO-ParametersDL-r15, sTTI-CA-MIMO-ParametersUL-r15, sTTI-SupportedCSI-Proc-r15 are not provided by the UE, the corresponding parameters of these fields reported from the band of the band combination for which the sTTI parameters are applied, are assumed to be supported for sTTI/sPT features as well. If any of the fields sTTI-MIMO-CA-ParametersPerBoBCs-r15, sTTI-MIMO-CA-ParametersPerBoBCs-v1530 are not provided by the UE, the corresponding parameters from mimo-UE-ParametersSTTI-r15, mimo-UE-ParametersSTTI-v1530 are applied, and if any of the fields mimo-UE-ParametersSTTI-r15, mimo-UE-ParametersSTTI-v1530 are not provided by the UE, then the corresponding parameters of these fields reported from the band of the band combination for which the sTTI parameters are applied, are assumed to be supported for sTTI/sPT features.

#### 4.3.4.106 sTTI-SupportedCSI-Proc-r15

This field indicates, for short TTI, the maximum number of CSI processes supported on a component carrier within a band. Value n1 corresponds to 1 CSI process, value n3 corresponds to 3 CSI processes, and value n4 corresponds to 4 CSI processes. If this field is included, the UE shall include the same number of entries listed in the same order as in bandParameterList-r11, bandParameterList-r13 if they are reported. If the UE supports at least 1 CSI process on any component carrier, then the UE shall include this field in all bands in all band combinations.

#### 4.3.4.107 txDiv-SPUCCH-r15

This field defines whether the UE supports Tx diversity on SPUCCH format 1, 1a, 1b and 3.

#### 4.3.4.108 ul-256QAM-Slot-r15

This field defines whether the UE supports 256QAM in UL for slot TTI operation on the band.

#### 4.3.4.109 ul-256QAM-Subslot-r15

This field defines whether the UE supports 256QAM in UL for subslot TTI operation on the band.

#### 4.3.4.110 ue-TxAntennaSelection-SRS-1T4R-r15

This field indicates whether the UE supports to select one antenna among four antennas to transmit SRS for the corresponding band of the band combination as described in TS 36.213 [22].

#### 4.3.4.111 ue-TxAntennaSelection-SRS-2T4R-2Pairs-r15

This field indicates whether the UE supports to select one antenna pair between two antenna pairs to transmit SRS simultaneously for the corresponding band of the band combination as described in TS 36.213 [22].

#### 4.3.4.112 ue-TxAntennaSelection-SRS-2T4R-3Pairs-r15

This field indicates whether the UE supports to select one antenna pair among three antenna pairs to transmit SRS simultaneously for the corresponding band of the band combination as described in TS 36.213 [22].

#### 4.3.4.113 wakeUpSignal-r15

This field indicates whether the UE supports WUS for FDD as specified in TS 36.211 [17], TS 36.213 [22] and TS 36.304 [14]. This feature is only applicable if the UE supports ce-ModeA-r13 or if the UE supports any ue-Category-NB.

#### 4.3.4.114 wakeUpSignalMinGap-eDRX-r15

This field indicates the minimum gap required between end of WUS and start of PO by a UE indicating support of extended idle mode DRX for FDD, as specified in TS 24.301 [28]. A UE indicating support of wakeUpSignalMinGap-eDRX-r15 shall also indicate support of wakeUpSignal-r15 or groupWakeUpSignal-r16. This feature is only applicable if the UE supports ce-ModeA-r13 or if the UE supports any ue-Category-NB.

#### 4.3.4.115 mixedOperationMode-r15

This field defines whether the UE supports multi-carrier operation where the anchor carrier is in standalone mode while the non-anchor carrier is in inband or guardand mode, and vice versa, for unicast, paging, and random access for FDD as specified in TS 36.300 [30]. This field is only applicable for UEs of any ue-Category-NB.

#### 4.3.4.116 void

#### 4.3.4.117 sr-WithHARQ-ACK-r15

This field defines whether the UE supports physical layer SR with HARQ ACK for FDD as specified in TS 36.213 [22]. This field is only applicable for UEs of any ue-Category-NB.

#### 4.3.4.118 sr-WithoutHARQ-ACK-r15

This field defines whether the UE supports physical layer SR without HARQ ACK for FDD as specified in TS 36.211 [17] and TS 36.213 [22]. This field is only applicable for UEs of any ue-Category-NB.

#### 4.3.4.119 nprach-Format2-r15

This field defines whether the UE supports NPRACH resources using preamble format 2 for FDD. This field is only applicable for UEs of any ue-Category-NB.

#### 4.3.4.120 ce-UL-HARQ-ACK-Feedback-r15

This field indicates whether the UE supports uplink HARQ ACK Feedback in RRC_CONNECTED when operating in coverage enhancement, as specified in TS 36.213 [22]. A UE indicating support of ce-UL-HARQ-ACK-Feedback-r15 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.121 ce-PDSCH-FlexibleStartPRB-CE-ModeA-r15

This field indicates whether the UE supports flexible starting PRB for PDSCH in RRC_CONNECTED when operating in coverage enhancement mode A, as specified in TS 36.211 [17] and TS 36.213 [22]. A UE indicating support of ce-PDSCH-FlexibleStartPRB-CE-ModeA-r15 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.122 ce-PDSCH-FlexibleStartPRB-CE-ModeB-r15

This field indicates whether the UE supports flexible starting PRB for PDSCH in RRC_CONNECTED when operating in coverage enhancement mode B, as specified in TS 36.211 [17] and TS 36.213 [22]. A UE indicating support of ce-PDSCH-FlexibleStartPRB-CE-ModeB-r15 shall also indicate support of ce-ModeB-r13.

#### 4.3.4.123 ce-PUSCH-FlexibleStartPRB-CE-ModeA-r15

This field indicates whether the UE supports flexible starting PRB for PUSCH in RRC_CONNECTED when operating in coverage enhancement mode A, as specified in TS 36.211 [17] and TS 36.213 [22]. A UE indicating support of ce-PUSCH-FlexibleStartPRB-CE-ModeA-r15 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.124 ce-PUSCH-FlexibleStartPRB-CE-ModeB-r15

This field indicates whether the UE supports flexible starting PRB for PUSCH in RRC_CONNECTED when operating in coverage enhancement mode B, as specified in TS 36.211 [17] and TS 36.213 [22]. A UE indicating support of ce-PUSCH-FlexibleStartPRB-CE-ModeB-r15 shall also indicate support of ce-ModeB-r13.

#### 4.3.4.125 ce-CRS-IntfMitig-r15

This field indicates whether the UE supports CRS interference mitigation, i.e., value supported indicates UE does not rely on the CRS outside certain PRBs and subframes as defined in TS 36.133 [16], clauses 3.6.1.2 and 3.6.1.3 and TS 36.213 [23] when operating in coverage enhancement mode. A UE indicating support of ce-CRS-IntfMitig-r15 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.126 ce-PDSCH-64QAM-r15

This field indicates whether the UE supports 64QAM for non-repeated unicast PDSCH in RRC_CONNECTED when operating in coverage enhancement mode A. A UE indicating support of ce-PDSCH-64QAM-r15 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.127 ce-CQI-AlternativeTable-r15

This field indicates whether the UE supports alternative CQI table in RRC_CONNECTED when operating in coverage enhancement mode A, as specified in TS 36.213 [22]. A UE indicating support of ce-CQI-AlternativeTable-r15 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.128 ce-PUSCH-SubPRB-Allocation-r15

This field indicates whether the UE supports sub-PRB resource allocation for PUSCH when operating in coverage enhancement mode A or B, as specified in TS 36.211 [17] and TS 36.213 [22]. A UE indicating support of ce-PUSCH-SubPRB-Allocation-r15 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.129 wakeUpSignal-TDD-r15

This field indicates whether the UE supports WUS for TDD as specified in TS 36.211 [17], TS 36.213 [22] and TS 36.304 [14]. This feature is only applicable if the UE supports ce-ModeA-r13.

#### 4.3.4.130 wakeUpSignalMinGap-eDRX-TDD-r15

This field indicates the minimum gap required between end of WUS and start of PO by a UE indicating support of extended idle mode DRX for TDD, as specified in TS 24.301 [28]. A UE indicating support of wakeUpSignalMinGap-eDRX-TDD-r15 shall also indicate support of wakeUpSignal-TDD-r15 or groupWakeUpSignalTDD-r16.

#### 4.3.4.131 shortCqi-ForSCellActivation-r15

This field defines whether the UE supports temporary CQI reporting periodicity after SCell activation as defined in TS 36.321 [4] and TS 36.331 [5].

#### 4.3.4.132 crs-IntfMitig-r15

This field defines whether the UE supports CRS interference mitigation as specified in TS 36.133 [16], clause 3.6.1.1.

#### 4.3.4.133 srs-UpPTS-6sym-r14

This field indicates whether the UE supports up to 6-symbol SRS in UpPTS.

#### 4.3.4.134 multiCarrierPagingTDD-r15

This field defines whether the UE supports paging on non-anchor carriers for TDD, as specified in TS 36.331 [5] and TS 36.304 [14]. This field is only applicable for UEs of any ue-Category-NB. It is mandatory for UEs of this release of the specification.

#### 4.3.4.135 altMCS-Table-r15

This field defines whether the UE supports 6-bit MCS table, see TS 36.212 [26] and TS 36.213 [22].

#### 4.3.4.136 ul-PowerControlEnhancements-r15

This field defines whether the UE supports UE specific UL power control.

#### 4.3.4.137 additionalTransmissionSIB1-r15

This field defines whether the UE supports additional SIB1 transmission in subframe #3 for FDD, as defined in TS 36.213 [22]. This field is only applicable for UEs of any ue-Category-NB.

#### 4.3.4.138 aperiodicCsi-ReportingSTTI-r15

This field defines whether the UE supports aperiodic CSI reporting for STTI.If the UE indicates the support of aperiodic CSI reporting for short TTI using this field, the UE also supports the legacy aperiodic CSI capabilities for short TTI.

#### 4.3.4.139 dmrs-BasedSPDCCH-MBSFN-r15

This field defines whether the UE supports sDCI monitoring in DMRS based SPDCCH for MBSFN subframe. If UE supports this, it also provides the corresponding DMRS based SPDCCH capability in min-Proc-TimelineSubslot.

#### 4.3.4.140 dmrs-BasedSPDCCH-nonMBSFN -r15

This field defines whether the UE supports sDCI monitoring in DMRS based SPDCCH for non-MBSFN subframe. If UE supports this, it also provides the corresponding DMRS based SPDCCH capability in min-Proc-TimelineSubslot

#### 4.3.4.141 maxNumberUpdatedCSI-Proc-STTI-Comb77-r15

This field defines, for {slot, slot}, if short TTI specific A-CSI reporting is supported, the maximum number of CSI processes to be updated per UE which aperiodic CSI is requested for CA with more than 2CCs as specified in TS 36.213 [22] which is supported by the UE.

#### 4.3.4.142 maxNumberUpdatedCSI-Proc-STTI-Comb27-r15

This field defines, for {subslot, slot}, if short TTI specific A-CSI reporting is supported, the maximum number of CSI processes to be updated per UE which aperiodic CSI is requested for CA with more than 2CCs as specified in TS 36.213 [22] which is supported by the UE.

#### 4.3.4.143 maxNumberUpdatedCSI-Proc-STTI-Comb22-Set1-r15

This field defines, for {subslot, subslot} set 1, if short TTI specific A-CSI reporting is supported, the maximum number of CSI processes to be updated per UE which aperiodic CSI is requested for CA with more than 2CCs as specified in TS 36.213 [22] which is supported by the UE.

#### 4.3.4.144 maxNumberUpdatedCSI-Proc-STTI-Comb22-Set2-r15

This field defines, for {subslot, subslot} set 2, if short TTI specific A-CSI reporting is supported, the maximum number of CSI processes to be updated per UE which aperiodic CSI is requested for CA with more than 2CCs as specified in TS 36.213 [22] which is supported by the UE.

#### 4.3.4.145 powerUCI-SlotPUSCH-r15

This field Indicates whether the UE supports BPRE derivation based on the actual derived O_CQI. The parameter uplinkPower-CSIPayload configures the UE to derive BPRE based on either the actual value of O_CQI or the largest value of O_CQI across all RI values. If the UE does not support the capability, the UE will derive BPRE based on the largest value of O_CQI across all RI values.

#### 4.3.4.146 powerUCI-SubslotPUSCH-r15

This field indicates whether the UE supports BPRE derivation based on the actual derived O_CQI. The parameter uplinkPower-CSIPayload configures the UE to derive BPRE based on either the actual value of O_CQI or the largest value of O_CQI across all RI values. If the UE does not support the capability, the UE will derive BPRE based on the largest value of O_CQI across all RI values.

#### 4.3.4.147 spdcch-Reuse-r15

This field indicates whether the UE supports L1 based SPDCCH reuse.

#### 4.3.4.148 sps-STTI-r15

This field indicates whether the UE supports SPS in DL and/or UL for slot or subslot based PDSCH and PUSCH, respectively.

#### 4.3.4.149 sTTI-FD-MIMO-Coexistence-r15

This field indicates whether the UE supports CSI feedback for more than 8 NZP CSI-RS ports on subframe based PUSCH in any serving cell and supporting sTTI in any serving cell.

#### 4.3.4.150 sTTI-SPT-Supported-r15

This field indicates whether the UE supports short TTI and/or short processing time features.

#### 4.3.4.151 tm8-slotPDSCH-r15

This field indicates whether the UE supports configuration and decoding of TM8 for slot PDSCH in TDD.

#### 4.3.4.152 tm9-slotSubslot-r15

This field indicates whether the UE supports configuration and decoding of TM9 for slot and/or subslot PDSCH for non-MBSFN.

#### 4.3.4.153 tm9-slotSubslotMBSFN-r15

This field indicates whether the UE supports configuration and decoding of TM9 for slot and/or subslot PDSCH for MBSFN.

#### 4.3.4.154 tm10-slotSubslot-r15

This field indicates whether the UE supports configuration and decoding of TM10 for slot and/or subslot PDSCH for non-MBSFN.

#### 4.3.4.155 tm10-slotSubslotMBSFN-r15

This field indicates whether the UE supports configuration and decoding of TM10 for slot and/or subslot PDSCH for MBSFN.

#### 4.3.4.156 ul-AsyncHarqSharingDiff-TTI-Lengths-r15

This field indicates whether the UE supports UL asynchronous HARQ sharing between different TTI lengths for an UL serving cell.

#### 4.3.4.157 semiStaticCFI-r15

This field indicates whether the UE supports the semi-static configuration of CFI for subframe/slot/sub-slot operation.

#### 4.3.4.158 semiStaticCFI-Pattern-r15

This field indicates whether the UE supports the semi-static configuration of CFI pattern for subframe/slot/sub-slot operation. This field is only applicable for UEs supporting TDD.

#### 4.3.4.159 pdsch-RepSubframe-r15

This field indicates whether the UE supports subframe PDSCH repetition. A UE indicating support of pdsch-RepSubframe-r15 shall also indicate support of semiStaticCFI-r15 or semiStaticCFI-Pattern-r15.

#### 4.3.4.160 pdsch-RepSlot-r15

This field indicates whether the UE supports slot PDSCH repetition. A UE indicating support of pdsch-RepSlot-r15 shall also indicate support of semiStaticCFI-r15 or semiStaticCFI-Pattern-r15. A UE indicating support of pdsch-RepSlot-r15 shall also indicate support of rel-15 slot PDSCH.

#### 4.3.4.161 pdsch-RepSubslot-r15

This field indicates whether the UE supports subslot PDSCH repetition. This field is only applicable for UEs supporting FDD. A UE indicating support of pdsch-RepSubslot-r15 shall also indicate support of semiStaticCFI-r15. A UE indicating support of pdsch-RepSlot-r15 shall also indicate support of rel-15 subslot PDSCH.

#### 4.3.4.162 pusch-SPS-SubframeRepPCell-r15

This field indicates whether the UE supports SPS repetition for subframe PUSCH for PCell. A UE indicating support of pusch-SPS-SubFrameRepPCell-r15 shall also indicate support of semiStaticCFI-r15 or semiStaticCFI-Pattern-r15.

#### 4.3.4.163 pusch-SPS-SubframeRepPSCell-r15

This field indicates whether the UE supports SPS repetition for subframe PUSCH for PSCell. A UE indicating support of pusch-SPS-SubframeRepPSCell-r15 shall also indicate support of semiStaticCFI-r15 or semiStaticCFI-Pattern-r15.

#### 4.3.4.164 pusch-SPS-SubframeRepSCell-r15

This field indicates whether the UE supports SPS repetition for subframe PUSCH for serving cells other than SpCell. A UE indicating support of pusch-SPS-SubframeRepSCell-r15 shall also indicate support of semiStaticCFI-r15 or semiStaticCFI-Pattern-r15.

#### 4.3.4.165 pusch-SPS-SlotRepPCell-r15

This field indicates whether the UE supports SPS repetition for slot PUSCH for PCell. A UE indicating support of pusch-SPS-SlotRepPCell-r15 shall also indicate support of semiStaticCFI-r15 or semiStaticCFI-Pattern-r15. A UE indicating support of pusch-SPS-SlotRepPCell-r15 shall also indicate support of slot PUSCH and SPS for slot PUSCH.

#### 4.3.4.166 pusch-SPS-SlotRepPSCell-r15

This field indicates whether the UE supports SPS repetition for slot PUSCH for PSCell. A UE indicating support of pusch-SPS-SlotRepPSCell-r15 shall also indicate support of semiStaticCFI-r15 or semiStaticCFI-Pattern-r15. A UE indicating support of pusch-SPS-SlotRepPSCell-r15 shall also indicate support of slot PUSCH and SPS for slot PUSCH.

#### 4.3.4.167 pusch-SPS-SlotRepSCell-r15

This field indicates whether the UE supports SPS repetition for slot PUSCH for serving cells other than SpCell. A UE indicating support of pusch-SPS-SlotRepSCell-r15 shall also indicate support of semiStaticCFI-r15 or semiStaticCFI-Pattern-r15. A UE indicating support of pusch-SPS-SlotRepSCell-r15 shall also indicate support of slot PUSCH and SPS for slot PUSCH.

#### 4.3.4.168 pusch-SPS-SubslotRepPCell-r15

This field indicates whether the UE supports SPS repetition for subslot PUSCH for PCell. This field is only applicable for UEs supporting FDD. A UE indicating support of pusch-SPS-SubslotRepPCell-r15 shall also indicate support of semiStaticCFI-r15. A UE indicating support of pusch-SPS-SubslotRepPCell-r15 shall also indicate support of subslot PUSCH and SPS for subslot PUSCH.

#### 4.3.4.169 pusch-SPS-SubslotRepPSCell-r15

This field indicates whether the UE supports SPS repetition for subslot PUSCH for PSCell. This field is only applicable for UEs supporting FDD. A UE indicating support of pusch-SPS-SubslotRepPSCell-r15 shall also indicate support of semiStaticCFI-r15. A UE indicating support of pusch-SPS-SubslotRepPSCell-r15 shall also indicate support of subslot PUSCH and SPS for subslot PUSCH.

#### 4.3.4.170 pusch-SPS-SubslotRepSCell-r15

This field indicates whether the UE supports SPS repetition for subslot PUSCH for serving cells other than SpCell. This field is only applicable for UEs supporting FDD. A UE indicating support of pusch-SPS-SubSlotRepSCell-r15 shall also indicate support of semiStaticCFI-r15. A UE indicating support of pusch-SPS-SubslotRepSCell-r15 shall also indicate support of subslot PUSCH and SPS for subslot PUSCH.

#### 4.3.4.171 pusch-SPS-MaxConfigSubframe-r15

This field indicates the maximum number of multiple SPS configurations of subframe PUSCH across all cells.

#### 4.3.4.172 pusch-SPS-MultiConfigSubframe-r15

This field indicates the number of multiple SPS configurations of slot PUSCH for each serving cell. A UE indicating support of pusch-SPS-MultiConfigSubframe-r15 shall also indicate support of pusch-SPS-SubframeRepPCell-r15, pusch-SPS-SubframeRepPSCell-r15 or pusch-SPS-SubframeRepSCell-r15.

#### 4.3.4.173 pusch-SPS-MaxConfigSlot-r15

This field indicates the maximum number of multiple SPS configurations of slot PUSCH across all cells.

#### 4.3.4.174 pusch-SPS-MultiConfigSlot-r15

This field indicates the number of multiple SPS configurations of subframe PUSCH for each serving cell. A UE indicating support of pusch-SPS-MultiConfigSlot-r15 shall also indicate support of pusch-SPS-SlotRepPCell-r15, pusch-SPS-SlotRepPSCell-r15 or pusch-SPS-SlotRepSCell-r15.

#### 4.3.4.175 pusch-SPS-MaxConfigSubslot-r15

This field indicates the maximum number of multiple SPS configurations of subslot PUSCH across all cells.

#### 4.3.4.176 pusch-SPS-MultiConfigSubslot-r15

This field indicates the number of multiple SPS configurations of subslot PUSCH for each serving cell. This field is only applicable for UEs supporting FDD. A UE indicating support of pusch-SPS-MultiConfigSubslot-r15 shall also indicate support of pusch-SPS-SubslotRepPCell-r15, pusch-SPS-SubslotRepPSCell-r15 or pusch-SPS-SubslotRepSCell-r15.

#### 4.3.4.177 npusch-3dot75kHz-SCS-TDD-r15

This field defines whether the UE supports NPUSCH with 3.75kHz SCS for TDD as specified in TS 36.211 [17]. This field is only applicable for UEs of any ue-Category-NB. It is mandatory for UEs of this release of the specification.

#### 4.3.4.178 crs-IM-TM1-toTM9-OneRX-Port

1) The field defines whether the DL Category 1bis UE or the DL Category M2 UE supports any of the below CRS interference mitigation (CRS-IM) features while operating in the following transmission modes (TM): TM 1, TM 2, …, TM 8 and TM 9. CRS-IM with 2 CRS antenna ports for PDSCH with 1 receiver antenna port (as specified in TS 36.101 [6]).

2) CRS-IM with 4 CRS antenna ports for PDSCH with 1 receiver antenna port (as specified in TS 36.101 [6]).

The UE shall not include the field if it does not support CRS IM in TMs 1-9.

#### 4.3.4.179 cch-IM-RefRecTypeA-OneRX-Port

The field defines whether the DL Category 1bis UE or DL Category M2 UE supports Type A downlink control channel interference mitigation receiver "LMMSE-IRC + CRS-IC" for PDCCH/PCFICH/PHICH/EPDCCH receive processing (Enhanced downlink control channel performance requirements Type A in TS 36.101 [6]).

For DL Category 1bis UE, if this field is present, the UE supports any of the following features:

1) Enhanced downlink control channel interference mitigation Type A receiver for 2 CRS antenna ports with 1 receiver antenna port (as specified in TS 36.101 [6]).

2) Enhanced downlink control channel interference mitigation Type A receiver for 4 CRS antenna ports with 1 receiver antenna port (as specified in TS 36.101 [6]).

For DL Category M2 UE, if this field is present, the UE supports the following feature:

1) Enhanced downlink control channel interference mitigation Type A receiver for 2 CRS antenna ports with 1 receiver antenna port (as specified in TS 36.101 [6]).

#### 4.3.4.180 dmrs-OverheadReduction-r15

This field defines whether the UE supports OCC4 for rank 3 and 4 transmission as specified in clause 5.3.3.1.5C of TS 36.212 [26].

#### 4.3.4.181 srs-DCI7-TriggeringFS2-r15

This field indicates whether the UE supports SRS triggerring via DCI format 7 for FS2.

#### 4.3.4.182 npusch-MultiTB-r16

This field indicates whether the UE supports multiple TB scheduling in the uplink for FDD as specified in TS 36.213 [22]. A UE indicating support of npusch-MultiTB-r16 shall also indicate support of twoHARQ-Processes-r14. This feature is only applicable if the UE supports category NB2.

#### 4.3.4.183 npdsch-MultiTB-r16

This field indicates whether the UE supports multiple TB scheduling in the downlink for FDD as specified in TS 36.213 [22]. A UE indicating support of npdsch-MultiTB-r16 shall also indicate support of twoHARQ-Processes-r14. This feature is only applicable if the UE supports category NB2.

#### 4.3.4.184 pusch-MultiTB-CE-ModeA-r16

This field indicates whether the UE supports multiple TB scheduling for unicast in the uplink when the UE is operating in coverage enhancement mode A as specified in TS 36.213 [22]. A UE indicating support of pusch-MultiTB-CE-ModeA-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.185 pdsch-MultiTB-CE-ModeA-r16

This field indicates whether the UE supports multiple TB scheduling for unicast in the downlink when the UE is operating in coverage enhancement mode A as specified in TS 36.213 [22]. A UE indicating support of pdsch-MultiTB-CE-ModeA-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.186 pusch-MultiTB-CE-ModeB-r16

This field indicates whether the UE supports multiple TB scheduling for unicast in the uplink when the UE is operating in coverage enhancement mode B as specified in TS 36.213 [22]. A UE indicating support of pusch-MultiTB-CE-ModeB-r16 shall also indicate support of ce-ModeB-r13.

#### 4.3.4.187 pdsch-MultiTB-CE-ModeB-r16

This field indicates whether the UE supports multiple TB scheduling for unicast in the downlink when the UE is operating in coverage enhancement mode B as specified in TS 36.213 [22]. A UE indicating support of pdsch-MultiTB-CE-ModeB-r16 shall also indicate support of ce-ModeB-r13.

#### 4.3.4.188 ce-CSI-RS-Feedback-r16

This field indicates whether the UE supports CSI-RS based feedback when the UE is operating in coverage enhancement mode A, as specified in TS 36.213 [22]. A UE indicating support of ce-CSI-RS-Feedback-r16 shall also indicate support of ce-ModeA-r13. This feature is only applicable if UE supports a UE Category other than Category M1 and M2.

#### 4.3.4.188a ce-CSI-RS-FeedbackCodebookRestriction-r16

This field indicates whether the UE supports codebook subset restriction for CSI-RS-based feedback when the UE is operating in coverage enhancement mode A, as specified in TS 36.213 [22]. A UE indicating support of ce-CSI-RS-FeedbackCodebookRestriction-r16 shall also indicate support of ce-CSI-RS-Feedback-r16.

#### 4.3.4.189 mpdcch-InLteControlRegionCE-ModeA-r16

This field indicates whether the UE supports MPDCCH reception in the LTE control channel region when the UE is operating in coverage enhancement mode A as specified in TS 36.211 [17]. A UE indicating support of mpdcch-InLteControlRegionCE-ModeA-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.189a mpdcch-InLteControlRegionCE-ModeB-r16

This field indicates whether the UE supports MPDCCH reception in the LTE control channel region when the UE is operating in coverage enhancement mode B as specified in TS 36.211 [17]. A UE indicating support of mpdcch-InLteControlRegion-CEModeB-r16 shall also indicate support of ce-ModeB-r13.

#### 4.3.4.189b pdsch-InLteControlRegionCE-ModeA-r16

This field indicates whether the UE supports PDSCH reception in the LTE control channel region when the UE is operating in coverage enhancement mode A as specified in TS 36.211 [17]. A UE indicating support of pdsch-InLteControlRegionCE-ModeA-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.189c pdsch-InLteControlRegionCE-ModeB-r16

This field indicates whether the UE supports PDSCH reception in the LTE control channel region when the UE is operating in coverage enhancement mode B as specified in TS 36.211 [17]. A UE indicating support of pdsch-InLteControlRegionCE-ModeB-r16 shall also indicate support of ce-ModeB-r13.

#### 4.3.4.190 crs-ChEstMPDCCH-CE-ModeA-r16

This field indicates whether the UE supports MPDCCH performance improvement with precoder cycling when the UE is operating in coverage enhancement mode A, as specified in TS 36.211 [17]. A UE indicating support of crs-ChEstMPDCCH-CE-ModeA-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.190a crs-ChEstMPDCCH-CE-ModeB-r16

This field indicates whether the UE supports MPDCCH performance improvement with precoder cycling when the UE is operating in coverage enhancement mode B, as specified in TS 36.211 [17]. A UE indicating support of crs-ChEstMPDCCH-CE-ModeB-r16 shall also indicate support of ce-ModeB-r13.

#### 4.3.4.190b crs-ChEstMPDCCH-CSI-r16

This field indicates whether the UE supports MPDCCH performance improvement with CSI-based mapping when the UE is operating in coverage enhancement mode A, as specified in TS 36.211 [17]. A UE indicating support of crs-ChEstMPDCCH-CSI-r16 shall also indicate support of crs-ChEstMPDCCH-CE-ModeA-r16.

#### 4.3.4.190c crs-ChEstMPDCCH-ReciprocityTDD-r16

This field indicates whether the UE supports MPDCCH performance improvement with reciprocity-based candidates for TDD when the UE is operating in coverage enhancement mode A, as specified in TS 36.211 [17]. A UE indicating support of crs-ChEstMPDCCH-ReciprocityTDD-r16 shall also indicate support of crs-ChEstMPDCCH-CE-ModeA-r16.

#### 4.3.4.191 widebandPRG-Slot-r16, widebandPRG-Subslot-r16, widebandPRG-Subframe-r16

This field indicates whether the UE supports wideband precoding resource block group size for slot/subslot/subframe PDSCH operation as specified in TS 36.213 [22].

#### 4.3.4.192 npusch-MultiTB-Interleaving-r16

This field indicates whether the UE supports interleaved transmissions when multiple TB scheduling is scheduled in the uplink for NB-IoT FDD as specified in TS 36.213 [22]. A UE indicating support of npusch-MultiTB-Interleaving-r16 shall also indicate support of twoHARQ-Processes-r14. This feature is only applicable if the UE supports category NB2.

#### 4.3.4.193 npdsch-MultiTB-Interleaving-r16

This field indicates whether the UE supports interleaved transmissions when multiple TB scheduling is scheduled in the downlink for NB-IoT FDD as specified in TS 36.213 [22]. A UE indicating support of npdsch-MultiTB-Interleaving-r16 shall also indicate support of twoHARQ-Processes-r14. This feature is only applicable if the UE supports category NB2.

#### 4.3.4.194 multiTB-HARQ-AckBundling-r16

This field indicates whether the UE supports HARQ ACK bundling for interleaved transmission in the downlink for NB-IoT FDD as specified in TS 36.213 [22]. A UE indicating support of multiTB-HARQ-AckBundling-r16 shall also indicate support of npdsch-multiTB-Interleaving-r16. This feature is only applicable if the UE supports category NB2.

#### 4.3.4.195 groupWakeUpSignal-r16

This field indicates whether the UE supports Group WUS without group resource alternation for FDD in RRC_IDLE as specified in TS 36.211 [17], TS 36.213 [22] and TS 36.304 [14]. This feature is only applicable if the UE supports ce-ModeA-r13 or if the UE supports any ue-Category-NB.

#### 4.3.4.196 groupWakeUpSignalAlternation-r16

This field indicates whether the UE supports Group WUS with group resource alternation for FDD in RRC_IDLE as specified in TS 36.211 [17], TS 36.213 [22] and TS 36.304 [14]. A UE indicating support of groupWakeUpSignalAlternation-r16 shall also indicate support of groupWakeUpSignal-r16. This feature is only applicable if the UE supports ce-ModeA-r13 or if the UE supports any ue-Category-NB.

#### 4.3.4.197 subframeResourceResvUL-r16

This field indicates whether the UE supports UL resource reservation with subframe-level granularity on non-anchor carriers e.g. for NB-IoT coexistence with NR, as specified in TS 36.211 [17]. This feature is only applicable if the UE supports any ue-Category-NB.

#### 4.3.4.198 subframeResourceResvDL-r16

This field indicates whether the UE supports DL resource reservation with subframe-level granularity on non-anchor carriers e.g. for NB-IoT coexistence with NR, as specified in TS 36.211 [17]. This feature is only applicable if the UE supports any ue-Category-NB.

#### 4.3.4.199 slotSymbolResourceResvUL-r16

This field indicates whether the UE supports UL resource reservation with slot-level granularity on non-anchor carriers e.g. for NB-IoT coexistence with NR, as specified in TS 36.211[17]. A UE indicating support of slotSymbolResourceResvUL-r16 shall also indicate support of subframeResourceResvUL-r16. This feature is only applicable if the UE supports any ue-Category-NB.

#### 4.3.4.200 slotSymbolResourceResvDL-r16

This field indicates whether the UE supports DL resource reservation with slot-level granularity on non-anchor carriers e.g. for NB-IoT coexistence with NR, as specified in TS 36.211[17]. A UE indicating support of slotSymbolResourceResvDL-r16 shall also indicate support of subframeResourceResvDL-r16. This feature is only applicable if the UE supports any ue-Category-NB.

#### 4.3.4.201 groupWakeUpSignalTDD-r16

This field indicates whether the UE supports Group WUS without group resource alternation for TDD in RRC_IDLE as specified in TS 36.211 [17], TS 36.213 [22] and TS 36.304 [14]. A UE indicating support of groupWakeUpSignalTDD-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.202 groupWakeUpSignalAlternationTDD-r16

This field indicates whether the UE supports Group WUS with group resource alternation for TDD in RRC_IDLE as specified in TS 36.211 [17], TS 36.213 [22] and TS 36.304 [14]. A UE indicating support of groupWakeUpSignalAlternationTDD-r16 shall also indicate support of groupWakeUpSignalTDD-r16.

#### 4.3.4.203 subframeResourceResvUL-CE-ModeA-r16

This field indicates whether the UE supports UL resource reservation with subframe-level granularity e.g. for coexistence with NR when the UE is operating in coverage enhancement mode A, as specified in TS 36.211 [17]. A UE indicating support of subframeResourceResvUL-CE-ModeA-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.204 subframeResourceResvUL-CE-ModeB-r16

This field indicates whether the UE supports UL resource reservation with subframe-level granularity e.g. for coexistence with NR when the UE is operating in coverage enhancement mode B, as specified in TS 36.211 [17]. A UE indicating support of subframeResourceResvUL-CE-ModeB-r16 shall also indicate support of ce-ModeB-r13.

#### 4.3.4.205 subframeResourceResvDL-CE-ModeA-r16

This field indicates whether the UE supports DL resource reservation with subframe-level granularity e.g. for coexistence with NR when the UE is operating in coverage enhancement mode A, as specified in TS 36.211 [17]. A UE indicating support of subframeResourceResvDL-CE-ModeA-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.206 subframeResourceResvDL-CE-ModeB-r16

This field indicates whether the UE supports DL resource reservation with subframe-level granularity e.g. for coexistence with NR when the UE is operating in coverage enhancement mode B, as specified in TS 36.211 [17]. A UE indicating support of subframeResourceResvDL-CE-ModeB-r16 shall also indicate support of ce-ModeB-r13.

#### 4.3.4.207 slotSymbolResourceResvUL-CE-ModeA-r16

This field indicates whether the UE supports UL resource reservation with slot/symbol-level granularity e.g. for coexistence with NR when the UE is operating in coverage enhancement mode A, as specified in TS 36.211 [17]. A UE indicating support of slotSymbolResourceResvUL-CE-ModeA-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.208 slotSymbolResourceResvUL-CE-ModeB-r16

This field indicates whether the UE supports UL resource reservation with slot/symbol-level granularity e.g. for coexistence with NR when the UE is operating in coverage enhancement mode B, as specified in TS 36.211 [17]. A UE indicating support of slotSymbolResourceResvUL-CE-ModeB-r16 shall also indicate support of ce-ModeB-r13.

#### 4.3.4.209 slotSymbolResourceResvDL-CE-ModeA-r16

This field indicates whether the UE supports DL resource reservation with slot/symbol-level granularity e.g. for coexistence with NR when the UE is operating in coverage enhancement mode A, as specified in TS 36.211 [17]. A UE indicating support of slotSymbolResourceResvDL-CE-ModeA-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.210 slotSymbolResourceResvDL-CE-ModeB-r16

This field indicates whether the UE supports DL resource reservation with slot/symbol-level granularity e.g. for coexistence with NR when the UE is operating in coverage enhancement mode B, as specified in TS 36.211 [17]. A UE indicating support of slotSymbolResourceResvDL-CE-ModeB-r16 shall also indicate support of ce-ModeB-r13.

#### 4.3.4.211 subcarrierPuncturingCE-ModeA-r16

This field indicates whether the UE supports DL subcarrier puncturing e.g. for coexistence with NR when the UE is operating in coverage enhancement mode A, as specified in TS 36.211 [17]. A UE indicating support of subcarrierPuncturing-CE-ModeA-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.212 subcarrierPuncturingCE-ModeB-r16

This field indicates whether the UE supports DL subcarrier puncturing e.g. for coexistence with NR when the UE is operating in coverage enhancement mode B, as specified in TS 36.211 [17]. A UE indicating support of subcarrierPuncturing-CE-ModeA-r16 shall also indicate support of ce-ModeB-r13.

#### 4.3.4.213 ce-MultiTB-Interleaving-r16

This field indicates whether the UE supports multiple TB scheduling for unicast with TB interleaving as specified in TS 36.213 [22]. A UE indicating support of ce-MultiTB-Interleaving-r16 shall also indicate support of pusch-MultiTB-CE-ModeA-r16 or pdsch-MultiTB-CE-ModeA-r16 or pusch-MultiTB-CE-ModeB-r16 or pdsch-MultiTB-CE-ModeB-r16.

#### 4.3.4.214 ce-MultiTB-HARQ-AckBundling-r16

This field indicates whether the UE supports multiple TB scheduling for unicast with HARQ bundling as specified in TS 36.213 [22]. A UE indicating support of ce-MultiTB-HARQ-AckBundling-r16 shall also indicate support of pusch-MultiTB-CE-ModeA-r16 or pdsch-MultiTB-CE-ModeA-r16 or pusch-MultiTB-CE-ModeB-r16 or pdsch-MultiTB-CE-ModeB-r16.

#### 4.3.4.215 ce-MultiTB-SubPRB-r16

This field indicates whether the UE supports multiple TB scheduling for unicast with UL sub-PRB as specified in TS 36.213 [22]. A UE indicating support of ce-MultiTB-SubPRB-r16 shall also indicate support of (pusch-MultiTB-CE-ModeA-r16 or pusch-MultiTB-CE-ModeB-r16) and ce-PUSCH-SubPRB-Allocation-r15.

#### 4.3.4.216 ce-MultiTB-EarlyTermination-r16

This field indicates whether the UE supports multiple TB scheduling for unicast with UL early termination as specified in TS 36.213 [22]. A UE indicating support of ce-MultiTB-EarlyTermination-r16 shall also indicate support of pusch-MultiTB-CE-ModeA-r16 or pusch-MultiTB-CE-ModeB-r16.

#### 4.3.4.217 ce-MultiTB-64QAM-r16

This field indicates whether the UE supports multiple TB scheduling for unicast with 64QAM in the downlink when the UE is operating in coverage enhancement mode A as specified in TS 36.213 [22]. A UE indicating support of ce-MultiTB-64QAM-r16 shall also indicate support of pdsch-MultiTB-CE-ModeA-r16 and ce-pdsch-64QAM-r15.

#### 4.3.4.218 ce-MultiTB-FrequencyHopping-r16

This field indicates whether the UE supports multiple TB scheduling for unicast with frequency hopping as specified in TS 36.213 [22]. A UE indicating support of ce-MultiTB-FrequencyHopping-r16 shall also indicate support of pusch-MultiTB-CE-ModeA-r16 or pdsch-MultiTB-CE-ModeA-r16 or pusch-MultiTB-CE-ModeB-r16 or pdsch-MultiTB-CE-ModeB-r16.

#### 4.3.4.219 Void

#### 4.3.4.220 virtualCellID-BasicSRS-r16

Indicates whether the UE supports virtual cell ID for basic SRS symbol(s).

#### 4.3.4.221 addSRS-r16

Presence of this field indicates the UE supports the additional SRS symbol(s) within the normal UL subframes in TDD as described in TS 36.213 [23].

##### 4.3.4.221.1 addSRS-1T2R-r16

Indicates whether the UE supports selecting one antenna among two antennas to transmit additional SRS symbol(s) for the corresponding band of the band combination as described in TS 36.213 [23]. This field can be included only if addSRS-r16 is included.

##### 4.3.4.221.2 addSRS-1T4R-r16

Indicates whether the UE supports selecting one antenna among four antennas to transmit additional SRS symbol(s) for the corresponding band of the band combination as described in TS 36.213 [23]. This field can be included only if addSRS-r16 is included.

##### 4.3.4.221.3 addSRS-2T4R-2Pairs-r16

Indicates whether the UE supports selecting one antenna pair between two antenna pairs to transmit additional SRS symbol(s) simultaneously for the corresponding band of the band combination as described in TS 36.213 [23]. This field can be included only if addSRS-r16 is included.

##### 4.3.4.221.4 addSRS-2T4R-3Pairs-r16

Indicates whether the UE supports selecting one antenna pair among three antenna pairs to transmit additional SRS symbol(s) simultaneously for the corresponding band of the band combination as described in TS 36.213 [23]. This field can be included only if addSRS-r16 is included.

##### 4.3.4.221.5 addSRS-AntennaSwitching-r16

Indicates the antenna switching capabilities for additional SRS symbol(s). This field can be included only if addSRS-r16 is included.

If signalled in addSRS, value useBasic indicates the antenna switching capabilities for additional SRS symbol(s) for a band of band combination for which the capability is not signalled in bandParameterList-v1610 is the same as indicated by bandParameterList-v1380 and/or bandParameterList-v1530 for the concerned band of band combination.

If signalled in bandParameterList-v1610, the field indicates the antenna switching capabilities for additional SRS symbol(s) for the concerned band of band combination.

##### 4.3.4.221.6 addSRS-CarrierSwitching-r16

Indicates the carrier switching capabilities for additional SRS symbol(s). This field can be included only if addSRS-r16 and srs-CapabilityPerBandPairList-r14 are included.

If signalled in addSRS, the field indicates whether carrier switching is supported for additional SRS symbol(s) for all band pairs of band combinations for which UE supports SRS carrier switching. If signalled in addSRS, the field in bandParameterList-v1610 is not signalled.

If signalled in bandParameterList-v1610, the field indicates whether carrier switching is supported for additional SRS symbol(s) for the concerned band pair of band combination. If signalled in bandParameterList-v1610, the field in addSRS is not signalled.

##### 4.3.4.221.7 addSRS-FrequencyHopping-r16

Indicates the frequency hopping capabilities for additional SRS symbol(s). This field can be included only if addSRS-r16 is included.

If signalled in addSRS, the field indicates whether frequency hopping is supported for additional SRS symbol(s) for all bands of band combinations for which the capability is not signalled in bandParameterList-v1610.

If signalled in bandParameterList-v1610, the field indicates whether frequency hopping is supported for additional SRS symbol(s) for the concerned band of band combination.

##### 4.3.4.221.8 virtualCellID-AddSRS-r16

Indicates whether the UE supports virtual cell ID for additional SRS symbol(s).

#### 4.3.4.222 npdsch-16QAM-r17

This field indicates whether the UE supports 16QAM for DL unicast, as specified in TS 36.211 [17], TS 36.212 [26] and TS 36.213 [22]. This feature is only applicable if the UE supports category NB2.

#### 4.3.4.223 npusch-16QAM-r17

This field indicates whether the UE supports 16QAM in the concerned band for UL unicast, as specified in TS 36.211 [17], TS 36.212 [26] and TS 36.213 [22]. This feature is only applicable if the UE supports category NB2.

#### 4.3.4.224 ce-PDSCH-MaxTBS-r17

This field indicates whether the UE supports the maximum DL TBS size of 1736 bits in 1.4 MHz when operating in coverage enhancement mode A as specified in TS 36.213 [22]. A UE indicating support of ce-PDSCH-MaxTBS-r17 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.225 ce-PDSCH-14HARQProcesses-r17

This field indicates whether the UE supports 14 DL HARQ processes with HARQ-ACK delay solution Alt-1 in FDD when operating in coverage enhancement mode A, as specified in TS 36.212 [26] and TS 36.213 [22]. A UE indicating support of ce-PDSCH-14HARQProcesses-r17 shall also indicate support of ce-ModeA-r13.

#### 4.3.4.226 ce-PDSCH-14HARQProcesses-Alt2-r17

This field indicates whether the UE supports 14 DL HARQ processes with HARQ-ACK delay solution Alt-2 in FDD when operating in coverage enhancement mode A, as specified in TS 36.212 [26] and TS 36.213 [22]. A UE indicating support of ce-PDSCH-14HARQProcesses-Alt2-r17 shall also indicate support of ce-PDSCH-14HARQProcesses-r17.

#### 4.3.4.227 csi-SubframeSet2ForDormantSCell-r17

This field defines whether the UE supports second CSI subframe set for periodic CSI reporting for dormant serving cells. This field is only applicable for UEs supporting TDD. A UE that indicates support of this field shall also indicate support for dormantSCellState-r15.

### 4.3.5 RF parameters

#### 4.3.5.1 supportedBandListEUTRA

This field defines which E-UTRA radio frequency bands, see TS 36.101 [6] and TS 36.102 [43] for NTN capable UE, are supported by the UE. For each band, support for either only half duplex operation, or full duplex operation is indicated. For TDD, the half duplex indication is not applicable.

##### 4.3.5.1.1 ue-PowerClass-N-r13, ue-PowerClass-5-r13

These fields define for each supported E-UTRA band whether the UE supports power UE Power Class 1, 2, 4 or 5 for the band, as specified in TS 36.101 [6], TS 36.307 [27] and TS 36.102 [43] for NTN capable UE. Absence of these fields means that the UE supports the default UE Power Class for the band, as specified in TS 36.101 [6].

##### 4.3.5.1.2 intraFreq-CE-NeedForGaps-r13

This field defines for each supported E-UTRA band whether measurement gaps are required to perform intra-frequency measurements on the E-UTRA band for UE in CE Mode A or CE Mode B.

##### 4.3.5.1.3 ue-CA-PowerClass-N

This field defines the power class the UE supports for a E-UTRA band combination, as specified in TS 36.101 [6] and TS 36.307 [27]. Absence of these fields means that the UE supports the default UE Power Class for the band combination, as specified in TS 36.101 [6].

##### 4.3.5.1.4 lowerMSD-MRDC-r18

This field defines for each supported E-UTRA band whether the UE supports lower maximum sensitivity degradation for an EN-DC band combination when the band is the victim band with sensitivity degradation as specified in TS 38.101-3 [44].

#### 4.3.5.1A supportedBandList-r13

This field defines which NB-IoT radio frequency bands, as specified in TS 36.101 [6] and TS 36.102 [43] for NTN capable UE, are supported by the UE. This field is only applicable for UEs of any ue-Category-NB.

##### 4.3.5.1A.1 powerClassNB-20dBm-r13

This field defines whether the UE supports power class 20dBm in NB-IoT for the band, as specified in TS 36.101 [6] and TS 36.102 [43] for NTN capable UE.

##### 4.3.5.1A.2 powerClassNB-14dBm-r14

This field defines whether the UE supports power class 14 dBm in NB-IoT for all the bands that are supported by the UE, as specified in TS 36.101 [6]. The UE shall not include the field if it includes powerClassNB-20dBm-r13.

##### 4.3.5.1A.3 powerBoostingNB-r19

This field defines whether the UE supports PC2 transmitted output power boosting in the NB-IoT NTN UL band as specified in TS 36.102 [43]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17.

#### 4.3.5.2 supportedBandCombination

This field defines the carrier aggregation, MIMO and MBMS reception capabilities (via MBSFN or SC-PTM) supported by the UE for configurations with inter-band, intra-band non-contiguous, intra-band contiguous carrier aggregation and without carrier aggregation. For each band in a band combination the UE provides the supported CA bandwidth classes and the corresponding MIMO capabilities for downlink. The UE also has to provide the supported uplink CA bandwidth class and the corresponding MIMO capability for at least one band in the band combination. Applicability of provisioning uplink CA bandwidth class for each band in the band combinations is defined in TS 36.101 [6]. A MIMO capability applies to all carriers of a bandwidth class of a band in a band combination. For bandwidth classes that include multiple component carriers (i.e. bandwidth classes B, C, D and so on), the UE may also indicate a separate MIMO capability that applies to each individual carrier of a bandwidth class of a band in a band combination.

In all non-CA band combinations the UE shall indicate a bandwidth class supporting the maximum channel bandwidth defined for the band.

In all non-CA band combinations the UE shall indicate at least the number of layers for spatial multiplexing according to the UE's Rel-8/9 category (Cat. 1-5). If the UE provides a Rel-10 category (Cat. 6-8) it shall indicate at least the number of layers according to that category for at least one band combination. In all other band combinations a UE indicating a category 2 and higher shall indicate support for at least 2 layers for downlink spatial multiplexing for all bands. The indicated number of layers for spatial multiplexing may exceed the number of layers required according to the category indicated by the UE. The carrier aggregation and MIMO capabilities indicated for at least one band combination together with modulation scheme shall meet the processing requirements defined by the physical layer parameter values in the UE category (i.e., maximum number of DL-SCH/UL-SCH transport block bits received/transmitted within a TTI, maximum number of bits of a DL-SCH/UL-SCH transport block received/transmitted within a TTI, and total number of soft channel bits for downlink).

NOTE: If the UE reports a subset of supported band combinations based on requestedFrequencyBands and/or skipFallbackCombinations and/or maximumCCsRetrieval, reported band combination(s) may or may not meet the processing requirements defined by the physical layer parameter values in the UE category.

The UE that supports MBMS reception via MBSFN shall support MBMS reception via MBSFN on the PCell of MCG, and it may indicate support for MBMS reception via MBSFN on configured SCells (mbms-SCell) and for any cell that may be additionally configured as an SCell (mbms-NonServingCell) according to this field. The UE may indicate support for MBMS reception from FeMBMS/Unicast mixed cells (fembmsMixedCell) or MBMS-dedicated cells (fembmsDedicatedCell). The UE that supports MBMS reception via SC-PTM shall support MBMS reception via SC-PTM on the PCell of MCG, and it may indicate support for MBMS reception via SC-PTM on configured SCells (scptm-SCell) and for any cell that may be additionally configured as an SCell (scptm-NonServingCell) according to this field. The UE shall apply the system information acquisition and change monitoring procedure relevant for MBMS operation for these cells.

The UE indicating more than one frequency in the MBMSInterestIndication message as specified in TS 36.331 [5] shall support simultaneous reception of MBMS (via MBSFN or SC-PTM) on the indicated frequencies when the frequencies of the configured serving cells and the indicated frequencies belong to at least one band combination.

NOTE: For the purposes of determining whether the carrier aggregation and MIMO capabilities indicated for a band combination meets the processing requirements defined by the physical layer parameter values in the UE category as described above, the carrier aggregation and MIMO capabilities indicated for a band combination is considered to meet the processing requirements if the UE supports the maximum processing requirements defined by the UE category assuming 20MHz channel bandwidth is supported on all bands.

While PCell is not changed, the UE shall support release of any SCell(s) or any uplink configuration of SCell(s) without requiring reconfiguration of parameters related to UE radio access capabilities for the remaining serving cell(s) in the fallback band combination, except for release of an SCell from a contiguous CA band configuration that results in a non-contiguous CA band configuration.

While reporting the sTTI/sPT capabilities, the UE is allowed to report the same band combination more than once with this IE, if the UE supports different combinations of the corresponding sTTI/sPT capabilities.

##### 4.3.5.2.1 supportedBandCombinationReduced-r13

This field is used to indicate the carrier aggregation, MIMO and MBMS reception capabilities supported by the UE as defined in 4.3.5.2 if requested by E-UTRAN as specified in TS 36.331 [5]. All descriptions in 4.3.5.2 are applied for this field unless explicitly stated otherwise. It is mandatory for UEs supporting carrier aggregation beyond 5 component carriers.

If a CA band combination beyond 5 component carriers is included in this field, the UE supports Activation/Deactivation MAC Control Element of four octets as specified in TS 36.321 [4]. If a CA band combination beyond 5 component carriers with uplink is included in this field, the UE supports Extended PHR MAC Control Element supporting 32 serving cells with configured uplink as specified in TS 36.321 [4].

If the fallback band combinations for a given band combination are omitted in this field (see TS 36.331 [5]), the UE shall for all the omitted fallback band combinations support the same UE radio access capabilities as for the parent band combination.

NOTE: A fallback band combination may have multiple different parent band combinations.

While reporting the sTTI/sPT capabilities, the UE is allowed to report the same band combination more than once with this IE, if the UE supports different combinations of the corresponding sTTI/sPT capabilities.

#### 4.3.5.3 multipleTimingAdvance

This field defines whether multiple timing advances are supported for each band combination supported by the UE. It is mandatory for UEs of this release of the specification to support this capability for band combinations having an UL on multiple FDD bands as specified in TS 36.101 [6]. If the band combination comprised of more than one band entry (i.e., inter-band or intra-band non-contiguous band combination), the field indicates that different timing advances on different band entries are supported. If the band combination comprised of one band entry (i.e., intra-band contiguous band combination), the field indicates that different timing advances across component carriers of the band entry are supported. It is mandatory for UEs to support 2 TAGs for inter-frequency DAPS handover.

#### 4.3.5.4 simultaneousRx-Tx

This field defines whether the UE supports simultaneous reception and transmission for inter-band TDD band combination.

#### 4.3.5.5 supportedCSI-Proc-r11

This field defines the maximum number of CSI processes supported on a component carrier within a band with PDSCH transmission mode 10. For bandwidth classes that include multiple component carriers (i.e. bandwidth classes B, C, D and so on), the field defines the maximum number of CSI processes supported by the UE on all component carriers in the corresponding band.

#### 4.3.5.6 freqBandRetrieval-r11

This parameter defines whether the UE supports reception of requestedFrequencyBands as specified in TS 36.331 [5].

#### 4.3.5.7 dl-256QAM-r12

This field defines whether the UE supports 256QAM in DL. This field is only applicable for UEs of category 11-12 and UEs of DL category 11 and onwards. It is mandatory for UEs of DL category 13-14 and 17 to support this feature. A UE that supports 256QAM in DL shall support 256QAM in DL in all supported frequency bands.

#### 4.3.5.8 supportedNAICS-2CRS-AP-r12

This field defines a bitmap points to the entries of naics-Capability-List-r12 to indicate NAICS 2 CRS AP capability for the band combination.

#### 4.3.5.9 dc-Support-r12

This field defines whether synchronous DC and power control mode 1 is supported by the UE which is capable of extendedMaxMeasId, multipleTimingAdvance for a given band combination. If the band combination entry is comprised of a single band, DC is supported for the intra-band contiguous band combination. If the band combination entry is comprised of multiple bands, DC is supported for the inter-band or intra-band non-contiguous band combination.

##### 4.3.5.9.1 asynchronous-r12

In addition to the UE capability indicated by dc-Support, this field defines whether asynchronous DC and power control mode 2 is supported by the UE which is capable of simultaneousRx-Tx. If the band combination is comprised of a single band entry for more than two carriers, the UE shall support any permutations of carriers to CGs. If the concerning band combination is comprised of more than two band entries, the carriers corresponding to a band entry shall belong to one cell group. For this band combination, the UE may indicate the supported carrier permutations to CGs.

##### 4.3.5.9.2 supportedCellGrouping-r12

In addition to the UE capability indicated by asynchronous, this field defines for which mapping of serving cells to cell groups (i.e. MCG or SCG) the UE supports asynchronous DC.

#### 4.3.5.10 modifiedMPR-Behavior-r10

This field defines whether the UE supports modified MPR/A-MPR behaviours as specified in TS 36.101 [6].

#### 4.3.5.11 freqBandPriorityAdjustment-r12

This field defines whether the UE supports the prioritization of the frequency bands in multiBandInfoList over the band in freqBandIndicator as defined by freqBandIndicatorPriority-r12 in TS 36.331 [5].

#### 4.3.5.12 commSupportedBandsPerBC-r12

This field indicates, for a particular band combination, the bands on which the UE supports simultaneous reception of EUTRA and sidelink communication. If the UE indicates support simultaneous transmission (using commSimultaneousTx-r12), this field also indicates, for a particular band combination, the bands on which the UE supports simultaneous transmission of EUTRA and sidelink communication. The first bit refers to the first band indicated by commSupportedBands-r12, with value 1 indicating sidelink is supported simultaneously.

#### 4.3.5.13 supportedCSI-Proc-r12

This field defines the maximum number of CSI processes with PDSCH transmission mode 10 supported by the UE on a single component carrier for bandwidth classes that include multiple component carriers (i.e. bandwidth classes B, C, D and so on).

#### 4.3.5.14 fourLayerTM3-TM4-r10

This field defines whether the UE supports 4-layer spatial multiplexing with transmission mode 3 and transmission mode 4.

#### 4.3.5.15 fourLayerTM3-TM4-perCC-r12

This field defines whether the UE supports 4-layer spatial multiplexing with transmission mode 3 and transmission mode 4 on a single component carrier for bandwidth classes that include multiple component carriers (i.e. bandwidth classes B, C, D and so on).

#### 4.3.5.16 multiNS-Pmax-r10

This field defines whether the UE supports the mechanisms defined for cells broadcasting NS-PmaxList as specified in TS 36.331 [5].

#### 4.3.5.16A multiNS-Pmax-r13

This field defines whether the UE supports the mechanisms defined for NB-IoT cells broadcasting NS-PmaxList as specified in TS 36.331 [5].

#### 4.3.5.17 differentFallbackSupported-r13

This field defines whether the UE supports the different capabilities for at least one fallback case of the concerning band combination. The sTTI/sPT capabilities are also considered by the UE when using this field.

#### 4.3.5.18 maximumCCsRetrieval-r13

This field defines whether the UE supports reception of requestedMaxCCsDL and requestedMaxCCsUL.

#### 4.3.5.19 skipFallbackCombinations-r13

This field defines whether the UE supports receiving reception of skipFallbackCombinations that requests UE to exclude fallback band combinations from capability signalling. UE that indicates support for this shall also indicate support for requestReducedFormat-r13. In this release of the specification, UEs capable of supportedBandCombinationReduced shall indicate support for skipFallbackCombinations-r13.

#### 4.3.5.20 Void

#### 4.3.5.21 reducedIntNonContComb-r13

This field defines whether the UE supports receiving requestReducedIntNonContComb. If the UE supports reducedIntNonContComb-r13, the UE only includes one intra-band non-contiguous CA band combination, and exclude the other intra-band non-contiguous CA band combinations for which the presence of uplink CA bandwidth class in the band combination entry is different. One band combination entry can also indicate support of any other possible permutations in the presence of uplink CA bandwidth class where a paired downlink CA bandwidth class is the same or where the number of UL CCs is smaller than the one of paired DL CCs expressed by the CA bandwidth class.

For example, if the UE supports reducedIntNonContComb-r13, the UE only needs to report "DL: CA_42C-42A, UL: 42A paired with DL 42C", in order to indicate also support of "DL: CA_42C-42A, UL: 42A paired with DL 42A", "DL: CA_42A-42C, UL: 42A paired with DL 42A" and "DL: CA_42A-42C, UL: 42A paired with DL 42C".

For these band combinations not included in the capability, RF parameters specified within BandCombinationParameters (e.g., supportedMIMO-CapabilityUL, multipleTimingAdvance if supported) and measurement parameters specified within BandCombinationListEUTRA are the same as the ones for the band combination included in the UE capability.

#### 4.3.5.22 additionalRx-Tx-PerformanceReq-r13

This field indicates whether the UE supports the additional Rx and Tx performance requirement for a given band combination as specified in TS 36.101 [6].

#### 4.3.5.23 maxLayersMIMO-Indication-r12

This field defines whether the UE supports the network configuration of maxLayersMIMO as specified in TS 36.331 [5].

If the UE supports fourLayerTM3-TM4 or intraBandContiguousCC-InfoList or FeatureSetDL-PerCC for MR-DC, UE supports the configuration of maxLayersMIMO for these cases regardless of indicating maxLayersMIMO-Indication.

#### 4.3.5.24 rf-RetuningTimeDL-r14

This field indicates the interruption time on DL reception within a band pair during the RF retuning for switching between the band pair to transmit SRS on a PUSCH-less SCell as specified in TS 36.331 [5]. This field is mandatory present if switching between the band pair is supported.

#### 4.3.5.25 rf-RetuningTimeUL-r14

This field indicates the interruption time on UL transmission within a band pair during the RF retuning for switching between the band pair to transmit SRS on a PUSCH-less SCell as specified in TS 36.331 [5]. This field is mandatory present if switching between the band pair is supported.

#### 4.3.5.26 diffFallbackCombReport-r14

This field indicates whether the UE supports reporting of UE radio access capabilities for the CA band combinations asked by the eNB as well as, if any, reporting of different UE radio access capabilities for their fallback band combination as specified in TS 36.331 [5]. The UE does not report fallback combinations if their UE radio access capabilities are the same as the ones for the CA band combination asked by the eNB. UEs capable of supportedBandCombinationReduced shall indicate support for diffFallbackCombReport-r14. UE that indicates support for this shall also indicate support for requestReducedFormat-r13.

#### 4.3.5.27 v2x-SupportedTxBandCombListPerBC-r14, v2x-SupportedRxBandCombListPerBC-r14

This field indicates, for a particular band combination of EUTRA, the supported band combination list among v2x-SupportedTxBandCombinationList or v2x-SupportedRxBandCombinationList on which the UE supports simultaneous transmission and reception of EUTRA and V2X sidelink communication respectively.

#### 4.3.5.28 txAntennaSwitchDL-r13

The field indicates the entry number of the first-listed band with UL in the band combination that causes this DL to be affected when transmit antenna switching occurs. If this field is not included, this DL is not affected by transmit antenna switching. All DL and UL that switch together indicate the same entry number.

#### 4.3.5.29 txAntennaSwitchUL-r13

The presence of this field indicates the UE supports transmit antenna selection for this UL band in the band combination as described in TS 36.213 [22], clauses 8.2 and 8.7.

The field indicates the entry number of the first-listed band with UL in the band combination that switches together with this UL when transmit antenna switching occurs. All DL and UL that switch together indicate the same entry number.

#### 4.3.5.30 supportedMIMO-CapabilityDL-r15

This field defines the number of downlink MIMO layers the UE supports when the UE is configured with sTTI. Only two layers or four layers for MIMO support using this field are applicable with sTTI.

#### 4.3.5.31 dl-1024QAM-r15

This field defines whether the UE supports 1024QAM in DL on this band or on this band within the band combination as described in TS 36.331 [5]. This field is only applicable for UEs of DL category 20, 22 and onwards.

When dl-1024QAM-ScalingFactor-r15 and dl-1024QAM-TotalWeightedLayers-r15 are included, the UE supports 1024QAM in a set of CCs in a band combination if the CCs belong to bands indicated to support 1024QAM in that band combination, and the 1024QAM processing capability condition described by equation 4.3.5.31-1 is satisfied.

$$ w.l_{1024QAM}+l_{non1024QAM}\leq  y $$


where:

- $ w $ is the scaling factor for processing a CC configured with 1024QAM with respect to a CC not configured with 1024QAM as indicated by dl-1024QAM-ScalingFactor-r15,

- $ l_{1024QAM}$ is the total number of DL layers across all CCs configured with 1024QAM,

- $ l_{non1024QAM}$ is the total number of DL layers acoss all CCs not configured with 1024QAM, and


- y is total number of weighted layers the UE can process for 1024QAM. Value of y is indicated by dl-1024QAM-TotalWeightedLayers-r15 for all band combinations except for those (NG)EN-DC/NE-DC band combinations for which dl-1024QAM-TotalWeightedLayers is included in ca-ParametersEUTRA (see TS 38.306 [32] and TS 38.331 [35]).

Equation 4.3.5.31-1: 1024QAM processing capability condition.

NOTE: The 1024QAM processing capability condition described by equation 4.3.5.31-1 applies only when at least one of the CCs in a band combination is configured with 1024QAM.

#### 4.3.5.32 srs-MaxSimultaneousCCs-r14

This field indicates, for a particular band combination, the maximum number of simultaneously configurable target CCs supported by the UE for SRS switching.

#### 4.3.5.33 powerClass-14dBm-r15

This field defines whether the UE supports power class 14 dBm when operating in coverage enhancement mode A or B for all the bands that are supported by the UE, as specified in TS 36.101 [6]. A UE indicating support of powerClass-14dBm-r15 shall also indicate support of ce-ModeA-r13.

#### 4.3.5.34 supportedMIMO-CapabilityDL-MRDC-r15

This field indicates in MR-DC the maximum number of supported layers in TM9/10 for the component carrier in the corresponding bandwidth class.

#### 4.3.5.35 srs-FlexibleTiming-r14

This field indicates, for a particular band pair, whether the UE supports configuration of soundingRS-FlexibleTiming-r14. For a TDD-TDD band pair, UE shall include at least one of srs-FlexibleTiming-r14 and/or srs-HARQ-ReferenceConfig-r14 when rf-RetuningTimeDL-r14 or rf-RetuningTimeUL-r14 corresponding to the band pair is larger than 1 OFDM symbol.

#### 4.3.5.36 srs-HARQ-ReferenceConfig-r14

This field indicates, for a particular band pair, whether the UE supports configuration of harq-ReferenceConfig-r14. For a TDD-TDD band pair, UE shall include at least one of srs-FlexibleTiming-r14 and/or srs-HARQ-ReferenceConfig-r14 when rf-RetuningTimeDL-r14 or rf-RetuningTimeUL-r14 corresponding to the band pair is larger than 1 OFDM symbol.

#### 4.3.5.37 fourLayerTM3-TM4-r15

This field indicates whether the UE supports 4-layer spatial multiplexing for TM3 and TM4 for MR-DC within the indicated feature set.

NOTE: Cat5 UE supporting only 2-layer spatial multiplexing will still determine the RI bit width according to TS 36.212 [26], which means it may still use 2-bit RI bit width despite not supporting more than 2-layer spatial multiplexing.

#### 4.3.5.38 supportedCSI-Proc-r15

This field indicates in MR-DC the number of CSI processes for the component carrier in the corresponding bandwidth class.

#### 4.3.5.39 intraFreqAsyncDAPS-r16

This field indicates whether the UE supports asynchronous DAPS handover in source PCell and intra-frequency target PCell.

#### 4.3.5.40 intraFreqDAPS-r16

This field indicates whether the UE supports DAPS handover in source PCell and intra-frequency target PCell, i.e. support of simultaneous DL reception of PDCCH and PDSCH from source and target cell. A UE indicating this capability shall also support synchronous DAPS handover, and single UL transmission for intra-frequency DAPS handover.

#### 4.3.5.41 Void

#### 4.3.5.42 interFreqAsyncDAPS-r16

This field indicates whether the UE supports asynchronous DAPS handover in source PCell and inter-frequency target PCell.

#### 4.3.5.43 interFreqDAPS-r16

This field indicates whether the UE supports DAPS handover in source PCell and inter-frequency target PCell, i.e. support of simultaneous DL reception of PDCCH and PDSCH from source and target cell. For a BC, the capability applies to every carrier pair for source and target. A UE indicating this capability shall also support synchronous DAPS handover, and single UL transmission for inter-frequency DAPS handover.

#### 4.3.5.44 interFreqMultiUL-TransmissionDAPS-r16

This field indicates whether the UE supports simultaneous UL transmission in source PCell and inter-frequency target PCell.

#### 4.3.5.45 intraFreqTwoTAGs-DAPS-r16

This field indicates whether the UE supports different timing advance groups in source PCell and intra-frequency target PCell. It is mandatory for intraFreqDAPS capable UE.

#### 4.3.5.46 v2x-SupportedTxBandCombListPerBC-v1630, v2x-SupportedRxBandCombListPerBC-v1630

This field indicates, for a particular band combination of EUTRA, the supported band combination list among v2x-SupportedBandCombinationListEUTRA-NR on which the UE supports simultaneous transmission or reception of EUTRA and NR sidelink communication respectively, or simultaneous transmission or reception of EUTRA and mixed V2X sidelink and NR sidelink communication respectively.

#### 4.3.5.47 scalingFactorTxSidelink-r16, scalingFactorRxSidelink-r16

This field indicates, for a particular band combination of EUTRA, the scaling factor, as defined in TS 38.306 [32], for the PC5 band combination(s) v2x-SupportedBandCombinationListEUTRA-NR on which the UE supports simultaneous transmission/reception of EUTRA and NR sidelink communication respectively, or simultaneous transmission or reception of EUTRA and joint V2X sidelink communication and NR sidelink communication respectively (as indicated by v2x-SupportedTxBandCombListPerBC-v1630 / v2x-SupportedRxBandCombListPerBC-v1630). The leading / leftmost value corresponds to the first band combination included in v2x-SupportedBandCombinationListEUTRA-NR which is indicated with value 1 by v2x-SupportedTxBandCombListPerBC-v1630 / v2x-SupportedRxBandCombListPerBC-v1630, the next value corresponds to the second band combination included in v2x-SupportedBandCombinationListEUTRA-NR which is indicated with value 1 by v2x-SupportedTxBandCombListPerBC-v1630 / v2x-SupportedRxBandCombListPerBC-v1630 and so on.

#### 4.3.5.48 interBandPowerSharingSyncDAPS-r16

This field indicates whether the UE supports power sharing for inter-band synchronous DAPS handovers as defined in TS 36.213 [22].

A UE that supports power sharing for inter-band synchronous DAPS handovers shall also support inter-frequency DAPS handovers.

#### 4.3.5.49 interBandPowerSharingAsyncDAPS-r16

This field indicates whether the UE supports power sharing for inter-band asynchronous DAPS handovers as defined in TS 36.213 [22].

A UE that supports power sharing for inter-band asynchronous DAPS handovers shall also support inter-frequency DAPS handovers.

#### 4.3.5.50 multiNS-PmaxAerial-r18

This field defines whether the UE supports the mechanisms defined for cells broadcasting NS-PmaxListAerial and freqBandInfoAerial as specified in TS 36.331 [5]. It is mandatory to support this feature for UEs which have Aerial UE subscription as defined in TS 23.401 [18].

#### 4.3.5.51 sl-A2X-SupportedBandCombinationList-r18

This field indicates the list of supported band combination(s) for A2X sidelink communication, as defined in TS 36.331 [5]. For each band in a band combination, the UE may indicate the bandwidth class(es) for A2X sidelink transmission and the bandwidth class(es) for A2X sidelink reception supported by the UE as defined in TS 36.101 [6], Table 5.6G.1-3. If a UE supports A2X sidelink communication, the UE shall support a maximum number of 8 sidelink processes associated with the Sidelink HARQ Entity for the transmission of A2X sidelink communication on SL-SCH.

### 4.3.6 Measurement parameters

#### 4.3.6.1 interFreqNeedForGaps and interRAT-NeedForGaps

These fields define for each supported E-UTRA band whether measurement gaps are required to perform inter-frequency measurements on each supported E-UTRA radio frequency band and inter-RAT measurements on each supported RAT/band combination. A UE also indicates for each band combination as in the supportedBandCombination whether measurement gaps are required to perform inter-frequency measurements on each supported E-UTRA radio frequency band and inter-RAT measurements on each supported RAT/band combination.

#### 4.3.6.2 rsrqMeasWideband

This field defines whether the UE can perform RSRQ measurements in RRC_IDLE and RRC_CONNECTED with wider bandwidth as specified in TS 36.133 [16].

#### 4.3.6.3 timerT312-r12

This field defines whether the UE supports T312 as specified in TS 36.331 [5].

#### 4.3.6.4 alternativeTimeToTrigger-r12

This field defines whether the UE supports alternativeTimeToTrigger as specified in TS 36.331 [5].

#### 4.3.6.5 benefitsFromInterruption-r11

This field indicates whether the UE power consumption could benefit from being allowed to cause interruptions to serving cells when performing measurements of deactivated SCell carriers for measCycleSCell of less than 640ms, as specified in TS 36.133 [16].

#### 4.3.6.6 incMonEUTRA-r12

This field defines whether the UE supports increased number of E-UTRA carrier monitoring in RRC_IDLE and RRC_CONNECTED as specified in TS 36.133 [16], and whether the UE supports extended number of cell re-selection priorities for EUTRA frequencies in RRCConnectionRelease, as specified in TS 36.331 [5]. It is mandatory for UEs of this release of the specification, except for Category 0 and 1bis UEs.

A UE that supports increased number of E-UTRA carrier monitoring shall also support extended number of measurement identities.

#### 4.3.6.7 incMonUTRA-r12

This field defines whether the UE supports increased number of UTRA carrier monitoring in RRC_IDLE and RRC_CONNECTED as specified in TS 36.133 [16].

A UE that supports increased number of UTRA carrier monitoring shall also support extended number of measurement identities.

#### 4.3.6.8 extendedMaxMeasId-r12

This field defines whether the UE supports extended number of measurement identities as defined by maxMeasId-r12 in TS 36.331 [5].

It is mandatory for UEs of this release of the specification if incMonEUTRA-r12 or incMonUTRA-r12 or dc-Support-r12 or extendedMaxObjectId-r13 is supported.

#### 4.3.6.9 crs-DiscoverySignalsMeas-r12

This field defines whether the UE supports CRS based discovery signals measurement as specified in TS 36.331 [5], and PDSCH/EPDCCH RE mapping with zero power CSI-RS configured for discovery signals.

#### 4.3.6.10 csi-RS-DiscoverySignalsMeas-r12

This field defines whether the UE supports CSI-RS based discovery signals measurement as specified in TS 36.331 [5]. A UE that supports this feature shall also support crs-DiscoverySignalsMeas-r12.

#### 4.3.6.11 extendedRSRQ-LowerRange-r12

This field defines whether the UE supports the extended RSRQ lower value range from -34dB to -19.5dB in measurement configuration and reporting as specified in TS 36.133 [16].

#### 4.3.6.12 rsrq-OnAllSymbols-r12

This field defines whether the UE supports the RSRQ measurement on all OFDM symbols as specified in TS 36.214 [23] and also the extended RSRQ upper value range from -3dB to 2.5dB in measurement configuration and reporting as specified in TS 36.133 [16]. If the UE supports rsrq-OnAllSymbols-r12 and rsrqMeasWideband it shall also support the RSRQ measurement on all OFDM symbols with wider bandwidth.

#### 4.3.6.13 rs-SINR-Meas-r13

This field defines whether the UE can perform RS-SINR measurements in RRC_CONNECTED as specified in TS 36.214 [23].

#### 4.3.6.14 allowedCellList-r13

This field defines whether the UE supports configuration and use of allow-listed cells as specified in TS 36.331 [5].

#### 4.3.6.15 extendedFreqPriorities-r13

This field defines whether the UE supports extended E-UTRA frequency priorities as specified in TS 36.331 [5] and indicated by cellReselectionSubPriority field.

A UE supporting NR SA operation shall support extended E-UTRA frequency priorities and NR frequency priorities as specified in TS 36.331 [9] and indicated by CellReselectionSubPriority field.

#### 4.3.6.16 extendedMaxObjectId-r13

This field defines whether the UE supports extended number of measurement object identities as defined by maxObjectId-r13 in TS 36.331 [5]. The field is mandatory present for the UE supporting the configuration of sCellToAddModListExt. A UE indicating support of extendedMaxObjectId-r13 shall also indicate the support of extendedMaxMeasId-r12.

#### 4.3.6.17 ul-PDCP-Delay-r13

This field defines whether the UE supports UL PDCP Packet Delay per QCI measurement as specified in TS 36.314 [25]. A UE that supports the UL PDCP Delay measurement shall also support the measurement configuration and reporting as specified in TS 36.331 [5].

#### 4.3.6.18 Void

#### 4.3.6.19 rssi-AndChannelOccupancyReporting-r13

This field defines whether the UE supports measurement and reporting for RSSI and channel occupancy. This field is only applicable if the UE supports downlink LAA operation.

#### 4.3.6.20 multiBandInfoReport-r13

This field defines whether the UE supports the acquisition and reporting of multi band information for reportCGI as specified in TS 36.331 [5].

#### 4.3.6.21 Void

#### 4.3.6.22 Void

#### 4.3.6.23 ceMeasurements-r14

This field defines whether the UE supports intra-frequency RSRQ measurements and inter-frequency RSRP and RSRQ measurements in RRC_CONNECTED, as specified in TS 36.133 [16], TS 36.304 [14] and TS 36.331 [5]. In this release of specification, it is mandatory for UEs of Category M1 and M2 and UEs that support coverage enhancements to support ceMeasurements-r14. A UE indicating support of ceMeasurements-r14 shall also indicate support of ce-ModeA-r13.

#### 4.3.6.24 ncsg-r14

This field defines whether the UE supports NCSG gap as specified in TS 36.133 [16]. If the UE supports ncsg-r14 and asynchronous DC, the UE shall support NCSG Pattern Id 0, 1, 2 and 3. If the UE supports ncsg-r14 but the UE does not support asynchronous DC, only NCSG Pattern Id 0 and 1 shall be supported.

#### 4.3.6.25 perServingCellMeasurementGap-r14

This field defines whether the UE supports per CC measurement gap as specified in TS 36.331 [5].

#### 4.3.6.26 shortMeasurementGap-r14

This field defines whether the UE supports shorter measurement gap length (i.e. gp2 and gp3) in LTE standalone as specified in TS 36.133 [16], and for independent measurement gap configuration on FR1 and per-UE gap in (NG)EN-DC as specified in TS38.133 [37].

#### 4.3.6.27 nonUniformGap-r14

This field defines whether the UE supports measurement non uniform Pattern Id 1, 2, 3 and 4 in LTE standalone as specified in TS 36.133 [16].

#### 4.3.6.28 rlm-ReportSupport-r14

This field defines whether the UE supports RLM event and information reporting as specified in TS 36.133 [16].

#### 4.3.6.29 Void

#### 4.3.6.30 qoe-MeasReport-r15

This field defines whether the UE supports QoE Measurement Collection for streaming services.

#### 4.3.6.31 ca-IdleModeMeasurements-r15

This field defines whether the UE supports performing eNB-configured CRS-based RRM measurements for configured carrier(s) in RRC_IDLE mode, including reporting them when requested by eNB while in RRC_CONNECTED, as specified in TS 36.331 [5].

#### 4.3.6.32 ca-IdleModeValidityArea-r15

This field defines whether the UE supports configuration of validityArea for performing eNB-configured CRS-based RRM measurements for configured carrier(s) in RRC_IDLE mode, as specified in TS 36.331 [5]. A UE that supports this feature shall also indicate support of ca-IdleModeMeasurements-r15.

#### 4.3.6.33 qoe-MTSI-MeasReport-r15

This field defines whether the UE supports QoE Measurement Collection for MTSI services.

#### 4.3.6.34 multipleCellsMeasExtension-r15

This field defines whether the UE supports measurement reporting triggered based on a number of cells.It is mandatory to support this feature for UEs which have Aerial UE subscription as defined in TS 23.401 [18].

#### 4.3.6.35 heightMeas-r15

This field defines whether the UE supports height-based measurement reporting as specified in TS 36.331 [5]. It is mandatory to support this feature for UEs which have Aerial UE subscription as defined in TS 23.401 [18].

#### 4.3.6.36 measGapPatterns-r15

This field defines whether the UE that supports NR supports gap patterns 4 to 11 in LTE standalone as specified in TS 36.133 [16], and for independent measurement gap configuration on FR1 and per-UE gap in (NG)EN-DC as specified in TS38.133 [37].

#### 4.3.6.37 dl-ChannelQualityReporting-r16

This field indicates whether the UE supports DL channel quality reporting of the configured carrier for FDD in RRC_CONNECTED as specified in TS 36.321 [4]. This feature is only applicable if the UE supports any ue-Category-NB.

#### 4.3.6.37a ce-DL-ChannelQualityReporting-r16

This field indicates whether the UE supports DL channel quality reporting of the serving cell when the UE is operating in coverage enhancement mode A or B in RRC_CONNECTED as specified in TS 36.321 [4]. A UE indicating support of ce-DL-ChannelQualityReporting-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.6.38 interRAT-NeedForGapsNR-r16

This field defines for each supported E-UTRA band or band combination whether measurement gaps are required to perform SSB based inter-RAT measurements on each supported NR band.

#### 4.3.6.39 ce-MeasRSS-Dedicated-r16

This field indicates whether the UE supports improved DL RSRP measurement accuracy through use of RSS in RRC_CONNECTED, and whether the UE supports measurement of neighbour cell RSS in the same narrowband as the MPDCCH, when the UE is operating in coverage enhancement mode A or B as specified in 36.133 [16]. A UE indicating support of ce-MeasRSS-Dedicated-r16 shall also support resynchronization signals as defined in 6.8.8.

#### 4.3.6.39a ce-MeasRSS-DedicatedSameRBs-r16

This field indicates whether the UE supports improved DL RSRP measurement accuracy through use of RSS in RRC_CONNECTED, and whether the UE supports measurement of neighbour cell RSS in the same 2-RBs as the serving cell RSS 2-RBs, when the UE is operating in coverage enhancement mode A or B as specified in 36.133 [16]. A UE indicating support of ce-MeasRSS-Dedicated-r16 shall also support resynchronization signals as defined in 6.8.8. A UE indicating support of ce-MeasRSS-DedicatedSameRBs-r16 shall not indicate support of ce-MeasRSS-Dedicated-r16.

#### 4.3.6.40 eutra-IdleInactiveMeasurements-r16

This field defines whether the UE supports:

- (if the UE also indicates support of inactiveState-r15), performing eNB-configured CRS-based RRM measurements for configured carrier(s) in RRC_INACTIVE, including reporting them when requested by the eNB while resuming from RRC_INACTIVE or in RRC_CONNECTED, as specified in TS 36.331 [5];

- (if the UE also indicates support of RRC connection suspension), reporting eNB-configured CRS-based RRM measurements for configured carrier(s) in RRC_IDLE while resuming the RRC connection from RRC_IDLE or in RRC_CONNECTED, as specified in TS 36.331 [5];

A UE that indicates support of this feature shall also indicate support of ca-IdleModeMeasurements-r15.

#### 4.3.6.41 nr-IdleInactiveMeasFR1-r16

This field defines whether the UE supports performing eNB-configured SSB-based RRM measurements for configured NR FR1 carrier(s) in RRC_IDLE and in RRC_INACTIVE (if the UE also indicates support of inactiveState-r15), including reporting them when requested by the eNB while resuming from RRC_IDLE/RRC_INACTIVE or in RRC_CONNECTED, as specified in TS 36.331 [5].

#### 4.3.6.42 nr-IdleInactiveMeasFR2-r16

This field defines whether the UE supports performing eNB-configured SSB-based RRM measurements for configured NR FR2 carrier(s) in RRC_IDLE and in RRC_INACTIVE (if the UE also indicates support of inactiveState-r15), including reporting them when requested by the eNB while resuming from RRC_IDLE/RRC_INACTIVE or in RRC_CONNECTED, as specified in TS 36.331 [5].

#### 4.3.6.43 idleInactiveValidityAreaList-r16

This field defines whether the UE supports configuration of validityAreaList-r16 for performing eNB-configured measurements for configured carrier(s) in RRC_IDLE and in RRC_INACTIVE (if the UE supports inactiveState-r15), as specified in TS 36.331 [5].

A UE that indicates support of this feature shall also indicate support of eutra-IdleInactiveMeasurements-r16 or nr-IdleInactiveMeasFR1-r16 or nr-IdleInactiveMeasFR2-r16.

#### 4.3.6.44 measGapPatterns-NRonly-r16

This field indicates whether the UE supports gap patterns 2, 3 and 11 in LTE standalone when the frequencies to be measured within this measurement gap are all NR frequencies.

#### 4.3.6.45 measGapPatterns-NRonly-ENDC-r16

This field indicates whether the UE supports gap patterns 2, 3 and 11 in (NG)EN-DC when the frequencies to be measured within this measurement gap are all NR frequencies.

#### 4.3.6.46 nr-IdleInactiveBeamMeasFR1-r16

This field defines whether the UE supports performing eNB-configured SSB-based beam level RRM measurements for configured NR FR1 carrier(s) in RRC_IDLE and in RRC_INACTIVE (if the UE also indicates support of inactiveState-r15), including reporting them when requested by the eNB while resuming from RRC_IDLE/RRC_INACTIVE or in RRC_CONNECTED, as specified in TS 36.331 [5].

A UE that supports this feature shall also support nr-IdleInactiveMeasFR1-r16.

#### 4.3.6.47 nr-IdleInactiveBeamMeasFR2-r16

This field defines whether the UE supports performing eNB-configured SSB-based beam level RRM measurements for configured NR FR2 carrier(s) in RRC_IDLE and in RRC_INACTIVE (if the UE also indicates support of inactiveState-r15), including reporting them when requested by the eNB while resuming from RRC_IDLE/RRC_INACTIVE or in RRC_CONNECTED, as specified in TS 36.331 [5].

A UE that supports this feature shall also support nr-IdleInactiveMeasFR2-r16.

#### 4.3.6.48 nr-RSSI-ChannelOccupancyReporting-r17

This field indicates whether the UE supports performing measurements and reporting of RSSI and channel occupancy on the corresponding NR band. If both sharedSpectrumMeasNR-EN-DC-r17 and sharedSpectrumMeasNR-SA-r17 are included, the UE shall set the value of nr-RSSI-ChannelOccupancyReporting-r17 consistently for the same NR band.

#### 4.3.6.49 connModeMeasIntraFreq-r17


This field defines whether the UE supports intra-frequency neighbour cell measurements in RRC_CONNECTED, as specified in TS 36.133 [16] and TS 36.331 [5]. This field is only applicable for UEs of any ue-Category-NB.

#### 4.3.6.50 connModeMeasInterFreq-r17

This field defines whether the UE supports inter-frequency neighbour cell measurements in RRC_CONNECTED, as specified in TS 36.133 [16] and TS 36.331 [5]. This field is only applicable for UEs of any ue-Category-NB.

#### 4.3.6.51 nr-CellIndividualOffset-r16

This parameter defines whether the UE supports use of cell specific offset for NR inter-RAT measurements in LTE for reporting of NR neighbours as specified in TS 36.331 [5].

#### 4.3.6.52 gaplessMeas-FR2-maxCC-r17

This field defines whether the UE supports inter-RAT NR FR2 measurement without measurement gap as specified in clause 9.1.2 of TS 38.133 [37] while the number of configured serving cells is less than or equal to the indicated number. This field is applicable when only E-UTRA serving cells are configured. The UE reporting this field and supporting (NG)EN-DC shall not indicate support of independentGapConfig in MeasAndMobParametersMRDC within UE-MRDC-Capability (defined in TS 38.306 [32]).

#### 4.3.6.53 interRAT-NeedForInterruptionNR-r18

This field defines for each supported E-UTRA band or band combination whether interruption is required to perform SSB based inter-RAT measurements without gap on each supported NR band. Value no-gap-with-interruption indicates measurement gap is not needed but interruption is needed, and value no-gap-no-interruption indicates neither measurement gap nor interruption is needed. The UE includes this field only if it indicates measurement gap is not required in the corresponding interRAT-NeedForGapsNR-r16 field.

#### 4.3.6.54 simultaneousRxDataSSB-DiffNumerology-FR1-r18

This field defines whether the UE supports concurrent SSB-based inter-RAT measurement on NR FR1 cell and PDCCH or PDSCH reception from the serving cell with a different numerology. The UE includes this field only if it indicates support of interRAT-NeedForInterruptionNR-r18 for at least one target band in at least one band combination. This field applies only if interRAT-NeedForInterruptionNR-r18 is reported for the target band in the band combination.

#### 4.3.6.55 a4-a5-ReportOnLeaveSupport-r15

This field defines whether the UE supports measurement reporting when the leaving condition is met for A4 and/or A5 event as specified in TS 36.331 [5].

### 4.3.7 Inter-RAT parameters

#### 4.3.7.1 utraFDD

This parameter defines whether the UE supports UTRA FDD.

A UE that supports UTRAN FDD shall support inter-RAT PS handover to UTRAN.

#### 4.3.7.2 supportedBandListUTRA-FDD

Only applicable if the UE supports UTRA FDD. This field defines which UTRA FDD radio frequency bands are supported by the UE.

#### 4.3.7.3 utraTDD128

This parameter defines whether the UE supports UTRA TDD 1.28 Mcps.

A UE that supports UTRAN TDD 1.28 Mcps shall support inter-RAT PS handover to UTRAN.

#### 4.3.7.4 supportedBandListUTRA-TDD128

Only applicable if the UE supports UTRA TDD 1.28 Mcps. This field defines which UTRA TDD 1.28 Mcps radio frequency bands are supported by the UE.

#### 4.3.7.5 utraTDD384

This parameter defines whether the UE supports UTRA TDD 3.84 Mcps.

A UE that supports UTRAN TDD 3.84 Mcps shall support inter-RAT PS handover to UTRAN.

#### 4.3.7.6 supportedBandListUTRA-TDD384

Only applicable if the UE supports UTRA TDD 3.84 Mcps. This field defines which UTRA TDD 3.84 Mcps radio frequency bands are supported by the UE.

#### 4.3.7.7 utraTDD768

This parameter defines whether the UE supports UTRA TDD 7.68 Mcps.

A UE that supports UTRAN TDD 7.68 Mcps shall support inter-RAT PS handover to UTRAN.

#### 4.3.7.8 supportedBandListUTRA-TDD768

Only applicable if the UE supports UTRA TDD 7.68 Mcps. This field defines which UTRA TDD 7.68 Mcps radio frequency bands are supported by the UE.

#### 4.3.7.9 geran

This parameter defines whether the UE supports GERAN.

#### 4.3.7.10 supportedBandListGERAN

Only applicable if the UE supports GERAN. This field defines which GERAN radio frequency bands are supported by the UE.

#### 4.3.7.11 interRAT-PS-HO-ToGERAN

Only applicable if the UE supports GERAN. This field defines whether the UE supports inter-RAT PS handover to GERAN.

#### 4.3.7.12 cdma2000-HRPD

This parameter defines whether the UE supports HRPD.

#### 4.3.7.13 supportedBandListHRPD

Only applicable if the UE supports HRPD. This field defines which HRPD radio frequency bands are supported by the UE.

#### 4.3.7.14 tx-ConfigHRPD

Only applicable if the UE supports HRPD. This field defines whether the UE supports single or dual transmitter. With dual transmitter, UE can transmit simultaneously on both E-UTRAN and HRPD.

#### 4.3.7.15 rx-ConfigHRPD

Only applicable if the UE supports HRPD. This field defines whether the UE supports single or dual receiver. With dual receiver, UE can receive simultaneously on both E-UTRAN and HRPD.

#### 4.3.7.16 cdma2000-1xRTT

This parameter defines whether the UE supports 1xRTT.

#### 4.3.7.17 supportedBandList1XRTT

Only applicable if the UE supports 1xRTT. This field defines which 1xRTT radio frequency bands are supported by the UE.

#### 4.3.7.18 tx-Config1XRTT

Only applicable if the UE supports 1xRTT. This field defines whether the UE supports single or dual transmitter. With dual transmitter, UE can transmit simultaneously on both E-UTRAN and 1xRTT.

#### 4.3.7.19 rx-Config1XRTT

Only applicable if the UE supports 1xRTT. This field defines whether the UE supports single or dual receiver. With dual receiver, UE can receive simultaneously on both E-UTRAN and 1xRTT.

#### .20 e-CSFB-1XRTT

Only applicable if the UE supports CDMA2000 1xRTT. This field defines whether the UE supports enhanced 1xRTT CS fallback.

#### .21 e-CSFB-ConcPS-Mob1XRTT

Only applicable if the UE supports CDMA2000 1xRTT and CDMA2000 HRPD simultaneously. This field defines whether the UE supports concurrent enhanced CS fallback to CDMA2000 1xRTT and handover/redirection to CDMA2000 HRPD.

#### 4.3.7.22 e-RedirectionUTRA

This parameter defines whether the UE supports use of UTRA system information provided by RRCConnectionRelease upon redirection.

#### 4.3.7.23 e-RedirectionGERAN

This parameter defines whether the UE supports use of GERAN system information provided by RRCConnectionRelease upon redirection.

A UE that supports CS fallback to GERAN shall support e-Redirection to GERAN.

#### 4.3.7.24 dtm

This parameter defines whether the UE supports Dual Transfer Mode (DTM) in GERAN.

#### 4.3.7.25 e-CSFB-dual-1XRTT

Only applicable if the UE supports CDMA2000 1xRTT, dual transmitter (i.e. UE can transmit simultaneously on both E-UTRAN and 1xRTT) and dual receiver (i.e. UE can receive simultaneously on both E-UTRAN and 1xRTT). This field defines whether the UE supports dual receiver/transmitter enhanced 1xRTT CS fallback (dual Rx/Tx e1xCSFB).

#### 4.3.7.26 e-RedirectionUTRA-TDD

This parameter defines whether the UE supports redirection to multiple carrier frequencies both with and without using UTRA TDD system information for cells on multiple carrier frequencies provided by RRCConnectionRelease.

#### 4.3.7.27 cdma2000-NW-Sharing-r11

Only applicable if the UE supports CDMA2000 1xRTT or CDMA2000 HRPD. This parameter defines whether the UE supports per PLMN CDMA2000 interworking in E-UTRAN shared networks as specified in TS 36.331 [5].

#### 4.3.7.28 mfbi-UTRA

This field is only applicable for a UE supporting UTRA FDD. It indicates if the UE supports the signalling requirements of multiple radio frequency bands in a UTRA FDD cell, as defined in TS 25.307 [20].

#### 4.3.7.29 supportedBandListWLAN

This field defines which WLAN radio frequency bands are supported by the UE.

#### 4.3.7.30 supportedBandListNB-r19

This field defines which NB-IoT radio frequency bands, as specified in TS 36.102 [43], are supported by the NTN capable UE for redirection from an E-UTRAN terrestrial network to an NB-IoT non-terrestrial network (ntn-Redirection-NB-r19).

### 4.3.8 General parameters

#### 4.3.8.1 accessStratumRelease

This field defines the release of the E-UTRA layer 1, 2, and 3 specifications supported by the UE e.g. Rel-8, Rel-9, etc.

#### 4.3.8.1A accessStratumRelease-r13

This field defines the release of the E-UTRA layer 1, 2, and 3 specifications supported by the UE e.g. Rel-13, Rel-14, etc. This field is only applicable for UEs of any ue-Category-NB.

#### 4.3.8.2 deviceType

This field defines whether the device does not benefit from NW-based battery consumption optimisation.

#### 4.3.8.3 Void

#### 4.3.8.4 Void

#### 4.3.8.5 multipleDRB-r13

This field indicates whether the UE supports multiple DRBs. This field is only applicable if the UE supports S1-U data transfer or User plane CIoT EPS Optimisation as defined in TS 24.301 [28] or NG-U data transfer or User plane CIoT 5GS Optimisation as defined in TS 24.501 [39], and any ue-Category-NB. If a UE of this release supports multiple DRBs, the UE shall support two simultaneous DRBs.

#### 4.3.8.6 Void

#### 4.3.8.7 earlyData-UP-r15

This field defines whether the UE supports MO-EDT for User Plane CIoT EPS optimizations, as defined in TS 24.301 [28]. This feature is only applicable if the UE supports ce-ModeA-r13, or for FDD if the UE supports any ue-Category-NB.

#### 4.3.8.8 void

#### 4.3.8.9 extendedNumberOfDRBs-r15

This field defines whether the UE supports up to 15 DRBs. The UE shall support any combination of RLC AM and RLC UM entities for the configured DRBs. A UE that supports extendedNumberOfDRBs-r15 shall also support the extended LCID as specified in TS 36.321 [4].

#### 4.3.8.10 reducedCP-Latency-r15

This field defines whether the UE supports reduced control plane latency as defined in TS 36.213 [22] and TS 36.331 [5].

#### 4.3.8.11 earlySecurityReactivation-r16

This field defines whether the UE supports early security reactivation when resuming a suspended RRC connection as specified in TS 36.331 [5].

#### 4.3.8.12 Void

#### 4.3.8.13 Void

#### 4.3.8.14 dl-DedicatedMessageSegmentation-r16

Indicates whether the UE supports reception of segmented DL RRC messages.

#### 4.3.8.15 altFreqPriority-r16

This field defines whether the UE supports alternative cell reselection priority as defined in TS 36.331 [5].

#### 4.3.8.16 coverageBasedPaging-r17

This field defines whether the UE supports coverage based paging carrier selection as specified in TS 36.304 [14]. This field is only applicable if the UE supports any ue-Category-NB.

#### 4.3.8.17 pws-Support-r19

This field indicates whether the UE supports the reception of PWS message including ETWS, CMAS, KPAS, EU-Alert in RRC_IDLE as defined in TS 36.331 [5]. This feature is only applicable if the UE supports ue-category-NB.

### 4.3.9 Void

### 4.3.10 CSG Proximity Indication parameters

#### 4.3.10.1 intraFreqProximityIndication

This parameter defines whether the UE supports proximity indication for intra-frequency E-UTRAN cells whose CSG Identities are in the UE's Permitted CSG list.

#### 4.3.10.2 interFreqProximityIndication

This parameter defines whether the UE supports proximity indication for inter-frequency E-UTRAN cells whose CSG Identities are in the UE's Permitted CSG list.

#### 4.3.10.3 utran-ProximityIndication

This parameter defines whether the UE supports proximity indication for UTRAN cells whose CSG IDs are in the UE's Permitted CSG list.

### 4.3.11 Neighbour cell SI acquisition parameters

#### 4.3.11.1 intraFreqSI-AcquisitionForHO

This parameter defines whether the UE supports, upon configuration of si-RequestForHO by the network, acquisition of relevant information from a neighbouring intra-frequency cell by reading the SI of the neighbouring cell using autonomous gaps and reporting the acquired information to the network as specified in TS 36.331 [5].

#### 4.3.11.2 interFreqSI-AcquisitionForHO

This parameter defines whether the UE supports, upon configuration of si-RequestForHO by the network, acquisition of relevant information from a neighbouring inter-frequency cell by reading the SI of the neighbouring cell using autonomous gaps and reporting the acquired information to the network as specified in TS 36.331 [5].

#### 4.3.11.3 utran-SI-AcquisitionForHO

This parameter defines whether the UE supports, upon configuration of si-RequestForHO by the network, acquisition of relevant information from a neighbouring UMTS cell by reading the SI of the neighbouring cell using autonomous gaps and reporting the acquired information to the network as specified in TS 36.331 [5].

#### 4.3.11.4 reportCGI-NR-EN-DC-r15

This parameter defines whether the UE supports acquisition of relevant information from a neighbouring NR cell by reading the SI of the neighbouring cell and reporting the acquired information to the network as specified in TS 36.331 [5] when the (NG)EN-DC is configured.

#### 4.3.11.5 reportCGI-NR-NoEN-DC-r15

This parameter defines whether the UE supports acquisition of relevant information from a neighbouring NR cell by reading the SI of the neighbouring cell and reporting the acquired information to the network as specified in TS 36.331 [5] when the (NG)EN-DC is not configured.

#### 4.3.11.6 eutra-CGI-Reporting-ENDC

This parameter defines whether the UE supports acquisition of relevant information from a neighbouring E-UTRA cell by reading the SI of the neighbouring cell and reporting the acquired information to the network as specified in TS 36.331 [5] when the (NG)EN-DC is configured wherein either MN and SN have different DRX cycles, or on-duration configured by MN does not contain on-duration configured by SN if their DRX cycles are same.

#### 4.3.11.7 utra-GERAN-CGI-Reporting-ENDC

This parameter defines whether the UE supports acquisition of relevant information from a neighbouring GERAN/UTRA cell by reading the SI of the neighbouring cell and reporting the acquired information to the network as specified in TS 36.331 [5] when the (NG)EN-DC is configured wherein either MN and SN have different DRX cycles, or on-duration configured by MN does not contain on-duration configured by SN if their DRX cycles are same.

#### 4.3.11.8 eutra-SI-AcquisitionForHO-ENDC-r16

This parameter defines whether the UE supports, upon configuration of si-RequestForHO by the network, acquisition of relevant information from a neighbouring E-UTRA cell by reading the SI of the neighbouring cell using autonomous gaps and reporting the acquired information to the network as specified in TS 36.331 [5] when the (NG)EN-DC is configured.

#### 4.3.11.9 nr-AutonomousGaps-ENDC-FR1-r16

This parameter defines whether the UE supports, upon configuration of useAutonomousGapsNR by the network, acquisition of relevant information from a neighbouring NR cell by reading the SI of the neighbouring cell on FR1 using autonomous gaps and reporting the acquired information to the network as specified in TS 36.331 [5] when it is configured with (NG)EN-DC.

#### 4.3.11.10 nr-AutonomousGaps-ENDC-FR2-r16

This parameter defines whether the UE supports, upon configuration of useAutonomousGapsNR by the network, acquisition of relevant information from a neighbouring NR cell by reading the SI of the neighbouring cell on FR2 using autonomous gaps and reporting the acquired information to the network as specified in TS 36.331 [5] when it is configured with (NG)EN-DC.

#### 4.3.11.11 nr-AutonomousGaps-FR1-r16

This parameter defines whether the UE supports, upon configuration of useAutonomousGapsNR by the network, acquisition of relevant information from a neighbouring NR cell by reading the SI of the neighbouring cell on FR1 using autonomous gaps and reporting the acquired information to the network as specified in TS 36.331 [5] when it is not configured with (NG)EN-DC.

#### 4.3.11.12 nr-AutonomousGaps-FR2-r16

This parameter defines whether the UE supports, upon configuration of useAutonomousGapsNR by the network, acquisition of relevant information from a neighbouring NR cell by reading the SI of the neighbouring cell on FR2 using autonomous gaps and reporting the acquired information to the network as specified in TS 36.331 [5] when it is not configured with (NG)EN-DC.

#### 4.3.11.13 eutra-CGI-Reporting-NEDC-r15

This parameter defines whether the UE supports acquisition of relevant information from a neighbouring E-UTRA cell by reading the SI of the neighbouring cell and reporting the acquired information to the network as specified in TS 36.331 [5] when the NE-DC is configured.

#### 4.3.11.14 gNB-ID-Length-Reporting-NR-EN-DC-r17

This parameter defines whether the UE supports the acquisition of length of the gNB identity from a neighbouring NR cell when it is configured with (NG)EN-DC by reading the SI of the neighbouring cell and reporting the acquired information to the network as specified in TS 36.331 [5]. If the UE supports reportCGI-NR-EN-DC-r15, the UE shall support the gNB-ID-Length-Reporting-NR-EN-DC-r17.

#### 4.3.11.15 gNB-ID-Length-Reporting-NR-NoEN-DC-r17

This parameter defines whether the UE supports the acquisition of length of the gNB identity from a neighbouring NR cell when it is not configured with (NG)EN-DC by reading the SI of the neighbouring cell and reporting the acquired information to the network as specified in TS 36.331 [5]. If the UE supports reportCGI-NR-NoEN-DC-r15, the UE shall support gNB-ID-Length-Reporting-NR-NoEN-DC-r17.

#### 4.3.11.16 eutra-reportCGI-HSDN-r19

This parameter defines whether the UE supports acquisition of HSDN cell information from a neighbouring EUTRA cell by reading the SI of the neighbouring cell and reporting the acquired information to the network as specified in TS 36.331 [5].

#### 4.3.11.17 nr-reportCGI-HSDN-r19

This parameter defines whether the UE supports acquisition of HSDN cell information from a neighbouring NR cell by reading the SI of the neighbouring cell and reporting the acquired information to the network as specified in TS 36.331 [5].

### 4.3.12 SON parameters

#### 4.3.12.1 rach-Report

This parameter defines whether the UE supports delivery of rachReport upon request from the network.

#### 4.3.12.2 anr-Report-r16

This field indicates whether the UE supports ANR measurement configuration and reporting in RRC_IDLE as specified in TS 36.304 [14] and TS 36.331 [5]. This feature is only applicable if the UE supports any ue-Category-NB.

#### 4.3.12.3 rach-Report-r16

This field indicates whether the UE supports delivery of rachReport upon request from the network as specified in TS 36.331 [5] when connected to EPC. This feature is only applicable if the UE supports any ue-Category-NB.

#### 4.3.12.4 rach-ReportForNR-r18

This field indicates whether the UE supports NR RACH report in LTE, upon request from the network.

#### 4.3.12.5 locationInfo-r16

This field indicates whether the UE supports reporting of location information in RLF-Report upon request from the network as specified in TS 36.331 [5]. This feature is only applicable if the UE supports any ue-Category-NB.

### 4.3.13 UE-based network performance measurement parameters

#### 4.3.13.1 loggedMeasurementsIdle

This parameter defines whether the UE supports logged measurements including logging in any cell selection state in RRC_IDLE upon request from the network as specified in TS 36.331 [5] and TS 36.304 [14]. A UE that supports logged measurements in RRC_IDLE shall also support a minimum of 64kB memory for log storage.

#### 4.3.13.2 standaloneGNSS-Location

This parameter defines whether the UE is equipped with a standalone GNSS receiver that may be used to provide detailed location information in RRC measurement report and logged measurements in RRC_IDLE. The GNSS receiver may be used to provide the location when operating in the NTN cell.

#### 4.3.13.3 Void

#### 4.3.13.4 loggedMBSFNMeasurements-r12

This parameter defines whether the UE supports logged MBSFN measurement in RRC_IDLE and RRC_CONNECTED upon request from the network. A UE that supports logged MBSFN measurements shall also support a minimum of 64kB memory for log storage. A UE that supports logged MBSFN measurements shall also support logged measurements in RRC_IDLE upon request from the network.

#### 4.3.13.5 locationReport-r14

This parameter defines whether the UE supports reporting of its geographical location information to eNB.

#### 4.3.13.6 loggedMeasBT-r15

This parameter indicates whether the UE supports Bluetooth measurements in RRC_IDLE mode.

#### 4.3.13.7 loggedMeasWLAN-r15

This parameter indicates whether the UE supports WLAN measurements in RRC_IDLE mode.

#### 4.3.13.8 immMeasBT-r15

This parameter indicates whether the UE supports Bluetooth measurements in RRC_CONNECTED mode.

#### 4.3.13.9 immMeasWLAN-r15

This parameter indicates whether the UE supports WLAN measurements in RRC_CONNECTED mode.

#### 4.3.13.10 ul-PDCP-AvgDelay-r16

This parameter indicates whether the UE supports UL PDCP Packet Average Delay measurement (as specified in TS 38.314 [41]) and reporting in RRC_CONNECTED state.

#### 4.3.13.11 loggedMeasIdleEventL1-r17

This parameter defines whether the UE supports event triggered logged measurements for eventL1 in RRC_IDLE upon request from the network. A UE indicating support of loggedMeasIdleEventL1-r17 shall also indicate support of loggedMeasurementsIdle.

#### 4.3.13.12 loggedMeasIdleEventOutOfCoverage-r17

This parameter defines whether the UE supports event triggered logged measurements for event outOfCoverage in RRC_IDLE upon request from the network. A UE indicating support of loggedMeasIdleEventOutOfCoverage-r17 shall also indicate support of loggedMeasurementsIdle.

#### 4.3.13.13 loggedMeasUncomBarPre-r17

This parameter indicates whether the UE supports logging of uncompensated barometric pressure measurement in RRC_IDLE mode.

#### 4.3.13.14 immMeasUncomBarPre-r17

This parameter indicates whether the UE supports uncompensated barometric pressure measurement in RRC_CONNECTED mode.

#### 4.3.13.15 sigBasedEUTRA-LoggedMeasOverrideProtect-r18

This parameter indicates whether the UE supports the override protection of the signalling based logged measurements configured in E-UTRA when entering RRC_CONNECTED state in NR.

### 4.3.14 IMS Voice parameters

#### 4.3.14.1 voiceOver-PS-HS-UTRA-FDD

Only applicable if the UE supports UTRA FDD. This parameter defines whether the UE supports IMS Voice in UTRA FDD according to GSMA IR.58 profile.

#### 4.3.14.2 voiceOver-PS-HS-UTRA-TDD128

Only applicable if the UE supports UTRA TDD 1.28Mcps. This parameter defines whether the UE supports IMS Voice in UTRA TDD 1.28Mcps.

#### 4.3.14.3 srvcc-FromUTRA-FDD-ToGERAN

Only applicable if the UE supports UTRA FDD and GERAN. This parameter defines whether the UE supports SRVCC handover from UTRA FDD PS HS to GERAN CS.

#### 4.3.14.4 srvcc-FromUTRA-FDD-ToUTRA-FDD

Only applicable if the UE supports UTRA FDD. This parameter defines whether the UE supports SRVCC handover from UTRA FDD PS HS to UTRA FDD CS.

#### 4.3.14.5 srvcc-FromUTRA-TDD128-ToGERAN

Only applicable if the UE supports UTRA TDD 1.28Mcps and GERAN. This parameter defines whether the UE supports SRVCC handover from UTRA TDD 1.28Mcps PS HS to GERAN CS.

#### 4.3.14.6 srvcc-FromUTRA-TDD128-ToUTRA-TDD128

Only applicable if the UE supports UTRA TDD 1.28Mcps. This parameter defines whether the UE supports SRVCC handover from UTRA TDD 1.28Mcps PS HS to UTRA TDD 1.28Mcps CS.

### 4.3.15 Other parameters

#### 4.3.15.1 Void

#### 4.3.15.2 inDeviceCoexInd-r11

This parameter defines whether the UE supports in-device coexistence indication as well as autonomous denial functionality as specified in TS 36.331 [5].

#### 4.3.15.3 powerPrefInd-r11

This parameter defines whether the UE supports power preference indication as specified in TS 36.331 [5].

#### 4.3.15.4 ue-Rx-TxTimeDiffMeasurements-r11

This parameter defines whether the UE supports Rx - Tx time difference measurements as specified in TS 36.331 [5] and TS 36.355 [13]. A TDD UE of this release of the specification that supports UE Rx-Tx time difference measurements, shall support to report UE Rx-Tx time difference measurement result including NTAoffset according to EUTRAN TDD Rx-Tx time difference measurement report mapping as specified in TS 36.133 [16].

#### 4.3.15.5 Void

#### 4.3.15.6 Void

#### 4.3.15.7 Void

#### 4.3.15.8 inDeviceCoexInd-UL-CA-r11

This parameter defines whether the UE supports UL CA related in-device coexistence indication as specified in TS 36.331 [5]. A UE that supports UL CA related in-device coexistence indication shall also support in-device coexistence indication.

#### 4.3.15.9 bwPrefInd-r14

This parameter defines whether the UE supports maximum PDSCH/PUSCH bandwidth preference indication as specified in TS 36.331 [5]. A UE indicating support of bwPrefInd-r14 shall also indicate support of ce-ModeA-r13.

#### 4.3.15.10 inDeviceCoexInd-HardwareSharingInd-r13

This parameter defines whether the UE supports hardware sharing indication as specified in TS 36.331 [5]. A UE that supports hardware sharing indication shall also indicate support of LAA operation.

#### 4.3.15.11 overheatingInd-r14

This parameter defines whether the UE supports overheating assistance information as specified in TS 36.331 [5].

#### 4.3.15.12 assistInfoBitForLC-r15

This parameter defines whether the UE supports assistance information bit for local cache as specified in TS 36.323 [2].

#### 4.3.15.13 timeReferenceProvision-r15

This parameter defines whether the UE supports provision of time reference message TimeReferenceInformation as specified in TS 36.331 [5].

#### 4.3.15.14 flightPathPlan-r15

This field defines whether the UE supports reporting of the flight path plan through the procedure defined in TS 36.331 [5].

#### 4.3.15.15 inDeviceCoexInd-ENDC-r15

This parameter defines whether the UE supports in-device coexistence indication for (NG)EN-DC operation as specified in TS 36.331 [5]. A UE that supports in-device coexistence indication for (NG)EN-DC operation shall also support in-device coexistence indication.

#### 4.3.15.16 nonCSG-SI-Reporting-r14

This parameter defines whether the UE supports reporting of PLMN list from cells not broadcasting the field csg-Identity.

#### 4.3.15.17 resumeWithStoredMCG-SCells-r16

This parameter defines whether the UE supports not deleting the stored E-UTRA MCG SCell configuration when initiating the resume procedure as specified in TS 36.331 [5]. A UE indicating support of resumeWithStoredMCG-SCells-r16 shall also indicate support of resumeWithMCG-SCellConfig-r16.

#### 4.3.15.18 resumeWithMCG-SCellConfig-r16

This parameter defines whether the UE supports (re-)configuration of E-UTRA MCG SCells in the RRCConnectionResume message as specified in TS 36.331 [5].

#### 4.3.15.19 resumeWithStoredSCG-r16

This parameter defines whether the UE supports not deleting the stored NR SCG configuration when initiating the resume procedure as specified in TS 36.331 [5]. A UE indicating support of resumeWithStoredSCG-r16 shall also indicate support of resumeWithSCG-Config-r16.

#### 4.3.15.20 resumeWithSCG-Config-r16

This parameter defines whether the UE supports (re-)configuration of an NR SCG in the RRCConnectionResume message as specified in TS 36.331 [5].

#### 4.3.15.21 mcgRLF-RecoveryViaSCG-r16

This parameter defines whether the UE supports recovery from MCG RLF via split SRB1 (if supported) and via SRB3 (if supported) as specified in TS 36.331 [5].

#### 4.3.15.22 overheatingIndForSCG-r16

This parameter defines whether the UE supports the inclusion of NR SCG reduced configuration in the overheating assistance information as specified in TS 36.331 [5]. The UE which indicates support of overheatingIndForSCG-r16 shall also indicate support of overheatingInd-r14.

#### 4.3.15.23 mpsPriorityIndication-r16

This parameter defines whether the UE supports mpsPriorityIndication on RRC release with redirect as defined in TS 36.331 [5].

#### 4.3.15.24 ul-RRC-Segmentation-r16

This parameter defines whether the UE supports uplink RRC segmentation of UECapabilityInformation according to the network indication rrc-SegAllowed as specified in TS 36.331 [5].

#### 4.3.15.25 ul-RRC-MaxCapaSegments-r17

This parameter defines whether the UE supports uplink RRC segmentation of UECapabilityInformation according to the network indication rrc-MaxCapaSegAllowed as specified in TS 36.331 [5].

#### 4.3.15.26 ntn-Redirection-r19

This parameter defines whether the UE supports intra-RAT redirection from a terrestrial network to a non-terrestrial network as specified in TS 36.331 [5]. This field is only applicable if the UE supports NTN access.

#### 4.3.15.27 ntn-Redirection-NB-r19

This parameter defines whether the UE supports redirection from an E-UTRAN terrestrial network to an NB-IoT non-terrestrial network as specified in TS 36.331 [5]. This field is only applicable if the UE supports NTN access.

### 4.3.16 Positioning parameters

#### 4.3.16.1 otdoa-UE-assisted

This parameter defines whether the UE supports UE-assisted OTDOA positioning as specified in TS 36.355 [13].

#### 4.3.16.2 interFreqRSTDmeasurement

This parameter defines whether the UE supports inter-frequency RSTD measurements for OTDOA positioning as specified in TS 36.355 [13].

### 4.3.17 MBMS parameters

#### 4.3.17.1 mbms-SCell-r11

This parameter defines whether the UE in RRC_CONNECTED supports MBMS reception via MBSFN on a frequency indicated in an MBMSInterestIndication message, when an SCell is configured on that frequency (regardless of whether the SCell is activated or deactivated), as specified in TS 36.331 [5].

#### 4.3.17.2 mbms-NonServingCell-r11

This parameter defines whether the UE in RRC_CONNECTED supports MBMS reception via MBSFN on a frequency indicated in an MBMSInterestIndication message, where (according to supportedBandCombination and to network synchronization properties) a serving cell may be additionally configured, as specified in TS 36.331 [5]. If this is supported, the UE shall also support MBMS reception via MBSFN on a frequency when an SCell is configured on that frequency (regardless of whether the SCell is activated or deactivated), as specified in TS 36.331 [5].

#### 4.3.17.3 mbms-AsyncDC-r12

This parameter defines whether the UE in RRC_CONNECTED supports MBMS reception via MBSFN on a frequency indicated in an MBMSInterestIndication message, where according to supportedBandCombination, the carriers are configured or can be configured as serving cells in the MCG and the SCG which are not synchronized, specified in TS 36.331 [5]. In this release of specification, it is mandatory to support this according to MBMSInterestIndication and indicated supportedBandCombination.

#### 4.3.17.4 fembmsMixedCell-r14

This parameter defines whether the UE in RRC_CONNECTED supports MBMS reception with 15kHz subcarrier spacings via MBSFN from FeMBMS/Unicast mixed cells on a frequency indicated in an MBMSInterestIndication message.

#### 4.3.17.5 fembmsDedicatedCell-r14

This parameter defines whether the UE in RRC_CONNECTED supports MBMS reception with 15kHz subcarrier spacings via MBSFN from MBMS-dedicated cells on a frequency indicated in an MBMSInterestIndication message.

#### 4.3.17.6 subcarrierSpacingMBMS-khz1dot25-r14, subcarrierSpacingMBMS-khz7dot5-r14

This parameter defines the supported subcarrier spacing for MBSFN subframes on FeMBMS/Unicast mixed cells or MBMS-Dedicated cells in addition to 15kHz subcarrier spacing. The subcarrierSpacingMBMS-khz7dot5-r14 refers to 7.5kHz subcarrier spacing and subcarrierSpacingMBMS-khz1dot25-r14 refers to 1.25 kHz subcarrier spacing as defined in TS 36.211 [21], clause 6.12. This field is included only if UE supports MBMS reception from FeMBMS/Unicast mixed cell or MBMS-dedicated cell.

#### 4.3.17.6a subcarrierSpacingMBMS-khz0dot37-r16, subcarrierSpacingMBMS-khz2dot5-r16

This parameter defines for each supported E-UTRA band the supported subcarrier spacing for MBSFN subframes on FeMBMS/Unicast mixed cells or MBMS-Dedicated cells in addition to 15kHz subcarrier spacing. The subcarrierSpacingMBMS-khz0dot37-r16 refers to 0.37 kHz subcarrier spacing and subcarrierSpacingMBMS-khz2dot5-r16 refers to 2.5 kHz subcarrier spacing as defined in TS 36.211 [21], clause 6.12. This field is included only if UE supports MBMS reception from FeMBMS/Unicast mixed cell or MBMS-dedicated cell for the supported E-UTRA band.

#### 4.3.17.7 mbms-MaxBW-r14

This parameter defines the maximum supported bandwidth (T) for MBMS reception, see TS 36.213 [22], clause 11.1. If the value is set to implicitValue, the corresponding value of T is calculated as specified in TS 36.213 [22], clause 11.1. If the value is set to explicitValue, the actual value of T = explicitValue * 40 MHz.

#### 4.3.17.8 mbms-ScalingFactor1dot25-r14, mbms-ScalingFactor7dot5-r14

These parameters correspond to A(1.25 and A(7.5, respectively, i.e., scaling factor for processing one unit of bandwidth corresponding to subcarrier spacing of 1.25 kHz and 7.5 kHz, with respect to one unit of bandwidth corresponding to subcarrier spacing of 15 kHz. See TS 36.213 [22], clause 11.1. The field is included only if UE supports corresponding subcarrier spacing for MBSFN subframes on FeMBMS/Unicast mixed cells or MBMS-Dedicated cells in addition to 15kHz subcarrier spacing. The field shall be included if the UE supports corresponding subcarrier spacing for MBSFN subframes on FeMBMS/Unicast mixed cells or MBMS-Dedicated cells in addition to 15kHz subcarrier spacing and mbms-MaxBW-r14 is included.

#### 4.3.17.9 mbms-ScalingFactor0dot37-r16, mbms-ScalingFactor2dot5-r16

These parameters correspond to A(0.37 / A(2..5, i.e., scaling factor for processing one unit of bandwidth corresponding to subcarrier spacing of 0.37 kHz / 2.5 kHz, with respect to one unit of bandwidth corresponding to subcarrier spacing of 15 kHz. See TS 36.213 [22], clause 11.1. This field is included only if UE supports MBMS reception from FeMBMS/Unicast mixed cell or MBMS-dedicated cell. This field shall be included if subcarrierSpacingMBMS-khz0dot37-r16 / subcarrierSpacingMBMS-khz2dot5-r16 is included for at least one supported E-UTRA band.

#### 4.3.17.10 timeSeparationSlot2-r16, timeSeparationSlot4-r16

These parameters define for each supported E-UTRA band the supported time staggering length of 2 slots (MBSFN reference signal pattern type 2) / 4 slots (MBSFN reference signal pattern type 1) for MBSFN-RS associated with PMCH with subcarrier spacing of 0.37 kHz for MBSFN subframes as described in TS 36.211 [17], clause 6.10.2.2.4. This field is included only if UE supports subcarrier spacing of 0.37 kHz for MBSFN subframes on FeMBMS/Unicast mixed cells or MBMS-Dedicated cells in addition to 15kHz subcarrier spacing.

#### 4.3.17.11 pmch-Bandwidth-n40-r17, pmch-Bandwidth-n35-r17, pmch-Bandwidth-n30-r17

This parameter defines, for the corresponding E-UTRA band, whether the UE in RRC_CONNECTED supports MBMS reception via MBSFN from MBMS-dedicated cells in an MBSFN area with PMCH bandwidth of 40/ 35/ 30 PRBs as described in TS 36.331 [5], TS 36.211 [17] and TS 36.213 [22].

#### 4.3.17.12 cas-Muting-5GB-r19

This parameter defines, for the corresponding E-UTRA band, whether the UE supports reception of LTE-based 5G broadcast with CAS muting from an MBMS-dedicated cell as described in TS 36.331 [5] and TS 36.211 [17].

A UE that supports this feature shall also support fembmsDedicatedCell-r14.

#### 4.3.17.13 timeInterleavingKhz15-r19, timeInterleavingKhz7dot5-r19, timeInterleavingKhz2dot5-r19, timeInterleavingKhz1dot25-r19

This parameter defines, for the corresponding E-UTRA band, whether the UE supports MBMS reception from an MBMS-dedicated cell configured with time interleaving. With time interleaving, one TB is mapped to N non-consecutive subframes and two transmissions of the same TB are separated by (M-1) subframes. A UE that supports this feature shall support the following components:

1) PMCH transmission pattern, excluding MCCH and MSI, with time interleaving for the corresponding PMCH numerology

2) TBS determination for the scaled TB up to a maximum TBS;

3) determining the starting point for reading from the circular buffer (k0) for each subframe;

4) extended MSI periodicities.

A UE which supports this feature shall also support fembmsDedicatedCell-r14 as specified in TS 36.331 [5].

#### 4.3.17.14 pmch-CyclicShiftAlpha1-r19

This parameter defines, for the corresponding E-UTRA band, whether the UE supports cyclic shift of PMCH with alpha1 for the bit sequence in clause 6.3.1 of TS 36.211 [17] for the ith subframe of the time-interleaved TB by X_i bits. A UE which supports this feature shall also support timeInterleaving-r19 as specified in TS 36.331 [5].

#### 4.3.17.15 pmch-CyclicShiftAlpha2-r19

This parameter defines, for the corresponding E-UTRA band, whether the UE supports cyclic shift of PMCH with alpha2 for the bit sequence in clause 6.3.1 of TS 36.211 [17] for the ith subframe of the time-interleaved TB by X_i bits. A UE which supports this feature shall also support timeInterleaving-r19 as specified in TS 36.331 [5].

#### 4.3.17.16 pmch-CyclicShiftAlpha3-r19

This parameter defines, for the corresponding E-UTRA band, whether the UE supports cyclic shift of PMCH with alpha3 for the bit sequence in clause 6.3.1 of TS 36.211 [17] for the ith subframe of the time-interleaved TB by X_i bits. A UE which supports this feature shall also support timeInterleaving-r19 as specified in TS 36.331 [5].

#### 4.3.17.17 freqInterleavingKhz15-r19, freqInterleavingKhz7dot5-r19, freqInterleavingKhz2dot5-r19, freqInterleavingKhz1dot25-r19

This parameter defines, for the corresponding E-UTRA band, whether the UE supports MBMS reception from an MBMS-dedicated cell configured with frequency interleaving. A UE that supports this feature shall support frequency-interleaving for MTCH for the corresponding PMCH numerology.

A UE which supports this feature shall also support fembmsDedicatedCell-r14 as specified in TS 36.331 [5].

### 4.3.18 RAN-assisted WLAN interworking parameters

#### 4.3.18.1 wlan-IW-RAN-Rules-r12

This parameter defines whether the UE supports RAN-assisted WLAN interworking based on access network selection and traffic steering rules specified in TS 36.304 [14]. A UE that supports RAN-assisted WLAN interworking based on access network selection and traffic steering rules specified in TS 36.304 [14] shall support to receive, via system information and dedicated signalling, the RAN assistance parameters relevant for those rules.

#### 4.3.18.2 wlan-IW-ANDSF-Policies-r12

This parameter defines whether the UE supports RAN-assisted WLAN interworking based on ANDSF policies specified in TS 24.312 [21]. A UE that supports RAN-assisted WLAN interworking based on ANDSF policies specified in TS 24.312 [21] shall support to receive, via system information and dedicated signalling, the RAN assistance parameters relevant for those policies.

#### 4.3.18.3 rclwi-r13

This parameter defines whether the UE supports RCLWI as specified in TS 36.331 [5]. A UE that supports RCLWI shall also support WLAN measurements.

### 4.3.19 MAC parameters

#### 4.3.19.1 longDRX-Command-r12

This field defines whether the UE supports Long DRX Command MAC Control Element as specified in TS 36.321 [4]. It is mandatory for UEs of this release of the specification.

#### 4.3.19.2 logicalChannelSR-ProhibitTimer-r12

This field defines whether the UE supports the logicalChannelSR-ProhibitTimer as specified in TS 36.321 [4]. It is mandatory for UEs of any ue-Category-NB to support this feature.

#### 4.3.19.3 extendedMAC-LengthField-r13

This field defines whether the UE supports 16 bit length of MAC L field as specified in TS 36.321 [4].

#### 4.3.19.4 extendedLongDRX-r13

This field defines whether the UE supports the longDRX-Cycle values of 5120 and 10240 subframes as specified in TS 36.321 [4].

#### 4.3.19.5 shortSPS-IntervalFDD-r14

This field indicates whether the UE supports uplink SPS intervals shorter than 10 subframes in FDD mode. A UE that supports shortSPS-IntervalFDD-r14 shall also support skipUplinkSPS-r14.

#### 4.3.19.6 shortSPS-IntervalTDD-r14

This field indicates whether the UE supports uplink SPS intervals shorter than 10 subframes in TDD mode. A UE that supports shortSPS-IntervalTDD-r14 shall also support skipUplinkSPS-r14.

#### 4.3.19.7 skipUplinkDynamic-r14

This field indicates whether the UE supports skipping of UL transmission for an uplink grant indicated on PDCCH if no data is available for transmission as specified in TS 36.321 [4].

#### 4.3.19.8 skipUplinkSPS-r14

This field indicates whether the UE supports skipping of UL transmission for a configured uplink grant if no data is available for transmission as specified in TS 36.321 [4].

#### 4.3.19.9 dataInactMon-r14

This field defines whether the UE supports data inactivity monitoring as specified in TS 36.321 [4].

#### 4.3.19.10 rai-Support-r14

This field defines whether the UE supports Release Assistance Indication (RAI) as specified in TS 36.321 [4]. This field is only applicable if the UE supports UE category M1 or UE category M2 or any ue-Category-NB.

#### 4.3.19.11 multipleUplinkSPS-r14

This field defines whether the UE supports multiple uplink SPS and reporting SPS assistance information. A UE indicating multipleUplinkSPS shall also support V2X communication via Uu, as defined in TS 36.300 [30].

#### 4.3.19.12 min-Proc-TimelineSubslot-r15

This field defines the UE minimum processing timeline supported for subslot operation for the different SPDCCH configurations. The minimum processing timeline is indicated by one of two sets in ProcessingTimelineSet-r15. Each set consists of two different processing timeline options and associated maximum TA. The minimum processing timeline to use out of the two options for a given set is configured by min-proc-TimeTA-SubslotSet1-r15 and min-procTimeTA-SubslotSet2-r15, see TS 36.331 [5]. Support of Set 1 implicitly means support of Set 2.

The sets supported can be different for 1os CRS-based SPDCCH, 2os CRS-based SPDCCH and DMRS-based SPDCCH. The field consists of a sequence of ProcessingTimelineSet-r15. The sequence applies to (in order):

1. 1os CRS based SPDCCH

2. 2os CRS based SPDCCH

3. DMRS based SPDCCH

#### 4.3.19.13 skipSubframeProcessing-r15

This fields defines whether the UE supports, within a serving cell, aborting reception of PDSCH if the UE receives slot-PDSCH/subslot-PDSCH during an ongoing PDSCH reception and instead starts receiving the slot-PDSCH/subslot-PDSCH, as well as whether the UE supports aborting a PUSCH transmission if the UE gets a grant for a slot-PUSCH/ subslot-PUSCH transmission that overlaps with a grant received for a PUSCH transmission. The capability indicates the number of subframes that the UE may drop prior to the subframe in which it prioritizes the processing of slot/subslot PDSCH/PUSCH. Separate capability for UL and DL and per sTTI length in each direction.

#### 4.3.19.14 earlyContentionResolution-r14

This field defines whether the UE supports MAC PDU that contains only the UE Contention Resolution Identity MAC control element but no RRC response message, as specified in TS 36.331 [5]. It is mandatory for UEs that support any ue-Category-NB of this release of the specification.

#### 4.3.19.15 sr-SPS-BSR-r15

This field defines whether the UE supports SR with SPS BSR, as defined in TS 36.321 [4]. This feature is only applicable if the UE supports any ue-Category-NB.

#### 4.3.19.16 dormantSCellState-r15

This field defines whether the UE supports the dormant SCell state, as specified in TS 36.321 [4] and TS 36.331 [5].

#### 4.3.19.17 directSCellActivation-r15

This field defines whether the UE supports having an E-UTRA SCell configured in activated SCell state in the RRCConnectionReconfiguration message, as defined in TS 36.321 [4] and TS 36.331 [5]. This field is applicable to both LTE standalone and LTE-DC.

#### 4.3.19.18 directSCellHibernation-r15

This field defines whether the UE supports having an SCell configured in dormant SCell state, as defined in TS 36.321 [4] and TS 36.331 [5]. A UE that indicates support for this shall also indicate support for dormantSCellState-r15.

#### 4.3.19.19 sps-ServingCell-r15

This field indicates whether the UE supports multiple UL/DL SPS configurations simultaneously active on different serving cells as specified in TS 36.321 [4].

#### 4.3.19.20 extendedLCID-Duplication-r15

This field indicates whether the UE supports use of extended LCIDs 32-38 for PDCP duplication. A UE that supports extendedLCID-Duplication-r15 shall also support the extended LCID as specified in TS 36.321 [4].

#### 4.3.19.21 eLCID-Support-r15

This field indicates whether the UE supports LCID "10000" and MAC PDU subheader containing the eLCID field as specified in TS 36.321 [4].

#### 4.3.19.22 rai-SupportEnh-r16

This field indicates whether the UE supports AS Release Assistance Indication (AS RAI) in Downlink Channel Quality Report and AS RAI MAC Control Element as specified in TS 36.321 [4] when connected to EPC. This feature is only applicable if the UE supports ce-ModeA-r13 or if the UE supports any ue-Category-NB.

#### 4.3.19.23 directMCG-SCellActivationResume-r16

This field defines whether the UE supports having an E-UTRA MCG SCell configured in activated SCell state in the RRCConnectionResume message, as defined in TS 36.321 [4] and TS 36.331 [5];

If the UE indicates support of directMCG-SCellActivationResume-r16, the UE shall also indicate support of resumeWithMCG-SCellConfig-r16.

#### 4.3.19.24 directSCG-SCellActivationResume-r16

This field defines whether the UE supports having an E-UTRA SCG SCell configured in activated SCell state in the RRCConnectionReconfiguration message contained in the RRCResume message, as defined in TS 36.321 [4], TS 36.331 [5] and TS 38.331 [35].

If the UE indicates support of directSCG-SCellActivationResume-r16, the UE shall also indicate support of ne-dc and resumeWithSCG-Config-r16 as specified in TS 38.331 [35].

#### 4.3.19.25 directSCG-SCellActivationNEDC-r16

This field defines whether the UE supports having an E-UTRA SCG SCell configured in activated SCell state in the RRCConnectionReconfiguration message contained in the NR RRCReconfiguration message, as defined in TS 36.321 [4], TS 36.331 [5] and TS 38.331 [35].

If the UE indicates support of directSCG-SCellActivationNEDC-r16, the UE shall also indicate support of ne-dc as specified in TS 38.331 [35].

### 4.3.20 Dual Connectivity parameters

#### 4.3.20.1 drb-TypeSplit-r12

This field defines whether the DRB type of Split bearer is supported by the UE which is capable of DC.

#### 4.3.20.2 drb-TypeSCG-r12

This field defines whether the DRB type of SCG bearer is supported by the UE which is capable of DC.

#### 4.3.20.3 pdcp-TransferSplitUL-r13

This field defines whether the PDCP data transfer toward both CGs for split bearer in UL as specified in TS 36.323 [2] is supported by the UE which is capable of DC. This field is only applicable for UEs supporting the DRB type of Split bearer.

#### 4.3.20.4 ue-SSTD-Meas-r13

This field defines whether the SSTD measurement between the PCell and the PSCell is supported by the UE which is capable of DC.

### 4.3.21 Sidelink parameters

#### 4.3.21.1 commSupportedBands-r12

This field indicates the bands on which the UE supports sidelink communication, as defined in TS 23.303 [24] and specified in TS 36.331 [5]. If a UE supports sidelink communication on at least one band, the UE shall support sidelink communication transmission based on UE autonomous resource selection, eNB scheduled resource allocation, ProSe Per Packet Priority (PPPP) handling and out of coverage sidelink discovery. If a UE supports sidelink communication, the UE shall support 16 sidelink processes for reception of SL-SCH.

#### 4.3.21.2 commSimultaneousTx-r12

This parameter indicates whether the UE supports simultaneous transmission of EUTRA and sidelink communication (on different carriers) in all bands for which the UE indicated simultaneous sidelink and EUTRA support in a band combination (using commSupportedBandsPerBC).

#### 4.3.21.3 discSupportedBands-r12

This field indicates the bands on which the UE supports sidelink discovery, as defined in TS 23.303 [24] and specified in TS 36.331 [5].

#### 4.3.21.4 discScheduledResourceAlloc-r12

This parameter indicates whether the UE supports transmission of discovery announcements based on network scheduled resource allocation. It is mandatory for UEs of this release of the specification to support this feature if sidelink discovery is supported on at least one band (indicated by discSupportedBands-r12).

#### 4.3.21.5 disc-UE-SelectedResourceAlloc-r12

This parameter indicates whether the UE supports transmission of discovery announcements based on UE autonomous resource selection. It is mandatory for UEs of this release of the specification to support this feature if sidelink discovery is supported on at least one band (indicated by discSupportedBands-r12).

#### 4.3.21.6 disc-SLSS-r12

This parameter indicates whether the UE supports SideLink Synchronization Signal (SLSS) transmission and reception for sidelink discovery.

#### 4.3.21.7 discSupportedProc-r12

This parameter indicates the number of processes supported by the UE for reception of sidelink discovery. This field shall be present if sidelink discovery is supported on at least one band (indicated by discSupportedBands-r12).

#### 4.3.21.8 commMultipleTx-r13

This parameter indicates whether the UE supports multiple transmissions of sidelink communication to different destinations in one SC period. If commMultipleTx-r13 is set to supported then the UE supports 8 transmitting sidelink processes.

#### 4.3.21.9 discInterFreqTx-r13

This parameter indicates whether the UE supports sidelink discovery announcements either a) on the primary frequency only or b) on other frequencies also, regardless of the UE configuration (e.g. CA, DC). The UE may set discInterFreqTx-r13 to supported when having a separate transmitter or if it can request sidelink discovery transmission gaps.

#### 4.3.21.10 discPeriodicSLSS-r13

This parameter indicates whether the UE supports periodic Sidelink Synchronization Signal (SLSS) transmission and reception for sidelink discovery. It is mandatory for UEs to support this feature if sidelink PS discovery is supported and it is optional otherwise.

#### 4.3.21.11 discSysInfoReporting-r13

This parameter indicates whether the UE supports reporting of System Information for inter-frequency/PLMN sidelink discovery.

#### 4.3.21.12 zoneBasedPoolSelection-r14

This parameter indicates whether the UE supports zone based transmission resource pool selection for V2X sidelink communication.

#### 4.3.21.13 v2x-HighReception-r14

This parameter indicates whether the UE supports reception of 20 PSCCH in a subframe and decoding of 136 RBs per subframe counting both PSCCH and PSSCH in a band for V2X sidelink communication.

#### 4.3.21.14 v2x-eNB-Scheduled-r14

This parameter indicates whether the UE supports transmitting PSCCH/PSSCH using dynamic scheduling, SPS in eNB scheduled mode for V2X sidelink communication, reporting SPS assistance information and the UE supports maximum transmit power associated with Power class 3 V2X UE, see TS 36.101 [6] in a band.

#### 4.3.21.15 ue-AutonomousWithFullSensing-r14

This parameter indicates whether the UE supports transmitting PSCCH/PSSCH using UE autonomous resource selection mode with full sensing (i.e., continuous channel monitoring) for V2X sidelink communication and the UE supports maximum transmit power associated with Power class 3 V2X UE, see TS 36.101 [6].

#### 4.3.21.16 ue-AutonomousWithPartialSensing-r14

This parameters indicates whether the UE supports transmitting PSCCH/PSSCH using UE autonomous resource selection mode with partial sensing (i.e., channel monitoring in a limited set of subframes) for V2X sidelink communication and the UE supports maximum transmit power associated with Power class 3 V2X UE, see TS 36.101 [6].

#### 4.3.21.17 slss-TxRx-r14

This parameter indicates whether the UE supports SLSS/PSBCH transmission and reception in UE autonomous resource selection mode and eNB scheduled mode for V2X sidelink communication.

#### 4.3.21.18 sl-CongestionControl-r14

This parameter indicates whether the UE supports Channel Busy Ratio measurement and reporting of Channel Busy Ratio measurement to eNB for V2X sidelink communication.

#### 4.3.21.19 v2x-TxWithShortResvInterval-r14

This parameter indicates whether the UE supports 20 ms and 50 ms resource reservation periods for UE autonomous resource selection and eNB scheduled resource allocation for V2X sidelink communication.

#### 4.3.21.20 v2x-numberTxRxTiming-r14

This parameter indicates the number of multiple reference TX/RX timings counted over all the configured sidelink carriers for V2X sidelink communication.

#### 4.3.21.21 v2x-nonAdjacentPSCCH-PSSCH-r14

This parameter indicates whether the UE supports transmission and reception in the configuration of non-adjacent PSCCH and PSSCH for V2X sidelink communication.

#### 4.3.21.22 v2x-HighPower-r14

This parameter indicates whether the UE supports maximum transmit power associated with Power class 2 V2X UE for V2X sidelink transmission in a band, see TS 36.101 [6].

#### 4.3.21.23 v2x-SupportedBandCombinationList-r14

This field indicates the bands on which the UE supports V2X sidelink communication, as defined in TS 23.285 [29] and specified in TS 36.331 [5]. If a UE supports V2X sidelink communication, the UE shall support a maximum number of 8 sidelink processes associated with the Sidelink HARQ Entity for the transmission of V2X sidelink communication on SL-SCH.

#### 4.3.21.24 slss-SupportedTxFreq-r15

This parameter indicates whether the UE supports the SLSS transmission on single carrier or on multiple carriers in the case of sidelink carrier aggregation.

#### 4.3.21.25 sl-64QAM-Tx-r15

This parameter indicates whether the UE supports 64QAM for the transmission of V2X sidelink communication.

#### 4.3.21.26 sl-TxDiversity-r15

This parameter indicates whether the UE supports transmit diversity for V2X sidelink communication. See TS 36.101 [6].

#### 4.3.21.27 v2x-EnhancedHighReception-r15

This parameter indicates whether the UE supports reception of 30 PSCCH in a subframe and decoding of 204 RBs per subframe counting both PSCCH and PSSCH in a band for V2X sidelink communication.

#### 4.3.21.28 sl-64QAM-Rx-r15

This parameter indicates whether the UE supports 64QAM for the reception of V2X sidelink communication. It is mandatory to support 64QAM for the reception of V2X sidelink communication for UEs which are supporting Rel-15 V2X sidelink communication as specified in TS 36.331 [5].

#### 4.3.21.29 sl-RateMatchingTBSScaling-r15

This parameter indicates whether the UE supports rate matching and TBS scaling of V2X sidelink communication. It is mandatory to support rate matching and TBS scaling of V2X sidelink communication for UEs which are supporting Rel-15 V2X sidelink communication as specified in TS 36.331 [5].

#### 4.3.21.30 sl-LowT2min-r15

This parameter indicates whether the UE supports 10ms as minimum value of T2 for resource selection of V2X sidelink communication. It is mandatory to support 10ms as minimum value of T2 of V2X sidelink communication for UEs which are supporting Rel-15 V2X sidelink communication as specified in TS 36.331 [5].

#### 4.3.21.31 v2x-SensingReportingMode3-r15

This parameter indicates whether the UE supports sensing measurements and reporting of measurement results in eNB scheduled mode for V2X sidelink communication.

#### 4.3.21.32 v2x-SupportedBandCombinationListEUTRA-NR-r16

This field indicates the supported band combination list on which the UE supports simultaneous transmission and/or reception of NR sidelink communication only as specified in TS 38.331 [35], or joint V2X sidelink communication and NR sidelink communication as specified in TS 36.331 [5].

#### 4.3.21.33 Void

#### 4.3.21.34 tx-Sidelink-r16, rx-Sidelink-r16

This parameter indicates whether the UE supports sidelink transmission/reception on the band in the band combination. For NR sidelink transmission, tx-Sidelink-r16 is only applicable if the UE supports at least one of sl-TransmissionMode1-r16 and sl-TransmissionMode2-r16 on the band as specified in TS 38.331 [35]. For NR sidelink reception, rx-Sidelink-r16 is only applicable if the UE supports sl-Reception-r16 on the band as specified in TS 38.331 [35].

#### 4.3.21.35 sl-A2X-Service-r18

This parameter indicates whether the UE supports A2X service and dedicated resource pool for A2X service as specified in TS 36.331 [5]. A UE supporting this feature shall also support LTE sidelink in at least one sidelink band.

### 4.3.22 SC-PTM parameters

#### 4.3.22.1 scptm-ParallelReception-r13

This parameter defines whether UEs supporting SC-PTM support the parallel reception of DL-SCH transport block(s) associated with G-RNTI/SC-RNTI and DL-SCH transport block(s) associated with C-RNTI/Semi-Persistent Scheduling C-RNTI as well as the parallel reception of multiple DL-SCH transport blocks associated with G-RNTI/SC-RNTI in the same subframe. In SC-PTM operation, the DL-SCH processing capability is shared between the DL-SCH transport block(s) associated with G-RNTI/SC-RNTI and the DL-SCH transport block(s) associated with C-RNTI/Semi-Persistent Scheduling C-RNTI. A UE that supports scptm-ParallelReception-r13 shall also support SC-PTM reception in RRC_CONNECTED and in RRC_IDLE according to SC-PTM procedures as specified in TS 36.331 [5], TS 36.321 [4] and TS 36.304 [14].

#### 4.3.22.2 Void

#### 4.3.22.3 scptm-SCell-r13

This parameter defines whether UEs supporting SC-PTM support in RRC_CONNECTED, MBMS reception via SC-PTM on a frequency indicated in an MBMSInterestIndication message, when an SCell is configured on that frequency (regardless of whether the SCell is activated or deactivated), as specified in TS 36.331 [5].

#### 4.3.22.4 scptm-NonServingCell-r13

This parameter defines whether UEs supporting SC-PTM support in RRC_CONNECTED, MBMS reception via SC-PTM on a frequency indicated in an MBMSInterestIndication message, where (according to supportedBandCombination and to network synchronization properties) a serving cell may be additionally configured, as specified in TS 36.331 [5]. If this is supported, the UE shall also support MBMS reception via SC-PTM on a frequency when an SCell is configured on that frequency (regardless of whether the SCell is activated or deactivated), as specified in TS 36.331 [5].

#### 4.3.22.5 scptm-AsyncDC-r13

This parameter defines whether the UE in RRC_CONNECTED supports MBMS reception via SC-PTM on a frequency indicated in an MBMSInterestIndication message, where according to supportedBandCombination, the carriers are configured or can be configured as serving cells in the MCG and the SCG which are not synchronized, specified in TS 36.331 [5]. In this release of specification, it is mandatory to support this according to MBMSInterestIndication and indicated supportedBandCombination.

### 4.3.23 LAA parameters

#### 4.3.23.1 downlinkLAA-r13

This field defines whether the UE supports downlink LAA operation including identification of downlink transmissions on LAA cell(s) for full downlink subframes, decoding of common downlink control signalling on LAA cell(s), CSI feedback for LAA cell(s), RRM measurements on LAA cell(s) based on CRS-based DRS.

#### 4.3.23.2 crossCarrierSchedulingLAA-DL-r13

This field defines whether the UE supports cross-carrier scheduling from a licensed carrier for LAA cell(s). This field is only applicable if the UE supports downlink LAA operation.

#### 4.3.23.3 csi-RS-DRS-RRM-MeasurementsLAA-r13

This field defines whether the UE supports performing RRM measurements on LAA cell(s) based on CSI-RS-based DRS. This field is only applicable if the UE supports downlink LAA operation.

#### 4.3.23.4 endingDwPTS-r13

This field defines whether the UE supports reception ending with a subframe occupied for a DwPTS-duration on LAA cell(s) as described in TS 36.211 [17] and TS 36.213 [22]. This field is only applicable if the UE supports downlink LAA operation.

#### 4.3.23.5 secondSlotStartingPosition-r13

This field defines whether the UE supports reception of subframes with second slot starting position on LAA cell(s) as described in TS 36.211 [17] and TS 36.213 [22]. This field is only applicable if the UE supports downlink LAA operation.

#### 4.3.23.6 tm9-LAA-r13

This field defines whether the UE supports tm9 operation on LAA cell(s). This field is only applicable if the UE supports downlink LAA operation.

#### 4.3.23.7 tm10-LAA-r13

This field defines whether the UE supports tm10 operation on LAA cell(s). This field is only applicable if the UE supports downlink LAA operation.

#### 4.3.23.8 uplinkLAA-r14

This field defines whether the UE supports uplink LAA operation.

#### 4.3.23.9 crossCarrierSchedulingLAA-UL-r14

This field defines whether the UE supports cross-carrier scheduling from a licensed carrier for LAA cell(s) for uplink. This field is only applicable if the UE supports uplink LAA operation.

#### 4.3.23.10 twoStepSchedulingTimingInfo-r14

This field defines whether the UE supports two step uplink scheduling using PUSCH trigger A and PUSCH trigger B as defined in TS 36.213 [22]. This field also defines the timing between reception of a PUSCH trigger B and the earliest time the UE supports performing the associated UL transmission. This field is only applicable if the UE supports uplink LAA operation.

#### 4.3.23.11 uss-BlindDecodingAdjustment-r14

This field defines whether the UE supports blind decoding adjustment on UE specific search space as defined in TS 36.213 [22]. This field is only applicable if the UE supports uplink LAA operation.

#### 4.3.23.12 uss-BlindDecodingReduction-r14

This field defines whether the UE supports blind decoding reduction on UE specific search space by not monitoring DCI format 0A/0B/4A/4B as defined in TS 36.213 [22]. This field is only applicable if the UE supports uplink LAA operation.

#### 4.3.23.13 outOfSequenceGrantHandling-r14

This field defines whether the UE supports PUSCH transmissions with out of sequence UL grants as defined in TS 36.213 [22]. This field is only applicable if the UE supports uplink LAA operation.

#### 4.3.23.14 aul-r15

This field defines whether the UE supports Autonomous Uplink as defined in TS 36.321 [4]. This field is only applicable if the UE supports uplink LAA operation.

#### 4.3.23.15 laa-PUSCH-Mode1-r15

This field defines whether the UE supports LAA PUSCH Mode 1 as defined in TS 36.213 [22]. This field is only applicable if the UE supports uplink LAA operation.

#### 4.3.23.16 laa-PUSCH-Mode2-r15

This field defines whether the UE supports LAA PUSCH Mode 2 as defined in TS 36.213 [22]. This field is only applicable if the UE supports uplink LAA operation.

#### 4.3.23.17 laa-PUSCH-Mode3-r15

This field defines whether the UE supports LAA PUSCH Mode 3 as defined in TS 36.213 [22]. This field is only applicable if the UE supports uplink LAA operation.

### 4.3.24 LWIP parameters

#### 4.3.24.1 lwip-r13

This field defines whether the UE supports LWIP operation. A UE which supports LWIP operation shall also support WLAN measurements.

#### 4.3.24.2 lwip-Aggregation-UL-r14

This field defines whether the UE supports aggregation over LWIP in uplink. A UE which supports aggregation over LWIP uplink shall also support LWIP operation.

#### 4.3.24.3 lwip-Aggregation-DL-r14

This field defines whether the UE supports aggregation over LWIP in downlink. A UE which supports aggregation over LWIP downlink shall also support LWIP operation.

### 4.3.25 LWA parameters

#### 4.3.25.1 lwa-r13

This parameter defines whether the UE supports LWA as specified in TS 36.331 [5]. A UE that supports LWA shall also support WLAN measurements. A UE that supports LWA shall also support switched bearer operation.

#### 4.3.25.2 lwa-SplitBearer-r13

Only applicable if the UE supports LWA. This parameter defines whether the UE supports split bearer operation in LWA, i.e. the capability to receive data transmission for the same DRB on both LTE and WLAN simultaneously.

#### 4.3.25.3 lwa-BufferSize-r13

Only applicable if the UE supports LWA. This field indicates whether the UE supports the layer 2 buffer sizes corresponding to "with support for split bearers" columns defined in Tables 4.1-3 and 4.1A-3.

#### 4.3.25.4 wlan-MAC-Address-r13

Only applicable if the UE supports LWA. This parameter defines the WLAN MAC address of the UE.

#### 4.3.25.5 lwa-HO-WithoutWT-Change-r14

Only applicable if the UE supports LWA. This parameter indicates whether the UE supports enhancements to HO operation without WT change for LWA operation as specified in TS36.331 [5].

#### 4.3.25.6 lwa-UL-r14

Only applicable if the UE supports LWA. This parameter indicates whether the UE supports LWA bearer in the UL.

#### 4.3.25.7 Void

#### 4.3.25.8 wlan-SupportedDataRate-r14

Only applicable if the UE supports LWA. This parameter indicates the maximum WLAN data rate supported by the UE for LWA operation.

#### 4.3.25.9 lwa-RLC-UM-r14

Only applicable if the UE supports LWA. This parameter indicates whether the UE supports RLC UM for LWA bearer.

### 4.3.26 Void

#### 4.3.26.1 Void

### 4.3.27 Inter-RAT parameters WLAN

#### 4.3.27.1 supportedBandListWLAN-r13

Only applicable if the UE supports WLAN. This field defines which WLAN frequency bands are supported by the UE.

### 4.3.28 EBF FD-MIMO parameters

#### 4.3.28.1 beamformed-r13

Indicates the UE capabilities concerning beamformed EBF/ FD-MIMO operation (class B), see TS 36.213 [22], clause 7.2.5. The capabilities comprise of a list of pairs of {k-Max, n-MaxList} values with the nth entry indicating the values that the UE supports for each CSI process in case n CSI processes would be configured, with:

- k-Max: Indicating the maximum number of NZP CSI RS resource configurations supported

- n-Max: Indicating the maximum number of NZP CSI RS ports supported within a CSI process.

The capability parameters are provided separately per transmission mode (TM9, TM10), which is applicable for all bands of band combinations except when additionally included per band of band combination per TM indicating the concerned capability is different from the per TM capability.

#### 4.3.28.2 channelMeasRestriction-r13

Indicates whether the UE supports channel measurement restriction, see TS 36.213 [22], clause 7.2.3. The capability parameter is provided separately per transmission mode (TM9, TM10).

#### 4.3.28.3 csi-RS-EnhancementsTDD-r13

Indicates whether the UE supports CSI-RS enhancements applicable for TDD, see TS 36.211 [17], clause 6.10.5. The capability parameter is provided separately per transmission mode (TM9, TM10).

#### 4.3.28.4 dmrs-Enhancements-r13

Indicates whether the UE supports DMRS enhancements for the indicated transmission mode, see TS 36.213 [22], clause 7.1.5B and TS 36.212 [26], clauses 5.3.3.1.5C/ D.

The capability parameter is provided separately per transmission mode (TM9, TM10), which is applicable for all bands of band combinations except when additionally included per band of band combination per TM indicating the concerned capability is different from the per TM capability.

This field is absent when the FD-MIMO capability is provided as part of sTTI/sPT band combinations.

#### 4.3.28.5 interferenceMeasRestriction-r13

Indicates whether the UE supports interference measurement restriction, see TS 36.213 [22], clause 7.2.

#### 4.3.28.6 nonPrecoded-r13

Indicates the UE capabilities concerning non-precoded EBF/ FD-MIMO operation (class A) for CSI-RS and CSI reporting using 8, 12 and 16 antenna ports, see TS 36.213 [22], clause 7.2.

- config1: Indicates support of codebook configuration 1.

- config2: Indicates support of codebook configuration 2.

- config3: Indicates support of codebook configuration 3.

- config4: Indicates support of codebook configuration 4.

The capability parameters are provided separately per transmission mode (TM9, TM10), which is applicable for all bands of band combinations except when additionally included per band of band combination per TM indicating the concerned capability is different from the per TM capability. See also TS 36.331 [5] clause 6.3.6, NOTE 8 in UE-EUTRA-Capability field descriptions.

#### 4.3.28.7 srs-Enhancements-r13

Indicates for a particular transmission mode whether the UE supports SRS enhancements, see TS 36.211 [17], clause 5.5.3.

#### 4.3.28.8 srs-EnhancementsTDD-r13

Indicates for a particular transmission mode whether the UE supports TDD specific SRS enhancements, see TS 36.211 [17], clauses 4.2 and 5.5.3.

#### 4.3.28.9 csi-ReportingAdvanced-r14, csi-ReportingAdvancedMaxPorts-r14

Indicates the maximum number of CSI-RS ports supported by the UE for advanced CSI reporting. The field csi-ReportingAdvanced-r14 is included to indicate 32 CSI-RS ports whereas csi-ReportingAdvancedMaxPorts-r14 is included to indicate 8, 12, 16, 20, 24 or 28 CSI-RS ports (i.e., UE shall not include both csi-ReportingAdvanced-r14 and csi-ReportingAdvancedMaxPorts-r14). The capability parameter is provided separately per transmission mode (TM9, TM10), which is applicable for all bands of band combinations except when additionally included per band of band combination per TM indicating the concerned capability is different from the per TM capability.

#### 4.3.28.10 mimo-CBSR-AdvancedCSI-r15

Indicates whether the UE supports CBSR for advanced CSI reporting with and without amplitude restriction as defined in TS 36.213 [22], clause 7.2.

#### 4.3.28.11 csi-ReportingNP-r14

Indicates whether the UE supports CSI reporting on non-precoded CSI-RS with 20, 24, 28 or 32 antenna ports, see TS 36.213 [22[, Table 7.2.4-9. The capability parameter is provided separately per transmission mode (TM9, TM10), which is applicable for all bands of band combinations except when additionally included per band of band combination per TM indicating the concerned capability is different from the per TM capability. See also TS 36.331 [5] clause 6.3.6, NOTE 8 in UE-EUTRA-Capability field descriptions. A UE indicating support of csi-ReportingNP-r14 shall also indicate support of nonPrecoded-r13.

#### 4.3.28.12 relWeightTwoLayers-r13, relWeightFourLayers-r13, relWeightEightLayers-r13

This field indicates relative weight of processing FD-MIMO with 2/ 4/ 8 layers with respect to non-FD-MIMO with the same number of layers, as described in equation 4.3.28.13-1 and TS 36.331 [5] clause 6.3.6, NOTE 8 in UE-EUTRA-Capability field descriptions. This field can be included only if the UE supports the corresponding number of layers (i.e. 2/ 4/ 8 layers).

#### 4.3.28.13 totalWeightedLayers-r13

This field indicates total number of weighted layers the UE can process for FD-MIMO, as described in equation 4.3.28.13-1 below and TS 36.331 [5] clause 6.3.6, NOTE 8 in UE-EUTRA-Capability field descriptions.

The FD-MIMO processing capability condition is satisfied if:


$$\sum  _{i\in  configured CCs}w_{i}\cdot  l_{i}\leq  y $$


where:

- y is total number of weighted layers the UE can process for FD-MIMO. Value of y is indicated by totalWeightedLayers-r13 for all band combinations except for those (NG)EN-DC/NE-DC band combinations for which fd-MIMO-TotalWeightedLayers is included in ca-ParametersEUTRA (see TS 38.331 [35] and TS 38.306 [32]),

- $ l_{i}$ is the maximum number of DL layers configured for CC $ i $, and

- $ w_{i}={\begin {matrix}relWeightTwoLayers,if CCiis configured with FD-MIMO andl_{i}=2 \\ relWeightFourLayers,if CCiis configured with FD-MIMO andl_{i}=4 \\ \begin {matrix}relWeightEightLayers,if CCiis configured with FD-MIMO andl_{i}=8 \\ 1,if CC i is not configured with FD-MIMO.\end {matrix}\end {matrix}$


Equation 4.3.28.13-1: FD-MIMO processing capability condition.

#### 4.3.28.14 zp-CSI-RS-AperiodicInfo-r14

Indicates whether the UE supports aperiodic ZP-CSI-RS transmission for the indicated transmission mode, see TS 36.213 [22], clause 7.2.1. The capability parameter is provided separately per transmission mode (TM9, TM10).

#### 4.3.28.15 ul-dmrs-Enhancements-r14

Indicates whether the UE supports UL DMRS enhancements, see TS 36.211 [17], clause 6.10.3A. The capability parameter is provided separately per transmission mode (TM9, TM10).

#### 4.3.28.16 densityReductionNP-r14, densityReductionBF-r14

Indicates whether the UE supports CSI-RS density reduction with values 1, 1/2 and 1/3 for non-precoded CSI-RS and beamformed CSI-RS respectively, see TS 36.213 [22], clause 7.2.5. The capability parameter is provided separately per transmission mode (TM9, TM10).

#### 4.3.28.17 hybridCSI-r14

Indicates whether the UE supports hybrid CSI transmission, see TS 36.213 [22], clauses 7.2.1 and 7.2.2. The capability parameter is provided separately per transmission mode (TM9, TM10).

#### 4.3.28.18 semiOL-r14

Indicates whether the UE supports semi-open-loop transmission for the indicated transmission mode, see TS 36.213 [22], clause 7.2.4. The capability parameter is provided separately per transmission mode (TM9, TM10).

#### 4.3.28.19 nzp-CSI-RS-AperiodicInfo-r14

This field indicates the support of aperiodic NZP CSI-RS transmission, separately per transmission mode (TM9, TM10). The field nMaxProc indicates the maximum number of updated CSI process for aperiodic NZP CSI-RS. The field nMaxResource indicates the maximum number of CSI-RS resources which can be activated by MAC CE for aperiodic NZP CSI-RS.

#### 4.3.28.20 nzp-CSI-RS-PeriodicInfo-r14

This field indicates the support of periodic NZP CSI-RS transmission, separately per transmission mode (TM9, TM10). The field nMaxResource indicates the maximum number of CSI-RS resources which can be activated by MAC CE for periodic NZP CSI-RS.

### 4.3.29 CE parameters

#### 4.3.29.1 ce-ModeA-r13

This field defines whether the UE supports operation in coverage enhancement mode A, as specified in TS 36.211 [17], TS 36.213 [22] and TS 36.331 [5], and PRACH CE levels 0 and 1 at Random Access, as specified in TS 36.321 [4]. It is mandatory for UEs of DL category M1, UL category M1, DL category M2 and UL category M2

#### 4.3.29.2 ce-ModeB-r13

This field defines whether the UE supports operation in coverage enhancement mode B, as specified in TS 36.211 [17], TS 36.213 [22] and TS 36.331 [5], and PRACH CE levels 2 and 3 at Random Access, as specified in TS 36.321 [4]. A UE indicating support of ce-ModeB-r13 shall also indicate support of ce-ModeA-r13.

#### 4.3.29.3 intraFreqA3-CE-ModeA-r13

This field defines whether the UE when operating in CE Mode A supports eventA3 for intra-frequency neighbouring cells in normal coverage and CE Mode A, as specified in TS 36.331 [5] and TS 36.133 [16]. It is mandatory for UEs of this release if ce-ModeA-r13 is supported.

#### 4.3.29.4 intraFreqA3-CE-ModeB-r13

This field defines whether the UE when operating in CE Mode B supports eventA3 for intra-frequency neighbouring cells in normal coverage, CE Mode A and CE Mode B, as specified in TS 36.331 [5] and TS 36.133 [16]. It is mandatory for UEs of this release if ce-ModeB-r13 is supported.

#### 4.3.29.5 intraFreqHO-CE-ModeA-r13

This field defines whether the UE when operating in CE Mode A supports intra-frequency handover to target cell in normal coverage and CE Mode A, as specified in TS 36.331 [5] and TS 36.133 [16]. It is mandatory for UEs of this release if ce-ModeA-r13 is supported.

#### 4.3.29.6 intraFreqHO-CE-ModeB-r13

This field defines whether the UE when operating in CE Mode B supports intra-frequency handover to target cell in normal coverage, CE Mode A or CE Mode B, as specified in TS 36.331 [5] and TS 36.133 [16]. It is mandatory for UEs of this release if ce-ModeB-r13 is supported.

#### 4.3.29.7 ue-CE-NeedULGaps-r13

This field defines whether the UE needs UL gaps during continuous uplink transmission in half-duplex FDD as specified in TS 36.331 [5] and TS 36.211 [17].

#### 4.3.29.8 unicastFrequencyHopping-r13

This field, and a specific MAC header field LCID value specified in TS 36.321 [4], define whether the UE supports frequency hopping for unicast MPDCCH/PDSCH (configured by mpdcch-pdsch-HoppingConfig) and unicast PUSCH (configured by pusch-HoppingConfig). It is mandatory for UEs of this release of the specification if ce-ModeA-r13 and/or ce-ModeB-r13 is supported.

#### 4.3.29.9 ce-SwitchWithoutHO-r14

This field defines whether the UE supports switching between normal and CE mode without a handover as specified in TS 36.331 [5]. A UE indicating support of ce-SwitchWithoutHO-r14 shall also indicate support of ce-ModeA-r13 except for UEs of DL category M1, UL category M1, DL category M2 or UL category M2.

#### 4.3.29.10 tm9-CE-ModeA-r13

This field indicates whether the UE supports tm9 operation in CE mode A as specified in TS 36.213 [22], TS 36.321 [4] and TS 36.331 [5]. A UE indicating support of tm9-CE-ModeA-r13 shall also indicate support of ce-ModeA-r13.

#### 4.3.29.11 tm9-CE-ModeB-r13

This field indicates whether the UE supports tm9 operation in CE mode B as specified in TS 36.213 [22], TS 36.321 [4] and TS 36.331 [5]. A UE indicating support of tm9-CE-ModeB-r13 shall also indicate support of ce-ModeB-r13 and tm9-CE-ModeA-r13.

#### 4.3.29.12 tm6-CE-ModeA-r13

This field indicates whether the UE supports tm6 operation in CE mode A as specified in TS 36.213 [22] and TS 36.331 [5]. A UE indicating support of tm6-CE-ModeA-r13 shall also indicate support of ce-ModeA-r13.

#### 4.3.29.13 etws-CMAS-RxInConnCE-ModeA-r16

This field indicates whether the UE supports ETWS/CMAS indication reception in RRC_CONNECTED state when the UE is operating in coverage enhancement mode A as specified in TS 36.331 [5]. A UE indicating support of etws-CMAS-RxInConnCE-ModeA-r16 shall also indicate support of ce-ModeA-r13. This feature is only applicable if the UE supports a UE Category other than Category M1 and M2.

#### 4.3.29.14 etws-CMAS-RxInConnCE-ModeB-r16

This field indicates whether the UE supports ETWS/CMAS indication reception in RRC_CONNECTED state when the UE is operating in coverage enhancement mode B as specified in TS 36.331 [5]. A UE indicating support of etws-CMAS-RxInConnCE-ModeB-r16 shall also indicate support of ce-ModeB-r13. This feature is only applicable if the UE supports a UE Category other than Category M1 and M2.

### 4.3.30 Mobility enhancement parameters

#### 4.3.30.1 makeBeforeBreak-r14

This field defines whether the UE supports Make-Before-Break handover and, if the UE supports DC, Make-Before-Break SeNB change, as specified in TS 36.331 [5].

#### 4.3.30.2 rach-Less-r14

This field defines whether the UE supports RACH-less handover and, if the UE supports DC, RACH-less SeNB change, as specified in TS 36.213 [22] and TS 36.331 [5].

#### 4.3.30.3 cho-r16

This field indicates whether the UE supports conditional handover including execution condition, candidate cell configuration and maximum 8 candidate cells.

#### 4.3.30.4 cho-Failure-r16

This field indicates whether the UE supports conditional handover during re-establishment procedure when the selected cell is configured as candidate cell for condition handover.

#### 4.3.30.5 cho-FDD-TDD-r16

This field indicates whether the UE supports conditional handover between FDD and TDD cells.

#### 4.3.30.6 cho-TwoTriggerEvents-r16

This field indicates whether the UE supports 2 trigger events for the same execution condition. It is mandatory supported if the UE supports cho.

### 4.3.31 Void

#### 4.3.31.1 Void

#### 4.3.31.2 Void

### 4.3.32 MMTEL parameters

#### 4.3.32.1 delayBudgetReporting-r14

This field defines whether the UE supports delay budget reporting as specified in TS 36.331 [5].

#### 4.3.32.2 pusch-Enhancements-r14

This field defines whether the UE supports the PUSCH enhancement mode as specified in TS 36.211 [17] and TS 36.213 [22].

#### 4.3.32.3 recommendedBitRate-r14

This field defines whether the UE supports the bit rate recommendation message from the eNB to the UE as specified in TS 36.321 [4], clause 6.1.3.13.

#### 4.3.32.4 recommendedBitRateQuery-r14

This field defines whether the UE supports the bit rate recommendation query message from the UE to the eNB as specified in TS 36.321 [4], clause 6.1.3.13. This field is only applicable if the UE supports recommendedBitRate-r14.

#### 4.3.32.5 recommendedBitRateMultiplier-r16

This field defines whether the UE supports the bit rate multiplier for recommended bit rate MAC CE as specified in TS 36.321 [4], clause 6.1.3.13. This field is only applicable if the UE supports recommendedBitRate-r14.

### 4.3.33 High speed enhancement parameters

#### 4.3.33.1 measurementEnhancements-r14

This field defines whether UE supports measurement enhancements in high speed scenario as specified in TS 36.133 [16].

#### 4.3.33.2 demodulationEnhancements-r14

This field defines whether the UE supports advanced receiver in SFN scenario as specified in TS 36.101 [6].

#### 4.3.33.3 prach-Enhancements-r14

This field defines whether the UE supports random access preambles generated from restricted set type B in high speed scenario as specified in TS 36.211 [17].

#### 4.3.33.4 measurementEnhancements2-r16

This field defines whether UE supports further enhanced measurements on PCC and timing adjustments to support 500km/h velocity in HST-SFN scenario as specified in TS 36.133 [16]. A UE indicating support of measurementEnhancements2-r16 shall also indicate support of measurementEnhancements-r14.

#### 4.3.33.5 demodulationEnhancements2-r16

This field defines whether the UE supports further enhanced demodulation requirements to support 500km/h velocity in HST-SFN scenario as specified in TS 36.101 [6]. A UE indicating support of demodulationEnhancements2-r16 shall also indicate support of demodulationEnhancements-r14.

#### 4.3.33.6 measurementEnhancementsSCell-r16

This field defines whether the UE supports enhanced measurements on SCC to support 350km/h velocity with active SCells or deactivated SCells as specified in TS 36.133 [16].

#### 4.3.33.7 interRAT-enhancementNR-r16

This field defines whether the UE supports enhanced inter-RAT NR measurement requirements to support high speed up to 500 km/h as specified in TS 36.133 [16], when EN-DC is not configured and when EN-DC is configured.

### 4.3.34 Inter-RAT Parameters NR

#### 4.3.34.1 en-DC-r15

This field indicates whether UE supports E-UTRA NR Dual Connectivity as specified in TS 37.340 [38].

#### 4.3.34.2 supportedBandListEN-DC-r15

Only applicable if the UE supports E-UTRA NR Dual Connectivity or NG-RAN E-UTRA-NR Dual Connectivity. This field includes the supported NR bands as defined in TS 38.101-1 [33] and TS 38.101-2 [34]. The presence of this field also indicates that the UE can perform both NR SS-RSRP and SS-RSRQ measurement in the included NR band(s) as specified in TS 38.215 [36].

#### 4.3.34.3 supportedBandListNR-SA-r15

This field indicates whether UE supports standalone NR, as specified in TS 38.331 [35], and includes the supported NR bands as defined in TS 38.101-1 [33], TS 38.101-2 [34], and TS 38.101-5 [45]. The presence of this field also indicates that the UE can perform both NR SS-RSRP and SS-RSRQ measurement in the included NR band(s) as specified in TS 38.215 [36].

#### 4.3.34.4 eutra-5GC-HO-ToNR-FDD-FR1-r15

This field indicates whether the UE supports handover from E-UTRA/5GC to NR FDD FR1. It is mandatory for UEs of this release of the specification if the UE supports the associated RATs and if the UE supports eutra-5GC-r15.

#### 4.3.34.5 eutra-5GC-HO-ToNR-TDD-FR1-r15

This field indicates whether the UE supports handover from E-UTRA/5GC to NR TDD FR1. It is mandatory for UEs of this release of the specification if the UE supports the associated RATs and if the UE supports eutra-5GC-r15.

#### 4.3.34.6 eutra-5GC-HO-ToNR-FDD-FR2-r15

This field indicates whether the UE supports handover from E-UTRA/5GC to NR FDD FR2. It is mandatory for UEs of this release of the specification if the UE supports the associated RATs and if the UE supports eutra-5GC-r15.

#### 4.3.34.7 eutra-5GC-HO-ToNR-TDD-FR2-r15

This field indicates whether the UE supports handover from E-UTRA/5GC to NR TDD FR2-1. It is mandatory for UEs of this release of the specification if the UE supports the associated RATs and if the UE supports eutra-5GC-r15.

#### 4.3.34.8 eutra-EPC-HO-ToNR-FDD-FR1-r15

This field indicates whether the UE supports handover from E-UTRA/EPC to NR FDD FR1. It is mandatory for UEs of this release of the specification if the UE supports the associated RATs.

#### 4.3.34.9 eutra-EPC-HO-ToNR-TDD-FR1-r15

This field indicates whether the UE supports handover from E-UTRA/EPC to NR TDD FR1. It is mandatory for UEs of this release of the specification if the UE supports the associated RATs.

#### 4.3.34.10 eutra-EPC-HO-ToNR-FDD-FR2-r15

This field indicates whether the UE supports handover from E-UTRA/EPC to NR FDD FR2. It is mandatory for UEs of this release of the specification if the UE supports the associated RATs.

#### 4.3.34.11 eutra-EPC-HO-ToNR-TDD-FR2-r15

This field indicates whether the UE supports handover from E-UTRA/EPC to NR TDD FR2-1. It is mandatory for UEs of this release of the specification if the UE supports the associated RATs.

#### 4.3.34.12 sa-NR-r15

This field indicates whether the UE supports standalone NR as specified in TS 38.331 [35].

#### 4.3.34.13 ims-VoiceOverNR-FR1-r15

This field indicates whether the UE supports IMS voice over NR FR1.

#### 4.3.34.14 ims-VoiceOverNR-FR2-r15

This field indicates whether the UE supports IMS voice over NR FR2-1.

#### 4.3.34.15 eventB2-r15

This field defines whether the UE supports event B2. In this release of specification, it is mandatory for a UE supporting NR SA operation to support eventB2-r15.

#### 4.3.34.16 ss-SINR-Meas-NR-FR1-r15

This field indicates whether the UE can perform NR FR1 SS-SINR measurement as specified in TS 38.215 [36].

#### 4.3.34.17 ss-SINR-Meas-NR-FR2-r15

This field indicates whether the UE can perform NR FR2 SS-SINR measurement as specified in TS 38.215 [36].

#### 4.3.34.18 ng-EN-DC-r15

This field indicates whether UE supports NG-RAN E-UTRA-NR Dual Connectivity as specified in TS 37.340 [38].

#### 4.3.34.19 nr-HO-ToEN-DC-r16

This field indicates whether the UE supports inter-RAT handover from NR to EN-DC while NR-DC or NE-DC is not configured as defined in TS 37.340 [38]. It is mandatory to support inter-RAT handover from NR to EN-DC if the UE supports E-UTRA NR Dual Connectivity.

#### 4.3.34.20 ce-EUTRA-5GC-HO-ToNR-FDD-FR1-r16

This field indicates whether the UE supports handover from E-UTRA/5GC in coverage enhancement mode A or B to NR FDD FR1. A UE indicating support of ce-EUTRA-5GC-HO-ToNR-FDD-FR1-r16 shall also indicate support of ce-EUTRA-5GC-r16. This feature is only applicable if the UE supports a UE Category other than Category M1 and M2.

#### 4.3.34.21 ce-EUTRA-5GC-HO-ToNR-TDD-FR1-r16

This field indicates whether the UE supports handover from E-UTRA/5GC in coverage enhancement mode A or B to NR TDD FR1. A UE indicating support of ce-EUTRA-5GC-HO-ToNR-TDD-FR1-r16 shall also indicate support of ce-EUTRA-5GC-r16. This feature is only applicable if the UE supports a UE Category other than Category M1 and M2.

#### 4.3.34.22 ce-EUTRA-5GC-HO-ToNR-FDD-FR2-r16

This field indicates whether the UE supports handover from E-UTRA/5GC in coverage enhancement mode A or B to NR FDD FR2. A UE indicating support of ce-EUTRA-5GC-HO-ToNR-FDD-FR2-r16 shall also indicate support of ce-EUTRA-5GC-r16. This feature is only applicable if the UE supports a UE Category other than Category M1 and M2.

#### 4.3.34.23 ce-EUTRA-5GC-HO-ToNR-TDD-FR2-r16

This field indicates whether the UE supports handover from E-UTRA/5GC in coverage enhancement mode A or B to NR TDD FR2-1. A UE indicating support of ce-EUTRA-5GC-HO-ToNR-TDD-FR2-r16 shall also indicate support of ce-EUTRA-5GC-r16. This feature is only applicable if the UE supports a UE Category other than Category M1 and M2.

#### 4.3.34.24 extendedBand-n77-r16

This field is only applicable for UEs that indicate support for band n77. If present, the UE supports the restriction to 3450 - 3550 MHz and 3700 - 3980 MHz ranges of band n77 in the USA as specified in Note 12 of Table 5.2-1 in TS 38.101-1 [33]. If absent, the UE supports only restriction to the 3700 - 3980 MHz range of band n77 in the USA. A UE that indicates this field shall also support NS value 55 as specified in TS 38.101-1 [33]. A UE supporting NS value 55 shall indicate this field.

#### 4.3.34.25 eutra-5GC-HO-ToNR-TDD-FR2-2-r17

This field indicates whether the UE supports handover from E-UTRA/5GC to NR TDD FR2-2. A UE that indicates this field also supports eutra-5GC-r15. A UE supporting handover from E-UTRA/5GC to NR TDD FR2-2 shall also support the RRM measurements for FR2-2 as specified in TS 36.331 [5].

#### 4.3.34.26 eutra-EPC-HO-ToNR-TDD-FR2-2-r17

This field indicates whether the UE supports handover from E-UTRA/EPC to NR TDD FR2-2. A UE supporting handover from E-UTRA/EPC to NR TDD FR2-2 shall also support the RRM measurements for FR2-2 as specified in TS 36.331 [5].

#### 4.3.34.27 ims-VoiceOverNR-FR2-2-r17

This field indicates whether the UE supports IMS voice over NR FR2-2.

#### 4.3.34.28 ce-EUTRA-5GC-HO-ToNR-TDD-FR2-2-r17

This field indicates whether the UE supports handover from E-UTRA/5GC in coverage enhancement mode A or B to NR TDD FR2-2. A UE indicating support of ce-EUTRA-5GC-HO-ToNR-TDD-FR2-2-r17 shall also indicate support of ce-EUTRA-5GC-r16. This feature is only applicable if the UE supports a UE Category other than Category M1 and M2.

#### 4.3.34.29 extendedBand-n77-2-r17

This field is only applicable for UEs that indicate support for band n77. If present, the UE supports the restriction to 3450 - 3650 MHz and 3650 - 3980 ranges of band n77 in Canada as specified in Note 12 of Table 5.2-1 in TS 38.101-1 [33]. If absent, the UE supports only restriction to the 3450 - 3650 MHz range of band n77 in Canada. A UE that indicates this field shall also support NS value 57 as specified in TS 38.101-1 [33]. A UE supporting NS value 57 shall indicate this field.

#### 4.3.34.30 ntn-IdleMobilityForNR-r19

This field indicates whether the UE supports the inter-RAT redirection from an E-UTRA terrestrial network cell to an NR NTN cell using satellite assistance information provided by RRCConnectionRelease, and whether the UE supports use of dedicated cell reselection priorities for NR NTN frequencies, as specified in TS 36.304 [14] and TS 36.331 [5].

### 4.3.35 FeCoMP Parameters

#### 4.3.35.1 qcl-CRI-BasedCSI-Reporting-r15

This field indicates whether the UE supports CRI based CSI feedback for the FeCoMP feature as specified in TS 36.213 [22], clause 7.1.10.

#### 4.3.35.2 qcl-TypeC-Operation-r15

This field indicates the support of the following three UE features: QCL Type-C operation for FeCoMP, the capability to support separate PDSCH RE mapping for different PDSCH CWs in non-coherent joint transmission and the capability to support handling new DMRS port to MIMO layer mapping for the CWs, as specified in TS 36.213 [22], clause 7.1.10. The UE includes this field only when all three features are supported by the UE.

### 4.3.36 E-UTRA/5GC Parameters

#### 4.3.36.1 eutra-5GC-r15

This field indicates whether the UE supports E-UTRA/5GC.

#### 4.3.36.2 eutra-EPC-HO-EUTRA-5GC-r15

This field indicates whether the UE supports handover between E-UTRA/EPC and E-UTRA/5GC. It is mandatory for UEs of this release of the specification if the UE supports the associated core networks.

#### 4.3.36.3 Void

#### 4.3.36.4 ho-EUTRA-5GC-FDD-TDD-r15

This field indicates whether the UE supports handover between E-UTRA/5GC FDD and E-UTRA/5GC TDD. It is mandatory for UEs of this release of the specification if the UE supports eutra-5GC-r15 and the associated RATs.

#### 4.3.36.5 ho-InterfreqEUTRA-5GC-r15

This field indicates whether the UE supports inter frequency handover within E-UTRA/5GC. It is mandatory for UEs of this release of the specification.

#### 4.3.36.6 IMS-VoiceOverMCG-BearerEUTRA-5GC-r15

This field indicates whether the UE supports IMS voice over NR PDCP for MCG bearer for E-UTRA/5GC. It is mandated to the IMS voice capable UE if the UE supports eutra-5GC-r15.

#### 4.3.36.7 inactiveState-r15

This field indicates whether the UE supports RRC_INACTIVE. It is mandatory for UEs of this release of the specification if the UE supports eutra-5GC-r15.

#### 4.3.36.8 reflectiveQoS-r15

This field indicates whether the UE supports AS reflective QoS.

#### 4.3.36.9 earlyData-UP-5GC-r16

This field indicates whether the UE supports MO-EDT for User Plane CIoT 5GS optimisations, as defined in TS 24.501 [39]. This feature is only applicable if the UE supports ce-ModeA-r13, or for FDD if the UE supports any ue-Category-NB.

#### 4.3.36.10 ce-InactiveState-r16

This field indicates whether the UE supports RRC_INACTIVE state with extended DRX cycles up to 10.24s without PTW when the UE is operating in coverage enhancement mode A or B as specified in TS 36.331 [5] . A UE indicating support of ce-InactiveState-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.36.11 ce-EUTRA-5GC-r16

This field indicates whether the UE supports E-UTRA/5GC when the UE is operating in coverage enhancement mode A or B as specified in TS 36.331 [5]. A UE indicating support of ce-EUTRA-5GC-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.36.12 inactiveStatePO-Determination-r17

This field indicates whether the UE supports to use the same i_s in RRC_INACTIVE as in RRC_IDLE for PO determination as specified in TS 36.304 [14]. A UE indicating support of inactiveStatePO-Determination-r17 shall also indicate support of inactiveState-r15.

### 4.3.37 PUR parameters

#### 4.3.37.1 pur-CP-EPC-r16

This field indicates whether the UE supports transmission in preconfigured UL resource (PUR) for NB-IoT FDD for Control Plane CIoT EPS optimisation, as defined in TS 36.300 [30]. This feature is only applicable if the UE supports any ue-Category-NB.

#### 4.3.37.2 pur-UP-EPC-r16

This field indicates whether the UE supports transmission in preconfigured UL resource (PUR) for NB-IoT FDD for User Plane CIoT EPS optimisation, as defined in TS 36.300 [30]. This feature is only applicable if the UE supports any ue-Category-NB.

#### 4.3.37.3 pur-CP-5GC-r16

This field indicates whether the UE supports transmission in preconfigured UL resource (PUR) for NB-IoT FDD for Control Plane CIoT 5GS optimisation as specified TS 36.300 [30]. This feature is only applicable if the UE supports any ue-Category-NB.

#### 4.3.37.4 pur-UP-5GC-r16

This field indicates whether the UE supports transmission in preconfigured UL resource (PUR) for NB-IoT FDD for User Plane CIoT 5GS optimisation as specified TS 36.300 [30]. This feature is only applicable if the UE supports any ue-Category-NB.

#### 4.3.37.5 pur-CP-L1Ack-r16

This field indicates whether the UE supports PUR Layer1 acknowledgement as specified in TS 36.213 [22]. A UE indicating support of pur-CP-L1Ack-r16 shall also indicate support of pur-CP-EPC-r16 or pur-CP-5GC-r16 or pur-CP-EPC-CE-ModeA-r16 or pur-CP-5GC-CE-ModeA-r16. This feature is only applicable if the UE supports ce-ModeA-r13, or for FDD if the UE supports any ue-Category-NB.

#### 4.3.37.6 pur-NRSRP-Validation-r16

This field indicates whether the UE supports NRSRP validation for FDD as specified in TS 36.304 [14] and TS 36.331 [5]. A UE indicating support of pur-NRSRP-Validation-r16 shall also indicate support of pur-CP-EPC-r16 or pur-CP-5GC-r16 or pur-UP-EPC-r16 or pur-UP-5GC-r16. This feature is only applicable if the UE supports any ue-Category-NB.

#### 4.3.37.7 pur-CP-EPC-CE-ModeA-r16

This field indicates whether the UE supports transmission in preconfigured UL resources (PUR) for full-PRB for Control Plane CIoT EPS optimisation when the UE is operating in coverage enhancement mode A, as specified in TS 36.300 [30]. A UE indicating support of pur-CP-EPC-CE-ModeA-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.37.8 pur-CP-EPC-CE-ModeB-r16

This field indicates whether the UE supports transmission in preconfigured UL resources (PUR) for full-PRB for Control Plane CIoT EPS optimisation when the UE is operating in coverage enhancement mode B, as specified in TS 36.300 [30]. A UE indicating support of pur-CP-EPC-CE-ModeB-r16 shall also indicate support of pur-CP-EPC-CE-ModeA-r16 and ce-ModeB-r13.

#### 4.3.37.9 pur-UP-EPC-CE-ModeA-r16

This field indicates whether the UE supports transmission in preconfigured UL resources (PUR) for full-PRB for User Plane CIoT EPS optimisation when the UE is operating in coverage enhancement mode A, as specified in TS 36.300 [30]. A UE indicating support of pur-UP-EPC-CE-ModeA-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.37.10 pur-UP-EPC-CE-ModeB-r16

This field indicates whether the UE supports transmission in preconfigured UL resources (PUR) for full-PRB for User Plane CIoT EPS optimisation when the UE is operating in coverage enhancement mode B, as specified in TS 36.300 [30]. A UE indicating support of pur-UP-EPC-CE-ModeB-r16 shall also indicate support of pur-UP-EPC-CE-ModeA-r16 and ce-ModeB-r13.

#### 4.3.37.11 pur-CP-5GC-CE-ModeA-r16

This field indicates whether the UE supports transmission in preconfigured UL resources (PUR) for full-PRB for Control Plane CIoT 5GS optimisation when the UE is operating in coverage enhancement mode A, as specified in TS 36.300 [30]. A UE indicating support of pur-CP-5GC-CE-ModeA-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.37.12 pur-CP-5GC-CE-ModeB-r16

This field indicates whether the UE supports transmission in preconfigured UL resources (PUR) for full-PRB for Control Plane CIoT 5GS optimisation when the UE is operating in coverage enhancement mode B, as specified in TS 36.300 [30]. A UE indicating support of pur-CP-5GC-CE-ModeB-r16 shall also indicate support of pur-CP-5GC-CE-ModeA-r16 and ce-ModeB-r13.

#### 4.3.37.13 pur-UP-5GC-CE-ModeA-r16

This field indicates whether the UE supports transmission in preconfigured UL resources (PUR) for full-PRB for User Plane CIoT 5GS optimisation when the UE is operating in coverage enhancement mode A, as specified in TS 36.300 [30]. A UE indicating support of pur-UP-5GC-CE-ModeA-r16 shall also indicate support of ce-ModeA-r13.

#### 4.3.37.14 pur-UP-5GC-CE-ModeB-r16

This field indicates whether the UE supports transmission in preconfigured UL resources (PUR) for full-PRB for User Plane CIoT 5GS optimisation when the UE is operating in coverage enhancement mode B, as specified in TS 36.300 [30]. A UE indicating support of pur-UP-5GC-CE-ModeB-r16 shall also indicate support of pur-UP-5GC-CE-ModeA-r16 and ce-ModeB-r13.

#### 4.3.37.15 pur-PUSCH-NB-MaxTBS-r16

This field indicates whether the UE supports Combination of PUR for full-PRB with maximum uplink TBS of 2984 bits when the UE is operating in coverage enhancement mode A, as specified in TS 36.213 [22]. A UE indicating support of pur-PUSCH-NB-MaxTBS-r16 shall also indicate support of (pur-CP-EPC-CE-ModeA-r16 or pur-CP-5GC-CE-ModeA-r16 or pur-UP-EPC-CE-ModeA-r16 or pur-UP-5GC-CE-ModeA-r16) and ce-PUSCH-NB-MaxTBS-r14.

#### 4.3.37.16 pur-SubPRB-CE-ModeA-r16

This field indicates whether the UE supports Combination of PUR for sub-PRB when the UE is operating in coverage enhancement mode A, as specified in TS 36.211 [17]. A UE indicating support of pur-SubPRB-CE-ModeA-r16 shall also indicate support of (pur-CP-EPC-CE-ModeA-r16 or pur-CP-5GC-CE-ModeA-r16 or pur-UP-EPC-CE-ModeA-r16 or pur-UP-5GC-CE-ModeA-r16) and ce-PUSCH-SubPRB-Allocation-r15.

#### 4.3.37.17 pur-SubPRB-CE-ModeB-r16

This field indicates whether the UE supports Combination of PUR for sub-PRB when the UE is operating in coverage enhancement mode B, as specified in TS 36.211 [17]. A UE indicating support of pur-SubPRB-CE-ModeB-r16 shall also indicate support of (pur-CP-EPC-CE-ModeB-r16 or pur-CP-5GC-CE-ModeB-r16 or pur-UP-EPC-CE-ModeB-r16 or pur-UP-5GC-CE-ModeB-r16) and ce-PUSCH-SubPRB-Allocation-r15.

#### 4.3.37.18 pur-RSRP-Validation-r16

This field indicates whether the UE supports PUR with serving cell RSRP TA validation, as specified in TS 36.331 [5]. A UE indicating support of pur-RSRP-Validation-r16 shall also indicate support of pur-CP-EPC-CE-ModeA-r16 or pur-CP-5GC-CE-ModeA-r16 or pur-UP-EPC-CE-ModeA-r16 or pur-UP-5GC-CE-ModeA-r16.

#### 4.3.37.19 pur-FrequencyHopping-r16

This field indicates whether the UE supports PUR frequency hopping, as specified in TS 36.213 [22]. A UE indicating support of pur-FrequencyHopping-r16 shall also indicate support of (pur-CP-EPC-CE-ModeA-r16 or pur-CP-5GC-CE-ModeA-r16 or pur-UP-EPC-CE-ModeA-r16 or pur-UP-5GC-CE-ModeA-r16).

### 4.3.38 IoT NTN parameters

#### 4.3.38.1 ntn-Connectivity-EPC-r17

This field indicates whether the UE supports NTN access. This field is only applicable if the UE supports ce-ModeA-r13 or any ue-Category-NB. If the UE indicates this capability the UE shall support the following enhancements:

- General:

- handling of cellBarred-NTN-r17 and trackingAreaList-r17 in SystemInformationBlockType1(-NB) as specified in TS 36.331 [5];

- reception of SystemInformationBlockType31(-NB) as specified in TS 36.331 [5];

- derivation of its position based on its GNSS measurements;

- reporting of the remaining GNSS validity duration as specified in TS 36.331 [5];

- PDCP:

- if the UE supports ce-ModeA-r13, discardTimerExt-r17 as specified in TS 36.331 [5];

- RLC:

- t-ReorderingExt-r17 as specified in TS 36.331 [5];

- MAC:

- estimation of UE-gNB RTT as specified in TS 36.321 [4];

- delaying the start of the RA response window as specified in TS 36.321 [4];

- delaying the start of the mac-ContentionResolutionTimer as specified in TS 36.321 [4];

- if the UE supports ce-ModeA-r13 or if the UE supports any ue-Category-NB and supports sr-WithoutHARQ-ACK-r15, handling of sr-ProhibitTimerOffset-r17 as specified in TS 36.331 [5];

- extending the length of the (UL) HARQ RTT timer as specified in TS 36.321 [4];

- Physical layer:

- calculation of the UE specific TA in RRC_IDLE and RRC_CONNECTED state based on its GNSS-acquired position and the serving satellite ephemeris as specified in TS 36.211 [17];

- calculation of the common TA in RRC_IDLE and RRC_CONNECTED as specified in TS 36.213 [22];

- for TA update in RRC_CONNECTED state, support of combination of both open (i.e. UE specific TA estimation, and common TA calculation) and closed (i.e., received TA commands) control loops;

- frequency pre-compensation to counter shift the Doppler experienced on the service link;

- timing relationship enhancements using higher layer parameters k-Offset-r17 and k-Mac-r17 as specified in TS 36.213 [22];

- segmented UL transmission using higher layer parameters prach-TxDuration-r17, nprach-TxDurationFmt01-r17, nprach-TxDurationFmt2-r17, pucch-TxDuration-r17 and (n)pusch-TxDuration-r17 as specified in TS 36.331 [5] except for UEs indicating support of ue-Category-NB and ntn-ScenarioSupport-r17 with value GSO.

A UE indicating support of ce-ModeA-r13 and ntn-Connectivity-EPC-r17 shall also indicate support of standaloneGNSS-Location. A UE indicating support for any ue-Category-NB and ntn-Connectivity-EPC-r17 is assumed to have GNSS location capability.

#### 4.3.38.2 ntn-TA-Report-r17

This field indicates whether the UE supports Timing advance reporting in NTN cell as specified in TS 36.321 [4]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17.

#### 4.3.38.3 ntn-PUR-TimerDelay-r17

This field indicates whether the UE supports delaying the start of the pur-ResponseWindowTimer for NTN operation as specified in TS36.321 [4]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17. A UE indicating support of ntn-PUR-TimerDelay-r17 shall also indicate support of pur-CP-EPC-CE-ModeA-r16 or pur-UP-EPC-CE-ModeA-r16 or pur-CP-EPC-r16 or pur-UP-EPC-r16.

#### 4.3.38.4 ntn-OffsetTimingEnh-r17

This field indicates whether the UE supports timing relationship enhancements using Differential Koffset as specified in TS 36.321 [4] and TS 36.213 [22]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17.

#### 4.3.38.5 ntn-ScenarioSupport-r17

This field indicates whether the UE supports NTN features in GSO or NGSO scenario. The UE indicating support of ntn-ScenarioSupport-r17 shall also indicate support of ntn-Connectivity-EPC-r17. If a UE does not include this field but includes ntn-Connectivity-EPC-r17, the UE supports the NTN features for both GSO and NGSO scenarios.

#### 4.3.38.6 ntn-SegmentedPrecompensationGaps-r17

This field indicates the supported gap length between segments for PUSCH and PUCCH required by a UE supporting ce-ModeA-r13 or for NPUSCH required by a UE supporting ue-category-NB, for TA pre-compensation. This feature is only applicable if the UE supports either ue-category-NB or ce-ModeA-r13 and also supports ntn-Connectivity-EPC-r17. If a UE does not include this field but includes ntn-Connectivity-EPC-r17, in case of overlapped transmission between successive uplink segments, UE shall follow the procedure specified in TS 36.213 [22]. This field is not applicable for UEs indicating support of ue-Category-NB and ntn-ScenarioSupport-r17 with value GSO.

#### 4.3.38.7 ntn-EventA4BasedCHO-r18

This field indicates whether the UE supports Event A4-based conditional handover, i.e., CondEvent A4 as specified in TS 36.331 [5]. A UE supporting this feature shall also indicate the support of cho-r16 and ntn-Connectivity-EPC-r17.

#### 4.3.38.8 ntn-LocationBasedCHO-EFC-r18

This field indicates whether the UE supports location-based conditional handover for (quasi-)earth fixed cell, i.e., CondEvent D1 as specified in TS 36.331 [5]. A UE supporting this feature shall also indicate the support of cho-r16 and ntn-Connectivity-EPC-r17.

#### 4.3.38.9 ntn-LocationBasedCHO-EMC-r18

This field indicates whether the UE supports location-based conditional handover for earth moving cell, i.e., CondEvent D2 as specified in TS 36.331 [5]. A UE supporting this feature shall also indicate the support of cho-r16 and ntn-Connectivity-EPC-r17.

#### 4.3.38.10 ntn-TimeBasedCHO-r18

This field indicates whether the UE supports time-based conditional handover, i.e., CondEvent T1 as specified in TS 36.331 [5]. A UE supporting this feature shall also indicate the support of cho-r16 and ntn-Connectivity-EPC-r17.

#### 4.3.38.11 ntn-LocationBasedMeasTrigger-EFC-r18

This field indicates whether the UE supports location-based measurement trigger in RRC_CONNECTED in (quasi-)earth fixed cell as specified in TS 36.331 [5]. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17.

#### 4.3.38.12 ntn-LocationBasedMeasTrigger-EMC-r18

This field indicates whether the UE supports location-based measurement trigger in RRC_CONNECTED in earth moving cell as specified in TS 36.331 [5]. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17.

#### 4.3.38.13 ntn-TimeBasedMeasTrigger-r18

This field indicates whether the UE supports time-based measurement trigger in RRC_CONNECTED as specified in TS 36.331 [5]. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17.

#### 4.3.38.14 ntn-RRC-HarqDisableSingleTB-r18

This field indicates whether the UE supports HARQ feedback disabling per HARQ process for downlink transmission by RRC configuration. This feature is only applicable if the UE supports ue-category-NB. A UE supporting this feature shall also indicate the support of ue-category-NB and ntn-Connectivity-EPC-r17.

#### 4.3.38.15 ntn-OverriddenHarqDisableSingleTB-r18

This field indicates whether the UE supports DCI-based HARQ feedback disabling for downlink transmission by overriding the RRC configuration. A UE supporting this feature shall also indicate the support of ntn-RRC-HarqDisableSingleTB-r18.

#### 4.3.38.16 ntn-DCI-HarqDisableSingleTB-r18

This field indicates whether the UE supports DCI-based HARQ feedback disabling for downlink transmission when HARQ feedback disabling per HARQ process for downlink transmission is not configured by RRC. This feature is only applicable if the UE supports ue-category-NB. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17.

#### 4.3.38.17 ntn-RRC-HarqDisableMultiTB-r18

This field indicates whether the UE supports HARQ feedback disabling per HARQ process for downlink transmission by RRC configuration when scheduled with downlink transmission of multiple TBs. This feature is only applicable if the UE supports ue-category-NB. A UE supporting this feature shall also indicate the support of npdsch-MultiTB-r16 and ntn-Connectivity-EPC-r17.

#### 4.3.38.18 ntn-OverriddenHarqDisableMultiTB-r18

This field indicates whether the UE supports DCI-based HARQ feedback disabling for downlink transmission by overriding the RRC configuration when scheduled with downlink transmission of multiple TBs. A UE supporting this feature shall also indicate the support of ntn-RRC-HarqDisableMultiTB-r18.

#### 4.3.38.19 ntn-DCI-HarqDisableMultiTB-r18

This field indicates whether the UE supports DCI-based HARQ feedback disabling for downlink transmission when HARQ feedback disabling per HARQ process for downlink transmission is not configured by RRC and when scheduled with downlink transmission of multiple TBs. This feature is only applicable if the UE supports ue-category-NB. A UE supporting this feature shall also indicate the support of npdsch-MultiTB-r16 and ntn-Connectivity-EPC-r17.

#### 4.3.38.20 ntn-RRC-HarqDisableSingleTB-CE-ModeA-r18

This field indicates whether the UE supports HARQ feedback disabling per HARQ process for downlink transmission by RRC configuration when operating in coverage enhancement mode A. This feature is only applicable if the UE supports ce-ModeA-r13. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17.

#### 4.3.38.21 ntn-RRC-HarqDisableSingleTB-CE-ModeB-r18

This field indicates whether the UE supports HARQ feedback disabling per HARQ process for downlink transmission by RRC configuration when operating in coverage enhancement mode B. This feature is only applicable if the UE supports ce-ModeB-r13. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17.

#### 4.3.38.22 ntn-OverriddenHarqDisableSingleTB-CE-ModeB-r18

This field indicates whether the UE supports DCI-based HARQ feedback disabling for downlink transmission by overriding the RRC configuration when operating in coverage enhancement mode B. A UE supporting this feature shall also indicate the support of ntn-RRC-HarqDisableSingleTB-CE-ModeB-r18.

#### 4.3.38.23 ntn-DCI-HarqDisableSingleTB-CE-ModeB-r18

This field indicates whether the UE supports DCI-based HARQ feedback disabling for downlink transmission when HARQ feedback disabling per HARQ process for downlink transmission is not configured by RRC and operating in coverage enhancement mode B. This feature is only applicable if the UE supports ce-ModeB-r13. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17.

#### 4.3.38.24 ntn-RRC-HarqDisableMultiTB-CE-ModeA-r18

This field indicates whether the UE supports HARQ feedback disabling per HARQ process for downlink transmission by RRC configuration when operating in coverage enhancement mode A and when scheduled with downlink transmission of multiple TBs. This feature is only applicable if the UE supports ce-ModeA-r13. A UE supporting this feature shall also indicate the support of pdsch-MultiTB-CE-ModeA-r16 and ntn-Connectivity-EPC-r17.

#### 4.3.38.25 ntn-RRC-HarqDisableMultiTB-CE-ModeB-r18

This field indicates whether the UE supports HARQ feedback disabling per HARQ process for downlink transmission by RRC configuration when operating in coverage enhancement mode B and when scheduled with downlink transmission of multiple TBs. This feature is only applicable if the UE supports ce-ModeB-r13. A UE supporting this feature shall also indicate the support of pdsch-MultiTB-CE-ModeB-r16 and ntn-Connectivity-EPC-r17.

#### 4.3.38.26 ntn-OverriddenHarqDisableMultiTB-CE-ModeB-r18

This field indicates whether the UE supports DCI-based HARQ feedback disabling for downlink transmission by overriding the RRC configuration when operating in coverage enhancement mode B and when scheduled with downlink transmission of multiple TBs. A UE supporting this feature shall also indicate the support of ntn-RRC-HarqDisableMultiTB-CE-ModeB-r18.

#### 4.3.38.27 ntn-DCI-HarqDisableMultiTB-CE-ModeB-r18

This field indicates whether the UE supports DCI-based HARQ feedback disabling for downlink transmission when HARQ feedback disabling per HARQ process for downlink transmission is not configured by RRC and operating in coverage enhancement mode B and when scheduled with downlink transmission of multiple TBs. This feature is only applicable if the UE supports ce-ModeB-r13. A UE supporting this feature shall also indicate the support of pdsch-MultiTB-CE-ModeB-r16 and ntn-Connectivity-EPC-r17.

#### 4.3.38.28 ntn-SemiStaticHarqDisableSPS-r18

This field indicates whether the UE supports HARQ feedback transmission for the first SPS PDSCH transmission after activation when operating in coverage enhancement mode A. A UE supporting this feature shall also indicate the support of ce-ModeA-r13 and ntn-Connectivity-EPC-r17.

#### 4.3.38.29 ntn-UplinkHarq-ModeB-SingleTB-r18

This field indicates whether the UE supports HARQ Mode B. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17. For a UE indicating support of ce-ModeA-r13, this field also indicates whether the UE supports the corresponding LCP restrictions for uplink transmission.

#### 4.3.38.30 ntn-HarqEnhScenarioSupport-r18

This field indicates whether the UL and DL HARQ process enhancements that are indicated as supported are applicable in GSO or NGSO scenarios for UE indicating support of GSO and NGSO scenarios. If this field is not included, the UL and DL HARQ process enhancements that are indicated as supported are applicable in both GSO and NGSO scenarios. The UL and DL HARQ process enhancements that are indicated as supported are mandatory for GSO scenario. This field is only applicable if the UE supports at least one of ntn-RRC-HarqDisableSingleTB-r18, ntn-OverriddenHarqDisableSingleTB-r18, ntn-DCI-HarqDisableSingleTB-r18, ntn-RRC-HarqDisableMultiTB-r18, ntn-OverriddenHarqDisableMultiTB-r18, ntn-DCI-HarqDisableMultiTB-r18, ntn-RRC-HarqDisableSingleTB-CE-ModeA-r18, ntn-RRC-HarqDisableSingleTB-CE-ModeB-r18, ntn-OverriddenHarqDisableSingleTB-CE-ModeB-r18, ntn-DCI-HarqDisableSingleTB-CE-ModeB-r18, ntn-RRC-HarqDisableMultiTB-CE-ModeA-r18, ntn-RRC-HarqDisableMultiTB-CE-ModeB-r18, ntn-OverriddenHarqDisableMultiTB-CE-ModeB-r18, ntn-DCI-HarqDisableMultiTB-CE-ModeB-r18, ntn-UplinkHarq-ModeB-SingleTB-r18 and ntn-UplinkHarq-ModeB-MultiTB-r18. If ntn-ScenarioSupport-r17 is included, this field is set in consistency with ntn-ScenarioSupport-r17 (i.e., this field is set to GSO if the ntn-ScenarioSupport-r17 indicates GSO).

#### 4.3.38.31 ntn-Triggered-GNSS-Fix-r18

This field indicates whether the UE supports network triggered GNSS position fix in RRC_CONNECTED as specified in TS 36.331 [5]. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17. If the UE indicates this capability, the UE shall support the following enhancements:

- UE reports GNSS position fix time duration for measurement in RRCConnectionSetupComplete (-NB), RRCConnectionResumeComplete (-NB), and RRCConnectionReestablishmentComplete (-NB) and RRCConnectionReconfigurationComplete messages;

- UE receives GNSS measurement trigger from eNB;

- UE re-acquires GNSS position fix within a configured gap;

- UE reports the remaining GNSS validity duration with MAC CE in RRC_CONNECTED.

#### 4.3.38.32 ntn-Autonomous-GNSS-Fix-r18

This field indicates whether the UE supports autonomous GNSS position fix in RRC_CONNECTED as specified in TS 36.331 [5]. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17. A UE supporting ce-ModeA-r13 and this feature in NGSO scenario shall also indicate the support of ntn-Triggered-GNSS-Fix-r18. If the UE indicates this capability, the UE shall support the following enhancements:

- UE reports GNSS position fix time duration for measurement in RRCConnectionSetupComplete (-NB), RRCConnectionResumeComplete (-NB), and RRCConnectionReestablishmentComplete (-NB) and RRCConnectionReconfigurationComplete messages;

- UE re-acquires GNSS autonomously (when configured by the network) if it does not receive eNB GNSS measurement trigger;

- UE reports the remaining GNSS validity duration with MAC CE in RRC_CONNECTED.

#### 4.3.38.33 ntn-UplinkTxExtension-r18

This field indicates whether the UE supports to perform UL transmission in a duration after original GNSS validity duration expires without GNSS re-acquisition as specified in TS 36.331 [5]. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17.

#### 4.3.38.34 ntn-GNSS-EnhScenarioSupport-r18

This field indicates whether the GNSS measurement and UL transmission extension enhancements in RRC_CONNECTED that are indicated as supported are applicable in GSO or NGSO scenario for UE indicating support of GSO and NGSO scenarios. If this field is not included, the GNSS measurement and UL transmission extension enhancements in RRC_CONNECTED that are indicated as supported are applicable in both GSO and NGSO scenario. The GNSS measurement and UL transmission extension enhancements that are indicated as supported are mandatory for GSO scenario. This field is only applicable if the UE supports at least one of ntn-Triggered-GNSS-Fix-r18, ntn-Autonomous-GNSS-Fix-r18 and ntn-UplinkTxExtension-r18. If ntn-ScenarioSupport-r17 is included, this field is set in consistency with ntn-ScenarioSupport-r17 (i.e., this field is set to GSO if the ntn-ScenarioSupport-r17 indicates GSO).

#### 4.3.38.35 ntn-UplinkHarq-ModeB-MultiTB-r18

This field indicates whether the UE supports HARQ Mode B when scheduled with uplink transmission of multiple TBs. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17 and one of npdsch-MultiTB-r16, pdsch-MultiTB-CE-ModeA-r16 and pdsch-MultiTB-CE-ModeB-r16. For a UE indicating support of ce-ModeA-r13, this field also indicates whether the UE supports the corresponding LCP restrictions for uplink transmission.

#### 4.3.38.36 eventD1-MeasReportTrigger-r18

This field indicates whether the UE supports location-based measurement report trigger in RRC_CONNECTED in (quasi-)earth fixed cell (i.e., event D1) as specified in TS 36.331 [5]. This feature is only applicable if the UE supports ce-ModeA-r13. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17.

#### 4.3.38.37 eventD2-MeasReportTrigger-r18

This field indicates whether the UE supports location-based measurement report trigger in RRC_CONNECTED in earth moving cell (i.e., event D2) as specified in TS 36.331 [5]. This feature is only applicable if the UE supports ce-ModeA-r13. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17.

#### 4.3.38.38 satelliteInfoConfigDedicated-r18

This field indicates whether the UE can be configured via dedicated signalling with NTN assistance information (i.e., satelliteId-r18 or ephemeris information in measObjectEUTRA) to measure an NTN cell in RRC_CONNECTED as specified in TS 36.331 [5]. This feature is only applicable if the UE supports ce-ModeA-r13. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17.

#### 4.3.38.39 ntn-MO-CB-Msg3-EDT-UP-r19

This field indicates whether the UE supports MO contention-based Msg3 EDT for User Plane CIoT EPS optimizations, as defined in TS 36.321 [4]. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17. This field is not applicable for UEs operating in coverage enhancement mode B.

#### 4.3.38.40 ntn-OCC-SingleTone-khz3dot75-r19

This field indicates whether the UE supports OCC for single-tone NPUSCH format 1 with 3.75 kHz SCS in RRC_CONNECTED. This feature is only applicable if the UE supports ue-category-NB. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17. If the UE indicates this capability, the UE shall support the following enhancements in RRC_CONNECTED:

- symbol-level length-2 OCC for single-tone NPUSCH format 1 with 3.75 kHz SCS;

- TDM DMRS over 4 slots where DMRS are transmitted in the first 2 slots and DMRS REs are blanked in the next 2 slots, or vice-versa;

- dynamic activation or deactivation of OCC for single-tone NPUSCH format 1 with 3.75 kHz SCS via DCI.

#### 4.3.38.41 ntn-OCC-SingleTone-khz15-r19

This field indicates whether the UE supports OCC for single-tone NPUSCH format 1 with 15 kHz SCS in RRC_CONNECTED. This feature is only applicable if the UE supports ue-category-NB. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17. If the UE indicates this capability, the UE shall support the following enhancements in RRC_CONNECTED:

- slot-level length-2 OCC for single-tone NPUSCH format 1 with 15 kHz SCS;

- Support of CDM DMRS for NPUSCH format 1 with 15 kHz SCS;

- dynamic activation or deactivation of OCC for single-tone NPUSCH format 1 with 15 kHz SCS via DCI.

#### 4.3.38.42 ntn-OCC-EnhScenarioSupport-r19

This field indicates whether the OCC enhancements in RRC_CONNECTED that are indicated as supported are applicable in GSO scenario or NGSO scenario for UE indicating support of both GSO and NGSO scenarios (i.e., for UE not including ntn-ScenarioSupport-r17). If this field is not included, the OCC enhancements in RRC_CONNECTED that are indicated as supported are applicable in both GSO and NGSO scenarios. This field is only applicable if the UE supports at least one of ntn-OCC-SingleTone-khz3dot75-r19 and ntn-OCC-SingleTone-khz15-r19. If ntn-ScenarioSupport-r17 is included, this field is set in consistency with ntn-ScenarioSupport-r17 (i.e., this field is set to GSO if the ntn-ScenarioSupport-r17 indicates GSO).

#### 4.3.38.43 ntn-SF-Mode-r19

This field indicates whether the UE supports accessing a cell operating in Store and Forward mode as specified in TS 36.300 [30]. A UE supporting this feature shall also indicate the support of ntn-Connectivity-EPC-r17.

# 5 Void

# 6 Optional features without UE radio access capability parameters

The following clauses list the optional UE features not having UE radio access capability.

NOTE: This clause does not yet contain complete analysis of all features of this release of specification.

## 6.1 CSG features

It is optional for UE to support some parts of CSG cell and hybrid cell reselection features as specified in TS 36.331 [5], clause B.2.

## 6.2 PWS features

### 6.2.1 ETWS

It is optional for UE to support ETWS reception as specified in TS 36.331 [5].

### 6.2.2 CMAS

It is optional for UE to support CMAS reception as specified in TS 36.331 [5]. It is optional for a CMAS-capable UE to support Geofencing information (warningAreaCoordinates-r15) as specified in TS 36.331 [5].

### 6.2.3 KPAS

It is optional for UE to support KPAS reception as specified in TS 36.331 [5]. The Korean Public Alert System (KPAS) uses the same AS mechanisms as defined for CMAS. Therefore a KPAS-capable UE shall support all behaviour that is included in TS 36.331 [5] and TS 36.304 [14] for a CMAS-capable UE.

### 6.2.4 EU-Alert

It is optional for UE to support EU-Alert reception as specified in TS 36.331 [5]. The Europearn Union Warning System EU-Alert uses the same AS mechanisms as defined for CMAS. Therefore a EU-Alert-capable UE shall support all behaviour that is included in TS 36.331 [5] and TS 36.304 [14] for a CMAS-capable UE.

## 6.3 MBMS features

It is optional for UE to support MBMS procedures as specified in TS 36.331 [5].

### 6.3.1 MBMS Service Continuity

It is optional for UE to support MBMS Service Continuity for UEs supporting MBMS as specified in TS 36.331 [5].

### 6.3.2 MBMS reception with 256QAM

It is optional to support MBMS reception with 256QAM for UEs supporting MBMS. A UE which supports MBMS reception with 256QAM shall also support dl-256QAM-r12 as specified in TS 36.331 [5], except UEs configured to operate in Receive Only Mode as defined in TS 23.246 [31].

### 6.3.3 PBCH repetition in CAS

It is optional to support PBCH repetition in CAS for UEs supporting MBMS as specified in TS 36.211 [17]. A UE which supports PBCH repetition in CAS shall also support fembmsDedicatedCell-r14 as specified in TS 36.331 [5].

### 6.3.4 PDCCH AL16 for CAS in MBMS-dedicated cell

It is optional to support of PDCCH AL16 for CAS in MBMS-dedicated cell for UEs supporting MBMS as specified in TS 36.211 [17]. A UE which supports PDCCH AL16 for CAS in MBMS-dedicated cell shall also support fembmsDedicatedCell-r14 as specified in TS 36.331 [5].

### 6.3.5 Semi-static CFI indication in MIB

It is optional to support semi-static CFI indication in MIB for UEs supporting MBMS as specified in TS 36.331 [5]. A UE which supports semi-static CFI indication in MIB shall also support fembmsDedicatedCell-r14 as specified in TS 36.331 [5].

### 6.3.6 MBMS reception using Receive Only Mode

It is optional to support indication of MBMS reception using Receive Only Mode in an MBMSInterestIndication message for UEs supporting MBMS as specified in TS 36.331 [5].

## 6.4 Void

## 6.5 Positioning features

### 6.5.0 Void

### 6.5.1 Void

## 6.6 UE receiver features

### 6.6.1 MMSE with IRC receiver

It is optional for UE to support MMSE with IRC receiver for all PDSCH transmission modes except for transmission mode 9.

### 6.6.2 MMSE with IRC receiver for PDSCH transmission mode 9

It is optional for UE to support MMSE with IRC receiver for PDSCH transmission mode 9, if the UE supports MMSE with IRC receiver as described in clause 6.6.1.

### 6.6.3 Single-user MIMO interference mitigation advanced receiver for UEs with 2 receiver antenna ports

It is optional for UE with 2 receiver antenna ports to support receivers with enhanced inter-stream interference suppression for SU-MIMO PDSCH with rank 2 (Enhanced performance requirements Type C for 2 receiver antenna ports capable UEs in the TS 36.101 [6]).

### 6.6.4 Single-user MIMO interference mitigation advanced receiver for UEs with 4 receiver antenna ports

It is optional for UE with 4 receiver antenna ports to support R-ML receivers with enhanced inter-stream interference suppression for SU-MIMO PDSCH with rank 2, 3, and 4 (Enhanced performance requirements Type C for 4 receiver antenna ports capable UEs in the TS 36.101 [6]).

### 6.6.5 MMSE-IRC DL Control Channel interference mitigation receiver for UEs with 4 receiver antenna ports

It is optional for UE with 4 receiver antenna ports to support MMSE-IRC DL Control Channel interference mitigation receivers for UEs with 4 receiver ports (Enhanced downlink control channel performance requirements Type A for 4 receiver antenna ports capable UEs in the TS 36.101 [6]).

## 6.7 RRC Connection

### 6.7.1 RRC Connection Reject with deprioritisation

It is optional for UE to support RRCConnectionReject with deprioritisationReq as specified in TS 36.331 [5].

### 6.7.2 RRC Connection Establishment Failure Temporary Qoffset

It is optional for UE to support RRC Connection Establishment failure temporary Qoffset as specified in TS 36.331 [5].

### 6.7.3 mo-VoiceCall establishment cause for mobile originating MMTEL video

It is optional for UE to support mo-VoiceCall establishment cause for mobile originating MMTEL video as specified in TS 36.331 [5].

### 6.7.4 mo-VoiceCall establishment cause for mobile originating MMTEL voice

It is optional for UE to support mo-VoiceCall establishment cause for mobile originating MMTEL voice as specified in TS 36.331 [5].

### 6.7.5 RRC Connection Re-establishment for the Control Plane CIoT EPS Optimization

It is optional for UE to support RRCConnectionReestablishment for the Control Plane CIoT EPS Optimization as specified in TS 36.331 [5]. This feature is only applicable if the UE supports any ue-Category-NB.

### 6.7.6 Void

## 6.8 Other features

### 6.8.1 System Information Block Type 16

It is optional for UE, including UEs of any ue- Category-NB, to support the reception of SystemInformationBlockType16 as specified in TS 36.331 [5].

### 6.8.2 QCI1 indication in Radio Link Failure Report

It is optional for the UE to include drb-EstablishedWithQCI-1 in RLF-Report as specified in TS 36.331 [5].

### 6.8.3 Enhanced random access power control

It is optional for UE to support enhanced random access power control for FDD as specified in TS 36.321 [4] and TS 36.213 [22], clauses 16.2.1.1.1 and 16.3.1. This feature is only applicable if the UE supports any ue-Category-NB.

### 6.8.4 MO-EDT for Control Plane CIoT EPS Optimization

It is optional for UE to support MO-EDT for Control Plane CIoT EPS optimizations as specified in TS 24.301 [28]. This feature is only applicable if the UE supports ce-ModeA-r13, or for FDD if the UE supports any ue-Category-NB.

### 6.8.5 Void

### 6.8.6 Enhanced PHR

It is optional for UE to support enhanced PHR in MSG3 for FDD, as defined in TS 36.321 [4]. This feature is only applicable if the UE supports any ue-Category-NB.

### 6.8.7 void

### 6.8.8 Resynchronization Signals

It is optional for UE to support resynchronization signals, as defined in TS 36.211 [17]. This feature is only applicable if the UE supports ce-ModeA-r13.

### 6.8.9 Measurement gaps for higher UE velocity

It is optional for UE to support measurement gaps for higher UE velocity, as defined in TS 36.331 [5] and TS 36.133[16]. This feature is only applicable if the UE supports ce-ModeA-r13.

### 6.8.10 MT-EDT for Control Plane CIoT EPS Optimisation

It is optional for UE to support MT-EDT for Control Plane CIoT EPS Optimisation, as defined in TS 24.301 [28]. If the UE supports 'MT-EDT for Control Plane CIoT EPS Optimisation' it shall support 'MO-EDT for Control Plane CIoT EPS Optimisation' as described in clause 6.8.4. This feature is only applicable if the UE supports ce-ModeA-r13, or for FDD if the UE supports any ue-Category-NB.

### 6.8.11 MT-EDT for User Plane CIoT EPS Optimisation

It is optional for UE to support MT-EDT for User Plane CIoT EPS Optimisation, as defined in TS 24.301 [28]. If the UE supports 'MT-EDT for User Plane CIoT EPS Optimisation' it shall support earlyData-UP-r15 as described in clause 4.3.8.7. This feature is only applicable if the UE supports ce-ModeA-r13, or for FDD if the UE supports any ue-Category-NB.

### 6.8.12 Void

### 6.8.13 Reduced MIB/SIB1-BR acquisition time

It is optional for UE to support reduced MIB/SIB1-BR acquisition time requirements as specified in TS 36.133 [16]. This feature is only applicable if the UE supports ce-ModeB-r13.

### 6.8.14 High speed dedicated network features

It is optional for UE to support HSDN cell reselection handling in RRC_IDLE and RRC_INACTIVE (if the UE supports eutra-5GC-r15) as specified in TS 36.304 [14] and TS 36.331 [5].

### 6.8.15 Carrier specific NRSRP thresholds for NPRACH resource selection

It is optional for UE to support carrier specific NRSRP thresholds for NPRACH resource selection as specified in TS 36.321 [4]. This feature is only applicable if the UE supports any ue-Category-NB and multiCarrier-NPRACH-r14 or multiCarrierPagingTDD-r15.

### 6.8.16 Protection against improper reselection to GERAN/UTRAN

It is optional for UE to support protection against improper reselection to GERAN/UTRAN as specified in TS 36.304 [14].

### 6.8.17 Inter-RAT cell reselection of an NR mobile IAB cell

It is optional for UE to support inter-RAT cell reselection priority handling of an NR mobile IAB cell in RRC_IDLE and RRC_INACTIVE (if the UE supports eutra-5GC-r15) as specified in TS 36.304 [14] and TS 36.331 [5].

### 6.8.18 Inter-RAT measurement on an NR NTN cell

It is optional for UE in RRC_IDLE, or in RRC_INACTIVE (if the UE supports eutra-5GC-r15) to support inter-RAT measurement for cell reselection from an E-UTRA terrestrial network cell to an NR NTN cell as specified in TS 36.304 [14] and TS 36.331 [5].

### 6.8.19 Minimization of service interruption in EPS

It is optional for UE to support minimization of service interruption including reporting to NAS of disaster roaming information for available PLMNs and Access Barring check for disaster roaming services in EPS, as specified in TS 36.331 [5].

## 6.9 Void

## 6.10 SON features

### 6.10.1 Radio Link Failure Report for inter-RAT MRO

It is optional for UE to include previousUTRA-CellId and selectedUTRA-CellId in RLF-Report upon request from the network as specified in TS 36.331 [5].

### 6.10.2 Radio Link Failure Report for NB-IoT

It is optional for UE to support the storage of RLF-Report and the reporting in UEInformationResponse message as specified in TS 36.331 [5] when connected to EPC. This feature is only applicable if the UE supports any ue-Category-NB.

### 6.10.3 Radio Link Failure Report for inter-RAT MRO NR

It is optional for UE to include previousNR-PCellId, failedNR-PCellId and nrReconnectCellId in RLF-Report upon request from the network as specified in TS 36.331 [5].

### 6.10.4 LTE RLF report for voice fallback in LTE

It is optional for UE to include voiceFallbackHO in RLF-Report upon request from the network as specified in TS 36.331 [5], when an RLF occurs shortly after successful HO from NR to E-UTRAN for voice fallback.

### 6.10.5 SCG failure information for EN-DC MRO

It is optional for UE to include previousPSCellId, failedPSCellId, timeSCG-Failure and perRA-InfoListNR in SCGFailureInformationNR message as specified in TS 36.331 [5].

## 6.11 Mobility state features

### 6.11.1 Mobility history information storage

It is optional for UE to support the storage of mobility history information and the reporting in UEInformationResponse message as specified in TS 36.331 [5].

## 6.12 Void

## 6.13 Sidelink features

### 6.13.1 Sidelink Relay UE operation

It is optional for UE to support sidelink relay UE operation as specified in TS 36.331 [5].

### 6.13.2 Sidelink Remote UE operation

It is optional for UE to support sidelink remote UE operation as specified in TS 36.331 [5].

### 6.13.3 Sidelink discovery gap

It is optional for UE to support sidelink discovery gaps as specified in TS 36.331 [5].

### 6.13.4 Enhanced sidelink resource selection

It is optional for limited TX capability UE to support enhanced sidelink resource selection with carrier aggregation as specified in clause 5.14.1.1 of TS 36.321 [4].

### 6.13.5 Short-term time-scale TDM for in-device coexistence

It is optional for UE to support prioritization between LTE sidelink transmission/reception and NR sidelink transmission/reception. This feature is only applicable if the UE supports at least one of sl-Reception-r16, sl-TransmissionMode1-r16 and sl-TransmissionMode2-r16 as specified in TS 38.331 [35], and if UE supports LTE V2X sidelink in the band combination.

## 6.14 DRX features

### 6.14.1 Extended DRX in RRC_IDLE

It is optional for UE to support extended DRX cycle values up to and beyond 10.24 seconds and paging in extended DRX in RRC_IDLE as specified in TS 36.331 [5] and TS 36.304 [14].

## 6.15 Load balancing features

### 6.15.1 Redistribution in RRC_IDLE

It is optional for UE to support redistribution in RRC_IDLE as specified in TS 36.331 [5] and TS 36.304 [14].

## 6.16 SC-PTM features

### 6.16.1 SC-PTM in Idle mode

It is optional for UE to support the SC-PTM reception in RRC_IDLE as specified in TS 36.331 [5]. This feature is only applicable if the UE supports UE category M1 or UE category M2 or if the UE supports coverage enhancements (ce-ModeB-r13 and/or ce-ModeA-r13) or for FDD, if the UE supports any ue-Category-NB.

### 6.16.2 Multiple TB scheduling for SC-PTM in Idle mode for NB-IoT

It is optional for UE to support multiple TB scheduling for multicast as specified in TS 36.331 [5] when connected to EPC. This feature is only applicable for FDD if the UE supports any ue-Category-NB.

### 6.16.3 Multiple TB scheduling for SC-PTM in Idle mode for CE Mode A

It is optional for UE to support multiple TB scheduling for multicast as specified in TS 36.331 [5] when connected to EPC. This feature is only applicable if the UE supports ce-ModeA-r13.

### 6.16.4 Multiple TB scheduling for SC-PTM in Idle mode for CE Mode B

It is optional for UE to support multiple TB scheduling for multicast as specified in TS 36.331 [5] when connected to EPC. This feature is only applicable if the UE supports ce-ModeB-r13.

## 6.17 Idle mode measurements

### 6.17.1 Relaxed monitoring

It is optional for UE to support relaxed monitoring in RRC_IDLE as specified in TS 36.304 [14]. This feature is only applicable if the UE supports any ue-Category-NB or if the UE supports UE category M1 or UE category M2 or if the UE supports coverage enhancements (ce-ModeB-r13 and/or ce-ModeA-r13).

### 6.17.2 DL channel quality reporting in Msg3 for the anchor carrier

It is optional for UE to support DL channel quality reporting in Msg3 for the anchor carrier for FDD, as specified in TS 36.331 [5]. This feature is only applicable if the UE supports any ue-Category-NB.

### 6.17.3 Serving cell idle mode measurements reporting

It is optional for UE to include measResultServCell-r14 in RRCConnectionRestablishmentComplete-NB, RRCConnectionResumeComplete-NB and RRCConnectionSetupComplete-NB messages as specified in TS 36.331 [5]. This feature is only applicable if the UE supports any ue-Category-NB.

### 6.17.4 NSSS-Based RRM measurements

It is optional for UE to support NSSS-Based RRM measurements for FDD, as specified in TS 36.211 [17] and TS 36.214 [23]. This feature is only applicable if the UE supports any ue-Category-NB.

### 6.17.5 NPBCH-Based RRM measurements

It is optional for UE to support NPBCH-Based RRM measurements for the serving cell for FDD, as specified in TS 36.214 [23]. This feature is only applicable if the UE supports any ue-Category-NB.

### 6.17.6 RRM measurements on non-anchor paging carriers

It is optional for UE to support idle mode RRM measurements on non-anchor paging carriers for FDD, as specified in TS 36.133 [6]. A UE supporting RRM measurements on non-anchor paging carriers shall also support NRS presence on non-anchor paging carriers. This feature is only applicable if the UE supports any ue-Category-NB.

### 6.17.7 NRS presence on non-anchor paging carriers

It is optional for UE to support NRS presence on non-anchor paging carriers for FDD as specified in TS 36.211 [17]. This feature is only applicable if the UE supports any ue-Category-NB.

### 6.17.8 DL channel quality reporting in Msg3 for non-anchor carrier

It is optional for UE to support DL channel quality reporting for a non-anchor carrier for FDD in Msg3 as specified in TS 36.331 [5]. This feature is only applicable if the UE supports any ue-Category-NB.

### 6.17.9 Assistance information for inter-RAT cell selection to/from NB-IoT

It is optional for UE to support assistance information for inter-RAT cell selection to/from NB-IoT as specified in TS 36.331 [5]. This feature is only applicable if the UE supports any ue-Category-NB.

### 6.17.10 DL channel quality reporting in Msg3

It is optional for UE to support DL channel quality reporting of the serving cell in Msg3, as specified in TS 36.321 [4]. This feature is only applicable if the UE supports ce-ModeA-r13.

### 6.17.11 Relaxed RRM measurements

It is optional for UE to support relaxation of RRM measurements for serving cell while using WUS, as specified in TS 36.133 [16]. This feature is only applicable if the UE supports ce-ModeA-r13 and (wakeUpSignal-r15 or groupWakeUpSignal-r16 or wakeUpSignal-TDD-r15 or groupWakeUpSignalTDD-r16).

### 6.17.12 RSS based measurement improvement

It is optional for UE to support improved DL RSRP measurement accuracy through use of RSS in RRC_IDLE as specified in TS 36.133 [16]. This feature is only applicable if the UE supports resynchronization signals as defined in 6.8.8.

### 6.17.13 RSS based measurement in paging MPDCCH narrowband

It is optional for UE to support measurement of the neighbour cell RSS in the same narrowband as the paging MPDCCH narrowband in RRC_IDLE as specified in TS 36.133 [16]. This feature is only applicable if the UE supports resynchronization signals as defined in 6.8.8.

## 6.18 E-UTRA/5GC features

### 6.18.1 Void

### 6.18.2 Void

### 6.18.3 RRC Connection Re-establishment for the Control Plane CIoT 5GS Optimisation

It is optional for UE to support RRCConnectionReestablishment for the Control Plane CIoT 5GS Optimisation as specified in TS 36.331 [5]. A UE supporting RRCConnectionReestablishment for the Control Plane CIoT 5GS Optimisation shall also support NB-IoT/5GC. This feature is only applicable if the UE supports any ue-Category-NB.

### 6.18.4 NB-IoT/5GC

It is optional for UE to support NB-IoT when connected to 5GC. This feature is only applicable if the UE supports any ue-Category-NB.

### 6.18.5 MO-EDT for Control Plane CIoT 5GS Optimisation

It is optional for UE to support MO-EDT for Control Plane CIoT 5GS optimisations as specified in TS 24.501 [39]. A UE supporting MO-EDT for the Control Plane CIoT 5GS Optimisation shall also support NB-IoT/5GC or indicate support of ce-EUTRA-5GC-r16. This feature is only applicable if the UE supports ce-ModeA-r13, or for FDD if the UE supports any ue-Category-NB.

### 6.18.6 AS RAI

It is optional for UE to support AS Release Assistance Indication (AS RAI) in Downlink Channel Quality Report and AS RAI MAC Control Element as specified in TS 36.321 [4] when connected to 5GC. A UE supporting AS RAI shall also support NB-IoT/5GC or indicate support of ce-EUTRA-5GC-r16. This feature is only applicable if the UE supports ce-ModeA-r13 or if the UE supports any ue-Category-NB.

### 6.18.7 Minimization of service interruption

It is optional for UE to support minimization of service interruption including reporting to NAS of disaster roaming information for available PLMNs and Access Barring check for Access Identity 3, as specified in TS 36.331 [5].

## 6.19 IoT NTN Features

### 6.19.1 Cell reselection measurements triggering based on service time

It is optional for UE camped on NTN cell to support triggering of early cell reselection measurements based on the service time broadcasted by the cell as specified in TS 36.304 [14]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17.

### 6.19.2 Discontinuous coverage

It is optional for a UE camped on NTN cell to support discontinuous coverage as specified in TS 36.304 [14]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17.

### 6.19.3 Early RLF triggering based on service time

It is optional for UE in RRC_CONNECTED in an NTN cell to support triggering of RLF upon reaching the service time broadcasted for the serving cell as specified in TS 36.331 [5]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17.

### 6.19.4 Neighbour cell measurements based on service start time of the neighbour cell

It is optional for UE camped on NTN cell to support NTN neighbour cell measurements based on the service start time of the neighbour cell broadcasted by the serving cell as specified in TS 36.304 [14]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17.

### 6.19.5 UE autonomous release based on service time

It is optional for UE in RRC_CONNECTED in an NTN cell to go to RRC_IDLE after RLF is triggered if the UE determines by implementation there is not enough time to finish the procedure of reestablishment due to the discontinuous coverage as specified in TS 36.331 [5]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17.

### 6.19.6 Cell reselection measurements triggering based on location for (quasi-)fixed cell

It is optional for UE camped on NTN (quasi-)earth fixed cell to support triggering of early cell reselection measurements based on the reference location broadcasted by the cell as specified in TS 36.304 [14]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17.

### 6.19.7 Cell reselection measurements triggering based on location for earth moving cell

It is optional for UE camped on NTN earth moving cell to support triggering of early cell reselection measurements based on the reference location and associated reference time and ephemeris broadcasted by the cell as specified in TS 36.304 [14]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17.

### 6.19.8 GNSS measurements during inactive time

It is optional for UE in RRC_CONNECTED in an NTN cell to perform GNSS measurements during inactive time of a C-DRX cycle. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17.

### 6.19.9 SystemInformationBlockType33(-NB) reception in a TN cell

It is optional for a UE in RRC_IDLE to support the reception of SystemInformationBlockType33(-NB) in a TN cell as specified in TS 36.331 [5]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17.

### 6.19.10 Inband operation with NR NTN

It is optional for a UE to support inband operation with NR NTN as specified in TS 36.102 [43]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17 and any ue-Category-NB.

### 6.19.11 MO-CB-Msg3-EDT for Control Plane CIoT EPS Optimization

It is optional for UE to support MO contention-based Msg3 EDT for Control Plane CIoT EPS optimizations as specified in TS 36.300 [30]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17. This field is not applicable for UEs operating in coverage enhancement mode B.

### 6.19.12 MT-CB-Msg3-EDT for Control Plane CIoT EPS Optimization

It is optional for UE to support MT contention-based Msg3 EDT for Control Plane CIoT EPS optimizations as specified in TS 36.300 [30]. If the UE supports 'MT-CB-Msg3-EDT for Control Plane CIoT EPS Optimisation' it shall support 'MO-CB-Msg3-EDT for Control Plane CIoT EPS Optimisation' as described in clause 6.19.11. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17. This field is not applicable for UEs operating in coverage enhancement mode B.

### 6.19.13 MT-CB-Msg3-EDT for User Plane CIoT EPS Optimization

It is optional for UE to support MT contention-based Msg3 EDT for User Plane CIoT EPS optimizations as specified in TS 36.300 [30]. If the UE supports 'MT-CB-Msg3-EDT for User Plane CIoT EPS Optimisation' it shall support 'ntn-MO-CB-Msg3-EDT-UP-r19' as described in clause 4.3.38.39. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17. This field is not applicable for UEs operating in coverage enhancement mode B.

### 6.19.14 Geofencing of PWS message

It is optional for a PWS-capable UE to support Geofencing information as specified in TS 36.331 [5]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17.

### 6.19.15 Inter-RAT cell selection to NB-IoT NTN

It is optional for UE to support inter-RAT cell selection to an NB-IoT NTN cell using the satellite assistance information in system information as specified in TS 36.331 [5]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17 and any ue-Category-NB.

### 6.19.16 Inter-RAT cell selection to NR NTN

It is optional for a UE to support assistance information for inter-RAT cell selection to NR NTN as specified in TS 36.331 [5]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17.

# 7 Conditionally Mandatory features

## 7.1 Access control features

### 7.1.1 SSAC

It is mandatory to support Service Specific Access Control subject to common and per PLMN access barring parameters as specified in TS 36.331 [5], clause 5.3.3.10 for UEs which are IMS voice capable in LTE.

### 7.1.2 CSFB Access Barring Control

It is mandatory to support CSFB Access Barring Control subject to common and per PLMN access barring parameters as specified in TS 36.331 [5], clause 5.3.3.2 for UEs which are supporting CSFB to UTRA or GERAN.

### 7.1.3 Extended Access Barring

It is mandatory to support Extended Access Barring check as specified in TS 36.331 [5], clause 5.3.3.12 for UEs which are supporting an access subject to Extended Access Barring.

### 7.1.4 ACDC

It is mandatory to support barring check for ACDC subject to common and per PLMN barring parameters for ACDC as specified in TS 36.331 [5], clause 5.3.3.13 for UEs which are supporting an access subject to ACDC.

### 7.1.5 EAB per RSRP

It is mandatory to support eab-PerRSRP as specified in clause 5.3.3.12 of TS 36.331 [5] for BL UEs or UEs in coverage enhancement supporting Extended Access Barring.

## 7.2 Emergency call features

### 7.2.1 IMS emergency call

It is mandatory to support IMS emergency call for UEs which are IMS voice capable in LTE.

## 7.3 MAC features

### 7.3.1 SR mask

It is mandatory to support configuration indicated by logicalChannelSR-Mask for UE which have set bit number 29 of featureGroupIndicators to "1" as specified in TS 36.331 [5].

### 7.3.2 Power Management Indicator in PHR

Power management indicator in PHR is mandatory to support for UE applying additional power backoff due to power management (as allowed by P-MPRc, see TS 36.101 [6]).

## 7.4 Inter-RAT Mobility features

### 7.4.1 High Priority CSFB redirection

It is mandatory to support the RRCConnectionRelease indicating 'cs-FallbackHighPriority' for UEs which are supporting CSFB to UTRA as specified in TS 36.331 [5].

### 7.4.2 GERAN A/Gb mode to E-UTRAN Inter RAT handover (PS Handover)

It is mandatory to support at least parameter values corresponding to ue-Category 1 for UEs which are supporting GERAN A/Gb mode to E-UTRAN Inter RAT handover (PS Handover) as specified in TS 23.401 [18].

### 7.4.3 SRVCC to E-UTRAN from GERAN

It is mandatory to support at least parameter values corresponding to ue-Category 1, and ROHC profiles for an 'IMS capable UE supporting voice' as specified in clause 4.3.1.1, for UEs which are supporting SRVCC to E-UTRAN from GERAN as specified in TS 23.216 [19].

NOTE: Requirements on functionality covered by Feature Group Indicators are specified in TS 36.331 [5], clause B.1.

### 7.4.4 Inter-RAT configuration for less than 5 MHz in SystemInformationBlockType24

It is mandatory to support configuration of dl-CarrierFreq-r18 and multiBandInfoList-r18 as specified in TS 36.331 [5] for UEs supporting support5MHz-ChannelBW-20PRB-CORESET0-r18, support3MHz-ChannelBW-Symmetric-r18 or support3MHz-ChannelBW-Asymmetric-r18 as specified in TS 38.306 [32].

## 7.5 Delay Tolerant Access Features

### 7.5.1 extendedWaitTime

It is mandatory to support the RRCConnectionRelease with extendedWaitTime and RRCConnectionReject with extendedWaitTime for UEs which support Delay Tolerant Access as specified in TS 36.331 [5].

## 7.6 RRC Connection

### 7.6.1 Void

## 7.7 Physical layer features

### 7.7.1 Different UL/ DL configuration for TDD inter-band carrier aggregation

It is mandatory to support different UL/ DL configuration for UEs supporting inter-band TDD carrier aggregation band combinations and for UEs supporting inter-band TDD dual connectivity band combinations within cell group(s) including at least two TDD bands.

### 7.7.2 Full duplex for TDD and FDD carrier aggregation

UE of this version of the specification shall be able to support simultaneous reception and transmission on different bands for each band combination including at least one FDD band and at least one TDD band.

### 7.7.3 Simultaneous transmission of PUCCH and PUSCH across PUCCH groups

It is mandatory to support simultaneous transmission of PUCCH and PUSCH across PUCCH groups if the UE indicates support for pucch-SCell.

### 7.7.4 Simultaneous transmission of PUCCH in licensed spectrum and PUSCH in LAA SCells

It is mandatory to support simultaneous transmission of PUCCH in licensed spectrum and PUSCH in LAA SCells if the UE supports uplink LAA operation. If the UE supports dual connectivity, this is applicable within each cell group.

## 7.8 Positioning features

### 7.8.1 OTDOA Inter-frequency RSTD measurement indication

It is mandatory to support delivery of InterFreqRSTDMeasurementIndication as specified in TS 36.331 [5], clause 5.5.7 for UEs indicating support for inter-frequency RSTD measurements for OTDOA as specified in TS 36.355 [13] and requiring measurement gaps for performing these measurements.

### 7.8.2 Acquisition of positioning SI message with 80ms offset

It is mandatory to support acquisition of positioning SI messages with 80 milliseconds offset position compared to SI messages in schedulingInfoList for UEs which support the acquisition of the posSIB types in posSchedulingInfoList as specified in TS 36.331 [5].

## 7.9 Void

## 7.10 Other features

### 7.10.1 Logged MDT measurement suspension due to IDC interference

It is mandatory to support Logged MDT measurement suspension due to IDC interference for UEs which are supporting logged measurements in RRC_IDLE upon request from the network and in-device coexistence indication as well as autonomous denial functionality as specified in TS 36.331 [5].

### 7.10.2 Support of extended reporting of WLAN measurements

It is mandatory to support reporting of extended number of measurements of WLAN IDs for UEs which are supporting WLAN measurements as specified in TS 36.331 [5].

### 7.10.3 wlan-ReportAnyWLAN-r14

Indicates whether UE supports reporting of measurements of unknown WLAN as specified in TS 36.331 [5]. It is mandatory to support reporting of measurements of unknown WLAN ID for UEs which are supporting WLAN measurements as specified in TS 36.331 [5].

### 7.10.4 wlan-PeriodicMeas-r14

This parameter indicates whether the UE supports periodic reporting of WLAN measurements. It is mandatory to support periodic reporting of WLAN measurements for UEs which are supporting WLAN measurements as specified in TS 36.331 [5].

### 7.10.5 TA Reporting during Initial Access for NTN

It is mandatory to support TA report during initial access for UEs which support ntn-TA-Report-r17 as specified in TS 36.321 [4].

### 7.10.6 IoT NTN TDD mode

It is mandatory to support IoT NTN TDD mode for UEs which indicate support of band 249, see TS 36.102 [43]. This feature is only applicable if the UE supports ntn-Connectivity-EPC-r17 and any ue-Category-NB. For the UE supporting IoT NTN TDD mode, the UE shall support the following components:

- IoT NTN TDD Frame Structure as defined in TS 36.211 [17];

- DL subframes of pattern fixed to subframes [3 4 5 6 7 8 9 0] across two consecutive radio frames;

- non-U NB-IoT subframes not being considered by the UE as "NB-IoT UL subframes";

- non-D NB-IoT subframes not being considered by the UE as "NB-IoT DL subframes";

- NPSS/NSSS/NPBCH/SIB1-NB transmissions dropped in non-D NB-IoT subframes;

- postponement of NPRACH, PUR and UL SPS transmissions in non-U NB-IoT subframes until the next U NB-IoT subframe(s);

- postponement of SI-message reception in non-D NB-IoT subframes to the next D NB-IoT subframe(s);

- NPRACH periodicities of 90ms and 180ms;

- extended k-Mac (k-Mac-r19).

## 7.11 E-UTRA/5GC Parameters

### 7.11.1 Downlink SDAP header

It is mandatory to support downlink SDAP header for UEs which are either NAS reflective QoS or AS reflective QoS (i.e., reflectiveQoS-r15) capable in LTE.

###### Annex A (informative):
Guideline on maximum number of DL PDCP SDUs per TTI

In order to help the dimensioning of the UE design, values for the maximum number of DL PDCP SDUs per TTI from Table A-1 may be used. The values are applicable for a TTI length of 1 ms. For other TTI lengths, the table refers to maximum number of DL PDCP SDUs within a 1ms period.

NOTE: Due to the need for the network buffer data for efficient scheduling, values for Category 1, 1bis and 2 are same. It is not expected that category 1 or category 1bis UE has to sustain the same rate of PDCP SDUs per TTI as category 2 for prolonged period of time.

Table A-1: Maximum values for DL PDCP SDUs per TTI

| UE Category / ue-CategoryDL | Maximum number of PDCP SDUs per TTI |
| --- | --- |
| Category 1 | 10 |
| Category 1bis | 10 |
| Category 2 | 10 |
| Category 3 | 20 |
| Category 4 /DL Category 4 | 30 |
| Category 5 | 50 |
| Category 6 /DL Category 6 | 50 |
| Category 7 /DL Category 7 | 50 |
| Category 9 /DL Category 9 | 80 |
| Category 10 /DL Category 10 | 80 |
| Category 11 /DL Category 11 | 100 |
| Category 12 /DL Category 12 | 100 |
| DL Category 13 | 65 |
| DL Category 15 | 130 |
| DL Category 16 | 180 |
| DL Category 18 | 200 |
| DL Category 19 | 280 |
| DL Category 20 | 360 |
| DL Category 21 | 240 |
| DL Category 22 | 430 |
| DL Category 23 | 480 |
| DL Category 24 | 510 |
| DL Category 25 | 560 |
| DL Category 26 | 600 |

###### Annex B (informative):
Change history

| Change history |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Date | TSG # | TSG Doc. | CR | Rev | Cat | Subject/Comment | New version |
| 11/2007 | RP-38 | RP-070916 |  |  |  | Presented for approval at TSG RAN-38 | 1.0.0 |
| 12/2007 |  | - |  |  |  | Approved at TSG RAN-38 and placed under change control | 8.0.0 |
| 03/2008 | RP-39 | RP-080194 | 0001 | 1 |  | CR to 36.306 with Update to E-UTRA UE capabilities | 8.1.0 |
| 05/2008 | RP-40 | RP-080409 | 0002 | 1 |  | Update to E-UTRA UE capabilities: CR 0002r1 to 36.306 with status after RAN2 #62 | 8.2.0 |
| 03/2009 | RP-43 | RP-090126 | 0007 | - |  | CR to remove the clauses on MBMS | 8.3.0 |
|  | RP-43 | RP-090126 | 0008 | - |  | Final values for L2 buffer sizes | 8.3.0 |
|  | RP-43 | RP-090126 | 0009 | - |  | Various Corrections | 8.3.0 |
|  | RP-43 | RP-090126 | 0010 | - |  | CR to update uplink transmit diversity (UE transmit antenna selection) | 8.3.0 |
|  | RP-43 | RP-090126 | 0011 | - |  | Downlink PDCP SDU limitation | 8.3.0 |
|  | RP-43 | RP-090126 | 0014 | - |  | Thoughts on UE capability for RoHC | 8.3.0 |
|  | RP-43 | RP-090126 | 0015 | 1 |  | Capturing USIMless UE to stage 3 | 8.3.0 |
| 06/2009 | RP-44 | RP-090511 | 0016 | 2 |  | Support of inter-RAT PS handover to GERAN Editor Note Removal | 8.4.0 |
|  | RP-44 | RP-090511 | 0017 | 1 |  | Clarification of Half Duplex in TDD | 8.4.0 |
|  | RP-44 | RP-090511 | 0018 | - |  | Correcting the maximum number of bits received during one TTI | 8.4.0 |
|  | RP-44 | RP-090511 | 0019 | - |  | Clarification of field names used in TS 36.331 | 8.4.0 |
|  | RP-44 | RP-090511 | 0021 | - |  | Clarification on disabling E-UTRA capabilities with a USIM | 8.4.0 |
| 09/2009 | RP-45 | RP-090906 | 0023 | - |  | Unit for "Total layer 2 buffer size" | 8.5.0 |
| 12/2009 | RP-46 | - | - |  |  | Upgrade to the Release 9 - no technical change | 9.0.0 |
| 03/2010 | RP-47 | RP-100308 | 0024 | 1 |  | CR to 36.306 on Optionality of Rel-9 UE features | 9.1.0 |
|  | RP-47 | RP-100308 | 0025 | - |  | Introduction of power-limited device indication in UE capability. | 9.1.0 |
|  | RP-47 | RP-100308 | 0026 | - |  | UE capability for enhanced 1xRTT CS fallback | 9.1.0 |
|  | RP-47 | RP-100285 | 0028 | 1 |  | Bounds to RoHC requirements for IMS capable UEs supporting voice | 9.1.0 |
|  | RP-47 | RP-100309 | 0029 | 1 |  | CR to 36.306 on Redirection enhancements to UTRAN | 9.1.0 |
|  | RP-47 | RP-100188 | 0030 | 1 |  | Redirection enhancements to GERAN | 9.1.0 |
| 06/2010 | RP-48 | RP-100556 | 0031 | 1 |  | Clarification regarding / alignment of REL-9 UE capabilities | 9.2.0 |
|  | RP-48 | RP-100531 | 0033 | - |  | Correction on the definition of ue-SpecificRefSigsSupported | 9.2.0 |
| 09/2010 | RP-49 | RP-100853 | 0035 | - |  | Clarification of MBMS UE capability | 9.3.0 |
| 12/2010 | RP-50 | RP-101268 | 0037 | - |  | Inclusion of new UE categories in Rel-10 | 10.0.0 |
| 03/2011 | RP-51 | RP-110290 | 0038 | - |  | Description of carrier aggregation and MIMO capabilities | 10.1.0 |
|  | RP-51 | RP-110290 | 0039 | - |  | L2 buffer sizes for Rel-10 categories | 10.1.0 |
|  | RP-51 | RP-110280 | 0041 | - |  | CR to 36.306 adding UE capability indicator for dual Rx/Tx e1xCSFB | 10.1.0 |
|  | RP-51 | RP-110288 | 0042 | 1 |  | UE UL&DL MIMO Capabilities | 10.1.0 |
|  | RP-51 | RP-110282 | 0043 | - |  | Counter proposal to R2-110795 on UE capabilities for MDT | 10.1.0 |
| 06/2011 | RP-52 | RP-110828 | 0048 | - |  | Clarification of optionality of UE features without capability | 10.2.0 |
|  | RP-52 | RP-110830 | 0051 | - |  | Options for CSFB to GSM | 10.2.0 |
|  | RP-52 | RP-110840 | 0056 | 1 |  | CR to 36.306 on UE capabilities for Rel-10 LTE features | 10.2.0 |
|  | RP-52 | RP-110701 | 0058 | 2 |  | CA and MIMO Capabilities in LTE Rel-10 | 10.2.0 |
|  | RP-52 | RP-110839 | 0062 | - |  | Introduction of UE capability for enhanced redirection to UTRA TDD | 10.2.0 |
|  | RP-52 | RP-110834 | 0063 | 2 |  | Clarification of "supportedMIMO-CapabilityDL" | 10.2.0 |
|  | RP-52 | RP-110627 | 0064 | - |  | Correction of "total number of soft channel bits" for category 6 and 7 | 10.2.0 |
| 09/2011 | RP-53 | RP-111291 | 0065 | - |  | The SON feature in optional features without UE radio access capability parameters | 10.3.0 |
|  | RP-53 | RP-111283 | 0067 | - |  | AdditionalSpectrumEmissions in CA | 10.3.0 |
|  | RP-53 | RP-111278 | 0069 | - |  | Correction to UE capability parameters for handover to CSG cell | 10.3.0 |
| 12/2011 | RP-54 | RP-111716 | 0070 | 1 |  | Corrections to enhancedDualLayerTDD | 10.4.0 |
|  | RP-54 | RP-111710 | 0072 | - |  | Optionality of SR Masking | 10.4.0 |
|  | RP-54 | RP-111709 | 0074 | 1 |  | Optionality of UE Rx-Tx time difference report | 10.4.0 |
|  | RP-54 | RP-111714 | 0077 | - |  | Correction to the number of soft channel bits | 10.4.0 |
| 03/2012 | RP-55 | RP-120321 | 0078 | - |  | Clarification on physical layer parameter values requirement | 10.5.0 |
|  | RP-55 | RP-120326 | 0080 | 1 |  | Clarification on number of PDCP SDUs for categories 6-7 UEs | 10.5.0 |
|  | RP-55 | RP-120326 | 0082 | - |  | UE processing requirement in the presence of MCH transmission | 10.5.0 |
| 06/2012 | RP-56 | RP-120813 | 0090 | - |  | Korean Public Alert System (KPAS) in relation to CMAS | 10.6.0 |
|  | RP-56 | RP-120813 | 0093 | 1 |  | EU-Alert in relation to CMAS | 11.0.0 |
| 09/2012 | RP-57 | RP-121359 | 0100 | - |  | Voice support Capabilities | 11.1.0 |
|  | RP-57 | RP-121375 | 0103 | - |  | Introducing MBMS enhancements | 11.1.0 |
|  | RP-57 | RP-121395 | 0105 | - |  | Clarification on spatial multiplexing requirement in supportedBandCombination | 11.1.0 |
| 12/2012 | RP-58 | RP-121936 | 0120 | - |  | Power Management Indicator in PHR | 11.2.0 |
|  | RP-58 | RP-121936 | 0124 | 1 |  | Clarification on UL CA in supportedBandCombination | 11.2.0 |
|  | RP-58 | RP-122002 | 0125 | 2 |  | Introduction of Rel-11 UE features | 11.2.0 |
|  | RP-58 | RP-121960 | 0132 | - |  | Broadcast of Time Info by Using a New SIB | 11.2.0 |
| 03/2013 | RP-59 | RP-130243 | 0133 | 2 |  | DL COMP capability related correction | 11.3.0 |
|  | RP-59 | RP-130233 | 0135 | - |  | MIMO capability related correction | 11.3.0 |
|  | RP-59 | RP-130241 | 0137 | - |  | Correction to supported DL MIMO capability for TM10 | 11.3.0 |
|  | RP-59 | RP-130240 | 0138 | - |  | Optional support of RLF report for inter-RAT MRO | 11.3.0 |
|  | RP-59 | RP-130248 | 0140 | 1 |  | Corrections to UE capabiliy naming and definition | 11.3.0 |
|  | RP-59 | RP-130233 | 0142 | - |  | Clarification on cross carrier scheduling capability | 11.3.0 |
|  | RP-59 | RP-130226 | 0146 | - |  | Introduction of PDSCH TM5 capabilities for FDD and TDD | 11.3.0 |
| 09/2013 | RP-61 | RP-131315 | 0151 | - |  | Remove TBD in max MCH TB size table | 11.4.0 |
|  | RP-61 | RP-131314 | 0157 | - |  | Clarification of InterFreqRSTDMeasurementIndication procedure support | 11.4.0 |
| 12/2013 | RP-62 | RP-131986 | 0160 | - |  | Introduction of capability bit for UTRA MFBI | 11.5.0 |
|  | RP-62 | RP-132003 | 0161 | 1 |  | Capturing mandatory/optional agreements on Rel-11 UE features | 11.5.0 |
|  | RP-62 | RP-131991 | 0163 | - |  | Clarification on eRedirection to UMTS TDD with multiple UMTS TDD frequencies | 11.5.0 |
|  | RP-62 | RP-131984 | 0165 | - |  | Addition of inter-frequency RSTD measurement capability indicator for OTDOA | 11.5.0 |
|  | RP-62 | RP-131789 | 0166 | 1 |  | MBMS reception on any configured or configurable SCell | 11.5.0 |
|  | RP-62 | RP-131993 | 0167 | - |  | Enabling SRVCC from GERAN without forwarding UE-EUTRA-Capability | 11.5.0 |
| 03/2014 | RP-63 | RP-140364 | 0168 | 1 |  | New UE categories for DL 450Mbps class | 11.6.0 |
|  | RP-63 | RP-140349 | 0170 | - |  | SS and common channel interference handling | 11.6.0 |
|  | RP-63 | RP-140354 | 0176 | 1 |  | IoT indication for inter-band TDD CA with different UL/DL configuration | 11.6.0 |
|  | RP-63 | RP-140353 | 0173 | 1 |  | Corrections to UE capability and feature descriptions | 12.0.0 |
| 06/2014 | RP-64 | RP-140887 | 0181 | - |  | Support of the enhancement for TTI bundling for FDD | 12.1.0 |
|  | RP-64 | RP-140888 | 0185 | 3 |  | Alternative 1: Introduction of FDD/TDD CA full duplex support to 36.306 | 12.1.0 |
|  | RP-64 | RP-140892 | 0190 | 1 |  | Extended RLC LI field | 12.1.0 |
|  | RP-64 | RP-140873 | 0194 | 1 |  | Network-requested CA Band Combination Capability Signalling | 12.1.0 |
|  | RP-64 | RP-140892 | 0196 | 1 |  | Introduction of RRC Connection Establishment failure temporary Qoffset handling | 12.1.0 |
|  | RP-64 | RP-141028 | 0198 | 3 |  | eMBMS reception on SCell and Non-Serving Cell | 12.1.0 |
| 09/2014 | RP-65 | RP-141498 | 0218 | 1 |  | The PDCP SDU number limitation for Category 9-10 UE | 12.2.0 |
|  | RP-65 | RP-141505 | 0215 | - |  | UE capabilities for Hetnet mobility in TS 36.306 | 12.2.0 |
|  | RP-65 | RP-141499 | 0212 | - |  | Introduction of UE eIMTA capabilities | 12.2.0 |
|  | RP-65 | RP-141493 | 0205 | - |  | Corrections to UE capabilities and features | 12.2.0 |
|  | RP-65 | RP-141507 | 0209 | - |  | Introduction of MBSFN MDT capability | 12.2.0 |
|  | RP-65 | RP-141506 | 0207 | 2 |  | Introduction of Category 0 for low complexity UEs | 12.2.0 |
| 12.2014 | RP-66 | RP-142129 | 0225 | - |  | Clarification on DL parallel reception of category 0 UEs | 12.3.0 |
|  | RP-66 | RP-142125 | 0228 | - |  | Optional features for Hetnet mobility in TS 36.306 | 12.3.0 |
|  | RP-66 | RP-142123 | 0230 | - |  | Corrections to eIMTA capabilities | 12.3.0 |
|  | RP-66 | RP-142140 | 0243 | - |  | Introduction of extended RSRQ value range and new RSRQ definition | 12.3.0 |
|  | RP-66 | RP-142132 | 0232 | - |  | Support of Discovery Signals in TS 36.306 | 12.3.0 |
|  | RP-66 | RP-142140 | 0247 | - |  | Prohibit timer for SR | 12.3.0 |
|  | RP-66 | RP-142128 | 0241 | 1 |  | UE capability for IncMon | 12.3.0 |
|  | RP-66 | RP-142115 | 0227 | 1 |  | Introduction of capability for serving cell interruptions | 12.3.0 |
|  | RP-66 | RP-142134 | 0239 | - |  | Introduction of missing Rel-12 UE capabilities | 12.3.0 |
|  | RP-66 | RP-142130 | 0245 | 1 |  | Optionality support of UE mandatory features for Category 0 UEs | 12.3.0 |
|  | RP-66 | RP-142135 | 0238 | 1 |  | Introduction of Dual Connectivity | 12.3.0 |
|  | RP-66 | RP-142139 | 0237 | 2 |  | NAICS Capability | 12.3.0 |
|  | RP-66 | RP-142124 | 0229 | 2 |  | Mandatory support of TTI bundling without resource allocation restriction for LTE coverage enhancements for Rel-12 | 12.3.0 |
|  | RP-66 | RP-141981 | 0248 | - |  | UE capability signaling for WLAN/3GPP radio interworking | 12.3.0 |
|  | RP-66 | RP-142232 | 0233 | 2 |  | Support of 256QAM in TS 36.306 | 12.3.0 |
| 03/2015 | RP-67 | RP-150378 | 0265 | - |  | UE capability for modified MPR behavior | 12.4.0 |
|  | RP-67 | RP-150373 | 0257 | - |  | Correction to UE capabilities for Low Complexity UEs | 12.4.0 |
|  | RP-67 | RP-150373 | 0259 | - |  | Clarification of TDD DC capability | 12.4.0 |
|  | RP-67 | RP-150373 | 0258 | - |  | Extended number of measurement identities capability | 12.4.0 |
|  | RP-67 | RP-150373 | 0253 | - |  | Introduction of total L2 buffer sizes for UEs supporting split bearersNOTE: Modifications on L2 buffer sizes with support for split bearers for Cat 13-15 in Table 4.1-3 were moved to Table 4.1A-3 due to the clash with CR0261R1. | 12.4.0 |
|  | RP-67 | RP-150374 | 0267 | - |  | Introduction of ProSe | 12.4.0 |
|  | RP-67 | RP-150376 | 0266 | 1 |  | Change related to configuration of the priority for frequency bands in mFBI | 12.4.0 |
|  | RP-67 | RP-150379 | 0261 | 1 |  | Introduction of UL64QAM based on split of DL and UL categories | 12.4.0 |
| 06/2015 | RP-68 | RP-150921 | 0269 | - |  | Dual Connectivity L2 buffer size for category combinations with UL64QAM | 12.5.0 |
|  | RP-68 | RP-150917 | 0272 | 1 |  | Corrections on MIMO capabilities | 12.5.0 |
|  | RP-68 | RP-150923 | 0277 | - |  | Clarification on UL 64QAM capability | 12.5.0 |
|  | RP-68 | RP-150917 | 0276 | - |  | UE support of CA fallback configurations | 12.5.0 |
|  | RP-68 | RP-150921 | 0283 | 1 |  | Corrections on requirements of sidelink reception in TS 36.306 | 12.5.0 |
|  | RP-68 | RP-150951 | 0280 | 1 |  | Introduction of new DL UE categories 15&16 | 12.5.0 |
| 09/2015 | RP-69 | RP-151438 | 0287 | - |  | Remove support of additionalSpectrumEmissionPCell | 12.6.0 |
|  | RP-69 | RP-151442 | 0288 | - |  | Capturing PCell support for FDD-TDD CA | 12.6.0 |
|  | RP-69 | RP-151442 | 0292 | - |  | Clarification of the maximum number of bits of a single DL-SCH transport block for DL Category 16 | 12.6.0 |
|  | RP-69 | RP-151442 | 0293 | - |  | Capturing mandatory/optional features of Rel-12 UEs | 12.6.0 |
|  | RP-69 | RP-151439 | 0298 | - |  | CR for IDC signalling enhancement for UL CA | 12.6.0 |
|  | RP-69 | RP-151441 | 0289 | 1 |  | Corrections on UE sidelink capabilities in TS 36.306 | 12.6.0 |
|  | RP-69 | RP-151467 | 0290 | 2 |  | Additional MIMO/CSI capability for intra-band contiguous CA | 12.6.0 |
|  | RP-69 | RP-151597 | 0296 | 3 |  | Capability for 4-layer MIMO with TM3 and TM4 | 12.6.0 |
| 12/2015 | RP-70 | RP-152053 | 0309 | - |  | Definitions of sidelink terminologies in TS 36.306 | 12.7.0 |
|  | RP-70 | RP-152055 | 0310 | - |  | Correction on categories in supportedBandCombination | 12.7.0 |
|  | RP-70 | RP-152048 | 0303 | 1 |  | Clarification on support of extended wait time | 12.7.0 |
|  | RP-70 | RP-152053 | 0312 | 1 |  | Clarification on tdd-FDD-CA-PCellDuplex | 12.7.0 |
|  | RP-70 | RP-152049 | 0299 | 2 |  | Alternative new maximum transport block sizes for DL 64QAM and 256QAM in TM9/10 | 12.7.0 |
|  | RP-70 | RP-152048 | 0318 | - |  | Enabling multiple NS and P-Max operation per cell | 12.7.0 |
|  | RP-70 | RP-152055 | 0315 | 1 |  | Correction on capability rsrq-OnAllSymbols | 12.7.0 |
|  | RP-70 | RP-152053 | 0313 | 1 |  | Clarification on Pcell support | 12.7.0 |
| 12/2015 | RP-70 | RP-152074 | 0301 | 1 |  | Introduction of DC enhancement | 13.0.0 |
|  | RP-70 | RP-152078 | 0319 | - |  | Introduction of Licensed-Assisted Access using LTE | 13.0.0 |
|  | RP-70 | RP-152075 | 0308 | 1 |  | Introduction of RS-SINR measurements | 13.0.0 |
|  | RP-70 | RP-152080 | 0304 | 1 |  | Introduction of SC-PTM | 13.0.0 |
|  | RP-70 | RP-152066 | 0314 | - |  | Introduction of Application specific Congestion control for Data Communication in LTE | 13.0.0 |
|  | RP-70 | RP-152084 | 0311 | 1 |  | White-list of cells for EUTRA measurement reporting | 13.0.0 |
|  | RP-70 | RP-152071 | 0305 | 2 |  | Introduction of CA enhancement | 13.0.0 |
|  | RP-70 | RP-152076 | 0322 | - |  | Introducing extended DRX | 13.0.0 |
| 03/2016 | RP-71 | RP-160470 | 0323 | 1 |  | Capture the UE capability for the extension of the MeasObjectId to 64 | 13.1.0 |
|  | RP-71 | RP-160470 | 0330 | - |  | Miscellaneous corrections to TS 36.306 | 13.1.0 |
|  | RP-71 | RP-160460 | 0333 | 1 |  | MDT enhancements support | 13.1.0 |
|  | RP-71 | RP-160460 | 0334 | 1 |  | The introduction of UE capability concerning extended E-UTRA frequency priorities | 13.1.0 |
|  | RP-71 | RP-160459 | 0335 | 3 |  | Introduction of LWIP UE capabilities | 13.1.0 |
|  | RP-71 | RP-160457 | 0337 | 2 |  | Introducing LWA and RCLWI UE capabilities | 13.1.0 |
|  | RP-71 | RP-160460 | 0338 | 1 |  | Leftover UE capabilities for LAA | 13.1.0 |
|  | RP-71 | RP-160470 | 0339 | 1 |  | Minor corrections for CA enhancements | 13.1.0 |
|  | RP-71 | RP-160462 | 0341 | 1 |  | Reference errors for inter-RAT capabilities | 13.1.0 |
|  | RP-71 | RP-160453 | 0342 | 1 |  | UE capabilities for LC and CE | 13.1.0 |
|  | RP-71 | RP-160454 | 0343 | 2 |  | Introduction of eD2D Capability | 13.1.0 |
|  | RP-71 | RP-160464 | 0344 | 2 |  | Modification of network requested CA band combination retrieval for intra-band non-contiguous CA | 13.1.0 |
|  | RP-71 | RP-160467 | 0346 | 1 |  | Correction on capability phy-TDD-ReConfig-FDD(TDD)-Pcell | 13.1.0 |
|  | RP-71 | RP-160470 | 0347 | 1 |  | ANR in case of MFBI | 13.1.0 |
|  | RP-71 | RP-160455 | 0348 | - |  | 36.306 CR on TM10 CRS-IM UE capability report signalling introduction | 13.1.0 |
|  | RP-71 | RP-160470 | 0349 | - |  | Introduction of capability on PDSCH collision handling | 13.1.0 |
|  | RP-71 | RP-160470 | 0350 | 1 |  | Corrections on SC-PTM | 13.1.0 |
|  | RP-71 | RP-160470 | 0351 | - |  | SC-PTM reception on non-Pcell | 13.1.0 |
|  | RP-71 | RP-160460 | 0352 | 1 |  | Additional Layer 1 capabilities for Rel-13 CA enhancements | 13.1.0 |
| 06/2016 | RP-72 | RP-161080 | 1321 | - |  | Correction to WLAN measurement support for LWIP | 13.2.0 |
|  | RP-72 | RP-161080 | 1322 | - |  | Introducing EBF/FD-MIMO capabilities | 13.2.0 |
|  | RP-72 | RP-161080 | 1315 | - |  | Clarifications on LWA capability | 13.2.0 |
|  | RP-72 | RP-161080 | 1326 | - |  | MBMS reception via MBSFN or SC-PTM | 13.2.0 |
|  | RP-72 | RP-161080 | 1329 | - |  | Corrections on capability linking for measurement object extension | 13.2.0 |
|  | RP-72 | RP-161080 | 1327 | 2 |  | Capturing a new capability signalling format for Rel-13 CA enhancements | 13.2.0 |
|  | RP-72 | RP-161080 | 1330 | - |  | Correction on the value of maxmum channel bandwidth | 13.2.0 |
|  | RP-72 | RP-161080 | 1334 | 2 |  | UE capabilities for eMTC | 13.2.0 |
|  | RP-72 | RP-161080 | 1333 | 1 |  | UE Power Class in UE capability signaling | 13.2.0 |
|  | RP-72 | RP-161080 | 1314 | 2 |  | Miscellaneous corrections to TS 36.306 | 13.2.0 |
|  | RP-72 | RP-161080 | 1323 | 1 |  | Clarification on eD2D capability | 13.2.0 |
|  | RP-72 | RP-161076 | 1317 | - |  | Clarification on maximum number of DL-SCH transport block bits for DL Category 15 and 16 | 13.2.0 |
|  | RP-72 | RP-161076 | 1318 | - |  | UE capability of an additional Rx and Tx requirement for a CA band combination | 13.2.0 |
|  | RP-72 | RP-161081 | 1328 | 2 |  | Introduction of NB-IoT UE capabilities | 13.2.0 |
|  | RP-72 | RP-161076 | 1320 | 2 |  | Definition of a fallback band combination | 13.2.0 |
| 09/2016 | RP-73 | RP-161761 | 1338 | 1 |  | Support of CAT 9/10 and CAT 13 | 13.3.0 |
|  | RP-73 | RP-161760 | 1346 | 2 |  | Introduction of 1.2Gbps and 1.6Gbps UE categories in Rel-13 | 13.3.0 |
|  | RP-73 | RP-161826 | 1347 | 2 |  | Continuous uplink transmission in eMTC | 13.3.0 |
|  | RP-73 | RP-161751 | 1350 | 1 |  | Indication of the maxLayersMIMO | 13.3.0 |
|  | RP-73 | RP-161759 | 1352 | 1 |  | Supporting new UE Rx – Tx time difference mapping table | 13.3.0 |
|  | RP-73 | RP-161761 | 1353 | - |  | Introducing UE capability of Rel 13 CCH IM | 13.3.0 |
|  | RP-73 | RP-161761 | 1354 | - |  | Introducing UE capability of CRS-IM for TM 1-9 | 13.3.0 |
| 09/2016 | RP-73 | RP-161745 | 1348 | - |  | Introduction of enhanced LAA for LTE | 14.0.0 |
| 12/2016 | RP-74 | RP-162327 | 1361 | 1 |  | Capability for LWIP aggregation | 14.1.0 |
|  | RP-74 | RP-162327 | 1364 | 1 |  | Miscellaneous corrections to TS 36.306 | 14.1.0 |
|  | RP-74 | RP-162318 | 1367 | - |  | Clarification on UE power class 2 indication | 14.1.0 |
|  | RP-74 | RP-162317 | 1369 | 1 |  | Correction on simultaneous transmission of PUCCH and PUSCH for B5C | 14.1.0 |
|  | RP-74 | RP-162321 | 1370 | 1 |  | Correction on simultaneous transmission of PUCCH and PUSCH for eLAA | 14.1.0 |
|  | RP-74 | RP-162327 | 1371 | - |  | Extension of PollByte | 14.1.0 |
|  | RP-74 | RP-162317 | 1373 | - |  | Definition of cch-InterfMitigation-MaxNumCCs | 14.1.0 |
|  | RP-74 | RP-162310 | 1377 | - |  | Clarification on UE category requirement | 14.1.0 |
|  | RP-74 | RP-162329 | 1383 | 1 |  | UE capabilities for Latency Reduction | 14.1.0 |
|  | RP-74 | RP-162314 | 1393 | - |  | Correction on channel bandwidth definition for NB-IoT | 14.1.0 |
|  | RP-74 | RP-162321 | 1397 | - |  | Introduction of capabilities for eLAA | 14.1.0 |
|  | RP-74 | RP-162555 | 1399 | 1 |  | Introduction of new UL UE category 15 for 225Mbps | 14.1.0 |
| 03/2017 | RP-75 | RP-170630 | 1382 | 2 | B | Introduction of mobility enhancement UE capabilities | 14.2.0 |
|  | RP-75 | RP-170639 | 1402 | 1 | A | Introduction of 1Rx UE category | 14.2.0 |
|  | RP-75 | RP-170628 | 1403 | 1 | B | Capability for extended reporting of WLAN measurements | 14.2.0 |
|  | RP-75 | RP-170668 | 1404 | - | B | Introduction of a new special subframe configuration | 14.2.0 |
|  | RP-75 | RP-170637 | 1406 | 2 | B | Introduction of UE capabilities for NB-IoT enhancements | 14.2.0 |
|  | RP-75 | RP-170636 | 1407 | 2 | B | Introduction of UE capabilities for feMTC enhancements | 14.2.0 |
|  | RP-75 | RP-170657 | 1410 | - | A | Support of multiple DRBs for S1-U data transfer | 14.2.0 |
|  | RP-75 | RP-170642 | 1416 | 1 | B | Introduction of data inactivity timer | 14.2.0 |
|  | RP-75 | RP-170652 | 1419 | 1 | A | IOT indication for unicast MPDCCH/PDSCH/PUSCH frequency hopping | 14.2.0 |
|  | RP-75 | RP-170638 | 1423 | 1 | B | Introduction of Voice and Video enhancements for LTE | 14.2.0 |
|  | RP-75 | RP-170646 | 1424 | 1 | B | Introduction of SRS switching capability | 14.2.0 |
|  | RP-75 | RP-170628 | 1425 | 1 | B | Introduction of Enhanced LTE-WLAN Aggregation (eLWA) | 14.2.0 |
|  | RP-75 | RP-170632 | 1426 | 2 | B | Introduction of new UL UE categories for UL 256QAM support | 14.2.0 |
|  | RP-75 | RP-170634 | 1429 | 2 | B | CR for introduction of measurement gap enhancement | 14.2.0 |
|  | RP-75 | RP-170642 | 1430 | 1 | C | Functional modification of retrieving different UE capabilities for a fallback band combination | 14.2.0 |
|  | RP-75 | RP-170636 | 1431 | - | B | FeMTC UE CE mode and maximum PDSCH/PUSCH BW preference indication | 14.2.0 |
|  | RP-75 | RP-170806 | 1434 | 1 | A | Feature optionality for Cat.1bis UE | 14.2.0 |
| 06/2017 | RP-76 | RP-171231 | 1437 | 1 | F | Correction on UE capabilities for eLAA | 14.3.0 |
|  | RP-76 | RP-171225 | 1438 | 2 | B | Introduction of new Transport Block Size for DL 256QAM | 14.3.0 |
|  | RP-76 | RP-171236 | 1439 | 4 | F | UE capabilities for eLWA | 14.3.0 |
|  | RP-76 | RP-171248 | 1442 | 2 | A | Entry-Level UE Support UL 64QAM | 14.3.0 |
|  | RP-76 | RP-171224 | 1443 | 2 | F | Miscellaneous corrections to TS 36.306 | 14.3.0 |
|  | RP-76 | RP-171222 | 1445 | 1 | F | CR for introduction of non-uniform gap in measurement gap enhancement | 14.3.0 |
|  | RP-76 | RP-171247 | 1446 | 1 | B | Introduction of a new UL UE category for 300Mbps with 64QAM | 14.3.0 |
|  | RP-76 | RP-171223 | 1448 | 2 | F | Corrections to capabilities for feMTC | 14.3.0 |
|  | RP-76 | RP-171223 | 1452 | 1 | C | CE mode configuration/deconfiguration without handover | 14.3.0 |
|  | RP-76 | RP-171241 | 1458 | 1 | A | Optional feature without UE capability bit for VoLTE | 14.3.0 |
|  | RP-76 | RP-171243 | 1461 | 2 | A | LAA/WiFi sharing indication | 14.3.0 |
|  | RP-76 | RP-171225 | 1462 | 1 | F | Update of ROHC profile referenc | 14.3.0 |
|  | RP-76 | RP-171225 | 1463 | - | B | UE Capabilitites to enable Uplink-Only RoHC operations | 14.3.0 |
|  | RP-76 | RP-171224 | 1464 | - | F | Corrections to capabilities for NB-IoT | 14.3.0 |
|  | RP-76 | RP-171234 | 1465 | - | F | UL 256QAM capability clarification | 14.3.0 |
|  | RP-76 | RP-171221 | 1470 | - | B | Introduction of FeMBMS to 36.306 | 14.3.0 |
|  | RP-76 | RP-171223 | 1475 | - | F | Correction on the description of ce-srsEnhancement for FeMTC | 14.3.0 |
|  | RP-76 | RP-171223 | 1476 | - | F | Minor correction on TS 36.306 for FeMTC | 14.3.0 |
|  | RP-76 | RP-171407 | 1478 | 2 | B | Introduction of UE capability for V2X in 36.306 | 14.3.0 |
|  | RP-76 | RP-171223 | 1479 | 2 | B | Introduction of enhanced RLM measurement capabilities | 14.3.0 |
|  | RP-76 | RP-171229 | 1480 | - | B | Introduction of UE capabilities for high speed | 14.3.0 |
|  | RP-76 | RP-171223 | 1483 | - | F | Correction to ceMeasurements-r14 measurement capability | 14.3.0 |
|  | RP-76 | RP-171224 | 1484 | - | B | Introduction of RRC connection re-establishment for NB-IoT control plane | 14.3.0 |
| 09/2017 | RP-77 | RP-171919 | 1486 | - | A | RoHC profile support for CIoT-only NB-IoT UE | 14.4.0 |
|  | RP-77 | RP-171914 | 1494 | 1 | F | Correction on UE category combination | 14.4.0 |
|  | RP-77 | RP-171918 | 1498 | 2 | A | Clarification on MBMS reception with 256QAM | 14.4.0 |
|  | RP-77 | RP-171913 | 1499 | - | F | Cat-M1 indication by Cat-M2 UE | 14.4.0 |
|  | RP-77 | RP-171913 | 1500 | - | F | Corrections on TS 36.306 for Rel-14 MTC | 14.4.0 |
|  | RP-77 | RP-171914 | 1501 | 2 | F | Clarification on NCSG UE capability | 14.4.0 |
|  | RP-77 | RP-171915 | 1502 | - | C | UE Capabilty for support of RLC UM for LWA bearer | 14.4.0 |
|  | RP-77 | RP-171913 | 1504 | 2 | C | Introduction of Release Assistance Indication | 14.4.0 |
|  | RP-77 | RP-171920 | 1506 | 2 | A | TM9 capabilities in CE mode | 14.4.0 |
|  | RP-77 | RP-171915 | 1507 | 1 | F | Introduction of interference randomisation in NB-IoT | 14.4.0 |
| 12/2017 | RP-78 | RP-172615 | 1490 | 5 | B | Introduction of the temporary UE capability for overheating indication | 14.5.0 |
|  | RP-78 | RP-172721 | 1508 | 2 | B | Introduction of DL 2Gbps Category | 14.5.0 |
|  | RP-78 | RP-172622 | 1511 | 2 | A | UE capabilities for Tx antenna selection | 14.5.0 |
|  | RP-78 | RP-172616 | 1514 | - | F | UE capability for support of SRS enhancements without support of comb 4 | 14.5.0 |
|  | RP-78 | RP-172616 | 1518 | 1 | B | Introduction of Enhanced CRS and SU-MIMO Interference Mitigation Performance Requirements for LTE | 14.5.0 |
|  | RP-78 | RP-172617 | 1523 | 2 | C | Introduction of relaxed monitoring in NB-IoT | 14.5.0 |
|  | RP-78 | RP-172624 | 1528 | 1 | A | TM6 capabilities in CE mode | 14.5.0 |
|  | RP-78 | RP-172616 | 1533 | - | F | MUST capability | 14.5.0 |
|  | RP-78 | RP-172617 | 1534 | 1 | F | Correction to random access power control in 36.306 | 14.5.0 |
|  | RP-78 | RP-172616 | 1536 | 1 | B | Introduction of a new UE capability for ssp10 with less CRS | 14.5.0 |
| 03/2018 | RP-79 | RP-180443 | 1545 | - | F | Correction to description for HARQ-ACK delay for Rel-14 MTC | 14.6.0 |
|  | RP-79 | RP-180443 | 1552 | 1 | C | Introduction of support of relaxed monitoring for BL and CE UE | 14.6.0 |
|  | RP-79 | RP-180448 | 1555 | 2 | B | Introduction of LTE DL 1.4Gbps Category | 14.6.0 |
|  | RP-79 | RP-180446 | 1561 | 1 | F | Capability for for reading shared PLMN information from non-CSG cells | 14.6.0 |
|  | RP-79 | RP-180446 | 1564 | 1 | F | Supported bandwidths in Fallback band combination | 14.6.0 |
|  | RP-79 | RP-180494 | 1566 | 2 | F | Correction on SRS carrier switching | 14.6.0 |
| 03/2018 | RP-79 | RP-180440 | 1559 | 2 | B | Introduction of EN-DC capabilities | 15.0.0 |
| 07/2018 | RP-80 | RP-181222 | 1519 | 1 | B | Introduction of QoE Measurement Collection for LTE | 15.1.0 |
|  | RP-80 | RP-181221 | 1535 | 3 | B | Running 36.306 CR to introduce assistance information for local cache | 15.1.0 |
|  | RP-80 | RP-181218 | 1542 | 3 | B | Introduction of shortened TTI and processing time for LTE | 15.1.0 |
|  | RP-80 | RP-181226 | 1543 | 3 | B | Introduction of DEFLATE based UDC Solution | 15.1.0 |
|  | RP-80 | RP-181228 | 1546 | 3 | B | Enhancement of SRS antenna switching in TS 36.306 | 15.1.0 |
|  | RP-80 | RP-181220 | 1547 | 3 | B | Support of 1024QAM in TS 36.306 | 15.1.0 |
|  | RP-80 | RP-181234 | 1569 | 3 | A | Addition of the number of SL processes for V2X sidelink communication | 15.1.0 |
|  | RP-80 | RP-181171 | 1570 | 2 | C | Introduction of support for MAC PDU containing UE contention resolution identity MAC control element without RRC response message in NB-IoT | 15.1.0 |
|  | RP-80 | RP-181232 | 1575 | 2 | A | Correction on reducedIntNonContComb-r13 description | 15.1.0 |
|  | RP-80 | RP-181232 | 1578 | 3 | A | Different power class support for band combinations | 15.1.0 |
|  | RP-80 | RP-181252 | 1581 | 3 | B | Introduction of further NB-IoT enhancements in 36.306 | 15.1.0 |
|  | RP-80 | RP-181227 | 1584 | 1 | B | Running 36.306 CR to introduce BT and WLAN in MDT | 15.1.0 |
|  | RP-80 | RP-181224 | 1591 | 3 | B | Introduction of even further eMTC enhancmenets for eMTC | 15.1.0 |
|  | RP-80 | RP-181250 | 1592 | 2 | B | UE capability definitions for euCA | 15.1.0 |
|  | RP-80 | RP-181225 | 1599 | - | B | Implementing network-based CRS interference mitigation | 15.1.0 |
|  | RP-80 | RP-181233 | 1602 | - | A | UE capability for handling of multiple numerologies in FeMBMS | 15.1.0 |
|  | RP-80 | RP-181233 | 1604 | 1 | A | Additional UE capabilities for SRS carrier switching | 15.1.0 |
|  | RP-80 | RP-181232 | 1606 | - | A | Additional UE capabilities for advanced CSI in FD-MIMO | 15.1.0 |
|  | RP-80 | RP-181223 | 1608 | 2 | B | Introduce reportCGI towards NR neighbour cell | 15.1.0 |
|  | RP-80 | RP-181236 | 1611 | 1 | A | Introduction of DL Channel Quality reporting | 15.1.0 |
|  | RP-80 | RP-181235 | 1612 | 1 | A | Introduction of serving cell idle mode measurements reporting in 36.306 | 15.1.0 |
|  | RP-80 | RP-181254 | 1613 | 1 | B | Introduction of increased number of E-UTRAN data bearers | 15.1.0 |
|  | RP-80 | RP-181228 | 1614 | 2 | B | Control Plane latency reduction | 15.1.0 |
|  | RP-80 | RP-181247 | 1616 | 2 | B | Introduction of time reference provision | 15.1.0 |
|  | RP-80 | RP-181249 | 1618 | - | B | Introduce feLAA in TS 36.306 | 15.1.0 |
|  | RP-80 | RP-181247 | 1619 | - | B | Introduction of Ultra Reliable Low Latency Communication for LTE | 15.1.0 |
| 09/2018 | RP-81 | RP-181960 | 1593 | 2 | B | Advanced CSI CBSR CBSR related capability for FD-MIMO | 15.2.0 |
|  | RP-81 | RP-181960 | 1596 | 1 | B | Avoiding FGI20 limitation | 15.2.0 |
|  | RP-81 | RP-181960 | 1600 | 1 | B | Introduction of QoE Measurement Collection for MTSI services | 15.2.0 |
|  | RP-81 | RP-181948 | 1620 | 1 | B | Introduction of UE capability for eV2X in TS 36.306 | 15.2.0 |
|  | RP-81 | RP-181940 | 1621 | 1 | F | Cell reselection priorities for NR frequency | 15.2.0 |
|  | RP-81 | RP-181963 | 1623 | - | A | Add missing NB-IoT capabilities in clause 4 | 15.2.0 |
|  | RP-81 | RP-181945 | 1624 | 1 | F | Introducing FDD-TDD differentiation in NB-IoT in 36.306 | 15.2.0 |
|  | RP-81 | RP-181960 | 1627 | - | B | Introduction of modulation enhancements | 15.2.0 |
|  | RP-81 | RP-181947 | 1628 | 2 | B | UE categories for 1024QAM | 15.2.0 |
|  | RP-81 | RP-181949 | 1633 | 1 | F | UE capability related with SPS | 15.2.0 |
|  | RP-81 | RP-181956 | 1635 | 2 | B | Introduction of capabilities for Rel-15 Aerial WI | 15.2.0 |
|  | RP-81 | RP-181945 | 1636 | 1 | F | Make additional SIB transmission an optional feature with capability reporting | 15.2.0 |
|  | RP-81 | RP-181960 | 1637 | 1 | C | Introduction of Geofencing information in CMAS | 15.2.0 |
|  | RP-81 | RP-181964 | 1643 | - | B | Introduction of further enhancements to CoMP | 15.2.0 |
|  | RP-81 | RP-181949 | 1644 | 1 | C | UE capabilities for short TTI | 15.2.0 |
|  | RP-81 | RP-181949 | 1645 | 2 | C | UE capabilities for Ultra Reliable Low Latency Communication | 15.2.0 |
| 12/2018 | RP-82 | RP-182671 | 1625 | 2 | F | Removal of duplicate rel-15 NB-IoT/eMTC capabilities and introducing TDD-FDD differentiation for WUS capabilities in eMTC | 15.3.0 |
|  | RP-82 | RP-182671 | 1632 | 3 | F | Missing UE capability introduction for efeMTC | 15.3.0 |
|  | RP-82 | RP-182678 | 1646 | 3 | F | Correction on UE capability for eV2X | 15.3.0 |
|  | RP-82 | RP-182679 | 1647 | 2 | F | Correction on SPS configuration for HRLLC | 15.3.0 |
|  | RP-82 | RP-182681 | 1648 | 2 | F | Adding NSSS-based RRM measurements, NPBCH-Based RRM measurements and npusch-3dot75kHz-SCS-TDD-r15 and removing twoHARQ-ProcessesTDD | 15.3.0 |
|  | RP-82 | RP-182677 | 1651 | 1 | A | Clarification to CA fallback band combinations | 15.3.0 |
|  | RP-82 | RP-182652 | 1652 | 1 | F | UE capabilty for IDC mechanism for EN-DC operation | 15.3.0 |
|  | RP-82 | RP-182674 | 1654 | 1 | F | Remaining aspects of capabilities for Rel-15 Aerial WI | 15.3.0 |
|  | RP-82 | RP-182678 | 1656 | 2 | F | Correction of UE capability for eV2X in TS 36.306 | 15.3.0 |
|  | RP-82 | RP-182679 | 1657 | 1 | F | Correction of capability name for NW based CRS interference mitigation | 15.3.0 |
|  | RP-82 | RP-182680 | 1659 | 3 | F | Various sTTI corrections | 15.3.0 |
|  | RP-82 | RP-182676 | 1660 | 3 | F | TS36.306 CR on UE capabilities for mobility and E-UTRA5GC | 15.3.0 |
|  | RP-82 | RP-182677 | 1661 | 1 | A | Mandatory support of skipFallbackCombinations-r13 and diffFallbackCombReport-r14 | 15.3.0 |
|  | RP-82 | RP-182667 | 1663 | 4 | F | Clarification on supportedMIMO-CapabilityDL-r15 | 15.3.0 |
|  | RP-82 | RP-182666 | 1665 | 3 | F | Alternative signalling option for SupportedBandListNR | 15.3.0 |
|  | RP-82 | RP-182671 | 1666 | - | F | Correction to CRS Muting Capability | 15.3.0 |
|  | RP-82 | RP-182674 | 1669 | 3 | F | Signalling of CRS IM and CCH-IM for UE cat 1bis and cat M2 | 15.3.0 |
|  | RP-82 | RP-182677 | 1670 | 1 | A | n1PUCCH-AN-CS-ListP1-r13 ASN.1 error correction | 15.3.0 |
| 03/2019 | RP-83 | RP-190546 | 1673 | 2 | F | CR to 36.306 on introducing eutra-CGI-Reporting-ENDC and utra-geran-CGI-Reporting-ENDC for EN-DC | 15.4.0 |
|  | RP-83 | RP-190548 | 1677 | 1 | A | Correction to support of reduced capability format | 15.4.0 |
|  | RP-83 | RP-190553 | 1678 | 1 | F | UE capability for eLCID support | 15.4.0 |
|  | RP-83 | RP-190550 | 1680 | 2 | F | Introduction of UE capabilities on DMRS overhead reduction | 15.4.0 |
|  | RP-83 | RP-190553 | 1683 | 1 | F | Rapporteur Corrections | 15.4.0 |
|  | RP-83 | RP-190549 | 1686 | 1 | A | UE capability for support of special subframe configuration 10 with TDD-only CA | 15.4.0 |
| 06/2019 | RP-84 | RP-191386 | 1691 | 1 | F | Addition of missing UE capabilities and miscellaneous corrections | 15.5.0 |
|  | RP-84 | RP-191386 | 1692 | - | F | Corrections to sTTI-SPT band parameters capabilities | 15.5.0 |
|  | RP-84 | RP-191383 | 1695 | 1 | A | UE capability signalling for FD-MIMO processing capabilities | 15.5.0 |
|  | RP-84 | RP-191383 | 1697 | - | A | Additional UE capability signalling for SRS carrier switching | 15.5.0 |
|  | RP-84 | RP-191383 | 1699 | 1 | A | Correction to PDCP profile | 15.5.0 |
|  | RP-84 | RP-191383 | 1703 | 1 | A | Corrections on UE capability for eFD-MIMO | 15.5.0 |
|  | RP-84 | RP-191384 | 1706 | 2 | F | Removing square brackets related to 8Rx | 15.5.0 |
|  | RP-84 | RP-191378 | 1707 | - | F | CR to 36.306 on clarification of ANR capability under EN-DC | 15.5.0 |
|  | RP-84 | RP-191376 | 1708 | - | F | UE capability signalling for FD-MIMO processing capabilities for EN-DC | 15.5.0 |
| 09/2019 | RP-85 | RP-192196 | 1709 | 1 | C | Additional capability signalling for 1024QAM support | 15.6.0 |
|  | RP-85 | RP-192196 | 1711 | 1 | F | Correction on the feature downlink SDAP header | 15.6.0 |
|  | RP-85 | RP-192280 | 1715 | 2 | F | CR to introduce NR SS-SINR measurement capability in LTE | 15.6.0 |
|  | RP-85 | RP-192193 | 1716 | - | F | MR-DC measurement gap pattern capability | 15.6.0 |
| 12/2019 | RP-86 | RP-192938 | 1719 | - | F | Miscellaneous corrections | 15.7.0 |
|  | RP-86 | RP-192937 | 1720 | 1 | F | Clarification on the en-DC and ng-EN-DC | 15.7.0 |
| 03/2020 | RP-87 | RP-200338 | 1734 | 2 | F | Correction to support of UP-EDT, CP-EDT, in eMTC TDD | 15.8.0 |
|  | RP-87 | RP-200338 | 1736 | 1 | F | Inclusion of Maximum Number of PDCP SDUs per TTI for DL Categories 22-26 | 15.8.0 |
| 03/2020 | RP-87 | RP-200366 | 1712 | 4 | B | Introduction of UE capabilities for further performance enhancement for LTE in high speed scenario in Rel-16 | 16.0.0 |
|  | RP-87 | RP-200357 | 1723 | 2 | B | Early security re-activation at RRC Connection Resume | 16.0.0 |
|  | RP-87 | RP-200358 | 1727 | 1 | B | Autonomous gap support for CGI reading | 16.0.0 |
|  | RP-87 | RP-200363 | 1729 | 1 | B | Introduction of LTE-based 5G terrestrial broadcast | 16.0.0 |
|  | RP-87 | RP-200361 | 1731 | 1 | B | Introduction of Rel-16 additional enhancements NB-IoT in TS 36.306 | 16.0.0 |
|  | RP-87 | RP-200357 | 1732 | 1 | B | Introduction of DL RRC segmentation | 16.0.0 |
|  | RP-87 | RP-200360 | 1735 | 1 | B | Introduction of additional enhancements for eMTC | 16.0.0 |
|  | RP-87 | RP-200357 | 1741 | - | B | Introduction of wideband PRG size | 16.0.0 |
|  | RP-87 | RP-200359 | 1743 | - | B | Recommended Bit Rate/Query for FLUS and MTSI | 16.0.0 |
|  | RP-87 | RP-200358 | 1745 | - | B | Introduction of UE capability indicator of supporting inter-RAT handover from NR to EN-DC in 36.306 | 16.0.0 |
| 07/2020 | RP-88 | RP-201165 | 1730 | 2 | B | Introduction of NeedForGap capability for NR measurement | 16.1.0 |
|  | RP-88 | RP-201193 | 1746 | 3 | F | Updates for Rel-16 additional enhancements NB-IoT | 16.1.0 |
|  | RP-88 | RP-201167 | 1750 | 3 | A | Clarification on codebook-HARQ-ACK-r13 capability for CA with more than 5CCs | 16.1.0 |
|  | RP-88 | RP-201192 | 1752 | 3 | F | Update of UE capabilities for eMTC | 16.1.0 |
|  | RP-88 | RP-201166 | 1754 | 4 | F | Allowing PDCP version change without handover | 16.1.0 |
|  | RP-88 | RP-201191 | 1755 | 3 | B | Introduce of alternative cell reselection priority for EN-DC | 16.1.0 |
|  | RP-88 | RP-201178 | 1757 | 2 | B | Introduction of UE capabilities for eDCCA | 16.1.0 |
|  | RP-88 | RP-201181 | 1758 | 2 | B | UE radio access capabilities introduction for IIOT WI (CR for 36.306) | 16.1.0 |
|  | RP-88 | RP-201186 | 1759 | 1 | B | CR to 36.306 on introduction of mandatory gap patterns in Rel-16 | 16.1.0 |
|  | RP-88 | RP-201159 | 1761 | - | A | Clarification on L1 feature of NGEN-DC and NE-DC | 16.1.0 |
|  | RP-88 | RP-201195 | 1763 | 1 | B | UE Capability for Rel-16 LTE even further mobility enhancement | 16.1.0 |
|  | RP-88 | RP-201194 | 1764 | 1 | F | MBMS UE capabilities per band for subcarrier spacing of 2.5 kHz and 0.37 kHz | 16.1.0 |
|  | RP-88 | RP-201190 | 1765 | 2 | F | 36.306 CR for overheating in (NG)EN-DC and NR-DC | 16.1.0 |
|  | RP-88 | RP-201185 | 1767 | 1 | B | Introduction of signalling for high-speed train scenarios | 16.1.0 |
|  | RP-88 | RP-201162 | 1769 | 1 | A | Correction to IMS capabilities for NGEN-DC | 16.1.0 |
|  | RP-88 | RP-201197 | 1770 | 1 | B | Introduction of UE capabilities for DL MIMO efficiency enhancement | 16.1.0 |
|  | RP-80 | RP-201164 | 1771 | 2 | A | Introduction of CGI reporting capability | 16.1.0 |
|  | RP-88 | RP-201184 | 1773 | - | B | UE capabilities for NR MDT and SON | 16.1.0 |
|  | RP-88 | RP-201162 | 1774 | - | A | Clarification on L2 and RAN4 features of NGEN-DC and NE-DC | 16.1.0 |
|  | RP-88 | RP-201176 | 1775 | - | B | CR for NR V2X UE capability | 16.1.0 |
| 09/2020 | RP-89 | RP-201927 | 1777 | 1 | B | CR for V2X UE capability | 16.2.0 |
|  | RP-89 | RP-201931 | 1778 | - | F | Correction on RLF Report for Inter-RAT MRO NR | 16.2.0 |
|  | RP-89 | RP-201933 | 1779 | 1 | F | Correction on LTE MOB capability | 16.2.0 |
|  | RP-89 | RP-201933 | 1781 | - | F | Correction on TS 36.306 for DAPS | 16.2.0 |
|  | RP-89 | RP-201931 | 1783 | 1 | F | CR on UE capability of segmentation for UE capability information | 16.2.0 |
| 12/2020 | RP-90 | RP-202779 | 1780 | 4 | F | Addition of missing RSS and relaxed RRM measurement capabilities for eMTC | 16.3.0 |
|  | RP-90 | RP-202769 | 1786 | 1 | B | Update on V2X UE capability | 16.3.0 |
|  | RP-90 | RP-202785 | 1788 | 1 | A | Capturing ul-256QAM-r15 capability | 16.3.0 |
|  | RP-90 | RP-202773 | 1789 | 1 | F | Corrections to UE capabilities | 16.3.0 |
|  | RP-90 | RP-202770 | 1790 | - | F | Correction to 36.306 on UE capability of direct SCell activation | 16.3.0 |
|  | RP-90 | RP-202770 | 1791 | 1 | F | Capability for beam level NR early measurement reporting | 16.3.0 |
|  | RP-90 | RP-202785 | 1794 | 1 | A | Addition of cross-TTI MIB/SIB-BR decoding capability | 16.3.0 |
|  | RP-90 | RP-202770 | 1795 | - | F | Correction on early measurement capabilities | 16.3.0 |
|  | RP-90 | RP-202782 | 1798 | 1 | F | Introducing power sharing for DAPS handover | 16.3.0 |
|  | RP-90 | RP-202780 | 1801 | - | A | Addition of missing NZP CSI-RS transmission capabilities | 16.3.0 |
|  | RP-90 | RP-202782 | 1802 | - | F | UE capability corrections to Mobility Enhancements (LTE) | 16.3.0 |
| 03/2021 | RP-91 | RP-210698 | 1803 | - | F | Dummifying intraFreqMultiUL-TransmissionDAPS-r16 capability | 16.4.0 |
| 06/2021 | RP-92 | RP-211476 | 1782 | 5 | F | Clarification to Fallback band combination definition | 16.5.0 |
|  | RP-92 | RP-211487 | 1804 | 5 | C | Redirection with MPS Indication [Redirect_MPS_I] | 16.5.0 |
|  | RP-92 | RP-211476 | 1806 | 2 | F | Correction on category dependency for DL Category 13 | 16.5.0 |
| 09/2021 | RP-93 | RP-212440 | 1823 | 1 | F | Clarification to RI bit width for Cat5 UEs | 16.6.0 |
|  | RP-93 | RP-212595 | 1824 | 2 | C | Distinguishing support of extended band n77 | 16.6.0 |
| 12/2021 | RP-94 | RP-213340 | 1826 | 1 | F | Addition of missing TEI15 features and other corrections | 16.7.0 |
|  | RP-94 | RP-213340 | 1829 | 1 | A | Add the missing HSDN UE capability for LTE | 16.7.0 |
| 03/2022 | RP-95 | RP-220472 | 1844 | 1 | F | Introduction of carrier specific NRSRP thresholds for NPRACH resource selection | 16.8.0 |
| 03/2022 | RP-95 | RP-220835 | 1827 | 4 | F | Addition of NR-U RSSI/CO measurement UE capability | 17.0.0 |
|  | RP-95 | RP-220837 | 1830 | 1 | B | Introduction of event-based trigger for LTE MDT logging [LTE-Event-MDT] | 17.0.0 |
|  | RP-95 | RP-220506 | 1835 | 1 | D | Inclusive Language Review for TS 36.306 | 17.0.0 |
|  | RP-95 | RP-220508 | 1836 | 1 | B | UE capabilities for new bands and bandwidth allocation for LTE-based 5G terrestrial broadcast | 17.0.0 |
|  | RP-95 | RP-220837 | 1837 | 1 | B | Introduction of MINT [MINT] | 17.0.0 |
|  | RP-95 | RP-220837 | 1838 | 1 | B | On introducing height information reporting in MDT reports [LTE-Height-MDT] | 17.0.0 |
|  | RP-95 | RP-220472 | 1839 | 1 | F | Correction on PO determination for UE in inactive state | 17.0.0 |
|  | RP-95 | RP-220507 | 1841 | 1 | B | Introduction of additional enhancements for NB-IoT and eMTC | 17.0.0 |
|  | RP-95 | RP-220475 | 1845 | 1 | B | UE capabilities for the support of NR 71GHz | 17.0.0 |
|  | RP-95 | RP-220509 | 1846 | 1 | B | Support of Non-Terrestrial Network in NB-IoT and eMTC | 17.0.0 |
| 06/2022 | RP-96 | RP-221738 | 1847 | 2 | C | Distinguishing support of band n77 restrictions in Canada [n77 Canada] | 17.1.0 |
|  | RP-96 | RP-221736 | 1850 | 1 | B | Introduction of gNB ID length reporting in the NR CGI report [gNB_ID_Length] | 17.1.0 |
|  | RP-96 | RP-221758 | 1851 | 1 | B | Introduction of additional IoT-NTN UE Capabilities | 17.1.0 |
|  | RP-96 | RP-221758 | 1853 | - | C | Introduction of uplink RRC Segmentation capability | 17.1.0 |
| 09/2022 | RP-97 | RP-222525 | 1856 | 1 | F | UE Capability CR for HO from E-UTRA to FR2-2 | 17.2.0 |
|  | RP-97 | RP-222522 | 1857 | 1 | F | UE capabilities correction for IoT-NTN | 17.2.0 |
|  | RP-97 | RP-222527 | 1859 | 1 | F | Ensuring consistent support of capability bits and associated NS-values in n77 in USA and Canada | 17.2.0 |
| 12/2022 | RP-98 | RP-223409 | 1864 | 1 | F | Miscellaneous Correction for IoT-NTN Capabilities | 17.3.0 |
|  | RP-98 | RP-223409 | 1865 | - | F | Correction to npusch-16QAM-r17 | 17.3.0 |
|  | RP-98 | RP-223405 | 1866 | - | F | Support of Multiple CSI Subframe Sets on CQI-ReportPeriodicScell | 17.3.0 |
| 03/2023 | RP-99 | RP-230696 | 1867 | - | F | Correct the references for IoT NTN | 17.4.0 |
|  | RP-99 | RP-230687 | 1869 | 2 | A | Introduction of UE capability parameter cellIndividualOffsetForNR [CIO-IRAT-HO-ToNR] | 17.4.0 |
| 12/2023 | RP-102 | RP-233890 | 1873 | 2 | F | Introduction of UE capability for inter-RAT NR FR2 measurements without measurement gap | 17.5.0 |
|  | RP-102 | RP-233915 | 1870 | 5 | B | Introduction of measurements without gap with interruption | 18.0.0 |
|  | RP-102 | RP-233892 | 1871 | 2 | B | Introduction of Enhanced LTE Support for UAV | 18.0.0 |
|  | RP-102 | RP-233891 | 1872 | 1 | B | Introduction of Rel-18 IoT NTN UE capabilities | 18.0.0 |
|  | RP-102 | RP-233883 | 1874 | 2 | B | Protection against improper reselection to GERAN/UTRAN [RESELECTION_TO GSM_AND_UTRAN] | 18.0.0 |
|  | RP-102 | RP-233909 | 1875 | - | B | CR to 36.306 for UE capability for R18 SONMDT | 18.0.0 |
| 03/2024 | RP-103 | RP-240654 | 1877 | - | A | Removal of references to unknown RAN4 specification | 18.1.0 |
|  | RP-103 | RP-240683 | 1878 | 1 | B | Lower MSD capability for EN-DC | 18.1.0 |
|  | RP-103 | RP-240652 | 1881 | 1 | A | UE Capability on UE location information in NB-IoT RLF report | 18.1.0 |
|  | RP-103 | RP-240704 | 1882 | - | B | Introduction of mIAB Inter-RAT cell reselection enhancements for 36.306 [TEI18_MIAB_IRAT] | 18.1.0 |
|  | RP-103 | RP-240660 | 1883 | - | F | Update on IoT NTN UE capabilities | 18.1.0 |
| 06/2024 | RP-104 | RP-241545 | 1884 | 2 | F | Capabilities for Rel-18 Enhanced LTE Support for UAV WI | 18.2.0 |
|  | RP-104 | RP-241548 | 1888 | 1 | A | Correction to mandatory 80ms scheduling offset for positioning SI acquisition | 18.2.0 |
|  | RP-104 | RP-241542 | 1889 | 1 | F | Miscellaneous corrections for IoT NTN capabilities | 18.2.0 |
| 09/2024 | RP-105 | RP-242237 | 1890 | 1 | F | Correction for UAV capabilities | 18.3.0 |
|  | RP-105 | RP-242237 | 1892 | - | F | Corrections of UE Capabilities in IoT NTN | 18.3.0 |
| 12/2024 | RP-106 | RP-243220 | 1894 | 3 | F | Applicability of optional UE Capabilities for NB-IoT | 18.4.0 |
|  | RP-106 | RP-243228 | 1901 | 1 | F | UE feature for SIB33(-NB) reception in RRC_IDLE state in a TN cell | 18.4.0 |
|  | RP-106 | RP-243220 | 1902 | - | F | IoT NTN UE capabilities correction for GNSS and HARQ enhancements | 18.4.0 |
|  | RP-106 | RP-243220 | 1903 | - | F | Capability on measurement gap enhancements | 18.4.0 |
|  | RP-106 | RP-243227 | 1905 | - | A | Introduction of network signalling of maximum number of UL segments [Max-RRC-SegUL] | 18.4.0 |
| 06/2025 | RP-108 | RP-251688 | 1910 | 1 | A | Introducing UE capability for A4 A5 ReportOnLeave | 18.5.0 |
|  | RP-108 | RP-251696 | 1913 | - | B | Introduction of the inband operation for NTN IoT in NR NTN [NTNNBIoT_inbandNTNNR] | 18.5.0 |
| 09/2025 | RP-109 | RP-252767 | 1922 | 2 | A | Correction on inter-RAT FR2 measurement capabilities | 18.6.0 |
| 09/2025 | RP-109 | RP-252796 | 1911 | 2 | B | Introduction of ANR reporting of HSDN cells [ANR_HSDN] | 19.0.0 |
|  | RP-109 | RP-252792 | 1912 | 3 | B | UE capability for Rel-19 IoT NTN | 19.0.0 |
|  | RP-109 | RP-252795 | 1914 | 1 | B | Introduction of capabilities for IoT NTN TDD | 19.0.0 |
|  | RP-109 | RP-252783 | 1915 | - | B | Introduction of SONMDT UE Capabilities | 19.0.0 |
|  | RP-109 | RP-252797 | 1916 | 1 | B | Introduction of CAS muting in LTE-based 5G broadcast [5GB_CASMuting] | 19.0.0 |
|  | RP-109 | RP-252796 | 1917 | - | B | Introduction of E-UTRAN to NB-IoT NTN Mobility UE Capability [EUTRAN-to-NBIoTNTN] | 19.0.0 |
|  | RP-109 | RP-252793 | 1918 | 1 | B | Introduction of LTE TN to NR NTN Mobility UE Capability | 19.0.0 |
|  | RP-109 | RP-252794 | 1920 | 1 | B | Introduction of LTE-based 5G Broadcast Phase 2 | 19.0.0 |
|  | RP-109 | RP-252797 | 1925 | 1 | B | Introduction of IoT TN to NTN redirection to 36.306 [IoT_TN_NTN_redir] | 19.0.0 |
| 12/2025 | RP-110 | RP-253735 | 1932 | 2 | B | Introduction of MINT in EPS | 19.1.0 |
|  | RP-110 | RP-253742 | 1933 | 1 | F | Correction for the redirection from E-UTRAN TN to NB-IoT NTN [IoT_TN_NTN_redir] | 19.1.0 |
|  | RP-110 | RP-253738 | 1934 | 2 | F | Correction on the capability of LTE-based 5G Broadcast | 19.1.0 |
|  | RP-110 | RP-253742 | 1935 | 1 | B | Assistance info for IoT-NTN to NR-NTN Cell Selection [IoT_NR_NTN_CellSelect] | 19.1.0 |
|  | RP-110 | RP-253745 | 1936 | 1 | F | UE capability for Rel-19 IoT NTN | 19.1.0 |
|  | RP-110 | RP-253742 | 1937 | 2 | F | Indication of supported NB-IoT NTN band list in E-UTRAN [IoT_TN_NTN_redir] | 19.1.0 |
| 03/2026 | RP-111 | RP-260671 | 1938 | 1 | F | Correction to TN-NTN redirection [IoT_TN_NTN_redir][EUTRAN-to-NBIoTNTN] | 19.2.0 |
|  | RP-111 | RP-260669 | 1939 | 1 | F | Support of power boost in Rel-19 NB-IoT NTN | 19.2.0 |
|  | RP-111 | RP-260666 | 1941 | 1 | A | Conditionally mandatory support for inter-RAT configuration for dedicated spectrum less than 5MHz for NR FR1 | 19.2.0 |

Note: In CR0313R1 " Clarification on Pcell support " for TS 36.306 v12.7.0 of RP-152053 which was approved by RAN #70 wrong CR number, 1313 used in CR coversheet due to a misallocation.
