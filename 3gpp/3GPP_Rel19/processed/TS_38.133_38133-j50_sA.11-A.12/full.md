# A.11 NR Standalone Tests with NR PCell under CCA and Other NR Cells in FR1

Editor’s note: Test cases for NR SA with NR PCell under CCA and SCell under CCA are also included here.

## A.11.1 RRC_IDLE state mobility

### A.11.1.1 Cell re-selection with both source and target NR carrier frequencies under CCA

#### A.11.1.1.1 Cell reselection to FR1 intra-frequency NR cells when subject to CCA on the serving and target cell

##### A.11.1.1.1.1 Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements subject to CCA specified in clause 4.2A.2.3. Supported test configurations are shown in table A.11.1.1.1.2-1.

##### A.11.1.1.1.2 Test Parameters

The test scenario comprises of 1 NR carrier that is subject to CCA and 2 cells as given in tables A.11.1.1.1.2-1, A.11.1.1.1.2-2 and A.11.1.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.11.1.1.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | With CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

Table A.11.1.1.1.2-2: General test parameters for intra frequency NR cell re-selection test case when subject to CCA

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial | Active cell |  | 1 | Cell 1 |  |
| condition | Neighbour cells |  | 1 | Cell 2 |  |
| T2 end condition | Active cell |  | 1 | Cell 2 |  |
|  | Neighbour cells |  | 1 | Cell 1 |  |
| Final condition | Active cell |  | 1 | Cell 1 |  |
| RF Channel Number |  |  | 1 | 1 |  |
| Time offset between cells |  |  | 1 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1 | Not Sent | No additional delays in random access procedure. |
| SSB configuration | Semi-static channel access |  | 1 | SSB.1 CCA | (As defined in A.3.10A) |
|  | Dynamic channel access |  |  | SSB.2 CCA |  |
| DBT Window Configuration |  |  | 1 | DBT.1 | As specified in clause A.3.28.1. |
| SMTC confituration |  |  |  | SMTC.1 |  |
| DL CCA model |  |  | 1 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | 1 | As specified in clause A.3.26.2.2 |  |
| DRX cycle length |  | s | 1 | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1 | 102 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| rangeToBestCell |  |  | 1 | Not configured |  |
| T1 |  | s | 1 | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2 |
| T2 |  | s | 1 | 40 | T2 needs to be defined so that cell re-selection reaction time is taken into account. |
| T3 |  | s | 1 | 15 | T3 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.11.1.1.1.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case in AWGN when subject to CCA

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| TDD configuration |  | 1 | TDDConf.1.1 CCA |  |  | TDDConf.1.1 CCA |  |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | 1 | 0.9 |  |  | 0.9 |  |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_1) |  | 1 | 0.75 |  |  | 0.75 |  |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_2) |  | 1 | 0.5 |  |  | 0.5 |  |  |
| UL CCA probability PCCA_UL |  | 1 | 1 |  |  | 1 |  |  |
| Md,max |  | 1 | 16 |  |  | 16 |  |  |
| Mm,max |  | 1 | 4 |  |  | 4 |  |  |
| Me,max |  | 1 | 8 |  |  | 8 |  |  |
| PDSCH RMC |  | 1 | SR.1.1 CCA |  |  | SR.1.1 CCA |  |  |
| RMSI CORESET |  | 1 | CR.1.1 CCA |  |  | CR.1.1 CCA |  |  |
| Dedicated CORESET |  | 1 | CCR.1.1 CCA |  |  | CCR.1.1 CCA |  |  |
| OCNG Pattern |  | 1 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1 | SSB |  |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1 | -127 |  |  | -127 |  |  |
| Pcompensation | dB | 1 | 0 |  |  | 0 |  |  |
| Qhysts | dB | 1 | 0 |  |  | 0 |  |  |
| Qoffsets, n | dB | 1 | 0 |  |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1 | SS-RSRP |  |  | SS-RSRP |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1 | 16 | -3.11 | 2.79 | -infinity | 2.79 | -3.11 |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -95 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 16 | 13 | 16 | -infinity | 16 | 13 |
|  |  |  |  |  |  |  |  |  |
| SS-RSRP Note3 | dBm/SCS | 1 | -79 | -82 | -79 | -infinity | -79 | -82 |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| Io | dBm/38.16 MHz | 1 | -47.85 | -46.12 | -46.12 | Same as parameters specified in Cell 1 columns- |  |  |
| Treselection | s | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| SintrasearchP | dB | 1 | 50 |  |  | 50 |  |  |
| Propagation Condition |  | 1 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4:  For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |  |

##### A.11.1.1.1.3 Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than (25 + Md)*1.28 + TSI_CCA s. Md is the number of DRX cycles with at least one SMTC where there are no SSBs available during the Tdetect,NR_Intra_CCA. If Md > Md,max the UE is required to restart the detection of Cell 2.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than (5+Me)*1.28 + TSI_CCA s. Me is the number of DRX cycles with at least one SMTC where there are no SSBs available during the Tevaluate,NR_Intra_CCA. If Me > Me,max the UE is required to restart the evaluation of Cell 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra_CCA + TSI_CCA, and to an already detected cell can be expressed as: Tevaluate, NR_ intra_CCA + TSI_CCA,

Where:

- Tdetect, NR_Intra_CCA See Table 4.2A.2.3 clause 4.2A.2.3

- Tevaluate, NR_ intra_CCA See Table 4.2A.2.3-1 in clause 4.2A.2.3

- TSI_CCA Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell.

This gives a total of (25 + Md)*1.28 + TSI_CCA s for the cell re-selection delay to a newly detectable cell and (5+Me)*1.28 + TSI_CCA s for the cell re-selection delay to an already detected cell in the test case.

#### A.11.1.1.2 Cell reselection to FR1 inter-frequency NR case when subject to CCA on the serving and target cell

##### A.11.1.1.2.1 Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements subject to CCA specified in clause 4.2A.2.4. Supported test configurations are shown in table A.11.1.1.2.2-1.

##### A.11.1.1.2.2 Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers that are subject to CCA respectively as given in tables A.11.1.1.2.2-1, A.11.1.1.2.2-2 and A.11.1.1.2.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

Table A.11.1.1.2.2-1: Supported test configurations

| Configuration | Description of Cell 1 with CCA | Description of Cell 2 with CCA |
| --- | --- | --- |
| 1 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

Table A.11.1.1.2.2-2: General test parameters for FR1 inter frequency NR cell re-selection test case when subject to CCA

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1 | Cell 2 | The UE camps on Cell 2 in the initial phase and during T1 period the UE reselects to Cell 1 |
| T1 end condition | Active cell |  | 1 | Cell 1 | The UE shall perform reselection to Cell 1 during T1 |
|  | Neighbour cells |  | 1 | Cell 2 |  |
| T3 end condition | Active cell |  | 1 | Cell 2 | The UE shall perform reselection to Cell 2 with higher priority during T3 |
| RF Channel Number |  |  | 1 | 1, 2 |  |
| Time offset between cells |  |  | 1 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1 | Not Sent | No additional delays in random access procedure. |
| SSB configuration | Semi-static channel access |  | 1 | SSB.1 CCA (As defined in A.3.10A ) |  |
|  | Dynamic channel access |  |  | SSB.2 CCA (As defined in A.3.10A ) |  |
| DBT Window Configuration |  |  | 1 | DBT.1 | As specified in clause A.3.28.1. |
| SMTC configuration |  |  | 1 | SMTC.1 |  |
| DL CCA model |  |  | 1 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | 1 | As specified in clause A.3.26.2.2 |  |
| DRX cycle length |  | s | 1 | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1 | 102 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| rangeToBestCell |  |  | 1 | Not configured |  |
| T1 |  | s | 1 | 15 | T1 needs to be defined so that cell re-selection reaction time is taken into account. |
| T2 |  | s | 1 | >7 | During T2, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed. The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T3. |
| T3 |  | s | 1 | 75 | T3 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.11.1.1.2.2-3: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case in AWGN

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| TDD configuration |  | 1 | TDDConf.1.1 CCA |  |  | TDDConf.1.1 CCA |  |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | 1 | 0.9 |  |  | 0.9 |  |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_1) |  | 1 | 0.75 |  |  | 0.75 |  |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_2) |  | 2 | 0.5 |  |  | 0.5 |  |  |
| UL CCA probability PCCA_UL |  | 1 | 1 |  |  | 1 |  |  |
| Md,max |  | 1 | 16 |  |  | 16 |  |  |
| Mm,max |  | 1 | 4 |  |  | 4 |  |  |
| Me,max |  | 1 | 8 |  |  | 8 |  |  |
| PDSCH RMC |  | 1 | SR.1.1 CCA |  |  | SR.1.1 CCA |  |  |
| RMSI CORESET |  | 1 | CR.1.1 CCA |  |  | CR.1.1 CCA |  |  |
| Dedicated CORESET |  | 1 | CCR.1.1 CCA |  |  | CCR.1.1 CCA |  |  |
| OCNG Pattern |  | 1 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1 | SSB |  |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1 | -137 |  |  | -137 |  |  |
|  |  |  |  |  |  |  |  |  |
| Pcompensation | dB | 1 | 0 |  |  | 0 |  |  |
| Qhysts | dB | 1 | 0 |  |  | 0 |  |  |
| Qoffsets, n | dB | 1 | 0 |  |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1 | SS-RSRP |  |  | SS-RSRP |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1 | 14 | 14 | 14 | -4 | -infinity | 12 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -95 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 14 | 14 | 14 | -4 | -infinity | 12 |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| SS-RSRP Note3 | dBm/SCS | 1 | -81 | -81 | -81 | -99 | -infinity | -83 |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| Io | dBm/38.16 MHz | 1 | -49.79 | -49.79 | -49.79 | -65.50 | -infinity | -54.69 |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| Treselection | s | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| SnonintrasearchP | dB | 1 | 50 |  |  | 50 |  |  |
| Threshx, high | dB | 1 | 48 |  |  | 48 |  |  |
| Threshserving, low | dB | 1 | 44 |  |  | 44 |  |  |
| Threshx, low | dB | 1 | 50 |  |  | 50 |  |  |
| Propagation Condition |  | 1 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4:  For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |  |

##### A.11.1.1.2.3 Test Requirements

The cell reselection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps again on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 60 + 1.28 x (5 + Me) + TSI_CCA s. Me is the number of DRX cycles with at least one SMTC where there are no SSBs available during the Tevaluate,NR_Intra_CCA. If Me > Me,max the UE is required to restart the evaluation of Cell 2.

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to a lower priority cell shall be less than 1.28 x (5 + Me) + TSI_CCA s. Me is the number of DRX cycles with at least one SMTC where there are no SSBs available during the Tevaluate,NR_Intra_CCA. If Me > Me,max the UE is required to restart the evaluation of Cell 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter_CCA + TSI_CCA, and to a lower priority cell can be expressed as: Tevaluate, NR_ inter_CCA + TSI_CCA,

Where:

- Thigher_priority_search See clause 4.2.2.7

- Tevaluate, NR_ inter_CCA See Table 4.2A.2.4-1 in clause 4.2A.2.4

- TSI_CCA Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell.

This gives a total of 60 + 1.28 x (5 + Me) + TSI_CCA s for the cell re-selection delay to a higher priority cell and 1.28 x (5 + Me) + TSI_CCA s for the cell re-selection delay to a lower priority cell in the test case.

### A.11.1.2 Cell re-selection to NR with source NR carrier frequency under CCA

#### A.11.1.2.1 Cell reselection to FR1 inter-frequency NR case when serving cell is subject to CCA

##### A.11.1.2.1.1 Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements specified in clause 4.2.2.4 when the serving cell is subject to CCA. Supported test configurations are shown in table A.11.1.2.1.2-1.

##### A.11.1.2.1.2 Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers where the first carrier is subject to CCA as given in tables A.11.1.2.1.2-1, A.11.1.2.1.2-2 and A.11.1.2.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

Table A.11.1.2.1.2-1: Supported test configurations

| Configuration | Description of a cell with CCA | Description of a cell without CCA |
| --- | --- | --- |
| 1 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |  |

Table A.11.1.2.1.2-2: General test parameters for FR1 inter frequency NR cell re-selection test case when serving cell is subject to CCA

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2, 3 | Cell 2 | The UE camps on Cell 2 which is subject to CCA in the initial phase and during T1 period the UE reselects to Cell 1 which is an inter-frequency NR cell |
| T1 end condition | Active cell |  | 1, 2, 3 | Cell 1 | The UE shall perform reselection to Cell 1 during T1 |
|  | Neighbour cells |  | 1, 2, 3 | Cell 2 |  |
| T3 end condition | Active cell |  | 1, 2, 3 | Cell 2 | The UE shall perform reselection to Cell 2 with higher priority during T3 |
| RF Channel Number |  |  | 1, 2, 3 | 1, 2 |  |
| Time offset between cells |  |  | 1 | 3 ms | Asynchronous cells |
|  |  |  | 2 | 3 s | Synchronous cells |
|  |  |  | 3 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1, 2, 3 | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | 1 | Cell 1: SSB.1 FR1Cell 2: SSB.1 CCA for semi-static channel access;Cell 2: SSB.2 CCA for dynamic channel access |  |
|  |  |  | 2 | Cell 1: SSB.1 FR1Cell 2: SSB.1 CCA for semi-static channel access;Cell 2: SSB.2 CCA for dynamic channel access |  |
|  |  |  | 3 | Cell 1: SSB.2 FR1Cell 2: SSB.1 CCA for semi-static channel access;Cell 2: SSB.2 CCA for dynamic channel access |  |
| SMTC configuration |  |  | 1 | Cell 1: SMTC.1Cell 2: SMTC.1 |  |
|  |  |  | 2 | Cell 1: SMTC.1Cell 2: SMTC.1 |  |
|  |  |  | 3 | Cell 1: SMTC.1Cell 2: SMTC.1 |  |
| DBT Window Configuration |  |  | 1, 2, 3 | Cell 1: N/ACell 2: DBT.1 | As specified in clause A.3.28.1. |
| DL CCA model |  |  | 1, 2, 3 | Cell 1: N/ACell 2: As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | 1, 2, 3 | Cell 1: N/ACell 2: As specified in clause A.3.26.2.2 |  |
| DRX cycle length |  | s | 1, 2, 3 | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2, 3 | 102 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2, 3 | Not configured |  |
| T1 |  | s | 1, 2, 3 | 15 | T1 needs to be defined so that cell re-selection reaction time is taken into account. |
| T2 |  | s | 1, 2, 3 | >7 | During T2, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed. The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T3. |
| T3 |  | s | 1, 2, 3 | 75 | T3 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.11.1.2.1.2-3: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case in AWGN when serving cell is subject to CCA

| Parameter | Unit | Test configuration | Cell 1 |  |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |  | T1 | T2 | T3 |
| TDD configuration |  | 1 | N/A |  |  |  | TDDConf.1.1.CCA |  |  |
|  |  | 2 | TDDConf.1.1 |  |  |  | TDDConf.1.1.CCA |  |  |
|  |  | 3 | TDDConf.2.1 |  |  |  | TDDConf.1.1.CCA |  |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | 1, 2, 3 | N/A |  |  |  | 0.9 |  |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_1) |  | 1, 2, 3 | N/A |  |  |  | 0.75 |  |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_2) |  | 1, 2, 3 | N/A |  |  |  | 0.5 |  |  |
| UL CCA probability PCCA_UL |  | 1, 2, 3 | N/A |  |  |  | 1 |  |  |
| Md,max |  | 1, 2, 3 | N/A |  |  |  | 16 |  |  |
| Mm,max |  | 1, 2, 3 | N/A |  |  |  | 4 |  |  |
| Me,max |  | 1, 2, 3 | N/A |  |  |  | 8 |  |  |
| PDSCH RMC |  | 1 | SR.1.1 FDD |  |  |  | SR.1.1 CCA |  |  |
| configuration |  | 2 | SR.1.1 TDD |  |  |  | SR.1.1 CCA |  |  |
|  |  | 3 | SR.2.1 TDD |  |  |  | SR.1.1 CCA |  |  |
| RMSI CORESET |  | 1 | CR.1.1 FDD |  |  |  | CR.1.1 CCA |  |  |
| RMC configuration |  | 2 | CR.1.1 TDD |  |  |  | CR.1.1 CCA |  |  |
|  |  | 3 | CR.2.1 TDD |  |  |  | CR.1.1 CCA |  |  |
| Dedicated CORESET |  | 1 | CCR.1.1 FDD |  |  |  | CCR.1.1 CCA |  |  |
| RMC configuration |  | 2 | CCR.1.1 TDD |  |  |  | CCR.1.1 CCA |  |  |
|  |  | 3 | CCR.2.1 TDD |  |  |  | CCR.1.1 CCA |  |  |
| OCNG Pattern |  | 1, 2, 3 | OP.1 defined in A.3.2.1 |  |  |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1, 2, 3 | DLBWP.0.1 |  |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2, 3 | ULBWP.0.1 |  |  |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1, 2, 3 | SSB |  |  |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1, 2 | -140 |  |  |  | -137 |  |  |
|  |  | 3 | -137 |  |  |  | -137 |  |  |
| Pcompensation | dB | 1, 2, 3 | 0 |  |  |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2, 3 | SS-RSRP |  |  |  | SS-RSRP |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1 | 14 | 14 | 14 |  | -4 | -infinity | 12 |
|  |  | 2 |  |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -98 |  |  | -95 |  |  |  |
|  |  | 2 | -98 |  |  | -95 |  |  |  |
|  |  | 3 | -95 |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -98 |  |  |  |  |  |  |
|  |  | 2 |  |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 14 | 14 | 14 |  | -4 | -infinity | 12 |
|  |  | 2 |  |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |  |
| SS-RSRP Note3 | dBm/SCS | 1 | -84 | -84 | -84 |  | -99 | -infinity | -83 |
|  |  | 2 | -84 | -84 | -84 |  | -99 | -infinity | -83 |
|  |  | 3 | -81 | -81 | -81 |  | -99 | -infinity | -83 |
| Io | dBm/9.36 MHz | 1 | -55.88 | -55.88 | -55.88 |  | -65.50 | -66.96 | -54.69 |
|  | dBm/9.36 MHz | 2 | -55.88 | -55.88 | -55.88 |  | -65.50 | -66.96 | -54.69 |
|  | dBm/38.16 MHz | 3 | -49.79 | -49.79 | -49.79 |  | -65.50 | -66.96 | -54.69 |
| Treselection | s | 1, 2, 3 | 0 | 0 | 0 |  | 0 | 0 | 0 |
| SnonintrasearchP | dB | 1, 2, 3 | 50 |  |  |  | 50 |  |  |
| Threshx, highP | dB | 1, 2, 3 | 48 |  |  |  | 48 |  |  |
| Threshserving, lowP | dB | 1, 2, 3 | 44 |  |  |  | 44 |  |  |
| Threshx, lowP | dB | 1, 2, 3 | 50 |  |  |  | 50 |  |  |
| Propagation Condition |  | 1, 2, 3 | AWGN |  |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |  |  |

##### A.11.1.2.1.3 Test Requirements

The cell reselection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps again on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 60 + 1.28 x (5 + Me) + TSI_CCA s. Me is the number of DRX cycles with at least one SMTC where there are no SSBs available during the Tevaluate,NR_Intra_CCA. If Me > Me,max the UE is required to restart the evaluation of Cell 2.

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to a lower priority cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter_CCA + TSI_CCA, and to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR.

Where:

- Thigher_priority_search See clause 4.2.2.7

- Tevaluate, NR_ inter_CCA See Table 4.2A.2.4-1 in clause 4.2A.2.4

- TSI_CCA Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell.

- Tevaluate, NR_ inter See Table 4.2.2.4-1 in clause 4.2.2.4

- TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test cases.

This gives a total of 60 + 1.28 x (5 + Me) + TSI_CCA s for the cell re-selection delay to a higher priority cell and 7.68 s for the cell re-selection delay to a lower priority cell in the test case, which we allow 8 s.

### A.11.1.3 Cell re-selection from NR carrier with target NR carrier frequency under CCA

#### A.11.1.3.1 Cell reselection to FR1 inter-frequency NR case when target cell is subject to CCA

##### A.11.1.3.1.1 Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements specified in clause 4.2A.2.4 when the target cell is subject to CCA. Supported test configurations are shown in table A. 11.1.3.1.2-1.

##### A.11.1.3.1.2 Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers where the second carrier is subject to CCA as given in tables A.11.1.3.1.2-1, A.11.1.3.1.2-2 and A.11.1.3.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

Table A.11.1.3.1.2-1: Supported test configurations

| Configuration | Description of a cell without CCA | Description of a cell with CCA |
| --- | --- | --- |
| 1 | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |  |

Table A.11.1.3.1.2-2: General test parameters for FR1 inter frequency NR cell re-selection test case when target cell is subject to CCA

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2, 3 | Cell 2 | The UE camps on Cell 2 which is an inter-frequency NR cell in the initial phase and during T1 period the UE reselects to Cell 1 which is cell subject to CCA |
|  | Neighbour cell |  | 1, 2, 3 | Cell 1 |  |
| T1 end condition | Active cell |  | 1, 2, 3 | Cell 1 | The UE shall perform reselection to Cell 1 during T1 |
|  | Neighbour cells |  | 1, 2, 3 | Cell 2 |  |
| T3 end condition | Active cell |  | 1, 2, 3 | Cell 2 | The UE shall perform reselection to Cell 2 with higher priority during T3 |
|  | Neighbour cell |  | 1, 2, 3 | Cell 1 |  |
| RF Channel Number |  |  | 1, 2, 3 | 1, 2 |  |
| Time offset between cells |  |  | 1 | 3 ms | Asynchronous cells |
|  |  |  | 2 | 3 s | Synchronous cells |
|  |  |  | 3 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1, 2, 3 | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | 1 | Cell 1: SSB.1 CCA for semi-static channel access;Cell 1: SSB.2 CCA for dynamic channel access;Cell 2: SSB.1 FR1 |  |
|  |  |  | 2 | Cell 1: SSB.1 CCA for semi-static channel access;Cell 1: SSB.2 CCA for dynamic channel access;Cell 2: SSB.1 FR1 |  |
|  |  |  | 3 | Cell 1: SSB.1 CCA for semi-static channel access;Cell 1: SSB.2 CCA for dynamic channel access; Cell 2: SSB.2 FR1 |  |
| SMTC configuration |  |  | 1 | Cell 1:  SMTC.1Cell 2: SMTC.2 |  |
|  |  |  | 2 | Cell 1: SMTC.1Cell 2: SMTC.1 |  |
|  |  |  | 3 | Cell 1: SMTC.1Cell 2: SMTC.1 |  |
| DBT Window Configuration |  |  | 1, 2, 3 | Cell 1: DBT.1Cell 2: N/A | As specified in clause A.3.28.1. |
| DL CCA model |  |  | 1, 2, 3 | Cell 1: As specified in clause A.3.26.2.1Cell 2: N/A |  |
| UL CCA model |  |  | 1, 2, 3 | Cell 1: As specified in clause A.3.26.2.2Cell 2: N/A |  |
| DRX cycle length |  | s | 1, 2, 3 | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2, 3 | 102 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2, 3 | Not configured |  |
| T1 |  | s | 1, 2, 3 | 15 | T1 needs to be defined so that cell re-selection reaction time is taken into account. |
| T2 |  | s | 1, 2, 3 | >7 | During T2, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed. The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T3. |
| T3 |  | s | 1, 2, 3 | 75 | T3 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.11.1.3.1.2-3: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case in AWGN when target cell is subject to CCA

| Parameter | Unit | Test configuration | Cell 1 |  |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |  | T1 | T2 | T3 |
| TDD configuration |  | 1 | TDDConf.1.1.CCA |  |  |  | N/A |  |  |
|  |  | 2 | TDDConf.1.1.CCA |  |  |  | TDDConf.1.1 |  |  |
|  |  | 3 | TDDConf.1.1.CCA |  |  |  | TDDConf.2.1 |  |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | 1, 2, 3 | 0.9 |  |  |  | N/A |  |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_1) |  | 1, 2, 3 | 0.75 |  |  |  | N/A |  |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_2) |  | 1, 2, 3 | 0.5 |  |  |  | N/A |  |  |
| UL CCA probability PCCA_UL |  | 1, 2, 3 | 1 |  |  |  | N/A |  |  |
| Md,max |  | 1, 2, 3 | 16 |  |  |  | N/A |  |  |
| Mm,max |  | 1, 2, 3 | 4 |  |  |  | N/A |  |  |
| Me,max |  | 1, 2, 3 | 8 |  |  |  | N/A |  |  |
| PDSCH RMC |  | 1 | SR.1.1 CCA |  |  |  | SR.1.1 FDD |  |  |
| configuration |  | 2 | SR.1.1 CCA |  |  |  | SR.1.1 TDD |  |  |
|  |  | 3 | SR.1.1 CCA |  |  |  | SR.2.1 TDD |  |  |
| RMSI CORESET |  | 1 | CR.1.1 CCA |  |  |  | CR.1.1 FDD |  |  |
| RMC configuration |  | 2 | CR.1.1 CCA |  |  |  | CR.1.1 TDD |  |  |
|  |  | 3 | CR.1.1 CCA |  |  |  | CR.2.1 TDD |  |  |
| Dedicated CORESET |  | 1 | CCR.1.1 CCA |  |  |  | CCR.1.1 FDD |  |  |
| RMC configuration |  | 2 | CCR.1.1 CCA |  |  |  | CCR.1.1 TDD |  |  |
|  |  | 3 | CCR.1.1 CCA |  |  |  | CCR.2.1 TDD |  |  |
| OCNG Pattern |  | 1, 2, 3 | OP.1 defined in A.3.2.1 |  |  |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1, 2, 3 | DLBWP.0.1 |  |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2, 3 | ULBWP.0.1 |  |  |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1, 2, 3 | SSB |  |  |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1, 2 | -137 |  |  |  | -140 |  |  |
|  |  | 3 | -137 |  |  |  | -137 |  |  |
| Pcompensation | dB | 1, 2, 3 | 0 |  |  |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2, 3 | SS-RSRP |  |  |  | SS-RSRP |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1 | 14 | 14 | 14 |  | -4 | -infinity | 12 |
|  |  | 2 |  |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -95 |  |  | -98 |  |  |  |
|  |  | 2 | -95 |  |  | -98 |  |  |  |
|  |  | 3 | -95 |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -98 |  |  |  |  |  |  |
|  |  | 2 |  |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 14 | 14 | 14 |  | -4 | -infinity | 12 |
|  |  | 2 |  |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |  |
| SS-RSRP Note3 | dBm/SCS | 1 | -81 | -81 | -81 |  | -102 | -infinity | -86 |
|  |  | 2 | -81 | -81 | -81 |  | -102 | -infinity | -86 |
|  |  | 3 | -81 | -81 | -81 |  | -99 | -infinity | -83 |
| Io | dBm/9.36 MHz | 1 | -- | -- | -- |  | -68.60 | -70.05 | -57.78 |
|  | dBm/9.36 MHz | 2 | -- | -- | -- |  | -68.60 | -70.05 | -57.78 |
|  | dBm/38.16 MHz | 3 | -49.79 | -49.79 | -49.79 |  | -65.50 | -66.96 | -54.69 |
| Treselection | s | 1, 2, 3 | 0 | 0 | 0 |  | 0 | 0 | 0 |
| SnonintrasearchP | dB | 1, 2, 3 | 50 |  |  |  | 50 |  |  |
| Threshx, highP | dB | 1, 2, 3 | 48 |  |  |  | 48 |  |  |
| Threshserving, lowP | dB | 1, 2, 3 | 44 |  |  |  | 44 |  |  |
| Threshx, lowP | dB | 1, 2, 3 | 50 |  |  |  | 50 |  |  |
| Propagation Condition |  | 1, 2, 3 | AWGN |  |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |  |  |

##### A.11.1.3.1.3 Test Requirements

The cell reselection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps again on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

## 1.28 x (5 + Me) + TSI_CCA s. Me is the number of DRX cycles with at least one SMTC where there are no SSBs available during the Tevaluate,NR_Intra_CCA. If Me > Me,max the UE is required to restart the evaluation of Cell 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR.

Where:

- Thigher_priority_search See clause 4.2.2.7

- Tevaluate, NR_ inter_CCA See Table 4.2A.2.4-1 in clause 4.2A.2.4

- TSI_CCA Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell.

- Tevaluate, NR_ inter See Table 4.2.2.4-1 in clause 4.2.2.4

- TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority cell and 1.28 x (5 + Me) + TSI_CCA s for the cell re-selection delay to a lower priority cell in the test case.

### A.11.1.4 Inter-RAT cell re-selection to E-UTRAN with source NR carrier frequency under CCA

#### A.11.1.4.1 Cell reselection to higher priority E-UTRAN when serving cell is subject to CCA

##### A.11.1.4.1.1 Test Purpose and Environment

This test is to verify the requirement for the NR cell subject to CCA to E-UTRAN inter-RAT cell reselection requirements specified in clause 4.2A.2.5 when the E-UTRAN cell is of higher priority.

##### A.11.1.4.1.2 Test Parameters

The test scenario comprises of one NR cell which is subject to CCA and one E-UTRAN cell as given in tables A.11.1.4.1.2-1, A.11.1.4.1.2-2, A.11.1.4.1.2-3 and A.11.1.4.1.2-4. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. NR Cell 1 is already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of higher priority than Cell 1.

Table A.11.1.4.1.2-1: Supported test configurations

| Configuration | Description of a cell with CCA | Description of a cell without CCA |
| --- | --- | --- |
| 1 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | LTE 10 MHz bandwidth, TDD duplex mode |
| 2 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | LTE 10 MHz bandwidth, FDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |  |

Table A.11.1.4.1.2-2: General test parameters for NR cell subject to CCA to E-UTRAN cell re-selection test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2 | Cell 1 | The UE camps on Cell 1 in the initial phase and during T2 period the UE reselects to Cell 2. |
| T2 end | Active cell |  | 1, 2 | Cell 2 | The UE shall perform reselection to cell |
| condition | Neighbour cells |  | 1, 2 | Cell 1 | 2 during T2. |
| T3 end | Active cell |  | 1, 2 | Cell 1 | The UE shall perform reselection to cell |
| condition | Neighbour cells |  | 1, 2 | Cell 2 | 1 during T3 for iteration of the tests. |
| Access Barring Information |  | - | 1, 2 | Not Sent | No additional delays in random access procedure. |
| SMTC configuration |  |  | 1, 2 | SMTC.1 |  |
| DBT Window Configuration |  |  | 1, 2 | DBT.1 | As specified in clause A.3.28.1. |
| SSB configuration |  |  |  | Cell 1: SSB.1 CCA for semi-static channel access;Cell 1: SSB.2 CCA for dynamic channel access; |  |
| DL CCA model |  |  | 1, 2 | As specified in clauseA.3.26.2.1 |  |
| UL CCA model |  |  | 1, 2 | As specified in clause A.3.26.2.2 |  |
| DRX cycle length |  | s | 1, 2 | 1.28 | The value shall be used for all cells in the test. |
| NR PRACH configuration index |  |  | 1, 2 | 102 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| E-UTRAN PRACH configuration index |  |  | 1 | 53 | As specified in table 5.7.1-2 in TS 36.211 [23] |
|  |  |  | 2 | 4 |  |
| E-UTRAN PRACH |  |  | 1 | 53 | As specified in table 5.7.1-2 in |
| configuration index |  |  | 2 | 4 | TS 36.211 [23] |
| T1 |  | s | 1, 2 | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed. The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2. |
| T2 |  | s | 1, 2 | 75 | T2 needs to be defined so that cell re-selection reaction time is taken into account. |
| T3 |  | s | 1, 2 | 15 | T3 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.11.1.4.1.2-3: Cell specific test parameters for NR Cell 1 subject to CCA

| Parameter | Unit | Test configuration | Cell 1 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| TDD configuration |  | 1, 2 | TDDConf.1.1.CCA |  |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | 1, 2 | 0.9 |  |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_1) |  | 1, 2 | 0.75 |  |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_2) |  | 1, 2 | 0.5 |  |  |
| UL CCA probability PCCA_UL |  | 1, 2 | 1 |  |  |
| Md,max |  | 1, 2 | 16 |  |  |
| Mm,max |  | 1, 2 | 4 |  |  |
| Me,max |  | 1, 2 | 8 |  |  |
| PDSCH parameters |  | 1, 2 | SR.1.1 CCA |  |  |
| RMSI CORESET parameters |  | 1, 2 | CR.1.1 CCA |  |  |
| Dedicated CORESET parameters |  | 1, 2 | CCR.1.1 CCA |  |  |
| SSB parameters |  | 1, 2 | SSB.1 CCA for semi-static channel access;SSB.2 CCA for dynamic channel access |  |  |
| NR SMTC parameters |  | 1, 2 | SMTC.1 |  |  |
| OCNG Pattern |  | 1, 2 | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1, 2 | DLBWP.0 |  |  |
| Initial UL BWP configuration |  | 1, 2 | ULBWP.0 |  |  |
| RLM-RS |  | 1, 2 | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1, 2 | -137 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] | dBm/SCS | 1, 2 | -95 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] | dBm/15 kHz | 1, 2 | -98 |  |  |
| SS-RSRP |  | 1, 2 | -81 | -81 | -81 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2 | 14 | 14 | 14 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2 | 14 | 14 | 14 |
| Io | dBm/38.16 MHz | 1, 2 | -49.79 | -49.79 | -49.79 |
| Treselection | s | 1, 2 | 0 |  |  |
| Snonintrasearch | dB | 1, 2 | 50 |  |  |
| Threshx, high (Note 2) | dB | 1, 2 | 48 |  |  |
| Threshserving, low | dB | 1, 2 | 44 |  |  |
| Threshx, low | dB | 1, 2 | 50 |  |  |
| Propagation Condition |  | 1, 2 | AWGN |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: This refers to the value of  Threshx, high  which is included in NR system information, and is a threshold for the E-UTRA target cellNOTE 3: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |

Table A.11.1.4.1.2-4: Cell specific test parameters for E-UTRA Cell 2

| Parameter | Unit | Cell 2 |  |  |
| --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 |
| E-UTRA RF Channel number |  | 1 |  |  |
| BWchannel | MHz | 10 |  |  |
| OCNG Patterns defined in TS 36.133 [15] clause A.3.2 |  | OP.2 TDD for test configuration 1, 2, 3;OP.2 FDD for test configuration 4, 5, 6 |  |  |
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
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] | dBm/15 kHz | -98 |  |  |
| RSRP | dBm/15 KHz | -infinity | -86 | -102 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | -infinity | 12 | -4 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{N}oc] | dB | -infinity | 12 | -4 |
| TreselectionEUTRAN | s | 0 |  |  |
| Snonintrasearch | dB | 50 |  |  |
| Threshx, high (Note 2) | dB | 48 |  |  |
| Threshserving, low | dB | 44 |  |  |
| Threshx, low | dB | 50 |  |  |
| Propagation Condition |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: This refers to the value of  Threshx, high  which is included in E-UTRA system information, and is a threshold for the NR target cell |  |  |  |  |

##### A.11.1.4.1.3 Test Requirements

The cell reselection delay to a higher priority E-UTRAN cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, E-UTRAN + TSI-E-UTRA,

Where:

- Thigher_priority_search See clause 4.2.2.7

- Tevaluate, E-UTRAN See Table 4.2.2.5-1 in clause 4.2.2.5

- TSI-E-UTRA Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority E-UTRAN cell.

#### A.11.1.4.2 Cell reselection to lower priority E-UTRAN when serving cell is subject to CCA

##### A.11.1.4.2.1 Test Purpose and Environment

This test is to verify the requirement for the NR cell subject to CCA to E-UTRAN inter-RAT cell reselection requirements specified in clause 4.2A.2.5 when the E-UTRAN cell is of lower priority.

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A.11.1.4.2.1-1, A.11.1.4.2.1-2, A.11.1.4.2.1-3 and A.11.1.4.2.1-4. The test consists of three successive time periods, with time duration of T1 and T2 respectively. Both NR Cell 1 and E-UTRAN Cell 2 are already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of lower priority than Cell 1.

Table A.11.1.4.2.1-1: Supported test configurations

| Configuration | Description of a cell with CCA | Description of a cell without CCA |
| --- | --- | --- |
| 1 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | LTE 10 MHz bandwidth, TDD duplex mode |
| 2 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | LTE 10 MHz bandwidth, FDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |  |

Table A.11.1.4.2.1-2: General test parameters for NR cell subject to CCA to E-UTRAN cell re-selection test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2 | Cell 1 | The UE camps on Cell 1 in the initial phase. |
| T1 end condition | Active cell |  | 1, 2 | Cell 2 | The UE shall perform reselection to Cell 2 during T1. |
|  | Neighbour cells |  | 1, 2 | Cell 1 |  |
| T2 end condition | Active cell |  | 1, 2 | Cell 1 | The UE shall perform reselection to Cell 1 during T2 for iteration of the tests. |
|  | Neighbour cells |  | 1, 2 | Cell 2 |  |
| Access Barring Information |  | - | 1, 2 | Not Sent | No additional delays in random access procedure. |
| SMTC configuration |  |  | 1, 2 | SMTC.1 |  |
| DBT Window Configuration |  |  | 1, 2 | DBT.1 | As specified in clause A.3.28.1. |
| DL CCA model |  |  | 1, 2 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | 1, 2 | As specified in clause A.3.26.2.2 |  |
| DRX cycle length |  | s | 1, 2 | 1.28 | The value shall be used for all cells in the test. |
| NR PRACH configuration index |  |  | 1, 2 | 102 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| E-UTRAN PRACH |  |  | 1 | 53 | As specified in table 5.7.1-2 in TS 36.211 [23] |
| configuration index |  |  | 2 | 4 |  |
| T1 |  | s | 1, 2 | 15 | T1 needs to be defined so that cell re-selection reaction time is taken into account. |
| T2 |  | s | 1, 2 | 75 | T2 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.11.1.4.2.1-3: Cell specific test parameters for NR Cell 1 subject to CCA

| Parameter | Unit | Test configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| TDD configuration |  | 1, 2 | TDDConf.1.1.CCA |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | 1, 2 | 0.9 |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_1) |  | 1, 2 | 0.75 |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_2) |  | 1, 2 | 0.5 |  |
| UL CCA probability PCCA_UL |  | 1, 2 | 1 |  |
| Md,max |  | 1, 2 | 16 |  |
| Mm,max |  | 1, 2 | 4 |  |
| Me,max |  | 1, 2 | 8 |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 CCA |  |
| RMSI CORESET RMC Configuration |  | 1, 2 | CR.1.1 CCA |  |
| Dedicated CORESET RMC |  | 1, 2 | CCR.1.1 CCA |  |
| Configuration |  |  |  |  |
| SSB configuration |  | 1, 2 | SSB.1 CCA for semi-static channel access;SSB.2 CCA for dynamic channel access |  |
|  |  |  |  |  |
| SMTC configuration |  | 1, 2 | SMTC.1 |  |
|  |  |  |  |  |
|  |  |  |  |  |
| OCNG Pattern |  | 1, 2 | OP.1 defined in A.3.2.1 |  |
| Initial DL BWP configuration |  | 1, 2 | DLBWP.0 |  |
| Initial UL BWP configuration |  | 1, 2 | ULBWP.0 |  |
| RLM-RS |  | 1, 2 | SSB |  |
| Qrxlevmin | dBm/SCS | 1, 2 | -137 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] | dBm/SCS | 1, 2 | -95 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] | dBm/15 kHz | 1, 2 | -98 |  |
| SS-RSRP | dBm/SCS | 1, 2 | -99 | -83 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2 | -4 | 12 |
|  |  |  |  |  |
|  |  |  |  |  |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2 | -4 | 12 |
|  |  |  |  |  |
|  |  |  |  |  |
| Io | dBm/38.16 MHz | 1, 2 | -62.50 | -51.69 |
| Treselection | s | 1, 2 | 0 |  |
| Snonintrasearch | dB | 1, 2 | 50 |  |
| Threshx, high (Note 2) | dB | 1, 2 | 48 |  |
| Threshserving, low | dB | 1, 2 | 44 |  |
| Threshx, low | dB | 1, 2 | 50 |  |
| Propagation Condition |  | 1, 2 | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: This refers to the value of  Threshx, high  which is included in NR system information, and is a threshold for the E-UTRA target cellNOTE 3: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |

Table A.11.1.4.2.1-4: Cell specific test parameters for E-UTRA Cell 2

| Parameter | Unit | Cell 2 |  |
| --- | --- | --- | --- |
|  |  | T1 | T2 |
| E-UTRA RF Channel number |  | 1 |  |
| BWchannel | MHz | 10 |  |
| OCNG Patterns defined in TS 36.133 [15] clause A.3.2 |  | OP.2 TDD for test configuration 1, 2, 3;OP.2 FDD for test configuration 4, 5, 6 |  |
| PBCH_RA | dB | 0 |  |
| PBCH_RB | dB |  |  |
| PSS_RA | dB |  |  |
| SSS_RA | dB |  |  |
| PCFICH_RB | dB |  |  |
| PHICH_RA | dB |  |  |
| PHICH_RB | dB |  |  |
| PDCCH_RA | dB |  |  |
| PDCCH_RB | dB |  |  |
| PDSCH_RA | dB |  |  |
| PDSCH_RB | dB |  |  |
| OCNG_RANote 1 | dB |  |  |
| OCNG_RBNote 1 | dB |  |  |
| Qrxlevmin | dBm | -140 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] | dBm/15 kHz | -98 |  |
| RSRP | dBm/15 KHz | -84 | -84 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 14 | 14 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 14 | 14 |
| TreselectionEUTRAN | s | 0 |  |
| Snonintrasearch | dB | 50 |  |
| Threshx, high (Note 2) | dB | 48 |  |
| Threshserving, low | dB | 44 |  |
| Threshx, low | dB | 50 |  |
| Propagation Condition |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: This refers to the value of  Threshx, high  which is included in E-UTRA system information, and is a threshold for the NR target cell |  |  |  |

##### A.11.1.4.2.2 Test Requirements

The cell reselection delay to a lower priority E-UTRAN cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a lower priority cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, E-UTRAN + TSI-E-UTRA,

Where:

- Tevaluate, E-UTRAN See Table 4.2.2.5-1 in clause 4.2.2.5

- TSI-E-UTRA Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 7.68 s, allow 8 s for the cell re-selection delay to a lower priority E-UTRAN cell.

## A.11.2 RRC_CONNECTED state mobility

### A.11.2.1 Handover

#### A.11.2.1.1 Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; known target cell

##### A.11.2.1.1.1 Test Purpose and Environment

This test is to verify the requirement for the NR intra frequency handover requirements from FR1 carrier under CCA to FR1 carrier under CCA specified in clause 6.1B.1.2.

##### A.11.2.1.1.2 Test Parameters

Supported test configurations are shown in table A.11.2.1.1.2-1. Both handover delay and interruption length are tested by using the parameters in table A.11.2.1.1.2-2, and A.11.2.1.1.2-3.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

NR shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.11.2.1.1.2-1: Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA test configurations

| Config | Description |
| --- | --- |
| 1 | Source cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

Table A.11.2.1.1.2-2: General test parameters Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 | On the carrier under CCA |
|  | Neighbouring cell |  | Cell 2 | On the carrier under CCA |
| Final condition | Active cell |  | Cell 2 | On the carrier under CCA |
| DL CCA model | Dynamic channel accessNote 1, 3 |  | As specified in clause A.3.26.2.1 |  |
|  | Semi-static channel access Note 2, 3 |  |  |  |
| UL CCA model | Dynamic channel access Note 1, 3 |  | As specified in clause A.3.26.2.2 |  |
|  | Semi-static channel access Note 2,3 |  |  |  |
| A3-Offset |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T304 |  | ms | 500 |  |
| LCCA_DL |  |  | 5 |  |
| WCCA_DL |  | ms | T304 |  |
| LCCA_UL |  |  | 5 |  |
| WCCA_UL |  | ms | T304 |  |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |
| T3 |  | s | ≥ Tinterrupt | Tinterrupt is defined in clause 6.1B.1.2 |
| NOTE 1: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 2: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.11.2.1.1.2-3: Cell specific test parameters for NR FR1-FR1 Intra frequency handover test case

| Parameter |  |  | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| NR RF Channel Number |  |  |  | 1 |  |  | 1 |  |  |
| PCCA_DL for dynamic channel access Note 4,6 |  |  | - | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |
| PCCA_DL for semi-static channel access Note 5,6 |  |  | - | PCCA_DL=0.9375 |  |  | PCCA_DL=0.9375 |  |  |
| PCCA_UL for dynamic channel access Note 4,6 |  |  | - | 0.75 |  |  | 0.75 |  |  |
| PCCA_UL for semi-static channel access Note 5,6 |  |  | - | 0.87 |  |  | 0.87 |  |  |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |  |  |  |  |
| BWchannel |  | Config 1 |  | 40: NPRB,c = 106 |  |  |  |  |  |
| BWP BW |  | Config 1 |  | 40: NPRB,c = 106 |  |  |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |  |
| PDSCH Reference |  | Config 1 |  | SR.1.1 CCA |  |  |  |  |  |
| CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA |  |  |  |  |  |
| Dedicated CORESET RMC configuration |  | Config 1 |  | CCR.1.1 CCA |  |  |  |  |  |
| TRS configuration |  | Config 1 |  | TRS.1.1 TDD |  |  |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |  |  |
| DBT window configuration |  | Config 1 |  | DBT.1 |  |  |  |  |  |
| SSB configuration for semi-static channel accessNote 4, 6 |  | Config 1 |  | SSB.1 CCA |  |  |  |  |  |
| SSB configuration for dynamic channel accessNote 5, 6 |  | Config 1 |  | SSB.2 CCA |  |  |  |  |  |
| ssb-PositionQCL |  | Config 1 |  | [1] |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 | kHz | 30 kHz |  |  |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1 | kHz | 30 kHz |  |  |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 under CCA |  |  |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | -98 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 |  | dBm/SCS | -95 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 8 | -3.3 | -3.3 | -Infinity | 2.36 | 2.36 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 8 | 8 | 8 | -Infinity | 11 | 11 |
| SSB_RP | Config 1 |  | dBm/SCS | -87 | -87 | -87 | -Infinity | -84 | -84 |
| IoNote3 | Config 1 |  | dBm/38.16 MHz | -55.31 | -50.96 | -50.96 | -55.31 | -50.96 | -50.96 |
| Propagation condition |  |  | - | AWGN |  |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 6: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |  |  |

##### A.11.2.1.1.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than Tinterrupt from the beginning of time period T3, where Tinterrupt is defined in clause 6.1B.1.2

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin

Tsearch = 0.

Tprocessing = 20 ms.

Tmargin = 2 ms.

T∆ = (1+ L2) *20 ms.

TIU = (1+ L3)*10 + 10 ms

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2], L2 is the number of SMTC occasions not available at the UE during the time tracking period where L2  LCCA_DL, and L3 is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure, where L3  LCCA_UL. L3 = 0 for Type 2C UL channel access procedure as defined in TS 37.213 [33]. The interruption time considering the potential extensions caused by L1, L2 , L3  and by the UL CCA failure detection/recovery mechanism is limited by the T304 timer. The UE behaviour at the T304 timer expiry is detailed in TS 38.331 [2]. Test equipment should make sure that LCCA_DL and LCCA_UL are not exceeded during a test by monitoring the number of CCA failures and preventing additional CCA failures from happening after LCCA_DL or LCCA_UL is reached.

#### A.11.2.1.2 Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; unknown target cell

##### A.11.2.1.2.1 Test Purpose and Environment

This test is to verify the requirement intra frequency handover requirements from FR1 carrier under CCA to FR1 carrier under CCA specified in clause 6.1B.1.2.

##### A.11.2.1.2.2 Test Parameters

Supported test configurations are shown in table A.11.2.1.2.2-1. Both handover delay and interruption length are tested by using the parameters in table A.11.2.1.2.2-2, and A.11.2.1.2.2-3.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.11.2.1.2.2-1: Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA test configurations

| Config | Description |
| --- | --- |
| 1 | Source cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

Table A.11.2.1.2.2-2: General test parameters Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 | On the carrier under CCA |
|  | Neighbouring cell |  | Cell 2 | On the carrier under CCA |
| Final condition | Active cell |  | Cell 2 | On the carrier under CCA |
| DL CCA model | Dynamic channel accessNote 1, 3 |  | As specified in clause A.3.26.2.1 |  |
|  | Semi-static channel access Note 2, 3 |  |  |  |
| UL CCA model | Dynamic channel access Note 1, 3 |  | As specified in clause A.3.26.2.2 |  |
|  | Semi-static channel access Note 2,3 |  |  |  |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T304 |  | ms | 500 |  |
| LCCA_DL |  |  | 5 |  |
| WCCA_DL |  | ms | T304 |  |
| LCCA_UL |  |  | 5 |  |
| WCCA_UL |  | ms | T304 |  |
| T1 |  | s | 5 |  |
| T2 |  | s | ≥ Tinterrupt | Tinterrupt is defined in clause 6.1B.1.2 |
| NOTE 1: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 2: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.11.2.1.2.2-3: Cell specific test parameters for NR FR1-FR1 Intra frequency handover test case

| Parameter |  |  | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | 1 |  | 1 |  |
| PCCA_DL for dynamic channel access Note 4,6 |  |  | - | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| PCCA_DL for semi-static channel access Note 5,6 |  |  | - | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
| PCCA_UL for dynamic channel access Note 4,6 |  |  | - | 0.75 |  | 0.75 |  |
| PCCA_UL for semi-static channel access Note 5,6 |  |  | - | 0.87 |  | 0.87 |  |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  | Config 1 |  | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  | Config 1 |  | 40: NPRB,c = 106 |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference |  | Config 1 |  | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA |  |  |  |
| Dedicated CORESET RMC configuration |  | Config 1 |  | CCR.1.1 CCA |  |  |  |
| TRS configuration |  | Config 1 |  | TRS.1.2 TDD |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |
| DBT window configuration |  | Config 1 |  | DBT.1 |  |  |  |
| SSB configuration for semi-static channel access Note 4, 6 |  | Config 1 |  | SSB.1 CCA |  |  |  |
| SSB configuration for dynamic channel access Note 5, 6 |  | Config 1 |  | SSB.2 CCA |  |  |  |
| ssb-PositionQCL |  | Config 1 |  | [1] |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 | kHz | 30 kHz |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1 | kHz | 30 kHz |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 under CCA |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | -98 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 |  | dBm/SCS | -95 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 8 | -0.64 | -Infinity | -0.64 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 8 | 8 | -Infinity | 8 |
| SSB_RP | Config 1 |  | dBm/SCS | -87 | -87 | -Infinity | -87 |
| IoNote3 | Config 1 |  | dBm/38.16 MHz | -55.31 | -52.60 | -55.31 | -52.60 |
| Propagation condition |  |  | - | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 6: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |

##### A.11.2.1.2.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than Tinterrupt from the beginning of time period T3, where Tinterrupt is defined in clause 6.1B.1.2

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin

Tsearch = (1+L1)* 20 ms.

Tprocessing = 20 ms.

Tmargin = 2 ms.

T∆ = (1+ L2) *20 ms.

TIU = (1+ L3)*10 + 10 ms

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2], L1 is the number of SMTC occasions not available at the UE during the intra-frequency detection period, L2 is the number of SMTC occasions not available at the UE during the time tracking period, where L1 + L2  LCCA_DL, and L3 is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure, where L3  LCCA_UL. L3 = 0 for Type 2C UL channel access procedure as defined in TS 37.213 [33]. The interruption time considering the potential extensions caused by L1, L2 , L3  and by the UL CCA failure detection/recovery mechanism is limited by the T304 timer.

#### A.11.2.1.3 Inter-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; unknown target cell

##### A.11.2.1.3.1 Test Purpose and Environment

This test is to verify the requirement for inter frequency handover requirements from FR1 carrier under CCA to FR1 carrier under CCA specified in clause 6.1B.1.2.

##### A.11.2.1.3.2 Test Parameters

Supported test configurations are shown in table A.11.2.1.3.2-1. Both handover delay and interruption length are tested by using the parameters in table A.11.2.1.3.2-2, and A.11.2.1.3.2-3.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.11.2.1.3.2-1: Inter-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA test configurations

| Config | Description |
| --- | --- |
| 1 | Source cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

Table A.11.2.1.3.2-2: General test parameters Inter-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 | On the carrier under CCA |
|  | Neighbouring cell |  | Cell 2 | On the carrier under CCA |
| Final condition | Active cell |  | Cell 2 | On the carrier under CCA |
| DL CCA model | Dynamic channel accessNote 1, 3 |  | As specified in clause A.3.26.2.1 |  |
|  | Semi-static channel access Note 2, 3 |  |  |  |
| UL CCA model | Dynamic channel access Note 1, 3 |  | As specified in clause A.3.26.2.2 |  |
|  | Semi-static channel access Note 2,3 |  |  |  |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| T304 |  | ms | 500 |  |
| LCCA_DL |  |  | 5 |  |
| WCCA_DL |  | ms | T304 |  |
| LCCA_UL |  |  | 5 |  |
| WCCA_UL |  | ms | T304 |  |
| T1 |  | s | 5 |  |
| T2 |  | s | Tinterrupt | Tinterrupt is defined in clause 6.1B.1.2 |
| NOTE 1: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 2: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.11.2.1.3.2-3: Cell specific test parameters for NR FR1-FR1 Inter frequency handover test case

| Parameter |  |  | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | 1 |  | 2 |  |
| PCCA_DL for dynamic channel access Note 4,6 |  |  | - | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| PCCA_DL for semi-static channel access Note 5,6 |  |  | - | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
| PCCA_UL for dynamic channel access Note 4,6 |  |  | - | 0.75 |  | 0.75 |  |
| PCCA_UL for semi-static channel access Note 5,6 |  |  | - | 0.87 |  | 0.87 |  |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  | Config 1 |  | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  | Config 1 |  | 40: NPRB,c = 106 |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference |  | Config 1 |  | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  | Config 1 |  | CR1.1 CCA |  |  |  |
| Dedicated CORESET RMC configuration |  | Config 1 |  | CCR.1.1 CCA |  |  |  |
| TRS configuration |  | Config 1 |  | TRS.1.2 TDD |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |
| DBT window configuration |  | Config 1 |  | DBT.1 |  |  |  |
| SSB configuration for semi-static channel access Note 4, 6 |  | Config 1 |  | SSB.1 CCA |  |  |  |
| SSB configuration for dynamic channel access Note 5, 6 |  | Config 1 |  | SSB.2 CCA |  |  |  |
| ssb-PositionQCL |  | Config 1 |  | [1] |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 | kHz | 30 kHz |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1 | kHz | 30 kHz |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 under CCA |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | -98 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 |  | dBm/SCS | -95 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 4 | 4 | -Infinity | 5 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4 | 4 | -Infinity | 5 |
| SSB_RP | Config 1 |  | dBm/SCS | -91 | -91 | -Infinity | -90 |
| IoNote3 | Config 1 |  | dBm/38.16 MHz | -58.49 | -58.49 | -63.94 | -57.75 |
| Propagation condition |  |  | - | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 6: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |

##### A.11.2.1.3.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than Tinterrupt from the beginning of time period T3, where Tinterrupt is defined in clause 6.1B.1.2

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin

Tsearch = (3+L1’)* 20 ms.

Tprocessing = 20 ms.

Tmargin = 2 ms.

T∆ = (1+ L2) *20 ms.

TIU = (1+ L3)*10 + 10 ms

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2], L1’ is the number of SMTC occasions not available at the UE during the inter-frequency detection period, L2 is the number of SMTC occasions not available at the UE during the time tracking period, where L1’ + L2  LCCA_DL, and L3 is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure, where L3  LCCA_UL. L3 = 0 for Type 2C UL channel access procedure as defined in TS 37.213 [33]. The interruption time considering the potential extensions caused by , L1, L2 , L3  and by the UL CCA failure detection/recovery mechanism is limited by the T304 timer.

#### A.11.2.1.4 Inter-frequency handover from FR1 carrier under CCA to FR1; known target cell

##### A.11.2.1.4.1 Test Purpose and Environment

This test is to verify the requirement for the NR with CCA FR1-NR FR1 handover requirements specified in clause6.1.1.2.

##### A.11.2.1.4.2 Test Parameters

Supported test configurations are shown in table A.11.2.1.4.2-1. Both handover delay and interruption length are tested by using the parameters in table A.11.2.1.4.2-2, and A.11.2.1.4.2-3.

The test consists of three successive time periods, with time durations of T1 T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

NR with CCA shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.11.2.1.4.2-1: Handover from NR with CCA FR1 to NR FR1 test configuration

| Config | Description |
| --- | --- |
| 1 | Source cell: NR with CCA 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | Source cell: NR with CCA 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | Source cell: NR with CCA 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.2.1.4.2-2: General test parameters handover from NR with CCA FR1 to NR FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 | NR cell with CCA |
|  | Neighbouring cell |  | Cell 2 | NR cell |
| Final condition | Active cell |  | Cell 2 |  |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |
| A3-Offset |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| T304 |  | ms | 500 |  |
| LCCA_DL |  |  | 5 |  |
| WCCA_DL |  | ms | T304 |  |
| LCCA_UL |  |  | 5 |  |
| WCCA_UL |  | ms | T304 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |
| T3 |  | s | 1 |  |

Table A.11.2.1.4.2-3: Cell specific test parameters for NR with CCA FR1 – NR FR1 handover test case

| Parameter |  |  | Unit | Test | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | configuration | T1 | T2 | T3 | T1 | T2 | T3 |
| NR RF Channel Number |  |  |  | 1,2,3 | 1 |  |  | 2 |  |  |
| Duplex mode |  |  |  | 1 | TDD |  |  | FDD |  |  |
|  |  |  |  | 2 | TDD |  |  | TDD |  |  |
|  |  |  |  | 3 | TDD |  |  | TDD |  |  |
| TDD configuration |  |  |  | 1 | TDDConf.1.1 CCA |  |  | Not Applicable |  |  |
|  |  |  |  | 2 | TDDConf.1.1 CCA |  |  | TDDConf.1.1 |  |  |
|  |  |  |  | 3 | TDDConf.1.1 CCA |  |  | TDDConf.2.1 |  |  |
| BWchannel |  |  | MHz | 1 | 40: NPRB,c = 106 |  |  | 10: NPRB,c = 52 |  |  |
|  |  |  |  | 2 | 40: NPRB,c = 106 |  |  | 10: NPRB,c = 52 |  |  |
|  |  |  |  | 3 | 40: NPRB,c = 106 |  |  | 40: NPRB,c = 106 |  |  |
| BWP BW |  |  | MHz | 1 | 40: NPRB,c = 106 |  |  | 10: NPRB,c = 52 |  |  |
|  |  |  |  | 2 | 40: NPRB,c = 106 |  |  | 10: NPRB,c = 52 |  |  |
|  |  |  |  | 3 | 40: NPRB,c = 106 |  |  | 40: NPRB,c = 106 |  |  |
| DRX Cycle |  |  | ms | 1,2,3 | Not Applicable |  |  |  |  |  |
| PDSCH Reference measurement channel |  |  |  | 1 | SR.1.1 CCA |  |  | SR.1.1 FDD |  |  |
|  |  |  |  | 2 | SR.1.1 CCA |  |  | SR.1.1 TDD |  |  |
|  |  |  |  | 3 | SR.1.1 CCA |  |  | SR2.1 TDD |  |  |
| CORESET Reference Channel |  |  |  | 1 | CR1.1 CCA |  |  | CR.1.1 FDD |  |  |
|  |  |  |  | 2 | CR1.1 CCA |  |  | CR.1.1 TDD |  |  |
|  |  |  |  | 3 | CR1.1 CCA |  |  | CR2.1 TDD |  |  |
| Dedicated CORESET RMC configuration |  |  |  | 1 | CCR.1.1 CCA |  |  | CCR.1.1 FDD |  |  |
|  |  |  |  | 2 | CCR.1.1 CCA |  |  | CCR.1.1 TDD |  |  |
|  |  |  |  | 3 | CCR.1.1 CCA |  |  | CCR.2.1 TDD |  |  |
| DL CCA probability for semi-static channel access (PCCA_DL)DL CCA probability PCCA_DL |  |  |  | 1,2,3 | 0.9375 |  |  | N/A |  |  |
| DL CCA probability for dynamic channel access (PCCA_DL_1) |  |  |  | 1,2,3 | 0.75 |  |  | N/A |  |  |
| DL CCA probability for dynamic channel access (PCCA_DL_2) |  |  |  | 1,2,3 | 0.75 |  |  | N/A |  |  |
| UL CCA probability for semi-static channel access PCCA_UL |  |  |  | 1,2,3 | 0.75 |  |  | N/A |  |  |
| UL CCA probability for dynamic static channel access  PCCA_UL |  |  |  | 1,2,3 | 0.87 |  |  |  |  |  |
| TRS configuration |  |  |  | 1 | TRS.1.2 TDD |  |  | TRS.1.1 FDD |  |  |
|  |  |  |  | 2 | TRS.1.2 TDD |  |  | TRS.1.1 TDD |  |  |
|  |  |  |  | 3 | TRS.1.2 TDD |  |  | TRS.1.2 TDD |  |  |
| OCNG Patterns |  |  |  |  | OP.1 |  |  |  |  |  |
| SMTC Configuration |  |  |  |  | SMTC.1 |  |  |  |  |  |
| SSB Configuration |  | Semi-static channel access |  | 1,2 | SSB.1 CCA (As defined in A.3.10A ) |  |  | SSB.1 FR1 |  |  |
|  |  | Dynamic channel access |  |  | SSB.2 CCA (As defined in A.3.10A ) |  |  |  |  |  |
|  |  | Semi-static channel access |  | 3 | SSB.1 CCA (As defined in A.3.10A ) |  |  | SSB.2 FR1 |  |  |
|  |  | Dynamic channel access |  |  | SSB.2 CCA (As defined in A.3.10A ) |  |  |  |  |  |
| DBT window configuration |  |  |  |  | As defined in A.3.28.1 |  |  | Not applicable |  |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 1,2 | 30 kHz |  |  | 15 kHz |  |  |
|  |  |  |  | 3 | 30 kHz |  |  | 30 kHz |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 1,2 | 30 kHz |  |  | 15 kHz |  |  |
|  |  |  |  | 3 | 30 kHz |  |  | 30 kHz |  |  |
| PRACH configuration |  |  |  |  | FR1 PRACH configuration 1 under CCA |  |  | FR1 PRACH configuration 1 |  |  |
| BWP configuration |  | Initial DL BWP |  | 1,2,3 | DLBWP.0.1 |  |  |  |  |  |
|  |  | Dedicated DL BWP |  | 1,2,3 | DLBWP.1.1 |  |  |  |  |  |
|  |  | Initial UL BWP |  | 1,2,3 | ULBWP.0.1 |  |  |  |  |  |
|  |  | Dedicated UL BWP |  | 1,2,3 | ULBWP.1.1 |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 1,2,3 | 0 |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  | 1,2,3 |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  | 1,2,3 |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  | 1,2,3 |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  | 1,2,3 |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  | 1,2,3 |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  | 1,2,3 |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote1 |  |  |  | 1,2,3 |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRSNote1 |  |  |  | 1,2,3 |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15kHz | 1,2 | -98 |  |  | -98 |  |  |
|  |  |  |  | 3 | -98 |  |  | -98 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | 1,2 | -95 |  |  | -98 |  |  |
|  |  |  |  | 3 | -95 |  |  | -95 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 1,2,3 | 8 | -3.3 | -3.3 | -Infinity | 2.36 | 2.36 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 1,2,3 | 8 | 8 | 8 | -Infinity | 11 | 11 |
| SSB_RP |  |  | dBm/SCS | 1,2 | -87 | -87 | -87 | -Infinity | -87 | -87 |
|  |  |  |  | 3 | -87 | -87 | -87 | -Infinity | -84 | -84 |
| IoNote3 |  |  | dBm/ChBW | 1,2 | -55.31 | -55.31 | -55.31 | -70.05 | -58.72 | -58.72 |
|  |  |  |  | 3 | -55.31 | -55.31 | -55.31 | -63.94 | -52.61 | -52.61 |
| Propagation condition |  |  | - | 1,2,3 | AWGN |  |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |  |  |  |

##### A.11.2.1.4.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 112 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 102 ms in the test. Tinterrupt is defined in clause 6.1.1.2.2.

This gives a total of 112 ms.

#### A.11.2.1.5 Inter-frequency handover from FR1 carrier under CCA to FR1; unknown target cell

##### A.11.2.1.5.1 Test Purpose and Environment

This test is to verify the requirement for the NR with CCA FR1-NR FR1 handover requirements specified in clause6.1.1.2.

##### A.11.2.1.5.2 Test Parameters

Supported test configurations are shown in table A.11.2.1.5.2-1. Both handover delay and interruption length are tested by using the parameters in table A.11.2.1.5.2-2, and A.12.2.1.7.2-3.

The test scenario comprises of two carriers and one cell on each carrier. Cell 1 is the NR with CCA cell and Cell 2 is an NR neighbour cell. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2.

Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.11.2.1.5.2-1: Handover from NR with CCA FR1 to NR FR1 test configuration

| Config | Description |
| --- | --- |
| 1 | Source cell: NR with CCA 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | Source cell: NR with CCA 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | Source cell: NR with CCA 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.2.1.5.2-2: General test parameters handover from NR with CCA FR1 to NR FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 | NR cell with CCA |
|  | Neighbouring cell |  | Cell 2 | NR cell |
| Final condition | Active cell |  | Cell 2 |  |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| T304 |  | ms | 500 |  |
| LCCA_DL |  |  | 5 |  |
| WCCA_DL |  | ms | T304 |  |
| LCCA_UL |  |  | 5 |  |
| WCCA_UL |  | ms | T304 |  |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |

Table A.11.2.1.5.2-3: Cell specific test parameters for NR with CCA FR1 – NR FR1 handover test case

| Parameter | Unit | Configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  | 1, 2, 3 | 1 |  | 2 |  |
| Duplex mode |  | 1 | TDD |  | FDD |  |
|  |  | 2 | TDD |  | TDD |  |
|  |  | 3 | TDD |  | TDD |  |
| DL CCA model |  | 1, 2, 3 | As specified in clause A.3.26.2.1 |  | N/A |  |
| UL CCA model |  | 1, 2, 3 | As specified in clause A.3.26.2.2 |  |  |  |
| TDD configuration |  | 1 | TDDConf.1.1 CCA |  | Not Applicable |  |
|  |  | 2 | TDDConf.1.1 CCA |  | TDDConf.1.1 |  |
|  |  | 3 | TDDConf.1.1 CCA |  | TDDConf.2.1 |  |
| BWchannel | MHz | 1 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  | 2 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  | 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW | MHz | 1 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  | 2 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  | 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| DRX Cycle | ms |  | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  | 1 | SR.1.1 CCA |  | SR.1.1 FDD |  |
|  |  | 2 | SR.1.1 CCA |  | SR.1.1 TDD |  |
|  |  | 3 | SR.1.1 CCA |  | SR2.1 TDD |  |
| CORESET Reference Channel |  | 1 | CR2.1 TDD |  | CR.1.1 FDD |  |
|  |  | 2 | CR2.1 TDD |  | CR.1.1 TDD |  |
|  |  | 3 | CR2.1 TDD |  | CR2.1 TDD |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.1.1 CCA |  | CCR.1.1 FDD |  |
|  |  | 2 | CCR.1.1 CCA |  | CCR.1.1 TDD |  |
|  |  | 3 | CCR.1.1 CCA |  | CCR.2.1 TDD |  |
| TRS configuration |  | 1 | TRS.1.2 TDD |  | TRS.1.1 FDD |  |
|  |  | 2 | TRS.1.2 TDD |  | TRS.1.1 TDD |  |
|  |  | 3 | TRS.1.2 TDD |  | TRS.1.2 TDD |  |
| DL CCA probability for semi-static channel access (PCCA_DL)DL CCA probability PCCA_DL |  | 1, 2, 3 | 0.9375 |  | N/A |  |
| DL CCA probability for dynamic channel access (PCCA_DL_1) |  | 1, 2, 3 | 0.75 |  | N/A |  |
| DL CCA probability for dynamic channel access (PCCA_DL_2) |  | 1, 2, 3 | 0.75 |  | N/A |  |
| UL CCA probability for semi-static channel access PCCA_UL |  | 1, 2, 3 | 0.75 |  | N/A |  |
| UL CCA probability for dynamic static channel access  PCCA_UL |  | 1, 2, 3 | 0.87 |  | N/A |  |
| OCNG Patterns |  | 1, 2, 3 | OP.1 |  |  |  |
| SMTC Configuration |  | 1, 2, 3 | SMTC.1 |  |  |  |
| DBT window configuration |  | 1, 2, 3 | As defined in A.3.28.1 |  | N/A |  |
| SSB configuration | Semi-static channel access | 1,2 | SSB.1 CCA (As defined in A.3.10A ) |  | SSB.1 FR1 |  |
|  | Dynamic channel access |  | SSB.2 CCA (As defined in A.3.10A ) |  |  |  |
|  | Semi-static channel access | 3 | SSB.1 CCA (As defined in A.3.10A ) |  | SSB.2 FR1 |  |
|  | Dynamic channel access |  | SSB.2 CCA (As defined in A.3.10A ) |  |  |  |
| ssb-PositionQCL |  |  | 1 |  | N/A |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1 | 30 kHz |  | 15 kHz |  |
|  |  | 2 | 30 kHz |  | 15 kHz |  |
|  |  | 3 | 30 kHz |  | 30 kHz |  |
| PUCCH/PUSCH subcarrier spacing | kHz | 1 | 30 kHz |  | 15 kHz |  |
|  |  | 2 | 30 kHz |  | 15 kHz |  |
|  |  | 3 | 30 kHz |  | 30 kHz |  |
| PRACH configuration |  | 1,2,3 | FR1 PRACH configuration 1 under CCA |  | FR1 PRACH configuration 1 |  |
| BWP configuration | Initial DL BWP | 1,2,3 | DLBWP.0.1 |  |  |  |
|  | Dedicated DL BWP | 1,2,3 | DLBWP.1.1 |  |  |  |
|  | Initial UL BWP | 1,2,3 | ULBWP.0.1 |  |  |  |
|  | Dedicated UL BWP | 1,2,3 | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS | dB | 1,2,3 | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | 1,2,3 |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | 1,2,3 |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | 1,2,3 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | 1,2,3 |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | 1,2,3 |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  | 1,2,3 |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote1 |  | 1,2,3 |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRSNote1 |  | 1,2,3 |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1,2 | -95 |  | -98 |  |
|  |  | 3 | -95 |  | -95 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1,2,3 | 4 | 4 | -Infinity | 5 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1,2,3 | 4 | 4 | -Infinity | 5 |
| SSB_RP | dBm/SCS | 1,2 | -91 | -91 | -Infinity | -93 |
|  |  | 3 | -91 | -91 | -Infinity | -90 |
| IoNote3 | dBm/ChBW | 1,2 | -58.49 | -58.49 | -70.05 | -63.85 |
|  |  | 3 | -58.49 | -58.49 | -63.94 | -57.75 |
| Propagation condition | - | 1,2,3 | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |

##### A.11.2.1.5.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 132 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 122 ms in the test. Tinterrupt is defined in clause 6.1.1.2.2.

This gives a total of 132 ms.

#### A.11.2.1.6 Inter-frequency handover from FR1 to FR1 carrier under CCA; unknown target cell

##### A.11.2.1.6.1 Test Purpose and Environment

This test is to verify the requirement for inter frequency handover requirements from FR1 to FR1 carrier under CCA specified in clause 6.1B.1.2.

##### A.11.2.1.6.2 Test Parameters

Supported test configurations are shown in table A.11.2.1.6.2-1. Both handover delay and interruption length are tested by using the parameters in table A.11.2.1.6.2-2, and A.11.2.1.6.2-3.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.11.2.1.6.2-1: Inter-frequency handover from FR1 to FR1 carrier under CCA test configurations

| Configuration | Description of a cell with CCA | Description of a cell without CCA |
| --- | --- | --- |
| 1 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |  |

Table A.11.2.1.6.2-2: General test parameters Inter-frequency handover from FR1 to FR1 carrier under CCA

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 | On the carrier under CCA |
| Final condition | Active cell |  | Cell 2 | On the carrier under CCA |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| T304 |  | ms | 500 |  |
| LCCA_DL |  |  | 5 |  |
| WCCA_DL |  | ms | T304 |  |
| LCCA_UL |  |  | 5 |  |
| WCCA_UL |  | ms | T304 |  |
| T1 |  | s | 5 |  |
| T2 |  | s | Tinterrupt | Tinterrupt is defined in clause 6.1B.1.2 |

Table A.11.2.1.6.2-3: Cell specific test parameters for NR FR1-FR1 Inter frequency handover test case

| Parameter |  | Unit | Configuration | Cell 1 |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 |  | T2 |
| NR RF Channel Number |  |  | 1, 2, 3 | 1 |  | 2 |  |  |
| DL CCA probability for semi-static channel access (PCCA_DL)DL CCA probability PCCA_DL |  |  | 1, 2, 3 | N/A |  | 0.9375 |  |  |
| DL CCA probability for dynamic channel access (PCCA_DL_1) |  |  | 1, 2, 3 | N/A |  | 0.75 |  |  |
| DL CCA probability for dynamic channel access (PCCA_DL_2) |  |  | 1, 2, 3 | N/A |  | 0.75 |  |  |
| UL CCA probability for semi-static channel access  PCCA_UL |  |  | 1, 2, 3 | N/A |  | 0.75 |  |  |
| UL CCA probability for dynamic static channel access  PCCA_UL |  |  | 1, 2, 3 | N/A |  | 0.87 |  |  |
| TDD configuration |  |  | 1 | N/A |  | TDDConf.1.1.CCA |  |  |
|  |  |  | 2 | TDDConf.1.1 |  | TDDConf.1.1.CCA |  |  |
|  |  |  | 3 | TDDConf.1.2 |  | TDDConf.1.1.CCA |  |  |
| BWchannel |  |  | 1 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  |  |
|  |  |  | 2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  |  |
|  |  |  | 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |  |
| BWP BW |  |  | 1 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  |  |
|  |  |  | 2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  |  |
|  |  |  | 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |  |
| DRX Cycle |  | ms |  | Not Applicable |  |  |  |  |
| PDSCH Reference |  |  | 1 | SR.1.1 FDD |  | SR.1.1 CCA |  |  |
|  |  |  | 2 | SR.1.1 TDD |  | SR.1.1 CCA |  |  |
|  |  |  | 3 | SR.2.1 TDD |  | SR.1.1 CCA |  |  |
| CORESET Reference Channel |  |  | 1 | CR.1.1 FDD |  | CR.1.1 CCA |  |  |
|  |  |  | 2 | CR.1.1 TDD |  | CR.1.1 CCA |  |  |
|  |  |  | 3 | CR.2.1 TDD |  | CR.1.1 CCA |  |  |
| Dedicated CORESET RMC configuration |  |  | 1 | CCR.1.1 FDD |  | CCR.1.1 CCA |  |  |
|  |  |  | 2 | CCR.1.1 TDD |  | CCR.1.1 CCA |  |  |
|  |  |  | 3 | CCR.2.1 TDD |  | CCR.1.1 CCA |  |  |
| TRS configuration |  |  | 1 | TRS.1.1 FDD |  | TRS.1.2 TDD |  |  |
|  |  |  | 2 | TRS.1.1 TDD |  | TRS.1.2 TDD |  |  |
|  |  |  | 3 | TRS.1.2 TDD |  | TRS.1.2 TDD |  |  |
| OCNG Patterns |  |  | 1, 2, 3 | OP.1 |  |  |  |  |
| SMTC Configuration |  |  | 1, 2, 3 | SMTC.1 |  |  |  |  |
| DBT window configuration |  |  | 1, 2, 3 | N/A |  | As defined in A.3.28.1 |  |  |
| SSB configuration |  |  | 1, 2 | SSB.1 FR1 |  | SSB.1 CCA for semi-static channel access; SSB.2 CCA for dynamic channel access; |  |  |
|  |  |  | 3 | SSB.2 FR1 |  | SSB.1 CCA for semi-static channel access; SSB.2 CCA for dynamic channel access; |  |  |
| ssb-PositionQCL |  |  |  | N/A |  | [1] |  |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 1 | 15 kHz |  | 30 kHz |  |  |
|  |  |  | 2 | 15 kHz |  | 30 kHz |  |  |
|  |  |  | 3 | 30 kHz |  | 30 kHz |  |  |
| PUCCH/PUSCH subcarrier spacing |  | kHz | 1 | 15 kHz |  | 30 kHz |  |  |
|  |  |  | 2 | 15 kHz |  | 30 kHz |  |  |
|  |  |  | 3 | 30 kHz |  | 30 kHz |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 |  | FR1 PRACH configuration 1 CCA |  |  |
| BWP configuration | Initial DL BWP |  | 1, 2, 3 | DLBWP.0.1 |  |  |  |  |
|  | Dedicated DL BWP |  | 1, 2, 3 | DLBWP.1.1 |  |  |  |  |
|  | Initial UL BWP |  | 1, 2, 3 | ULBWP.0.1 |  |  |  |  |
|  | Dedicated UL BWP |  | 1, 2, 3 | ULBWP.1.1 |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  | 0 |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz |  | -98 |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | 1, 2 | -98 |  |  | -95 |  |
|  |  |  | 3 | -95 |  |  | -95 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB |  | 4 | 4 | -Infinity |  | 5 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB |  | 4 | 4 | -Infinity |  | 5 |
| SSB_RP | Config 1 | dBm/SCS | 1, 2 | -94 | -94 | -Infinity |  | -90 |
|  |  |  | 3 | -91 | -91 | -Infinity |  | -90 |
| IoNote3 | Config 1 | dBm/9.36 MHz | 1, 2 | -64.59 | -64.59 | -63.94 |  | -57.75 |
|  |  | dBm/38.16 MHz | 3 | -58.49 | -58.49 | -63.94 |  | -57.75 |
| Propagation condition |  | - |  | AWGN |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |  |

##### A.11.2.1.6.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than Tinterrupt from the beginning of time period T3, where Tinterrupt is defined in clause 6.1B.1.2

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin

Tsearch = (3+L1’)* 20 ms.

Tprocessing = 20 ms.

Tmargin = 2 ms.

T∆ = (1+ L2) *20 ms.

TIU = (1+ L3)*10 + 10 ms

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2], L1’ is the number of SMTC occasions not available at the UE during the inter-frequency detection period, L2 is the number of SMTC occasions not available at the UE during the time tracking period, and L3 is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure. L3 = 0 for Type 2C UL channel access procedure as defined in TS 37.213 [33]. The interruption time considering the potential extensions caused by L1, L1´, L2, L3  and by the UL CCA failure detection/recovery mechanism is limited by the T304 timer. The UE behaviour at the T304 timer expiry is detailed in TS 38.331 [2].

#### A.11.2.1.7  SA NR FR1 carrier under CCA - E-UTRAN handover with known target cell

##### A.11.2.1.7.1 Test Purpose and Environment

The purpose of this set of tests is to verify that the UE can make correct inter-RAT E-UTRAN handover when operating in standalone (SA) operation with PCell in FR1 carrier under CCA. This test shall verify the NR to E-UTRAN handover requirements as specified in clause 6.1.2.1.

The test comprises of one NR carrier under CCA and one E-UTRA carrier. There are two cells and one cell on each carrier. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in table 9.1.2-1 is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2 after the UE has reported Event B2. The start of T3 is the next instant after the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.11.2.1.7-1. General test parameters are provided in table A.11.2.1.7-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.11.2.1.7-3 and A.11.2.1.7-4 respectively.

Table A.11.2.1.7-1: Supported test configurations for SA inter-RAT E-UTRAN handover tests

| Configuration | Description of a cell with CCA | Description of a cell without CCA |
| --- | --- | --- |
| 1 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | LTE 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | LTE 10 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations.NOTE 2: The UE supporting SA operation only on NR band(s) with shared spectrum access is required to be tested. |  |  |

Table A.11.2.1.7-2: General test parameters for SA inter-RAT E-UTRAN handover

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  |  | 1 | 1 NR carrier frequency is used in the test |
| LTE RF Channel Number |  |  | 2 | 1 E-UTRAN carrier frequency is used in the test |
| Initial conditions | Active cell |  | Cell 1 | NR cell on a carrier under CCA |
|  | Neighbouring cell |  | Cell 2 | E-UTRAN cell |
| Final condition | Active cell |  | Cell 2 |  |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |
| NR measurement quantity |  |  | SS-RSRP |  |
| E-UTRAN measurement quantity |  |  | RSRP |  |
| b2-Threshold1 |  | dBm | As specified in table A.11.2.1.7-3 | Absolute NR SS-RSRP threshold for event B2 |
| b2-Threshold2EUTRAN |  | dBm | -98 | Absolute E-UTRAN RSRP threshold for event B2 |
| Hysteresis |  | dB | 0 |  |
| TimeToTrigger |  | s | 0 |  |
| T304 |  | ms | 500 |  |
| LCCA_DL |  |  | 5 |  |
| WCCA_DL |  | ms | T304 |  |
| LCCA_UL |  |  | 5 |  |
| WCCA_UL |  | ms | T304 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| DRX |  |  | OFF | Non-DRX test |
| Access Barring Information |  | - | Not sent | No additional delays in random access procedure |
| Time offset between cells |  |  | 3 ms | Asynchronous cells |
| Gap pattern configuration Id |  |  | 0 | As specified in table 9.1.2-1 started before T2 starts |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |
| T3 |  | s | 1 |  |

Table A.11.2.1.7-3: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 1)

| Parameter |  | Unit | Configuration | Cell 1 |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 |
| RF channel number |  |  | 1, 2 | 1 |  |  |
| TDD Configuration |  |  | 1, 2 | TDDConf.1.1.CCA |  |  |
| DL CCA probability for semi-static channel access (PCCA_DL)DL CCA probability PCCA_DL |  |  | 1, 2 | 0.9375 |  |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_1) |  |  | 1, 2 | 0.75 |  |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_2) |  |  | 1, 2 | 0.75 |  |  |
| UL CCA probability for semi-static channel access  PCCA_UL |  |  | 1, 2 | 0.75 |  |  |
| UL CCA probability for dynamic static channel access  PCCA_UL |  |  | 1, 2 | 0.87 |  |  |
| BWchannel |  |  | 1, 2 | 40: NPRB,c = 106 (TDD) |  |  |
| PDSCH reference measurement channel |  |  | 1, 2 | SR.1.1 CCA |  |  |
| CORESET reference channel |  |  | 1, 2 | CR.1.1 CCA |  |  |
| Dedicated CORESET RMC configuration |  |  | 1, 2 | CCR.1.1 CCA |  |  |
| TRS configuration |  |  | 1, 2 | TRS.1.2 TDD |  |  |
| OCNG patternNote1 |  |  | 1, 2 | OP.1 |  |  |
| BWP | Initial DL BWP |  | 1, 2 | DLBWP.0.1 |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |
| SMTC configuration |  |  | 1, 2 | SMTC.1 |  |  |
| DBT window configuration |  |  | 1, 2 | As defined in A.3.28.1 |  |  |
| SSB configuration |  |  | 1, 2 | SSB.1 CCA for semi-static channel access; SSB.2 CCA for dynamic channel access; |  |  |
| b2-Threshold1 |  | dBm | 1, 2 | -93 |  |  |
| EPRE ratio of PSS to SSS |  | dB | 1, 2 | 0 |  |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  |  |  |  |  |
| NocNote2 |  | dBm/15 KHz | 1, 2 | -100 | -104 | -100 |
| NocNote2 |  | dBm/SCS | 1, 2 | -97 | -101 | -97 |
| Ês/Noc |  | dB | 1, 2 | 12 | 0 | 0 |
| Ês/IotNote3 |  | dB | 1, 2 | 12 | 0 | 0 |
| SS-RSRPNote3 |  | dBm/SCS | 1, 2 | -85 | -101 | -97 |
| IoNote3 |  | dBm/38.16 MHz | 1, 2 | -53.68 | -66.93 | -62.93 |
| Propagation condition |  |  | 1, 2 | AWGN |  |  |
| Antenna Configuration and Correlation Matrix |  |  | 1, 2 | 1x2 Low |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: Ês/Iot, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |

Table A.11.2.1.7-4: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 2)

| Parameter | Unit | Configuration | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| RF channel number |  | 1, 2 | 2 |  |  |
| Duplex mode |  | 1 | FDD |  |  |
|  |  | 2 | TDD |  |  |
| TDD special subframe configurationNote1 |  | 2 | 6 |  |  |
| TDD uplink-downlink configurationNote1 |  | 2 | 1 |  |  |
| BWchannel | MHz | 1, 2 | 10 MHz: NPRB,c = 50 |  |  |
| PRACH ConfigurationNote2 |  | 1 | 4 |  |  |
|  |  | 2 | 53 |  |  |
| PDSCH parameters:DL Reference Measurement ChannelNote3 |  | 1 | 10 MHz: R.3 FDD |  |  |
|  |  | 2 | 10 MHz: R.0 TDD |  |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote3 |  | 1 | 10 MHz: R.6 FDD |  |  |
|  |  | 2 | 10 MHz: R.6 TDD |  |  |
| OCNG PatternsNote3 |  | 1 | 10 MHz: OP.10 FDD |  |  |
|  |  | 2 | 10 MHz: OP.1 TDD |  |  |
| PBCH_RA | dB | 1, 2 | 0 |  |  |
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
| NocNote5 | dBm/15 kHz | 1, 2 | -98 |  |  |
| Ês/Noc | dB | 1, 2 | -Infinity | 8 | 8 |
| Ês/IotNote6 | dB | 1, 2 | -Infinity | 8 | 8 |
| RSRPNote6 | dBm/15 kHz | 1, 2 | -Infinity | -90 | -90 |
| SCH_RPNote6 | dBm/15 kHz | 1, 2 | -Infinity | -90 | -90 |
| IoNote6 | dBm/9 MHz | 1, 2 | -67.21+10log(NPRB,c/100) | -58.57+10log(NPRB,c/100) | -58.57+10log(NPRB,c/100) |
| Propagation Condition |  | 1, 2 | AWGN |  |  |
| Antenna Configuration and Correlation Matrix Note7 |  | 1, 2 | 1x2 Low |  |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: PRACH configurations are specified in table 5.7.1-2 and table 5.7.1-3 in TS 36.211 [23].NOTE 3: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 4: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 5: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 6: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 7: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |  |

##### A.11.2.1.7.2 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 85 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and is specified in clause 6.1.2.1.

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 6.1.2.1.

This gives a total of 85 ms.

#### A.11.2.1.8 SA NR FR1 carrier under CCA - E-UTRAN handover with unknown target cell

##### A.11.2.1.8.1 Test Purpose and Environment

The purpose of this set of tests is to verify that the UE can make correct inter-RAT E-UTRAN handover when operating in standalone (SA) operation with PCell in FR1 carrier under CCA. This test shall verify the NR to E-UTRAN handover requirements for the case when the target E-UTRAN cell is unknown as specified in clause 6.1.2.1.

The test comprises of one NR carrier under CCA and one E-UTRA carrier. There are two cells and one cell on each carrier. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable. No Gap pattern shall be configured.

A RRC message implying handover shall be sent to the UE during period T1. The start of T2 is the next instant after the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.11.2.1.8-1. General test parameters are provided in table A.11.2.1.8-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.11.2.1.8-3 and A.11.2.1.8-4 respectively.

Table A.11.2.1.8-1: Supported test configurations for SA inter-RAT E-UTRAN handover tests

| Configuration | Description of a cell with CCA | Description of a cell without CCA |
| --- | --- | --- |
| 1 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | LTE 10 MHz bandwidth, TDD duplex mode |
| 2 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode | LTE 10 MHz bandwidth, FDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations.NOTE 2: The UE supporting SA operation only on NR band(s) with shared spectrum access is required to be tested. |  |  |

Table A.11.2.1.8-2: General test parameters for SA inter-RAT E-UTRAN handover

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  |  | 1 | 1 NR carrier frequency is used in the test |
| LTE RF Channel Number |  |  | 2 | 1 E-UTRAN carrier frequency is used in the test |
| Initial conditions | Active cell |  | Cell 1 | NR cell on a carrier under CCA |
|  | Neighbouring cell |  | Cell 2 | E-UTRAN cell |
| Final condition | Active cell |  | Cell 2 |  |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |
| NR measurement quantity |  |  | SS-RSRP |  |
| DRX |  |  | OFF | Non-DRX test |
| Access Barring Information |  | - | Not sent | No additional delays in random access procedure |
| T304 |  | ms | 500 |  |
| LCCA_DL |  |  | 5 |  |
| WCCA_DL |  | ms | T304 |  |
| LCCA_UL |  |  | 5 |  |
| WCCA_UL |  | ms | T304 |  |
| Time offset between cells |  |  | 3 ms | Asynchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 1 |  |

Table A.11.2.1.8-3: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 1)

| Parameter |  | Unit | Configuration | Cell 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 |
| RF channel number |  |  | 1, 2 | 1 |  |
| DL CCA probability for semi-static channel access (PCCA_DL)DL CCA probability PCCA_DL |  |  | 1, 2 | 0.9375 |  |
| DL CCA probability for dynamic channel access (PCCA_DL_1) |  |  | 1, 2 | 0.75 |  |
| DL CCA probability for dynamic channel access (PCCA_DL_2) |  |  | 1, 2 | 0.75 |  |
| UL CCA probability for semi-static channel access  PCCA_UL |  |  | 1, 2 | 0.75 |  |
| UL CCA probability for dynamic static channel access  PCCA_UL |  |  | 1, 2 | 0.87 |  |
| TDD Configuration |  |  | 1, 2 | TDDConf.1.1.CCA |  |
| BWchannel |  | MHz | 1, 2 | 40: NPRB,c = 106 (TDD) |  |
| PDSCH reference measurement channel |  |  | 1, 2 | SR.1.1 CCA |  |
| CORESET reference channel |  |  | 1, 2 | CR.1.1 CCA |  |
| Dedicated CORESET RMC configuration |  |  | 1, 2 | CCR.1.1 CCA |  |
| TRS configuration |  |  | 1, 2 | TRS.1.2 TDD |  |
| OCNG patternNote1 |  |  | 1, 2 | OP.1 |  |
| BWP | Initial DL BWP |  | 1, 2 | DLBWP.0.1 |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |
| SMTC configuration |  |  | 1, 2 | SMTC.1 |  |
| DBT window configuration |  |  | 1, 2 | As defined in A.3.28.1 |  |
| SSB configuration |  |  | 1, 2 | SSB.1 CCA for semi-static channel access; SSB.2 CCA for dynamic channel access; |  |
| EPRE ratio of PSS to SSS |  | dB | 1, 2 | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  |  |  |  |
| NocNote2 |  | dBm/15 KHz | 1, 2 | -98 |  |
| NocNote2 |  | dBm/SCS | 1, 2 | -95 |  |
| Ês/Noc |  | dB | 1, 2 | 0 | 0 |
| Ês/IotNote3 |  | dB | 1, 2 | 0 | 0 |
| SS-RSRPNote3 |  | dBm/SCS | 1, 2 | -95 | -95 |
| IoNote3 |  | dBm/38.16 MHz | 1, 2 | -60.94 | -60.94 |
| Propagation condition |  |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix |  |  | 1, 2 | 1x2 Low |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: Ês/Iot, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |

Table A.11.2.1.8-4: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 2)

| Parameter | Unit | Configuration | Cell 2 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1, 2 | 2 |  |
| Duplex mode |  | 1 | FDD |  |
|  |  | 2 | TDD |  |
| TDD special subframe configurationNote1 |  | 2 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 2 | 1 |  |
| BWchannel | MHz | 1, 2 | 10 MHz: NPRB,c = 50 |  |
| PRACH ConfigurationNote2 |  | 1 | 4 |  |
|  |  | 2 | 53 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote3 |  | 1 | 10 MHz: R.3 FDD |  |
|  |  | 2 | 10 MHz: R.0 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote3 |  | 1 | 10 MHz: R.6 FDD |  |
|  |  | 2 | 10 MHz: R.6 TDD |  |
| OCNG PatternsNote3 |  | 1 | 10 MHz: OP.10 FDD |  |
|  |  | 2 | 10 MHz: OP.1 TDD |  |
| PBCH_RA | dB | 1, 2 | 0 |  |
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
| NocNote5 | dBm/15 kHz | 1, 2 | -98 |  |
| Ês/Noc | dB | 1, 2 | -Infinity | 7 |
| Ês/IotNote6 | dB | 1, 2 | -Infinity | 7 |
| RSRPNote6 | dBm/15 kHz | 1, 2 | -Infinity | -91 |
| SCH_RPNote6 | dBm/15 kHz | 1, 2 | -Infinity | -91 |
| IoNote6 | dBm/9 MHz | 1, 2 | -70.22 | -62.43 |
| Propagation Condition |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix Note7 |  | 1, 2 | 1x2 Low |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: PRACH configurations are specified in table 5.7.1-2 and table 5.7.1-3 in TS 36.211 [23].NOTE 3: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 4: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 5: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 6: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 7: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |

##### A.11.2.1.8.2 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 165 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and is specified in clause 6.1.2.1.

Tinterrupt = 115 ms in the test; Tinterrupt is defined in clause 6.1.2.1.

This gives a total of 165 ms.


#### A.11.2.1.9 Handover with PSCell from NR SA to EN-DC with known target PSCell using CCA

##### A.11.2.1.9.1 Test Purpose and Environment

The purpose of this set of tests is to verify that the UE can make correct SA inter-RAT handover from NR to E-UTRAN with FR1 PSCell addition when operating in standalone (SA) operation with PCell in FR1, for the case where the PSCell is known to the UE at the time of addition and SMTC of target known PSCell is not present in RRCConnectionReconfiguration. This test shall verify delay requirements of inter-RAT handover from NR to E-UTRAN and FR1 PSCell carrier with CCA addition as specified in clause 6.1.5.

The test comprises of two NR cells and one E-UTRA cell. Cell 1 is the NR PCell, Cell 2 is an inter-RAT E-UTRAN neighbour cell and Cell 3 is the target NR PSCell, which is on CCA, on radio channel 1 in FR1, radio channel 2 in E-UTRAN and radio channel 3 in FR1 with CCA, respectively.

In this test, inter-RAT handover from NR to E-UTRAN and FR1 PSCell addition are performed in parallel processing. The test consists of successive time periods for inter-RAT handover with time durations of T1, T2 and T3 respectively, and successive time periods for FR1 PSCell addition with time durations of T1’, T2’, T3’and T4’ respectively.

At the start of time duration T1, the UE does not have any timing information of Cell 2, and the UE is only monitoring Cell 1. During T1, only Cell 1 is known to the UE.

Before the start of T2 or T2’, the test system shall send measurement control information including measurement gap configuration and event-triggered reporting configuration with event B2 for neighbour Cell 2 and event B1 for Cell 3. Gap pattern configuration with id #0 as specified in table 9.1.2-1 is configured before T2 or T2’ begins.

Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. A RRC message implying handover shall be sent to the UE during period T2 after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

During T3, the UE shall carry out random access (i.e., transmit the PRACH) towards the Cell 2. Reception by the test system of the PRACH preamble defines the end of T3.

Starting T2’, the Cell 3 (PSCell-to-be) on radio channel 3 becomes known to the UE at the time of addition. Therefore, during T2’ the UE shall report Event B1. After receiving the Event B1, the test system shall send a RRC message to the UE to release the measurement gaps. The test system shall send a RRC message to the UE to add PSCell (Cell 3) on radio channel 3. The RRC message (to add PSCell) also includes a request for the UE to start periodic CSI reporting for the PSCell after the PSCell has been successfully added. The RRC message to add PSCell shall be sent to the UE during period T2’, after the measurement gaps are released by the test system. The point in time at which the RRC message to add PSCell (Cell 3) is received at the UE antenna connector defines the start of period T3’.

During T3’, the UE shall carry out random access (i.e., transmit the PRACH) towards the Cell 3. Reception by the test system of the PRACH preamble defines the start of period T4’.

During T4’, the UE shall send periodic CSI reports in PSCell and the test system shall observe the periodic reporting of CSI for PSCell.

Supported test configurations are shown in table A.11.2.1.9.1-1. General test parameters are provided in table A.11.2.1.9.1-2. Cell specific test parameters for NR Cell 1, E-UTRAN PCell Cell 2 are provided in tables A.11.2.1.9.1-3, A.11.2.1.9.1-4 and A.11.2.1.xn-5 respectively. Table A.11.2.1.9.1-5 provides General test parameters for NR FR1 PSCell carrier with CCA addition, and table A.11.2.1.9.1-6 provides Cell specific test parameters for PSCell addition of FR1 carrier under CCA.

Table A.11.2.1.9.1-1: Supported test configurations for SA inter-RAT E-UTRAN handover with FR1 PSCell addition tests

| Config | Description |  |
| --- | --- | --- |
|  | NR PCell and EUTRA PCell | NR PSCell on CCA |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD, LTE FDD, | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD, LTE FDD |  |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD, LTE FDD |  |
| 4 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD, LTE TDD |  |
| 5 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD, LTE TDD |  |
| 6 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD, LTE TDD |  |
| NOTE:  The UE is only required to be tested in one of the supported test configurations depending on the UE capability |  |  |

Table A.11.2.1.9.1-2: General test parameters for SA inter-RAT E-UTRAN handover with FR1 PSCell addition

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  |  | 1, 3 | 2 NR carrier frequency is used in the test |
| LTE RF Channel Number |  |  | 2 | 1 E-UTRAN carrier frequency is used in the test |
| Initial conditions | Active cell |  | Cell 1 | NR cell |
|  | Neighbouring cell |  | Cell 2, 3 | E-UTRAN cell and NR cell in FR1 |
| Final condition | Active Pcell |  | Cell 2 | E-UTRAN cell |
|  | Active PSCell |  | Cell 3 | NR cell in FR1 |
| NR measurement quantity |  |  | SS-RSRP |  |
| E-UTRAN measurement quantity |  |  | RSRP |  |
| Event B1 | Hysteresis | dB | 0 | Hysteresis for evaluation of event B1. |
|  | Threshold RSRP | dBm | -93 | Actual RSRP threshold for event B1. Needs to take absolute accuracy tolerance in clause 9.1.11.1 into account plus margin. |
|  | Time to Trigger | s | 0 |  |
| Event B2 | Threshold1 | dBm | As specified in table A.6.3.1.4-3 | Absolute NR SS-RSRP threshold for event B2 |
|  | Threshold2EUTRAN | dBm | -98 | Absolute E-UTRAN RSRP threshold for event B2 |
|  | Hysteresis | dB | 0 |  |
|  | TimeToTrigger | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| DRX |  |  | OFF | Non-DRX test |
| Access Barring Information |  | - | Not sent | No additional delays in random access procedure |
| Time offset between Cell 1 and Cell 2 |  |  | 3 ms | Asynchronous cells |
| Measurement Gap pattern ID |  |  | 0 | As specified in table 9.1.2-1 |
| T1/T1’ |  | s | 1 | During this time only Cell 1 is known to UE. |
| T2 |  | s | 5 | During this time the UE shall identify Cell 2 and report event B2. |
| T3 |  | s | 1 | During this time the UE handovers to Cell 2. |
| T2’ |  | s | 5 | During this time the UE shall identify Cell 3 and report event B1. |
| T3’ |  | s | ≥ Tinterrupt | During this time the UE adds the PSCell (Cell 3). |
| T4’ |  | s | 1 | During this time the UE sends CSI reports for PSCell (Cell 3). |

Table A.11.2.1.9.1-3: Cell specific test parameters for SA inter-RAT E-UTRA handover with FR1 PSCell addition (NR Cell 1)

| Parameter |  | Unit | Configuration | Cell 1 |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 |
| RF channel number |  |  | 1, 2, 3, 4, 5, 6 | 1 |  |  |
| Duplex mode |  |  | 1, 4 | FDD |  |  |
|  |  |  | 2, 3, 5, 6 | TDD |  |  |
| TDD Configuration |  |  | 2, 5 | TDDConf.1.1 |  |  |
|  |  |  | 3, 6 | TDDConf.2.1 |  |  |
| BWchannel |  | MHz | 1, 4 | 10: NPRB,c = 52 (FDD) |  |  |
|  |  |  | 2, 5 | 10: NPRB,c = 52 (TDD) |  |  |
|  |  |  | 3, 6 | 40: NPRB,c = 106 (TDD) |  |  |
| PDSCH reference measurement channel |  |  | 1, 4 | SR.1.1 FDD |  |  |
|  |  |  | 2, 5 | SR.1.1 TDD |  |  |
|  |  |  | 3, 6 | SR.2.1 TDD |  |  |
| CORSET reference channel |  |  | 1, 4 | CR.1.1 FDD |  |  |
|  |  |  | 2, 5 | CR.1.1 TDD |  |  |
|  |  |  | 3, 6 | CR.2.1 TDD |  |  |
| TRS configuration |  |  | 1, 4 | TRS.1.1 FDD |  |  |
|  |  |  | 2, 5 | TRS.1.1 TDD |  |  |
|  |  |  | 3, 6 | TRS.1.2 TDD |  |  |
| OCNG patternNote1 |  |  | 1, 2, 3, 4, 5, 6 | OP.1 |  |  |
| BWP | Initial DL BWP |  | 1, 2, 3, 4, 5, 6 | DLBWP.0.1 |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |
| SMTC configuration |  |  | 1, 2, 3, 4, 5, 6 | SMTC.1 |  |  |
| SSB configuration |  |  | 1, 2, 4, 5 | SSB.1 FR1 |  |  |
|  |  |  | 3, 6 | SSB.2 FR1 |  |  |
| b2-Threshold1 |  | dBm | 1, 2, 4, 5 | -96 |  |  |
|  |  |  | 3, 6 | -93 |  |  |
| EPRE ratio of PSS to SSS |  | dB | 1, 2, 3, 4, 5, 6 | 0 |  |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  |  |  |  |  |
| NocNote2 |  | dBm/15 KHz | 1, 2, 3, 4, 5, 6 | -100 | -104 | -100 |
| NocNote2 |  | dBm/SCS | 1, 2, 4, 5 | -100 | -104 | -100 |
|  |  |  | 3, 6 | -97 | -101 | -97 |
| Ês/Noc |  | dB | 1, 2, 3, 4, 5, 6 | 12 | 0 | -4 |
| Ês/IotNote3 |  | dB | 1, 2, 3, 4, 5, 6 | 12 | 0 | -4 |
| SS-RSRPNote3 |  | dBm/SCS | 1, 2, 4, 5 | -88 | -104 | -104 |
|  |  |  | 3, 6 | -85 | -101 | -101 |
| IoNote3 |  | dBm/9.36 MHz | 1, 2, 4, 5 | -59.78 | -73.04 | -70.59 |
|  |  | dBm/38.16 MHz | 3, 6 | -53.68 | -66.9448 | -64.49 |
| Propagation condition |  |  | 1, 2, 3, 4, 5, 6 | AWGN |  |  |
| Antenna Configuration and Correlation Matrix |  |  | 1, 2, 3, 4, 5, 6 | 1x2 Low |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: Ês/Iot, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

Table A.11.2.1.9.1-4: Cell specific test parameters for SA inter-RAT E-UTRA handover with FR1 PSCell addition (E-UTRA Cell 2)

| Parameter | Unit | Configuration | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| RF channel number |  | 1, 2, 3, 4, 5, 6 | 2 |  |  |
| Duplex mode |  | 1, 2, 3 | FDD |  |  |
|  |  | 4, 5, 6 | TDD |  |  |
| TDD special subframe configurationNote1 |  | 4, 5, 6 | 6 |  |  |
| TDD uplink-downlink configurationNote1 |  | 4, 5, 6 | 1 |  |  |
| BWchannel | MHz | 1, 2, 3, 4, 5, 6 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |  |
| PRACH ConfigurationNote2 |  | 1, 2, 3 | 4 |  |  |
|  |  | 4, 5, 6 | 53 |  |  |
| PDSCH parameters:DL Reference Measurement ChannelNote3 |  | 1, 2, 3 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |  |
|  |  | 4, 5, 6 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote3 |  | 1, 2, 3 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |  |
|  |  | 4, 5, 6 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |  |
| OCNG PatternsNote3 |  | 1, 2, 3 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |  |
|  |  | 4, 5, 6 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |  |
| PBCH_RA | dB | 1, 2, 3, 4, 5, 6 | 0 |  |  |
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
| NocNote5 | dBm/15 kHz | 1, 2, 3, 4, 5, 6 | -98 |  |  |
| Ês/Noc | dB | 1, 2, 3, 4, 5, 6 | -Infinity | 8 | 78 |
| Ês/IotNote6 | dB | 1, 2, 3, 4, 5, 6 | -Infinity | 78 | 78 |
| RSRPNote6 | dBm/15 kHz | 1, 2, 3, 4, 5, 6 | -Infinity | -90 | -90 |
| SCH_RPNote6 | dBm/15 kHz | 1, 2, 3, 4, 5, 6 | -Infinity | -90 | -90 |
| IoNote6 | dBm/9 MHz | 1, 2, 3, 4, 5, 6 | -67.21+10log(NPRB,c/100) | -58.57+10log(NPRB,c/100) | -58.57+10log(NPRB,c/100) |
| Propagation Condition |  | 1, 2, 3, 4, 5, 6 | AWGN |  |  |
| Antenna Configuration and Correlation Matrix Note7 |  | 1, 2, 3, 4, 5, 6 | 1x2 Low |  |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: PRACH configurations are specified in table 5.7.1-2 and table 5.7.1-3 in TS 36.211 [23].NOTE 3: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 4: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 5: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 6: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 7: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |  |

Table A.11.2.1.9.1-5: General test parameters for NR FR1 PSCell carrier with CCA addition

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial condition | Neighbouring cell |  | Cell 3 | On the carrier under CCA |
| Final condition | Active cell |  | Cell 3 | On the carrier under CCA |
| DL CCA model | Dynamic channel accessNote 1, 3 |  | As specified in clause A.3.20.2.1 |  |
|  | Semi-static channel access Note 2, 3 |  |  |  |
| UL CCA model | Dynamic channel access Note 1, 3 |  | As specified in clause A.3.20.2.2 |  |
|  | Semi-static channel access Note 2,3 |  |  |  |
| A3-Offset |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T304 |  | ms | 500 |  |
| LCCA_DL |  |  | 5 |  |
| WCCA_DL |  | ms | T304 |  |
| LCCA_UL |  |  | 5 |  |
| WCCA_UL |  | ms | T304 |  |
| T1’ |  | s | 5 |  |
| T2’ |  | s | 5 |  |
| T3’ |  | s | ≥ Tinterrupt | Tinterrupt is defined in clause 6.1B.1.2 |
| T4’ |  | s | 1 |  |
| NOTE 1: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 2: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.11.2.1.9.1-6: Cell specific test parameters for PSCell addition of FR1 carrier under CCA

| Parameter |  |  | Unit | Cell 3 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1’ | T2’ | T3’ | T4’ |
| NR RF Channel Number |  |  |  | 1 |  |  |  |
| PCCA_DL for dynamic channel access Note 4,6 |  |  | - | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |  |
| PCCA_DL for semi-static channel access Note 5,6 |  |  | - | PCCA_DL=0.9375 |  |  |  |
| PCCA_UL for dynamic channel access Note 4,6 |  |  | - | 0.75 |  |  |  |
| PCCA_UL for semi-static channel access Note 5,6 |  |  | - | 0.87 |  |  |  |
| TDD configuration |  | Config 1, 2, 3, 4, 5, 6 |  | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  | Config 1, 2, 3, 4, 5, 6 |  | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  | Config 1, 2, 3, 4, 5, 6 |  | 40: NPRB,c = 106 |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference |  | Config 1, 2, 3, 4, 5, 6 |  | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  | Config 1, 2, 3, 4, 5, 6 |  | CR.1.1 CCA |  |  |  |
| Dedicated CORESET RMC configuration |  | Config 1, 2, 3, 4, 5, 6 |  | CCR.1.1 CCA |  |  |  |
| TRS configuration |  | Config 1, 2, 3, 4, 5, 6 |  | TRS.1.1 TDD |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |
| DBT window configuration |  | Config 1, 2, 3, 4, 5, 6 |  | DBT.1 |  |  |  |
| SSB configuration for semi-static channel accessNote 4, 6 |  | Config 1, 2, 3, 4, 5, 6 |  | SSB.1 CCA |  |  |  |
| SSB configuration for dynamic channel accessNote 5, 6 |  | Config 1, 2, 3, 4, 5, 6 |  | SSB.2 CCA |  |  |  |
| ssb-PositionQCL |  | Config 1, 2, 3, 4, 5, 6 |  | 1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2, 3, 4, 5, 6 | kHz | 30 kHz |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1, 2, 3, 4, 5, 6 | kHz | 30 kHz |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 under CCA |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | -98 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2, 3, 4, 5, 6 |  | dBm/SCS | -95 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -∞ | 2.36 | 2.36 | 2.36 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -∞ | 11 | 11 | 11 |
| SSB_RP | Config 1, 2, 3, 4, 5, 6 |  | dBm/SCS | -∞ | -84 | -84 | -84 |
| IoNote3 | Config 1, 2, 3, 4, 5, 6 |  | dBm/38.16 MHz | -55.31 | -50.96 | -50.96 | -50.96 |
| Propagation condition |  |  | - | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 6: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |

##### A.11.2.1.9.2 Test Requirements

In this test, the UE shall start to transmit the PRACH to E-UTRA Cell 2 less than 55 ms Note1 from the beginning of time period T3.

The above test requirements shall be fulfilled in order of T1, T2, T3 for the observed inter-RAT handover delay from NR to E-UTRAN to be counted as correct, and in order of T1, T2‘, T3‘, T4‘ for the observed PSCell addition delay to be counted as correct.

The rate of correct handovers and correct PSCell addition delay during repeated tests shall be at least 90 %.

NOTE1: The handover delay can be expressed as specified in clause6.1.5.2:

DHOwithPSCell_PCell = RRC procedure delay + Tinterrupt,

Where RRC procedure delay = 50 ms, and

Tinterrupt = Tsearch_HO + TIU + Tprocessing is defined in clause 6.1.5.2.1, where

Tsearch = 0 ms

TIU = 10 ms,

Tprocessing = 25 ms

DHOwithPSCell_PCell is equal to 85 ms.

The UE shall transmit the PRACH to PSCell no later than DHOwithPSCell_PSCell from the start of T3’. The UE shall send at least one CSI report for PSCell with non-zero CQI index during T4’. The UE shall periodically send CSI reports for PSCell after the UE has sent first CQI report with non-zero CQI index during T4.

The PSCell addition delay can be expressed as follows as specified in clause 6.1.5.5.3:

DHOwithPSCell_PSCell = TRRC_delay + Tprocessing + Tsearch_PCell + Tsearch_PSCell + T∆ + TIU_PSCell + 2 ms

Where:

TRRC_delay = 20 ms

Tprocessing = 25 ms

Tsearch_PCell = 0

Tsearch_PSCell = 0T∆ = (1+ L2) *20 ms.

TIU_PSCell = (1+ L3) *10 + 10 ms

L2 is the number of SMTC occasions not available at the UE during the time tracking period where L2  LCCA_DL, and L3 is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure, where L3  LCCA_UL. L3 = 0 for Type 2C UL channel access procedure as defined in TS 37.213 [33]. The interruption time considering the potential extensions caused by L1, L2, L3 and by the UL CCA failure detection/recovery mechanism is limited by the T304 timer. The UE behaviour at the T304 timer expiry is detailed in TS 38.331 [2]. Test equipment should make sure that LCCA_DL and LCCA_UL are not exceeded during a test by monitoring the number of CCA failures and preventing additional CCA failures from happening after LCCA_DL or LCCA_UL is reached.

The rate of correct PSCell addition observed during repeated tests shall be at least 90 %.

### A.11.2.2 RRC connection mobility control

#### A.11.2.2.1 RRC re-establishment

##### A.11.2.2.1.1 Intra-frequency RRC Re-establishment with CCA in FR1

A.11.2.2.1.1.1 Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay with CCA in FR1 with known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1A.

The test parameters are given in table A.11.2.2.1.1.1-1, table A.11.2.2.1.1.1-2 and table A.11.2.2.1.1.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell with CCA, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.11.2.2.1.1.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

Table A.11.2.2.1.1.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case with CCA

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial Condition | Active cell | - | Cell 1 | Cell 1 is with CCA. |
|  | Neighbour cells | - | Cell 2 | Cell 2 is with CCA. |
| Final condition | Active cell | - | Cell 2 |  |
| RF Channel Number |  | - | 1 |  |
| DL CCA model | Dynamic channel accessNote 1, 3 | - | As specified in clause A.3.26.2.1 |  |
|  | Semi-static channel access Note 2, 3 | - |  |  |
| UL CCA model | Dynamic channel access Note 1, 3 | - | As specified in clause A.3.26.2.2 |  |
|  | Semi-static channel access Note 2,3 | - |  |  |
| LCCA_DL |  |  | 5 |  |
| WCCA_DL |  | ms | T311 |  |
| LCCA_UL |  |  | 5 |  |
| WCCA_UL |  | ms | T311 |  |
| Time offset between cells |  | - | 3 s | Synchronous cells |
| N310 |  | - | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 0 | Radio link failure timer; T310 is disabled |
| T311 |  | ms | 3000 | RRC re-establishment timer |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| SSB configuration | Dynamic channel access Note 1, 3 | - | SSB.2 CCA | Table A.3.10A.1.2-1 |
|  | Semi-static channel access Note 2, 3 | - | SSB.1 CCA | Table A.3.10A.1.1-1 |
| DBT window configuration |  | - | DBT.1 | Table A.3.28.1-1 |
| SMTC configuration |  | - | SMTC pattern 1 |  |
| DRX cycle length |  | s | OFF |  |
| PRACH configuration |  | - | FR1 PRACH configuration 1 under CCA | Table A.3.8A.2.1-1 |
| T1 |  | s | 5 |  |
| T2 |  | ms | 520 | Time for the UE to detect RLF (Summation of TEvaluate_out_SSB defined in clause 8.1A in TS 38.133, T310 and the period for UE turns off transmitter) |
| T3 |  | s | 2 |  |
| NOTE 1: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.   NOTE 2: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.11.2.2.1.1.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case with CCA

| Parameter | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| TDD configuration | - | TDDConf.1.1 CCA |  |  | TDDConf.1.1 CCA |  |  |
| DL CCA probability PCCA_DL for dynamic channel access Note 4,6 | - | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |
| DL CCA probability PCCA_DL for semi-static channel access Note 5,6 | - | PCCA_DL=0.9375 |  |  | PCCA_DL=0.9375 |  |  |
| UL CCA probability PCCA_UL | - | 1 |  |  | 1 |  |  |
| PDSCH RMC configuration |  | SR.1.1 CCA |  |  | SR.1.1 CCA |  |  |
| RMSI CORESET RMC configuration |  | CR.1.1 CCA |  |  | CR.1.1 CCA |  |  |
| Dedicated CORESET RMC configuration |  | CCR.1.1 CCA |  |  | CCR.1.1 CCA |  |  |
| OCNG Pattern |  | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| TRS configuration |  | TRS.1.2 TDD |  |  | N/A |  |  |
| Initial DL BWP configuration |  | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Active DL BWP confgiuration |  | DLBWP.1.1 | N/A | N/A | N/A | N/A | DLBWP.1.1 |
| Active UL BWP configuration |  | ULBWP.1.1 | N/A | N/A | N/A | N/A | ULBWP.1.1 |
| RLM-RS |  | SSB |  |  | SSB |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1.54 | -infinity | -infinity | -3.79 | 4 | 4 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | -95 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 7 | -infinity | -infinity | 4 | 4 | 4 |
| SS-RSRP Note3 | dBm/SCS | -88 | -infinity | -infinity | -91 | -91 | -91 |
| Io | dBm/38.16 MHz | -54.65 | -58.50 | -58.50 | -54.65 | -58.50 | -58.50 |
| Propagation Condition |  | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for NOC to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.   NOTE 5: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |

A.11.2.2.1.1.2 Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to a known NR intra frequency cell with CCA shall be less than 1350 + MAX (200, (5+K1) x 20) ms.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE: The RRC re-establishment delay in the test is derived from the following expression:

$$ T_{re-establish\_delay\_CCA}=T_{UE\_re-establish\_delay\_CCA}+T_{UL\_grant}$$

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

$$ T_{UE\_re-establish\_delay\_CCA}=50ms+T_{identify\_intra\_NR\_CCA}+\sum  _{i=1}^{N_{freq}-1}T_{identify\_inter\_NR\_CCA,i}+T_{SI-NR\_CCA}+T_{PRACH\_CCA}$$

Where

Nfreq = 1

Tidentify_intra_NR_CCA = MAX (200 ms, (5+K1) x TSMTC), where

K1 is the number of SMTC occasions not available at the UE due to DL CCA failures during RRC re-establishment period on the carrier with CCA.

TSMTC = 20 ms is the SMTC periodicity.

Tidentify_inter_NR_CCA = 0 ms

TSI-NR_CCA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target intra-frequency NR cell.

TPRACH_CCA = TSSB,RO + 10 ms, where:

- TSSB,RO is the SSB to PRACH occasion association period as defined in table 8.1-1 of TS 38.213 [39], which is TSSB,RO=10 ms for FR1 PRACH configuration 1 under CCA.

This gives a total of 1350 + MAX (200, (5+K1) x 20) ms, allow 1870 + MAX (200, (5+K1) x 20) ms from the beginning of T2 in the test case.

##### A.11.2.2.1.2 Inter-frequency RRC Re-establishment with CCA in FR1

A.11.2.2.1.2.1 Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay with CCA in FR1 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1A.

The test parameters are given in table A.11.2.2.1.2.1-1, table A.11.2.2.1.2.1-2 and table A.11.2.2.1.2.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell with CCA, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

Table A.11.2.2.1.2.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

Table A.11.2.2.1.2.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial Condition | Active cell | - | Cell 1 | Cell 1 is with CCA. |
|  | Neighbour cells | - | Cell 2 | Cell 2 is with CCA. |
| Final condition | Active cell | - | Cell 2 |  |
| RF Channel Number |  | - | 1, 2 |  |
| DL CCA model | Dynamic channel access Note 1, 3 | - | As specified in clause A.3.26.2.1 |  |
|  | Semi-static channel access Note 2, 3 | - |  |  |
| UL CCA model | Dynamic channel access Note 1, 3 | - | As specified in clause A.3.26.2.2 |  |
|  | Semi-static channel access Note 2, 3 | - |  |  |
| LCCA_DL |  |  | 5 |  |
| WCCA_DL |  | ms | T311 |  |
| LCCA_UL |  |  | 5 |  |
| WCCA_UL |  | ms | T311 |  |
| Time offset between cells |  | - | 3 s | Synchronous cells |
| N310 |  | - | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 0 | Radio link failure timer; T310 is disabled |
| T311 |  | ms | 3000 | RRC re-establishment timer |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| SSB configuration | Dynamic channel access Note 1, 3 | - | SSB.2 CCA | Table A.3.10A.1.2-1 |
|  | Semi-static channel access Note 2, 3 | - | SSB.1 CCA | Table A.3.10A.1.1-1 |
| DBT window configuration |  | - | DBT.1 | Table A.3.28.1-1 |
| SMTC configuration |  | - | SMTC pattern 1 |  |
| DRX cycle length |  | s | OFF |  |
| PRACH configuration |  | - | FR1 PRACH configuration 1 under CCA | Table A.3.8A.2.1-1 |
| T1 |  | s | 5 |  |
| T2 |  | ms | 520 | Time for the UE to detect RLF (Summation of TEvaluate_out_SSB defined in clause 8.1A in TS 38.133, T310 and the period for UE turns off transmitter) |
| T3 |  | s | 2 |  |
| NOTE 1: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.   NOTE 2: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic cannel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.11.2.2.1.2.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1

| Parameter | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| TDD configuration |  | TDDConf.1.1 CCA |  |  | TDDConf.1.1 CCA |  |  |
| DL CCA probability PCCA_DL for dynamic channel access Note 4,6 | - | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |
| DL CCA probability PCCA_DL for semi-static channel access Note 5,6 | - | PCCA_DL=0.9375 |  |  | PCCA_DL=0.9375 |  |  |
| UL CCA probability PCCA_UL | - | 1 |  |  | 1 |  |  |
| PDSCH RMC configuration |  | SR.1.1 CCA |  |  | SR.1.1 CCA |  |  |
| RMSI CORESET RMC configuration |  | CR.1.1 CCA |  |  | CR.1.1 CCA |  |  |
| Dedicated CORESET RMC configuration |  | CCR.1.1 CCA |  |  | CCR.1.1 CCA |  |  |
| OCNG Pattern |  | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| TRS configuration |  | TRS.1.2 TDD |  |  | N/A |  |  |
| Initial DL BWP configuration |  | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Active DL BWP confgiuration |  | DLBWP.1.1 | N/A | N/A | N/A | N/A | DLBWP.1.1 |
| Active UL BWP configuration |  | ULBWP.1.1 | N/A | N/A | N/A | N/A | ULBWP.1.1 |
| RLM-RS |  | SSB |  |  | SSB |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 7 | -infinity | -infinity | -infinity | -infinity | 4 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | -95 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 7 | -infinity | -infinity | -infinity | -infinity | 4 |
| SS-RSRP Note3 | dBm/SCS | -88 | -infinity | -infinity | -infinity | -infinity | -91 |
| Io | dBm/9.36 MHz | -56.15 | -63.94 | -63.94 | -63.94 | -63.94 | -58.50 |
| Propagation Condition |  | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for NOC to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.   NOTE 5: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |

A.11.2.2.1.2.2 Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell shall be less than $ T_{re-establish_{delay_{CCA}}}$.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE: The RRC re-establishment delay in the test is derived from the following expression:

$$ T_{re-establish_{delay_{CCA}}}=T_{UE_{re}-establish_{delay_{CCA}}}+T_{UL_{grant}}$$

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

$$ T_{UE\_re-establish\_delay\_CCA}=50ms+T_{identify\_intra\_NR\_CCA}+\sum  _{i=1}^{N_{freq}-1}T_{identify\_inter\_NR\_CCA,i}+T_{SI-NR\_CCA}+T_{PRACH\_CCA}$$

Where

Tidentify_intra_NR_CCA: 0 ms

Tidentify_inter_NR_CCA,i: MAX (200 ms, ([6]+K2,i) x TSMTC, i),

where

K2,i is the number of SMTC not available at the UE during RRC re-establishment period on the “i” th carrier with CCA

TSMTC,i: It is the periodicity of the SMTC occasion configured for the inter-frequency carrier i.

Nfreq = 2

TSI-NR_CCA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH_CCA = (1+ K3)*TSSB,RO + 10 ms, where:

- TSSB,RO is the SSB to PRACH occasion association period as defined in table 8.1-1 of TS 38.213 [3].

- K3 is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure. K3 = 0 for Type 2C UL channel access procedure as defined in TS 37.213 [33].

This gives a total of $ T_{re-establish_{delay_{CCA}}}$ = 50 + MAX (200 ms, (6+K2,1) x TSMTC, 1) + 1280 + (1+ K3)*TSSB,RO + 10 ms, allow 1860 + MAX (200 ms, (6+K2,1) x TSMTC, 1) + (1+ K3)*TSSB,RO ms from the beginning of T2 in the test case.

A.11.2.2.1.3 Intra-frequency RRC Re-establishment with CCA in FR1 without serving cell timing

A.11.2.2.1.3.1 Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay with CCA in FR1 without serving cell timing is within the specified limits. These tests will verify the requirements in clause 6.2.1A.

The test parameters are given in table A.11.2.2.1.3.1-1, table A.11.2.2.1.3.1-2 and table A.11.2.2.1.3.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell with CCA, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.11.2.2.1.3.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

Table A.11.2.2.1.3.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial Condition | Active cell | - | Cell 1 | Cell 1 is with CCA. |
|  | Neighbour cells | - | Cell 2 | Cell 2 is with CCA. |
| Final condition | Active cell | - | Cell 2 |  |
| RF Channel Number |  | - | 1 |  |
| DL CCA model | Dynamic channel accessNote 1,3 | - | As specified in clause A.3.26.2.1 |  |
|  | Semi-static channel access Note 2,3 | - |  |  |
| UL CCA model | Dynamic channel access Note 1,3 | - | As specified in clause A.3.26.2.2 |  |
|  | Semi-static channel access Note 2,3 | - |  |  |
| LCCA_DL |  |  | 5 |  |
| WCCA_DL |  | ms | T311 |  |
| LCCA_UL |  |  | 5 |  |
| WCCA_UL |  | ms | T311 |  |
| Time offset between cells |  | - | 3 s | Synchronous cells |
| N310 |  | - | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 0 | Radio link failure timer; T310 is disabled |
| T311 |  | ms | 3000 | RRC re-establishment timer |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| SSB configuration | Dynamic channel access Note 1, 3 | - | SSB.2 CCA | Table A.3.10A.1.2-1 |
|  | Semi-static channel access Note 2, 3 | - | SSB.1 CCA | Table A.3.10A.1.1-1 |
| DBT window configuration |  | - | DBT.1 | Table A.3.28.1-1 |
| SMTC configuration |  | - | SMTC pattern 1 |  |
| DRX cycle length |  | s | OFF |  |
| PRACH configuration |  | - | FR1 PRACH configuration 1 | Table A.3.8A.2.1-1 |
| T1 |  | s | 5 |  |
| T2 |  | ms | 520 | Time for the UE to detect RLF (Summation of TEvaluate_out_SSB defined in clause 8.1A in TS 38.133, T310 and the period for UE turns off transmitter) |
| T3 |  | s | ≥ TUE_re-establish_delay_CCA | As defined in clause 6.2.1A |
| NOTE 1: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.   NOTE 2: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic cannel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.11.2.2.1.3.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR1

| Parameter | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| TDD configuration |  | TDDConf.1.1 CCA |  |  | TDDConf.1.1 CCA |  |  |
| DL CCA probability PCCA_DL for dynamic channel access Note 4,6 | - | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |
| DL CCA probability PCCA_DL for semi-static channel access Note 5,6 | - | PCCA_DL=0.9375 |  |  | PCCA_DL=0.9375 |  |  |
| UL CCA probability PCCA_UL | - | 1 |  |  | 1 |  |  |
| PDSCH RMC configuration |  | SR.1.1 CCA |  |  | SR.1.1 CCA |  |  |
| RMSI CORESET RMC configuration |  | CR.1.1 CCA |  |  | CR.1.1 CCA |  |  |
| Dedicated CORESET RMC configuration |  | CCR.1.1 CCA |  |  | CCR.1.1 CCA |  |  |
| OCNG Pattern |  | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| TRS configuration |  | TRS.1.2 TDD |  |  | N/A |  |  |
| Initial DL BWP configuration |  | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Active DL BWP confgiuration |  | DLBWP.1.1 | N/A | N/A | N/A | N/A | DLBWP.1.1 |
| Active UL BWP configuration |  | ULBWP.1.1 | N/A | N/A | N/A | N/A | ULBWP.1.1 |
| RLM-RS |  | SSB |  |  | SSB |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 4 | -infinity | -infinity | -infinity | -infinity | 4 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | -95 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | -98 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 4 | -infinity | -infinity | -infinity | -infinity | 4 |
| SS-RSRP Note3 | dBm/SCS | -91 | -infinity | -infinity | -infinity | -infinity | -91 |
| Io | dBm/38.16 MHz | -58.50 | -63.94 | -63.94 | -63.94 | -63.94 | -58.50 |
| Propagation Condition |  | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for NOC to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.   NOTE 5: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |

A.11.2.2.1.3.2 Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR intra frequency cell without serving cell timing shall be less than 1350 + MAX (800 ms, (10+ K1) x 20) ms.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE: The RRC re-establishment delay in the test is derived from the following expression:

$$ T_{re-establish\_delay\_CCA}=T_{UE\_re-establish\_delay\_CCA}+T_{UL\_grant}$$

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

$$ T_{UE\_re-establish\_delay\_CCA}=50ms+T_{identify\_intra\_NR\_CCA}+\sum  _{i=1}^{N_{freq}-1}T_{identify\_inter\_NR\_CCA,i}+T_{SI-NR\_CCA}+T_{PRACH\_CCA}$$

Where,

Nfreq = 1

Tidentify_intra_NR = MAX (800 ms, (10+ K1) x TSMTC), where

K1 is the number of SMTC occasions not available at the UE due to DL CCA failures during RRC re-establishment period on the carrier with CCA.

TSMTC is the SMTC periodicity which is 20 ms.

Tidentify_inter_NR_CCA = 0 ms

TSI-NR_CCA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 [2] for the target intra-frequency NR cell.

TPRACH_CCA = (1+ K3)*TSSB,RO + 10 ms, where:

- TSSB,RO is the SSB to PRACH occasion association period as defined in table 8.1-1 of TS 38.213 [39]. It is 10 ms for FR1 PRACH configuration 1 under CCA.

- K3 = 0.

This gives total $ T_{UE\_re-establish\_delay\_CCA}$=1350 + MAX (800 ms, (10+ K1) x 20) ms, allow 1870 + MAX (800 ms, (10+ K1) x 20) ms from the beginning of T2 in the test case.

##### A.11.2.2.1.4 Inter-frequency RRC Re-establishment from NR FR1 carrier without CCA to NR FR1 carrier under CCA

A.11.2.2.1.4.1 Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay requirement for RRC re-establishment from NR FR1 carrier without CCA to NR FR1 inter-frequency carrier under CCA with unknown target cell. These tests will verify the requirements in clause 6.2.1A.

The test parameters are given in table A.11.2.2.1.4.1-1, table A.11.2.2.1.4.1-2 and table A.11.2.2.1.4.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

Table A.11.2.2.1.4.1-1: Supported test configurations inter-frequency RRC re-establishment from NR FR1 without under CCA to NR FR1 inter-frequency carrier under CCA

| Configuration | Source cell without CCA | Target cell with CCA |
| --- | --- | --- |
| 1 | 15 kHz SSB SCS, 10 MHz bandwidth, FDD | 30 kHz SSB SCS, 40 MHz bandwidth, TDD |
| 2 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD | 30 kHz SSB SCS, 40 MHz bandwidth, TDD |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD | 30 kHz SSB SCS, 40 MHz bandwidth, TDD |
| NOTE:  The UE is only required to be tested in one of the supported test configurations |  |  |

Table A.11.2.2.1.4.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case from NR FR1 carrier without CCA to NR FR1 inter-frequency carrier under CCA

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | Cell 1 |  |
|  | Neighbour cells |  | Cell 2 |  |
| Final condition | Active cell |  | Cell 2 |  |
| RF Channel Number |  |  | 1, 2 |  |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| DL CCA model | Dynamic channel accessNote 1,3 |  | As specified in clause A.3.26.2.1 |  |
|  | Semi-static channel access Note 2,3 |  |  |  |
| UL CCA model | Dynamic channel access Note 1,3 |  | As specified in clause A.3.26.2.2 |  |
|  | Semi-static channel access Note 2,3 |  |  |  |
| LCCA_DL |  |  | 5 |  |
| WCCA_DL |  | ms | T311 |  |
| LCCA_UL |  |  | 5 |  |
| WCCA_UL |  | ms | T311 |  |
| N310 |  | - | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 0 | Radio link failure timer; T310 is disabled |
| T311 |  | ms | 5000 | RRC re-establishment timer |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| DRX cycle length |  | s | OFF |  |
| PRACH configuration |  |  | FR1 PRACH configuration 1 | Table A.3.8A.2.1-1 |
| T1 |  | s | 5 |  |
| T2 |  | ms | 520 | Time for the UE to detect RLF (Summation of TEvaluate_out_SSB defined in clause 8.1A in TS 38.133, T310 and the period for UE turns off transmitter) |
| T3 |  | s | ≥ TUE_re-establish_delay_CCA | As defined in clause 6.2.1A |

Table A.11.2.2.1.4.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case from NR FR1 carrier without CCA to NR FR1 inter-frequency carrier under CCA

| Parameter |  | Test config | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| TDD configuration |  | 1 |  | N/A |  |  | TDDConf.1.1.CCA |  |  |
|  |  | 2 |  | TDDConf.1.1 |  |  | TDDConf.1.1.CCA |  |  |
|  |  | 3 |  | TDDConf.2.1 |  |  | TDDConf.1.1.CCA |  |  |
| PDSCH RMC configuration |  | 1 |  | SR.1.1 FDD |  |  | SR.1.1 CCA |  |  |
|  |  | 2 |  | SR.1.1 TDD |  |  | SR.1.1 CCA |  |  |
|  |  | 3 |  | SR.2.1 TDD |  |  | SR.1.1 CCA |  |  |
| RMSI CORESET RMC configuration |  | 1 |  | CR.1.1 FDD |  |  | CR.1.1 CCA |  |  |
|  |  | 2 |  | CR.1.1 TDD |  |  | CR.1.1 CCA |  |  |
|  |  | 3 |  | CR.2.1 TDD |  |  | CR.1.1 CCA |  |  |
| Dedicated CORESET RMC configuration |  | 1 |  | CCR.1.1 FDD |  |  | CCR.1.1 CCA |  |  |
|  |  | 2 |  | CCR.1.1 TDD |  |  | CCR.1.1 CCA |  |  |
|  |  | 3 |  | CCR.2.1 TDD |  |  | CCR.1.1 CCA |  |  |
| OCNG Pattern |  | 1 |  | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| TRS configuration |  | 1 |  | TRS.1.1 FDD |  |  | TRS.1.2 TDD |  |  |
|  |  | 2 |  | TRS.1.1 TDD |  |  | TRS.1.2 TDD |  |  |
|  |  | 3 |  | TRS.1.2 TDD |  |  | TRS.1.2 TDD |  |  |
| SMTC configuration |  | 1,2,3 |  | SMTC.1 |  |  | SMTC.1 |  |  |
| SSB configuration | Semi- static channel acces | 1,2 |  | SSB.1 FR1 |  |  | SSB.1 CCA |  |  |
|  | Semi- static channel acces | 3 |  | SSB.2 FR1 |  |  | SSB.1 CCA |  |  |
|  | Dymamic channel acces | 1,2 |  | SSB.1 FR1 |  |  | SSB.2 CCA |  |  |
|  | Dymamic channel acces | 3 |  | SSB.2 FR1 |  |  | SSB.2 CCA |  |  |
| Initial DL BWP configuration |  | 1,2,3 |  | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1,2,3 |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Active DL BWP confgiuration |  | 1,2,3 |  | DLBWP.1.1 | N/A | N/A | N/A | N/A | DLBWP.1.1 |
| Active UL BWP configuration |  | 1,2,3 |  | ULBWP.1.1 | N/A | N/A | N/A | N/A | ULBWP.1.1 |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | 1,2,3 |  | N/A | N/A | N/A | 1 | 1 | 0.9375 |
| DL CCA probability for for dynamic static channel access (PCCA_DL_1) |  | 1,2,3 |  | N/A | N/A | N/A | 1 | 1 | 0.75 |
| DL CCA probability for for dynamic static channel access (PCCA_DL_2) |  | 1,2,3 |  | N/A | N/A | N/A | 1 | 1 | 0.75 |
| UL CCA probability (PCCA_UL) |  | 1,2,3 |  | N/A | N/A | N/A | 1 | 1 | 1 |
| RLM-RS |  | 1,2,3 |  | SSB |  |  | SSB |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  | 1,2,3 | dB | 4 | -infinity | -infinity | -infinity | -infinity | 7 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 |  | 1,2,3 | dBm/15 KHz | -98 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 |  | 1,2 | dBm/SCS | -98 |  |  |  |  |  |
|  |  | 3 |  | -95 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | 1,2,3 | dB | 4 | -infinity | -infinity | -infinity | -infinity | 7 |
| SS-RSRP Note3 |  | 1, 2 | dBm/SCS | -94 | -infinity | -infinity | -infinity | -infinity | -91 |
|  |  | 3 |  | -91 | -infinity | -infinity | -infinity | -infinity | -88 |
| Io |  | 1,2 | dBm/9.36 MHz | -64.59 | -70.05 | -70.05 | -63.94 | -63.94 | -56.15 |
|  |  | 3 | dBm/38.16 MHz | -58.50 | -63.94 | -63.94 | -63.94 | -63.94 | -56.15 |
| Propagation Condition |  | 1,2,3 |  | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for NOC to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Parameters PCCA_DL, PCCA_DL_1, PCCA_DL_2 and PCCA_UL are defined in clause A.3.26.2.NOTE 5: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |  |  |

A.11.2.2.1.4.2 Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell shall be less $ T_{UE\_re-establish\_delay\_CCA}$.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE: The RRC re-establishment delay in the test is derived from the following expression:

$$ T_{re-establish\_delay\_CCA}=T_{UE\_re-establish\_delay\_CCA}+T_{UL\_grant}$$

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

$$ T_{UE\_re-establish\_delay\_CCA}=50ms+T_{identify\_intra\_NR\_CCA}+\sum  _{i=1}^{N_{freq}-1}T_{identify\_inter\_NR\_CCA,i}+T_{SI-NR\_CCA}+T_{PRACH\_CCA}$$

Nfreq = 2

Tidentify_intra_NR_CCA = MAX (800 ms, (10+ K1) x 20) ms

Tidentify_inter_NR_CCA = MAX (800 ms, (13+K2,2) x 20) ms

TSI-NR_CCA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH_CCA = It is the delay uncertainty in acquiring the first available PRACH occasion in the target NR cell. TPRACH_CCA = (1+ K3)*TSSB,RO + 10 ms; where K3=0 and TSSB,RO=10 ms for FR1 PRACH configuration 1 under CCA.

K1 is the number of SMTC occasions not available at the UE due during RRC re-establishment period on the carrier with CCA and with RF channel number # 1.

K2,2 is the number of SMTC occasions not available at the UE during RRC re-establishment period on the carrier with CCA and with RF channel number # 2.

This gives total $ T_{UE\_re-establish\_delay\_CCA}$=1350+MAX (800 ms, (10+ K1) x 20) ms+MAX (800 ms, ([13]+K2,2) x 20) ms, allow 1870 + MAX (800 ms, (10+ K1) x 20) ms+MAX (800 ms, ([13]+K2,2) x 20) ms from the beginning of T2 in the test case.

#### A.11.2.2.2 Random Access


##### A.11.2.2.2.1 4-step RA type contention-based random access for NR PCell with CCA

###### A.11.2.2.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause6.2.2A.2 and clause7.1.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1, which operates on a carrier frequency with CCA.  Supported test parameters are shown in table A.11.2.2.2.1.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.11.2.2.2.1.1-2.

Table A.11.2.2.2.1.1-1: Supported test configurations for contention based random access test for FR1 PCell with CCA

| Config | Description |
| --- | --- |
| 1 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: Void |  |

Table A.11.2.2.2.1.1-2: General test parameters for contention based random access test for FR1 PCell with CCA

| Parameter |  |  |  |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SSB Configuration | Note 4, 6 |  |  | Config 1 |  | SSB.3 CCA | As defined in A.3.10A |
|  | Note 5, 6 |  |  | Config 1 |  | SSB.4 CCA | As defined in A.3.10A |
| DBT Window Configuration |  |  |  | Config 1 |  | DBT.1 | As specified in A.3.28.1 |
| DL CCA model |  |  |  | Config 1 |  | As specified in A.3.26.2.1 |  |
| UL CCA model |  |  |  | Config 1 |  | As specified in A.3.26.2.2 |  |
| Duplex Mode for Cell 2 |  |  |  | Config 1 |  | TDD |  |
| TDD Configuration |  |  |  | Config 1 |  | TDDConf.1.1 CCA |  |
| OCNG Pattern Note 1 |  |  |  |  |  | OCNG pattern 1 | As defined in A.3.2.1. |
| PDSCH parameters Note 3 |  |  |  | Config 1 |  | SR.1.1 CCA | As defined in A.3.1A.1. |
| NR RF Channel Number |  |  |  |  |  | 1 |  |
| EPRE ratio of PSS to SSS |  |  |  |  | dB | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  | dB |  |  |
| SSB with index 0 |  | ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 3 | Power of SSB with index 0 is set to be above configured rsrp-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 |  |
|  |  | SS-RSRP |  |  | dBm/ SCS | -95 |  |
| SSB with index 1 |  | ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -17 | Power of SSB with index 1 is set to be below configured rsrp-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -17 |  |
|  |  | SS-RSRP |  |  | dBm/ SCS | -115 |  |
| Io Note 2 |  |  |  | Config 1 | dBm | -62.2/38.16 MHz | For symbols without SSB index 1 |
| ss-PBCH-BlockPower |  |  |  |  | dBm/ SCS | -5 | As defined in clause 6.3.2 in TS 38.331 [2]. |
| Configured UE transmitted power (PCMAX,f,c) |  |  |  |  | dBm | 23 | As defined in clause 6.2.4 in TS 38.101-1. |
| PRACH Configuration |  |  |  |  |  | FR1 PRACH configuration 1 under CCA | As defined in A.3.8A.2. |
| DL CCA probability |  |  | Note 4, 6 |  |  | 0.9375 |  |
| PCCA_DL |  |  | Note 5, 6 |  |  | 0.75 / 0.75 |  |
| LCCA_DL Note 7 |  |  |  |  |  | 4 |  |
| WCCA_DL Note 8 |  |  |  |  |  | Inf |  |
| UL CCA probability |  |  | Note 4, 6 |  |  | 0.87 |  |
| PCCA_UL |  |  | Note 5, 6 |  |  | 0.75 |  |
| LCCA_UL Note 7 |  |  |  |  |  | 5 |  |
| WCCA_UL Note 8 |  |  |  |  |  | Inf |  |
| Semi-static channel access config period Note 4, 6 |  |  |  |  | ms | 2 |  |
| Propagation Condition |  |  |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters.NOTE 3: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic channel occupancy and semi-static channel occupancy configuration.NOTE 7: LCCA_DL and LCCA_UL are chosen such that preambleTransMax > 5 + LCCA_DL + LCCA_UL.NOTE 8: A window WCCA_DL=WCCA_UL=Inf is used to indicate that LCCA_DL and LCCA_UL are considered during the entire duration of a test run. |  |  |  |  |  |  |  |

###### A.11.2.2.2.1.2 Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

###### A.11.2.2.2.1.2.1 Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2.2A.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB, if the UL CCA is successful.

The three requirements below are relevant for all cases of PRACH transmissions described within the whole clause A.11.2.2.2.1.2:

- The System Simulator shall implement the UL CCA model of A.3.26.2 for the RACH occasions where PRACH transmissions are expected. The System Simulator shall monitor the RACH occasions to detect if the UE is transmitting PRACH preambles. If a PRACH transmission is detected on a RACH occasion that is expected to have UL CCA failure, the test is considered as failed.

- In case of CCA DL failure, the test equipment should verify that the UE does not transmit PRACH for semi-static channel access mode; for dynamic channel access mode it is assumed that RACH occasions are always scheduled within a UE-initiated COT.

- In case of UL CCA failure, The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.11.2.2.2.1.2.2 Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 transmission is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.11.2.2.2.1.2.3 No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.11.2.2.2.1.2.4 Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2.2A.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

###### A.11.2.2.2.1.2.5 Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2.2A.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

###### A.11.2.2.2.1.2.6 Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2.2A.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

###### A.11.2.2.2.1.2.7 Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2.2A.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

##### A.11.2.2.2.2 4-step RA type non-contention based random access for NR PSCell with CCA

###### A.11.2.2.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause6.2.2A.2 and clause7.1.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1, which operates on a carrier frequency with CCA. Supported test parameters are shown in table A.11.2.2.2.2.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.11.2.2.2.2.1-2.

Table A.11.2.2.2.2.1-1: Supported test configurations for non-contention based random access test for FR1 PCell with CCA

| Config | Description |
| --- | --- |
| 1 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: Void |  |

Table A.11.2.2.2.2.1-2: General test parameters for non-contention based random access test for FR1 PCell with CCA

| Parameter |  |  |  |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SSB Configuration | Note 4, 6 |  |  | Config 1 |  | SSB.3 CCA | As defined in A.3.10A |
|  | Note 5, 6 |  |  | Config 1 |  | SSB.4 CCA | As defined in A.3.10A |
| DBT Window Configuration |  |  |  | Config 1 |  | DBT.1 | As specified in A.3.28.1 |
| DL CCA model |  |  |  | Config 1 |  | As specified in A.3.26.2.1 |  |
| UL CCA model |  |  |  | Config 1 |  | As specified in A.3.26.2.2 |  |
| Duplex Mode for Cell 2 |  |  |  | Config 1 |  | TDD |  |
| TDD Configuration |  |  |  | Config 1 |  | TDDConf.1.1 CCA |  |
| OCNG Pattern Note 1 |  |  |  |  |  | OCNG pattern 1 | As defined in A.3.2.1. |
| PDSCH parameters Note 3 |  |  |  | Config 1 |  | SR.1.1 CCA | As defined in A.3.1A.1. |
| NR RF Channel Number |  |  |  |  |  | 1 |  |
| EPRE ratio of PSS to SSS |  |  |  |  | dB | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  | dB |  |  |
| SSB with index 0 |  | ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 3 | Power of SSB with index 0 is set to be above configured rsrp-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 |  |
|  |  | SS-RSRP |  |  | dBm/ SCS | -95 |  |
| SSB with index 1 |  | ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -17 | Power of SSB with index 1 is set to be below configured rsrp-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -17 |  |
|  |  | SS-RSRP |  |  | dBm/ SCS | -115 |  |
| Io Note 2 |  |  |  | Config 1 | dBm | -62.2/38.16 MHz | For symbols without SSB index 1 |
| ss-PBCH-BlockPower |  |  |  |  | dBm/ SCS | -5 | As defined in clause 6.3.2 in TS 38.331 [2]. |
| Configured UE transmitted power (![](media_svg/image7.svg) [公式≈: ^{P}CMAX,f,c]) |  |  |  |  | dBm | 23 | As defined in clause 6.2.4 in TS 38.101-1. |
| PRACH Configuration |  |  |  |  |  | FR1 PRACH configuration 2 under CCA | As defined in A.3.8A.2. |
| DL CCA probability |  |  | Note 4, 6 |  |  | 0.9375 |  |
| PCCA_DL |  |  | Note 5, 6 |  |  | 0.75 / 0.75 |  |
| LCCA_DL Note 7 |  |  |  |  |  | 4 |  |
| WCCA_DL Note 8 |  |  |  |  |  | Inf |  |
| UL CCA probability |  |  | Note 4, 6 |  |  | 0.87 |  |
| PCCA_UL |  |  | Note 5, 6 |  |  | 0.75 |  |
| LCCA_UL Note 7 |  |  |  |  |  | 5 |  |
| WCCA_UL Note 8 |  |  |  |  |  | Inf |  |
| Semi-static channel access config period Note 4, 6 |  |  |  |  | ms | 2 |  |
| Propagation Condition |  |  |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters.NOTE 3: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic channel occupancy and semi-static channel occupancy configuration.NOTE 7: LCCA_DL and LCCA_UL are chosen such that preambleTransMax > 5 + LCCA_DL + LCCA_UL.NOTE 8: A window WCCA_DL=WCCA_UL=Inf is used to indicate that LCCA_DL and LCCA_UL are considered during the entire duration of a test run. |  |  |  |  |  |  |  |

###### A.11.2.2.2.2.2 Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

###### A.11.2.2.2.2.2.1 SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2A.2.2.1 for SSB-based Random Access Preamble transmission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

The three requirements below are relevant for all cases of PRACH transmissions described within the clause A.11.2.2.2.2.2:

- The System Simulator shall implement the UL CCA model of A.3.26.2 for the RACH occasions where PRACH transmissions are expected. The System Simulator shall monitor the RACH occasions to detect if the UE is transmitting PRACH preambles. If a PRACH transmission is detected on a RACH occasion that is expected to have UL CCA failure, the test is considered as failed.

- In case of CCA DL failure, the test equipment should verify that the UE does not transmit PRACH for semi-static channel access mode; for dynamic channel access mode it is assumed that RACH occasions are always scheduled within a UE-initiated COT.

- In case of UL CCA failure The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belong to the PRACH occasions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.11.2.2.2.2.2.2 Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.11.2.2.2.2.2.3 No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

##### A.11.2.2.2.3 2-step RA type contention-based random access for NR PCell with CCA

###### A.11.2.2.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the 2-step RA type random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause6.2.2A.3 and clause7.1.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1, which operates on a carrier frequency with CCA. Supported test parameters are shown in table A.11.2.2.2.3.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.11.2.2.2.3.1-2.

Table A.11.2.2.2.3.1-1: Supported test configurations for 2-step RA type contention based random access with successRAR test for FR1 PCell with CCA

| Config | Description |
| --- | --- |
| 1 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: Void |  |

Table A.11.2.2.2.3.1-2: General test parameters for 2-step RA type contention based random access with successRAR test for FR1 PCell with CCA

| Parameter |  |  |  |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SSB Configuration | Note 4, 6 |  |  | Config 1 |  | SSB.3 CCA | As defined in A.3.10A |
|  | Note 5, 6 |  |  | Config 1 |  | SSB.4 CCA | As defined in A.3.10A |
| DBT Window Configuration |  |  |  | Config 1 |  | DBT.1 | As specified in A.3.28.1 |
| DL CCA model |  |  |  | Config 1 |  | As specified in A.3.26.2.1 |  |
| UL CCA model |  |  |  | Config 1 |  | As specified in A.3.26.2.2 |  |
| Duplex Mode for Cell 2 |  |  |  | Config 1 |  | TDD |  |
| TDD Configuration |  |  |  | Config 2 |  | TDDConf.1.1 CCA |  |
| OCNG Pattern Note 1 |  |  |  |  |  | OCNG pattern 1 | As defined in A.3.2.1. |
| PDSCH parameters Note 3 |  |  |  | Config 1 |  | SR.1.1 CCA | As defined in A.3.1A.1. |
| NR RF Channel Number |  |  |  |  |  | 1 |  |
| EPRE ratio of PSS to SSS |  |  |  |  | dB | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  | dB |  |  |
| SSB with index 0 |  | ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 3 | Power of SSB with index 0 is set to be above configured msgA-RSRP-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 |  |
|  |  | SS-RSRP |  |  | dBm/ SCS | -95 |  |
| SSB with index 1 |  | ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -17 | Power of SSB with index 1 is set to be below configured msgA-RSRP-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -17 |  |
|  |  | SS-RSRP |  |  | dBm/ SCS | -115 |  |
| Io Note 2 |  |  |  | Config 1 | dBm | -62.2/38.16 MHz | For symbols without SSB index 1 |
| ss-PBCH-BlockPower |  |  |  |  | dBm/ SCS | -5 | As defined in clause 6.3.2 in TS 38.331 [2]. |
| Configured UE transmitted power (PCMAX,f,c) |  |  |  |  | dBm | 23 | As defined in clause 6.2.4 in TS 38.101-1. |
| MsgA Configuration |  |  |  |  |  | FR1 MsgA configuration 1 under CCA | As defined in A.3.20A.2. |
| msgA-RSRP-ThresholdSSB |  |  |  |  | dBm | RSRP_51 | The actual value of the threshold is -105 dBm, as defined in TS 38.331 [2]. |
| DL CCA probability |  |  | Note 4, 6 |  |  | 0.9375 |  |
| PCCA_DL |  |  | Note 5, 6 |  |  | 0.75 / 0.75 |  |
| LCCA_DL Note 7 |  |  |  |  |  | 4 |  |
| WCCA_DL Note 8 |  |  |  |  |  | Inf |  |
| UL CCA probability |  |  | Note 4, 6 |  |  | 0.87 |  |
| PCCA_UL |  |  | Note 5, 6 |  |  | 0.75 |  |
| LCCA_UL Note 7 |  |  |  |  |  | 5 |  |
| WCCA_UL Note 8 |  |  |  |  |  | Inf |  |
| Semi-static channel access config period Note 4, 6 |  |  |  |  | ms | 2 |  |
| Propagation Condition |  |  |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters.NOTE 3: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic channel occupancy and semi-static channel occupancy configuration.NOTE 7: LCCA_DL and LCCA_UL are chosen such that preambleTransMax > 5 + LCCA_DL + LCCA_UL.NOTE 8: A window WCCA_DL=WCCA_UL=Inf is used to indicate that LCCA_DL and LCCA_UL are considered during the entire duration of a test run. |  |  |  |  |  |  |  |

###### A.11.2.2.2.3.2 Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

###### A.11.2.2.2.3.2.1 MsgA Transmission

To test the UE behavior specified in clause 6.2.2A.3.1.1 the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured msgA-RSRP-ThresholdSSB, if the UL CCA is successful.

The three requirements below are relevant for all cases of MsgA transmissions described within the clause A.11.2.2.2.3.2:

- The System Simulator shall implement the UL CCA model for the MsgA occasions (i.e. both MsgA PRACH and MsgA PUSCH occasions) where MsgA transmissions are expected. The System Simulator shall monitor the MsgA occasions to detect if the UE is transmitting MsgA. If a MsgA transmission is detected on MsgA occasions that are expected to have UL CCA failure, the test is considered as failed.

- In case of CCA DL failure, the test equipment should verify that the UE does not transmit MsgA for semi-static channel access mode; for dynamic channel access mode it is assumed that MsgA occasions are always scheduled within a UE-initiated COT.

- The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated PRACH transmission power in case of UL CCA failure.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble transmission shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be $ 0.6+3\left ( \mu  +2\right ) $ dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where $\mu  $ indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.11.2.2.2.3.2.2 MsgB Reception

To test the UE behavior specified in clause 6.2.2A.3.1.2 the System Simulator shall transmit a MsgB containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE may stop monitoring for MsgB(s) and shall transmit an ACK if the MsgB with a successRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble and if the Contention Resolution is successful and if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting ACK in the case of CCA UL failure. If ACK transmission is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB(s) contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be $ 0.6+3\left ( \mu  +2\right ) $ dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where $\mu  $ indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.11.2.2.2.3.2.3 No MsgB Reception

To test the UE behavior specified in clause 6.2.2A.3.1.3 the System Simulator shall transmit a MsgB containing a successRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if no MsgB is received within the MsgB Response window.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be $ 0.6+3\left ( \mu  +2\right ) $ dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where $\mu  $ indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

##### A.11.2.2.2.4 2-step RA type non-contention-based random access for NR PCell with CCA

###### A.11.2.2.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause6.2.2A.3 and clause7.1.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1, which operates on a carrier frequency with CCA. Supported test parameters are shown in table A.11.2.2.2.4.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.11.2.2.2.4.1-2.

Table A.11.2.2.2.4.1-1: Supported test configurations for non-contention based random access test for FR1 PCell with CCA

| Config | Description |
| --- | --- |
| 1 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: Void |  |

Table A.11.2.2.2.4.1-2: General test parameters for non-contention based random access test for FR1 PCell with CCA

| Parameter |  |  |  |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SSB Configuration | Note 4, 6 |  |  | Config 1 |  | SSB.3 CCA | As defined in A.3.10A |
|  | Note 5, 6 |  |  | Config 1 |  | SSB.4 CCA | As defined in A.3.10A |
| DBT Window Configuration |  |  |  | Config 1 |  | DBT.1 | As specified in A.3.28.1 |
| DL CCA model |  |  |  | Config 1 |  | As specified in A.3.26.2.1 |  |
| UL CCA model |  |  |  | Config 1 |  | As specified in A.3.26.2.2 |  |
| Duplex Mode for Cell 1 |  |  |  | Config 1 |  | TDD |  |
| TDD Configuration |  |  |  | Config 1 |  | TDDConf.1.1 CCA |  |
| OCNG Pattern Note 1 |  |  |  |  |  | OCNG pattern 1 | As defined in A.3.2.1. |
| PDSCH parameters Note 3 |  |  |  | Config 1 |  | SR.1.1 CCA | As defined in A.3.1A.1. |
| NR RF Channel Number |  |  |  |  |  | 1 |  |
| EPRE ratio of PSS to SSS |  |  |  |  | dB | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  | dB |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  | dB |  |  |
| msgA-RSRP-ThresholdSSB |  |  |  |  | dBm | RSRP_51 | The actual value of the threshold is -105 dBm, as defined in TS 38.331 [2]. |
| SSB with index 0 |  | ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 3 | Power of SSB with index 0 is set to be above configured msgA-RSRP-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 |  |
|  |  | SS-RSRP |  |  | dBm/ SCS | -95 |  |
| SSB with index 1 |  | ![](media_svg/image5.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -17 | Power of SSB with index 1 is set to be below configured msgA-RSRP-ThresholdSSB |
|  |  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] |  | Config 1 | dBm/15 kHz | -101 |  |
|  |  | ![](media_svg/image6.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -17 |  |
|  |  | SS-RSRP |  |  | dBm/ SCS | -115 |  |
| Io Note 2 |  |  |  | Config 1 | dBm | -62.2/38.16 MHz | For symbols without SSB index 1 |
| ss-PBCH-BlockPower |  |  |  |  | dBm/ SCS | -5 | As defined in clause 6.3.2 in TS 38.331 [2]. |
| Configured UE transmitted power (![](media_svg/image7.svg) [公式≈: ^{P}CMAX,f,c]) |  |  |  |  | dBm | 23 | As defined in clause 6.2.4 in TS 38.101-1. |
| MsgA Configuration |  |  |  |  |  | FR1 MsgA configuration 2 under CCA | As defined in A.3.20A.2. |
| DL CCA probability |  |  | Note 4, 6 |  |  | 0.9375 |  |
| PCCA_DL |  |  | Note 5, 6 |  |  | 0.75 / 0.75 |  |
| LCCA_DL Note 7 |  |  |  |  |  | 4 |  |
| WCCA_DL Note 8 |  |  |  |  |  | Inf |  |
| UL CCA probability |  |  | Note 4, 6 |  |  | 0.87 |  |
| PCCA_UL |  |  | Note 5, 6 |  |  | 0.75 |  |
| LCCA_UL Note 7 |  |  |  |  |  | 5 |  |
| WCCA_UL Note 8 |  |  |  |  |  | Inf |  |
| Semi-static channel access config period Note 4, 6 |  |  |  |  | ms | 2 |  |
| Propagation Condition |  |  |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters.NOTE 3: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic channel occupancy and semi-static channel occupancy configuration.NOTE 7: LCCA_DL and LCCA_UL are chosen such that preambleTransMax > 5 + LCCA_DL + LCCA_UL.NOTE 8: A window WCCA_DL=WCCA_UL=Inf is used to indicate that LCCA_DL and LCCA_UL are considered during the entire duration of a test run. |  |  |  |  |  |  |  |

###### A.11.2.2.2.4.2 Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

###### A.11.2.2.2.4.2.1 MsgA Transmission

To test the UE behavior specified in clause 6.2.2A.3.2.1, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0.

In addition, the System Simulator shall receive the MsgA PRACH on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belong to the PRACH occasions permitted by the restrictions given first by the msgA-SSB-SharedRO-MaskIndex if configured, or next by the ra-ssb-OccasionMaskIndex if configured.

The three requirements below are relevant for all cases of MsgA transmissions described within the clause A.11.2.2.2.4.2:

- The System Simulator shall implement the UL CCA model for the MsgA occasions (i.e. both MsgA PRACH and MsgA PUSCH occasions) where MsgA transmissions are expected. The System Simulator shall monitor the MsgA occasions to detect if the UE is transmitting MsgA. If a MsgA transmission is detected on MsgA occasions that are expected to have UL CCA failure, the test is considered as failed.

- In case of CCA DL failure, the test equipment should verify that the UE does not transmit MsgA for semi-static channel access mode; for dynamic channel access mode it is assumed that MsgA occasions are always scheduled within a UE-initiated COT.

- The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated PRACH transmission power in case of UL CCA failure.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be $ 0.6+3\left ( \mu  +2\right ) $ dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where $\mu  $ indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.11.2.2.2.4.2.2 MsgB Reception

To test the UE behavior specified in clause 6.2.2A.3.2.2 the System Simulator shall transmit a MsgB containing a fallbackRAR containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 containing the payload of MsgA PUSCH if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 is detected on a grant expected to have UL CCA failure, the test is considered as failed. The UE shall monitor contention resolution as described in clause 8.2A in TS 38.213 [3].

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB’s contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

The system simulator shall implement the UL CCA model of A.3.26.2 for the MsgA occasions where MsgA System Simulator transmissions are expected. The System Simulator shall monitor the MsgA occasions to detect if the UE is transmitting MsgA. If a MsgA transmission is detected on a MsgA occasion that is expected to have UL CCA failure, the test is considered as failed.

In case of CCA DL failure, the test equipment should verify that the UE does not transmit MsgA for semi-static channel access mode.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated MsgA transmission power in case UL CCA failure.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be $ 0.6+3\left ( \mu  +2\right ) $ dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where $\mu  $ indicates the MsgA PUSCH numerology. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA and msg3 transmissions shall be within the accuracy specified in clause 7.1.2.

###### A.11.2.2.2.4.2.3 No MsgB Reception

To test the UE behavior specified in clause 6.2.2A.3.2.3 the System Simulator shall transmit a MsgB containing a successRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA transmission power when the backoff time expires if no MsgB is received within the MsgB Response window.

The System Simulator shall implement the UL CCA model of A.3.26.2 for the MsgA occasions where MsgA transmissions are expected. The System Simulator shall monitor the MsgA occasions to detect if the UE is transmitting MsgA. If a MsgA transmission is detected on a MsgA occasion that is expected to have UL CCA failure, the test is considered as failed.

In case of CCA DL failure, the test equipment should verify that the UE does not transmit MsgA for semi-static channel access mode.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated MsgA transmission power in case UL CCA failure.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be $ 0.6+3\left ( \mu  +2\right ) $ dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where $\mu  $ indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

#### A.11.2.2.3 RRC connection release with redirection

##### A.11.2.2.3.1 Redirection from NR FR1 carrier under CCA to NR FR1 carrier under CCA

A.11.2.2.3.1.1 Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR FR1 carrier under CCA to NR FR1 carrier under CCA specified in clause 6.2.3.2.3.

A.11.2.2.3.1.2 Test Parameters

Supported test configurations are shown in table A.11.2.2.3.1.2-1. The time delay is tested by using the parameters in table A.11.2.2.3.1.2-2, and A.11.2.2.3.1.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.11.2.2.3.1.2-1: Redirection from NR to NR test configurations

| Config | Description |
| --- | --- |
| 1 | Source cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

Table A.11.2.2.3.1.2-2: General test parameters for Redirection from NR to NR test case

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 | On the carrier under CCA |
|  | Neighbouring cell |  | Cell 2 | On the carrier under CCA |
| Final condition | Active cell |  | Cell 2 | On the carrier under CCA |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| DL CCA model | Dynamic channel accessNote 1, 3 |  | As specified in clause A.3.26.2.1 |  |
|  | Semi-static channel access Note 2, 3 |  |  |  |
| UL CCA model | Dynamic channel access Note 1, 3 |  | As specified in clause A.3.26.2.2 |  |
|  | Semi-static channel access Note 2,3 |  |  |  |
| T1 |  | s | 5 |  |
| T2 |  | s | ≥ Tconnection_release_redirect_NR_CCA | Tconnection_release_redirect_NR_CCA is defined in clause 6.2.3.2.3 |
| NOTE 1: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 2: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.11.2.2.3.1.2-3: Cell specific test parameters for Redirection from NR to NR test case

| Parameter |  |  | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | 1 |  | 2 |  |
| PCCA_DL for dynamic channel access Note 4,6 |  |  | - | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| PCCA_DL for semi-static channel access Note 5,6 |  |  | - | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
| PCCA_UL for dynamic channel access Note 4,6 |  |  | - | 1 |  | 1 |  |
| PCCA_UL for semi-static channel access Note 5,6 |  |  | - | 1 |  | 1 |  |
| LCCA_DL Note 7 |  |  |  | N/A |  | 8 |  |
| WCCA_DL Note 7 |  |  | ms | N/A |  | Tidentify-NR_CCA |  |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  | Config 1 |  | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  | Config 1 |  | 40: NPRB,c = 106 |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference |  | Config 1 |  | SR.1.1 CCA |  |  |  |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA |  |  |  |
| Dedicated CORESET RMC configuration |  | Config 1 |  | CCR.1.1 CCA |  |  |  |
| TRS configuration |  | Config 1 |  | TRS.1.2 TDD |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |
| DBT configuration |  |  |  | DBT.1 |  |  |  |
| SSB configuration for semi-static channel access Note 4, 6 |  | Config 1 |  | SSB.1 CCA |  |  |  |
| SSB configuration for dynamic channel access Note 5, 6 |  | Config 1 |  | SSB.2 CCA |  |  |  |
| ssb-PositionQCL |  | Config 1 |  | [1] |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 | kHz | 30 kHz |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1 | kHz | 30 kHz |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 under CCA |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | -98 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 |  | dBm/SCS | -95 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 4 | 4 | -infinity | 4 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4 | 4 | -infinity | 4 |
| IoNote3 | Config 1 |  | dBm/38.16 MHz | -58.49 | -58.49 | -63.94 | -58.49 |
| Propagation condition |  |  | - | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 6: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only.NOTE 7: As defined in clause 6.2.3.2.3 for Trs ≤ 40 ms. |  |  |  |  |  |  |  |

A.11.2.2.3.1.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than Tconnection_release_redirect_NR_CCA ms from the beginning of time period T2, where Tconnection_release_redirect_NR_CCA is defined in clause 6.2.3.2.3.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE: The redirection delay can be expressed as:

Tconnection_release_redirect_NR_CCA = TRRC_procedure_delay + Tidentify-NR_CCA + TSI-NR_CCA + TRACH_CCA,

where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR_CCA = MAX (680 ms, (L1+11)  20 ms) in the test.

TSI-NR =  1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH_CCA is the delay uncertainty in acquiring the first available PRACH occasion in the target NR cell.

L1 is the number of SMTC occasions not available at the UE due to DL CCA failures. The test equipment ensure that number of L1 in target cell does not exceed L1,max using the configured LCCA_DL as in clause A.3.26.2.1;

##### A.11.2.2.3.2 Redirection from NR FR1 carrier without CCA to NR FR1 carrier with CCA

A.11.2.2.3.2.1 Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR FR1 carrier without CCA to NR FR1 carrier with CCA specified in clause 6.2.3.2.3.

A.11.2.2.3.2.2 Test Parameters

Supported test configurations are shown in table A.11.2.2.3.2.2-1. The time delay is tested by using the parameters in table A.11.2.2.3.2.2-2, and A.11.2.2.3.2.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.11.2.2.3.2.2-1: Redirection from NR to NR test configurations

| Configuration | Source cell without CCA | Target cell with CCA |
| --- | --- | --- |
| 1 | 15 kHz SSB SCS, 10 MHz bandwidth, FDD | 30 kHz SSB SCS, 40 MHz bandwidth, TDD |
| 2 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD | 30 kHz SSB SCS, 40 MHz bandwidth, TDD |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD | 30 kHz SSB SCS, 40 MHz bandwidth, TDD |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |  |

Table A.11.2.2.3.2.2-2: General test parameters for Redirection from NR to NR test case

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 | On the carrier without CCA |
|  | Neighbouring cell |  | Cell 2 | On the carrier under CCA |
| Final condition | Active cell |  | Cell 2 | On the carrier under CCA |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| DL CCA model | Dynamic channel accessNote 1, 3 |  | As specified in clause A.3.26.2.1 |  |
|  | Semi-static channel access Note 2, 3 |  |  |  |
| UL CCA model | Dynamic channel access Note 1, 3 |  | As specified in clause A.3.26.2.2 |  |
|  | Semi-static channel access Note 2,3 |  |  |  |
| T1 |  | s | 5 |  |
| T2 |  | s | ≥ Tconnection_release_redirect_NR_CCA | Tconnection_release_redirect_NR_CCA is defined in clause 6.2.3.2.3 |
| NOTE 1: For a UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 2: For a UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.11.2.2.3.2.2-3: Cell specific test parameters for Redirection from NR to NR test case

| Parameter |  |  | Unit | Cell 1 |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 |  | T2 |
| NR RF Channel Number |  |  |  | 1 |  | 2 |  |  |
| PCCA_DL for dynamic channel access Note 4,6 |  |  |  | N/A |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| PCCA_DL for semi-static channel access Note 5,6 |  |  |  | N/A |  | PCCA_DL=0.9375 | PCCA_DL=0.9375 |  |
| PCCA_UL for dynamic channel access Note 4,6 |  |  |  | N/A |  | 1 | 1 |  |
| PCCA_UL for semi-static channel access Note 5,6 |  |  |  | N/A |  | 1 | 1 |  |
| LCCA_DL Note 7 |  |  |  | N/A |  | 8 |  |  |
| WCCA_DL Note 7 |  |  | ms | N/A |  | Tidentify-NR_CCA |  |  |
| Duplex mode |  | Config 1 |  | FDD |  | TDD |  |  |
|  |  | Config 2,3 |  | TDD |  |  |  |  |
| TDD configuration |  | Config 1 |  | Not Applicable |  | TDDConf.1.1 CCA |  |  |
|  |  | Config 2 |  | TDDConf.1.1 |  | TDDConf.1.1 CCA |  |  |
|  |  | Config 3 |  | TDDConf.2.1 |  | TDDConf.1.1 CCA |  |  |
| BWchannel |  | Config 1 | MHz | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  |  |
|  |  | Config 2 |  | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  |  |
|  |  | Config 3 |  | 40: NPRB,c = 106 |  |  |  |  |
| BWP BW |  | Config 1 | MHz | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  |  |
|  |  | Config 2 |  | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  |  |
|  |  | Config 3 |  | 40: NPRB,c = 106 |  |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 FDD |  | SR.1.1 CCA |  |  |
|  |  | Config 2 |  | SR.1.1 TDD |  | SR.1.1 CCA |  |  |
|  |  | Config 3 |  | SR2.1 TDD |  | SR.1.1 CCA |  |  |
| RMSI CORESET RMC configuration |  | Config 1 |  | CR.1.1 FDD |  | CR.1.1 CCA |  |  |
|  |  | Config 2 |  | CR.1.1 TDD |  | CR.1.1 CCA |  |  |
|  |  | Config 3 |  | CR.2.1 TDD |  | CR.1.1 CCA |  |  |
| Dedicated CORESET RMC configuration |  | Config 1 |  | CCR.1.1 FDD |  | CCR.1.1 CCA |  |  |
|  |  | Config 2 |  | CCR.1.1 TDD |  | CCR.1.1 CCA |  |  |
|  |  | Config 3 |  | CCR.2.1 TDD |  | CCR.1.1 CCA |  |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |  |
| SSB Configuration | Semi-static channel acces | Config 1,2 |  | SSB.1 FR1 |  | SSB.1 CCA |  |  |
|  | Dymamic channel acces | Config 3 |  | SSB.2 FR1 |  | SSB.2 CCA |  |  |
|  | Semi-static channel acces | Config 1,2 |  | SSB.1 FR1 |  | SSB.1 CCA |  |  |
|  | Dymamic channel acces | Config 3 |  | SSB.2 FR1 |  | SSB.2 CCA |  |  |
| SMTC configuration |  | Config 1,2 |  | SMTC.1 FR1 |  | SMTC.2 FR1 |  |  |
|  |  | Config 3 |  | SMTC.2 FR1 |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 | kHz | 15 kHz |  | 30 kHz |  |  |
|  |  | Config 3 |  | 30 kHz |  |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1,2 | kHz | 15 kHz |  | 30 kHz |  |  |
|  |  | Config 3 |  | 30 kHz |  |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 under CCA in table A.3.8A.2.1-1 |  |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | -98 |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | Config 1,2 | dBm/SCS | -98 |  | -95 |  |  |
|  |  | Config 3 |  | -95 |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 4 | 4 | -infinity |  | 4 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4 | 4 | -infinity |  | 4 |
| IoNote3 |  | Config 1,2 | dBm/9.36 MHz | -64.59 | -64.59 | N/A |  | N/A |
|  |  | Config 3 | dBm/38.16 MHz | -58.49 | -58.49 | -63.94 |  | -58.49 |
| Propagation condition |  |  | - | AWGN |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 6: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only.NOTE 7: As defined in clause 6.2.3.2.3 for Trs ≤ 40 ms. |  |  |  |  |  |  |  |  |

A.11.2.2.3.2.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than Tconnection_release_redirect_NR_CCA ms from the beginning of time period T2, where Tconnection_release_redirect_NR_CCA is defined in clause 6.2.3.2.3.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE: The redirection delay can be expressed as:

Tconnection_release_redirect_NR_CCA = TRRC_procedure_delay + Tidentify-NR_CCA + TSI-NR_CCA + TRACH_CCA,

where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR_CCA = MAX (680 ms, (L1+11)  20 ms) in the test.

TSI-NR_CCA = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH_CCA is the delay uncertainty in acquiring the first available PRACH occasion in the target NR cell. TRACH_CCA = (1+L2)´TSSB,RO + 10 ms; where TSSB,RO = 10 ms for FR1 PRACH configuration 1.

L1 is the number of SMTC occasions not available at the UE due to DL CCA failures. The test equipment shall ensure that L1 does not exceed L1,max. In the test L1,max= LCCA_DL which is defined in clause A.3.26.2.1.

L2 is the consecutive number of SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failures. L2 = 0 in the test.


The total delay, Tconnection_release_redirect_NR_CCA, shall be less than 1410 + MAX (680, (L1+11)´20) ms.

## A.11.3 Timing

### A.11.3.1 UE transmit timing

#### A.11.3.1.1 UE Transmit Timing Test with PCell under DL CCA

##### A.11.3.1.1.1 Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeb when PCell is subject to DL CCA and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1.2.

Supported test configurations are shown in table 11.3.1.1.1-1

Table A.11.3.1.1.1-1: Supported test configuration for UE transmit timing test

| Configuration | Description |
| --- | --- |
| 1 | NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |

For this test a single NR cell is used. Table A.11.3.1.1.1-2 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.11.3.1.1.1-3.

Table A.11.3.1.1.1-2: Cell Specific Test Parameters for UE transmit timing test

| Parameter |  | Unit | Configuration | Test1 | Test2 |
| --- | --- | --- | --- | --- | --- |
| SSB ARFCN |  |  | 1 | 1 | 1 |
| TDD configuration |  |  | 1 | TDDConf.1.1 CCA |  |
| BWchannel |  | MHz | 1 | 40: NPRB,c = 106 |  |
| Initial BWP Configuration |  |  | 1 | DLBWP.0.1ULBWP.0.1 |  |
| Dedicated BWP Configuration |  |  | 1 | DLBWP.1.1ULBWP.1.1 |  |
| DRX Cycle |  | ms | 1 | N/A | DRX.8Note5 |
| DL CCA model |  |  | 1 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | 1 | As specified in clause A.3.26.2.2 |  |
| PDSCH Reference measurement channel |  |  | 1 | SR.1.1 CCA |  |
| RMSI CORESET Reference Channel |  |  | 1 | CR.1.1 CCA |  |
| Dedicated CORESET Reference Channel |  |  | 1 | CCR.1.1 CCA |  |
| OCNG Patterns |  |  | 1 | OP.1 |  |
| SSB configuration | Semi- static channel acces |  | 1 | SSB.1 CCA |  |
|  | Dymamic channel acces |  | 1 | SSB.2 CCA |  |
| SMTC Configuration |  |  | 1 | SMTC.1 FR1 |  |
| TRS configuration |  |  | 1 | TRS.1.2 TDD |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  |  | 1 | 0.9375 | 0.9375 |
| DL CCA model probability for dynamic static channel access (PCCA_DL_1) |  |  | 1 | 0.75 | 0.75 |
| DL CCA model probability for dynamic static channel access (PCCA_DL_2) |  |  | 1 | 0.75 | 0.75 |
| UL CCA probability (PCCA_UL) |  |  | 1 | 1 | 1 |
| EPRE ratio of PSS to SSS |  | dB | 1 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/30 KHz | 1 | -95 | -95 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | 1 | 3 | 3 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | 1 | 3 | 3 |
| SS-RSRPNote3 |  | dBm/30 kHz | 1 | -92 | -92 |
| IoNote3 |  | dBm/38.1 MHz | 1 | -59.2 | -59.2 |
| Propagation condition |  |  | 1 | AWGN |  |
| SRS Config |  |  | 1 | SRSConf.1Note6 | SRSConf.2Note6 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: DRX related parameters are given in table A.3.3.8-1NOTE 6: SRS configs are given in table A.11.3.1.1.1-3NOTE 7: Parameters PCCA_DL, PCCA_DL_1, PCCA_DL_2 and PCCA_UL are defined in clause A.3.26.2.NOTE 8: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |

Table A.11.3.1.1.1-3: SRS Configuration for UE transmit timing test

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
|  | resourceMapping startPosition | 0 | 0 |  |
|  | resourceMapping nrofSymbols | n1 | n1 |  |
|  | resourceMappingrepetitionFactor | n1 | n1 |  |
|  | freqDomainPosition | 0 | 0 |  |
|  | freqDomainShift | 0 | 0 |  |
|  | freqHopping c-SRS | 14 for test configuration 1,225 for test configuration 3 | 25 | Matches NPRB,c |
|  | freqHopping b-SRS | 0 | 0 |  |
|  | freqHopping b-hop | 0 | 0 |  |
|  | groupOrSequenceHopping | Neither | Neither |  |
|  | resourceType | Periodic | Periodic |  |
|  | periodicityAndOffset-p | sl1, 0 | sl640, 0 | Offset to align with DRX periodicity |
|  | sequenceId | 0 | 0 | Any 10 bit number |

##### A.11.3.1.1.2 Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1) Setup NR PCell according to parameters given in table A.11.3.1.1.1-1.

2) After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB.

a. The NTA offset value (in Tc units) is 25600

b. The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3) The test system shall adjust the timing of the DL path by values given in table A.11.3.1.1.2-1

Table A.11.3.1.1.2-1: Adjustment Value for DL Timing

| SCS of SSB signals (KHz) | Adjustment Value |  |
| --- | --- | --- |
|  | Test1 | Test2 |
| 30 | +32*64Tc | +16*64Tc |

4) The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 Table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first detected path (in time) of DL SSB.  Skip this step for test 2 with DRX configured.

5) The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment

### A.11.3.2 UE timing advance

#### A.11.3.2.1 UE Timing Advance Adjustment Accuracy with PCell under DL CCA

##### A.11.3.2.1.1 Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3.

##### A.11.3.2.1.2 Test Parameters

Supported test configurations are shown in table A.11.3.2.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.11.3.2.1.2-2, A.11.3.2.1.2-3 and A.11.3.2.1.2-4.

In all test cases, single cell is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.11.3.2.1.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.11.3.2.1.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause7.3.2.1, the UE adjusts its uplink timing at slot n+k for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.11.3.2.1.2-1: Supported test configuration for timing advance test

| Config | Description |
| --- | --- |
| 1 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE supporting SA operation only on NR band(s) with shared spectrum access is required to be tested |  |

Table A.11.3.2.1.2-2: General test parameters for timing advance test

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| RF channel number |  | 1 |  |
| Initial DL BWP |  | DLBWP.0.1 | As specified in table A.3.9.2.1-1 |
| Dedicated DL BWP |  | DLBWP.1.1 | As specified in table A.3.9.2.2-1 |
| Initial UL BWP |  | ULBWP.0.1 | As specified in table A.3.9.3.1-1 |
| Dedicated UL BWP |  | ULBWP.1.1 | As specified in table A.3.9.3.2-1 |
| Timing Advance Command (TA) value during T1 |  | 31 | NTA_new = NTA_old  for the purpose of establishing a reference value from which the timing advance adjustment accuracy can be measured during T2 |
| Timing Advance Command (TA) value during T2 |  | 39 | For 30 kHz SCS NTA_new = NTA_old  + 4096*Tc (based on equation in clause 4.2 of TS 38.213 [3]) |
| T1 | s | 5 |  |
| T2 | s | 5 |  |

Table A.11.3.2.1.2-3: Cell specific test parameters for timing advance test

| Parameter |  |  | Unit | Test1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |
| BWchannel |  | Config 1 | MHz | 40: NPRB,c = 106 |  |
| BWP BW |  | Config 1 | MHz | 40: NPRB,c = 106 |  |
| DRX Cycle |  | Config 1 | ms | Not Applicable |  |
| DL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.2 |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 CCA |  |
| CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA |  |
| TRS configuration |  | Config 1 |  | TRS.1.2 TDD |  |
| OCNG Patterns |  | Config 1 |  | OCNG pattern 1 |  |
| SMTC configuration |  | Config 1 |  | SMTC.1 FR1 |  |
| SSB configuration | Semi- static channel acces | Config 1 |  | SSB.1 CCA |  |
|  | Dymamic channel acces | Config 1 |  | SSB.2 CCA |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | Config 1 |  | 1 |  |
| DL CCA model probability for dynamic static channel access (PCCA_DL_1) |  | Config 1 |  | 1 |  |
| DL CCA model probability for dynamic static channel access (PCCA_DL_2) |  | Config 1 |  | 1 |  |
| UL CCA probability PCCA |  | Config 1 |  | 1 |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | Config 1 | dBm/30 kHz | -95 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 3 |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 |  |
| IoNote3 |  | Config 1 | dBm/38.16 MHz | -62.58 |  |
| Propagation condition |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Parameters PCCA_DL, PCCA_DL_1, PCCA_DL_2 and PCCA_UL are defined in clause A.3.26.2.NOTE 5: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |

Table A.11.3.2.1.2-4: Sounding Reference Symbol Configuration for Timing Advance Accuracy Test

| Field | Value | Comment |
| --- | --- | --- |
| c-SRS | 24 | Frequency hopping is disabled |
| b-SRS | 0 |  |
| b-hop | 0 |  |
| freqDomainPosition | 0 | Frequency domain position of SRS |
| freqDomainShift | 0 |  |
| groupOrSequenceHopping | neither | No group or sequence hopping |
| SRS-PeriodicityAndOffset | sl5=4 for SCS 30 kHz | Once every 5 slots |
| pathlossReferenceRS | ssb-Index=0 | SSB #0 is used for SRS path loss estimation |
| usage | Codebook | Codebook based UL transmission |
| startPosition | 0 | resourceMapping setting: SRS on last symbol of slot, and 1 symbols for SRS without repetition. |
| nrofSymbols | n1 |  |
| repetitionFactor | n1 |  |
| combOffset-n2 | 0 | transmissionComb setting |
| cyclicShift-n2 | 0 |  |
| nrofSRS-Ports | port1 | Number of antenna ports used for SRS transmission |
| NOTE: For further information see clause 6.3.2 in TS 38.331 [2]. |  |  |

##### A.11.3.2.1.3 Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k=5.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.11.4 Signalling characteristics

### A.11.4.1 Radio link monitoring

#### A.11.4.1.1 Introduction

In the test cases specified in clause A.11.4.1, any uplink signal transmitted by the UE is used for detecting the in-/out-of-sync state of the UE. In terms of measurement, the uplink signal is verified based on the UE output power:

- UE output power higher than Transmit OFF power -50 dBm (as defined in TS 38.101-1 [18]) means uplink signal.

- UE output power equal to or less than Transmit OFF power -50 dBm (as defined in TS 38.101-1 [18]) means no uplink signal.

For intra-band contiguous carrier aggregation, transmit OFF power is measured as the mean power per component carrier.

For UE with multiple transmit antennas, transmit OFF power is measured as the mean power at each transmit connector.

#### A.11.4.1.2 Radio link monitoring out-of-sync test for PCell configured with SSB-based RLM RS in non-DRX mode

##### A.11.4.1.2.1 Test purpose and environment

The purpose of this test is to verify that the UE properly detects the out-of-sync and in-sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR1 PCell radio link monitoring requirements in clause 8.1A.

In the test, UE is configured to perform RLM based on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.11.4.1.2.1-1. The test parameters are given in tables A.11.4.1.2.1-2, A.11.4.1.2.1-3, and A.11.4.1.2.1-4 below. There is one cell (Cell 1), which is the active NR cell in FR1, in the test. Cell 1 operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model.

The test consists of three successive time periods, with time duration of T1, T2 and T3, respectively. Figure A.11.4.1.2.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE transmits according to UL CCA model. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in the test.

Table A.11.4.1.2.1-1: Supported test configurations.

| Configuration | Description |
| --- | --- |
| 1 | TDD, SSB SCS 30 kHz, data SCS 30 kHz, bandwidth 40 MHz |

Table A.11.4.1.2.1-2: General test parameters for PCell out-of-sync testing in non-DRX mode.

| Parameter |  |  | Unit | Value |
| --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |
| Active PCell |  |  |  | Cell 1 |
| RF Channel Number |  |  |  | 1 |
| DL CCA model |  |  |  | As specified in clause A.3.26.2.1 |
| UL CCA model |  |  |  | As specified in clause A.3.26.2.2 |
| Duplex mode |  | Config 1 |  | TDD |
| BWchannel |  | Config 1 | MHz | 40: NPRB,c = 106 |
| DL initial BWP configuration |  | Config 1 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  | Config 1 |  | DLBWP.1.1 |
| UL initial BWP configuration |  | Config 1 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  | Config 1 |  | ULBWP.1.1 |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |
| CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA |
| SSB configuration for semi-static channel accessNote 3, 5 |  | Config 1 |  | SSB.1 CCA |
| SSB configuration for dynamic channel accessNote 4, 5 |  | Config 1 |  | SSB.2 CCA |
| DBT window configuration |  | Config 1 |  | DBT.1 |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 |  | 30 kHz |
| PRACH Configuration |  | Config 1 |  | FR1 PRACH configuration 1 under CCA |
| SSB index assigned as RLM RS |  |  |  | 0 |
| OCNG parameters |  |  |  | OP.1 |
| CP length |  |  |  | Normal |
| Correlation Matrix and Antenna Configuration |  |  |  | 2x2 Low |
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
| CSI-RS configuration for CSI reporting |  | Config 1 |  | CSI-RS.2.1 TDD |
| CSI-RS for tracking |  | Config 1 |  | TRS.1.2 TDD |
| T1 |  |  | s | 0.2 |
| T2 |  |  | s | 1.04 |
| T3 |  |  | s | 1.04 |
| D1 |  |  | s | 1 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5:  For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 6: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.11.4.1.2.1-3: Cell-specific test parameters for PCell out-of-sync testing in non-DRX mode.

| Parameter |  |  | Unit | Test 1 |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 |
| DL CCA probability PCCA_DL |  | Note 6,8 |  | PCCA_DL=0.9375 |  |  |
|  |  | Note 7,8 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |
| UL CCA probability PCCA_UL |  |  |  | 1 |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  | dB | 4 |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | dB | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  | dB | 0 |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  | dB |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  | dB |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  | dB |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  | dB |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  | dB |  |  |  |
| SNRNote 3,4 on RLM-RS | Config 1 |  | dB | 1 | -7 | -15 |
| SNR on other channels and signals | Config 1 |  | dB | 1 |  |  |
| ![](media_svg/image8.svg) [公式≈: ^{N}oc] | Config 1 |  | dBm/SCS | -95 |  |  |
| Propagation condition |  |  |  | TDL-C 300 ns 100 Hz |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in slots with RMC burst transmission and is not transmitted during muted slots or during DBT windows.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the transmitted SSS REs during DBT windows.NOTE 4: The SNR in time periods T1, T2 and T3 is denoted as SNR1, SNR2 and SNR3, respectively, in figure A.10.4.1.2.1-1.NOTE 5: The SNR values are specified for testing a UE which supports 2 RX on at least one band. For testing of a UE which supports 4 RX on all bands, the SNR during T3 is A.3.6.NOTE 6:   For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7:   For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8:   For UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |

Table A.11.4.1.2.1-4: Measurement gap configuration for PCell out-of-sync testing in non-DRX mode.

| Field | Test 1 |  |
| --- | --- | --- |
|  | Value |  |
| gapOffset | 0 |  |
| NOTE: Ensure that RLM RS is partially overlapped with measurement gap0 |  |  |

Figure A.11.4.1.2.1-1: SNR variation for out-of-sync testing.

##### A.11.4.1.2.2 Test requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

- During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

- The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.11.4.1.3 Radio link monitoring in-sync test for PCell configured with SSB-based RLM RS in non-DRX mode

##### A.11.4.1.3.1 Test purpose and environment

The purpose of this test is to verify that the UE properly detects the out-of-sync and in-sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR1 PCell radio link monitoring requirements in clause 8.1A.

In the test, UE is configured to perform RLM based on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.11.4.1.3.1-1. The test parameters are given in tables A.11.4.1.3.1-2, and A.11.4.1.3.1-3 below. There is one cell (Cell 1), which is the active NR cell in FR1, in the test. Cell 1 operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model.

The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5, respectively. Figure A.11.4.1.3.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE transmits according to UL CCA model.

Table A.11.4.1.3.1-1: Supported test configurations.

| Configuration | Description |
| --- | --- |
| 1 | NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |

Table A.11.4.1.3.1-2: General test parameters for PCell in-sync testing in non-DRX mode.

| Parameter |  |  | Unit | Value |
| --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |
| Active PCell |  |  |  | Cell 1 |
| RF Channel Number |  |  |  | 1 |
| DL CCA model |  |  |  | As specified in clause A.3.26.2.1 |
| UL CCA model |  |  |  | As specified in clause A.3.26.2.2 |
| Duplex mode |  | Config 1 |  | TDD |
| BWchannel |  | Config 1 | MHz | 40: NPRB,c = 106 |
| DL initial BWP configuration |  | Config 1 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  | Config 1 |  | DLBWP.1.1 |
| UL initial BWP configuration |  | Config 1 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  | Config 1 |  | ULBWP.1.1 |
| TDD Configuration |  | Config 1 |  | TDDConf.1.1 CCA |
| CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA |
| SSB configuration for semi-static channel accessNote 3, 5 |  | Config 1 |  | SSB.1 CCA |
| SSB configuration for dynamic channel accessNote 4,5 |  | Config 1 |  | SSB.2 CCA |
| DBT window configuration |  | Config 1 |  | DBT.1 |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 |  | 30 kHz |
| PRACH Configuration |  | Config 1 |  | FR1 PRACH configuration 1 under CCA |
| SSB index assigned as RLM RS |  |  |  | 0 |
| OCNG parameters |  |  |  | OP.1 |
| CP length |  |  |  | Normal |
| Correlation Matrix and Antenna Configuration |  |  |  | 2x2 Low |
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
| Gap pattern ID |  |  |  | N/A |
| Layer 3 filtering |  |  |  | Enabled |
| T310 timer |  |  | ms | 2000 |
| T311 timer |  |  | ms | 1000 |
| N310 |  |  |  | 1 |
| N311 |  |  |  | 1 |
| CSI-RS configuration for CSI reporting | Config 1 |  |  | CSI-RS.2.1 TDD |
| CSI-RS for tracking | Config 1 |  |  | TRS.1.2 TDD |
| T1 |  |  | s | 0.2 |
| T2 |  |  | s | 0.2 |
| T3 |  |  | s | 0.52 |
| T4 |  |  | s | 0.2 |
| T5 |  |  | s | 2.04 |
| D1 |  |  | s | 2 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts.NOTE 4:  For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5:  For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 6:  For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.11.4.1.3.1-3: Cell-specific test parameters for PCell in-sync testing in non-DRX mode.

| Parameter |  |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 | T4 | T5 |
| DL CCA probability PCCA_DL |  | Note 6,8 |  | PCCA_DL=0.9375 |  |  |  |  |
|  |  | Note 7,8 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |  |  |
| UL CCA probability PCCA_UL |  |  |  | 1 |  |  |  |  |
| LCCA_DL |  |  |  | 7 |  |  |  |  |
| WCCA_DL |  |  | ms | TEvaluate_in_SSB,CCANOTE 9 |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  | dB | 4 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | dB | 0 |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  | dB | 0 |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  | dB |  |  |  |  |  |
| SNR on RLM-RS | Config 1 |  | dB | 1 | -7 | -15 | -4.5 | 1 |
| SNR on other channels and signals | Config 1 |  | dB | 1 |  |  |  |  |
| ![](media_svg/image8.svg) [公式≈: ^{N}oc] | Config 1 |  | dBm/SCS | -95 |  |  |  |  |
| Propagation condition |  |  |  | TDL-C 300 ns 100 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in slots with RMC burst transmission and is not transmitted during muted slots or during DBT windows.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the transmitted SSS REs during DBT windows.NOTE 4: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2, SNR3, SNR4 and SNR5 respectively in figure A.11.4.1.3.1-1.NOTE 5: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4 RX on all bands, the SNR during T3 and T4 is modified as specified in clause A.3.6.NOTE 6:  For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7:  For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8:  For UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only.NOTE 9: As defined in table 8.1A.2.2-1. |  |  |  |  |  |  |  |  |

Figure A.11.4.1.3.1-1: SNR variation for in-sync testing.

##### A.11.4.1.3.2 Test requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

- During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.11.4.1.4 Void

##### A.11.4.1.4.1 Void

##### A.11.4.1.4.2 Void

#### A.11.4.1.5 Void

##### A.11.4.1.5.1 Void

##### A.11.4.1.5.2 Void

### A.11.4.2 Void

### A.11.4.3 SCell activation and deactivation delay

#### A.11.4.3.1 SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 160 ms SCell measurement cycle

##### A.11.4.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for SCell, with PCell and SCell both under CCA, are within the requirements stated in clause 8.3A, when the SCell is known by the UE at the time of activation and the configured SCell measurement cycle is 160 ms.

The supported test configurations are shown in table A.11.4.3.1.1-1.

The test parameters are given in table A.11.4.3.1.1-2 and cell-specific parameters in table A.11.4.3.1.1-3 below. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two carriers, each with one cell: Cell 1 (PCell) on radio channel 1 (PCC) in NR with CCA, and Cell 2 (SCell) on radio channel 2 (SCC) in NR with CCA. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2, as the UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. At the end of T1, the test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2. The UE shall be able to report a valid CSI in PCell for the activated SCell at latest in slot m + (THARQ+Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, as defined in clause 8.3A.2. The UE shall start reporting CSI in PCell in first available uplink resource for CSI reporting after at least one CSI-RS transmission occasion for channel measurement and reporting following slot m+ $\frac {T_{HARQ}+3 ms}{NR slot length}$ and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption shall fall within the time window specified in clause 8.3.2.

The point in time at which the MAC message is received by at the UE antenna connector, in a slot # denoted n, defines the start of time period T3. The UE shall complete the activation at latest in slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$. Any PCell interruption shall fall within the time window specified in clause 8.3A.3.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received, while taking into account CCA failures on SCC.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.11.4.3.1.1-1: Supported test configurations for SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 160 ms SCell measurement cycle

| Configuration | Description |
| --- | --- |
| 1 | With CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode;With CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

Table A.11.4.3.1.1-2: General test parameters for known SCell activation with PCell and SCell under CCA, 160 ms SCell measurement cycle

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| RF Channel Number |  | 1,2 | Two radio channels (1, 2) are used for this test |
| Active PCell |  | Cell 1 | Primary cell on NR RF channel number 1. |
| Configured deactivated SCell |  | Cell 2 | Configured deactivated secondary cell on NR RF channel number 2 |
| CP length |  | Normal |  |
| DRX |  | OFF | Continuous monitoring of primary cell |
| CQI/PMI periodicity and offset configuration index |  | 0 | CQI reporting for SCell every second subframe |
| SCell measurement cycle (measCycleSCell) | ms | 160 |  |
| Cell 2 timing offset to Cell 1 | s | 0 |  |
| Time alignment error between Cell 2 and Cell 1 | s | TAE as specified in TS 38.104 [13] clause 6.5.3.1. | The value of time alignment error depends upon the type of carrier aggregation. |
| T1 | s | 7 | During this time the PCell shall be known and the SCell configured and detected. |
| T2 | s | 1 | During this time the UE shall activate the SCell. |
| T3 | s | 1 | During this time the UE shall deactivate the SCell. |
| THARQ | ms | k1 $\times  $ NR slot length | k1 is a number of slots and is indicated by the PDSCH-to-HARQ-timing-indicator field in the DCI format, if present, or provided by dl-DataToUL-ACK, the value of k should be the minimum value defined in TS 38.213 [3] depends on UE’s capability |
| TCSI_Reporting | ms | $ 10+5\cdot  2^{µ_{DL}}$ | The delay (in ms) including uncertainty in acquiring the first available downlink CSI reference resource, UE processing time for CSI reporting (clause 5.2.2.5 in TS 38.214) and uncertainty in acquiring the first available CSI reporting resources as specified in TS 38.331[2]$µ_{DL}$ is the subcarrier spacing configuration for DL |

Table A.11.4.3.1.1-3: Cell specific test parameters for known SCell activation case with PCell and SCell under CCA, 160 ms SCell measurement cycle

| Parameter |  | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Duplex mode | Config 1 |  | TDD |  |  | TDD |  |  |
| TDD configuration | Config 1 |  | TDDConf.1.1 CCA |  |  | TDDConf.1.1 CCA |  |  |
| BWchannel | Config 1 | MHz | 40: NPRB,c = 106 |  |  | 40: NPRB,c = 106 |  |  |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |  | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |  | As specified in clause A.3.26.2.2 |  |  |
| DL CCA probability for semi-static channel accessNote5,7 | PCCA_DL |  | 0.9375 |  |  | 0.9375 |  |  |
| DL CCA probability for dynamic channel accessNote6,7 | PCCA_DL_1 |  | 0.75 |  |  | 0.75 |  |  |
|  | PCCA_DL_2 |  | 0.75 |  |  | 0.75 |  |  |
| UL CCA probability for semi-static channel access | PCCA_UL |  | 0.87 |  |  | 0.87 |  |  |
| UL CCA probability | PCCA_UL |  | 0.75 |  |  | 0.75 |  |  |
| LCCA_DL Note 8 |  |  | 2 |  |  | 2 |  |  |
| WCCA_DL Note 8 |  | ms | Tactivation_time_withCCA |  |  | Tactivation_time_withCCA |  |  |
| Initial downlink BWP configuration |  |  | DLBWP.0.2 |  |  | DLBWP.0.2 |  |  |
| Initial uplink BWP configuration |  |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Dedicated downlink BWP configuration |  |  | DLBWP.0.2 |  |  | DLBWP.0.2 |  |  |
| Dedicated uplink BWP configuration |  |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| TCI state |  |  | TCI.State.0 |  |  | TCI.State.0 |  |  |
| TRS Configuration | Config 1 |  | TRS.1.2 TDD |  |  | TRS.1.2 TDD |  |  |
| PDSCH Reference measurement channel | Config 1 |  | SR.1.1 CCA |  |  | SR.1.1 CCA |  |  |
| Dedicated CORESET parameters | Config 1 |  | CCR.1.3 CCA |  |  | SR.1.1 CCA |  |  |
| RMSI CORESET parameters | Config 1 |  | CR.1.1 CCA |  |  | SR.1.1 CCA |  |  |
| OCNG Patterns Note1 |  |  | OP.1 |  |  | OP.1 |  |  |
| SSB Configuration for semi-static channel accessNote5,7 | Config 1 |  | SSB.1 CCA |  |  | SSB.1 CCA |  |  |
| SSB Configuration for dynamic channel accessNote6,7 | Config 1 |  | SSB.2 CCA |  |  | SSB.2 CCA |  |  |
| SMTC configuration |  |  | SMTC.1 |  |  | SMTC.1 |  |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |  | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote1 |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRSNote1 |  |  |  |  |  |  |  |  |
| Noc Note2 | Config 1 | dBm/15 kHz | -104 |  |  | -104 |  |  |
| Noc Note2 | Config 1 | dBm/SCS | -101 |  |  | -101 |  |  |
| Ês/Iot |  | dB | 17 |  |  | 17 |  |  |
| Ês/Noc |  | dB | 17 |  |  | 17 |  |  |
| SS-RSRP Note3 | Config 1 | dBm/SCS | -84 |  |  | -84 |  |  |
| IoNote3 | Config 1 | dBm/38.16 MHz | -52.87 |  |  | -52.87 |  |  |
| Propagation condition |  | - | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that resources in the cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols in slots with downlink transmission bursts. OCNG is not transmitted during muted slots or during DBT windows.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T2.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations.NOTE 8: As specified in clause 8.3A for L1,max, L2,1,max, L2,2,max, L3,1,max, and L3,2,max |  |  |  |  |  |  |  |  |

##### A.11.4.3.1.2 Test Requirements

During T2, starting after at least one CSI-RS transmission occasion for channel measurement and reporting from the slot specified in clause 4.3 of TS 38.213 [3] and until the UE has completed the SCell activation, the UE shall report out of range if the UE has available uplink resources to report CQI for the SCell.

During T2, the UE shall send the first valid CSI report (non-zero CQI) for the SCell in first available uplink resource for CSI reporting no later than slot m + (THARQ+Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB + L1*Trs + 5 ms, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$, as defined in clause 8.3A.3.

During T2, interruption on PCell shall not occur outside slot m +1+$\frac {T_{HARQ}}{NR slot length}$  to slot m +1+$\frac {T_{HARQ}+3+T_{X}}{NR slot length}$ with TX = TFirstSSB.

During T3, interruption on PCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PCell shall not be more than specified for SA in clause 8.2.2.2.2.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

#### A.11.4.3.2 SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 640 ms SCell measurement cycle

##### A.11.4.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for SCell, with PCell and SCell under CCA, are within the requirements stated in clause 8.3A, when the SCell is known by the UE at the time of activation and the configured SCell measurement cycle is 640 ms.

The supported test configurations are same as in table A.11.4.3.1.1-1 above.

The test parameters are same as in table A.11.4.3.1.1-2 above, except for parameters listed below in table A.11.4.3.2.1-1. The cell-specific parameters are same as in table A.11.4.3.1.1-3 above.

The test execution is the same as described in clause A.11.4.3.1 above.

Table A.11.4.3.2.1-1: General test parameters for known SCell activation with PCell and SCell under CCA, 640 ms SCell measurement cycle

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| SCell measurement cycle (measCycleSCell) | ms | 640 |  |

##### A.11.4.3.2.2 Test Requirements

During T2, starting after at least one CSI-RS transmission occasion for channel measurement and reporting from the slot specified in clause 4.3 of TS 38.213 [3] and until the UE has completed the SCell activation, the UE shall report out of range if the UE has available uplink resources to report CQI for the SCell.

During T2, the UE shall send the first valid CSI report (non-zero CQI) for the SCell in first available uplink resource for CSI reporting no later than slot m + (THARQ+Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB_MAX + L2,1*TSMTC_MAX + (1 +L2,2)*Trs + 5 ms, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$, as defined in clause 8.3A.3.

During T2, interruption on PCell shall not occur outside slot m +1+$\frac {T_{HARQ}}{NR slot length}$  to slot m +1+$\frac {T_{HARQ}+3+T_{X}}{NR slot length}$ with TX = TFirstSSB_MAX + L2,1* TSMTC_MAX.

During T3, interruption on PCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PCell shall not be more than specified for SA in clause 8.2.2.2.2.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

#### A.11.4.3.3 SCell Activation and Deactivation of unknown SCell with PCell and SCell under CCA

##### A.11.4.3.3.1 Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for SCell, with PCell and SCell under CCA, are within the requirements stated in clause 8.3A, when the SCell is unknown to the UE at the time of activation.

The supported test configurations are same as in table A.11.4.3.1.1-1 above.

The test parameters are same as in table A.11.4.3.1.1-2 above, except for parameters listed below in table A.11.4.3.3.1-1. The cell-specific parameters are same as in table A.11.4.3.1.1-3 above.

The test execution is the same as described in clause A.11.4.3.1 above.

Table A.11.4.3.3.1-1: General test parameters for unknown SCell activation with PCell ans SCell under CCA

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| T1 | s | 0.1 | During this time period the PCell shall be known and the SCell configured, but not detected. |

##### A.11.4.3.3.2 Test Requirements

During T2, starting after at least one CSI-RS transmission occasion for channel measurement and reporting from the slot specified in clause 4.3 of TS 38.213 [3] and until the UE has completed the SCell activation, the UE shall report out of range if the UE has available uplink resources to report CQI for the SCell.

During T2, the UE shall send the first valid CSI report (non-zero CQI) for the SCell in first available uplink resource for CSI reporting no later than slot m + (THARQ+Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB_MAX + (1 + L3,1)*TSMTC_MAX + (2 + L3,2)*Trs + 5 ms, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$, as defined in clause 8.3A.3.

During T2, interruption on PCell shall not occur outside slot m +1+$\frac {T_{HARQ}}{NR slot length}$  to slot m +1+$\frac {T_{HARQ}+3+T_{X}}{NR slot length}$ with TX = TFirstSSB_MAX + L3,1* TSMTC_MAX.

During T3, interruption on PCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PCell shall not be more than specified for SA in clause 8.2.2.2.2.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

### A.11.4.4 Beam failure detection and link recovery procedures

#### A.11.4.4.1 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode

##### A.11.4.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5A.

The test parameters are given in tables A.11.4.4.1.1-1, A.11.4.4.1.1-2, A.11.4.4.1.1-3 and A.11.4.4.1.1-4 below. There is one cell, Cell 1 which is the active cell, in the test. Cell 1 operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.11.4.4.1.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.11.4.4.1.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 2 ms. The UE transmits the reporting according to UL CCA mode. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

Table A.11.4.4.1.1-1: Supported test configurations for FR1 PCell with CCA

| Configuration | Description |
| --- | --- |
| 1 | TDD duplex mode, 30 kHz SSB SCS, 40 MHz bandwidth |

Table A.11.4.4.1.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  |  | Unit | Value |  | Comment |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |  |  |
| Active PSCell |  |  |  | Cell 1 |  |  |
| RF Channel Number |  |  |  | 1 |  |  |
| DL CCA model |  |  |  | As specified in A.3.26.2.1 |  |  |
| UL CCA model |  |  |  | As specified in A.3.26.2.2 |  |  |
| Duplex mode |  | Config 1 |  | TDD |  |  |
| BWchannel |  | Config 1 | MHz | 40: NRB,c = 106 |  |  |
| DL initial BWP configuration |  | Config 1 |  | DLBWP.0.1 |  |  |
| DL dedicated BWP configuration |  | Config 1 |  | DLBWP.1.1 |  |  |
| UL initial BWP configuration |  | Config 1 |  | ULBWP.0.1 |  |  |
| UL dedicated BWP configuration |  | Config 1 |  | ULBWP.1.1 |  |  |
| TDD Configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |  |
| CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA |  |  |
| SSB Configuration |  | Config 1 |  | SSB.3 CCA for semi-static channel accessSSB.4 CCA for dynamic channel access |  |  |
| DBT Window Configuration |  | Config 1 |  | DBT.1 |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 |  | 30 KHz |  |  |
| PRACH Configuration |  | Config 1 |  | Table  A.3.8A.2.2-1 |  |  |
| SSB Index assigned as BFD RS (q0) |  |  |  | 0 |  |  |
| SSB Index assigned as CBD RS (q1) |  |  |  | 1 |  |  |
| OCNG parameters |  |  |  | OP.1 |  |  |
| CP length |  |  |  | Normal |  |  |
| Correlation Matrix and Antenna Configuration |  |  |  | 2x2 Low |  |  |
| Beam failure detection transmission parameters | DCI format |  |  | 1-0 |  |  |
|  | Number of Control OFDM symbols |  |  | 2 |  |  |
|  | Aggregation level |  | CCE | 8 |  |  |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 0 |  |  |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 0 |  |  |
|  | DMRS precoder granularity |  |  | REG bundle size |  |  |
|  | REG bundle size |  |  | 6 |  |  |
| DRX |  |  |  | OFF |  |  |
| Gap pattern ID |  |  |  | gp0 |  |  |
| gapOffset |  |  |  | 0 |  |  |
| rlmInSyncOutOfSyncThreshold |  |  |  | absent |  | When the field is absent, the UE applies the value 0. (Table 8.1.1-1). |
| rsrp-ThresholdSSB | Config 1 |  | dBm/SCS kHz | -95 |  | Threshold used for Qin_LR_SSB |
| powerControlOffsetSS |  |  |  | db0 |  | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  |  |  | n1 |  | see clause 5.17 of TS 38.321 [7] |
| beamFailureDetectionTimer |  |  |  | pbfd4 |  | see clause 5.17 of TS 38.321 [7] |
| CSI-RS configuration for CSI reporting | Config 1 |  |  | CSI-RS.2.1 TDD |  |  |
| CSI-RS for tracking | Config 1 |  |  | TRS.1.2 TDD |  |  |
| SSB Index assigned as RLM RS |  |  |  | 0, 1 |  |  |
| T310 Timer |  |  | ms | 1000 |  |  |
| N310 |  |  |  | 2 |  |  |
| T1 |  |  | s | 0.2 |  | During this time the the UE shall be fully synchronized to Cell 1 |
| T2 |  |  | s | 0.93 |  |  |
| T3 |  |  | s | 0.52 |  |  |
| T4 |  |  | s | 0 |  |  |
| T5 |  |  | s | 0.45 |  |  |
| D1 |  |  | s | 0.41 |  |  |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |  |

Table A.11.4.4.1.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 | T4 | T5 |
| DL CCA probability PCCA,DL |  | Note 10, 12 |  | 1.0 | 0.9375 | 0.9375 | 0.9375 | 0.9375 |
|  |  | Note 11, 12 |  | 1.0/1.0 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 |
| UL CCA probability PCCA,UL |  |  |  | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| LCCA_DL |  |  |  | N/A | 7 |  |  |  |
| WCCA_DL |  |  | ms | N/A | TEvaluate_CBD_SSB_CCA Note 13 |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  | dB | 0 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  | dB |  |  |  |  |  |
| SNR_SSB of set q0 | Config 1 |  | dB | 5 | -3 | -12 | -12 | -12 |
| SNR_SSB of set q1 | Config 1 |  | dB | -10 | -10 | 10 | 10 | 10 |
| SSB_RP of set q1 | Config 1 |  | dBm/SCS kHz | -105 | -105 | -85 | -85 | -85 |
| ![](media_svg/image8.svg) [公式≈: ^{N}oc] | Config 1 |  | dBm/15 KHz | -98 |  |  |  |  |
| Propagation condition |  |  |  | TDL-C 300 ns 100 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio the transmitted SSS REs during DBT window.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.4.5.5.1.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4RX on all bands, the SNR during T3 is modified as specified in clause A.3.6A.NOTE 10: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 11: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2.NOTE 12: For UE supporting both semi-static and dynamic cannel access, the UE can be tested under dynamic channel occupancy only.NOTE 13:  As defined in table 8.5A.5.2-1. |  |  |  |  |  |  |  |  |

![](media/C:\Users\w00527694\Pictures\图片28.png)

Figure A.11.4.4.1.1-1: SNR and L1-RSRP variation SSB for SSB-based beam failure detection and link recovery testing in non-DRX mode

##### A.11.4.4.1.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 410 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.11.4.4.2 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode

##### A.11.4.4.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5A.

The test parameters are given in tables A.11.4.4.2.1-1, A.11.4.4.2.1-2, and A.11.4.4.2.1-3 below. There is one cell, Cell 1 which is the active cell, in the test. Cell 1 operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.11.4.4.2.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.11.4.4.2.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 2 ms. The UE transmits the reporting according to UL CCA mode. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.11.4.4.2.1-1: Supported test configurations for FR1 PCell with CCA

| Configuration | Description |
| --- | --- |
| 1 | TDD duplex mode, 30 kHz SSB SCS, 40 MHz bandwidth |

Table A.11.4.4.2.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

| Parameter |  |  | Unit | Value |  | Comment |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |  |  |
| Active PSCell |  |  |  | Cell 1 |  |  |
| RF Channel Number |  |  |  | 1 |  |  |
| DL CCA model |  |  |  | As specifieed in A.3.26.2.1 |  |  |
| UL CCA model |  |  |  | As specified in A.3.26.2.2 |  |  |
| Duplex mode |  | Config 1 |  | TDD |  |  |
| BWchannel |  | Config 1 | MHz | 40: NRB,c = 106 |  |  |
| DL initial BWP configuration |  | Config 1 |  | DLBWP.0.1 |  |  |
| DL dedicated BWP configuration |  | Config 1 |  | DLBWP.1.1 |  |  |
| UL initial BWP configuration |  | Config 1 |  | ULBWP.0.1 |  |  |
| UL dedicated BWP configuration |  | Config 1 |  | ULBWP.1.1 |  |  |
| TDD Configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |  |
| CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA |  |  |
| SSB Configuration |  | Config 1 |  | SSB.3 CCA for semi-static channel accessSSB.4 CCA for dynamic channel access |  |  |
| DBT Window Configuration |  | Config 1 |  | DBT.1 |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 |  | 30 KHz |  |  |
| PRACH Configuration |  | Config 1 |  | Table  A.3.8A.2.2-1 |  |  |
| SSB Index assigned as BFD RS (q0) |  |  |  | 0 |  |  |
| SSB Index assigned as CBD RS (q1) |  |  |  | 1 |  |  |
| OCNG parameters |  |  |  | OP.1 |  |  |
| CP length |  |  |  | Normal |  |  |
| Correlation Matrix and Antenna Configuration |  |  |  | 2x2 Low |  |  |
| Beam failure detection transmission parameters | DCI format |  |  | 1-0 |  |  |
|  | Number of Control OFDM symbols |  |  | 2 |  |  |
|  | Aggregation level |  | CCE | 8 |  |  |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 0 |  |  |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 0 |  |  |
|  | DMRS precoder granularity |  |  | REG bundle size |  |  |
|  | REG bundle size |  |  | 6 |  |  |
| DRX |  |  |  | DRX.7 |  | A.3.3.7 |
| Gap pattern ID |  |  |  | N.A. |  |  |
| rlmInSyncOutOfSyncThreshold |  |  |  | absent |  | When the field is absent, the UE applies the value 0. (Table 8.1.1-1). |
| rsrp-ThresholdSSB | Config 1 |  | dBm/SCS kHz | -95 |  | Threshold used for Qin_LR_SSB |
| powerControlOffsetSS |  |  |  | db0 |  | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  |  |  | n1 |  | see clause 5.17 of TS 38.321 [7] |
| beamFailureDetectionTimer |  |  |  | pbfd4 |  | see clause 5.17 of TS 38.321 [7] |
| CSI-RS configuration for CSI reporting | Config 1 |  |  | CSI-RS.2.1 TDD |  |  |
| CSI-RS for tracking | Config 1 |  |  | TRS.1.2 TDD |  |  |
| SSB Index assigned as RLM RS |  |  |  | 0, 1 |  |  |
| T310 Timer |  |  | ms | 1000 |  |  |
| N310 |  |  |  | 2 |  |  |
| T1 |  |  | s | 1 |  | During this time the the UE shall be fully synchronized to Cell 1 |
| T2 |  |  | s | 9.01 |  |  |
| T3 |  |  | s | 5.16 |  |  |
| T4 |  |  | s | 0 |  |  |
| T5 |  |  | s | 3.89 |  |  |
| D1 |  |  | s | 3.85 |  |  |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |  |

Table A.11.4.4.2.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

| Parameter |  |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 | T4 | T5 |
| DL CCA probability PCCA |  | Note 10, 12 |  | 1.0 | 0.9375 | 0.9375 | 0.9375 | 0.9375 |
|  |  | Note 11, 12 |  | 1.0/1.0 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 |
| UL CCA probability PCCA |  |  |  | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| EPRE ratio of PDCCH DMRS to SSS |  |  | dB | 0 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  | dB |  |  |  |  |  |
| SNR_SSB of set q0 | Config 1 |  | dB | 5 | -3 | -12 | -12 | -12 |
| SNR_SSB of set q1 | Config 1 |  | dB | -10 | -10 | 10 | 10 | 10 |
| SSB_RP of set q1 | Config 1 |  | dBm/SCS kHz | -105 | -105 | -85 | -85 | -85 |
| ![](media_svg/image8.svg) [公式≈: ^{N}oc] | Config 1 |  | dBm/15 KHz | -98 |  |  |  |  |
| Propagation condition |  |  |  | TDL-C 300 ns 100 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio the transmitted SSS REs during DBT window.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.4.5.5.1.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4RX on all bands, the SNR during T3 is modified as specified in clause A.3.6A.NOTE 10: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 11: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2.NOTE 12: For UE supporting both semi-static and dynamic cannel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |  |

![](media/C:\Users\w00527694\Pictures\图片28.png)

Figure A.11.4.4.2.1-1: SNR and L1-RSRP variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

##### A.11.4.4.2.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 3850 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

### A.11.4.5 Active BWP switching

#### A.11.4.5.1 UL active BWP switch delay with consistent UL LBT failure on PCell subject to UL CCA

##### A.11.4.5.1.1 Test Purpose and Environment

The purpose of this test is to verify the UL BWP switch delay requirement defined in clause 8.6.4.

The supported test configurations are shown in table A.11.4.5.1.1-1. The test scenario comprises of one cell (Cell 1), which is Pcell as given in table A.11.4.5.1.1-2. Cell-specific parameters of the cell are specified in table A.11.4.5.1.1-3 below. SRS configuration used in the test is specified in table A.11.4.5.1.1-4.

Before the test starts,

- UE is connected to Cell 1 on radio channel 1.

- UE is configured with 2 different UE-specific downlink and uplink bandwidth parts: DL BWP-1, DL BWP-2, UL BWP-1 and UL BWP-2 before starting the test. DL BWP-1 and DL BWP-2 always include bandwidth of the initial DL BWP and SSB. UL BWP-1 and UL BWP-2 always include bandwidth of the SRS.

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is DL BWP-1.

- UE is indicated in firstActiveUplinkBWP-Id that the active UL BWP is UL BWP-1.

- UE is configured with LBT-FailureRecoveryConfig parameters for Cell 1.

The cell has constant signal levels throughout the test. The test consists of 2 successive time periods, with durations of T1 and T2, respectively.

During T1,

- Time period T1 starts when the UE has received the SRS configuration for periodic SRS transmission on active UL BWP-1.

- The UE shall perform UL CCA before SRS transmission.

- The parameter UL CCA probability PCCA is set to 0 during T1. This requires the test system to set energy level above the detection level during portion of the UL slot where the UE performs UL CCA. This in turn forces the UE to fail the UL CCA. The UE consistently fails UL CCA during T1 and is therefore unable to transmit SRS.

During T2,

- T2 starts when the UE detects consistent UL LBT failures i.e. when total number of UL LBT failures in Cell 1 on active UL BWP-1 exceeds lbt-FailureInstanceMaxCount during lbt-FailureDetectionTimer.

- The UE upon detected consistent UL LBT failure starts the LBT recovery mechanism, which requires the UE to switch to active UL BWP-2 in Cell 1 and to send PRACH in the active UL BWP-2.

- Staring from T2, the UE shall be able to send PRACH in the active UL BWP-2 within the delay specified in clause 8.6.4.

Table A.11.4.5.1.1-1: Supported test configurations for UL BWP switch test in SA

| Config | Description |
| --- | --- |
| 1 | With CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: void |  |

Table A.11.4.5.1.1-2: General test parameters for UL BWP switch test in SA

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active Cell |  | Cell 1 | Cell 1 on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| lbt-FailureDetectionTimer [2] | ms | 80 | Parameter configured by IE: LBT-FailureRecoveryConfig [1] |
| lbt-FailureInstanceMaxCount [2] |  | 4 | Parameter configured by IE: LBT-FailureRecoveryConfig [1] |
| T1 | s | 0.1 | During T1 consistent LBT failure is detected on active UL BWP-1 |
| T2 | s | 0.1 | During T2 UE sends PRACH on active UL BWP-2 |

Table A.11.4.5.1.1-3: NR Cell specific test parameters for UL BWP switch test in SA

| Parameter |  |  | Unit | Cell 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |
| BWchannel |  | Config 1 |  | 40 MHz: NPRB,c = 106 |  |
| DL CCA model |  | Config 1 |  | As specified in clauseA.3.26.2.1 |  |
| UL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.2 |  |
| Active BWP ID |  | Config 1 |  | 1, 2 |  |
| Initial DL BWP Configuration |  | Config 1 |  | DLBWP.0.2 Note 4 |  |
| Active DL BWP-1 Configuration |  | Config 1 |  | DLBWP.1.1 Note 4 |  |
| Active DL BWP-2 Configuration |  | Config 1 |  | DLBWP.1.3 Note 4 |  |
| Initial UL BWP Configuration |  | Config 1 |  | ULBWP.0.2 Note 4 |  |
| Active UL BWP-1 Configuration |  | Config 1 |  | ULBWP.1.1 Note 4 |  |
| Active UL BWP-2 Configuration |  | Config 1 |  | ULBWP.1.3 Note 4 |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 CCA |  |
| RMSI CORESET parameters |  | Config 1 |  | CR.1.1 CCA |  |
| Dedicated CORESET parameters |  | Config 1 |  | CCR.1.3 CCA |  |
| OCNG Patterns |  | Config 1 |  | OP.1 |  |
| SSB Configuration | Semi- static channel acces | Config 1 |  | SSB.1 CCA |  |
|  | Dymamic channel acces | Config 1 |  | SSB.2 CCA |  |
| SMTC Configuration |  | Config 1 |  | SMTC.1 FR1 |  |
| Correlation Matrix and Antenna Configuration |  | Config 1 |  | 1x2 Low |  |
| TRS Configuration |  | Config 1 |  | TRS.1.2 TDD |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | Config 1 |  | 1 | 1 |
| DL CCA model probability for dynamic static channel access (PCCA_DL_1) |  | Config 1 |  | 1 | 1 |
| DL CCA model probability for dynamic static channel access (PCCA_DL_2) |  | Config 1 |  | 1 | 1 |
| UL CCA probability (PCCA_UL) |  | Config 1 |  | 0 | 1 |
| PRACH configuration |  | Config 1 |  | N/A | Configuration #1 in table A.3.8.2.1-1 |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| NocNote 2 |  | Config 1 | dBm/SCS | -101 |  |
| SS-RSRP Note 3 |  | Config 1 | dBm/SCS | -84 |  |
| Ês/Iot |  | Config 1 | dB | 17 |  |
| Ês/Noc |  | Config 1 | dB | 17 |  |
| IoNote3 |  | Config 1 | dBm/38.16 MHz | -52.86 |  |
| Propagation Condition |  |  |  | AWGN |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For unpaired spectrum, a DL BWP is linked with an UL BWP. DLBWP.0.2 is linked with ULBWP.0.2; DLBWP.1.1 is linked with ULBWP.1.1; DLBWP.1.3 is linked with ULBWP.1.3 defined in clause 12 of TS 38.213 [3].NOTE 5: Parameters PCCA_DL, PCCA_DL_1, PCCA_DL_2 and PCCA_UL are defined in clause A.3.26.2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |

Table A.11.4.5.1.1-4: Sounding Reference Symbol Configuration for UL BWP Switch Test

| Field | Value | Comment |
| --- | --- | --- |
| c-SRS | 24 | Frequency hopping is disabled |
| b-SRS | 0 |  |
| b-hop | 0 |  |
| freqDomainPosition | 0 | Frequency domain position of SRS |
| freqDomainShift | 0 |  |
| groupOrSequenceHopping | neither | No group or sequence hopping |
| SRS-PeriodicityAndOffset | sl5=4 for SCS 30 kHz | Once every 5 slots |
| pathlossReferenceRS | ssb-Index=0 | SSB #0 is used for SRS path loss estimation |
| usage | Codebook | Codebook based UL transmission |
| startPosition | 0 | resourceMapping setting: SRS on last symbol of slot, and 1 symbols for SRS without repetition. |
| nrofSymbols | n1 |  |
| repetitionFactor | n1 |  |
| combOffset-n2 | 0 | transmissionComb setting |
| cyclicShift-n2 | 0 |  |
| nrofSRS-Ports | port1 | Number of antenna ports used for SRS transmission |
| NOTE: For further information see clause 6.3.2 in TS 38.331 [2]. |  |  |

##### A.11.4.5.1.2 Test Requirements

The UE capable of bwp-SwitchingDelay type1 [2] shall start to transmit the PRACH on active UL BWP-2 of Cell 1 (PCell) less than 21.5 ms from the beginning of time period T1.

The UE capable of bwp-SwitchingDelay type2 [2] shall start to transmit the PRACH on active UL BWP-2 of Cell 1 (PCell) less than 23 ms from the beginning of time period T1.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The above delay is calculated as follows:’

The active UL BWP switch delay from UL BWP-1 to UL BWP-2 can be expressed as:

TBWPswitchDelay*Tslot +1*Tslot + (1+ L3)*TSSB,RO + 10 ms

Where:

TBWPswitchDelay = 1 ms (2 slots) and 2.5 ms (5 slots) for bwp-SwitchingDelay [2] type1 and type2 UE capabilities according to clause 8.6.4.

Tslot = It is the slot length. It is 0.5 ms for 30 kHz.

L3 = It is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure. L3= 0 during T2 since PCCA = 1.

TSSB,RO = 10 ms according to FR1 PRACH configuration 1.

This gives a total of 21.5 ms and 23 ms for type1 and type2 UE respectively.

#### A.11.4.5.2 DCI-based and Timer-based Active BWP Switch

##### A.11.4.5.2.1 NR FR1- NR FR1 DL active BWP switch of PCell with non-DRX in SA

A.11.4.5.2.1.1 Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6, and interruption requirement on other active serving cell defined in clause 8.2.2.2.5.

The supported test configurations are shown in table A.11.4.5.2.1.1-1 below. The test scenario comprises of one PCell (Cell 1) and one SCell (Cell 2) as given in table A.11.4.5.2.1.1-2. NR Cell-specific parameters are specified in table A.11.4.5.2.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 1 and the time duration of T2.

PDCCHs indicating new transmissions shall be sent continuously on SCell (Cell 2) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

- UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (SCell) on radio channel 2 (SCC).

- UE is configured with 2 different UE-specific downlink bandwidth parts for PCell, BWP-1 and BWP-2, in Cell 1 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

- UE is configured with 1 UE-specific downlink bandwidth parts the same as initial BWP for SCell, BWP-0 in Cell 2 before starting the test.

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PCell.

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in SCell.

- UE is configured with a bwp-InactivityTimer timer value for PCell.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for PCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH no later than the first DL slot that occurs after the beginning of PCell’s DL slot (i+TBWPswitchDelay) as defined in clause8.6 and starts to report valid ACK/NACK for the PCell no later than the first UL slot that occurs after the beginning of slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PCell’s BWP-2 no later than the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).

The starting time of SCell (Cell 2) interruption due to BWP switch on PCell shall occur within the BWP switch delay.

During T2, the test equipment won’t transmit DCI format for PDSCH reception on PCell (Cell 1).

During T3,

The time period T3 starts from the slot #j, where j is the first  slot of the subframe immediately after bwp-InactivityTimer timer expires. The UE should switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH no later than the first DL slot that occurs after the beginning of PCell’s slot (j+TBWPswitchDelay) as defined in clause8.6 and starts to report valid ACK/NACK for the SCell at latest on the first UL slot that occurs after the beginning of slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PCell’s BWP-1 no later than the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

The starting time of SCell (Cell 2) interruption due to BWP switch of PCell shall occur within the BWP switch delay.

The test equipment verifies the DL BWP switch time in PCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK/NACK is received.

The test equipment verifies that potential interruption to SCell is carried out in the correct time span by monitoring ACK/NACK sent in SCell during BWP switch of PCell, respectively.

Table A.11.4.5.2.1.1-1: DL BWP switch supported test configurations

| Config | Description |
| --- | --- |
| 1 | With CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: VoidNOTE 2:  The UE supporting SA operation with only NR band(s) with shared spectrum access is required to be tested. |  |

Table A.11.4.5.2.1.1-2: General test parameters for DL BWP switch in SA

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1, 2 | Two NR radio channels are used in this test |
| Active PCell |  | Cell 1 | PCell on RF channel number 1. |
| Active SCell |  | Cell 2 | SCell on RF channel number 2. |
| CP length |  | Normal |  |
| DRX |  | OFF | For both PCell and SCell |
| DL CCA model |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | As specified in clauseA.3.26.2.2 |  |
| bwp-InactivityTimer | ms | 200 |  |
| Cell-individual offset for cells on RF channel number 1 | dB | 0 | Individual offset for cells on PCC. |
| Cell-individual offset for cells on RF channel number 2 | dB | 0 | Individual offset for cells on SCC. |
| Cell 2 timing offset to Cell 1 | s | 3 | Time alignment error as specified in TS 38.104 [13] clause 6.5.3.1. |
| T1 | s | 0.2 |  |
| T2 | s | 0.2 |  |
| T3 | s | 0.2 |  |

Table A.11.4.5.2.1.1-3: NR Cell specific test parameters for DL BWP switch in SA

| Parameter |  |  | Unit | Cell 1 | Cell 2 |
| --- | --- | --- | --- | --- | --- |
| Frequency Range |  |  |  | FR1 |  |
| Duplex mode |  | Config 1 |  | TDD |  |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |
| BWchannel |  | Config 1 |  | 40 MHz: NPRB,c = 106 |  |
| Active BWP ID |  |  |  | 1, 2 | 0 |
| Initial DL BWP Configuration |  |  |  | DLBWP.0.2Note4 |  |
| Initial UL BWP Configuration |  |  |  | ULBWP.0.2Note4 |  |
| Active DL BWP-0 Configuration |  |  |  | N.A. | DLBWP.0.2Note4 |
| Active DL BWP-1 Configuration |  |  |  | DLBWP.1.1Note4 | N.A. |
| Active DL BWP-2 Configuration |  |  |  | DLBWP.1.3Note4 | N.A. |
| Active UL BWP-0 Configuration |  |  |  | N.A. | ULBWP.0.2Note4 |
| Active UL BWP-1 Configuration |  |  |  | ULBWP.1.1Note4 | N.A. |
| Active UL BWP-2 Configuration |  |  |  | ULBWP.1.3Note4 | N.A. |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 CCA |  |
| RMSI CORESET parameters |  | Config 1 |  | CR.1.1 CCA |  |
| Dedicated CORESET parameters |  | Config 1 |  | CCR.1.3 CCA |  |
| OCNG Patterns |  |  |  | OP.1 |  |
| SSB Configuration | Semi- static channel acces | Config 1 |  | SSB.1 CCA |  |
|  | Dymamic channel acces | Config 1 |  | SSB.2 CCA |  |
| SMTC Configuration |  | Config 1 |  | SMTC.1 |  |
| DL CCA probability (PCCA_DL) |  | Config 1 |  | 1 | 1 |
| UL CCA probability (PCCA_UL) |  | Config 1 |  | 1 | 1 |
| Correlation Matrix and Antenna Configuration |  |  |  | 1x2 Low |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| NocNote 2 |  | Config 1 | dBm/SCS | -101 | -101 |
| SS-RSRP Note 3 |  | Config 1 | dBm/SCS | -84 | -84 |
| Ês/Iot |  | Config 1 | dB | 17 | 17 |
| Ês/Noc |  | Config 1 | dB | 17 | 17 |
| IoNote3 |  | Config 1 | dBm/38.16 MHz | -52.86 | -52.86 |
| Propagation Condition |  |  |  | AWGN | AWGN |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.Note 3 SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For unpaired spectrum, a DL BWP is linked with an UL BWP. DLBWP.0.2 is linked with ULBWP.0.2; DLBWP.1.1 is linked with ULBWP.1.1; DLBWP.1.3 is linked with ULBWP.1.3 defined in clause 12 of TS 38.213 [3]. |  |  |  |  |  |

A.11.4.5.2.1.2 Test Requirements

During T1, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

During T1 and T3, the start time of SCell interruption during PCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of SCell shall not be longer than the interruption duration specified for active BWP switch in clause 8.2.2.2.5.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch interruption to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first DL slot that occurs after the beginning of DL slot (i+ TBWPswitchDelay+k1), (j+ TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

##### A.11.4.5.2.2 NR FR1 DL active BWP switch with non-DRX in SA

A.11.4.5.2.2.1 Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6.

The supported test configurations are shown in table A.11.4.5.2.2.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.11.4.5.2.2.1-2. Cell-specific parameters of the cell are specified in table A.11.4.5.2.2.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.

Before the test starts,

- UE is connected to Cell 1 on radio channel 1.

- UE is configured with 2 different UE-specific downlink bandwidth parts, BWP-1 and BWP-2 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1.

- UE is configured with a bwp-InactivityTimer timer value for Cell 1.

The cell has constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for DL BWP switch, sent from the test equipment to the UE, is received at the UE side in Cell 1’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the Cell 1 no later than the first UL slot that occurs after the beginning of slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on Cell 1’s BWP-2 starting from the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).

During T2, the test equipment won’t transmit DCI format for PDSCH reception on Cell 1.

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the subframe immediately after bwp-InactivityTimer timer expires. The UE shall switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s slot (j+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the Cell 1 at latest on the first UL slot that occurs after the beginning of slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on Cell 1’s BWP-1 starting from the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

The test equipment verifies the DL BWP switch time by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK/NACK is received.

Table A.11.4.5.2.2.1-1: DL BWP switch supported test configurations

| Config | Description |
| --- | --- |
| 1 | With CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations.NOTE 2: A UE which fulfils the requirements in test case A.11.4.5.2.1 can skip the test cases in A.11.4.5.2.2.NOTE 3: The UE supporting SA operation with only NR band(s) with shared spectrum access is required to be tested. |  |

Table A.11.4.5.2.2.1-2: General test parameters for DL BWP switch in SA

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active Cell |  | Cell 1 | Cell 1 on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| DL CCA model |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | As specified in clause A.3.26.2.2 |  |
| bwp-InactivityTimer | ms | 200 |  |
| T1 | s | 0.2 |  |
| T2 | s | 0.2 |  |
| T3 | s | 0.2 |  |

Table A.11.4.5.2.2.1-3: NR Cell specific test parameters for DL BWP switch in SA

| Parameter |  |  | Unit | Cell 1 |
| --- | --- | --- | --- | --- |
| Frequency Range |  |  |  | FR1 |
| Duplex mode |  | Config 1 |  | TDD |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |
| BWchannel |  | Config 1 |  | 40 MHz: NPRB,c = 106 |
| Active BWP ID |  |  |  | 1, 2 |
| Initial DL BWP Configuration |  | Config 1 |  | DLBWP.0.2 Note 4 |
| Active DL BWP-1 Configuration |  | Config 1 |  | DLBWP.1.1 Note 4 |
| Active DL BWP-2 Configuration |  | Config 1 |  | DLBWP.1.3 Note 4 |
| Initial UL BWP Configuration |  | Config 1 |  | ULBWP.0.2 Note 4 |
| Active UL BWP-1 Configuration |  | Config 1 |  | ULBWP.1.1 Note 4 |
| Active UL BWP-2 Configuration |  | Config 1 |  | ULBWP.1.3 Note 4 |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 CCA |
| RMSI CORESET parameters |  | Config 1 |  | CR.1.1 CCA |
| Dedicated CORESET parameters |  | Config 1 |  | CCR.1.3 CCA |
| OCNG Patterns |  |  |  | OP.1 |
| SSB Configuration | Semi- static channel acces | Config 1 |  | SSB.1 CCA |
|  | Dymamic channel acces | Config 1 |  | SSB.2 CCA |
| SMTC Configuration |  | Config 1 |  | SMTC.1 |
| Correlation Matrix and Antenna Configuration |  |  |  | 1x2 Low |
| TRS Configuration |  | Config 1 |  | TRS.1.2 TDD |
| DL CCA probability (PCCA_DL) |  | Config 1 |  | 1 |
| UL CCA probability (PCCA_UL) |  | Config 1 |  | 1 |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| NocNote 2 |  | Config 1 | dBm/SCS | -101 |
| SS-RSRP Note 3 |  | Config 1 | dBm/SCS | -84 |
| Ês/Iot |  | Config 1 | dB | 17 |
| Ês/Noc |  | Config 1 | dB | 17 |
| IoNote3 |  | Config 1 | dBm/38.16 MHz | -52.86 |
| Propagation Condition |  |  |  | AWGN |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For unpaired spectrum, a DL BWP is linked with an UL BWP. DLBWP.0.2 is linked with ULBWP.0.2; DLBWP.1.1 is linked with ULBWP.1.1; DLBWP.1.3 is linked with ULBWP.1.3 defined in clause 12 of TS 38.213 [3]. |  |  |  |  |

A.11.4.5.2.2.2 Test Requirements

During T1, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed Cell 1 active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first UL slot that occurs after beginning of DL slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

#### A.11.4.5.3 RRC-based Active BWP Switch

##### A.11.4.5.3.1 NR FR1 DL active BWP switch of Cell with non-DRX in SA

A.11.4.5.3.1.1 Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6.

The supported test configurations are shown in table A.11.4.5.3.1.1-1. The test scenario comprises of one Cell (Cell 1) as given in table A.11.4.5.3.1.1-2. Cell-specific parameters of Cell are specified in table A.11.4.5.3.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.

Before the test starts,

- UE is connected to Cell 1 on radio channel 1.

- UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1.

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in Cell 1.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is completely received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition.

The UE shall be able to receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}$ as defined in clause 8.6.3 and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}+k1 $ on BWP-1 of final condition. The UE shall be continuously scheduled on PCell’s BWP-1 of final condition starting from the first DL slot right after slot $ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}$.

TRRCprocessingDelay and TBWPswitchDelayRRC are defined in clause 8.6.3.

The test equipment verifies the DL BWP switch time in Cell by counting the time from the time when the RRC Reconfiguration message including updated BWP configuration is sent till the time when a vaild ACK/NACK is received is received.

Table A.11.4.5.3.1.1-1: DL BWP switch supported test configurations in SA scenario

| Config | Description |
| --- | --- |
| 1 | With CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: VoidNOTE 2: The UE supporting SA operation with only NR band(s) with shared spectrum access is required to be tested. |  |

Table A.11.4.5.3.1.1-2: General test parameters for DL BWP switch in SA scenario

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active Cell |  | Cell 1 | Cell on RF channel number 1. |
| CP length |  | Normal |  |
| DL CCA model |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | As specified in clause A.3.26.2.2 |  |
| DRX |  | OFF |  |
| T1 | s | 0.2 |  |

Table A.11.4.5.3.1.1-3: NR Cell specific test parameters for DL BWP switch in SA scenario

| Parameter |  |  |  | Unit | Cell 1 |
| --- | --- | --- | --- | --- | --- |
| Frequency Range |  |  |  |  | FR1 |
| Duplex mode |  |  | Config 1 |  | TDD |
| TDD configuration |  |  | Config 1 |  | TDDConf.1.1 CCA |
| BWchannel |  |  | Config 1 |  | 40 MHz: NPRB,c = 106 |
| Active BWP ID |  |  |  |  | 1 |
| Initial DL BWP Configuration |  |  | Config 1 |  | DLBWP.0.2 |
| Initial UL BWP Configuration |  |  | Config 1 |  | ULBWP.0.2 |
| Initial Condition | Active DL BWP-1 Configuration |  | Config 1 |  | DLBWP.1.3 |
|  | Active UL BWP-1 Configuration |  | Config 1 |  | ULBWP.1.3 |
| FinalCondition | Active DL BWP-1 Configuration |  | Config 1 |  | DLBWP.1.1 |
|  | Active UL BWP-1 Configuration |  | Config 1 |  | ULBWP.1.1 |
| PDSCH Reference measurement channel |  |  | Config 1 |  | SR.1.1 CCA |
| RMSI CORESET parameters |  |  | Config 1 |  | CR.1.1 CCA |
| Dedicated CORESET parameters |  |  | Config 1 |  | CCR.1.3 CCA |
| OCNG Patterns |  |  |  |  | OP.1 |
| SSB Configuration |  | Semi-static channel acces | Config 1 |  | SSB.1 CCA |
|  |  | Dymamic channel acces | Config 1 |  | SSB.2 CCA |
| SMTC Configuration |  |  |  |  | SMTC.1 |
| TRS Configuration |  |  | Config 1 |  | TRS.1.2 TDD |
| DL CCA probability (PCCA_DL) |  |  | Config 1 |  | 1 |
| UL CCA probability (PCCA_UL) |  |  | Config 1 |  | 1 |
| Propagation Condition |  |  |  |  | AWGN |
| EPRE ratio of PSS to SSS |  |  |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| NocNote 2 |  |  | Config 1 | dBm/SCS | -101 |
| SS-RSRP Note 3 |  |  | Config 1 | dBm/SCS | -84 |
| Ês/Iot |  |  | Config 1 | dB | 17 |
| Ês/Noc |  |  | Config 1 | dB | 17 |
| IoNote3 |  |  | Config 1 | dBm/38.16 MHz | -52.86 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For unpaired spectrum, a DL BWP is linked with an UL BWP. DLBWP.0.2 is linked with ULBWP.0.2; DLBWP.1.1 is linked with ULBWP.1.1; DLBWP.1.3 is linked with ULBWP.1.3 defined in clause 12 of TS 38.213 [3]. |  |  |  |  |  |

A.11.4.5.3.1.2 Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the Cell from the first DL slot that occurs right after the begining of slot $ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}$ and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}+k1 $.

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed Cell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

### A.11.4.6 Void

## A.11.5 Measurement procedure

### A.11.5.1 Intra-frequency measurements

#### A.11.5.1.1 Event-triggered reporting tests on PCC without gaps under non-DRX

##### A.11.5.1.1.1 Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.5.1 and 9.2A.5.2.

##### A.11.5.1.1.2 Test parameters

Two cells are deployed in the test, which are PCell (Cell 1) and a neighbour cell (Cell 2) on the same carrier frequency with CCA transmitting SSBs in DBT windows according to DL CCA model. The test parameters for the two cells are given in table A.11.5.1.1.2-1 and A.11.5.1.1.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

Table A.11.5.1.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

Table A.11.5.1.1.2-2: General test parameters for intra-frequency event triggered reporting without gaps

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Active cell |  |  | 1 | Cell 1 |  |
| Neighbour cell |  |  | 1 | Cell 2 | Cell to be identified. |
| RF Channel Number |  |  | 1 | 1: Cell 1 and Cell 2 |  |
| DL CCA model |  |  | 1 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | 1 | As specified in clause A.3.26.2.2 |  |
| SSB configuration | Semi-static channel access Note 1,3 |  | 1 | SSB.1 CCA |  |
|  | Dynamic channel access Note 2,3 |  | 1 | SSB.2 CCA |  |
| SMTC configuration |  |  | 1 | SMTC.1 |  |
| A3-Offset |  | dB | 1 | -4.5 |  |
| CP length |  |  | 1 | Normal |  |
| Hysteresis |  | dB | 1 | 0 |  |
| Time To Trigger |  | s | 1 | 0 |  |
| Filter coefficient |  |  | 1 | 0 | L3 filtering is not used |
| DRX |  |  | 1 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  |  | 1 | 3 s | Synchronous cells |
| T1 |  | s | 1 | 5 |  |
| T2 |  | s | 1 | 5 |  |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |

Table A.11.5.1.1.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gaps

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| TDD configuration |  | 1 | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | 1 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_1) |  | 1 | PCCA_DL_1=0.75 |  | PCCA_DL_1=0.75 |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_2) |  | 1 | PCCA_DL_2=0.75 |  | PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL |  | 1 | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  | 1 | 7 |  | 7 |  |
| WCCA_DL | ms | 1 | 600 |  | 600 |  |
| PDSCH RMC configuration |  | 1 | SR.1.1 CCA |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1 | CR.1.1 CCA |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.1.1 CCA |  | N/A |  |
| OCNG Patterns |  | 1, 2, 3 | OP.1 |  | OP.1 |  |
| TRS Configuration |  | 1 | TRS.1.2 TDD |  | N/A |  |
| IInitial BWP configuration |  | 1 | DLBWP.0.1 ULBWP.0.1 |  | DLBWP.0.1 ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1 | DLBWP.1.1 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1 | ULBWP.1.1 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1 | SSB |  | SSB |  |
| Note 2 | dBm/SCS | 1 | -95 |  |  |  |
| Note 2 | dBm/15 kHz | 1 | -98 |  |  |  |
|  | dB | 1 | 4 | -1.46 | -Infinity | -1.46 |
|  |  | 2 |  |  |  |  |
|  |  | 3 |  |  |  |  |
|  | dB | 1 | 4 | 4 | -Infinity | 4 |
| SS-RSRP Note 3 | dBm/SCS kHz | 1 | -91 | -91 | -Infinity | -91 |
| Io | dBm/38.16 MHz | 1 | -58.50 | -56.16 | -58.50 | -56.16 |
| Propagation Condition |  | 1 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window. |  |  |  |  |  |  |

##### A.11.5.1.1.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 840 ms from the beginning of time period T2.

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.11.5.1.2 Event-triggered reporting tests on PCC without gaps under DRX

##### A.11.5.1.2.1 Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.5.1 and 9.2A.5.2.

##### A.11.5.1.2.2 Test parameters

Two cells are deployed in the test, which are PCell (Cell 1) and a neighbour cell (Cell 2) on the same carrier frequency with CCA transmitting SSBs in DBT windows according to DL CCA model. The test parameters for the two cells are given in table A.11.5.1.2.2-1 and A.11.5.1.2.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, the UE is allocated with PUSCH resource at every DRX cycle.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

Table A.11.5.1.2.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

Table A.11.5.1.2.2-2: General test parameters for intra-frequency event triggered reporting without gaps

| Parameter |  | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 | Test |  |
| Active cell |  |  | 1 | Cell 1 |  |  |
| Neighbour cell |  |  | 1 | Cell 2 |  | Cell to be identified. |
| RF Channel Number |  |  | 1 | 1: Cell 1 and Cell 2 |  |  |
| DL CCA model |  |  | 1 | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  |  | 1 | As specified in clause A.3.26.2.2 |  |  |
| SSB configuration | Semi-static channel access Note 1,3 |  | 1 | SSB.1 CCA |  |  |
|  | Dynamic channel access Note 2,3 |  | 1 | SSB.2 CCA |  |  |
| SMTC configuration |  |  | 1 | SMTC.1 |  |  |
| A3-Offset |  | dB | 1 | -4.5 |  |  |
| CP length |  |  | 1 | Normal |  |  |
| Hysteresis |  | dB | 1 | 0 |  |  |
| Time To Trigger |  | s | 1 | 0 |  |  |
| Filter coefficient |  |  | 1 | 0 |  | L3 filtering is not used |
| DRX |  |  | 1 | DRX.1 | DRX.7 |  |
| Time offset between serving and neighbour cells |  |  | 1 | 3 s |  | Synchronous cells |
| T1 |  | s | 1 | 5 |  |  |
| T2 |  | s | 1 | 5 | 15 |  |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |

Table A.11.5.1.2.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gaps

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| TDD configuration |  | 1 | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | 1 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_1) |  | 1 | PCCA_DL_1=0.75 |  | PCCA_DL_1=0.75 |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_2) |  | 1 | PCCA_DL_2=0.75 |  | PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL |  | 1 | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  | 1 | Test 1: LCCA_DL = 5Test 2: LCCA_DL = 3 |  | Test 1: LCCA_DL = 5Test 2: LCCA_DL = 3 |  |
| WCCA_DL | ms | 1 | Test 1: WCCA_DL = 600Test 2: WCCA_DL = 5120 |  | Test 1: WCCA_DL = 600Test 2: WCCA_DL = 5120 |  |
| PDSCH RMC configuration |  | 1 | SR.1.1 CCA |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1 | CR.1.1 CCA |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.1.1 CCA |  | N/A |  |
| OCNG Patterns |  | 1, 2, 3 | OP.1 |  | OP.1 |  |
| TRS Configuration |  | 1 | TRS.1.2 TDD |  | N/A |  |
| IInitial BWP configuration |  | 1 | DLBWP.0.1 ULBWP.0.1 |  | DLBWP.0.1 ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1 | DLBWP.1.1 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1 | ULBWP.1.1 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1 | SSB |  | SSB |  |
| Note 2 | dBm/SCS | 1 | -95 |  |  |  |
| Note 2 | dBm/15 kHz | 1 | -98 |  |  |  |
|  | dB | 1 | 4 | -1.46 | -Infinity | -1.46 |
|  |  | 2 |  |  |  |  |
|  |  | 3 |  |  |  |  |
|  | dB | 1 | 4 | 4 | -Infinity | 4 |
| SS-RSRP Note 3 | dBm/SCS kHz | 1 | -91 | [-91] | -Infinity | -91 |
| Io | dBm/38.16 MHz | 1 | -58.50 | -56.16 | [-58.50 | -56.16 |
| Propagation Condition |  | 1 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window. |  |  |  |  |  |  |

##### A.11.5.1.2.3 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report with a measurement reporting delay less than 1200 ms from the beginning of time period T2.

In test 2, the UE shall send one Event A3 triggered measurement report with a measurement reporting delay less than 10240 ms from the beginning of time period T2.

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.11.5.1.3 Void

#### A.11.5.1.4 Void

#### A.11.5.1.5 Void

#### A.11.5.1.6 Void

#### A.11.5.1.7 Void

#### A.11.5.1.8 Void

#### A.11.5.1.9 Void

#### A.11.5.1.10 Void

#### A.11.5.1.11 Void

#### A.11.5.1.12 Void

### A.11.5.2 Inter-frequency measurements

#### A.11.5.2.1 Void

#### A.11.5.2.2 Void

#### A.11.5.2.3 Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is not used

##### A.11.5.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements for NR cell with CCA in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 with CCA as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters are given in tables A.11.5.2.3.1-1, A.11.5.2.3.1-2 and A.11.5.2.3.1-3.

In this test, measurement gap pattern configuration # 0 as defined in table A.11.5.2.3.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

Table A.11.5.2.3.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1 with CCA

| Config | Description |
| --- | --- |
| 1 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.5.2.3.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1 | 1, 2 | Two FR1 NR carrier frequencies are used. Channels 1 and 2 are with CCA. |
| Active cells |  | Config 1 | NR Cell 1 with CCA (PCell) | NR Cell 1 is on NR RF channel number 1 with CCA. |
| Neighbour cell |  | Config 1 | NR Cell 2 with CCA | NR Cell 2 is on NR RF channel number 2 with CCA. |
| DL CCA model |  | Config 1 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | Config 1 | As specified in clause A.3.26.2.2 |  |
| Gap Pattern Id |  | Config 1 | 0 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1 | 9 |  |
| A3-Offset | dB | Config 1 | -6 |  |
| Hysteresis | dB | Config 1 | 0 |  |
| CP length |  | Config 1 | Normal |  |
| TimeToTrigger | s | Config 1 | 0 |  |
| Filter coefficient |  | Config 1 | 0 | L3 filtering is not used |
| DRX |  | Config 1 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | Config 1 | 3 s | Synchronous cells. |
| T1 | s | Config 1 | 5 |  |
| T2 | s | Config 1 | 1.7 |  |

Table A.11.5.2.3.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1 | 1 |  | 2 |  |
| Duplex mode |  |  |  | Config 1 | TDD |  |  |  |
| TDD configuration |  |  |  | Config 1 | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  |  | MHz | Config 1 | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  |  | MHz | Config 1 | 40: NPRB,c = 106 |  |  |  |
| BWP configuration | Initial DL BWP |  | Config 1 | Config 1 | DLBWP.0.1 |  | NA |  |
|  | Initial UL BWP |  | Config 1 |  | ULBWP.0.1 |  | NA |  |
|  | Dedicated DL BWP |  | Config 1 |  | DLBWP.1.1 |  | NA |  |
|  | Dedicated UL BWP |  | Config 1 |  | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  |  | Config 1 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1 | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1 | CR.1.1 CCA |  |  |  |
| SSB parameters |  | Semi-static channel access Note 5,7 |  | Config 1 | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1 | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  |  | Config 1 | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1 | SMTC.1 |  | SMTC.4 |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1 | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1 | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  |  | Config 1 | 12 |  | 12 |  |
| WCCA_DL |  |  | ms | Config 1 | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1 | 30 |  |  |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/9.36 MHz | Config 1 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  |  | Config 1 | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |

##### A.11.5.2.3.2 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2 UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.11.5.2.4 Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is used

##### A.11.5.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 as PCell in FR1 with CCA on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters are given in tables A.11.5.2.4.1-1, A.11.5.2.4.1-2 and A.11.5.2.4.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.11.5.2.4.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.11.5.2.4.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1 with CCA

| Config | Description |
| --- | --- |
| 1 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.5.2.4.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| NR RF Channel Number |  | Config 1 | 1, 2 |  | Two FR1 NR carrier frequencies are used. Channels 1 and 2 are with CCA. |
| Active cells |  | Config 1 | NR Cell 1 with CCA (PCell) |  | NR Cell 1 is on NR RF channel number 1 with CCA. |
| Neighbour cell |  | Config 1 | NR Cell 2 with CCA |  | NR Cell 2 is on NR RF channel number 2 with CCA. |
| DL CCA model |  | Config 1 | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  | Config 1 | As specified in clause A.3.26.2.2 |  |  |
| Gap Pattern Id |  | Config 1 | 0 |  | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1 | 9 |  |  |
| A3-Offset | dB | Config 1 | -6 |  |  |
| Hysteresis | dB | Config 1 | 0 |  |  |
| CP length |  | Config 1 | Normal |  |  |
| TimeToTrigger | s | Config 1 | 0 |  |  |
| Filter coefficient |  | Config 1 | 0 |  | L3 filtering is not used |
| DRX |  | Config 1 | DRX.1 | DRX.2 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | Config 1 | 3 s |  | Synchronous cells. |
| T1 | s | Config 1 | 5 |  |  |
| T2 | s | Config 1 | 2.5 | 17 |  |

Table A.11.5.2.4.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1 | 1 |  | 2 |  |
| Duplex mode |  |  |  | Config 1 | TDD |  |  |  |
| TDD configuration |  |  |  | Config 1 | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  |  | MHz | Config 1 | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  |  | MHz | Config 1 | 40: NPRB,c = 106 |  |  |  |
| BWP configuration | Initial DL BWP |  | Config 1 | Config 1 | DLBWP.0.1 |  | NA |  |
|  | Initial UL BWP |  | Config 1 |  | ULBWP.0.1 |  | NA |  |
|  | Dedicated DL BWP |  | Config 1 |  | DLBWP.1.1 |  | NA |  |
|  | Dedicated UL BWP |  | Config 1 |  | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  |  | Config 1 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1 | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1 | CR.1.1 CCA |  |  |  |
| SSB parameters |  | Semi-static channel access Note 5,7 |  | Config 1 | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1 | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  |  | Config 1 | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1 | SMTC.1 |  | SMTC.4 |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1 | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1 | PCCA_UL=1 |  | PCCA_UL=1 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1 | 30 |  |  |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/9.36 MHz | Config 1 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  |  | Config 1 | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for NOC to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |

Table A.11.5.2.4.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value |  | Comment |
| --- | --- | --- | --- |
|  | Test 1 | Test 2 |  |
| drx-onDurationTimer | ms1 | ms1 | As specified in clause 6.3.2 in TS 38.331 [2] |
| drx-InactivityTimer | ms1 | ms1 |  |
| drx-RetransmissionTimerDL | sl1 | sl1 |  |
| drx-RetransmissionTimerUL | sl1 | sl1 |  |
| drx-LongCycleStartOffset | ms40 | Ms640 |  |
| shortDRX | disable | disable |  |

Table A.11.5.2.4.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value | Comment |
| --- | --- | --- |
| TimeAlignmentTimer | ms500 | As specified in clause 6.3.2 in TS 38.331 [2] |

##### A.11.5.2.4.2 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2, the UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1, DRX cycle = 40 ms and for test 2, DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.11.5.2.5 Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is not used

##### A.11.5.2.5.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 as PCell in FR1 with CCA on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 with CCA on NR RF channel 2. The test parameters are given in tables A.11.5.2.5.1-1, A.11.5.2.5.1-2 and A.11.5.2.5.1-3.

In this test, measurement gap pattern configuration # 0 as defined in table A.11.5.2.5.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

Table A.11.5.2.5.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1 with CCA

| Config | Description |
| --- | --- |
| 1 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.5.2.5.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1 | 1, 2 | Two FR1 NR carrier frequencies are used. Channels 1 and 2 are with CCA. |
| Active cells |  | Config 1 | NR Cell 1 with CCA (PCell) | NR Cell 1 is on NR RF channel number 1 with CCA. |
| Neighbour cell |  | Config 1 | NR Cell 2 with CCA | NR Cell 2 is on NR RF channel number 2 with CCA. |
| DL CCA model |  | Config 1 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | Config 1 | As specified in clause A.3.26.2.2 |  |
| Gap Pattern Id |  | Config 1 | 0 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1 | 9 |  |
| A3-Offset | dB | Config 1 | -6 |  |
| Hysteresis | dB | Config 1 | 0 |  |
| CP length |  | Config 1 | Normal |  |
| TimeToTrigger | s | Config 1 | 0 |  |
| Filter coefficient |  | Config 1 | 0 | L3 filtering is not used |
| DRX |  | Config 1 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | Config 1 | 3s | Synchronous cells. |
| T1 | s | Config 1 | 5 |  |
| T2 | s | Config 1 | 2 |  |

Table A.11.5.2.5.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1 | 1 |  | 2 |  |
| Duplex mode |  |  |  | Config 1 | TDD |  |  |  |
| TDD configuration |  |  |  | Config 1 | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  |  | MHz | Config 1 | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  |  | MHz | Config 1 | 40: NPRB,c = 106 |  |  |  |
| BWP configuration | Initial DL BWP |  | Config 1 | Config 1 | DLBWP.0.1 |  | NA |  |
|  | Initial UL BWP |  | Config 1 |  | ULBWP.0.1 |  | NA |  |
|  | Dedicated DL BWP |  | Config 1 |  | DLBWP.1.1 |  | NA |  |
|  | Dedicated UL BWP |  | Config 1 |  | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  |  | Config 1 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1 | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1 | CR.1.1 CCA |  |  |  |
| SSB parameters |  | Semi-static channel access Note 5,7 |  | Config 1 | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  |  |  |  |  |  |  |  |
|  |  | Semi-static channel access Note 5,7 |  | Config 1 | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  |  |  |  |  |  |  |  |
| DBT window configuration |  |  |  | Config 1 | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1 | SMTC.1 |  | SMTC.4 |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1 | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1 | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  |  | Config 1 | 5 |  | 5 |  |
| WCCA_DL |  |  | ms | Config 1 | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1 | 30 |  |  |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/9.36 MHz | Config 1 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  |  | Config 1 | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |

##### A.11.5.2.5.2 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.11.5.2.6 Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is used

##### A.11.5.2.6.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 as PCell in FR1 with CCA on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters are given in tables A.11.5.2.6.1-1, A.11.5.2.6.1-2 and A.11.5.2.6.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.11.5.2.6.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.11.5.2.6.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1 with CCA

| Config | Description |
| --- | --- |
| 1 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.5.2.6.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| NR RF Channel Number |  | Config 1 | 1, 2 |  | Two FR1 NR carrier frequencies are used. Channels 1 and 2 are with CCA. |
| Active cells |  | Config 1 | NR Cell 1 with CCA (PCell) |  | NR Cell 1 is on NR RF channel number 1 with CCA. |
| Neighbour cell |  | Config 1 | NR Cell 2 with CCA |  | NR Cell 2 is on NR RF channel number 2 with CCA. |
| DL CCA model |  | Config 1 | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  | Config 1 | As specified in clause A.3.26.2.2 |  |  |
| Gap Pattern Id |  | Config 1 | 0 |  | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1 | 9 |  |  |
| A3-Offset | dB | Config 1 | -6 |  |  |
| Hysteresis | dB | Config 1 | 0 |  |  |
| CP length |  | Config 1 | Normal |  |  |
| TimeToTrigger | s | Config 1 | 0 |  |  |
| Filter coefficient |  | Config 1 | 0 |  | L3 filtering is not used |
| DRX |  | Config 1 | DRX.1 | DRX.2 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | Config 1 | 3s |  | Synchronous cells. |
| T1 | s | Config 1 | 5 |  |  |
| T2 | s | Config 1 | 3 | 20 |  |

Table A.11.5.2.6.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1 | 1 |  | 2 |  |
| Duplex mode |  |  |  | Config 1 | TDD |  |  |  |
| TDD configuration |  |  |  | Config 1 | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  |  | MHz | Config 1 | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  |  | MHz | Config 1 | 40: NPRB,c = 106 |  |  |  |
| BWP configuration | Initial DL BWP |  | Config 1 | Config 1 | DLBWP.0.1 |  | NA |  |
|  | Initial UL BWP |  | Config 1 |  | ULBWP.0.1 |  | NA |  |
|  | Dedicated DL BWP |  | Config 1 |  | DLBWP.1.1 |  | NA |  |
|  | Dedicated UL BWP |  | Config 1 |  | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  |  | Config 1 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1 | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1 | CR.1.1 CCA |  |  |  |
| SSB parameters |  | Semi-static channel access Note 5,7 |  | Config 1 | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  |  |  |  |  |  |  |  |
|  |  | Semi-static channel access Note 5,7 |  | Config 1 | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  |  |  |  |  |  |  |  |
| DBT window configuration |  |  |  | Config 1 | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1 | SMTC.1 |  | SMTC.4 |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1 | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1 | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1 | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  |  | Config 1 | 2 |  | 2 |  |
| WCCA_DL |  |  | ms | Config 1 | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1 | 30 |  |  |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/9.36 MHz | Config 1 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  |  | Config 1 | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |

Table A.11.5.2.6.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value |  | Comment |
| --- | --- | --- | --- |
|  | Test 1 | Test 2 |  |
| drx-onDurationTimer | ms1 | ms1 | As specified in clause 6.3.2 in TS 38.331 [2] |
| drx-InactivityTimer | ms1 | ms1 |  |
| drx-RetransmissionTimerDL | sl1 | sl1 |  |
| drx-RetransmissionTimerUL | sl1 | sl1 |  |
| drx-LongCycleStartOffset | ms40 | Ms640 |  |
| shortDRX | disable | disable |  |

Table A.11.5.2.6.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value | Comment |
| --- | --- | --- |
| TimeAlignmentTimer | ms500 | As specified in clause 6.3.2 in TS 38.331 [2] |

##### A.11.5.2.6.2 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2, UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1, DRX cycle = 40 ms and for test 2, DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of

#### A.11.5.2.7 Event triggered reporting tests for FR1 without SSB time index detection when DRX is not used

##### A.11.5.2.7.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements for NR cell with CCA in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 with CCA as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.11.5.2.7.1-1, A.11.5.2.7.1-2 and A.11.5.2.7.1-3.

In this test, measurement gap pattern configuration # 0 as defined in table A.11.5.2.7.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

Table A.11.5.2.7.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1 with CCA

| Config | Description |
| --- | --- |
| 1 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.5.2.7.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1,2,3 | 1, 2 | Two FR1 NR carrier frequencies are used. NR channel 1 is with CCA. |
| Active cell |  | Config 1,2,3 | NR Cell 1 (PCell) | NR Cell 1 is on NR RF channel number 1 with CCA. |
| Neighbour cell |  | Config 1,2,3 | NR Cell 2 | NR Cell 2 is on NR RF channel number 2. |
| DL CCA model |  | Config 1,2,3 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | Config 1,2,3 | As specified in clause A.3.26.2.2 |  |
| Gap Pattern Id |  | Config 1,2,3 | 0 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2,3 | 9 |  |
| A3-Offset | dB | Config 1,2,3 | -6 |  |
| Hysteresis | dB | Config 1,2,3 | 0 |  |
| CP length |  | Config 1,2,3 | Normal |  |
| TimeToTrigger | s | Config 1,2,3 | 0 |  |
| Filter coefficient |  | Config 1,2,3 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2,3 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | Config 1,2,3 | 3 ms | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
|  |  | Config 1,2,3 | 3 s | Synchronous cells. |
| T1 | s | Config 1,2,3 | 5 |  |
| T2 | s | Config 1,2,3 | 1.7 |  |

Table A.11.5.2.7.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1,2,3 | 1 |  | 2 |  |
| Duplex mode |  |  |  | Config 1 | TDD |  | FDD |  |
|  |  |  |  | Config 2,3 | TDD |  | TDD |  |
| TDD configuration |  |  |  | Config 1 | TDDConf.1.1 CCA |  | Not Applicable |  |
|  |  |  |  | Config 2 | TDDConf.1.1 CCA |  | TDDConf.1.1 |  |
|  |  |  |  | Config 3 | TDDConf.1.1 CCA |  | TDDConf.2.1 |  |
| BWchannel |  |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP configuration | Initial DL BWP |  |  | Config 1,2,3 | DLBWP.0.1 |  | NA |  |
|  | Initial UL BWP |  |  |  | ULBWP.0.1 |  | NA |  |
|  | Dedicated DL BWP |  |  |  | DLBWP.1.1 |  | NA |  |
|  | Dedicated UL BWP |  |  |  | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  |  | Config 1,2,3 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1,2,3 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1,2,3 | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1,2,3 | CR.1.1 CCA |  |  |  |
| SSB parameters |  | Semi-static channel access Note 5,7 |  | Config 1,2 | SSB.1 CCA |  | SSB.1 FR1 |  |
|  |  |  |  | Config 3 | SSB.1 CCA |  | SSB.2 FR1 |  |
|  |  | Semi-static channel access Note 5,7 |  | Config 1,2 | SSB.2 CCA |  | SSB.1 FR1 |  |
|  |  |  |  | Config 3 | SSB.2 CCA |  | SSB.2 FR1 |  |
| DBT window configuration |  |  |  | Config 1,2,3 | As defined in A.3.28.1 |  | Not applicable |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1,2,3 | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1,2 | 30 |  | 15 |  |
|  |  |  |  | Config 3 | 30 |  | 30 |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | PCCA_DL=0.9375 |  | NA |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | NA |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | PCCA_UL=1 |  | NA |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | PCCA_UL=1 |  | NA |  |
| LCCA_DL |  |  |  | Config 1,2,3 | 12 |  | 12 |  |
| WCCA_DL |  |  | ms | Config 1,2,3 | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1,2,3 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1,2,3 | --98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1,2 | -95 |  | -98 |  |
|  |  |  |  | Config 3 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1,2 | -91 | -91 | -Infinity | -91 |
|  |  |  |  | Config 3 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1,2,3 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1,2,3 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/9.36 MHz | Config 1,2 | -58.49 | -58.49 | -70.05 | -62.26 |
|  |  |  | dBm/38.16 MHz | Config 3 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  |  | Config 1,2,3 | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |

##### A.11.5.2.7.2 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.11.5.2.8 Event triggered reporting tests for FR1 without SSB time index detection when DRX is used

##### A.11.5.2.8.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 with CCA as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.11.5.2.8.1-1, A.11.5.2.8.1-2 and A.11.5.2.8.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.11.5.2.8.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.11.5.2.8.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1 with CCA

| Config | Description |
| --- | --- |
| 1 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.5.2.8.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| NR RF Channel Number |  | Config 1,2,3 | 1, 2 |  | Two FR1 NR carrier frequencies are used. NR channel 1 is with CCA. |
| Active cell |  | Config 1,2,3 | NR Cell 1 (PCell) |  | NR Cell 1 is on NR RF channel number 1 with CCA. |
| Neighbour cell |  | Config 1,2,3 | NR Cell 2 |  | NR Cell 2 is on NR RF channel number 2. |
| DL CCA model |  | Config 1,2,3 | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  | Config 1,2,3 | As specified in clause A.3.26.2.2 |  |  |
| Gap Pattern Id |  | Config 1,2,3 | 0 |  | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2,3 | 9 |  |  |
| A3-Offset | dB | Config 1,2,3 | -6 |  |  |
| Hysteresis | dB | Config 1,2,3 | 0 |  |  |
| CP length |  | Config 1,2,3 | Normal |  |  |
| TimeToTrigger | s | Config 1,2,3 | 0 |  |  |
| Filter coefficient |  | Config 1,2,3 | 0 |  | L3 filtering is not used |
| DRX |  | Config 1,2,3 | DRX.1 | DRX.2 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | Config 1,2,3 | 3 ms |  | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
|  |  | Config 1,2,3 | 3s |  | Synchronous cells. |
| T1 | s | Config 1,2,3 | 5 |  |  |
| T2 | s | Config 1,2,3 | 2.5 | 17 |  |

Table A.11.5.2.8.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1,2,3 | 1 |  | 2 |  |
| Duplex mode |  |  |  | Config 1 | TDD |  | FDD |  |
|  |  |  |  | Config 2,3 | TDD |  | TDD |  |
| TDD configuration |  |  |  | Config 1 | TDDConf.1.1 CCA |  | Not Applicable |  |
|  |  |  |  | Config 2 | TDDConf.1.1 CCA |  | TDDConf.1.1 |  |
|  |  |  |  | Config 3 | TDDConf.1.1 CCA |  | TDDConf.2.1 |  |
| BWchannel |  |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP configuration | Initial DL BWP |  |  | Config 1,2,3 | DLBWP.0.1 |  | NA |  |
|  | Initial UL BWP |  |  |  | ULBWP.0.1 |  | NA |  |
|  | Dedicated DL BWP |  |  |  | DLBWP.1.1 |  | NA |  |
|  | Dedicated UL BWP |  |  |  | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  |  | Config 1,2,3 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1,2,3 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1,2,3 | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1,2,3 | CR.1.1 CCA |  |  |  |
| SSB parameters |  | Semi-static channel access Note 5,7 |  | Config 1,2 | SSB.1 CCA |  | SSB.1 FR1 |  |
|  |  |  |  | Config 3 | SSB.1 CCA |  | SSB.2 FR1 |  |
|  |  | Semi-static channel access Note 5,7 |  | Config 1,2 | SSB.2 CCA |  | SSB.1 FR1 |  |
|  |  |  |  | Config 3 | SSB.2 CCA |  | SSB.2 FR1 |  |
| DBT window configuration |  |  |  | Config 1,2,3 | As defined in A.3.28.1 |  | Not applicable |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1,2,3 | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1,2 | 30 |  | 15 |  |
|  |  |  |  | Config 3 | 30 |  | 30 |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | PCCA_DL=0.9375 |  | NA |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | NA |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | PCCA_UL=1 |  | NA |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | PCCA_UL=1 |  | NA |  |
| LCCA_DL |  |  |  | Config 1,2,3 | 5 |  | 5 |  |
| WCCA_DL |  |  | ms | Config 1,2,3 | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1,2,3 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1,2,3 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1,2 | -95 |  | -98 |  |
|  |  |  |  | Config 3 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1,2 | -91 | -91 | -Infinity | -91 |
|  |  |  |  | Config 3 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1,2,3 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1,2,3 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/9.36 MHz | Config 1,2 | -58.49 | -58.49 | -70.05 | -62.26 |
|  |  |  | dBm/38.16 MHz | Config 3 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  |  | Config 1,2,3 | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |

Table A.11.5.2.8.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value |  | Comment |
| --- | --- | --- | --- |
|  | Test 1 | Test 2 |  |
| drx-onDurationTimer | ms1 | ms1 | As specified in clause 6.3.2 in TS 38.331 [2] |
| drx-InactivityTimer | ms1 | ms1 |  |
| drx-RetransmissionTimerDL | sl1 | sl1 |  |
| drx-RetransmissionTimerUL | sl1 | sl1 |  |
| drx-LongCycleStartOffset | ms40 | Ms640 |  |
| shortDRX | disable | disable |  |

Table A.11.5.2.8.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value | Comment |
| --- | --- | --- |
| TimeAlignmentTimer | ms500 | As specified in clause 6.3.2 in TS 38.331 [2] |

##### A.11.5.2.8.2 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2, the UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1, DRX cycle = 40 ms and for test 2, DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.11.5.2.9 Event triggered reporting tests for FR1 with SSB time index detection when DRX is not used

##### A.11.5.2.9.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 with CCA as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.11.5.2.9.1-1, A.11.5.2.9.1-2 and A.11.5.2.9.1-3.

In this test, measurement gap pattern configuration # 0 as defined in table A.11.5.2.9.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

Table A.11.5.2.9.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1 with CCA

| Config | Description |
| --- | --- |
| 1 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.5.2.9.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1,2,3 | 1, 2 | Two FR1 NR carrier frequencies are used. NR channel 1 is with CCA. |
| Active cell |  | Config 1,2,3 | NR Cell 1 (PCell) | NR Cell 1 is on NR RF channel number 1 with CCA. |
| Neighbour cell |  | Config 1,2,3 | NR Cell 2 | NR Cell 2 is on NR RF channel number 2. |
| DL CCA model |  | Config 1,2,3 | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | Config 1,2,3 | As specified in clause A.3.26.2.2 |  |
| Gap Pattern Id |  | Config 1,2,3 | 0 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2,3 | 9 |  |
| A3-Offset | dB | Config 1,2,3 | -6 |  |
| Hysteresis | dB | Config 1,2,3 | 0 |  |
| CP length |  | Config 1,2,3 | Normal |  |
| TimeToTrigger | s | Config 1,2,3 | 0 |  |
| Filter coefficient |  | Config 1,2,3 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2,3 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | Config 1,2,3 | 3 ms | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
|  |  | Config 1,2,3 | 3s | Synchronous cells. |
| T1 | s | Config 1,2,3 | 5 |  |
| T2 | s | Config 1,2,3 | 2 |  |

Table A.11.5.2.9.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1,2,3 | 1 |  | 2 |  |
| Duplex mode |  |  |  | Config 1 | TDD |  | FDD |  |
|  |  |  |  | Config 2,3 | TDD |  | TDD |  |
| TDD configuration |  |  |  | Config 1 | TDDConf.1.1 CCA |  | Not Applicable |  |
|  |  |  |  | Config 2 | TDDConf.1.1 CCA |  | TDDConf.1.1 |  |
|  |  |  |  | Config 3 | TDDConf.1.1 CCA |  | TDDConf.2.1 |  |
| BWchannel |  |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP configuration | Initial DL BWP |  |  | Config 1,2,3 | DLBWP.0.1 |  | NA |  |
|  | Initial UL BWP |  |  |  | ULBWP.0.1 |  | NA |  |
|  | Dedicated DL BWP |  |  |  | DLBWP.1.1 |  | NA |  |
|  | Dedicated UL BWP |  |  |  | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  |  | Config 1,2,3 | TRS.1.2 TDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1,2,3 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1,2,3 | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1,2,3 | CR.1.1 CCA |  |  |  |
| SSB parameters |  | Semi-static channel access Note 5,7 |  | Config 1,2 | SSB.1 CCA |  | SSB.1 FR1 |  |
|  |  |  |  | Config 3 | SSB.1 CCA |  | SSB.2 FR1 |  |
|  |  | Semi-static channel access Note 5,7 |  | Config 1,2 | SSB.2 CCA |  | SSB.1 FR1 |  |
|  |  |  |  | Config 3 | SSB.2 CCA |  | SSB.2 FR1 |  |
| DBT window configuration |  |  |  | Config 1,2,3 | As defined in A.3.28.1 |  | Not applicable |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1,2,3 | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1,2 | 30 |  | 15 |  |
|  |  |  |  | Config 3 | 30 |  | 30 |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | PCCA_DL=0.9375 |  | NA |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | NA |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | PCCA_UL=1 |  | NA |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | PCCA_UL=1 |  | NA |  |
| LCCA_DL |  |  |  | Config 1,2,3 | 5 |  | 5 |  |
| WCCA_DL |  |  | ms | Config 1,2,3 | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1,2,3 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1,2,3 | -98 |  | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1,2 | -95 |  | -98 |  |
|  |  |  |  | Config 3 | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1,2 | -91 | -91 | -Infinity | -91 |
|  |  |  |  | Config 3 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1,2,3 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1,2,3 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/9.36 MHz | Config 1,2 | -58.49 | -58.49 | -70.05 | -62.26 |
|  |  |  | dBm/38.16 MHz | Config 3 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  |  | Config 1,2,3 | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |

##### A.11.5.2.9.2 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.11.5.2.10 Event triggered reporting tests for FR1 with SSB time index detection when DRX is used

##### A.11.5.2.10.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 with CCA as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.11.5.2.10.1-1, A.11.5.2.10.1-2 and A.11.5.2.10.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.11.5.2.10.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.11.5.2.10.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1 with CCA

| Config | Description |
| --- | --- |
| 1 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR cell without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.5.2.10.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| NR RF Channel Number |  | Config 1,2,3 | 1, 2 |  | Two FR1 NR carrier frequencies are used. NR channel 1 is with CCA. |
| Active cell |  | Config 1,2,3 | NR Cell 1 (PCell) |  | NR Cell 1 is on NR RF channel number 1 with CCA. |
| Neighbour cell |  | Config 1,2,3 | NR Cell 2 |  | NR Cell 2 is on NR RF channel number 2. |
| DL CCA model |  | Config 1,2,3 | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  | Config 1,2,3 | As specified in clause A.3.26.2.2 |  |  |
| Gap Pattern Id |  | Config 1,2,3 | 0 |  | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2,3 | 9 |  |  |
| A3-Offset | dB | Config 1,2,3 | -6 |  |  |
| Hysteresis | dB | Config 1,2,3 | 0 |  |  |
| CP length |  | Config 1,2,3 | Normal |  |  |
| TimeToTrigger | s | Config 1,2,3 | 0 |  |  |
| Filter coefficient |  | Config 1,2,3 | 0 |  | L3 filtering is not used |
| DRX |  | Config 1,2,3 | DRX.1 | DRX.2 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | Config 1,2,3 | 3 ms |  | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
|  |  | Config 1,2,3 | 3s |  | Synchronous cells. |
| T1 | s | Config 1,2,3 | 5 |  |  |
| T2 | s | Config 1,2,3 | 3 | 20 |  |

Table A.11.5.2.10.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

| Parameter |  |  | Unit | Test configuration | Cell 1 |  |  |  | Cell 2 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T3 | T4 | T1 | T2 | T3 | T4 |
| NR RF Channel Number |  |  |  | Config 1,2,3 | 1 |  |  |  | 2 |  |  |  |
| Duplex mode |  |  |  | Config 1 | TDD |  |  |  | FDD |  |  |  |
|  |  |  |  | Config 2,3 | TDD |  |  |  | TDD |  |  |  |
| TDD configuration |  |  |  | Config 1 | TDDConf.1.1 CCA |  |  |  | Not Applicable |  |  |  |
|  |  |  |  | Config 2 | TDDConf.1.1 CCA |  |  |  | TDDConf.1.1 |  |  |  |
|  |  |  |  | Config 3 | TDDConf.1.1 CCA |  |  |  | TDDConf.2.1 |  |  |  |
| BWchannel |  |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  |  |  | 10: NPRB,c = 52 |  |  |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  |  |  | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  |  | MHz | Config 1,2 | 40: NPRB,c = 106 |  |  |  | 10: NPRB,c = 52 |  |  |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  |  |  | 40: NPRB,c = 106 |  |  |  |
| BWP configuration | Initial DL BWP |  |  | Config 1,2,3 | DLBWP.0.1 |  |  |  | NA |  |  |  |
|  | Initial UL BWP |  |  |  | ULBWP.0.1 |  |  |  | NA |  |  |  |
|  | Dedicated DL BWP |  |  |  | DLBWP.1.1 |  |  |  | NA |  |  |  |
|  | Dedicated UL BWP |  |  |  | ULBWP.1.1 |  |  |  | NA |  |  |  |
| TRS configuration |  |  |  | Config 1,2,3 | TRS.1.2 TDD |  |  |  | NA |  |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1,2,3 | OP.1 |  |  |  | OP.1 |  |  |  |
| PDSCH Reference measurement channel |  |  |  | Config 1,2,3 | SR.1.1 CCA |  |  |  |  |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1,2,3 | CR.1.1 CCA |  |  |  |  |  |  |  |
| SSB parameters |  | Semi-static channel access Note 5,7 |  | Config 1,2 | SSB.1 CCA |  |  |  | SSB.1 FR1 |  |  |  |
|  |  |  |  | Config 3 | SSB.1 CCA |  |  |  | SSB.2 FR1 |  |  |  |
|  |  | Semi-static channel access Note 5,7 |  | Config 1,2 | SSB.2 CCA |  |  |  | SSB.1 FR1 |  |  |  |
|  |  |  |  | Config 3 | SSB.2 CCA |  |  |  | SSB.2 FR1 |  |  |  |
| DBT window configuration |  |  |  | Config 1,2,3 | As defined in A.3.28.1 |  |  |  | Not applicable |  |  |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1,2,3 | SMTC.1 |  |  |  | SMTC.4 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1,2 | 30 |  |  |  | 15 |  |  |  |
|  |  |  |  | Config 3 | 30 |  |  |  | 30 |  |  |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | PCCA_DL=0.9375 |  |  |  | NA |  |  |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |  | NA |  |  |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | PCCA_UL=1 |  |  |  | NA |  |  |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | PCCA_UL=1 |  |  |  | NA |  |  |  |
| LCCA_DL |  |  |  | Config 1,2,3 | 2 |  |  |  | 2 |  |  |  |
| WCCA_DL |  |  | ms | Config 1,2,3 | TPSS/SSS_sync_inter_cca |  |  |  | TPSS/SSS_sync_inter_cca |  |  |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1,2,3 | 0 |  |  |  | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1,2,3 | -98 |  |  |  | -98 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1,2 | -95 |  |  |  | -98 |  |  |  |
|  |  |  |  | Config 3 | -95 |  |  |  | -95 |  |  |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1,2 | -91 |  | -91 |  | -Infinity |  | -91 |  |
|  |  |  |  | Config 3 | -91 |  | -91 |  | -Infinity |  | -88 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1,2,3 | 4 |  | 4 |  | -Infinity |  | 7 |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1,2,3 | 4 |  | 4 |  | -Infinity |  | 7 |  |
| IoNote3 |  |  | dBm/9.36 MHz | Config 1,2 | -58.49 |  | -58.49 |  | -70.05 |  | -62.26 |  |
|  |  |  | dBm/38.16 MHz | Config 3 | -58.49 |  | -58.49 |  | -63.94 |  | -56.15 |  |
| Propagation Condition |  |  |  | Config 1,2,3 | AWGN |  |  |  | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. . For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |  |  |  |  |

Table A.11.5.2.10.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value |  | Comment |
| --- | --- | --- | --- |
|  | Test 1 | Test 2 |  |
| drx-onDurationTimer | ms1 | ms1 | As specified in clause 6.3.2 in TS 38.331 [2] |
| drx-InactivityTimer | ms1 | ms1 |  |
| drx-RetransmissionTimerDL | sl1 | sl1 |  |
| drx-RetransmissionTimerUL | sl1 | sl1 |  |
| drx-LongCycleStartOffset | ms40 | Ms640 |  |
| shortDRX | disable | disable |  |

Table A.11.5.2.10.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value | Comment |
| --- | --- | --- |
| TimeAlignmentTimer | ms500 | As specified in clause 6.3.2 in TS 38.331 [2] |

##### A.11.5.2.10.2 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2, the UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1, DRX cycle = 40 ms and for test 2, DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

### A.11.5.3 Inter-RAT E-UTRAN measurements

#### A.11.5.3.1 SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1

##### A.11.5.3.1.1 Test Purpose and Environment

The purpose of this set of tests is to verify that the UE makes correct event-triggered reporting of inter-RAT E-UTRAN measurements when operating in standalone (SA) operation with PCell in FR1. This test shall partly verify the cell search and measurement requirements in clauses 9.4.2 and 9.4.3.

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell on a frequency carrier with CCA and Cell 2 is an inter-RAT E-UTRAN inter-RAT neighbour cell. In the measurement control information from the PCell it is indictated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

Supported test configurations are shown in table A.11.5.3.1.1-1. General test parameters are provided in table A.11.5.3.1.1-2 below. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.11.5.3.1.1-3 and A.11.5.3.1.1-4, respectively.

Table A.11.5.3.1.1-1: Supported test configurations in SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

| Configuration | Description |
| --- | --- |
| 1 | NR with CCA 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode, LTE FDD |
| 2 | NR with CCA 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode, LTE TDD |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.5.3.1.1-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | 1 NR carrier frequency is used in the test |
| LTE RF Channel Number |  | 1 | 1 LTE carrier frequency is used in the test |
| Channel Bandwidth | MHz | As specified in tables A.11.5.3.1.1-2 and A.11.5.3.1.1-3. |  |
| Active cell |  | Cell 1 | Cell 1 is on RF channel number 1 |
| Neighbour cell |  | Cell 2 | Cell 2 is on RF channel number 2 |
| Gap Pattern Id |  | 0 | As specified in clauseTable 9.1.2-1. Per-UE gap pattern. |
| NR measurement quantity |  | SS-RSRP | Measurement quantity for Cell 1 |
| Inter-RAT E-UTRAN measurement quantity |  | RSRP | Measurement quantity for Cell 2 |
| b2-Threshold1 | dBm | Note 1 | SS-RSRP threshold for SS-RSRP measurement on Cell 1 for event B2 |
| b2-Threshold2EUTRA | dBm | -95 | E-UTRAN RSRP threshold for SS-RSRP measurement on Cell 1 for event B2 |
| Hysteresis | dB | 0 |  |
| TimeToTrigger | s | 0 |  |
| Filter coefficient |  | 0 | L3 filtering is not used |
| DRX |  | OFF | OFF |
| T1 | s | 5 |  |
| T2 | s | 5 |  |
| NOTE 1: Values are defined in table A.11.5.3.1.1-3 |  |  |  |

Table A.11.5.3.1.1-3: PCell specific test parameters for SA inter-RAT E-UTRA event triggered reporting in non-DRX with PCell in FR1

| Parameter | Unit | Test configuration | Cell 1 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |  |
| NR RF Channel Number |  | 1, 2 | 1 |  |  |
| TDD configuration |  | 1, 2 | TDDConf.1.1 CCA |  |  |
| BWchannel | MHz | 1, 2 | 40: NPRB,c = 106 |  |  |
| PCCA_DL for dynamic channel access Note 6,8 |  | 1, 2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |
| PCCA_DL for semi-static channel access Note 7,8 |  | 1, 2 | PCCA_DL=0.9375 |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  | 1, 2 | OP.1 |  |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  | 1, 2 | SMTC.1 |  |  |
| DBT window configuration |  | 1, 2 | DBT.1 |  |  |
| SSB configuration  for semi-static channel access |  | 1, 2 | SSB.1 CCA |  |  |
| SSB configuration for dynamic channel access |  | 1, 2 | SSB.2 CCA |  |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2 | 30 |  |  |
| b2-Threshold1 | dBm | 1 | -96 |  |  |
|  |  | 2 | -93 |  |  |
| EPRE ratio of PSS to SSS |  | 1, 2 | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1, 2 | -106 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1, 2 | -103 |  |  |
| SS-RSRP Note 3,5 | dBm/SCS | 1, 2 | -85 |  | -105 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] Note 5 | dB | 1, 2 | 18 |  | -2 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] Note 5 | dB | 1, 2 | 18 |  | -2 |
| IoNote3 | dBm/38.16 MHz | 1, 2 | -53.88 |  | -69.82 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2 | 1x2 Low |  |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.11.5.3.1.1-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

| Parameter | Unit | Configuration | Cell 2 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1,2 | 1 |  |
| Duplex mode |  | 1 | FDD |  |
|  |  | 2 | TDD |  |
| TDD special subframe configurationNote1 |  | 2 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 2 | 1 |  |
| BWchannel | MHz | 1,2 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 2 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 2 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote2 |  | 1 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 2 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| PBCH_RA | dB | 1, 2 | 0 |  |
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
| NocNote4 | dBm/15 kHz | 1, 2 | -104 |  |
| Ês/Noc | dB | 1, 2 | -Infinity | 17 |
| Ês/IotNote5 | dB | 1, 2 | -Infinity | 17 |
| RSRPNote5 | dBm/15 kHz | 1, 2 | -Infinity | -87 |
| SCH_RPNote5 | dBm/15 kHz | 1, 2 | -Infinity | -87 |
| IoNote5 | dBm/9 MHz | 1, 2 | -73.21+10log (NPRB,c /50) | -56.12+10log (NPRB,c /50) |
| Propagation Condition |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2 | 1x2 |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |

##### A.11.5.3.1.2 Test Requirements

The UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 3.84 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.11.5.3.2 SA NR - E-UTRAN event-triggered reporting in DRX in FR1

##### A.11.5.3.2.1 Test Purpose and Environment

The purpose of this set of tests is to verify that the UE makes correct event-triggered reporting of inter-RAT E-UTRAN measurements when operating in standalone (SA) operation with PCell in FR1 when DRX is used. This test shall partly verify the cell search and measurement requirements in clauses 9.4.2 and 9.4.3. There are two test cases. In test 1 the UE shall be configured with DRX cycle of 40 ms. In test 2 the UE shall be configured with DRX cycle of 640 ms.

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell with CCA and Cell 2 is an inter-RAT E-UTRAN inter-RAT neighbour cell. In the measurement control information from the PCell it is indctated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

In each test the UE shall be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, the UE shall be allocated with PUSCH resource at every DRX cycle.

Supported test configurations are shown in table A.11.5.3.2.1-1. General test parameters are provided in table A.11.5.3.2.1-2 below. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.11.5.3.2.1-3 and A.11.5.3.2.1-4, respectively.

Table A.11.5.3.2.1-1: Supported test configurations in SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

| Configuration | Description |
| --- | --- |
| 1 | NR with CCA 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode, LTE FDD |
| 2 | NR with CCA 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode, LTE TDD |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.5.3.2.1-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

| Parameter | Unit | Test 1 | Test 2 | Comment |
| --- | --- | --- | --- | --- |
|  |  | Value |  |  |
| NR RF Channel Number |  | 1 |  | 1 NR carrier frequency is used in the test |
| LTE RF Channel Number |  | 2 |  | 1 LTE carrier frequency is used in the test |
| Channel Bandwidth | MHz | As specified in tables A.11.5.3.2.1-2 and A.11.5.3.2.1-3. |  |  |
| Active cell |  | Cell 1 |  | Cell 1 is on RF channel number 1 |
| Neighbour cell |  | Cell 2 |  | Cell 2 is on RF channel number 2 |
| Gap Pattern Id |  | 0 |  | As specified in clauseTable 9.1.2-1. Per-UE gap pattern. |
| NR measurement quantity |  | SS-RSRP |  | Measurement quantity for Cell 1 |
| Inter-RAT E-UTRAN measurement quantity |  | RSRP |  | Measurement quantity for Cell 2 |
| b2-Threshold1 | dBm | Note 1 |  | SS-RSRP threshold for SS-RSRP measurement on Cell 1 for event B2 |
| b2-Threshold2EUTRA | dBm | -95 |  | E-UTRAN RSRP threshold for SS-RSRP measurement on Cell 1 for event B2 |
| Hysteresis | dB | 0 |  |  |
| TimeToTrigger | s | 0 |  |  |
| Filter coefficient |  | 0 |  | L3 filtering is not used |
| DRX |  | DRX.1 | DRX.7 | DRX cycle configurations DRX.1 and DRX.7 are defined in table A.3.3.1-1 and table A.3.3.7-1 respectively. |
| T1 | s | 5 |  |  |
| T2 | s | 5 | 15 |  |
| NOTE 1: Values are defined in table A.11.5.3.2.1-3 |  |  |  |  |

Table A.11.5.3.2.1-3: PCell specific test parameters for SA inter-RAT E-UTRA event triggered reporting in DRX with PCell in FR1

| Parameter | Unit | Test configuration | Cell 1 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |  |
| NR RF Channel Number |  | 1, 2 | 1 |  |  |
| TDD configuration |  | 1, 2 | TDDConf.1.1 CCA |  |  |
| BWchannel | MHz | 1, 2 | 40: NPRB,c = 106 |  |  |
| PCCA_DL for dynamic channel access Note 6,8 |  | 1, 2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |
| PCCA_DL for semi-static channel access Note 7,8 |  | 1, 2 | PCCA_DL=0.9375 |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  | 1, 2 | OP.1 |  |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  | 1, 2 | SMTC.1 |  |  |
| DBT window configuration |  | 1, 2 | DBT.1 |  |  |
| SSB configuration  for semi-static channel access |  | 1, 2 | SSB.1 CCA |  |  |
| SSB configuration for dynamic channel access |  | 1, 2 | SSB.2 CCA |  |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2 | 30 |  |  |
| b2-Threshold1 | dBm | 1 | -96 |  |  |
|  |  | 2 | -93 |  |  |
| EPRE ratio of PSS to SSS |  | 1, 2 | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1, 2 | -106 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1, 2 | -103 |  |  |
| SS-RSRP Note 3,5 | dBm/SCS | 1, 2 | -85 |  | -105 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] Note 5 | dB | 1, 2 | 18 |  | -2 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] Note 5 | dB | 1, 2 | 18 |  | -2 |
| IoNote3 | dBm/38.16 MHz | 1, 2 | -53.88 |  | -69.82 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2 | 1x2 Low |  |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5:  The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8:  For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.11.5.3.2.1-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

| Parameter | Unit | Configuration | Cell 2 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1,2 | 1 |  |
| Duplex mode |  | 1 | FDD |  |
|  |  | 2 | TDD |  |
| TDD special subframe configurationNote1 |  | 2 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 2 | 1 |  |
| BWchannel | MHz | 1,2 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 2 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 2 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote2 |  | 1 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 2 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| PBCH_RA | dB | 1, 2 | 0 |  |
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
| NocNote4 | dBm/15 kHz | 1, 2 | -104 |  |
| Ês/Noc | dB | 1, 2 | -Infinity | 17 |
| Ês/IotNote5 | dB | 1, 2 | -Infinity | 17 |
| RSRPNote5 | dBm/15 kHz | 1, 2 | -Infinity | -87 |
| SCH_RPNote5 | dBm/15 kHz | 1, 2 | -Infinity | -87 |
| IoNote5 | dBm/9 MHz | 1, 2 | -73.21+10log (NPRB,c /50) | -56.12+10log (NPRB,c /50) |
| Propagation Condition |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2 | 1x2 |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |

##### A.11.5.3.2.2 Test Requirements

In test 1, the UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 3.84 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

In test 2, the UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 12.8 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

### A.11.5.4 L1-RSRP measurements for beam reporting

#### A.11.5.4.1 SSB based L1-RSRP measurement when DRX is not used

##### A.11.5.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.11.5.4.1.1-1.

Table A.11.5.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | With CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

##### A.11.5.4.1.2 Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). Cell 1 operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The test parameters for the Cell 1 are given in table A.11.5.4.1.2-1 and table A.11.5.4.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.11.5.4.1.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB ARFCN | 1 |  | freq1 |
| DL CCA model | 1 |  | As specifieed in A.3.20.2.1 |
| UL CCA model | 1 |  | As specified in A.3.20.2.2 |
| Duplex mode | 1 |  | TDD |
| TDD Configuration | 1 |  | TDDConf.1.1 CCA |
| BWchannel | 1 | MHz | 40: NPRB,c = 106 |
| PDSCH Reference measurement channel | 1 |  | SR.1.1 CCA |
| RMSI CORESET Reference Channel | 1 |  | CR.1.1 CCA |
| Dedicated CORESET Reference Channel | 1 |  | CCR.1.1 CCA |
| SSB configuration | 1 |  | SSB.3 CCA for semi-static channel accessSSB.4 CCA for dynamic channel access |
| OCNG Patterns | 1 |  | OP.1 |
| Initial BWP Configuration | 1 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1 |  | DLBWP.1.1ULBWP.1.1 |
| DBT Window Configuration | 1 |  | DBT.1 |
| TRS Configuration | 1 |  | TRS.1.2 TDD |
| DRX configuration | 1 |  | Off |
| reportConfigType | 1 |  | periodic |
| reportQuantity | 1 |  | ssb-Index-RSRP |
| Number of reported RS | 1 |  | 2 |
| L1-RSRP reporting period | 1 | slot | 80 |
| T1 | 1 | s | 5 |
| T2 | 1 | s | 1 |
| EPRE ratio of PSS to SSS | 1 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1 |  | AWGN |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window. |  |  |  |

Table A.11.5.4.1.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| DL CCA Probability PCCA_DL Note 4,6 | 1 |  | 0.9375 | 0.9375 | 0.9375 | 0.9375 |
| DL CCA Probability PCCA_DL Note 4.7 | 1 |  | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 |
| UL CCA probability PCCA_UL | 1 |  | 1.0 | 1.0 | 1.0 | 1.0 |
| Note2 | 1 | dBm/15 kHz | -94.65 |  |  |  |
| Note2 | 1 | dBm/SSB SCS | -91.65 |  |  |  |
|  | 1 | dB | 0 | 0 | -Infinity | 3 |
| SSB RSRP Note3 | 1 | dBm/SSB SCS | -91.65 | -91.65 | -Infinity | -88.65 |
| Io Note3 | 1 | dBm/38.16 MHz | -57.59 | -57.59 | -60.61 | -55.84 |
|  | 1 | dB | 0 | 0 | -Infinity | 3 |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: DL and UL CCA probabilities apply for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.NOTE 5: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2. |  |  |  |  |  |  |

##### A.11.5.4.1.3 Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.11.5.4.2 SSB based L1-RSRP measurement when DRX is used

##### A.11.5.4.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.11.5.4.2.1-1.

Table A.11.5.4.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | With CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

##### A.11.5.4.2.2 Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). Cell 1 operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The test parameters for the Cell 1 are given in table A.11.5.4.2.2-1 and table A.11.5.4.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.11.5.4.2.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB ARFCN | 1 |  | freq1 |
| DL CCA model | 1 |  | As specifieed in A.3.20.2.1 |
| UL CCA model | 1 |  | As specified in A.3.20.2.2 |
| Duplex mode | 1 |  | TDD |
| TDD Configuration | 1 |  | TDDConf.1.1 CCA |
| BWchannel | 1 | MHz | 40: NPRB,c = 106 |
| PDSCH Reference measurement channel | 1 |  | SR.1.1 CCA |
| RMSI CORESET Reference Channel | 1 |  | CR.1.1 CCA |
| Dedicated CORESET Reference Channel | 1 |  | CCR.1.1 CCA |
| SSB configuration | 1 |  | SSB.3 CCA for semi-static channel accessSSB.4 CCA for dynamic channel access |
| OCNG Patterns | 1 |  | OP.1 |
| Initial BWP Configuration | 1 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1 |  | DLBWP.1.1ULBWP.1.1 |
| DBT Window Configuration | 1 |  | DBT.1 |
| TRS Configuration | 1 |  | TRS.1.2 TDD |
| DRX configuration | 1 |  | DRX.3 |
| reportConfigType | 1 |  | periodic |
| reportQuantity | 1 |  | ssb-Index-RSRP |
| Number of reported RS | 1 |  | 2 |
| L1-RSRP reporting period | 1 | slot | 80 |
| T1 | 1 | s | 5 |
| T2 | 1 | s | 1 |
| EPRE ratio of PSS to SSS | 1 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1 |  | AWGN |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window. |  |  |  |

Table A.11.5.4.2.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| DL CCA Probability PCCA_DL Note 4,6 | 1 |  | 0.9375 | 0.9375 | 0.9375 | 0.9375 |
| DL CCA Probability PCCA_DL Note 4.7 | 1 |  | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 |
| UL CCA probability PCCA_UL | 1 |  | 1.0 | 1.0 | 1.0 | 1.0 |
| Note2 | 1 | dBm/15 kHz | -94.65 |  |  |  |
| Note2 | 1 | dBm/SSB SCS | -91.65 |  |  |  |
|  | 1 | dB | 0 | 0 | -Infinity | 3 |
| SSB RSRP Note3 | 1 | dBm/SSB SCS | -91.65 | -91.65 | -Infinity | -88.65 |
| Io Note3 | 1 | dBm/38.16 MHz | -57.59 | -57.59 | -60.61 | -55.84 |
|  | 1 | dB | 0 | 0 | -Infinity | 3 |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: DL and UL CCA probabilities apply for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.NOTE 5: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2. |  |  |  |  |  |  |

##### A.11.5.4.2.3 Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.11.5.4.3 SSB based L1-RSRP measurement on SCC when DRX is not used

##### A.11.5.4.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.11.5.4.3.1-1.

Table A.11.5.4.3.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | With CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

##### A.11.5.4.3.2 Test parameters

There are two cells in the test, the FR1 PCell (Cell 1) and FR1 SCell (Cell 2). Both Cell 1 and Cell 2 operate on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The test parameters for the Cell 1 are given in table A.11.5.4.3.2-1 and table A.11.5.4.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.11.5.4.3.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| Active PCell | 1 |  | Cell 1 |
| Active SCell | 1 |  | Cell 2 |
| RF Channel Number | 1 |  | 1: Cell 12: Cell 2 |
| DL CCA model | 1 |  | As specifieed in A.3.20.2.1 |
| UL CCA model | 1 |  | As specified in A.3.20.2.2 |
| Duplex mode | 1 |  | TDD |
| TDD Configuration | 1 |  | TDDConf.1.1 CCA |
| BWchannel | 1 | MHz | 40: NPRB,c = 106 |
| PDSCH Reference measurement channel | 1 |  | SR.1.1 CCA |
| RMSI CORESET Reference Channel | 1 |  | CR.1.1 CCA |
| Dedicated CORESET Reference Channel | 1 |  | CCR.1.1 CCA |
| SSB configuration | 1 |  | SSB.3 CCA for semi-static channel accessSSB.4 CCA for dynamic channel access |
| OCNG Patterns | 1 |  | OP.1 |
| Initial BWP Configuration | 1 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1 |  | DLBWP.1.1ULBWP.1.1 |
| DBT Window Configuration | 1 |  | DBT.1 |
| TRS Configuration | 1 |  | TRS.1.2 TDD |
| DRX configuration | 1 |  | Off |
| reportConfigType | 1 |  | periodic |
| reportQuantity | 1 |  | ssb-Index-RSRP |
| Number of reported RS | 1 |  | 2 |
| L1-RSRP reporting period | 1 | slot | 80 |
| T1 | 1 | s | 5 |
| T2 | 1 | s | 1 |
| EPRE ratio of PSS to SSS | 1 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1 |  | AWGN |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window. |  |  |  |

Table A.11.5.4.3.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |  |
| DL CCA Probability PCCA_DL Note 4,6 | 1 |  | 0.9375 | 0.9375 | 0.9375 | 0.9375 |  |
| DL CCA Probability PCCA_DL Note 4.7 | 1 |  | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 |  |
| UL CCA probability PCCA_UL | 1 |  | 1.0 | 1.0 | 1.0 | 1.0 |  |
| Note2 | 1 | dBm/15 kHz | -94.65 |  |  |  |  |
| Note2 | 1 | dBm/SSB SCS | -91.65 |  |  |  |  |
|  | 1 | dB | 0 | 0 | -Infinity | 3 |  |
| SSB RSRP Note3 | 1 | dBm/SSB SCS | -91.65 | -91.65 | -Infinity | -88.65 |  |
| Io Note3 | 1 | dBm/38.16 MHz | -57.59 | -57.59 | -60.61 | -55.84 |  |
|  | 1 | dB | 0 | 0 | -Infinity | 3 |  |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: DL and UL CCA probabilities apply for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.NOTE 5: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2. |  |  |  |  |  |  |  |

##### A.11.5.4.3.3 Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 2.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.11.5.4.4 SSB based L1-RSRP measurement on SCC when DRX is used

##### A.11.5.4.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.11.5.4.4.1-1.

Table A.11.5.4.4.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | With CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

##### A.11.5.4.4.2 Test parameters

There are two cells in the test, the FR1 PCell (Cell 1) and FR1 SCell (Cell 2). Both Cell 1 and Cell 2 operate on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The test parameters for the Cell 1 are given in table A.11.5.4.4.2-1 and table A.11.5.4.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.11.5.4.4.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| Active PCell | 1 |  | Cell 1 |
| Active SCell | 1 |  | Cell 2 |
| RF Channel Number | 1 |  | 1: Cell 12: Cell 2 |
| DL CCA model | 1 |  | As specifieed in A.3.20.2.1 |
| UL CCA model | 1 |  | As specified in A.3.20.2.2 |
| Duplex mode | 1 |  | TDD |
| TDD Configuration | 1 |  | TDDConf.1.1 CCA |
| BWchannel | 1 | MHz | 40: NPRB,c = 106 |
| PDSCH Reference measurement channel | 1 |  | SR.1.1 CCA |
| RMSI CORESET Reference Channel | 1 |  | CR.1.1 CCA |
| Dedicated CORESET Reference Channel | 1 |  | CCR.1.1 CCA |
| SSB configuration | 1 |  | SSB.3 CCA for semi-static channel accessSSB.4 CCA for dynamic channel access |
| OCNG Patterns | 1 |  | OP.1 |
| Initial BWP Configuration | 1 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1 |  | DLBWP.1.1ULBWP.1.1 |
| DBT Window Configuration | 1 |  | DBT.1 |
| TRS Configuration | 1 |  | TRS.1.2 TDD |
| DRX configuration | 1 |  | DRX.3 |
| reportConfigType | 1 |  | periodic |
| reportQuantity | 1 |  | ssb-Index-RSRP |
| Number of reported RS | 1 |  | 2 |
| L1-RSRP reporting period | 1 | slot | 80 |
| T1 | 1 | s | 5 |
| T2 | 1 | s | 1 |
| EPRE ratio of PSS to SSS | 1 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1 |  | AWGN |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window. |  |  |  |

Table A.11.5.4.4.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |  |
| DL CCA Probability PCCA_DL Note 4,6 | 1 |  | 0.9375 | 0.9375 | 0.9375 | 0.9375 |  |
| DL CCA Probability PCCA_DL Note 4.7 | 1 |  | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 |  |
| UL CCA probability PCCA_UL | 1 |  | 1.0 | 1.0 | 1.0 | 1.0 |  |
| Note2 | 1 | dBm/15 kHz | -94.65 |  |  |  |  |
| Note2 | 1 | dBm/SSB SCS | -91.65 |  |  |  |  |
|  | 1 | dB | 0 | 0 | -Infinity | 3 |  |
| SSB RSRP Note3 | 1 | dBm/SSB SCS | -91.65 | -91.65 | -Infinity | -88.65 |  |
| Io Note3 | 1 | dBm/38.16 MHz | -57.59 | -57.59 | -60.61 | -55.84 |  |
|  | 1 | dB | 0 | 0 | -Infinity | 3 |  |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: DL and UL CCA probabilities apply for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.NOTE 5: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2. |  |  |  |  |  |  |  |

##### A.11.5.4.4.3 Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 2.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.11.6 Measurement performance

### A.11.6.1 SS-RSRP

#### A.11.6.1.1 Intra-frequency measurement accuracy on a carrier frequency with CCA

##### A.11.6.1.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy on the carrier frequency with CCA is within the specified limits. This test will verify the requirements in clauses 10.1.36.1.1 and 10.1.36.1.2 for intra-frequency measurements under CCA.

##### A.11.6.1.1.2 Test parameters

In this set of test cases all cells are on the same carrier frequency with CCA and transmit SSBs in DBT windows according to DL CCA model. Supported test configurations are shown in table A.11.6.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.11.6.1.1.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

Table A.11.6.1.1.2-1: SS-RSRP  Intra frequency SS-RSRP supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

Table A.11.6.1.1.2-2: SS-RSRP Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Cell ID |  |  |  | 489 | 0 | 489 | 0 | 489 | 0 |
| SSB ARFCN |  |  |  | freq1 |  | freq1 |  | freq1 |  |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |  |  |  |  |
| BWchannel |  | Config 1 | MHz | 40: NPRB,c = 106 |  |  |  |  |  |
| BWP BW |  | Config 1 |  | 40: NPRB,c = 106 |  |  |  |  |  |
| DL CCA model |  |  |  | As specified in clause A.3.26.2.1 |  |  |  |  |  |
| UL CCA model |  |  |  | As specified in clause A.3.26.2.2 |  |  |  |  |  |
| PCCA_DL for dynamic channel access Note 7,9 |  |  |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |  |  |  |
| PCCA_DL for semi-static channel access Note 8,9 |  |  |  | PCCA_DL=0.9375 |  |  |  |  |  |
| PCCA_UL |  |  |  | 1 |  |  |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |  |  |
| TRS configuration |  | Config 1 |  | TRS.1.2 TDD | NA | TRS.1.2 TDD | NA | TRS.1.2 TDD | NA |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 CCA | - | SR.1.1 CCA | - | SR.1.1 CCA | - |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA | - | CR.1.1 CCA | - | CR.1.1 CCA | - |
| Control channel RMC |  | Config 1 |  | CR.1.1 CCA | - | CR.1.1 CCA | - | CR.1.1 CCA | - |
| SSB configuration for semi-static channel access |  | Config 1 |  | SSB.1 CCA | SSB.1 CCA | SSB.1 CCA | SSB.1 CCA | SSB.1 CCA | SSB.1 CCA |
| SSB configuration for dynamic channel access |  | Config 1 |  | SSB.2 CCA | SSB.2 CCA | SSB.2 CCA | SSB.2 CCA | SSB.2 CCA | SSB.2 CCA |
| DBT window configuration |  | Config 1,2,3 |  | DBT.1 | DBT.1 | DBT.1 | DBT.1 | DBT.1 | DBT.1 |
| Time offset with Cell 1 |  | Config 1 | s | - | 3 | - | 3 | - | 3 |
| SMTC configuration |  | Config 1 |  | SMTC.1 |  |  |  |  |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 | kHz | 30 kHz |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 | NR_CCA_FR1_I |  | Not applicableNote 5 |  | -94 |  | -110 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -109.5 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 | NR_CCA_FR1_I | dBm/SCS | Not applicableNote 5 |  | -91 |  | -107.0 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -106.5 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] Note6 |  |  | dB | 2.46 | -5.97 | 2.46 | -5.97 | -2.01 | -3.54 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] Note6 |  |  | dB | 6 | 1 | 6 | 1 | 1 | 0 |
| SS-RSRPNote3,6 | Config 1 | NR_CCA_FR1_I | dBm/SCS | Not applicableNote 5 | Not applicableNote 5 | -85 | -90 | -106.00 | -107.00 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -105.50 | -106.50 |
| IoNote3 | Config 1 | NR_CCA_FR1_I | dBm/38.16 MHz | Not applicableNote 5- |  | -51.99 |  | -70.82 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -70.32 |  |
| Propagation condition |  |  | - | AWGN |  |  |  |  |  |
| Antenna configuration |  |  |  | 1x2 |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Subtest 1 is not used when testing with 30 kHz SSB SCS.NOTE 6: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 9: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |  |  |

##### A.11.6.1.1.3 Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.36.1.1 and relative requirement in clause 10.1.36.1.2.

#### A.11.6.1.2 Intra-frequency measurement accuracy on SCC on a carrier frequency with CCA

##### A.11.6.1.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy on the carrier frequency with CCA is within the specified limits. This test will verify the requirements in clauses 10.1.36.1.1 and 10.1.36.1.2 for intra-frequency measurements under CCA.

##### A.11.6.1.2.2 Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1) on the carrier frequency with CCA, and two cells on the same carrier frequency with CCA and transmit SSBs in DBT windows according to DL CCA model: SCell (Cell 2) and a neighbour cell (Cell 3).  Supported test configurations are shown in table A.11.6.1.2.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.11.6.1.2.2-2.

Table A.11.6.1.2.2-1: SS-RSRP  Intra frequency SS-RSRP supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

Table A.11.6.1.2.2-2: SS-RSRP Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 | Cell 3 | Cell 2 | Cell 3 | Cell 2 | Cell 3 |
| Cell ID |  |  |  | 489 | 0 | 489 | 0 | 489 | 0 |
| SSB ARFCN |  |  |  | freq1 |  | freq1 |  | freq1 |  |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |  |  |  |  |
| BWchannel |  | Config 1 | MHz | 40: NPRB,c = 106 |  |  |  |  |  |
| BWP BW |  | Config 1 |  | 40: NPRB,c = 106 |  |  |  |  |  |
| DL CCA model |  |  |  | As specified in clause A.3.26.2.1 |  |  |  |  |  |
| UL CCA model |  |  |  | As specified in clause A.3.26.2.2 |  |  |  |  |  |
| PCCA_DL for dynamic channel access Note 7,9 |  |  |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |  |  |  |
| PCCA_DL for semi-static channel access Note 8,9 |  |  |  | PCCA_DL=0.9375 |  |  |  |  |  |
| PCCA_UL |  |  |  | 1 |  |  |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |  |  |
| TRS configuration |  | Config 1 |  | TRS.1.2 TDD | NA | TRS.1.2 TDD | NA | TRS.1.2 TDD | NA |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 CCA | - | SR.1.1 CCA | - | SR.1.1 CCA | - |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA | - | CR.1.1 CCA | - | CR.1.1 CCA | - |
| Control channel RMC |  | Config 1 |  | CR.1.1 CCA | - | CR.1.1 CCA | - | CR.1.1 CCA | - |
| SSB configuration for semi-static channel access |  | Config 1 |  | SSB.1 CCA | SSB.1 CCA | SSB.1 CCA | SSB.1 CCA | SSB.1 CCA | SSB.1 CCA |
| SSB configuration for dynamic channel access |  | Config 1 |  | SSB.2 CCA | SSB.2 CCA | SSB.2 CCA | SSB.2 CCA | SSB.2 CCA | SSB.2 CCA |
| DBT window configuration |  | Config 1,2,3 |  | DBT.1 | DBT.1 | DBT.1 | DBT.1 | DBT.1 | DBT.1 |
| Time offset with Cell 1 |  | Config 1 | s | - | 3 | - | 3 | - | 3 |
| SMTC configuration |  | Config 1 |  | SMTC.1 |  |  |  |  |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 | kHz | 30 kHz |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 | NR_CCA_FR1_I |  | Not applicableNote 5 |  | -94 |  | -110 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -109.5 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 | NR_CCA_FR1_I | dBm/SCS | Not applicableNote 5 |  | -91 |  | -107.0 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -106.5 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] Note6 |  |  | dB | 2.46 | -5.97 | 2.46 | -5.97 | -2.01 | -3.54 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] Note6 |  |  | dB | 6 | 1 | 6 | 1 | 1 | 0 |
| SS-RSRPNote3 | Config 1 | NR_CCA_FR1_I | dBm/SCS | Not applicableNote 5 | Not applicableNote 5 | -85 | -90 | -106.00 | -107.00 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -105.50 | -106.50 |
| IoNote3 | Config 1 | NR_CCA_FR1_I | dBm/38.16 MHz | Not applicableNote 5- |  | -51.99 |  | -70.82 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -70.32 |  |
| Propagation condition |  |  | - | AWGN |  |  |  |  |  |
| Antenna configuration |  |  |  | 1x2 |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Subtest 1 is not used when testing with 30 kHz SSB SCS.NOTE 6: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 9: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |  |  |

##### A.11.6.1.2.3 Test Requirements

The SS-RSRP measurement accuracy for Cell 2 and Cell 3 shall fulfil absolute requirement in clause 10.1.36.1.1 and relative requirement in clause 10.1.36.1.2.

### A.11.6.2 SS-RSRQ

#### A.11.6.2.1 Intra-frequency measurement accuracy

##### A.11.6.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.29.1.1.

##### A.11.6.2.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.11.6.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.11.6.2.1.2-2. In all test cases, Cell 1 is the PCell with CCA and Cell 2 is the target cell with CCA. Three sub-tests (Test 1, Test 2, and Test 3) are provided different Noc on Cells 1 and 2.

Table A.11.6.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

| Config | Description |
| --- | --- |
| 1 | With CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.6.2.1.2-2: SS-RSRQ Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| SSB ARFCN |  |  |  | freq1 |  |  |  |
| DL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.1 |  |  |  |
| UL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.2 |  |  |  |
| DL CCA probability for semi-static channel access Note 7, 8 |  | PCCA_UL |  | 1.0 | - | 1.0 | - |
|  |  | PCCA_DL |  | 0.9375 | - | 0.9375 | - |
| DL CCA probability fordynamic channel access Note 8, 9 |  | PCCA_DL_1 |  | 0.75 | - | 0.75 | - |
|  |  | PCCA_DL_2 |  | 0.75 | - | 0.75 | - |
| Duplex mode |  | Config 1 |  | TDD |  |  |  |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  | Config 1 | MHz | 40: NRB,c = 106 |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 CCA |  | SR.1.1 CCA |  |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA |  | CR.1.1 CCA |  |
| Control Channel RMC |  | Config 1 |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  |
| TRS configuration |  | Config 1 |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  |
| OCNG Patterns |  |  |  | OP. 1 |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |
| Time offset with Cell 1 |  | Config 1 | s | - | 3 | - | 3 |
| DBT Window Configuration |  | Config 1 |  | DBT.1(As defined in A.3.28.1) |  |  |  |
| SSB configuration |  | Config 1 |  | SSB.1 CCA for semi-static channel accessSSB.2 CCA for dynamic channel access |  |  |  |
| SMTC configuration |  | Config 1 |  | SMTC.1 |  |  |  |
| PDSCH/PDCCH |  | Config 1 | kHz | 30kHz |  |  |  |
| subcarrier spacing |  |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config1 | NR_CCA_FR1_I | dBm/15kHz | -91 |  | -110 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -109.5 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 | NR_CCA_FR1_I | dBm/SCS | -88 |  | -107 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -106.5 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.76 |  | -5.46 | -5.46 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 | 3 | -4 | -4 |
| SS-RSRPNote3 | Config 1 | NR_CCA_FR1_I | dBm/SCS | -85 | -85 | -111 | -111 |
|  |  | NR_CCA_FR1_J |  |  |  | -110.5 | -110.5 |
| SS-RSRQ Note3 |  | NR_CCA_FR1_I | dB | -14.77 | -14.77 | -17.34 | -17.34 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| IoNote3 | Config 1 | NR_CCA_FR1_I | dBm/38.16MHz | -50 |  | -73.4 | -73.4 |
|  |  | NR_CCA_FR1_J |  |  |  | -72.9 | -72.9 |
| Propagation condition |  |  | - | AWGN | AWGN | AWGN | AWGN |
| Antenna configuration |  |  |  | 1x2 | 1x2 | 1x2 | 1x2 |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.Note 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.Note 3: SS-RSRQ, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.Note 4: SS-RSRQ, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.Note 5: NR operating band groups are as defined in clause 3.5.2.Note 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations.Note 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.Note 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.Note 9: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |

##### A.11.6.2.1.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.29.1.1.

#### A.11.6.2.2 Inter-frequency measurement accuracy

##### A.11.6.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.30.1.1 and 10.1.30.1.2.

##### A.11.6.2.2.2 Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.11.6.2.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.11.6.2.2.2-2. In all test cases, Cell 1 is the PCell with CCA and Cell 2 is target cell with CCA. Two sub-tests (Test 1 and Test 2) are provided different Noc on Cells 1 and 2.

Table A.11.6.2.2.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

| Config | Description |
| --- | --- |
| 1 | With CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.6.2.2.2-2: SS-RSRQ Inter frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| SSB ARFCN |  |  |  | freq1 | freq2 | freq1 | freq2 |
| DL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.1 |  |  |  |
| UL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.2 |  |  |  |
| UL CCA probability |  | PCCA_UL |  | 1.0 | - | 1.0 | - |
| DL CCA probability for semi-static channel access Note 7, 8 |  | PCCA_DL |  | 0.9375 | - | 0.9375 | - |
| DL CCA probability fordynamic channel access Note 8, 9 |  | PCCA_DL_1 |  | 0.75 | - | 0.75 | - |
|  |  | PCCA_DL_2 |  | 0.75 | - | 0.75 | - |
| Duplex mode |  | Config 1 |  | TDD |  |  |  |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  | Config 1 | MHz | 40: NRB,c = 106 |  |  |  |
| Gap pattern ID |  | Config 1 |  | 0 |  |  |  |
| BWP BW |  | Config 1 |  | 40: NRB,c = 106 |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 CCA |  | SR.1.1 CCA |  |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA |  | CR.1.1 CCA |  |
| Dedicated CORESET Reference Channel |  | Config 1 |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  |
| TRS Configuration |  | Config 1 |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |
| Time offset with Cell 1 |  | Config 1 | s | - | 3 | - | 3 |
| DBT Window configuration |  | Config 1 |  | DBT.1 |  |  |  |
| SSB configuration |  | Config 1 |  | SSB.1 CCA for semi-static channel accessSSB.2 CCA for dynamic channel access |  |  |  |
| SMTC configuration |  | Config 1 |  | SMTC.1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 | kHz | 30 kHz |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | NR_CCA_FR1_I | dBm/15kHz | -86.27 |  | -112 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -111.5 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 | NR_CCA_FR1_I | dBm/SCS | -83.27 |  | -109 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -108.5 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.75 |  | 3 | -1.75 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -1.75 |  | 3 | -1.75 |
| SS-RSRPNote3 | Config 1 | NR_CCA_FR1_I |  | -85.02 | -85.02 | -106 | -110.75 |
|  |  | NR_CCA_FR1_J |  |  |  | -105.5 | -110-.25 |
| SS-RSRQNote3 |  | NR_CCA_FR1_I | dB | -14.77 | -14.77 | 12.56 | 14.76 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |
| IoNote3 | Config 1 | NR_CCA_FR1_I | dBm/SCS | -50 |  | -73.19 | -75.73 |
|  |  | NR_CCA_FR1_J |  |  |  | -72.69 | -75.23 |
| Propagation condition |  |  | - | AWGN | AWGN | AWGN | AWGN |
| Antenna configuration |  |  |  | 1x2 | 1x2 | 1x2 | 1x2 |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.Note 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.Note 3: SS-RSRQ, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.Note 4: SS-RSRQ, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.Note 5: NR operating band groups are as defined in clause 3.5.2. Note 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configuration.Note 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.Note 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.Note 9: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |

##### A.11.6.2.2.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.30.1.1 and 10.1.30.1.2.

#### A.11.6.2.3 Intra-frequency measurement accuracy on SCC

##### A.11.6.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.29.1.1.

##### A.11.6.2.3.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.11.6.2.3.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.11.6.2.3.2-2. In all test cases, Cell 1 is the PCell with CCA, Cell 2 is the SCell with CCA, and Cell 3 is the target cell with CCA. Three sub-tests (Test 1, Test 2, and Test 3) are provided different Noc on Cells 1, 2, and 3.

Table A.11.6.2.3.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

| Config | Description |
| --- | --- |
| 1 | With CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.6.2.3.2-2: SS-RSRQ Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 / Cell 2 | Cell 3 | Cell 1 / Cell 2 | Cell 3 |
| SSB ARFCN |  |  |  | freq1 for Cell 1freq2 for Cell 2 | freq2 | freq1 for Cell 1freq2 for Cell 2 | freq2 |
| DL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.1 |  |  |  |
| UL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.2 |  |  |  |
| DL CCA probability for semi-static channel access Note 7, 8 |  | PCCA_UL |  | 1.0 | - | 1.0 | - |
|  |  | PCCA_DL |  | 0.9375 | - | 0.9375 | - |
| DL CCA probability fordynamic channel access Note 8, 9 |  | PCCA_DL_1 |  | 0.75 | - | 0.75 | - |
|  |  | PCCA_DL_2 |  | 0.75 | - | 0.75 | - |
| Duplex mode |  | Config 1 |  | TDD |  |  |  |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  | Config 1 | MHz | 40: NRB,c = 106 |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 CCA |  | SR.1.1 CCA |  |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA |  | CR.1.1 CCA |  |
| Control Channel RMC |  | Config 1 |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  |
| TRS configuration |  | Config 1 |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  |
| OCNG Patterns |  |  |  | OP. 1 |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |
| Time offset with Cell 1 |  | Config 1 | s | - | 3 | - | 3 |
| DBT Window Configuration |  | Config 1 |  | DBT.1(As defined in A.3.28.1) |  |  |  |
| SSB configuration |  | Config 1 |  | SSB.1 CCA for semi-static channel accessSSB.2 CCA for dynamic channel access |  |  |  |
| SMTC configuration |  | Config 1 |  | SMTC.1 |  |  |  |
| CSI-RS for tracking |  | Config 1 |  | TRS.1.2 TDD |  |  |  |
| PDSCH/PDCCH |  | Config 1 | kHz | 30kHz |  |  |  |
| subcarrier spacing |  |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config1 | NR_CCA_FR1_I | dBm/15kHz | -91 |  | -110 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -109.5 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 | NR_CCA_FR1_I | dBm/SCS | -88 |  | -107 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -106.5 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.76 |  | -5.46 | -5.46 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 | 3 | -4 | -4 |
| SS-RSRPNote3 | Config 1 | NR_CCA_FR1_I | dBm/SCS | -85 | -85 | -111 | -111 |
|  |  | NR_CCA_FR1_J |  |  |  | -110.5 | -110.5 |
| SS-RSRQ Note3 |  | NR_CCA_FR1_I | dB | -14.77 | -14.77 | -17.34 | -17.34 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| IoNote3 | Config 1 | NR_CCA_FR1_I | dBm/38.16MHz | -50 |  | -73.4 | -73.4 |
|  |  | NR_CCA_FR1_J |  |  |  | -72.9 | -72.9 |
| Propagation condition |  |  | - | AWGN | AWGN | AWGN | AWGN |
| Antenna configuration |  |  |  | 1x2 | 1x2 | 1x2 | 1x2 |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.Note 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.Note 3: SS-RSRQ, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.Note 4: SS-RSRQ, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.Note 5: NR operating band groups are as defined in clause 3.5.2.Note 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations.Note 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.Note 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.Note 9: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |

##### A.11.6.2.3.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.29.1.1.

#### A.11.6.2.4 Inter-frequency measurement accuracy

##### A.11.6.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.30.1.1 and 10.1.30.1.2.

##### A.11.6.2.4.2 Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.11.6.2.4.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.11.6.2.4.2-2 and A.11.6.2.4.2-3. In all test cases, Cell 1 is the PCell and Cell 2 is target cell with CCA. Two sub-tests (Test 1 and Test 2) are provided different Noc on Cells 1 and 2.

Table A.11.6.2.4.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

| Config | Description |
| --- | --- |
| 1 | Without CCA: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.6.2.4.2-2: SS-RSRQ Inter frequency test parameters

| Parameter |  |  | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 | Cell 2 |
| SSB ARFCN |  |  |  | freq2 | freq2 |
| DL CCA model |  | Config 1, 2, 3 |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  | Config 1, 2, 3 |  | As specified in clause A.3.26.2.2 |  |
| UL CCA probability |  | PCCA_UL |  | 1.0 |  |
| DL CCA probability for semi-static channel access Note 7, 8 |  | PCCA_DL |  | 0.9375 |  |
| DL CCA probability fordynamic channel access Note 8, 9 |  | PCCA_DL_1 |  | 0.75 |  |
|  |  | PCCA_DL_2 |  | 0.75 |  |
| Duplex mode |  | Config 1, 2, 3 |  | TDD |  |
| TDD configuration |  | Config 1, 2, 3 |  | TDDConf.1.1 CCA |  |
| BWchannel |  | Config 1, 2, 3 | MHz | 40: NRB,c = 106 |  |
| Gap pattern ID |  | Config 1, 2, 3 |  | 0 |  |
| BWP BW |  | Config 1, 2, 3 |  | 40: NRB,c = 106 |  |
| DRX Cycle |  |  | ms | Not Applicable |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |
| Time offset with Cell 1 |  | Config 1, 2, 3 | s | 3 |  |
| DBT Window configuration |  | Config 1, 2, 3 |  | DBT.1 |  |
| SSB configuration |  | Config 1, 2, 3 |  | SSB.1 CCA for semi-static channel accessSSB.2 CCA for dynamic channel access |  |
| SMTC configuration |  | Config 1, 2, 3 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2, 3 | kHz | 30 kHz |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | NR_CCA_FR1_I | dBm/15kHz | -86.27 | -112 |
|  |  | NR_CCA_FR1_J |  |  | -111.5 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2, 3 | NR_CCA_FR1_I | dBm/SCS | -83.27 | -109 |
|  |  | NR_CCA_FR1_J |  |  | -108.5 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.75 | -1.75 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -1.75 | -1.75 |
| SS-RSRPNote3 | Config 1, 2, 3 | NR_CCA_FR1_I |  | -85.02 | -110.75 |
|  |  | NR_CCA_FR1_J |  |  | -110.25 |
| SS-RSRQNote3 |  | NR_CCA_FR1_I | dB | -14.77 | 14.76 |
|  |  | NR_CCA_FR1_J |  |  |  |
| IoNote3 | Config 1, 2, 3 | NR_CCA_FR1_I | dBm/SCS | -50 | -75.73 |
|  |  | NR_CCA_FR1_J |  |  | -75.23 |
| Propagation condition |  |  | - | AWGN | AWGN |
| Antenna configuration |  |  |  | 1x2 | 1x2 |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.Note 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.Note 3: SS-RSRQ, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.Note 4: SS-RSRQ, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.Note 5: NR operating band groups are as defined in clause 3.5.2. Note 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configuration.Note 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.Note 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.Note 9: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |

Table A.11.6.2.4.2-3: SS-RSRQ Intra frequency test parameters for NR PCell

| Parameter |  |  |  |  | Unit |  | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  | Cell 1 |  | Cell 1 |  |
| SSB ARFCN |  |  |  |  |  |  | freq1 |  |  |  |
| Duplex mode |  |  | Config 1 |  |  |  | FDD |  |  |  |
|  |  |  | Config 2,3 |  |  |  | TDD |  |  |  |
| TDD configuration |  |  | Config 1 |  |  |  | Not Applicable |  |  |  |
|  |  |  | Config 2 |  |  |  | TDDConf.1.1 |  |  |  |
|  |  |  | Config 3 |  |  |  | TDDConf.2.1 |  |  |  |
| BWchannel |  |  | Config 1 |  | MHz |  | 10: NRB,c = 52 |  |  |  |
|  |  |  | Config 2 |  |  |  | 10: NRB,c = 52 |  |  |  |
|  |  |  | Config 3 |  |  |  | 40: NRB,c = 106 |  |  |  |
| Gap Pattern ID |  |  |  |  |  |  | 0 |  |  |  |
| BWP configuration |  |  | Initial DL BWP |  |  |  | DLBWP.0.1 |  |  |  |
|  |  |  | Dedicated DL BWP |  |  |  | DLBWP.1.1 |  |  |  |
|  |  |  | Initial UL BWP |  |  |  | ULBWP.0.1 |  |  |  |
|  |  |  | Dedicated UL BWP |  |  |  | ULBWP.1.1 |  |  |  |
| DRX Cycle |  |  |  |  | ms |  | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  |  | Config 1 |  |  |  | SR.1.1 FDD |  |  |  |
|  |  |  | Config 2 |  |  |  | SR.1.1 TDD |  |  |  |
|  |  |  | Config 3 |  |  |  | SR2.1 TDD |  |  |  |
| RMSI CORESET Reference Channel |  |  | Config 1 |  |  |  | CR.1.1 FDD |  |  |  |
|  |  |  | Config 2 |  |  |  | CR.1.1 TDD |  |  |  |
|  |  |  | Config 3 |  |  |  | CR.2.1 TDD |  |  |  |
| Control Channel RMC |  |  | Config 1 |  |  |  | CCR.1.1 FDD |  |  |  |
|  |  |  | Config 2 |  |  |  | CCR.1.1 TDD |  |  |  |
|  |  |  | Config 3 |  |  |  | CCR.2.1 TDD |  |  |  |
| TRS Configuration |  |  | Config 1 |  |  |  | TRS.1.1 FDD |  |  |  |
|  |  |  | Config 2 |  |  |  | TRS.1.1 TDD |  |  |  |
|  |  |  | Config 3 |  |  |  | TRS.1.2 TDD |  |  |  |
| OCNG Patterns |  |  |  |  |  |  | OP. 1 |  |  |  |
| SS-RSSI-Measurement |  |  |  |  |  |  | Not Applicable |  |  |  |
| SMTC configuration |  |  | Config 1 |  |  |  | SMTC.2 |  |  |  |
|  |  |  | Config 2,3 |  |  |  | SMTC.1 |  |  |  |
| SSB configuration |  |  | Config 1,2 |  |  |  | SSB.1 FR1 |  |  |  |
|  |  |  | Config 3 |  |  |  | SSB.2 FR1 |  |  |  |
| CSI-RS for tracking |  |  | Config 1 |  |  |  | TRS.1.1 FDD |  |  |  |
|  |  |  | Config 2 |  |  |  | TRS.1.1 TDD |  |  |  |
|  |  |  | Config 3 |  |  |  | TRS.1.2 TDD |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  |  | Config 1,2 |  | kHz |  | 15 kHz |  |  |  |
|  |  |  | Config 3 |  |  |  | 30 kHz |  |  |  |
| EPRE ratio of PSS to SSS |  |  |  |  | dB |  | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| Noc Note2 | Config 1,2 |  | NR_FDD_FR1_A |  | dBm/15kHz |  | -85 |  | -114 |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  | -113.5 |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  | -113 |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  | -112.5 |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  | -112 |  |
|  |  | NR_FDD_FR1_G |  |  |  |  |  | -111 |  |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  | -110.5 |  |
|  | Config 3 |  | NR_FDD_FR1_A |  |  |  | -91 |  | -114 |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  | -113.5 |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  | -113 |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  | -112.5 |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  | -112 |  |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  | -111 |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  | -110.5 |  |
| Noc Note2 | Config 1,2 |  | NR_FDD_FR1_A |  | dBm/SCS |  | -85 |  | -114 |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  | -113.5 |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  | -113 |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  | -112.5 |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  | -112 |  |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  | -111 |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  | -110.5 |  |
|  | Config 3 |  | NR_FDD_FR1_A |  |  |  | -88 |  | -111 |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  | -110.5 |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  | -110 |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  | -109.5 |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  | -109 |  |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  | -108 |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  | -107.5 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  |  |  | dB |  | -1.76 |  | -5.46 |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  |  |  | dB |  | 3 |  | -4 |  |
| SS-RSRPNote3 | Config 1,2 |  | NR_FDD_FR1_A |  | dBm/SCS |  | -82 |  | -118 |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  | -117.5 |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  | -117 |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  | -116.5 |  |
|  |  |  | NR_FDD_FR1_E, |  |  |  |  |  | -116 |  |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  | -115 |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  | -114.5 |  |
|  | Config 3 |  | NR_FDD_FR1_A |  |  |  | -85 |  | -115 |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  | -114.5 |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  | -114 |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  | -113.5 |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  | -113 |  |
|  |  | NR_FDD_FR1_G |  |  |  |  |  | -112 |  |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  | -111.5 |  |
| SS-RSRQ Note3 |  |  | NR_FDD_FR1_A |  | dB |  | -14.77 |  | -17.34 |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  |  |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  |  |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  |  |
| IoNote3 | Config 1,2 |  | NR_FDD_FR1_A |  | dBm/9.36MHz |  | -50 |  | -83.5 |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  | -83 |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  | -82.5 |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  | -82 |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  | -81.5 |  |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  | -80.5 |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  | -80 |  |
|  | Config 3 |  | NR_FDD_FR1_A |  | dBm/38.16MHz |  | -50 |  | -77.4 |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  | -76.9 |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  | -76.4 |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  | -75.9 |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  | -75.4 |  |
|  |  | NR_FDD_FR1_G |  |  |  |  |  | -74.4 |  |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  | -73.9 |  |
| Propagation condition |  |  |  |  | - |  | AWGN |  | AWGN |  |
| Antenna configuration |  |  |  |  |  |  | 1x2 |  | 1x2 |  |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.Note 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.Note 3: SS-RSRQ, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.Note 4: SS-RSRQ, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.Note 5: NR operating band groups are as defined in clause 3.5.2. |  |  |  |  |  |  |  |  |  |  |

##### A.11.6.2.4.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.30.1.1 and 10.1.30.1.2.

### A.11.6.3 SS-SINR

#### A.11.6.3.1 Intra-frequency measurement accuracy

##### A.11.6.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.31.1.1.

##### A.11.6.3.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.11.6.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.11.6.3.1.2-2. In all test cases, Cell 1 is the PCell with CCA and Cell 2 is the target cell with CCA. Two sub-tests (Test 1 and Test 2) are provided different Noc on Cells 1 and 2.

Table A.11.6.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

| Config | Description |
| --- | --- |
| 1 | With CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.6.3.1.2-2: SS-SINR Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| SSB ARFCN |  |  |  | freq1 |  | freq1 |  |
| DL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.1 |  |  |  |
| UL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.2 |  |  |  |
| UL CCA probability |  | PCCA_UL |  | 1.0 | - | 1.0 | - |
| DL CCA probability for semi-static channel access Note 7, 8 |  | PCCA_DL |  | 0.9375 | - | 0.9375 | - |
| DL CCA probability fordynamic channel access Note 8, 9 |  | PCCA_DL_1 |  | 0.75 | - | 0.75 | - |
|  |  | PCCA_DL_2 |  | 0.75 | - | 0.75 | - |
| Duplex mode |  | Config 1 |  | TDD |  |  |  |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |  |  |
| TRS configuration |  | Config 1 |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 CCA |  | SR.1.1 CCA |  |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA |  | CR.1.1 CCA |  |
| Dedicated CORESET Reference Channel |  | Config 1 |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |
| DBT Window configuration |  | Config 1 |  | DBT.1 |  |  |  |
| Time offset with Cell 1 |  | Config 1 | s | - | 3 | - | 3 |
| SSB configuration |  | Config 1 |  | SSB.1 CCA for semi-static channel accessSSB.2 CCA for dynamic channel access |  |  |  |
| SMTC configuration |  | Config 1 |  | SMTC.1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 | kHz | 30 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | NR_CCA_FR1_I | dBm/15 kHz | -93 |  | -112 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -111.5 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 | NR_CCA_FR1_I | dBm/SCS | -90 |  | -109 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -108.5 |  |
| ![](media_svg/image15.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 0 | -3.19 | -5.46 | -5.46 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4.54 | 2.66 | -4 | -4 |
| SS-RSRPNote3 | Config 1 | NR_CCA_FR1_I | dBm/SCS | -85.46 | -87.34 | -113 | -113 |
|  |  | NR_CCA_FR1_J |  |  |  | -112.5 | -112.5 |
| SS-SINR Note3 |  | NR_CCA_FR1_I | dB | 0 | -3.19 | -5.46 | -5.46 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |
| IoNote3 | Config 1 | NR_CCA_FR1_I | dBm/38.16 MHz | -51.41 |  | -75.41 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -74.91 |  |
| Propagation condition |  |  | - | AWGN |  |  |  |
| Antenna configuration |  |  | - | 1x2 |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2. NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configuration.NOTE 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 9: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |

##### A.11.6.3.1.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.31.1.1.

#### A.11.6.3.2 Inter-frequency measurement accuracy

##### A.11.6.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.32.1.1 and 10.1.32.1.2.

##### A.11.6.3.2.2 Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.11.6.3.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.11.6.3.2.2-2. In all test cases, Cell 1 is the PCell with CCA and Cell 2 is target cell with CCA. Three sub-tests (Test 1, Test 2, and Test 3) are provided different Noc on Cells 1 and 2.

Table A.11.6.3.2.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

| Config | Description |
| --- | --- |
| 1 | With CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.6.3.2.2-2: SS-SINR Inter frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |  | Cell 1 | Cell 2 |
| SSB ARFCN |  |  |  | freq1 | freq2 | freq1 | freq2 |  | freq1 | freq2 |
| DL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.1 |  |  |  |  |  |  |
| UL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.2 |  |  |  |  |  |  |
| UL CCA probability |  | PCCA_UL |  | 1.0 | - | 1.0 | - | 1.0 |  | - |
| DL CCA probability for semi-static channel access Note 7, 8 |  | PCCA_DL |  | 0.9375 | - | 0.9375 | - | 0.9375 |  | - |
| DL CCA probability fordynamic channel access Note 8, 9 |  | PCCA_DL_1 |  | 0.75 | - | 0.75 | - | 0.75 |  | - |
|  |  | PCCA_DL_2 |  | 0.75 | - | 0.75 | - | 0.75 |  | - |
| Duplex mode |  | Config 1 |  | TDD |  |  |  |  |  |  |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |  |  |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |  |  |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |  |  |  |  |  |
| Gap pattern ID |  |  |  | 0 | - | 0 | - |  | 0 | - |
| TRS configuration |  | Config 1 |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  |  | TRS.1.2 TDD |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 CCA |  | SR.1.1 CCA |  |  | SR.1.1 CCA |  |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA |  | CR.1.1 CCA |  |  | CR.1.1 CCA |  |
| Dedicated CORESET Reference Channel |  | Config 1 |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  |  | CCR.1.1 CCA |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |  |  |  |
| Time offset with Cell 1 |  | Config 1 | s | - | 3 | - | 3 |  | - | 3 |
| DBT Window configuration |  | Config 1 |  | DBT.1 |  |  |  |  |  |  |
| SSB configuration |  | Config 1 |  | SSB.1 CCA for semi-static channel accessSSB.2 CCA for dynamic channel access |  |  |  |  |  |  |
| SMTC configuration |  | Config 1 |  | SMTC.1 |  |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 | kHz | 30 |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 |  | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | NR_CCA_FR1_I | dBm/15 kHz | -88 |  | -108.5 |  |  | -115.5 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |  | -115 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 | NR_CCA_FR1_I | dBm/SCS | -85 |  | -105.5 |  |  | -112.5 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |  | -112 |  |
| ![](media_svg/image16.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.75 | -1.75 | 20 | 20 |  | -4.0 | -4.0 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -1.75 |  | 20 |  |  | -4.0 |  |
| SS-RSRP Note3 | Config 1 | NR_CCA_FR1_I | dBm/SCS | -86.75 |  | -85.5 |  |  | -116.5 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |  | -116 |  |
| SS-SINRNote3 |  | NR_CCA_FR1_I | dB | -1.75 |  | 20 |  |  | -4.0 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |  |  |  |
| IoNote3 | Config 1 | NR_CCA_FR1_I | dBm/38.16 MHz | -51.73 |  | -54.41 |  |  | -80 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |  | -79.5 |  |
| Propagation condition |  |  | - | AWGN |  |  |  |  |  |  |
| Antenna configuration |  |  | - | 1x2 |  |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configuration.NOTE 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 9: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |  |  |  |

##### A.11.6.3.2.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.32.1.1 and 10.1.32.1.2.

#### A.11.6.3.3 Intra-frequency measurement accuracy on SCC

##### A.11.6.3.3.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.31.1.1.

##### A.11.6.3.3.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.11.6.3.3.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.11.6.3.3.2-2. In all test cases, Cell 1 is the PCell with CCA, Cell 2 is the SCell with CCA, and Cell 3 is the target cell with CCA. Two sub-tests (Test 1 and Test 2) are provided different Noc on Cells 1, 2, and 3.

Table A.11.6.3.3.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

| Config | Description |
| --- | --- |
| 1 | With CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.6.3.3.2-2: SS-SINR Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 / Cell 2 | Cell 3 | Cell 1 / Cell 2 |  | Cell 3 |
| SSB ARFCN |  |  |  | freq1 for Cell 1freq2 for Cell 2 | freq2 | freq1 for Cell 1freq2 for Cell 2 |  | freq2 |
| DL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.1 |  |  |  |  |
| UL CCA model |  | Config 1 |  | As specified in clause A.3.26.2.2 |  |  |  |  |
| UL CCA probability |  | PCCA_UL |  | 1.0 | - | 1.0 | - |  |
| DL CCA probability for semi-static channel access Note 7, 8 |  | PCCA_DL |  | 0.9375 | - | 0.9375 | - |  |
| DL CCA probability fordynamic channel access Note 8, 9 |  | PCCA_DL_1 |  | 0.75 | - | 0.75 | - |  |
|  |  | PCCA_DL_2 |  | 0.75 | - | 0.75 | - |  |
| Duplex mode |  | Config 1 |  | TDD |  |  |  |  |
| TDD configuration |  | Config 1 |  | TDDConf.1.1 CCA |  |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |  |  |  |
| TRS configuration |  | Config 1 |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 CCA |  | SR.1.1 CCA |  |  |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.1.1 CCA |  | CR.1.1 CCA |  |  |
| Dedicated CORESET Reference Channel |  | Config 1 |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |  |
| DBT Window configuration |  | Config 1 |  | DBT.1 |  |  |  |  |
| Time offset with Cell 1 |  | Config 1 | s | 3 (for Cell 2) | 3 | 3 (for Cell 2) |  | 3 |
| SSB configuration |  | Config 1 |  | SSB.1 CCA for semi-static channel accessSSB.2 CCA for dynamic channel access |  |  |  |  |
| SMTC configuration |  | Config 1 |  | SMTC.1 |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1 | kHz | 30 |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 |  | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | NR_CCA_FR1_I | dBm/15 kHz | -93 |  | -112 |  |  |
|  |  | NR_CCA_FR1_J |  |  |  | -111.5 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 | NR_CCA_FR1_I | dBm/SCS | -90 |  | -109 |  |  |
|  |  | NR_CCA_FR1_J |  |  |  | -108.5 |  |  |
| ![](media_svg/image15.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 0 | -3.19 | -5.46 |  | -5.46 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4.54 | 2.66 | -4 |  | -4 |
| SS-RSRPNote3 | Config 1 | NR_CCA_FR1_I | dBm/SCS | -85.46 | -87.34 | -113 |  | -113 |
|  |  | NR_CCA_FR1_J |  |  |  | -112.5 |  | -112.5 |
| SS-SINR Note3 |  | NR_CCA_FR1_I | dB | 0 | -3.19 | -5.46 |  | -5.46 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |  |
| IoNote3 | Config 1 | NR_CCA_FR1_I | dBm/38.16 MHz | -51.41 |  | -75.41 |  |  |
|  |  | NR_CCA_FR1_J |  |  |  | -74.91 |  |  |
| Propagation condition |  |  | - | AWGN |  |  |  |  |
| Antenna configuration |  |  | - | 1x2 |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2. NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configuration.NOTE 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 9: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |  |

##### A.11.6.3.3.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.31.1.1.

#### A.11.6.3.4 Inter-frequency measurement accuracy

##### A.11.6.3.4.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.32.1.1 and 10.1.32.1.2.

##### A.11.6.3.4.2 Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.11.6.3.4.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.11.6.3.4.2-2 and table A.11.6.3.4.2-3. In all test cases, Cell 1 is the PCell and Cell 2 is target cell with CCA. Three sub-tests (Test 1, Test 2, and Test 3) are provided different Noc on Cells 1 and 2.

Table A.11.6.3.4.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

| Config | Description |
| --- | --- |
| 1 | Without CCA: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.11.6.3.4.2-2: SS-SINR Inter frequency test parameters

| Parameter |  |  | Unit |  | Test 1 | Test 2 | Test 3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Cell 2 | Cell 2 | Cell 2 |
| SSB ARFCN |  |  |  |  | freq2 | freq2 | freq2 |
| DL CCA model |  | Config 1, 2, 3 |  |  | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  | Config 1, 2, 3 |  |  | As specified in clause A.3.26.2.2 |  |  |
| UL CCA probability |  | PCCA_UL |  |  | 1.0 |  |  |
| DL CCA probability for semi-static channel access Note 7, 8 |  | PCCA_DL |  |  | 0.9375 |  |  |
| DL CCA probability fordynamic channel access Note 8, 9 |  | PCCA_DL_1 |  |  | 0.75 |  |  |
|  |  | PCCA_DL_2 |  |  | 0.75 |  |  |
| Duplex mode |  | Config 1, 2, 3 |  |  | TDD |  |  |
| TDD configuration |  | Config 1, 2, 3 |  |  | TDDConf.1.1 CCA |  |  |
| Downlink initial BWP configuration |  |  |  |  | DLBWP.0.1 |  |  |
| Downlink dedicated BWP configuration |  |  |  |  | DLBWP.1.1 |  |  |
| Uplink initial BWP configuration |  |  |  |  | ULBWP.0.1 |  |  |
| Uplink dedicated BWP configuration |  |  |  |  | ULBWP.1.1 |  |  |
| DRX Cycle configuration |  |  | ms |  | Not Applicable |  |  |
| Gap pattern ID |  |  |  |  | - |  |  |
| OCNG Patterns |  |  |  |  | OP.1 |  |  |
| SS-RSSI-Measurement |  |  |  |  | Not Applicable |  |  |
| Time offset with Cell 1 |  | Config 1, 2, 3 | s |  | 3 |  |  |
| DBT Window configuration |  | Config 1, 2, 3 |  |  | DBT.1 |  |  |
| SSB configuration |  | Config 1, 2, 3 |  |  | SSB.1 CCA for semi-static channel access SSB.2 CCA for dynamic channel access |  |  |
| SMTC configuration |  | Config 1, 2, 3 |  |  | SMTC.1 |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2, 3 | kHz |  | 30 |  |  |
| EPRE ratio of PSS to SSS |  |  | dB |  | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | NR_CCA_FR1_I | dBm/15 kHz |  | -88 | -108.5 | -115.5 |
|  |  | NR_CCA_FR1_J |  |  |  |  | -115 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1 | NR_CCA_FR1_I | dBm/SCS |  | -85 | -105.5 | -112.5 |
|  |  | NR_CCA_FR1_J |  |  |  |  | -112 |
| ![](media_svg/image16.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB |  | -1.75 | 20 | -4.0 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB |  | -1.75 | 20 | -4.0 |
| SS-RSRP Note3 | Config 1 | NR_CCA_FR1_I | dBm/SCS |  | -86.75 | -85.5 | -116.5 |
|  |  | NR_CCA_FR1_J |  |  |  |  | -116 |
| SS-SINRNote3 |  | NR_CCA_FR1_I | dB |  | -1.75 | 20 | -4.0 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |
| IoNote3 | Config 1 | NR_CCA_FR1_I | dBm/38.16 MHz |  | -51.73 | -54.41 | -80 |
|  |  | NR_CCA_FR1_J |  |  |  |  | -79.5 |
| Propagation condition |  |  | - |  | AWGN |  |  |
| Antenna configuration |  |  | - |  | 1x2 |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configuration.NOTE 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 9: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |

Table A.11.6.3.4.2-3: SS-SINR Inter frequency test parameters for NR PCell

| Parameter |  |  | Unit | Test 1 | Test 2 | Test 3 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 1 | Cell 1 |
| SSB ARFCN |  |  |  | freq1 | freq1 | freq1 |
| Duplex mode |  | Config 1 |  |  | FDD |  |
|  |  | Config 2,3 |  |  | TDD |  |
| TDD configuration |  | Config 1 |  |  | Not Applicable |  |
|  |  | Config 2 |  |  | TDDConf.1.1 |  |
|  |  | Config 3 |  |  | TDDConf.2.1 |  |
| Downlink initial BWP configuration |  |  |  |  | DLBWP.0.1 |  |
| Downlink dedicated BWP configuration |  |  |  |  | DLBWP.1.1 |  |
| Uplink initial BWP configuration |  |  |  |  | ULBWP.0.1 |  |
| Uplink dedicated BWP configuration |  |  |  |  | ULBWP.1.1 |  |
| DRX Cycle configuration |  |  | ms |  | Not Applicable |  |
| Gap pattern ID |  |  |  |  | 0 |  |
| TRS configuration |  | Config 1 |  |  | TRS.1.1 FDD |  |
|  |  | Config 2 |  |  | TRS.1.1 TDD |  |
|  |  | Config 3 |  |  | TRS.1.2 TDD |  |
| PDSCH Reference measurement channel |  | Config 1 |  |  | SR.1.1 FDD |  |
|  |  | Config 2 |  |  | SR.1.1 TDD |  |
|  |  | Config 3 |  |  | SR2.1 TDD |  |
| RMSI CORESET Reference Channel |  | Config 1 |  |  | CR.1.1 FDD |  |
|  |  | Config 2 |  |  | CR.1.1 TDD |  |
|  |  | Config 3 |  |  | CR2.1 TDD |  |
| Dedicated CORESET Reference Channel |  | Config 1 |  |  | CCR.1.1 FDD |  |
|  |  | Config 2 |  |  | CCR.1.1 TDD |  |
|  |  | Config 3 |  |  | CCR2.1 TDD |  |
| OCNG Patterns |  |  |  |  | OP.1 |  |
| SS-RSSI-Measurement |  |  |  |  | Not Applicable |  |
| SMTC configuration |  | Config 1 |  |  | SMTC pattern 2 |  |
|  |  | Config 2,3 |  |  | SMTC pattern 1 |  |
| SSB configuration |  | Config 1,2 |  |  | SSB.1 FR1 |  |
|  |  | Config 3 |  |  | SSB.2 FR1 |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 | kHz |  | 15 |  |
|  |  | Config 3 |  |  | 30 |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 | NR_FDD_FR1_A | dBm/15 kHz | -88 | -108.5 | -119.5 |
|  |  | NR_FDD_FR1_B |  |  |  | -119 |
|  |  | NR_TDD_FR1_C |  |  |  | -118.5 |
|  |  | NR_FDD_FR1_DNR_TDD_FR1_D |  |  |  | -118 |
|  |  | NR_FDD_FR1_E |  |  |  | -117.5 |
|  |  | NR_FDD_FR1_G |  |  |  | -116.5 |
|  |  | NR_FDD_FR1_H |  |  |  | -116 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 |  | dBm/SCS | -88 | -108.5 | Same as Noc for 15 kHz |
|  | Config 3 | NR_FDD_FR1_A |  | -85 | -105.5 | -116.5 |
|  |  | NR_FDD_FR1_B |  |  |  | -116 |
|  |  | NR_TDD_FR1_C |  |  |  | -115.5 |
|  |  | NR_FDD_FR1_DNR_TDD_FR1_D |  |  |  | -115 |
|  |  | NR_FDD_FR1_E |  |  |  | -114.5 |
|  |  | NR_FDD_FR1_F |  |  |  | -114 |
|  |  | NR_FDD_FR1_G |  |  |  | -113.5 |
|  |  | NR_FDD_FR1_H |  |  |  | -113 |
| ![](media_svg/image16.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.75 | 20 | -4.0 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -1.75 | 20 | -4.0 |
| SS-RSRP Note3 | Config 1,2 | NR_FDD_FR1_A | dBm/SCS | -89.75 | -88.5 | -123.5 |
|  |  | NR_FDD_FR1_B |  |  |  | -123 |
|  |  | NR_TDD_FR1_C |  |  |  | -122.5 |
|  |  | NR_FDD_FR1_DNR_TDD_FR1_D |  |  |  | -122 |
|  |  | NR_FDD_FR1_E |  |  |  | -121.5 |
|  |  | NR_FDD_FR1_G |  |  |  | -120.5 |
|  |  | NR_FDD_FR1_H |  |  |  | -120 |
|  | Config 3 | NR_FDD_FR1_A |  | -86.75 | -85.5 | -120.5 |
|  |  | NR_FDD_FR1_B |  |  |  | -120 |
|  |  | NR_TDD_FR1_C |  |  |  | -119.5 |
|  |  | NR_FDD_FR1_DNR_TDD_FR1_D |  |  |  | -119 |
|  |  | NR_FDD_FR1_E |  |  |  | -118.5 |
|  |  | NR_FDD_FR1_G |  |  |  | -117.5 |
|  |  | NR_FDD_FR1_H |  |  |  | -117 |
| SS-SINRNote3 |  | NR_FDD_FR1_A | dB | -1.75 | 20 | -4.0 |
|  |  | NR_FDD_FR1_B |  |  |  |  |
|  |  | NR_TDD_FR1_C |  |  |  |  |
|  |  | NR_FDD_FR1_DNR_TDD_FR1_D |  |  |  |  |
|  |  | NR_FDD_FR1_E |  |  |  |  |
|  |  | NR_FDD_FR1_G |  |  |  |  |
|  |  | NR_FDD_FR1_H |  |  |  |  |
| IoNote3 | Config 1,2 | NR_FDD_FR1_A | dBm/9.36 MHz | -57.83 | -60.5 | -90.09 |
|  |  | NR_FDD_FR1_B |  |  |  | -89.59 |
|  |  | NR_TDD_FR1_C |  |  |  | -89.09 |
|  |  | NR_FDD_FR1_DNR_TDD_FR1_D |  |  |  | -88.59 |
|  |  | NR_FDD_FR1_E |  |  |  | -88.09 |
|  |  | NR_FDD_FR1_G |  |  |  | -87.09 |
|  |  | NR_FDD_FR1_H |  |  |  | -86.59 |
|  | Config 3 | NR_FDD_FR1_A | dBm/38.16 MHz | -51.73 | -54.41 | -84 |
|  |  | NR_FDD_FR1_B |  |  |  | -83.5 |
|  |  | NR_TDD_FR1_C |  |  |  | -83 |
|  |  | NR_FDD_FR1_DNR_TDD_FR1_D |  |  |  | -82.5 |
|  |  | NR_FDD_FR1_E |  |  |  | -82 |
|  |  | NR_FDD_FR1_G |  |  |  | -81 |
|  |  | NR_FDD_FR1_H |  |  |  | -80.5 |
| Propagation condition |  |  | - |  | AWGN |  |
| Antenna configuration |  |  | - |  | 1x2 |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2. |  |  |  |  |  |  |

##### A.11.6.3.4.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.32.1.1 and 10.1.32.1.2.

### A.11.6.4 L1-RSRP measurement for beam reporting with CCA serving cell

#### A.11.6.4.1 SSB based L1-RSRP measurement

##### A.11.6.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.33.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.11.6.4.1.1-1.

Table A.11.6.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations in each supported band |  |

##### A.11.6.4.1.2 Test parameters

In this set of test cases there one cell in the test, PCell under CCA (Cell 1). Cell 1 operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model.

Two sub-tests (Test 1 and Test 2) are provided with different Noc  on Cell 1. The test parameters for the Cell 1 are given in table A.11.6.4.1.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.11.6.4.1.2-1.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.11.6.4.1.2-1: FR1 SSB based L1-RSRP test parameters

| Parameter |  | Config | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- | --- | --- |
| SSB ARFCN |  | 1 |  | freq1 | freq1 |
| DL CCA model |  | 1 |  | As specifieed in A.3.20.2.1 | As specifieed in A.3.20.2.1 |
| UL CCA model |  | 1 |  | As specified in A.3.20.2.2 | As specified in A.3.20.2.2 |
| Duplex mode |  | 1 |  | TDD | TDD |
| TDD configuration |  | 1 |  | TDDConf.1.1 CCA | TDDConf.1.1 CCA |
| BWchannel |  | 1 | MHz | 40: NPRB,c = 106 | 40: NPRB,c = 106 |
| PDSCH Reference measurement channel |  | 1 |  | SR.1.1 CCA | SR.1.1 CCA |
| RMSI CORESET Reference Channel |  | 1 |  | CR.1.1 CCA | CR.1.1 CCA |
| Dedicated CORESET Reference Channel |  | 1 |  | CCR.1.1 CCA | CCR.1.1 CCA |
| SSB configuration Semi-static channel access |  | 1 |  | SSB.3 CCA | SSB.3 CCA |
| SSB configuration for Dynamic channel access |  | 1 |  | SSB.4 CCA | SSB.4 CCA |
| OCNG Patterns |  | 1 |  | OP.1 | OP.1 |
| Initial BWP Configuration |  | 1 |  | DLBWP.0.1ULBWP.0.1 | DLBWP.0.1ULBWP.0.1 |
| TRS configuration |  | 1 |  | TRS.1.2 TDD | TRS.1.2 TDD |
| Dedicated BWP configuration |  | 1 |  | DLBWP.1.1ULBWP.1.1 | DLBWP.1.1ULBWP.1.1 |
| DBT Window Configuration |  | 1 |  | DBT.1 | DBT.1 |
| reportConfigType |  | 1 |  | periodic | periodic |
| reportQuantity |  | 1 |  | ssb-Index-RSRP | ssb-Index-RSRP |
| Number of reported RS |  | 1 |  | 2 | 2 |
| L1-RSRP reporting period |  | 1 |  | slot80 | slot80 |
| EPRE ratio of PSS to SSS |  | 1 | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Note2 | NR_TDD_FR1_I | 1 | dBm/15 kHz | -94.65 | -113 |
| Note2 | NR_TDD_FR1_I | 1 | dBm/SCS | -91.65 | -110 |
|  |  | 1 | dB | 10 | -3 |
| SS-RSRPNote3 | NR_TDD_FR1_I | 1 | dBm/SCS | -81.65 | -113 |
| IoNote3 | NR_TDD_FR1_I | 1 | dBm/38.16 MHz | -50.19 | -77.19 |
|  |  | 1 | dB | 10 | -3 |
| Propagation condition |  | 1 |  | AWGN | AWGN |
| Antenna configuration |  | 1 |  | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: The test configuration excludes support for band n51 and it is not required to run this test on band n51 in this release of the specification. |  |  |  |  |  |

##### A.11.6.4.1.3 Test Requirements

In both Test 1 and Test 2, the L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 1 shall fulfil the requirements in clauses 10.1.33.1.

### A.11.6.5 RSSI

#### A.11.6.5.1 Intra-frequency RSSI measurement accuracy on PCC with CCA

##### A.11.6.5.1.1 Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.1.

##### A.11.6.5.1.2 Test parameters

In all test cases, Cell 1 is the PCell with CCA. RSSI is measured on channel number 1. Supported test configurations are shown in table A.11.6.5.1.2-1. The accuracy of RSSI intra-frequency measurements is tested by using the parameters in A.11.6.5.1.2-2 and A.11.6.5.1.2-3.

Table A.11.6.5.1.2-1: Intra frequency RSSI supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, bandwidth 40 MHz |

Table A.11.6.5.1.2-2: RSSI Intra frequency test parameters

| Parameter |  | Configurations | Unit | Test 1 |
| --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 |
| RF Channel Number |  |  |  | 1 |
| BWchannel |  |  | MHz | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1 |  | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1 |  | SSB.2 CCA |
| PCCA_DL |  |  |  | 0.9375 (Note 1, 3) 0.75 / 0.75 (Note 2, 3) |
| PCCA_UL |  |  |  | 0.87 (Note 1, 3) 0.75 (Note 2, 3) |
| DL CCA model |  |  |  | As specified in A.3.26.2.1 |
| UL CCA model |  |  |  | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image17.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |
| Channel access bandwidth |  |  | MHz | 20 |
| DRX Cycle configuration |  |  | ms | Not Applicable |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 CCA |
| RMSI CORESET Reference Channel |  |  |  | CR.1.1 CCA |
| Dedicated CORESET Reference Channel |  |  |  | CCR.1.1 CCA |
| OCNG Patterns |  |  |  | OP.1 |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -87 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -58.96 |
| Propagation condition |  |  | - | AWGN |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.11.6.5.1.2-3: RSSI RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.11.6.5.1.3 Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.1. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

#### A.11.6.5.2 Intra-frequency RSSI measurement accuracy on SCC with CCA

##### A.11.6.5.2.1 Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.1.

##### A.11.6.5.2.2 Test parameters

In all test cases, Cell 1 which is PCell operating on a carrier frequency under CCA, and Cell 2 which is SCell operating on a carrier frequency under CCA. RSSI is measured on channel number 2. Supported test configurations are shown in table A.11.6.5.2.2-1. The accuracy of RSSI intra-frequency measurements is tested by using the parameters in A.11.6.5.2.2-2 and A.11.6.5.2.2-3.

Table A.11.6.5.2.2-1: Intra frequency RSSI supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, bandwidth 40 MHz |

Table A.11.6.5.2.2-2: RSSI Intra frequency test parameters

| Parameter |  | Configurations | Unit | Test 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 |
| RF Channel Number |  |  |  | 1 | 2 |
| BWchannel |  |  | MHz | 40 | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1 |  | SSB.1 CCA | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1 |  | SSB.2 CCA | SSB.2 CCA |
| PCCA_DL |  |  |  | 1 | 0.9375 (Note 1, 3) 0.75 / 0.75 (Note 2, 3) |
| PCCA_UL |  |  |  | 1 | 0.87 (Note 1, 3) 0.75 (Note 2, 3) |
| DL CCA model |  |  |  | N/A | As specified in A.3.26.2.1 |
| UL CCA model |  |  |  | N/A | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image17.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |  |
| Channel access bandwidth |  |  | MHz | 20 |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 CCA | SR.1.1 CCA |
| RMSI CORESET Reference Channel |  |  |  | CR.1.1 CCA | CR.1.1 CCA |
| Dedicated CORESET Reference Channel |  |  |  | CCR.1.1 CCA | CCR.1.1 CCA |
| OCNG Patterns |  |  |  | OP.1 | OP.1 |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -106 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -87 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | 2.5 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -103.5 | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -58.96 |
| Propagation condition |  |  | - | AWGN |  |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.11.6.5.2.2-3: RSSI RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.11.6.5.2.3 Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.1. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

#### A.11.6.5.3 Inter-frequency RSSI measurement accuracy on a carrier with CCA

##### A.11.6.5.3.1 Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.2.

##### A.11.6.5.3.2 Test parameters

In all test cases, Cell 1 which is PCell operating on a carrier frequency under CCA, and Cell 2 which is neighbor cell operating on a carrier frequency under CCA. RSSI is measured on channel number 2. Supported test configurations are shown in table A.11.6.5.3.2-1. The accuracy of RSSI intra-frequency measurements is tested by using the parameters in A.11.6.5.3.2-2 and A.11.6.5.3.2-3.

Table A.11.6.5.3.2-1: Inter frequency RSSI supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, bandwidth 40 MHz |

Table A.11.6.5.3.2-2: RSSI Inter frequency test parameters

| Parameter |  | Configurations | Unit | Test 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 |
| RF Channel Number |  |  |  | 1 | 2 |
| BWchannel |  |  | MHz | 40 | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1 |  | SSB.1 CCA | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1 |  | SSB.2 CCA | SSB.2 CCA |
| PCCA_DL |  |  |  | 1 | 0.9375 (Note 1, 3) 0.75 / 0.75 (Note 2, 3) |
| PCCA_UL |  |  |  | 1 | 0.87 (Note 1, 3) 0.75 (Note 2, 3) |
| DL CCA model |  |  |  | N/A | As specified in A.3.26.2.1 |
| UL CCA model |  |  |  | N/A | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image17.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |  |
| Channel access bandwidth |  |  | MHz | 20 |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 CCA | SR.1.1 CCA |
| RMSI CORESET Reference Channel |  |  |  | CR.1.1 CCA | CR.1.1 CCA |
| Dedicated CORESET Reference Channel |  |  |  | CCR.1.1 CCA | CCR.1.1 CCA |
| OCNG Patterns |  |  |  | OP.1 | OP.1 |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -106 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -87 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | 2.5 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -103.5 | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -58.96 |
| Propagation condition |  |  | - | AWGN |  |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.11.6.5.3.2-3: RSSI RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.11.6.5.3.3 Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.2. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

### A.11.6.6 Channel occupancy

#### A.11.6.6.1 Intra-frequency channel occupancy measurement accuracy on PCC with CCA

##### A.11.6.6.1.1 Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.1.

##### A.11.6.6.1.2 Test parameters

In all test cases, Cell 1 is the PCell with CCA. channel occupancy is measured on channel number 1. Supported test configurations are shown in table A.11.6.6.1.2-1. The accuracy of channel occupancy intra-frequency measurements is tested by using the parameters in A.11.6.6.1.2-2 and A.11.6.6.1.2-3.

Table A.11.6.6.1.2-1: Intra frequency CO supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, bandwidth 40 MHz |

Table A.11.6.6.1.2-2: CO Intra frequency test parameters

| Parameter |  | Configurations | Unit | Test 1 |
| --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 |
| RF Channel Number |  |  |  | 1 |
| BWchannel |  |  | MHz | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1 |  | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1 |  | SSB.2 CCA |
| PCCA_DL |  |  |  | 0.9375 (Note 1, 3) 0.75 / 0.75 (Note 2, 3) |
| PCCA_UL |  |  |  | 0.87 (Note 1, 3) 0.75 (Note 2, 3) |
| DL CCA model |  |  |  | As specified in A.3.26.2.1 |
| UL CCA model |  |  |  | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image17.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |
| Channel access bandwidth |  |  | MHz | 20 |
| DRX Cycle configuration |  |  | ms | Not Applicable |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 CCA |
| RMSI CORESET Reference Channel |  |  |  | CR.1.1 CCA |
| Dedicated CORESET Reference Channel |  |  |  | CCR.1.1 CCA |
| OCNG Patterns |  |  |  | OP.1 |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -87 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -58.96 |
| Propagation condition |  |  | - | AWGN |
| channelOccupancyThreshold |  |  | dBm | -83 |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

Table A.11.6.6.1.2-3: CO RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.11.6.6.1.3 Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.

#### A.11.6.6.2 Intra-frequency channel occupancy measurement accuracy on SCC with CCA

##### A.11.6.6.2.1 Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.1.

##### A.11.6.6.2.2 Test parameters

In all test cases, Cell 1 which is PCell operating on a carrier frequency under CCA, and Cell 2 which is SCell operating on a carrier frequency under CCA. Channel occupancy is measured on channel number 2. Supported test configurations are shown in table A.11.6.6.2.2-1. The accuracy of channel occupancy intra-frequency measurements is tested by using the parameters in A.11.6.6.2.2-2 and A.11.6.6.2.2-3.

Table A.11.6.6.2.2-1: Intra frequency CO supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, bandwidth 40 MHz |

Table A.11.6.6.2.2-2: CO Intra frequency test parameters

| Parameter |  | Configurations | Unit | Test 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 |
| RF Channel Number |  |  |  | 1 | 2 |
| BWchannel |  |  | MHz | 40 | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1 |  | SSB.1 CCA | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1 |  | SSB.2 CCA | SSB.2 CCA |
| PCCA_DL |  |  |  | 1 | 0.9375 (Note 1, 3) 0.75 / 0.75 (Note 2, 3) |
| PCCA_UL |  |  |  | 1 | 0.87 (Note 1, 3) 0.75 (Note 2, 3) |
| DL CCA model |  |  |  | N/A | As specified in A.3.26.2.1 |
| UL CCA model |  |  |  | N/A | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image17.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |  |
| Channel access bandwidth |  |  | MHz | 20 |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 CCA | SR.1.1 CCA |
| RMSI CORESET Reference Channel |  |  |  | CR.1.1 CCA | CR.1.1 CCA |
| Dedicated CORESET Reference Channel |  |  |  | CCR.1.1 CCA | CCR.1.1 CCA |
| OCNG Patterns |  |  |  | OP.1 | OP.1 |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -106 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -87 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | 2.5 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -103.5 | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -58.96 |
| Propagation condition |  |  | - | AWGN |  |
| channelOccupancyThreshold |  |  | dBm | -83 |  |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.11.6.6.2.2-3: CO RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.11.6.6.2.3 Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.

#### A.11.6.6.3 Inter-frequency channel occupancy measurement accuracy on a carrier with CCA

##### A.11.6.6.3.1 Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.2.

##### A.11.6.6.3.2 Test parameters

In all test cases, Cell 1 which is PCell operating on a carrier frequency under CCA, and Cell 2 which is neighbor cell operating on a carrier frequency under CCA. Channel occupancy is measured on channel number 2. Supported test configurations are shown in table A.11.6.6.3.2-1. The accuracy of channel occupancy intra-frequency measurements is tested by using the parameters in A.11.6.6.3.2-2 and A.11.6.6.3.2-3.

Table A.11.6.6.3.2-1: Inter frequency CO supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NR TDD, SSB SCS 30 kHz, data SCS 30 kHz, bandwidth 40 MHz |

Table A.11.6.6.3.2-2: CO Inter frequency test parameters

| Parameter |  | Configurations | Unit | Test 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 |
| RF Channel Number |  |  |  | 1 | 2 |
| BWchannel |  |  | MHz | 40 | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1 |  | SSB.1 CCA | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1 |  | SSB.2 CCA | SSB.2 CCA |
| PCCA_DL |  |  |  | 1 | 0.9375 (Note 1, 3) 0.75 / 0.75 (Note 2, 3) |
| PCCA_UL |  |  |  | 1 | 0.87 (Note 1, 3) 0.75 (Note 2, 3) |
| DL CCA model |  |  |  | N/A | As specified in A.3.26.2.1 |
| UL CCA model |  |  |  | N/A | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image17.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |  |
| Channel access bandwidth |  |  | MHz | 20 |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 CCA | SR.1.1 CCA |
| RMSI CORESET Reference Channel |  |  |  | CR.1.1 CCA | CR.1.1 CCA |
| Dedicated CORESET Reference Channel |  |  |  | CCR.1.1 CCA | CCR.1.1 CCA |
| OCNG Patterns |  |  |  | OP.1 | OP.1 |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -106 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -87 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | 2.5 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -103.5 | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -58.96 |
| Propagation condition |  |  | - | AWGN |  |
| channelOccupancyThreshold |  |  | dBm | -83 |  |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.11.6.6.3.2-3: CO RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.11.6.6.3.3 Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.

### A.11.6.7 E-UTRAN RSRP

### A.11.6.8 E-UTRAN RSRQ

### A.11.6.9 E-UTRAN SINR

# A.12 E-UTRA Standalone Tests with at Least One NR Cell under CCA

## A.12.1 RRC_IDLE state mobility

### A.12.1.1 Inter-RAT cell re-selection to NR on a carrier frequency with CCA

#### A.12.1.1.1 E-UTRA Cell reselection to higher priority NR target Cell in FR1 when target cell is subject to CCA

##### A.12.1.1.1.1 Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN to NR inter-RAT cell subject to CCA reselection requirements specified in clause 4.2.2.5.7 in TS 36.133 [15].

The test scenario comprises of 1 E-UTRA cell and 1 NR cell subject to CCA as given in tables A.12.1.1.1.1-1, A.8.2.1.1.1-2, A.8.2.1.1.1-3 and A.8.2.1.1.1-4. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. E-UTRA Cell 1 is already identified by the UE prior to the start of the test. Cell 2 is of higher priority than Cell 1.

Table A.12.1.1.1.1-1: Supported test configurations

| Configuration | Description of a cell without CCA | Description of a cell with CCA |
| --- | --- | --- |
| 1 | LTE FDD | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |  |

Table A.12.1.1.1.1-2: General test parameters for E-UTRA cell re-selection FR1 NR cell subject to CCA test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2 | Cell 2 | The UE camps on Cell 2 in the initial phase |
|  | Neighbour cell |  | 1, 2 | Cell 1 |  |
| T1 end condition | Active cell |  |  | Cell 1 | During T1 period the UE reselects to Cell 1 |
|  | Neighbour cell |  |  | Cell 2 |  |
| T3 end condition | Active cell |  | 1, 2 | Cell 2 | The UE shall perform reselection to Cell 2 during T3 |
|  | Neighbour cell |  | 1, 2 | Cell 1 |  |
| RF Channel Number |  |  | 1, 2 | 1, 2 | E-UTRAN radio channel (1) and NR radio channel (2) are used for this test |
| Time offset between cells |  |  | 1, 2 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1, 2 | Not Sent | No additional delays in random access procedure. |
| DBT Window Configuration |  |  | 1, 2 | DBT.1 | As specified in clause A.3.28.1. |
| DL CCA model |  |  | 1, 2 | As specified in clause A.3.26.2.1 | DL CCA model |
| UL CCA model |  |  | 1, 2 | As specified in clause A.3.26.2.2 | UL CCA model |
| DRX cycle length |  | s | 1, 2 | 1.28 | The value shall be used for all cells in the test. |
| NR PRACH configuration index |  |  | 1, 2 | 102 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| T1 |  | s | 1, 2 | 15 | T1 needs to be defined so that cell re-selection reaction time is taken into account. |
| T2 |  | s | 1, 2 | >7 | During T2, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed. The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T3. |
| T3 |  | s | 1, 2 | 75 | T3 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.12.1.1.1.1-3: Cell specific test parameters for NR Cell 2 subject to CCA

| Parameter | Unit | Test configuration | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| TDD configuration |  | 1, 2 | TDDConf.1.1.CCA |  |  |
| DL CCA probability for semi-static channel access (PCCA_DL) |  | 1, 2 | 0.9 |  |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_1) |  | 1, 2 | 0.75 |  |  |
| DL CCA probability for for dynamic static channel access (PCCA_DL_2) |  | 1, 2 | 0.5 |  |  |
| UL CCA probability PCCA_UL |  | 1, 2 | 1 |  |  |
| Md,max |  | 1, 2 | 16 |  |  |
| Mm,max |  | 1, 2 | 4 |  |  |
| Me,max |  | 1, 2 | 8 |  |  |
| PDSCH Reference measurement channel |  | 1, 2 | SR.1.1 CCA |  |  |
| RMSI CORESET Reference Channel |  | 1, 2 | CR.1.1 CCA |  |  |
| RMC CORESET Reference Channel |  | 1, 2 | CCR.1.1 CCA |  |  |
| NR SMTC parameters |  | 1, 2 | SMTC.1 |  |  |
| OCNG Patterns |  | 1, 2 | OP.1 |  |  |
| SSB configuration |  | 1, 2 | SSB.1 CCA Note4 SSB.2 CCA Note5,6 |  |  |
| Initial DL BWP configuration |  | 1, 2 | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2 | ULBWP.0.1 |  |  |
| RLM-RS |  | 1, 2 | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1, 2 | -137 |  |  |
| Pcompensation | dB | 1, 2 | 0 |  |  |
| Qhysts | dB | 1, 2 | 0 |  |  |
| Qoffsets, n | dB | 1, 2 | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2 | SS-RSRP |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2 | -4 | -infinity | 12 |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1, 2 | -95 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 2 | -98 |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2 | -4 | -infinity | 12 |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
| SS-RSRP Note3 | dBm/SCS | 1, 2 | -99 | -infinity | -83 |
| Io | dBm/38.16 MHz | 1, 2 | -62.50 | -63.95 | -51.69 |
| Treselection | s | 1, 2 | 0 | 0 | 0 |
| SnonintrasearchP | dB | 1, 2 | 50 |  |  |
| Threshx, highP | dB | 1, 2 | 48 |  |  |
| Threshserving, lowP | dB | 1, 2 | 44 |  |  |
| Threshx, lowP | dB | 1, 2 | 50 |  |  |
| Propagation Condition |  | 1, 2 | AWGN |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. . For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 6: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |

Table A.12.1.1.1.1-4: Cell specific test parameters for E-UTRA Cell 1

| Parameter | Unit | Cell 1 |  |  |
| --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 |
| E-UTRA RF Channel number |  | 1 |  |  |
| BWchannel | MHz | 10 |  |  |
| OCNG Patterns defined in TS 36.133 [15] clause A.3.2 |  | OP.2 TDD for test configuration 1, 2, 3;OP.2 FDD for test configuration 4, 5, 6 |  |  |
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
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note 2 | dBm/15 kHz | -98 |  |  |
| RSRP Note 3 | dBm/15 KHz | -84 | -84 | -84 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 14 | 14 | 14 |
| ![](media_svg/image4.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 14 | 14 | 14 |
| TreselectionEUTRAN | s | 0 |  |  |
| SnonintrasearchP | dB | 50 |  |  |
| Threshx, highP | dB | 48 |  |  |
| Threshserving, lowP | dB | 44 |  |  |
| Threshx, lowP | dB | 50 |  |  |
| Propagation Condition |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |

##### A.12.1.1.1.2 Test Requirements

The cell reselection delay to a higher priority NR cell subject to CCA is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration updateon Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 60 + 1.28 x (5 + Me) + TSI_CCA s. Me is the number of DRX cycles with at least one SMTC where there are no SSBs available during the Tevaluate,NR_Intra_CCA. If Me > Me,max the UE is required to restart the evaluation of Cell 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter_CCA + TSI_CCA, and to a lower priority cell can be expressed as: Tevaluate, NR + TSI-NR,

Where:

Thigher_priority_search See clause 4.2.2 in TS 36.133[15]

Tevaluate, NR_ inter_CCA See Table 4.2.2.5.7-1 in clause 4.2.2.5.7

TSI_CCA Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell.

Tevaluate, NR See Table 4.2.2.5.6-1 in clause 4.2.2.5.6 in TS 36.133[15]

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority NR cell and 7.68 s for the cell re-selection delay to a lower priority cell in the test case, which we allow 8 s.

## A.12.2 RRC_CONNECTED state mobility

### A.12.2.1 Handover

#### A.12.2.1.1 E-UTRAN - NR with CCA handover

##### A.12.2.1.1.1 Test Purpose and Environment

This test shall verify the E-UTRAN to NR FR1 handover requirements specified in clause 5.3.4A in TS 36.133 [15].

The test comprises of one E-UTRA carrier and one NR carrier with CCA. There are two cells and one cell on each carrier. Cell 1 is the E-UTRAN cell and Cell 2 is an inter-RAT NR neighbour cell with CCA.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in table 8.1.2.1-1 of TS 36.133 [15] is configured before T2 begins to enable inter-RAT frequency monitoring. A RRC message implying handover shall be sent to the UE during period T2 after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.12.2.1.1-1. General test parameters are provided in table A.12.2.1.1-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.12.2.1.1-3 and A.12.2.1.1-4 respectively.

Table A.12.2.1.1-1: Supported test configurations for E-UTRAN inter-RAT NR handover

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD, NR with CCA 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD, NR with CCA 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE:  The UE is only required to be tested in one of the supported test configurations. |  |

Table A.12.2.1.1-2: General test parameters for E-UTRAN inter-RAT NR handover

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  |  | 1 | 1 NR carrier frequency with CCA is used in the test |
| LTE RF Channel Number |  |  | 2 | 1 E-UTRAN carrier frequency is used in the test |
| Initial conditions | Active cell |  | Cell 1 | E-UTRAN cell |
|  | Neighbouring cell |  | Cell 2 | NR cell with CCA |
| Final condition | Active cell |  | Cell 2 |  |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |
| NR measurement quantity |  |  | SS-RSRP |  |
| E-UTRAN measurement quantity |  |  | RSRP |  |
| b2-Threshold1 |  | dBm | -84 | Absolute E-UTRAN RSRP threshold for event B2 |
| b2-Threshold2NR |  | dBm | As specified in table A.12.2.1.1-4 | Absolute NR SS-RSRP threshold for event B2 |
| Hysteresis |  | dB | 0 |  |
| TimeToTrigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| DRX |  |  | OFF | Non-DRX test |
| Access Barring Information |  | - | Not sent | No additional delays in random access procedure |
| Time offset between cells |  |  | 3 ms | Asynchronous cells |
| Gap pattern configuration Id |  |  | 0 | As specified in table 8.1.2.1-1 started before T2 starts [15] |
| T1 |  | s | 5 |  |
| T2 |  | s | £5 |  |
| T3 |  | s | 1 |  |

Table A.12.2.1.1-3: Cell specific test parameters for E-UTRAN inter-RAT NR handover with CCA (Cell 1)

| Parameter | Unit | Configuration | Cell 1 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| RF channel number |  | 1, 2 | 2 |  |  |
| Duplex mode |  | 1 | FDD |  |  |
|  |  | 2 | TDD |  |  |
| TDD special subframe configurationNote1 |  | 1, 2 | 6 |  |  |
| TDD uplink-downlink configurationNote1 |  | 1, 2 | 1 |  |  |
| BWchannel | MHz | 1, 2 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |  |
| PRACH ConfigurationNote2 |  | 1 | 4 |  |  |
|  |  | 2 | 53 |  |  |
| PDSCH parameters:DL Reference Measurement ChannelNote3 |  | 1 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |  |
|  |  | 2 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote3 |  | 1 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |  |
|  |  | 2 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |  |
| OCNG PatternsNote3 |  | 1 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |  |
|  |  | 2 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |  |
| PBCH_RA | dB | 1, 2 | 0 |  |  |
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
| NocNote5 | dBm/15 kHz | 1, 2 | -98 |  |  |
| Ês/Noc | dB | 1, 2 | 7 | 7 | 7 |
| Ês/IotNote6 | dB | 1, 2 | 7 | 7 | 7 |
| RSRPNote6 | dBm/15 kHz | 1, 2 | -91 | -91 | -91 |
| SCH_RPNote6 | dBm/15 kHz | 1, 2 | -91 | -91 | -91 |
| IoNote6 | dBm/9 MHz | 1, 2 | -62.43 | -62.43 | -62.43 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |
| Antenna Configuration and Correlation Matrix Note7 |  | 1, 2 | 1x2 Low |  |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: PRACH configurations are specified in table 5.7.1-2 and table 5.7.1-3 in TS 36.211 [23].NOTE 3: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 4: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 5: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 6: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 7: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |  |

Table A.12.2.1.1-4: Cell specific test parameters E-UTRAN inter-RAT NR with CCA handover (Cell 2)

| Parameter |  | Unit | Configuration | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 |
| RF channel number |  |  | 1, 2 | 1 |  |  |
| DL CCA probability PCCA_DL | Semi-static channel access Note 4, 6 |  | 1, 2 | PCCA_DL=0.9375 |  |  |
|  | Dynamic channel access Note 5, 6 |  | 1, 2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |
| UL CCA probability PCCA_UL | Semi-static channel access Note 4, 6 |  | 1, 2 | PCCA_UL=0.87 |  |  |
|  | Dynamic channel access Note 5, 6 |  | 1, 2 | PCCA_UL=0.75 |  |  |
| LCCA_DL |  | - | 1, 2 | 5 |  |  |
| WCCA_DL |  | ms | 1, 2 | T304 |  |  |
| LCCA_UL |  | - | 1, 2 | 5 |  |  |
| WCCA_UL |  | ms | 1, 2 | T304 |  |  |
| T304 |  | ms | 1, 2 | 500 |  |  |
| Duplex mode |  |  | 1, 2 | TDD |  |  |
| TDD Configuration |  |  | 1, 2 | TDDConf.1.1 CCA |  |  |
| BWchannel |  | MHz | 1, 2 | 40: NPRB,c = 106 (TDD) |  |  |
| PDSCH reference measurement channel |  |  | 1, 2 | SR.1.1 CCA |  |  |
| CORESET reference channel |  |  | 1, 2 | CR.1.1 CCA |  |  |
| PRACH configuration |  |  | 1, 2 | FR1 PRACH configuration 1 under CCA |  |  |
| OCNG patternNote1 |  |  | 1, 2 | OP.1 |  |  |
| BWP | Initial DL BWP |  | 1, 2 | DLBWP.0.1 |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |
| SMTC configuration |  |  | 1, 2 | SMTC.1 |  |  |
| SSB configuration | Semi-static channel access Note 4, 6 |  | 1, 2 | SSB.1 CCA |  |  |
|  | Dynamic channel access Note 5, 6 |  | 1, 2 | SSB.2 CCA |  |  |
| DBT window configuration |  |  |  | As defined in A.3.28.1 |  |  |
| b2-Threshold2NR |  | dBm | 1 | -105 |  |  |
|  |  |  | 2 | -103 |  |  |
| EPRE ratio of PSS to SSS |  | dB | 1, 2 | 0 |  |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  |  |  |  |  |
| NocNote2 |  | dBm/15 KHz | 1, 2 | -98 |  |  |
| NocNote2 |  | dBm/SCS | 1, 2 | -95 |  |  |
| Ês/Noc |  | dB | 1, 2 | -inifinit | 0 | 0 |
| Ês/IotNote3 |  | dB | 1, 2 | -inifinit | 0 | 0 |
| SS-RSRPNote3 |  | dBm/SCS | 1, 2 | -inifinit | -95 | -95 |
| IoNote3 |  | dBm/38.16 MHz | 1, 2 | -63.96 | -60.94 | -60.94 |
| Propagation condition |  |  | 1, 2 | AWGN |  |  |
| Antenna Configuration and Correlation Matrix |  |  | 1, 2 | 1x2 Low |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. . For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: Ês/Iot, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 5: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |

##### A.12.2.1.1.2 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 112 + (L1´ + L3)*20 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and is specified in TS36.331.

Tinterrupt = 62 + ( L1´ + L3) * TSMTC; Tinterrupt is defined in TS36.133 clause 5.3.4A.3 where

- L1´ is the number of SMTC occasions not available at the UE during the inter-RAT detection period.

- L3 is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure.  L3 = 0 for Type 2C UL channel access procedure as defined in TS 37.213 [33].

TSMTC = 20 ms is the SMTC periodicity ms in the test.

This gives a total of 112 +( L1´ + L3 )*20 ms.

## A.12.3 Void

## A.12.4 Measurement procedure

### A.12.4.1 E-UTRANNR inter-RAT SFTD measurements

#### A.12.4.1.1 E-UTRA – NR Inter-RAT SFTD Measurement Delay with NR under CCA in non-DRX

##### A.12.4.1.1.1 Test Purpose and Environment

The purpose of this test is to partly verify that measurement reporting delay for SFTD between E-UTRA PCell and inter-RAT NR neighbour cell under CCA is within the requirements stated in clauses 8.1.2.4.25 and 8.1.2.4.26 of TS 36.133 [15] for E-UTRA FDD and TDD, respectively, when no measurement gaps are provided and no DRX is configured.

The tests consist of a single time period of duration T1. Two carriers are used in the tests: one E-UTRA carrier with the PCell (Cell 1), and one NR carrier under CCA with the NR neighbour cell (Cell 2).

Prior to the start of time duration T1, the UE is connected to Cell 1 and configured to carry out intra-frequency measurements only. The point in time at which the UE receives, at the UE antenna connector(s), a RRC message containing a measurement configuration for SFTD measurements on RF channel 2 defines the start of time duration T1. Following the start of T1 the UE shall detect Cell 2, determine the SFN and frame time difference of Cell 2 relative to Cell 1, and send a measurement report.

The supported test configurations are listed in table A.12.4.1.1.1-1 below. General test parameters and cell-specific parameters for the NR cell are provided in tables A.12.4.1.1.1-2 and A.12.4.1.1.1-3 below, respectively. Cell-specific parameters for the E-UTRA cell are provided in clause A.3.7.2.1.

Table A.12.4.1.1.1-1: Applicable test configurations for inter-RAT SFTD measurement delay test with NR under CCA

| Config | Description |
| --- | --- |
| 1 | LTE FDD; NR: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDD; NR: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.12.4.1.1.1-2: General test parameters for inter-RAT SFTD measurement delay test with NR under CCA

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| E-UTRA RF Channel Number |  | Config 1,2 | 1 |  | One E-UTRAN carrier frequencies is used. |
| NR RF Channel Number |  | Config 1,2 | 1 |  | One NR carrier frequencies is used. |
| Active cell |  | Config 1,2 | Cell 1 |  | Cell 1 is on E-UTRA RF channel number 1. |
| Neighbour cell |  | Config 1,2 | Cell 2 |  | Cell 2 is on NR RF channel number 1. |
| CP length |  | Config 1,2 | Normal |  | Applicable to both cells. |
| DRX |  | Config 1,2 | OFF |  | DRX is not used |
| Frame time offset between serving and neighbour cells | ms | Config 1 | 3 | 7 | Asynchronous cells.The timing of Cell 2 relative to the timing of Cell 1. |
|  | ms | Config 2 | 3 |  | Synchronous cells. |
| SFN offset between serving and neighbour cells |  | Config 1,2 | 0 | 1 | SFN of Cell 2 relative to SFN of Cell 1. |
| SS-RSRP reporting |  | Config 1,2 | No |  | Only SFTD is reported. |
| T1 | s | Config 1,2 | 2 |  | T1 shall exceed Tmeasure_SFTD_LBT_max = 56 × SMTC |

Table A.12.4.1.1.1-3: Cell specific test parameters for Cell 2 in inter-RAT SFTD measurement delay test with NR under CCA

| Parameter |  | Unit | Cell 2 |
| --- | --- | --- | --- |
| NR RF Channel Number |  |  | 1 |
| Duplex mode |  |  | TDD |
| BWchannel |  | MHz | 40: NPRB,c = 106 |
| TDD configuration |  |  | TDDConf.1.1 CCA |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |
| DL CCA probability for semi-static channel accessNote5,7 | PCCA_DL |  | 0.9375 |
| DL CCA probability for dynamic channel accessNote6,7 | PCCA_DL_1 |  | 0.75 |
|  | PCCA_DL_2 |  | 0.75 |
| OCNG Pattern defined in A.3.2.1.1Note 1 |  |  | OP.1 |
| SMTC configuration defined in A.3.2.11.1 and A.3.2.11.2 |  |  | SMTC.2 |
| SSB configuration for semi-static channel accessNote5,7 |  |  | SSB.1 CCA |
| SSB configuration for dynamic channel accessNote6,7 |  |  | SSB.2 CCA |
| DBT window configuration |  |  | DBT.1 |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 30 |
| EPRE ratio of PSS to SSS |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  | dB |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |
| EPRE ratio of OCNG DMRS to SSS Note 1 |  | dB |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  | dB |  |
| Noc Note2 |  | dBm/15 kHz | -98 |
| Noc Note2 |  | dBm/SCS | -95 |
| SS-RSRP Note 3, 4 |  | dBm/SCS | -91 |
| Ês/Iot |  | dB | 4 |
| Ês/Noc |  | dB | 4 |
| Io Note 3 |  | dBm/38.16 MHz | -58.50 |
| Propagation Condition |  |  | AWGN |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols in slots with downlink transmission bursts. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic cannel access, the UE can be tested under dynamic channel access only.. |  |  |  |

##### A.12.4.1.1.2 Test Requirements

Following the start of T1, the UE shall detect Cell 2 and determine the relative time difference between Cell 1 and Cell 2. At latest at TRRC_procedure_delay + Tmeasure_SFTD_LBT_max after the beginning of time duration T1, the UE shall send a measurement report on SFTD between Cell 1 and Cell 2.

The observed rate of successful SFTD reports in repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2×TTIDCCH longer than the measurement reporting delays above due to TTI insertion uncertainty of the measurement report in DCCH.

### A.12.4.2 E-UTRANNR inter-RAT measurements on NR carrier frequency under CCA

#### A.12.4.2.1 E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used

##### A.12.4.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21A of TS 36.133 [15] for E-UTRAN FDD-NR measurements under CCA and clause 8.1.2.4.22A of TS 36.133[15] for E-UTRAN TDD-NR measurements under CCA.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1 on a carrier frequency with CCA. The test parameters are given in tables A.12.4.2.1.1-1, A.12.4.2.1.1-2, A.12.4.2.1.1-3 and A.12.4.2.1.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In this test, measurement gap pattern configuration # 0 as defined in table A.12.4.2.1.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.12.4.2.1.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| 2 | LTE TDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.12.4.2.1.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| E-UTRA RF Channel Number |  | 1, 2 | 1 | One E-UTRA carrier frequency is used. |
| NR RF Chanel Number |  | 1, 2 | 1 | One FR1 NR carrier frequency under CCA is used. |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |
| LCCA_DL |  | 1, 2 | 12 |  |
| WCCA_DL | ms | 1, 2 | TPSS/SSS_sync_irat_cca |  |
| Active cell |  | 1, 2 | E-UTRA Cell 1 (PCell) | E-UTRA Cell 1 is on E-UTRA RF channel number 1. |
| Neighbour cell |  | 1, 2 | NR Cell 2 | NR Cell 2 is on NR RF channel number 1. |
| Gap Pattern Id |  | 1, 2 | 0 | As specified in clause Table 8.1.2.1-1 of TS 36.133[15]. |
| Measurement gap offset |  | 1, 2 | 39 | As specified in TS 36.331 [16]. |
| b2-Threshold1 | dBm | 1, 2 | Note 1 | E-UTRA RSRP/RSRQ/SINR threshold for E-UTRA RSRP measurement on Cell 1 for event B2 [16] |
| b2-Threshold2NR | dBm | 1, 2 | Note 2 | SS-RSRP/ SS-RSRQ/ SS-SINR threshold measurement on Cell 2 for event B2 [16] |
| Hysteresis | dB | 1, 2 | 0 |  |
| CP length |  | 1, 2 | Normal |  |
| TimeToTrigger | s | 1, 2 | 0 |  |
| Filter coefficient |  | 1, 2 | 0 | L3 filtering is not used |
| DRX |  | 1, 2 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | 1, 2 | 3s | Synchronous cells. |
| T1 | s | 1, 2 | 5 |  |
| T2 | s | 1, 2 | ≥Tidentify_irat_cca_without_index | Tidentify_irat_cca_without_index is defined in clause 8.1.2.4.21A.1 and 8.1.2.4.22A.1 in TS 36.133 |
| NOTE 1: The value of b2-Threshold1 is defined in table A.12.4.2.1.1-3NOTE 2: The value of b2-Threshold2NR is defined in table A.12.4.2.1.1-4 |  |  |  |  |

Table A.12.4.2.1.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

| Parameter | Unit | Configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1, 2 | 1 |  |
| Duplex mode |  | 1 | FDD |  |
|  |  | 2 | TDD |  |
| TDD special subframe configurationNote1 |  | 2 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 2 | 1 |  |
| BWchannel | MHz | 1, 2 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 2 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 2 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote2 |  | 1 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 2 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| b2-Threshold1 | dBm | 1, 2 | -77 |  |
| PBCH_RA | dB | 1, 2 | 0 |  |
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
| NocNote4 | dBm/15 kHz | 1, 2 | -104 |  |
| Ês/Noc | dB | 1, 2 | 17 | 17 |
| Ês/IotNote5 | dB | 1, 2 | 17 | 17 |
| RSRPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| SCH_RPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| IoNote5 | dBm/9 MHz | 1, 2 | -59.13+10log (NPRB,c /50) | -59.13+10log (NPRB,c /50) |
| Propagation Condition Note6 |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix Note6 |  | 1, 2 | 1x2 Low |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 6: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |

Table A.12.4.2.1.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Cell 2 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| NR RF Channel Number |  | 1, 2 | 2 |  |
| TDD configuration |  | 1, 2 | TDDConf.1.1 CCA |  |
| BWchannel | MHz | 1, 2 | 40: NPRB,c = 106 |  |
| PCCA_DL for dynamic channel access Note 6,8 |  | 1, 2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| PCCA_DL for semi-static channel access Note 7,8 |  | 1, 2 | PCCA_DL=0.9375 |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  | 1, 2 | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  | 1, 2 | SMTC.1 |  |
| DBT window configuration |  | 1, 2 | DBT.1 |  |
| SSB configuration for semi-static channel access |  | 1, 2 | SSB.1 CCA |  |
| SSB configuration for dynamic channel access |  | 1, 2 | SSB.2 CCA |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2 | 30 |  |
| b2-Threshold2NR | dBm | 1, 2 | -98 |  |
| EPRE ratio of PSS to SSS |  | 1, 2 | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1, 2 | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1, 2 | -95 |  |
| SS-RSRP Note 3,5 | dBm/SCS | 1, 2 | -Infinity | -88 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot]Note 5 | dB | 1, 2 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] Note 5 | dB | 1, 2 | -Infinity | 7 |
| IoNote3 | dBm/38.16 MHz | 1, 2 | -63.95 | -56.16 |
| Propagation Condition |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2 | 1x2 Low |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5:  The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6:  For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7:  For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

##### A.12.4.2.1.2 Test Requirements

The UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_without_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index. Tidentify_irat_cca_without_index is defined in defined in clause 8.1.2.4.21A.1 and 8.1.2.4.22A.1 in TS 36.133.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.12.4.2.2 E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used

##### A.12.4.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21A of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22A of TS 36.133[15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1 on a carrier frequency with CCA. The test parameters are given in tables A.12.4.2.2.1-1, A.12.4.2.2.1-2, A.12.4.2.2.1-3 and A.12.4.2.2.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In this test, measurement gap pattern configuration # 0 as defined in table A.12.4.2.2.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.12.4.2.2.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| 2 | LTE TDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.12.4.2.2.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value |  |  | Comment |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |  |
| E-UTRA RF Channel Number |  | 1, 2 | 1 |  |  | One E-UTRAcarrier frequency is used. |
| NR RF Chanel Number |  | 1, 2 | 1 |  |  | One FR1 NR carrier frequency under CCA is used. |
| Active cell |  | 1, 2 | E-UTRA Cell 1 (PCell) |  |  | E-UTRA Cell 1 is on E-UTRA RF channel number 1. |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |  |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |  |  |
| LCCA_DL |  | 1, 2 | 12 |  | 5 |  |
| WCCA_DL | ms | 1, 2 | TPSS/SSS_sync_irat_cca |  |  |  |
| Neighbour cell |  | 1, 2 | NR Cell 2 |  |  | NR Cell 2 is on NR RF channel number 1. |
| Gap Pattern Id |  | 1, 2 | 0 |  |  | As specified in clause Table 8.1.2.1-1 of TS 36.133[15]. |
| Measurement gap offset |  | 1, 2 | 39 |  |  | As specified in TS 36.331 [16]. |
| b2-Threshold1 | dBm | 1, 2 | Note 1 |  |  | E-UTRA RSRP threshold for E-UTRA RSRP measurement on Cell 1 for event B2 [16] |
| b2-Threshold2NR | dBm | 1, 2 | Note 2 |  |  | SS-RSRP threshold for measurement on Cell 2 for event B2 [16] |
| Hysteresis | dB | 1, 2 | 0 |  |  |  |
| CP length |  | 1, 2 | Normal |  |  |  |
| TimeToTrigger | s | 1, 2 | 0 |  |  |  |
| Filter coefficient |  | 1, 2 | 0 |  |  | L3 filtering is not used |
| DRX |  | 1, 2 | DRX.9 | DRX.12 |  | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | 1, 2 | 3s |  |  | Synchronous cells. |
| T1 | s | 1, 2 | 5 |  |  |  |
| T2 | s | 1, 2 | ≥Tidentify_irat_cca_without_index |  |  | Tidentify_irat_cca_without_index is defined in clause 8.1.2.4.21A.1 and 8.1.2.4.22A.1 in TS 36.133 |
| NOTE 1: The value of b2-Threshold1 is defined in table A.12.4.2.1.1-3NOTE 2: The value of b2-Threshold2NR is defined in table A.12.4.2.1.1-4 |  |  |  |  |  |  |

Table A.12.4.2.2.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

| Parameter | Unit | Configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1, 2 | 1 |  |
| Duplex mode |  | 1 | FDD |  |
|  |  | 2 | TDD |  |
| TDD special subframe configurationNote1 |  | 2 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 2 | 1 |  |
| BWchannel | MHz | 1, 2 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 2 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 2 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote2 |  | 1 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 2 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| b2-Threshold1 | dBm | 1, 2 | -77 |  |
| PBCH_RA | dB | 1, 2 | 0 |  |
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
| NocNote4 | dBm/15 kHz | 1, 2 | -104 |  |
| Ês/Noc | dB | 1, 2 | 17 | 17 |
| Ês/IotNote5 | dB | 1, 2 | 17 | 17 |
| RSRPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| SCH_RPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| IoNote5 | dBm/9 MHz | 1, 2 | -59.13+10log (NPRB,c /50) | -59.13+10log (NPRB,c /50) |
| Propagation Condition Note6 |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix Note6 |  | 1, 2 | 1x2 Low |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 6: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |

Table A.12.4.2.2.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Cell 2 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| NR RF Channel Number |  | 1, 2 | 1 |  |
| TDD configuration |  | 1, 2 | TDDConf.1.1 CCA |  |
| BWchannel | MHz | 1, 2 | 40: NPRB,c = 106 |  |
| PCCA_DL for dynamic channel access Note 6,8 |  | 1, 2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| PCCA_DL for semi-static channel access Note 7,8 |  | 1, 2 | PCCA_DL=0.9375 |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  | 1, 2 | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  | 1, 2 | SMTC.1 |  |
| DBT window configuration |  | 1, 2 | DBT.1 |  |
| SSB configuration  for semi-static channel access |  | 1, 2 | SSB.1 CCA |  |
| SSB configuration for dynamic channel access |  | 1, 2 | SSB.2 CCA |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2 | 30 |  |
| b2-Threshold2NR | dBm | 1, 2 | -98 |  |
| EPRE ratio of PSS to SSS |  | 1, 2 | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1, 2 | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1, 2 | -95 |  |
| SS-RSRP Note 3,5 | dBm/SCS | 1, 2 | -Infinity | -88 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] Note 5 | dB | 1, 2 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] Note 5 | dB | 1, 2 | -Infinity | 7 |
| IoNote3 | dBm/38.16 MHz | 1, 2 | -63.95 | -56.16 |
| Propagation Condition |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2, | 1x2 Low |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6:  For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7:  For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

##### A.12.4.2.2.2 Test Requirements

In test 1, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_without_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_without_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is not required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.12.4.2.3 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used

##### A.12.4.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21A of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22A of TS 36.133[15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1 on a carrier frequency with CCA.  The test parameters are given in tables A.12.4.2.3.1-1, A.12.4.2.3.1-2, A.12.4.2.3.1-3 and A.12.4.2.3.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In this test, measurement gap pattern configuration # 0 as defined in table A.12.4.2.3.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.12.4.2.3.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR1

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| 2 | LTE TDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.12.4.2.3.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| E-UTRA RF Channel Number |  | 1, 2 | 1 | One E-UTRAcarrier frequency is used. |
| NR RF Chanel Number |  | 1, 2 | 1 | One FR1 NR carrier frequency under CCA is used. |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |
| LCCA_DL |  | 1, 2 | 12 |  |
| WCCA_DL | ms | 1, 2 | TPSS/SSS_sync_irat_cca |  |
| Active cell |  | 1, 2 | E-UTRA Cell 1 (PCell) | E-UTRA Cell 1 is on E-UTRA RF channel number 1. |
| Neighbour cell |  | 1, 2 | NR Cell 2 | NR Cell 2 is on NR RF channel number 1. |
| Gap Pattern Id |  | 1, 2 | 0 | As specified in clause Table 8.1.2.1-1 of TS 36.133[15]. |
| Measurement gap offset |  | 1, 2 | 39 | As specified in TS 36.331 [16]. |
| b2-Threshold1 | dBm | 1, 2 | Note 1 | E-UTRA RSRP/RSRQ/SINR threshold for E-UTRA RSRP measurement on Cell 1 for event B2 [16] |
| b2-Threshold2NR | dBm | 1, 2 | Note 2 | SS-RSRP/ SS-RSRQ/ SS-SINR threshold measurement on Cell 2 for event B2 [16] |
| Hysteresis | dB | 1, 2 | 0 |  |
| CP length |  | 1, 2 | Normal |  |
| TimeToTrigger | s | 1, 2 | 0 |  |
| Filter coefficient |  | 1, 2 | 0 | L3 filtering is not used |
| DRX |  | 1, 2 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | 1, 2 | 3s | Synchronous cells. |
| T1 | s | 1, 2 | 5 |  |
| T2 | s | 1, 2 | ≥ Tidentify_irat_cca_with_index | Tidentify_irat_cca_with_index is defined in clause 8.1.2.4.21A.1 and 8.1.2.4.22A.1 in TS 36.133 |
| NOTE 1: The value of b2-Threshold1 is defined in table A.12.4.2.3.1-3NOTE 2: The value of b2-Threshold2NR is defined in table A.12.4.2.3.1-4 |  |  |  |  |

Table A.12.4.2.3.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 with SSB time index detection

| Parameter | Unit | Configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1, 2 | 1 |  |
| Duplex mode |  | 1 | FDD |  |
|  |  | 2 | TDD |  |
| TDD special subframe configurationNote1 |  | 2 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 2 | 1 |  |
| BWchannel | MHz | 1, 2 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 2 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 2 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote2 |  | 1 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 2 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| b2-Threshold1 | dBm | 1, 2 | -77 |  |
| PBCH_RA | dB | 1, 2 | 0 |  |
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
| NocNote4 | dBm/15 kHz | 1, 2 | -104 |  |
| Ês/Noc | dB | 1, 2 | 17 | 17 |
| Ês/IotNote5 | dB | 1, 2 | 17 | 17 |
| RSRPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| SCH_RPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| IoNote5 | dBm/9 MHz | 1, 2 | -59.13+10log (NPRB,c /50) | -59.13+10log (NPRB,c /50) |
| Propagation Condition Note6 |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix Note6 |  | 1, 2 | 1x2 Low |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 6: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |

Table A.12.4.2.3.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

| Parameter | Unit | Test configuration | Cell 2 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| NR RF Channel Number |  | 1, 2 | 1 |  |
| TDD configuration |  | 1, 2 | TDDConf.1.1 CCA |  |
| BWchannel | MHz | 1, 2 | 40: NPRB,c = 106 |  |
| PCCA_DL for dynamic channel access Note 6,8 |  | 1, 2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| PCCA_DL for semi-static channel access Note 7,8 |  | 1, 2 | PCCA_DL=0.9375 |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  | 1, 2 | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  | 1, 2 | SMTC.1 |  |
| DBT window configuration |  | 1, 2 | DBT.1 |  |
| SSB configuration for semi-static channel access |  | 1, 2 | SSB.1 CCA |  |
| SSB configuration for dynamic channel access |  | 1, 2 | SSB.2 CCA |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2 | 30 |  |
| b2-Threshold2NR | dBm | 1, 2 | -98 |  |
| EPRE ratio of PSS to SSS |  | 1, 2 | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1, 2 | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1, 2 | -95 |  |
| SS-RSRP Note 3,5 | dBm/SCS | 1, 2 | -Infinity | -88 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] Note 5 | dB | 1, 2 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] Note 5 | dB | 1, 2 | -Infinity | 7 |
| IoNote3 | dBm/38.16 MHz | 1, 2 | -63.95 | -56.16 |
| Propagation Condition |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2, | 1x2 Low |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for NOC to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5:  The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6:  For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

##### A.12.4.2.3.2 Test Requirements

The UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_with_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.12.4.2.4 NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used

##### A.12.4.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21A of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22A of TS 36.133[15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1 on a carrier frequency with CCA. The test parameters are given in tables A.12.4.2.4.1-1, A.12.4.2.4.1-2, A.12.4.2.4.1-3 and A.12.4.2.4.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In this test, measurement gap pattern configuration # 0 as defined in table A.12.4.2.4.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.12.4.2.4.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR1

| Configuration | Description |
| --- | --- |
| 1 | LTE FDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| 2 | LTE TDD; NR with CCA: SCS 30 kHz, BW 40 MHz, TDD |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.12.4.2.4.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| E-UTRA RF Channel Number |  | 1, 2 | 1 |  | One E-UTRAcarrier frequency is used. |
| NR RF Chanel Number |  | 1, 2 | 1 |  | One FR1 NR carrier frequency under CCA is used. |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |  |
| LCCA_DL |  | 1, 2 | 12 | 5 |  |
| WCCA_DL | ms | 1, 2 | TPSS/SSS_sync_irat_cca |  |  |
| Active cell |  | 1, 2 | E-UTRA Cell 1 (PCell) |  | E-UTRA Cell 1 is on E-UTRA RF channel number 1. |
| Neighbour cell |  | 1, 2 | NR Cell 2 |  | NR Cell 2 is on NR RF channel number 1. |
| Gap Pattern Id |  | 1, 2 | 0 |  | As specified in clause Table 8.1.2.1-1 of TS 36.133[15]. |
| Measurement gap offset |  | 1, 2 | 39 |  | As specified in TS 36.331 [16]. |
| b2-Threshold1 | dBm | 1, 2 | Note 1 |  | E-UTRA RSRP/RSRQ/SINR threshold for E-UTRA RSRP measurement on Cell 1 for event B2 [16] |
| b2-Threshold2NR | dBm | 1, 2 | Note 2 |  | SS-RSRP/ SS-RSRQ/ SS-SINR threshold measurement on Cell 2 for event B2 [16] |
| Hysteresis | dB | 1, 2 | 0 |  |  |
| CP length |  | 1, 2 | Normal |  |  |
| TimeToTrigger | s | 1, 2 | 0 |  |  |
| Filter coefficient |  | 1, 2 | 0 |  | L3 filtering is not used |
| DRX |  | 1, 2 | DRX.9 | DRX.12 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | 1, 2 | 3s |  | Synchronous cells. |
| T1 | s | 1, 2 | 5 |  |  |
| T2 | s | 1, 2 | ≥Tidentify_irat_cca_with_index |  | Tidentify_irat_cca_with_index is defined in clause 8.1.2.4.21A.1 and 8.1.2.4.22A.1 in TS 36.133 |
| NOTE 1: The value of b2-Threshold1 is defined in table A.12.4.2.4.1-3NOTE 2: The value of b2-Threshold2NR is defined in table A.12.4.2.4.1-4 |  |  |  |  |  |

Table A.12.4.2.4.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 with SSB time index detection

| Parameter | Unit | Configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| RF channel number |  | 1, 2 | 1 |  |
| Duplex mode |  | 1 | FDD |  |
|  |  | 2 | TDD |  |
| TDD special subframe configurationNote1 |  | 2 | 6 |  |
| TDD uplink-downlink configurationNote1 |  | 2 | 1 |  |
| BWchannel | MHz | 1, 2 | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |  |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD |  |
|  |  | 2 | 5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |  |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 1 | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD |  |
|  |  | 2 | 5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |  |
| OCNG PatternsNote2 |  | 1 | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD |  |
|  |  | 2 | 5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |  |
| b2-Threshold1 | dBm | 1, 2 | -77 |  |
| PBCH_RA | dB | 1, 2 | 0 |  |
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
| NocNote4 | dBm/15 kHz | 1, 2 | -104 |  |
| Ês/Noc | dB | 1, 2 | 17 | 17 |
| Ês/IotNote5 | dB | 1, 2 | 17 | 17 |
| RSRPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| SCH_RPNote5 | dBm/15 kHz | 1, 2 | -87 | -87 |
| IoNote5 | dBm/9 MHz | 1, 2 | -59.13+10log (NPRB,c /50) | -59.13+10log (NPRB,c /50) |
| Propagation Condition Note6 |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix Note6 |  | 1, 2 | 1x2 Low |  |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Ês/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 6: Propagation condition and correlation matrix are defined in clause B.2 in TS 36.101 [25]. |  |  |  |  |

Table A.12.4.2.4.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

| Parameter | Unit | Test configuration | Cell 2 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| NR RF Channel Number |  | 1, 2 | 1 |  |
| TDD configuration |  | 1, 2 | TDDConf.1.1 CCA |  |
| BWchannel | MHz | 1, 2 | 40: NPRB,c = 106 |  |
| PCCA_DL for dynamic channel access Note 6,8 |  | 1, 2 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| PCCA_DL for semi-static channel access Note 7,8 |  | 1, 2 | PCCA_DL=0.9375 |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  | 1, 2 | OP.1 |  |
| SMTC configuration defined in A.3.11.1 and A.3.11.2 |  | 1, 2 | SMTC.1 |  |
| DBT window configuration |  | 1, 2 | DBT.1 |  |
| SSB configuration for semi-static channel access |  | 1, 2 | SSB.1 CCA |  |
| SSB configuration for dynamic channel access |  | 1, 2 | SSB.2 CCA |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2 | 30 |  |
| b2-Threshold2NR | dBm | 1, 2 | -98 |  |
| EPRE ratio of PSS to SSS |  | 1, 2 | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS (Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1, 2 | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1, 2 | -95 |  |
| SS-RSRP Note 3,5 | dBm/SCS | 1, 2 | -Infinity | -88 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] Note 5 | dB | 1, 2 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] Note 5 | dB | 1, 2 | -Infinity | 7 |
| IoNote3 | dBm/38.16 MHz | 1, 2 | -63.95 | -56.16 |
| Propagation Condition |  | 1, 2 | AWGN |  |
| Antenna Configuration and Correlation Matrix |  | 1, 2, | 1x2 Low |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5:  The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |

##### A.12.4.2.4.2 Test Requirements

In test 1, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_with_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_with_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.12.4.2.5 Void

#### A.12.4.2.6 Void

## A.12.5 Measurement performance

### A.12.5.1 E-UTRANNR SFTD

#### A.12.5.1.1 Inter-RAT SFTD accuracy with NR target cell under CCA

##### A.12.5.1.1.1 Test Purpose

The purpose of this set of tests is to verify that the SFTD measurement accuracy is within the specified limits. This test will verify the requirements as specified in clause 9.1.28 in TS 36.133 [15] for inter-RAT SFTD measurements between E-UTRA PCell and NR target cell under CCA.

##### A.12.5.1.1.2 Test Environment

Supported test configurations are shown in table A.12.5.1.1.2-1. In this set of test cases there are two cells on different carriers. Cell 1 is E-UTRAN PCell and Cell 2 is inter-RAT NR target cell under CCA. The test parameters of Cell 1 are given in clause A.12.5.1.1.2-2. The test parameters of Cell 2 are given in table A.12.5.1.1.2-3. The SFTD between PCell and NR target cell shall be set by the test equipment to one of the time differences in table A.12.5.1.1.2-4.

Table A.12.5.1.1.2-1: Supported test configurations for SFTD accuracy with NR target cell under CCA

| Config | Description |
| --- | --- |
| 1 | LTE FDDNR with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | LTE TDDNR with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.12.5.1.1.2-2: Test parameters for inter-RAT SFTD accuracy with NR target cell under CCA (Cell 1)

| Parameter | Unit | Test 1 |
| --- | --- | --- |
| E-UTRA RF Channel Number |  | 1 |
| Duplex mode |  | FDD or TDD |
| TDD special subframe configurationNote1 |  | 6 |
| TDD uplink-downlink configurationNote1 |  | 1 |
| BWchannel |  | 5 MHz: NPRB,c = 2510 MHz: NPRB,c = 5020 MHz: NPRB,c = 100 |
| PDSCH parameters:DL Reference Measurement ChannelNote2 |  | 5 MHz: R.7 FDD10 MHz: R.3 FDD20 MHz: R.6 FDD5 MHz: R.4 TDD10 MHz: R.0 TDD20 MHz: R.3 TDD |
| PCFICH/PDCCH/PHICH parameters:DL Reference Measurement ChannelNote2 |  | 5 MHz: R.11 FDD10 MHz: R.6 FDD20 MHz: R.10 FDD5 MHz: R.11 TDD10 MHz: R.6 TDD20 MHz: R.10 TDD |
| OCNG PatternsNote2 |  | 5 MHz: OP.20 FDD10 MHz: OP.10 FDD20 MHz: OP.17 FDD5 MHz: OP.9 TDD10 MHz: OP.1 TDD20 MHz: OP.7 TDD |
| PBCH_RA | dB | 0 |
| PBCH_RB | dB |  |
| PSS_RA | dB |  |
| SSS_RA | dB |  |
| PCFICH_RB | dB |  |
| PHICH_RA | dB |  |
| PHICH_RB | dB |  |
| PDCCH_RA | dB |  |
| PDCCH_RB | dB |  |
| PDSCH_RA | dB |  |
| PDSCH_RB | dB |  |
| OCNG_RANote3 | dB |  |
| OCNG_RBNote3 | dB |  |
| NocNote4 | dBm/15 kHz | -104 |
| Ês/Noc | dB | -3 |
| Ês/Iot | dB | -3 |
| RSRP Note5 | dBm/15 kHz | -107 |
| SCH_RP Note5 | dBm/15 kHz | -107 |
| Io Note5 | dBm/Ch BW | -74.45+10log(NPRB,c /50) |
| Propagation Condition |  | AWGN |
| Antenna Configuration |  | 1x2 |
| NOTE 1: Special subframe and uplink-downlink configurations are specified in table 4.2-1 in TS 36.211 [23].NOTE 2: DL RMCs and OCNG patterns are specified in clauses A 3.1 and A 3.2 of TS 36.133 [15] respectively.NOTE 3: OCNG shall be used such that all cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 4: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 5: Es/Iot, RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |

Table A.12.5.1.1.2-3: Test parameters for inter-RAT SFTD accuracy with NR target cell under CCA (Cell 2)

| Parameter |  | Unit | Test 1 |
| --- | --- | --- | --- |
| Duplex mode |  |  | TDD |
| TDD Configuration |  |  | TDDConf.1.1 CCA |
| BWchannel |  | MHz | 40: NPRB,c = 106 |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |
| DL CCA probability for semi-static channel accessNote6,8 | PCCA |  | 0.75 |
| DL CCA probability for dynamic channel accessNote7,8 | PCCA_DL_1 |  | 0.75 |
|  | PCCA_DL_2 |  | 0.75 |
| SSB configuration for semi-static channel accessNote6,8 |  |  | SSB.1 CCA |
| SSB configuration for dynamic channel accessNote7,8 |  |  | SSB.2 CCA |
| SMTC configuration |  |  | SMTC.1 |
| DBT window configuration |  |  | DBT.1 |
| OCNG Patterns |  |  | OP.1 |
| EPRE ratio of PSS to SSS |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Noc Note2 |  | dBm/15 kHz | -104 |
| Noc Note2 |  | dBm/SSB SCS | -101 |
| Ês/Iot |  | dB | -3 |
| Ês/Noc |  | dB | -3 |
| SS-RSRP Note3 |  | dBm/SCS | -104 |
| Io Note3 |  | dBm/38.16 MHz | -68.18 |
| Propagation condition |  |  | AWGN |
| Antenna configuration |  |  | 1x2 |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols in slots with downlink transmission bursts. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5:  The test configuration excludes support for band n51 and it is not required to run this test on band n51 in this release of the specificationNOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 8: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |

Table A.12.5.1.1.2-4: Timing offsets for inter-RAT SFTD accuracy test with NR target cell under CCA

| Configuration | SFN offset between PCell and NR neighbor cell | Frame boundary offset between PCell and NR neighbour cell (Ts) |
| --- | --- | --- |
| 1 | 100 | -122000 |
| 2 | 300 | -60540 |
| 3 | 500 | 1000 |
| 4 | 700 | 62540 |
| 5 | 900 | 124000 |

##### A.12.5.1.1.3 Test Requirements

The SFTD reported by the UE consists of 2 elements, SFN offset and frame boundary offset between PCell and inter-RAT NR target cell. The reported SFTD accuracy shall fulfil the requirement in clause 9.1.27 in TS 36.133 [15].

### A.12.5.2 Void

### A.12.5.3 Void

### A.12.5.4 Void

### A.12.5.5 Void

### A.12.5.6 Void
