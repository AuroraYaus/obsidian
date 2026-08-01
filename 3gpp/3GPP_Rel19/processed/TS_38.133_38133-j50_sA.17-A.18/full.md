# A.17 NR standalone tests with one or more NR cells in FR2 for RedCap

## A.17.1 SA: RRC_IDLE state mobility for RedCap

### A.17.1.1 Cell re-selection to NR

#### A.17.1.1.1 Cell reselection to FR2 intra-frequency NR case for 2 Rx

##### A.17.1.1.1.1 Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements specified in clause 4.2B.2.3.

##### A.17.1.1.1.2 Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.17.1.1.1.2-1, A.17.1.1.1.2-2 and A.17.1.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.17.1.1.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.17.1.1.1.2-2: General test parameters for RedCap UE intra frequency NR cell re-selection test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2 | Cell 1 |  |
| T2 end condition | Active cell |  | 1, 2 | Cell 2 |  |
|  | Neighbour cell |  | 1, 2 | Cell 1 |  |
| Final condition | Active cell |  | 1, 2 | Cell 1 |  |
|  | Neighbour cell |  | 1, 2 | Cell 2 |  |
| RF Channel Number |  |  | 1, 2 | 1 |  |
| Time offset between cells |  |  | 1, 2 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1, 2 | Not Sent | No additional delays in random access procedure. |
| SMTC configuration |  |  | 1, 2 | SMTC.1 |  |
| DRX cycle length |  | s | 1, 2 | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2 | 190 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2 | Not configured |  |
| T1 |  | s | 1, 2 | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, the intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2 |
| T2 |  | s | 1, 2 | 135 | T2 needs to be defined so that cell re-selection reaction time is taken into account. |
| T3 |  | s | 1, 2 | 35 | T3 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.17.1.1.1.2-3: Cell specific test parameters for RedCap UE intra frequency NR cell re-selection test case in AWGN

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| TDD configuration |  | 1, 2 | TDDConf.3.1 |  |  | TDDConf.3.1 |  |  |
| PDSCH RMC configuration |  | 1 | SR.3.1 TDD |  |  | SR.3.1 TDD |  |  |
|  |  | 2 | SR.3.1 TDD |  |  | SR.3.1 TDD |  |  |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD |  |  | CR.3.1 TDD |  |  |
|  |  | 2 | CR.3.1 TDD |  |  | CR.3.1 TDD |  |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 TDD |  |  | CCR.3.1 TDD |  |  |
|  |  | 2 | CCR.3.1 TDD |  |  | CCR.3.1 TDD |  |  |
| SSB configuration |  | 1 | SSB.3 FR2 |  |  | SSB.7 FR2 |  |  |
|  |  | 2 | SSB.4 FR2 |  |  | SSB.8 FR2 |  |  |
| OCNG Pattern |  | 1, 2 | OP.4 |  |  | OP.4 |  |  |
| BWchannel | MHz | 1, 2 | 100: NPRB,c = 66 |  |  | 100: NPRB,c = 66 |  |  |
| Data PRBs allocated |  | 1, 2 | 66 |  |  | 66 |  |  |
| Initial DL BWP configuration |  | 1, 2 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1, 2 | SSB |  |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1 | -138 |  |  | -138 |  |  |
|  |  | 2 | -135 |  |  | -135 |  |  |
| Pcompensation | dB | 1, 2 | 0 |  |  | 0 |  |  |
| Qhysts | dB | 1, 2 | 0 |  |  | 0 |  |  |
| Qoffsets, n | dB | 1, 2 | 0 |  |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2 | SS-RSRP |  |  | SS-RSRP |  |  |
| AoA setup |  | 1, 2 | Setup 1 defined in clause A.3.15.1 |  |  | Setup 1 defined in clause A.3.15.1 |  |  |
| Beam assumptionNote 4 |  | 1,2 | Rough |  |  | Rough |  |  |
| $\hat  {E}_{s}/I_{otBB}$ Note 5 | dB | 1, 2 | 7.45 | -3.55 | 0.95 | -infinity | 0.95 | -3.55 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -93 |  |  |  |  |  |
|  |  | 2 | -90 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 2 | -102 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2 | 8 | -3 | 1.5 | -infinity | 1.5 | -3 |
| SSB_RP Note3 | dBm/SCS | 1 | -85 | -96 | -91.5 | -infinity | -91.5 | -96 |
|  |  | 2 | -82 | -93 | -88.5 | -infinity | -88.5 | -93 |
| Io on SSB symbols | dBm/95.04 MHz | 1 | -60.53 | -67.40 | -65.34 | -69.17 | -65.34 | -67.40 |
| of each cell |  | 2 | -57.52 | -64.39 | -62.33 | -66.16 | -62.33 | -64.39 |
| Treselection | s | 1, 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| SintrasearchP | dB | 1, 2 | 50 |  |  | 50 |  |  |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SSB_RP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 5: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] Table 6.2.1.3-4. |  |  |  |  |  |  |  |  |

##### A.17.1.1.1.3 Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2 and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration updateon Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 130 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1 and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration updateon Cell 1.

The cell re-selection delay to an already detected cell shall be less than 27 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_Intra See Table 4.2B.2.3-1 in clause 4.2B.2.3

Tevaluate, NR_ intra See Table 4.2B.2.3-1 in clause 4.2B.2.3

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 129.28 s, allow 130 s for the cell re-selection delay to a newly detectable cell and 26.88 s for the cell re-selection delay to an already detected cell in the test case, which we allow 27 s.

#### A.17.1.1.2 Cell reselection to FR2 inter-frequency NR case

##### A.17.1.1.2.1 Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements specified in clause 4.2B.2.4.

##### A.17.1.1.2.2 Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.17.1.1.2.2-1, A.17.1.1.2.2-2 and A.17.1.1.2.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.17.1.1.2.2-1: Supported test configurations

| Configuration | Description for serving cell | Description for target cell |
| --- | --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode | 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |  |

Table A.17.1.1.2.2-2: General test parameters for RedCap UE FR2 inter frequency NR cell re-selection test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2 | Cell 2 | The UE camps on Cell 2 in the initial phase and during T1 period the UE reselects to Cell 1 |
|  | Neighbour cell |  | 1, 2 | Cell 1 |  |
| T1 end condition | Active cell |  | 1, 2 | Cell 1 | The UE shall perform reselection to Cell 1 during T1 |
|  | Neighbour cells |  | 1, 2 | Cell 2 |  |
| T3 end condition | Active cell |  | 1, 2 | Cell 2 | The UE shall perform reselection to Cell 2 with higher priority during T3 |
|  | Neighbour cell |  | 1, 2 | Cell 1 |  |
| RF Channel Number |  |  | 1, 2 | 1, 2 |  |
| Time offset between cells |  |  | 1, 2 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1, 2 | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | 1 | SSB.1 FR2 |  |
|  |  |  | 2 | SSB.2 FR2 |  |
| SMTC configuration |  |  | 1, 2 | SMTC.1 |  |
| DRX cycle length |  | s | 1, 2 | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2 | 190 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2 | Not configured |  |
| T1 |  | s | 1, 2 | 35 | T1 needs to be defined so that cell re-selection reaction time is taken into account. |
| T2 |  | s | 1, 2 | >7 | During T2, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed. The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T3. |
| T3 |  | s | 1, 2 | 95 | T3 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.17.1.1.2.2-3: Cell specific test parameters for RedCap UE FR2 inter frequency NR cell re-selection test case in AWGN

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| TDD configuration |  | 1, 2 | TDDConf.3.1 |  |  | TDDConf.3.1 |  |  |
| PDSCH RMC configuration |  | 1, 2 | SR.3.1 TDD |  |  | SR.3.1 TDD |  |  |
| RMSI CORESET parameters |  | 1, 2 | CR.3.1 TDD |  |  | CR.3.1 TDD |  |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CCR.3.1 TDD |  |  | CCR.3.1 TDD |  |  |
| OCNG Pattern |  | 1, 2 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1, 2 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1, 2 | SSB |  |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1 | -140 |  |  | -140 |  |  |
|  |  | 2 | -137 |  |  | -137 |  |  |
| Pcompensation | dB | 1, 2 | 0 |  |  | 0 |  |  |
| Qhysts | dB | 1, 2 | 0 |  |  | 0 |  |  |
| Qoffsets, n | dB | 1, 2 | 0 |  |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2 | SS-RSRP |  |  | SS-RSRP |  |  |
| AoA setup |  | 1, 2 | Setup 1 defined in clause A.3.15.1 |  |  | Setup 1 defined in clause A.3.15.1 |  |  |
| Beam assumptionNote 4 |  | 1,2 | Rough |  |  | Rough |  |  |
| $\hat  {E}_{s}/I_{otBB}$ Note 5 | dB | 1,2 | 9.95 | 9.95 | 7.45 | -11.05 | -infinity | 7.95 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -93 |  |  | -93 |  |  |
|  |  | 2 | -90 |  |  | -90 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 2 | -102 |  |  | -102 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 10.5 | 10.5 | 8 | -10.5 | -infinity | 8.5 |
| SSB_RP Note3 | dBm/SCS | 1 | —82.5 | —82.5 | -85 | -103.5 | -infinity | -84.5 |
|  |  | 2 | -79.5 | -79.5 | -82 | -100.5 | -infinity | -81.5 |
| Io | dBm/95.04 MHz | 1, 2 | -53.11 | -53.11 | -55.34 | -63.61 | -63.98 | -54.91 |
| Treselection | s | 1, 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| SnonintrasearchP | dB | 1, 2 | 50 |  |  | 50 |  |  |
| Threshx, highP | dB | 1, 2 | 48 |  |  | 48 |  |  |
| Threshserving, lowP | dB | 1, 2 | 44 |  |  | 44 |  |  |
| Threshx, lowP | dB | 1, 2 | 50 |  |  | 50 |  |  |
| Propagation Condition |  | 1, 2 | AWGN |  |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated, and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SSB_RP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 5: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] Table 6.2.1.3-4. |  |  |  |  |  |  |  |  |

##### A.17.1.1.2.3 Test Requirements

The cell reselection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 2 and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration updateon Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 87 s.

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1 and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration updateon Cell 1.

The cell re-selection delay to a lower priority cell shall be less than 27 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Thigher_priority_search See clause 4.2B.2.7

Tevaluate, NR_ inter See Table 4.2B.2.4-1 in clause 4.2B.2.4

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 86.88 s, allow 87 s for the cell re-selection delay to a higher priority cell and 26.88 s for the cell re-selection delay to a lower priority cell in the test case, which we allow 27 s.

#### A.17.1.1.3 Cell reselection to FR2 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE

##### A.17.1.1.3.1 Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for UE configured with stationary relaxed measurement criterion specified in clause 4.2B.2.9.2.

##### A.17.1.1.3.2 Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.17.1.1.3.2-1, A.17.1.1.3.2-2 and A.17.1.1.3.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. During T1 and T2, only criteria stationaryMobilityEvaluation is configured and fulfilled. UE has not registered with network for the tracking area containing cell2.

Table A.17.1.1.3.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.17.1.1.3.2-2: General test parameters for FR2 intra-frequency NR cell re-selection test case for UE fulfilling stationary criterion for 2 Rx UE

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2 | Cell 1 | The UE camps on Cell 1 in the initial phase |
|  | Neighbour cells |  | 1, 2 | Cell 2 |  |
| T1 end condition | Active cell |  | 1, 2 | Cell 2 | The UE reselects to Cell 2 during T1 period |
|  | Neighbour cells |  | 1, 2 | Cell 1 |  |
| Final condition | Active cell |  | 1, 2 | Cell 1 | The UE reselects to Cell 1 during T2 period |
|  | Neighbour cells |  | 1,2 | Cell 2 |  |
| RF Channel Number |  |  | 1, 2 | 1 |  |
| Time offset between cells |  |  | 1, 2 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1, 2 | Not Sent | No additional delays in random access procedure. |
| SMTC configuration |  |  | 1, 2 | SMTC.1 |  |
| DRX cycle length |  | s | 1, 2 | 0.64 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2 | 190 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2 | Not configured |  |
| T1 |  | s | 1, 2 | 100 |  |
| T2 |  | s | 1, 2 | 100 |  |

Table A.17.1.1.3.2-3: Cell specific test parameters for FR2 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling stationary mobility criterion for 2 Rx UE

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 |  | T2 |
| TDD configuration |  | 1, 2 | TDDConf.3.1 |  | TDDConf.3.1 |  |  |
| PDSCH RMC |  | 1 | SR.3.1 TDD |  | SR.3.1 TDD |  |  |
| configuration |  | 2 | SR.3.1 TDD |  | SR.3.1 TDD |  |  |
| RMSI CORESET |  | 1 | CR.3.1 TDD |  | CR.3.1 TDD |  |  |
| RMC configuration |  | 2 | CR.3.1 TDD |  | CR.3.1 TDD |  |  |
| Dedicated CORESET |  | 1 | CCR.3.1 TDD |  | CCR.3.1 TDD |  |  |
| RMC configuration |  | 2 | CCR.3.1 TDD |  | CCR.3.1 TDD |  |  |
| SSB configuration |  | 1 | SSB.3 FR2 |  | SSB.7 FR2 |  |  |
|  |  | 2 | SSB.4 FR2 |  | SSB.8 FR2 |  |  |
| OCNG Pattern |  | 1, 2 | OP.4 |  | OP.4 |  |  |
| Initial DL BWP configuration |  | 1, 2 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |  |
| Initial UL BWP configuration |  | 1, 2 | 66 |  | 66 |  |  |
| RLM-RS |  | 1, 2 | SSB |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1 | -140 |  | -140 |  |  |
|  |  | 2 | -137 |  | -137 |  |  |
| SSearchDeltaP-Stationary | dB | 1, 2 | 6 |  | 6 |  |  |
| TSearchDeltaP-Stationary | s | 1,2 | 5 |  | 5 |  |  |
| Pcompensation | dB | 1, 2 | 0 |  | 0 |  |  |
| Qhysts | dB | 1, 2 | 0 |  | 0 |  |  |
| Qoffsets, n | dB | 1, 2 | 0 |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2 | SS-RSRP |  | SS-RSRP |  |  |
| AoA setup |  | 1, 2 | Setup 1 defined in clause A.3.15.1 |  | Setup 1 defined in clause A.3.15.1 |  |  |
| Beam assumptionNote 4 |  | 1,2 | Rough |  | Rough |  |  |
| $\hat  {E}_{s}/I_{otBB}$ Note 5 | dB | 1 | -3.55 | 0.95 | 0.95 | -3.55 |  |
|  |  | 2 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -93 |  |  |  |  |
|  |  | 2 | -90 |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -102 |  |  |  |  |
|  |  | 2 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | -3 | 1.5 | 1.5 | -3 |  |
|  |  | 2 |  |  |  |  |  |
| SS-RSRP Note3 | dBm/SCS | 1 | 96 | 91.5 | 91.5 | 96 |  |
|  |  | 2 | 93 | -88.5 | 88.5 | 93 |  |
| Io on SSB symbols of each cell | dBm/95.04 MHz | 1 | -67.40 | -65.34 | -65.34 | -67.40 |  |
|  |  | 2 | -64.40 | -62.34 | -62.34 | -64.40 |  |
| Treselection | s | 1, 2 | 0 | 0 | 0 | 0 |  |
| SintrasearchP | dB | 1, 2 | 50 |  | 50 |  |  |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |  |  |

##### A.17.1.1.3.3 Test Requirements

The cell reselection delay to an already detected cell for UE fulfilling stationary relaxed criterion is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected cell shall be less than 155 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to an already detectable cell can be expressed as: Tevaluate,NR_Intra_RedCap_Relax + TSI-NR,

Where:

Tevaluate,NR_Intra_RedCap_Relax See Table 4.2B.2.9.2-2 in clause4.2B.2.9.2,

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 154.88 s, allow 155 s for the cell re-selection delay to an already detected cell for UE fulfilling stationary criterion in the test case.

#### A.17.1.1.4 Cell reselection to FR2 inter-frequency NR case for UE fulfilling stationary mobility relaxed measurement criterion for 2 Rx UE

##### A.17.1.1.4.1 Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for UE fulfilling stationary relaxed measurement criterion specified in clause4.2B.2.10.2.

##### A.17.1.1.4.2 Test Parameters

The test scenario comprises of 2 cells (Cell 1 and Cell 2) on 2 different NR carriers respectively as given in tables A.17.1.1.4.2-1, A.17.1.1.4.2-2 and A.17.1.1.4.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. Cell 2 is of higher priority than Cell 1. The UE is configured with stationaryMobilityEvaluation criterion [2].

Table A.17.1.1.4.2-1: Supported test configurations

| Configuration | Description for serving cell | Description for target cell |
| --- | --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode | 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |  |

Table A.17.1.1.4.2-2: General test parameters for FR2 inter frequency NR cell re-selection test case for UE fulfilling stationary criterion for 2 Rx UE

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2 | Cell 2 | The UE camps on cell2 and fulfils stationary (stationaryMobilityEvaluation [2]) criterion. |
|  | Neighbour cell |  | 1, 2 | Cell 1 |  |
| T1 final condition | Active cell |  | 1, 2 | Cell 1 | The UE reselects to low priority cell1 during T1 |
|  | Neighbour cell |  | 1, 2 | Cell 2 |  |
| T2 final condition | Active cell |  | 1, 2 | Cell 2 | The UE reselects to high priority cell2 during T2 |
|  | Neighbour cell |  |  | Cell 1 |  |
| RF Channel Number |  |  | 1, 2 | 1, 2 |  |
| Time offset between cells |  |  | 1, 2 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1, 2 | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | 1 | SSB.1 FR2 |  |
|  |  |  | 2 | SSB.2 FR2 |  |
| SMTC configuration |  |  | 1, 2 | SMTC.1 |  |
| DRX cycle length |  | s | 1, 2 | 0.64 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2 | 190 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2 | Not configured |  |
| T1 |  | s | 1, 2 | 85 | T1 needs to be long enough to allow cell re-selection to already known cell1 |
| T2 |  | s | 1, 2 | 85 | T2 needs to be long enough to allow cell re-selection to already known cell2 |

Table A.17.1.1.4.2-3: Cell specific test parameters for FR2 inter frequency NR cell re-selection test case in AWGN for UE fulfilling stationary criterion for 2 Rx UE

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| TDD configuration |  | 1, 2 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| PDSCH RMC configuration |  | 1, 2 | SR.3.1 TDD |  | SR.3.1 TDD |  |
| RMSI CORESET parameters |  | 1, 2 | CR.3.1 TDD |  | CR.3.1 TDD |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CCR.3.1 TDD |  | CCR.3.1 TDD |  |
| OCNG Pattern |  | 1, 2 | OP.1 defined in A.3.2.1 |  | OP.1 defined in A.3.2.1 |  |
| Initial DL BWP configuration |  | 1, 2 | DLBWP.0.1 |  | DLBWP.0.1 |  |
| Initial UL BWP configuration |  | 1, 2 | ULBWP.0.1 |  | ULBWP.0.1 |  |
| RLM-RS |  | 1, 2 | SSB |  | SSB |  |
| Qrxlevmin | dBm/SCS | 1 | -140 |  | -140 |  |
|  |  | 2 | -137 |  | -137 |  |
| Pcompensation | dB | 1, 2 | 0 |  | 0 |  |
| Qhysts | dB | 1, 2 | 0 |  | 0 |  |
| Qoffsets, n | dB | 1, 2 | 0 |  | 0 |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2 | SS-RSRP |  | SS-RSRP |  |
| AoA setup |  | 1, 2 | Setup 1 defined in clause A.3.15.1 |  | Setup 1 defined in clause A.3.15.1 |  |
| Beam assumptionNote 4 |  | 1, 2 | Rough |  | Rough |  |
| $\hat  {E}_{s}/I_{otBB}$ Note 5 | dB | 1, 2 | 9.95 | 7.45 | -11.05 | 7.95 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -93 |  | -93 |  |
|  |  | 2 | -90 |  | -90 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 2 | -102 |  | -102 |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2 | 10.5 | 8 | -10.5 | 8.5 |
| SSB_RP Note3 | dBm/SCS | 1 | -82.5 | -85 | -103.5 | -84.5 |
|  |  | 2 | -79.5 | -82 | -100.5 | -81.5 |
| Io | dBm/95.04 MHz | 1, 2 | -53.14 | -55.37 | -63.64 | -54.94 |
| TreselectionNR | s | 1, 2 | 0 |  | 0 |  |
| SnonintrasearchP | dB | 1, 2 | 50 |  | Not sent |  |
| SSearchDeltaP-Stationary | dB | 1, 2 | 6 |  | 6 |  |
| TSearchDeltaP-Stationary | s | 1, 2 | 5 |  | 5 |  |
| Threshx, highP | dB | 1, 2 | 48 |  | 48 |  |
| Threshserving, lowP | dB | 1, 2 | 44 |  | 44 |  |
| Threshx, lowP | dB | 1, 2 | 50 |  | 50 |  |
| Propagation Condition |  | 1, 2 | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SSB_RP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 5: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] Table 6.2.1.3-4. |  |  |  |  |  |  |

##### A.17.1.1.4.3 Test Requirements

The cell reselection delay to an already detected low priority cell (Cell 1) for UE fulfilling stationary criterion is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected low priority cell, Cell 1, shall be less than 155 s.

The cell reselection delay to an already detected high priority cell (Cell 2) for UE fulfilling stationary criterion is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected high priority cell, Cell 2, shall be less than 155 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE 1: The cell re-selection delay to an already detected low priority cell can be expressed as: Tevaluate,NR_Inter_RedCap_Relax + TSI-NR

NOTE 2: The cell re-selection delay to an already detected higher priority cell can be expressed as: Tevaluate,NR_Inter_RedCap_Relax + TSI-NR

Where:

Tevaluate,NR_Inter_RedCap_Relax See Table 4.2B.2.10.2-2 in clause4.2B.2.10.2

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 154.88 s, allow 155 s for the cell re-selection delay to an already detected low priority cell for UE fulfilling stationary criterion in the test case.

This gives a total of 154.88 s, allow 155 s for the cell re-selection delay to an already detected high priority cell for UE fulfilling stationary criterion in the test case.

## A.17.2 SA: RRC_INACTIVE state mobility for RedCap

### A.17.2.1 Configured Grant based Small Data Transmissions (CG-SDT) for RedCap

#### A.17.2.1.1 TA validation for CG-SDT in FR2 for RedCap

##### A.17.2.1.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly perform TA validation for CG-SDT transmission in clause 5.2B.3. The test includes two sub-tests, Sub-test#1 for testing valid TA where UE can initiate CG-SDT transmission, and Sub-test#2 for testing invalid TA where UE does not initiate CG-SDT transmission. Sub-test#2 is only tested if Sub-test#1 is passed. For each sub-test, UE is configured with CG-SDT configurations when entering RRC Inactive state. Sub-test#1 consists of four successive time periods, with time duration of T1, T2, T3 and T4 respectively. Sub-test#2 consists of two successive time periods, with time duration of T5 and T6 respectively. There is one cell, which is the active NR cell in FR2. Figure A.17.1.1.2.1-1 shows the variation of the RSRP over the duration of Sub-test#1 and Figure A.17.1.1.2.1-2 shows the variation of the RSRP over the duration of Sub-test#2.

In Sub-test#1:

- Prior to the time point TA, the UE shall be fully synchronized to PCell (Cell 1), be registered to the cell and have entered RRC connected mode.

- Before starting the test at time point TA, test equipment configures RSRP to P0.

- At time point TB, RSRP is changed from P0 to P1.

- At time point TC which is W1 after time point TB, UE expect to receive RRC release with CG-SDT configuration and RRC status is changed to INACTIVE status.

- At time point TD, RSRP is changed from P1 to P0.

- At time point TE, RSRP is changed from P0 to P2. TE must be W2 before TF.

- Test equipment triggers UL data arrival at UE lower layer at time point TF. After time point TF, test equipment observes whether UE transmits with CG-SDT no later than TG which is W3 after TF.

- After time point TG, RRC status is changed from RRC INACTIVE to RRC CONNECTED.

In Sub-test#2:

- Prior to the time point TA, the UE shall pass Sub-test#1 and have entered RRC connected mode. Otherwise, Sub-test#2 shall not be executed.

- From time point TA to time point TD, RSRP is set to P2.

- At time point TC, which is W1 after time point TB, UE expect to receive RRC release with CG SDT configuration and RRC status is changed to INACTIVE status.

- At time point TD, RSRP is changed from P2 to P0.

- Test equipment triggers UL data arrival at UE lower layer at time point TF. TF is 3520 ms after TD. After time point TF, test equipment observes whether UE transmits with CG-SDT no later than TG which is W3 after TF.

W1 equals to 480 ms and W2 equals to 480 ms based on requirements in clause 5.2.B2.1. W3 is 1060 ms.

Table A.17.2.1.1.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | NR TDD, SSB SCS 120 kHz, data SCS 120KHz, BW 100 MHz |

Table A.17.2.1.1.1-2: General test parameters for TA validation for CG-SDT in FR2

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| Active PCell |  |  | Cell 1 |
| RF Channel Number |  |  | 1 |
| Duplex mode | Config 1 |  | TDD |
| BWchannel | Config 1 | MHz | 100: NPRB,c = 66 |
| DL initial BWP configuration | Config 1 |  | DLBWP.0.1 |
| UL initial BWP configuration | Config 1 |  | ULBWP.0.1 |
| TDD Configuration | Config 1 |  | TDDConf.3.1 |
| RMSI CORESET Reference Channel | Config 1 |  | CR.3.1 DD |
| SSB Configuration | Config 1 |  | SSB.3 FR2 |
| SMTC Configuration | Config 1 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing | Config 1 | kHz | 120 |
| PRACH Configuration | Config 1 |  | Table A.3.8.3.4 |
| OCNG parameters |  |  | OP.5 |
| CP length |  |  | Normal |
| Correlation Matrix and Antenna Configuration |  |  | 2x2 Low |
| DRX |  | s | 0.64 |
| cg-SDT-RSRP-ThresholdSSB |  | dBm | -110 |
| cg-SDT-RSRP-ChangeThreshold |  | dB | 8 |
| cg-SDT-TimeAlignmentTime |  |  | infinity |
| CG-SDT resource period |  | ms | 320 |
| T1 |  | s | 0.8 |
| T2 |  | s | 0.96 |
| T3 |  | s | 3.04 |
| T4 |  | s | 1.54 |
| T5 |  | s | 1.76 |
| T6 |  | s | 4.58 |

Table A.17.2.1.1.1-3: Cell specific test parameters TA validation for CG-SDT in FR2

| Parameter |  | Unit | SSB#0 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 | T6 |
| AoA setup |  |  | Setup 1 defined in A.3.15 |  |  |  |  |  |
| Assumption for UE beams Note 4 |  |  | Rough |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 4 |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB | 0 |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB | 0 |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15 kHz | -109 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | Config 1 | dBm/SCS | -100 |  |  |  |  |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] | Config 1 | dB | 0 | 13 | 0 | 24.5 | 24.5 | 0 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | Config 1 | dB | 0 | 13 | 0 | 24.5 | 24.5 | 0 |
| SS-RSRP | Config 1 | dBm/SCS | -100 | -87 | -100 | -75.5 | -75.5 | -100 |
| Io | Config 1 | dBm/95.04 MHz | -68 | -57.8 | -68 | -46.5 | -46.5 | -68 |
| Propagation condition |  |  | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation. |  |  |  |  |  |  |  |  |

Figure A.17.2.1.1.1-1: RSRP variation model for CG-SDT Sub-test#1

Figure A.17.2.1.1.1-2: RSRP variation model for CG-SDT Sub-test#2

##### A.17.2.1.1.2 Test Requirements

The UE behaviour in each test during time durations shall be as follows:

During Sub-test#1, UE shall transmit UL data with CG-SDT within 1060 ms after time point TF.

During Sub-test#2, after passing Sub-test#1, UE shall not transmit PUSCH at CG-SDT resources after TF until the end of the test at time point TG.

The rate of correct events observed during repeated tests shall be at least 90 %.

### A.17.2.2 Cell Reselection for Positioning

#### A.17.2.2.1 Cell reselection to FR2 intra-frequency NR case with RRC_INACTIVE eDRX and positioning SRS

##### A.17.2.2.1.1 Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell reselection requirements specified in clause 5.6A.2.2, when a RedCap UE is in RRC_INACTIVE and configured with eDRX and to transmit SRS for positioning.

##### A.17.2.2.1.2 Test Parameters

The test procedure, supported test configurations, and test parameters in clause A.7.2.2.1.2 apply for this test.

##### A.17.2.2.1.3 Test Requirements

The test requirements in A.7.2.2.1.3 apply for this test.

## A.17.3 RRC_CONNECTED state mobility for RedCap

### A.17.3.1 Handover for RedCap

#### A.17.3.1.1 Intra-frequency handover from FR2 to FR2; unknown target cell for 2 Rx

##### A.17.3.1.1.1 Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 intra frequency handover requirements specified in clause6.1D.1.3.

##### A.17.3.1.1.2 Test Parameters

Supported test configurations are shown in table A.17.3.1.1.2-1. Both handover delay and interruption length are tested by using the parameters in table A.17.3.1.1.2-2, and A.17.3.1.1.2-3.

NR shall send a RRC message implying handover to Cell 2, then UE handover to Cell 2’s intial BWP associated with CD-SSB.The test scenario comprises of carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.17.3.1.1.2-1: Intra-frequency handover from FR2 to FR2 test configurations

| Config | Description |
| --- | --- |
| 1 | Source cell: NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex modeTarget cell: NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.3.1.1.2-2: General test parameters Intra-frequency handover from FR2 to FR2

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 |  |
| Final condition | Active cell |  | Cell 2 |  |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 10 |  |

Table A.17.3.1.1.2-3: Cell specific test parameters for NR FR2-FR2 Intra frequency handover test case

| Parameter |  |  | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| Assumption for UE beamsNote 6 |  |  |  | Rough |  | Rough |  |
| AoA setup |  |  |  | Setup 1 as defined in A.3.15 |  |  |  |
| NR RF Channel Number |  |  |  | 1 |  | 1 |  |
| Duplex mode |  |  |  | TDD |  |  |  |
| TDD configuration |  |  |  | TDDConf.3.1 |  |  |  |
| BWchannel |  |  | MHz | 100: NPRB,c = 66 |  |  |  |
| BWP BW |  |  | MHz | 100: NPRB,c = 66 |  |  |  |
| Data PRBs allocated |  |  |  | 66 |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  |  |  | SR3.1 TDD |  |  |  |
| RMSI CORESET Reference Channel |  |  |  | CR3.1 TDD |  |  |  |
| Control Channel RMC |  |  |  | CCR.3.1 TDD |  |  |  |
| OCNG Patterns |  |  |  | OP. 1 |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |
| SSB Configuration |  |  |  | SSB.3 FR2 |  | SSB. 3 FR2 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 120 |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 120 |  |  |  |
| PRACH configuration |  |  |  | PRACH.1 FR2 |  |  |  |
| TRS configuration |  |  |  | TRS.2.1 TDD |  |  |  |
| PDSCH/PDCCH TCI state |  |  |  | TCI.State.2 |  |  |  |
| BWP configuraiton |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | -104.7 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | -95.7 |  |  |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 6 | -1.8 | -Infinity | 0 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 6 | 6 | -Infinity | 7 |
| IoNote3 |  |  | dBm/BW | -59.7 | -56.7 | -59.7 | -56.7 |
| Propagation condition |  |  | - | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the centre of the quiet zone NOTE 6: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |  |  |

##### A.17.3.1.1.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 232 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 222 ms in the test. Tinterrupt is defined in clause 6.1D.1.3.

This gives a total of 232 ms.

#### A.17.3.1.2 Inter-frequency handover from FR2 to FR2; unknown target cell for 2 Rx

##### A.17.3.1.2.1 Test Purpose and Environment

This test is to verify the requirement for the NR FR2 NCD-SSB to NR FR2 NCD-SSB inter frequency handover requirements specified in clause6.1D.1.3.

##### A.17.3.1.2.2 Test Parameters

Supported test configurations are shown in table A.17.3.1.2.2-1. Both handover delay and interruption length are tested by using the parameters in table A.17.3.1.2.2-2, and A.17.3.1.2.2-3.

NR shall send a RRC message implying handover to Cell 2, then UE handover from Cell 1’s NCD-SSB to Cell 2’s specific RedCap BWP associated with NCD-SSB.The test scenario comprises of carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.17.3.1.2.2-1: Inter-frequency handover from FR2 to FR2 test configurations

| Config | Description |
| --- | --- |
| 1 | Source cell: NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex modeTarget cell: NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.3.1.2.2-2: General test parameters Inter-frequency handover from FR2 to FR2

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 |  |
| Final condition | Active cell |  | Cell 2 |  |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 10 |  |

Table A.17.3.1.2.2-3: Cell specific test parameters for NR FR2-FR2 Inter frequency handover test case

| Parameter |  |  | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| Assumption for UE beamsNote 6 |  |  |  | Rough |  | Rough |  |
| AoA setup |  |  |  | Setup 1as defined in A.3.15 |  |  |  |
| NR RF Channel Number |  |  |  | 1 |  | 2 |  |
| Duplex mode |  |  |  | TDD |  |  |  |
| TDD configuration |  |  |  | TDDConf.3.1 |  |  |  |
| BWchannel |  |  | MHz | 100: NPRB,c = 66 |  |  |  |
| BWP BW |  |  | MHz | 100: NPRB,c = 66 |  |  |  |
| Data PRBs allocated |  |  |  | 66 |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  |  |  | SR.3.1 TDD |  |  |  |
| RMSI CORESET Reference Channel |  |  |  | CR.3.1 TDD |  |  |  |
| Control Channel RMC |  |  |  | CCR.3.1 TDD |  |  |  |
| OCNG Patterns |  |  |  | OP. 1 |  |  |  |
| SMTC Configuration for CD-SSB |  |  |  | SMTC.1 |  |  |  |
| SMTC Configuration for NCD-SSB |  |  |  | SMTC.2 RedCap |  |  |  |
| CD-SSB Configuration |  |  |  | SSB.3 RedCap FR2 |  | SSB.3 RedCap FR2 |  |
| NCD-SSB Configuration |  |  |  | SSB.3 RedCap FR2 Note 7 |  | SSB.3 RedCap FR2 Note 7 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 120 |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 120 |  |  |  |
| PRACH configuration |  |  |  | PRACH.1 FR2 |  |  |  |
| TRS configuration |  |  |  | TRS.2.1 TDD |  |  |  |
| PDSCH/PDCCH TCI state |  |  |  | TCI.State.2 |  |  |  |
| BWP configuraiton |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.3 RedCap Note 8 |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.3 RedCap Note 8 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | -104.7 |  | -104.7 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | -95.7 |  | -95.7 |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 5 | 5 | -Infinity | 5 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 5 | 5 | -Infinity | 5 |
| IoNote3 | Config 1,2 |  | dBm/BW | -60.5 | -60.5 | -66.7 | -60.5 |
| Propagation condition |  |  | - | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 6: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 7: NCD-SSB is configured within dedicated RedCap DL BWP and CD-SSB is configured completely outside the dedicated RedCap DL BWPNOTE 8: The starting PRB index for dedicated DL BWP corresponding to NCD-SSB PRB indexNOTE 9: The starting PRB index for dedicated UL BWP is the same as the dedicated DL BWP corresponding to NCD-SSB PRB index |  |  |  |  |  |  |  |

##### A.17.3.1.2.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2052 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 2042 ms in the test. Tinterrupt is defined in clause 6.1D.1.3.

This gives a total of 2052 ms.

### A.17.3.2 RRC Connection Mobility Control for RedCap

#### A.17.3.2.1 SA: RRC Re-establishment

##### A.17.3.2.1.1 Intra-frequency RRC Re-establishment in FR2

###### A.17.3.2.1.1.1 Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR2 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1B.

The test parameters are given in table A.17.3.2.1.1.1-1, table A.17.3.2.1.1.1-2 and table A.17.3.2.1.1.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure.

Table A.17.3.2.1.1.1-1: Supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.3.2.1.1.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR2

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1 | Cell 1 |  |
|  | Neighbour cells |  | 1 | Cell 2 |  |
| Final condition | Active cell |  | 1 | Cell 2 |  |
| RF Channel Number |  |  | 1 | 1 |  |
| Time offset between cells |  |  | 1 | 3 s | Synchronous cells |
| N310 |  | - | 1 | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1 | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 1 | 0 | Radio link failure timer; T310 is disabled |
| T311 |  | ms | 1 | 5000 | RRC re-establishment timer |
| Access Barring Information |  | - | 1 | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | 1 | SSB.3 FR2 |  |
| SMTC configuration |  |  | 1 | SMTC pattern 1 |  |
| DRX cycle length |  | s | 1 | OFF |  |
| PRACH configuration |  |  | 1 | FR2 PRACH configuration 1 | Table A.3.8.3.1-1 |
| T1 |  | s | 1 | 5 |  |
| T2 |  | s | 1 | 4.84 | Time for the UE to detect RLF(Summation of TEvaluate_out_SSB defined in clause 8.1 in TS 38.133, T310 and the period for UE turns off transmitter defined in clause 8.1.5 in TS 38.133 ) |
| T3 |  | s | 1 | 5 |  |

Table A.17.3.2.1.1.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR2

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Assumption for UE beamsNote 4 |  |  | Rough |  |  | Rough |  |  |
| TDD configuration |  | 1 | TDDConf.3.1 |  |  | TDDConf.3.1 |  |  |
| BWchannel | MHz | 1 | 100: NPRB,c = 66 |  |  | 100: NPRB,c = 66 |  |  |
| Data PRBs allocated |  | 1 | 24 |  |  | 24 |  |  |
| PDSCH RMC configuration |  | 1 | SR.3.1 TDD |  |  | N/A |  |  |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD |  |  | CR.3.1 TDD |  |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 TDD |  |  | CCR.3.1 TDD |  |  |
| TRS configuration |  | 1 | TRS.2.1 TDD |  |  | N/A |  |  |
| PDSCH/PDCCH TCI state |  | 1 | TCI.State.2 |  |  | N/A |  |  |
| OCNG Pattern |  | 1 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1 | SSB |  |  | SSB |  |  |
| AoA setup |  | 1 | Setup 1 defined in clause A.3.15.1 |  |  | Setup 1 defined in clause A.3.15.1 |  |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1 | -0.12 | -infinity | -infinity | -3.46 | 2 | 2 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -104.7 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -95.7 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 4 | -infinity | -infinity | 2 | 2 | 2 |
| SS-RSRP Note3 | dBm/SCS | 1 | -91.7 | -infinity | -infinity | -93.7 | -93.7 | -93.7 |
| Io | dBm/95.04 MHz | 1 | -64.00 | -66.95 | -66.95 | -64.00 | -66.95 | -66.95 |
| Propagation Condition |  | 1 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |  |  |  |

A.17.3.2.1.1.2 Test Requirements

he RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR intra frequency cell shall be less than 5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE: The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

$ T_{UE\_re-establish\_delay}=50 ms+T_{identify\_intra\_NR}+\sum  _{i=1}^{Nfreq-1}T_{identify\_inter\_NR,i}+T_{SI-NR}+T_{PRACH}$

Nfreq = 1

Tidentify_intra_NR = 3520 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 4865 ms, allow 5 s in the test case.

##### A.17.3.2.1.2 Inter-frequency RRC Re-establishment in FR2

###### A.17.3.2.1.2.1 Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR2 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1B.

The test parameters are given in table A.17.3.2.1.2.1-1, table A.17.3.2.1.2.1-2 and table A.17.3.2.1.2.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

Table A.17.3.2.1.2.1-1: Supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.3.2.1.2.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR2

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1 | Cell 1 |  |
|  | Neighbour cells |  | 1 | Cell 2 |  |
| Final condition | Active cell |  | 1 | Cell 2 |  |
| RF Channel Number |  |  | 1 | 1, 2 |  |
| Time offset between cells |  |  | 1 | 3 s | Synchronous cells |
| N310 |  | - | 1 | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1 | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 1 | 0 | Radio link failure timer; T310 is disabled |
| T311 |  | ms | 1 | 5000 | RRC re-establishment timer |
| Access Barring Information |  | - | 1 | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | 1 | SSB.3 FR2 |  |
| SMTC configuration |  |  | 1 | SMTC pattern 1 |  |
| DRX cycle length |  | s | 1 | OFF |  |
| PRACH configuration |  |  | 1 | FR2 PRACH configuration 1 | Table A.3.8.3.1-1 |
| T1 |  | s | 1 | 5 |  |
| T2 |  | s | 1 | 4.84 | Time for the UE to detect RLF(Summation of TEvaluate_out_SSB defined in clause 8.1 in TS 38.133, T310 and the period for UE turns off transmitter defined in clause 8.1.5 in TS 38.133 ) |
| T3 |  | s | 1 | 6 |  |

Table A.17.3.2.1.2.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR2

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Assumption for UE beamsNote 4 |  |  | Rough |  |  | Rough |  |  |
| AoA setup |  | 1 | Setup 3 as specified in clause A.3.15 |  |  |  |  |  |
|  |  |  | AoA1 |  |  | AoA2 |  |  |
| TDD configuration |  | 1 | TDDConf.3.1 |  |  | TDDConf.3.1 |  |  |
| BWchannel | MHz | 1 | 100: NPRB,c = 66 |  |  | 100: NPRB,c = 66 |  |  |
| Data PRBs allocated |  | 1 | 24 |  |  | 24 |  |  |
| PDSCH RMC configuration |  | 1 | SR.3.1 TDD |  |  | N/A |  |  |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD |  |  | CR.3.1 TDD |  |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 TDD |  |  | CCR.3.1 TDD |  |  |
| TRS configuration |  | 1 | TRS.2.1 TDD |  |  | N/A |  |  |
| PDSCH/PDCCH TCI state |  | 1 | TCI.State.2 |  |  | N/A |  |  |
| OCNG Pattern |  | 1 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1 | SSB |  |  | SSB |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -92.1 |  |  | -92.1 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -83.1 |  |  | -83.1 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 0 | -infinity | -infinity | -infinity | -infinity | 0 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot]BB Note 5 | dB | 1 | -1.01 | -infinity | -infinity | -infinity | -infinity | -1.01 |
| SSB_RP Note3 | dBm/SCS | 1 | -83.1 | -infinity | -infinity | -infinity | -infinity | -83.1 |
| Io | dBm/95.04 MHz | 1 | -55.46 | -58.51 | -58.51 | -58.51 | -58.51 | -55.46 |
| Propagation Condition |  | 1 | AWGN |  |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that a constant total transmitted power is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Es/Iot, SSB_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 5: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBS from TS 38.101-2 [19] Table 6.2.1.3-4. |  |  |  |  |  |  |  |  |

A.17.3.2.1.2.2 Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell shall be less than 6 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE: The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

$ T_{UE\_re-establish\_delay}=50 ms+T_{identify\_intra\_NR}+\sum  _{i=1}^{Nfreq-1}T_{identify\_inter\_NR,i}+T_{SI-NR}+T_{PRACH}$

Nfreq = 2

Tidentify_intra_NR = 1600 ms

Tidentify_inter_NR = 2080 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 5025 ms, allow 6 s in the test case.

##### A.17.3.2.1.3 Intra-frequency RRC Re-establishment in FR2 without serving cell timing

###### A.17.3.2.1.3.1 Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR2 without serving cell timing is within the specified limits. These tests will verify the requirements in clause 6.2.1B.

The test parameters are given in table A.17.3.2.1.3.1-1, table A.17.3.2.1.3.1-2 and table A.17.3.2.1.3.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.17.3.2.1.3.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.3.2.1.3.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR2

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1 | Cell 1 |  |
|  | Neighbour cells |  | 1 | Cell 2 |  |
| Final condition | Active cell |  | 1 | Cell 2 |  |
| RF Channel Number |  |  | 1 | 1 |  |
| Time offset between cells |  |  | 1 | 3 s | Synchronous cells |
| N310 |  | - | 1 | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1 | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 1 | 6000 | Radio link failure timer configured by RLF-TimersAndConstants |
| T311 |  | ms | 1 | 5000 | RRC re-establishment timer |
| Access Barring Information |  | - | 1 | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | 1 | SSB.3 FR2 |  |
| SMTC configuration |  |  | 1 | SMTC pattern 1 |  |
| DRX cycle length |  | s | 1 | OFF |  |
| PRACH configuration |  |  | 1 | FR2 PRACH configuration 1 | Table A.3.8.3.1-1 |
| T1 |  | s | 1 | 5 |  |
| T2 |  | s | 1 | 10.84 | Time for the UE to detect RLF(Summation of TEvaluate_out_SSB defined in clause 8.1B in TS 38.133, T310 and the period for UE turns off transmitter defined in clause 8.1B.5 in TS 38.133 ) |
| T3 |  | s | 1 | 5 |  |

Table A.17.3.2.1.3.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR2

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Assumption for UE beamsNote 4 |  |  | Rough |  |  | Rough |  |  |
| TDD configuration |  | 1 | TDDConf.3.1 |  |  | TDDConf.3.1 |  |  |
| PDSCH RMC configuration |  | 1 | SR.3.1 TDD |  |  | N/A |  |  |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 FDD |  |  | CR.3.1 FDD |  |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 FDD |  |  | CCR.3.1 FDD |  |  |
| TRS configuration |  | 1 | TRS.2.1 TDD |  |  | N/A |  |  |
| PDSCH/PDCCH TCI state |  | 1 | TCI.State.2 |  |  | N/A |  |  |
| OCNG Pattern |  | 1 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1 | SSB |  |  | SSB |  |  |
| AoA setup |  | 1 | Setup 1 defined in clause A.3.15.1 |  |  | Setup 1 defined in clause A.3.15.1 |  |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1 | 5 | -infinity | -infinity | -infinity | -infinity | 5 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -104.7 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -95.7 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 5 | -infinity | -infinity | -infinity | -infinity | 5 |
| SS-RSRP Note3 | dBm/SCS | 1 | -90.7 | -infinity | -infinity | -infinity | -infinity | -90.7 |
| Io | dBm/95.04 MHz | 1 | -60.52 | -66.71 | -60.52 | -60.52 | -66.71 | -60.52 |
| Propagation Condition |  | 1 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. NOTE 4: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |  |  |  |

###### A.17.3.2.1.3.2 Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR intra frequency cell without serving cell timing shall be less than 5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE: The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

$ T_{UE\_re-establish\_delay}=50ms+T_{identify\_intra\_NR}+\sum  _{i=1}^{Nfreq-1}T_{identify\_inter\_NR,i}+T_{SI-NR}+T_{PRACH}$

Nfreq = 1

Tidentify_intra_NR = 3520 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 [2] for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 4865 ms, allow 5 s in the test case.


#### A.17.3.2.2 Random Access

##### A.17.3.2.2.1 4-step RA type contention based random access test in FR2 for NR Standalone

###### A.17.3.2.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause6.2.2B.2 and clause7.1A.2 in an AWGN model.

For this test one cell is used, with the configuration of Cell 1 configured as PCell in FR2. Supported test parameters are shown in table A.17.3.2.2.1.1-1. UE capable of SA with PCell in FR2 needs to be tested by using the parameters in table A.17.3.2.2.1.1-2 and table A.17.3.2.2.1.1-3.

Table A.17.3.2.2.1.1-1: Supported test configurations for contention based random access test in FR2 for NR Standalone

| Config | Description |
| --- | --- |
| 1 | NR PSCell 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.3.2.2.1.1-2: General test parameters for contention based random access test in FR2 for NR Standalone

| Parameter |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- |
| SSB Configuration | Config 1 |  | SSB.1 FR2 | As defined in A.3.10 |
| CSI-RS for tracking | Config 1 |  | TRS.2.1 TDD |  |
| Duplex Mode for Cell 1 | Config 1 |  | TDD |  |
| TDD Configuration | Config 1 |  | TDDConf.3.1 | As defined in A.3.1.4 |
| BWchannel | Config 1 | MHz | 100: NPRB,c = 66 |  |
| Data PRBs allocated | Config 1 |  | 24 |  |
| OCNG Pattern Note 1 |  |  | OCNG pattern 1 | As defined in A.3.2.1. |
| PDSCH Reference Channel Note 2 | Config 1 |  | SR.3.1 TDD | As defined in A.3.1.1. |
| RMSI CORESET Reference Channel | Config 1 |  | CR.3.1 TDD | As defined in A.3.1.2 |
| NR RF Channel Number |  |  | 1 |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  | dB |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  | dB |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  | dB |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  | dB |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  | dB |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  | dB |  |  |
| ss-PBCH-BlockPower |  | dBm/ SCS | +20 +ΔUL | As defined in TS 38.331 [2].ΔUL is derived from the uplink calibration process Note 3 |
| Configured UE transmitted power (![](media_svg/image7.svg) [公式≈: ^{P}CMAX,f,c]) |  | dBm | maximum value configurable for certain power class | As defined in clause 6.2.4 in TS 38.101-2 [19] |
| PRACH Configuration |  |  | FR2 PRACH configuration 1 | As defined in A.3.8B.3, with exceptions as defined below |
| rsrp-ThresholdSSB |  | dBm | RSRP_69 +ΔDL | RSRP_69 corresponds to -88 dBm. ΔDL is derived from the downlink calibration process Note 4 |
| preambleReceivedTargetPower |  | dBm | -100 | As defined in TS 38.331 [2] |
| NOTE 1: OCNG shall be used such that a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required.NOTE 3: The ΔUL value is calculated as -ROUND(PPRACH0 -1), where PPRACH0 is the measured first PRACH power with -80.6 dBm/SCS applied, preambleReceivedTargetPower = -100 dBm and ss-PBCH-BlockPower = 20 dBm. These values are used during the uplink calibration process carried out before the test case is run, with the UE configured to send PRACH.NOTE 4: The ΔDL value is calculated as (RSRP_REP – RSRP_76), where RSRP_REP is the SS-RSRP Reported value in table 10.1.6.1-1 with -80.6 dBm/SCS applied. These values are used during the downlink calibration process carried out before the test case is run, with the UE configured to report SS-RSRP. For a Reported value RSRP_x, x is treated as a positive integer value. |  |  |  |  |

Table A.17.3.2.2.1.1-3: OTA-related test parameters for contention based random access test in FR2 for NR Standalone

| Parameter |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- |
| AoA setup |  |  | Setup 1 | As defined in clause A.3.15.1 |
| Assumption for UE beamsNote 3 |  |  | Rough |  |
| SSB with index 0 | Es Note1 | dBm/SCS | -80.6 | Power of SSB with index 0 is set to be above configured rsrp-ThresholdSSB |
|  | SSB_RP | dBm/SCS | -80.6 |  |
|  | Es/IotBB | dB | 21.09 |  |
|  | Io | dBm/95.04 MHz | -56.01 | Io in symbols containing SSB index 0 |
| SSB with index 1 | Es Note1 | dBm/SCS | -95.0 | Power of SSB with index 1 is set to be below configured rsrp-ThresholdSSB |
|  | SSB_RP | dBm/SCS | -95.0 |  |
|  | Es/IotBB | dB | 6.69 |  |
|  | Io | dBm/95.04 MHz | -70.41 | Io in symbols containing SSB index 1 |
| Propagation Condition |  | - | No external noise (Note 4) |  |
| NOTE 1: No articial noise is applied in this test.NOTE 2: Void.NOTE 3: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 4: The downlink connection between the System Simulator and the UE is without Additive White Gaussian Noise, and has no fading or multipath effects as specified in TS 38.521-2 B.0 [38]. |  |  |  |  |

###### A.17.3.2.2.1.2 Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.17.3.2.2.1.2.1 Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2.2.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.17.3.2.2.1.2.2 Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.17.3.2.2.1.2.3 No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 2 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.17.3.2.2.1.2.4 Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2.2.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

A.17.3.2.2.1.2.5 Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.17.3.2.2.1.2.6 Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.17.3.2.2.1.2.7 Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

##### A.17.3.2.2.2 4-step RA type non-contention based random access test in FR2 for NR Standalone

###### A.17.3.2.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause6.2.2.2 and clause7.1.2 in an AWGN model.

For this test one cell is used, with the configuration of Cell 1 configured as PCell in FR2. Supported test parameters are shown in table A.17.3.2.2.2.1-1. UE capable of SA with PCell or SCell in FR2 needs to be tested by using the parameters in table A.17.3.2.2.2.1-2 and table A.17.3.2.2.2.1-3 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2). Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

Table A.17.3.2.2.2.1-1: Supported test configurations for non-contention based random access test in FR2 for NR Standalone

| Config | Description |
| --- | --- |
| 1 | NR PSCell 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.3.2.2.2.1-2: General test parameters for non-contention based random access test in FR2 for NR Standalone

| Parameter |  | Unit | Test-1 | Test-2 | Comments |
| --- | --- | --- | --- | --- | --- |
| SSB Configuration | Config 1 |  | SSB.1 FR2 | SSB.1 FR2 | As defined in A.3.10 |
| CSI-RS for tracking | Config 1 |  | TRS.2.1 TDD | TRS.2.1 TDD |  |
| CSI-RS Configuration | Config 1 |  | N/A | CSI-RS.3.1 TDD | As defined in A. 3.14.2 |
| Duplex Mode for Cell 2 | Config 1 |  | TDD | TDD |  |
| TDD Configuration | Config 1 |  | TDDConf.3.1 | TDDConf.3.1 |  |
| BWchannel | Config 1 | MHz | 100: NPRB,c = 66 | 100: NPRB,c = 66 |  |
| Data PRBs allocated | Config 1 |  | 24 | 24 |  |
| OCNG Pattern Note 1 |  |  | OP.3 | OP.3 | As defined in A.3.2.1. |
| PDSCH Reference Channel Note 2 | Config 1 |  | SR3.1 TDD | SR3.1 TDD | As defined in A.3.1.1. |
| NR RF Channel Number |  |  | 1 | 1 |  |
| EPRE ratio of PSS to SSS |  | dB | 0 | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  | dB |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  | dB |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  | dB |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  | dB |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  | dB |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  | dB |  |  |  |
| ss-PBCH-BlockPower |  | dBm/ SCS | +20 +ΔUL | +20 +ΔUL | As defined in TS 38.331 [2].ΔUL is derived from the uplink calibration process Note 3 |
| Configured UE transmitted power (![](media_svg/image7.svg) [公式≈: ^{P}CMAX,f,c]) |  | dBm | maximum value configurable for certain power class | maximum value configurable for certain power class | As defined in clause 6.2.4 in TS 38.101-2 [19] |
| PRACH Configuration |  |  | FR2 PRACH configuration 2 | FR2 PRACH configuration 3 | As defined in A.3.8.3, with exceptions as defined below. |
| rsrp-ThresholdSSB |  | dBm | RSRP_69 +ΔDL | RSRP_69 +ΔDL | RSRP_69 corresponds to -88 dBm. ΔDL is derived from the downlink calibration process Note 4 |
| preambleReceivedTargetPower |  | dBm | -100 | -100 | As defined in TS 38.331 [2] |
| NOTE 1: OCNG shall be used such that a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required.NOTE 3: The ΔUL value is calculated as -ROUND(PPRACH0 -1), where PPRACH0 is the measured first PRACH power with -80.6 dBm/SCS applied, preambleReceivedTargetPower = -100 dBm and ss-PBCH-BlockPower = 20 dBm. These values are used during the uplink calibration process carried out before the test case is run, with the UE configured to send PRACH.NOTE 4: The ΔDL value is calculated as (RSRP_REP – RSRP_76), where RSRP_REP is the SS-RSRP Reported value in table 10.1.6.1-1 with -80.6 dBm/SCS applied. These values are used during the downlink calibration process carried out before the test case is run, with the UE configured to report SS-RSRP. For a Reported value RSRP_x, x is treated as a positive integer value. |  |  |  |  |  |

Table A.17.3.2.2.2.1-3: OTA-related test parameters for non-contention based random access test in FR2 for NR Standalone

| Parameter |  | Unit | Test-1 | Test-2 | Comments |
| --- | --- | --- | --- | --- | --- |
| AoA setup |  |  | Setup 1 | Setup 1 | As defined in clause A.3.15.1 |
| Assumption for UE beamsNote 3 |  |  | Rough | Rough |  |
| SSB with index 0 | Es Note1 | dBm/SCS | -80.6 | -80.6 | Power of SSB with index 0 is set to be above configured rsrp-ThresholdSSB |
|  | SSB_RP | dBm/SCS | -80.6 | -80.6 |  |
|  | Es/IotBB | dB | 21.09 | 21.09 |  |
|  | Io | dBm/95.04 MHz | -56.01 | -56.01 | Io in symbols containing SSB index 0 |
| SSB with index 1 | Es Note1 | dBm/SCS | -95.0 | -95.0 | Power of SSB with index 1 is set to be below configured rsrp-ThresholdSSB |
|  | SSB_RP | dBm/SCS | -95.0 | -95.0 |  |
|  | Es/IotBB | dB | 6.69 | 6.69 |  |
|  | Io | dBm/95.04 MHz | -70.41 | -70.41 | Io in symbols containing SSB index 1 |
| Propagation Condition |  | - | No external noise (Note 4) | No external noise (Note 4) |  |
| NOTE 1: No articial noise is applied in this test.NOTE 2: void. NOTE 3: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 4: The downlink connection between the System Simulator and the UE is without Additive White Gaussian Noise, and has no fading or multipath effects as specified in TS 38.521-2 B.0 [38]. |  |  |  |  |  |

###### A.17.3.2.2.2.2 Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.17.3.2.2.2.2.1 SSB-based Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2.2.2.2.1 for SSB-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.7.3.2.2.2.2.2 CSI-RS-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2.2.2.1 for CSI-RS-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with CSI-RSs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the CSI-RS configured.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the CSI-RS configured, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-OccasionList.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.17.3.2.2.2.2.3 Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.17.3.2.2.2.2.4 No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 2 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

##### A.17.3.2.2.3 2-step RA type contention based random access test in FR2 for NR Standalone

###### A.17.3.2.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the 2-step RA type random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits. This test will verify the requirements in clause6.2.2B.2 and clause7.1A.2 in an AWGN model.

For this test one cell is used, with the configuration of Cell 1 configured as PCell or SCell in FR2. Supported test parameters are shown in table A.17.3.2.2.3.1-1. UE capable of SA with PCell or SCell in FR2 needs to be tested by using the parameters in table A.17.3.2.2.3.1-2 and table A.17.3.2.2.3.1-3.

Table A.17.3.2.2.3.1-1: Supported test configurations for 2-step RA type contention based random access test in FR2 for NR Standalone

| Config | Description |
| --- | --- |
| 1 | NR PSCell/SCell 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.3.2.2.3.1-2: General test parameters for 2-step RA type contention based random access test in FR2 for NR Standalone

| Parameter |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- |
| SSB Configuration | Config 1 |  | SSB.3 FR2 | As defined in A.3.10 |
| Duplex Mode for Cell 1 | Config 1 |  | TDD |  |
| TDD Configuration | Config 1 |  | TDDConf.3.1 | As defined in A.3.1.4 |
| BWchannel | Config 1 | MHz | 100: NPRB,c = 24 |  |
| OCNG Pattern Note 1 |  |  | OCNG pattern 1 | As defined in A.3.2.1. |
| PDSCH Reference Channel Note 2 | Config 1 |  | SR.3.1 TDD | As defined in A.3.1.1. |
| RMSI CORESET Reference Channel | Config 1 |  | CR.3.1 TDD | As defined in A.3.1.2 |
| NR RF Channel Number |  |  | 1 |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  | dB |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  | dB |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  | dB |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  | dB |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  | dB |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  | dB |  |  |
| ss-PBCH-BlockPower |  | dBm/ SCS | +20 +ΔUL | As defined in TS 38.331 [2].ΔUL is derived from the uplink calibration process Note 3 |
| Configured UE transmitted power (![](media_svg/image7.svg) [公式≈: ^{P}CMAX,f,c]) |  | dBm | maximum value configurable for certain power class | As defined in clause 6.2.4 in TS 38.101-2 [19] |
| MsgA Configuration |  |  | FR2 MsgA configuration 1 | As defined in A.3.20.3, with exceptions as defined below |
| msgA-RSRP-ThresholdSSB |  | dBm | RSRP_69 +ΔDL | RSRP_69 corresponds to -88 dBm. ΔDL is derived from the downlink calibration process Note 4 |
| preambleReceivedTargetPower |  | dBm | -100 | As defined in TS 38.331 [2] |
| NOTE 1: OCNG shall be used such that a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required.NOTE 3: The ΔUL value is calculated as -ROUND(PMsgA0 -1), where PMsgA0 is the measured first MsgA PRACH power with -80.6 dBm/SCS applied, msgA-PreambleReceivedTargetPower = -100 dBm and ss-PBCH-BlockPower = 20 dBm. These values are used during the uplink calibration process carried out before the test case is run, with the UE configured to send MsgA.NOTE 4: The ΔDL value is calculated as (RSRP_REP – RSRP_76), where RSRP_REP is the SS-RSRP Reported value in table 10.1.6.1-1 with -80.6 dBm/SCS applied. These values are used during the downlink calibration process carried out before the test case is run, with the UE configured to report SS-RSRP. For a Reported value RSRP_x, x is treated as a positive integer value. |  |  |  |  |

Table A.17.3.2.2.3.1-3: OTA-related test parameters for 2-step RA type contention based random access test in FR2 for NR Standalone

| Parameter |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- |
| AoA setup |  |  | Setup 2b | As defined in A.3.15.2 |
| Assumption for UE beamsNote 2 |  |  | Rough |  |
| SSB with index 0 | Es Note1 | dBm/SCS | -80.6 | Power of SSB with index 0 is set to be above configured msgA-RSRP-ThresholdSSB |
|  | SSB_RP | dBm/SCS | -80.6 |  |
|  | Es/IotBB | dB | 21.09 |  |
|  | Io | dBm/95.04 MHz | -56.01 | Io in symbols containing SSB index 0 |
| SSB with index 1 | Es Note1 | dBm/SCS | -95.0 | Power of SSB with index 1 is set to be below configured msgA-RSRP-ThresholdSSB |
|  | SSB_RP | dBm/SCS | -95.0 |  |
|  | Es/IotBB | dB | 6.69 |  |
|  | Io | dBm/95.04 MHz | -70.41 | Io in symbols containing SSB index 1 |
| Propagation Condition |  | - | No external noise (Note 3) |  |
| NOTE 1: No articial noise is applied in this test.NOTE 2: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 3: The downlink connection between the System Simulator and the UE is without Additive White Gaussian Noise, and has no fading or multipath effects as specified in TS 38.521-2 B.0 [38]. |  |  |  |  |

###### A.17.3.2.2.3.2 Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.17.3.2.2.3.2.1 MsgA Transmission

To test the UE behavior specified in clause 6.2.2.3.1.1 the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured msgA-RSRP-ThresholdSSB.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first MsgA preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

A.17.3.2.2.3.2.2 MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.1.2 the System Simulator shall transmit a MsgB containing a fallbackRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit MsgA with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB’s contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first MsgA PRACH shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

A.17.3.2.2.3.2.3 No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.1.3 the System Simulator shall transmit a MsgB containing a fallbackRAR message and Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 2 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if no MsgB is received within the MsgB Response window.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in Clause 6.2.2.3. The power of the first MsgA PRACH shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

##### A.17.3.2.2.4 2-step RA type non-contention based random access test in FR2 for NR Standalone

###### A.17.3.2.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits. This test will verify the requirements in clause6.2.2B.2 and clause7.1A.2 in an AWGN model.

For this test one cell is used, with the configuration of Cell 1 configured as PCell or SCell in FR2. Supported test parameters are shown in table A.17.3.2.2.4.1-1. UE capable of SA with PCell or SCell in FR2 needs to be tested by using the parameters in table A.17.3.2.2.4.1-2 and table A.17.3.2.2.4.1-3.

Table A.17.3.2.2.4.1-1: Supported test configurations for non-contention based random access test for 2-step RA type in FR2 for NR Standalone

| Config | Description |
| --- | --- |
| 1 | NR PSCell/SCell 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.3.2.2.4.1-2: General test parameters for non-contention based random access test for 2-step RA type in FR2 for NR Standalone

| Parameter |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- |
| SSB Configuration | Config 1 |  | SSB.3 FR2 | As defined in A.3.10 |
| Duplex Mode for Cell 2 | Config 1 |  | TDD |  |
| TDD Configuration | Config 1 |  | TDDConf.3.1 |  |
| BWchannel | Config 1 | MHz | 100: NPRB,c = 24 |  |
| OCNG Pattern Note 1 |  |  | OP.3 | As defined in A.3.2.1. |
| PDSCH Reference Channel Note 2 | Config 1 |  | SR3.1 TDD | As defined in A.3.1.1. |
| NR RF Channel Number |  |  | 1 |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  | dB |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  | dB |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  | dB |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  | dB |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  | dB |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  | dB |  |  |
| ss-PBCH-BlockPower |  | dBm/ SCS | +20 +ΔUL | As defined in TS 38.331 [2].ΔUL is derived from the uplink calibration process Note 3 |
| Configured UE transmitted power (PCMAX,f,c) |  | dBm | maximum value configurable for certain power class | As defined in clause 6.2.4 in TS 38.101-2 [19] |
| MsgA Configuration |  |  | FR2 MsgA configuration 2 | As defined in A.3.20.3, with exceptions as defined below. |
| msgA-RSRP-ThresholdSSB |  | dBm | RSRP_69 +ΔDL | RSRP_69 corresponds to -88 dBm. ΔDL is derived from the downlink calibration process Note 4 |
| msgA-PreambleReceivedTargetPower |  | dBm | -100 | As defined in TS 38.331 [2] |
| NOTE 1: OCNG shall be used such that a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required.NOTE 3: The ΔUL value is calculated as -ROUND(PMsgA0 -1), where PMsgA0 is the measured first MsgA PRACH power with -80.6 dBm/SCS applied, msgA-PreambleReceivedTargetPower = -100 dBm and ss-PBCH-BlockPower = 20 dBm. These values are used during the uplink calibration process carried out before the test case is run, with the UE configured to send MsgA.NOTE 4: The ΔDL value is calculated as (RSRP_REP – RSRP_76), where RSRP_REP is the SS-RSRP Reported value in table 10.1.6.1-1 with -80.6 dBm/SCS applied. These values are used during the downlink calibration process carried out before the test case is run, with the UE configured to report SS-RSRP. For a Reported value RSRP_x, x is treated as a positive integer value. |  |  |  |  |

Table A.17.3.2.2.4.1-3: OTA-related test parameters for non-contention based random access test for 2-step RA type in FR2 for NR Standalone

| Parameter |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- |
| AoA setup |  |  | Setup 1 | As defined in clause A.3.15.1 |
| Assumption for UE beams Note 2 |  |  | Rough |  |
| SSB with index 0 | Es Note1 | dBm/SCS | -80.6 | Power of SSB with index 0 is set to be above configured msgA-RSRP-ThresholdSSB |
|  | SSB_RP | dBm/SCS | -80.6 |  |
|  | Es/IotBB | dB | 21.09 |  |
|  | Io | dBm/95.04 MHz | -56.01 | Io in symbols containing SSB index 0 |
| SSB with index 1 | Es Note1 | dBm/SCS | -95.0 | Power of SSB with index 1 is set to be below configured msgA-RSRP-ThresholdSSB |
|  | SSB_RP | dBm/SCS | -95.0 |  |
|  | Es/IotBB | dB | 6.69 |  |
|  | Io | dBm/95.04 MHz | -70.41 | Io in symbols containing SSB index 1 |
| Propagation Condition |  | - | No external noise (Note 3) |  |
| NOTE 1: No artificial noise is applied in this test.NOTE 2: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 3: The downlink connection between the System Simulator and the UE is without Additive White Gaussian Noise, and has no fading or multipath effects as specified in TS 38.521-2 B.0 [38]. |  |  |  |  |

###### A.17.3.2.2.4.2 Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.17.3.2.2.4.2.1 MsgA Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2.3.2.1 for MsgA transmission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the MsgA which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the MsgA on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given first by the msgA-SSB-SharedRO-MaskIndex if configured, or next by the ra-ssb-OccasionMaskIndex if configured.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

A.17.3.2.2.4.2.2 MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.2 the System Simulator shall transmit a MsgB containing a successRAR MAC subPDU corresponding to the transmitted Random Access Preamble after 3 MsgA transmissions have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB if the MsgB contains a successRAR MAC subPDU corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA transmission power if all received Random Access Response Reception has not been considered as successful.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

A.17.3.2.2.4.2.3 No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.3 the System Simulator shall transmit a MsgB corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 2 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA transmission power when the backoff time expires if no MsgB is received within the MsgB Response window configured in RACH-ConfigGenericTwoStepRA.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

#### A.17.3.2.3 SA: RRC Connection Release with Redirection

##### A.17.3.2.3.1 Redirection from NR in FR2 to NR in FR2

###### A.17.3.2.3.1.1 Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements specified in clause 6.2.3A.2.1.

###### A.17.3.2.3.1.2 Test Parameters

Supported test configurations are shown in table A.17.3.2.3.1.2-1. The time delay is tested by using the parameters in table A.17.3.2.3.1.2-2, and A.17.3.2.3.1.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.17.3.2.3.1.2-1: Redirection from NR to NR test configurations

| Config | Description |
| --- | --- |
| 1 | Source cell: NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex modeTarget cell: NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.3.2.3.1.2-2: General test parameters for Redirection from NR to NR test case

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 |  |
| Final condition | Active cell |  | Cell 2 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 3.2 |  |

Table A.17.3.2.3.1.2-3: Cell specific test parameters for Redirection from NR to NR test case

| Parameter |  |  | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| Assumption for UE beamsNote 6 |  |  |  | Rough |  | Rough |  |
| AoA setup |  |  |  | Setup 1as defined in A.3.15 |  |  |  |
| NR RF Channel Number |  |  |  | 1 |  | 2 |  |
| Duplex mode |  |  |  | TDD |  |  |  |
| TDD configuration |  |  |  | TDDConf.3.1 |  |  |  |
| BWchannel |  |  | MHz | 100: NPRB,c = 66 |  |  |  |
| BWP BW |  |  | MHz | 100: NPRB,c = 66 |  |  |  |
| Data PRBs allocated |  |  |  | 66 |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  |  |  | SR.3.1 TDD |  |  |  |
| RMSI CORESET Reference Channel |  |  |  | CR.3.1 TDD |  |  |  |
| Control Channel RMC |  |  |  | CCR.3.1 TDD |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SMTC configuration |  |  |  | SMTC.1 |  |  |  |
| SSB Configuration |  |  |  | SSB.3 FR2 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 120 |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 120 |  |  |  |
| PRACH configuration |  |  |  | PRACH.1 FR2 |  |  |  |
| TRS configuration |  |  |  | TRS.2.1 TDD |  |  |  |
| PDSCH/PDCCH TCI state |  |  |  | TCI.State.2 |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | -104.7 |  | -104.7 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | -95.7 |  | -95.7 |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 5 | 5 | -Infinity | 5 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 5 | 5 | -Infinity | 5 |
| IoNote3 |  |  | dBm/BW | -60.5 | -60.5 | -66.7 | -60.5 |
| Propagation condition |  |  | - | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 6: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |  |  |

###### A.17.3.2.3.1.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 3160 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE: The redirection delay can be expressed as:

Tconnection_release_redirect_NR = TRRC_procedure_delay + Tidentify-NR + TSI-NR + TRACH,

where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR = 1760 ms in the test.

TSI-NR = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH = 10 ms in the test.

This gives a total of 3160 ms.

## A.17.4 Timing

### A.17.4.1 UE transmit timing

#### A.17.4.1.1 NR UE Transmit Timing Test for FR2

##### A.17.4.1.1.1 Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeb and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1.2.

Supported test configurations are shown in table A.17.4.1.1.1-1.

Table A.17.4.1.1.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | NR TDD, SSB SCS 240 kHz, data SCS 120 kHz, BW 100 MHz |

For this test a single NR cell is used. Tables A.17.4.1.1.1-2 and A.17.4.1.1.1-2A define the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.17.4.1.1.1-3.

Table A.17.4.1.1.1-2: Cell Specific Test Parameters for UL Transmit Timing test

| Parameter | Unit | Config |  | Test1 |  |  | Test2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SSB ARFCN |  | 1 |  | Freq1 |  |  | Freq1 |  |
| TDD configuration |  | 1 |  | TDDConf.3.1 |  |  |  |  |
| BWchannel | MHz | 1 |  | 100: NPRB,c = 66 |  |  |  |  |
| Data PRBs allocated |  | 1 |  | 66 |  |  |  |  |
| Initial BWP Configuration |  | 1 |  | DLBWP.0.1ULBWP.0.1 |  |  |  |  |
| Dedicated BWP Configuration |  | 1 |  | DLBWP.1.1ULBWP.1.1 |  |  |  |  |
| TRS Configuration |  | 1 |  | TRS.2.1 TDD |  |  |  |  |
| PDSCH/PDCCH TCI state |  | 1 |  | TCI.State.2 |  |  |  |  |
| DRX Cycle | ms | 1 |  | N/A |  |  | DRX.8Note5 |  |
| PDSCH Reference measurement channel |  | 1 |  | SR.3. 3 TDD |  |  |  |  |
| RMSI CORESET Reference Channel |  | 1 |  | CR.3. 2 TDD |  |  |  |  |
| Dedicated CORESET Reference Channel |  | 1 |  | CCR.3. 7 TDD |  |  |  |  |
| OCNG Patterns |  | 1 |  | OP.1 |  |  |  |  |
| SSB Configuration |  | 1 |  | SSB.4 FR2 |  |  |  |  |
| SMTC Configuration |  | 1 |  | SMTC.1 |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1 |  | 120 |  |  |  |  |
| EPRE ratio of PSS to SSS | dB | 1 | 0 |  |  | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| Propagation condition |  | 1 | AWGN |  |  |  |  |  |
| SRS Config |  | 1 | SRSConf.1Note6 |  | SRSConf.2Note6 |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: VoidNOTE 3: VoidNOTE 4: VoidNOTE 5: DRX related parameters are given in table A.3.3.8-1NOTE 6: SRS configs are given in table A.17.4.1.1.1-3 |  |  |  |  |  |  |  |  |

Table A.17.4.1.1.1-2A: OTA related test parameters

| Parameter | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |
| Assumption for UE beamsNote 6 |  | Fine |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15 kHzNote4 | -112 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote3 | -100 |  |
| ![](media_svg/image8.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 4 |  |
| SS-RSRPNote2 | dBm/SCS Note4 | -96 |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 4 |  |
| IoNote2 | dBm/95.04 MHz Note4 | -68.5 |  |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: SS B_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: VoidNOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 6: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |

Table A.17.4.1.1.1-3: SRS Configuration for Timing Accuracy Test

|  | Field | SRSConf.1 | SRSConf.2 | Comments |
| --- | --- | --- | --- | --- |
| SRS-ResourceSet | srs-ResourceSetId | 0 | 0 |  |
|  | srs-ResourceIdList | 0 | 0 |  |
|  | resourceType | Periodic | Periodic |  |
|  | Usage | Codebook | Codebook |  |
| SRS-Resource | SRS-ResourceId | 0 | 0 |  |
|  | nrofSRS-Ports | Port1 | Port1 |  |
|  | transmissionComb | n2 | n2 |  |
|  | combOffset-n2 | 0 | 0 |  |
|  | cyclicShift-n2 | 0 | 0 |  |
|  | resourceMappingstartPosition | 0 | 0 |  |
|  | resourceMappingnrofSymbols | n1 | n1 |  |
|  | resourceMappingrepetitionFactor | n1 | n1 |  |
|  | freqDomainPosition | 0 | 0 |  |
|  | freqDomainShift | 0 | 0 |  |
|  | freqHoppingc-SRS | 17 | 17 | Matches NPRB,c |
|  | freqHoppingb-SRS | 0 | 0 |  |
|  | freqHoppingb-hop | 0 | 0 |  |
|  | groupOrSequenceHopping | Neither | Neither |  |
|  | resourceType | Periodic | Periodic |  |
|  | periodicityAndOffset-p | sl1, 0 | sl2560, 4 | Offset to align with DRX periodicity |
|  | sequenceId | 0 | 0 | Any 10 bit number |

Table A.17.4.1.1.1-4: Void

##### A.17.4.1.1.2 Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test:

1) Setup NR PCell according to parameters given in table A.17.4.1.1.1-1.

2) After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB.

a. The NTA offset value (in Tc units) is 13792

b. The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3) The test system shall adjust the timing of the DL path by values given in table A.17.4.1.1.2-1

Table A.17.4.1.1.2-1 Adjustment Value for DL Timing

| SCS of SSB signals (kHz) | Adjustment Value |  |
| --- | --- | --- |
|  | Test1 | Test2 |
| 240 | +8*64Tc | +4*64Tc |

4) The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 Table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first detected path (in time) of DL SSB.  Skip this step for test 2 with DRX confiured.

5) The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

### A.17.4.2 UE timer accuracy

### A.17.4.3 Timing advance

#### A.17.4.3.1 SA FR2 timing advance adjustment accuracy

##### A.17.4.3.1.1 Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3A.

##### A.17.4.3.1.2 Test Parameters

Supported test configurations are shown in table A.17.4.3.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.17.4.3.1.2-2, A.17.4.3.1.2-3 and A.17.4.3.1.2-4.

In all test cases, single cell is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.17.4.3.1.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.17.4.3.1.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause7.3.2.1, the UE adjusts its uplink timing at slot n+k for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.17.4.3.1.2-1: Timing advance supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.4.3.1.2-2: General test parameters for timing advance

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| RF channel number |  | 1 |  |
| Initial DL BWP |  | DLBWP.0.1 | As specified in table A.3.9.2.1-1 |
| Dedicated DL BWP |  | DLBWP.1.1 | As specified in table A.3.9.2.2-1 |
| Initial UL BWP |  | ULBWP.0.1 | As specified in table A.3.9.3.1-1 |
| Dedicated UL BWP |  | ULBWP.1.1 | As specified in table A.3.9.3.2-1 |
| Timing Advance Command (TA) value during T1 |  | 31 | NTA_new = NTA_old  for the purpose of establishing a reference value from which the timing advance adjustment accuracy can be measured during T2 |
| Timing Advance Command (TA) value during T2 |  | 39 | For 120 kHz SCS NTA_new = NTA_old  + 1024*Tc (based on equation in clause 4.2 of TS 38.213 [3]) |
| T1 | s | 5 |  |
| T2 | s | 5 |  |

Table A.17.4.3.1.2-3: Cell specific test parameters for timing advance

| Parameter | Unit | Test1 |  |
| --- | --- | --- | --- |
|  |  | T1 | T2 |
| Duplex mode |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  |
| BWchannel | MHz | 100: NPRB,c = 66 |  |
| BWP BW | MHz | 100: NPRB,c = 66 |  |
| DRX Cycle | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  | SR.3.1 TDD |  |
| CORESET Reference Channel |  | CR.3.1 TDD |  |
| OCNG Patterns |  | OP.1 |  |
| TRS configuration |  | TRS.2.1 TDD |  |
| PDSCH/PDCCH TCI state |  | TCI.State.2 |  |
| SMTC configuration |  | SMTC.1 |  |
| SSB Configuration |  | SSB.1 FR2 |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 |  |
| PUCCH/PUSCH subcarrier spacing | kHz | 120 |  |
| EPRE ratio of PSS to SSS | dB | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |
| Propagation condition | - | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the centre of the quiet zone |  |  |  |

Table A.17.4.3.1.2-3A: OTA related test parameters

| Parameter | Unit | Test 1 |  |
| --- | --- | --- | --- |
|  |  | T1 | T2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |
| Assumption for UE beamsNote 6 |  | Fine |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15 kHzNote4 | -112 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote3 | -103 |  |
| ![](media_svg/image8.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 4 |  |
| SS-RSRPNote2 | dBm/SCS Note4 | -99 |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 4 |  |
| IoNote2 | dBm/95.04 MHz Note4 | -68.5 |  |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 6: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |

Table A.17.4.3.1.2-4: Sounding Reference Symbol Configuration for timing advance

| Field | Value | Comment |
| --- | --- | --- |
| c-SRS | 16 | Frequency hopping is disabled |
| b-SRS | 0 |  |
| b-hop | 0 |  |
| freqDomainPosition | 0 | Frequency domain position of SRS |
| freqDomainShift | 0 |  |
| groupOrSequenceHopping | neither | No group or sequence hopping |
| SRS-PeriodicityAndOffset | sl5=0 | Once every 5 slots |
| pathlossReferenceRS | ssb-Index=0 | SSB #0 is used for SRS path loss estimation |
| usage | Codebook | Codebook based UL transmission |
| startPosition | 0 | resourceMapping setting. SRS on last symbol of slot, and 1 symbols for SRS without repetition. |
| nrofSymbols | n1 |  |
| repetitionFactor | n1 |  |
| combOffset-n2 | 0 | transmissionComb setting |
| cyclicShift-n2 | 0 |  |
| nrofSRS-Ports | port1 | Number of antenna ports used for SRS transmission |
| NOTE: For further information see clause 6.3.2 in TS 38.331 [2]. |  |  |

##### A.17.4.3.1.3 Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k = 11.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.17.5 Signaling characteristics for RedCap

### A.17.5.1 Radio link Monitoring for RedCap

#### A.17.5.1.1 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode

##### A.17.5.1.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1B.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.17.5.1.1 .1-1. The test parameters are given in tables A.17.5.1.1 .1-2, A.17.5.1.1 .1-3, and A.17.5.1.1 .1-4 below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.17.5.1.1 .1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states, and Figure A.17.5.1.1 .1-2 shows the Time multiplexed downlink transmissions from each Angle of Arrival. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In addition to RLM-RS radio link monitoring using SSB index 0 and SSB index 1, the UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

Table A.17.5.1.1 .1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | TDD, SSB SCS 120 KHz, data SCS 120KHz, BW 100 MHz |

Table A.17.5.1.1 .1-2: General test parameters for FR2 out-of-sync testing in non-DRX mode

| Parameter |  |  | Unit | Value |
| --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |
| Active PCell |  |  |  | Cell 1 |
| RF Channel Number |  |  |  | 1 |
| Duplex mode |  | Config 1 |  | TDD |
| BWchannel |  | Config 1 |  | 100: NPRB,c = 66 |
| Data PRBs allocated |  | Config 1 |  | 24 |
| DL initial BWP configuration |  | Config 1 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  | Config 1 |  | DLBWP.1.1 |
| UL initial BWP configuration |  | Config 1 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  | Config 1 |  | ULBWP.1.1 |
| TDD Configuration |  | Config 1 |  | TDDConf.3.1 |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.3.1 TDD |
| Dedicated CORESET Reference Channel |  | Config 1 |  | CCR.3.4 TDD |
| SSB Configuration |  | Config 1 |  | SSB.1 FR2 |
| SMTC Configuration |  | Config 1 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 |  | 120 KHz |
| PRACH Configuration |  | Config 1 |  | Table A.3.8.3.4 |
| SSB index assigned as RLM RS |  | Config 1 |  | 0,1 |
| OCNG parameters |  |  |  | OP.5 |
| CP length |  |  |  | Normal |
| Out of sync transmission parameters | DCI format |  |  | 1-0 |
|  | Number of Control OFDM symbols |  |  | 2 |
|  | Aggregation level |  | CCE | 8 |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 4 |
|  | DMRS precoder granularity |  |  | REG bundle size |
|  | REG bundle size |  |  | 6 |
| DRX |  |  |  | OFF |
| Gap pattern ID |  |  |  | gp0 |
| Layer 3 filtering |  |  |  | Enabled |
| T310 timer |  |  | ms | 0 |
| T311 timer |  |  | ms | 1000 |
| N310 |  |  |  | 1 |
| N311 |  |  |  | 1 |
| CSI-RS for CSI reporting |  | Config 1 |  | CSI-RS.3.1 TDD |
| reportConfigType |  |  |  | periodic |
| reportQuantity |  |  |  | cri-RI-PMI-CQI |
| CSI reporting periodicity |  |  | slot | 40 |
| CSI reporting offset |  |  | slot | 4 |
| TCI states for PDCCH/PDSCH |  |  |  | TCI.State.2 |
| CSI-RS for tracking |  | Config 1 |  | TRS.2.1 TDD |
| T1 |  |  | s | 0.2 |
| T2 |  |  | s | 9.68 |
| T3 |  |  | s | 9.68 |
| D1 |  |  | s | 9.64 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |

Table A.17.5.1.1 .1-3: OTA related cell specific test parameters for FR2 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| AoA setup |  |  | Setup 3 defined in A.3.15 |  |  |  |  |  |
|  |  |  | AoA1 |  |  | AoA2 |  |  |
| Assumption for UE beams Note 5 |  |  | Rough |  |  | Rough |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 4 |  |  | Not sent |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB | 0 |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |  |
| ssb-Index 0 SNR | Config 1 | dB | 2Note 6 | -6Note 6 | -15 |  |  |  |
| ssb-Index 1 SNR | Config 1 |  | Not sent |  |  | 2Note 6 | -15 | -15 |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | Config 1 | dBm/ 15 kHz | -92.1 |  |  | -92.1 |  |  |
| Time multiplexing of the downlink transmissions from each AoA |  |  | Defined in figure A.17.5.1.1 .1-2 |  |  |  |  |  |
| Propagation condition |  |  | TDL-A 30 ns 75 Hz |  |  | TDL-A 30 ns 75 Hz |  |  |
| NOTE 1: OCNG shall be used such a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 4: The SNR values are specified for testing a UE which supports 2RX on at least one band..NOTE 5:  Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 6: This value allows up to 1 dB degradation from applied SNR to UE baseband |  |  |  |  |  |  |  |  |

Table A.17.5.1.1 .1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

| Field | Test 1 |
| --- | --- |
|  | Value |
| gapOffset | 0 |

![](media/SA FR2 OOS.PNG)

Figure A.17.5.1.1 .1-1: SNR variation for out-of-sync testing


![](media/image10.emf)

Figure A.17.5.1.1 .1-2: Time multiplexed downlink transmissions

##### A.17.5.1.1.2 Test Requirements

The UE behavior in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.


#### A.17.5.1.2 Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode

##### A.17.5.1.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1B.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.17.5.1.2.1-1.The test parameters are given in tables A.17.5.1.2.1-2, and A.17.5.1.2.1-3 below. There is one cell (Cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.1.2.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states, and Figure A.17.5.1.2.1-2 shows the Time multiplexed downlink transmissions from each Angle of Arrival. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

Table A.17.5.1.2.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | TDD, SSB SCS 120 KHz, data SCS 120KHz, BW 100 MHz |

Table A.17.5.1.2.1-2: General test parameters for FR2 in-sync testing in non-DRX mode

| Parameter |  |  | Unit | Value |
| --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |
| Active PCell |  |  |  | Cell 1 |
| RF Channel Number |  |  |  | 1 |
| Duplex mode |  | Config 1 |  | TDD |
| BWchannel |  | Config 1 |  | 100: NPRB,c = 66 |
| Data PRBs allocated |  | Config 1 |  | 24 |
| DL initial BWP configuration |  | Config 1 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  | Config 1 |  | DLBWP.1.1 |
| UL initial BWP configuration |  | Config 1 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  | Config 1 |  | ULBWP.1.1 |
| TDD Configuration |  | Config 1 |  | TDDConf.3.1 |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.3.1 TDD |
| Dedicated CORESET Reference Channel |  | Config 1 |  | CCR.3.1 TDD |
| SSB Configuration |  | Config 1 |  | SSB.1 FR2 |
| SMTC Configuration |  | Config 1 |  | SMTC.3 |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 |  | 120 KHz |
| PRACH Configuration |  | Config 1 |  | Table A.3.8.3.4 |
| SSB index assigned as RLM RS |  | Config 1 |  | 0,1 |
| OCNG parameters |  |  |  | OP.5 |
| CP length |  |  |  | Normal |
| In sync transmission parameters | DCI format |  |  | 1-0 |
|  | Number of Control OFDM symbols |  |  | 2 |
|  | Aggregation level |  | CCE | 4 |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 0 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 0 |
|  | DMRS precoder granularity |  |  | REG bundle size |
|  | REG bundle size |  |  | 6 |
| Out of sync transmission parameters | DCI format |  |  | 1-0 |
|  | Number of Control OFDM symbols |  |  | 2 |
|  | Aggregation level |  | CCE | 8 |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 4 |
|  | DMRS precoder granularity |  |  | REG bundle size |
|  | REG bundle size |  |  | 6 |
| DRX |  |  |  | OFF |
| Gap pattern ID |  |  |  | N.A. |
| Layer 3 filtering |  |  |  | Enabled |
| T310 timer |  |  | ms | 4000 |
| T311 timer |  |  | ms | 1000 |
| N310 |  |  |  | 1 |
| N311 |  |  |  | 1 |
| CSI-RS for CSI reporting |  | Config 1 |  | CSI-RS.3.1 TDD |
| reportConfigType |  |  |  | periodic |
| reportQuantity |  |  |  | cri-RI-PMI-CQI |
| CSI reporting periodicity |  |  | slot | 40 |
| CSI reporting offset |  |  | slot | 4 |
| TCI states for PDCCH/PDSCH |  |  |  | TCI.State.2 |
| CSI-RS for tracking |  | Config 1 |  | TRS.2.1 TDD |
| T1 |  |  | s | 0.2 |
| T2 |  |  | s | 0.2 |
| T3 |  |  | s | 1.88 |
| T4 |  |  | s | 0.2 |
| T5 |  |  | s | 3.84 |
| D1 |  |  | s | 3.8 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |

Table A.17.5.1.2.1-3: OTA related cell specific test parameters for FR2 (Cell 1) for in-sync radio link monitoring tests in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 | T1 | T2 | T3 | T4 | T5 |
| AoA setup |  |  | Setup 3 defined in A.3.15 |  |  |  |  |  |  |  |  |  |
|  |  |  | AoA1 |  |  |  |  | AoA2 |  |  |  |  |
| Assumption for UE beams Note 5 |  |  | Rough |  |  |  |  | Rough |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 0 |  |  |  |  | Not sent |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB | 0 |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |  |  |  |  |  |
| ssb-Index 0 SNR | Config 1 | dB | 2Note 6 | -6Note 6 | -15 | -15 | -15 |  |  |  |  |  |
| ssb-Index 1 SNR | Config 1 |  | Not sent |  |  |  |  | 2Note 6 | -15 | -15 | -4.5 | 2Note 6 |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | Config 1 | dBm/ 15 kHz | -92.1 |  |  |  |  | -92.1 |  |  |  |  |
| Time multiplexing of the downlink transmissions from each AoA |  |  | Defined in figure A.17.5.1.2.1-2 |  |  |  |  |  |  |  |  |  |
| Propagation condition |  |  | TDL-A 30 ns 75 Hz |  |  |  |  | TDL-A 30 ns 75 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 4: The SNR values are specified for testing a UE which supports 2RX on at least one band.NOTE 5:  Information about types of UE beam is given inannex  B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 6: This value allows up to 1 dB degradation from applied SNR to UE baseband |  |  |  |  |  |  |  |  |  |  |  |  |

Table A.17.5.1.2.1-4: Void

Figure A.17.5.1.2.1-1: SNR variation for in-sync testing


![](media/image12.emf)

Figure A.17.5.1.2.1-2: Time multiplexed downlink transmissions

##### A.17.5.1.2.2 Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.17.5.1.3 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode

##### A.17.5.1.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1B.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.17.5.1.3.1-1. The test parameters are given in tables A.17.5.1.3.1-2, and A.17.5.1.3.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.17.5.1.3.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states, and Figure A.17.5.1.3.1-2 shows the Time multiplexed downlink transmissions from each Angle of Arrival. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.17.5.1.3.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | TDD, SSB SCS 120 KHz, data SCS 120KHz, BW 100 MHz |

Table A.17.5.1.3.1-2: General test parameters for FR2 out-of-sync testing in DRX mode

| Parameter |  |  | Unit | Value |
| --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |
| Active PCell |  |  |  | Cell 1 |
| RF Channel Number |  |  |  | 1 |
| Duplex mode |  | Config 1 |  | TDD |
| BWchannel |  | Config 1 |  | 100: NPRB,c = 66 |
| Data PRBs allocated |  | Config 1 |  | 24 |
| DL initial BWP configuration |  | Config 1 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  | Config 1 |  | DLBWP.1.1 |
| UL initial BWP configuration |  | Config 1 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  | Config 1 |  | ULBWP.1.1 |
| TDD Configuration |  | Config 1 |  | TDDConf.3.1 |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.3.1 TDD |
| Dedicated CORESET Reference Channel |  | Config 1 |  | CCR.3.4 TDD |
| SSB Configuration |  | Config 1 |  | SSB.1 FR2 |
| SMTC Configuration |  | Config 1 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 |  | 120 KHz |
| PRACH Configuration |  | Config 1 |  | Table A.3.8.3.1 |
| SSB index assigned as RLM RS |  | Config 1 |  | 0,1 |
| OCNG parameters |  |  |  | OP.5 |
| CP length |  |  |  | Normal |
| Out of sync transmission parameters | DCI format |  |  | 1-0 |
|  | Number of Control OFDM symbols |  |  | 2 |
|  | Aggregation level |  | CCE | 8 |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 4 |
|  | DMRS precoder granularity |  |  | REG bundle size |
|  | REG bundle size |  |  | 6 |
| DRX Configuration |  |  |  | DRX.3 |
| Gap pattern ID |  |  |  | N.A. |
| Layer 3 filtering |  |  |  | Enabled |
| T310 timer |  |  | ms | 0 |
| T311 timer |  |  | ms | 1000 |
| N310 |  |  |  | 1 |
| N311 |  |  |  | 1 |
| CSI-RS for CSI reporting |  | Config 1 |  | CSI-RS.3.1 TDD |
| reportConfigType |  |  |  | periodic |
| reportQuantity |  |  |  | cri-RI-PMI-CQI |
| CSI reporting periodicity |  |  | slot | 40 |
| CSI reporting offset |  |  | slot | 4 |
| TCI states for PDCCH/PDSCH |  |  |  | TCI.State.2 |
| CSI-RS for tracking |  | Config 1 |  | TRS.2.1 TDD |
| T1 |  |  | s | 0.2 |
| T2 |  |  | s | 14.48 |
| T3 |  |  | s | 14.48 |
| D1 |  |  | s | 14.44 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |

Table A.17.5.1.3.1-3: OTA related cell specific test parameters for FR2 (Cell 1) for out-of-sync radio link monitoring tests in DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| AoA setup |  |  | Setup 3 defined in A.3.15 |  |  |  |  |  |
|  |  |  | AoA1 |  |  | AoA2 |  |  |
| Assumption for UE beams Note 5 |  |  | Rough |  |  | Rough |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 4 |  |  | Not sent |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB | 0 |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |  |
| ssb-Index 0 SNR | Config 1 | dB | 2Note 6 | -6Note 6 | -15 |  |  |  |
| ssb-Index 1 SNR | Config 1 |  | Not sent |  |  | 2Note 6 | -15 | -15 |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | Config 1 | dBm/ 15 kHz | -92.1 |  |  | -92.1 |  |  |
| Time multiplexing of the downlink transmissions from each AoA |  |  | Defined in figure A.17.5.1.1 .1-2 |  |  |  |  |  |
| Propagation condition |  |  | TDL-A 30 ns 75 Hz |  |  | TDL-A 30 ns 75 Hz |  |  |
| NOTE 1: OCNG shall be used such a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 4: The SNR values are specified for testing a UE which supports 2RX on at least one band..NOTE 5:  Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 6: This value allows up to 1 dB degradation from applied SNR to UE baseband |  |  |  |  |  |  |  |  |

Figure A.17.5.1.3.1-1: SNR variation for out-of-sync testing

![](media/image10.emf)

Figure A.17.5.1.3.1-2: Time multiplexed downlink transmissions

##### A.17.5.1.3.2 Test Requirements

The UE behavior in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.17.5.1.4 Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode

##### A.17.5.1.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1B.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.17.5.1.4.1-1. The test parameters are given in tables A.17.5.1.4.1-2, and A.17.5.1.4.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.1.4.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.17.5.1.4.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | TDD, SSB SCS 120 KHz, data SCS 120KHz, BW 100 MHz |

Table A.17.5.1.4.1-2: General test parameters for FR2 in-sync testing in DRX mode

| Parameter |  |  | Unit | Value |
| --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |
| Active PCell |  |  |  | Cell 1 |
| RF Channel Number |  |  |  | 1 |
| Duplex mode |  | Config 1 |  | TDD |
| BWchannel |  | Config 1 |  | 100: NPRB,c = 66 |
| Data PRBs allocated |  | Config 1 |  | 66 |
| DL initial BWP configuration |  | Config 1 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  | Config 1 |  | DLBWP.1.1 |
| UL initial BWP configuration |  | Config 1 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  | Config 1 |  | ULBWP.1.1 |
| TDD Configuration |  | Config 1 |  | TDDConf.3.1 |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.3.1 TDD |
| Dedicated CORESET Reference Channel |  | Config 1 |  | CCR.3.1 TDD |
| SSB Configuration |  | Config 1 |  | SSB.1 FR2 |
| SMTC Configuration |  | Config 1 |  | SMTC.3 |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 |  | 120 KHz |
| PRACH Configuration |  | Config 1 |  | Table A.3.8.3.4 |
| SSB index assigned as RLM RS |  | Config 1 |  | 0,1 |
| OCNG parameters |  |  |  | OP.1 |
| CP length |  |  |  | Normal |
| In sync transmission parameters | DCI format |  |  | 1-0 |
|  | Number of Control OFDM symbols |  |  | 2 |
|  | Aggregation level |  | CCE | 4 |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 0 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 0 |
|  | DMRS precoder granularity |  |  | REG bundle size |
|  | REG bundle size |  |  | 6 |
| Out of sync transmission parameters | DCI format |  |  | 1-0 |
|  | Number of Control OFDM symbols |  |  | 2 |
|  | Aggregation level |  | CCE | 8 |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 4 |
|  | DMRS precoder granularity |  |  | REG bundle size |
|  | REG bundle size |  |  | 6 |
| DRX Configuration |  |  |  | DRX.11 |
| Gap pattern ID |  |  |  | N.A. |
| Layer 3 filtering |  |  |  | Enabled |
| T310 timer |  |  | ms | 4000 |
| T311 timer |  |  | ms | 1000 |
| N310 |  |  |  | 1 |
| N311 |  |  |  | 1 |
| CSI-RS for CSI reporting |  | Config 1 |  | CSI-RS.3.1 TDD |
| reportConfigType |  |  |  | periodic |
| reportQuantity |  |  |  | cri-RI-PMI-CQI |
| CSI reporting periodicity |  |  | slot | 40 |
| CSI reporting offset |  |  | slot | 4 |
| TCI states for PDCCH/PDSCH |  |  |  | TCI.State.2 |
| CSI-RS for tracking |  | Config 1 |  | TRS.2.1 TDD |
| T1 |  |  | s | 0.2 |
| T2 |  |  | s | 0.2 |
| T3 |  |  | s | 2.8 |
| T4 |  |  | s | 0.2 |
| T5 |  |  | s | 3.88 |
| D1 |  |  | s | 3.84 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |

Table A.17.5.1.4.1-3: OTA related cell specific test parameters for FR2 (Cell 1) for in-sync radio link monitoring test in DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 |
| AoA setup |  |  | Setup 1 defined in A.3.15 |  |  |  |  |
| Assumption for UE beams Note 5 |  |  | Rough |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |
| ssb-Index 0 SNR | Config 1 | dB | 2Note 6 | -6Note 6 | -15 | -4.5 | 2Note 6 |
| ssb-Index 1 SNR | Config 1 |  | 2Note 6 | -15 | -15 | -15 | -15 |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15KHz | -104.7 |  |  |  |  |
| Propagation condition |  |  | TDL-A 30 ns 75 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.3NOTE 3: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 4: The SNR values are specified for testing a UE which supports 2RX on at least one band.NOTE 5: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 6: This value allows up to 1 dB degradation from applied SNR to UE baseband. |  |  |  |  |  |  |  |

Table A.17.5.1.4.1-4: Void

Table A.17.5.1.4.1-5: Void

![](media/SA FR2 INS.PNG)

Figure A.17.5.1.4.1-1: SNR variation for in-sync testing

##### A.17.5.1.4.2 Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.17.5.1.5 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode

##### A.17.5.1.5.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used. This test will partly verify the FR2 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1B.3.

The test parameters are given in tables A.17.5.1.5.1-1, A.17.5.1.5.1-2, A.17.5.1.5.1-3 and A.17.5.1.5.1-4 below. There is one cell, Cell 1 which is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.17.5.1.5.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 10 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 and SSB1 are configured as BFD-RS.

Table A.17.5.1.5.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | TDD duplex mode, 120 kHz SSB SCS, 100 MHz bandwidth |

Table A.17.5.1.5.1-2: General test parameters for FR2 PCell for CSI-RS out-of-sync testing in non-DRX mode

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| Active PCell |  |  | Cell 1 |
| RF Channel Number |  |  | 1 |
| Duplex mode | Config 1 |  | TDD |
| BWchannel | Config 1 |  | 100: NPRB,c = 66 |
| Data PRBs allocated | Config 1 |  | 24 |
| BWoccupied | Config 1 |  | 24 |
| TDD Configuration | Config 1 |  | TDDConf.3.1 |
| DL initial BWP configuration | Config 1 |  | DLBWP.0.1 |
| DL dedicated BWP configuration | Config 1 |  | DLBWP.1.4 |
| UL initial BWP configuration | Config 1 |  | ULBWP.0.1 |
| UL dedicated BWP configuration | Config 1 |  | ULBWP.1.4 |
| RMSI CORESET Reference Channel | Config 1 |  | CR.3.1 TDD |
| Dedicated CORESET Reference Channel | Config 1 |  | CCR.3.4 TDDCCR.3.6 TDD |
| SSB Configuration | Config 1 |  | SSB.1 FR2 |
| SMTC Configuration | Config 1 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing | Config 1 |  | 120 KHz |
| CSI-RS for RLM | Config 1 |  | Resource #4 in TRS.2.1 TDDResource #4 in TRS.2.2 TDD |
| TRS configuration |  |  | TRS.2.1 TDDTRS.2.2 TDD |
| TCI configuration for PDCCH#1/PDSCH |  |  | TCI.State.2 |
| TCI configuration for PDCCH#2 |  |  | TCI.State.3 |
| OCNG parameters |  |  | OP.5 |
| CP length |  |  | Normal |
| Out of sync transmission parameters | DCI format |  | 1-0 |
|  | Number of Control OFDM symbols |  | 2 |
|  | Aggregation level | CCE | 8 |
|  | Ratio of hypothetical PDCCH RE energy to average CSI-RS RE energy | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average CSI-RS RE energy | dB | 4 |
|  | DMRS precoder granularity |  | REG bundle size |
|  | REG bundle size |  | 6 |
| DRX |  |  | OFF |
| Gap pattern ID |  |  | *gp0 |
| Layer 3 filtering |  |  | Enabled |
| T310 timer |  | ms | 0 |
| T311 timer |  | ms | 1000 |
| N310 |  |  | 1 |
| N311 |  |  | 1 |
| CSI-RS for CSI reporting | Config 1 |  | CSI-RS.3.1 TDD |
| reportConfigType |  |  | periodic |
| reportQuantity |  |  | cri-RI-PMI-CQI |
| CSI reporting periodicity |  | slot | 40 |
| CSI reporting offset |  | slot | 4 |
| T1 |  | s | 0.2 |
| T2 |  | s | 0.35 |
| T3 |  | s | 0.35 |
| D1 |  | s | 0.31 |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |

Table A.17.5.1.5.1-3: Cell specific test parameters for FR2 for CSI-RS out-of-sync radio link monitoring in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| AoA setup |  |  | Setup 3 defined in A.3.15 |  |  |  |  |  |
|  |  |  | AoA1 |  |  | AoA2 |  |  |
| Assumption for UE beams Note 10 |  |  | Rough |  |  | Rough |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 4 |  |  | Not sent |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB | 0 |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |  |
| SNR on RLM-RS1 | Config 1 | dB | 2Note 11 | -6Note 11 | -15 |  |  |  |
| SNR on RLM-RS2 | Config 1 |  | Not sent |  |  | 2Note 11 | -15 | -15 |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | Config 1 | dBm/ 15 kHz | -92.1 |  |  | -92.1 |  |  |
| Propagation condition |  |  | TDL-A 30ns 75Hz |  |  | TDL-A 30ns 75Hz |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2 and T3 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.17.5.1.5.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. NOTE 10: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 11: This value allows up to 1 dB degradation from applied SNR to UE baseband |  |  |  |  |  |  |  |  |

Table A.17.5.1.5.1-4: Measurement gap configuration for FR2 CSI-RS out-of-sync radio link monitoring in non-DRX mode

| Field | Test 1 |
| --- | --- |
|  | Value |
| gapOffset | 0 |
| NOTE 1: RLM RS is partially overlapped with measurement gap |  |

Figure A.17.5.1.5.1-1: SNR variation for CSI-RS out-of-sync testing

##### A.17.5.1.5.2 Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During time durations T1, T2 and T3, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 no later than time point C (D1 second after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.17.5.1.6 Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode

##### A.17.5.1.6.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used. This test will partly verify the FR2 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1B.3.

The test parameters are given in tables A.17.5.1.6.1-1, A.17.5.1.6.1-2 and A.17.5.1.6.1-3 below. There is one cells, Cell 1which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.1.6.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 10 ms. In the test, DRX configuration is not enabled. In the test, SSB0 and SSB1 are configured as BFD-RS.

Table A.17.5.1.6.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | TDD duplex mode, 120 kHz SSB SCS, 100 MHz bandwidth |

Table A.17.5.1.6.1-2: General test parameters for FR2 PCell for CSI-RS in-sync testing in non-DRX mode

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| Active PCell |  |  | Cell 1 |
| RF Channel Number |  |  | 1 |
| Duplex mode | Config 1 |  | TDD |
| BWchannel | Config 1 |  | 100: NPRB,c = 66 |
| Data PRBs allocated | Config 1 |  | 24 |
| BWoccupied | Config 1 |  | 24 |
| TDD Configuration | Config 1 |  | TDDConf.3.1 |
| DL initial BWP configuration | Config 1 |  | DLBWP.0.1 |
| DL dedicated BWP configuration | Config 1 |  | DLBWP.1.4 |
| UL initial BWP configuration | Config 1 |  | ULBWP.0.1 |
| UL dedicated BWP configuration | Config 1 |  | ULBWP.1.4 |
| RMSI CORESET Reference Channel | Config 1 |  | CR.3.1 TDD |
| Dedicated CORESET Reference Channel | Config 1 |  | CCR.3.1 TDDCCR.3.3 TDD |
| SSB Configuration | Config 1 |  | SSB.1 FR2 |
| SMTC Configuration | Config 1 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing | Config 1 |  | 120 KHz |
| CSI-RS for RLM | Config 1 |  | Resource #4 in TRS.2.1 TDDResource #4 in TRS.2.2 TDD |
| TRS configuration |  |  | TRS.2.1 TDDTRS.2.2 TDD |
| TCI configuration for PDCCH#1/PDSCH |  |  | TCI.State.2 |
| TCI configuration for PDCCH#2 |  |  | TCI.State.3 |
| OCNG parameters |  |  | OP.5 |
| CP length |  |  | Normal |
| Out of sync transmission parameters | DCI format |  | 1-0 |
|  | Number of Control OFDM symbols |  | 2 |
|  | Aggregation level | CCE | 8 |
|  | Ratio of hypothetical PDCCH RE energy to average CSI-RS RE energy | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average CSI-RS RE energy | dB | 4 |
|  | DMRS precoder granularity |  | REG bundle size |
|  | REG bundle size |  | 6 |
| In sync transmission parameters | DCI format |  | 1-0 |
|  | Number of Control OFDM symbols |  | 2 |
|  | Aggregation level | CCE | 4 |
|  | Ratio of hypothetical PDCCH RE energy to average CSI-RS RE energy | dB | 0 |
|  | Ratio of hypothetical PDCCH DMRS energy to average CSI-RS RE energy | dB | 0 |
|  | DMRS precoder granularity |  | REG bundle size |
|  | REG bundle size |  | 6 |
| DRX |  |  | OFF |
| Gap pattern ID |  |  | N.A. |
| Layer 3 filtering |  |  | Enabled |
| T310 timer |  | ms | 1000 |
| T311 timer |  | ms | 1000 |
| N310 |  |  | 1 |
| N311 |  |  | 1 |
| CSI-RS for CSI reporting | Config 1 |  | CSI-RS.3.1 TDD |
| reportConfigType |  |  | periodic |
| reportQuantity |  |  | cri-RI-PMI-CQI |
| CSI reporting periodicity |  | slot | 40 |
| CSI reporting offset |  | slot | 4 |
| T1 |  | s | 0.2 |
| T2 |  | s | 0.2 |
| T3 |  | s | 0.24 |
| T4 |  | s | 0.2 |
| T5 |  | s | 0.88 |
| D1 |  | s | 0.84 |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |

Table A.17.5.1.6.1-3: Cell specific test parameters for FR2 for CSI-RS in-sync radio link monitoring in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 | T1 | T2 | T3 | T4 | T5 |
| AoA setup |  |  | Setup 3 defined in A.3.15 |  |  |  |  |  |  |  |  |  |
|  |  |  | AoA1 |  |  |  |  | AoA2 |  |  |  |  |
| Assumption for UE beams Note 10 |  |  | Rough |  |  |  |  | Rough |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 4 |  |  |  |  | Not sent |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB | 0 |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |  |  |  |  |  |
| SNR on RLM-RS1 | Config 1 | dB | 2Note 11 | -6Note 11 | -15 | -15 | -15 |  |  |  |  |  |
| SNR on RLM-RS2 | Config 1 |  | Not sent |  |  |  |  | 2Note 11 | -15 | -15 | -4.5 | 2Note 11 |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | Config 1 | dBm/ 15KHz | -92.1 |  |  |  |  | -92.1 |  |  |  |  |
| Propagation condition |  |  | TDL-A 30ns 75Hz |  |  |  |  | TDL-A 30ns 75Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2, SNR3, SNR4 and SNR5 respectively in figure A.17.5.1.6.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band.NOTE 10:  Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 11: This value allows up to 1 dB degradation from applied SNR to UE baseband. |  |  |  |  |  |  |  |  |  |  |  |  |

Figure A.17.5.1.6.1-1: SNR variation for CSI-RS in-sync testing

##### A.17.5.1.6.2 Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.17.5.1.7 Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode

##### A.17.5.1.7.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when DRX is used. This test will partly verify the FR2 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1B.3.

The test parameters are given in tables A.17.5.1.7.1-1, A.17.5.1.7.1-2, and A.17.5.1.7.1-3 below. There is one cell, Cell 1 is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.17.5.1.7.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 10 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test. In the test, SSB0 and SSB1 are configured as BFD-RS.

Table A.17.5.1.7.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | TDD duplex mode, 120 kHz SSB SCS, 100 MHz bandwidth |

Table A.17.5.1.7.1-2: General test parameters for FR2 PCell for CSI-RS out-of-sync testing in DRX mode

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| Active PCell |  |  | Cell 1 |
| RF Channel Number |  |  | 1 |
| Duplex mode | Config 1 |  | TDD |
| TDD Configuration | Config 1 |  | TDDConf.3.1 |
| DL initial BWP configuration | Config 1 |  | DLBWP.0.1 |
| DL dedicated BWP configuration | Config 1 |  | DLBWP.1.1 |
| UL initial BWP configuration | Config 1 |  | ULBWP.0.1 |
| UL dedicated BWP configuration | Config 1 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel | Config 1 |  | CR.3.1 TDD |
| Dedicated CORESET Reference Channel | Config 1 |  | CCR.3.4 TDDCCR.3.6 TDD |
| SSB Configuration | Config 1 |  | SSB.1 FR2 |
| SMTC Configuration | Config 1 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing | Config 1 |  | 120 KHz |
| CSI-RS for RLM | Config 1 |  | Resource #4 in TRS.2.1 TDDResource #4 in TRS.2.2 TDD |
| TRS configuration |  |  | TRS.2.1 TDDTRS.2.2 TDD |
| TCI configuration for PDCCH#1/PDSCH |  |  | TCI.State.2 |
| TCI configuration for PDCCH#2 |  |  | TCI.State.3 |
| OCNG parameters |  |  | OP.1 |
| CP length |  |  | Normal |
| Out of sync transmission parameters | DCI format |  | 1-0 |
|  | Number of Control OFDM symbols |  | 2 |
|  | Aggregation level | CCE | 8 |
|  | Ratio of hypothetical PDCCH RE energy to average CSI-RS RE energy | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average CSI-RS RE energy | dB | 4 |
|  | DMRS precoder granularity |  | REG bundle size |
|  | REG bundle size |  | 6 |
| DRX |  |  | DRX.3 |
| Gap pattern ID |  |  | N.A. |
| Layer 3 filtering |  |  | Enabled |
| T310 timer |  | ms | 0 |
| T311 timer |  | ms | 1000 |
| N310 |  |  | 1 |
| N311 |  |  | 1 |
| CSI-RS for CSI reporting | Config 1 |  | CSI-RS.3.1 TDD |
| reportConfigType |  |  | periodic |
| reportQuantity |  |  | cri-RI-PMI-CQI |
| CSI reporting periodicity |  | slot | 40 |
| CSI reporting offset |  | slot | 4 |
| T1 |  | s | 0.2 |
| T2 |  | s | 1.28 |
| T3 |  | s | 1.28 |
| D1 |  | s | 1.24 |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |

Table A.17.5.1.7.1-3: Cell specific test parameters for FR2 for CSI-RS out-of-sync radio link monitoring in DRX mode

| Parameter |  | Unit | Test 1 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| AoA setup |  | dB | Setup 1 defined in A.3.15 |  |  |
| Assumption for UE beams Note 10 |  |  | Rough |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 4 |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB | 0 |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |
| SNR on RLM-RS1 | Config 1 | dB | 2Note 11 | -6Note 11 | -15 |
| SNR on RLM-RS2 | Config 1 | dB | 2Note 11 | -15 | -15 |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15KHz | -104.7 |  |  |
| Propagation condition |  |  | TDL-A 30ns 75Hz |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2 and T3 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.17.5.1.7.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band.NOTE 10: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 11: This value allows up to 1 dB degradation from applied SNR to UE baseband. |  |  |  |  |  |

Figure A.17.5.1.7.1-1: SNR variation for CSI-RS out-of-sync testing

##### A.17.5.1.7.2 Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During time durations T1, T2 and T3, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on PCell.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 (PCell) at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 (PCell) no later than time point C (D1 secondafter the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.17.5.1.8 Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode

##### A.17.5.1.8.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when DRX is used. This test will partly verify the FR2 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1B.

The test parameters are given in tables A.17.5.1.8.1-1, A.17.5.1.8.1-2, A.17.5.1.8.1-3 and A.17.5.1.8.1-4 below. There is one cells, Cell 1which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.1.8.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 10 ms. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 and SSB1 are configured as BFD-RS.

Table A.17.5.1.8.1-1: Supported test configurations for FR2 PSCell

| Configuration | Description |
| --- | --- |
| 1 | TDD duplex mode, 120 kHz SSB SCS, 100 MHz bandwidth |

Table A.17.5.1.8.1-2: General test parameters for FR2 PCell for CSI-RS in-sync testing in DRX mode

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| Active PCell |  |  | Cell 1 |
| RF Channel Number |  |  | 1 |
| Duplex mode | Config 1 |  | TDD |
| TDD Configuration | Config 1 |  | TDDConf.3.1 |
| DL initial BWP configuration | Config 1 |  | DLBWP.0.1 |
| DL dedicated BWP configuration | Config 1 |  | DLBWP.1.1 |
| UL initial BWP configuration | Config 1 |  | ULBWP.0.1 |
| UL dedicated BWP configuration | Config 1 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel | Config 1 |  | CR.3.1 TDD |
| Dedicated CORESET Reference Channel | Config 1 |  | CCR.3.1 TDDCCR.3.3 TDD |
| SSB Configuration | Config 1 |  | SSB.1 FR2 |
| SMTC Configuration | Config 1 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing | Config 1 |  | 120 KHz |
| CSI-RS for RLM | Config 1 |  | Resource #4 in TRS.2.1 TDDResource #4 in TRS.2.2 TDD |
| TRS configuration |  |  | TRS.2.1 TDDTRS.2.2 TDD |
| TCI configuration for PDCCH#1/PDSCH |  |  | TCI.State.2 |
| TCI configuration for PDCCH#2 |  |  | TCI.State.3 |
| OCNG parameters |  |  | OP.1 |
| CP length |  |  | Normal |
| Out of sync transmission parameters | DCI format |  | 1-0 |
|  | Number of Control OFDM symbols |  | 2 |
|  | Aggregation level | CCE | 8 |
|  | Ratio of hypothetical PDCCH RE energy to average CSI-RS RE energy | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average CSI-RS RE energy | dB | 4 |
|  | DMRS precoder granularity |  | REG bundle size |
|  | REG bundle size |  | 6 |
| In sync transmission parameters | DCI format |  | 1-0 |
|  | Number of Control OFDM symbols |  | 2 |
|  | Aggregation level | CCE | 4 |
|  | Ratio of hypothetical PDCCH RE energy to average CSI-RS RE energy | dB | 0 |
|  | Ratio of hypothetical PDCCH DMRS energy to average CSI-RS RE energy | dB | 0 |
|  | DMRS precoder granularity |  | REG bundle size |
|  | REG bundle size |  | 6 |
| DRX |  |  | DRX.3 |
| Gap pattern ID |  |  | *gp0 |
| Layer 3 filtering |  |  | Enabled |
| T310 timer |  | ms | 2000 |
| T311 timer |  | ms | 1000 |
| N310 |  |  | 1 |
| N311 |  |  | 1 |
| CSI-RS for CSI reporting | Config 1 |  | CSI-RS.3.1 TDD |
| reportConfigType |  |  | periodic |
| reportQuantity |  |  | cri-RI-PMI-CQI |
| CSI reporting periodicity |  | slot | 40 |
| CSI reporting offset |  | slot | 4 |
| T1 |  | s | 0.2 |
| T2 |  | s | 0.2 |
| T3 |  | s | 1.64 |
| T4 |  | s | 0.2 |
| T5 |  | s | 1.88 |
| D1 |  | s | 1.84 |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |

Table A.17.5.1.8.1-3: Cell specific test parameters for FR2 for CSI-RS in-sync radio link monitoring in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 |
| AoA setup |  | dB | Setup 1 defined in A.3.15 |  |  |  |  |
| Assumption for UE beams Note 10 |  |  | Rough |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 4 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |
| SNR on RLM-RS1 | Config 1 | dB | 2Note 11 | -6Note 11 | -15 | -4.5 | 2Note 11 |
| SNR on RLM-RS2 | Config 1 | dB | 2Note 11 | -15 | -15 | -15 | -15 |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15KHz | -104.7 |  |  |  |  |
| Propagation condition |  |  | TDL-A 30ns 75Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2, SNR3, SNR4 and SNR5 respectively in figure A.17.5.1.8.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band..NOTE 10:  Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 11: This value allows up to 1 dB degradation from applied SNR to UE baseband. |  |  |  |  |  |  |  |

Table A.17.5.1.8.1-4: Measurement gap configuration for FR2 CSI-RS in-sync radio link monitoring in non-DRX mode

| Field | Test 1 |
| --- | --- |
|  | Value |
| gapOffset | 0 |
| NOTE 1: RLM RS is partially overlapped with measurement gap |  |

Figure A.17.5.1.8.1-1: SNR variation for CSI-RS in-sync testing

##### A.17.5.1.8.2 Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.17.5.1.9 UE Radio Link Monitoring Scheduling Restrictions on FR2

##### A.17.5.1.9.1 Test Purpose and Environment

The purpose is to verify that the NR UE correctly follows the RLM scheduling restrictions requirements defined in clause 8.1B.7. This test verifies that the UE correctly receive the PDCCH scheduled on the symbols right before the RLM SSB symbols without overlap so that it sends ACK/NACK correctly. The test case is only applicable to UE which supports pdcch-MonitoringAnyOccasions or pdcch-MonitoringAnyOccasionsWithSpanGap.

The test parameters are given in table A.17.5.1.9.1-1, table A.17.5.1.9.1-2 and table A.17.5.1.9.1-3 below. The UE is required during time period T1 to transmit ACK/NACK correctly upon scheduling of PDSCH.

Table A.17.5.1.9.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 120 kHz RMC SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.5.1.9.1-2: General test parameters for NR RLM scheduling restriction test case in FR2

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  | 1 | 1 |  |
| SSB configuration |  | 1 | SSB.1 FR2 |  |
| SMTC configuration |  | 1 | SMTC.3 |  |
| DRX cycle length | s | 1 | OFF |  |
| T1 | s | 1 | 5 | During T1 the UE is required to correctly transmit ACK/NACK |

Table A.17.5.1.9.1-3: Cell specific test parameters for NR RLM scheduling restriction test case in FR2

| Parameter | Unit | Test configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
| AoA setup |  | 1 | Setup 3 defined in A.3.15.3 |  |
|  |  |  | AoA1 | AoA2 |
| Assumption for UE beams Note 1 |  |  | Rough | Rough |
| TDD configuration |  | 1 | TDDConf.3.1 |  |
| BWchannel | MHz | 1 | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  | 1 | 24 |  |
| PDSCH Reference measurement channel |  | 1 | SR.3.2 TDD | Not sent |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD | Not sent |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.2 TDD | Not sent |
| TRS configuration |  | 1 | TRS.2.1 TDD | TRS.2.2 TDD |
| PDCCH/PDSCH TCI state |  | 1 | TCI.State.2 | N/A |
| OCNG Pattern |  | 1 | OP.5 defined in A.3.2.1 | Not sent |
| Initial DL BWP configuration |  | 1 | DLBWP.0.1 |  |
| Initial UL BWP configuration |  | 1 | ULBWP.0.1 |  |
| RLM-RS |  | 1 | SSB with index 0 | SSB with index 1 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] | dBm/15 kHz | 1 | -92.1 | -92.1 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -83.1 | -83.1 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 2 | 2 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot]BB Note 4 | dB | 1 | 1 | 1 |
| SSB_RP Note3 | dBm/SCS | 1 | -81.1 | -81.1 |
| Io | dBm/95.04 MHz | 1 | -54.35 | -54.35 |
| Time multiplexing of the downlink transmissions from each AoA |  | 1 | Defined in figure A.17.5.1.9.1-1 |  |
| Propagation Condition |  | 1 | AWGN | AWGN |
| NOTE 1:  Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Es/Iot, SSB_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBS from TS 38.101-2 [19] Table 6.2.1.3-4. |  |  |  |  |

![](media/image18.emf)

Figure A.17.5.1.9.1-1: Time multiplexed downlink transmissions

##### A.17.5.1.9.2 Test Requirements

The UE behaviour follows the requirements defined in clause 8.1B.7.3.

### A.17.5.2 Beam Failure Detection and Link recovery procedures

#### A.17.5.2.1 Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode

##### A.17.5.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5B.

The test parameters are given in tables A.17.5.2.1.1-1, A.17.5.2.1.1-2 and A.17.5.2.1.1-3 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.2.1.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.17.5.2.1.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

Table A.17.5.2.1.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | TDD duplex mode, 120 kHz SSB SCS, 100 MHz bandwidth |

Table A.17.5.2.1.1-2: General test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  | TestConfig. | Unit | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |  |
| Active PCell |  | 1 |  | Cell 1 |  |
| RF Channel Number |  | 1 |  | 1 |  |
| Duplex mode |  | 1 |  | TDD |  |
| TDD Configuration |  | 1 |  | TDDConf.3.1 |  |
| BWchannel |  | 1 |  | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  | 1 |  | 66 |  |
| PDSCH/PDCCH subcarrier spacing |  | 1 | kHz | 120 |  |
| DL initial BWP configuration |  | 1 |  | DLBWP.0.1 |  |
| DL dedicated BWP configuration |  | 1 |  | DLBWP.1.1 |  |
| UL initial BWP configuration |  | 1 |  | ULBWP.0.1 |  |
| UL dedicated BWP configuration |  | 1 |  | ULBWP.1.1 |  |
| PDSCH Reference Channel |  | 1 |  | SR.3.2 TDD |  |
| RMSI CORESET Reference Channel |  | 1 |  | CR.3.1 TDD |  |
| Dedicated CORESET Reference Channel |  | 1 |  | CCR.3.1 TDD |  |
| OCNG parameters |  | 1 |  | OP.1 |  |
| CP length |  | 1 |  | Normal |  |
| PDSCH/PDCCH TCI state |  | 1 |  | TCI.State.0 |  |
| CSI-RS for tracking |  | 1 |  | TRS.2.1 TDD |  |
| SSB Configuration |  | 1 |  | SSB.1 FR2 |  |
| SMTC Configuration |  | 1 |  | SMTC.3 |  |
| PRACH Configuration |  | 1 |  | FR2 PRACH configuration 2 | A.3.8.3.2 |
| DRX configuration |  | 1 |  | OFF |  |
| SSB index assigned as BFD RS (q0) |  | 1 |  | 0 |  |
| SSB index assigned as CBD RS (q1) |  | 1 |  | 1 |  |
| SSB index assigned as RLM RS |  | 1 |  | 0,1 |  |
| Beam failure detection transmission parameters | DCI format | 1 |  | 1-0 |  |
|  | Number of Control OFDM symbols | 1 |  | 2 |  |
|  | Aggregation level | 1 | CCE | 8 |  |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy | 1 | dB | 0 |  |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy | 1 | dB | 0 |  |
|  | DMRS precoder granularity | 1 |  | REG bundle size |  |
|  | REG bundle size | 1 |  | 6 |  |
| Gap pattern ID |  | 1 |  | gp0 |  |
| gapOffset |  | 1 | ms | 0 |  |
| rlmInSyncOutOfSyncThreshold |  | 1 |  | absent | Value 0 is applied. (Table 8.1.1-1). |
| rsrp-ThresholdSSB |  | 1 | dBm/SCS | -95 | Threshold used for Qin_LR_SSB |
| powerControlOffsetSS |  | 1 |  | db0 | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  | 1 |  | n1 | see TS 38.321 [7], clause 5.17 |
| beamFailureDetectionTimer |  | 1 |  | pbfd4 | see TS 38.321 [7], clause 5.17 |
| CSI-RS configuration for CSI reporting |  | 1 |  | CSI-RS.3.1 TDD |  |
| reportConfigType |  | 1 |  | periodic |  |
| reportQuantity |  | 1 |  | cri-RI-PMI-CQI |  |
| CSI reporting periodicity |  | 1 | slot | 40 |  |
| CSI reporting offset |  | 1 | slot | 4 |  |
| T310 |  | 1 | ms | 1000 |  |
| N310 |  | 1 |  | 2 |  |
| T1 |  | 1 | s | 1 | The UE shall be fully synchronized to Cell 1 during T1 |
| T2 |  | 1 | s | 2.61 |  |
| T3 |  | 1 | s | 1.64 |  |
| T4 |  | 1 | s | 0 |  |
| T5 |  | 1 | s | 1.01 |  |
| D1 |  | 1 | s | 0.97 |  |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |

Table A.17.5.2.1.1-3: Cell specific test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

| Parameter | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 | T4 | T5 |
| AoA setup |  | Setup 1 defined in A.3.15 |  |  |  |  |
| Assumption for UE beams Note 10 |  | Rough |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS | dB | 0 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS | dB |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS | dB |  |  |  |  |  |
| SNR_SSB of set q0 | dB | 5Note 11 | -3Note 11 | -12 | -12 | -12 |
| SNR_SSB of set q1 | dB | 0.2 | 0.2 | 20.2 | 20.2 | 20.2 |
| SSB_RP of set q1 | dBm/SCS | -104.5 | -104.5 | -84.5 | -84.5 | -84.5 |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | dBm/120 KHz | -104.7 |  |  |  |  |
| Propagation condition |  | TDL-A 30 ns 75 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.17.5.2.1.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band.NOTE 10: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 11: This value allows up to 1 dB degradation from applied SNR to UE baseband |  |  |  |  |  |  |

Figure A.17.5.2.1.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.17.5.2.1.1-2: SSB_RP level variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

##### A.17.5.2.1.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 960+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.17.5.2.2 Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in DRX mode

##### A.17.5.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5.

The test parameters are given in tables A.17.5.2.2.1-1, A.17.5.2.2.1-2 and A.17.5.2.2.1-3 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.2.2.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.17.5.2.2.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.17.5.2.2.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | TDD duplex mode, 120 kHz SSB SCS, 100 MHz bandwidth |

Table A.17.5.2.2.1-2: General test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

| Parameter |  | TestConfig. | Unit | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |  |
| Active PCell |  | 1 |  | Cell 1 |  |
| RF Channel Number |  | 1 |  | 1 |  |
| Duplex mode |  | 1 |  | TDD |  |
| TDD Configuration |  | 1 |  | TDDConf.3.1 |  |
| BWchannel |  | 1 |  | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  | 1 |  | 66 |  |
| PDSCH/PDCCH subcarrier spacing |  | 1 | kHz | 120 |  |
| DL initial BWP configuration |  | 1 |  | DLBWP.0.1 |  |
| DL dedicated BWP configuration |  | 1 |  | DLBWP.1.1 |  |
| UL initial BWP configuration |  | 1 |  | ULBWP.0.1 |  |
| UL dedicated BWP configuration |  | 1 |  | ULBWP.1.1 |  |
| PDSCH Reference Channel |  | 1 |  | SR.3.2 TDD |  |
| RMSI CORESET Reference Channel |  | 1 |  | CR.3.1 TDD |  |
| Dedicated CORESET Reference Channel |  | 1 |  | CCR.3.1 TDD |  |
| OCNG parameters |  | 1 |  | OP.1 |  |
| CP length |  | 1 |  | Normal |  |
| PDSCH/PDCCH TCI state |  | 1 |  | TCI.State.0 |  |
| CSI-RS for tracking |  | 1 |  | TRS.2.1 TDD |  |
| SSB Configuration |  | 1 |  | SSB.1 FR2 |  |
| SMTC Configuration |  | 1 |  | SMTC.3 |  |
| PRACH Configuration |  | 1 |  | FR2 PRACH configuration 2 | A.3.8.3.2 |
| DRX configuration |  | 1 |  | DRX.3 | A.3.3.3 |
| SSB index assigned as BFD RS (q0) |  | 1 |  | 0 |  |
| SSB index assigned as CBD RS (q1) |  | 1 |  | 1 |  |
| SSB index assigned as RLM RS |  | 1 |  | 0,1 |  |
| Beam failure detection transmission parameters | DCI format | 1 |  | 1-0 |  |
|  | Number of Control OFDM symbols | 1 |  | 2 |  |
|  | Aggregation level | 1 | CCE | 8 |  |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy | 1 | dB | 0 |  |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy | 1 | dB | 0 |  |
|  | DMRS precoder granularity | 1 |  | REG bundle size |  |
|  | REG bundle size | 1 |  | 6 |  |
| Gap pattern ID |  | 1 |  | N/A |  |
| rlmInSyncOutOfSyncThreshold |  | 1 |  | absent | Value 0 is applied. (Table 8.1.1-1). |
| rsrp-ThresholdSSB |  | 1 | dBm/SCS | -95 | Threshold used for Qin_LR_SSB |
| powerControlOffsetSS |  | 1 |  | db0 | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  | 1 |  | n1 | see TS 38.321 [7], clause 5.17 |
| beamFailureDetectionTimer |  | 1 |  | pbfd4 | see TS 38.321 [7], clause 5.17 |
| CSI-RS configuration for CSI reporting |  | 1 |  | CSI-RS.3.1 TDD |  |
| reportConfigType |  | 1 |  | periodic |  |
| reportQuantity |  | 1 |  | cri-RI-PMI-CQI |  |
| CSI reporting periodicity |  | 1 | slot | 40 |  |
| CSI reporting offset |  | 1 | slot | 4 |  |
| T310 |  | 1 | ms | 1000 |  |
| N310 |  | 1 |  | 2 |  |
| T1 |  | 1 | s | 1 | The UE shall be fully synchronized to Cell 1 during T1 |
| T2 |  | 1 | s | 3.37 |  |
| T3 |  | 1 | s | 2.8 |  |
| T4 |  | 1 | s | 0 |  |
| T5 |  | 1 | s | 0.61 |  |
| D1 |  | 1 | s | 0.57 |  |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |

Table A.17.5.2.2.1-3: Cell specific test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

| Parameter | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 | T4 | T5 |
| AoA setup |  | Setup 1 defined in A.3.15 |  |  |  |  |
| Assumption for UE beams Note 9 |  | Rough |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS | dB | 0 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS | dB |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS | dB |  |  |  |  |  |
| SNR_SSB of set q0 | dB | 5Note 10 | -3Note 10 | -12 | -12 | -12 |
| SNR_SSB of set q1 | dB | 0.2 | 0.2 | 20.2 | 20.2 | 20.2 |
| SSB_RP of set q1 | dBm/SCS | -104.5 | -104.5 | -84.5 | -84.5 | -84.5 |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | dBm/120 KHz | -104.7 |  |  |  |  |
| Propagation condition |  | TDL-A 30 ns 75 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 5: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 6: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 7: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.17.5.2.1.1-1.NOTE 8: The SNR values are specified for testing a UE which supports 2RX on at least one band. NOTE 9: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 10: This value allows up to 1 dB degradation from applied SNR to UE baseband. |  |  |  |  |  |  |

Figure A.17.5.2.2.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in DRX mode

Figure A.17.5.2.2.1-2: SSB_RP level variation for SSB-based beam failure detection and link recovery testing in DRX mode

##### A.17.5.2.2.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 560+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.17.5.2.3 Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode

##### A.17.5.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5B.

The test parameters are given in tables A.17.5.2.3.1-1, A.17.5.2.3.1-2, and A.17.5.2.3.1-3 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.2.3.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.17.5.2.3.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

Table A.17.5.2.3.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | TDD duplex mode, 120 kHz SSB SCS, 100 MHz bandwidth |

Table A.17.5.2.3.1-2: General test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  | TestConfig. | Unit | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |  |
| Active PCell |  | 1 |  | Cell 1 |  |
| RF Channel Number |  | 1 |  | 1 |  |
| Duplex mode |  | 1 |  | TDD |  |
| TDD Configuration |  | 1 |  | TDDConf.3.1 |  |
| BWchannel |  | 1 |  | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  | 1 |  | 66 |  |
| PDSCH/PDCCH subcarrier spacing |  | 1 | kHz | 120 |  |
| DL initial BWP configuration |  | 1 |  | DLBWP.0.1 |  |
| DL dedicated BWP configuration |  | 1 |  | DLBWP.1.1 |  |
| UL initial BWP configuration |  | 1 |  | ULBWP.0.1 |  |
| UL dedicated BWP configuration |  | 1 |  | ULBWP.1.1 |  |
| PDSCH Reference Channel |  | 1 |  | SR.3.2 TDD |  |
| RMSI CORESET Reference Channel |  | 1 |  | CR.3.1 TDD |  |
| Dedicated CORESET Reference Channel |  | 1 |  | CCR.3.1 TDD |  |
| OCNG parameters |  | 1 |  | OP.1 |  |
| CP length |  | 1 |  | Normal |  |
| PDSCH/PDCCH TCI state |  | 1 |  | TCI.State.0 |  |
| CSI-RS for tracking |  | 1 |  | TRS.2.1 TDD |  |
| SSB Configuration |  | 1 |  | SSB.1 FR2 |  |
| SMTC Configuration |  | 1 |  | SMTC.3 |  |
| PRACH Configuration |  | 1 |  | FR2 PRACH configuration 4 | A.3.8.3.4 |
| DRX configuration |  | 1 |  | OFF |  |
| CSI-RS configuration for BFD/CBD/RLM |  | 1 |  | CSI-RS.3.2 TDD | A.3.14.2 |
| CSI-RS index assigned as BFD RS (q0) |  | 1 |  | 0 |  |
| CSI-RS index assigned as CBD RS (q1) |  | 1 |  | 1 |  |
| CSI-RS index assigned as RLM RS |  | 1 |  | 0,1 |  |
| Beam failure detection transmission parameters | DCI format | 1 |  | 1-0 |  |
|  | Number of Control OFDM symbols | 1 |  | 2 |  |
|  | Aggregation level | 1 | CCE | 8 |  |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy | 1 | dB | 0 |  |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy | 1 | dB | 0 |  |
|  | DMRS precoder granularity | 1 |  | REG bundle size |  |
|  | REG bundle size | 1 |  | 6 |  |
| Gap pattern ID |  | 1 |  | N/A |  |
| rlmInSyncOutOfSyncThreshold |  | 1 |  | absent | Value 0 is applied. (Table 8.1.1-1). |
| rsrp-ThresholdSSB |  | 1 | dBm/SCS | -95 | Threshold used for Qin_LR_SSB |
| powerControlOffsetSS |  | 1 |  | db0 | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  | 1 |  | n1 | see TS 38.321 [7], clause 5.17 |
| beamFailureDetectionTimer |  | 1 |  | pbfd4 | see TS 38.321 [7], clause 5.17 |
| CSI-RS configuration for CSI reporting |  | 1 |  | CSI-RS.3.1 TDD | A.3.14.2 |
| reportConfigType |  | 1 |  | periodic |  |
| reportQuantity |  | 1 |  | cri-RI-PMI-CQI |  |
| CSI reporting periodicity |  | 1 | slot | 40 |  |
| CSI reporting offset |  | 1 | slot | 4 |  |
| T310 |  | 1 | ms | 1000 |  |
| N310 |  | 1 |  | 2 |  |
| T1 |  | 1 | s | 1 | The UE shall be fully synchronized to Cell 1 during T1 |
| T2 |  | 1 | s | 1.17 |  |
| T3 |  | 1 | s | 0.9 |  |
| T4 |  | 1 | s | 0 |  |
| T5 |  | 1 | s | 0.31 |  |
| D1 |  | 1 | s | 0.27 |  |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |

Table A.17.5.2.3.1-3: Cell specific test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 |
| AoA setup |  |  | Setup 1 defined in A.3.15 |  |  |  |  |
| Assumptpion for UE beams Note 10 |  |  | Rough |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |
| SNR_CSI-RS of set q0 | Config 1 | dB | 5 Note 11 | -3 Note 11 | -12 | -12 | -12 |
| SNR_CSI-RS of set q1 | Config 1 | dB | 0.2 | 0.2 | 20.2 | 20.2 | 20.2 |
| CSI-RS_RP of set q1 | Config 1 | dBm/SCS | -104.5 | -104.5 | -84.5 | -84.5 | -84.5 |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | Config 1 | dBm/120 KHz | -104.7 |  |  |  |  |
| Propagation condition |  |  | TDL-A 30 ns 75 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: VoidNOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the REs carrying CSI-RS.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.7.5.5.3.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. NOTE 10:  Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 11: This value allows up to 1 dB degradation from applied SNR to UE baseband |  |  |  |  |  |  |  |

Editor notes: The Figure A.17.5.2.3.1-1 is missing

Figure A.17.5.2.3.1-1: SNR variation for CSI-RS based beam failure detection and link recovery testing in non-DRX mode

Figure A.17.5.2.3.1-2: CSI-RS_RP level variation for CSI-RS based beam failure detection and link recovery testing in non-DRX mode

##### A.17.5.2.3.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.17.5.2.4 Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode

##### A.17.5.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5B.

The test parameters are given in tables A.17.5.2.4.1-1, A.17.5.2.4.1-2, A.17.5.2.4.1-3, and A.17.5.2.4.1-4 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.2.4.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.17.5.2.4.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.17.5.2.4.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | TDD duplex mode, 120 kHz SSB SCS, 100 MHz bandwidth |

Table A.17.5.2.4.1-2: General test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

| Parameter |  | TestConfig. | Unit | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |  |
| Active PCell |  | 1 |  | Cell 1 |  |
| RF Channel Number |  | 1 |  | 1 |  |
| Duplex mode |  | 1 |  | TDD |  |
| TDD Configuration |  | 1 |  | TDDConf.3.1 |  |
| BWchannel |  | 1 |  | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  | 1 |  | 66 |  |
| PDSCH/PDCCH subcarrier spacing |  | 1 | kHz | 120 |  |
| DL initial BWP configuration |  | 1 |  | DLBWP.0.1 |  |
| DL dedicated BWP configuration |  | 1 |  | DLBWP.1.1 |  |
| UL initial BWP configuration |  | 1 |  | ULBWP.0.1 |  |
| UL dedicated BWP configuration |  | 1 |  | ULBWP.1.1 |  |
| PDSCH Reference Channel |  | 1 |  | SR.3.2 TDD |  |
| RMSI CORESET Reference Channel |  | 1 |  | CR.3.1 TDD |  |
| Dedicated CORESET Reference Channel |  | 1 |  | CCR.3.1 TDD |  |
| OCNG parameters |  | 1 |  | OP.1 |  |
| CP length |  | 1 |  | Normal |  |
| PDSCH/PDCCH TCI state |  | 1 |  | TCI.State.0 |  |
| CSI-RS for tracking |  | 1 |  | TRS.2.1 TDD |  |
| SSB Configuration |  | 1 |  | SSB.1 FR2 |  |
| SMTC Configuration |  | 1 |  | SMTC.3 |  |
| PRACH Configuration |  | 1 |  | FR2 PRACH configuration 4 | A.3.8.3.4 |
| DRX configuration |  | 1 |  | DRX.3 | A.3.3.3 |
| CSI-RS configuration for BFD/CBD/RLM |  | 1 |  | CSI-RS.3.2 TDD | A.3.14.2 |
| CSI-RS index assigned as BFD RS (q0) |  | 1 |  | 0 |  |
| CSI-RS index assigned as CBD RS (q1) |  | 1 |  | 1 |  |
| CSI-RS index assigned as RLM RS |  | 1 |  | 0,1 |  |
| Beam failure detection transmission parameters | DCI format | 1 |  | 1-0 |  |
|  | Number of Control OFDM symbols | 1 |  | 2 |  |
|  | Aggregation level | 1 | CCE | 8 |  |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy | 1 | dB | 0 |  |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy | 1 | dB | 0 |  |
|  | DMRS precoder granularity | 1 |  | REG bundle size |  |
|  | REG bundle size | 1 |  | 6 |  |
| Gap pattern ID |  | 1 |  | N/A |  |
| rlmInSyncOutOfSyncThreshold |  | 1 |  | absent | Value 0 is applied. (Table 8.1.1-1). |
| rsrp-ThresholdSSB |  | 1 | dBm/SCS | -95 | Threshold used for Qin_LR_SSB |
| powerControlOffsetSS |  | 1 |  | db0 | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  | 1 |  | n1 | see TS 38.321 [7], clause 5.17 |
| beamFailureDetectionTimer |  | 1 |  | pbfd4 | see TS 38.321 [7], clause 5.17 |
| CSI-RS configuration for CSI reporting |  | 1 |  | CSI-RS.3.1 TDD | A.3.14.2 |
| reportConfigType |  | 1 |  | periodic |  |
| reportQuantity |  | 1 |  | cri-RI-PMI-CQI |  |
| CSI reporting periodicity |  | 1 | slot | 40 |  |
| CSI reporting offset |  | 1 | slot | 4 |  |
| T310 |  | 1 | ms | 1000 |  |
| N310 |  | 1 |  | 2 |  |
| T1 |  | 1 | s | 1 | The UE shall be fully synchronized to Cell 1 during T1 |
| T2 |  | 1 | s | 5.43 |  |
| T3 |  | 1 | s | 5.16 |  |
| T4 |  | 1 | s | 0 |  |
| T5 |  | 1 | s | 0.31 |  |
| D1 |  | 1 | s | 0.27 |  |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |

Table A.17.5.2.4.1-3: Cell specific test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 |
| AoA setup |  |  | Setup 1 defined in A.3.15 |  |  |  |  |
| Assumption for UE beams Note 10 |  |  | Rough |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |
| SNR_CSI-RS of set q0 | Config 1 | dB | 5 Note 11 | -3 Note 11 | -12 | -12 | -12 |
| SNR_CSI-RS of set q1 | Config 1 | dB | 0.2 | 0.2 | 20.2 | 20.2 | 20.2 |
| CSI-RS_RP of set q1 | Config 1 | dBm/SCS | -104.5 | -104.5 | -84.5 | -84.5 | -84.5 |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | Config 1 | dBm/120 KHz | -104.7 |  |  |  |  |
| Propagation condition |  |  | TDL-A 30 ns 75 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: VoidNOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the REs carrying CSI-RS.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.7.5.5.4.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. NOTE 10:  Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 11: This value allows up to 1 dB degradation from applied SNR to UE baseband |  |  |  |  |  |  |  |

Figure A.17.5.2.4.1-1: SNR variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Figure A.17.5.2.4.1-2: CSI-RS_RP level variation for CSI-RS based beam failure detection and link recovery testing in DRX mode

##### A.17.5.2.4.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.17.5.2.5 Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode for 2 Rx UE

##### A.17.5.2.5.1 Test Purpose and Environment

The purpose is to test scheduling availability restrictions when the UE is performing beam failure detection or when the UE is performing L1-RSRP measurement for candidate beam detection, when no DRX is used. This test will verify the scheduling availability restriction requirements in clause 8.5B.7 and 8.5B.8.

The test parameters are given in tables A.17.5.2.5.1-1, A.17.5.2.5.1-2 and A.17.5.2.5.1-3 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.2.5.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.17.5.2.5.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. This test will focus on the scheduling availability during beam failure detection) and candidate beam detection. In the test, DRX configuration is not enabled. Test is to test the scheduling availability restriction of UE performing beam failure detection and candidate beam detection when SSB RS configured for Beam failure detection and candidate beam detection. During the test the UE is scheduled to transmit continuously in UL.

Table A.17.5.2.5.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.17.5.2.5.1-2: General test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  | TestConfig. | Unit | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |  |
| Active PCell |  | 1-2 |  | Cell 1 |  |
| RF Channel Number |  | 1-2 |  | 1 |  |
| Duplex mode |  | 1-2 |  | TDD |  |
| TDD Configuration |  | 1-2 |  | TDDConf.3.1 |  |
| BWchannel |  | 1-2 |  | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  | 1-2 |  | 66 |  |
| PDSCH/PDCCH subcarrier spacing |  | 1-2 | kHz | 120 |  |
| DL initial BWP configuration |  | 1-2 |  | DLBWP.0.1 |  |
| DL dedicated BWP configuration |  | 1-2 |  | DLBWP.1.1 |  |
| UL initial BWP configuration |  | 1-2 |  | ULBWP.0.1 |  |
| UL dedicated BWP configuration |  | 1-2 |  | ULBWP.1.1 |  |
| PDSCH Reference Channel |  | 1 |  | SR.3.2 TDD |  |
|  |  | 2 |  | SR.3.3 TDD |  |
| RMSI CORESET Reference Channel |  | 1 |  | CR.3.1 TDD |  |
|  |  | 2 |  | CR.3.2 TDD |  |
| Dedicated CORESET Reference Channel |  | 1 |  | CCR.3.1 TDD |  |
|  |  | 2 |  | CCR.3.7 TDD |  |
| OCNG parameters |  | 1-2 |  | OP.1 |  |
| CP length |  | 1-2 |  | Normal |  |
| PDSCH/PDCCH TCI state |  | 1-2 |  | TCI.State.0 |  |
| CSI-RS for tracking |  | 1-2 |  | TRS.2.1 TDD |  |
| SSB Configuration |  | 1 |  | SSB.1 FR2 |  |
|  |  | 2 |  | SSB.2 FR2 |  |
| SMTC Configuration |  | 1-2 |  | SMTC.1 |  |
| PRACH Configuration |  | 1-2 |  | FR2 PRACH configuration 2 | A.3.8.3.2 |
| DRX configuration |  | 1-2 |  | OFF |  |
| SSB index assigned as BFD RS (q0) |  | 1-2 |  | 0 |  |
| SSB index assigned as CBD RS (q1) |  | 1-2 |  | 1 |  |
| Beam failure detection transmission parameters | DCI format | 1-2 |  | 1-0 |  |
|  | Number of Control OFDM symbols | 1-2 |  | 2 |  |
|  | Aggregation level | 1-2 | CCE | 8 |  |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy | 1-2 | dB | 0 |  |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy | 1-2 | dB | 0 |  |
|  | DMRS precoder granularity | 1-2 |  | REG bundle size |  |
|  | REG bundle size | 1-2 |  | 6 |  |
| Gap pattern ID |  | 1-2 |  | N/A |  |
| rlmInSyncOutOfSyncThreshold |  | 1-2 |  | absent | Value 0 is applied. (Table 8.1.1-1). |
| rsrp-ThresholdSSB |  | 1 | dBm/SCS | -95 | Threshold used for Qin_LR_SSB |
|  |  | 2 |  | -92 |  |
| powerControlOffsetSS |  | 1-2 |  | db0 | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  | 1-2 |  | n1 | see TS 38.321 [7], clause 5.17 |
| beamFailureDetectionTimer |  | 1-2 |  | pbfd4 | see TS 38.321 [7], clause 5.17 |
| CSI-RS configuration for CSI reporting |  | 1-2 |  | CSI-RS.3.1 TDD |  |
| reportConfigType |  | 1-2 |  | periodic |  |
| reportQuantity |  | 1-2 |  | cri-RI-PMI-CQI |  |
| CSI reporting periodicity |  | 1-2 | slot | 40 |  |
| CSI reporting offset |  | 1-2 | slot | 4 |  |
| T310 |  | 1-2 | ms | 1000 |  |
| N310 |  | 1-2 |  | 2 |  |
| T1 |  | 1-2 | s | 1 | The UE shall be fully synchronized to Cell 1 during T1 |
| T2 |  | 1-2 | s | 2.6 |  |
| T3 |  | 1-2 | s | 1.64 |  |
| T4 |  | 1-2 | s | 0 |  |
| T5 |  | 1-2 | s | 1.01 |  |
| D1 |  | 1-2 | s | 0.97 |  |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |

Table A.17.5.2.5.1-3: Cell specific test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 |
| AoA Setup |  |  | Setup1 defined in clause A.3.15.1 |  |  |  |  |
| Assumption for UE beams Note 10 |  |  | Rough |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |
| SNR_SSB of set q0 | Config 1-2 | dB | 5Note 11 | -3Note 11 | -12 | -12 | -12 |
| SNR_SSB of set q1 | Config 1-2 | dB | 0.2 | 0.2 | 20.2 | 20.2 | 20.2 |
| SSB_RP of set q1 | Config 1 | dBm/SCS | -104.5 | -104.5 | -84.5 | -84.5 | -84.5 |
|  | Config 2 |  | -101.5 | -101.5 | -81.5 | -81.5 | -81.5 |
| ![](media_svg/image3.svg) [公式≈: ^{N}oc] | Config 1-2 | dBm/120 kHz | -104.7 |  |  |  |  |
| Propagation condition |  |  | TDL-A 30 ns 75 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: VoidNOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.17.5.2.5.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. NOTE 10: Information about types of UE beam given in annex B.2.1.3 and does not limit UE implementation or test system implementationNOTE 11: This value allows up to 1 dB degradation from applied SNR to UE baseband. |  |  |  |  |  |  |  |

Figure A.17.5.2.5.1-1: SNR variation SSB for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.17.5.2.5.1-2: SSB_RP level variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

##### A.17.5.2.5.2 Test Requirements

The UE behaviour during time duration T3 follows the requirements defined in clause 8.5B.7.3:

- The UE is not expected to transmit PUCCH/PUSCH/SRS or receive PDCCH/PDSCH/CSI-RS for tracking/CSI-RS for CQI on BFD-RS symbols to be measured for beam failure detection.

The UE behaviour during time durations T4 and T5 follows the requirements defined in clause 8.5B.8.3:

- The UE is not expected to transmit PUCCH/PUSCH or receive PDCCH/PDSCH on reference symbols to be measured for candidate beam detection.

### A.17.5.3 Active BWP switch for RedCap

#### A.17.5.3.1 DCI-based and Timer-based Active BWP Switch

##### A.17.5.3.1.1 NR FR2 DL active BWP switch with non-DRX in SA

###### A.17.5.3.1.1.1 Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6A. Supported test configurations are shown in table A.17.5.3.1.1.1-1.

The test scenario comprises of one cell (Cell 1) as given in table A.17.5.3.1.1.1-2. Cell-specific parameters of NR PCell is specified in table A.17.5.3.1.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.17.5.3.1.1.1-4.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.

Before the test starts,

- UE is connected to Cell 1 on radio channel 1.

- UE is configured with 2 different UE-specific downlink bandwidth parts, BWP-1 and BWP-2 before starting the test. BWP-1 include bandwidth of the initial DL BWP and SSB.

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1.

- UE is configured with a bwp-InactivityTimer timer value for Cell 1.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for DL BWP switch, sent from the test equipment to the UE, is received at the UE side in Cell 1’s slot # denoted i. The UE should switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s DL slot (i+TBWPswitchDelay) as defined in clause8.6A and starts to report valid ACK/NACK for the Cell 1 no later than the first UL slot that occurs after the beginning of slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on Cell 1’s BWP-2 starting from the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).

During T2, the test equipment won’t transmit DCI format for PDSCH reception on Cell 1.

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the half subframe immediately after bwp-InactivityTimer timer expires. The UE should switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s DL slot (j+TBWPswitchDelay) as defined in clause8.6A and starts to report valid ACK/NACK for the Cell 1 at latest on the first UL slot that occurs after the beginning of slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on Cell 1’s BWP-1 starting from the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

The test equipment verifies the DL BWP switch time by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK is received.

Table A.17.5.3.1.1.1-1: DL BWP switch supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.5.3.1.1.1-2: General test parameters for DL BWP switch in SA

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active Cell |  | Cell 1 | Cell on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| bwp-InactivityTimer | ms | [200] |  |
| T1 | s | [0.2] |  |
| T2 | s | [0.2] |  |
| T3 | s | [0.2] |  |

Table A.17.5.3.1.1.1-3: NR Cell specific test parameters for DL BWP switch in SA

| Parameter | Unit | Cell 1 |
| --- | --- | --- |
| Frequency Range |  | FR2 |
| Duplex mode |  | TDD |
| TDD configuration |  | TDDConf.3.1 |
| BWchannel |  | 100 MHz: NPRB,c = 66 |
| Active BWP ID |  | 1, 2 |
| Initial DL BWP Configuration |  | DLBWP.0.2 Note 2 |
| Active DL BWP-1 Configuration |  | DLBWP.1.1 Note 2 |
| Active DL BWP-2 Configuration |  | DLBWP.1.2 REDCAP Note 2 |
| Initial UL BWP Configuration |  | ULBWP.0.2 Note 2 |
| Active UL BWP-1 Configuration |  | ULBWP.1.1 Note 2 |
| Active UL BWP-2 Configuration |  | DLBWP.1.2 REDCAP Note 2 |
| PDSCH Reference measurement channel |  | SR.3.1 TDD |
| RMSI CORESET parameters |  | CR.3.1 TDD |
| Dedicated CORESET parameters |  | CCR.3.1 TDD |
| OCNG Patterns |  | OP.1 |
| SSB Configuration |  | SSB.1 FR2 |
| SMTC Configuration |  | SMTC.1 |
| TCI State |  | TCI.State.0 |
| TRS Configuration |  | TRS.2.1 TDD |
| Correlation Matrix and Antenna Configuration |  | 1x2 Low |
| EPRE ratio of PSS to SSS | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |
| Propagation Condition |  | AWGN |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: For unpaired spectrum, a DL BWP is linked with an UL BWP. DLBWP.0.2 is linked with ULBWP.0.2; DLBWP.1.1 is linked with ULBWP.1.1; DLBWP.1.2 REDCAP is linked with ULBWP.1.3 defined in clause 12 of TS 38.213 [3]. |  |  |

Table A.17.5.3.1.1.1-4: OTA related test parameters for DL BWP switch in SA

| Parameter | Unit | Cell 2 |
| --- | --- | --- |
| Angle of arrival configuration |  | Setup 1 defined in clause A.3.15.1 |
| Assumption for UE beams Note 6 |  | Fine |
| NocNote 1 | dBm/15 kHz | -112 |
| NocNote 1 | dBm/SCS | -103 |
| SS-RSRP Note 2 | dBm/120 kHz Note3 | -85 |
| Ês/Iot | dB | 18 |
| Ês/Noc Note 5 | dB | 18 |
| IoNote2 | dBm/95.04 MHz Note4 | -56 |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 2: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 6: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation. |  |  |

###### A.17.5.3.1.1.2 Test Requirements

During T1, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6A.2-1.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first UL slot that occurs after the beginning of DL slot (i+ TBWPswitchDelay+k1), (j+ TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

#### A.17.5.3.2 RRC-based Active BWP Switch

##### A.17.5.3.2.1 NR FR2 DL active BWP switch of PCell with non-DRX in SA

###### A.17.5.3.2.1.1 Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6A.3. Supported test configurations are shown in table A.17.5.3.2.1.1-1.

The test scenario comprises of one Cell (Cell 1) as given in table A.17.5.3.2.1.1-2. Cell-specific parameters of Cell 1 are specified in table A.17.5.3.2.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.

Before the test starts,

- UE is connected to Cell 1 on radio channel 1.

- UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1.

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in Cell 1.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is received at the UE side in PSCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition.

The UE shall be able to completely receive PDSCH on Cell 1 from the first DL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}$ as defined in clause 8.6A.3 and starts to report valid ACK/NACK for the Cell 1 from the first UL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}+k1 $. The UE shall be continuously scheduled on PSCell’s BWP-1 starting from the first DL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}$.

TRRCprocessingDelay and TBWPswitchDelayRRC are defined in clause8.6A.3.

The test equipment verifies the DL BWP switch time in PSCell by counting the time from the time when the RRC Reconfiguration message including updated BWP configurationis sent till the time when RRC Reconfiguration Complete message is received.

Table A.17.5.3.2.1.1-1: DL BWP switch supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | NR 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.17.5.3.2.1.1-2: General test parameters for DL BWP switch in SA

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active PCell |  | Cell 1 | PCell on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| Cell-individual offset for cells on RF channel number 1 | dB | 0 |  |
| T1 | s | [0.2] |  |

Table A.17.5.3.2.1.1-3: NR Cell specific test parameters for DL BWP switch in SA

| Parameter |  | Unit | Cell 1 |
| --- | --- | --- | --- |
| Frequency Range |  |  | FR2 |
| Duplex mode |  |  | TDD |
| TDD configuration |  |  | TDDConf.3.1 |
| BWchannel |  |  | 100 MHz: NPRB,c = 66 |
| Active BWP ID |  |  | 1 |
| Initial Condition | Active DL BWP-1 Configuration |  | DLBWP.1.2 REDCAP |
|  | Active UL BWP-1 Configuration |  | ULBWP.1.3 |
| FinalCondition | Active DL BWP-1 Configuration |  | DLBWP.1.1 |
|  | Active UL BWP-1 Configuration |  | ULBWP.1.1 |
| 'PDSCH Reference measurement channel |  |  | SR.3.1 TDD |
| RMSI CORESET parameters |  |  | CR.3.1 TDD |
| Dedicated CORESET parameters |  |  | CCR.3.1 TDD |
| OCNG Patterns |  |  | OP.1 |
| SSB Configuration |  |  | SSB.1 FR2 |
| SMTC Configuration |  |  | SMTC.1 |
| TCI State |  |  | TCI.State.0 |
| TRS Configuration |  |  | TRS.2.1 TDD |
| Antenna Configuration |  |  | 1x2 |
| Propagation Condition |  |  | AWGN |
| EPRE ratio of PSS to SSS |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For unpaired spectrum, a DL BWP is linked with an UL BWP. DLBWP.0.2 is linked with ULBWP.0.2; DLBWP.1.1 is linked with ULBWP.1.1; DLBWP.1.2 REDCAP is linked with ULBWP.1.3 defined in clause 12 of TS 38.213 [3]. |  |  |  |

Table A.17.5.3.2.1.1-4: OTA related test parameters for BWP switching test case

| Parameter |  | Unit | Cell 2 |
| --- | --- | --- | --- |
| Angle of arrival configuration |  |  | Setup 1 according to table A.3.15 |
| Assumption for UE beams Note 5 |  |  | Fine |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | NR_TDD_FR2_A | dBm/15 kHz | -112 |
|  | NR_TDD_FR2_B |  |  |
|  | NR_TDD_FR2_F |  |  |
|  | NR_TDD_FR2_G |  |  |
|  | NR_TDD_FR2_T |  |  |
|  | NR_TDD_FR2_Y |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | NR_TDD_FR2_A | dBm/SCS | -103 |
|  | NR_TDD_FR2_B |  |  |
|  | NR_TDD_FR2_F |  |  |
|  | NR_TDD_FR2_G |  |  |
|  | NR_TDD_FR2_T |  |  |
|  | NR_TDD_FR2_Y |  |  |
| SS-RSRPNote2 | NR_TDD_FR2_A | dBm/SCS Note3 | -85 |
|  | NR_TDD_FR2_B |  |  |
|  | NR_TDD_FR2_F |  |  |
|  | NR_TDD_FR2_G |  |  |
|  | NR_TDD_FR2_T |  |  |
|  | NR_TDD_FR2_Y |  |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 18 |
| IoNote2 | NR_TDD_FR2_A | dBm/95.04 MHz Note4 | -56 |
|  | NR_TDD_FR2_B |  |  |
|  | NR_TDD_FR2_F |  |  |
|  | NR_TDD_FR2_G |  |  |
|  | NR_TDD_FR2_T |  |  |
|  | NR_TDD_FR2_Y |  |  |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5:  Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation. |  |  |  |

###### A.17.5.3.2.1.2 Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PCell from the first DL slot that occurs after the beginning of slot $ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}$ and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}+k1 $.

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

### A.17.5.4 Active TCI state switch delay

#### A.17.5.4.1 MAC-CE based active TCI state switch

##### A.17.5.4.1.1 NR PCell FR2 active TCI state switch for a known TCI state

###### A.17.5.4.1.1.1 Test Purpose and Environment

The purpose of this test is to verify the active TCI state switch delay requirement defined in clause 8.10B.3. Supported test configuration is shown in table A.17.5.4.1.1.1-1.

The test scenario comprises of one NR PCell (Cell 1) as given in table A.17.5.4.1.1.1-2. Cell-specific parameters of NR PCell are specified in table A.17.5.4.1.1.1-3 below. The OTA related test parameters for FR2 are shown in table A.17.5.4.1.1.1-4.

PDCCHs indicating new transmissions shall be sent continuously on PCell to ensure that the UE would have ACK/NACK sending.

Before the test starts,

- UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

- UE is configured with 2 different TCI states for PCell, PDCCH TCI state 0 (QCL’d to SSB0) and TCIstate 1 (QCL’d to SSB1), in Cell 1 before starting the test.

- UE is indicated in TCI state 0 as the active PDCCH TCI state

The test consists of two time periods, T1 and T2. Figure A.17.5.4.1.1.1-1 and Figure A.17.5.4.1.1.1-2 show the Time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival. During T1 only SSB to which PDCCH-TCI-state0 is QCL’d is transmitted. At the beginning of T2, the SSB corresponding to TCI state 1 starts transmitting. The UE is configured to provide periodic L1-RSRP reports. In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 and SSB1, UE receives a MAC-CE command indicating a switch to TCI state 1. tci-PresentInDCI is not configured in the PDSCH configuration, i.e. TCI state for the PDSCH is identical to the PDCCH TCI state.

The test equipment verifies that UE can be scheduled on PCell on TCI state 0 till n+ THARQ +3 ms. The test equipment also verifies the TCI state switch time in PCell by scheduling the UE on TCI state 1 after n+ THARQ +3 ms + (Tfirst-SSB + TSSB-proc).

Table A.17.5.4.1.1.1-1: Supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.5.4.1.1.1-2: General test parameters for TCI state switch

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active PCell |  | Cell 1 | PCell on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| T1 | s | 0.2 |  |
| T2 | s | 0.2 |  |

Table A.17.5.4.1.1.1-3: NR Cell specific test parameters for TCI state switch

| Parameter | Unit | Cell 1 |
| --- | --- | --- |
| Frequency Range |  | FR2 |
| Duplex mode |  | TDD |
| TDD configuration |  | TDDConf.3.1 |
| BWchannel |  | 100 MHz: NPRB,c = 66 |
| Data PRBs allocated |  | 24 |
| Initial DL BWP Configuration |  | DLBWP.0.2 |
| Dedicated DL BWP Configuration |  | DLBWP.1.1 |
| Initial UL BWP Configuration |  | ULBWP.0.2 |
| Dedicated UL BWP Configuration |  | ULBWP.1.1 |
| PDSCH Reference measurement channel |  | SR.3.2 TDD |
| RMSI CORESET parameters |  | CR.3.1 TDD |
| Dedicated CORESET parameters |  | CCR.3.1 TDD |
| OCNG Patterns |  | OP.5 |
| SSB Configuration |  | SSB.1 FR2 |
| SMTC Configuration |  | SMTC.1 |
| TCI State 0 |  | TCI.State.0 |
| TCI State 1 |  | TCI.State.1 |
| TRS Configuration |  | TRS.2.1 TDD |
| Correlation Matrix and Antenna Configuration |  | 1x2 Low |
| EPRE ratio of PSS to SSS | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |
| Propagation Condition |  | No external noise (Note 2) |
| NOTE 1: OCNG shall be used such that a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The downlink connection between the System Simulator and the UE is without Additive White Gaussian Noise, and has no fading or multipath effects as specified in TS 38.521-2 B.0 [29]. |  |  |

Table A.17.5.4.1.1.1-4: OTA related test parameters for TCI state switch

| Parameter | Unit | Cell 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | SSB0 |  | SSB1 |  |  |
|  |  | T1 | T2 | T1 |  | T2 |
| Angle of arrival configuration |  | Setup 3 according to clause A.3.15.3 |  |  |  |  |
|  |  | AoA1 |  |  | AoA2 |  |
| Assumption for UE beams Note 6 |  | Rough |  |  |  |  |
| Ês | dBm/SCS | -80.6 | -80.6 | -Infinity |  | -80.6 |
| SS B_RP Note 2 | dBm/ SCS | -80.6 | -80.6 | -Infinity |  | -80.6 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot]BB Note 7 | dB | 8.3 | 8.3 | -Infinity |  | 8.3 |
| IoNote2 | dBm/95.04 MHz Note4 | -56.0 | -56.0 | - Infinity |  | -56.0 |
| NOTE 1: VoidNOTE 2: SS B_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: VoidNOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the center of the quiet zone.NOTE 6:  Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 7: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] Table 6.2.1.3-4. |  |  |  |  |  |  |

![](media/image23.emf)

Figure A.17.5.4.1.1.1-1: Time multiplexed downlink transmissions during T1

![](media/image24.emf)

Figure A.17.5.4.1.1.1-2: Time multiplexed downlink transmissions during T2

###### A.17.5.4.1.1.2 Test Requirements

During T2, UE shall send L1-RSRP report with results for both SSB0 and SSB1.

After receiving MAC-CE command in slot n, UE shall:

- be able to continue to receive on TCI state 0 till   n+ THARQ +3 ms

- be able to start receiving on TCI state 1 after n+ THARQ +5 ms + Tfirst-SSB

#### A.17.5.4.2 RRC based active TCI state switch

##### A.17.5.4.2.1 NR PCell FR2 active TCI state switch for a known TCI state

###### A.17.5.4.2.1.1 Test Purpose and Environment

The purpose of this test is to verify the active TCI state switch delay requirement defined in clause 8.10B.5. Supported test configuration is shown in table A.17.5.4.2.1.1-1.

The test scenario comprises of one NR PCell as given in table A.17.5.4.2.1.1-2. Cell-specific parameters of NR PCell is specified in table A.17.5.4.2.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.17.5.4.2.1.1-4.

PDCCHs indicating new transmissions shall be sent continuously on PCell to ensure that the UE would have ACK/NACK sending.

Before the test starts,

- UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

- UE is configured with 1 TCI state for PCell, PDCCH-TCI-state0 (QCL’d to SSB0)

- UE is indicated in TCI state0 as the active TCI state

The test consists of two time periods, T1 and T2. Figure A.17.5.4.2.1.1-1-1 and Figure A.17.5.4.2.1.1-1-2 show the Time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival. During T1 only SSB to which TCI-state0 is QCL’d is transmitted. At the beginning of T2, the SSB corresponding to TCI-state1 starts transmitting. The UE is configured to provide periodic L1-RSRP reports.  In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 and SSB1, UE receives a RRC command indicating a switch to TCI-state1.

The test equipment verifies the TCI state switch time in PCell by scheduling the UE on TCI state 1 after n+ TRRC_processing  + Tfirst-SSB + 2 ms.

Table A.17.5.4.2.1.1-1-1: Supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.5.4.2.1.1-1-2: General test parameters for TCI state switch

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active PCell |  | Cell 1 | PCell on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| T1 | s | 0.2 |  |
| T2 | s | 2 |  |

Table A.17.5.4.2.1.1-1-3: NR Cell specific test parameters for TCI state switch

| Parameter | Unit |  |
| --- | --- | --- |
| Frequency Range |  | FR2 |
| Duplex mode |  | TDD |
| TDD configuration |  | TDDConf.3.1 |
| BWchannel |  | 100 MHz: NPRB,c = 66 |
| Data PRBs allocated |  | 24 |
| Initial DL BWP Configuration |  | DLBWP.0.2 |
| Dedicated DL BWP Configuration |  | DLBWP.1.1 |
| Initial UL BWP Configuration |  | ULBWP.0.2 |
| Dedicated UL BWP Configuration |  | ULBWP.1.1 |
| PDSCH Reference measurement channel |  | SR.3.2 TDD |
| RMSI CORESET parameters |  | CR.3.1 TDD |
| Dedicated CORESET parameters |  | CCR.3.1 TDD |
| OCNG Patterns |  | OP.5 |
| SSB Configuration |  | SSB.1 FR2 |
| SMTC Configuration |  | SMTC.1 |
| TCI State 0 |  | TCI.State.0 |
| TCI State 1 |  | TCI.State.1 |
| reportConfigType |  | ssb-Index-RSRP |
| reportConfigType |  | periodic |
| Number of reported RS |  | 2 |
| L1-RSRP reporting period | slot | 640 |
| timeRestrictionForChannelMeasurements |  | configured |
| TRS Configuration |  | TRS.2.1 TDDTRS.2.2 TDD |
| Correlation Matrix and Antenna Configuration |  | 1x2 Low |
| EPRE ratio of PSS to SSS | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |
| Propagation Condition |  | No external noise (Note 2) |
| NOTE 1: OCNG shall be used such that a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The downlink connection between the System Simulator and the UE is without Additive White Gaussian Noise, and has no fading or multipath effects as specified in TS 38.521-2 B.0 [29]. |  |  |

Table A.17.5.4.2.1.1-1-4: OTA related test parameters for TCI state switch

| Parameter | Unit | Cell 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | SSB0 |  | SSB1 |  |  |
|  |  | T1 | T2 | T1 |  | T2 |
| Angle of arrival configuration |  | Setup 3 according to clause A.3.15.3 |  |  |  |  |
|  |  | AoA1 |  |  | AoA2 |  |
| Assumption for UE beams Note 6 |  | Rough |  |  |  |  |
| Ês | dBm/SCS | -80.6 | -80.6 | -Infinity |  | -80.6 |
| SS B_RP Note 2 | dBm/ SCS | -80.6 | -80.6 | -Infinity |  | -80.6 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot]BB Note 7 | dB | 8.3 | 8.3 | -Infinity |  | 8.3 |
| IoNote2 | dBm/95.04 MHz Note4 | -6.0 | -56.0 | - Infinity |  | -56.0 |
| NOTE 1: VoidNOTE 2: SS B_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: VoidNOTE 4:  Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the center of the quiet zone.NOTE 6: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation.NOTE 7: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] Table 6.2.1.3-4. |  |  |  |  |  |  |

![](media/image23.emf)

Figure A.17.5.4.2.1.1-1-1: Time multiplexed downlink transmissions during T1

![](media/image24.emf)

Figure A.17.5.4.2.1.1-1-2: Time multiplexed downlink transmissions during T2

###### A.17.5.4.2.1.2 Test Requirements

During T2, UE shall send L1-RSRP report with both SSB0 and SSB1.

After receiving RRC command in slot n, UE shall be able to start receiving on TCI state 1 after n+ TRRC_processing  + Tfirst-SSB + 2 ms.

### A.17.5.5 Uplink spatial relation switch delay

#### A.17.5.5.1 MAC-CE based Spatial Relation switch

##### A.17.5.5.1.1  NR PCell FR2 spatial relation associated with known DL-RS

###### A.17.5.5.1.1.1 Test Purpose and Environment

The purpose of this test is to verify fulfillment of the uplink spatial relation switch delay requirement defined in clause 8.12A.3 by a UE capable of beam correspondence without the need for UL beam sweeping. The supported test configurations are shown in table A.17.5.5.1.1.1-1.

The test scenario comprises one PCell (Cell 1) as outlined in table A.17.5.5.1.1.1-2. Cell-specific parameters are provided in table A.17.5.5.1.1.1-3. OTA-related test parameters are provided in table A.17.5.5.1.1.1-4.

Throughout the test, PDCCH indicating new transmissions shall ge sent continuously on PCell to ensure that the UE will send ACK/NACKs on PUCCH.

Before the test starts,

- UE is connected to Cell 1 on radio channel 1.

- UE is configured with a single TCI state, TCI State-0, which is QCLed with SSB0.

- UE is configured with two spatial relation information configurations Spatial Relation Info-0 and Spatial Relation Info-1 for PUCCH, each associated with SSB0 and SSB1, respectively.

- UE is indicated via MAC-CE activation of PUCCH-SpatialRelationInfoId corresponding to Spatial Relation Info-0

- UE is configured with a CSI measurement configuration indicating L1-RSRP measurements on SSB0 and SSB1 with periodic reporting. The L1-RSRP measurement period is influenced by the following: the higher layer parameter timeRestrictionForChannelMeasurement is configured, measured SSBs are fully overlapping with SMTC window, and there are no conflicts with measurement gaps.

The test consists of two time periods, T1 and T2. During T1 only the SSB associated with PDCCH TCI state-0 and PUCCH Spatial Relation Info-0 is transmitted. At the beginning of T2, transmission of the SSB associated with PUCCH Spatial Relation Info-1 starts. The UE conducts periodic L1-RSRP measurements and SSB-Index-RSRP reporting for SSB0 and SSB1. In slot n, which is within 1280 ms after UE receiving both SSB0 and SSB1, and after reporting valid results for both the SSB0 and the SSB1, the UE receives a MAC-CE indicating a switch of spatial relation to PUCCH Spatial Relation Info 1.

The test equipment verifies that the UE transmits according to PUCCH Spatial Relation Info 0 up until slot n + THARQ/NR slot length + $ 3N_{slot}^{subframe,µ}$, and according to PUCCH Spatial Relation Info 1 from slot n + THARQ/NR slot length + $ 3N_{slot}^{subframe,µ}$ + 1 and onwards.

Table A.17.5.5.1.1.1-1: Supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.5.5.1.1.1-2: General test parameters

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active PCell |  | Cell 1 | PCell on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| L1-RSRP reporting period | slot | 160 | Periodic L1-RSRP reporting configured |
| L1-RSRP measured RS |  | SSB0, SSB1 | L1-RSRP measurements of SSB0 and SSB1. |
| Number of reported RS |  | 2 | L1-RSRP reporting of measurements on SSB0 and SSB1. |
| T1 | s | [0.2] |  |
| T2 | s | [2] |  |

A.17.5.5.1.1.1: NR Cell specific test parameters

| Parameter | Unit | Cell 1 |
| --- | --- | --- |
| Frequency Range |  | FR2 |
| Duplex mode |  | TDD |
| TDD configuration |  | TDDConf.3.1 |
| BWchannel |  | 100 MHz: NPRB,c = 66 |
| Initial DL BWP Configuration |  | DLBWP.0.2 |
| Dedicated DL BWP Configuration |  | DLBWP.1.1 |
| Initial UL BWP Configuration |  | ULBWP.0.2 |
| Dedicated UL BWP Configuration |  | ULBWP.1.1 |
| PDSCH Reference measurement channel |  | SR.3.1 TDD |
| RMSI CORESET parameters |  | CR.3.1 TDD |
| Dedicated CORESET parameters |  | CCR.3.1 TDD |
| OCNG Patterns |  | OP.1 |
| SSB Configuration |  | SSB.1 FR2 |
| SMTC Configuration |  | SMTC.1 |
| TCI State-0 Configuration |  | TCI.State.0 |
| reportConfigType |  | ssb-Index-RSRP |
| reportConfigType |  | periodic |
| timeRestrictionForChannelMeasurements |  | configured |
| TRS Configuration |  | TRS.2.1 TDD |
| Spatial Relation Info-0 Configuration |  | PUCCH.SRI.0 |
| Spatial Relation Info-1 Configuration |  | PUCCH.SRI.1 |
| Correlation Matrix and Antenna Configuration |  | 1x2 Low |
| EPRE ratio of PSS to SSS | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |
| EPRE ratio of OCNG to OCNG DMRSNote 1 |  |  |
| Propagation Condition |  | AWGN |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |

Table A.17.5.5.1.1.1-4: OTA related test parameters

| Parameter | Unit | Cell 1 |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | SSB0 |  | SSB1 |  |
|  |  | T1 | T2 | T1 | T2 |
| Angle of arrival configuration |  | Setup 3 according to clause A.3.15.3 |  |  |  |
|  |  | AoA1 |  | AoA2 |  |
| Assumption for UE beams Note 6 |  | Rough |  |  |  |
| NocNote 1 | dBm/15 kHz | -92.1 |  |  |  |
| NocNote 1 | dBm/SCS | -83.1 |  |  |  |
| Ês/Noc | dB | 1 |  | -infinity | 1 |
| SS-RSRP Note 2 | dBm/120 kHz Note3 | -82.1 |  | -infinity | -82.1 |
| IoNote2 | dBm/95.04 MHz Note4 | -50.6 |  | -54.1 | -50.6 |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 2: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the center of the quiet zone.NOTE 6:  Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation. |  |  |  |  |  |

###### A.17.5.5.1.1.2 Test Requirements

During T2, the UE shall send L1-RSRP report with results for SSB0 and SSB1.

After receiving MAC-CE command in slot n, the UE shall:

- Continue transmitting using PUCCH spatial relation associated with SSB0 up to and including slot n + THARQ/NR slot length + $ 3N_{slot}^{subframe,µ}$

- Start transmitting using PUCCH spatial relation associated with SSB1 from slot n + THARQ/NR slot length + $ 3N_{slot}^{subframe,µ}$ + 1 and onwards.

The rate of correct events observed during repeated tests shall be at least [90]%.

#### A.17.5.5.2 RRC based spatial relation switch

##### A.17.5.5.2.1 NR PCell FR2 spatial relation switch associated with a known DL-RS

A.17.5.5.2.1.1 Test Purpose and Environment

The purpose of this test is to verify the RRC based spatial relation switch delay requirement defined in clause 8.12A.5 by a UE capable of beam correspondence without the need for UL beam sweeping. In the test the higher layer parameter timeRestrictionForChannelMeasurements is configured. Supported test configuration is shown in table A.17.5.5.2.1.1-1.

The test scenario comprises of one PCell (Cell 1) as given in table A.17.5.5.2.1.1-2. Cell-specific parameters of PCell is specified in table A.17.5.5.2.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.17.5.5.2.1.1-4.

Periodic SRS is transmitted on PCell (Cell 1), and the SRS configuration is SRSConf.1 given in table A.5.4.1.1.1-3.

Before the test starts,

- UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

- UE is configured with 1 SRS-SpatialRelation0 associated with SSB0.

- UE is indicated SRS-SpatialRelation0 as the active SRS spatial relation.

The test consists of two time periods, T1 and T2. During T1 only SSB0 to which SRS-SpatialRelation0 associated is transmitted. UE shall transmit periodic SRS with SRS-SpatialRelation0 on the UL of the PCell.

T2 start when the tester initiates transmission of SSB1 corresponding to SRS-SpatialRelation1. The UE is configured to transmit periodic L1-RSRP reports.

In slot n, which is within [1280]ms of UE providing the L1-RSRP report with results for both SSB0 and SSB1, the UE receives an RRC command indicating a switch to transmit periodic SRS with target SRS-SpatialRelation1. The UE shall be able to transmit periodic SRS with target spatial relation (SRS-SpatialRelation1) on PCell in slot n + TRRC_processing/NR slot length +1.

Table A.17.5.5.2.1.1-1: Supported test configurations

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.5.5.2.1.1-2: General test parameters for spatial relation switch associated with a known DL-RS

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active PCell |  | Cell 1 | PCell on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| Cell-individual offset for cells on RF channel number 1 | dB | 0 | Individual offset for cells on PCC. |
| timeRestrictionForChannelMeasurements |  | configured | Time domain measurement restriction for the channel (signal) measurements (see TS 38.214 [19], clause 5.2.1.1) |
| T1 | s | 0.5 |  |
| T2 | s | 1.5 |  |

Table A.17.5.5.2.1.1-3: NR Cell specific test parameters for spatial relation switch associated with a known DL-RS

| Parameter | Unit | Cell 1 |
| --- | --- | --- |
| Frequency Range |  | FR2 |
| Duplex mode |  | TDD |
| TDD configuration |  | TDDConf.3.1 |
| BWchannel |  | 100 MHz: NPRB,c = 66 |
| Initial DL BWP Configuration |  | DLBWP.0.2 |
| Dedicated DL BWP Configuration |  | DLBWP.1.1 |
| Initial UL BWP Configuration |  | ULBWP.0.2 |
| Dedicated UL BWP Configuration |  | ULBWP.1.1 |
| PDSCH Reference measurement channel |  | SR.3.1 TDD |
| RMSI CORESET parameters |  | CR.3.1 TDD |
| Dedicated CORESET parameters |  | CCR.3.1 TDD |
| OCNG Patterns |  | OP.1 |
| SSB Configuration |  | SSB.1 FR2 |
| SMTC Configuration |  | SMTC.1 |
| SRS-SpatialRelation0 |  | SRS.SRI0 |
| SRS-SpatialRelation1 |  | SRS.SRI1 |
| reportConfigType |  | ssb-Index-RSRP |
| reportConfigType |  | periodic |
| Number of reported RS |  | 2 |
| L1-RSRP reporting period | slot | 160 |
| TRS Configuration |  | TRS.2.1 TDD |
| Correlation Matrix and Antenna Configuration |  | 1x2 Low |
| EPRE ratio of PSS to SSS | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |
| Propagation Condition |  | AWGN |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |

Table A.17.5.5.2.1.1-4: OTA related test parameters for spatial relation switch associated with a known DL-RS

| Parameter | Unit | Cell 1 |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | SSB0 |  | SSB1 |  |
|  |  | T1 | T2 | T1 | T2 |
| Angle of arrival |  | Setup 3 according to clause A.3.15.3 |  |  |  |
| configuration |  | AoA1 |  | AoA2 |  |
| Assumption for UE beamsNote 6 |  | Rough |  | Rough |  |
| NocNote 1 | dBm/15 kHz | -92.1 |  |  |  |
| NocNote 1 | dBm/SCS | -83.1 |  |  |  |
| Ês/Noc | dB | 1 | 1 | -Infinity | 1 |
| SS-RSRP Note 2 | dBm/120 kHz Note3 | -82.1 | -82.1 | -Infinity | -82.1 |
| IoNote2,Note6 | dBm/95.04 MHz Note4 | -50.6 | -50.6 | -54.1 | -50.6 |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 2: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 4:  Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the center of the quiet zone.NOTE 6: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |

###### A.17.5.5.2.1.2 Test Requirements

During T1 UE shall send L1-RSRP report with SSB0 to which SRS-SpatialRelation0 is associated. During T2, UE shall send L1-RSRP report with SSB1 to which SRS-SpatialRelation1 is associated.

After receiving RRC command in slot n, UE shall be able to transmit target periodic SRS with SRS-SpatialRelation1 on the PCell in the slot n +  TRRC_processing/NR slot length + 1.

The rate of correct events observed during repeated tests shall be at least 90 %.

### A.17.5.6 UE specific CBW change

#### A.17.5.6.1 NR FR2 UE specific CBW change of PCell with non-DRX in SA

##### A.17.5.6.1.1 Test Purpose and Environment

The purpose of this test is to verify the UE specific CBW change delay requirement defined in clause 8.13A. Supported test configurations are shown in table A.17.5.6.1.1-1.

The test scenario comprises of one PCell (Cell 1) as given in table A.17.5.6.1.1-2. Cell-specific parameters of PCell are specified in table A.17.5.6.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK transmission.

Before the test starts,

- UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

- UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1 (PCell).

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PCell.

- UE has been configured with UE-specific CBW (CBW-1)

- UE is indicated in SCS-SpecificCarrier [2] that the UE-specific CBW is CBW-1 as the initial condition in Cell 1 (PCell).

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated CBW configuration, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its CBW with the updated CBW of final condition.

The UE shall be able to completely receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}$ as defined in clause 8.13.2 and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}+k1 $. The UE shall be continuously scheduled on PCell’s new CBW starting from the first DL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}$.

TRRCprocessingDelay and TCBWchangeDelayRRC are defined in clause8.13A.

The test equipment verifies the UE specific CBW switch time in PCell by counting the time from the time when the RRC Reconfiguration message including updated CBW configurations sent till the time when RRC Reconfiguration Complete message is received.

Table A.17.5.6.1.1-1: UE specific CBW change supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | NR 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.17.5.6.1.1-2: General test parameters for UE specific CBW change in NR SA

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active PCell |  | Cell 1 | PCell on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| Cell-individual offset for cells on RF channel number 1 | dB | 0 | Individual offset for cells on PCC. |
| T1 | s | [0.2] |  |

Table A.17.5.6.1.1-3: NR Cell specific test parameters for UE specific CBW change in NR SA

| Parameter |  | Unit | Cell 1 |
| --- | --- | --- | --- |
| Frequency Range |  |  | FR2 |
| Duplex mode |  |  | TDD |
| TDD configuration |  |  | TDDConf.3.1 |
| BWchannel |  |  | 100 MHz: NPRB,c = 66 |
| Active DL BWP ID |  |  | 1 |
| Initial DL BWP Configuration (BWP-1) |  |  | DLBWP.0.2 |
| Initial UL BWP Configuration |  |  | ULBWP.0.2 |
| Initial Condition | Active DL CBW-1 Configuration |  | DLCBW.1.1 |
|  | Active UL CBW-1 Configuration |  | ULCBW.1.1 |
| Final Condition | Active DL CBW-1 Configuration |  | DLCBW.1.2 |
|  | Active UL CBW-1 Configuration |  | ULCBW.1.2 |
| 'PDSCH Reference measurement channel |  |  | SR.3.1 TDD |
| RMSI CORESET parameters |  |  | CR.3.1 TDD |
| Dedicated CORESET parameters |  |  | CCR.3.1 TDD |
| OCNG Patterns |  |  | OP.1 |
| SSB Configuration |  |  | SSB.1 FR2 |
| SMTC Configuration |  |  | SMTC.1 |
| TCI State |  |  | TCI.State.0 |
| TRS Configuration |  |  | TRS.2.1 TDD |
| Antenna Configuration |  |  | 1x2 |
| Propagation Condition |  |  | AWGN |
| EPRE ratio of PSS to SSS |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |

Table A.17.5.6.1.1-4: OTA related test parameters for UE specific CBW change test case

| Parameter |  | Unit | Cell 2 |
| --- | --- | --- | --- |
| Angle of arrival configuration |  |  | Setup 1 according to table A.3.15 |
| Assumption for UE beams Note 5 |  |  | Fine |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | NR_TDD_FR2_A | dBm/15 kHz | -112 |
|  | NR_TDD_FR2_B |  |  |
|  | NR_TDD_FR2_F |  |  |
|  | NR_TDD_FR2_G |  |  |
|  | NR_TDD_FR2_T |  |  |
|  | NR_TDD_FR2_Y |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | NR_TDD_FR2_A | dBm/SCS | -103 |
|  | NR_TDD_FR2_B |  |  |
|  | NR_TDD_FR2_F |  |  |
|  | NR_TDD_FR2_G |  |  |
|  | NR_TDD_FR2_T |  |  |
|  | NR_TDD_FR2_Y |  |  |
| SS-RSRPNote2 | NR_TDD_FR2_A | dBm/SCS Note3 | -85 |
|  | NR_TDD_FR2_B |  |  |
|  | NR_TDD_FR2_F |  |  |
|  | NR_TDD_FR2_G |  |  |
|  | NR_TDD_FR2_T |  |  |
|  | NR_TDD_FR2_Y |  |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 18 |
| IoNote2 | NR_TDD_FR2_A | dBm/95.04 MHz Note4 | -56 |
|  | NR_TDD_FR2_B |  |  |
|  | NR_TDD_FR2_F |  |  |
|  | NR_TDD_FR2_G |  |  |
|  | NR_TDD_FR2_T |  |  |
|  | NR_TDD_FR2_Y |  |  |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5:  Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation. |  |  |  |

##### A.17.5.6.1.2 Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PCell from the first DL slot that occurs after the beginning of slot $ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}$ and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}+k1 $.

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed PCell UE specific CBW change delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.6 Measurement procedure for RedCap

### A.17.6.1 Intra-frequency Measurements

#### A.17.6.1.1 SA event triggered reporting test without gap under non-DRX

##### A.17.6.1.1.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements for RedCap in clause 9.2B.5.1 and 9.2B.5.2. Supported test configurations are shown in table A.17.6.1.1.1-1.

Table A.17.6.1.1.1-1: supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.17.6.1.1.1-2, A.17.6.1.1.1-3 and A.17.6.1.1.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.17.6.1.1.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX for RedCap

| Parameter | Unit | Config | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1, 2 | PCell (Cell 1) |  |
| Neighbour cell |  | 1, 2 | Cell 2 | Cell to be identified. |
| RF Channel Number |  | 1, 2 | 1: Cell 1 and Cell 2 | One TDD carrier frequency is used for the NR cells. |
| SMTC configuration |  | 1, 2 | SMTC.1 |  |
| A3-Offset | dB | 1, 2 | -11 |  |
| CP length |  | 1, 2 | Normal |  |
| Hysteresis | dB | 1, 2 | 0 |  |
| TimeToTrigger | s | 1, 2 | 0 |  |
| Filter coefficient |  | 1, 2 | 0 | L3 filtering is not used |
| DRX |  | 1, 2 | OFF |  |
| Time offset between Cell 1 and Cell 2 |  | 1, 2 | 3 s | Synchronous cells |
| T1 | s | 1, 2 | 5 |  |
| T2 | s | 1, 2 | 5 |  |

Table A.17.6.1.1.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX for RedCap

| Parameter | Unit | Config | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| TDD configuration |  | 1, 2 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel | MHz | 1, 2 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  | 1 | 24 |  | 24 |  |
|  |  | 2 | 48 |  | 48 |  |
| Intial BWP configuration |  | 1, 2 | DLBWP.0.1ULBWP.0.1 |  | DLBWP.0.1ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1, 2 | DLBWP.1.1 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.1 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1, 2 | SSB |  | SSB |  |
| PDSCH RMC configuration |  | 1 | SR.3.2 TDD |  | N/A |  |
|  |  | 2 | SR.3.3 TDD |  |  |  |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD |  | N/A |  |
|  |  | 2 | CR.3.2 TDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 TDD |  | N/A |  |
|  |  | 2 | CCR.3.7 TDD |  | N/A |  |
| TRS configuration |  | 1, 2 | TRS.2.1 TDD |  | N/A |  |
| PDSCH/PDCCH TCI states |  | 1, 2 | TCI.State.2 |  | N/A |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2 | 120 |  | 120 |  |
| OCNG Patterns |  | 1, 2 | OP.5 |  | N/A |  |
| cellIndividualOffset | dB | 1~2 | N/A |  | 16 |  |
| SSB |  | 1 | SSB.1 FR2 |  | SSB.7 FR2 |  |
|  |  | 2 | SSB.2 FR2 |  | SSB.8 FR2 |  |
| Propagation Condition |  | 1, 2 | No external noise (Note 1) |  | No external noise (Note 1) |  |
| NOTE 1: The downlink connection between the System Simulator and the UE is without Additive White Gaussian Noise, and has no fading or multipath effects as specified in TS 38.521-2 B.0 [38]. |  |  |  |  |  |  |

Table A.17.6.1.1.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX for RedCap

| Parameter | Unit | Config | Cell 1 |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 |  | T2 |
| AoA setup |  | 1, 2 | Setup 3 defined in A.3.15.3 |  |  |  |  |
|  |  |  | AoA1 |  | AoA2 |  |  |
| Beam assumptionNote 4 |  | 1,2 | Rough |  | Rough |  |  |
| Es | dBm/SCS | 1 | -89 | -89 |  | -Infinity | -89 |
|  |  | 2 | -86 | -86 |  | -Infinity | -86 |
| BB Note 5 | dB | 1, 2 | -0.12 | -0.12 |  | -Infinity | -0.12 |
| SSB_RP | dBm/SCS | 1 | -89 | -89 | -Infinity |  | -89 |
|  |  | 2 | -86 | -86 | -Infinity |  | -86 |
|  | dBm/95.04 MHz | 1 | -64.41 | -64.41 | -Infinity |  | -64.41 |
|  |  | 2 | -61.41 | -61.41 | -Infinity |  | -61.41 |
| Time multiplexing of the downlink transmissions from each AoA |  | 1, 2 | Defined in figure A.17.6.1.1.1-1 |  |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: VoidNOTE 3: Es/Iot, SSB_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 5: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] Table 6.2.1.3-4. |  |  |  |  |  |  |  |


![](media/image27.emf)

Figure A.17.6.1.1.1-1: Time multiplexed downlink transmissions (Config 1 example)

##### A.17.6.1.1.2 Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

- 2.4 s for a UE supporting power class 1 or 5,

- 1.44 s for a UE supporting power class 2, 3, 4 or 7.

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.17.6.1.2 SA event triggered reporting test without gap under DRX

##### A.17.6.1.2.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2B.5.1 and 9.2B.5.2. Supported test configurations are shown in table A.7.6.1.2.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.2.1-2, A.7.6.1.2.1-3 and A.7.6.1.2.1-4.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

##### A.7.6.1.2.2 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

- 7.2 s for a UE supporting power class 1 or 5,

- 4.32 s for a UE supporting power class 2, 3, 4, or 7.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

- 51.2 s for a UE supporting power class 1 or 5,

- 30.72 s for a UE supporting power class 2, 3 4, or 7.

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.17.6.1.3 SA event triggered reporting test with per-UE gaps under non-DRX

##### A.17.6.1.3.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2B.6.1 and 9.2B.6.2. Supported test configurations are shown in table A.17.6.1.3.1-1.

Table A.17.6.1.3.1-1: supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.17.6.1.3.1-2 ~ 4 below.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.17.6.1.3.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps without DRX

| Parameter | Unit | Config | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1, 2 | PCell (Cell 1) |  |
| Neighbour cell |  | 1, 2 | Cell 2 | Cell to be identified. |
| RF Channel Number |  | 1, 2 | 1: Cell 1 and Cell 2 | One TDD carrier frequency is used for the NR cells. |
| Gap type |  | 1, 2 | Per-UE gaps |  |
| Measurement gap repitition periodicity | ms | 1, 2 | 40 |  |
| Measurement gap length | ms | 1, 2 | 6 |  |
| Measurement gap offset | ms | 1, 2 | 4 |  |
| SMTC configuration for CD-SSB |  | 1, 2 | SMTC.1 RedCap |  |
| SMTC configuration for NCD-SSB |  | 1, 2 | SMTC.2 RedCap |  |
| CSI-RS parameters |  | 1, 2 | CSI-RS.3.2 TDD |  |
| A3-Offset | dB | 1, 2 | -11 |  |
| CP length |  | 1, 2 | Normal |  |
| Hysteresis | dB | 1, 2 | 0 |  |
| Time To Trigger | s | 1, 2 | 0 |  |
| Filter coefficient |  | 1, 2 | 0 | L3 filtering is not used |
| DRX |  | 1, 2 | OFF |  |
| Time offset between Cell 1 and Cell 2 |  | 1, 2 | 3 s | Synchronous cells |
| T1 | s | 1, 2 | 5 |  |
| T2 | s | 1, 2 | 5 |  |

Table A.17.6.1.3.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps without DRX

| Parameter | Unit | Config | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| TDD configuration |  | 1, 2 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel | MHz | 1, 2 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  | 1 | 24 |  | 24 |  |
|  |  | 2 | 48 |  | 48 |  |
| Intial BWP configuration |  | 1, 2 | DLBWP.0.1ULBWP.0.1 |  | DLBWP.0.1ULBWP.0.1 |  |
| Dedicated DL BWP configuration |  | 1, 2 | DLBWP.1.3 RedCap Note 1 |  | DLBWP.1.3 RedCap Note 1 |  |
| Dedicated UL BWP configuration |  | 1, 2 | ULBWP.1.3 RedCap Note 2 |  | ULBWP.1.3 RedCap Note 2 |  |
| RLM-RS |  | 1, 2 | CSI-RS |  | SSB |  |
| PDSCH RMC configuration |  | 1 | SR.3.2 TDD |  | N/A |  |
|  |  | 2 | SR.3.3 TDD |  |  |  |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD |  | N/A |  |
|  |  | 2 | CR.3.2 TDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 TDD |  | N/A |  |
|  |  | 2 | CCR.3.7 TDD |  | N/A |  |
| TRS configuration |  | 1, 2 | TRS.2.1 TDD |  | N/A |  |
| PDSCH/PDCCH TCI states |  | 1, 2 | TCI.State.2 |  | N/A |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2 | 120 |  | 120 |  |
| OCNG Patterns |  | 1, 2 | OP.5 |  | N/A |  |
| cellIndividualOffset | dB | 1~2 | N/A |  | 16 |  |
| CD-SSB |  | 1 | SSB.2 RedCap FR2 |  | SSB.2 RedCap FR2 |  |
|  |  | 2 | SSB.4 RedCap FR2 |  | SSB.4 RedCap FR2 |  |
| NCD-SSB |  | 1 | SSB.3 RedCap FR2 |  | SSB.3 RedCap FR2 |  |
|  |  | 2 | SSB.5 RedCap FR2 |  | SSB.5 RedCap FR2 |  |
| Propagation Condition |  | 1, 2 | No external noise (Note 3) |  | No external noise (Note 3) |  |
| NOTE 1: The starting PRB index for dedicated DL BWP1 corresponding to CD-SSB PRB index; the starting PRB index for dediacted DL BWP2 corresponding to NCD-SSB PRB index;NOTE 2: The starting PRB index for dedicated UL BWP1 is the same as the starting PRB index for dedicated DL BWP1; the starting PRB index for dedicated UL BWP2 is the same as the starting PRB index for dedicated DL BWP2.NOTE 3: The downlink connection between the System Simulator and the UE is without Additive White Gaussian Noise, and has no fading or multipath effects as specified in TS 38.521-2 B.0 [38]. |  |  |  |  |  |  |

Table A.17.6.1.3.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps without DRX

| Parameter | Unit | Config | Cell 1 |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 |  | T2 |
| AoA setup |  | 1, 2 | Setup 3 defined in A.3.15.3 |  |  |  |  |
|  |  |  | AoA1 |  | AoA2 |  |  |
| Beam AssumptionNote 4 |  | 1,2 | Rough |  | Rough |  |  |
| Es | dBm/SCS | 1 | -89 | -89 |  | -Infinity | -89 |
|  |  | 2 | -86 | -86 |  | -Infinity | -86 |
| BB Note 5 | dB | 1, 2 | -0.12 | -0.12 |  | -Infinity | -0.12 |
| SSB_RP | dBm/SCS | 1 | -89 | -89 | -Infinity |  | -89 |
|  |  | 2 | -86 | -86 | -Infinity |  | -86 |
|  | dBm/95.04 MHz | 1 | -64.41 | -64.41 | -Infinity |  | -64.41 |
|  |  | 2 | -61.41 | -61.41 | -Infinity |  | -61.41 |
| Time multiplexing of the downlink transmissions from each AoA |  | 1 | Defined in figure A.17.6.1.3.1-1 |  |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: VoidNOTE 3: Es/Iot, SSB_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 5: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] Table 6.2.1.3-4. |  |  |  |  |  |  |  |


![](media/image27.emf)

Figure A.17.6.1.3.1-1: Time multiplexed downlink transmissions (Config 1 example)

##### A.17.6.1.3.2 Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

- 3.2 s for a UE supporting power class 1 or 5,

- 1.92 s for a UE supporting power class 2, 3 4 or 7

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.17.6.1.4 SA event triggered reporting test with per-UE gaps under DRX

##### A.17.6.1.4.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2B.6.1 and 9.2B.6.2. Supported test configurations are shown in table A.17.6.1.4.1-1.

Table A.17.6.1.4.1-1: supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.17.6.1.4.1-2, A.17.6.1.4.1-3 and A.17.6.1.4.1-4 below.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.17.6.1.4.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps with DRX

| Parameter | Unit | Config | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| Active cell |  | 1, 2 | PCell (Cell 1) |  |  |
| Neighbour cell |  | 1, 2 | Cell 2 |  | Cell to be identified. |
| RF Channel Number |  | 1, 2 | 1: Cell 1 and Cell 2 |  | One TDD carrier frequency is used for the NR cells. |
| Gap type |  | 1, 2 | Per-UE gaps |  |  |
| Measurement gap repitition periodicity | ms | 1, 2 | 40 |  |  |
| Measurement gap length | ms | 1, 2 | 6 |  |  |
| Measurement gap offset | ms | 1, 2 | 39 |  |  |
| SMTC configuration |  | 1, 2 | SMTC.1 |  |  |
| CSI-RS parameters |  | 1, 2 | CSI-RS.3.2 TDD |  |  |
| A3-Offset | dB | 1, 2 | -6 |  |  |
| CP length |  | 1, 2 | Normal |  |  |
| Hysteresis | dB | 1, 2 | 0 |  |  |
| Time To Trigger | s | 1, 2 | 0 |  |  |
| Filter coefficient |  | 1, 2 | 0 |  | L3 filtering is not used |
| DRX |  | 1, 2 | DRX.1 | DRX.7 | DRX related parameters are defined in table A.7.6.1.2.1-5 |
| Time offset between Cell 1 and Cell 2 |  | 1, 2 | 3 s |  | Synchronous cells |
| T1 | s | 1, 2 | 5 |  |  |
| T2 | s | 1, 2 | 10 | 52 |  |

Table A.17.6.1.4.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps with DRX

| Parameter | Unit | Config | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| TDD configuration |  | 1, 2 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel | MHz | 1, 2 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  | 1, 2 | 66 |  | 66 |  |
| Intial BWP configuration |  | 1, 2 | DLBWP.0.1ULBWP.0.1 |  | DLBWP.0.1ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1, 2 | DLBWP.1.2 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.2 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1, 2 | SCSI-RS |  | SSB |  |
| PDSCH RMC configuration |  | 1 | SR.3.2 TDD |  | N/A |  |
|  |  | 2 | SR.3.3 TDD |  |  |  |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD |  | N/A |  |
|  |  | 2 | CR.3.2 TDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 TDD |  | N/A |  |
|  |  | 2 | CCR.3.7 TDD |  | N/A |  |
| TRS configuration |  | 1, 2 | TRS.2.1 TDD |  | N/A |  |
| PDSCH/PDCCH TCI state |  | 1, 2 | TCI.State.2 |  | N/A |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2 | 120 |  | 120 |  |
| OCNG Patterns |  | 1, 2 | OP.1 |  | OP.1 |  |
| SSB |  | 1 | SSB.3 FR2 |  | SSB.3 FR2 |  |
|  |  | 2 | SSB.4 FR2 |  | SSB.4 FR2 |  |
| Propagation Condition |  | 1, 2 | AWGN |  | AWGN |  |

Table A.17.6.1.4.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps with DRX

| Parameter | Unit | Config | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  | 1, 2 | Setup 1 defined in clause A.3.15.1 |  |  |  |
| Beam AssumptionNote 4 |  | 1,2 | Rough |  |  |  |
| BB Note 5 | dB | 1, 2 | 3.77 | -1.52 | -Infinity | -1.52 |
| Note 2 | dBm/15 KHz | 1, 2 | -98 |  |  |  |
| Note 2 | dBm/SCS | 1 | -89 |  |  |  |
|  |  | 2 | -86 |  |  |  |
| SSB_RP | dBm/SCS | 1 | -85 | -85 | -Infinity | -85 |
|  |  | 2 | -82 | -82 | -Infinity | -82 |
|  | dB | 1, 2 | 4 | 4 | -Infinity | 4 |
|  | dBm/95.04 MHz | 1,2 | -54.53 | -52.18 | See Cell 1 columns |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: Es/Iot, SSB_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 5: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] Table 6.2.1.3-4. |  |  |  |  |  |  |

Table A.17.6.1.4.1-5: Void

Table A.17.6.1.4.1-6:Void

##### A.17.6.1.4.2 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

- 7.2 s for a UE supporting power class 1 or 5,

- 4.32 s for a UE supporting power class 2, 3 4 or 7

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

- 51.2 s for a UE supporting power class 1 or 5,

- 30.72 s for a UE supporting power class 2, 3 4 or 7

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

### A.17.6.2 Inter-frequency Measurements

#### A.17.6.2.1 SA event triggered reporting tests For FR2 without SSB time index detection when DRX is not used (PCell in FR2)

##### A.17.6.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR2 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.17.6.2.1.1-1, A.17.6.2.1.1-2, and A.17.6.2.1.1-3.

Measurement gap pattern configuration # 13 as defined in table A.17.6.2.1.1-2 is provided for UE that does not support per-FR gap and for UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Supported test configurations are shown in table A.17.6.2.1.1-1.

Table A.17.6.2.1.1-1 SA event triggered reporting tests without SSB index reading for FR2-FR2

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE 1: Void. |  |

Table A.17.6.2.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1 | 1, 2 | Two FR2 NR carrier frequencies is used. |
| Active cell |  | Config 1 | NR Cell 1 (Pcell) | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1 | NR Cell 2 | NR Cell 2 is on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1 | 13 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1 | 39 |  |
| SMTC-CD-SSB parameters |  | Config 1 | SSB.2 RedCap FR2 | As specified in clause A.3.10.2 |
| NCD-SSB parameters |  | Config 1 | SSB.3 RedCap FR2 |  |
| offsetMO | dB | Config 1 | 16 | Applied to NR Cell 2 measurement object |
| A3-Offset | dB | Config 1 | -11 |  |
| Hysteresis | dB | Config 1 | 0 |  |
| CP length |  | Config 1 | Normal |  |
| TimeToTrigger | s | Config 1 | 0 |  |
| Filter coefficient |  | Config 1 | 0 | L3 filtering is not used |
| DRX |  | Config 1 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | Config 1 | 3s | Synchronous cells. |
| T1 | s | Config 1 | 5 |  |
| T2 | s | Config 1 | 5.2 for PC1; 3.5 for other PC |  |

Table A.17.6.2.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  |  | Config 1 | Setup 3 as specified in clause A.3.15 |  |  |  |
|  |  |  |  | AoA1 |  | AoA2 |  |
| Beam AssumptionNote 7 |  |  | 1,2 | Rough |  | Rough |  |
| NR RF Channel Number |  |  | Config 1 | 1 |  | 2 |  |
| Duplex mode |  |  | Config 1 | TDD |  | TDD |  |
| TDD configuration |  |  | Config 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel |  | MHz | Config 1 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  |  | Config 1 | 66 |  | 66 |  |
| BWP BW |  | MHz | Config 1 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| BWP configuration | Initial DL BWP |  | Config 1 | DLBWP.0.1 |  | N/A |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | N/A |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | N/A |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | N/A |  |
|  | Dedicated DL BWP configuration |  |  | DLBWP.1.3 RedCap Note 9 |  | N/A |  |
|  | Dedicated UL BWP configuration |  |  | ULBWP.1.3 RedCap Note 10 |  | N/A |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1 | SR.3.1 TDD |  | - |  |
| CORESET Reference Channel |  |  | Config 1 | CR.3.1 TDD |  | - |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 for CD-SSB |  |  | Config 1 | SMTC.1 |  | SMTC.1 |  |
| SMTC configuration for NCD-SSB |  |  | Config 1 | SMTC.2 RedCap |  | SMTC.2 RedCap |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1 | 120 |  | 120 |  |
| TRS configuration |  |  | Config 1 | TRS.2.1 TDD |  | N/A |  |
| PDSCH/PDCCH TCI state |  |  | Config 1 | TCI.State.2 |  | N/A |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| Ês |  | dBm/SCS | Config 1 | -87 | -87 | -Infinity | -87 |
| SSBRP Note 3 |  | dBm/SCS Note5 | Config 1 | -87 | -87 | -Infinity | -87 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] BB Note 8 |  | dB | Config 1 | 1.89 | 1.89 | -Infinity | 1.89 |
| IoNote3 |  | dBm/95.04 MHz Note5 | Config 1 | -58.01 | -58.01 | -Infinity | -58.01 |
| Propagation Condition |  |  | Config 1 | No external noise (Note 11) |  | No external noise (Note 11) |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: VoidNOTE 3: SSBRP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: VoidNOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 8: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBS from TS 38.101-2 [19] Table 6.2.1.3-4.NOTE 9: The starting PRB index for dedicated DL BWP1 corresponding to CD-SSB PRB index; the starting PRB index for dediacted DL BWP2 corresponding to NCD-SSB PRB index;NOTE 10: The starting PRB index for dedicated UL BWP1 is the same as the starting PRB index for dedicated DL BWP1; the starting PRB index for dedicated UL BWP2 is the same as the starting PRB index for dedicated DL BWP2.NOTE 11: The downlink connection between the System Simulator and the UE is without Additive White Gaussian Noise, and has no fading or multipath effects as specified in TS 38.521-2 B.0 [38]. |  |  |  |  |  |  |  |

##### A.17.6.2.1.2 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 5120 for UE supporting power class 1, or

## 3200 for UE supporting other power class.

The  UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.17.6.2.2 SA event triggered reporting tests For FR2 without SSB time index detection when DRX is used (PCell in FR2)

##### A.17.6.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that RedCap UE makes correct reporting of an event in FR2. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR2 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 2. The test parameters and configurations are given in tables A.17.6.2.2.1-1, A.17.6.2.2.1-2, and A.17.6.2.2.1-3.

In test 1&2 measurement gap pattern configuration # 13 as defined in table A.17.6.2.2.1-2 is provided for RedCap UE that does not support per-FR gap and for RedCap UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Supported test configurations are shown in table A.17.6.2.2.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.17.6.2.2.1-1: SA event triggered reporting tests without SSB index reading for FR2-FR2

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE 1: Void. |  |

Table A.17.6.2.2.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| NR RF Channel Number |  | Config 1 | 1, 2 |  | Two FR2 NR carrier frequencies is used. |
| Active cell |  | Config 1 | NR Cell 1 (Pcell) |  | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1 | NR Cell 2 |  | NR Cell 2 is on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1 | 13 |  | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1 | 39 |  |  |
| SMTC-SSB parameters |  | Config 1 | SSB.3 FR2 |  | As specified in clause A.3.10.2 |
| A3-Offset | dB | Config 1 | -6 |  |  |
| Hysteresis | dB | Config 1 | 0 |  |  |
| CP length |  | Config 1 | Normal |  |  |
| TimeToTrigger | s | Config 1 | 0 |  |  |
| Filter coefficient |  | Config 1 | 0 |  | L3 filtering is not used |
| DRX |  | Config 1 | DRX.1 | DRX.7 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | Config 1 | 3s |  | Synchronous cells. |
| T1 | s | Config 1 | 5 |  |  |
| T2 | s | Config 1 | 8 for PC1;5 for other PC | 82 for PC1; 52 for other PC |  |

Table A.17.6.2.2.1-3: Cell specific test parameters for CA inter-frequency event triggered reporting without SSB time index detection

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  |  | Config 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  |  | Config 1 | Rough |  | Rough |  |
| NR RF Channel Number |  |  | Config 1 | 1 |  | 2 |  |
| TDD configuration |  |  | Config 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| Duplex mode |  |  | Config 1 | TDD |  | TDD |  |
| BWchannel |  | MHz | Config 1 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  |  | Config 1 | 66 |  | 66 |  |
| BWP BW |  | MHz | Config 1 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| BWP configuration | Initial DL BWP |  | Config 1 | DLBWP.0.1 |  | N/A |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | N/A |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | N/A |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | N/A |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1 | SR.3.1 TDD |  | - |  |
| CORESET Reference Channel |  |  | Config 1 | CR.3.1 TDD |  | - |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  |  | Config 1 | SMTC.1 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1 | 120 |  | 120 |  |
| TRS configuration |  |  | Config 1 | TRS.2.1 TDD |  | N/A |  |
| PDSCH/PDCCH TCI state |  |  | Config 1 | TCI.State.2 |  | N/A |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz Note5 |  | -104.7 |  | -104.7 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS Note4 | Config 1 | -95.7 |  | -95.7 |  |
| SS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -89.7 | -89.7 | -Infinity | -86.7 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1 | 6 | 6 | -Infinity | 9 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1 | 6 | 6 | -Infinity | 9 |
| IoNote3 |  | dBm/95.04 MHz Note5 | Config 1 | -59.7 | -59.7 | -66.7 | -57.2 |
| Propagation Condition |  |  | Config 1 | AWGN |  | AWGN |  |
| Antenna Configuration |  |  | Config 1 | 1x2 |  | 1x2 |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SSB_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: VoidNOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |  |  |

##### A.17.6.2.2.2 Test Requirements

In test 1 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 7680 for UE supporting power class 1, or

## 4800 for UE supporting other power class.

In test 2 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

## 81920 for UE supporting power class 1, or

## 51200 for UE supporting other power class.

In test 1 and 2 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.17.6.2.3 SA event triggered reporting tests For FR2 with SSB time index detection when DRX is not used (PCell in FR2)

##### A.17.6.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR2 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.17.6.2.3.1-1, A.17.6.2.3.1-2, and A.17.6.2.3.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Supported test configurations are shown in table A.17.6.2.3.1-1.

Table A.17.6.2.3.1-1: SA event triggered reporting tests with SSB index reading for FR2-FR2

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE 1: Void. |  |

Table A.17.6.2.3.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1 | 1, 2 | Two FR2 NR carrier frequencies is used. |
| Active cell |  | Config 1 | NR Cell 1 (Pcell) | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1 | NR Cell 2 | NR Cell 2 is on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1 | 13 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1 | 39 |  |
| SMTC-SSB parameters |  | Config 1 | SSB.3 FR2 | As specified in clause A.3.10.2 |
| offsetMO | dB | Config 1 | 16 | Applied to NR Cell 2 measurement object |
| A3-Offset | dB | Config 1 | -11 |  |
| Hysteresis | dB | Config 1 | 0 |  |
| CP length |  | Config 1 | Normal |  |
| TimeToTrigger | s | Config 1 | 0 |  |
| Filter coefficient |  | Config 1 | 0 | L3 filtering is not used |
| DRX |  | Config 1 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | Config 1 | 3s | Synchronous cells. |
| T1 | s | Config 1 | 5 |  |
| T2 | s | Config 1 | 7 for PC1; 4.5 for other PC |  |

Table A.17.6.2.3.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 |  | T2 |
| AoA setup |  |  | Config 1 | Setup 3 as specified in clause A.3.15 |  |  |  |  |
|  |  |  |  | AoA1 |  | AoA2 |  |  |
| Beam AssumptionNote 7 |  |  | Config 1 | Rough |  | Rough |  |  |
| NR RF Channel Number |  |  | Config 1 | 1 |  | 2 |  |  |
| Duplex mode |  |  | Config 1 | TDD |  | TDD |  |  |
| TDD configuration |  |  | Config 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |  |
| BWchannel |  | MHz | Config 1 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |  |
| Data PRBs allocated |  |  | Config 1 | 66 |  | 66 |  |  |
| BWP BW |  | MHz | Config 1 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |  |
| BWP configuration | Initial DL BWP |  | Config 1 | DLBWP.0.1 |  | N/A |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | N/A |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | N/A |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | N/A |  |  |
| OCNG Patterns defined in A.3.2.1.1 |  |  | Config 1 | OP.1 |  | OP.1 |  |  |
| PDSCH Reference measurement channel |  |  | Config 1 | SR.3.1 TDD |  | - |  |  |
| CORESET Reference Channel |  |  | Config 1 | CR.3.1 TDD |  | - |  |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  |  | Config 1 | SMTC.1 |  | SMTC.1 |  |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1 | 120 |  | 120 |  |  |
| TRS configuration |  |  | Config 1 | TRS.2.1 TDD |  | N/A |  |  |
| PDSCH/PDCCH TCI state |  |  | Config 1 | TCI.State.2 |  | N/A |  |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1 | 0 |  | 0 |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| Ês |  | dBm/SCS | Config 1 | -87 | -87 | -Infinity |  | -87 |
| SSBRP Note 3 |  | dBm/SCS Note5 | Config 1 | -87 | -87 | -Infinity |  | -87 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] BB Note 8 |  | dB | Config 1 | 1.89 | 1.89 | -Infinity |  | 1.89 |
| Io Note3 |  | dBm/95.04 MHz Note5 | Config 1 | -58.01 | -58.01 | -Infinity |  | -58.01 |
| Propagation Condition |  |  | Config 1 | No external noise (Note 9) |  |  | No external noise (Note 9) |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: VoidNOTE 3: SBRP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: VoidNOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 8: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBS from TS 38.101-2 [19] Table 6.2.1.3-4.NOTE 9: The downlink connection between the System Simulator and the UE is without Additive White Gaussian Noise, and has no fading or multipath effects as specified in TS 38.521-2 B.0 [38]. |  |  |  |  |  |  |  |  |

##### A.17.6.2.3.2 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 6720 for UE supporting power class 1, or

## 4160 for UE supporting other power class.

The UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.17.6.2.4 SA event triggered reporting tests For FR2 with SSB time index detection when DRX is used (PCell in FR2) for 2 RX UE

##### A.17.6.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR2 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.17.6.2.4.1-1, A.17.6.2.4.1-2, and A.17.6.2.4.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Supported test configurations are shown in table A.17.6.2.4.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.17.6.2.4.1-1: SA event triggered reporting tests with SSB index reading for FR2-FR2

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE 1: Void. |  |

Table A.17.6.2.4.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| NR RF Channel Number |  | Config 1 | 1, 2 |  | Two FR2 NR carrier frequencies is used. |
| Active cell |  | Config 1 | NR Cell 1 (Pcell) |  | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1 | NR Cell 2 |  | NR Cell 2 is on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1 | 13 |  | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1 | 39 |  |  |
| SMTC-SSB parameters |  | Config 1 | SSB.3 FR2 |  | As specified in clause A.3.10.2 |
| A3-Offset | dB | Config 1 | -6 |  |  |
| Hysteresis | dB | Config 1 | 0 |  |  |
| CP length |  | Config 1 | Normal |  |  |
| TimeToTrigger | s | Config 1 | 0 |  |  |
| Filter coefficient |  | Config 1 | 0 |  | L3 filtering is not used |
| DRX |  | Config 1 | DRX.1 | DRX.7 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | Config 1 | 3s |  | Synchronous cells. |
| T1 | s | Config 1 | 5 |  |  |
| T2 | s | Config 1 | 11 for PC1; 6.5 for other PC | 108 for PC1; 67 for other PC |  |

Table A.17.6.2.4.1-3: Cell specific test parameters for CA inter-frequency event triggered reporting with SSB time index detection

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  |  | Config 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  |  | Config 1 | Rough |  | Rough |  |
| NR RF Channel Number |  |  | Config 1 | 1 |  | 2 |  |
| Duplex mode |  |  | Config 1 | TDD |  | TDD |  |
| TDD configuration |  |  | Config 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel |  | MHz | Config 1 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  |  | Config 1 | 66 |  | 66 |  |
| BWP BW |  | MHz | Config 1 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| BWP configuration | Initial DL BWP |  | Config 1 | DLBWP.0.1 |  | N/A |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | N/A |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | N/A |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | N/A |  |
| OCNG Patterns defined in A.3.2.1.1 |  |  | Config 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1 | SR.3.1 TDD |  | - |  |
| CORESET Reference Channel |  |  | Config 1 | CR.3.1 TDD |  | - |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  |  | Config 1 | SMTC.1 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1 | 120 |  | 120 |  |
| TRS configuration |  |  | Config 1 | TRS.2.1 TDD |  | N/A |  |
| PDSCH/PDCCH TCI state |  |  | Config 1 | TCI.State.2 |  | N/A |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz Note5 |  | -104.7 |  | -104.7 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS Note4 | Config 1 | -95.7 |  | -95.7 |  |
| SS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -89.7 | -89.7 | -Infinity | -86.7 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1 | 6 | 6 | -Infinity | 9 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1 | 6 | 6 | -Infinity | 9 |
| IoNote3 |  | dBm/95.04 MHz Note5 | Config 1 | -59.7 | -59.7 | -66.7 | -57.2 |
| Propagation Condition |  |  | Config 1 | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SSB_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: VoidNOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |  |  |

##### A.17.6.2.4.2 Test Requirements

In test 1 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 10080 for UE supporting power class 1, or

## 6240 for UE supporting other power class.

In test 1 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

## 107520 for UE supporting power class 1, or

## 66560 for UE supporting other power class.

In test 1 and 2 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

### A.17.6.3 L1-RSRP measurement for beam reporting

#### A.17.6.3.1 SSB based L1-RSRP measurement when DRX is not used

##### A.17.6.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.1, with the testing configurations for NR cells in table A.7.6.3.1.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

##### A.17.6.3.1.2 Test parameters

Test parameters are the same as in clause A.7.6.3.1.2.

##### A.17.6.3.1.3 Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than X ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in clause [10.xx.xx.1], where X is

- 1680 for UE supporting power class 1 or 5.

- 1200 for UE supporting power class 2,3, 4 or 7.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.17.6.3.2 SSB based L1-RSRP measurement when DRX is used

##### A.17.6.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.1, with the testing configurations for NR cells in table A.17.6.3.2.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

Table A.17.6.3.2.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | NR 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

##### A.17.6.3.2.2 Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.17.6.3.2.2-1 and table A.17.6.3.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.17.6.3.2.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB ARFCN | 1~2 |  | freq1 |
| Duplex mode | 1~2 |  | TDD |
| TDD Configuration | 1~2 |  | TDDConf.3.1 |
| BWchannel | 1~2 | MHz | 100: NPRB,c = 66 |
| Data PRBs allocated | 1~2 |  | 66 |
| PDSCH Reference measurement channel | 1 |  | SR.3.2 TDD |
|  | 2 |  | SR.3.3 TDD |
| RMSI CORESET Reference Channel | 1 |  | CR.3.1 TDD |
|  | 2 |  | CR.3.2 TDD |
| Dedicated CORESET Reference Channel | 1 |  | CCR.3.1 TDD |
|  | 2 |  | CCR.3.7 TDD |
| SSB configuration | 1 |  | SSB.1 FR2 |
|  | 2 |  | SSB.2 FR2 |
| OCNG Patterns | 1~2 |  | OP.1 |
| Initial BWP Configuration | 1~2 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1~2 |  | DLBWP.1.3ULBWP.1.3 |
| SMTC configuration | 1~2 |  | SMTC.1 |
| TRS Configuration | 1~2 |  | TRS.2.1 TDD |
| PDCCH/PDSCH TCI Configuration | 1~2 |  | TCI.State.2 |
| DRX configuration | 1~2 |  | DRX.3 |
| reportConfigType | 1~2 |  | periodic |
| reportQuantity | 1~2 |  | ssb-Index-RSRP |
| Number of reported RS | 1~2 |  | 2 |
| L1-RSRP reporting period | 1~2 | slot | 320 |
| T1 | 1~2 | s | 5 |
| T2 | 1~2 | s | 3 |
| EPRE ratio of PSS to SSS | 1~2 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1~2 |  | AWGN |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |

Table A.17.6.3.2.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Angle of arrival configuration |  |  | Setup 1 according to clause A.3.15.1 |  |  |  |
| Beam AssumptionNote 4 | 1-2 |  | Rough |  |  |  |
| Note2 | 1~2 | dBm/15 kHz | -105 |  |  |  |
| Note2 | 1 | dBm/SSB SCS | -96 |  |  |  |
|  | 2 |  | -93 |  |  |  |
|  | 1~2 | dB | 0 | 0 | -Infinity | 9 |
| SSB_RP Note3 | 1 | dBm/SSB SCS | -96 | -96 | -Infinity | -87 |
|  | 2 |  | -93 | -93 | -Infinity | -84 |
| Io Note3 | 1 | dBm/95.04 MHz | -63.97 | -63.97 | -66.98 | -57.47 |
|  | 2 |  | -63.97 | -63.97 | -66.98 | -57.47 |
|  | 1~2 | dB | 0 | 0 | -Infinity | 9 |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SSB_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |  |

##### A.17.6.3.2.3 Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than X ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in clause 10.1.20.1, where X is

- 2880 for UE supporting power class 1

- 1920 for UE supporting power class 2,3 or 4.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.17.6.3.3 CSI-RS based L1-RSRP measurement when DRX is not used

##### A.17.6.3.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.2, with the testing configurations for NR cells in table A.17.6.3.3.1-1.

Table A.17.6.3.3.1-1: Applicable NR configurations for FR2 CSI-RS based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | NR 120 kHz CSI-RS SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

##### A.17.6.3.3.2 Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.17.6.3.3.2-1 and table A.17.6.3.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 480 ms from the beginning of the test, the DCI trigger comes in slot 1  of a frame and UE provides the report back based on the reporting configuration as defined in table A.17.6.3.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.17.6.3.3.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB ARFCN | 1 |  | freq1 |
| Duplex mode | 1 |  | TDD |
| TDD Configuration | 1 |  | TDDConf.3.1 |
| BWchannel | 1 | MHz | 100: NPRB,c = 66 |
| PDSCH Reference measurement channel | 1 |  | SR.3.1 TDD |
| RMSI CORESET Reference Channel | 1 |  | CR.3.1 TDD |
| Dedicated CORESET Reference Channel | 1 |  | CCR.3.1 TDD |
| SSB configuration | 1 |  | SSB.1 FR2 |
| CSI-RS configuration | 1 |  | CSI-RS.3.3 TDD |
| OCNG Patterns | 1 |  | OP.1 |
| Initial BWP Configuration | 1 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1 |  | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration | 1 |  | SMTC.1 |
| TRS Configuration | 1 |  | TRS.2.1 TDD |
| PDCCH/PDSCH TCI Configuration | 1 |  | TCI.State.2 |
| DRX configuration | 1 |  | Off |
| reportConfigType | 1 |  | aperiodic |
| reportQuantity | 1 |  | cri-RSRP |
| Number of reported RS | 1 |  | 2 |
| qcl-Info | 1 |  | SSB#0 for resource#0 |
|  |  |  | SSB#1 for resource#1 |
| reportSlotOffsetList | 1 |  | 8 |
| Propagation condition | 1 |  | AWGN |
| T1 | 1 | s | 5 |
| EPRE ratio of PSS to SSS | 1 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |

Table A.17.6.3.3.2-1: CSI-RS specific test parameters

| Parameter | Config | Unit | CSI-RS#0 | CSI-RS#1 |
| --- | --- | --- | --- | --- |
| Angle of arrival configuration | 1 |  | Setup 1 according to clause A.3.15.1 |  |
| Beam AssumptionNote 4 | 1 |  | Rough | Rough |
| Note1 | 1 | dBm/15 kHz | -105 |  |
| Note1 | 1 | dBm/SSB SCS | -95.97 |  |
|  | 1 | dB | 0 | 9 |
| CSI-RS RSRP Note2 | 1 | dBm/SSB SCS | -95.97 | -86.97 |
| Io Note2 | 1 | dBm/95.04 MHz | -63.97 | -57.47 |
|  | 1 | dB | 0 | 9 |
| NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  CSI-RS RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |

##### A.17.6.3.3.3 Test Requirements

After 480 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the accuracy requirements defined in clause 10.1.20.1. The reported L1-RSRP value shall include the Rx antenna gain in the range of [-10 ~ +20] dB.

For absolute accuracy of CSI-RS0 and absolute accuracy of CSI-RS1, the UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.17.6.3.3.3-1.

For relative accuracy of CSI-RS0 compared with CSI-RS1, the UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

Table A.17.6.3.3.3-1: L1-RSRP absolute accuracy test requirement

|  | Test requirement Notes1,2,3 |
| --- | --- |
| CSI-RS0 | CSI-RS _RP0 -δ + Gmin ≤ Reported RSRP(dBm) ≤CSI-RS _RP0 +δ + Gmax |
| CSI-RS1 | CSI-RS _RP1 -δ + Gmin ≤ Reported RSRP(dBm) ≤CSI-RS _RP1 +δ + Gmax |
| NOTE 1: CSI-RS_RPn is the  equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone configured in the test for the CSI-RS n under considerationNOTE 2: δ is the RSRP absolute accuracy requirement from Table 10.1.20.2.1-1, selected according to the Io used in the testNOTE 3: Gmin and Gmax are the minimum and maximum UE gain values from Table B.2.1.5.1-1, selected according to the UE power class |  |

#### A.17.6.3.4 CSI-RS based L1-RSRP measurement when DRX is used

##### A.17.6.3.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.2, with the testing configurations for NR cells in table A.17.6.3.4.1-1.

Table A.17.6.3.4.1-1: Applicable NR configurations for FR2 CSI-RS based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | NR 120 kHz CSI-RS SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

##### A.17.6.3.4.2 Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.17.6.3.4.2-1 and table A.17.6.3.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 1440 ms from the beginning of the test, the DCI trigger comes in slot 1  of a frame and UE provides the report back based on the reporting configuration as defined in table A.17.6.3.4.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.17.6.3.4.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB ARFCN | 1 |  | freq1 |
| Duplex mode | 1 |  | TDD |
| TDD Configuration | 1 |  | TDDConf.3.1 |
| BWchannel | 1 | MHz | 100: NPRB,c = 66 |
| PDSCH Reference measurement channel | 1 |  | SR.3.1 TDD |
| RMSI CORESET Reference Channel | 1 |  | CR.3.1 TDD |
| Dedicated CORESET Reference Channel | 1 |  | CCR.3.1 TDD |
| SSB configuration | 1 |  | SSB.1 FR2 |
| CSI-RS configuration | 1 |  | CSI-RS.3.3 TDD |
| OCNG Patterns | 1 |  | OP.1 |
| Initial BWP Configuration | 1 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1 |  | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration | 1 |  | SMTC.1 |
| TRS Configuration | 1 |  | TRS.2.1 TDD |
| PDCCH/PDSCH TCI Configuration | 1 |  | TCI.State.2 |
| DRX configuration | 1 |  | DRX.3 |
| reportConfigType | 1 |  | aperiodic |
| reportQuantity | 1 |  | cri-RSRP |
| Number of reported RS | 1 |  | 2 |
| qcl-Info | 1 |  | SSB#0 for resource#0 |
|  |  |  | SSB#1 for resource#1 |
| reportSlotOffsetList | 1 |  | 8 |
| Propagation condition | 1 |  | AWGN |
| T1 | 1 | s | 5 |
| EPRE ratio of PSS to SSS | 1 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |

Table A.17.6.3.4.2-1: CSI-RS specific test parameters

| Parameter | Config | Unit | CSI-RS#0 | CSI-RS#1 |  |
| --- | --- | --- | --- | --- | --- |
| Angle of arrival configuration | 1 |  | Setup 1 according to clause A.3.15.1 |  |  |
| Beam AssumptionNote 4 | 1 |  | Rough | Rough |  |
| Note1 | 1 | dBm/15 kHz | -105 |  |  |
| Note1 | 1 | dBm/SSB SCS | -95.97 |  |  |
|  | 1 | dB | 0 | 9 |  |
| CSI-RS RSRP Note2 | 1 | dBm/SSB SCS | -95.97 | -86.97 |  |
| Io Note2 | 1 | dBm/95.04 MHz | -63.97 | -57.47 |  |
|  | 1 | dB | 0 | 9 |  |
| NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: CSI-RS RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |

##### A.7.6.3.3.3 Test Requirements

After 1440 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the accuracy requirements defined in clause 10.1.20.1. The reported L1-RSRP value shall include the Rx antenna gain in the range of [-10 ~ +20] dB.

For absolute accuracy of CSI-RS0 and absolute accuracy of CSI-RS1, the UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.17.6.3.4.3-1.

For relative accuracy of CSI-RS0 compared with CSI-RS1, the UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

Table A.17.6.3.4.3-1: L1-RSRP absolute accuracy test requirement

|  | Test requirement Notes1,2,3 |
| --- | --- |
| CSI-RS0 | CSI-RS _RP0 -δ + Gmin ≤ Reported RSRP(dBm) ≤CSI-RS _RP0 +δ + Gmax |
| CSI-RS1 | CSI-RS _RP1 -δ + Gmin ≤ Reported RSRP(dBm) ≤CSI-RS _RP1 +δ + Gmax |
| NOTE 1: CSI-RS_RPn is the  equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone configured in the test for the CSI-RS n under considerationNOTE 2: δ is the RSRP absolute accuracy requirement from Table 10.1.20.2.1-1, selected according to the Io used in the testNOTE 3: Gmin and Gmax are the minimum and maximum UE gain values from Table B.2.1.5.1-1, selected according to the UE power class |  |

A.17.6.4 NR Measurements with autonomous gaps

#### A.17.6.4.1 SA interfrequency CGI reporting in autonomous gaps test (PCell in FR2) for 2 RX UE

##### A.17.6.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an CGI. This test will partly verify the SA inter-frequency NR cell search requirements in clause8.2.1.2.16 and 9.11

In this test, there are two cells: NR Cell 1 as PCell in FR2 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.17.6.4.1.1-1, A.17.6.4.1.1-2, and A.17.6.4.1.1-3.

Measurement gap patterns are configured. During T1 the UE shall report event A3 for Cell 2. Within 3 seconds of the event report, the test equipment shall add a measurement reporting configuration using ReportConfigNR which containsa ReportCGI IE with cellForWhichToReportCGI set to the physical Cell ID of Cell 2 and including the optional IE useAutonomousGaps-r16

In the measurement control information, it is indicated to the UE to decode the CGI of the neighbour cell using autonomous gaps. The test consists of two time phases, T1 and T2. Time period T2 begins 10 ms after the test equipment has transmitted the RRC reconfiguration message containing the ReportCGI IE.

Supported test configurations are shown in table A.17.6.4.1.1-1.

Table A.17.6.4.1.1-1 SA interfrequency CGI reporting test in autonomous gaps

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.6.4.1.1-2: General test parameters for SA interfrequency CGI reporting in autonomous gaps

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1 | 1, 2 | Two FR2 NR carrier frequencies is used. |
| Active cell |  | Config 1 | NR Cell 1 (Pcell) | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1 | NR Cell 2 | NR Cell 2 is on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1 | 13 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1 | 39 |  |
| SMTC-SSB parameters |  | Config 1 | SSB.3 FR2 | As specified in clause A.3.10.2 |
| SI-RNTI scheduling rate | ms |  | 40 ms | S-RNTI scheduled on four occasions per 160 ms transmission period |
| A3-Offset | dB | Config 1 | -30 |  |
| Hysteresis | dB | Config 1 | 0 |  |
| CP length |  | Config 1 | Normal |  |
| TimeToTrigger | s | Config 1 | 0 |  |
| Filter coefficient |  | Config 1 | 0 | L3 filtering is not used |
| DRX |  | Config 1 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | Config 1 | 3s | Synchronous cells. |
| T1 | s | Config 1 | <10 | UE expected to report event A3 for Cell 2 within 5,2 s (PC1)or 3.5 s (other PC) of the start of T1. Test equipment shall configure CGI reporting within 3 s after receiving the event A3 report. T2 begins 10 ms after test equipment has transmitted the RRC reconfiguration to configure CGI reporting. |
| T2 | s | Config 1 | 1 |  |

Table A.17.6.4.1.1-3: Cell specific test parameters SA interfrequency CGI reporting in autonomous gaps

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  |  | Config 1 | Setup 3 as specified in clause A.3.15 |  |  |  |
|  |  |  |  | AoA1 |  | AoA2 |  |
| Beam AssumptionNote 7 |  |  | 1,2 | Rough |  |  |  |
| NR RF Channel Number |  |  | Config 1 | 1 |  | 2 |  |
| Duplex mode |  |  | Config 1 | TDD |  | TDD |  |
| TDD configuration |  |  | Config 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel |  | MHz | Config 1 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| BWP BW |  | MHz | Config 1 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| BWP configuration | Initial DL BWP |  | Config 1 | DLBWP.0.1 |  | N/A |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | N/A |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | N/A |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | N/A |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1 | OP.1 |  | Not sent |  |
| PDSCH Reference measurement channel |  |  | Config 1 | SR.3.1 TDD |  | - |  |
| CORESET Reference Channel |  |  | Config 1 | CR.3.1 TDD |  | - |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  |  | Config 1 | SMTC.1 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1 | 120 |  | 120 |  |
| TRS configuration |  |  | Config 1 | TRS.2.1 TDD |  | N/A |  |
| TCI configuration |  |  | Config 1 | CSI-RS.Config.0 |  | N/A |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz Note5 |  | -99.03 |  | -99.03 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS Note4 | Config 1 | -90 |  | -90 |  |
| SS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -87 |  | -93 |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1 | 3 |  | -3 |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1 | 3 |  | -3 |  |
| IoNote3 |  | dBm/95.04 MHz Note5 | Config 1 | -56.25 |  | -59.25 |  |
| Propagation Condition |  |  | Config 1 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |  |  |

##### A.17.6.4.1.2 Test Requirements

The UE shall report the CGI of Cell 2 within 25*Tsmtc + 6*Tsi-rnti+20 ms +2 ms= 762 ms from the start of T2, allow 765 ms. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall be scheduled continuously throughout the test, and from the start of T3 until 775 ms the number of interrupted slots shall not exceed the allowed number as defined in clause 8.2.2.2.14.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

### A.17.6.5 RSTD measurements

#### A.17.6.5.1 NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA

##### A.17.6.5.1.1 Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC CONNECTED state meets the requirements specified in clause 9.9A.2 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

Supported test configurations are shown in table A.17.6.5.1.1-1. The test parameters are as given in table A.17.6.5.1.1-2, Table A.17.6.5.1.1-3, and table A.17.6.5.1.1-4.

Table A.17.6.5.1.1-1: Supported test configurations for NR RSTD

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layers.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the RedCap UE during T1. The measurement reporting delay test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #13 before T2.

Table A.17.6.5.1.1-2: General test parameters for RSTD measurement reporting delay

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Reference cell |  |  | Cell 1 | Reference cell is the cell in the DL-TDOA assistance data with respect to which the RSTD measurement is defined, as specified in TS 38.215 [4] and TS 37.355 [34]. The reference cell is the PCell in this test case. |
| Neighbor cells |  |  | Cell 2 and Cell 3 | Cell 2 and Cell 3 appear at the first and second places in the neighbour cell list in the DL-TDOA assistance data. |
| SSB configuration | Config 1 |  | SSB.3 FR2 |  |
| SMTC configuration | Config 1 |  | SMTC.1 |  |
| PDSCH RMC configuration | Config 1 |  | SR.1.1 FDD |  |
| RMSI CORESET RMC configuration | Config 1 |  | CR.3.1 TDD | As specified in clause A.3.1.2.1 |
| Dedicated CORESET RMC configuration | Config 1 |  | CCR.1.1 FDD |  |
| PRS Configuration | Config 1 |  | PRS.1.1 FR2 | As specified in clause A.3. 31 |
| Physical cell ID PCI |  |  | (PCI of Cell 1 – PCI of Cell 2)mod6=0and(PCI of Cell 1 – PCI of Cell 3)mod6=0 | The cell PCIs are selected such that the relative shifts of PRS patterns among cells are as given by the test parameters |
| CP length |  |  | Normal |  |
| DRX |  |  | OFF |  |
| Measurement gap |  |  | GP#24 or GP#13 | GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured |
| Radio frame receive time offset between the cells at the UE antenna connector |  | s | Cell 2 to Cell 1: 0Cell 3 to Cell 1: 3 | PRS are transmitted from synchronous cells |
| Expected RSTD |  | s | Cell 2: 3 Cell 3: 3Other neighbour cells: randomly between -3 and 3 | The expected RSTD is what is expected at the receiver. The corresponding parameter in the DL-TDOA assistance data specified in TS 37.355 [34] is the expectedRSTD indicator |
| Expected RSTD uncertainty for all neighbour cells |  | s | 5 | The corresponding parameter in the DL-TDOA assistance data specified in TS 37.355 [34] is the expectedRSTD-Uncertainty index |
| Number of cells provided in DL-TDOA assistance data |  |  | 3 | Including the reference cell |
| PRS muting info |  |  | Cell 1: ‘10’Cell 2: ‘01’Cell 3: ‘10’ | Correponds to prs-MutingInfo defined in TS 37.355 [34] |
| PRS resource RE offset |  |  | Cell 1: 0Cell 2: 0Cell 3: 1 | Cell 1 and Cell 3 are configured with different resource offsets |
| T1 |  | s | 3 | The length of the time interval from the beginning of each test |
| T2 |  | s | 1.28 | The length of the time interval that follows immediately after time interval T1 |
| AoA setup |  |  | Setup 1 | As defined in clause A.3.15.1 |
| Beam assumption |  |  | Rough | Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |

Table A.17.6.5.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

| Parameter |  | Unit | Cell 1 | Cell 2 | Cell 3 |
| --- | --- | --- | --- | --- | --- |
| NR RF Channel Number |  |  | 1 | 1 | 1 |
| Positiong frequency layer |  |  | 1 | 1 | 1 |
| BWchannel |  | MHz | 100: NRB,c = 66 | 100: NRB,c = 66 | 100: NRB,c = 66 |
| Correlation Matrix and Antenna Configuration |  |  | 1x2 Low | 1x2 Low | 1x2 Low |
| OCNG patterns defined in A.3.2.1 |  |  | OP.1 | N/A | N/A |
| EPRE ratio of PSS to SSS |  | dB | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note 3 | Config 1 | dBm/SCS | -89 |  |  |
| PRS ![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] |  | dB | -Infinity | -Infinity | -Infinity |
| Io Note 4 | Config 1 | dBm/95.04MHz | -57 | -57 | -57 |
| SSB_RP Note4 | Config 1 | dBm/SCS | -89 | -Infinity | -Infinity |
| SSB![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] | Config 1 | dB | 0 | -Infinity | -Infinity |
| Propagation Condition |  |  | AWGN |  |  |
| NOTE 1:  OCNG shall be used such that active cell (Cell 1) is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the slots with transmitted PRS.NOTE 2: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 3:  Interference from other cells and noise sources not specified in the test are assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 4:  SSB_RP and Io levels have been derived from other parameters and are given for information purpose. These are not settable test parameters. |  |  |  |  |  |

Table A.17.6.5.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

| Parameter |  | Unit | Cell 1 | Cell 2 | Cell 3 |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T2 | T2 | T2 |
| RF Channel Number |  |  | 1 | 1 | 1 |
| Positiong frequency layer |  |  | 1 | 1 | 1 |
| BWchannel |  | MHz | 100: NRB,c = 66 | 100: NRB,c = 66 | 100: NRB,c = 66 |
| Correlation Matrix and Antenna Configuration |  |  | 1x2 Low | 1x2 Low | 1x2 Low |
| OCNG patterns defined in A.3.2.1 |  |  | OP.1 | OP.1 | OP.1 |
| EPRE ratio of PSS to SSS |  | dB | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| EPRE ratio of PRS to SSS |  |  |  |  |  |
| PRACH configuration |  |  | FR2 PRACH configuration 1 | FR2 PRACH configuration 1 | FR2 PRACH configuration 1 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note 3 | Config 1 | dBm/SCS | -89 | -89 | -89 |
| PRS ![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] | Config 1 | dB | -5.45 | -11.67 | -11.67 |
| Io Note4 | Config 1 | dBm/95.04MHz | -58.49 | -58.49 | -58.49 |
| PRS ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | -6 | -13 | -13 |
| PRP Note 4 |  | dBm/SCS | -94.45 | -100.67 | -100.67 |
| Propagation Condition |  |  | AWGN |  |  |
| NOTE 1:  OCNG shall be used such that active cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the slots with transmitted PRS.NOTE 2: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 3:  Interference from other cells and noise sources not specified in the test are assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 4:  PRP and Io levels have been derived from other parameters and are given for information purpose. These are not settable test parameters. The Io is calculated based only on the symbols in which PRS is transmitted.NOTE 5: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |  |

##### A.17.6.5.1.2 Test Requirements

The RSTD measurement time without FH for RedCap fulfils the requirements specified in clause 9.9A.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 9.9.2A.5 starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD_1970049.

#### A.17.6.5.2 NR RSTD measurement reporting delay test case with PRS frequency hopping

##### A.17.6.5.2.1 Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 9.9A.2.6 in FR2 in standalone scenario when PRS frequency hopping is configured.

Supported test configurations are shown in table A.17.6.5.2.1-1. The test parameters are as given in table A.17.6.5.2.1-2, table A.17.6.5.2.1-3, and table A.17.6.5.2.1-4.

Table A.17.6.5.2.1-1: Supported test configurations for NR RSTD

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1: This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layers.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The test requirements apply when frequencyHopping is configured to UE.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #13 before T2.

Table A.17.6.5.2.1-2: General test parameters for RSTD measurement reporting delay

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Reference cell |  |  | Cell 1 | Reference cell is the cell in the DL-TDOA assistance data with respect to which the RSTD measurement is defined, as specified in TS 38.215 [4] and TS 37.355 [34]. The reference cell is the PCell in this test case. |
| Neighbor cells |  |  | Cell 2 and Cell 3 | Cell 2 and Cell 3 appear at the first and second places in the neighbour cell list in the DL-TDOA assistance data. |
| SSB configuration | Config 1 |  | SSB.1 RedCap FR2 |  |
| SMTC configuration | Config 1 |  | SMTC.1 RedCap |  |
| PDSCH RMC configuration | Config 1 |  | SR.3.2 TDD |  |
| RMSI CORESET RMC configuration | Config 1 |  | CR.3.1 TDD |  |
| Dedicated CORESET RMC configuration | Config 1 |  | CCR.3.1 TDD |  |
| PRS Configuration | Config 1 |  | PRS.1.6 FR2 | PRS configured with frequency hopping as specified in clause A.3.31 |
| Physical cell ID PCI |  |  | (PCI of Cell 1 – PCI of Cell 2)mod6=0and(PCI of Cell 1 – PCI of Cell 3)mod6=0 | The cell PCIs are selected such that the relative shifts of PRS patterns among cells are as given by the test parameters |
| CP length |  |  | Normal |  |
| DRX |  |  | OFF |  |
| Measurement gap |  |  | GP#24 or GP#13 | GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured |
| Radio frame receive time offset between the cells at the UE antenna connector |  | s | Cell 2 to Cell 1: 0Cell 3 to Cell 1: 3 | PRS are transmitted from synchronous cells |
| Expected RSTD |  | s | Cell 2: 3 Cell 3: 3Other neighbour cells: randomly between -3 and 3 | The expected RSTD is what is expected at the receiver. The corresponding parameter in the DL-TDOA assistance data specified in TS 37.355 [34] is the expectedRSTD indicator |
| Expected RSTD uncertainty for all neighbour cells |  | s | 5 | The corresponding parameter in the DL-TDOA assistance data specified in TS 37.355 [34] is the expectedRSTD-Uncertainty index |
| Number of cells provided in DL-TDOA assistance data |  |  | 3 | Including the reference cell |
| PRS muting info |  |  | Cell 1: ‘10’Cell 2: ‘01’Cell 3: ‘10’ | Correponds to prs-MutingInfo defined in TS 37.355 [34] |
| PRS resource RE offset |  |  | Cell 1: 0Cell 2: 0Cell 3: 1 | Cell 1 and Cell 3 are configured with different resource offsets |
| T1 |  | s | 3 | The length of the time interval from the beginning of each test |
| T2 |  | s | 1.28 | The length of the time interval that follows immediately after time interval T1 |
| AoA setup |  |  | Setup 1 | As defined in clause A.3.15.1 |
| Beam assumption |  |  | Rough | Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |

Table A.17.6.5.2.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

| Parameter |  | Unit | Cell 1 | Cell 2 | Cell 3 |
| --- | --- | --- | --- | --- | --- |
| NR RF Channel Number |  |  | 1 | 1 | 1 |
| Positiong frequency layer |  |  | 1 | 1 | 1 |
| BWchannel |  | MHz | 400: NRB,c = 264 | 400: NRB,c = 264 | 400: NRB,c = 264 |
| Correlation Matrix and Antenna Configuration |  |  | 1x2 Low | 1x2 Low | 1x2 Low |
| OCNG patterns defined in A.3.2.1 |  |  | OP.1 | N/A | N/A |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note 3 | Config 1 | dBm/SCS | -89 |  |  |
| PRS ![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] |  | dB | -Infinity | -Infinity | -Infinity |
| Io Note 4 | Config 1 | dBm/380.16MHz | -53.99 | -53.99 | -53.99 |
| SSB_RP Note4 | Config 1 | dBm/SCS | -89 | -Infinity | -Infinity |
| SSB![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] | Config 1 | dB | 0 | -Infinity | -Infinity |
| Propagation Condition |  |  | AWGN |  |  |
| NOTE 1:  OCNG shall be used such that active cell (Cell 1) is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the slots with transmitted PRS.NOTE 2: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 3:  Interference from other cells and noise sources not specified in the test are assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 4:  SSB_RP and Io levels have been derived from other parameters and are given for information purpose. These are not settable test parameters. |  |  |  |  |  |

Table A.17.6.5.2.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

| Parameter |  | Unit | Cell 1 | Cell 2 | Cell 3 |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T2 | T2 | T2 |
| RF Channel Number |  |  | 1 | 1 | 1 |
| Positiong frequency layer |  |  | 1 | 1 | 1 |
| BWchannel |  | MHz | 400: NRB,c = 264 | 400: NRB,c = 264 | 400: NRB,c = 264 |
| Correlation Matrix and Antenna Configuration |  |  | 1x2 Low | 1x2 Low | 1x2 Low |
| OCNG patterns defined in A.3.2.1 |  |  | OP.1 | OP.1 | OP.1 |
| PRACH configuration |  |  | FR2 PRACH configuration 1 | FR2 PRACH configuration 1 | FR2 PRACH configuration 1 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note 3 | Config 1 | dBm/SCS | -89 | -89 | -89 |
| PRS ![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] | Config 1 | dB | -5.44 | -11.67 | -11.67 |
| Io Note4 | Config 1 | dBm/380.16MHz | -52.68 | -52.68 | -52.68 |
| PRS ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | dB | -6 | -13 |
| PRP Note 4 |  | dBm/SCS | dBm/SCS | -94.44 | -100.67 |
| Propagation Condition |  |  | AWGN |  |  |
| NOTE 1:  OCNG shall be used such that active cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the slots with transmitted PRS.NOTE 2: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 3:  Interference from other cells and noise sources not specified in the test are assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 4:  PRP and Io levels have been derived from other parameters and are given for information purpose. These are not settable test parameters. The Io is calculated based only on the symbols in which PRS is transmitted.NOTE 5: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |  |

##### A.17.6.5.2.2 Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 9.9A.2.6.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 9.9A.2.6 starting from the beginning of time interval T2.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD_1970049.

### A.17.6.6 UE Rx-Tx Measurements

#### A.17.6.6.1 UE Rx-Tx measurement reporting delay for single positioning frequency layer in FR2 SA without RX FH in RRC_CONNECTED mode

##### A.17.6.6.1.1 Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement without RX FH in RRC_CONNECTED mode meets the requirements specified in clause 9.9A.4.5 in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configuration is listed in table A.17.6.6.1.1-1.

Table A.17.6.6.1.1-1: Supported test configurations.

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB and PRS SCS, 100 MHz bandwidth, TDD duplex mode |

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. In nr-Multi-RTT-RequestLocationInformation, nr-DL-PRS-RxHoppingRequest is not present.

The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID #13 or ID #24 before T2.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.17.6.6.1.1-2 and table A.17.6.6.1.1-3 respectively.

Table A.17.6.6.1.1-2: General test parameters

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1 | Cell 1 | Cell 1 is the PCell in NR-Multi-RTT-ProvideAssistanceData [34]. |
| Neighbour cell |  | 1 | Cell 2 | Cell 2 is a neighbour cell in NR-Multi-RTT-ProvideAssistanceData [34]. |
| RF Channel Number |  | 1 | 1 | For both Cell 1 and Cell 2 |
| BWchannel | MHz | 1 | 100: NRB,c = 66 |  |
| SSB configuration |  | 1 | SSB.2 RedCap FR2 |  |
| SMTC configuration |  | 1 | SMTC.1 RedCap |  |
| Measurement gap |  | 1 | GP#24 or GP#13 Note 1 |  |
| CP length |  | 1 | Normal |  |
| DRX |  | 1 | OFF |  |
| Time offset between serving and neighbour cells | s | 1 | 3 | Synchronous cells |
| Expected RSTD | s | 1 | 3 |  |
| Expected RSTD uncertainty | s | 1 | 5 |  |
| T1 | s | 1 | 5 |  |
| T2 | s | 1 | 20 |  |
| NOTE 1: GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured. |  |  |  |  |

Table A.17.6.6.1.1-3: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  | 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  | 1 | Rough |  | Rough |  |
| TDD configuration |  | 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| PDSCH RMC configuration |  | 1 | SR.3.1 TDD |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 TDD |  | N/A |  |
| OCNG Patterns |  | 1 | OP.1 |  | OP.1 |  |
| EPRE ratio of PSS to SSS | dB | 1 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |  |
| EPRE ratio of PRS to SSS |  |  |  |  |  |  |
| TRS Configuration |  | 1 | TRS.2.1 TDD |  | N/A |  |
| Initial BWP configuration |  | 1 | DLBWP.0.1 ULBWP.0.1 |  | N/A |  |
| Active DL BWP configuration |  | 1 | DLBWP.1.1 RedCap |  | N/A |  |
| Active UL BWP configuration |  | 1 | ULBWP.1.1 RedCap |  | N/A |  |
| PRS configuration |  | 1 | PRS.1.5 FR2 |  | PRS.1.5 FR2 |  |
| PRS muting info |  | 1 | ‘10’ |  | ‘01’ |  |
| SRS configuration |  | 1 | POS-SRS.3 |  | N/A |  |
| Note 2 | dBm/SCS | 1 | -89 |  |  |  |
| Note 2 | dBm/SCS | 1 | -98 |  |  |  |
| PRS | dB | 1 | -Infinity | -2.41 | -Infinity | -12.12 |
| PRS | dB | 1 | -Infinity | -2 | -Infinity | -10 |
| PRP Note 3 | dBm/SCS kHz | 1 | -Infinity | -91 | -Infinity | -99 |
| Io | dBm/92.16 MHz | 1 | N/A | -57.63 | N/A | -57.63 |
| Propagation Condition |  | 1 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over sub-carriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: PRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 8: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |  |  |

##### A.17.6.6.1.2 Test requirements

The UE Rx-Tx time difference measurement time fulfills the requirements specified in clause 9.9A.4.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1A.18.3.

#### A.17.6.6.2 UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR2 SA in RRC_CONNECTED state

##### A.17.6.6.2.1 Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement with Rx FH meets the requirements specified in clause 9.9A.4.8 in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.17.6.6.2.1-1.

Table A.17.6.6.2.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1: This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID #13 or ID #24 before T2.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.17.6.6.2.1-2 and table A.17.6.6.2.1-3, respectively.

Table A.17.6.6.2.1-2: General test parameters

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1 | Cell 1 | Cell 1 is the PCell in NR-Multi-RTT-ProvideAssistanceData [34]. |
| Neighbour cell |  | 1 | Cell 2 | Cell 2 is a neighbour cell in NR-Multi-RTT-ProvideAssistanceData [34]. |
| RF Channel Number |  | 1 | 1 | For both Cell 1 and Cell 2 |
| BWchannel | MHz | 1 | 400: NRB,c = 264 |  |
| SSB configuration |  | 1 | SSB.3 FR2 |  |
| SMTC configuration |  | 1 | SMTC.1 |  |
| Measurement gap |  | 1 | GP#24 or GP#13 Note 1 |  |
| CP length |  | 1 | Normal |  |
| DRX |  | 1 | OFF |  |
| Time offset between serving and neighbour cells | s | 1 | 3 | Synchronous cells |
| PRS RX hopping request |  | 1 | requested |  |
| T1 | s | 1 | 5 |  |
| T2 | s | 1 | 10 |  |
| NOTE 1: GP#24 is configured if RedCap UE supports MG#24, otherwise GP#13 is configured. |  |  |  |  |

Table A.17.6.6.2.1-3: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  | 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  | 1 | Rough |  | Rough |  |
| TDD configuration |  | 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| PDSCH RMC configuration |  | 1 | SR.3.1 TDD |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 TDD |  | N/A |  |
| OCNG Patterns |  | 1 | OP.1 |  | OP.1 |  |
| EPRE ratio of PSS to SSS | dB | 1 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |  |
| EPRE ratio of PRS to SSS |  |  |  |  |  |  |
| TRS Configuration |  | 1 | TRS.2.1 TDD |  | N/A |  |
| Initial BWP configuration |  | 1 | DLBWP.0.1 ULBWP.0.1 |  | N/A |  |
| Active DL BWP configuration |  | 1 | DLBWP.1.1 RedCap |  | N/A |  |
| Active UL BWP configuration |  | 1 | ULBWP.1.1 RedCap |  | N/A |  |
| PRS configuration |  | 1 | PRS.1.6 FR2 |  | PRS.1.6 FR2 |  |
| PRS muting info |  | 1 | ‘10’ |  | ‘01’ |  |
| SRS configuration |  | 1 | POS-SRS.3 |  | N/A |  |
| Note 2 | dBm/SCS | 1 | -89 |  |  |  |
| Note 2 | dBm/15 kHz | 1 | -98 |  |  |  |
| PRS | dB | 1 | -Infinity | -2.41 | -Infinity | -12.12 |
| PRS | dB | 1 | -Infinity | -2 | -Infinity | -10 |
| PRP Note 3 | dBm/SCS | 1 | -Infinity | -91 | -Infinity | -99 |
| Io | dBm/ 380.16MHz | 1 | N/A | -51.61 | N/A | -51.61 |
| Propagation Condition |  | 1 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: PRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 8: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |  |  |

##### A.17.6.6.2.2 Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9A.4.8.

The RedCap UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1A.18.3.

### A.17.6.7 PRS-RSRP measurements

#### A.17.6.7.1 PRS-RSRP measurement delay test case for RedCap positioning without Rx FH in RRC_CONNECTED state in FR2

##### A.17.6.7.1.1 PRS-RSRP measurement delay test case for single positioning frequency layer

###### A.17.6.7.1.1.1 Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements specified in clause 9A.9.3.5 for single positioning frequency layer under AWGN propagation conditions in standalone scenario. Supported test configurations are shown in table A.17.6.7.1.1.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. The measurement reporting delay test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform PRS-RSRP measurement with RX FH via NR-DL-AoD-RequestLocationInformation or the UE is configured by the LMF to perform PRS-RSRP measurement with RX FH but reports the PRS-RSRP measurement based on the single hop in NR-DL-AoD-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is DT after slot #n, where DT = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.6.7.1.1.1-2 and table A.17.6.7.1.1.1-3.

Table A.17.6.7.1.1.1-1: supported test configurations for PRS RSRP measurement for FR2

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.6.7.1.1.1-2: General test parameters for PRS RSRP measurement reporting delay

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | 1: Cell 1 and Cell 2 | One TDD carrier frequency is used for the NR cells. |
| Active cell |  | 1 | NR cell 1 (Pcell) | Cell 1 is the PCell and the DL-AoD reference cell in the positioning assistance data. |
| Neighbour cell |  | 1 | NR cell 2 | Cell 2 is a neighbour cell in the positioning assistance data. |
| Gap Pattern Id |  | 1 | GP#13 or GP#24Note1 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | 1 | 39 |  |
| SMTC parameters |  | 1 | SMTC.1 | As specified in clause A.3.11 |
| SSB parameters |  | 1 | SSB.3 FR2 | As specified in clause A.3.10.2 |
| A3-Offset | dB | 1 | -6 |  |
| Hysteresis | dB | 1 | 0 |  |
| CP length |  | 1 | Normal |  |
| TimeToTrigger | s | 1 | 0 |  |
| Filter coefficient |  | 1 | 0 | L3 filtering is not used |
| DRX |  | 1 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | 1 | 3ms | Synchronous cells. |
| Expected RSTD | ms | 1 | 3 |  |
| Expected RSTD uncertainty | ms | 1 | 5 |  |
| T1 | s | 1 | 5 |  |
| T2 | s | 1 | 7 |  |
| NOTE 1: GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured. |  |  |  |  |

Table A.17.6.7.1.1.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  |  | 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  |  | 1 | Rough |  | Rough |  |
| TDD configuration |  |  | 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| Duplex mode |  |  | 1 | TDD |  | TDD |  |
| BWchannel |  | MHz | 1 | 100: NRB,c = 66 |  | 100: NRB,c = 66 |  |
| BWP configuration | Initial DL BWP |  | 1 | DLBWP.0.1 |  | N/A |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | N/A |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | N/A |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | N/A |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | 1 | SR.3.1 TDD |  | - |  |
| CORESET Reference Channel |  |  | 1 | CR.3.1 TDD |  | - |  |
| Dedicated CORESET RMC configuration |  |  | 1 | CCR.3.1 TDD |  | - |  |
| TRS configuration |  |  | 1 | TRS.2.1 TDD |  | - |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 1 | 120 |  | 120 |  |
| PRS configuration |  |  | 1 | PRS.1.1 FR2 |  | PRS.1.1 FR2 |  |
| PRS muting configuration |  |  | 1 | ‘10’ |  | ‘01’ |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | 1 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15kHz Note5 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS Note4 | 1 | -89 |  | -89 |  |
| SSB_RP Note 3 |  | dBm/SCS Note5 | 1 | -91 | -91 | -Infinity | -99 |
| PRP Note 3 |  | dBm/SCS Note5 | 1 | -Infinity | -91 | -Infinity | -99 |
| PRS |  | dB | 1 | -Infinity | -2.41 | -Infinity | -12.12 |
| PRS |  | dB | 1 | -Infinity | -2 | -Infinity | -10 |
| SSB |  | dB | 1 | -2 | -2 | -Infinity | -10 |
| IoNote3 |  | dBm/95.04 MHz Note5 | 1 | -57.89 | -57.63 | -57.89 | -57.63 |
| Propagation Condition |  |  | 1 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SSB_RP/PRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 8: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |  |  |  |

###### A.17.6.7.1.1.2 Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 9.9A.3.5. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9A.3.5 starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause10.1A.17.3.

##### A.17.6.7.1.2 PRS-RSRP measurement delay test case for dual positioning frequency layer

###### A.17.6.7.1.2.1 Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements specified in clause 9.9A.3.5 for dual positioning frequency layers under AWGN propagation conditions in standalone scenario. Supported test configurations are shown in table A.17.6.7.1.2.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the different frequency from the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is DT after slot #n, where DT = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.6.7.1.2.1-2, and table A.17.6.7.1.2.1-3.

Table A.17.6.7.1.2.1-1: supported test configurations for PRS RSRP measurement for FR2

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.6.7.1.2.1-2: General test parameters for PRS RSRP measurement reporting delay

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1 | NR cell 1 (Pcell) | Cell 1 is the PCell and the DL-AoD reference cell in the positioning assistance data. |
| Neighbour cell |  | 1 | NR cell 2 | Cell 2 is a neighbour cell in the positioning assistance data. |
| Gap Pattern Id |  | 1 | GP#13 or GP#24Note1 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | 1 | 39 |  |
| SMTC parameters |  | 1 | SMTC.1 | As specified in clause A.3.11 |
| SSB parameters |  | 1 | SSB.3 FR2 | As specified in clause A.3.10.2 |
| A3-Offset | dB | 1 | -6 |  |
| Hysteresis | dB | 1 | 0 |  |
| CP length |  | 1 | Normal |  |
| TimeToTrigger | s | 1 | 0 |  |
| Filter coefficient |  | 1 | 0 | L3 filtering is not used |
| DRX |  | 1 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | 1 | 3ms | Synchronous cells. |
| Expected RSTD | ms | 1 | 3 |  |
| Expected RSTD uncertainty | ms | 1 | 5 |  |
| T1 | s | 1 | 5 |  |
| T2 | s | 1 | 7 |  |
| NOTE 1: GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured. |  |  |  |  |

Table A.17.6.7.1.2.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  |  | 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  |  | 1 | Rough |  | Rough |  |
| NR RF Channel Number |  |  | 1 | 1 |  | 2 |  |
| TDD configuration |  |  | 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| Duplex mode |  |  | 1 | TDD |  | TDD |  |
| BWchannel |  | MHz | 1 | 100: NRB,c = 66 |  | 100: NRB,c = 66 |  |
| BWP configuration | Initial DL BWP |  | 1 | DLBWP.0.1 |  | N/A |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | N/A |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | N/A |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | N/A |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | 1 | SR.3.1 TDD |  | - |  |
| CORESET Reference Channel |  |  | 1 | CR.3.1 TDD |  | - |  |
| Dedicated CORESET RMC configuration |  |  | 1 | CCR.3.1 TDD |  | - |  |
| TRS configuration |  |  | 1 | TRS.2.1 TDD |  | - |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 1 | 120 |  | 120 |  |
| PRS configuration |  |  | 1 | PRS.1.1 FR2 |  | PRS.1.2 FR2 |  |
| PRS muting configuration |  |  | 1 | ‘10’ |  | ‘01’ |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | 1 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15kHz Note5 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS Note4 | 1 | -89 |  | -89 |  |
| SSB_RP Note 3 |  | dBm/SCS Note5 | 1 | -92 | -92 | -Infinity | -102 |
| PRP Note 3 |  | dBm/SCS Note5 | 1 | -Infinity | -92 | -Infinity | -102 |
| PRS |  | dB | 1 | -Infinity | -3 | -Infinity | -13 |
| PRS |  | dB | 1 | -Infinity | -3 | -Infinity | -13 |
| SSB |  | dB | 1 | -3 | -3 | -Infinity | -13 |
| IoNote3 |  | dBm/95.04 MHz Note5 | 1 | -58.25 | -58.25 | -60.01 | -59.80 |
| Propagation Condition |  |  | 1 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SSB_RP/PRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 8: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |  |  |  |

###### A.17.6.7.1.2.2 Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 9.9A.3.5.The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9A.3.5 starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause10.1A.17.3.

#### A.17.6.7.2 PRS-RSRP measurement delay with FH in RRC_CONNECTED state in FR2

##### A.17.6.7.2.1 Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement with FH by a RedCap UE meets requirements specified in clause 9.9A.3.6 for single positioning frequency layer under AWGN propagation conditions in standalone scenario. Supported test configurations are shown in table A.17.6.7.2.1-1

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.6.7.2.1-2, and table A.17.6.7.2.1-3.

Table A.17.6.7.2.1-1: Supported test configurations for PRS RSRP measurement

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, UE bandwidth 100 MHz, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1:   This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

Table A.17.6.7.2.1-2: General test parameters for PRS RSRP measurement reporting delay

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1 | 1: Cell 1 and Cell 2 | One TDD carrier frequency is used for the NR cells. |
| Active cell |  | Config 1 | NR cell 1 (PCell) | Cell 1 is the PCell and the DL-AoD reference cell in the positioning assistance data. |
| Neighbour cell |  | Config 1 | NR cell 2 | Cell 2 is a neighbour cell in the positioning assistance data. |
| Gap Pattern Id |  | Config 1 | GP#13 or GP#24Note1 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1 | 39 |  |
| SMTC parameters |  | Config 1 | SMTC.1 | As specified in clause A.3.11 |
| SSB parameters |  | Config 1 | SSB.3 FR2 | As specified in clause A.3.10.2 |
| CP length |  | Config 1 | Normal |  |
| DRX |  | Config 1 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | Config 1 | 3s | Synchronous cells. |
| Expected RSTD | s | Config 1 | 3 |  |
| Expected RSTD uncertainty | s | Config 1 | 5 |  |
| PRS RX hopping request |  | Config 1 | Present |  |
| T1 | s | Config 1 | 5 |  |
| T2 | s | Config 1 | 7 |  |
| NOTE 1: GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured. |  |  |  |  |

Table A.17.6.7.2.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  |  | Config 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  |  | Config 1 | Rough |  | Rough |  |
| TDD configuration |  |  | Config 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| Duplex mode |  |  | Config 1 | TDD |  | TDD |  |
| BWchannel |  | MHz | Config 1 | 400: NRB,c = 264 |  | 400: NRB,c = 264 |  |
| BWP configuration | Initial DL BWP |  | Config 1 | DLBWP.0.1 |  | N/A |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | N/A |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | N/A |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | N/A |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1 | SR.3.1 TDD |  | - |  |
| CORESET Reference Channel |  |  | Config 1 | CR.3.1 TDD |  | - |  |
| Dedicated CORESET RMC configuration |  |  | Config 1 | CCR.3.1 TDD |  | - |  |
| TRS configuration |  |  | Config 1 | TRS.2.1 TDD |  | - |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1 | 120 |  | 120 |  |
| PRS configuration |  |  | Config 1 | PRS.1.6 FR2 |  | PRS.1.6 FR2 |  |
| PRS muting configuration |  |  | Config 1 | ‘10’ |  | ‘01’ |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15kHz Note5 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS Note4 | Config 1 | -89 |  | -89 |  |
| SSB_RP Note 3 |  | dBm/SCS Note5 | Config 1 | -91 | -91 | -Infinity | -99 |
| PRP Note 3 |  | dBm/SCS Note5 | Config 1 | -Infinity | -91 | -Infinity | -99 |
| PRS |  | dB | Config 1 | -Infinity | -2.41 | -Infinity | -12.12 |
| PRS |  | dB | Config 1 | -Infinity | -2 | -Infinity | -10 |
| SSB |  | dB | Config 1 | -2 | -2 | -Infinity | -10 |
| IoNote3 |  | dBm/ 380.16MHz Note5 | Config 1 | -53.99 | -51.61 | -53.99 | -51.61 |
| Propagation Condition |  |  | Config 1 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that active cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the subframes with transmitted PRS.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SSB_RP/PRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 8: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |  |  |  |

##### A.17.6.7.2.2 Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 9.9A.3.6. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9A.3.6 starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause10.1A.17.3, i.e., between PRS RSRP_0 and PRS RSRP_126.

### A.17.6.8 PRS-RSRPP Measurements

#### A.17.6.8.1 PRS-RSRPP measurement delay without FH in RRC_CONNECTED state in FR2

##### A.17.6.8.1.1 Test Purpose and Environment

The purpose of the test is to verify that the PRS RSRPP measurement without FH by a RedCap UE meets requirements specified in clause 9.9A.5.5 for single positioning frequency layer under 2-tap channel propagation conditions in standalone scenario. Supported test configurations are shown in table A.17.6.8.1.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.6.8.1.1-2, and table A.17.6.8.1.1-3.

Table A.17.6.8.1.1-1: supported test configurations for PRS RSRPP measurement for FR2

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100MHz bandwidth, TDD duplex mode |

Table A.17.6.8.1.1-2: General test parameters for PRS RSRPP measurement reporting delay

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1 | 1: Cell 1 and Cell 2 | One TDD carrier frequency is used for the NR cells. |
| Active cell |  | Config 1 | NR cell 1 (PVell) | Cell 1 is the PCell and the DL-AoD reference cell in the positioning assistance data. |
| Neighbour cell |  | Config 1 | NR cell 2 | Cell 2 is a neighbour cell in the positioning assistance data. |
| Gap Pattern Id |  | Config 1 | GP#13 or GP#24Note1 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1 | 39 |  |
| SMTC parameters |  | Config 1 | SMTC.1 | As specified in clause A.3.11 |
| SSB parameters |  | Config 1 | SSB.3 FR2 | As specified in clause A.3.10.2 |
| CP length |  | Config 1 | Normal |  |
| DRX |  | Config 1 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | Config 1 | 3s | Synchronous cells. |
| Expected RSTD | s | Config 1 | 3 |  |
| Expected RSTD uncertainty | s | Config 1 | 5 |  |
| PRS RX hopping request |  | 1, 2, 3, 4 | NOT present |  |
| T1 | s | Config 1 | 5 |  |
| T2 | s | Config 1 | 7 |  |
| NOTE 1: GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured. |  |  |  |  |

Table A.17.6.8.1.1-3: Cell-specific test parameters for PRS RSRPP measurement reporting delay

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  |  | Config 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  |  | Config 1 | Rough |  | Rough |  |
| TDD configuration |  |  | Config 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| Duplex mode |  |  | Config 1 | TDD |  | TDD |  |
| BWchannel |  | MHz | Config 1 | 100: NRB,c = 66 |  | 100: NRB,c = 66 |  |
| BWP BW |  | MHz | Config 1 | 100: NRB,c = 66 |  | 100: NRB,c = 66 |  |
| BWP configuration | Initial DL BWP |  | Config 1 | DLBWP.0.1 |  | N/A |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | N/A |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | N/A |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | N/A |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1 | SR.3.1 TDD |  | - |  |
| CORESET Reference Channel |  |  | Config 1 | CR.3.1 TDD |  | - |  |
| Dedicated CORESET RMC configuration |  |  | Config 1 | CCR.3.1 TDD |  | - |  |
| TRS configuration |  |  | Config 1 | TRS.2.1 TDD |  | - |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1 | 120 |  | 120 |  |
| PRS configuration |  |  | Config 1 | PRS.1.3 FR2 |  | PRS.1.3 FR2 |  |
| PRS muting configuration |  |  | Config 1 | ‘10’ |  | ‘01’ |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15kHz Note5 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS Note4 | Config 1 | -89 |  | -89 |  |
| SS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -89 | -89 | -Infinity | -89 |
| PRS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -Infinity | -91 | -Infinity | -99 |
| PRS |  | dB | Config 1 | -Infinity | -2.41 | -Infinity | -12.12 |
| PRS |  | dB | Config 1 | -Infinity | -2 | -Infinity | -10 |
| IoNote3 |  | dBm/95.04 MHz Note5 | Config 1 | -60.01 | -57.63 | -60.01 | -57.63 |
| Propagation Condition |  |  | Config 1 | Two-tap channel defined in 38.101-4 annex B.2.4, a = 1, $\tau  _{d}=0.45 $ µs and $ f_{D}=5 $ Hz |  |  |  |
| NOTE 1: OCNG shall be used such that active cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the subframes with transmitted PRS.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP/PRS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 8: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |  |  |  |

##### A.17.6.8.1.2 Test Requirements

The PRS RSRPP measurement time fulfils the requirements specified in clause 9.9A.5.5. The UE shall perform and report the PRS RSRPP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9A.5.5 starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRPP measurement for each correct event shall be within the PRS RSRPP reporting range specified in clause10.1A.19, i.e., between PRS RSRPP_0 and PRS RSRPP_126.

#### A.17.6.8.2 PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR2 SA in RRC_CONNECTED state

##### A.17.6.8.2.1 Test Purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement requirements with Rx FH in RRC_CONNECTED state meets the delay requirements specified in clause 9.9A.5.8 in an environment with two-tap channel propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.17.6.8.2.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the Pcell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.6.8.2.1-2, and table A.17.6.8.2.1-3.

Table A.17.6.8.2.1-1: supported test configurations for PRS-RSRPP measurement for FR2

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1:   This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

Table A.17.6.8.2.1-2: General test parameters for PRS-RSRPP measurement reporting delay

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1 | 1: Cell 1 and Cell 2 | One TDD carrier frequency is used for the NR cells. |
| Active cell |  | Config 1 | NR cell 1 (PCell) | Cell 1 is the PCell and the DL-AoD reference cell in the positioning assistance data. |
| Neighbour cell |  | Config 1 | NR cell 2 | Cell 2 is a neighbour cell in the positioning assistance data. |
| Gap Pattern Id |  | Config 1 | GP#13 or GP#24Note1 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1 | 39 |  |
| SMTC parameters |  | Config 1 | SMTC.1 | As specified in clause A.3.11 |
| SSB parameters |  | Config 1 | SSB.3 FR2 | As specified in clause A.3.10.2 |
| A3-Offset | dB | Config 1 | -6 |  |
| Hysteresis | dB | Config 1 | 0 |  |
| CP length |  | Config 1 | Normal |  |
| TimeToTrigger | s | Config 1 | 0 |  |
| Filter coefficient |  | Config 1 | 0 | L3 filtering is not used |
| DRX |  | Config 1 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | Config 1 | 3s | Synchronous cells. |
| PRS RX hopping request |  | 1 | requested |  |
| Expected RSTD | s | Config 1 | 3 |  |
| Expected RSTD uncertainty | s | Config 1 | 5 |  |
| T1 | s | Config 1 | 5 |  |
| T2 | s | Config 1 | 7 |  |
| NOTE 1: GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured. |  |  |  |  |

Table A.17.6.8.2.1-3: Cell-specific test parameters for PRS-RSRPP measurement reporting delay

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  |  | Config 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  |  | Config 1 | Rough |  | Rough |  |
| TDD configuration |  |  | Config 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| Duplex mode |  |  | Config 1 | TDD |  | TDD |  |
| BWchannel |  | MHz | Config 1 | 400: NRB,c = 264 |  | 400: NRB,c = 264 |  |
| BWP BW |  | MHz | Config 1 | 400: NRB,c = 264 |  | 400: NRB,c = 264 |  |
| BWP configuration | Initial DL BWP |  | Config 1 | DLBWP.0.1 |  | N/A |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | N/A |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1RedCap |  | N/A |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1RedCap |  | N/A |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1 | SR.3.1 TDD |  | - |  |
| CORESET Reference Channel |  |  | Config 1 | CR.3.1 TDD |  | - |  |
| Dedicated CORESET RMC configuration |  |  | Config 1 | CCR.3.1 TDD |  | - |  |
| TRS configuration |  |  | Config 1 | TRS.2.1 TDD |  | - |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1 | 120 |  | 120 |  |
| PRS configuration |  |  | Config 1 | PRS.1.6 FR2 |  | PRS.1.6 FR2 |  |
| PRS muting configuration |  |  | Config 1 | ‘10’ |  | ‘01’ |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15kHz Note5 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS Note4 | Config 1 | -89 |  | -89 |  |
| SS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -89 | -89 | -Infinity | -89 |
| PRS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -Infinity | -91 | -Infinity | -99 |
| PRS |  | dB | Config 1 | -Infinity | -2.41 | -Infinity | -12.12 |
| PRS |  | dB | Config 1 | -Infinity | -2 | -Infinity | -10 |
| IoNote3 |  | dBm/ 380.16MHz Note5 | Config 1 | -50.98 | -51.61 | -50.98 | -51.61 |
| Propagation Condition |  |  | Config 1 | Two-tap channel defined in 38.101-4 annex B.2.4, a = 1, $\tau  _{d}=0.45 $ µs and $ f_{D}=5 $ Hz |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP/PRS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 8: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |  |  |  |

##### A.17.6.8.2.2 Test Requirements

The PRS-RSRPP measurement time fulfils the requirements specified in clause 9.9A.5.8. The UE shall perform and report the PRS-RSRPP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9A.5.8 starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS-RSRPP measurement for each correct event shall be within the PRS-RSRPP reporting range specified in clause 10.1A.19, i.e., between PRS RSRPP_0 and PRS RSRPP_126.

## A.17.7 Measurement Performance requirements

### A.17.7.1 SS-RSRP

#### A.17.7.1.1 SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

##### A.17.7.1.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy for RedCap UE is within the specified limits. This test will verify the requirements in clauses10.1.3A.3 for intra-frequency measurements.

##### A.17.7.1.1.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.7.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in table A.17.7.1.1.2-2 and A.17.7.1.1.2-3. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1. The test consists of two time phases T1 and T2.

Table A.17.7.1.1.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.7.1.1.2-2: SS-RSRP  Intra frequency general test parameters

| Parameter | Unit | T1 |  | T2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Cell ID |  | 489 | 0 | 489 | 0 |
| SSB ARFCN |  | freq1 |  | freq1 |  |
| Duplex mode |  | TDD |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel | MHz | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  | 24 |  | 24 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - | DLBWP.0.1 | - |
| Downlink dedicated BWP configuration |  | DLBWP.1.1 | - | DLBWP.1.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - | ULBWP.0.1 | - |
| Uplink dedicated BWP configuration |  | ULBWP.1.1 | - | ULBWP.1.1 | - |
| DRX cycle configuration |  | Not applicable | - | Not applicable | - |
| TRS configuration |  | TRS.2.1 TDD | - | TRS.2.1 TDD | - |
| TCI state |  | TCI.State.0 | - | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3. 2TDD | - | SR.3. 2 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - | CR.3.1 TDD | - |
| Dedicated CORESET Reference channel |  | CCR.3.1 TDD | - | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.3 | OP.3 | OP.3 | OP.3 |
| SSB configuration |  | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 |
| SMTC configuration |  | SMTC.1 | SMTC.1 | SMTC.1 | SMTC.1 |
| Time offset with Cell 1 | s | - | 3 | - | 3 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Propagation conditions |  | AWGN | AWGN | AWGN | AWGN |
| Antenna configuration |  | 1x2 | 1x2 | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: VoidNOTE 3: VoidNOTE 4: VoidNOTE 5:  Void |  |  |  |  |  |

Table A.17.7.1.1.2-3: SS-RSRP Intra frequency OTA related test parameters

| Parameter | Unit | T1 |  | T2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |  |  |
| Assumption for UE beamsNote 7 |  | Rough |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15 kHzNote4 | -91.6 |  | N/A |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote4 | -82.6 |  | N/A |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 6.0 | 1.0 | N/A | N/A |
| Es | dBm/SCSNote4 |  |  | (Table B.2.2-2 Rx Beam Peak +2.1 dB) | (Table B.2.2-2 Rx Beam Peak +2.1 dB) |
| SSB_RPNote2 | dBm/SCS | -76.6 | -81.6 | (Table B.2.2-2 Rx Beam Peak +2.1 dB) | (Table B.2.2-2 Rx Beam Peak +2.1 dB) |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot]BB Note6 | dB | 2.44 | -5.98 | -5.98 | -5.98 |
| IoNote2 | dBm/95.04 MHz Note4 | -50.05 |  | (Table B.2.2-2 Rx Beam Peak +29.70 dB) |  |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: SSB_RP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: VoidNOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: VoidNOTE 6: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] Table 6.2.1.3-4.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |

##### A.17.7.1.1.3 Test Requirements

The SS-RSRP measurement accuracy shall fulfil the absolute accuracy requirements in clauses 10.1A.3.1.1 and relative accuracy requirements in clause 10.1A.3.1.2. The following requirements are to be verified:

During T1:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.17.7.1.1.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1A.3.1.2-1.

During T2:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.17.7.1.1.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1A.3.1.2-1.

During T1 and T2:

Relative accuracy of Cell 1 during T2 compared with Cell 1 during T1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1A.3.1.2-1

Relative accuracy of Cell 2 during T2 compared with Cell 2 during T1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1A.3.1.2-1.

Table A.17.7.1.1.3-1: SS-RSRP absolute accuracy test requirement

|  | Test requirement Notes1,2,3 |
| --- | --- |
| Cell 1 | SSB_RP1 -δ +Gmin ≤ Reported RSRP(dBm) ≤ SSB_RP1 +δ +Gmax |
| Cell 2 | SSB_RP2 -δ +Gmin ≤ Reported RSRP(dBm) ≤ SSB_RP2 +δ +Gmax |
| NOTE 1:  SSB_RPn is the  equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone configured in the test for the cell n under considerationNOTE 2:  δ is the RSRP absolute accuracy requirement from Table 10.1.3.1.1-1, selected according to the Io used in the testNOTE 3:  Gmin and Gmax are the minimum and maximum UE gain values from Table B.2.1.5.1-1, selected according to the UE power class |  |

#### A.17.7.1.2 SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

##### A.17.7.1.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1A.5.1.1 and 10.1.5A.1.2 for intrer-frequency measurements with the testing configurations for NR cells in table A.17.7.1.2.1-1.

Table A.17.7.1.2.1-1: Applicable NR configurations for FR2 inter-frequency SS-RSRP accuracy test

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

##### A.17.7.1.2.2 Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 1 and Cell 2 are given in table A.17.7.1.2.2-1 and table A.17.7.1.2.2-2 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in A.17.7.1.2.2-1

The inter-frequency measurements are supported by a measurement gap.

Table A.17.7.1.2.2-1: SS-RSRP inter-frequency test parameters

| Parameter |  | Config | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| SSB ARFCN |  | 1~2 |  | freq1 | freq2 | freq1 | freq2 |
| BWchannel |  | 1~2 |  | 100:NPRB,c = 66 |  | 100:NPRB,c = 66 |  |
| Data PRBs allocated |  | 1 |  | 24 |  | 24 |  |
|  |  | 2 |  | 48 |  | 48 |  |
| Gap pattern ID |  |  |  | 0 |  | 0 |  |
| Duplex mode |  | 1~2 |  | TDD |  | TDD |  |
| TDD configuration |  | 1~2 |  | TDDConf.3.1 |  | TDDConf.3.1 |  |
| PDSCH Reference measurement channel |  | 1 |  | SR.3. 2 TDD | - | SR.3. 2 TDD | - |
|  |  | 2 |  | SR.3.3 TDD |  | SR.3.3 TDD |  |
| RMSI CORESET Reference Channel |  | 1 |  | CR.3.1 TDD | - | CR.3.1 TDD | - |
|  |  | 2 |  | CR.3.2 TDD |  | CR.3.2 TDD |  |
| Dedicated CORESET Reference Channel |  | 1 |  | CCR.3.1 TDD | - | CCR.3.1 TDD | - |
|  |  | 2 |  | CCR.3.7 TDD |  | CCR.3.7 TDD |  |
| SSB configuration |  | 1 |  | SSB.3 FR2 |  | SSB.3 FR2 |  |
|  |  | 2 |  | SSB.4 FR2 |  | SSB.4 FR2 |  |
| PDSCH/PDCCH subcarrier spacing |  | 1~2 | kHz | 120 |  | 120 |  |
| OCNG Patterns |  | 1~2 |  | OP.3 |  | OP.3 |  |
| Initial BWP Configuration |  | 1~2 |  | DLBWP.0.1ULBWP.0.1 |  | DLBWP.0.1ULBWP.0.1 |  |
| Dedicated BWP configuration |  | 1~2 |  | DLBWP.1.3ULBWP.1.3 |  | DLBWP.1.3ULBWP.1.3 |  |
| TRS Configuration |  | 1~2 |  | TRS.2.1 TDD |  | TRS.2.1 TDD |  |
| PDCCH/PDSCH TCI Configuration |  | 1~2 |  | TCI.State.2 |  | TCI.State.2 |  |
| SMTC configuration |  | 1~2 |  | SMTC.1 |  | SMTC.1 |  |
| Time offset between Cell 2 and Cell 1 |  | 1~2 | s | 3 |  | 3 |  |
| EPRE ratio of PSS to SSS |  | 1~2 | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |  |  |
| Propagation condition |  | 1~2 | - | AWGN | AWGN | AWGN | AWGN |
| Antenna configuration |  | 1~2 | - | 1x2 | 1x2 | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Void. |  |  |  |  |  |  |  |

Table A.17.7.1.2.2-2: SS-RSRP inter frequency OTA related test parameters

| Parameter | Config | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Angle of arrival configuration | 1~2 |  | Setup 4b according to clause A.3.15.4.2 |  | Setup 4b according to clause A.3.15.4.2 |  |
|  |  |  | AoA1  Spherical coverage | AoA2  Rx Beam Peak | AoA1  Spherical coverage | AoA2  Rx Beam Peak |
| Assumption for UE beamsNote 7 | 1~2 |  | Rough |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | 1 | dBm/15 kHzNote4 | -90.6 | -90.6 | (Table B.2.3-2 Rx Beam PeakNote 8 +1.97 dB) | (Table B.2.3-2 Rx Beam PeakNote 8 -3.03 dB) |
|  | 2 |  | -93.7 | -93.7 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | 1 | dBm/SCSNote4 | -81.6 | -81.6 | (Table B.2.3-2 Rx Beam PeakNote 8 +11.0 dB) | (Table B.2.3-2 Rx Beam PeakNote 8 +6.0 dB) |
|  | 2 |  | -81.7 | -81.7 | (Table B.2.3-2 Rx Beam PeakNote 8 +14.0 dB) | (Table B.2.3-2 Rx Beam PeakNote 8 +9.0 dB) |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | 1~2 | dB | 6.0 | 6.0 | 17.0 | -1.0 |
| SSB_RPNote2 | 1 | dBm/SCS | -75.6 | -75.6 | (Table B.2.3-2 Rx Beam PeakNote 8 +28.0 dB) | (Table B.2. 3-2 Rx Beam PeakNote 8 +5.0 dB) |
|  | 2 |  | -75.7 | -75.7 | (Table B.2.3-2 Rx Beam PeakNote 8 +31.0 dB) | (Table B.2. 3-2 Rx Beam PeakNote 8 +8.0 dB) |
| (SSB_RPCell 1 – SSB_RPCell 2) | 1~2 | dB | 0 |  | 23.00 |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot]BBNote6 | 1 | dB | 5.26 | 5.96 | 9.53 | -3.46 |
|  | 2 |  | 4. 61 | 5.91 |  |  |
| IoNote2 | 1 | dBm/95.04 MHz Note4 | -50.00 | -50.00 | (Table B.2.3-2 Rx Beam PeakNote 8 +52.68 dB) | (Table B.2.3-2 Rx Beam PeakNote 8 +33.13 dB) |
|  | 2 |  | -50.09 | -50.09 | (Table B.2.3-2 Rx Beam PeakNote 8 +55.69 dB) | (Table B.2.3-2 Rx Beam PeakNote 8 +36.14 dB) |
| (Iofreq 1 – Io freq 2) | 1~2 | dB | 0 |  | 19.55 |  |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: SSB_RP, Es/Iot, Io, (SSB_RPCell 2 – SSB_RPCell 1) and (Iofreq 2 – Io freq 1) levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: VoidNOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: VoidNOTE 6: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBP or ΔMBS from TS 38.101-2 [19] Table 6.2.1.3-4. NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 8: The value in table B.2.3-2 is the Minimum SSB_RP for SCSSSB = 120 kHz, selected according to the operating band of Cell 2 and UE power class, without ∆MBP,n adjustment. |  |  |  |  |  |  |

##### A.17.7.1.2.3 Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil the absolute requirements in clause 10.1A.5.1.1 and the relative requirements in clause 10.1.5A.1.2.

Test 1:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.17.7.1.2.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table A.17.7.1.2.3-2.

Test 2:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.17.7.1.2.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table A.17.7.1.2.3-2.

Table A.17.7.1.2.3-1: SS-RSRP absolute accuracy test requirement

|  | Test requirement Notes1,2,3,4 |
| --- | --- |
| Cell 1 | SSB_RP1 -δ +Gmin +X ≤ Reported RSRP(dBm) ≤ SSB_RP1 +δ +Gmax |
| Cell 2 | SSB_RP2 -δ +Gmin ≤ Reported RSRP(dBm) ≤ SSB_RP2 +δ +Gmax |
| NOTE 1: SSB_RPn is the equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone configured in the test for the cell n under considerationNOTE 2:  δ is the RSRP absolute accuracy requirement from Table 10.1.5.1.1-1, selected according to the Io used in the testNOTE 3:  Gmin and Gmax are the minimum and maximum UE gain values from Table B.2.1.5.1-1, selected according to the UE power class NOTE 4:  X is the Spherical coverage gain difference in dB, derived as (UE Refsens - UE Spherical coverage) from TS 38.101-2 [19] clauses 7.3.2 and 7.3.4, selected according to the UE power class and operating band. X is always a negative value. |  |

Table A.17.7.1.2.3-2: SS-RSRP relative accuracy test requirement

|  | Test requirement Notes1,2,3,4, 5, 6 |
| --- | --- |
| Cell 2 – Cell 1 | SSB_RP2 - SSB_RP1 -δ - D - Ginter ≤ Reported RSRP(dB) ≤ SSB_RP2 - SSB_RP1 +δ + Ginter –(X) |
| NOTE 1:  SSB_RPn is the equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone configured in the test for the cell n under considerationNOTE 2:  δ is the RSRP relative accuracy requirement from Table 10.1.5.1.2-1NOTE 3:  Void NOTE 4:  X is the Spherical coverage gain difference in dB, derived as (UE Refsens - UE Spherical coverage) from TS 38.101-2 [19] clauses 7.3.2 and 7.3.4, selected according to the UE power class and operating band. X is always a negative value.NOTE 5:  D = [5.5 dB]. D is the margin due to mis-alignment between fine beam and rough beam.NOTE 6:  Ginter = [3 dB]. Ginter is the margin due to different antenna gain caused by frequency separation. |  |

### A.17.7.2 SS-RSRQ

#### A.17.7.2.1 SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell

##### A.17.7.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1A.7.

##### A.17.7.2.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.7.2.1.2-1. . The absolute accuracy of SS-RSRQ intra-frequency measurement is test by using the parameters in table A.17.7.2.1.2-2 and table A.17.7.2.1.2-3. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.17.7.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.7.2.1.2-2: SS-RSRQ Intra frequency test parameters

| Parameter |  | Unit | Test 1 |  |  | Test 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 |  | Cell 2 | Cell 1 | Cell 2 |  |
| SSB ARFCN |  |  | Freq1 |  |  | Freq1 |  |  |
| Duplex mode |  |  | TDD |  |  | TDD |  |  |
| TDD configuration |  |  | TDDConf.3.1 |  |  | TDDConf.3.1 |  |  |
| BWchannel |  | MHz | 100: NPRB,c = 66 |  |  | 100: NPRB,c = 66 |  |  |
| Data PRBs allocated |  |  | 66 |  |  | 66 |  |  |
| BWP configuration | Initial DL BWP |  | DLBWP.0.1 |  |  |  |  |  |
|  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |  |  |
|  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |  |  |
|  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |  |  |
| TRS configuration |  |  | TRS.2.1 TDD |  |  | TRS.2.1 TDD |  |  |
| TCI state |  |  | TCI.State.0 |  |  | TCI.State.0 |  |  |
| PDSCH Reference measurement channel |  |  | SR.3.1 TDD |  |  | SR.3.1 TDD |  |  |
| RMSI CORESET Reference Channel |  |  | CR.3.1 TDD |  | - | CR.3.1 TDD |  |  |
| Control channel RMC |  |  | CCR.3.1 TDD |  | - | CCR.3.1 TDD | - |  |
| OCNG Patterns |  |  | OP.1 |  | OP.1 | OP.1 | OP.1 |  |
| SMTC configuration |  |  | SMTC.1 |  |  |  |  |  |
| SSB configuration |  |  | SSB.1 FR2 |  | SSB.1 FR2 | SSB.1 FR2 | SSB.1 FR2 |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 120 |  | 120 | 120 | 120 |  |
| SS-RSSI-Measurement |  |  | Not Applicable |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  | 0 | 0 | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |  |  |  |
| Propagation condition |  |  | AWGN |  |  | AWGN |  |  |
| Antenna configuration |  |  | 1x2 | 1x2 |  | 1x2 |  | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: VoidNOTE 3: VoidNOTE 4: VoidNOTE 5:  Void. |  |  |  |  |  |  |  |  |

Table A.17.7.2.1.2-3: SS-RSRQ Intra frequency OTA related test parameters

|  | Unit | Test 1 |  |  | Test 2 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 |  | Cell 1 |  | Cell 2 |  |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |  | Setup 1according to clause A.3.15.1 |  |  |  |
| Assumption for UE beamsNote 9 |  | Rough |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15 kHzNote4 | -95 |  |  |  | -95 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote3 | -86 |  |  |  | -86 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 3 |  |  |  | 3 |  |  |
| SSB_RPNote2 | dBm/SCS Note4 | -83 |  | -83 |  | -89 |  | -89 |
| SS-RSRQ Note2 | dB | -14.77 |  | -14.77 |  | -16.81 |  | -16.81 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] | dB | -1.76 |  | -1.76 |  | -4.76 |  | -4.76 |
| IoNote2 | dBm/95.04 MHz Note4 | -50 |  |  |  | -54 |  |  |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: SS-RSRQ, SSB_RP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: SS-RSRQ and SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 6: VoidNOTE 7: VoidNOTE 8: VoidNOTE 9: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |  |  |  |

##### A.17.7.2.1.3 Test Requirements

The SS-RSRQ absolute measurement accuracy in test 1 shall be within the range Nominal SS-RSRQ+2.5 dB to Nominal SS-RSRQ-2.5 dB and the SS-RSRQ measurement accuracy in test 2 shall be within the range Nominal RSRQ+3.5 dB to Nominal RSRQ-3.5 dB  according to the requirements in clause 10.1.8.1.1.Nominal RSRQ is the value shown in table A.17.7.2.1.2-3.

#### A.17.7.2.2 SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell for 2 Rx UE

##### A.17.7.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1A.9.1.1 and 10.1A.9.1.2 for inter-frequency measurement.

##### A.17.7.2.2.2 Test parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.17.7.2.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in tableA.17.7.2.2.2-2 and table A.17.7.2.2.2-3. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.17.7.2.2.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.7.2.2.2-2: SS-RSRQ Inter frequency test parameters

| Parameter |  | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| SSB ARFCN |  |  | Freq1 | freq2 | freq1 | Freq2 |
| SSB Configuration |  |  | SSB.1 FR2 | SSB.1 FR2 | SSB.1 FR2 | SSB.1 FR2 |
| Duplex mode |  |  | TDD |  | TDD |  |
| TDD configuration |  |  | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel |  | MHz | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| BWP configuration | Initial DL BWPDedicated DL BWP |  | DLBWP.0.1 |  |  |  |
|  |  |  | DLBWP.1.1 |  |  |  |
|  | Initial UL BWPDedicated UL BWP |  | ULBWP.0.1 |  |  |  |
|  |  |  | ULBWP.1.1 |  |  |  |
| TRS configuration |  |  | TRS.2.1 TDD | - | TRS.2.1 TDD | - |
| TCI state |  |  | TCI.State.0 | - | TCI.State.0 | - |
| Data PRBs allocated |  |  | 66 |  | 66 |  |
| PDSCH Reference measurement channel |  |  | SR.3.1 TDD | - | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  |  | CR.3.1 TDD | - | CR.3.1 TDD | - |
| OCNG Patterns |  |  | OP.1 | OP.1 | OP.1 | OP.1 |
| SMTC configuration |  |  | SMTC.1 | SMTC.1 | SMTC.1 | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 120 | 120 | 120 | 120 |
| EPRE ratio of PSS to SSS |  | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |  |
| Propagation conditions |  |  | AWGN | AWGN | AWGN | AWGN |
| Antenna configuration |  |  | 1x2 | 1x2 | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: VoidNOTE 3: VoidNOTE 4: Void |  |  |  |  |  |  |

Table A.17.7.2.2.2-3 SS-RSRQ Inter frequency OTA related test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| AoA setup |  | Setup 1 in clause A.3.15. |  | Setup 1 in clause A.3.15. |  |
| Assumption for UE beamsNote 8 |  | Rough |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15 kHzNote4 | -94.03 | -94.03 | -94.03 | -94.03 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote3 | -85.0 | -85.0 | -85.0 | -85.0 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | -1.75 |  | -1.75 |  |
| SSB_RPNote2 | dBm/SCS Note4 | -86.75 | -86.75 | -88 | -88 |
| SS-RSRQNote2 | dB | -14.75 | -14.75 | -15.56 | -15.56 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] | dB | -1.75 | -1.75 | -3 | -3 |
| IoNote2 | dBm/95.04 MHz Note4 | -53.8 | -53.8 | -54.25 | -54.25 |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: SS-RSRQ, SSB_RP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: SS-RSRQ and SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 4:  Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 6: VoidNOTE 7:  VoidNOTE 8: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |

##### A.17.7.2.2.3 Test Requirements

The SS-RSRQ absolute measurement accuracy in test 1 shall be within the range Nominal SS-RSRQ+2.5 dB to Nominal SS-RSRQ -2.5 dB and the SS-RSRQ measurement accuracy in test 2 shall be within the range Nominal SS-RSRQ +3.5 dB to Nominal SS-RSRQ -3.5 dB according to the requirements in clause 10.1A.10.1.1.

The SS-RSRQ relative measurement accuracy shall fulfil the requirements in clause 10.1A.10.1.2.

#### A.17.7.2.3 SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell

### A.17.7.3 L1-RSRP measurement for beam reporting

#### A.17.7.3.1 SSB based L1-RSRP measurement

##### A.17.7.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.5B.2 and clause [10.xx.xx.1] for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.7.7.4.1.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

##### A.17.7.3.1.2 Test parameters

Test parameters are the same as in clause A.7.7.4.1.2.

##### A.17.7.3.1.3 Test Requirements

After 320 ms from the beginning of the test, the L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 2 shall fulfil the requirements in clauses [10.xx.xx.1]. The following requirements are to be verified:

For Test 1:

Absolute accuracy of SSB0 and absolute accuracy of SSB1. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.17.7.3.1.3-1.

Relative accuracy of SSB0 compared with SSB1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table [10.xx.xx.1.2-1].

For Test 2:

Absolute accuracy of SSB0 and absolute accuracy of SSB1. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.17.7.3.1.3-1.

Relative accuracy of SSB0 compared with SSB1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table [10.xx.xx.1.2-1].

Table A.17.7.3.1.3-1: L1-RSRP absolute accuracy test requirement

|  | Test requirement Notes1,2,3 |
| --- | --- |
| SSB0 | SSB_RP0 -δ + Gmin ≤ Reported RSRP(dBm) ≤ SSB_RP0 +δ + Gmax |
| SSB1 | SSB_RP1 -δ + Gmin ≤ Reported RSRP(dBm) ≤ SSB_RP1 +δ + Gmax |
| NOTE 1:  SSB_RPn is the  equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone configured in the test for the SSB n under considerationNOTE 2:  δ is the RSRP absolute accuracy requirement from Table [10.xx.xx.1.1-1], selected according to the Io used in the testNOTE 3:  Gmin and Gmax are the minimum and maximum UE gain values from Table B.2.1.5.1-1, selected according to the UE power class |  |

#### A.17.7.3.2 CSI-RS based L1-RSRP measurement on resource set with repetition off

##### A.17.7.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.5.3 and clause [10.1.xx.2] for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.7.7.4.2.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

##### A.17.7.3.2.2 Test parameters

Test parameters are the same as in clause A.7.7.4.2.2.

##### A.17.7.3.2.3 Test Requirements

After 640 ms from the beginning of the test, the L1-RSRP measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirements in clause [10.1.xx.2]. The following requirements are to be verified:

For Test 1:

Absolute accuracy of CSI-RS0 and absolute accuracy of CSI-RS1. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.17.7.3.2.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table [10.1.xx.2.2-1].

For Test 2:

Absolute accuracy of CSI-RS0 and absolute accuracy of CSI-RS1. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.17.7.3.2.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table [10.1.xx.2.2-1].

Table A.17.7.3.2.3-1: L1-RSRP absolute accuracy test requirement

|  | Test requirement Notes1,2,3 |
| --- | --- |
| CSI-RS0 | CSI-RS _RP0 -δ + Gmin ≤ Reported RSRP(dBm) ≤CSI-RS _RP0 +δ + Gmax |
| CSI-RS1 | CSI-RS _RP1 -δ + Gmin ≤ Reported RSRP(dBm) ≤CSI-RS _RP1 +δ + Gmax |
| NOTE 1: CSI-RS_RPn is the  equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone configured in the test for the CSI-RS n under considerationNOTE 2: δ is the RSRP absolute accuracy requirement from Table [10.1.xx.2.1-1], selected according to the Io used in the testNOTE 3: Gmin and Gmax are the minimum and maximum UE gain values from Table B.2.1.5.1-1, selected according to the UE power class |  |

### A.17.7.4 SS-SINR

#### A.17.7.4 SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell for 2Rx UE

##### A.17.7.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1A.13.1.1.

##### A.17.7.4.1.2 Test parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A A.17.7.4.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is test by using the parameters in table A.17.7.4.1.2-2 and table Table A.17.7.4.1.2-3. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.17.7.4.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.7.4.1.2-2: SS-SINR Intra frequency test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| SSB ARFCN |  | Freq2 |  | Freq2 |  |
| Duplex mode |  | TDD |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel | MHz | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  | 66 |  | 66 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 |  |  |  |
| Downlink dedicated BWP configuration |  | DLBWP.1.1 |  |  |  |
| Uplink initial BWP configuration |  | ULBWP.0.1 |  |  |  |
| Uplink dedicated BWP configuration |  | ULBWP.1.1 |  |  |  |
| DRX cycle configuration | ms | Not applicable |  |  |  |
| TRS configuration |  | TRS.2.1 TDD |  |  |  |
| TCI state |  | TCI.State.0 |  |  |  |
| PDSCH Reference measurement channel |  | SR.3.1 TDD |  | SR.3.1 TDD |  |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - | CR.3.1 TDD |  |
| Dedicated RMSI CORESET Reference Channel |  | CCR.3.1 TDD | - | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.1 | OP.1 | OP.1 | OP.1 |
| SMTC configuration |  | SMTC.1 |  |  |  |
| SSB configuration |  | SSB.1 FR2 | SSB.1 FR2 | SSB.1 FR2 | SSB.1 FR2 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 | 120 | 120 |
| SS-RSSI-Measurement |  | Not Applicable |  |  |  |
| EPRE ratio of PSS to SSS | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Propagation conditions |  | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: VoidNOTE 3: VoidNOTE 4: Void |  |  |  |  |  |

Table A.17.7.4.1.2-3: SS-SINR Intra frequency OTA related test parameters

| Parameter | Unit | Test 1 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  | Setup 1 according to clause A.3.15.1 |  |
| Assumption for UE beamsNote 9 |  | Rough |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15 kHz Note4 | -105 |  | -105 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCS Note3 | -96 |  | -96 |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 4.54 |  | 2.66 |  |
| SSB_RPNote2 | dBm/SCS Note4 | -91.46 | -93.34 | -99 | -99 |
| SS-SINR Note2 | dB | 0 | -3.2 | -4.76 | -4.76 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 0 | -3.2 | -4.76 | -4.76 |
| IoNote2 | dBm/95.04 MHz  Note4 | -59.2 |  | -64 |  |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: SS-SINR, SSB_RP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: SS-SINR and SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 6: VoidNOTE 7: VoidNOTE 8: VoidNOTE 9: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |

##### A.17.7.4.1.3 Test Requirements

The SS-SINR absolute measurement accuracy in test 1 shall be within the range Nominal SS-SINR+3B to Nominal SS-SINR -3 dB and the SS-SINR measurement accuracy in test 2 shall be within the range Nominal SS-SINR +3.5 dB to Nominal SS-SINR -3.5 dB according to the requirements in clause 10.1A.10.13.1.

### A.17.7.5 RSTD measurements

#### A.17.7.5.1 RSTD measurement accuracy test case for RedCap UE without FH

##### A.17.7.5.1.1 Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC CONNECTED state meets the accuracy requirements specified in clause 10.1A.16.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.17.7.5.1.1-1.

Table A.17.7.5.1.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cells. Both cells are on the same NR RF channel in FR2. GP#24 is configured if UE supports GP#24, otherwise, GP#13 is configured for the test. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the RedCap UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 9.9A.2.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The accuracy test parameters and OTA related test parameters are as given in table A.17.7.5.1.1-2 and table A.17.7.5.1.1-3, respectively.

Table A.17.7.5.1.1-2: RSTD accuracy test parameters

| Parameter | Unit | Test 1 |  |
| --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 |
| PRS ARFCN |  | freq1 |  |
| Duplex mode |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  |
| BWchannel | MHz | 100: NRB,c = 66 |  |
| Measurement gap |  | GP#24 or GP#13 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - |
| Downlink dedicated BWP configuration |  | DLBWP.1.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - |
| Uplink dedicated BWP configuration |  | ULBWP.1.1 | - |
| DRX cycle configuration |  | Not applicable | - |
| TRS configuration |  | TRS.2.1 TDD | - |
| TCI state |  | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.1 | OP.1 |
| SSB configuration |  | SSB.3 FR2 | SSB.3 FR2 |
| SMTC configuration |  | SMTC.1 | SMTC.1 |
| PRS configuration |  | PRS.1.1 FR2 | PRS.1.1 FR2 |
| PRS Resource slot offset | slot | 0 | 4 |
| Expected RSTD | s | N/A | 3 |
| Expected RSTD uncertainty | s | N/A | 5 |
| Time offset with Cell 1 | s | - | 3 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| EPRE ratio of PRS to SSS | dB | 0 | 0 |
| Propagation conditions |  | AWGN | AWGN |
| Antenna configuration |  | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the slots with transmitted PRS. |  |  |  |

Table A.17.7.5.1.1-3: RSTD accuracy OTA related test parameters

| Parameter | Unit | Test 1 |  |
| --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |
| Assumption for UE beamsNote 5 |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote3 | -89 |  |
| PRS | dB | -5.7 | -11.9 |
| PRPNote2 | dBm/SCS | -94.7 | -100.9 |
| PRS | dB | -6 | -13 |
| IoNote2 | dBm/95.04 MHz Note3 | -58.76 | -58.76 |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: PRP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. The Io is calculated based only on the symbols in which PRS is transmitted.NOTE 3: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 4: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 5: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation. |  |  |  |

##### A.17.7.5.1.2 Test Requirements

The RSTD measurement accuracy shall fulfil the absolute requirement in clause 10.1A.16.2.

A.17.7.5.2 RSTD measurement accuracy test case for RedCap UE with FH in RRC_CONNECTED state

A.17.7.5.2.1 Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the accuracy requirements specified in clause10.1A.16.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.17.7.5.2.1-1. The test parameters are as given in table A.17.7.5.2.1-2, table A.17.7.5.2.1-3, and table A.17.7.5.2.1-4.

Table A.17.7.5.2.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1:   This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2. GP#24 is configured if UE supports GP#24, otherwise, GP#13 is configured for the test. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the UE before the start of the test.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation as specified in TS 37.355 [34], clause 6.5.12. The frequency hopping configurations are specified in clause A.3.31.

Table A.17.7.5.2.1-2: RSTD accuracy test parameters

| Parameter | Unit | Cell 1 | Cell 2 |
| --- | --- | --- | --- |
|  |  |  |  |
| PRS ARFCN |  | freq1 |  |
| Duplex mode |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  |
| BWchannel | MHz | 400: NRB,c = 264 |  |
| Measurement gap |  | GP#24 or GP#13 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - |
| Downlink dedicated BWP configuration |  | DLBWP.1.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - |
| Uplink dedicated BWP configuration |  | ULBWP.1.1 | - |
| DRX cycle configuration |  | Not applicable | - |
| TRS configuration |  | TRS.2.1 TDD | - |
| TCI state |  | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.1 | OP.1 |
| SSB configuration |  | SSB.3 FR2 | SSB.3 FR2 |
| SMTC configuration |  | SMTC.1 | SMTC.1 |
| PRS configuration |  | PRS.1.6 FR2 | PRS.1.6 FR2 |
| PRS Resource slot offset | slot | 0 | 4 |
| Expected RSTD | s | N/A | 3 |
| Expected RSTD uncertainty | s | N/A | 5 |
| Time offset with Cell 1 | s | - | 3 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| EPRE ratio of PRS to SSS | dB | 0 | 0 |
| Propagation conditions |  | AWGN | AWGN |
| Antenna configuration |  | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated, and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the slots with transmitted PRS. |  |  |  |

Table A.17.7.5.2.1-3: RSTD accuracy OTA related test parameters

| Parameter | Unit | Cell 1 | Cell 2 |
| --- | --- | --- | --- |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |
| Assumption for UE beamsNote 5 |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote3 | -89 |  |
| PRS | dB | -5.7 | -11.9 |
| PRPNote2 | dBm/SCS | -94.7 | -100.9 |
| PRS | dB | -6 | -13 |
| IoNote2 | dBm/380.16MHz Note3 | -52.74 | -52.74 |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: PRP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. The Io is calculated based only on the symbols in which PRS is transmitted.NOTE 3: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 4: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 5: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation. |  |  |  |

A.17.7.5.2.2 Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1A.16.2.

### A.17.7.6 UE Rx-Tx Measurements

#### A.17.7.6.1 UE Rx-Tx measurement accuracy for single positioning frequency layer in FR2 SA without RX FH in RRC_CONNECTED mode

##### A.17.7.6.1.1 Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy without RX FH in RRC_CONNECTED state is within the specified limits. This test will verify the requirements in clause 10.1A.18.2. The test is conducted in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configuration is listed in table A.17.7.6.1.1-1.

Table A.17.7.6.1.1-1: Supported test configurations.

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB and PRS SCS, 100 MHz bandwidth, TDD duplex mode |

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test. In nr-Multi-RTT-RequestLocationInformation, nr-DL-PRS-RxHoppingRequest is not present.

The UE is configured with measurement gap pattern ID #13 or ID #24 before the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

##### A.17.7.6.1.2 Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.17.7.6.1.2-1.

Table A.17.7.6.1.2-1: UE Rx-Tx time difference measurement accuracy test parameters

| Parameter | Unit | Test configuration | Cell 1 | Cell 2 |
| --- | --- | --- | --- | --- |
| AoA setup |  | 1 | Setup 1 as specified in clause A.3.15 |  |
| BWchannel | MHz | 1 | 100: NRB,c = 66 |  |
| Beam AssumptionNote 6 |  | 1 | Rough | Rough |
| Measurement gap |  | 1 | GP#24 or GP#13 Note 7 |  |
| DRX |  | 1 | OFF |  |
| Time offset with Cell 1 | s | 1 | N/A | 3 |
| TDD configuration |  | 1 | TDDConf.3.1 | TDDConf.3.1 |
| PDSCH RMC configuration |  | 1 | SR.3.1 TDD | N/A |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD | N/A |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 TDD | N/A |
| OCNG Patterns |  | 1 | OP.1 | OP.1 |
| EPRE ratio of PSS to SSS | dB | 1 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  |  |  |
| EPRE ratio of PRS to SSS |  |  |  |  |
| TRS Configuration |  | 1 | TRS.2.1 TDD | N/A |
| Initial BWP configuration |  | 1 | DLBWP.0.1 ULBWP.0.1 | N/A |
| Active DL BWP configuration |  | 1 | DLBWP.1.1 RedCap | N/A |
| Active UL BWP configuration |  | 1 | ULBWP.1.1 RedCap | N/A |
| PRS configuration |  | 1 | PRS.1.5 FR2 | PRS.1.5 FR2 |
| PRS Resource slot offset | slot | 1 | 0 | 4 |
| SRS configuration |  | 1 | POS-SRS.3 | N/A |
| Note 1 | dBm/SCS | 1 | -89 |  |
| Note 1 | dBm/15 kHz | 1 | -98 |  |
| PRS | dB | 1 | -2.41 | -12.12 |
| PRS | dB | 1 | -2 | -10 |
| PRP Note 2 | dBm/SCS kHz | 1 | -91 | -99 |
| Io | dBm/92.16 MHz | 1 | -57.6 | -57.6 |
| Propagation Condition |  | 1 | AWGN |  |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over sub-carriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 2: PRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 5: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 6: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 7: GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured.NOTE 8: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |

##### A.17.7.6.1.3 Test requirements

The UE Rx-Tx time difference measurement fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1A.18.3 for both Cell 1 and Cell 2.

#### A.17.7.6.2 SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC_CONNECTED state in FR2

##### A.17.7.6.2.1 Test purpose and Environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy with FH by a RedCap UE in RRC_CONNECTED is within the specified limits. This test will verify the requirements in clause 10.1A.18.2.3. The test is conducted in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configuration is listed in table A.17.7.6.2.1-1.

Table A.17.7.6.2.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1:   This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test. The test requirements apply when frequencyHopping is configured to UE.

The UE is configured with measurement gap pattern ID #13 or ID #24 before the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

##### A.17.7.6.2.2 Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.17.7.6.2.2-1.

Table A.17.7.6.2.2-1: UE Rx-Tx time difference measurement accuracy test parameters

| Parameter | Unit | Test configuration | Test 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 |
| AoA setup |  | 1 | Setup 1 as specified in clause A.3.15 |  |
| BWchannel | MHz | 1 | 400: NRB,c = 264 |  |
| Beam AssumptionNote 7 |  | 1 | Rough | Rough |
| Measurement gap |  | 1 | GP#24 or GP#13 Note 8 |  |
| DRX |  | 1 | OFF |  |
| Time offset with Cell 1 | s | 1 | N/A | 3 |
| TDD configuration |  | 1 | TDDConf.3.1 | TDDConf.3.1 |
| PDSCH RMC configuration |  | 1 | SR.3.1 TDD | N/A |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD | N/A |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 TDD | N/A |
| OCNG Patterns |  | 1 | OP.1 | OP.1 |
| EPRE ratio of PSS to SSS | dB | 1 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |
| EPRE ratio of PRS to SSS |  |  |  |  |
| TRS Configuration |  | 1 | TRS.2.1 TDD | N/A |
| Initial BWP configuration |  | 1 | DLBWP.0.1 ULBWP.0.1 | N/A |
| Active DL BWP configuration |  | 1 | DLBWP.1.1 | N/A |
| Active UL BWP configuration |  | 1 | ULBWP.1.1 | N/A |
| PRS configuration |  | 1 | PRS.1.6 FR2 | PRS.1.6 FR2 |
| PRS Resource slot offset | slot | 1 | 0 | 4 |
| SRS configuration |  | 1 | POS-SRS.3 | N/A |
| Note 2 | dBm/SCS | 1 | -89 |  |
| Note 2 | dBm/15 kHz | 1 | -98 |  |
| PRS | dB | 1 | -2.41 | -12.12 |
| PRS | dB | 1 | -2 | -10 |
| PRP Note 3 | dBm/SCS | 1 | -91 | -99 |
| Io | dBm/380.16MHz | 1 | -51.61 | -51.61 |
| Propagation Condition |  | 1 | AWGN |  |
| NOTE 1: OCNG shall be used such that active cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the subframes with transmitted PRS.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: PRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 8: GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured.NOTE 9: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |

##### A.17.7.6.2.3 Test requirements

The UE Rx-Tx time difference measurement fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1A.18.2.3 for both Cell 1 and Cell 2.

### A.17.7.7 PRS-RSRP Measurements

#### A.17.7.7.1 PRS-RSRP measurement accuracy without FH in RRC_CONNECTED state in FR2

##### A.17.7.7.1.1 Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRP measurement without FH by a RedCap UE is within the specified limits. This test will verify the requirements in clauses10.1A.17.2.1 and 10.1A.17.2.2.

##### A.17.7.7.1.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.7.7.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in table A.17.7.7.1.2-2 and A.17.7.7.1.2-3. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.17.7.7.1.2-1: PRS-RSRP supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.7.7.1.2-2: PRS-RSRP general test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Cell ID |  | 489 | 0 | 489 | 0 |
| SSB ARFCN |  | freq1 |  | freq1 |  |
| Duplex mode |  | TDD |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel | MHz | 100: NRB,c = 66 |  | 100: NRB,c = 66 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - | DLBWP.0.1 | - |
| Downlink dedicated BWP configuration |  | DLBWP.1.1 | - | DLBWP.1.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - | ULBWP.0.1 | - |
| Uplink dedicated BWP configuration |  | ULBWP.1.1 | - | ULBWP.1.1 | - |
| DRX cycle configuration |  | Not applicable | - | Not applicable | - |
| Measurement gap |  | GP#13 or GP#24 Note2 |  |  |  |
| TRS configuration |  | TRS.2.1 TDD | - | TRS.2.1 TDD | - |
| TCI state |  | TCI.State.0 | - | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3.1 TDD | - | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.1 | OP.1 | OP.1 | OP.1 |
| SSB configuration |  | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 |
| SMTC configuration |  | SMTC.1 | SMTC.1 | SMTC.1 | SMTC.1 |
| Time offset with Cell 1 | s | - | 3 | - | 3 |
| Expected RSTD | s | 3 |  |  |  |
| Expected RSTD uncertainty | s | 5 |  |  |  |
| PRS configuration |  | PRS.1.3 FR2 | PRS.1.3 FR2 | PRS.1.5 FR2 | PRS.1.5 FR2 |
| PRS Resource slot offset | slot | 0 | 4 | 0 | 4 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| EPRE ratio of PRS to SSS | dB | 0 | 0 | 0 | 0 |
| Propagation conditions |  | AWGN | AWGN | AWGN | AWGN |
| Antenna configuration |  | 1x2 | 1x2 | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that active cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the subframes with transmitted PRS.NOTE 2: GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured. |  |  |  |  |  |

Table A.17.7.7.1.2-3: PRS-RSRP OTA related test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |  |  |
| Assumption for UE beamsNote 5 |  | Rough |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15kHzNote 3 | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote 3 | -89 |  | -89 |  |
| PRS | dB | -2 | -10 | -2 | 10 |
| PRPNote 2 | dBm/SCS | -91 | -99 | -91 | -99 |
| PRS | dB | -2.41 | -12.12 | -2.41 | -12.12 |
| IoNote 2 | dBm/95.04 MHz Note 3 | -57.63 |  | -57.63 |  |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: PRP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 4: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 5: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation. |  |  |  |  |  |

##### A.17.7.7.1.3 Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1 if the reported PRS-RSRP is in the range shown in table A.17.7.7.1.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2.

Table A.17.7.7.1.3-1: PRS-RSRP absolute accuracy test requirement

|  | Test requirement Notes1,2,3 |
| --- | --- |
| Cell 1 | PRS_RP1 -δ +Gmin ≤ Reported RSRP(dBm) ≤ PRS_RP1 +δ +Gmax |
| Cell 2 | PRS_RP2 -δ +Gmin ≤ Reported RSRP(dBm) ≤ PRS_RP2 +δ +Gmax |
| NOTE 1:  PRS_RPn is the equivalent power received by an antenna with 0dBi gain at the centre of the quiet zone configured in the test for the cell n under consideration.NOTE 2:  δ is the RSRP absolute accuracy requirement from table 10.1.24.2.1-2, selected according to the Io used in the test.NOTE 3:  Gmin and Gmax are the minimum and maximum UE gain values from table B.2.1.6.1-1, selected according to the UE power class. |  |

#### A.17.7.7.2 PRS-RSRP measurement accuracy with FH in RRC_CONNECTED state in FR2

##### A.17.7.7.2.1 Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRP measurement with FH by a RedCap UE is within the specified limits. This test will verify the requirements in clauses 10.1A.17.2.1 and 10.1A.17.2.2.

##### A.17.7.7.2.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.7.7.2.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in table A.17.7.7.2.2-2 and A.17.7.7.2.2-3. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1. PRS RX hopping is present in NR-DL-AoD-RequestLocationInformation.

Table A.17.7.7.2.2-1: PRS-RSRP supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1:   This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

Table A.17.7.7.2.2-2: PRS-RSRP general test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Cell ID |  | 489 | 0 | 489 | 0 |
| SSB ARFCN |  | freq1 |  | freq1 |  |
| Duplex mode |  | TDD |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel | MHz | 400: NRB,c = 264 |  | 400: NRB,c = 264 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - | DLBWP.0.1 | - |
| Downlink dedicated BWP configuration |  | DLBWP.1.1 | - | DLBWP.1.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - | ULBWP.0.1 | - |
| Uplink dedicated BWP configuration |  | ULBWP.1.1 | - | ULBWP.1.1 | - |
| DRX cycle configuration |  | Not applicable | - | Not applicable | - |
| Measurement gap |  | GP#13 or GP#24 Note2 |  |  |  |
| TRS configuration |  | TRS.2.1 TDD | - | TRS.2.1 TDD | - |
| TCI state |  | TCI.State.0 | - | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3.1 TDD | - | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.1 | OP.1 | OP.1 | OP.1 |
| SSB configuration |  | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 |
| SMTC configuration |  | SMTC.1 | SMTC.1 | SMTC.1 | SMTC.1 |
| Time offset with Cell 1 | s | - | 3 | - | 3 |
| Expected RSTD | s | 3 |  |  |  |
| Expected RSTD uncertainty | s | 5 |  |  |  |
| PRS configuration |  | PRS.1.6 FR2 | PRS.1.6 FR2 | PRS.1.6 FR2 | PRS.1.6 FR2 |
| PRS Resource slot offset | Slot | 0 | 4 | 0 | 4 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| EPRE ratio of PRS to SSS | dB | 0 | 0 | 0 | 0 |
| Propagation conditions |  | AWGN | AWGN | AWGN | AWGN |
| Antenna configuration |  | 1x2 | 1x2 | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that active cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the subframes with transmitted PRS.NOTE 2: GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured. |  |  |  |  |  |

Table A.17.7.7.2.2-3: PRS-RSRP OTA related test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |  |  |
| Assumption for UE beamsNote 5 |  | Rough |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15kHzNote 3 | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote 3 | -89 |  | -89 |  |
| PRS | dB | -2 | -10 | -2 | 10 |
| PRPNote 2 | dBm/SCS | -91 | -99 | -91 | -99 |
| PRS | dB | -2.41 | -12.12 | -2.41 | -12.12 |
| IoNote 2 | dBm/380.16MHz Note 3 | -51.61 |  | -51.61 |  |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: PRP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 4: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 5: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation. |  |  |  |  |  |

##### A.17.7.7.2.3 Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1 if the reported PRS-RSRP is in the range shown in table A.17.7.7.2.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2.

Table A.17.7.7.2.3-1: PRS-RSRP absolute accuracy test requirement

|  | Test requirement Notes1,2,3 |
| --- | --- |
| Cell 1 | PRS_RP1 -δ +Gmin ≤ Reported RSRP(dBm) ≤ PRS_RP1 +δ +Gmax |
| Cell 2 | PRS_RP2 -δ +Gmin ≤ Reported RSRP(dBm) ≤ PRS_RP2 +δ +Gmax |
| NOTE 1:  PRS_RPn is the equivalent power received by an antenna with 0dBi gain at the centre of the quiet zone configured in the test for the cell n under consideration.NOTE 2:  δ is the RSRP absolute accuracy requirement from table 10.1.24.2.1-2, selected according to the Io used in the test.NOTE 3:  Gmin and Gmax are the minimum and maximum UE gain values from table B.2.1.6.1-1, selected according to the UE power class. |  |

### A.17.7.8 PRS-RSRPP Measurements

#### A.17.7.8.1 PRS-RSRPP measurement accuracy without FH in RRC_CONNECTED state in FR2

##### A.17.7.8.1.1 Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRPP measurement without FH by a RedCap UE in RRC_CONNECTED is within the specified limits. This test will verify the requirements in clauses10.1A.19.2.

##### A.17.7.8.1.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.7.8.1.2-1. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.17.7.8.1.2-1: PRS-RSRPP supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100MHz bandwidth, TDD duplex mode |

Table A.17.7.8.1.2-2: PRS-RSRPP general test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Cell ID |  | 489 | 0 | 489 | 0 |
| SSB ARFCN |  | freq1 |  | freq1 |  |
| Duplex mode |  | TDD |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel | MHz | 100: NRB,c = 66 |  | 100: NRB,c = 66 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - | DLBWP.0.1 | - |
| Downlink dedicated BWP configuration |  | DLBWP.1.1 | - | DLBWP.1.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - | ULBWP.0.1 | - |
| Uplink dedicated BWP configuration |  | ULBWP.1.1 | - | ULBWP.1.1 | - |
| DRX cycle configuration |  | Not applicable | - | Not applicable | - |
| Measurement gap |  | GP#13 or GP#24 Note2 |  |  |  |
| TRS configuration |  | TRS.2.1 TDD | - | TRS.2.1 TDD | - |
| TCI state |  | TCI.State.0 | - | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3.1 TDD | - | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.3 | OP.3 | OP.3 | OP.3 |
| SSB configuration |  | SSB.1 RedCap FR2 | SSB.1 RedCap FR2 | SSB.1 RedCap FR2 | SSB.1 RedCap FR2 |
| SMTC configuration |  | SMTC.1 | SMTC.1 | SMTC.1 | SMTC.1 |
| Time offset with Cell 1 | s | - | 3 | - | 3 |
| PRS configuration |  | PRS.1.5 FR2 | PRS.1.5 FR2 | PRS.1.5 FR2 | PRS.1.5 FR2 |
| PRS Resource slot offset | slot | 0 | 4 | 0 | 4 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Propagation conditions |  | Two-tap channel defined in 38.101-4 annex B.2.4, a = 1, $\tau  _{d}=0.45 $ µs and $ f_{D}=5 $ Hz |  |  |  |
| Antenna configuration |  | 1x2 | 1x2 | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured. |  |  |  |  |  |

Table A.17.7.8.1.2-3: PRS-RSRPP OTA related test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |  |  |
| Assumption for UE beamsNote 5 |  | Rough |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15kHzNote3 | -98 |  | Same as Test 1 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote3 | -89 |  | Same as Test 1 |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | -2 | -10 | -2 | -10 |
| Es | dBm/SCSNote3 | - | - | - | - |
| PRS_RPNote2 | dBm/SCS | -91 | -99 | -91 | -99 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot]BB Note4 | dB | -2.41 | -12.12 | -2.41 | -12.12 |
| IoNote2 | dBm/190.08 MHzNote3 | -54.62 |  | -54.62 |  |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: PRS_RP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 4: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 36.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 5: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation. |  |  |  |  |  |

##### A.17.7.8.1.3 Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.19.2 if the reported PRS-RSRPP is in the range shown in table A.17.7.8.1.3-1.

Table A.17.7.8.1.3-1: PRS-RSRPP absolute accuracy test requirement

|  | Test requirement Notes1,2,3 |
| --- | --- |
| Cell 1 | PRS_RP1 -δ +Gmin ≤ Reported RSRP(dBm) ≤ PRS_RP1 +δ +Gmax |
| Cell 2 | PRS_RP2 -δ +Gmin ≤ Reported RSRP(dBm) ≤ PRS_RP2 +δ +Gmax |
| NOTE 1:  PRS_RPn is the equivalent power received by an antenna with 0dBi gain at the centre of the quiet zone configured in the test for the cell n under consideration.NOTE 2:  δ is the RSRP absolute accuracy requirement from table 10.1.24.2.1-2, selected according to the Io used in the test.NOTE 3:  Gmin and Gmax are the minimum and maximum UE gain values from table B.2.1.6.1-1, selected according to the UE power class. |  |

#### A.17.7.8.2 SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_CONNECTED state in FR2

##### A.17.7.8.2.1 Test purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRPP measurement with FH by a RedCap UE in RRC_CONNECTED is within the specified limits. This test will verify the requirements in clauses10.1A.19.2.

##### A.17.7.8.2.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.7.8.2.2-1. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.17.7.8.2.2-1: PRS-RSRPP supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1:   This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

Table A.17.7.8.2.2-2: PRS-RSRPP general test parameters

| Parameter | Unit | Cell 1 | Cell 2 |
| --- | --- | --- | --- |
| Cell ID |  | 489 | 0 |
| SSB ARFCN |  | freq1 |  |
| Duplex mode |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  |
| BWchannel | MHz | 400: NRB,c = 264 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - |
| Downlink dedicated BWP configuration |  | DLBWP.1.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - |
| Uplink dedicated BWP configuration |  | ULBWP.1.1 | - |
| DRX cycle configuration |  | Not applicable | - |
| Measurement gap |  | GP#13 or GP#24 Note2 |  |
| TRS configuration |  | TRS.2.1 TDD | - |
| TCI state |  | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.3 | OP.3 |
| SSB configuration |  | SSB.1 RedCap FR2 | SSB.1 RedCap FR2 |
| SMTC configuration |  | SMTC.1 | SMTC.1 |
| Time offset with Cell 1 | s | - | 3 |
| PRS configuration |  | PRS.1.6 FR2 | PRS.1.6 FR2 |
| PRS Resource slot offset | slot | 0 | 4 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation conditions |  | Two-tap channel defined in 38.101-4 annex B.2.4, a = 1, $\tau  _{d}=0.45 $ µs and $ f_{D}=5 $ Hz |  |
| Antenna configuration |  | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured. |  |  |  |

Table A.17.7.8.2.2-3: PRS-RSRPP OTA related test parameters

| Parameter | Unit | Cell 1 | Cell 2 |  |
| --- | --- | --- | --- | --- |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |  |
| Assumption for UE beamsNote 5 |  | Rough |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note 1 | dBm/15kHzNote 3 | -98 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note 1 | dBm/SCSNote 3 | -89 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | -2 |  | -10 |
| PRS_RPNote 2 | dBm/SCS | -91 |  | -99 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot]BB Note 4 | dB | -2.41 |  | -12.12 |
| IoNote2 | dBm/380.16MHzNote3 | -51.61 |  |  |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: PRS_RP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 4: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 36.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 5: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation. |  |  |  |  |

##### A.17.7.8.2.3 Test requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.38.2 if the reported PRS-RSRPP is in the range shown in table A.17.7.8.2.3-1.

Table A.17.7.8.2.3-1: PRS-RSRPP absolute accuracy test requirement

|  | Test requirement Notes1,2,3 |
| --- | --- |
| Cell 1 | PRS_RP1 -δ +Gmin ≤ Reported RSRP(dBm) ≤ PRS_RP1 +δ +Gmax |
| Cell 2 | PRS_RP2 -δ +Gmin ≤ Reported RSRP(dBm) ≤ PRS_RP2 +δ +Gmax |
| NOTE 1:  PRS_RPn is the equivalent power received by an antenna with 0dBi gain at the centre of the quiet zone configured in the test for the cell n under consideration.NOTE 2:  δ is the RSRP absolute accuracy requirement from table 10.1.24.2.1-2, selected according to the Io used in the test.NOTE 3:  Gmin and Gmax are the minimum and maximum UE gain values from table B.2.1.6.1-1, selected according to the UE power class. |  |

## A.17.8 Measurement Procedure for RedCap in RRC_INACTIVE

### A.17.8.1 RSTD Measurements

#### A.17.8.1.1 NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA in RRC_INACTIVE state

##### A.17.8.1.1.1 Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC INACTIVE state meets the requirements specified in clause 5.6A.4.5 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.17.8.1.1.1-1.

Table A.17.8.1.1.1-1: Supported test configurations for NR RSTD

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layers.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell3. During T2 UE shall be in RRC_INACTIVE state and all cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the RedCap UE during T1. The measurement reporting delay test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The last TTI containing the two messages shall be provided to the RedCap UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s).

The UE is configured with DRX cycle of 0.64 s.

The general test parameters are listed in table A.17.8.1.1.1-2, and cell specific test parameters are listed in table A.17.8.1.1.1-3 and table A.17.8.1.1.1-4.

Table A.17.8.1.1.1-2: General test parameters for RSTD measurement reporting delay

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Reference cell |  |  | Cell 1 | Reference cell is the cell in the DL-TDOA assistance data with respect to which the RSTD measurement is defined, as specified in TS 38.215 [4] and TS 37.355 [34]. The reference cell is the PCell in this test case. |
| Neighbor cells |  |  | Cell 2 and Cell 3 | Cell 2 and Cell 3 appear at the first and second places in the neighbour cell list in the DL-TDOA assistance data. |
| BWchannel |  | MHz | 100: NRB,c = 66 |  |
| SSB configuration | Config 1 |  | SSB.2 FR2 |  |
| SMTC configuration | Config 1 |  | SMTC.1 |  |
| PDSCH RMC configuration | Config 1 |  | SR.1.1 FDD |  |
| RMSI CORESET RMC configuration | Config 1 |  | CR.3.1 TDD | As specified in clause A.3.1.2.1 |
| Dedicated CORESET RMC configuration | Config 1 |  | CR.1.1 FDD |  |
| PRS Configuration | Config 1 |  | PRS.1.5 FR2 | As specified in clause A.3. 31 |
| Physical cell ID PCI |  |  | (PCI of Cell 1 – PCI of Cell 2)mod6=0and(PCI of Cell 1 – PCI of Cell 3)mod6=0 | The cell PCIs are selected such that the relative shifts of PRS patterns among cells are as given by the test parameters |
| CP length |  |  | Normal |  |
| DRX |  | s | 0.64 |  |
| Radio frame receive time offset between the cells at the UE antenna connector |  | s | Cell 2 to Cell 1: 0Cell 3 to Cell 1: 3 | PRS are transmitted from synchronous cells |
| Expected RSTD |  | s | Cell 2: 3 Cell 3: 3Other neighbour cells: randomly between -3 and 3 | The expected RSTD is what is expected at the receiver. The corresponding parameter in the DL-TDOA assistance data specified in TS 37.355 [34] is the expectedRSTD indicator |
| Expected RSTD uncertainty for all neighbour cells |  | s | 5 | The corresponding parameter in the DL-TDOA assistance data specified in TS 37.355 [34] is the expectedRSTD-Uncertainty index |
| Number of cells provided in DL-TDOA assistance data |  |  | 3 | Including the reference cell |
| PRS muting info |  |  | Cell 1: ‘10’Cell 2: ‘01’Cell 3: ‘10’ | Correponds to prs-MutingInfo defined in TS 37.355 [34] |
| PRS resource RE offset |  |  | Cell 1: 0Cell 2: 0Cell 3: 1 | Cell 1 and Cell 3 are configured with different resource offsets |
| T1 |  | s | 3 | The length of the time interval from the beginning of each test |
| T2 |  | s | 1.28 | The length of the time interval that follows immediately after time interval T1 |
| AoA setup |  |  | Setup 1 | As defined in clause A.3.15.1 |
| Beam assumption |  |  | Rough | Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |

Table A.17.8.1.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

| Parameter |  | Unit | Cell 1 | Cell 2 | Cell 3 |
| --- | --- | --- | --- | --- | --- |
| NR RF Channel Number |  |  | 1 | 1 | 1 |
| Positiong frequency layer |  |  | 1 | 1 | 1 |
| Correlation Matrix and Antenna Configuration |  |  | 1x2 Low | 1x2 Low | 1x2 Low |
| OCNG patterns defined in A.3.2.1 |  |  | OP.5 FDD | N/A | N/A |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note 3 | Config 1 | dBm/SCS | -89 |  |  |
| PRS ![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] |  | dB | -Infinity | -Infinity | -Infinity |
| Io Note 4 | Config 1 | dBm/95.04MHz | -57 | -57 | -57 |
| SSB RP Note4 | Config 1 | dBm/SCS | -89 | -Infinity | -Infinity |
| ![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] |  | dB | 0 | -Infinity | -Infinity |
| Propagation Condition |  |  | AWGN |  |  |
| NOTE 1:  OCNG shall be used such that active cell (Cell 1) is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The resources for uplink transmission are assigned after the end of time period T2 to UEs that do not support SDT for measurement reporting.NOTE 3:  Interference from other cells and noise sources not specified in the test are assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 4: SSB RP and Io levels have been derived from other parameters and are given for information purpose. These are not settable test parameters. |  |  |  |  |  |

Table A.17.8.1.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

| Parameter |  | Unit | Cell 1 | Cell 2 | Cell 3 |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T2 | T2 | T2 |
| RF Channel Number |  |  | 1 | 1 | 1 |
| Positiong frequency layer |  |  | 1 | 1 | 1 |
| Correlation Matrix and Antenna Configuration |  |  | 1x2 Low | 1x2 Low | 1x2 Low |
| OCNG patterns defined in A.3.2.1 |  |  | OP.1 | OP.1 | OP.1 |
| PRACH configuration |  |  | FR2 PRACH configuration 1 | FR2 PRACH configuration 1 | FR2 PRACH configuration 1 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note 3 | Config 1 | dBm/SCS | -89 | -89 | -89 |
| PRS ![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] | Config 1 | dB | -5.44 | -11.67 | -11.67 |
| Io | Config 1 | dBm/95.04MHz | -58.49 | -58.49 | -58.49 |
| PRS ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | -6 | -13 | -13 |
| Propagation Condition |  |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that active cells (all, except Cell 3 in T2) are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the slots with transmitted PRS.NOTE 2: The resources for uplink transmission are assigned after the end of time period T2 to UEs that do not support SDT for measurement reporting.NOTE 3: Interference from other cells and noise sources not specified in the test are assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled. |  |  |  |  |  |

##### A.17.8.1.1.2 Test Requirements

The RSTD measurement time without FH for RedCap fulfils the requirements specified in clause 5.6A.4.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 5.6A.4.5 starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD_1970049.

#### A.17.8.1.2 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state

##### A.17.8.1.2.1 Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 5.6A.4.6 in FR2 in standalone scenario when PRS frequency hopping is configured.

The supported test configurations are specified in table A.17.8.1.2.1-1.

Table A.17.8.1.2.1-1: Supported test configurations for NR RSTD

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1:   This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layers.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell3. During T2 UE shall be in RRC_INACTIVE state and all cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The test requirements apply when frequencyHopping is configured to UE.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s).

The UE is configured with DRX cycle of 0.64 s.

The general test parameters are listed in table A.17.8.1.2.1-2, and cell specific test parameters are listed in table A.17.8.1.2.1-3 and table A.17.8.1.2.1-4.

Table A.17.8.1.2.1-2: General test parameters for RSTD measurement reporting delay

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Reference cell |  |  | Cell 1 | Reference cell is the cell in the DL-TDOA assistance data with respect to which the RSTD measurement is defined, as specified in TS 38.215 [4] and TS 37.355 [34]. The reference cell is the PCell in this test case. |
| Neighbor cells |  |  | Cell 2 and Cell 3 | Cell 2 and Cell 3 appear at the first and second places in the neighbour cell list in the DL-TDOA assistance data. |
| BWchannel |  | MHz | 400: NRB,c = 264 |  |
| SSB configuration | Config 1 |  | SSB.1 RedCap FR2 |  |
| SMTC configuration | Config 1 |  | SMTC.1 RedCap |  |
| PDSCH RMC configuration | Config 1 |  | SR.3.2 TDD |  |
| RMSI CORESET RMC configuration | Config 1 |  | CR.3.1 TDD |  |
| Dedicated CORESET RMC configuration | Config 1 |  | CCR.3.1 TDD |  |
| PRS Configuration | Config 1 |  | PRS.1.6 FR2 | PRS configured with frequency hopping as specified in clause A.3.31 |
| Physical cell ID PCI |  |  | (PCI of Cell 1 – PCI of Cell 2)mod6=0and(PCI of Cell 1 – PCI of Cell 3)mod6=0 | The cell PCIs are selected such that the relative shifts of PRS patterns among cells are as given by the test parameters |
| CP length |  |  | Normal |  |
| DRX |  | s | 0.64 |  |
| Radio frame receive time offset between the cells at the UE antenna connector |  | s | Cell 2 to Cell 1: 0Cell 3 to Cell 1: 3 | PRS are transmitted from synchronous cells |
| Expected RSTD |  | s | Cell 2: 3 Cell 3: 3Other neighbour cells: randomly between -3 and 3 | The expected RSTD is what is expected at the receiver. The corresponding parameter in the DL-TDOA assistance data specified in TS 37.355 [34] is the expectedRSTD indicator |
| Expected RSTD uncertainty for all neighbour cells |  | s | 5 | The corresponding parameter in the DL-TDOA assistance data specified in TS 37.355 [34] is the expectedRSTD-Uncertainty index |
| Number of cells provided in DL-TDOA assistance data |  |  | 3 | Including the reference cell |
| PRS muting info |  |  | Cell 1: ‘10’Cell 2: ‘01’Cell 3: ‘10’ | Correponds to prs-MutingInfo defined in TS 37.355 [34] |
| PRS resource RE offset |  |  | Cell 1: 0Cell 2: 0Cell 3: 1 | Cell 1 and Cell 3 are configured with different resource offsets |
| T1 |  | s | 3 | The length of the time interval from the beginning of each test |
| T2 |  | s | 1.28 | The length of the time interval that follows immediately after time interval T1 |
| AoA setup |  |  | Setup 1 | As defined in clause A.3.15.1 |
| Beam assumption |  |  | Rough | Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |

Table A.17.8.1.2.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

| Parameter |  | Unit | Cell 1 | Cell 2 | Cell 3 |
| --- | --- | --- | --- | --- | --- |
| NR RF Channel Number |  |  | 1 | 1 | 1 |
| Positiong frequency layer |  |  | 1 | 1 | 1 |
| Correlation Matrix and Antenna Configuration |  |  | 1x2 Low | 1x2 Low | 1x2 Low |
| OCNG patterns defined in A.3.2.1 |  |  | OP.5 FDD | N/A | N/A |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note 3 | Config 1 | dBm/SCS | -89 |  |  |
| PRS ![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] |  | dB | -Infinity | -Infinity | -Infinity |
| Io Note 4 | Config 1 | dBm/380.16MHz | -50.98 | -53.99 | -53.99 |
| SSB RP Note4 | Config 1 | dBm/SCS | -89 | -Infinity | -Infinity |
| SSB ![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] |  | dB | 0 | -Infinity | -Infinity |
| Propagation Condition |  |  | AWGN |  |  |
| NOTE 1:  OCNG shall be used such that active cell (Cell 1) is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The resources for uplink transmission are assigned after the end of time period T2 to UEs that do not support SDT for measurement reporting.NOTE 3:  Interference from other cells and noise sources not specified in the test are assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 4: SSB RP and Io levels have been derived from other parameters and are given for information purpose. These are not settable test parameters. |  |  |  |  |  |

Table A.17.8.1.2.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

| Parameter |  | Unit | Cell 1 | Cell 2 | Cell 3 |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T2 | T2 | T2 |
| RF Channel Number |  |  | 1 | 1 | 1 |
| Positiong frequency layer |  |  | 1 | 1 | 1 |
| Correlation Matrix and Antenna Configuration |  |  | 1x2 Low | 1x2 Low | 1x2 Low |
| OCNG patterns defined in A.3.2.1 |  |  | OP.1 | OP.1 | OP.1 |
| PRACH configuration |  |  | FR2 PRACH configuration 1 | FR2 PRACH configuration 1 | FR2 PRACH configuration 1 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note 3 | Config 1 | dBm/SCS | -89 | -89 | -89 |
| PRS ![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] | Config 1 | dB | -5.44 | -11.67 | -11.67 |
| Io | Config 1 | dBm/380.16MHz | -52.46 | -52.46 | -52.46 |
| PRS ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | -6 | -13 | -13 |
| Propagation Condition |  |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that active cells (all, except Cell 3 in T3) are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the slots with transmitted PRS.NOTE 2: The resources for uplink transmission are assigned after the end of time period T2 to UEs that do not support SDT for measurement reporting.NOTE 3: Interference from other cells and noise sources not specified in the test are assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled. |  |  |  |  |  |

##### A.17.8.1.2.2 Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 5.6A.4.6.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 5.6A.4.6 starting from the beginning of time interval T2.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD_1970049.

#### A.17.8.1.3 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state with eDRX > 10.24s

##### A.17.8.1.3.1 Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 5.6A.4.5 for RSTD measurements in RRC_INACTIVE with eDRX. Refer to clause A.7.8.1.4.1 for test configuration and procedure.

##### A.17.8.1.3.2 Test requirements

The RSTD measurement time shall fulfill the requirements specified in clause 5.6A.4.5.

The UE shall perform and report the RSTD measurements for Cell 1, Cell 2 and Cell 3 within the specified measurement period duration starting from the beginning of time interval T2. The requirement shall be evaluated based on the first measurement report received from the UE.

NOTE 1: The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3.

### A.17.8.2 UE Rx-Tx Measurements

#### A.17.8.2.1 UE Rx-Tx measurement reporting delay for single positioning frequency layer in FR2 SA without RX FH in RRC_INACTIVE mode

##### A.17.8.2.1.1 Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement without RX FH in RRC_INACTIVE state meets the requirements specified in clause 5.6A.6.5 in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configuration is listed in table A.17.8.2.1.1-1.

Table A.17.8.2.1.1-1: Supported test configurations.

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB and PRS SCS, 100 MHz bandwidth, TDD duplex mode |

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. In nr-Multi-RTT-RequestLocationInformation, nr-DL-PRS-RxHoppingRequest is not present.

The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE state.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.17.8.2.1.1-2 and table A.17.8.2.1.1-3, respectively.

Table A.17.8.2.1.1-2: General test parameters

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1 | Cell 1 | Cell 1 is the PCell in NR-Multi-RTT-ProvideAssistanceData [34]. |
| Neighbour cell |  | 1 | Cell 2 | Cell 2 is a neighbour cell in NR-Multi-RTT-ProvideAssistanceData [34]. |
| RF Channel Number |  | 1 | 1 | For both Cell 1 and Cell 2 |
| BWchannel | MHz | 1 | 100: NRB,c = 66 |  |
| SSB configuration |  | 1 | SSB.2 RedCap FR2 |  |
| SMTC configuration |  | 1 | SMTC.1 RedCap |  |
| CP length |  | 1 | Normal |  |
| DRX cycle |  | 1 | 0.64 s |  |
| Time offset between serving and neighbour cells | s | 1 | 3 | Synchronous cells |
| T1 | s | 1 | 5 |  |
| T2 | s | 1 | 20 |  |

Table A.17.8.2.1.1-3: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  | 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  | 1 | Rough |  | Rough |  |
| TDD configuration |  | 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| PDSCH RMC configuration |  | 1 | SR.3.1 TDD |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 TDD |  | N/A |  |
| OCNG Patterns |  | 1 | OP.1 |  | OP.1 |  |
| EPRE ratio of PSS to SSS | dB | 1 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |  |
| EPRE ratio of PRS to SSS |  |  |  |  |  |  |
| TRS Configuration |  | 1 | TRS.2.1 TDD |  | N/A |  |
| Initial BWP configuration |  | 1 | DLBWP.0.1 ULBWP.0.1 |  | N/A |  |
| PRS configuration |  | 1 | PRS.1.5 FR2 |  | PRS.1.5 FR2 |  |
| PRS muting info |  | 1 | ‘10’ |  | ‘01’ |  |
| SRS configuration |  | 1 | POS-SRS.3 |  | N/A |  |
| Note 2 | dBm/SCS | 1 | -89 |  |  |  |
| Note 2 | dBm/15 kHz | 1 | -98 |  |  |  |
| PRS | dB | 1 | -Infinity | -2.41 | -Infinity | -12.12 |
| PRS | dB | 1 | -Infinity | -2 | -Infinity | -10 |
| PRP Note 3 | dBm/SCS kHz | 1 | -Infinity | -91 | -Infinity | -99 |
| Io | dBm/92.16 MHz | 1 | N/A | -57.6 | N/A | -57.6 |
| Propagation Condition |  | 1 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: PRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 8: The resources for uplink transmission are assigned to the UE prior to the start of time period T2. |  |  |  |  |  |  |

##### A.17.8.2.1.2 Test requirements

The UE Rx-Tx time difference measurement time in RRC_INACTIVE state fulfills the requirements specified in clause 5.6A.6.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time specified in clause 5.6A.6 starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1A.18.3.

#### A.17.8.2.2 UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR2 SA in RRC_INACTIVE state

##### A.17.8.2.2.1 Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement with Rx FH meets the requirements specified in clause 5.6A.6.6 in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.17.8.2.2.1-1.

Table A.17.8.2.2.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1:   This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the RedCap UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, RedCap UE is released into RRC_INACTIVE state.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.17.8.2.2.1-2 and table A.17.8.2.2.1-3, respectively.

Table A.17.8.2.2.1-2: General test parameters

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1 | Cell 1 | Cell 1 is the PCell in NR-Multi-RTT-ProvideAssistanceData [34]. |
| Neighbour cell |  | 1 | Cell 2 | Cell 2 is a neighbour cell in NR-Multi-RTT-ProvideAssistanceData [34]. |
| RF Channel Number |  | 1 | 1 | For both Cell 1 and Cell 2 |
| BWchannel | MHz | 1 | 400: NRB,c = 264 |  |
| SSB configuration |  | 1 | SSB.3 FR2 |  |
| SMTC configuration |  | 1 | SMTC.1 |  |
| CP length |  | 1 | Normal |  |
| DRX |  | 1 | 1.28s |  |
| Time offset between serving and neighbour cells | s | 1 | 3 | Synchronous cells |
| PRS RX hopping request |  | 1 | requested |  |
| T1 | s | 1 | 5 |  |
| T2 | s | 1 | 10 |  |

Table A.17.8.2.2.1-3: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  | 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  | 1 | Rough |  | Rough |  |
| TDD configuration |  | 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| PDSCH RMC configuration |  | 1 | SR.3.1 TDD |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 TDD |  | N/A |  |
| OCNG Patterns |  | 1 | OP.1 |  | OP.1 |  |
| EPRE ratio of PSS to SSS | dB | 1 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |  |
| EPRE ratio of PRS to SSS |  |  |  |  |  |  |
| TRS Configuration |  | 1 | TRS.2.1 TDD |  | N/A |  |
| Initial BWP configuration |  | 1 | DLBWP.0.1 ULBWP.0.1 |  | N/A |  |
| PRS configuration |  | 1 | PRS.1.6 FR2 |  | PRS.1.6 FR2 |  |
| PRS muting info |  | 1 | ‘10’ |  | ‘01’ |  |
| SRS configuration |  | 1 | POS-SRS.3 |  | N/A |  |
| Note 2 | dBm/SCS | 1 | -89 |  |  |  |
| Note 2 | dBm/15 kHz | 1 | -98 |  |  |  |
| PRS | dB | 1 | -Infinity | -2.41 | -Infinity | -12.12 |
| PRS | dB | 1 | -Infinity | -2 | -Infinity | -10 |
| PRP Note 3 | dBm/SCS | 1 | -Infinity | -91 | -Infinity | -99 |
| Io | dBm/380.16MHz | 1 | N/A | -51.61 | N/A | -51.61 |
| Propagation Condition |  | 1 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: PRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 8: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |  |  |

##### A.17.8.2.2.2 Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause5.6A.6.6.

The RedCap UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1A.18.3.

#### A.17.8.2.3 UE Rx-Tx time difference measurements for single positioning frequency layer with eDRX > 10.24s in FR2 SA

##### A.17.8.2.3.1 Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 5.6A.6.5 for UE Rx-Tx measurements in RRC_INACTIVE with eDRX. Refer to clause A.7.8.3.3.1 for test configuration and procedure.

##### A.17.8.2.3.2 Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 5.6A.6.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE 1: The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1A.18.3.

### A.17.8.3 PRS-RSRP Measurements

#### A.17.8.3.1 PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_INACTIVE

##### A.17.8.3.1.1 Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements specified in clause 9.9A.3.5 for single positioning frequency layer under AWGN propagation conditions in RRC_INACTIVE. Supported test configurations are shown in table A.17.8.3.1.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

During T1 UE is in RRC_CONNECTED, the NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The measurement reporting delay test in this clause is valid in the cases where the RedCap UE is either not configured by the LMF to perform PRS-RSRP measurement with RX FH via NR-DL-AoD-RequestLocationInformation or the UE is configured by the LMF to perform PRS-RSRP measurement with RX FH and reports the PRS-RSRP measurement based on the single hop in NR-DL-AoD-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.8.3.1.1-2, and table A.17.8.3.1.1-3.

Table A.17.8.3.1.1-1: supported test configurations for PRS RSRP measurement for FR2

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.8.3.1.1-2: General test parameters for PRS RSRP measurement reporting delay

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1 | 1: Cell 1 and Cell 2 | One TDD carrier frequency is used for the NR cells. |
| Active cell |  | Config 1 | NR cell 1 (PCell) | Cell 1 is the PCell and the DL-AoD reference cell in the positioning assistance data. |
| Neighbour cell |  | Config 1 | NR cell 2 | Cell 2 is a neighbour cell in the positioning assistance data. |
| SMTC parameters |  | Config 1 | SMTC.1 | As specified in clause A.3.11 |
| SSB parameters |  | Config 1 | SSB.3 FR2 | As specified in clause A.3.10.2 |
| CP length |  | Config 1 | Normal |  |
| DRX |  | Config 1 | 0.64 s |  |
| Time offset between serving and neighbour cells |  | Config 1 | 3 s | Synchronous cells. |
| Expected RSTD | s | Config 1 | 3 |  |
| Expected RSTD uncertainty | s | Config 1 | 5 |  |
| T1 | s | Config 1 | 5 |  |
| T2 | s | Config 1 | 41 |  |

Table A.17.8.3.1.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

| Parameter |  | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 |  | T2 | T1 | T2 |  |
| AoA setup |  |  | Config 1 | Setup 1 as specified in clause A.3.15 |  |  |  |  |  |
| Beam AssumptionNote 7 |  |  | Config 1 | Rough |  |  | Rough |  |  |
| TDD configuration |  |  | Config 1 | TDDConf.3.1 |  |  | TDDConf.3.1 |  |  |
| Duplex mode |  |  | Config 1 | TDD |  |  | TDD |  |  |
| BWchannel |  | MHz | Config 1 | 100: NRB,c = 66 |  |  | 100: NRB,c = 66 |  |  |
| BWP BW |  | MHz | Config 1 | 100: NRB,c = 66 |  |  | 100: NRB,c = 66 |  |  |
| BWP configuration | Initial DL BWP |  | Config 1 | DLBWP.0.1 |  |  | N/A |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  | N/A |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1 | OP.1 |  |  | OP.1 |  |  |
| PDSCH Reference measurement channel |  |  | Config 1 | SR.3.1 TDD |  |  | - |  |  |
| CORESET Reference Channel |  |  | Config 1 | CR.3.1 TDD |  |  | - |  |  |
| Dedicated CORESET RMC configuration |  |  | Config 1 | CCR.3.1 TDD |  |  | - |  |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1 | 120 |  |  | 120 |  |  |
| PRS configuration |  |  | Config 1 | PRS.1.5 FR2 |  |  | PRS.1.5 FR2 |  |  |
| PRS muting configuration |  |  | Config 1 | ‘10’ |  |  | ‘01’ |  |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1 | 0 |  |  | 0 |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15kHz Note5 |  | -98 |  |  | -98 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS Note4 | Config 1 | -89 |  |  | -89 |  |  |
| SS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -91 |  | -91 | -Infinity | -99 |  |
| PRS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -Infinity |  | -91 | -Infinity | -99 |  |
| PRS |  | dB | Config 1 | -Infinity |  | -2.41 | -Infinity | -12.12 |  |
| PRS |  | dB | Config 1 | -Infinity |  | -2 | -Infinity | -10 |  |
| IoNote3 |  | dBm/95.04 MHz Note5 | Config 1 | -57.89 | -57.63 |  | -57.89 |  | -57.63 |
| Propagation Condition |  |  | Config 1 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP/PRS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation. |  |  |  |  |  |  |  |  |  |

##### A.17.8.3.1.2 Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 9.9A.3.5. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9A.3.5 starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1A.17, i.e., between PRS RSRP_0 and PRS RSRP_126.

A.17.8.3.2 PRS-RSRP measurement delay with FH in RRC_INACTIVE state in FR2

A.17.8.3.2.1 Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement with FH by a RedCap UE meets requirements specified in clause 5.6A.5.5 for single positioning frequency layer under AWGN propagation conditions in RRC_INACTIVE. Supported test configurations are shown in table A.17.8.3.2.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

During T1 UE is in RRC_CONNECTED, the NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.7.8.1.2.1.1-2, and table A.17.8.3.2.1-3.

Table A.17.8.3.2.1-1: supported test configurations for PRS RSRP measurement for FR2-FR2

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 100 MHz, cell bandwidth 400 MHz, TDD duplex mode |

Table A.17.8.3.2.1-2: General test parameters for PRS RSRP measurement reporting delay

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1 | 1: Cell 1 and Cell 2 | One TDD carrier frequency is used for the NR cells. |
| Active cell |  | Config 1 | NR cell 1 (Pcell) | Cell 1 is the PCell and the DL-AoD reference cell in the positioning assistance data. |
| Neighbour cell |  | Config 1 | NR cell 2 | Cell 2 is a neighbour cell in the positioning assistance data. |
| SMTC parameters |  | Config 1 | SMTC.1 | As specified in clause A.3.11 |
| SSB parameters |  | Config 1 | SSB.3 FR2 | As specified in clause A.3.10.2 |
| CP length |  | Config 1 | Normal |  |
| DRX |  | Config 1 | 0.64 s |  |
| Time offset between serving and neighbour cells |  | Config 1 | 3 s | Synchronous cells. |
| Expected RSTD | s | Config 1 | 3 |  |
| Expected RSTD uncertainty | s | Config 1 | 5 |  |
| PRS RX hopping request |  | Config 1 | Present |  |
| T1 | s | Config 1 | 5 |  |
| T2 | s | Config 1 | 41 |  |

Table A.17.8.3.2.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

| Parameter |  | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 |  | T1 | T2 |  |
| AoA setup |  |  | Config 1 | Setup 1 as specified in clause A.3.15 |  |  |  |  |  |
| Beam AssumptionNote 7 |  |  | Config 1 | Rough |  |  | Rough |  |  |
| TDD configuration |  |  | Config 1 | TDDConf.3.1 |  |  | TDDConf.3.1 |  |  |
| Duplex mode |  |  | Config 1 | TDD |  |  | TDD |  |  |
| BWchannel |  | MHz | Config 1 | 100: NRB,c = 66 |  |  | 100: NRB,c = 66 |  |  |
| BWP configuration | Initial DL BWP |  | Config 1 | DLBWP.0.1 |  |  | N/A |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  | N/A |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1 | OP.1 |  |  | OP.1 |  |  |
| PDSCH Reference measurement channel |  |  | Config 1 | SR.3.1 TDD |  |  | - |  |  |
| CORESET Reference Channel |  |  | Config 1 | CR.3.1 TDD |  |  | - |  |  |
| Dedicated CORESET RMC configuration |  |  | Config 1 | CCR.3.1 TDD |  |  | - |  |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1 | 120 |  |  | 120 |  |  |
| PRS configuration |  |  | Config 1 | PRS.1.6 FR2 |  |  | PRS.1.6 FR2 |  |  |
| PRS muting configuration |  |  | Config 1 | ‘10’ |  |  | ‘01’ |  |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1 | 0 |  |  | 0 |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15kHz Note5 |  | -98 |  |  | -98 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS Note4 | Config 1 | -89 |  |  | -89 |  |  |
| SS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -91 | -91 |  | -Infinity | -99 |  |
| PRS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -Infinity | -91 |  | -Infinity | -99 |  |
| PRS |  | dB | Config 1 | -Infinity | -2.41 |  | -Infinity | -12.12 |  |
| PRS |  | dB | Config 1 | -Infinity | -2 |  | -Infinity | -10 |  |
| IoNote3 |  | dBm/95.04 MHz Note5 | Config 1 | -60.01 |  | -57.63 | -60.01 |  | -57.63 |
| Propagation Condition |  |  | Config 1 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that active cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the subframes with transmitted PRS.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP/PRS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation. |  |  |  |  |  |  |  |  |  |

##### A.17.8.3.2.2 Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 5.6A.5.5. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 5.6A.5.5 starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause10.1A.17.3, i.e., between PRS RSRP_0 and PRS RSRP_126.

#### A.17.8.3.3 PRS-RSRP reporting delay in RRC_INACTIVE with eDRX

##### A.17.8.3.3.1 Test Purpose and Environment

The purpose of the test is to verify a RedCap UE can meet the PRS RSRP measurement requirements specified in clause 5.6A.5.5 for single positioning frequency layer under AWGN propagation conditions in RRC_INACTIVE, when configured with eDRX and without FH. Supported test configurations are shown in table A.17.8.3.3.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

During T1 UE is in RRC_CONNECTED, the NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.8.3.3.1-2, and table A.17.8.3.3.1-3.

Table A.17.8.3.3.1-1: supported test configurations for PRS RSRP measurement for FR2

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.8.3.3.1-2: General test parameters for PRS RSRP measurement reporting delay

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1 | 1: Cell 1 and Cell 2 | One TDD carrier frequency is used for the NR cells. |
| Active cell |  | Config 1 | NR cell 1 (Pcell) | Cell 1 is the PCell and the DL-AoD reference cell in the positioning assistance data. |
| Neighbour cell |  | Config 1 | NR cell 2 | Cell 2 is a neighbour cell in the positioning assistance data. |
| SMTC parameters |  | Config 1 | SMTC.1 | As specified in clause A.3.11 |
| SSB parameters |  | Config 1 | SSB.3 FR2 | As specified in clause A.3.10.2 |
| CP length |  | Config 1 | Normal |  |
| DRX |  | Config 1 | 0.64 s |  |
| CN and RAN eDRX configuration |  | Config 1 | eDRX cycle = 40.96 sPTW length = 1.28 s |  |
| Reporting periodicity | s | Config 1 | 20 | reportingInterval for periodic reporting defined in TS 37.355 [34]. |
| Time offset between serving and neighbour cells |  | Config 1 | 3 s | Synchronous cells. |
| Expected RSTD | s | Config 1 | 3 |  |
| Expected RSTD uncertainty | s | Config 1 | 5 |  |
| T1 | s | Config 1 | 5 |  |
| T2 | s | Config 1 | 41 |  |

Table A.17.8.3.3.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  |  | Config 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  |  | Config 1 | Rough |  | Rough |  |
| TDD configuration |  |  | Config 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| Duplex mode |  |  | Config 1 | TDD |  | TDD |  |
| BWchannel |  | MHz | Config 1 | 100: NRB,c = 66 |  | 100: NRB,c = 66 |  |
| BWP configuration | Initial DL BWP |  | Config 1 | DLBWP.0.1 |  | N/A |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | N/A |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1 | SR.3.1 TDD |  | - |  |
| CORESET Reference Channel |  |  | Config 1 | CR.3.1 TDD |  | - |  |
| Dedicated CORESET RMC configuration |  |  | Config 1 | CCR.3.1 TDD |  | - |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1 | 120 |  | 120 |  |
| PRS configuration |  |  | Config 1 | PRS.1.1 FR2 |  | PRS.1.1 FR2 |  |
| PRS muting configuration |  |  | Config 1 | ‘10’ |  | ‘01’ |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15kHz Note5 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS Note4 | Config 1 | -89 |  | -89 |  |
| SS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -91 | -91 | -Infinity | -99 |
| PRS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -Infinity | -91 | -Infinity | -99 |
| PRS |  | dB | Config 1 | -Infinity | -2.41 | -Infinity | -12.12 |
| PRS |  | dB | Config 1 | -Infinity | -2 | -Infinity | -10 |
| IoNote3 |  | dBm/95.04Note5 | Config 1 | -57.89 |  | -57.89 |  |
| Propagation Condition |  |  | Config 1 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP/PRS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation. |  |  |  |  |  |  |  |

##### A.17.8.3.3.2 Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 5.6A.5.5. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 5.6A.5.5 with Tavailable_PRS = 0.64 s starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

A test is considered complete after the UE reports the first set of positioning measurements based on the configured reportingInterval.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1A.17.3.

### A.17.8.4 PRS-RSRPP Measurements

#### A.17.8.4.1 PRS-RSRPP measurement delay without FH in RRC_INACTIVE state in FR2

##### A.17.8.4.1.1 Test Purpose and Environment

The purpose of the test is to verify the PRS RSRPP measurement without FH by a RedCap UE meets requirements specified in clause 5.6A.7.5 for single positioning frequency layer under a 2-tap channel propagation conditions in standalone scenario. Supported test configurations are shown in table A.17.8.4.1.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the Pcell.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2. During T2 UE shall be in RRC_INACTIVE state and both cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.8.4.1.1-2, and table A.17.8.4.1.1-3.

Table A.17.8.4.1.1-1: supported test configurations for PRS RSRPP measurement for FR2

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.8.4.1.1-2: General test parameters for PRS RSRPP measurement reporting delay

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1 | 1: Cell 1 and Cell 2 | One TDD carrier frequency is used for the NR cells. |
| Active cell |  | Config 1 | NR cell 1 (Pcell) | Cell 1 is the PCell and the DL-AoD reference cell in the positioning assistance data. |
| Neighbour cell |  | Config 1 | NR cell 2 | Cell 2 is a neighbour cell in the positioning assistance data. |
| SMTC parameters |  | Config 1 | SMTC.1 | As specified in clause A.3.11 |
| SSB parameters |  | Config 1 | SSB.3 FR2 | As specified in clause A.3.10.2 |
| CP length |  | Config 1 | Normal |  |
| DRX | s | Config 1 | 0.64 | ON |
| Time offset between serving and neighbour cells | s | Config 1 | 3 | Synchronous cells. |
| Expected RSTD | s | Config 1 | 3 |  |
| Expected RSTD uncertainty | s | Config 1 | 5 |  |
| PRS RX hopping request |  | Config 1 | NOT present |  |
| T1 | s | Config 1 | 5 |  |
| T2 | s | Config 1 | 7 |  |

Table A.17.8.4.1.1-3: Cell-specific test parameters for PRS RSRPP measurement reporting delay

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  |  | Config 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  |  | Config 1 | Rough |  | Rough |  |
| TDD configuration |  |  | Config 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| Duplex mode |  |  | Config 1 | TDD |  | TDD |  |
| BWchannel |  | MHz | Config 1 | 100: NRB,c = 66 |  | 100: NRB,c = 66 |  |
| BWP configuration | Initial DL BWP |  | Config 1 | DLBWP.0.1 |  | N/A |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | N/A |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1 | SR.3.1 TDD |  | - |  |
| CORESET Reference Channel |  |  | Config 1 | CR.3.1 TDD |  | - |  |
| Dedicated CORESET RMC configuration |  |  | Config 1 | CCR.3.1 TDD |  | - |  |
| TRS configuration |  |  | Config 1 | TRS.2.1 TDD |  | - |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1 | 120 |  | 120 |  |
| PRS configuration |  |  | Config 1 | PRS.1.3 FR2 |  | PRS.1.3 FR2 |  |
| PRS muting configuration |  |  | Config 1 | ‘10’ |  | ‘01’ |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15kHz Note5 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS Note4 | Config 1 | -89 |  | -89 |  |
| SS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -89 | -91 | -Infinity | -99 |
| PRS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -Infinity | -91 | -Infinity | -99 |
| PRS |  | dB | Config 1 | -Infinity | -2.12 | -Infinity | -12.12 |
| PRS |  | dB | Config 1 | -Infinity | -2 | -Infinity | -10 |
| IoNote3 |  | dBm/95.04 MHz Note5 | Config 1 | -60.01 | -57.63 | -60.01 | -57.63 |
| Propagation Condition |  |  | Config 1 | Two-tap channel defined in 38.101-4 annex B.2.4, a = 1, $\tau  _{d}=0.45 $ µs and $ f_{D}=5 $ Hz |  |  |  |
| NOTE 1: OCNG shall be used such that active cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the subframes with transmitted PRS.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP/PRS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation. |  |  |  |  |  |  |  |

A.17.8.4.1.2 Test Requirements

The PRS RSRPP measurement time fulfils the requirements specified in clause 5.6A.7.5. The UE shall perform and report the PRS RSRPP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 5.6A.7.5 starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRPP measurement for each correct event shall be within the PRS RSRPP reporting range specified in clause10.1A.19.3, i.e., between PRS RSRPP_0 and PRS RSRPP_126.

#### A.17.8.4.2 PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state

##### A.17.8.4.2.1 Test Purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement requirements with Rx FH in RRC_INACTIVE state meets the delay requirements specified in clause 5.6A.7.6 in an environment with two-tap channel propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.17.8.4.2.1-1.

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The test requirements apply when frequencyHopping is configured to UE.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource occasion occuring T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.8.4.2.1-2, and table A.17.8.4.2.1-3.

Table A.17.8.4.2.1-1: supported test configurations for PRS-RSRPP measurement for FR2

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1:   This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

Table A.17.8.4.2.1-2: General test parameters for PRS-RSRPP measurement reporting delay

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1 | 1: Cell 1 and Cell 2 | One TDD carrier frequency is used for the NR cells. |
| Active cell |  | Config 1 | NR cell 1 (PCell) | Cell 1 is the PCell and the DL-AoD reference cell in the positioning assistance data. |
| Neighbour cell |  | Config 1 | NR cell 2 | Cell 2 is a neighbour cell in the positioning assistance data. |
| SMTC parameters |  | Config 1 | SMTC.1 | As specified in clause A.3.11 |
| SSB parameters |  | Config 1 | SSB.3 FR2 | As specified in clause A.3.10.2 |
| A3-Offset | dB | Config 1 | -6 |  |
| Hysteresis | dB | Config 1 | 0 |  |
| CP length |  | Config 1 | Normal |  |
| TimeToTrigger | s | Config 1 | 0 |  |
| Filter coefficient |  | Config 1 | 0 | L3 filtering is not used |
| DRX | s | Config 1 | 1.28 |  |
| Time offset between serving and neighbour cells | s | Config 1 | 3 | Synchronous cells. |
| PRS RX hopping request |  | 1 | requested |  |
| Expected RSTD | s | Config 1 | 3 |  |
| Expected RSTD uncertainty | s | Config 1 | 5 |  |
| T1 | s | Config 1 | 5 |  |
| T2 | s | Config 1 | 7 |  |

Table A.17.8.4.2.1-3: Cell-specific test parameters for PRS-RSRPP measurement reporting delay

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  |  | Config 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  |  | Config 1 | Rough |  | Rough |  |
| TDD configuration |  |  | Config 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| Duplex mode |  |  | Config 1 | TDD |  | TDD |  |
| BWchannel |  | MHz | Config 1 | 400: NRB,c = 264 |  | 400: NRB,c = 264 |  |
| BWP configuration | Initial DL BWP |  | Config 1 | DLBWP.0.1 |  | N/A |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | N/A |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1RedCap |  | N/A |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1RedCap |  | N/A |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1 | SR.3.1 TDD |  | - |  |
| CORESET Reference Channel |  |  | Config 1 | CR.3.1 TDD |  | - |  |
| Dedicated CORESET RMC configuration |  |  | Config 1 | CCR.3.1 TDD |  | - |  |
| TRS configuration |  |  | Config 1 | TRS.2.1 TDD |  | - |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1 | 120 |  | 120 |  |
| PRS configuration |  |  | Config 1 | PRS.1.6 FR2 |  | PRS.1.6 FR2 |  |
| PRS muting configuration |  |  | Config 1 | ‘10’ |  | ‘01’ |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | Config 1 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15kHz Note5 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS Note4 | Config 1 | -89 |  | -89 |  |
| SS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -89 | -89 | -Infinity | -89 |
| PRS-RSRP Note 3 |  | dBm/SCS Note5 | Config 1 | -Infinity | -91 | -Infinity | -99 |
| PRS |  | dB | Config 1 | -Infinity | -2.41 | -Infinity | -12.12 |
| PRS |  | dB | Config 1 | -Infinity | -2 | -Infinity | -10 |
| IoNote3 |  | dBm/380.16MHz Note5 | Config 1 | -50.98 | -51.61 | -50.98 | -51.61 |
| Propagation Condition |  |  | Config 1 | Two-tap channel defined in 38.101-4 annex B.2.4, a = 1, $\tau  _{d}=0.45 $ µs and $ f_{D}=5 $ Hz |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP/PRS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 8: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |  |  |  |

##### A.17.8.4.2.2 Test Requirements

The PRS-RSRPP measurement time fulfils the requirements specified in clause 5.6A.7.6. The UE shall perform and report the PRS-RSRPP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 5.6A.7.6 starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS-RSRPP measurement for each correct event shall be within the PRS-RSRPP reporting range specified in clause 10.1A.19.3, i.e., between PRS RSRPP_0 and PRS RSRPP_126.

#### A.17.8.4.3 PRS-RSPP reporting delay in RRC_INACTIVE state with eDRX > 10.24s

##### A.17.8.4.3.1 Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 5.6A.7.5 for PRS-RSRPP measurements in RRC_INACTIVE with eDRX. Refer to clause A.7.8.4.3.1 for test configuration and procedure.

##### A.17.8.4.3.2 Test requirements

The PRS-RSRPP measurement time fulfils the requirements specified in clause 5.6A.7.5.

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2 within the specified measurement period duration starting from the beginning of time interval T2. The requirement shall be evaluated based on the first measurement report received from the UE.

NOTE 1: The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS-RSRPP measurement for each correct event shall be within the PRS-RSRPP reporting range specified in clause 10.1A.19.3.

## A.17.9 Measurement Performance Requirements for RedCap in RRC_INACTIVE

### A.17.9.1 RSTD Measurements

#### A.17.9.1.1 RSTD measurement accuracy test case for RedCap UE without FH in FR2 in RRC_INACTIVE state

##### A.17.9.1.1.1 Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC_INACTIVE state meets the accuracy requirements specified in clause 10.1A.16.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.17.9.1.1.1-1.

Table A.17.9.1.1.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2. The UE is configured with DRX cycle of 0.64 s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the RedCap UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 5.6A.4.5.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The accuracy test parameters and OTA related test parameters are as given in table A.17.9.1.1.1-2 and table A.17.9.1.1.1-3, respectively.

Table A.17.9.1.1.1-2: RSTD accuracy test parameters

| Parameter | Unit | Test 1 |  |
| --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 |
| PRS ARFCN |  | freq1 |  |
| Duplex mode |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  |
| BWchannel | MHz | 100: NRB,c = 66 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - |
| Uplink dedicated BWP configuration |  | ULBWP.1.1 | - |
| TRS configuration |  | TRS.2.1 TDD | - |
| TCI state |  | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.3 | OP.3 |
| SSB configuration |  | SSB.3 FR2 | SSB.3 FR2 |
| SMTC configuration |  | SMTC.1 | SMTC.1 |
| PRS configuration |  | PRS.1.1 FR2 | PRS.1.1 FR2 |
| PRS Resource slot offset | slot | 0 | 4 |
| Expected RSTD | s | N/A | 3 |
| Expected RSTD uncertainty | s | N/A | 5 |
| Time offset with Cell 1 | s | - | 3 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation conditions |  | AWGN | AWGN |
| Antenna configuration |  | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |

Table A.17.9.1.1.1-3: RSTD accuracy OTA related test parameters

| Parameter | Unit | Test 1 |  |
| --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |
| Assumption for UE beamsNote 5 |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote3 | -89 |  |
| PRS | dB | -5.7 | -11.9 |
| PRS-RSRPNote2 | dBm/SCS | -94.7 | -100.9 |
| PRS BB Note4 | dB | -6 | -13 |
| IoNote2 | dBm/95.04 MHz Note3 | -58.76 | -58.76 |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: SSB_RP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 4: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 36.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 5: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation. |  |  |  |

##### A.17.9.1.1.2 Test Requirements

The RSTD measurement accuracy shall fulfil the absolute requirement in clause 10.1A.16.2.

#### A.17.9.1.2 RSTD measurement accuracy test case for RedCap UE with FH in FR2 in RRC_INACTIVE state

##### A.17.9.1.2.1 Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement in RRC_INACTIVE state meets the accuracy requirements specified in clause10.1A.16.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.17.9.1.2.1-1. The test parameters are as given in table A.17.9.1.2.1-2, table A.17.9.1.2.1-3 and table A.17.9.1.2.1-4.

Table A.17.9.1.2.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1:   This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2. The UE is configured with DRX cycle of 0.64s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the UE before the start of the test.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation as specified in TS 37.355 [34], clause 6.5.12. The frequency hopping configurations are specified in clause A.3.31.

Table A.17.9.1.2.1-2: RSTD accuracy test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| PRS ARFCN |  | freq1 |  | freq1 |  |
| Duplex mode |  | TDD |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel | MHz | 400: NRB,c = 264 |  | 400: NRB,c = 264 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - | DLBWP.0.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - | ULBWP.0.1 | - |
| Uplink dedicated BWP configuration |  | ULBWP.1.1 | - | ULBWP.1.1 | - |
| TRS configuration |  | TRS.2.1 TDD | - | TRS.2.1 TDD | - |
| TCI state |  | TCI.State.0 | - | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3.1 TDD | - | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.3 | OP.3 | OP.3 | OP.3 |
| SSB configuration |  | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 |
| SMTC configuration |  | SMTC.1 | SMTC.1 | SMTC.1 | SMTC.1 |
| PRS configuration |  | PRS.1.6 FR2 | PRS.1.6 FR2 | PRS.1.6 FR2 | PRS.1.6 FR2 |
| PRS Resource slot offset | slot | 0 | 4 | 0 | 4 |
| Expected RSTD | s | N/A | 3 | N/A | 3 |
| Expected RSTD uncertainty | s | N/A | 5 | N/A | 5 |
| Time offset with Cell 1 | s | - | 3 | - | 3 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Propagation conditions |  | AWGN | AWGN | AWGN | AWGN |
| Antenna configuration |  | 1x2 | 1x2 | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |  |  |

Table A.17.9.1.2.1-3: RSTD accuracy OTA related test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |  |  |
| Assumption for UE beamsNote 5 |  | Rough |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote3 | -89 |  | -89 |  |
| PRS ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | -5.7 | -11.9 | -5.7 | -11.9 |
| PRS-RSRPNote2 | dBm/SCS | -94.7 | -100.9 | -94.7 | -100.9 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot]BB Note4 | dB | -6 | -13 | -6 | -13 |
| IoNote2 | dBm/380.16MHz Note3 | -52.74 | -52.74 | -52.74 | -52.74 |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: SSB_RP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 4: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 36.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 5: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation. |  |  |  |  |  |

##### A.17.9.1.2.2 Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1A.16.2.

### A.17.9.2 UE Rx-Tx Measurements

#### A.17.9.2.1 UE Rx-Tx measurement accuracy for single positioning frequency layer in FR2 SA without RX FH in RRC_INACTIVE mode

##### A.17.9.2.1.1 Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy without RX FH in RRC_INACTIVE mode is within the specified limits. This test will verify the requirements in clause 10.1A.18.2. The test is conducted in AWGN propagation condition in FR2 in standalone scenario.

The supported test configuration is listed in table A.17.9.2.1.1-1.

Table A.17.9.2.1.1-1: Supported test configurations.

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB and PRS SCS, 100 MHz bandwidth, TDD duplex mode |

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test. In nr-Multi-RTT-RequestLocationInformation, nr-DL-PRS-RxHoppingRequest is not present.

The UE is configured to transmit SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

##### A.17.9.2.1.2 Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.17.9.2.1.2-1.

Table A.17.9.2.1.2-1: UE Rx-Tx time difference measurement accuracy test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |
| --- | --- | --- | --- | --- | --- |
| AoA setup |  | 1 | Setup 1 as specified in clause A.3.15 |  |  |
| BWchannel | MHz | 1 | 100: NRB,c = 66 |  |  |
| Beam AssumptionNote 6 |  | 1 | Rough | Rough |  |
| DRX | s | 1 | 0.64 |  |  |
| Time offset with Cell 1 | s | 1 | N/A | 3 |  |
| TDD configuration |  | 1 | TDDConf.3.1 | TDDConf.3.1 |  |
| PDSCH RMC configuration |  | 1 | SR.3.1 TDD | N/A |  |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD | N/A |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 TDD | N/A |  |
| OCNG Patterns |  | 1 | OP.1 | OP.1 |  |
| Initial BWP configuration |  | 1 | DLBWP.0.1 ULBWP.0.1 | N/A |  |
| PRS configuration |  | 1 | PRS.1.5 FR2 | PRS.1.5 FR2 |  |
| PRS Resource slot offset | slot | 1 | 0 | 4 |  |
| SRS configuration |  | 1 | POS-SRS.3 | N/A |  |
| Note 1 | dBm/SCS | 1 | -89 |  |  |
| Note 1 | dBm/15 kHz | 1 | -98 |  |  |
| PRS | dB | 1 | -2.41 | -12.12 |  |
| PRS | dB | 1 | -2 | -10 |  |
| PRS-RSRP Note 2 | dBm/SCS kHz | 1 | -91 | -99 |  |
| Io | dBm/92.16 MHz | 1 | -57.6 | -57.6 |  |
| Propagation Condition |  | 1 | AWGN |  |  |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over sub-carriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 2: PRS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 5: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 6: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 7: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 36.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |  |

##### A.17.9.2.1.3 Test requirements

The UE Rx-Tx time difference measurement time fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1A.18.2 for both Cell 1 and Cell 2.

#### A.17.9.2.2 SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC_INACTIVE state in FR2

##### A.17.9.2.2.1 Test purpose and Environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement requirements with FH by RedCap UE in RRC_INACTIVE state are within the specified limits. This test will verify the requirements in clause 10.1A.18.2.3. The test is conducted in AWGN propagation condition in FR2 in standalone scenario.

The supported test configuration is listed in table A.17.9.2.2.1-1.

Table A.17.9.2.2.1-1: Supported test configurations

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1:   This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test. The test requirements apply when frequencyHopping is configured to UE.

The UE is configured to transmit SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

##### A.17.9.2.2.2 Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.17.9.2.2.2-1.

Table A.17.9.2.2.2-1: UE Rx-Tx time difference measurement accuracy test parameters

| Parameter | Unit | Test configuration | Test 1 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 |  |
| AoA setup |  | 1 | Setup 1 as specified in clause A.3.15 |  |  |
| BWchannel | MHz | 1 | 400: NRB,c = 264 |  |  |
| Beam AssumptionNote 7 |  | 1 | Rough | Rough |  |
| DRX | s | 1 | 0.64 |  |  |
| Time offset with Cell 1 | s | 1 | N/A | 3 |  |
| TDD configuration |  | 1 | TDDConf.3.1 | TDDConf.3.1 |  |
| PDSCH RMC configuration |  | 1 | SR.3.1 TDD | N/A |  |
| RMSI CORESET RMC configuration |  | 1 | CR.3.1 TDD | N/A |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.3.1 TDD | N/A |  |
| OCNG Patterns |  | 1 | OP.1 | OP.1 |  |
| Initial BWP configuration |  | 1 | DLBWP.0.1 ULBWP.0.1 | N/A |  |
| PRS configuration |  | 1 | PRS.1.6 FR2 | PRS.1.6 FR2 |  |
| PRS Resource slot offset | slot | 1 | 0 | 4 |  |
| SRS configuration |  | 1 | POS-SRS.3 | N/A |  |
| Note 2 | dBm/SCS | 1 | -89 |  |  |
| Note 2 | dBm/15 kHz | 1 | -98 |  |  |
| PRS | dB | 1 | -2.41 | -12.12 |  |
| PRS | dB | 1 | -2 | -10 |  |
| PRS-RSRP Note 3 | dBm/SCS | 1 | -91 | -99 |  |
| Io Note 3 | dBm/380.16MHz | 1 | -51.61 | -51.61 |  |
| Propagation Condition |  | 1 | AWGN |  |  |
| NOTE 1: OCNG shall be used such that active cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the subframes with transmitted PRS.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: PRS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 8: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 36.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |  |

##### A.17.9.2.2.3 Test requirements

The UE Rx-Tx time difference measurement time fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1A.18.2.3for both Cell 1 and Cell 2.

### A.17.9.3 PRS-RSRP Measurements

A.17.9.3.1 PRS-RSRP measurement accuracy without FH in RRC_INACTIVE state in FR2

A.17.9.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRP measurement without FH by a RedCap UE in RRC_INACTIVE is within the specified limits. This test will verify the requirements in clauses 10.1A.17.2.1 for absolute accuracy and 10.1A.17.2.2 for relative accuracy.

A.17.9.3.1.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.9.3.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in table A.17.9.3.1.2-2 and A.17.9.3.1.2-3. In all test cases, Cell 1 is the PCell.

Table A.17.9.3.1.2-1: PRS-RSRP supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.9.3.1.2-2: PRS-RSRP general test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Cell ID |  | 489 | 0 | 489 | 0 |
| SSB ARFCN |  | freq1 |  | freq1 |  |
| Duplex mode |  | TDD |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel | MHz | 100: NRB,c = 66 |  | 100: NRB,c = 66 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - | DLBWP.0.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - | ULBWP.0.1 | - |
| DRX cycle configuration |  | 1.28s | - | 1.28s | - |
| TCI state |  | TCI.State.0 | - | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3.1 TDD | - | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.3 | OP.3 | OP.3 | OP.3 |
| SSB configuration |  | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 |
| SMTC configuration |  | SMTC.1 | SMTC.1 | SMTC.1 | SMTC.1 |
| Time offset with Cell 1 | s | - | 3 | - | 3 |
| PRS configuration |  | PRS.1.5 FR2 | PRS.1.5 FR2 | PRS.1.5 FR2 | PRS.1.5 FR2 |
| PRS Resource slot offset | slot | 0 | 4 | 0 | 4 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Propagation conditions |  | AWGN | AWGN | AWGN | AWGN |
| Antenna configuration |  | 1x2 | 1x2 | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that active cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the subframes with transmitted PRS. |  |  |  |  |  |

Table A.17.9.3.1.2-3: PRS-RSRP OTA related test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |  |  |
| Assumption for UE beamsNote 5 |  | Rough |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15kHzNote 3 | -98 |  | Same as Test 1 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote 3 | -89 |  | Same as Test 1 |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | -2 | -10 | -2 | -10 |
| Es | dBm/SCSNote 3 | - | - | - | - |
| PRS_RPNote2 | dBm/SCS | -91 | -99 | -91 | -99 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot]BB Note 4 | dB | -2.41 | -12.12 | -2.41 | -12.12 |
| IoNote2 | dBm/95.04 MHz Note3 | -57.63 |  | -57.63 |  |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: PRS_RP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 4: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 36.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 5: Information about types of UE beam is given in anex B.2.1.3 and does not limit UE implementation or test system implementation. |  |  |  |  |  |

A.17.9.3.1.3 Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1 if the reported PRS-RSRP is in the range shown in table A.17.9.3.1.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2.

Table A.17.9.3.1.3-1: PRS-RSRP absolute accuracy test requirement

|  | Test requirement Notes1,2,3 |
| --- | --- |
| Cell 1 | PRS_RP1 -δ +Gmin ≤ Reported RSRP(dBm) ≤ PRS_RP1 +δ +Gmax |
| Cell 2 | PRS_RP2 -δ +Gmin ≤ Reported RSRP(dBm) ≤ PRS_RP2 +δ +Gmax |
| NOTE 1:  PRS_RPn is the equivalent power received by an antenna with 0dBi gain at the centre of the quiet zone configured in the test for the cell n under consideration.NOTE 2:  δ is the RSRP absolute accuracy requirement from table 10.1.24.2.1-2, selected according to the Io used in the test.NOTE 3:  Gmin and Gmax are the minimum and maximum UE gain values from table B.2.1.6.1-1, selected according to the UE power class. |  |

#### A.17.9.3.2 PRS-RSRP measurement accuracy with FH in RRC_INACTIVE state in FR2

##### A.17.9.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRP measurement with FH by a RedCap UE in RRC_INACTIVE is within the specified limits. This test will verify the requirements in clauses 10.1A.17.2.1 for absolute accuracy and 10.1A.17.2.2 for relative accuracy.

##### A.17.9.3.2.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.9.3.2.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in table A.17.9.3.2.2-2 and A.17.9.3.2.2-3. In all test cases, Cell 1 is the PCell. PRS RX hopping is present in NR-DL-AoD-RequestLocationInformation.

Table A.17.9.3.2.2-1: PRS-RSRP supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1:   This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

Table A.17.9.3.2.2-2: PRS-RSRP general test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Cell ID |  | 489 | 0 | 489 | 0 |
| SSB ARFCN |  | freq1 |  | freq1 |  |
| Duplex mode |  | TDD |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel | MHz | 400: NRB,c = 264 |  | 400: NRB,c = 264 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - | DLBWP.0.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - | ULBWP.0.1 | - |
| DRX cycle configuration |  | 1.28s | - | 1.28s | - |
| TCI state |  | TCI.State.0 | - | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3.1 TDD | - | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.3 | OP.3 | OP.3 | OP.3 |
| SSB configuration |  | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 |
| SMTC configuration |  | SMTC.1 | SMTC.1 | SMTC.1 | SMTC.1 |
| Time offset with Cell 1 | s | - | 3 | - | 3 |
| PRS configuration |  | PRS.1.6 FR2 | PRS.1.6 FR2 | PRS.1.6 FR2 | PRS.1.6 FR2 |
| PRS Resource slot offset | slot | 0 | 4 | 0 | 4 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Propagation conditions |  | AWGN | AWGN | AWGN | AWGN |
| Antenna configuration |  | 1x2 | 1x2 | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that active cells are fully allocated, and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the subframes with transmitted PRS. |  |  |  |  |  |

Table A.17.9.3.2.2-3: PRS-RSRP OTA related test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |  |  |
| Assumption for UE beamsNote 5 |  | Rough |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15kHzNote 3 | -98 |  | Same as Test 1 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote 3 | -89 |  | Same as Test 1 |  |
| PRS ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | -2 | -10 | -2 | -10 |
| PRS_RPNote2 | dBm/SCS | -91 | -99 | -91 | -99 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot]BB Note 4 | dB | -2.41 | -12.12 | -2.41 | -12.12 |
| IoNote2 | dBm/380.16MHz Note3 | -51.61 |  | -51.61 |  |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: PRS_RP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 4: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 36.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 5: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation. |  |  |  |  |  |

##### A.17.9.3.2.3 Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1 if the reported PRS-RSRP is in the range shown in table A.17.9.3.2.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2.

Table A.17.9.3.2.3-1: PRS-RSRP absolute accuracy test requirement

|  | Test requirement Notes1,2,3 |
| --- | --- |
| Cell 1 | PRS_RP1 -δ +Gmin ≤ Reported RSRP(dBm) ≤ PRS_RP1 +δ +Gmax |
| Cell 2 | PRS_RP2 -δ +Gmin ≤ Reported RSRP(dBm) ≤ PRS_RP2 +δ +Gmax |
| NOTE 1:  PRS_RPn is the equivalent power received by an antenna with 0dBi gain at the centre of the quiet zone configured in the test for the cell n under consideration.NOTE 2:  δ is the RSRP absolute accuracy requirement from table 10.1.24.2.1-2, selected according to the Io used in the test.NOTE 3:  Gmin and Gmax are the minimum and maximum UE gain values from table B.2.1.6.1-1, selected according to the UE power class. |  |

### A.17.9.4 PRS-RSRPP Measurements

#### A.17.9.4.1 SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_INACTIVE state in FR2

##### A.17.9.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRPP measurement accuracy in RRC_INACTIVE state is within the specified limits. This test will verify the requirements in clauses 10.1A.19.2.

##### A.17.9.4.1.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.9.4.1.2-1. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.17.9.4.1.2-2 and TRS configuration for Cell 1 is defined in table A.17.9.4.1.2-2.

Table A.17.9.4.1.2-1: PRS-RSRPP supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1:   This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

Table A.17.9.4.1.2-2: PRS-RSRPP general test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Cell ID |  | 489 | 0 | 489 | 0 |
| SSB ARFCN |  | freq1 |  | freq1 |  |
| Duplex mode |  | TDD |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel | MHz | 400: NRB,c = 264 |  | 400: NRB,c = 264 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - | DLBWP.0.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - | ULBWP.0.1 | - |
| DRX cycle configuration | Ms | 640 |  |  |  |
| TRS configuration |  | TRS.2.1 TDD | - | TRS.2.1 TDD | - |
| TCI state |  | TCI.State.0 | - | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3.1 TDD | - | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.3 | OP.3 | OP.3 | OP.3 |
| SSB configuration |  | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 |
| SMTC configuration |  | SMTC.1 | SMTC.1 | SMTC.1 | SMTC.1 |
| Time offset with Cell 1 | s | - | 3 | - | 3 |
| PRS configuration |  | PRS.1.6 FR2 | PRS.1.6 FR2 | PRS.1.6 FR2 | PRS.1.6 FR2 |
| PRS Resource slot offset | slot | 0 | 4 | 0 | 4 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Propagation conditions |  | Two-tap channel  Note 2 |  |  |  |
| Antenna configuration |  | 1x2 |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The two-tap channel model is defined in 38.101-4 annex B.2.4 (a = 1, τd=0.45 µs and fD=5 Hz). |  |  |  |  |  |

TableA.17.9.4.1.2-3: PRS-RSRPP OTA related test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |  |  |
| Assumption for UE beamsNote 5 |  | Rough |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15kHzNote 3 | -98 |  | Same as Test 1 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote 3 | -89 |  | Same as Test 1 |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | -2 | -10 | -2 | -10 |
| PRS_RPNote2 | dBm/SCS | -91 | -99 | -91 | -99 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot]BB Note 4 | dB | -2.41 | -12.12 | -2.41 | -12.12 |
| IoNote2 | dBm/380.16MHzNote3 | -51.61 |  | -51.61 |  |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: PRS_RP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 4: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 36.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 5: Information about types of UE beam is given in annex B.2.1.3 and does not limit UE implementation or test system implementation. |  |  |  |  |  |

##### A.17.9.4.1.3 Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.19.2. if the reported PRS-RSRPP is in the range shown in table A.17.9.4.1.3-1.

Table A.17.9.4.1.3-1: PRS-RSRPP absolute accuracy test requirement

|  | Test requirement Notes1,2,3 |
| --- | --- |
| Cell 1 | PRS_RP1 -δ +Gmin ≤ Reported RSRPP(dBm) ≤ PRS_RP1 +δ +Gmax |
| Cell 2 | PRS_RP2 -δ +Gmin ≤ Reported RSRPP(dBm) ≤ PRS_RP2 +δ +Gmax |
| NOTE 1: PRS_RPn is the equivalent power received by an antenna with 0dBi gain at the centre of the quiet zone configured in the test for the cell n under consideration.NOTE 2: δ is the RSRPP absolute accuracy requirement from table 10.1A.19.2, selected according to the Io used in the test.NOTE 3: Gmin and Gmax are the minimum and maximum UE gain values from table B.2.1.6.1-1, selected according to the UE power class. |  |

#### A.17.9.4.2 SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_INACTIVE state in FR2

##### A.17.9.4.2.1 Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRPP measurement accuracy in RRC_INACTIVE state with FH by a RedCap UE is within the specified limits. This test will verify the requirements in clauses 10.1A.19.2.

##### A.17.9.4.2.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.9.4.2.2-1. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.17.9.4.2.2-1.

Table A.17.9.4.2.2-1: PRS-RSRPP supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, cell bandwidth 400 MHz, TDD duplex mode |
| NOTE 1:   This test case is applicable to the UE supporting per hop bandwidth = 100 MHz for SCS 120 kHz. |  |

Table A.17.9.4.2.2-2: PRS-RSRPP general test parameters

| Parameter | Unit | Cell 1 | Cell 2 |
| --- | --- | --- | --- |
| Cell ID |  | 489 | 0 |
| SSB ARFCN |  | freq1 |  |
| Duplex mode |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  |
| BWchannel | MHz | 400: NRB,c = 264 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - |
| DRX cycle configuration | ms | 640 |  |
| TRS configuration |  | TRS.2.1 TDD | - |
| TCI state |  | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.3 | OP.3 |
| SSB configuration |  | SSB.3 RedCap FR2 | SSB.3 RedCap FR2 |
| SMTC configuration |  | SMTC.1 | SMTC.1 |
| Time offset with Cell 1 | s | - | 3 |
| PRS configuration |  | PRS.1.6 FR2 | PRS.1.6 FR2 |
| PRS Resource slot offset | slot | 0 | 4 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation conditions |  | Two-tap channel  Note 2 |  |
| Antenna configuration |  | 1x2 |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The two-tap channel model is defined in TS 38.101-4 annex B.2.4 (a = 1, τd=0.45 µs and fD=5 Hz). |  |  |  |

Table A.17.9.4.2.2-3: PRS-RSRPP OTA related test parameters

| Parameter | Unit | Cell 1 | Cell 2 |
| --- | --- | --- | --- |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |
| Assumption for UE beamsNote 5 |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15kHzNote 3 | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote 3 | -89 |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | -2 | -10 |
| PRS_RPNote 2 | dBm/SCS | -91 | -99 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot]BB Note 4 | dB | -2.41 | -12.12 |
| IoNote 2 | dBm/380.16MHzNote3 | -51.16 |  |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: PRS_RP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 4: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 36.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 5: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation. |  |  |  |

##### A.17.9.4.2.3 Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.19.2, if the reported PRS-RSRPP is in the range shown in table A.17.9.4.2.3-1.

Table A.17.9.4.2.3-1: PRS-RSRPP absolute accuracy test requirement

|  | Test requirement Notes1,2,3 |
| --- | --- |
| Cell 1 | PRS_RP1 -δ +Gmin ≤ Reported RSRPP(dBm) ≤ PRS_RP1 +δ +Gmax |
| Cell 2 | PRS_RP2 -δ +Gmin ≤ Reported RSRPP(dBm) ≤ PRS_RP2 +δ +Gmax |
| NOTE 1: PRS_RPn is the equivalent power received by an antenna with 0dBi gain at the centre of the quiet zone configured in the test for the cell n under consideration.NOTE 2: δ is the RSRPP absolute accuracy requirement from table 10.1.38.2.1, selected according to the Io used in the test.NOTE 3: Gmin and Gmax are the minimum and maximum UE gain values from table B.2.1.6.1-1, selected according to the UE power class. |  |

## A.17.10 Measurement Procedure for RedCap in RRC_IDLE

### A.17.10.1 RSTD Measurements

#### A.17.10.1.1 NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA in RRC_IDLE state without eDRX

##### A.17.10.1.1.1 Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC IDLE state and without eDRX meets the requirements specified in clause 4.6.2.5 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.17.10.1.1.1-1.

Table A.17.10.1.1.1-1: Supported test configurations for NR RSTD

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layers.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell3. During T2 UE shall be in RRC_IDLE state and all cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the RedCap UE during T1. The measurement reporting delay test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The last TTI containing the two messages shall be provided to the RedCap UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s).

The UE is configured with DRX cycle of 0.64 s.

The general test parameters are listed in table A.17.10.1.1.1-2, and cell specific test parameters are listed in table A.17.10.1.1.1-3 and table A.17.10.1.1.1-4.

Table A.17.10.1.1.1-2: General test parameters for RSTD measurement reporting delay

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Reference cell |  |  | Cell 1 | Reference cell is the cell in the DL-TDOA assistance data with respect to which the RSTD measurement is defined, as specified in TS 38.215 [4] and TS 37.355 [34]. The reference cell is the PCell in this test case. |
| Neighbor cells |  |  | Cell 2 and Cell 3 | Cell 2 and Cell 3 appear at the first and second places in the neighbour cell list in the DL-TDOA assistance data. |
| BWchannel |  | MHz | 100: NRB,c = 66 |  |
| SSB configuration | Config 1 |  | SSB.2 FR2 |  |
| SMTC configuration | Config 1 |  | SMTC.1 |  |
| PDSCH RMC configuration | Config 1 |  | SR.1.1 FDD |  |
| RMSI CORESET RMC configuration | Config 1 |  | CR.3.1 TDD | As specified in clause A.3.1.2.1 |
| Dedicated CORESET RMC configuration | Config 1 |  | CR.1.1 FDD |  |
| PRS Configuration | Config 1 |  | PRS.1.5 FR2 | As specified in clause A.3. 31 |
| Physical cell ID PCI |  |  | (PCI of Cell 1 – PCI of Cell 2)mod6=0and(PCI of Cell 1 – PCI of Cell 3)mod6=0 | The cell PCIs are selected such that the relative shifts of PRS patterns among cells are as given by the test parameters |
| CP length |  |  | Normal |  |
| DRX |  | s | 0.64 |  |
| Radio frame receive time offset between the cells at the UE antenna connector |  | s | Cell 2 to Cell 1: 0Cell 3 to Cell 1: 3 | PRS are transmitted from synchronous cells |
| Expected RSTD |  | s | Cell 2: 3 Cell 3: 3Other neighbour cells: randomly between -3 and 3 | The expected RSTD is what is expected at the receiver. The corresponding parameter in the DL-TDOA assistance data specified in TS 37.355 [34] is the expectedRSTD indicator |
| Expected RSTD uncertainty for all neighbour cells |  | s | 5 | The corresponding parameter in the DL-TDOA assistance data specified in TS 37.355 [34] is the expectedRSTD-Uncertainty index |
| Number of cells provided in DL-TDOA assistance data |  |  | 3 | Including the reference cell |
| PRS muting info |  |  | Cell 1: ‘10’Cell 2: ‘01’Cell 3: ‘10’ | Correponds to prs-MutingInfo defined in TS 37.355 [34] |
| PRS resource RE offset |  |  | Cell 1: 0Cell 2: 0Cell 3: 1 | Cell 1 and Cell 3 are configured with different resource offsets |
| T1 |  | s | 3 | The length of the time interval from the beginning of each test |
| T2 |  | s | 1.28 | The length of the time interval that follows immediately after time interval T1 |
| AoA setup |  |  | Setup 1 | As defined in clause A.3.15.1 |
| Beam assumption |  |  | Rough | Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |

Table A.17.10.1.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

| Parameter |  | Unit | Cell 1 | Cell 2 | Cell 3 |
| --- | --- | --- | --- | --- | --- |
| NR RF Channel Number |  |  | 1 | 1 | 1 |
| Positiong frequency layer |  |  | 1 | 1 | 1 |
| Correlation Matrix and Antenna Configuration |  |  | 1x2 Low | 1x2 Low | 1x2 Low |
| OCNG patterns defined in A.3.2.1 |  |  | OP.5 FDD | N/A | N/A |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note 3 | Config 1 | dBm/SCS | -89 |  |  |
| PRS ![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] |  | dB | -Infinity | -Infinity | -Infinity |
| Io Note 4 | Config 1 | dBm/95.04MHz | -57 | -57 | -57 |
| SSB RP Note4 | Config 1 | dBm/SCS | -89 | -Infinity | -Infinity |
| ![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] |  | dB | 0 | -Infinity | -Infinity |
| Propagation Condition |  |  | AWGN |  |  |
| NOTE 1:  OCNG shall be used such that active cell (Cell 1) is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The resources for uplink transmission are assigned after the end of time period T2 to UEs that do not support SDT for measurement reporting.NOTE 3:  Interference from other cells and noise sources not specified in the test are assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 4: SSB RP and Io levels have been derived from other parameters and are given for information purpose. These are not settable test parameters. |  |  |  |  |  |

Table A.17.10.1.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

| Parameter |  | Unit | Cell 1 | Cell 2 | Cell 3 |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T2 | T2 | T2 |
| RF Channel Number |  |  | 1 | 1 | 1 |
| Positiong frequency layer |  |  | 1 | 1 | 1 |
| Correlation Matrix and Antenna Configuration |  |  | 1x2 Low | 1x2 Low | 1x2 Low |
| OCNG patterns defined in A.3.2.1 |  |  | OP.1 | OP.1 | OP.1 |
| PRACH configuration |  |  | FR2 PRACH configuration 1 | FR2 PRACH configuration 1 | FR2 PRACH configuration 1 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note 3 | Config 1 | dBm/SCS | -89 | -89 | -89 |
| PRS ![](media_svg/image30.svg) [公式≈: ^{E}^{ˆ}s^{/}^{N}oc] | Config 1 | dB | -5.44 | -11.67 | -11.67 |
| Io | Config 1 | dBm/95.04MHz | -58.49 | -58.49 | -58.49 |
| PRS ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | -6 | -13 | -13 |
| Propagation Condition |  |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that active cells (all, except Cell 3 in T2) are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols other than those in the slots with transmitted PRS.NOTE 2: The resources for uplink transmission are assigned after the end of time period T2 to UEs that do not support SDT for measurement reporting.NOTE 3: Interference from other cells and noise sources not specified in the test are assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled. |  |  |  |  |  |

##### A.17.10.1.1.2 Test Requirements

The RSTD measurement time without FH for RedCap fulfils the requirements specified in clause 4.6.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 4.6.2.5 starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD_1970049.

#### A.17.10.1.2 NR RSTD without FH measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_IDLE state with eDRX > 10.24s

##### A.17.10.1.2.1 Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 4.6.2.5 for RSTD measurements in RRC_IDLE with eDRX and periodic reporting. Refer to clause A.7.10.1.2.1 for test configuration and procedure.

##### A.17.10.1.2.2 Test requirements

The RSTD measurement time shall fulfill the requirements specified in clause 4.6.2.5.

The UE shall perform and report the RSTD measurements for Cell 1, Cell 2 and Cell 3 within the specified measurement period duration starting from the beginning of time interval T2. The requirement shall be evaluated based on the first measurement report received from the UE.

NOTE 1: The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3.

### A.17.10.2 PRS-RSRP Measurements

#### A.17.10.2.1 PRS-RSRP measurement delay test case for single positioning frequency layer in RRC_IDLE

##### A.17.10.2.1.1 Test Purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement without RX FH in RRC_IDLE in FR2 meets the delay requirements specified in clause 4.6.3.5 for single positioning frequency layer under AWGN propagation conditions in standalone scenario. Supported test configurations are shown in table A.17.10.2.1.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the DL slot next to slot #n, UE is released into RRC_IDLE. PRS RX FH is not requested in NR-DL-AoD-RequestLocationInformation.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is DT after slot #n, where DT = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.10.2.1.1-2 and table A.17.10.2.1.1-3.

Table A.17.10.2.1.1-1: Supported test configurations for PRS-RSRP measurement reporting delay

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.10.2.1.1-2: General test parameters for PRS-RSRP measurement reporting delay

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | 1: Cell 1 and Cell 2 | One TDD carrier frequency is used for the NR cells. |
| Active cell |  | 1 | NR cell 1 (Pcell) | Cell 1 is the PCell and the DL-AoD reference cell in the positioning assistance data. |
| Neighbour cell |  | 1 | NR cell 2 | Cell 2 is a neighbour cell in the positioning assistance data. |
| Gap Pattern Id |  | 1 | GP#13 or GP#24Note1 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | 1 | 39 |  |
| SMTC parameters |  | 1 | SMTC.1 RedCap | As specified in clause A.3.11A |
| SSB parameters |  | 1 | SSB.3 FR2 | As specified in clause A.3.10.2 |
| A3-Offset | dB | 1 | -6 |  |
| Hysteresis | dB | 1 | 0 |  |
| CP length |  | 1 | Normal |  |
| TimeToTrigger | s | 1 | 0 |  |
| Filter coefficient |  | 1 | 0 | L3 filtering is not used |
| DRX |  | 1 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | 1 | 3ms | Synchronous cells. |
| Expected RSTD | ms | 1 | 3 |  |
| Expected RSTD uncertainty | ms | 1 | 5 |  |
| T1 | s | 1 | 5 |  |
| T2 | s | 1 | 41 |  |
| NOTE 1: GP#24 is configured if UE supports MG#24, otherwise GP#13 is configured. |  |  |  |  |

Table A.17.10.2.1.1-3: Cell-specific test parameters for PRS-RSRP measurement reporting delay

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  |  | 1 | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 7 |  |  | 1 | Rough |  | Rough |  |
| TDD configuration |  |  | 1 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| Duplex mode |  |  | 1 | TDD |  | TDD |  |
| BWchannel |  | MHz | 1 | 100: NRB,c = 66 |  | 100: NRB,c = 66 |  |
| BWP configuration | Initial DL BWP |  | 1 | DLBWP.0.1 |  | N/A |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | N/A |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | N/A |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | N/A |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | 1 | SR.3.1 TDD |  | - |  |
| CORESET Reference Channel |  |  | 1 | CR.3.1 TDD |  | - |  |
| Dedicated CORESET RMC configuration |  |  | 1 | CCR.3.1 TDD |  | - |  |
| TRS configuration |  |  | 1 | TRS.2.1 TDD |  | - |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 1 | 120 |  | 120 |  |
| PRS configuration |  |  | 1 | PRS.1.1 FR2 |  | PRS.1.1 FR2 |  |
| PRS muting configuration |  |  | 1 | ‘10’ |  | ‘01’ |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | 1 | 0 |  | 0 |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15kHz Note5 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS Note4 | 1 | -89 |  | -89 |  |
| SSB_RP Note 3 |  | dBm/SCS Note5 | 1 | -91 | -91 | -Infinity | -99 |
| PRP Note 3 |  | dBm/SCS Note5 | 1 | -Infinity | -91 | -Infinity | -99 |
| PRS |  | dB | 1 | -Infinity | -2.41 | -Infinity | -12.12 |
| PRS |  | dB | 1 | -Infinity | -2 | -Infinity | -10 |
| SSB |  | dB | 1 | -2 | -2 | -Infinity | -10 |
| IoNote3 |  | dBm/95.04 MHz Note5 | 1 | -57.89 | -57.63 | -57.89 | -57.63 |
| Propagation Condition |  |  | 1 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SSB_RP/PRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: PRS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 6: As observed with 0 dBi gain antenna at the centre of the quiet zone.NOTE 7: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 8: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4. |  |  |  |  |  |  |  |

##### A.17.10.2.1.2 Test Requirements

The PRS-RSRP measurement time fulfils the requirements specified in clause 4.6.3.5. The UE shall perform and report the PRS-RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 4.6.3.5 starting from the beginning of time interval T2.

NOTE: The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS-RSRP measurement for each correct event shall be within the PRS-RSRP reporting range specified in clause10.1.24.3, i.e., between PRS-RSRP_0 and PRS-RSRP_126.

#### A.17.10.2.2 PRS-RSRP reporting delay test case in RRC_IDLE state in FR2 when eDRX cycle > 10.24s

##### A.17.10.2.2.1 Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements specified in clause 4.6.3.5 for single positioning frequency layer under AWGN propagation conditions in RRC_IDLE when configured with eDRX.

The supported test configurations in table A.17.8.3.3.1-1 apply for this test.

The test procedure in clause A.17.8.3.3.1 apply for this test, except that during T2, UE is in RRC_IDLE state.

The general test parameters as specified in table A.17.8.3.3.1-2 apply for this test, except those specified in table A.17.10.2.2.1-1.

The cell specific test parameters as specified in table A.17.8.3.3.1-3 apply for this test.

Table A.17.10.2.2.1-1: General test parameters for PRS RSRP measurement reporting delay

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| CN eDRX configuration |  | Config 1 | eDRX cycle = 40.96sPTW length = 1.28s |  |

##### A.17.10.2.2.2 Test Requirements

The test requirements in clause A.17.8.3.3.2 apply for this test, except that the time limits are specified in clause 4.6.3.5.

## A.17.11  Measurement Performance Requirements for RedCap in RRC_IDLE

### A.17.11.1 RSTD Measurements

#### A.17.11.1.1 RSTD measurement accuracy test case for RedCap UE without FH in FR2 in RRC_IDLE state without eDRX

##### A.17.11.1.1.1 Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC_IDLE state and without eDRX meets the accuracy requirements specified in clause 10.1A.16.2 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.17.11.1.1.1-1.

Table A.17.11.1.1.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2. The UE is configured with DRX cycle of 0.64 s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the RedCap UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 4.6.2.5.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The accuracy test parameters and OTA related test parameters are as given in table A.17.11.1.1.1-2 and table A.17.11.1.1.1-3, respectively.

Table A.17.11.1.1.1-2: RSTD accuracy test parameters

| Parameter | Unit | Test 1 |  |
| --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 |
| PRS ARFCN |  | freq1 |  |
| Duplex mode |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  |
| BWchannel | MHz | 100: NRB,c = 66 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - |
| Uplink dedicated BWP configuration |  | ULBWP.1.1 | - |
| TRS configuration |  | TRS.2.1 TDD | - |
| TCI state |  | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.3 | OP.3 |
| SSB configuration |  | SSB.3 FR2 | SSB.3 FR2 |
| SMTC configuration |  | SMTC.1 | SMTC.1 |
| PRS configuration |  | PRS.1.1 FR2 | PRS.1.1 FR2 |
| PRS Resource slot offset | slot | 0 | 4 |
| Expected RSTD | s | N/A | 3 |
| Expected RSTD uncertainty | s | N/A | 5 |
| Time offset with Cell 1 | s | - | 3 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation conditions |  | AWGN | AWGN |
| Antenna configuration |  | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated, and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |

Table A.17.11.1.1.1-3: RSTD accuracy OTA related test parameters

| Parameter | Unit | Test 1 |  |
| --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |
| Assumption for UE beamsNote 5 |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote3 | -89 |  |
| PRS | dB | -5.7 | -11.9 |
| PRS-RSRPNote2 | dBm/SCS | -94.7 | -100.9 |
| PRS BB Note4 | dB | -6 | -13 |
| IoNote2 | dBm/95.04 MHz Note3 | -58.76 | -58.76 |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: SSB_RP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 4: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 36.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 5: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation. |  |  |  |

##### 11.1.1.2 Test Requirements

The RSTD measurement accuracy shall fulfil the absolute requirement in clause 10.1A.16.2.

#### A.17.11.1.2 RSTD without FH measurement accuracy test case for single positioning frequency layer in FR2 SA in RRC_IDLE state with eDRX > 10.24s

##### A.17.11.1.2.1 Test purpose and environment

The purpose of this test is to verify that RSTD measurements performed in RRC_IDLE with eDRX and periodic reporting satisfy the measurement accuracy requirements specified in clause 10.1A.16.2. The tests are conducted under AWGN propagation condition with the UE operating in FR2 stand-alone mode and configured to perform RSTD measurements on a single positioning frequency layer (PFL) in FR2.

The supported test configurations are listed in table A.17.11.1.2.1-1.

Table A.17.11.1.2.1-1: Supported test configurations

| PCell configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

There are two synchronous cells in the test: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2.

The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 4.5.2.5.

The general test parameters and cell specific test parameters are as given in table A.17.11.1.2.1-2 and table A.17.11.1.2.1-3, respectively.

Table A.17.11.1.2.1-2: General test parameters

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Reference cell |  | 1 | Cell 1 |  |
| Neighbour cell |  | 1 | Cell 2 |  |
| RF Channel Number |  | 1 | 1 | For Cell 1 and Cell 2 |
| BWchannel | MHz | 1 | 100: NRB,c = 66 |  |
| SSB configuration |  | 1 | SSB.3 FR2 |  |
| SMTC configuration |  | 1 | SMTC.1 |  |
| CP length |  | 1 | Normal |  |
| DRX | s | 1 | 0.64 |  |
| eDRX cycle length | s | 1 | 40.96 |  |
| PTW length | s | 1 | 1.28 |  |
| Reporting periodicity | s | 1 | 20 | reportingInterval for periodic reporting defined in TS 37.355 [34]. |
| Time offset between serving and neighbour cell | s | 1 | 3 | Synchronous cells |
| Expected RSTD | s | 1 | 3 |  |
| Expected RSTD uncertainty | s | 1 | 5 |  |

Table A.17.11.1.2.1-3: Cell specific test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| AoA setup |  | Setup 1 as specified in clause A.3.15 |  |  |  |
| Beam AssumptionNote 4 |  | Rough |  | Rough |  |
| TDD configuration |  | TDDConf.3.1 |  | TDDConf.3.1 |  |
| PDSCH RMC configuration |  | SR.3.1 TDD | - | SR.3.1 TDD | - |
| RMSI CORESET RMC configuration |  | CR.3.1 TDD | - | CR.3.1 TDD | - |
| Dedicated CORESET RMC configuration |  | CR.3.1 TDD | - | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.1 | OP.1 | OP.1 | OP.1 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| TRS configuration |  | TRS.2.1 TDD | - | TRS.2.1 TDD | - |
| Initial BWP configuration |  | DLBWP.0.1ULBWP.0.1 | - | DLBWP.0.1ULBWP.0.1 | - |
| Dedicated BWP configuration |  | DLBWP.1.1ULBWP.1.1 | - | DLBWP.1.1ULBWP.1.1 | - |
| PRS configuration |  | PRS.1.1 FR2 | PRS.1.1FR2 | PRS.1.2 FR2 | PRS.1.2 FR2 |
| PRS num PRB |  | 32 | 32 | 64 | 64 |
| PRS Resource slot offset | slot | 0 | 4 | 0 | 4 |
| Note 2 | dBm/SCS | -89 |  |  |  |
| PRS | dB | -6 | -13 | -6 | -13 |
| PRS | dB | -6 | -13 | -6 | -13 |
| PRP Note 3 | dBm/SCS kHz | -95 | -102 | -95 | -102 |
| Io Note 3 (on symbols where PRS is not allocated) | dBm/95.04 MHz | -58.7 | -58.7 | -58.7 | -58.7 |
| Propagation conditions |  | AWGN |  |  |  |
| Antenna configuration |  | 1x2 | 1x2 | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that active cell (Cell 1) is fully allocated and a constant total transmitted power spectral density is achieved on all OFDM symbols except those in which PRS is allocated. NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: PRP and Io levels have been derived from other parameters and they are provided for information only. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation.NOTE 5: Calculation of Es/Iot includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 6: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 7: As observed with 0 dBi gain antenna at the centre of the quiet zone. |  |  |  |  |  |

##### A.17.11.1.2.2 Test requirements

The reported RSTD measurements shall fulfill the absolute accuracy requirements specified in clause 10.1A.16.2.

### A.17.11.2 PRS-RSRP Measurements

#### A.17.11.2.1 PRS-RSRP measurement accuracy test case for RedCap UE in FR2 in RRC_IDLE state

##### A.17.11.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRP measurement accuracy for 2Rx RedCap UE in RRC_IDLE is within the specified limits in FR2. This test will verify the requirements in clauses 10.1A.17.2.1 and 10.1A.17.2.2, when the PRS-RSRP measurement is performed without RX FH.

##### A.17.11.2.1.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.11.2.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in table A.17.11.2.1.2-2 and A.17.11.2.1.2-3. In all test cases, Cell 1 is the PCell.

Table A.17.11.2.1.2-1: PRS-RSRP supported test configurations

| Config | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |

Table A.17.11.2.1.2-2: PRS-RSRP general test parameters.

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Cell ID |  | 489 | 0 | 489 | 0 |
| SSB ARFCN |  | freq1 |  | freq1 |  |
| Duplex mode |  | TDD |  | TDD |  |
| TDD configuration |  | TDDConf.3.1 |  | TDDConf.3.1 |  |
| BWchannel | MHz | 100: NRB,c = 66 |  | 100: NRB,c = 66 |  |
| Downlink initial BWP configuration |  | DLBWP.0.1 | - | DLBWP.0.1 | - |
| Uplink initial BWP configuration |  | ULBWP.0.1 | - | ULBWP.0.1 | - |
| DRX cycle configuration |  | 1.28s | - | 1.28s | - |
| TCI state |  | TCI.State.0 | - | TCI.State.0 | - |
| PDSCH Reference measurement channel |  | SR.3.1 TDD | - | SR.3.1 TDD | - |
| RMSI CORESET Reference Channel |  | CR.3.1 TDD | - | CR.3.1 TDD | - |
| Control channel RMC |  | CCR.3.1 TDD | - | CCR.3.1 TDD | - |
| OCNG Patterns |  | OP.1 | OP.1 | OP.1 | OP.1 |
| SSB configuration |  | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 |
| SMTC configuration |  | SMTC.1 RedCap | SMTC.1RedCap | SMTC.1RedCap | SMTC.1RedCap |
| Time offset with Cell 1 | s | - | 3 | - | 3 |
| PRS configuration |  | PRS.1.3 FR2 | PRS.1.3 FR2 | PRS.1.5 FR2 | PRS.1.5 FR2 |
| PRS Resource slot offset | slot | 0 | 4 | 0 | 4 |
| PDSCH/PDCCH subcarrier spacing | kHz | 120 | 120 | 120 | 120 |
| EPRE ratio of PSS to SSS | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Propagation conditions |  | AWGN | AWGN | AWGN | AWGN |
| Antenna configuration |  | 1x2 | 1x2 | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |  |  |

Table A.17.11.2.1.2-3: PRS-RSRP OTA related test parameters

| Parameter | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |  |  |
| Assumption for UE beamsNote 6 |  | Rough |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15kHzNote3 | -98 |  | Same as Test 1 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote3 | -89 |  | Same as Test 1 |  |
| $\frac {\hat  {E}_{s}}{N_{oc}}$ | dB | -2 | -10 | -2 | -10 |
| Es | dBm/SCSNote3 | - | - | - | - |
| PRS_RPNote2 | dBm/SCS | -91 | -99 | -91 | -99 |
| $\frac {\hat  {E}_{s}}{I_{ot}}$ BB Note5 | dB | -2.41 | -12.12 | -2.41 | -12.12 |
| IoNote2 | dBm/95.04 MHz Note3 | -57.63 |  | -57.63 |  |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: PRS_RP, Es/Iot and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone.NOTE 5: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 36.101-2 [19], and an allowance of 1dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] table 6.2.1.3-4.NOTE 6: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation. |  |  |  |  |  |

A.17.11.2.1.3 Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1 when the PRS-RSRP measurement is performed without RX FH and if the reported PRS-RSRP is in the range shown in table A.17.11.2.1.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2 when the PRS-RSRP measurement is performed without RX FH.

Table A.17.11.2.1.3-1: PRS-RSRP absolute accuracy test requirement

|  | Test requirement Notes1,2,3 |
| --- | --- |
| Cell 1 | PRS_RP1 -δ +Gmin ≤ Reported RSRP(dBm) ≤ PRS_RP1 +δ +Gmax |
| Cell 2 | PRS_RP2 -δ +Gmin ≤ Reported RSRP(dBm) ≤ PRS_RP2 +δ +Gmax |
| NOTE 1:  PRS_RPn is the equivalent power received by an antenna with 0dBi gain at the centre of the quiet zone configured in the test for the cell n under consideration.NOTE 2:  δ is the RSRP absolute accuracy requirement from table 10.1.24.2.1-2, selected according to the Io used in the test.NOTE 3:  Gmin and Gmax are the minimum and maximum UE gain values from table B.2.1.6.1-1, selected according to the UE power class. |  |

#### A.17.11.2.2 PRS-RSRP measurement accuracy test case in RRC_IDLE state in FR2 when eDRX cycle > 10.24s

##### A.17.11.2.2.1 Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement in RRC_IDLE with eDRX meets the accuracy requirements specified in clause10.1A.17.2.1 and 10.1A.17.2.2 in an environment with AWGN propagation conditions.

##### A.17.11.2.2.1 Test parameters

The supported test configurations in table A.17.9.3.1.2-1 apply for this test.

The test procedure in clause A.17.9.3.1.2 apply for this test, except that UE is in RRC_IDLE state.

The general test parameters as specified in table A.17.9.3.1.2-2 apply for this test, except those additionally specified in table A.17.11.2.2.1-1.

The OTA related test parameters in table A.17.9.3.1.2-3 apply for this test.

Table A.17.11.2.2.1-1: PRS-RSRP test parameters

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| eDRX cycle length (for CN eDRX) | s | 1, 2, 3 | 40.96 |  |
| PTW window length | s | 1, 2, 3 | 1.28 |  |

##### A.17.11.2.2.2 Test Requirements

The test requirements in clause A.17.9.3.1.3 apply for this test.

# A.18 E-UTRA standalone tests for NR RRM for RedCap

## A.18.1 RRC_IDLE state mobility

### A.18.1.1 Inter-RAT NR Cell re-selection

#### A.18.1.1.1 E-UTRA Cell reselection to higher priority NR target Cell in FR1

##### A.18.1.1.1.1 Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN to NR inter-RAT cell reselection requirements for 2Rx RedCap specified in clause 4.2.2.5.8 in TS 36.133 [15].

The test scenario comprises of 1 E-UTRA cell and 1 NR cell as given in tables A.18.1.1.1.1-1, A.18.1.1.1.1-2, A.18.1.1.1.1-3 and A.18.1.1.1.1-4. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. E-UTRA Cell 1 is already identified by the UE prior to the start of the test. Cell 2 is of higher priority than Cell 1.

Table A.18.1.1.1.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | LTE FDD, NR 30 kHz SSB SCS, 20 MHz bandwidth, TDD duplex mode |
| 4 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 5 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 6 | LTE TDD, NR 30 kHz SSB SCS, 20 MHz bandwidth, TDD duplex mode |
| 7 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, HD-FDD duplex mode |
| 8 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, HD-FDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.18.1.1.1.1-2: General test parameters for E-UTRA cell re-selection FR1 NR cell test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2, 3, 4, 5, 6, 7, 8 | Cell 2 | The UE camps on Cell 2 in the initial phase |
|  | Neighbour cell |  | 1, 2, 3, 4, 5, 6, 7, 8 | Cell 1 |  |
| T1 end condition | Active cell |  |  | Cell 1 | During T1 period the UE reselects to Cell 1 |
|  | Neighbour cell |  |  | Cell 2 |  |
| T3 end condition | Active cell |  | 1, 2, 3, 4, 5, 6, 7, 8 | Cell 2 | The UE shall perform reselection to Cell 2 during T3 |
|  | Neighbour cell |  | 1, 2, 3, 4, 5, 6, 7, 8 | Cell 1 |  |
| RF Channel Number |  |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1, 2 | E-UTRAN radio channel (1) and NR radio channel (2) are used for this test |
| Time offset between cells |  |  | 1, 4, 7, 8 | 3 ms | Asynchronous cells |
|  |  |  | 2, 5 | 3 s | Synchronous cells |
|  |  |  | 3, 6 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1, 2, 3, 4, 5, 6, 7, 8 | Not Sent | No additional delays in random access procedure. |
| DRX cycle length |  | s | 1, 2, 3, 4, 5, 6, 7, 8 | 1.28 | The value shall be used for all cells in the test. |
| NR PRACH configuration index |  |  | 1, 2, 3, 4, 5, 6, 7, 8 | 102 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| T1 |  | s | 1, 2, 3, 4, 5, 6, 7, 8 | 15 | T1 needs to be defined so that cell re-selection reaction time is taken into account. |
| T2 |  | s | 1, 2, 3, 4, 5, 6, 7, 8 | >7 | During T2, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed. The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T3. |
| T3 |  | s | 1, 2, 3, 4, 5, 6, 7, 8 | 75 | T3 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.18.1.1.1.1-3: Cell specific test parameters for NR Cell 2

| Parameter | Unit | Test configuration | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| TDD configuration |  | 1, 4, 7, 8 | N/A |  |  |
|  |  | 2, 5 | TDDConf.1.1 |  |  |
|  |  | 3, 6 | TDDConf.2.1 |  |  |
| PDSCH Reference measurement channel |  | 1, 4, 7, 8 | SR.1.1 FDD |  |  |
|  |  | 2, 5 | SR.1.1 TDD |  |  |
|  |  | 3, 6 | SR.2.1 TDD |  |  |
| RMSI CORESET Reference Channel |  | 1, 4, 7, 8 | CR.1.1 FDD |  |  |
|  |  | 2, 5 | CR.1.1 TDD |  |  |
|  |  | 3, 6 | CR.2.1 TDD |  |  |
| RMC CORESET Reference Channel |  | 1, 4, 7, 8 | CCR.1.1 FDD |  |  |
|  |  | 2, 5 | CCR.1.1 TDD |  |  |
|  |  | 3, 6 | CCR.2.1 TDD |  |  |
| OCNG Patterns |  | 1, 2, 3, 4, 5, 6, 7, 8 | OP.1 |  |  |
| SMTC configuration |  | 1, 2, 3, 4, 5, 6, 7, 8 | SMTC.1 |  |  |
| SSB configuration |  | 1, 4, 7, 8 | SSB.1 FR1 |  |  |
|  |  | 2, 5 | SSB.1 FR1 |  |  |
|  |  | 3, 6 | SSB.1 RedCap FR1 |  |  |
| Initial DL BWP configuration |  | 1, 2, 3, 4, 5, 6, 7, 8 | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2, 3, 4, 5, 6, 7, 8 | ULBWP.0.1 |  |  |
| RLM-RS |  | 1, 2, 3, 4, 5, 6, 7, 8 | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1, 2, 4, 5, 7, 8 | -140 |  |  |
|  |  | 3, 6 | -137 |  |  |
| Pcompensation | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |  |
| Qhysts | dB | 1, 2, 3, 4, 5, 6 | 0 |  |  |
| Qoffsets, n | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2, 3, 4, 5, 6, 7, 8 | SS-RSRP |  |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 4, 7, 8 | -4 | -infinity | 12 |
|  |  | 2, 5 |  |  |  |
|  |  | 3, 6 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1, 4, 7, 8 | -98 |  |  |
|  |  | 2, 5 | -98 |  |  |
|  |  | 3, 6 | -95 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 4, 7, 8 | -98 |  |  |
|  |  | 2, 5 |  |  |  |
|  |  | 3, 6 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 4, 7, 8 | -4 | -infinity | 12 |
|  |  | 2, 5 |  |  |  |
|  |  | 3, 6 |  |  |  |
| SS-RSRP Note3 | dBm/SCS | 1, 4, 7, 8 | -102 | -infinity | -86 |
|  |  | 2, 5 | -102 | -infinity | -86 |
|  |  | 3, 6 | -99 | -infinity | -83 |
| Io | dBm/9.36 MHz | 1, 4, 7, 8 | -68.60 | -70.05 | -57.78 |
|  | dBm/9.36 MHz | 2, 5 | -68.60 | -70.05 | -57.78 |
|  | dBm/18.36 MHz | 3, 6 | -65.67 | -67.12 | -54.86 |
| Treselection | s | 1, 2, 3, 4, 5, 6, 7, 8 | 0 | 0 | 0 |
| SnonintrasearchP | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 50 |  |  |
| Threshx, highP | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 48 |  |  |
| Threshserving, lowP | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 44 |  |  |
| Threshx, lowP | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 50 |  |  |
| Propagation Condition |  | 1, 2, 3, 4, 5, 6, 7, 8 | AWGN |  |  |
| Antenna Configuration |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1x2 |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |

Table A.18.1.1.1.1-4: Cell specific test parameters for E-UTRA Cell 1

| Parameter | Unit | Cell 1 |  |  |
| --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 |
| E-UTRA RF Channel number |  | 1 |  |  |
| BWchannel | MHz | 10 |  |  |
| OCNG Patterns defined in TS 36.133 [15] clause A.3.2 |  | OP.2 FDD for test configuration 1, 2, 3, 7;OP.2 TDD for test configuration 4, 5, 6, 8 |  |  |
| PBCH_RA | dB | 0 |  |  |
| PBCH_RB | dB |  |  |  |
| PSS_RA | dB |  |  |  |
| SSS_RA | dB |  |  |  |
| PCFICH_RB | dB |  |  |  |
| PHICH_RA | dB |  |  |  |
| PHICH_RB | dB |  |  |  |
| PDCCH_RA | dB |  |  |  |
| PDCCH_RB | dB |  |  |  |
| PDSCH_RA | dB |  |  |  |
| PDSCH_RB | dB |  |  |  |
| OCNG_RANote 1 | dB |  |  |  |
| OCNG_RBNote 1 | dB |  |  |  |
| Qrxlevmin | dBm | -140 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note 2 | dBm/15 kHz | -98 |  |  |
| RSRP Note 3 | dBm/15 KHz | -84 | -84 | -84 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 14 | 14 | 14 |
| ![](media_svg/image31.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 14 | 14 | 14 |
| TreselectionEUTRAN | S | 0 |  |  |
| SnonintrasearchP | dB | 50 |  |  |
| Threshx, highP | dB | 48 |  |  |
| Threshserving, lowP | dB | 44 |  |  |
| Threshx, lowP | dB | 50 |  |  |
| Propagation Condition |  | AWGN |  |  |
| Antenna Configuration |  | 1x2 |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |

##### A.18.1.1.1.2 Test Requirements

The cell reselection delay to a higher priority NR cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 2 and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, NR + TSI-NR,

Where:

Thigher_priority_search See clause 4.2.2 in TS 36.133[15]

Tevaluate, NR See Table 4.2.2.5.6-1 in clause 4.2.2.5.6 in TS 36.133[15]

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority NR cell and 7.68 s for the cell re-selection delay to a lower priority cell in the test case, which we allow 8 s.

## A.18.2 RRC_CONNECTED state mobility

### A.18.2.1 Handover

#### A.18.2.1.1 E-UTRAN - NR handover in FR1

##### A.18.2.1.1.1 Test Purpose and Environment

This test shall verify the E-UTRAN to NR FR1 handover requirements for 2RX RedCap as specified in clause 5.3.4B in TS 36.133 [15].

The test comprises of one E-UTRA carrier and one NR carrier. There are two cells and one cell on each carrier. Cell 1 is the E-UTRAN and Cell 2 is an inter-RAT NR neighbour cell. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in table 8.1.2.1-1 of TS 36.133 [15] is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2 after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.18.2.1.1-1. General test parameters are provided in table A.18.2.1.1-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.18.2.1.1-3 and A.18.2.1.1-4 respectively.

Table A.18.2.1.1-1: Supported test configurations for E-UTRAN inter-RAT NR handover

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | LTE FDD, NR 30 kHz SSB SCS, 20 MHz bandwidth, TDD duplex mode |
| 4 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, HD-FDD duplex mode |
| 5 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 6 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 7 | LTE TDD, NR 30 kHz SSB SCS, 20 MHz bandwidth, TDD duplex mode |
| 8 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, HD-FDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.18.2.1.1-2: General test parameters for E-UTRAN inter-RAT NR handover

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  |  | 1 | 1 NR carrier frequency is used in the test |
| LTE RF Channel Number |  |  | 2 | 1 E-UTRAN carrier frequency is used in the test |
| Initial conditions | Active cell |  | Cell 1 | E-UTRAN cell |
|  | Neighbouring cell |  | Cell 2 | NR cell |
| Final condition | Active cell |  | Cell 2 |  |
| NR measurement quantity |  |  | SS-RSRP |  |
| E-UTRAN measurement quantity |  |  | RSRP |  |
| b2-Threshold1 |  | dBm | -83 | Absolute E-UTRAN RSRP threshold for event B2 |
| b2-Threshold2NR |  | dBm | As specified in table A.18.2.1.1-4 | Absolute NR SS-RSRP threshold for event B2 |
| Hysteresis |  | dB | 0 |  |
| TimeToTrigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| DRX |  |  | OFF | Non-DRX test |
| Access Barring Information |  | - | Not sent | No additional delays in random access procedure |
| Time offset between cells |  |  | 3 ms | Asynchronous cells |
| Gap pattern configuration Id |  |  | 0 | As specified in table 8.1.2.1-1 started before T2 starts [15] |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |
| T3 |  | s | 1 |  |

Table A.18.2.1.1-3: Cell specific test parameters for E-UTRAN inter-RAT NR handover (Cell 1)

| Parameter | Unit | Configuration | Cell 1 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| RF channel number |  | 1, 2, 3, 4, 5, 6,7,8 | 2 |  |  |
| Duplex mode |  | 1, 2, 3,4 | FDD |  |  |
|  |  | 5, 6,7, 8 | TDD |  |  |
| TDD special subframe configurationNote1 |  | 5, 6,7, 8 | 6 |  |  |
| TDD uplink-downlink configurationNote1 |  | 5, 6,7, 8 | 1 |  |  |
| BWchannel | MHz | 1, 2, 3, 4, 5, 6, 7, 8 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |  |
| PRACH ConfigurationNote2 |  | 1, 2, 3,4 | 4 |  |  |
|  |  | 5, 6,7, 8 | 53 |  |  |
| PDSCH parameters:DL Reference Measurement ChannelNote3 |  | 1, 2, 3,4 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |  |
|  |  | 5, 6,7, 8 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote3 |  | 1, 2, 3,4 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |  |
|  |  | 5, 6,7, 8 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |  |
| OCNG PatternsNote3 |  | 1, 2, 3,4 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |  |
|  |  | 5, 6,7, 8 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |  |
| PBCH_RA | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |  |
| PBCH_RB |  |  |  |  |  |
| PSS_RA |  |  |  |  |  |
| SSS_RA |  |  |  |  |  |
| PCFICH_RB |  |  |  |  |  |
| PHICH_RA |  |  |  |  |  |
| PHICH_RB |  |  |  |  |  |
| PDCCH_RA |  |  |  |  |  |
| PDCCH_RB |  |  |  |  |  |
| PDSCH_RA |  |  |  |  |  |
| PDSCH_RB |  |  |  |  |  |
| OCNG_RANote4 |  |  |  |  |  |
| OCNG_RBNote4 |  |  |  |  |  |
| NocNote5 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -98 |  |  |
| Ês/Noc | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 7 | 7 | 7 |
| Ês/IotNote6 | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 7 | 7 | 7 |
| RSRPNote6 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -91 | -91 | -91 |
| SCH_RPNote6 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -91 | -91 | -91 |
| IoNote6 | dBm/9 MHz | 1, 2, 3, 4, 5, 6, 7, 8 | -62.43 | -62.43 | -62.43 |
| Propagation Condition |  | 1, 2, 3, 4, 5, 6, 7, 8 | AWGN |  |  |
| Antenna Configuration and Correlation Matrix Note7 |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1x2 Low |  |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: PRACH configurations are specified in table 5.7.1-2 and table 5.7.1-3 in TS 36.211 [23].NOTE 3: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 4: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 5: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 6: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 7: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |  |

Table A.18.2.1.1-4: Cell specific test parameters E-UTRAN inter-RAT NR handover (Cell 2)

| Parameter |  | Unit | Configuration | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 |
| RF channel number |  |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 |  |  |
| Duplex mode |  |  | 1, 5 | FDD |  |  |
|  |  |  | 2, 3, 6, 7 | TDD |  |  |
|  |  |  | 4,8 | HD-FDD |  |  |
| TDD Configuration |  |  | 2, 6 | TDDConf.1.1 |  |  |
|  |  |  | 3, 7 | TDDConf.2.1 |  |  |
| BWchannel |  | MHz | 1, 4,5,8 | 10: NPRB,c = 52 (FDD) |  |  |
|  |  |  | 2, 6 | 10: NPRB,c = 52 (TDD) |  |  |
|  |  |  | 3, 7 | 20: NPRB,c = 51 (TDD) |  |  |
| PDSCH reference measurement channel |  |  | 1, 4,5,8 | SR.1.1 FDD |  |  |
|  |  |  | 2, 6 | SR.1.1 TDD |  |  |
|  |  |  | 3, 7 | SR.2.1 TDD |  |  |
| CORSET reference channel |  |  | 1, 4,5,8 | CR.1.1 FDD |  |  |
|  |  |  | 2, 6 | CR.1.1 TDD |  |  |
|  |  |  | 3, 7 | CR.2.1 TDD |  |  |
| PRACH configuration |  |  | 1, 2, 3, 4, 5, 6, 7, 8 | FR1 PRACH configuration 1 |  |  |
| OCNG patternNote1 |  |  | 1, 2, 3, 4, 5, 6, 7, 8 | OP.1 |  |  |
| BWP | Initial DL BWP |  | 1, 2, 3, 4, 5, 6, 7, 8 | DLBWP.0.1 |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |
| SMTC configuration |  |  | 1, 2, 3, 4, 5, 6, 7, 8 | SMTC.2 |  |  |
| SSB configuration |  |  | 1,2,4,5,6,8 | SSB.4 RedCap FR1 |  |  |
|  |  |  | 3,7 | SSB.2 RedCap FR1 |  |  |
| b2-Threshold2NR |  | dBm | 1,2,4,5,6,8 | -106 |  |  |
|  |  |  | 3,7 | -103 |  |  |
| EPRE ratio of PSS to SSS |  | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  |  |  |  |  |
| NocNote2 |  | dBm/15 KHz | 1, 2, 3, 4, 5, 6, 7, 8 | -98 |  |  |
| NocNote2 |  | dBm/SCS | 1,2,4,5,6,8 | -98 |  |  |
|  |  |  | 3,7 | -95 |  |  |
| Ês/Noc |  | dB | 1, 2, 3, 4, 5, 6, 7, 8 | -inifinity | 0 | 0 |
| Ês/IotNote3 |  | dB | 1, 2, 3, 4, 5, 6, 7, 8 | -inifinity | 0 | 0 |
| SS-RSRPNote3 |  | dBm/SCS | 1, 2, 4, 5, 6,8 | -inifinity | -98 | -98 |
|  |  |  | 3, 7 | -inifinity | -95 | -95 |
| IoNote3 |  | dBm/9.36 MHz | 1, 2, 4, 5, 6,8 | -70.05 | -67.04 | -67.04 |
|  |  | dBm/18.36 MHz | 3, 7 | -67.13 | -60.94 | -64.12 |
| Propagation condition |  |  | 1, 2, 3, 4, 5, 6, 7, 8 | AWGN |  |  |
| Antenna Configuration and Correlation Matrix |  |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1x2 Low |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: Ês/Iot, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.18.2.1.1.2 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 112 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and is specified in TS36.133.

Tinterrupt = 62 ms in the test; Tinterrupt is defined in TS36.133 clause 5.3.4.3.

This gives a total of 112 ms.

### A.18.2.2 RRC connection release with redirection

#### A.18.2.2.1 Redirection from E-UTRA to NR FR1 for redcap UE

##### A.18.2.2.1.1 Test Purpose and Environment

This test is to verify RRC connection release with redirection from E-UTRA to NR requirements for 2Rx RedCap specified in 36.133 clause 6.3.2.6.

##### A.18.2.2.1.2 Test Parameters

Supported test configurations are shown in table A.18.2.2.1.2-1. The time delay is tested by using the parameters in table A.18.2.2.1.2-2, A.18.2.2.1.2-3, and A.18.2.2.1.2-4.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCConnectionRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.18.2.2.1.2-1: Redirection from E-UTRAN to NR test configurations

| Configuration | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode, LTE FDD |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode, LTE FDD |
| 3 | NR 30 kHz SSB SCS, 20 MHz bandwidth, TDD duplex mode, LTE FDD |
| 4 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode, LTE TDD |
| 5 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode, LTE TDD |
| 6 | NR 30 kHz SSB SCS, 20 MHz bandwidth, TDD duplex mode, LTE TDD |
| 7 | NR 15 kHz SSB SCS, 10 MHz bandwidth, HD-FDD duplex mode, LTE FDD |
| 8 | NR 15 kHz SSB SCS, 10 MHz bandwidth, HD-FDD duplex mode, LTE TDD |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.18.2.2.1.2-2: General test parameters for Redirection from E-UTRAN to NR test case

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 | E-UTRAN cell |
|  | Neighbouring cell |  | Cell 2 | NR cell |
| Final condition | Active cell |  | Cell 2 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 2.3 |  |

Table A.18.2.2.1.2-3: Cell specific test parameters for Redirection from E-UTRAN to NR test case (Cell 1)

| Parameter | Unit | Configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1, 2, 3, 4, 5, 6,7,8 | 2 |  |
| Duplex mode |  | 1, 2, 3,7 | FDD |  |
|  |  | 4, 5, 6,8 | TDD |  |
| TDD special subframe configurationNote1 |  | 4, 5, 6,8 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 4, 5, 6,8 | 1 |  |
| BWchannel | MHz | 1, 2, 3, 4, 5, 6,7,8 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PRACH ConfigurationNote2 |  | 1, 2, 3,7 | 4 |  |
|  |  | 4, 5, 6,8 | 53 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote3 |  | 1, 2, 3,7 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 4, 5, 6,8 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote3 |  | 1, 2, 3,7 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 4, 5, 6,8 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote3 |  | 1, 2, 3,7 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 4, 5, 6,8 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| PBCH_RA | dB | 1, 2, 3, 4, 5, 6,7,8 | 0 |  |
| PBCH_RB |  |  |  |  |
| PSS_RA |  |  |  |  |
| SSS_RA |  |  |  |  |
| PCFICH_RB |  |  |  |  |
| PHICH_RA |  |  |  |  |
| PHICH_RB |  |  |  |  |
| PDCCH_RA |  |  |  |  |
| PDCCH_RB |  |  |  |  |
| PDSCH_RA |  |  |  |  |
| PDSCH_RB |  |  |  |  |
| OCNG_RANote4 |  |  |  |  |
| OCNG_RBNote4 |  |  |  |  |
| NocNote5 | dBm/15 kHz | 1, 2, 3, 4, 5, 6,7,8 | -98 |  |
| Ês/Noc | dB | 1, 2, 3, 4, 5, 6,7,8 | 4 | 4 |
| Ês/IotNote6 | dB | 1, 2, 3, 4, 5, 6,7,8 | 4 | 4 |
| RSRPNote6 | dBm/15 kHz | 1, 2, 3, 4, 5, 6,7,8 | -94 | -94 |
| SCH_RPNote6 | dBm/15 kHz | 1, 2, 3, 4, 5, 6,7,8 | -94 | -94 |
| IoNote6 | dBm/9 MHz | 1, 2, 3, 4, 5, 6,7,8 | -64.76 | -64.76 |
| Propagation Condition |  | 1, 2, 3, 4, 5, 6,7,8 | AWGN |  |
| Antenna Configuration |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1x2 |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: PRACH configurations are specified in table 5.7.1-2 and table 5.7.1-3 in TS 36.211 [23].NOTE 3: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 4: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 5: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 6: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 7: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |

Table A.18.2.2.1.2-4: Cell specific test parameters for Redirection from E-UTRAN to NR test case (Cell 2)

| Parameter |  |  | Unit | Cell 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 |
| RF Channel Number |  |  |  | 1 |  |
| Duplex mode |  | Config 1,4 |  | FDD |  |
|  |  | Config 2,3,5,6 |  | TDD |  |
|  |  | Config 7,8 |  | HD-FDD |  |
| SSB Configuration |  | Config 1,2,4,5,7,8 |  | SSB.1 FR1 |  |
|  |  | Config 3,6 |  | SSB.1 RedCap FR1 |  |
| TDD configuration |  | Config 1,4,7,8 |  | Not Applicable |  |
|  |  | Config 2,5 |  | TDDConf.1.1 |  |
|  |  | Config 3,6 |  | TDDConf.2.1 |  |
| BWchannel |  | Config 1,4,7,8 | MHz | 10: NPRB,c = 52 |  |
|  |  | Config 2,5 |  | 10: NPRB,c = 52 |  |
|  |  | Config 3,6 |  | 20: NPRB,c = 51 |  |
| BWP BW |  | Config 1,4,7,8 | MHz | 10: NPRB,c = 52 |  |
|  |  | Config 2,5 |  | 10: NPRB,c = 52 |  |
|  |  | Config 3,6 |  | 20: NPRB,c = 51 |  |
| DRX Cycle |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  | Config 1,4,7,8 |  | SR.1.1 FDD |  |
|  |  | Config 2,5 |  | SR.1.1 TDD |  |
|  |  | Config 3,6 |  | SR.2.1 TDD |  |
| CORESET Reference Channel |  | Config 1,4,7,8 |  | CR.1.1 FDD |  |
|  |  | Config 2,5 |  | CR.1.1 TDD |  |
|  |  | Config 3,6 |  | CR.2.1 TDD |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |
| SMTC configuration |  | Config 1,2,4,5,7,8 |  | SMTC.1 RedCap FR1 |  |
|  |  | Config 3,6 |  | SMTC.1 RedCap FR1 |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2,4,5,7,8 | kHz | 15 kHz |  |
|  |  | Config 3,6 |  | 30 kHz |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1,2,4,5,7,8 | kHz | 15 kHz |  |
|  |  | Config 3,6 |  | 30 kHz |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,4,5,7,8 |  | dBm/SCS | -98 |  |
|  | Config 3,6 |  |  | -95 |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -infinity | 4 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -infinity | 4 |
| IoNote3 | Config 1,2,4,5,7,8 |  | dBm/9.36 MHz | -70.05 | -64.59 |
|  | Config 3,6 |  | dBm/18.36 MHz | -67.12 | -61.67 |
| Propagation condition |  |  | - | AWGN |  |
| Antenna Configuration |  |  |  | 1x2 |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |

##### A.18.2.2.1.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2240 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE: The redirection delay can be expressed as:

Tconnection_release_redirect_NR_RedCap = TRRC_procedure_delay + Tidentify-NR_Redcap + TSI-NR_RedCap + TRACH_RedCap,

where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR_Redcap = 680 ms.

TSI-NR_RedCap = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.


TRACH_RedCap = 170 ms in the test.

This gives a total of 2240 ms.

## A.18.3 Measurement procedure

### A.18.3.1 E-UTRA – NR Inter-RAT Measurements

#### A.18.3.1.1 NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used

##### A.18.3.1.1.1 Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements for 2Rx RedCap specified in clause 8.20.2.2 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133[15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1. The test parameters are given in tables A.18.3.1.1.1-1, A.18.3.1.1.1-2, A.18.3.1.1.1-3 and A.18.3.1.1.1-4.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.18.3.1.1.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | LTE FDD, NR 30 kHz SSB SCS, 20 MHz bandwidth, TDD duplex mode |
| 4 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 5 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 6 | LTE TDD, NR 30 kHz SSB SCS, 20 MHz bandwidth, TDD duplex mode |
| 7 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, HD-FDD duplex mode |
| 8 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, HD-FDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.18.3.1.1.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| E-UTRA RF Channel Number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 | One E-UTRAcarrier frequency is used. |
| NR RF Chanel Number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 | One FR1 NR carrier frequency is used. |
| Active cell |  | 1, 2, 3, 4, 5, 6, 7, 8 | E-UTRA Cell 1 (PCell) | E-UTRA Cell 1 is on E-UTRA RF channel number 1. |
| Neighbour cell |  | 1, 2, 3, 4, 5, 6, 7, 8 | NR Cell 2 | NR Cell 2 is on NR RF channel number 1. |
| Gap Pattern Id |  | 1, 2, 3, 4, 5, 6, 7, 8 | 0 | As specified in clause Table 8.1.2.1-1 of TS 36.133 [15]. |
| Measurement gap offset |  | 1, 2, 3, 4, 5, 6, 7, 8 | 39 | As specified in TS 36.331 [16]. |
| b2-Threshold1 | dBm | 1, 2, 3, 4, 5, 6, 7, 8 | Note 1 | E-UTRA RSRP threshold for E-UTRA RSRP measurement on Cell 1 for event B2 [16] |
| b2-Threshold2NR | dBm | 1, 2, 3, 4, 5, 6, 7, 8 | Note 2 | SS-RSRP threshold for SS-RSRP measurement on Cell 2 for event B2 [16] |
| Hysteresis | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |
| CP length |  | 1, 2, 3, 4, 5, 6, 7, 8 | Normal |  |
| TimeToTrigger | s | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |
| Filter coefficient |  | 1, 2, 3, 4, 5, 6, 7, 8 | 0 | L3 filtering is not used |
| DRX |  | 1, 2, 3, 4, 5, 6, 7, 8 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | 1, 4, 7, 8 | 3 ms | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
|  |  | 2, 3, 5, 6 | 3s | Synchronous cells. |
| T1 | s | 1, 2, 3, 4, 5, 6, 7, 8 | 5 |  |
| T2 | s | 1, 2, 3, 4, 5, 6, 7, 8 | 1 |  |
| NOTE 1: The value of b2-Threshold1 is defined in table A.18.3.1.1.1-3NOTE 2: The value of b2-Threshold2NR is defined in table A.18.3.1.1.1-4 |  |  |  |  |

Table A.18.3.1.1.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

| Parameter | Unit | Configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 |  |
| Duplex mode |  | 1, 2, 3, 7 | FDD |  |
|  |  | 4, 5, 6, 8 | TDD |  |
| TDD special subframe configurationNote1 |  | 4, 5, 6, 8 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 4, 5, 6, 8 | 1 |  |
| BWchannel | MHz | 1, 2, 3, 4, 5, 6, 7, 8 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 1, 2, 3, 7 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 4, 5, 6, 8 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 1, 2, 3, 7 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 4, 5, 6, 8 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote2 |  | 1, 2, 3, 7 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 4, 5, 6, 8 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| b2-Threshold1 | dBm | 1, 2, 3, 4, 5, 6, 7, 8 | -77 |  |
| PBCH_RA | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |
| PBCH_RB |  |  |  |  |
| PSS_RA |  |  |  |  |
| SSS_RA |  |  |  |  |
| PCFICH_RB |  |  |  |  |
| PHICH_RA |  |  |  |  |
| PHICH_RB |  |  |  |  |
| PDCCH_RA |  |  |  |  |
| PDCCH_RB |  |  |  |  |
| PDSCH_RA |  |  |  |  |
| PDSCH_RB |  |  |  |  |
| OCNG_RANote3 |  |  |  |  |
| OCNG_RBNote3 |  |  |  |  |
| NocNote4 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -104 |  |
| Ês/Noc | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 17 | 17 |
| Ês/IotNote5 | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 17 | 17 |
| RSRPNote5 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -87 | -87 |
| SCH_RPNote5 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -87 | -87 |
| IoNote5 | dBm/9 MHz | 1, 2, 3, 4, 5, 6, 7, 8 | -59.13+10log (NPRB,c /50) | -59.13+10log (NPRB,c /50) |
| Propagation Condition Note6 |  | 1, 2, 3, 4, 5, 6, 7, 8 | AWGN |  |
| Antenna Configuration and Correlation Matrix Note6 |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1x2 |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 6: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |

Table A.18.3.1.1.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Cell 2 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| NR RF Channel Number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 |  |
| Duplex mode |  | 1, 4 | FDD |  |
|  |  | 2, 3, 5, 6 | TDD |  |
|  |  | 7, 8 | HD-FDD |  |
| TDD configuration |  | 2, 5 | TDDConf.1.1 |  |
|  |  | 3, 6 | TDDConf.2.1 |  |
| BWchannel | MHz | 1, 2, 4, 5, 7, 8 | 10: NPRB,c = 52 |  |
|  |  | 3, 6 | 20: NPRB,c = 51 |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  | 1, 2, 3, 4, 5, 6, 7, 8 | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  | 1, 4, 7, 8 | SMTC.2 |  |
|  |  | 2, 3, 5, 6 | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2, 4, 5, 7, 8 | 15 |  |
|  |  | 3, 6 | 30 |  |
| b2-Threshold2NR | dBm/SCS | 1, 2, 4, 5, 7, 8 | -101 |  |
|  |  | 3, 6 | -98 |  |
| EPRE ratio of PSS to SSS |  | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1, 2, 4, 5, 7, 8 | -98 |  |
|  |  | 3, 6 | -95 |  |
| SS-RSRP Note 3 | dBm/SCS | 1, 2, 4, 5, 7, 8 | -Infinity | -91 |
|  |  | 3, 6 | -Infinity | -88 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2, 3, 4, 5, 6, 7, 8 | -Infinity | 7 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2, 3, 4, 5, 6, 7, 8 | -Infinity | 7 |
| IoNote3 | dBm/9.36 MHz | 1, 2, 4, 5, 7, 8 | -70.05 | -62.26 |
|  | dBm/18.36 MHz | 3, 6 | -67.13 | -59.34 |
| Propagation Condition |  | 1, 2, 3, 4, 5, 6, 7, 8 | AWGN |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1x2 |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |

##### A.18.3.1.1.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1, the UE is not required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.18.3.1.2 NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used

##### A.18.3.1.2.1 Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements for 2Rx RedCap specified in clause 8.20.2.2 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133[15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1. The test parameters are given in tables A.18.3.1.2.1-1, A.18.3.1.2.1-2, A.18.3.1.2.1-3 and A.18.3.1.2.1-4.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.18.3.1.2.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | LTE FDD, NR 30 kHz SSB SCS, 20 MHz bandwidth, TDD duplex mode |
| 4 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 5 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 6 | LTE TDD, NR 30 kHz SSB SCS, 20 MHz bandwidth, TDD duplex mode |
| 7 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, HD-FDD duplex mode |
| 8 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, HD-FDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.18.3.1.2.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| E-UTRA RF Channel Number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 |  | One E-UTRA carrier frequency is used. |
| NR RF Channel Number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 |  | One FR1 NR carrier frequency is used. |
| Active cell |  | 1, 2, 3, 4, 5, 6, 7, 8 | E-UTRA Cell 1 (PCell) |  | E-UTRA Cell 1 is on E-UTRA RF channel number 1. |
| Neighbour cell |  | 1, 2, 3, 4, 5, 6, 7, 8 | NR Cell 2 |  | NR Cell 2 is on NR RF channel number 1. |
| Gap Pattern Id |  | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  | As specified in clause Table 8.1.2.1-1 of TS 36.133 [15]. |
| Measurement gap offset |  | 1, 2, 3, 4, 5, 6, 7, 8 | 39 |  | As specified in TS 36.331 [16]. |
| b2-Threshold1 | dBm | 1, 2, 3, 4, 5, 6, 7, 8 | Note 1 |  | E-UTRA RSRP threshold for E-UTRA RSRP measurement on Cell 1 for event B2 [16] |
| b2-Threshold2NR | dBm | 1, 2, 3, 4, 5, 6, 7, 8 | Note 2 |  | SS-RSRP threshold for SS-RSRP measurement on Cell 2 for event B2 [16] |
| Hysteresis | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |  |
| CP length |  | 1, 2, 3, 4, 5, 6, 7, 8 | Normal |  |  |
| TimeToTrigger | s | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |  |
| Filter coefficient |  | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  | L3 filtering is not used |
| DRX |  | 1, 2, 3, 4, 5, 6, 7, 8 | DRX.9 | DRX.12 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | 1, 4, 7, 8 | 3 ms |  | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
|  |  | 2, 3, 5, 6 | 3s |  | Synchronous cells. |
| T1 | s | 1, 2, 3, 4, 5, 6, 7, 8 | 5 |  |  |
| T2 | s | 1, 2, 3, 4, 5, 6, 7, 8 | 2 | 11 |  |
| NOTE 1: The value of b2-Threshold1 is defined in table A.18.3.1.2.1-3NOTE 2: The value of b2-Threshold2NR is defined in table A.18.3.1.2.1-4 |  |  |  |  |  |

Table A.18.3.1.2.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

| Parameter | Unit | Configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 |  |
| Duplex mode |  | 1, 2, 3, 7 | FDD |  |
|  |  | 4, 5, 6, 8 | TDD |  |
| TDD special subframe configurationNote1 |  | 4, 5, 6, 8 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 4, 5, 6, 8 | 1 |  |
| BWchannel | MHz | 1, 2, 3, 4, 5, 6, 7, 8 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 1, 2, 3, 7 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 4, 5, 6, 8 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 1, 2, 3, 7 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 4, 5, 6, 8 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote2 |  | 1, 2, 3, 7 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 4, 5, 6, 8 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| b2-Threshold1 | dBm | 1, 2, 3, 4, 5, 6, 7, 8 | -77 |  |
| PBCH_RA | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |
| PBCH_RB |  |  |  |  |
| PSS_RA |  |  |  |  |
| SSS_RA |  |  |  |  |
| PCFICH_RB |  |  |  |  |
| PHICH_RA |  |  |  |  |
| PHICH_RB |  |  |  |  |
| PDCCH_RA |  |  |  |  |
| PDCCH_RB |  |  |  |  |
| PDSCH_RA |  |  |  |  |
| PDSCH_RB |  |  |  |  |
| OCNG_RANote3 |  |  |  |  |
| OCNG_RBNote3 |  |  |  |  |
| NocNote4 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -104 |  |
| Ês/Noc | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 17 | 17 |
| Ês/IotNote5 | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 17 | 17 |
| RSRPNote5 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -87 | -87 |
| SCH_RPNote5 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -87 | -87 |
| IoNote5 | dBm/9 MHz | 1, 2, 3, 4, 5, 6, 7, 8 | -59.13+10log (NPRB,c /50) | -59.13+10log (NPRB,c /50) |
| Propagation Condition Note6 |  | 1, 2, 3, 4, 5, 6, 7, 8 | AWGN |  |
| Antenna Configuration and Correlation Matrix Note6 |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1x2 |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 6: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |

Table A.18.3.1.2.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Cell 2 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| NR RF Channel Number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 |  |
| Duplex mode |  | 1, 4 | FDD |  |
|  |  | 2, 3, 5, 6 | TDD |  |
|  |  | 7, 8 | HD-FDD |  |
| TDD configuration |  | 2, 5 | TDDConf.1.1 |  |
|  |  | 3, 6 | TDDConf.2.1 |  |
| BWchannel | MHz | 1, 2, 4, 5, 7, 8 | 10: NPRB,c = 52 |  |
|  |  | 3, 6 | 20: NPRB,c = 51 |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  | 1, 2, 3, 4, 5, 6, 7, 8 | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  | 1, 4, 7, 8 | SMTC.2 |  |
|  |  | 2, 3, 5, 6 | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2, 4, 5 | 15 |  |
|  |  | 3, 6 | 30 |  |
| b2-Threshold2NR | dBm/SCS | 1, 2, 4, 5, 7, 8 | -101 |  |
|  |  | 3, 6 | -98 |  |
| EPRE ratio of PSS to SSS |  | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1, 2, 4, 5, 7, 8 | -98 |  |
|  |  | 3, 6 | -95 |  |
| SS-RSRP Note 3 | dBm/SCS | 1, 2, 4, 5, 7, 8 | -Infinity | -91 |
|  |  | 3, 6 | -Infinity | -88 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2, 3, 4, 5, 6, 7, 8 | -Infinity | 7 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2, 3, 4, 5, 6, 7, 8 | -Infinity | 7 |
| IoNote3 | dBm/9.36 MHz | 1, 2, 4, 5, 7, 8 | -70.05 | -62.26 |
|  | dBm/18.36 MHz | 3, 6 | -67.13 | -59.34 |
| Propagation Condition |  | 1, 2, 3, 4, 5, 6, 7, 8 | AWGN |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1x2 |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |

##### A.18.3.1.2.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement In test 1 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 1080 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 10240 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is not required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.18.3.1.3 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used

##### A.18.3.1.3.1 Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements for 2Rx RedCap specified in clause 8.20.2.2of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133[15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1.  The test parameters are given in tables A.18.3.1.3.1-1, A.18.3.1.3.1-2, A.18.3.1.3.1-3 and A.18.3.1.3.1-4.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2..

Table A.18.3.1.3.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | LTE FDD, NR 30 kHz SSB SCS, 20 MHz bandwidth, TDD duplex mode |
| 4 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 5 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 6 | LTE TDD, NR 30 kHz SSB SCS, 20 MHz bandwidth, TDD duplex mode |
| 7 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, HD-FDD duplex mode |
| 8 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, HD-FDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.18.3.1.3.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| E-UTRA RF Channel Number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 | One E-UTRA carrier frequency is used. |
| NR RF Channel Number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 | One FR1 NR carrier frequency is used. |
| Active cell |  | 1, 2, 3, 4, 5, 6, 7, 8 | E-UTRA Cell 1 (PCell) | E-UTRA Cell 1 is on E-UTRA RF channel number 1. |
| Neighbour cell |  | 1, 2, 3, 4, 5, 6, 7, 8 | NR Cell 2 | NR Cell 2 is on NR RF channel number 1. |
| Gap Pattern Id |  | 1, 2, 3, 4, 5, 6, 7, 8 | 0 | As specified in clause Table 8.1.2.1-1 of TS 36.133 [15]. |
| Measurement gap offset |  | 1, 2, 3, 4, 5, 6, 7, 8 | 39 | As specified in TS 36.331 [16]. |
| b2-Threshold1 | dBm | 1, 2, 3, 4, 5, 6, 7, 8 | Note 1 | E-UTRA RSRP threshold for E-UTRA RSRP measurement on Cell 1 for event B2 [16] |
| b2-Threshold2NR | dBm | 1, 2, 3, 4, 5, 6, 7, 8 | Note 2 | SS-RSRP threshold for SS-RSRP measurement on Cell 2 for event B2 [16] |
| Hysteresis | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |
| CP length |  | 1, 2, 3, 4, 5, 6, 7, 8 | Normal |  |
| TimeToTrigger | s | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |
| Filter coefficient |  | 1, 2, 3, 4, 5, 6, 7, 8 | 0 | L3 filtering is not used |
| DRX |  | 1, 2, 3, 4, 5, 6, 7, 8 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | 1, 4, 7, 8 | 3 ms | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
|  |  | 2, 3, 5, 6 | 3s | Synchronous cells. |
| T1 | s | 1, 2, 3, 4, 5, 6, 7, 8 | 5 |  |
| T2 | s | 1, 2, 3, 4, 5, 6, 7, 8 | 2 |  |
| NOTE 1: The value of b2-Threshold1 is defined in table A.18.3.1.3.1-3NOTE 2: The value of b2-Threshold2NR is defined in table A.18.3.1.3.1-4 |  |  |  |  |

Table A.18.3.1.3.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

| Parameter | Unit | Configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 |  |
| Duplex mode |  | 1, 2, 3, 7 | FDD |  |
|  |  | 4, 5, 6, 8 | TDD |  |
| TDD special subframe configurationNote1 |  | 4, 5, 6, 8 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 4, 5, 6, 8 | 1 |  |
| BWchannel | MHz | 1, 2, 3, 4, 5, 6, 7, 8 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 1, 2, 3, 7 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 4, 5, 6, 8 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 1, 2, 3, 7 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 4, 5, 6, 8 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote2 |  | 1, 2, 3, 7 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 4, 5, 6, 8 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| b2-Threshold1 | dBm | 1, 2, 3, 4, 5, 6, 7, 8 | -77 |  |
| PBCH_RA | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |
| PBCH_RB |  |  |  |  |
| PSS_RA |  |  |  |  |
| SSS_RA |  |  |  |  |
| PCFICH_RB |  |  |  |  |
| PHICH_RA |  |  |  |  |
| PHICH_RB |  |  |  |  |
| PDCCH_RA |  |  |  |  |
| PDCCH_RB |  |  |  |  |
| PDSCH_RA |  |  |  |  |
| PDSCH_RB |  |  |  |  |
| OCNG_RANote3 |  |  |  |  |
| OCNG_RBNote3 |  |  |  |  |
| NocNote4 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -104 |  |
| Ês/Noc | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 17 | 17 |
| Ês/IotNote5 | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 17 | 17 |
| RSRPNote5 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -87 | -87 |
| SCH_RPNote5 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -87 | -87 |
| IoNote5 | dBm/9 MHz | 1, 2, 3, 4, 5, 6, 7, 8 | -59.13+10log (NPRB,c /50) | -59.13+10log (NPRB,c /50) |
| Propagation Condition Note6 |  | 1, 2, 3, 4, 5, 6, 7, 8 | AWGN |  |
| Antenna Configuration and Correlation Matrix Note6 |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1x2 |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 6: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |

Table A.18.3.1.3.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Cell 2 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| NR RF Channel Number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 |  |
| Duplex mode |  | 1, 4 | FDD |  |
|  |  | 2, 3, 5, 6 | TDD |  |
|  |  | 7, 8 |  |  |
| TDD configuration |  | 2, 5 | TDDConf.1.1 |  |
|  |  | 3, 6 | TDDConf.2.1 |  |
| BWchannel | MHz | 1, 2, 4, 5, 7, 8 | 10: NPRB,c = 52 |  |
|  |  | 3, 6 | 20: NPRB,c = 51 |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  | 1, 2, 3, 4, 5, 6, 7, 8 | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  | 1, 4, 7, 8 | SMTC.2 |  |
|  |  | 2, 3, 5, 6 | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2, 4, 5, 7, 8 | 15 |  |
|  |  | 3, 6 | 30 |  |
| b2-Threshold2NR | dBm/SCS | 1, 2, 4, 5, 7, 8 | -101 |  |
|  |  | 3, 6 | -98 |  |
| EPRE ratio of PSS to SSS |  | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1, 2, 4, 5, 7, 8 | -98 |  |
|  |  | 3, 6 | -95 |  |
| SS-RSRP Note 3 | dBm/SCS | 1, 2, 4, 5, 7, 8 | -Infinity | -91 |
|  |  | 3, 6 | -Infinity | -88 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2, 3, 4, 5, 6, 7, 8 | -Infinity | 7 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2, 3, 4, 5, 6, 7, 8 | -Infinity | 7 |
| IoNote3 | dBm/9.36 MHz | 1, 2, 4, 5, 7, 8 | -70.05 | -62.26 |
|  | dBm/18.36 MHz | 3, 6 | -67.13 | -59.34 |
| Propagation Condition |  | 1, 2, 3, 4, 5, 6, 7, 8 | AWGN |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1x2 |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |

##### A.18.3.1.3.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 1040 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1, the UE is required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.18.3.1.4 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used

##### A.18.3.1.4.1 Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements for 2Rx RedCap specified in clause 8.20.2.2of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133[15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1. The test parameters are given in tables A.18.3.1.4.1-1, A.18.3.1.4.1-2, A.18.3.1.4.1-3 and A.18.3.1.4.1-4.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2

Table A.18.3.1.4.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | LTE FDD, NR 30 kHz SSB SCS, 20 MHz bandwidth, TDD duplex mode |
| 4 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 5 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 6 | LTE TDD, NR 30 kHz SSB SCS, 20 MHz bandwidth, TDD duplex mode |
| 7 | LTE FDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, HD-FDD duplex mode |
| 8 | LTE TDD, NR 15 kHz SSB SCS, 10 MHz bandwidth, HD-FDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.18.3.1.4.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| E-UTRA RF Channel Number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 |  | One E-UTRA carrier frequency is used. |
| NR RF Channel Number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 |  | One FR1 NR carrier frequency is used. |
| Active cell |  | 1, 2, 3, 4, 5, 6, 7, 8 | E-UTRA Cell 1 (PCell) |  | E-UTRA Cell 1 is on E-UTRA RF channel number 1. |
| Neighbour cell |  | 1, 2, 3, 4, 5, 6, 7, 8 | NR Cell 2 |  | NR Cell 2 is on NR RF channel number 1. |
| Gap Pattern Id |  | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  | As specified in clause Table 8.1.2.1-1 of TS 36.133 [15]. |
| Measurement gap offset |  | 1, 2, 3, 4, 5, 6, 7, 8 | 39 |  | As specified in TS 36.331 [16]. |
| b2-Threshold1 | dBm | 1, 2, 3, 4, 5, 6, 7, 8 | Note 1 |  | E-UTRA RSRP threshold for E-UTRA RSRP measurement on Cell 1 for event B2 [16] |
| b2-Threshold2NR | dBm | 1, 2, 3, 4, 5, 6, 7, 8 | Note 2 |  | SS-RSRP threshold for SS-RSRP measurement on Cell 2 for event B2 [16] |
| Hysteresis | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |  |
| CP length |  | 1, 2, 3, 4, 5, 6, 7, 8 | Normal |  |  |
| TimeToTrigger | s | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |  |
| Filter coefficient |  | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  | L3 filtering is not used |
| DRX |  | 1, 2, 3, 4, 5, 6, 7, 8 | DRX.9 | DRX.12 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | 1, 4, 7, 8 | 3 ms |  | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
|  |  | 2, 3, 5, 6 | 3s |  | Synchronous cells. |
| T1 | s | 1, 2, 3, 4, 5, 6, 7, 8 | 5 |  |  |
| T2 | s | 1, 2, 3, 4, 5, 6, 7, 8 | 2 | 13 |  |
| NOTE 1: The value of b2-Threshold1 is defined in table A.18.3.1.4.1-3NOTE 2: The value of b2-Threshold2NR is defined in table A.18.3.1.4.1-4 |  |  |  |  |  |

Table A.18.3.1.4.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

| Parameter | Unit | Configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 |  |
| Duplex mode |  | 1, 2, 3, 7 | FDD |  |
|  |  | 4, 5, 6, 8 | TDD |  |
| TDD special subframe configurationNote1 |  | 4, 5, 6, 8 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 4, 5, 6, 8 | 1 |  |
| BWchannel | MHz | 1, 2, 3, 4, 5, 6, 7, 8 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 1, 2, 3, 7 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 4, 5, 6, 8 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 1, 2, 3, 7 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 4, 5, 6, 8 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote2 |  | 1, 2, 3, 7 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 4, 5, 6, 8 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| b2-Threshold1 | dBm | 1, 2, 3, 4, 5, 6, 7, 8 | -77 |  |
| PBCH_RA | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |
| PBCH_RB |  |  |  |  |
| PSS_RA |  |  |  |  |
| SSS_RA |  |  |  |  |
| PCFICH_RB |  |  |  |  |
| PHICH_RA |  |  |  |  |
| PHICH_RB |  |  |  |  |
| PDCCH_RA |  |  |  |  |
| PDCCH_RB |  |  |  |  |
| PDSCH_RA |  |  |  |  |
| PDSCH_RB |  |  |  |  |
| OCNG_RANote3 |  |  |  |  |
| OCNG_RBNote3 |  |  |  |  |
| NocNote4 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -104 |  |
| Ês/Noc | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 17 | 17 |
| Ês/IotNote5 | dB | 1, 2, 3, 4, 5, 6, 7, 8 | 17 | 17 |
| RSRPNote5 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -87 | -87 |
| SCH_RPNote5 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -87 | -87 |
| IoNote5 | dBm/9 MHz | 1, 2, 3, 4, 5, 6, 7, 8 | -59.13+10log (NPRB,c /50) | -59.13+10log (NPRB,c /50) |
| Propagation Condition Note6 |  | 1, 2, 3, 4, 5, 6, 7, 8 | AWGN |  |
| Antenna Configuration and Correlation Matrix Note6 |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1x2 |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 6: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |

Table A.18.3.1.4.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Cell 2 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| NR RF Channel Number |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1 |  |
| Duplex mode |  | 1, 4 | FDD |  |
|  |  | 2, 3, 5, 6 | TDD |  |
|  |  | 7, 8 | HD-FDD |  |
| TDD configuration |  | 2, 5 | TDDConf.1.1 |  |
|  |  | 3, 6 | TDDConf.2.1 |  |
| BWchannel | MHz | 1, 2, 4, 5, 7, 8 | 10: NPRB,c = 52 |  |
|  |  | 3, 6 | 20: NPRB,c = 51 |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  | 1, 2, 3, 4, 5, 6, 7, 8 | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  | 1, 4, 7, 8 | SMTC.2 |  |
|  |  | 2, 3, 5, 6 | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2, 4, 5, 7, 8 | 15 |  |
|  |  | 3, 6 | 30 |  |
| b2-Threshold2NR | dBm/SCS | 1, 2, 4, 5, 7, 8 | -101 |  |
|  |  | 3, 6 | -98 |  |
| EPRE ratio of PSS to SSS |  | 1, 2, 3, 4, 5, 6, 7, 8 | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1, 2, 3, 4, 5, 6, 7, 8 | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1, 2, 4, 5, 7, 8 | -98 |  |
|  |  | 3, 6 | -95 |  |
| SS-RSRP Note 3 | dBm/SCS | 1, 2, 4, 5, 7, 8 | -Infinity | -91 |
|  |  | 3, 6 | -Infinity | -88 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2, 3, 4, 5, 6, 7, 8 | -Infinity | 7 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2, 3, 4, 5, 6, 7, 8 | -Infinity | 7 |
| IoNote3 | dBm/9.36 MHz | 1, 2, 4, 5, 7, 8 | -70.05 | -62.26 |
|  | dBm/18.36 MHz | 3, 6 | -67.13 | -59.34 |
| Propagation Condition |  | 1, 2, 3, 4, 5, 6, 7, 8 | AWGN |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2, 3, 4, 5, 6, 7, 8 | 1x2 |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |

##### A.18.3.1.4.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 1280 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 12160 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.18.3.1.5 NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is not used

##### A.18.3.1.5.1 Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.20.2.2 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133[15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 1. The test parameters are given in tables A.18.3.1.5.1-1, A.18.3.1.5.1-2 and A.18.3.1.5.1-3.

The cell specific test parameters for E-UTRA cell1 as PCell are defined in clause A.3.7.2.2.

In test 1 measurement gap pattern configuration # 0 as defined in table A.18.3.1.5.1-2 is provided for RedCap UE that does not support per-FR gap and in test 2 no measurement gap pattern configuration  is provided for RedCap UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B1 (Inter RAT neighbour becomes better than threshold) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have timing information of NR Cell 2.

Table A.18.3.1.5.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR2 in non-DRX

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD, NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.18.3.1.5.1-2: General test parameters for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in non-DRX

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| E-UTRA RF Channel Number |  | 1, 2 | 1 |  | One E-UTRAcarrier frequency is used. |
| NR RF Channel Number |  | 1, 2 | 1 |  | One FR2 NR carrier frequency is used. |
| Active cell |  | 1, 2 | E-UTRA Cell 1 (PCell) |  | E-UTRA Cell 1 is on E-UTRA RF channel number 1 as defined in clause A.3.7.2.2. |
| Neighbour cell |  | 1, 2 | NR Cell 2 |  | NR Cell 2 is on NR RF channel number 1. |
| Gap Pattern Id |  | 1, 2 | 0 | N/A | As specified in clause Table 8.1.2.1-1 of TS 36.133 [15]. |
| Measurement gap offset |  | 1, 2 | 39 | N/A | As specified in TS 36.331 [16]. |
| b1-ThresholdNR | dBm | 1, 2 | Note 1 |  | SS-RSRP threshold for SS-RSRP measurement on Cell 2 for event B1 [16] |
| Hysteresis | dB | 1, 2 | 0 |  |  |
| CP length |  | 1, 2 | Normal |  |  |
| TimeToTrigger | s | 1, 2 | 0 |  |  |
| Filter coefficient |  | 1, 2 | 0 |  | L3 filtering is not used |
| DRX |  | 1, 2 | OFF |  | DRX is not used |
| Time offset between serving and neighbour cells |  | 1 | 3 ms |  | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
|  |  | 2 | 3s |  | Synchronous cells. |
| T1 | s | 1, 2 | 10 |  |  |
| T2 | s | 1, 2 | 6 | 3 |  |
| NOTE 1: The value of b1-ThresholdNR is defined in table A.18.3.1.5.1-3 |  |  |  |  |  |

Table A.18.3.1.5.1-3: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in non-DRX

| Parameter |  | Unit | Test configuration | Cell 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 |
| AoA setup defined in A.3.15.2.1 |  |  | 1, 2 | Setup 2a |  |
| Assumption for UE beamsNote 5 |  |  | 1, 2 | Rough |  |
| NR RF Channel Number |  |  | 1, 2 | 1 |  |
| Duplex mode |  |  | 1, 2 | TDD |  |
| TDD configuration |  |  | 1, 2 | TDDConf.3.1 |  |
| BWchannel |  | MHz | 1, 2 | 100: NPRB,c = 24 |  |
| OCNG patterns defined in A.3.2.1.1 |  |  | 1, 2 | OP. 3 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  |  | 1 | SMTC.2 |  |
|  |  |  | 2 | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 1, 2 | 120 |  |
| b1-ThresholdNR | UE power class 3 | dBm/SCS | 1, 2 | -112 |  |
| EPRE ratio of PSS to SSS |  |  | 1, 2 | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Ês |  | dBm/SCS | 1, 2 | - Infinity | -80.6 |
| SS B_RP Note 3 |  | dBm/SCS | 1, 2 | -Infinity | -80.6 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] BB Note 6 |  | dB | 1, 2 | -Infinity | 8.3 |
| IoNote3 |  | dBm/95.04 MHz | 1, 2 | -Infinity | -56.0 |
| Propagation Condition |  |  | 1, 2 | No external noise (Note 7) |  |
| NOTE 1: OCNG shall be used such that a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: VoidNOTE 3: SS B_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: VoidNOTE 5: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementationNOTE 6: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] Table 6.2.1.3-4.NOTE 7: The downlink connection between the System Simulator and the UE is without Additive White Gaussian Noise, and has no fading or multipath effects as specified in TS 38.521-2 B.0 [38]. |  |  |  |  |  |

##### A.18.3.1.5.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D1 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-FR gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D2 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and test 2, the UE is not required to report SSB time index.

Table A.18.3.1.5.2-1: Test requirements for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in non-DRX

| Test case | Measurement reporting delay (ms) |  |
| --- | --- | --- |
|  | Test 1: D1 ms | Test 2: D2 ms |
| UE power class 3 | 3200 | 1600 |


NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.18.3.1.6 NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is used

##### A.18.3.1.6.1 Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.20.2.2 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133[15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 1.  The test parameters are given in tables A.18.3.1.6.1-1, A.18.3.1.6.1-2 and A.18.3.1.6.1-3.

The cell specific test parameters for E-UTRA cell1 as PCell are defined in clause A.3.7.2.2.


In tests 1 and 2, measurement gap pattern configuration # 0 as defined in table A.18.3.1.6.1-2 is provided for RedCap UE that does not support per-FR gap and in tests 3 and 4, no measurement gap pattern configuration is provided for RedCap UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B1 (Inter RAT neighbour becomes better than threshold) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have timing information of NR Cell 2.

Table A.18.3.1.6.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR2 in DRX

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD, NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.18.3.1.6.1-2: General test parameters for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in DRX

| Parameter | Unit | Test configuration | Value |  |  |  |  |  | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  | Test 3 | Test 4 |  |  |
| E-UTRA RF Channel Number |  | 1, 2 | 1 |  |  |  |  |  | One E-UTRA carrier frequency is used. |
| NR RF Channel Number |  | 1, 2 | 1 |  |  |  |  |  | One FR2 NR carrier frequency is used. |
| Active cell |  | 1, 2, 3, 4, 5, 6 | E-UTRA Cell 1 (PCell) |  |  |  |  |  | E-UTRA Cell 1 is on E-UTRA RF channel number 1 as defined in clause A.3.7.2.2. |
| Neighbour cell |  | 1, 2, 3, 4, 5, 6 | NR Cell 2 |  |  |  |  |  | NR Cell 2 is on NR RF channel number 1. |
| Gap Pattern Id |  | 1, 2, 3, 4, 5, 6 | 0 |  |  | N/A |  |  | As specified in clause Table 8.1.2.1-1 of TS 36.133 [15]. |
| Measurement gap offset |  | 1, 2, 3, 4, 5, 6 | 39 |  |  | N/A |  |  | As specified in TS 36.331 [16]. |
| b1-ThresholdNR | dBm | 1, 2 | Note 1 |  |  |  |  |  | SS-RSRP threshold for SS-RSRP measurement on Cell 2 for event B1 [16] |
| Hysteresis | dB | 1, 2, 3, 4, 5, 6 | 0 |  |  |  |  |  |  |
| CP length |  | 1, 2, 3, 4, 5, 6 | Normal |  |  |  |  |  |  |
| TimeToTrigger | s | 1, 2, 3, 4, 5, 6 | 0 |  |  |  |  |  |  |
| Filter coefficient |  | 1, 2, 3, 4, 5, 6 | 0 |  |  |  |  |  | L3 filtering is not used |
| DRX |  | 1, 2, 3, 4, 5, 6 | DRX.9 | DRX.12 |  | DRX.9 | DRX.12 |  | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | 1 | 3 ms |  |  |  |  |  | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
|  |  | 2 | 3s |  |  |  |  |  | Synchronous cells. |
| T1 | s | 1, 2, 3, 4, 5, 6 | 5 |  |  |  |  |  |  |
| T2 | s | 1, 2, 3, 4, 5, 6 | 6 |  | 83 | 6 |  | 83 |  |
| NOTE 1: The value of b1-ThresholdNR is defined in table A.18.3.1. 6.1-3 |  |  |  |  |  |  |  |  |  |

Table A.18.3.1.6.1-3: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in DRX

| Parameter |  | Unit | Test configuration | Cell 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 |
| AoA setup defined in clause A.3.15.1 |  |  | 1, 2 | Setup 1 |  |
| Assumption for UE beamsNote 5 |  |  | 1, 2 | Rough |  |
| NR RF Channel Number |  |  | 1, 2 | 1 |  |
| Duplex mode |  |  | 1, 2 | TDD |  |
| TDD configuration |  |  | 1, 2 | TDDConf.3.1 |  |
| BWchannel |  | MHz | 1, 2 | 100: NPRB,c = 66 |  |
| OCNG patterns defined in A.3.2.1.1 (OP.1) |  |  | 1, 2 | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  |  | 1 | SMTC.2 |  |
|  |  |  | 2 | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 1, 2 | 120 |  |
| b1-ThresholdNR | UE power class 3 | dBm/SCS | 1, 2 | -106 |  |
| EPRE ratio of PSS to SSS |  |  | 1, 2 | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | 1, 2 | -104.7 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | 1, 2 | -95.7 |  |
| SS-RSRP Note 3 |  | dBm/SCS | 1, 2 | -Infinity | -87.7 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 1, 2 | -Infinity | 8 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 1, 2 | -Infinity | 8 |
| IoNote3 |  | dBm/95.04 MHz | 1, 2 | -66.7 | -58. 0 |
| Propagation Condition |  |  | 1, 2 | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc]to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |

##### A.18.3.1.6.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D1 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D2 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 3 with per-FR gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D3 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 4 with per-FR gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D4 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1, 2, 3 and 4, the UE is not required to report SSB time index.

Table A.18.3.1.6.2-1: Test requirements for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in DRX

| Test case | Measurement reporting delay (ms) |  |  |  |
| --- | --- | --- | --- | --- |
|  | Test 1: D1 ms | Test 2: D2 ms | Test 3: D3 ms | Test 4: D4 ms |
| UE power class 3 | 4800 | 51200 | 4800 | 51200 |

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.18.3.1.7 NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is not used

##### A.18.3.1.7.1 Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.20.2.2 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133[15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 1. The test parameters are given in tables A.18.3.1.7.1-1, A.18.3.1.7.1-2 and A.18.3.1.7.1-3.

The cell specific test parameters for E-UTRA cell1 as PCell are defined in clause A.3.7.2.2.

In test 1 measurement gap pattern configuration # 0 as defined in table A.18.3.1.7.1-2 is provided for RedCap UE that does not support per-FR gap and in test 2 no measurement gap pattern configuration is provided for RedCap UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B1 (Inter RAT neighbour becomes better than threshold) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.18.3.1.7.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR2 in non-DRX

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD, NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.18.3.1.7.1-2: General test parameters for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in non-DRX

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| E-UTRA RF Channel Numbers |  | 1, 2 | 1 |  | One E-UTRA carrier frequency is used. |
| NR RF Channel Numbers |  | 1, 2 | 1 |  | One FR2 NR carrier frequency is used. |
| Active cell |  | 1, 2 | E-UTRA Cell 1 (PCell) |  | E-UTRA Cell 1 is on E-UTRA RF channel number 1 as defined in clause A.3.7.2.2. |
| Neighbour cell |  | 1, 2 | NR Cell 2 |  | NR Cell 2 is on NR RF channel number 1. |
| Gap Pattern Id |  | 1, 2 | 0 | N/A | As specified in clause Table 8.1.2.1-1 of TS 36.133 [15]. |
| Measurement gap offset |  | 1, 2 | 39 | N/A | As specified in TS 36.331 [16]. |
| b1-ThresholdNR | dBm | 1, 2 | Note 1 |  | SS-RSRP threshold for SS-RSRP measurement on Cell 2 for event B1 [16] |
| Hysteresis | dB | 1, 2 | 0 |  |  |
| CP length |  | 1, 2 | Normal |  |  |
| TimeToTrigger | s | 1, 2 | 0 |  |  |
| Filter coefficient |  | 1, 2 | 0 |  | L3 filtering is not used |
| DRX |  | 1, 2 | OFF |  | DRX is not used |
| Time offset between serving and neighbour cells |  | 1 | 3 ms |  | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
|  |  | 2 | 3s |  | Synchronous cells. |
| T1 | s | 1, 2 | 5 |  |  |
| T2 | s | 1, 2 | 5 | 3 |  |
| NOTE 1: The value of b1-ThresholdNR is defined in table A.18.3.1. 7.1-3 |  |  |  |  |  |

Table A.18.3.1.7.1-3: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in non-DRX

| Parameter |  | Unit | Test configuration | Cell 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 |
| AoA setup defined in clause A.3.15.1 |  |  | 1, 2 | Setup 1 |  |
| Assumption for UE beamsNote 5 |  |  | 1, 2 | Rough |  |
| NR RF Channel Number |  |  | 1, 2 | 1 |  |
| Duplex mode |  |  | 1, 2 | TDD |  |
| TDD configuration |  |  | 1, 2 | TDDConf.3.1 |  |
| BWchannel |  | MHz | 1, 2 | 100: NPRB,c = 66 |  |
| OCNG patterns defined in A.3.2.1.1 |  |  | 1, 2 | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  |  | 1 | SMTC.2 |  |
|  |  |  | 2 | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 1, 2 | 120 |  |
| b1-ThresholdNR | UE power class 3 | dBm/SCS | 1, 2 | -106 |  |
| EPRE ratio of PSS to SSS |  |  | 1, 2 | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | 1, 2 | -104.7 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | 1, 2 | -95.7 |  |
| SS-RSRP Note 3 |  | dBm/SCS | 1, 2 | -Infinity | -87.7 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 1, 2 | -Infinity | 8 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 1, 2 | -Infinity | 8 |
| IoNote3 |  | dBm/95.04 MHz | 1, 2 | -66.7 | -58. 0 |
| Propagation Condition |  |  | 1, 2 | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc]to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |

##### A.18.3.1.7.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D1 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-FR gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D2 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and test 2, the UE is required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

Table A.18.3.1.7.2-1: Test requirements for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in non-DRX

| Test case | Measurement reporting delay (ms) |  |
| --- | --- | --- |
|  | Test 1: D1 ms | Test 2: D2 ms |
| UE power class 3 | 4160 | 2080 |

#### A.18.3.1.8 NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is used

##### A.18.3.1.8.1 Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.20.2.2 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133[15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 1. The test parameters are given in tables A.18.3.1.8.1-1, A.18.3.1.8.1-2 and A.18.3.1.8.1-3.

The cell specific test parameters for E-UTRA cell1 as PCell are defined in clause A.3.7.2.2.

In tests 1 and 2, measurement gap pattern configuration # 0 as defined in table A.18.3.1.8.1-2 is provided for RedCap UE that does not support per-FR gap and in tests 3 and 4, no measurement gap pattern configuration #4 is provided for RedCap UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B1 (Inter RAT neighbour becomes better than threshold) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.18.3.1.8.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR2 in DRX

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD, NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.18.3.1.8.1-2: General test parameters for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in DRX

| Parameter | Unit | Test configuration | Value |  |  |  | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 | Test 3 | Test 4 |  |
| E-UTRA RF Channel Number |  | 1, 2 | 1 |  |  |  | One E-UTRA carrier frequency is used. |
| NR RF Channel Number |  | 1, 2 | 1 |  |  |  | One FR2 NR carrier frequency is used. |
| Active cell |  | 1, 2 | E-UTRA Cell 1 (PCell) |  |  |  | E-UTRA Cell 1 is on E-UTRA RF channel number 1 as defined in clause A.3.7.2.2. |
| Neighbour cell |  | 1, 2 | NR Cell 2 |  |  |  | NR Cell 2 is on NR RF channel number 1. |
| Gap Pattern Id |  | 1, 2 | 0 |  | N/A |  | As specified in clause Table 8.1.2.1-1 of TS 36.133 [15]. |
| Measurement gap offset |  | 1, 2 | 39 |  | N/A |  | As specified in TS 36.331 [16]. |
| b1-ThresholdNR | dBm | 1, 2 | Note 1 |  |  |  | SS-RSRP threshold for SS-RSRP measurement on Cell 2 for event B1 [16] |
| Hysteresis | dB | 1, 2 | 0 |  |  |  |  |
| CP length |  | 1, 2 | Normal |  |  |  |  |
| TimeToTrigger | s | 1, 2 | 0 |  |  |  |  |
| Filter coefficient |  | 1, 2 | 0 |  |  |  | L3 filtering is not used |
| DRX |  |  | DRX.9 | DRX.12 | DRX.9 | DRX.12 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | 1 | 3 ms |  |  |  | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
|  |  | 2 | 3s |  |  |  | Synchronous cells. |
| T1 | s | 1, 2 | 5 |  |  |  |  |
| T2 | s | 1, 2 | 7 | 70 | 7 | 70 |  |
| NOTE 1: The value of b1-ThresholdNR is defined in table A.18.3.1. 8.1-3 |  |  |  |  |  |  |  |

Table A.18.3.1.8.1-3: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR2 with SSB time index detection

| Parameter |  | Unit | Test configuration | Cell 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 |
| AoA setup defined in clause A.3.15.1 |  |  | 1, 2 | Setup 1 |  |
| Assumption for UE beamsNote 5 |  |  | 1, 2 | Rough |  |
| NR RF Channel Number |  |  | 1, 2 | 1 |  |
| Duplex mode |  |  | 1, 2 | TDD |  |
| TDD configuration |  |  | 1, 2 | TDDConf.3.1 |  |
| BWchannel |  | MHz | 1, 2 | 100: NPRB,c = 66 |  |
| OCNG patterns defined in A.3.2.1.1 |  |  | 1, 2 | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  |  | 1 | SMTC.2 |  |
|  |  |  | 2 | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 1, 2 | 120 |  |
| b1-ThresholdNR | UE power class 3 | dBm/SCS | 1, 2 | -206 |  |
| EPRE ratio of PSS to SSS |  |  | 1, 2 | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | 1, 2 | -104.7 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | 1, 2 | -95.7 |  |
| SS-RSRP Note 3 |  | dBm/SCS | 1, 2 | -Infinity | -87.7 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 1, 2 | -Infinity | 8 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 1, 2 | -Infinity | 8 |
| IoNote3 |  | dBm/95.04 MHz | 1, 2 | -66.7 | -58. 0 |
| Propagation Condition |  |  | 1, 2 | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc]to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Information about types of UE beam is given in annex B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |  |  |

##### A.18.3.1.8.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D1 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D2 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 3 with per-FR gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D3 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 4 with per-FR gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D4 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1, 2, 3 and 4, the UE is required to report SSB time index.

Table A.18.3.1.8.2-1: Test requirements for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in DRX

| Test case | Measurement reporting delay (ms) |  |  |  |
| --- | --- | --- | --- | --- |
|  | Test 1: D1 ms | Test 2: D2 ms | Test 3: D3 ms | Test 4: D4 ms |
| UE power class 3 | 6240 | 66560 | 6240 | 66560 |

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.
