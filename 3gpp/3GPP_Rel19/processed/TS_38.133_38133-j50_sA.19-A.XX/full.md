# A.19 NR standalone tests for ATG

## A.19.1 RRC_IDLE state mobility

#### A.19.1.1 Cell reselection to FR1 intra-frequency NR case

##### A.19.1.1.1 Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for ATG specified in clause 4.2D.2.3.

##### A.19.1.1.2 Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells, supported test configurations are shown in table A.19.1.1.2-1. The test parameters from table A.6.1.1.1.2-2 and table A.6.1.1.1.2-3 are used except those described in the tables A.19.1.1.2-2 and A.19.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.1.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.19.1.1.2-2: General test parameters for intra frequency NR cell re-selection test case

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Access Barring Information | - | 1, 2, 3 | not barred | No additional delays in random access procedure. |
| T2 | s | 1, 2, 3 | 40 | T2 needs to be defined so that cell re-selection reaction time is taken into account.The value applies for UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18 |
| T3 | s | 1, 2, 3 | 15 | T3 needs to be defined so that cell re-selection reaction time is taken into account.The value applies for UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18 |

Table A.19.1.1.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Propagation Condition |  | 1, 2 | AWGN+220 Hz |  |  |  |  |  |
|  |  | 3 | AWGN+500 Hz |  |  |  |  |  |

##### A.19.1.1.3 Test Requirements

For UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_Intra See Table 4.2D.2.3-1 in clause 4.2D.2.3

Tevaluate, NR_ intra See Table 4.2D.2.3-1 in clause 4.2D.2.3

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB22 are scheduled with 20 ms period and 80 ms period, respectively.

For the cell re-selection delay to a newly detectable cell, Tdetect, NR_ intra + TSI-NR = 33.28 s, allow 34 s.

For the cell re-selection delay to an already detected cell in the test case, Tevaluate, NR_Intra + TSI-NR = 7.68 s, allow 8 s.

#### A.19.1.2 Cell reselection to FR1 inter-frequency NR case

##### A.19.1.2.1 Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for ATG specified in clause 4.2D.2.4.

##### A.19.1.2.2 Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.19.1.2.2-1, A.19.1.2.2-2 and A.19.1.2.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.1.2.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.19.1.2.2-2: General test parameters for FR1 inter frequency NR cell re-selection test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2, 3 | Cell 1 |  |
| T2 end condition | Active cell |  | 1, 2, 3 | Cell 2 |  |
|  | Neighbour cells |  | 1, 2, 3 | Cell 1 |  |
| T3 end condition | Active cell |  | 1, 2, 3 | Cell 1 |  |
|  | Neighbour cell |  | 1, 2, 3 | Cell 2 |  |
| Time offset between cells |  |  | 1 | 3 ms | Asynchronous cells |
|  |  |  | 2 | 3 s | Synchronous cells |
|  |  |  | 3 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1, 2, 3 | not barred | No additional delays in random access procedure. |
| SSB configuration |  |  | 1 | SSB.1 FR1 |  |
|  |  |  | 2 | SSB.1 FR1 |  |
|  |  |  | 3 | SSB.2 FR1 |  |
| SMTC configuration |  |  | 1 | SMTC.2 | Configured in SIB4 of Cell 1 |
|  |  |  |  | SMTC.6 | Configured in SIB4 of Cell 2 |
|  |  |  | 2 | SMTC.1 |  |
|  |  |  | 3 | SMTC.1 |  |
| DRX cycle length |  | s | 1, 2, 3 | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2, 3 | 102 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2, 3 | Not configured |  |
| T1 |  | s | 1, 2, 3 | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2 |
| T2 |  | s | 1, 2, 3 | 40 | T2 needs to be defined so that cell re-selection reaction time is taken into account.The value applies for UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18 |
| T3 |  | s | 1, 2, 3 | 15 | T3 needs to be defined so that cell re-selection reaction time is taken into account.The value applies for UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18 |

Table A.19.1.2.2-3: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| RF Channel Number |  | 1, 2, 3 | 1 |  |  | 2 |  |  |
| TDD configuration |  | 1 | N/A |  |  | N/A |  |  |
|  |  | 2 | TDDConf.1.1 |  |  | TDDConf.1.1 |  |  |
|  |  | 3 | TDDConf.2.1 |  |  | TDDConf.2.1 |  |  |
| PDSCH RMC |  | 1 | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |
|  |  | 2 | SR.1.1 TDD |  |  | SR.1.1 TDD |  |  |
|  |  | 3 | SR.2.1 TDD |  |  | SR.2.1 TDD |  |  |
| RMSI CORESET |  | 1 | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |
|  |  | 2 | CR.1.1 TDD |  |  | CR.1.1 TDD |  |  |
|  |  | 3 | CR.2.1 TDD |  |  | CR.2.1 TDD |  |  |
| Dedicated CORESET |  | 1 | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |
|  |  | 2 | CCR.1.1 TDD |  |  | CCR.1.1 TDD |  |  |
|  |  | 3 | CCR.2.1 TDD |  |  | CCR.2.1 TDD |  |  |
| OCNG Pattern |  | 1, 2, 3 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1, 2, 3 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2, 3 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1, 2, 3 | SSB |  |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1, 2 | -140 |  |  | -140 |  |  |
|  |  | 3 | -137 |  |  | -137 |  |  |
| Pcompensation | dB | 1, 2, 3 | 0 |  |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2, 3 | SS-RSRP |  |  | SS-RSRP |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1 | 16 | 11 | 16 | -infinity | 16 | 11 |
|  |  | 2 |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -98 |  |  |  |  |  |
|  |  | 2 | -98 |  |  |  |  |  |
|  |  | 3 | -95 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -98 |  |  |  |  |  |
|  |  | 2 |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 16 | 11 | 16 | -infinity | 16 | 11 |
|  |  | 2 |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |
| SS-RSRP Note3 | dBm/SCS | 1, 2 | -82 | -87 | -82 | -infinity | -82 | -87 |
|  |  | 3 | -79 | -84 | -79 | -infinity | -79 | -84 |
| Io | dBm/9.36 MHz | 1, 2 | -53.94 | -58.72 | -53.94 | -70.05 | -53.94 | -58.72 |
|  | dBm/38.16 MHz | 3 | -47.85 | -52.61 | -47.85 | -63.96 | -47.85 | -52.61 |
| Treselection | s | 1, 2, 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| SnonintrasearchP | dB | 1, 2, 3 | 60 |  |  | 60 |  |  |
| Propagation Condition |  | 1, 2 | AWGN+220 Hz |  |  |  |  |  |
|  |  | 3 | AWGN+500 Hz |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

##### A.19.1.2.3 Test Requirements

For UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Inter + TSI-NR, and to an already detected cell can be expressed as: Tevaluate, NR_ intrer+ TSI-NR,

Where:

Tdetect, NR_Inter See Table 4.2D.2.4-1 in clause 4.2D.2.4

Tevaluate, NR_ inter See Table 4.2D.2.4-1 in clause 4.2D.2.4

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB22 are scheduled with 20 ms period and 80 ms period, respectively.

For the cell re-selection delay to a newly detectable cell, Tdetect, NR_ inter + TSI-NR = 33.28 s, allow 34 s.

For the cell re-selection delay to an already detected cell in the test case, Tevaluate, NR_Inter + TSI-NR = 7.68 s, allow 8 s.

#### A.19.1.3 Cell reselection to FR1 inter-frequency NR case for UE configured with hs-ATG-cellReselectionSet-r18

##### A.19.1.3.1 Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for ATG UE configured with hs-ATG-cellReselectionSet-r18 and for ATG UE supporting the feature for enhanced RRM requirements (Enhanced RRM requirements for measurements in IDLE and INACTIVE modes for ATG) specified in clause 4.2D.2.4.

##### A.19.1.3.2 Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.19.1.3.2-1, A.19.1.3.2-2 and A.19.1.3.2-3. The test consists of two successive time periods, with time duration of T1 and T2. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.1.3.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.19.1.3.2-2: General test parameters for FR1 inter frequency NR cell re-selection test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2, 3 | Cell 1 |  |
| T2 end condition | Active cell |  | 1, 2, 3 | Cell 2 |  |
|  | Neighbour cells |  | 1, 2, 3 | Cell 1 |  |
| Time offset between cells |  |  | 1 | 3 ms | Asynchronous cells |
|  |  |  | 2 | 3 s | Synchronous cells |
|  |  |  | 3 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1, 2, 3 | not barred | No additional delays in random access procedure. |
| SSB configuration |  |  | 1 | SSB.1 FR1 |  |
|  |  |  | 2 | SSB.1 FR1 |  |
|  |  |  | 3 | SSB.2 FR1 |  |
| SMTC configuration |  |  | 1 | SMTC.2 | Configured in SIB4 of Cell 1 |
|  |  |  |  | SMTC.6 | Configured in SIB4 of Cell 2 |
|  |  |  | 2 | SMTC.1 |  |
|  |  |  | 3 | SMTC.1 |  |
| DRX cycle length |  | s | 1, 2, 3 | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2, 3 | 102 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2, 3 | Not configured |  |
| T1 |  | s | 1, 2, 3 | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2 |
| T2 |  | s | 1, 2, 3 | 20 | T2 needs to be defined so that cell re-selection reaction time is taken into account.The value applies for UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18 |

Table A.19.1.3.2-3: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| RF Channel Number |  | 1, 2, 3 | 1 |  | 2 |  |
| TDD configuration |  | 1 | N/A |  | N/A |  |
|  |  | 2 | TDDConf.1.1 |  | TDDConf.1.1 |  |
|  |  | 3 | TDDConf.2.1 |  | TDDConf.2.1 |  |
| PDSCH RMC |  | 1 | SR.1.1 FDD |  | SR.1.1 FDD |  |
|  |  | 2 | SR.1.1 TDD |  | SR.1.1 TDD |  |
|  |  | 3 | SR.2.1 TDD |  | SR.2.1 TDD |  |
| RMSI CORESET |  | 1 | CR.1.1 FDD |  | CR.1.1 FDD |  |
|  |  | 2 | CR.1.1 TDD |  | CR.1.1 TDD |  |
|  |  | 3 | CR.2.1 TDD |  | CR.2.1 TDD |  |
| Dedicated CORESET |  | 1 | CCR.1.1 FDD |  | CCR.1.1 FDD |  |
|  |  | 2 | CCR.1.1 TDD |  | CCR.1.1 TDD |  |
|  |  | 3 | CCR.2.1 TDD |  | CCR.2.1 TDD |  |
| OCNG Pattern |  | 1, 2, 3 | OP.1 defined in A.3.2.1 |  | OP.1 defined in A.3.2.1 |  |
| Initial DL BWP configuration |  | 1, 2, 3 | DLBWP.0.1 |  | DLBWP.0.1 |  |
| Initial UL BWP configuration |  | 1, 2, 3 | ULBWP.0.1 |  | ULBWP.0.1 |  |
| RLM-RS |  | 1, 2, 3 | SSB |  | SSB |  |
| Qrxlevmin | dBm/SCS | 1, 2 | -140 |  | -140 |  |
|  |  | 3 | -137 |  | -137 |  |
| Pcompensation | dB | 1, 2, 3 | 0 |  | 0 |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2, 3 | SS-RSRP |  | SS-RSRP |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1 | 16 | 8 | -infinity | 16 |
|  |  | 2 |  |  |  |  |
|  |  | 3 |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1, 2 | -98 |  |  |  |
|  |  | 2 | -95 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -98 |  |  |  |
|  |  | 2 |  |  |  |  |
|  |  | 3 |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 16 | 11 | -infinity | 16 |
|  |  | 2 |  |  |  |  |
|  |  | 3 |  |  |  |  |
| SS-RSRP Note3 | dBm/SCS | 1, 2 | -82 | -87 | -infinity | -82 |
|  |  | 3 | -79 | -84 | -infinity | -79 |
| Io | dBm/9.36 MHz | 1, 2 | -53.94 | -58.72 | -70.05 | -53.94 |
|  | dBm/38.16 MHz | 3 | -47.85 | -52.61 | -63.96 | -47.85 |
| Treselection | s | 1, 2, 3 | 0 | 0 | 0 | 0 |
| SnonintrasearchP | dB | 1, 2, 3 | 60 |  | 60 |  |
| Propagation Condition |  | 1, 2 | AWGN+220 Hz |  |  |  |
|  |  | 3 | AWGN+500 Hz |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.19.1.3.3 Test Requirements

For UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 12 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Inter_enh + TSI-NR

Where:

Tdetect, NR_Inter_enh See Table 4.2D.2.4-2 in clause 4.2D.2.4

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB22 are scheduled with 20 ms period and 80 ms period, respectively.

For the cell re-selection delay to a newly detectable cell, Tdetect, NR_ inter_enh + TSI-NR = 11.52 s, allow 12 s.

## A.19.2 RRC_CONNECTED state mobility

### A.19.2.1 Handover

#### A.19.2.1.1 Intra-frequency handover from FR1 to FR1; known target cell

##### A19.2.1.1.1 Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra frequency handover requirements for ATG specified in clause6.1E.1.2.

##### A.19.2.1.1.2 Test Parameters

Supported test configurations are shown in table A.19.2.1.1.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.1.2-2 and table A.6.3.1.1.2-3 except those described in the table A.19.2.1.1.2-2 and A.19.2.1.1.2-3.

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

NR shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.1.1.2-1: Intra-frequency handover from FR1 to FR1 test configurations

| Config | Description |
| --- | --- |
| 1 | Source cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeTarget cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | Source cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeTarget cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | Source cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.19.2.1.1.2-2: General test parameters Intra-frequency handover from FR1 to FR1

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| Access Barring Information | - | not barred | No additional delays in random access procedure. |

Table A.19.2.1.1.2-3: Cell specific test parameters for NR FR1-FR1 Intra frequency handover test case

| Parameter |  | Unit | Cell 1 |  |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |  | T1 | T2 | T3 |
| Propagation condition | Config 1, 2 | - | AWGN+220 Hz |  |  | AWGN+220 Hz |  |  |  |
|  | Config 3 |  | AWGN+500 Hz |  |  | AWGN+500 Hz |  |  |  |

##### A.19.2.1.2.3 Test Requirements

For UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 62 ms in the test. Tinterrupt is defined in clause 6.1E.1.2.2.

#### A.19.2.1.2 Inter-frequency handover from FR1 to FR1; unknown target cell

##### A.19.2.1.2.1 Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 inter frequency handover requirements for ATG specified in clause6.1E.1.2.

##### A.19.2.1.2.2 Test Parameters

Supported test configurations are shown in table A.19.2.1.2.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.3.2-2 and table A.6.3.1.3.2-3 except those described in the table A.19.2.1.2.2-2 and A.19.2.1.2.2-3.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.1.2.2-1: Inter-frequency handover from FR1 to FR1 test configurations

| Config | Description |
| --- | --- |
| 1 | Source cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeTarget cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | Source cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeTarget cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | Source cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.19.2.1.2.2-2: General test parameters Inter-frequency handover from FR1 to FR1

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| Access Barring Information | - | not barred | No additional delays in random access procedure. |
| Time offset between cells |  | 3 s | Synchronous cells |

Table A.19.2.1.2.2-3: Cell specific test parameters for NR FR1-FR1 Inter frequency handover test case

| Parameter |  | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Propagation condition | Config 1, 2 | - | AWGN + 220 Hz |  | AWGN + 220 Hz |  |
|  | Config 3 |  | AWGN + 500 Hz |  | AWGN + 500 Hz |  |

##### A.19.2.1.2.3 Test Requirements

For UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The UE shall start to transmit the PRACH to Cell 2 less than 132 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 122 ms in the test. Tinterrupt is defined in clause 6.1E.1.2.2.

This gives a total of 132 ms.

### A.19.2.2 Conditional Handover

#### A.19.2.2.1 Intra-frequency distance-based conditional Handover from FR1 to FR1

##### A.19.2.2.1.1 Test Purpose and Environment

This test is to verify the requirement for intra-frequency distance-based conditional handover from FR1 to FR1 for ATG specified in clause 6.1E.2.

##### A.19.2.2.1.2 Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in table A.19.2.2.1.2-1, and A.19.2.2.1.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure intra-frequency neighbour cell. The RRC message implying distance-based handover to Cell 2 with Event D1 shall be sent to UE, at a time earlier than TRRC (10 ms) before the beginning of T2.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and location condition event condEventD1-r17 is fulfilled.

The specific gNB reference location is emulated by test system.

Table A.19.2.2.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | Source cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeTarget cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | Source cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeTarget cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | Source cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.19.2.2.1.2-2: General test parameters for Intra-frequency distance-based conditional handover from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 |  |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 |  |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L, B, H) at T1 start |  |  | (0, 0, 3000) | Set by AT command(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| UE moving speed |  | km/h | (1200, 0, 0) | Set by AT command |
| referenceLocation1-r17.condEventD1-r17 |  | m | (-4600, 0, 0) | Reference location for serving cell |
| referenceLocation2-r17.condEventD1-r17 |  | m | (14479, 0, 0) | Reference location for target cell |
| distanceThreshFromReference1-r17.condEventD1-r17 |  | 50m | 200 | D1-1 Location condition is fulfilled at T2 |
| distanceThreshFromReference2-r17.condEventD1-r17 |  | 50m | 200 | D1-2 Location condition is fulfilled at T2 |
| hysteresis-r17.condEventD1-r17 |  | 10m | 0 |  |
| timeToTrigger-r17.condEventD1-r17 |  | s | 0 |  |
| A3-Offset in condition |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | not barred | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 15 |  |
| T2 |  | s | 6 |  |

Table A.19.2.2.1.2-3: Cell specific test parameters for Intra-frequency distance-based conditional handover from FR1 to FR1

| Parameter |  | Test configuration | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| Duplex mode |  | Config 1 |  | FDD |  |  |  |
|  |  | Config 2, 3 |  | TDD |  |  |  |
| TDD configuration |  | Config 1 |  | Not Applicable |  |  |  |
|  |  | Config 2 |  | TDDConf.1.1 |  |  |  |
|  |  | Config 3 |  | TDDConf.2.1 |  |  |  |
| BWchannel |  | Config 1, 2 | MHz | 10: NPRB,c = 52 |  |  |  |
|  |  | Config 3 |  | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  | Config 1, 2 | MHz | 10: NPRB,c = 52 |  |  |  |
|  |  | Config 3 |  | 40: NPRB,c = 106 |  |  |  |
| DRX Cycle |  | Config 1, 2, 3 | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 FDD |  |  |  |
|  |  | Config 2 |  | SR.1.1 TDD |  |  |  |
|  |  | Config 3 |  | SR.2.1 TDD |  |  |  |
| CORESET Reference Channel |  | Config 1 |  | CR.1.1 FDD |  |  |  |
|  |  | Config 2 |  | CR.1.1 TDD |  |  |  |
|  |  | Config 3 |  | CR.2.1 TDD |  |  |  |
| TRS configuration |  | Config 1 |  | TRS.1.1 FDD |  |  |  |
|  |  | Config 2 |  | TRS.1.1 TDD |  |  |  |
|  |  | Config 3 |  | TRS.1.2 TDD |  |  |  |
| OCNG Patterns |  | Config 1, 2, 3 |  | OP.1 |  |  |  |
| SMTC Configuration |  | Config 1, 2, 3 |  | SMTC.1 |  |  |  |
| SSB Configuration |  | Config 1, 2 |  | SSB.1 FR1 |  |  |  |
|  |  | Config 3 |  | SSB.2 FR1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2 | kHz | 15 kHz |  |  |  |
|  |  | Config 3 |  | 30 kHz |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1, 2 | kHz | 15 kHz |  |  |  |
|  |  | Config 3 |  | 30 kHz |  |  |  |
| PRACH configuration |  | Config 1, 2, 3 |  | FR1 PRACH configuration 1 |  |  |  |
| BWP configuration | Initial DL BWP | Config 1, 2, 3 |  | DLBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  | Config 1, 2, 3 | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | Config 1, 2 | dBm/ SCS | -98 |  |  |  |
|  |  | Config 3 |  | -95 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  | Config 1, 2, 3 | dB | 8 | -3.3 | -Infinity | 2.36 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | Config 1, 2, 3 | dB | 8 | 8 | -Infinity | 11 |
| SSB_RP |  | Config 1, 2 | dBm/ SCS | -90 | -90 | -Infinity | -87 |
|  |  | Config 3 |  | -87 | -87 | -Infinity | -84 |
| IoNote3 |  | Config 1, 2 | dBm/ 9.36 MHz | -61.41 | -57.06 | -61.41 | -57.06 |
|  |  | Config 3 | dBm/38.16 MHz | -55.31 | -50.96 | -55.31 | -50.96 |
| Propagation condition |  | Config 1, 2 | - | AWGN + 2412 HzNote4 |  |  |  |
|  |  | Config 3 |  | AWGN + 5556 HzNote5 |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: 2412 Hz is the maximum value of doppler with carrier frequency of 2170 MHz. The specific doppler shift trajectory is up to test system’s design considering of BS location and UE GNSS emulation.NOTE 5: 5556 Hz is the maximum value of doppler with carrier frequency of 5 GHz. The specific doppler shift trajectory is up to test system’s design considering of BS location and UE GNSS emulation. |  |  |  |  |  |  |  |

##### A.19.2.2.1.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 872 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay is defined in clause 6.1E.2, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

At start of T2,

distance to source cell reference location is $\sqrt {(3000)^{2}+(1200*1000/3600*15-(-4600))^{2}}$  = 10057.8m, and D1-1 = 10000m

distance to target cell reference location is $\sqrt {(3000)^{2}+(1200*1000/3600*15-(14479))^{2}}$  = 9942.4m, and D1-2 = 10000m

i.e. D1-1 and D1-2 conditions are fulfilled at start of T2 with >=50m location margin.

Tmeasure = max(600 + 200 ms, 0) = 800 ms;

Tinterrupt = 62 ms; TCHO_execution = 10 ms.

This gives a total of 800 ms + 62 ms + 10 ms = 872 ms.

#### A.19.2.2.2 Inter-frequency distance-based conditional Handover from FR1 to FR1

##### A.19.2.2.2.1 Test Purpose and Environment

This test is to verify the requirement for inter-frequency distance-based conditional handover from FR1 to FR1 for ATG specified in clause 6.1E.2.

##### A.19.2.2.2.2 Test Parameters

The test scenario comprises of 2 NR carrier and one cell on each carrier as given in table A.19.2.2.2.2-1, and A.19.2.2.2.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure inter-frequency neighbour cell and Gap pattern ID gp0. The RRC message implying distance-based handover to Cell 2 with Event D1 shall be sent to UE, at a time earlier than TRRC (10 ms) before the beginning of T2.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and after 9976 ms of T2, location condition event condEventD1-r17 is fulfilled.

The specific gNB reference location is emulated by test system.

Table A.19.2.2.2.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | Source cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeTarget cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | Source cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeTarget cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | Source cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.19.2.2.2.2-2: General test parameters for Inter-frequency distance-based conditional handover from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 |  |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L, B, H) at T1 start |  |  | (0, 0, 3000) | Set by AT command(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| UE moving speed |  | km/h | (1200, 0, 0) | Set by AT command |
| referenceLocation1-r17.condEventD1-r17 |  | m | (-4600, 0, 0) | Reference location for serving cell |
| referenceLocation2-r17.condEventD1-r17 |  | m | (14479, 0, 0) | Reference location for target cell |
| distanceThreshFromReference1-r17.condEventD1-r17 |  | 50m | 200 | D1-1 Location condition is fulfilled at T2 |
| distanceThreshFromReference2-r17.condEventD1-r17 |  | 50m | 200 | D1-2 Location condition is fulfilled at T2 |
| hysteresis-r17.condEventD1-r17 |  | 10m | 0 |  |
| timeToTrigger-r17.condEventD1-r17 |  | s | 0 |  |
| A3-Offset in condition |  | dB | -4 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | not barred | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 16 |  |

Table A.19.2.2.2.2-3: Cell specific test parameters for Inter-frequency distance-based conditional handover from FR1 to FR1

| Parameter |  | Test configuration | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| RF channel number |  | Config 1, 2, 3 |  | 1 |  | 2 |  |
| Duplex mode |  | Config 1 |  | FDD |  |  |  |
|  |  | Config 2, 3 |  | TDD |  |  |  |
| TDD configuration |  | Config 1 |  | Not Applicable |  |  |  |
|  |  | Config 2 |  | TDDConf.1.1 |  |  |  |
|  |  | Config 3 |  | TDDConf.2.1 |  |  |  |
| BWchannel |  | Config 1, 2 | MHz | 10: NPRB,c = 52 |  |  |  |
|  |  | Config 3 |  | 40: NPRB,c = 106 |  |  |  |
| BWP BW |  | Config 1, 2 | MHz | 10: NPRB,c = 52 |  |  |  |
|  |  | Config 3 |  | 40: NPRB,c = 106 |  |  |  |
| DRX Cycle |  | Config 1, 2, 3 | ms | Not Applicable |  |  |  |
| Gap pattern ID |  |  |  | gp0 |  |  |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 FDD |  |  |  |
|  |  | Config 2 |  | SR.1.1 TDD |  |  |  |
|  |  | Config 3 |  | SR.2.1 TDD |  |  |  |
| CORESET Reference Channel |  | Config 1 |  | CR.1.1 FDD |  |  |  |
|  |  | Config 2 |  | CR.1.1 TDD |  |  |  |
|  |  | Config 3 |  | CR.2.1 TDD |  |  |  |
| TRS configuration |  | Config 1 |  | TRS.1.1 FDD |  |  |  |
|  |  | Config 2 |  | TRS.1.1 TDD |  |  |  |
|  |  | Config 3 |  | TRS.1.2 TDD |  |  |  |
| OCNG Patterns |  | Config 1, 2, 3 |  | OP.1 |  |  |  |
| SMTC Configuration |  | Config 1, 2, 3 |  | SMTC.1 |  |  |  |
| SSB Configuration |  | Config 1, 2 |  | SSB.1 FR1 |  |  |  |
|  |  | Config 3 |  | SSB.2 FR1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2 | kHz | 15 kHz |  |  |  |
|  |  | Config 3 |  | 30 kHz |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1, 2 | kHz | 15 kHz |  |  |  |
|  |  | Config 3 |  | 30 kHz |  |  |  |
| PRACH configuration |  | Config 1, 2, 3 |  | FR1 PRACH configuration 1 |  |  |  |
| BWP configuration | Initial DL BWP | Config 1, 2, 3 |  | DLBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  | Config 1, 2, 3 | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | Config 1, 2 | dBm/ SCS | -98 |  |  |  |
|  |  | Config 3 |  | -95 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  | Config 1, 2, 3 | dB | 4 | 4 | -Infinity | 5 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | Config 1, 2, 3 | dB | 4 | 4 | -Infinity | 5 |
| SSB_RP |  | Config 1, 2 | dBm/ SCS | -94 | -94 | -Infinity | -93 |
|  |  | Config 3 |  | -91 | -91 | -Infinity | -90 |
| IoNote3 |  | Config 1, 2 | dBm/ 9.36 MHz | -64.59 | -64.59 | -70.05 | -63.85 |
|  |  | Config 3 | dBm/38.16 MHz | -58.49 | -58.49 | -63.94 | -57.75 |
| Propagation condition |  | Config 1, 2 | - | AWGN + 2412 HzNote4 |  |  |  |
|  |  | Config 3 |  | AWGN + 5556 HzNote5 |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: 2412 Hz is the maximum value of doppler with carrier frequency of 2170 MHz. The specific doppler shift trajectory is up to test system’s design considering of BS location and UE GNSS emulation.NOTE 5: 5556 Hz is the maximum value of doppler with carrier frequency of 5 GHz. The specific doppler shift trajectory is up to test system’s design considering of BS location and UE GNSS emulation. |  |  |  |  |  |  |  |

##### A.19.2.2.2.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 later than 9976 ms and less than 10048 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay is defined in clause 6.1E.2, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

At 9976 ms after start of T2,

distance to source cell reference location is $\sqrt {(3000)^{2}+(1200*1000/3600*14.976-(-4600))^{2}}$  = 10050.2m, and D1-1 = 10000m

distance to target cell reference location is $\sqrt {(3000)^{2}+(1200*1000/3600*14.976-(14479))^{2}}$  = 9949.08m, and D1-2 = 10000m

i.e. D1-1 and D1-2 conditions are fulfilled at start of T2 with >=50m location margin.

Tmeasure = max(600 + 200 ms, 9976 ms) = 9976 ms;

Tinterrupt = 62 ms; TCHO_execution = 10 ms.

This gives a total of 9976 ms + 62 ms + 10 ms = 10048 ms.

### A.19.2.3 RRC Connection Mobility Control

#### A.19.2.3.1 SA: RRC Re-establishment

##### A.19.2.3.1.1 Intra-frequency RRC Re-establishment in FR1 for ATG

###### A.19.2.3.1.1.1 Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR1 with known target cell is within the specified limits for ATG. These tests will verify the requirements in clause 6.2D.1.

The test configurations are given in table A.19.2.3.1.1.1-1, and the test parameters are given in table A.6.3.2.1.1.1-2 and table A.6.3.2.1.1.1-3, except those described in the table A.19.2.3.1.1.1-2. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.3.1.1.1-1: Supported test configurations for ATG

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.19.2.3.1.1.1-2: Modified test parameters for ATG for UE with omnidirectional antenna

| Parameter | Config | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Propagation condition | 1,2 |  | AWGN + 220 Hz |  |
|  | 3 |  | AWGN + 500 Hz |  |
| DRX | 1,2,3 |  | OFF | Only non-DRX tests apply |
| T2 | 1,2,3 | ms | 240 | The value applies for UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18 |
| T3 | 1,2,3 | s | 2 | The value applies for UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18 |

###### A.19.2.3.1.1.2 Test Requirements

For ATG UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The test requirements of this test case are the same as those defined in clause A.6.3.2.1.1.2.

##### A.19.2.3.1.2 Inter-frequency RRC Re-establishment in FR1 with unknown target cell without serving cell timing for ATG

###### A.19.2.3.1.2.1 Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR1 with unknown target cell and without serving cell timing are within the specified limits. These tests will verify the requirements in clause 6.2D.1.

The test parameters are given in table A.19.2.3.1.2.1-1, table A.19.2.3.1.2.1-2 and table A.19.2.3.1.2.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.3.1.2.1-1: Supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.19.2.3.1.2.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2, 3 | Cell 1 |  |
|  | Neighbour cells |  | 1, 2, 3 | Cell 2 |  |
| Final condition | Active cell |  | 1, 2, 3 | Cell 2 |  |
| RF Channel Number |  |  | 1, 2, 3 | 1, 2 |  |
| Time offset between cells |  |  | 1 | 3 ms | Asynchronous cells |
|  |  |  | 2, 3 | 3 s | Synchronous cells |
| N310 |  | - | 1, 2, 3 | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1, 2, 3 | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 1, 2, 3 | 0 | Radio link failure timer; |
| T311 |  | ms | 1, 2, 3 | 5000 | RRC re-establishment timer |
| Access Barring Information |  | - | 1, 2, 3 | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | 1 | SSB.1 FR1 |  |
|  |  |  | 2 | SSB.1 FR1 |  |
|  |  |  | 3 | SSB.2 FR1 |  |
| SMTC configuration |  |  | 1 | SMTC.2 |  |
|  |  |  | 2 | SMTC.1 |  |
|  |  |  | 3 | SMTC.1 |  |
| DRX cycle length |  | s | 1, 2, 3 | OFF |  |
| PRACH configuration |  |  | 1, 2, 3 | FR1 PRACH configuration 1 | Table A.3.8.2.1-1 |
| T1 |  | s | 1, 2, 3 | 5 |  |
| T2 |  | ms | 1, 2, 3 | 240 | Time for the UE to detect RLF(Summation of TEvaluate_out_SSB defined in clause 8.1 in TS 38.133, T310 and the period for UE turns off transmitter defined in clause 8.1.5 in TS 38.133 )The value applies for UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18 |
| T3 |  | s | 1, 2, 3 | 5 | The value applies for UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18 |

Table A.19.2.3.1.2.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| RF Channel Number |  | 1, 2, 3 | 1 |  |  | 2 |  |  |
| TDD configuration |  | 1 | N/A |  |  | N/A |  |  |
|  |  | 2 | TDDConf.1.1 |  |  | TDDConf.1.1 |  |  |
|  |  | 3 | TDDConf.2.1 |  |  | TDDConf.2.1 |  |  |
| PDSCH RMC configuration |  | 1 | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |
|  |  | 2 | SR.1.1 TDD |  |  | SR.1.1 TDD |  |  |
|  |  | 3 | SR.2.1 TDD |  |  | SR.2.1 TDD |  |  |
| RMSI CORESET RMC configuration |  | 1 | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |
|  |  | 2 | CR.1.1 TDD |  |  | CR.1.1 TDD |  |  |
|  |  | 3 | CR.2.1 TDD |  |  | CR.2.1 TDD |  |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |
|  |  | 2 | CCR.1.1 TDD |  |  | CCR.1.1 TDD |  |  |
|  |  | 3 | CCR.2.1 TDD |  |  | CCR.2.1 TDD |  |  |
| OCNG Pattern |  | 1, 2, 3 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| TRS configuration |  | 1 | TRS.1.1 FDD |  |  | TRS.1.1 FDD |  |  |
|  |  | 2 | TRS.1.1 TDD |  |  | TRS.1.1 TDD |  |  |
|  |  | 3 | TRS.2.1 TDD |  |  | TRS.2.1 TDD |  |  |
| Initial DL BWP configuration |  | 1, 2, 3 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2, 3 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Active DL BWP confgiuration |  | 1, 2, 3 | DLBWP.1.1 | N/A | N/A | N/A | N/A | DLBWP.1.1 |
| Active UL BWP configuration |  | 1, 2, 3 | ULBWP.1.1 | N/A | N/A | N/A | N/A | ULBWP.1.1 |
| RLM-RS |  | 1, 2, 3 | SSB |  |  | SSB |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1 | 4 | -infinity | -infinity | -infinity | -infinity | 7 |
|  |  | 2 |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -98 |  |  |  |  |  |
|  |  | 2 | -98 |  |  |  |  |  |
|  |  | 3 | -95 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 4 | -infinity | -infinity | -infinity | -infinity | 7 |
|  |  | 2 |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |
| SS-RSRP Note3 | dBm/SCS | 1, 2 | -94 | -infinity | -infinity | -infinity | -infinity | -91 |
|  |  | 3 | -91 | -infinity | -infinity | -infinity | -infinity | -88 |
| Io | dBm/9.36 MHz | 1 | -64.59 | -70. 05 | -70.05 | -70.05 | -70.05 | -62.26 |
|  | dBm/9.36 MHz | 2 | -64.59 | -70. 05 | -70.05 | -70.05 | -70.05 | -62.26 |
|  | dBm/38.16 MHz | 3 | -58.50 | -63.94 | -63.94 | -63.94 | -63.94 | -56.15 |
| Propagation Condition |  | 1, 2 | AWGN + 220 Hz |  |  |  |  |  |
|  |  | 3 | AWGN + 500 Hz |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

###### A.19.2.3.1.2.2 Test Requirements

For UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell without serving cell timing shall be less than 3 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE: The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

$ T_{UE\_re-establish\_delay}=50ms+T_{identify\_intra\_NR}+\sum  _{i=1}^{Nfreq-1}T_{identify\_inter\_NR,i}+T_{SI-NR}+T_{PRACH}$

Nfreq = 2

Tidentify_intra_NR = 800 ms

Tidentify_inter_NR = 800 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 2945 ms, allow 3 s in the test case.

#### A.19.2.3.2 Random Access for ATG UE

A.19.2.3.2.1 4-step RA type contention based random access test in FR1 for NR standalone

###### A.19.2.3.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause6.2D.2.2 and clause7.1D.2 in an AWGN with constant residual doppler model.

For this test one cell is used and configured as PCell in FR1. Supported test configurations are shown in table A.19.2.3.2.1.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.6.3.2.2.1.1-2, except those described in the Table A.19.2.3.2.1.1-2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.3.2.1.1-1: Supported test configurations for contention based random access test in FR1 for NR standalone

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode, |
| 2 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations depending on UE capability |  |

Table A.19.2.3.2.1.1-2: General test parameters for contention based random access test in FR1 for NR Standalone

| Parameter | Test configuration | Unit | Test 1 | Comments |
| --- | --- | --- | --- | --- |
| Propagation Condition | Config 1 | - | AWGN+220 Hz |  |
|  | Config 2 | - | AWGN+500 Hz |  |

###### A.19.2.3.2.1.2 Test Requirements

The test requirements defined in clause A.6.3.2.2.1.2 shall apply for ATG.

A.19.2.3.2.2 4-step RA type non-contention based random access test in FR1 for NR standalone

###### A.19.2.3.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause6.2D.2.2 and clause7.1D.2 in an AWGN with constant residual doppler model.

For this test one cell is used and configured as PCell in FR1. Supported test configurations are shown in table A.19.2.3.2.2.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.6.3.2.2.2.1-2 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2), except those described in the Table A.19.2.3.2.2.1-2. Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.3.2.2.1-1: Supported test configurations for non-contention based random access test in FR1 for NR standalone

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations depending on UE capability |  |

Table A.19.2.3.2.2.1-2: General test parameters for non-contention based random access test in FR1 for NR Standalone

| Parameter | Test configuration | Unit | Test 1 | Test 2 | Comments |
| --- | --- | --- | --- | --- | --- |
| Propagation Condition | Config 1 | - | AWGN+220 Hz | AWGN+220 Hz |  |
|  | Config 2 | - | AWGN+500 Hz | AWGN+500 Hz |  |

###### A.19.2.3.2.2.2 Test Requirements

The test requirements defined in clause A.6.3.2.2.2.2 shall apply for ATG.

##### A.19.2.3.2.3 2-step RA type contention based random access test in FR1 for NR standalone


###### A.19.2.3.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the 2-step RA type random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits. This test will verify the requirements in clause6.2D.2.3 and clause7.1D.2 in an AWGN with constant residual doppler model.

For this test one cell is used and configured as PCell in FR1. Supported test configurations are shown in table A.19.2.3.2.3.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.6.3.2.2.3.1-2, except those described in the Table A.19.2.3.2.3.1-2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.3.2.3.1-1: Supported test configurations for 2-step RA type contention based random access with successRAR test in FR1 for NR standalone

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations depending on UE capability |  |

Table A.19.2.3.2.3.1-2: General test parameters for 2-step RA type contention based random access with successRAR test in FR1 for NR standalone

| Parameter | Test configuration | Unit | Test 1 | Comments |
| --- | --- | --- | --- | --- |
| Propagation Condition | Config 1 | - | AWGN+220 Hz |  |
|  | Config 2 | - | AWGN+500 Hz |  |

###### A.19.2.3.2.3.2 Test Requirements

The test requirements defined in clause A.6.3.2.2.3.2 shall apply for ATG.

##### A.19.2.3.2.4 2-step RA type non-contention based test in FR1 for NR standalone

###### A.19.2.3.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits. This test will verify the requirements in clause6.2D.2.3 and clause7.1D.2 in an AWGN with constant residual doppler model.

For this test one cell is used and configured as PCell in FR1. Supported test configurations are shown in table A.19.2.3.2.4.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.6.3.2.2.4.1-2, except those described in the Table A.19.2.3.2.4.1-2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.3.2.4.1-1: Supported test configurations for non-contention based random access test in FR1 for NR standalone

| Config | Description |
| --- | --- |
| 1 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations depending on UE capability |  |

Table A.19.2.3.2.4.1-2: General test parameters for non-contention based random access test in FR1 for NR Standalone

| Parameter | Test configuration | Unit | Test 1 | Comments |
| --- | --- | --- | --- | --- |
| Propagation Condition | Config 1 | - | AWGN+220 Hz |  |
|  | Config 2 | - | AWGN+500 Hz |  |

###### A.19.2.3.2.4.2 Test Requirements

The test requirements defined in clause A.6.3.2.2.4.2 shall apply for ATG.

A.19.2.3.3 SA: RRC Connection Release with Redirection for ATG UE



A.19.2.3.3.1 Redirection from NR in FR1 to NR in FR1

###### A.19.2.3.3.1.1 Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements specified in clause 6.2D.3.2.1.

###### A.19.2.3.3.1.2 Test Parameters

Supported test configurations are shown in table A.19.2.3.3.1.2-1. The time delay is tested by using the parameters in table A.6.3.2.3.1.2-2 and table A.6.3.2.3.1.2-3, except those described in the Table A.19.2.3.3.1.2-2 and table A.19.2.3.3.1.2-3.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2. Cell 1 and Cell 2 belong to different tracking areas.

Table A.19.2.3.3.1.2-1: Redirection from NR to NR test configurations

| Config | Description |
| --- | --- |
| 1 | Source cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeTarget cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | Source cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeTarget cell: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | Source cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeTarget cell: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.19.2.3.3.1.2-2: General test parameters for Redirection from NR to NR test case

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| Access Barring Information | - | not barred | No additional delays in random access procedure. |
| T2 | s | 2.3 | The value applies for UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18 |

Table A.19.2.3.3.1.2-3: Cell specific test parameters for Redirection from NR to NR test case

| Parameter |  | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Propagation condition | Config 1, 2 | - | AWGN + 220 Hz |  | AWGN + 220 Hz |  |
|  | Config 3 |  | AWGN + 500 Hz |  | AWGN + 500 Hz |  |

###### A.19.2.3.3.1.3 Test Requirements

For UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The UE shall start to transmit the PRACH to Cell 2 less than 2240 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE: The redirection delay can be expressed as:

Tconnection_release_redirect_NR = TRRC_procedure_delay + Tidentify-NR + TSI-NR + TRACH,

where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR = 680 ms in the test.

TSI-NR = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH = 170 ms in the test.

## A.19.3 Timing

### A.19.3.1 UE transmit timing

#### A.19.3.1.1 ATG UE Transmit Timing Test for FR1

##### A.19.3.1.1.1 Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeb and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1D.2.

Supported test configurations refer to Table A.6.4.1.1.1-1.

A single NR cell is used during the test. Table A.19.3.1.1.1-1 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration SRSconfig.1 defined in table A.6.4.1.1.1-3.

Changed UE location with the mobility assumption of 1200km/h, the specific UE location should be emulated by test system and provided to UE by AT command or GNSS simulator.

The specific gNB reference location is emulated by test system.

Table A.19.3.1.1.1-1: Cell Specific Test Parameters for UL Transmit Timing test

| Parameter | Unit | Config | Test1 |
| --- | --- | --- | --- |
| SSB ARFCN |  | 1,2,3 | 1 |
| TDD configuration |  | 1 | Not Applicable |
|  |  | 2 | TDDConf.1.1 |
|  |  | 3 | TDDConf.2.1 |
| BWchannel | MHz | 1 | 10: NPRB,c = 52 |
|  |  | 2 | 10: NPRB,c = 52 |
|  |  | 3 | 40: NPRB,c = 106 |
| Initial BWP Configuration |  | 1,2,3 | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP Configuration |  | 1,2,3 | DLBWP.1.1ULBWP.1.1 |
| DRx Cycle | ms | 1,2,3 | N/A |
| PDSCH Reference measurement channel |  | 1 | SR.1.1 FDD |
|  |  | 2 | SR.1.1 TDD |
|  |  | 3 | SR.2.1 TDD |
| RMSI CORESET Reference Channel |  | 1 | CR.1.1 FDD |
|  |  | 2 | CR.1.1 TDD |
|  |  | 3 | CR.2.1 TDD |
| Dedicated CORESET Reference Channel |  | 1 | CCR.1.1 FDD |
|  |  | 2 | CCR.1.1 TDD |
|  |  | 3 | CCR.2.1 TDD |
| OCNG Patterns |  | 1,2,3 | OP.1 |
|  |  |  |  |
| SSB configuration |  | 1,2 | SSB.1 FR1 |
|  |  | 3 | SSB.2 FR1 |
| SMTC Configuration |  | 1,2 | SMTC.1 |
|  |  | 3 | SMTC.2 |
| TRS configuration |  | 1 | TRS.1.1 FDD |
|  |  | 2 | TRS.1.1 TDD |
|  |  | 3 | TRS.1.2 TDD |
| EPRE ratio of PSS to SSS | dB | 1,2,3 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1,2,3 | -98 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1,2 | -98 |
|  |  | 3 | -95 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  | 1,2,3 | 3 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | 1,2,3 | 3 |
| SS-RSRPNote3 | dBm/SCS | 1,2 | -95 |
|  |  | 3 | -92 |
| IoNote3 | dBm/9.36 MHz | 1,2 | -65.2 |
|  | dBm/38.1 MHz | 3 | -59.2 |
| Propagation condition |  | 1,2 | AWGN + 2412 HzNote6 |
|  |  | 3 | AWGN + 5556 HzNote7 |
| SRS Config |  | 1,2 | SRSConf.1Note5 |
|  |  | 3 | SRSConf.1Note5 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: SRS configs are given in table A.6.4.1.1.1-3NOTE 6: 2412 Hz is the maximum value of doppler with carrier frequency of 2170 MHz. The specific doppler shift trajectory is up to test system’s design considering of BS location and UE GNSS emulation.NOTE 7: 5556 Hz is the maximum value of doppler with carrier frequency of 5 GHz. The specific doppler shift trajectory is up to test system’s design considering of BS location and UE GNSS emulation. |  |  |  |

##### A.19.3.1.1.2 Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1) Setup NR PCell according to parameters given in table A.19.3.1.1.1-1.

2) After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset+$ N_{TA,adj}^{UE}$) ×Tc ± Te_ATG of the first detected path of DL SSB.

a. The NTA offset value (in Tc units) is 25600

b. The Te_ATG values depend on the DL and UL SCS for which the test is being run and are given in table 7.1D.2-1

c. The $ N_{TA,adj}^{UE}$ value is computed by the UE based on UE position and BS location.

3) The test system shall adjust the timing of the DL path by values given in table A.19.3.1.1.2-1

Table A.19.3.1.1.2-1: Adjustment Value for DL Timing

| SCS of SSB signals (KHz) | Adjustment Value |  |
| --- | --- | --- |
|  | Test1 | Test2 |
| 15 | +64*64Tc | +32*64Tc |
| 30 | +32*64Tc | +16*64Tc |

4) The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1D.2 Table 7.1D.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset+$ N_{TA,adj}^{UE}$) ×Tc ± Te_ATG respective to the first path (in time) of DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna.

5) The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset+$ N_{TA,adj}^{UE}$) ×Tc ± Te_ATG of the first path (in time) of DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna.

### A.19.3.2 UE timer accuracy

### A.19.3.3 Timing advance

#### A.19.3.3.1 SA FR1 timing advance adjustment accuracy

##### A.19.3.3.1.1 Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3D.

##### A.19.3.3.1.2 Test Parameters

Supported test configurations refer to table A.6.4.3.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.6.4.3.1.2-2, A.6.4.3.1.2-3 and A.6.4.3.1.2-4, except those defined in table A.19.3.3.1.2-1.

In all test cases, single cell is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.6.4.3.1.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.6.4.3.1.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause7.3D.2.1, the UE adjusts its uplink timing at slot n+k+2µ $\cdot  K_{offset}$ for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Changed UE location with the mobility assumption of 1200km/h, the specific UE location should be emulated by test system and provided to UE by AT command or GNSS simulator.

The specific gNB reference location is emulated by test system.

Table A.19.3.3.1.2-1 Cell specific test parameters for timing advance

| Parameter |  | Unit | Test1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| Propagation condition | Config 1 , 2 | - | AWGN + 220 Hz |  |
|  | Config 3 |  | AWGN + 500 Hz |  |
| Cell specific koffset |  |  | 3 |  |

##### A.19.3.3.1.3 Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1+2µ $\cdot  K_{offset}$ slots after the reception of the timing advance command, where k=5.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3D.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.19.4 Signalling characteristics

### A.19.4.1 Radio link Monitoring

In the following clause, any uplink signal transmitted by the UE is used for detecting the In-/Out-of-Sync state of the UE. In terms of measurement, the uplink signal is verified on the basis of the UE output power:

For UE with multiple transmit antennas, transmit OFF power is measured as the mean power at each transmit connector.

- UE output power higher than Transmit OFF power -50 dBm (as defined in TS 38.101-1 [18]) means uplink signal

- UE output power equal to or less than Transmit OFF power -50 dBm (as defined in TS 38.101-1 [18]) means no uplink signal.

#### A.19.4.1.1 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode

##### A.19.4.1.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1D.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.19.4.1.1.1-1. The test parameters are given in tables A.19.4.1.1.1-2, A.19.4.1.1.1-3, and A.19.4.1.1.1-4 below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.19.4.1.1.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.1.1.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | TDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.19.4.1.1.1-2: General test parameters for FR1 out-of-sync testing in non-DRX mode

| Parameter |  |  | Unit | Value |
| --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |
| Active PCell |  |  |  | Cell 1 |
| RF Channel Number |  |  |  | 1 |
| Duplex mode |  | Config 1 |  | FDD |
|  |  | Config 2, 3 |  | TDD |
| BWchannel |  | Config 1 | MHz | 10: NPRB,c = 52 |
|  |  | Config 2 |  | 10: NPRB,c = 52 |
|  |  | Config 3 |  | 40: NPRB,c = 106 |
| DL initial BWP configuration |  | Config 1, 2, 3 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  | Config 1, 2, 3 |  | DLBWP.1.1 |
| UL initial BWP configuration |  | Config 1, 2, 3 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  | Config 1, 2, 3 |  | ULBWP.1.1 |
| TDD Configuration |  | Config 1 |  | Not Applicable |
|  |  | Config 2 |  | TDDConf.1.1 |
|  |  | Config 3 |  | TDDConf.2.1 |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.1.1 FDD |
|  |  | Config 2 |  | CR.1.1 TDD |
|  |  | Config 3 |  | CR.2.1 TDD |
| Dedicated CORESET Reference Channel |  | Config 1 |  | CCR.1.3 FDD |
|  |  | Config 2 |  | CCR.1.3 TDD |
|  |  | Config 3 |  | CCR.2.2 TDD |
| SSB Configuration |  | Config 1 |  | SSB.1 FR1 |
|  |  | Config 2 |  | SSB.1 FR1 |
|  |  | Config 3 |  | SSB.2 FR1 |
| SMTC Configuration |  | Config 1, 2 |  | SMTC.1 |
|  |  | Config 3 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2 |  | 15 kHz |
|  |  | Config 3 |  | 30 kHz |
| PRACH Configuration |  | Config 1, 2 |  | Table A.3.8.2.1-1 |
|  |  | Config 3 |  | Table A.3.8.2.1-1 |
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
| CSI-RS configuration for CSI reporting |  | Config 1 |  | CSI-RS.1.1 FDD |
|  |  | Config 2 |  | CSI-RS.1.1 TDD |
|  |  | Config 3 |  | CSI-RS.2.1 TDD |
| CSI-RS for tracking |  | Config 1 |  | TRS.1.1 FDD |
|  |  | Config 2 |  | TRS.1.1 TDD |
|  |  | Config 3 |  | TRS.1.2 TDD |
| T1 |  |  | s | 0.2 |
| T2 |  |  | s | 0.48 |
| T3 |  |  | s | 0.48 |
| D1 |  |  | s | 0.44 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |

Table A.19.4.1.1.1-3: Cell specific test parameters for FR1 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 4 |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB | 0 |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |
| SNR on RLM-RS | Config 1 | dB | 1 | -7 | -15 |
|  | Config 2 |  | 1 | -7 | -15 |
|  | Config 3 |  | 1 | -7 | -15 |
| ![](media_svg/image4.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15 kHz | -98 |  |  |
|  | Config 2 |  | -98 |  |  |
|  | Config 3 |  | -98 |  |  |
| ![](media_svg/image4.svg) [公式≈: ^{N}oc] | Config 1 | dBm/SCS | -98 |  |  |
|  | Config 2 |  | -98 |  |  |
|  | Config 3 |  | -95 |  |  |
| Propagation condition | Config 1, 2 |  | AWGN+220 Hz |  |  |
|  | Config 3 |  | AWGN+500 Hz |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 4: The SNR in time periods T1, T2 and T3 is denoted as SNR1, SNR2 and SNR3 respectively in Figure A.19.4.1.1.1-1.NOTE 5: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4RX on all bands, the SNR during T3 is A.3.6. |  |  |  |  |  |

Table A.19.4.1.1.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

| Field | Test 1 |
| --- | --- |
|  | Value |
| gapOffset | 0 |
| NOTE: Ensure that RLM RS is partially overlapped with measurement gap |  |

Figure A.19.4.1.1.1-1: SNR variation for out-of-sync testing

##### A.19.4.1.1.2 Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.19.4.1.2 Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode

##### A.19.4.1.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1D.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.19.4.1.2.1-1. The test parameters are given in tables A.19.4.1.2.1-2, and A.19.4.1.2.1-3 below. There is one cell (Cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.19.4.1.2.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.1.2.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | TDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | TDD, SSB SCS 30 kHz, data SCS 30 kHz, BW 40 MHz |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.19.4.1.2.1-2: General test parameters for FR1 in-sync testing in non-DRX mode

| Parameter |  |  | Unit | Value |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |  |
| Active PCell |  |  |  | Cell 1 |  |
| RF Channel Number |  |  |  | 1 |  |
| Duplex mode |  | Config 1 |  | FDD |  |
|  |  | Config 2, 3 |  | TDD |  |
| BWchannel |  | Config 1 | MHz | 10: NPRB,c = 52 |  |
|  |  | Config 2 |  | 10: NPRB,c = 52 |  |
|  |  | Config 3 |  | 40: NPRB,c = 106 |  |
| DL initial BWP configuration |  | Config 1, 2, 3 |  | DLBWP.0.1 |  |
| DL dedicated BWP configuration |  | Config 1, 2, 3 |  | DLBWP.1.1 |  |
| UL initial BWP configuration |  | Config 1, 2, 3 |  | ULBWP.0.1 |  |
| UL dedicated BWP configuration |  | Config 1, 2, 3 |  | ULBWP.1.1 |  |
| TDD Configuration |  | Config 1 |  | Not Applicable |  |
|  |  | Config 2 |  | TDDConf.1.1 |  |
|  |  | Config 3 |  | TDDConf.2.1 |  |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.1.1 FDD |  |
|  |  | Config 2 |  | CR.1.1 TDD |  |
|  |  | Config 3 |  | CR.2.1 TDD |  |
| Dedicated CORESET Reference Channel |  | Config 1 |  | CCR.1.1 FDD |  |
|  |  | Config 2 |  | CCR.1.1 TDD |  |
|  |  | Config 3 |  | CCR.2.1 TDD |  |
| SSB Configuration |  | Config 1 |  | SSB.1 FR1 |  |
|  |  | Config 2 |  | SSB.1 FR1 |  |
|  |  | Config 3 |  | SSB.2 FR1 |  |
| SMTC Configuration |  | Config 1, 2 |  | SMTC.1 |  |
|  |  | Config 3 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2 |  | 15 kHz |  |
|  |  | Config 3 |  | 30 kHz |  |
| PRACH Configuration |  | Config 1, 2 |  | Table  A.3.8.2.1-1 |  |
|  |  | Config 3 |  | Table  A.3.8.2.1-1 |  |
| SSB index assigned as RLM RS |  |  |  | 0 |  |
| OCNG parameters |  |  |  | OP.1 |  |
| CP length |  |  |  | Normal |  |
| Correlation Matrix and Antenna Configuration |  |  |  | 2x2 Low |  |
| In sync transmission parameters | DCI format |  |  | 1-0 |  |
|  | Number of Control OFDM symbols |  |  | 2 |  |
|  | Aggregation level |  | CCE | 4 |  |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 0 |  |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 0 |  |
|  | DMRS precoder granularity |  |  | REG bundle size |  |
|  | REG bundle size |  |  | 6 |  |
| Out of sync transmission parameters | DCI format |  |  | 1-0 |  |
|  | Number of Control OFDM symbols |  |  | 2 |  |
|  | Aggregation level |  | CCE | 8 |  |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 4 |  |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 4 |  |
|  | DMRS precoder granularity |  |  | REG bundle size |  |
|  | REG bundle size |  |  | 6 |  |
| DRX |  |  |  | OFF |  |
| Gap pattern ID |  |  |  | N.A. |  |
| Layer 3 filtering |  |  |  | Enabled |  |
| T310 timer |  |  | ms | 1000 |  |
| T311 timer |  |  | ms | 1000 |  |
| N310 |  |  |  | 1 |  |
| N311 |  |  |  | 1 |  |
| CSI-RS configuration for CSI reporting | Config 1 |  |  | CSI-RS.1.1 FDD |  |
|  | Config 2 |  |  | CSI-RS.1.1 TDD |  |
|  | Config 3 |  |  | CSI-RS.2.1 TDD |  |
| CSI-RS for tracking | Config 1, 4 |  |  | TRS.1.1 FDD |  |
|  | Config 2, 5 |  |  | TRS.1.1 TDD |  |
|  | Config 3, 6 |  |  | TRS.1.2 TDD |  |
| T1 |  |  | s |  | 0.2 |
| T2 |  |  | s |  | 0.2 |
| T3 |  |  | s |  | 0.24 |
| T4 |  |  | s |  | 0.2 |
| T5 |  |  | s |  | 0.88 |
| D1 |  |  | s |  | 0.84 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |

Table A.19.4.1.2.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |
| SNR on RLM-RS | Config 1 | dB | 1 | -7 | -15 | -4.5 | 1 |
|  | Config 2 |  | 1 | -7 | -15 | -4.5 | 1 |
|  | Config 3 |  | 1 | -7 | -15 | -4.5 | 1 |
| ![](media_svg/image4.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15 kHz | -98 |  |  |  |  |
|  | Config 2 |  | -98 |  |  |  |  |
|  | Config 3 |  | -98 |  |  |  |  |
| ![](media_svg/image4.svg) [公式≈: ^{N}oc] | Config 1 | dBm/SCS | -98 |  |  |  |  |
|  | Config 2 |  | -98 |  |  |  |  |
|  | Config 3 |  | -95 |  |  |  |  |
| Propagation condition | Config 1, 2 |  | AWGN +220 Hz |  |  |  |  |
|  | Config 3 |  | AWGN +500 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 4: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2, SNR3, SNR4 and SNR5 respectively in Figure A.19.4.1.2.1-1.NOTE 5: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4RX on all bands, the SNR during T3 and T4 is modified as specified in clause A.3.6. |  |  |  |  |  |  |  |

Table A.19.4.1.2.1-4: Void

Figure A.19.4.1.2.1-1: SNR variation for in-sync testing

##### A.19.4.1.2.2 Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.19.4.1.3 Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode

##### A.19.4.1.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used. This test will partly verify the FR1 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause8.1D.

The test parameters are given in tables A.19.4.1.3.1-1, A.19.4.1.3.1-2, A.19.4.1.3.1-3, and A.19.4.1.3.1-3A below. There is one cell, Cell 1 which is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.19.4.1.3.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting of 5 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 is configured as the BFD-RS.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.1.3.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | FDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| 2 | TDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| 3 | TDD duplex mode, 30 kHz SSB SCS, 40 MHz bandwidth |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.19.4.1.3.1-2: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in non-DRX mode

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| Active PCell |  |  | Cell 1 |
| RF Channel Number |  |  | 1 |
| Duplex mode | Config 1 |  | FDD |
|  | Config 2, 3 |  | TDD |
| TDD Configuration | Config 1 |  | Not Applicable |
|  | Config 2 |  | TDDConf.1.1 |
|  | Config 3 |  | TDDConf.2.1 |
| DL initial BWP configuration | Config 1, 2, 3 |  | DLBWP.0.1 |
| DL dedicated BWP configuration | Config 1, 2, 3 |  | DLBWP.1.1 |
| UL initial BWP configuration | Config 1, 2, 3 |  | ULBWP.0.1 |
| UL dedicated BWP configuration | Config 1, 2, 3 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel | Config 1 |  | CR.1.1 FDD |
|  | Config 2 |  | CR.1.1 TDD |
|  | Config 3 |  | CR.2.1 TDD |
| Dedicated CORESET Reference Channel | Config 1 |  | CCR.1.3 FDD |
|  | Config 2 |  | CCR.1.3 TDD |
|  | Config 3 |  | CCR.2.2 TDD |
| SSB Configuration | Config 1 |  | SSB.1 FR1 |
|  | Config 2 |  | SSB.1 FR1 |
|  | Config 3 |  | SSB.2 FR1 |
| SMTC Configuration | Config 1, 2 |  | SMTC.1 |
|  | Config 3 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing | Config 1, 2 |  | 15 kHz |
|  | Config 3 |  | 30 kHz |
| TRS configuration | Config 1 |  | TRS.1.1 FDD |
|  | Config 2 |  | TRS.1.1 TDD |
|  | Config 3 |  | TRS.1.2 TDD |
| CSI-RS for RLM | Config 1 |  | Resource #4 in TRS.1.1 FDD |
|  | Config 2 |  | Resource #4 in TRS.1.1 TDD |
|  | Config 3 |  | Resource #4 in TRS.1.2 TDD |
| TCI configuration for PDCCH/PDSCH |  |  | TCI.State. 2 |
| OCNG parameters |  |  | OP.1 |
| CP length |  |  | Normal |
| Correlation Matrix and Antenna Configuration |  |  | 2x2 Low |
| Out of sync transmission parameters | DCI format |  | 1-0 |
|  | Number of Control OFDM symbols |  | 2 |
|  | Aggregation level | CCE | 8 |
|  | Ratio of hypothetical PDCCH RE energy to average CSI-RS RE energy | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average CSI-RS RE energy | dB | 4 |
|  | DMRS precoder granularity |  | REG bundle size |
|  | REG bundle size |  | 6 |
| DRX |  |  | OFF |
| Gap pattern ID |  |  | gp0 |
| Layer 3 filtering |  |  | Enabled |
| T310 timer |  | ms | 0 |
| T311 timer |  | ms | 1000 |
| N310 |  |  | 1 |
| N311 |  |  | 1 |
| CSI-RS configuration for CSI reporting | Config 1 |  | CSI-RS.1.1 FDD |
|  | Config 2 |  | CSI-RS.1.1 TDD |
|  | Config 3 |  | CSI-RS.2.1 TDD |
| T1 |  | s | 0.2 |
| T2 |  | s | 0.48 |
| T3 |  | s | 0.48 |
| D1 |  | s | 0.44 |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |

Table A.19.4.1.3.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| EPRE ratio of PDCCH DMRS to SSSPDCCH_beta |  | dB | 4 |  |  |
| EPRE ratio of PDCCH to PDCCH DMRSPDCCH_DMRS_beta |  | dB |  |  |  |
| EPRE ratio of PBCH DMRS to SSSPBCH_beta |  | dB | 0 |  |  |
| EPRE ratio of PBCH to PBCH DMRSPSS_beta |  | dB |  |  |  |
| EPRE ratio of PSS to SSSSSS_beta |  | dB |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS PDSCH_beta |  | dB |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |
| SNR on RLM-RS | Config 1 | dB | 1 | -7 | -15 |
|  | Config 2 |  | 1 | -7 | -15 |
|  | Config 3 |  | 1 | -7 | -15 |
| ![](media_svg/image4.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15 kHz | -98 |  |  |
|  | Config 2 |  | -98 |  |  |
|  | Config 3 |  | -98 |  |  |
| Propagation condition | Config 1, 2 |  | AWGN +220 Hz |  |  |
|  | Config 3 |  | AWGN +500 Hz |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2 and T3 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.19.4.1.3.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4RX on all bands, the SNR during T3 is A.3.6. |  |  |  |  |  |

Table A.19.4.1.3.1-3A: Measurement gap configuration for FR1 CSI-RS out-of-sync radio link monitoring in non-DRX mode

| Field | Test 1 |
| --- | --- |
|  | Value |
| gapOffset | 0 |
| NOTE 1: Void |  |

Table A.19.4.1.3.1-4: Void



![](media/image7.emf)

Figure A.19.4.1.3.1-1: SNR variation for CSI-RS out-of-sync testing

##### A.19.4.1.3.2 Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 no later than time point C (D1 ms after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.19.4.1.4 Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode

##### A.19.4.1.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used. This test will partly verify the FR1 PCell CSI-RS In-sync radio link monitoring requirements in clause8.1D.

The test parameters are given in tables A.19.4.1.4.1-1, A.19.4.1.4.1-2, and A.19.4.1.4.1-3 below. There is one cell (Cell 1), which is the PCell in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.19.4.1.4.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled. In the test, SSB0 is configured as the BFD-RS.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.1.4.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | FDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| 2 | TDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| 3 | TDD duplex mode, 30 kHz SSB SCS, 40 MHz bandwidth |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.19.4.1.4.1-2: General test parameters for FR1 PCell for CSI-RS in-sync testing in non-DRX mode

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| Active PCell |  |  | Cell 1 |
| RF Channel Number |  |  | 1 |
| Duplex mode | Config 1 |  | FDD |
|  | Config 2, 3 |  | TDD |
| TDD Configuration | Config 1 |  | Not Applicable |
|  | Config 2 |  | TDDConf.1.1 |
|  | Config 3 |  | TDDConf.2.1 |
| DL initial BWP configuration | Config 1, 2, 3 |  | DLBWP.0.1 |
| DL dedicated BWP configuration | Config 1, 2, 3 |  | DLBWP.1.1 |
| UL initial BWP configuration | Config 1, 2, 3 |  | ULBWP.0.1 |
| UL dedicated BWP configuration | Config 1, 2, 3 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel | Config 1 |  | CR.1.1 FDD |
|  | Config 2 |  | CR.1.1 TDD |
|  | Config 3 |  | CR.2.1 TDD |
| Dedicated CORESET Reference Channel | Config 1 |  | CCR.1.1 FDD |
|  | Config 2 |  | CCR.1.1 TDD |
|  | Config 3 |  | CCR.2.1 TDD |
| SSB Configuration | Config 1 |  | SSB.1 FR1 |
|  | Config 2 |  | SSB.1 FR1 |
|  | Config 3 |  | SSB.2 FR1 |
| SMTC Configuration | Config 1, 2 |  | SMTC.1 |
|  | Config 3 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing | Config 1, 2 |  | 15 kHz |
|  | Config 3 |  | 30 kHz |
| TRS configuration | Config 1 |  | TRS.1.1 FDD |
|  | Config 2 |  | TRS.1.1 TDD |
|  | Config 3 |  | TRS.1.2 TDD |
| CSI-RS for RLM | Config 1 |  | Resource #4 in TRS.1.1 FDD |
|  | Config 2 |  | Resource #4 in TRS.1.1 TDD |
|  | Config 3 |  | Resource #4 in TRS.1.2 TDD |
| TCI configuration for PDCCH/PDSCH |  |  | TCI.State. 2 |
| OCNG parameters |  |  | OP.1 |
| CP length |  |  | Normal |
| Correlation Matrix and Antenna Configuration |  |  | 2x2 Low |
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
| CSI-RS configuration for CSI reporting | Config 1 |  | CSI-RS.1.1 FDD |
|  | Config 2 |  | CSI-RS.1.1 TDD |
|  | Config 3 |  | CSI-RS.2.1 TDD |
| T1 |  | s | 0.2 |
| T2 |  | s | 0.2 |
| T3 |  | s | 0.44 |
| T4 |  | s | 0.2 |
| T5 |  | s | 0.88 |
| T6 |  | s | 0.84 |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |

Table A.19.4.1.4.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 |
| EPRE ratio of PDCCH DMRS to SSSPDCCH_beta |  | dB | 4 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRSPDCCH_DMRS_beta |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSSPBCH_beta |  | dB | 0 |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRSPSS_beta |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSSSSS_beta |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS PDSCH_beta |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |
| SNR on RLM-RS | Config 1 | dB | 1 | -7 | -15 | -4.5 | 1 |
|  | Config 2 |  | 1 | -7 | -15 | -4.5 | 1 |
|  | Config 3 |  | 1 | -7 | -15 | -4.5 | 1 |
| ![](media_svg/image4.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15 kHz | -98 |  |  |  |  |
|  | Config 2 |  | -98 |  |  |  |  |
|  | Config 3 |  | -98 |  |  |  |  |
| Propagation condition | Config 1, 2 |  | AWGN +220 Hz |  |  |  |  |
|  | Config 3 |  | AWGN +500 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2, SNR3, SNR4 and SNR5 respectively in figure A.19.4.1.4.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4RX on all bands, the SNR during T3 is specified in clause A.3.6.1.1. |  |  |  |  |  |  |  |

Table A.19.4.1.4.1-4: Void

Figure A.19.4.1.4.1-1: SNR variation for CSI-RS in-sync testing

##### A.19.4.1.4.2 Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

### A.19.4.2 Beam Failure Detection and Link recovery procedures

#### A.19.4.2.1 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode

##### A.19.4.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5D.

The test parameters are given in tables A.19.4.2.1.1-1, A.19.4.2.1.1-2, A.19.4.2.1.1-3 and A.19.4.2.1.1-4 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.19.4.2.1.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.19.4.2.1.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.2.1.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | FDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| 2 | TDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| 3 | TDD duplex mode, 30 kHz SSB SCS, 40 MHz bandwidth |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.19.4.2.1.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |  |
| Active PSCell |  |  |  | Cell 1 |  |
| RF Channel Number |  |  |  | 1 |  |
| Duplex mode |  | Config 1 |  | FDD |  |
|  |  | Config 2, 3 |  | TDD |  |
| BWchannel |  | Config 1 | MHz | 10: NPRB,c = 52 |  |
|  |  | Config 2 |  | 10: NPRB,c = 52 |  |
|  |  | Config 3 |  | 40: NPRB,c = 106 |  |
| DL initial BWP configuration |  | Config 1, 2, 3 |  | DLBWP.0.1 |  |
| DL dedicated BWP configuration |  | Config 1, 2, 3 |  | DLBWP.1.1 |  |
| UL initial BWP configuration |  | Config 1, 2, 3 |  | ULBWP.0.1 |  |
| UL dedicated BWP configuration |  | Config 1, 2, 3 |  | ULBWP.1.1 |  |
| TDD Configuration |  | Config 1 |  | Not Applicable |  |
|  |  | Config 2 |  | TDDConf.1.1 |  |
|  |  | Config 3 |  | TDDConf.2.1 |  |
| RMSI CORESET Reference Channel |  | Config 1 |  | CR.1.1 FDD |  |
|  |  | Config 2 |  | CR.1.1 TDD |  |
|  |  | Config 3 |  | CR.2.1 TDD |  |
| Dedicated CORESET Reference Channel |  | Config 1 |  | CCR.1.1 FDD |  |
|  |  | Config 2 |  | CCR.1.1 TDD |  |
|  |  | Config 3 |  | CCR.2.1 TDD |  |
| SSB Configuration |  | Config 1 |  | SSB.3 FR1 |  |
|  |  | Config 2 |  | SSB.3 FR1 |  |
|  |  | Config 3 |  | SSB.4 FR1 |  |
| SMTC Configuration |  | Config 1, 2 |  | SMTC.1 |  |
|  |  | Config 3 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2 |  | 15 KHz |  |
|  |  | Config 3 |  | 30 KHz |  |
| PRACH Configuration |  | Config 1, 2 |  | Table A.3.8.2.2-1 |  |
|  |  | Config 3 |  | Table A.3.8.2.2-1 |  |
| SSB Index assigned as BFD RS (q0) |  |  |  | 0 |  |
| SSB Index assigned as CBD RS (q1) |  |  |  | 1 |  |
| OCNG parameters |  |  |  | OP.1 |  |
| CP length |  |  |  | Normal |  |
| Correlation Matrix and Antenna Configuration |  |  |  | 2x2 Low |  |
| Beam failure detection transmission parameters | DCI format |  |  | 1-0 |  |
|  | Number of Control OFDM symbols |  |  | 2 |  |
|  | Aggregation level |  | CCE | 8 |  |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  | dB | 0 |  |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  | dB | 0 |  |
|  | DMRS precoder granularity |  |  | REG bundle size |  |
|  | REG bundle size |  |  | 6 |  |
| DRX |  |  |  | OFF |  |
| Gap pattern ID |  |  |  | gp0 |  |
| gapOffset |  |  |  | 0 |  |
| rlmInSyncOutOfSyncThreshold |  |  |  | absent | When the field is absent, the UE applies the value 0. (Table 8.1.1-1). |
| rsrp-ThresholdSSB | Config 1, 2 |  | dBm/SCS kHz | -98 | Threshold used for Qin_LR_SSB |
|  | Config 3 |  |  | -95 |  |
| powerControlOffsetSS |  |  |  | db0 | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  |  |  | n1 | see clause 5.17 of TS 38.321 [7] |
| beamFailureDetectionTimer |  |  |  | pbfd4 | see clause 5.17 of TS 38.321 [7] |
| CSI-RS configuration  for CSI reporting | Config 1 |  |  | CSI-RS.1.1 FDD |  |
|  | Config 2 |  |  | CSI-RS.1.1 TDD |  |
|  | Config 3 |  |  | CSI-RS.2.1 TDD |  |
| CSI-RS for tracking | Config 1 |  |  | TRS.1.1 FDD |  |
|  | Config 2 |  |  | TRS.1.1 TDD |  |
|  | Config 3 |  |  | TRS.1.2 TDD |  |
| SSB Index assigned as RLM RS |  |  |  | 0, 1 |  |
| T310 Timer |  |  | ms | 1000 |  |
| N310 |  |  |  | 2 |  |
| T1 |  |  | s | 0.2 | During this time the the UE shall be fully synchronized to Cell 1 |
| T2 |  |  | s | 0.37 |  |
| T3 |  |  | s | 0.24 |  |
| T4 |  |  | s | 0 |  |
| T5 |  |  | s | 0.17 |  |
| D1 |  |  | s | 0.13 |  |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |

Table A.19.4.2.1.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |
| SNR_SSB of set q0 | Config 1 | dB | 5 | -3 | -12 | -12 | -12 |
|  | Config 2 |  | 5 | -3 | -12 | -12 | -12 |
|  | Config 3 |  | 5 | -3 | -12 | -12 | -12 |
| SNR_SSB of set q1 | Config 1 | dB | -10 | -10 | 10 | 10 | 10 |
|  | Config 2 |  | -10 | -10 | 10 | 10 | 10 |
|  | Config 3 |  | -10 | -10 | 10 | 10 | 10 |
| SSB_RP of set q1 | Config 1 | dBm/SCS kHz | -108 | -108 | -88 | -88 | -88 |
|  | Config 2 |  | -108 | -108 | -88 | -88 | -88 |
|  | Config 3 |  | -105 | -105 | -85 | -85 | -85 |
| ![](media_svg/image4.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15 KHz | -98 |  |  |  |  |
|  | Config 2 |  | -98 |  |  |  |  |
|  | Config 3 |  | -98 |  |  |  |  |
| Propagation condition | Config 1, 2 |  | AWGN +220 Hz |  |  |  |  |
|  | Config 3 |  | AWGN +500 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.4.5.5.1.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4RX on all bands, the SNR during T3 is modified as specified in clause A.3.6. |  |  |  |  |  |  |  |

Table A.19.4.2.1.1-4: Void

Figure A.19.4.2.1.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.19.4.2.1.1-2: L1-RSRP level variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

##### A.19.4.2.1.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 120+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.19.4.2.2 Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode

##### A.19.4.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5D.

The test parameters are given in tables A.19.4.2.2.1-1, A.19.4.2.2.1-2, and below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.19.4.2.2.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.19.4.2.2.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.2.2.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | FDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| 2 | TDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| 3 | TDD duplex mode, 30 kHz SSB SCS, 40 MHz bandwidth |
| NOTE: The UE is only required to pass in one of the supported test configurations in FR1 |  |

Table A.19.4.2.2.1-2: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  |  |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Test 1 |  |
| Active PCell |  |  |  |  | Cell 1 |  |
| RF Channel Number |  |  |  |  | 1 |  |
| Duplex mode | Config 1 |  |  |  | FDD |  |
|  | Config 2, 3 |  |  |  | TDD |  |
| TDD Configuration | Config 1 |  |  |  | Not Applicable |  |
|  | Config 2 |  |  |  | TDDConf.1.1 |  |
|  | Config 3 |  |  |  | TDDConf.2.1 |  |
| RMSI CORESET Reference Channel | Config 1 |  |  |  | CR.1.1 FDD | A.3.1.2 |
|  | Config 2 |  |  |  | CR.1.1 TDD |  |
|  | Config 3 |  |  |  | CR.2.1 TDD |  |
| Dedicated CORESET Reference Channel | Config 1 |  |  |  | CCR.1.1 FDD | A.3.1.3 |
|  | Config 2 |  |  |  | CCR.1.1 TDD |  |
|  | Config 3 |  |  |  | CCR.2.1 TDD |  |
| SSB Configuration | Config 1 |  |  |  | SSB.3 FR1 | A.3.10 |
|  | Config 2 |  |  |  | SSB.3 FR1 |  |
|  | Config 3 |  |  |  | SSB.4 FR1 |  |
| SSB Configuration | Config 1 |  |  |  | SSB. 3  FR1 | A.3.10 |
|  | Config 2 |  |  |  | SSB. 3 FR1 |  |
|  | Config 3 |  |  |  | SSB. 4  FR1 |  |
| SMTC Configuration | Config 1, 2 |  |  |  | SMTC.1 | A.3.11 |
|  | Config 3 |  |  |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing | Config 1, 2 |  |  |  | 15 KHz |  |
|  | Config 3 |  |  |  | 30 KHz |  |
| PRACH Configuration | Config 1, 2 |  |  |  | FR1 PRACH configuration 4 | A.3.8.2 |
|  | Config 3 |  |  |  | FR1 PRACH configuration 4 | A.3.8.2 |
| csi-RS-Index assigned as beam failure detection RS in set q0 |  |  |  |  | 0 |  |
| OCNG parameters |  |  |  |  | OP.1 | A.3.2.1 |
| CP length |  |  |  |  | Normal |  |
| Correlation Matrix and Antenna Configuration |  |  |  |  | 2x2 Low |  |
| Beam failure detection transmission parameters | DCI format |  |  |  | 1-0 |  |
|  | Number of Control OFDM symbols |  |  |  | 2 |  |
|  | Aggregation level |  |  | CCE | 8 |  |
|  | Ratio of hypothetical PDCCH RE energy to average CSI-RS RE energy |  |  | dB | 0 |  |
|  | Ratio of hypothetical PDCCH DMRS energy to average CSI-RS RE energy |  |  | dB | 0 |  |
|  | DMRS precoder granularity |  |  |  | REG bundle size |  |
|  | REG bundle size |  |  |  | 6 |  |
| DRX |  |  |  |  | OFF |  |
| Gap pattern ID |  |  |  |  | N.A. |  |
| csi-RS-Index assigned as candidate beam detection RS in set q1 |  |  |  |  | 1 | N |
| rlmInSyncOutOfSyncThreshold |  |  |  |  | absent | When the field is absent, the UE applies the value 0. (Table 8.1.1-1). |
| rsrp-ThresholdCSI-RS |  | Config 1, 2 |  | dBm/SCS kHz | -98 | Threshold used for Qin_LR_CSI-RS |
|  |  | Config 3 |  |  | -95 |  |
| powerControlOffsetSS |  |  |  |  | db0 | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  |  |  |  | n1 | see clause 5.17 of TS 38.321 [7] |
| beamFailureDetectionTimer |  |  |  |  | pbfd4 | see clause 5.17 of TS 38.321 [7] |
| CSI-RS configuration for q0 and q1 |  |  | Config 1 |  | CSI-RS.1.2 FDD | A.3.14 |
|  |  |  | Config 2 |  | CSI-RS.1.2 TDD |  |
|  |  |  | Config 3 |  | CSI-RS.2.2 TDD |  |
| CSI-RS configuration for CSI reporting |  |  | Config 1 |  | CSI-RS.1.1 FDD | A.3.14 |
|  |  |  | Config 2 |  | CSI-RS.1.1 TDD |  |
|  |  |  | Config 3 |  | CSI-RS.2.1 TDD |  |
| TRS configuration |  |  | Config 1 |  | TRS.1.1 FDD |  |
|  |  |  | Config 2 |  | TRS.1.1 TDD |  |
|  |  |  | Config 3 |  | TRS.1.2 TDD |  |
| CSI-RS-Index assigned as RLM RS |  |  | Config 1 |  | CSI-RS.1.2 FDD | A.3.14 |
|  |  |  | Config 2 |  | CSI-RS.1.2 TDD |  |
|  |  |  | Config 3 |  | CSI-RS.2.2 TDD |  |
| T310 Timer |  |  |  | ms | 1000 |  |
| N310 |  |  |  |  | 2 |  |
| T1 |  |  |  | s | 0.2 | During this time the the UE shall be fully synchronized to Cell 1 |
| T2 |  |  |  | s | 0.18 |  |
| T3 |  |  |  | s | 0.14 |  |
| T4 |  |  |  | s | 0 |  |
| T5 |  |  |  | s | 0.08 |  |
| D1 |  |  |  | s | 0.04 |  |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |  |

Table A.19.4.2.2.1-3: Cell specific test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |
| SNR_CSI-RS of set q0 | Config 1 | dB | 5 | -3 | -12 | -12 | -12 |
|  | Config 2 |  | 5 | -3 | -12 | -12 | -12 |
|  | Config 3 |  | 5 | -3 | -12 | -12 | -12 |
| SNR_CSI-RS of set q1 | Config 1 | dB | -10 | -10 | 10 | 10 | 10 |
|  | Config 2 |  | -10 | -10 | 10 | 10 | 10 |
|  | Config 3 |  | -10 | -10 | 10 | 10 | 10 |
| CSI-RS_RP of set q1 | Config 1 | dBm/SCS kHz | -108 | -108 | -88 | -88 | -88 |
|  | Config 2 |  | -108 | -108 | -88 | -88 | -88 |
|  | Config 3 |  | -105 | -105 | -85 | -85 | -85 |
| ![](media_svg/image4.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15 KHz | -98 |  |  |  |  |
|  | Config 2 |  | -98 |  |  |  |  |
|  | Config 3 |  | -98 |  |  |  |  |
| Propagation condition | Config 1, 2 |  | AWGN +220 Hz |  |  |  |  |
|  | Config 3 |  | AWGN +500 Hz |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: VoidNOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the REs carrying CSI-RS.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.4.5.5.1.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4RX on all bands, the SNR during T3 is modified as specified in clause A.3.6. |  |  |  |  |  |  |  |

Table A.19.4.2.2.1-4: Void

Table A.19.4.2.2.1-5: Void

Figure A.19.4.2.2.1-1: SNR variation for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Figure A.19.4.2.2.1-2: L1-RSRP level variation for CSI-RS based beam failure detection and link recovery testing in non-DRX mode

##### A.19.4.2.2.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 30+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.19.4.2.3 Beam Failure Detection and Link Recovery Test for FR1 SCell configured with with CSI-RS-based BFD and SSB-based LR in non-DRX mode

##### A.19.4.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP without schedulingRequestID-BFR-SCell-r16 configuration, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5D.

The test parameters are given in table A.19.4.2.3.1-1 below. The test parameters for PCell and SCell refer to Table A.6.5.5.5.1-2 and A.6.5.5.5.1-3 except those described in the table A.19.4.2.3.1-2.

There are two cells, Cell 1 is the PCell and Cell 2 is the SCell, in the test. UE is not provided by schedulingRequestID-BFR-SCell-r16, i.e., no configuration for PUCCH transmission resources, and UE shall perform the random access procedure to recover the beam failure. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.19.4.2.1.1-1 shows the SNR of the CSI-RS in set q0 in the active SCell to emulate beam failure. Figure A.19.4.2.1.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery.

Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.2.3.1-1: Supported test configurations for FR1 PCell and SCell

| Configuration | Description |
| --- | --- |
| 1 | FDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| 2 | TDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| 3 | TDD duplex mode, 30 kHz SSB SCS, 40 MHz bandwidth |
| NOTE 1: The UE is only required to pass in one of the supported test configurations in FR1NOTE 2: The UE is only required to be tested in one with smallest aggregated channel bandwidth from supported band combinations which is composed of CCs ≥ the bandwidth (BWchannel) defined in each test configuration.NOTE 3: Test configuration for NR PCell and test configuration for NR SCell shall be chosen independently. |  |

Table A.19.4.2.3.1-2: Cell specific test parameters for FR1 SCell for beam failure detection and link recovery testing in non-DRX mode

| Parameter |  | Unit | Cell 1 | Test 1 Cell 2 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 to T5 | T1 | T2 | T3 | T4 | T5 |
| Propagation condition | Config 1, 2 |  | AWGN+220 Hz |  |  |  |  |  |
|  | Config 3 |  | AWGN+500 Hz |  |  |  |  |  |

##### A.19.4.2.3.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 120+10 ms after the start of T5, the UE shall transmit preamble for UL-SCH resource application, followed by MAC-CE on the assigned uplink resources containing a beam associated with the candidate beam set q1. The UE shall not transmit preamble earlier than time point B.

During T5, the System Simulator shall transmit a Random Access Response to UE after the System Simulator receives the preamble from UE. The UE shall transmit the msg.3 containing candidate beam set q1 for SCell BFR if UE receives the Random Access Response.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

### A.19.4.3 Active BWP switch

#### A.19.4.3.1 DCI-based and Timer-based Active BWP Switch

##### A.19.4.3.1.1 NR FR1 DL active BWP switch with non-DRX in SA

A.19.4.3.1.1.1 Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6D.

The supported test configurations are shown in table A.19.4.3.1.1.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.19.4.3.1.1.1-2. Cell-specific parameters of the cell are specified in table A.19.4.3.1.1.1-3 below.

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

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.3.1.1.1-1: DL BWP switch supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations.NOTE 2: A UE which fulfils the requirements in test case A.19.4.3.1.1 can skip the test cases in A.19.4.3.1.1. |  |

Table A.19.4.3.1.1.1-2: General test parameters for DL BWP switch in SA

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active Cell |  | Cell 1 | Cell 1 on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| bwp-InactivityTimer | ms | 200 |  |
| PDCCH and PDSCH maximum number of HARQ transmission |  | 1 |  |
| T1 | s | 0.2 |  |
| T2 | s | 0.2 |  |
| T3 | s | 0.2 |  |

Table A.19.4.3.1.1.1-3: NR Cell specific test parameters for DL BWP switch in SA

| Parameter |  |  | Unit | Cell 1 |
| --- | --- | --- | --- | --- |
| Frequency Range |  |  |  | FR1 |
| Duplex mode |  | Config 1 |  | FDD |
|  |  | Config 2,3 |  | TDD |
| TDD configuration |  | Config 1 |  | Not Applicable |
|  |  | Config 2 |  | TDDConf.1.1 |
|  |  | Config 3 |  | TDDConf.2.1 |
| BWchannel |  | Config 1 |  | 10 MHz: NPRB,c = 52 |
|  |  | Config 2 |  | 10 MHz: NPRB,c = 52 |
|  |  | Config 3 |  | 40 MHz: NPRB,c = 106 |
| Active BWP ID |  |  |  | 1, 2 |
| Initial DL BWP Configuration |  | Config 1,2,3 |  | DLBWP.0.2 Note 4 |
| Active DL BWP-1 Configuration |  | Config 1,2,3 |  | DLBWP.1.1 Note 4 |
| Active DL BWP-2 Configuration |  | Config 1,2,3 |  | DLBWP.1.3 Note 4 |
| Initial UL BWP Configuration |  | Config 1,2,3 |  | ULBWP.0.2 Note 4 |
| Active UL BWP-1 Configuration |  | Config 1,2,3 |  | ULBWP.1.1 Note 4 |
| Active UL BWP-2 Configuration |  | Config 1 |  | N/A |
|  |  | Config 2,3 |  | ULBWP.1.3 Note 4 |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 FDD |
|  |  | Config 2 |  | SR.1.1 TDD |
|  |  | Config 3 |  | SR.2.1 TDD |
| RMSI CORESET parameters |  | Config 1 |  | CR.1.1 FDD |
|  |  | Config 2 |  | CR.1.1 TDD |
|  |  | Config 3 |  | CR.2.1 TDD |
| Dedicated CORESET parameters |  | Config 1 |  | CCR.1.2 FDD |
|  |  | Config 2 |  | CCR.1.2 TDD |
|  |  | Config 3 |  | CCR.2.4 TDD |
| OCNG Patterns |  |  |  | OP.1 |
| SSB Configuration |  | Config 1,2 |  | SSB.1 FR1 |
|  |  | Config 3 |  | SSB.2 FR1 |
| SMTC Configuration |  |  |  | SMTC.1 |
| Correlation Matrix and Antenna Configuration |  |  |  | 1x2 Low |
| TRS Configuration |  | Config 1,4 |  | TRS.1.1 FDD |
|  |  | Config 2,5 |  | TRS.1.1 TDD |
|  |  | Config 3,6 |  | TRS.1.2 TDD |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| NocNote 2 | Config 1,2 |  | dBm/SCS | -104 |
|  | Config 3 |  |  | -101 |
| NocNote 2 |  |  | dBm/15 kHz | -104 |
| SS-RSRP Note 3 | Config 1,2 |  | dBm/SCS | -87 |
|  | Config 3 |  |  | -84 |
| Ês/Iot |  |  | dB | 17 |
| Ês/Noc |  |  | dB | 17 |
| IoNote3 |  | Config 1,2 | dBm/9.36 MHz | -58.96 |
|  |  | Config 3 | dBm/38.16 MHz | -52.86 |
| Propagation condition |  | Config 1, 2 |  | AWGN +220 Hz |
|  |  | Config 3 |  | AWGN +500 Hz |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For unpaired spectrum, a DL BWP is linked with an UL BWP. DLBWP.0.2 is linked with ULBWP.0.2; DLBWP.1.1 is linked with ULBWP.1.1; DLBWP.1.3 is linked with ULBWP.1.3 defined in clause 12 of TS 38.213 [3]. |  |  |  |  |

A.19.4.3.1.1.2 Test Requirements

During T1, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed Cell 1 active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

NOTE: During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first UL slot that occurs after beginning of DL slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

#### A.19.4.3.2 RRC-based Active BWP Switch

##### A.19.4.3.2.1 NR FR1 DL active BWP switch of Cell with non-DRX in SA

A.19.4.3.2.1.1 Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6D.

The supported test configurations are shown in table A.19.4.3.2.1.1-1. The test scenario comprises of one Cell (Cell 1) as given in table A.19.4.3.2.1.1-2. Cell-specific parameters of Cell are specified in table A.19.4.3.2.1.1-3 below.

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

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.3.2.1.1-1: DL BWP switch supported test configurations in SA scenario

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.19.4.3.2.1.1-2: General test parameters for DL BWP switch in SA scenario

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active Cell |  | Cell 1 | Cell on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| PDCCH and PDSCH maximum number of HARQ transmission |  | 1 |  |
| T1 | s | 0.2 |  |

Table A.19.4.3.2.1.1-3: NR Cell specific test parameters for DL BWP switch in SA scenario

| Parameter |  |  | Unit | Cell 1 |
| --- | --- | --- | --- | --- |
| Frequency Range |  |  |  | FR1 |
| Duplex mode |  | Config 1 |  | FDD |
|  |  | Config 2,3 |  | TDD |
| TDD configuration |  | Config 1 |  | Not Applicable |
|  |  | Config 2 |  | TDDConf.1.1 |
|  |  | Config 3 |  | TDDConf.2.1 |
| BWchannel |  | Config 1 |  | 10 MHz: NPRB,c = 52 |
|  |  | Config 2 |  | 10 MHz: NPRB,c = 52 |
|  |  | Config 3 |  | 40 MHz: NPRB,c = 106 |
| Active BWP ID |  |  |  | 1 |
| Initial DL BWP Configuration |  | Config 1,2, 3 |  | DLBWP.0.2 |
| Initial UL BWP Configuration |  | Config 1,2, 3 |  | ULBWP.0.2 |
| Initial Condition | Active DL BWP-1 Configuration | Config 1, 2, 3 |  | DLBWP.1.3 |
|  | Active UL BWP-1 Configuration | Config 1, 2, 3 |  | ULBWP.1.3 |
| FinalCondition | Active DL BWP-1 Configuration | Config 1, 2, 3 |  | DLBWP.1.1 |
|  | Active UL BWP-1 Configuration | Config 1, 2, 3 |  | ULBWP.1.1 |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 FDD |
|  |  | Config 2 |  | SR.1.1 TDD |
|  |  | Config 3 |  | SR2.1 TDD |
| RMSI CORESET parameters |  | Config 1 |  | CR.1.1 FDD |
|  |  | Config 2 |  | CR.1.1 TDD |
|  |  | Config 3 |  | CR2.1 TDD |
| Dedicated CORESET parameters |  | Config 1 |  | CCR.1.2 FDD |
|  |  | Config 2 |  | CCR.1.2 TDD |
|  |  | Config 3 |  | CCR.2.4 TDD |
| OCNG Patterns |  |  |  | OP.1 |
| SSB Configuration |  | Config 1,2 |  | SSB.1 FR1 |
|  |  | Config 3 |  | SSB.2 FR1 |
| SMTC Configuration |  |  |  | SMTC.1 |
| TRS Configuration |  | Config 1 |  | TRS.1.1 FDD |
|  |  | Config 2 |  | TRS.1.1 TDD |
|  |  | Config 3 |  | TRS.1.2 TDD |
| Propagation condition |  | Config 1, 2 |  | AWGN +220 Hz |
|  |  | Config 3 |  | AWGN +500 Hz |
| Antenna Configuration |  |  |  | 1x2 Low |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS(Note 1) |  |  |  |  |
| NocNote 2 |  | Config 1,2 | dBm/SCS | -104 |
|  |  | Config 3 |  | -101 |
| SS-RSRP Note 3 |  | Config 1,2 | dBm/SCS | -87 |
|  |  | Config 3 |  | -84 |
| Ês/Iot |  |  | dB | 17 |
| Ês/Noc |  |  | dB | 17 |
| IoNote3 |  | Config 1,2 | dBm/9.36 MHz | -58.96 |
|  |  | Config 3 | dBm/38.16 MHz | -52.86 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For unpaired spectrum, a DL BWP is linked with an UL BWP. DLBWP.0.2 is linked with ULBWP.0.2; DLBWP.1.1 is linked with ULBWP.1.1; DLBWP.1.3 is linked with ULBWP.1.3 defined in clause 12 of TS 38.213 [3]. |  |  |  |  |

A.19.4.3.2.1.2 Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the Cell from the first DL slot that occurs right after the begining of slot $ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}$ and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}+k1 $.

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed Cell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

### A.19.4.4 UE specific CBW change

#### A19.4.4.1 UE specific CBW change on PCell in FR1 in non-DRX

##### A19.4.4.1.1 Test Purpose and Environment

The purpose of this test is to verify the UE specific CBW change delay requirement defined in clause 8.13D.

The supported test configurations are shown in table A.19.4.4.1.1-1. The test scenario comprises of one Cell (Cell 1), which is PCell as given in table A.19.4.4.1.1-2. Cell-specific parameters are specified in table A.19.4.4.1.1-3.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE sends ACK/NACK during the test.

Before the test starts:

- UE is connected to Cell 1 (PCell) on radio channel 1.

- UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1 (PCell).

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PCell.

- UE has been configured with UE specific CBW (CBW-1).

- UE is indicated in SCS-SpecificCarrier [2] that the UE specific CBW is CBW-1 as the initial condition in Cell 1 (PCell).

Cell 1 (PCell) has constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration containing SCS-SpecificCarrier with updated UE specific CBW, sent from the test equipment to the UE, is completely received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its UE specific CBW with the updated CBW-2 for the final condition.

The UE shall be able to receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}$ as defined in clause 8.13 and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}+k1 $ on the PCell’s BWP-1 on CBW-2 for the final condition. The UE shall be continuously scheduled on the PCell’s BWP-1 on CBW-2  for the final condition starting from the first DL slot right after slot $ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}$.

$ T_{RRCprocessingDelay}$ and $ T_{CBWchangeDelayRRC}$ are defined in clause 8.13.

The test equipment verifies the UE specific CBW switching delay in PCell by estimating the time from the moment the RRC Reconfiguration message including updated UE specific CBW configuration is sent until the moment a vaild ACK/NACK is received.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.4.1.1-1: Supported test configurations for UE specific CBW change in SA scenario

| Configuration | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.19.4.4.1.1-2: General test parameters for UE specific CBW change in SA scenario

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active Cell |  | Cell 1 | Cell on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| T1 | s | 0.2 |  |

Table A.19.4.4.1.1-3: NR Cell specific test parameters for UE specific CBW change in SA scenario

| Parameter |  |  | Unit | Cell 1 |
| --- | --- | --- | --- | --- |
| Frequency Range |  |  |  | FR1 |
| Duplex mode |  | Config 1 |  | FDD |
|  |  | Config 2,3 |  | TDD |
| TDD configuration |  | Config 1 |  | Not Applicable |
|  |  | Config 2 |  | TDDConf.1.1 |
|  |  | Config 3 |  | TDDConf.2.1 |
| BWchannel |  | Config 1 |  | 10 MHz: NPRB,c = 52 |
|  |  | Config 2 |  | 10 MHz: NPRB,c = 52 |
|  |  | Config 3 |  | 40 MHz: NPRB,c = 106 |
| Active DL BWP ID |  | Config 1,2, 3 |  | 1 |
| Initial DL BWP Configuration (BWP-1) |  | Config 1,2, 3 |  | DLBWP.0.2 |
| Initial UL BWP Configuration |  | Config 1,2, 3 |  | ULBWP.0.2 |
| Initial Condition | Active DLCBW-1 Configureation | Config 1, 2, 3 |  | DLCBW.1.1 |
|  | Active UL CBW-1Configuration | Config 1, 2, 3 |  | ULCBW.1.1 |
| Final Condition | Active DLCBW-1 Configureation | Config 1, 2, 3 |  | DLCBW.1.2 |
|  | Active UL CBW-1Configuration | Config 1, 2, 3 |  | ULCBW.1.2 |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 FDD |
|  |  | Config 2 |  | SR.1.1 TDD |
|  |  | Config 3 |  | SR2.1 TDD |
| RMSI CORESET parameters |  | Config 1 |  | CR.1.1 FDD |
|  |  | Config 2 |  | CR.1.1 TDD |
|  |  | Config 3 |  | CR2.1 TDD |
| Dedicated CORESET parameters |  | Config 1 |  | CCR.1.1 FDD |
|  |  | Config 2 |  | CCR.1.1 TDD |
|  |  | Config 3 |  | CCR.2.1 TDD |
| OCNG Patterns |  |  |  | OP.1 |
| SSB Configuration |  | Config 1,2 |  | SSB.1 FR1 |
|  |  | Config 3 |  | SSB.2 FR1 |
| SMTC Configuration |  |  |  | SMTC.1 |
| TRS Configuration |  | Config 1 |  | TRS.1.1 FDD |
|  |  | Config 2 |  | TRS.1.1 TDD |
|  |  | Config 3 |  | TRS.1.2 TDD |
| Propagation condition |  | Config 1, 2 |  | AWGN +220 Hz |
|  |  | Config 3 |  | AWGN +500 Hz |
| Antenna Configuration |  |  |  | 1x2 Low |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS(Note 1) |  |  |  |  |
| NocNote 2 |  | Config 1,2 | dBm/SCS | -104 |
|  |  | Config 3 |  | -101 |
| SS-RSRP Note 3 |  | Config 1,2 | dBm/SCS | -87 |
|  |  | Config 3 |  | -84 |
| Ês/Iot |  |  | dB | 17 |
| Ês/Noc |  |  | dB | 17 |
| IoNote3 |  | Config 1,2 | dBm/9.36 MHz | -58.96 |
|  |  | Config 3 | dBm/38.16 MHz | -52.86 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For unpaired spectrum, a DL BWP is linked with an UL BWP. DLBWP.0.1 is linked with ULBWP.0.1; DLBWP.1.1 is linked with ULBWP.1.1; as defined in clause 12 of TS 38.213 [3]. |  |  |  |  |

##### A.19.4.4.1.2 Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the PCell from the first DL slot that occurs right after the begining of slot $ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}$ and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot $ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}+k1 $.

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed UE specific CBW change delay on the PCell to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

### A.19.4.5 Pathloss reference signal switching delay

#### A.19.4.5.1 MAC-CE based pathloss reference signal switch delay

##### A.19.4.5.1.1 Test Purpose and Environment

The purpose of this test is to verify the MAC-CE based pathloss reference signal switch delay requirement defined in clause 8.14D.

The supported test configurations are shown in table A.19.4.5.1.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.19.4.5.1.1-2. Cell-specific parameters of the cell are specified in table A.19.4.5.1.1-3 below.

The test consists of 3 successive time periods, with duration of T1, T2 and T3, respectively.

Prior to the start of the time duration T1,

- UE is connected to Cell 1 on radio channel 1.

- UE shall be fully synchronized to SSB #0.

During T1,

- The UE shall track SSB #1 so that SSB #1 as a pathloss reference signal is known to the UE.

Time period T2 starts when the UE is configured of the power headroom reporting functionality by upper layers by the test equipment and the UE shall transmit a PHR during T2.

During T2,

- UE is configured with a phr-ProhibitTimer timer value for Cell 1.

- UE is configured with a phr-Tx-PowerFactorChange value for Cell 1.

During T3,

Time period T3 starts when a PDSCH carrying MAC-CE activation for pathloss reference signal switch, sent from the test equipment to the UE to swicth the pathloss reference signal from SSB 0 to SSB 1, is received at the UE side in Cell 1’s slot # denoted i. The UE shall switch its pathloss reference signal to the target one and send PHR.

The UE shall be able to apply the target pathloss reference signal of the serving cell on which pathloss reference signal switch occurs no later than the slot i + $ T_{HARQ}$+ $\lceil  \frac {3 ms + 5*T_{target\_PL-RS}+ 2 ms}{NRslotlength}\rceil  $ as defined in clause 8.14.  The UE shall be able to apply old pathloss reference signals until the slot i + $ T_{HARQ}$+ $ 3N_{slot}^{subframe,µ}$ as defined in clause 8.14.

The test equipment verifies the pathloss RS switch time by counting the slots from the time when the pathloss RS switch command is transmitted till a PHR is received during T3.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.5.1.1-1: MAC-CE based pathloss reference signal switch supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.19.4.5.1.1-2: General test parameters for MAC-CE based pathloss reference signal switch in SA

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Active PCell |  |  | Cell 1 |  |
| RF Channel Number |  |  | 1 |  |
| Duplex mode | Config 1 |  | FDD |  |
|  | Config 2, 3 |  | TDD |  |
| DL initial BWP configuration | Config 1, 2, 3 |  | DLBWP.0.1 |  |
| DL dedicated BWP configuration | Config 1, 2, 3 |  | DLBWP.1.1 |  |
| UL initial BWP configuration | Config 1, 2, 3 |  | ULBWP.0.1 |  |
| UL dedicated BWP configuration | Config 1, 2, 3 |  | ULBWP.1.1 |  |
| TDD Configuration | Config 1 |  | Not Applicable |  |
|  | Config 2 |  | TDDConf.1.1 |  |
|  | Config 3 |  | TDDConf.2.1 |  |
| CORESET Reference Channel | Config 1 |  | CR.1.1 FDD |  |
|  | Config 2 |  | CR.1.1 TDD |  |
|  | Config 3 |  | CR.2.1 TDD |  |
| SSB Configuration | Config 1 |  | SSB.1 FR1 |  |
|  | Config 2 |  | SSB.1 FR1 |  |
|  | Config 3 |  | SSB.2 FR1 |  |
| SMTC Configuration | Config 1, 2 |  | SMTC.1 |  |
|  | Config 3 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing | Config 1, 2 |  | 15 kHz |  |
|  | Config 3 |  | 30 kHz |  |
| SSB index assigned as pathloss RS |  |  | 0 in T1, 0 in T2, 1 in T3 |  |
| OCNG parameters |  |  | OP.1 |  |
| CP length |  |  | Normal |  |
| Correlation Matrix and Antenna Configuration |  |  | 1x2 Low |  |
| DRX |  |  | OFF |  |
| Gap pattern ID |  |  | gp0 |  |
| phr-ProhibitTimer |  | sub frame | 0 |  |
| phr-Tx-PowerFactorChange |  | dB | 5 |  |
| phr-PeriodicTimer |  | sub frame | infinity |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| T1 |  | s | 2 |  |
| T2 |  | s | 2 |  |
| T3 |  | s | 0.2 |  |

Table A.19.4.5.1.1-3: NR Cell specific test parameters for MAC-CE based pathloss reference signal switch in SA

| Parameter |  |  |  | Unit | Test 1 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T3 |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  | dB | 4 |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  | dB | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  | dB | 0 |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  | dB |  |  |  |
| EPRE ratio of PSS to SSS |  |  |  | dB |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  | dB |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  | dB |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  |  |  | dB |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  |  |  | dB |  |  |  |
| SSB with index 0 | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 7 |  |  |
|  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] | Config 1, 2, 3 |  | dBm/15 kHz | -101 |  |  |
|  | ![](media_svg/image14.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 7 |  |  |
|  | SS-RSRP Note 4 |  | Config 1, 2 | dBm/ SCS | -94 |  |  |
|  |  |  | Config 3 |  | -91 |  |  |
| SSB with index 1 | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -3 |  |  |
|  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] | Config 1, 2, 3 |  | dBm/15 kHz | -101 |  |  |
|  | ![](media_svg/image14.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -3 |  |  |
|  | SS-RSRP Note 4 |  | Config 1, 2 | dBm/ SCS | -104 |  |  |
|  |  |  | Config 3 |  | -101 |  |  |
| SSB with index 0Io Note 5 | Config 1, 2 |  |  | dBm | -65.3/9.36 MHz |  |  |
|  | Config 3 |  |  |  | -59.2/38.16 MHz |  |  |
| SSB with index 1Io Note 5 | Config 1, 2 |  |  | dBm | -71.28/9.36 MHz |  |  |
|  | Config 3 |  |  |  | -65.18/38.16 MHz |  |  |
| Propagation condition | Config 1, 2 |  |  |  | AWGN +220 Hz |  |  |
|  | Config 3 |  |  |  | AWGN +500 Hz |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 4: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required.NOTE 5: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters. |  |  |  |  |  |  |  |

##### A.19.4.5.1.2 Test Requirements

During T3, the UE shall start to send the PHR for PCell no later than the slot i + $ T_{HARQ}$+ $\lceil  \frac {3 ms + 5*T_{target\_PL-RS}+ 2 ms}{NRslotlength}\rceil  $.

During T3, the UE shall start to send the PHR for PCell no earlier than the slot i + $ T_{HARQ}$+ $ 3N_{slot}^{subframe,µ}$.

Where, $ T_{HARQ}$ is the timing between pathloss reference MAC-CE activation command and acknowledgement as specified in [7], $ T_{target\_PL-RS}$ is the periodicity of the target pathloss reference signal which is SSB in this test.

During T3, UE shall send L1-RSRP report with measurement results for both SSB0 and SSB1.

All of the above test requirements shall be fulfilled in order for the observed pathloss RS switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The UE shall be given proper uplink transmission grant during T2 and T3.

### A.19.4.6 Interruption

#### A.19.4.6.1 SA interruptions at NR SRS antenna port switching with 1 SRS symbol in a slot in NR-CA

##### A.19.4.6.1.1 Test Purpose and Environment

The purpose of this test is to verify that when a ATG UE performs SRS antenna port switching, i.e. transmits SRS on the antenna port(s) not used for PUCCH/PUSCH transmission and on the antenna port(s) used for PUCCH/PUSCH transmission at different SRS transmission occasions. The test will partly verify the interruption requirements on PCell and SCell in clause 8.2D.1.2.10.

##### A.19.4.6.1.2 Test Parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the FR1 PCell and Cell 2 is activated SCell on the TDD PCC. Only PCC is configured with 1 SRS resources in each SRS resource set with usage set to ‘antennaSwitching’. The test parameters for PCell and SCell are given in table A.19.4.6.1.2-2 and A.19.4.6.1.2-3 below. The test consists of two successive time periods, with duration of T1 and T2, respectively. Immediately at the beginning of T2, the UE is configured with periodic SRS for antenna port switching via RRC reconfiguration. Note that the RRC reconfiguration message should be sent to UE at the time 50 ms before the beginning of T2.

The test equipment verifies that potential interruption is carried out correctly by monitoring ACK/NACK sent in PCell.

Table A.19.4.6.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode for NR PCell and FDD duplex mode for NR SCell |
| 2 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode for NR PCell and TDD duplex mode for NR SCell |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode for NR PCell and TDD duplex mode for NR SCell |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations.NOTE 2: Test configuration for NR PCell and NR SCell are chosen independently. |  |

Table A.19.4.6.1.2-2: General test parameters for SA interruptions at NR SRS antenna switching

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| RF Channel Number |  | 1,2 | Two NR radio channel (1, 2) are used for this test |
| Active PCell |  | Cell 1 | Primary cell on NR RF channel number 1 |
| Configured SCell |  | Cell 2 | Activated secondary cell on NR RF channel number 2 |
| CP length |  | Normal |  |
| DRX |  | OFF | Continuous monitoring of primary cell |
| Cell 2 timing offset to cell1 | s | 0 |  |
| Time alignment error between cell2 and cell1 | s | Time alignment error as specified in TS 38.104 [13] clause 6.5.3.1. | The value of time alignment error depends upon the type of carrier aggregation. |
| T1 | s | 5 |  |
| T2 | ms | 40 | UE shall perform SRS antenna switching during T2 |

Table A.19.4.6.1.2-3: Cell specific test parameters for SA interruptions at NR SRS antenna switching

| Parameter |  |  |  | Unit | T1 |  | T2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Duplex mode |  |  | Config 1 |  | TDD | FDD | TDD | FDD |
|  |  |  | Config 2,3 |  | TDD |  |  |  |
| TDD configuration |  |  | Config 1 |  | TDDConf.1.2 | N/A | TDDConf.1.2 | N/A |
|  |  |  | Config 2 |  | TDDConf.1.2 |  |  |  |
|  |  |  | Config 3 |  | TDDConf.2.3 |  |  |  |
| BWchannel |  |  | Config 1,2 | MHz | 10: NPRB,c = 52 |  |  |  |
|  |  |  | Config 3 |  | 40: NPRB,c = 106 |  |  |  |
| Downlink initial BWP Configuration |  |  |  |  | DLBWP.0.1 |  |  |  |
| Downlink dedicated BWP Configuration |  |  |  |  | DLBWP.1.1 |  |  |  |
| Uplink initial BWP configuration |  |  |  |  | ULBWP.0.1 | N/A | ULBWP.0.1 | N/A |
| Uplink dedicated BWP configuration |  |  |  |  | ULBWP.1.1 | N/A | ULBWP.1.1 | N/A |
| TCI state |  |  |  |  | TCI.State.0 |  |  |  |
| TRS Configuration |  |  |  |  | TRS.1.1 TDD |  |  |  |
| PDSCH Reference measurement channel |  |  | Config 1 |  | SR.1.1 FDD | SR.1.1 FDD | SR.1.1 FDD | SR.1.1 FDD |
|  |  |  | Config 2 |  | SR.1.1 TDD | SR.1.1 TDD | SR.1.1 TDD | SR.1.1 TDD |
|  |  |  | Config 3 |  | SR2.1 TDD | SR2.1 TDD | SR2.1 TDD | SR2.1 TDD |
| Dedicated CORESET parameters |  |  | Config 1 |  | CCR.1.1 FDD | CCR.1.1 FDD | CCR.1.1 FDD | CCR.1.1 FDD |
|  |  |  | Config 2 |  | CCR.1.1 TDD | CCR.1.1 TDD | CCR.1.1 TDD | CCR.1.1 TDD |
|  |  |  | Config 3 |  | CCR.2.1 TDD | CCR.2.1 TDD | CCR.2.1 TDD | CCR.2.1 TDD |
| RMSI CORESET parameters |  |  | Config 1 |  | CR.1.1 FDD | CR.1.1 FDD | CR.1.1 FDD | CR.1.1 FDD |
|  |  |  | Config 2 |  | CR.1.1 TDD | CR.1.1 TDD | CR.1.1 TDD | CR.1.1 TDD |
|  |  |  | Config 3 |  | CR2.1 TDD | CR2.1 TDD | CR2.1 TDD | CR2.1 TDD |
| OCNG Patterns |  |  |  |  | OP.1 |  |  |  |
| SRS Configuration | Config 1,2 |  |  |  | SRS.1, with dedicated SRS configuation in Table A.19.4.6.1.2-4 | N/A | SRS.1, with dedicated SRS configuation in Table A.19.4.6.1.2-4 | N/A |
|  | Config 3 |  |  |  | SRS.2, with dedicated SRS configuation in Table A.19.4.6.1.2-4 | N/A | SRS.2, with dedicated SRS configuation in Table A.19.4.6.1.2-4 | N/A |
| SSB Configuration | Config 1,2 |  |  |  | SSB.1 FR1 |  |  |  |
|  | Config 3 |  |  |  | SSB.2 FR1 |  |  |  |
| SMTC configuration |  |  |  |  | SMTC.1 |  |  |  |
| EPRE ratio of PSS to SSS |  |  |  | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 2) |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note3 |  |  | Config 1,2 | dBm/15kHz | -104 |  |  |  |
|  |  |  | Config 3 |  | -101 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  |  | dB | 17 |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  |  | dB | 17 |  |  |  |
| SS-RSRPNote4 |  |  | Config 1,2 | dBm/SCS | -87 |  |  |  |
|  |  |  | Config 3 |  | -84 |  |  |  |
| SCH_RP Note 4 |  |  |  | dBm/15 kHz | -87 |  |  |  |
| Propagation condition |  | Config 1,2 |  | - | AWGN + 220Hz |  |  |  |
|  |  | Config 3 |  |  | AWGN + 500Hz |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and SCH_RP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T2. |  |  |  |  |  |  |  |  |

Table A.19.4.6.1.2-4: Specific Sounding Reference Symbol Configuration for xTyR configuration

| Parameter |  | xTyR configuration |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 1T2R |  | 2T4R |  | 1T4R |  |  |  |
| srs-ResourceId |  | 0 | 1 | 0 | 1 | 0 | 1 | 2 | 3 |
| startPosition |  | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| nrofSRS-Ports |  | port1 | port1 | port2 | port2 | port1 | port1 | port1 | port1 |
| nrofSymbols |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| periodicityAndOffset-p | Config 1,2 | sl40, 1 | sl40, 6 | sl40, 1 | sl40, 6 | sl40, 1 | sl40, 6 | sl40, 11 | sl40, 16 |
|  | Config 3 | sl80, 3 | sl80, 13 | sl80, 3 | sl80, 13 | sl80, 3 | sl80, 13 | sl80, 23 | sl80, 33 |

##### A.19.4.6.1.3 Test Requirements

The UE shall be scheduled on SCell continuously throughout the test.

During the time duration T2, the DL interruption on NR SCell during the SRS antenna switching in each SRS transmission slot on NR PCell shall not exceed 1 slot if SCell is indicated in txSwitchImpactToRx.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.19.4.6.2 SA interruptions at NR SRS antenna port switching with more than 1 SRS symbol in a slot in NR-CA

##### A.19.4.6.2.1 Test Purpose and Environment

The purpose of this test is to verify that when a ATG UE performs SRS antenna port switching with more than 1 SRS symbols on aggressor CC defined in clause 8.2D.1.2.10. The interruption requirement is defined based on the band combination capability reported by UE, i.e., based on txSwitchImpactToRx as specified in requirement applicability in clause 8.2D.1.2.10.

##### A.19.4.6.2.2 Test Parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the FR1 PCell and Cell 2 is FR1 SCell. The UE is configured with the SRS antenna port in FR1 PCell. The test parameters for PCell and SCell are given in table A.19.4.6.2.2-2 and A.19.4.6.2.2-3 below. Common SRS configuration is given in clause A.3.24. Dedicated SRS configuration which is dependent on reported SRS capability supportedSRS-TxPortSwitch, is given in table A.19.4.6.2.2-4. The test consists of two successive time periods, with duration of T1 and T2, respectively. Immediately at the beginning of T2, the UE is triggered for SRS antenna port switching.

The test equipment verifies that potential interruption is carried out correctly by monitoring ACK/NACK sent in PCell.

Table A.19.4.6.2.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode for NR PCell and FDD duplex mode for NR SCell |
| 2 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode for NR PCell and TDD duplex mode for NR SCell |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode for NR PCell and TDD duplex mode for NR SCell |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations. NOTE 2: Test configuration for NR PCell and NR SCell are chosen independently. |  |

Table A.19.4.6.2.2-2: General test parameters for SA interruptions at NR SRS antenna switching

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| RF Channel Number |  | 1,2 | Two NR radio channel (1, 2) are used for this test |
| Active PCell |  | Cell 1 | Primary cell on NR RF channel number 1 |
| Configured SCell |  | Cell 2 | Activated secondary cell on NR RF channel number 2 |
| CP length |  | Normal |  |
| DRX |  | OFF | Continuous monitoring of primary cell |
| Cell 2 timing offset to cell1 | s | 0 |  |
| Time alignment error between cell2 and cell1 | s | Time alignment error as specified in TS 38.104 [13] clause 6.5.3.1. | The value of time alignment error depends upon the type of carrier aggregation. |
| T1 | s | 5 |  |
| T2 | ms | 40 | UE shall perform SRS antenna switching during T2 |

Table A.19.4.6.2.2-3: Cell specific test parameters for SA interruptions at NR SRS antenna switching

| Parameter |  | Unit | T1 |  | T2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Duplex mode | Config 1 |  | TDD | FDD | TDD | FDD |
|  | Config 2,3 |  | TDD |  |  |  |
| TDD configuration | Config 1 |  | TDDConf.1.2 | N/A | TDDConf.1.2 | N/A |
|  | Config 2 |  | TDDConf.1.2 |  |  |  |
|  | Config 3 |  | TDDConf.2.3 |  |  |  |
| BWchannel | Config 1,2 | MHz | 10: NPRB,c = 52 |  |  |  |
|  | Config 3 |  | 40: NPRB,c = 106 |  |  |  |
| Downlink initial BWP Configuration |  |  | DLBWP.0.1 |  |  |  |
| Downlink dedicated BWP Configuration |  |  | DLBWP.1.1 |  |  |  |
| Uplink initial BWP configuration |  |  | ULBWP.0.1 | N/A | ULBWP.0.1 | N/A |
| Uplink dedicated BWP configuration |  |  | ULBWP.1.1 | N/A | ULBWP.1.1 | N/A |
| TCI state |  |  | TCI.State.0 |  |  |  |
| TRS Configuration |  |  | TRS.1.1 TDD |  |  |  |
| PDSCH Reference measurement channel | Config 1 |  | SR.1.1 FDD | SR.1.1 FDD | SR.1.1 FDD | SR.1.1 FDD |
|  | Config 2 |  | SR.1.1 TDD | SR.1.1 TDD | SR.1.1 TDD | SR.1.1 TDD |
|  | Config 3 |  | SR2.1 TDD | SR2.1 TDD | SR2.1 TDD | SR2.1 TDD |
| Dedicated CORESET parameters | Config 1 |  | CCR.1.1 FDD | CCR.1.1 FDD | CCR.1.1 FDD | CCR.1.1 FDD |
|  | Config 2 |  | CCR.1.1 TDD | CCR.1.1 TDD | CCR.1.1 TDD | CCR.1.1 TDD |
|  | Config 3 |  | CCR.2.1 TDD | CCR.2.1 TDD | CCR.2.1 TDD | CCR.2.1 TDD |
| RMSI CORESET parameters | Config 1 |  | CR.1.1 FDD | CR.1.1 FDD | CR.1.1 FDD | CR.1.1 FDD |
|  | Config 2 |  | CR.1.1 TDD | CR.1.1 TDD | CR.1.1 TDD | CR.1.1 TDD |
|  | Config 3 |  | CR2.1 TDD | CR2.1 TDD | CR2.1 TDD | CR2.1 TDD |
| OCNG Patterns |  |  | OP.1 |  |  |  |
| SRS Configuration | Config 1,2 |  | SRS.1, with dedicated SRS configuation in Table A.19.4.6.2.2-4 | N/A | SRS.1, with dedicated SRS configuation in Table A.19.4.6.2.2-4 | N/A |
|  | Config 3 |  | SRS.2, with dedicated SRS configuation in Table A.19.4.6.2.2-4 | N/A | SRS.2, with dedicated SRS configuation in Table A.19.4.6.2.2-4 | N/A |
| SSB Configuration | Config 1,2 |  | SSB.1 FR1 |  |  |  |
|  | Config 3 |  | SSB.2 FR1 |  |  |  |
| SMTC configuration |  |  | SMTC.1 |  |  |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 2) |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note3 | Config 1,2 | dBm/15kHz | -104 |  |  |  |
|  | Config 3 |  | -101 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 17 |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 17 |  |  |  |
| SS-RSRPNote4 | Config 1,2 | dBm/SCS | -87 |  |  |  |
|  | Config 3 |  | -84 |  |  |  |
| SCH_RP Note 4 |  | dBm/15 kHz | -87 |  |  |  |
| Propagation condition | Config 1,2 | - | AWGN + 220Hz |  |  |  |
|  | Config 3 |  | AWGN + 500Hz |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and SCH_RP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T2.NOTE 5: Test configuration for NR PCell and NR SCell are chosen independently. |  |  |  |  |  |  |

Table A.19.4.6.2.2-4: Specific Sounding Reference Symbol Configuration for xTyR configuration

| Parameter |  | xTyR configuration |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 1T2R |  | 2T4R |  | 1T4R |  |  |  |
| srs-ResourceId |  | 0 | 1 | 0 | 1 | 0 | 1 | 2 | 3 |
| startPosition |  | 5 | 3 | 5 | 3 | 5 | 3 | 5 | 3 |
| nrofSRS-Ports |  | port1 | port1 | port2 | port2 | port1 | port1 | port1 | port1 |
| nrofSymbols |  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| periodicityAndOffset-p | Config 1,2 | sl40, 1 | sl40, 1 | sl40, 1 | sl40, 1 | sl40, 1 | sl40, 1 | sl40, 6 | sl40, 6 |
|  | Config 3 | sl80, 3 | sl80, 3 | sl80, 3 | sl80, 3 | sl80, 3 | sl80, 13 | sl80, 13 | sl80, 13 |

##### A.19.4.6.2.3 Test Requirements

The UE shall be scheduled on PCell continuously throughout the test. During the time duration T2, the interruption on SCell shall not be more than the values specified in table 8.2D.1.2.10-2 in clause 8.2D.1.2.10 for each SRS transmission slot.

The rate of correct events observed during repeated tests shall be at least 90 %.

### A.19.4.7 SCell Activation and Deactivation Delay for ATG

#### A.19.4.7.1 SCell Activation and deactivation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle

##### A.19.4.7.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3D, when the SCell in FR1 is known by the UE at the time of activation. Besides, the interruption on PCell due to SCell activation and deactivation is also verified in this test.

The supported test configurations for NR PCell are shown in table A.19.4.7.1.1-1 below. Supported test configurations for NR SCell are shown in table A.19.4.7.1.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently. The test parameters are given in tables A.19.4.7.1.1-2 and cell-specific parameters in tables A.19.4.7.1.1-3 and A.19.4.7.1.1-4 below. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot $ n+\frac {T_{HARQ}+T_{activation\_time}+T_{CSI\_Reporting}}{NR slot length}$, as defined in clause 8.3D. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in 5.2.2.5 in [26], and reporting after slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$ and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot $ n+1+\frac {T_{HARQ}}{NR slot length}$ to $ n+1+\frac {T_{HARQ}+3 ms+T_{X}}{NR slot length}+N_{interruption}$, as defined in clause 8.3D, where $ N_{interruption}$ is the interruption length given in clause 8.2D.

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot $ m+\frac {T_{HARQ}+3ms}{NR slot length}$, as defined in clause 8.3D, and The starting point of any PCell interruption due to the deactivation shall occur in the slot $ m+1+\frac {T_{HARQ}}{NR slot length}$ to $ m+1+\frac {T_{HARQ}+3 ms}{NR slot length}$, as defined in clause 8.3D.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.19.4.7.1.1-1: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR PCell

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, ≥10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, ≥10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, ≥40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurationsNOTE 2: The UE is only required to be tested in one with smallest aggregated channel bandwidth from supported band combinations which is composed of CCs ≥ the bandwidth (BWchannel) defined in each test configuration, |  |

Table A.19.4.7.1.1-1A: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR SCell

| ConfigSCell | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, ≥10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, ≥10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30kHz SSB SCS, ≥40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurationsNOTE 2: The UE is only required to be tested in one with smallest aggregated channel bandwidth from supported band combinations which is composed of CCs ≥ the bandwidth (BWchannel) defined in each test configuration, |  |

Table A.19.4.7.1.1-2: General test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| RF Channel Number |  | 1,2 | Two NR radio channel (1, 2) are used for this test |
| Active PCell |  | Cell 1 | Primary cell on NR RF channel number 1 |
| Configured deactivated SCell |  | Cell 2 | Configured deactivated secondary cell on NR RF channel number 2 |
| CP length |  | Normal |  |
| DRX |  | OFF | Continuous monitoring of primary cell |
| Cell-individual offset for cells on NR channel number | dB | 0 | Individual offset for cells on primary component carrier |
| SCell measurement cycle (measCycleSCell) | ms | 160 |  |
| Cell 2 timing offset to cell1 | s | 0 |  |
| Time alignment error between cell2 and cell1 | s | Time alignment error as specified in TS 38.104 [13] clause 6.5.3.1. | The value of time alignment error depends upon the type of carrier aggregation |
| T1 | s | 7 | During this time the PCell shall be known and the SCell configured and detected |
| T2 | s | 1 | During this time the UE shall activate the SCell |
| T3 | s | 1 | During this time the UE shall deactivate the SCell |
| A3-offset | dB | -15 |  |
| THARQ | ms | Config 1: 2Config 2: 3Config 3: 2.5 | k1 $\times  $ NR slot lengthk1 is a number of slots and is indicated by the PDSCH-to-HARQ-timing-indicator field in the DCI format, if present, or provided by dl-DataToUL-ACK, the value of k should be the minimum value defined in TS 38.213 [3] that will meet the timing constraints of this test case |
| TCSI_Reporting | ms | 15 | The delay (in ms) including uncertainty in acquiring the first available downlink CSI reference resource, UE processing time for CSI reporting (clause 5.2.2.5 in TS 38.214 [26]) and uncertainty in acquiring the first available CSI reporting resources as specified in TS 38.331 [2] |

Table A.19.4.7.1.1-3: Cell specific test parameters for NR PCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

| Parameter |  |  | Unit | Cell 1 |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 |
| Duplex mode |  | Config 1 |  | FDD |  |  |
|  |  | Config 2,3 |  | TDD |  |  |
| TDD configuration |  | Config 1 |  | Not applicable |  |  |
|  |  | Config 2 |  | TDDConf.1.1 |  |  |
|  |  | Config 3 |  | TDDConf.2.1 |  |  |
| BWchannel |  | Config 1,2 | MHz | Note 7 |  |  |
|  |  | Config 3 |  | Note 7 |  |  |
| BWoccupied |  | Config 1,2 | RB | 52 Note 5 |  |  |
|  |  | Config 3 |  | 106 Note 6 |  |  |
| Initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |
| TCI state |  |  |  | TCI.State.0 |  |  |
| TRS Configuration |  | Config 1 |  | TRS.1.1 FDD |  |  |
|  |  | Config 2 |  | TRS.1.1 TDD |  |  |
|  |  | Config 3 |  | TRS.1.2 TDD |  |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 FDD |  |  |
|  |  | Config 2 |  | SR.1.1 TDD |  |  |
|  |  | Config 3 |  | SR.2.1 TDD |  |  |
| Dedicated CORESET parameters |  | Config 1 |  | CCR.1.1 FDD |  |  |
|  |  | Config 2 |  | CCR.1.1 TDD |  |  |
|  |  | Config 3 |  | CCR.2.1 TDD |  |  |
| RMSI CORESET parameters |  | Config 1 |  | CR.1.1 FDD |  |  |
|  |  | Config 2 |  | CR.1.1 TDD |  |  |
|  |  | Config 3 |  | CR.2.1 TDD |  |  |
| OCNG Patterns |  | Config 1,2 |  | OP.1Note 5 |  |  |
|  |  | Config 3, |  | OP.1 Note 6 |  |  |
| SSB Configuration |  | Config 1,2 |  | SSB.1 FR1 |  |  |
|  |  | Config 3 |  | SSB.2 FR1 |  |  |
| CSI-RS configuration for CSI reporting (Note 8) |  | Config 1 |  | CSI-RS.1.1 FDD |  |  |
|  |  | Config 2 |  | CSI-RS.1.1 TDD |  |  |
|  |  | Config 3 |  | CSI-RS.2.1 TDD |  |  |
| SMTC configuration |  |  |  | SMTC.1 |  |  |
| reportConfigType |  |  |  | periodic |  |  |
| reportQuantity |  |  |  | cri-RI-PMI-CQI |  |  |
| CSI reporting periodicity |  | Config 1,2 | slot | 5 |  |  |
|  |  | Config 3 |  | 10 |  |  |
| CSI reporting offset |  | Config 1,2 | slot | 3 |  |  |
|  |  | Config 3 |  | 5 |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS Note 1 |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | Config 1,2 | dBm/SCS | -104 |  |  |
|  |  | Config 3 |  | -101 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 17 |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 17 |  |  |
| SS-RSRPNote3 |  | Config 1,2 | dBm/SCS | -87 |  |  |
|  |  | Config 3 |  | -84 |  |  |
| SCH_RP Note 3 |  |  | dBm/15 kHz | -87 |  |  |
| Io Note3 |  | Config 1,2 | dBm/9.36 MHz | -58.96 |  |  |
|  |  | Config 3 | dBm/38.16 MHz | -52.87 |  |  |
| Propagation condition | Config 1,2 |  | - | AWGN + 220Hz |  |  |
|  | Config 3 |  |  | AWGN + 500Hz |  |  |
| Correlation Matrix and Antenna Configuration |  |  | - | 2x2 Low |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled within BWoccupied.NOTE 3: SS-RSRP and SCH_RP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T2.NOTE 5: All UL/DL transmission shall be confined within BWoccupied (i.e. 10 MHz, 52 PRBs) from FC,low, and Io is independent of the BWchannel configured.NOTE 6: All UL/DL transmission shall be confined within BWoccupied (i.e. 40 MHz, 106 PRBs) from FC,low, and Io is independent of the BWchannel configured.NOTE 7: NPRB,c. is derived from Table 5.3.2-1 in TS38.101-1[2] with configured BWchannel.NOTE 8:  On top of the reference configurations, CSI-RS offset should be set to meet the CSI reference resource timing definition in TS 38.214 [26] clause 5.2.2.5. |  |  |  |  |  |  |

Table A.19.4.7.1.1-4: Cell specific test parameters for NR SCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

| Parameter |  | Unit | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| Duplex mode | ConfigSCell 1 |  | FDD |  |  |
|  | ConfigSCell 2,3 |  | TDD |  |  |
| TDD configuration | ConfigSCell 1 |  | Not applicable |  |  |
|  | ConfigSCell 2 |  | TDDConf.1.1 |  |  |
|  | ConfigSCell 3 |  | TDDConf.2.1 |  |  |
| BWchannel | ConfigSCell 1,2 | MHz | Note 7 |  |  |
|  | ConfigSCell 3 |  | Note 7 |  |  |
| BWoccupied | ConfigSCell 1,2 | RB | 52 Note 5 |  |  |
|  | ConfigSCell 3 |  | 106 Note 6 |  |  |
| Initial BWP configuration |  |  | DLBWP.0.1 |  |  |
| TCI state |  |  | TCI.State.0 |  |  |
| TRS Configuration | ConfigSCell 1 |  | TRS.1.1 FDD |  |  |
|  | ConfigSCell 2 |  | TRS.1.1 TDD |  |  |
|  | ConfigSCell 3 |  | TRS.1.2 TDD |  |  |
| PDSCH Reference measurement channel | ConfigSCell 1 |  | N/A |  |  |
|  | ConfigSCell 2 |  | N/A |  |  |
|  | ConfigSCell 3 |  | N/A |  |  |
| Dedicated CORESET parameters | ConfigSCell 1 |  | N/A |  |  |
|  | ConfigSCell 2 |  | N/A |  |  |
|  | ConfigSCell 3 |  | N/A |  |  |
| RMSI CORESET parameters | ConfigSCell 1 |  | N/A |  |  |
|  | ConfigSCell 2 |  | N/A |  |  |
|  | ConfigSCell 3 |  | N/A |  |  |
| OCNG Patterns | ConfigSCell 1,2 |  | OP.1Note 5 |  |  |
|  | ConfigSCell 3, |  | OP.1 Note 6 |  |  |
| SSB Configuration | ConfigSCell 1,2 |  | SSB.1 FR1 |  |  |
|  | ConfigSCell 3 |  | SSB.2 FR1 |  |  |
| CSI-RS configuration for CSI reporting Note 8 | ConfigSCell 1 |  | CSI-RS.1.1 FDD |  |  |
|  | ConfigSCell 2 |  | CSI-RS.1.1 TDD |  |  |
|  | ConfigSCell 3 |  | CSI-RS.2.1 TDD |  |  |
| SMTC configuration |  |  | SMTC.1 |  |  |
| reportConfigType |  |  | N/A |  |  |
| reportQuantity |  |  | N/A |  |  |
| CSI reporting periodicity | ConfigSCell 1,2 | slot | N/A |  |  |
|  | ConfigSCell 3 |  | N/A |  |  |
| CSI reporting offset | ConfigSCell 1,2 | slot | N/A |  |  |
|  | ConfigSCell 3 |  | N/A |  |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS Note 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | ConfigSCell 1,2 | dBm/SCS | -104 |  |  |
|  | ConfigSCell 3 |  | -101 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 17 |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 17 |  |  |
| SS-RSRPNote3 | ConfigSCell 1,2 | dBm/SCS | -87 |  |  |
|  | ConfigSCell 3 |  | -84 |  |  |
| SCH_RP Note 3 |  | dBm/15 kHz | -87 |  |  |
| Io Note3 | ConfigSCell 1,2 | dBm/9.36 MHz | -58.96 |  |  |
|  | ConfigSCell 3 | dBm/38.16 MHz | -52.87 |  |  |
| Propagation condition | ConfigSCell 1,2 | - | AWGN + 220Hz |  |  |
|  | ConfigSCell 3 |  | AWGN + 500Hz |  |  |
| Correlation Matrix and Antenna Configuration |  |  | 2x2 Low |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled within BWoccupied.NOTE 3: SS-RSRP and SCH_RP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T2.NOTE 5: All UL/DL transmission shall be confined within BWoccupied (i.e. 10 MHz, 52 PRBs) from FC,low, and Io is independent of the BWchannel configured.NOTE 6: All UL/DL transmission shall be confined within BWoccupied (i.e. 40 MHz, 106 PRBs) from FC,low, and Io is independent of the BWchannel configured.NOTE 7: NPRB,c. is derived from Table 5.3.2-1 in TS38.101-1[18] with configured BWchannel.NOTE 8: On top of the reference configurations, CSI-RS offset should be set to meet the CSI reference resource timing definition in clause 5.2.2.5 in TS 38.214 [26]. |  |  |  |  |  |

##### A.19.4.7.1.2 Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in clause 5.2.2.5 in TS 38.214 [26], and reporting after slot ($ n+1+\frac {T_{HARQ}+3 ms}{NR slot length}$). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.

During T3 the UE shall stop sending CSI reports for SCell at latest in a slot $ m+\frac {T_{HARQ}+3 ms}{NR slot length}$, as defined in clause 8.3D.

During T2 interruption of PCell during SCell activation shall not happen outside the slot $ n+1+\frac {T_{HARQ}}{NR slot length}$ to $ n+1+\frac {T_{HARQ}+3 ms+T_{X}}{NR slot length}+N_{interruption}$, as defined in clause 8.3D.

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot $ m+1+\frac {T_{HARQ}}{NR slot length}$ to $ m+1+\frac {T_{HARQ}+3 ms}{NR slot length}$, as defined in clause 8.3D.

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2D.1.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE: During T2 if there are no uplink resources for reporting the valid CSI in a slot $\frac {T_{HARQ}+T_{activtion\_time}+T_{CSI\_Reporting}}{NR slot length}$ as defined in clause 8.3D then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.

#### A.19.4.7.2 SCell Activation and deactivation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle

##### A.19.4.7.2.1 Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.19.4.7.1.1. The supported test configurations are the same as defined in clause A.19.4.7.1.1. The test parameters are the same except those described in the following clause. The listed parameter values in tables A.19.4.7.2.1-1 will replace the values of corresponding parameters in tables A.19.4.7.1.1-1.

Table A.19.4.7.2.1-1: General test parameters for known FR1 SCell activation case, 640 ms SCell measurement cycle

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| SCell measurement cycle (measCycleSCell) | ms | 640 |  |

##### A.19.4.7.2.2 Test Requirements

The test requirements defined in clause A.19.4.7.1.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstSSB_MAX + Trs + 5 ms.

#### A.19.4.7.3 SCell Activation and deactivation of unknown SCell in FR1 in non-DRX

##### A.19.4.7.3.1 Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3D, when the SCell in FR1 is unknown by the UE at the time of activation. and both the PCell and SCell are co-located in an ATG NR SA configuration. The test also verifies that any PCell interruption occurring due to SCell activation or deactivation remains within the limits defined in clause 8.2D.

The supported test configurations are shown in table A.6.5.3.1.1-1 and table A.6.5.3.1.1-1A. The test parameters are given in table A.6.5.3.1.1-2 and cell-specific parameters in table A.6.5.3.1.1-3, except the parameters that are defined in A.19.4.7.3.1-1. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot $ n+\frac {T_{HARQ}+T_{activation\_time}+T_{CSI\_Reporting}}{NR slot length}$, as defined in clause 8.3D. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in 5.2.2.5 in [26], and reporting after slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$ and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot $ n+1+\frac {T_{HARQ}}{NR slot length}$ to $ n+1+\frac {T_{HARQ}+3 ms+T_{X}}{NR slot length}+N_{interruption}$, as defined in clause 8.3D, where $ N_{interruption}$ is the interruption length given in clause 8.2D.

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot $ m+\frac {T_{HARQ}+3ms}{NR slot length}$, as defined in clause 8.3D, and The starting point of any PCell interruption due to the deactivation shall occur in the slot $ m+1+\frac {T_{HARQ}}{NR slot length}$ to $ m+1+\frac {T_{HARQ}+3 ms}{NR slot length}$, as defined in clause 8.3D.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.19.4.7.3.1-1: General test parameters for unknown FR1 SCell activation case, 160 ms SCell measurement cycle

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| T1 |  | ms | 100 | During this time the PCell shall be known and the SCell configured, but not detected. |
| Propagation Condition | Config 1,2,1A,2A |  | AWGN + 220Hz |  |
|  | Config 3,3A |  | AWGN +500Hz |  |

##### A.19.4.7.3.2 Test Requirements

The test requirements defined in clause A.6.5.3.3.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstSSB_MAX + TSMTC_MAX + 2*Trs + 5 ms as defined in clause 8.3D.

#### A.19.4.7.4 Direct SCell activation at SCell addition of known SCell in FR1

##### A.19.4.7.4.1 Test Purpose and Environment

The purpose of this test is to verify fulfillment of direct SCell activation delay and interruption requirements at SCell addition as defined in clause 8.3D.4 and 8.2D.1, respectively. The supported test configurations for NR PCell are shown in table A.19.4.7.4.1-1. The supported test configurations for NR SCell are shown in table A.19.4.7.4.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently.

The test scenario comprises one PCell (Cell 1) and one SCell (Cell 2) as outlined in table A.19.4.7.4.1-2. Cell-specific parameters are provided in table A.19.4.7.4.1-3 and table A.19.4.7.4.1-4.

The test consists of two successive time periods with duration T1 and T2, respectively. There are two carriers, each with one cell. Cell 1 (PCell) is on RF channel 1 (PCC), and Cell 2 (SCell) is on RF channel 2 (SCC). Cell 1 and Cell 2 both operate according to one of the configurations in table A.19.4.7.4.1-1 and table A.19.4.7.4.1-1A respectively.

Before the test starts the UE is connected to Cell 1 on RF channel 1. The UE is only monitoring RF channel 1 and is not aware of Cell 2 on RF channel 2.

The UE is continuously scheduled in PCell throughout the test.

At the beginning of T1 the UE is configured to measure RF channel 2 in measurement gaps. During T1, the UE detects and measures Cell 2 on RF channel 2, and sends a measurement report containing Cell 2 to the test equipment. After having received a measurement report containing Cell 2, the test equipment deconfigures the measurement gaps and thereafter sends a RRC connection reconfiguration message to the UE by which it configures the SCell (Cell 2) in activated state (sCellState is set to activated). The time between reception of the last measurement report carrying SCell and transmission of the RRC connection reconfiguration message directly activating SCell is kept short enough to allow the SCell to remain known to the UE.

Time period T2 starts when the UE receives the RRC connection reconfiguration message at the UE antenna connector. The corresponding slot at which the message is received at the UE antenna connector is denoted n. The UE shall complete activation of the SCell no later than in slot n + $\frac {N_{direct}}{NR slot length}$, as specified in clause 8.3D.4. From slot n+ $\frac {N_{direct}}{NR slot length}$ and onwards the UE shall report valid CSI both for PCell and SCell.

The test equipment verifies the activation time by counting the slots between the RRC connection reconfiguration message is sent and until CSI report with non-zero CQI for both PCell and SCell is received.

The test equipment verifies that interruptions on other serving cells are within the requirements by counting ACK/NACKs transmitted in PCell.

Table A.19.4.7.4.1-1: Supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |

| NOTE 1: The UE is only required to be tested in one of the supported test configurationsNOTE 2: The UE is only required to be tested in one with smallest aggregated channel bandwidth from supported band combinations which is composed of CCs ≥ the bandwidth (BWchannel) defined in each test configuration, |
| --- |

Table A.19.4.7.4.1-1A: Supported test configurations for NR SCell

| ConfigSCell | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, ≥10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, ≥10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, ≥40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurationsNOTE 2: The UE is only required to be tested in one with smallest aggregated channel bandwidth from supported band combinations which is composed of CCs ≥ the bandwidth (BWchannel) defined in each test configuration. |  |

Table A.19.4.7.4.1-2: General test parameters

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1, 2 | Two NR radio channels are used for this test |
| Active PCell |  | Cell 1 | Primary cell on NR RF channel number 1. |
| Inter-frequency neighbor cell (SCell to-be) |  | Cell 2 | Inter-frequency neighbor cell on NR RF channel number 2 |
| CP length |  | Normal |  |
| DRX |  | OFF | Continuous monitoring of primary cell |
| Measurement gap pattern |  | gp0 | Measurement gap is used during parts of time period T1 for detection of Cell 2. |
| CSI reporting periodicity | ms | 2 | CSI reporting periodicity for periodic reporting of CQI for PCell and, when added, SCell. |
| SCell measurement cycle (measCycleSCell) | ms | 160 | Measurement cycle for SCell does not come into effect in direct activation at SCell addition. |
| Timing offset between Cell 1 and Cell 2 | s | MRTD | The value of maximum timing offset depends upon the carrier aggregation scenario. |
| T1 | s | 7 | During this time period the PCell shall be known and Cell 2 shall be detected as an inter-frequency neighbor cell. |
| T2 | s | 1 | During this time period Cell 2 shall be configured and directly activated as SCell. |
| A3-offset | dB | -15 |  |
| THARQ | ms | k1×NR slot length | k1 is a number of slots indicated by the PDSCH-to-HARQ_feedback timing indicator field in a corresponding DCI format or provided by dl-DataToUL-ACK if the PDSCH-to-HARQ feedback timing field is not present in the DCI format, the value is defined in  38.213 [3] |
| TCSI_Reporting | ms | 2 | the delay uncertainty in acquiring the first available CSI reporting resources as specified in TS 38.331 [2] |
| k | ms | ![](media_svg/image15.svg) [公式≈: _{k}_{1}_{+}_{3}_{∪}_{N}_{slot}subframe,Μ_{+}_{1}] | As specified in clause 4.3 of TS 38.213 [3] |

Table A.19.4.7.4.1-3: NR Cell specific test parameters

| Parameter |  |  | Unit | Cell 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 |
| Duplex mode |  | Config 1 |  | FDD |  |
|  |  | Config 2,3 |  | TDD |  |
| TDD configuration |  | Config 2 |  | TDDConf.1.1 |  |
|  |  | Config 3 |  | TDDConf.2.1 |  |
| BWchannel |  | Config 1,2 | MHz | 10: NPRB,c = 52 |  |
|  |  | Config 3 |  | 40: NPRB,c = 106 |  |
| BWP configuration |  | Initial DL |  | DLBWP.0.1 |  |
|  |  | Initial UL |  | ULBWP.0.1 |  |
|  |  | Dedicated DL |  | DLBWP.1.1 |  |
|  |  | Dedicated UL |  | ULBWP.1.1 |  |
| TCI state |  |  |  | TCI.State.0 |  |
| CSI-RS configuration for CSI reporting |  | Config 1 |  | CSI-RS.1.1 FDD |  |
|  |  | Config 2 |  | CSI-RS.1.1 TDD |  |
|  |  | Config 3 |  | CSI-RS.2.1 TDD |  |
| TRS Configuration |  | Config 1 |  | TRS.1.1 FDD |  |
|  |  | Config 2 |  | TRS.1.1 TDD |  |
|  |  | Config 3 |  | TRS.1.2 TDD |  |
| PDSCH Reference measurement channel |  | Config 1 |  | SR.1.1 FDD |  |
|  |  | Config 2 |  | SR.1.1 TDD |  |
|  |  | Config 3 |  | SR.2.1 TDD |  |
| Dedicated CORESET parameters |  | Config 1 |  | CCR.1.1 FDD |  |
|  |  | Config 2 |  | CCR.1.1 TDD |  |
|  |  | Config 3 |  | CCR.2.1 TDD |  |
| RMSI CORESET parameters |  | Config 1 |  | CR.1.1 FDD |  |
|  |  | Config 2 |  | CR.1.1 TDD |  |
|  |  | Config 3 |  | CR.2.1 TDD |  |
| OCNG Pattern |  |  |  | OP.1 |  |
| SSB Configuration |  | Config 1,2 |  | SSB.1 FR1 |  |
|  |  | Config 3 |  | SSB.2 FR1 |  |
| SMTC configuration |  |  |  | SMTC.1 |  |
| reportConfigType |  |  |  | periodic |  |
| reportQuantity |  |  |  | cri-RI-PMI-CQI |  |
| CSI reporting periodicity |  | Config 1,2 | slot | 5 |  |
|  |  | Config 3 |  | 10 |  |
| CSI reporting offset |  | Config 1,2 | slot | 3 |  |
|  |  | Config 3 |  | 5 |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS Note1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note1 |  |  |  |  |  |
| Noc Note2 | Config 1,2 |  | dBm/SCS | -104 |  |
|  | Config 3 |  |  | -101 |  |
| Ês/Iot |  |  | dB | 17 |  |
| Ês/Noc |  |  | dB | 17 |  |
| SS-RSRP Note3 | Config 1,2 |  | dBm/SCS | -87 |  |
|  | Config 3 |  |  | -84 |  |
| Io Note3 | Config 1,2 |  | dBm/9.36 MHz | -59.0 |  |
|  | Config 3 |  | dBm/38.16 MHz | -52.9 |  |
| Propagation condition | Config 1,2 |  | - | AWGN+220 Hz |  |
|  | Config 3 |  | - | AWGN+500 Hz |  |
| Correlation Matrix and Antenna Configuration |  |  | - | 1x2 Low |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated, and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP, SCH_RP, and Io levels have been derived from other parameters for information purpose. They are not settable parameters themselves. |  |  |  |  |  |

Table A.19.4.7.4.1-4: NR Cell specific test parameters for NR Scell

| Parameter |  | Unit | Cell 2 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| Duplex mode | ConfigSCell 1 |  | FDD |  |
|  | ConfigSCell 2,3 |  | TDD |  |
| TDD configuration | ConfigSCell 2 |  | TDDConf.1.1 |  |
|  | ConfigSCell 3 |  | TDDConf.2.1 |  |
| BWchannel | ConfigSCell 1,2 | MHz | 10: NPRB,c = 52 |  |
|  | ConfigSCell 3 |  | 40: NPRB,c = 106 |  |
| BWP configuration | Initial DL |  | N/A | DLBWP.0.1 |
|  | Initial UL |  |  | N/A |
|  | Dedicated DL |  |  | DLBWP.1.1 |
|  | Dedicated UL |  |  | N/A |
| TCI state |  |  | N/A | TCI.State.0 |
| CSI-RS configuration for CSI reporting | ConfigSCell 1 |  | N/A | CSI-RS.1.1 FDD |
|  | ConfigSCell 2 |  |  | CSI-RS.1.1 TDD |
|  | ConfigSCell 3 |  |  | CSI-RS.2.1 TDD |
| TRS Configuration | ConfigSCell 1 |  | N/A | TRS.1.1 FDD |
|  | ConfigSCell 2 |  |  | TRS.1.1 TDD |
|  | ConfigSCell 3 |  |  | TRS.1.2 TDD |
| PDSCH Reference measurement channel | ConfigSCell 1 |  | N/A | SR.1.1 FDD |
|  | ConfigSCell 2 |  |  | SR.1.1 TDD |
|  | ConfigSCell 3 |  |  | SR.2.1 TDD |
| Dedicated CORESET parameters | ConfigSCell 1 |  | N/A | CCR.1.1 FDD |
|  | ConfigSCell 2 |  |  | CCR.1.1 TDD |
|  | ConfigSCell 3 |  |  | CCR.2.1 TDD |
| RMSI CORESET parameters | ConfigSCell 1 |  | N/A |  |
|  | ConfigSCell 2 |  |  |  |
|  | ConfigSCell 3 |  |  |  |
| OCNG Pattern |  |  | OP.1 |  |
| SSB Configuration | ConfigSCell 1,2 |  | SSB.1 FR1 |  |
|  | ConfigSCell 3 |  | SSB.2 FR1 |  |
| SMTC configuration |  |  | SMTC.1 |  |
| reportConfigType |  |  | N/A |  |
| reportQuantity |  |  | N/A |  |
| CSI reporting periodicity | ConfigSCell 1,2 | slot | N/A |  |
|  | ConfigSCell 3 |  | N/A |  |
| CSI reporting offset | ConfigSCell 1,2 | slot | N/A |  |
|  | ConfigSCell 3 |  | N/A |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS Note1 |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note1 |  |  |  |  |
| Noc Note2 | ConfigSCell 1,2 | dBm/SCS | -104 |  |
|  | ConfigSCell 3 |  | -101 |  |
| Ês/Iot |  | dB | 17 |  |
| Ês/Noc |  | dB | 17 |  |
| SS-RSRP Note3 | ConfigSCell 1,2 | dBm/SCS | -87 |  |
|  | ConfigSCell 3 |  | -84 |  |
| Io Note3 | ConfigSCell 1,2 | dBm/9.36 MHz | -59.0 |  |
|  | ConfigSCell 3 | dBm/38.16 MHz | -52.9 |  |
| Propagation condition | ConfigScell 1, 2 | - | AWGN+220 Hz |  |
|  | ConfigSCell 3 | - | AWGN+500 Hz |  |
| Correlation Matrix and Antenna Configuration |  | - | 1x2 Low |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP, SCH_RP, and Io levels have been derived from other parameters for information purpose. They are not settable parameters themselves. |  |  |  |  |

##### A.19.4.7.4.2 Test Requirements

The UE shall complete the direct activation of the SCell no later than at slot n + $\frac {N_{direct}}{NR slot length}$.

The UE shall report non-zero CQI for SCell from slot n + $\frac {N_{direct}}{NR slot length}$ and onwards throughout time period T2.

The interruption on PCell during direct activation of the SCell shall occur within the interruption window specified in clause 8.3D.4 and shall not exceed the length specified in clause 8.2D.1.2.4.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.19.4.7.5 Direct SCell activation at handover with known SCell in FR1

##### A.19.4.7.5.1 Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD and TDD-TDD intra-frequency handover with direct SCell activation requirements specified in subclause 8.3D.5.

Supported test configurations for NR PCell are shown in table A.19.4.7.5.1-1. Supported test configurations for NR SCell are shown in table A.19.4.7.5.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently. Both handover with direct SCell activation requirements are tested by using the parameters in table A.19.4.7.5.1-2, A.19.4.7.5.1-3 and A.19.4.7.5.1-4.

The test scenario comprises of two NR carriers and 3 cells as given in tables A.19.4.7.5.1-3 and A.19.4.7.5.1-4. The test consists of three successive time periods, with time durations of T1, T2, and T3 respectively.

At the start of time duration T1, the UE is in connected mode with PCell (Cell 1) and UE is reporting CQI for PCell. The UE is configured to measure RF channel 2 in measurement gaps. During T1, the UE detects and measures Cell 2 on RF channel 2 and sends a measurement report containing Cell 2 to the test equipment. After having received a measurement report containing Cell 2, the test equipment deconfigures the measurement gaps and thereafter sends a RRC connection reconfiguration message to the UE. The time between reception of the last measurement report carrying SCell and transmission of the RRC connection reconfiguration message directly activating SCell is kept short enough to allow the SCell to remain known to the UE.

Time period T2 starts when UE receives a handover command to PCell (Cell 3) that also activates SCell 1 (Cell 2). This is done using an RRCReconfiguration message with parameter sCellState set to activated for the SCell 1 (Cell 2). The message is sent from the test equipment to the UE and is received in a subframe # denoted n at the UE antenna connector. The UE shall accomplish the activation of the SCell no later than subframe (n + Ndirect).

Time period T3 starts at (n + Ndirect), at which point UE shall be reporting a valid CQI for both PCell (Cell 3) and SCell 1.

Table A.19.4.7.5.1-1: Intra-frequency handover with direct SCell activation from FR1 to FR1 test configurations for NR PCell

| Config | Description |
| --- | --- |
| 1 | Source PCell: NR 15 kHz SSB SCS, ≥10 MHz bandwidth, FDD duplex modeTarget PCell: NR 15 kHz SSB SCS, ≥10 MHz bandwidth, FDD duplex mode |
| 2 | Source PCell: NR 15 kHz SSB SCS, ≥10 MHz bandwidth, TDD duplex modeTarget PCell: NR 15 kHz SSB SCS, ≥10 MHz bandwidth, TDD duplex mode |
| 3 | Source PCell: NR 30 kHz SSB SCS, ≥40 MHz bandwidth, TDD duplex modeTarget PCell: NR 30 kHz SSB SCS, ≥40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurationsNOTE 2: The UE is only required to be tested in one with smallest aggregated channel bandwidth from supported band combinations which is composed of CCs ≥ the bandwidth (BWchannel) defined in each test configuration, |  |

Table A.19.4.7.5.1-1A: Intra-frequency handover with direct SCell activation from FR1 to FR1 test configurations for NR SCell

| ConfigSCell | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, ≥10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, ≥10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, ≥40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurationsNOTE 2: The UE is only required to be tested in one with smallest aggregated channel bandwidth from supported band combinations which is composed of CCs ≥ the bandwidth (BWchannel) defined in each test configuration. |  |

Table A.19.4.7.5.1-2: General test parameters Intra-frequency handover with direct SCell activation from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | PCell |  | Cell 1 |  |
|  | neighbour cell |  | Cell 2 |  |
|  | Target cell |  | Cell 3 |  |
| Final condition | PCell |  | Cell 3 |  |
|  | SCell |  | Cell 2 |  |
|  | neighbour cell |  | Cell 1 |  |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| PRACH configuration index |  |  | FR1 PRACH configuration 1 | As specified in table 6.3.3.2-3 in TS 38.211 [6] |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| Measurement gap pattern |  |  | gp0 | Measurement gap is used during parts of time period T1 for detection of Cell 2. |
| T1 |  | s | 7 | UE is in connected mode with PCell and SCell 1 (Cell 2) is in activated state. UE receives a handover command |
| T2 |  | s | Ndirect | UE shall accomplish the activation of the SCell |
| T3 |  | s | 1 |  |
| A3-offset |  | dB | -15 |  |
| THARQ |  | slot | k | k is a number of slots indicated by the PDSCH-to-HARQ_feedback timing indicator field in a corresponding DCI format or provided by dl-DataToUL-ACK if the PDSCH-to-HARQ feedback timing field is not present in the DCI format, the value is defined in 38.213 [3] |
| TCSI_Reporting |  | ms | 2 | the delay uncertainty in acquiring the first available CSI reporting resources as specified in TS 38.331 [2] |
| k |  | ms | ![](media_svg/image15.svg) [公式≈: _{k}_{1}_{+}_{3}_{∪}_{N}_{slot}subframe,Μ_{+}_{1}] | As specified in clause 4.3 of TS 38.213 [3] |

Table A.19.4.7.5.1-3: Cell specific test parameters for NR PCell for NR FR1-FR1 Intra-frequency handover with direct SCell activation test case

| Parameter |  | Unit | Cell 1 |  |  | Cell 3 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| NR RF Channel Number |  |  | 1 |  |  | 1 |  |  |
| Duplex mode | Config 1 |  | FDD |  |  |  |  |  |
|  | Config 2,3 |  | TDD |  |  |  |  |  |
| TDD configuration | Config 1 |  | Not Applicable |  |  |  |  |  |
|  | Config 2 |  | TDDConf.1.1 |  |  |  |  |  |
|  | Config 3 |  | TDDConf.2.1 |  |  |  |  |  |
| BWchannel | Config 1 | MHz | 10: NPRB,c = 52 |  |  |  |  |  |
|  | Config 2 |  | 10: NPRB,c = 52 |  |  |  |  |  |
|  | Config 3 |  | 40: NPRB,c = 106 |  |  |  |  |  |
| BWP BW | Config 1 | MHz | 10: NPRB,c = 52 |  |  |  |  |  |
|  | Config 2 |  | 10: NPRB,c = 52 |  |  |  |  |  |
|  | Config 3 |  | 40: NPRB,c = 106 |  |  |  |  |  |
| DRX Cycle |  | ms | Not Applicable |  |  |  |  |  |
| PDSCH Reference measurement channel | Config 1 |  | SR.1.1 FDD |  |  |  |  |  |
|  | Config 2 |  | SR.1.1 TDD |  |  |  |  |  |
|  | Config 3 |  | SR.2.1 TDD |  |  |  |  |  |
| CORESET Reference Channel | Config 1 |  | CR.1.1 FDD |  |  |  |  |  |
|  | Config 2 |  | CR.1.1 TDD |  |  |  |  |  |
|  | Config 3 |  | CR.2.1 TDD |  |  |  |  |  |
| TRS configuration | Config 1 |  | TRS.1.1 FDD |  |  |  |  |  |
|  | Config 2 |  | TRS.1.1 TDD |  |  |  |  |  |
|  | Config 3 |  | TRS.1.2 TDD |  |  |  |  |  |
| OCNG Patterns |  |  | OCNG pattern OP.1 |  |  |  |  |  |
| SMTC Configuration |  |  | SMTC pattern SMTC.1 |  |  |  |  |  |
| SSB Configuration | Config 1,2 |  | SSB.1 FR1 |  |  |  |  |  |
|  | Config 3 |  | SSB.2 FR1 |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing | Config 1,2 | kHz | 15 kHz |  |  |  |  |  |
|  | Config 3 |  | 30 kHz |  |  |  |  |  |
| PUCCH/PUSCH subcarrier spacing | Config 1,2 | kHz | 15 kHz |  |  |  |  |  |
|  | Config 3 |  | 30 kHz |  |  |  |  |  |
| PRACH configuration |  |  | FR1 PRACH configuration 1 |  |  |  |  |  |
| BWP configuraiton | Initial DL BWP |  | DLBWP.0.1 |  |  |  |  |  |
|  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |  |  |
|  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |  |  |
|  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |  |  |
| CSI-RS configuration for CSI reporting | Config 1 |  | CSI-RS.1.1 FDD |  |  |  |  |  |
|  | Config 2 |  | CSI-RS.1.1 TDD |  |  |  |  |  |
|  | Config 3 |  | CSI-RS.2.1 TDD |  |  |  |  |  |
| reportConfigType |  |  | periodic |  |  |  |  |  |
| reportQuantity |  |  | cri-RI-PMI-CQI |  |  |  |  |  |
| CSI reporting periodicity | Config 1,2 | slot | 5 |  |  |  |  |  |
|  | Config 3 |  | 10 |  |  |  |  |  |
| CSI reporting offset | Config 1,2 | slot | 3 |  |  |  |  |  |
|  | Config 3 |  | 5 |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15kHz | -98 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 | dBm/SCS | -98 |  |  |  |  |  |
|  | Config 3 |  | -95 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 8 | 8 | 8 | 8 | 8 | 8 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 8 | 8 | 8 | 8 | 8 | 8 |
| SSB_RP | Config 1,2 | dBm/SCS | -90 | -90 | -90 | -90 | -90 | -90 |
|  | Config 3 | dBm/SCS | -87 | -87 | -87 | -87 | -87 | -87 |
| IoNote3 | Config 1,2 | dBm/9.36 MHz | -58.71 | -58.71 | -58.71 | -58.71 | -58.71 | -58.71 |
|  | Config 3 | dBm/38.16 MHz | -52.60 | -52.60 | -52.60 | -52.60 | -52.60 | -52.60 |
| Propagation condition | Config 1,2 | - | AWGN+220 Hz |  |  | AWGN+220 Hz |  |  |
|  | Config 3 | - | AWGN+500 Hz |  |  | AWGN+500 Hz |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

Table A.19.4.7.5.1-4: Cell specific test parameters for NR SCell for NR FR1-FR1 Intra-frequency handover with direct SCell activation test case

| Parameter |  | Unit | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| NR RF Channel Number |  |  | 2 |  |  |
| Duplex mode | ConfigSCell 1 |  | FDD |  |  |
|  | ConfigSCell 2,3 |  | TDD |  |  |
| TDD configuration | ConfigSCell 1 |  | Not Applicable |  |  |
|  | ConfigSCell 2 |  | TDDConf.1.1 |  |  |
|  | ConfigSCell 3 |  | TDDConf.2.1 |  |  |
| BWchannel | ConfigSCell 1 | MHz | 10: NPRB,c = 52 |  |  |
|  | ConfigSCell 2 |  | 10: NPRB,c = 52 |  |  |
|  | ConfigSCell 3 |  | 40: NPRB,c = 106 |  |  |
| BWP BW | ConfigSCell 1 | MHz | 10: NPRB,c = 52 |  |  |
|  | ConfigSCell 2 |  | 10: NPRB,c = 52 |  |  |
|  | ConfigSCell 3 |  | 40: NPRB,c = 106 |  |  |
| DRX Cycle |  | ms | Not Applicable |  |  |
| PDSCH Reference measurement channel | ConfigSCell 1 |  | SR.1.1 FDD |  |  |
|  | ConfigSCell 2 |  | SR.1.1 TDD |  |  |
|  | ConfigSCell 3 |  | SR.2.1 TDD |  |  |
| CORESET Reference Channel | ConfigSCell 1 |  | CR.1.1 FDD |  |  |
|  | ConfigSCell 2 |  | CR.1.1 TDD |  |  |
|  | ConfigSCell 3 |  | CR.2.1 TDD |  |  |
| TRS configuration | ConfigSCell 1 |  | TRS.1.1 FDD |  |  |
|  | ConfigSCell 2 |  | TRS.1.1 TDD |  |  |
|  | ConfigSCell 3 |  | TRS.1.2 TDD |  |  |
| OCNG Patterns |  |  | OCNG pattern OP.1 |  |  |
| SMTC Configuration |  |  | SMTC pattern SMTC.1 |  |  |
| SSB Configuration | ConfigSCell 1,2 |  | SSB.1 FR1 |  |  |
|  | ConfigSCell 3 |  | SSB.2 FR1 |  |  |
| PDSCH/PDCCH subcarrier spacing | ConfigSCell 1,2 | kHz | 15 kHz |  |  |
|  | ConfigSCell 3 |  | 30 kHz |  |  |
| PUCCH/PUSCH subcarrier spacing | ConfigSCell 1,2 | kHz | 15 kHz |  |  |
|  | ConfigSCell 3 |  | 30 kHz |  |  |
| PRACH configuration |  |  | FR1 PRACH configuration 1 |  |  |
| BWP configuraiton | Initial DL BWP |  | DLBWP.0.1 |  |  |
|  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |
|  | Initial UL BWP |  | ULBWP.0.1 |  |  |
|  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15kHz | -98 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | ConfigSCell 1,2 | dBm/SCS | -98 |  |  |
|  | ConfigSCell 3 |  | -95 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 8 | 8 | 8 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 8 | 8 | 8 |
| SSB_RP | ConfigSCell 1,2 | dBm/SCS | -90 | -90 | -90 |
|  | ConfigSCell 3 | dBm/SCS | -87 | -87 | -87 |
| IoNote3 | ConfigSCell 1,2 | dBm/9.36 MHz | -61.41 | -61.41 | -61.41 |
|  | ConfigSCell 3 | dBm/38.16 MHz | -55.31 | -55.31 | -55.31 |
| Propagation condition | ConfigSCell 1,2 | - | AWGN+220 Hz |  |  |
|  | ConfigSCell 3 | - | AWGN+500 Hz |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |

##### A.19.4.7.5.2 Test Requirements

The UE shall be capable to transmit valid CSI report for the directly activated SCell 1 no later than in subframe n+Ndirect.

The rate of correct observed SCell 1 direct activation delay during repeated tests shall be at least 90 %.

NOTE: The SCell activation delay, Ndirect, can be expressed as: Ndirect = TRRC_process + Tinterrupt + T2 + T3 + Tactivation_time + TCSI_Reporting - 3 ms, where:

TRRC_Process: RRC procedure delay defined in clause 12 of TS 38.331 [2],

Tinterrupt: Interruption time during handover as specified in clause 6.1E.1,

T2: Delay from slot $ n+\frac {TRRC\_Process+Tinterrupt}{NR slot length}$ until UE has obtained a valid TA command for the target PCell,

T3: Delay for applying the received TA for uplink transmission in the target PCell, and greater than or equal to k+1 slot, where k is defined in clause 4.2 in TS 38.213,

Tactivation_time and TCSI_Reporting are specified in clause 8.3D.2, where the following definitions of TFirstSSB and TFirstSSB_MAX as defined in section 8.3D.5 shall apply:

- TFirstSSB: the time to the end of the first complete SSB burst indicated by the SMTC after slot n + (𝑇𝑅𝑅𝐶_𝑃𝑟𝑜𝑐𝑒𝑠𝑠+𝑇𝑖𝑛𝑡𝑒𝑟𝑟𝑢𝑝𝑡+𝑇2+𝑇3)/(N𝑅 𝑠𝑙𝑜𝑡 𝑙𝑒𝑛𝑔𝑡ℎ)

- TFirstSSB_MAX: the time to the end of the first complete SSB burst indicated by the SMTC after slot n + (𝑇𝑅𝑅𝐶𝑃𝑟𝑜𝑐𝑒𝑠𝑠+𝑇𝑖𝑛𝑡𝑒𝑟𝑟𝑢𝑝𝑡+𝑇2+𝑇3)/(N𝑅 𝑠𝑙𝑜𝑡 𝑙𝑒𝑛𝑔𝑡ℎ)

This gives a total of Ndirect = 10 + 52 + TIU + T2 + T3 + Tactivation_time + TCSI_Reporting - 3 ms = 62 + 10 + 13 + 6 + 20 + 2 - 3 = 94 ms for test configurations 1 and 2.

This gives a total of Ndirect = 10 + 52 + TIU + T2 + T3 + Tactivation_time + TCSI_Reporting - 3 ms = 62 + 10 + 13 + 6 + 20 + 2 - 3 = 94 ms for test configuration 3.

During T3 the UE shall send valid CSI reports for PCell and SCell 1 with non-zero CQI index and continue to send CSI reports for PCell and SCell 1 (Cell 2) with non-zero CQI index until the end of T3.

All of the above test requirements shall be fulfilled in order for the observed SCell 1 direct activation delay to be counted as correct.

#### A.19.4.7.6 Fast SCell Activation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle

##### A.19.4.7.6.1 Test Purpose and Environment

The purpose of this test is to verify that the fast SCell activation and deactivation times are within the requirements stated in clause 8.3D.7, when the SCell in FR1 is known by the UE at the time of activation.

The supported test configurations are shown in table A.19.4.7.6.1-1 below. The test parameters refer to Table A.6.5.3.10.1-2 and A.6.5.3.10.1-3 except those described in the Table A.19.4.7.6.1-2. The test consists of two successive time periods, with duration of T1and T2, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell and triggering the aperiodic CSI-RS for fast SCell activation.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n (where n mode 20=1), defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot $ n+\frac {T_{HARQ}+T_{activation\_time}+T_{CSI\_Reporting}}{NR slot length}$, as defined in clause 8.3D. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$ and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot $ n+1+\frac {T_{HARQ}}{NR slot length}$ to $ n+1+\frac {T_{HARQ}+3 ms+T_{X}}{NR slot length}+N_{interruption}$, as defined in clause 8.3D, where $ N_{interruption}$ is the interruption length given in clause 8.2D.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.7.6.1-1: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, ≥10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, ≥10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, ≥40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurationsNOTE 2: The UE is only required to be tested in one with smallest aggregated channel bandwidth from supported band combinations which is composed of CCs ≥ the bandwidth (BWchannel) defined in each test configuration, |  |

Table A.19.4.7.6.1-2: Cell specific test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

| Parameter |  | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Propagation condition | Config 1,2 | - | AWGN+220Hz |  |  |  |
|  | Config 3 |  | AWGN+500Hz |  |  |  |

##### A.19.4.7.6.2 Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement and reporting after slot ($ n+1+\frac {T_{HARQ}+3 ms}{NR slot length}$). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption. During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot $ n+\frac {T_{HARQ}+T_{activtion\_time}+T_{CSI\_Reporting}}{NR slot length}$, Tactivation_time = TFirstATRS + 5 ms, as defined in clause 8.3D.7.

During T2 interruption of PCell / PSCell during SCell activation shall not happen outside the slot $ n+1+\frac {T_{HARQ}}{NR slot length}$ to $ n+1+\frac {T_{HARQ}+3 ms+T_{X}}{NR slot length}+N_{interruption}$, as defined in clause 8.3D.7.

The interruption on any activated serving cell shall not be more than the values specified in clause 8.2D.1.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

NOTE: During T2 if there are no uplink resources for reporting the valid CSI in a slot $\frac {T_{HARQ}+T_{activtion\_time}+T_{CSI\_Reporting}}{NR slot length}$ as defined in clause 8.3D then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.

#### A.19.4.7.7 Fast SCell Activation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle

##### A.19.4.7.7.1 Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.19.4.7.6.1. The supported test configurations are the same as defined in clause A.19.4.7.6.1. The test parameters refer to Table A.6.5.3.10.1-2 and A.6.5.3.10.1-3 except those described in the Table A.19.4.7.7.1-1 and A.19.4.7.7.1-2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system

Table A.19.4.7.7.1-1: General test parameters for known FR1 SCell activation case, 640 ms SCell measurement cycle

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| SCell measurement cycle (measCycleSCell) | ms | 640 |  |

Table A.19.4.7.7.1-2: Cell specific test parameters for known FR1 SCell activation case, 640 ms SCell measurement cycle

| Parameter |  | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| gapBetweenBursts |  | slots | 2 |  |  |  |
| Propagation condition | Config 1,2 | - | AWGN+220Hz |  |  |  |
|  | Config 3 |  | AWGN+500Hz |  |  |  |

##### A.19.4.7.7.2 Test Requirements

The test requirements defined in clause A.19.4.7.6.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstATRS + Tgap + TATRS + 5 ms.

#### A.19.4.7.8 SCell Activation of unknown SCell with valid L3 measurement results in FR1 in non-DRX for 160 ms SCell measurement cycle

##### A.19.4.7.8.1 Test Purpose and Environment

The purpose of this test is to verify that the SCell activation time are within the requirements stated in clause 8.3D.8, when the target SCell in FR1 is unknown to the UE at the time of activation, but UE has valid L3 measurement results of the SCell.

The supported test configurations for NR PCell are shown in table A.19.4.7.8.1-1 below. Supported test configurations for NR SCell are shown in table A.19.4.7.8.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently. The test parameters are given in Tables A.19.4.7.8.1-2 and cell-specific parameters in tables A.19.4.7.8.1-3 and A.19.4.7.8.1-4 below. The test consists of three successive time periods, with duration of T1, T2 and T3 respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC.

The test consists of three sub tests. The slot at which the MAC message is received at the UE antenna connector, is denoted slot #n. TE continuously schedules the downlink data to UE on PCell. In Sub-test 1, TE shall schedule DCI format 0_1 at slot n + $\frac {T_{HARQ}+7ms}{NR slot length}$. In Sub-test 2, TE shall schedule DCI format 0_1 at slot n + $\frac {T_{HARQ}+3ms+M-k2}{NR slot length}$, where M is defined in clause 8.3D.8 and k2 = 1. In Sub-test 3, UE shall tranmsit scheduling request on the first SR resource by 7ms+ THARQ + TSR_Periodicity to obtain the UL grant for L3 report transmission.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE then starts monitoring the SCC. T1 is sufficiently long so that UE is able to complete the L3 detection and measurements on the SCell to be activated. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. UE is expected to report L3 measurement result at the first PUSCH scheduled by TE.

The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot $ n+\frac {T_{HARQ}+T_{activation\_time}+T_{CSI\_Reporting}}{NR slot length}$, as defined in clause 8.3D.8. TE also indicates the TCI, based on L3 report of the UE. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after the slot that UE sends the L3 reports and shall report CQI index 0 (out-of-range) until the SCell activation has been completed.

During T2, any PCell interruption due to activation of SCell shall occur in the slot $ n+1+\frac {T_{HARQ}}{NR slot length}$ to $ n+1+\frac {T_{HARQ}+3 ms+T_{X}}{NR slot length}+N_{interruption}$, as defined in clause 8.3D.8, where $ N_{interruption}$ is the interruption length given in clause 8.2D.

At the beginning of T3, the SCell de-activation command is sent. T3 shall be sufficiently long to ensure UE completes the SCell de-activation.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation of SCell.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.19.4.7.8.1-1: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR PCell

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurationsNOTE 2: The UE is only required to be tested in one with smallest aggregated channel bandwidth from supported band combinations which is composed of CCs ≥ the bandwidth (BWchannel) defined in each test configuration, |  |

Table A.19.4.7.8.1-1A: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR SCell

| ConfigSCell | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurationsNOTE 2: The UE is only required to be tested in one with smallest aggregated channel bandwidth from supported band combinations which is composed of CCs ≥ the bandwidth (BWchannel) defined in each test configuration, |  |

Table A.19.4.7.8.1-2: General test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| RF Channel Number |  | 1,2 | Two NR radio channel (1, 2) are used for this test |
| Active PCell |  | Cell 1 | Primary cell on NR RF channel number 1. |
| Configured deactivated SCell |  | Cell 2 | Configured deactivated secondary cell on NR RF channel number 2 |
| CP length |  | Normal |  |
| DRX |  | OFF | Continuous monitoring of primary cell |
| Cell-individual offset for cells on NR channel number | dB | 0 | Individual offset for cells on primary component carrier. |
| SCell measurement cycle (measCycleSCell) | ms | 160 |  |
| Cell 2 timing offset to cell1 | s | 0 |  |
| Time alignment error between cell2 and cell1 | s | Time alignment error as specified in TS 38.104 [13] clause 6.5.3.1. | The value of time alignment error depends upon the type of carrier aggregation. |
| T1 | s | 7 | During this time the PCell shall be known and the SCell configured and detected. |
| T2 | ms | < 200 ms | During this time the UE shall activate the SCell. |
| T3 | ms | 200 ms |  |
| A2-threshold | dBm | -130 |  |
| ReportCofing |  | reportConfigId = 0: A2-event-triggeredreportConfig = 1: reportOnScellActivation-r18 |  |
| THARQ | ms | Config 1: 2Config 2: 3Config 3: 2.5 | k1 $\times  $ NR slot lengthk1 is a number of slots and is indicated by the PDSCH-to-HARQ-timing-indicator field in the DCI format, if present, or provided by dl-DataToUL-ACK, the value of k should be the minimum value defined in TS 38.213 [3] that will meet the timing constraints of this test case. |
| TCSI_Reporting | ms | 15 | the delay (in ms) including uncertainty in acquiring the first available downlink CSI reference resource, UE processing time for CSI reporting (clause 5.2.2.5 in TS 38.214 [26]) and uncertainty in acquiring the first available CSI reporting resources as specified in TS 38.331 [2] |
| Tuncertainty_RRC | ms | 0 | The CSI reporting for SCell being activated is provided during SCell addition. |

Table A.19.4.7.8.1-3: Cell specific test parameters for NR PCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

| Parameter |  | Unit | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1-T3 | T4 |
| Duplex mode | Config 1 |  | FDD |  |
|  | Config 2,3 |  | TDD |  |
| TDD configuration | Config 1 |  | Not applicable |  |
|  | Config 2 |  | TDDConf.1.1 |  |
|  | Config 3 |  | TDDConf.2.1 |  |
| BWchannel | Config 1,2 | MHz | 10: NPRB,c = 52 |  |
|  | Config 3 |  | 40: NPRB,c = 106 |  |
| BWoccupied | Config 1,2 | RB | 52 Note 5 |  |
|  | Config 3 |  | 106 Note 6 |  |
| Initial BWP configuration |  |  | DLBWP.0.1 |  |
| TCI state |  |  | TCI.State.0 |  |
| TRS Configuration | Config 1 |  | TRS.1.1 FDD |  |
|  | Config 2 |  | TRS.1.1 TDD |  |
|  | Config 3 |  | TRS.1.2 TDD |  |
| PDSCH Reference measurement channel | Config 1 |  | SR.1.1 FDD |  |
|  | Config 2 |  | SR.1.1 TDD |  |
|  | Config 3 |  | SR.2.1 TDD |  |
| Dedicated CORESET parameters | Config 1 |  | CCR.1.1 FDD |  |
|  | Config 2 |  | CCR.1.1 TDD |  |
|  | Config 3 |  | CCR.2.1 TDD |  |
| RMSI CORESET parameters | Config 1 |  | CR.1.1 FDD |  |
|  | Config 2 |  | CR.1.1 TDD |  |
|  | Config 3 |  | CR.2.1 TDD |  |
| OCNG Patterns | Config 1,2 |  | OP.1Note 5 |  |
|  | Config 3, |  | OP.1 Note 6 |  |
| SSB Configuration | Config 1,2 |  | SSB.1 FR1 |  |
|  | Config 3 |  | SSB.2 FR1 |  |
| CSI-RS configuration for CSI reporting (Note 5) | Config 1 |  | CSI-RS.1.1 FDD |  |
|  | Config 2 |  | CSI-RS.1.1 TDD |  |
|  | Config 3 |  | CSI-RS.2.1 TDD |  |
| SMTC configuration |  |  | SMTC.1 |  |
| reportConfigType |  |  | periodic |  |
| reportQuantity |  |  | cri-RI-PMI-CQI |  |
| CSI reporting periodicity | Config 1,2 | slot | 5 |  |
|  | Config 3 |  | 10 |  |
| CSI reporting offset | Config 1,2 | slot | 3 |  |
|  | Config 3 |  | 5 |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS Note 1 |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 | dBm/SCS | -104 |  |
|  | Config 3 |  | -101 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 17 |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 17 |  |
| SS-RSRPNote3 | Config 1,2 | dBm/SCS | -87 |  |
|  | Config 3 |  | -84 |  |
| SCH_RP Note 3 |  | dBm/15 kHz | -87 |  |
| Io Note3 | Config 1,2 | dBm/9.36 MHz | -58.96 |  |
|  | Config 3 | dBm/38.16 MHz | -52.87 |  |
| Propagation condition | Config 1,2 |  | AWGN+220 Hz |  |
|  | Config 3 |  | AWGN+500 Hz |  |
| Correlation Matrix and Antenna Configuration |  | - | 2x2 Low |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled within BWoccupied.NOTE 3: SS-RSRP and SCH_RP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T2.NOTE 5:  On top of the reference configurations, CSI-RS offset should be set to meet the CSI reference resource timing definition in Clause 5.2.2.5 in TS 38.214 [26]. |  |  |  |  |

Table A.19.4.7.8.1-4: Cell specific test parameters for NR SCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

| Parameter |  | Unit | Cell 2 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1-T3 | T4 |
| Duplex mode | ConfigSCell 1 |  | FDD |  |
|  | ConfigSCell 2,3 |  | TDD |  |
| TDD configuration | ConfigSCell 1 |  | Not applicable |  |
|  | ConfigSCell 2 |  | TDDConf.1.1 |  |
|  | ConfigSCell 3 |  | TDDConf.2.1 |  |
| BWchannel | ConfigSCell 1,2 | MHz | 10: NPRB,c = 52 |  |
|  | ConfigSCell 3 |  | 40: NPRB,c = 106 |  |
| BWoccupied | ConfigSCell 1,2 | RB | 52 |  |
|  | ConfigSCell 3 |  | 106 |  |
| Initial BWP configuration |  |  | DLBWP.0.1 |  |
| TCI state |  |  | TCI.State.0 |  |
| TRS Configuration | ConfigSCell 1 |  | TRS.1.1 FDD |  |
|  | ConfigSCell 2 |  | TRS.1.1 TDD |  |
|  | ConfigSCell 3 |  | TRS.1.2 TDD |  |
| PDSCH Reference measurement channel | ConfigSCell 1 |  | N/A |  |
|  | ConfigSCell 2 |  | N/A |  |
|  | ConfigSCell 3 |  | N/A |  |
| Dedicated CORESET parameters | ConfigSCell 1 |  | N/A |  |
|  | ConfigSCell 2 |  | N/A |  |
|  | ConfigSCell 3 |  | N/A |  |
| RMSI CORESET parameters | ConfigSCell 1 |  | N/A |  |
|  | ConfigSCell 2 |  | N/A |  |
|  | ConfigSCell 3 |  | N/A |  |
| OCNG Patterns | ConfigSCell 1,2 |  | OP.1 |  |
|  | ConfigSCell 3, |  | OP.1 |  |
| SSB Configuration | ConfigSCell 1,2 |  | SSB.3 FR1 |  |
|  | ConfigSCell 3 |  | SSB.4 FR1 |  |
| CSI-RS configuration for CSI reporting Note 5 | ConfigSCell 1 |  | CSI-RS.1.1 FDD |  |
|  | ConfigSCell 2 |  | CSI-RS.1.1 TDD |  |
|  | ConfigSCell 3 |  | CSI-RS.2.1 TDD |  |
| SMTC configuration |  |  | SMTC.1 |  |
| reportConfigType |  |  | N/A |  |
| reportQuantity |  |  | N/A |  |
| CSI reporting periodicity | ConfigSCell 1,2 | slot | N/A |  |
|  | ConfigSCell 3 |  | N/A |  |
| CSI reporting offset | ConfigSCell 1,2 | slot | N/A |  |
|  | ConfigSCell 3 |  | N/A |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS Note 1 |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | ConfigSCell 1,2 | dBm/SCS | -104 |  |
|  | ConfigSCell 3 |  | -101 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 17 |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 17 |  |
| SS-RSRPNote3 | ConfigSCell 1,2 | dBm/SCS | -87 |  |
|  | ConfigSCell 3 |  | -84 |  |
| SCH_RP Note 3 |  | dBm/15 kHz | -87 |  |
| Io Note3 | ConfigSCell 1,2 | dBm/9.36 MHz | -58.96 |  |
|  | ConfigSCell 3 | dBm/38.16 MHz | -52.87 |  |
| Propagation condition | ConfigSCell 1,2 | - | AWGN +220 Hz |  |
|  | ConfigSCell 3 |  | AWGN +500 Hz |  |
| Correlation Matrix and Antenna Configuration |  |  | 2x2 Low |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled within BWoccupied.NOTE 3: SS-RSRP and SCH_RP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T2.NOTE 5:  On top of the reference configurations, CSI-RS offset should be set to meet the CSI reference resource timing definition in Clause 5.2.2.5 in TS 38.214 [26]. |  |  |  |  |

Table A.19.4.7.8.1-5: Scheduling request parameters

| Parameter |  | Value |
| --- | --- | --- |
| schedulingRequestId |  | 0 |
| sr-ProhibitTimer |  | 16ms |
| sr-TransMax |  | n4 |
| periodicityAndOffset |  | Sl2 |
| PUCCH resource ID |  | 0 |
| PUCCH resource | Starting PRB | To be determined by RAN5 |
|  | intraSlotFrequencyHopping | disabled |
|  | Format | format 2 |
|  | nrofPRBs | 2 |
|  | nrofSymbols | 1 |
|  | startingSymbolIndex | 0 |

##### A.19.4.7.8.2 Test Requirements

During T2, the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement and reporting after slot ($ n+1+\frac {T_{HARQ}+3 ms}{NR slot length}$). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption. During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot $ n+\frac {T_{HARQ}+T_{activtion\_time}+T_{CSI\_Reporting}}{NR slot length}$.

For Sub-test 1, Tactivation_time = 7 ms + k2/SCS + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3D.8, where k2/SCS is 1 ms for config 1,2 and 0.5 ms for config 3.

For Sub-test 2, Tactivation_time = 3 ms + M + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3D.8.

For Sub-test 3, Tactivation_time = 7ms + Tuncertainity_ULgrant + max (THARQ + Tuncertainty_MAC + 5ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3D.8. Where, Tuncertainity_ULgrant is uncertainty in acquiring UL grant after sending scheduling request.

During T2, interruption of PCell during SCell activation shall not happen outside the slot $ n+1+\frac {T_{HARQ}}{NR slot length}$ to $ n+1+\frac {T_{HARQ}+3 ms+T_{X}}{NR slot length}+N_{interruption}$, as defined in clause 8.3D.8.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and L3 measurement reporting to be counted as correct. The rate of correct observed SCell activation delay and L3 measurement reporting during repeated tests shall be at least 90 %.

NOTE: During T2, if there are no uplink resources for reporting the valid CSI in a slot $\frac {T_{HARQ}+T_{activtion\_time}+T_{CSI\_Reporting}}{NR slot length}$ as defined in clause 8.3D then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.

#### A.19.4.7.9 TRS based SCell Activation of SSB-less SCell in FR1 inter-band CA in non-DRX for ATG

##### A.19.4.7.9.1 Test Purpose and Environment

The purpose of this test is to verify that the SSB-less SCell activation delay is within the requirements stated in clause 8.3D.2, when the to be activated SCell in FR1 is provided with periodic CSI-RS for tracking instead of SSB. SCell does not provide neither SSB configuration (absoluteFrequencySSB) nor SMTC configuration.

The supported test configurations are shown in table A.19.4.7.9.1-1A and A.19.4.7.9.1-1B below. The test parameters for PCell and SCell refer to Table A.6.5.3.15.1-2, A.6.6.1.1.1.2-3 and A.6.6.1.1.1.2-4 except those described in the table A.19.4.7.9.1-2. The test consists of two successive time periods, with duration of T1 and T2, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1(PCell), but is not aware of Cell 2(SCell). Cell 1 and Cell 2 are in different bands. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. At the same time, UE also receives the indication of reference serving cell in the same RRC message. The Cell 1 is indicated as the reference cell of Cell 2. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n (where n mod 20=1), defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot $ n+\frac {T_{HARQ}+T_{activation\_time}+T_{CSI\_Reporting}}{NR slot length}$, as defined in clause 8.3D. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$ and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot $ n+1+\frac {T_{HARQ}}{NR slot length}$ to $ n+1+\frac {T_{HARQ}+3 ms+T_{X}}{NR slot length}+N_{interruption}$, as defined in clause 8.3D, where $ N_{interruption}$ is the interruption length given in clause 8.2D.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

This test case is only applicable to ATG UE capable of one common Rx beam between PCC band and SCC band.

Table A.19.4.7.9.1-1A: FR1 inter-band SSB-less SCell activation based on TRS for NR PCell in non-DRX for 160 ms SCell measurement cycle supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, ≥10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, ≥10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, ≥40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurationsNOTE 2: The UE is only required to be tested in one with smallest aggregated channel bandwidth from supported band combinations which is composed of CCs ≥ the bandwidth (BWchannel) defined in each test configuration,NOTE 3:  Test configuration for NR PCell and test configuration for NR SCell shall be chosen independently. |  |

Table A.19.4.7.9.1-1B: FR1 inter-band SSB-less SCell activation based on TRS for NR SCell in non-DRX for 160 ms SCell measurement cycle supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SCS, ≥10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SCS, ≥10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SCS, ≥40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurationsNOTE 2: The UE is only required to be tested in one with smallest aggregated channel bandwidth from supported band combinations which is composed of CCs ≥ the bandwidth (BWchannel) defined in each test configuration.NOTE 3:  Test configuration for NR PCell and test configuration for NR SCell shall be chosen independently. |  |

Table A.19.4.7.9.1-2: PCell and SCell test configuration parameters for TRS based SCell activation of SSB-less SCell in FR1 inter-band CA in non-DRX for 160 ms measurement cycle

| Parameter |  | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Propagation Condition | Config 1, 2 |  | AWGN+220 Hz |  |  |  |
|  | Config 3 |  | AWGN+500 Hz |  |  |  |

##### A.19.4.7.9.2 Test Requirements

During T2 the ATG UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement and reporting after slot ($ n+1+\frac {T_{HARQ}+3 ms}{NR slot length}$). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption. During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot $ n+\frac {T_{HARQ}+T_{activtion\_time}+T_{CSI\_Reporting}}{NR slot length}$, Tactivation_time  is

- Tfirst_TRS + TTRS + 5 ms, if aperiodic CSI-RS resources are not configured for SCell activation or UE do not support aperiodicCSI-RS-FastScellActivation-r17, when the the EPRE difference (ΔEPRE) is 12 dB

- Tfirst_TRS + 2*TTRS +5 ms, when the EPRE difference (ΔEPRE) is 30 dB

During T2 interruption of PCell / PSCell during SCell activation shall not happen outside the slot $ n+1+\frac {T_{HARQ}}{NR slot length}$ to $ n+1+\frac {T_{HARQ}+3 ms+T_{X}}{NR slot length}+N_{interruption}$, as defined in clause 8.3D.2.

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2D.1.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

NOTE: During T2 if there are no uplink resources for reporting the valid CSI in a slot $\frac {T_{HARQ}+T_{activtion\_time}+T_{CSI\_Reporting}}{NR slot length}$ as defined in clause 8.3D then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.

## A.19.5 Measurement procedure

### A.19.5.1 Intra-frequency Measurements

#### A.19.5.1.1 SA event triggered reporting tests without gap without SSB index reading under non-DRX

##### A.19.5.1.1.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2D.5.1 and 9.2D.5.2.

##### A.19.5.1.1.2 Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test configurations are given in the Table A.19.5.1.1.2-1, the test parameters for PCell and neighbour cell refer to Table A.6.6.1.1.1.2-2 and A.6.6.1.1.1.2-3 except those described in the table A.19.5.1.1.2-2. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.5.1.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.19.5.1.1.2-2: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Propagation Condition |  | 1, 2 | AWGN+220 Hz |  |  |  |
|  |  | 3 | AWGN+500 Hz |  |  |  |

##### A.19.5.1.1.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.19.5.1.2 SA event triggered reporting tests with per-UE gaps under non-DRX

##### A.19.5.1.2.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2D.6.2 and 9.2D.6.3.

##### A.19.5.1.2.2 Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test configuration refer to Table A.6.6.1.3.2-1, the test parameters refer to Table A.6.6.1.3.2-2 and A.6.6.1.3.2-3, except those described in the table A.19.5.1.2.2-1. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.5.1.2.2-1: NR Cell specific test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Propagation Condition |  | 1, 2 | AWGN+220 Hz |  |  |  |
|  |  | 3 | AWGN+500 Hz |  |  |  |

##### A.19.5.1.2.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.19.5.1.3 SA event triggered reporting tests without gap under non-DRX with SSB index reading

##### A.19.5.1.3.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2D.5.1 and 9.2D.5.2.

##### A.19.5.1.3.2 Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test configuration refer to Table A.6.6.1.5.2-1, the test parameters for FDD PCell and neighbour cell refer to Table A.6.6.1.5.2-2 and A.6.6.1.5.2-3 except those described in the table A.19.5.1.3.2-1. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.5.1.3.2-1: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Propagation Condition |  | 1 | AWGN+220 Hz |  |  |  |

##### A.19.5.1.3.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.19.5.1.4 SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading

##### A.19.5.1.4.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the  intra-frequency cell search requirements in clause 9.2D.6.2 and 9.2D.6.3.

##### A.19.5.1.4.2 Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test configuration refer to Table A.6.6.1.6.2-1, the test parameters refer to Table A.6.6.1.6.2-2 and A.6.6.1.6.2-3 except those described in the table A.19.5.1.4.2-1. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.5.1.4.2-1: NR Cell specific test parameters for SA intra-frequency event triggered reporting with gap for FDD PCell in FR1 with SSB index reading

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Propagation Condition |  | 1 | AWGN+[220 Hz] |  |  |  |

##### A.19.5.1.4.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.19.5.1.5 Event triggered reporting tests on SCC with deactivated SCell under non-DRX with measurement cycle of 640ms

##### A.19.5.1.5.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event when measuring the CC with deactivated SCell. This test will partly verify the intra-frequency cell search requirements in clause 9.2D.5.1 and 9.2D.5.2, and verify that the UE missed ACK/NACK rate does not exceed the limits at NR PCell interruptions during the measurement on the deactivated NR SCC as specified in 8.2D.1.2.3.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system. The specific gNB reference location is emulated by test system.

##### A.19.5.1.5.2 Test parameters

Supported test configurations for NR PCell are shown in table A.19.5.1.5.2-1. Supported test configurations for NR SCell are shown in table A.19.5.1.5.2-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently.

Three cells are deployed in the test, which are FR1 PCell (Cell 1), a FR1 deactivated SCell (Cell 2) and a FR1 neighbour cell (Cell 3) on the same frequency as the SCell (Cell 2). The test parameters are given in table A.19.5.1.5.2-2 and A.19.5.1.5.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A6 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell 2 and the RRC message including measCycleSCell or allowInterruptions for the deactivated NR SCells is received at the UE antenna connector. During time duration T1, PCell is continuously scheduled in DL, the UE shall not have any timing information of Cell 3.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment.

Table A.19.5.1.5.2-1: Supported PCell test configurations

| Configuration | Description |
| --- | --- |
| 1 | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations.NOTE 2: The UE is only required to be tested in one of the supported test configurations with the smallest aggregated channel bandwidth from supported band combinations which is composed of CCs ≥ the bandwidth (BWchannel) defined in each test configuration. |  |

Table A.19.5.1.5.2-1A: Supported SCell test configurations

| ConfigurationSCell | Description |
| --- | --- |
| 1A | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2A | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3A | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations.NOTE 2: The UE is only required to be tested in one of the supported test configurations with smallest aggregated channel bandwidth from supported band combinations which is composed of CCs ≥ the bandwidth (BWchannel) defined in each test configuration.NOTE 3: NR Cell 3 has the same SCS, BW and duplex mode as NR Cell 2. |  |

Table A.19.5.1.5.2-2: General test parameters for intra-frequency event triggered reporting without gap for SCC with deactivated SCell in FR1 with non-DRX

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Active cell |  | 1, 2, 3 | Cell 1 |  |
| Deactivated SCell |  | 1A, 2A, 3A | Cell 2 |  |
| Neighbour cell |  | 1A, 2A, 3A | Cell 3 | Cell to be identified. |
| RF Channel Number |  | 1, 2, 3 | 1: Cell 1 2: Cell 2 and 3 |  |
| SSB configuration |  | 1 | SSB.1 FR1 |  |
|  |  | 2 | SSB.1 FR1 |  |
|  |  | 3 | SSB.2 FR1 |  |
| SMTC configuration |  | 1 | SMTC.2 |  |
|  |  | 2 | SMTC.1 |  |
|  |  | 3 | SMTC.1 |  |
| A6-Offset | dB | 1, 2, 3 | -4.5 |  |
| CP length |  | 1, 2, 3 | Normal |  |
| Hysteresis | dB | 1, 2, 3 | 0 |  |
| Time To Trigger | s | 1, 2, 3 | 0 |  |
| Filter coefficient |  | 1, 2, 3 | 0 | L3 filtering is not used |
| DRX |  | 1, 2, 3 | OFF |  |
| Measurement gap pattern Id |  | 1, 2, 3 | OFF |  |
| measCycleSCell |  | 1, 2, 3 | 640 ms |  |
| Time offset between serving and neighbour cells |  | 1 | 3 ms | Asynchronous cells.The timing of Cell 3 is 3 ms later than the timing of Cell 2. |
|  |  | 2 | 3 s | Synchronous cells |
|  |  | 3 | 3 s | Synchronous cells |
| T1 | s | 1, 2, 3 | 10 |  |
| T2 | s | 1, 2, 3 | 10 |  |

Table A.19.5.1.5.2-3: Cell specific test parameters for intra-frequency event triggered reporting without gap for SCC with deactivated SCell in FR1 with non-DRX

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |
| TDD configuration |  | 1,1A | N/A |  | N/A |  | N/A |  |
|  |  | 2,2A | TDDConf.1.1 |  | TDDConf.1.1 |  | TDDConf.1.1 |  |
|  |  | 3,3A | TDDConf.2.1 |  | TDDConf.2.1 |  | TDDConf.2.1 |  |
| PDSCH RMC configuration |  | 1,1A | SR.1.1 FDD |  | N/A |  | N/A |  |
|  |  | 2,2A | SR.1.1 TDD |  |  |  |  |  |
|  |  | 3,3A | SR.2.1 TDD |  |  |  |  |  |
| RMSI CORESET RMC configuration |  | 1,1A | CR.1.1 FDD |  | N/A |  | N/A |  |
|  |  | 2,2A | CR.1.1 TDD |  | N/A |  | N/A |  |
|  |  | 3,3A | CR.2.1 TDD |  | N/A |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1,1A | CCR.1.1 FDD |  | N/A |  | N/A |  |
|  |  | 2,2A | CCR.1.1 TDD |  | N/A |  | N/A |  |
|  |  | 3,3A | CCR.2.1 TDD |  | N/A |  | N/A |  |
| OCNG Patterns |  | 1, 2, 3,1A,2A,3A | OP.1 |  | OP.1 |  | OP.1 |  |
| TRS configuration |  | 1,1A | TRS.1.1 FDD |  | N/A |  | N/A |  |
|  |  | 2,2A | TRS.1.1 TDD |  | N/A |  | N/A |  |
|  |  | 3,3A | TRS.1.2 TDD |  | N/A |  | N/A |  |
| Initial BWP configuration |  | 1, 2, 3,1A,2A,3A | DLBWP.0.1 ULBWP.0.1 |  | DLBWP.0.1 ULN/A |  | DLBWP.0.1 ULN/A |  |
| Active DL BWP configuration |  | 1, 2, 3,1A,2A,3A | DLBWP.1.1 |  | DLBWP.1.1 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1, 2, 3,1A,2A,3A | ULBWP.1.1 |  | N/A |  | N/A |  |
| RLM-RS |  | 1, 2, 3,1A,2A,3A | SSB |  | SSB |  | SSB |  |
| Note 2 | dBm/SCS | 1,1A | -98 |  |  |  |  |  |
|  |  | 2,2A | -98 |  |  |  |  |  |
|  |  | 3,3A | -95 |  |  |  |  |  |
| Note 2 | dBm/15 kHz | 1,1A | -98 |  |  |  |  |  |
|  |  | 2,2A |  |  |  |  |  |  |
|  |  | 3,3A |  |  |  |  |  |  |
|  | dB | 1,1A | 4 | 4 | 4 | -1.46 | -Infinity | -1.46 |
|  |  | 2,2A |  |  |  |  |  |  |
|  |  | 3,3A |  |  |  |  |  |  |
|  | dB | 1,1A | 4 | 4 | 4 | 4 | -Infinity | 4 |
|  |  | 2,2A |  |  |  |  |  |  |
|  |  | 3,3A |  |  |  |  |  |  |
| SSB_RP Note 3 | dBm/SCS kHz | 1,1A | -94 | -94 | -94 | -94 | -Infinity | -94 |
|  |  | 2,2A | -94 | -94 | -94 | -94 | -Infinity | -94 |
|  |  | 3,3A | -91 | -91 | -91 | -91 | -Infinity | -91 |
| Io | dBm/9.36 MHz | 1,1A | -64.60 | -64.60 | -64.60 | -62.25 | -64.60 | -62.25 |
|  | dBm/9.36 MHz | 2,2A | -64.60 | -64.60 | -64.60 | -62.25 | -64.60 | -62.25 |
|  | dBm/38.16 MHz | 3,3A | -58.50 | -58.50 | -58.50 | -56.16 | -58.50 | -56.16 |
| Propagation Condition |  | 1,2,1A,2A | AWGN + 220Hz |  |  |  |  |  |
|  |  | 3,3A | AWGN +500Hz |  |  |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

##### A.19.5.1.5.3 Test Requirements

The UE shall send one Event A6 triggered measurement report, with a measurement reporting delay less than 6400 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The UE shall be continuously scheduled on PCell during the entire length of T1. During the time duration T1, the UE shall transmit at least 99.5 % of ACK/NACK on PCell.

If the NR PCell is not in the same band as the deactivated SCell, the UE is only allowed to cause interruptions on NR PCell immediately before and immediately after an SMTC. Each interruption on NR PCell shall not exceed the value defined in table A.19.5.1.5.3-1.

If the NR PCell is contiguous to the deactivated SCell in the same band, the UE is only allowed to cause an interruption on PCell no earlier than 1 slot before an SMTC and no later than 1 slot after the SMTC. The interruption on NR PCell shall not exceed the value defined in table A.19.5.1.5.3-2.

Table A.19.5.1.5.3-1: Interruption duration if the PCell is not in the same band as the deactivated SCell

|  | NR Slot length (ms) | Interruption length (slots) |
| --- | --- | --- |
| 0 | 1 | 1 |
| 1 | 0.5 | 1 |

Table  A.19.5.1.5.3-2: Interruption duration if the PCell is in the same band as the deactivated SCell

|  | NR Slot length (ms) | Interruption length (slots) |
| --- | --- | --- |
| 0 | 1 | 2 + SMTC duration |
| 1 | 0.5 | 2 + SMTC duration |

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

### A.19.5.2 Inter-frequency Measurements

A.19.5.2.1 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used

A.19.5.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3D.4.

##### A.19.5.2.1.2 Test parameters

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test configuration refer to Table A.6.6.1.3.2-1. The general test parameters are given in table A.19.5.2.1.2-1. The cell specific test parameters refer to A.6.6.2.2.1-3, except those described in the table A.19.5.2.1.2-2.The DRX configuration is given in table A.19.5.2.1.2-3. The TimeAlignmentTimer configuration refers to Table A.6.6.2.2.1-5.

Measurement gap pattern configuration defined in table A.19.5.2.1.2-1 is per-UE gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE needs to be provided  with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.5.2.1.2-1: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| NR RF Channel Number |  | Config 1,2,3 | 1, 2 |  | Two FR1 NR carrier frequencies is used. |
| Active cell |  | Config 1,2,3 | NR Cell 1 (Pcell) |  | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2,3 | NR cell2 |  | NR Cell 2 is on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1,2,3 | 0 |  | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2,3 | 9 |  |  |
| A3-Offset | dB | Config 1,2,3 | -6 |  |  |
| Hysteresis | dB | Config 1,2,3 | 0 |  |  |
| CP length |  | Config 1,2,3 | Normal |  |  |
| TimeToTrigger | s | Config 1,2,3 | 0 |  |  |
| Filter coefficient |  | Config 1,2,3 | 0 |  | L3 filtering is not used |
| DRX |  | Config 1,2,3 | DRX.1 | DRX. 7 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | Config 1 | 3 ms |  | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
|  |  | Config 2,3 | 3s |  | Synchronous cells. |
| T1 | s | Config 1,2,3 | 5 |  |  |
| T2 | s | Config 1,2,3 | 1.1 | 11 |  |

Table A.19.5.2.1.2-2: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Propagation Condition |  | 1, 2 | AWGN+220 Hz |  |  |  |
|  |  | 3 | AWGN+500 Hz |  |  |  |

Table A.19.5.2.1.2-3: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

| Field | Test1 | Test2 | Comment |
| --- | --- | --- | --- |
|  | Value | Value |  |
| drx-onDurationTimer | ms1 | ms1 | As specified in clause 6.3.2 in TS 38.331 [2] |
| drx-InactivityTimer | ms1 | ms1 |  |
| drx-RetransmissionTimerDL | sl1 | sl1 |  |
| drx-RetransmissionTimerUL | sl1 | sl1 |  |
| drx-LongCycleStartOffset | ms40 | Ms640 |  |
| shortDRX | disable | disable |  |

##### A.19.5.2.1.3 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1080 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.


In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 10240 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

A.19.5.2.2 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used

A.19.5.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3D.4 and 9.3D.5.

##### A.19.5.2.2.2 Test parameters

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test configurations refer to Tables A.6.6.2.5.1-1. The test parameters refer to Table A.6.6.2.5.1-2 and A.6.6.2.5.1-3 except those described in table A.19.5.2.2.2-1.

Measurement gap pattern configuration defined in table A.6.6.2.5.1-2 is per-UE gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.5.2.2.2-1: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Propagation Condition |  | 1, 2 | AWGN+220 Hz |  |  |  |
|  |  | 3 | AWGN+500 Hz |  |  |  |

A.19.5.2.2.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1040 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

A.19.5.2.3 SA event triggered reporting tests for FR1 without gap when DRX is not used

A.19.5.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3D.9.

##### A.19.5.2.3.2 Test parameters

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The SSB of Cell 2 is completely within UE’s active BWP BW. The RBs containing SSB from Cell 1 and Cell 2 should be different in frequency location within the cell bandwidth. The test configuration refer to Table A.6.6.2.11.1-1. The test parameters refer to Tables A.6.6.2.11.1-2 and A.6.6.2.11.1-3 except those described in table A.19.5.2.3.2-1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.5.2.3.2-1: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without gap

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Propagation Condition |  | 1, 2 | AWGN+220 Hz |  |  |  |
|  |  | 3 | AWGN+500 Hz |  |  |  |

##### A.19.5.2.3.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

### A.19.5.3 L1-RSRP measurement for beam reporting for ATG

#### A.19.5.3.1 SSB based L1-RSRP measurement when DRX is not used

##### A.19.5.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5D.4.1, with the testing configurations for NR ATG cells in table A.19.5.3.1.1-1.

Table A.19.5.3.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test for ATG

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

##### A.19.5.3.1.2 Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). The test parameters from Table A.6.6.4.1.2-1 and table A.6.6.4.1.2-2 are used except those described in table A.19.5.3.1.2-1.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.19.5.3.1.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| Propagation condition | 1,2 |  | AWGN+220 Hz |
|  | 3 |  | AWGN+500 Hz |

##### A.19.5.3.1.3 Test Requirements

The test requirements of this test case are the same as those defined in clause A.6.6.4.1.3.

#### A.19.5.3.2 CSI-RS based L1-RSRP measurement when DRX is not used

##### A.19.5.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5D.4.2, with the testing configurations for NR ATG cells in table A.19.5.3.2.1-1.

Table A.19.5.3.2.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test for ATG

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz CSI-RS SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz CSI-RS SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz CSI-RS SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

##### A.19.5.3.2.2 Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). The test parameters from Table A.6.6.4.3.2-1 and table A.6.6.4.3.2-2 are used except those described in table A.19.5.3.2.2-1.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (0 for Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.6.6.4.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.19.5.3.2.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| Propagation condition | 1,2 |  | AWGN+220 Hz |
|  | 3 |  | AWGN+500 Hz |

##### A.19.5.3.2.3 Test Requirements

The test requirements of this test case are the same as those defined in clause A.6.6.4.3.3.

### A.19.5.4 L1-SINR measurement for beam reporting for ATG

#### A.19.5.4.1 L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured when DRX is not used

A.19.5.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements in clause 9.8D.4.1, with the testing configurations for NR ATG cells in table A.19.5.4.1.1-1.

Table A.19.5.4.1.1-1: Applicable NR configurations for FR1 CSI-RS based L1-SINR test for ATG

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz CSI-RS SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz CSI-RS SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz CSI-RS SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

A.19.5.4.1.2 Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). The test parameters from Table A.6.6.8.1.2-1 and table A.6.6.8.1.2-2 are used except those described in table A.19.5.4.1.2-1.

In the CSI-RS measurement configuration, UE is indicated to perform L1-SINR measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-SINR on aperiodic CSI-RS resources. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (1 Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.6.6.8.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.19.5.4.1.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| DRX configuration | 1~3 |  | Off |
| Propagation condition | 1,2 |  | AWGN+220 Hz |
|  | 3 |  | AWGN+500 Hz |

##### A.19.5.4.1.3 Test Requirements

The test requirements of this test case are the same as those defined in clause A.6.6.8.1.3.

#### A.19.5.4.2 L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used

##### A.19.5.4.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements in clause 9.8D.4.2, with the testing configurations for NR ATG cells in table A.19.5.4.2.1-1.

Table A.19.5.4.2.1-1: Applicable NR configurations for FR1 L1-SINR measurement test with SSB based CMR and CSI-RS based IMR for ATG

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

##### A.19.5.4.2.2 Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). The test parameters from Table A.6.6.8.2.2-1, table A.6.6.8.2.2-2, and table A.6.6.8.2.2-3 are used except those described in table A.19.5.4.2.2-1.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the SSBs and the associated CSI-RS resources, and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD measurements based on the SSBs, and UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-RS resources as IMR.

Table A.19.5.4.2.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| Propagation condition | 1,2 |  | AWGN+220 Hz |
|  | 3 |  | AWGN+500 Hz |

##### A.19.5.4.2.3 Test Requirements

The test requirements of this test case are the same as those defined in clause A.6.6.8.2.3.

#### A.19.5.4.3 L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used

##### A.19.5.4.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements with CSI-RS based CMR and dedicated IMR configured in clause 9.8D.4.3, with the testing configurations for NR ATG cells in table A.19.5.4.3.1-1.

Table A.19.5.4.3.1-1: Applicable NR configurations for FR1 L1-SINR test with CMR and dedicated IMR for ATG

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz CSI-RS SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz CSI-RS SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz CSI-RS SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

##### A.19.5.4.3.2 Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). The test parameters from Table A.6.6.8.3.2-1 and table A.6.6.8.3.2-2 are used except those described in table A.19.5.4.3.2-1.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the configured CSI-RS as CMR and an associated CSI-IM as IMR, and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-SINR on aperiodic CSI-RS resources. UE is also configured to measure L1-SINR based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (1 Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.6.6.8.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs, and UE is configured to perform L1-SINR measurement based on the CSI-RS as CMR and the CSI-IM as IMR.

Table A.19.5.4.3.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| Propagation condition | 1,2 |  | AWGN+220 Hz |
|  | 3 |  | AWGN+500 Hz |

##### A.19.5.4.3.3 Test Requirements

The test requirements of this test case are the same as those defined in clause A.6.6.8.3.3

### A.19.5.5 NR measurements with autonomous gaps for ATG

#### A.19.5.5.1 SA intra-frequency CGI identification of NR neighbor cell in FR1

##### A.19.5.5.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of intra-frequency CGI identification of an NR neighbour ATG cell in FR1 with autonomous gaps. This test shall partly verify the measurement requirements in clause 9.11D, with the testing configurations for NR ATG cells in table A.19.5.5.1.1-1

Table A.19.5.5.1.1-1: Supported test configurations for ATG

| Configuration | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

##### A.19.5.5.1.2 Test Parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the FR1 PCell and Cell 2 is an FR1 neighbour cell on the same frequency as the PCell. The test parameters from Table A.6.6.7.1.2-2 and table A.6.6.7.1.2-3 are used except those described in A.19.5.5.1.2-1.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable.  A measurement object is configured for the frequency of the PCell and it is indicated to the UE that event-triggered reporting with Event A3 is used. The UE is expected to detect and send a measurement report with Event A3.

A new RRC message triggering CGI identification shall be sent to the UE during period T2, after the UE has reported Event A3. The RRC message shall create a measurement report configuration with purpose reportCGI and useAutonomousGaps set to TRUE. The start of T3 is the instant when the last TTI containing the RRC message implying CGI identification is sent to the UE.

The test equipment verifies that potential interruption is carried out correctly by monitoring ACK/NACK sent in PCell during T3 until a measurement report with CGI is sent.

Table A.19.5.5.1.2-1: NR Cell specific test parameters for SA intra-frequency CGI identification of NR neighbor cell in FR1

| Parameter | Unit | Test | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | configuration | T1 | T2 | T3 | T1 | T2 | T3 |
| Propagation Condition |  | 1,2 | AWGN+220 Hz |  |  |  |  |  |
|  |  | 3 | AWGN+500 Hz |  |  |  |  |  |

##### A.19.5.5.1.3 Test Requirements

The test requirements of this test case are the same as those defined in clause A.6.6.7.1.3

## A.19.6 Measurement Performance requirements

Unless explicitly stated otherwise:

- Reported measurements shall be within defined range of accuracy limits defined in clause 10 for at least 90 % of the reported cases. If multiple measurement performance requirements are verified in the same test, the reported measurements for each requirement shall be within defined range of accuracy limits of the corresponding requirement defined in clause10 for at least 90 % of the reported cases.

- Measurements are performed in RRC_CONNECTED state.

- The reference channels assume transmission of PDSCH with a maximum number of 5 HARQ transmissions unless otherwise specified.

### A.19.6.1 SS-RSRP for ATG UE

#### A.19.6.1.1 SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

##### A.19.6.1.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.2.1.1 and 10.1.2.1.2 for intra-frequency measurements.

##### A.19.6.1.1.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.19.6.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in table A.6.7.1.1.2-2, except those described in the Table A.19.6.1.1.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.1.1.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations in each supported band |  |

Table A.19.6.1.1.2-2: SS-RSRP Intra frequency test parameters

| Parameter | Test configuration | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Propagation Condition | Config 1,2 | - | AWGN+220 Hz |  | AWGN+220 Hz |  | AWGN+220 Hz |  |
|  | Config 3 | - | AWGN+500 Hz |  | AWGN+500 Hz |  | AWGN+500 Hz |  |

##### A.19.6.1.1.3 Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.2.1.1 and relative requirement in clause 10.1.2.1.2.

#### A.19.6.1.2 SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

##### A.19.6.1.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.4.1.1 and 10.1.4.1.2 for inter-frequency measurements with the testing configurations for NR cells in table A.19.6.1.2.1-1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.1.2.1-1: Applicable NR configurations for FR1 inter-frequency SS-RSRP accuracy test

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations in each supported band |  |

##### A.19.6.1.2.2 Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.19.6.1.2.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.6.7.1.2.2-1, except those described in the Table A.19.6.1.2.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.19.6.1.2.2-1: SS-RSRP inter-frequency test parameters

| Parameter | Test configuration | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Propagation Condition | Config 1,2 | - | AWGN+220 Hz |  | AWGN+220 Hz |  |
|  | Config 3 | - | AWGN+500 Hz |  | AWGN+500 Hz |  |

##### A.19.6.1.2.3 Test Requirements

The SS-RSRP measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.4.1.1 and relative requirement in clause 10.1.4.1.2.

### A.19.6.2 SS-RSRQ for ATG UE

#### A.19.6.2.1 SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

##### A.19.6.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.7.1.1.

##### A.19.6.2.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.19.6.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.6.7.2.1.2-2, except those described in the given in table A.19.6.2.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.19.6.2.1.2-2: SS-RSRQ Intra frequency test parameters

| Parameter | Test configuration | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Propagation Condition | Config 1,2 | - | AWGN+220 Hz |  | AWGN+220 Hz |  | AWGN+220 Hz |  |
|  | Config 3 | - | AWGN+500 Hz |  | AWGN+500 Hz |  | AWGN+500 Hz |  |

##### A.19.6.2.1.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.7.1.1.

#### A.19.6.2.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

##### A.19.6.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.9.1.1 and 10.1.9.1.2.

##### A.19.6.2.2.2 Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.19.6.2.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.6.7.2.2.2-2 except those described in the Table A.19.6.2.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.2.2.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.19.6.2.2.2-2: SS-RSRQ Inter frequency test parameters

| Parameter | Test configuration | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Propagation Condition | Config 1,2 | - | AWGN+220 Hz |  | AWGN+220 Hz |  | AWGN+220 Hz |  |
|  | Config 3 | - | AWGN+500 Hz |  | AWGN+500 Hz |  | AWGN+500 Hz |  |

##### A.19.6.2.2.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.9.1.1 and 10.1.9.1.2.



### A.19.6.3 SS-SINR for ATG UE

#### A.19.6.3.1 SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

##### A.19.6.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.12.1.1.

##### A.19.6.3.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.19.6.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.6.7.3.1.2-2, except those described in the Table A.19.6.3.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.19.6.3.1.2-2: SS-SINR Intra frequency test parameters

| Parameter | Test configuration | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Propagation Condition | Config 1,2 | - | AWGN+220 Hz |  | AWGN+220 Hz |  |
|  | Config 3 | - | AWGN+500 Hz |  | AWGN+500 Hz |  |

##### A.19.6.3.1.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.12.1.1.

#### A.19.6.3.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

##### A.19.6.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.14.1.1 and 10.1.14.1.2.

##### A.19.6.3.2.2 Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.19.6.3.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.6.7.3.2.2-2, except those described in the Table A.19.6.3.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.3.2.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.19.6.3.2.2-2: SS-SINR Inter frequency test parameters

| Parameter | Test configuration | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Propagation Condition | Config 1,2 | - | AWGN+220 Hz |  | AWGN+220 Hz |  | AWGN+220 Hz |  |
|  | Config 3 | - | AWGN+500 Hz |  | AWGN+500 Hz |  | AWGN+500 Hz |  |

##### A.19.6.3.2.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.14.1.1 and 10.1.14.1.2.

### A.19.6.4 L1-RSRP measurement for beam reporting for ATG UE

#### A.19.6.4.1 SSB based L1-RSRP measurement

##### A.19.6.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.5D.2 and clause 10.1.19.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.19.6.4.1.1-1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations in each supported band |  |

##### A.19.6.4.1.2 Test parameters

In this set of test cases there one cell in the test, PCell (Cell 1).. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.6.7.4.1.2-1, except those described in the Table A.19.6.4.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.19.6.4.1.2-1: FR1 SSB based L1-RSRP test parameters

| Parameter | Test configuration | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- | --- |
| Propagation Condition | Config 1,2 | - | AWGN+220 Hz | AWGN+220 Hz |
|  | Config 3 | - | AWGN+500 Hz | AWGN+500 Hz |

##### A.19.6.4.1.3 Test Requirements

The L1-RSRP measurement accuracy for SSB resource reported by UE in L1-RSRP report (SSB#0 or SSB#1) of Cell 2 shall fulfil the requirements in clauses 10.1.19.1.

#### A.19.6.4.2 CSI-RS based L1-RSRP measurement on resource set with repetition off

##### A.19.6.4.2.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.5D.3 and clause 10.1.19.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.19.6.4.2.1-1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.4.2.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz CSI-RS SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz CSI-RS SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz CSI-RS SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations in each supported band |  |

##### A.19.6.4.2.2 Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1). The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.6.7.4.2.2-2 is used except those described in the Table A.19.6.4.2.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.19.6.4.2.2-1: FR1 CSI-RS based L1-RSRP test parameters

| Parameter | Test configuration | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- | --- |
| Propagation Condition | Config 1,2 | - | AWGN+220 Hz | AWGN+220 Hz |
|  | Config 3 | - | AWGN+500 Hz | AWGN+500 Hz |

##### A.19.6.4.2.3 Test Requirements

The L1-RSRP measurement accuracy for CSI-RS resource reported by UE in L1-RSRP report (CSI-RS#0 or CSI-RS#1) of Cell 1 shall fulfil the requirements in clause 10.1.19.2.

### A.19.6.5 L1-SINR measurement for beam reporting based CMR for ATG UE

#### A.19.6.5.1 L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured and CSI-RS resource set with repetition off

##### A.19.6.5.1.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.8D.4.1 and clause 10.1.27.1 for L1-SINR measurements based on CSI-RS with the testing configurations for NR cells in table A.19.6.5.1.1-1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.5.1.1-1: Applicable NR configurations for FR1 L1-SINR test with CSI-RS based CMR and no dedicated IMR configured

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz CSI-RS SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz CSI-RS SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz CSI-RS SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations in each supported band |  |

##### A.19.6.5.1.2 Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1).The absolute and relative accuracy of L1-SINR measurements are tested by using the parameters in table A.6.7.9.1.2-1 except those described in table A.19.6.5.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.19.6.5.1.2-1: FR1 CSI-RS based L1-SINR test parameters

| Parameter | Config | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- | --- |
| Propagation condition | 1, 2 |  | AWGN+220 Hz | AWGN+220 Hz |
|  | 3 |  | AWGN+500 Hz | AWGN+500 Hz |

##### A.19.6.5.1.3 Test Requirements

The L1-SINR measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirements in clause 10.1.27.1.

#### A.19.6.5.2 L1-SINR measurement with SSB based CMR and dedicated IMR

##### A.19.6.5.2.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.8D.4.2 and clause 10.1.27.2 for L1-SINR measurements with SSB based CMR and dedicated CSI-RS based IMR, with the testing configurations for NR cells in table A.19.6.5.2.1-1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.5.2.1-1: Applicable NR configurations for FR1 L1-SINR measurement test with SSB based CMR and CSI-RS based IMR

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations in each supported band |  |

##### A.19.6.5.2.2 Test parameters

In this set of test cases there one cell in the test, PCell (Cell 1). The absolute accuracy of L1-SINR measurements are tested by using the parameters in table A.6.7.9.2.2-1 except those described in the Table A.19.6.5.2.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources and one CSI-RS resource set with two CSI-RS resource. UE is configured to perform RLM and BFD measurement based on the SSB resources 0 and 1. UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-RS resources as IMR.

Table A.19.6.5.2.2-1: FR1 SSB based L1-SINR test parameters

| Parameter | Config | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- | --- |
| Propagation condition | 1, 2 |  | AWGN+220 Hz | AWGN+220 Hz |
|  | 3 |  | AWGN+500 Hz | AWGN+500 Hz |

##### A.19.6.5.2.3 Test Requirements

The L1-SINR measurement accuracy for SSB#0+CSI-RS#0 and SSB#1+CSI-RS#1 of Cell 1 shall fulfil the requirements in clauses 10.1.27.2.

#### A.19.6.5.3 L1-SINR measurement with CSI-RS based CMR and dedicated IMR

##### A.19.6.5.3.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will partly verify the requirements in clauses 9.8D.4.3 and clause 10.1.27.3 for L1-SINR measurements based on CSI-RS as CMR and CSI-IM as IMR with the testing configurations for NR cells in table A.19.6.5.3.1-1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.5.3.1-1: Applicable NR configurations for FR1 L1-SINR measurement test with CSI-RS based CMR and CSI-IM based IMR

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz CSI-RS SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz CSI-RS SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz CSI-RS SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations in each supported band |  |

##### A.19.6.5.3.2 Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1). The absolute and relative accuracy of L1-SINR measurements are tested by using the parameters in table A.6.7.9.3.2-1 except those described in table A.19.6.5.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources and one CSI-IM resource set with two CSI-IM resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB. UE is configured to perform L1-SINR measurement based on the configured CSI-RS as CMR and CSI-IM as IMR.

Table A.19.6.5.3.2-1: FR1 L1-SINR measurement test with CSI-RS based CMR and CSI-IM based IMR

| Parameter | Config | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- | --- |
| Propagation condition | 1, 2 |  | AWGN+220 Hz | AWGN+220 Hz |
|  | 3 |  | AWGN+500 Hz | AWGN+500 Hz |

##### A.19.6.5.3.3 Test Requirements

The L1-SINR measurement accuracy for CSI-RS#0+CSI-IM#0 and CSI-RS#1+CSI-IM# of Cell 1 shall fulfil the requirements in clause 10.1.27.3.

### A.19.6.6 CSI-RSRP for ATG UE

#### A.19.6.6.1 SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

##### A.19.6.6.1.1 Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.2.3.1 and 10.1.2.3.2 for CSI-RS intra-frequency measurements.

##### A.19.6.6.1.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.19.6.6.1.2-1. Both absolute and relative accuracy of CSI-RSRP intra-frequency measurements are tested by using the parameters in table A.6.7.10.1.2-2, except those described in the Table A.19.6.6.1.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.6.1.2-1: CSI-RSRP intra frequency supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB and CSI-RS SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB and CSI-RS SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB and CSI-RS SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations in each supported band |  |

Table A.19.6.6.1.2-2: CSI-RSRP intra frequency test parameters

| Parameter | Test configuration | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Propagation Condition | Config 1,2 | - | AWGN+220 Hz |  | AWGN+220 Hz |  | AWGN+220 Hz |  |
|  | Config 3 | - | AWGN+500 Hz |  | AWGN+500 Hz |  | AWGN+500 Hz |  |

##### A.19.6.6.1.3 Test Requirements

The CSI-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.2.3.1 and relative requirement in clause 10.1.2.3.2.

#### A.19.6.6.2 SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

##### A.19.6.6.2.1 Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.4.3.1 and 10.1.4.3.2 for CSI-RS inter-frequency measurements with the testing configurations for NR cells in table A.19.6.6.2.1-1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.6.2.1-1: Applicable NR configurations for FR1 inter-frequency CSI-RSRP accuracy test

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB and CSI-RS SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB and CSI-RS SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB and CSI-RS SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations in each supported band |  |

##### A.19.6.6.2.2 Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency than the PCell. Both absolute and relative accuracy of CSI-RSRP inter-frequency measurements are tested by using the parameters in table A.6.7.10.2.2-1, except those described in the Table A.19.6.6.2.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.19.6.6.2.2-1: CSI-RSRP inter-frequency test parameters

| Parameter | Test configuration | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Propagation Condition | Config 1,2 | - | AWGN+220 Hz |  | AWGN+220 Hz |  |
|  | Config 3 | - | AWGN+500 Hz |  | AWGN+500 Hz |  |

##### A.19.6.6.2.3 Test Requirements

The CSI-RSRP measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.4.3.1 and relative requirement in clause 10.1.4.3.2.

### A.19.6.7 CSI-RSRQ for ATG UE

#### A.19.6.7.1 SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

##### A.19.6.7.1.1 Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.7.2.

##### A.19.6.7.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.19.6.7.1.2-1. The absolute accuracy of CSI-RSRQ intra-frequency measurement is tested by using the parameters in table A.6.7.11.1.2-2, except those described in the Table A.19.6.7.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.7.1.2-1: Intra frequency CSI-RSRQ supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB and CSI-RS SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB and CSI-RS SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB and CSI-RS SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.19.6.7.1.2-2: CSI-RSRQ Intra frequency test parameters

| Parameter | Test configuration | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Propagation Condition | Config 1,2 | - | AWGN+220 Hz |  | AWGN+220 Hz |  | AWGN+220 Hz |  |
|  | Config 3 | - | AWGN+500 Hz |  | AWGN+500 Hz |  | AWGN+500 Hz |  |

##### A.19.6.7.1.3 Test Requirements

The CSI-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.7.2.

#### A.19.6.7.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

##### A.19.6.7.2.1 Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.9.2.1 and 10.1.9.2.2.

##### A.19.6.7.2.2 Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.19.6.7.2.2-1. Both absolute accuracy and relative accuracy requirements of CSI-RSRQ inter-frequency measurement are tested by using test parameters in table A.6.7.11.2.2-2, except those described in the Table A.19.6.7.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.7.2.2-1: CSI-RSRQ Inter frequency CSI-RSRQ supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz CSI-RS SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz CSI-RS SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz CSI-RS SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.19.6.7.2.2-2: CSI-RSRQ Inter frequency test parameters

| Parameter | Test configuration | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Propagation Condition | Config 1,2 | - | AWGN+220 Hz |  | AWGN+220 Hz |  | AWGN+220 Hz |  |
|  | Config 3 | - | AWGN+500 Hz |  | AWGN+500 Hz |  | AWGN+500 Hz |  |

##### A.19.6.7.2.3 Test Requirements

The CSI-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.9.2.1 and 10.1.9.2.2.

### A.19.6.8 CSI-SINR for ATG UE

#### A.19.6.8.1 SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

##### A.19.6.8.1.1 Test Purpose and Environment

The purpose of this test is to verify that the CSI-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.12.2.1.

##### A.19.6.8.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.19.6.8.1.2-1. The absolute accuracy of CSI-SINR intra-frequency measurement is tested by using the parameters in table A.6.7.12.1.2-2, except those described in the Table A.19.6.8.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.8.1.2-1: CSI-SINR Intra frequency CSI-SINR supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB and CSI-RS SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB and CSI-RS SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB and CSI-RS SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.19.6.8.1.2-2: CSI-SINR Intra frequency test parameters

| Parameter | Test configuration | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Propagation Condition | Config 1,2 | - | AWGN+220 Hz |  | AWGN+220 Hz |  |
|  | Config 3 | - | AWGN+500 Hz |  | AWGN+500 Hz |  |

##### A.19.6.8.1.3 Test Requirements

The CSI-SINR measurement accuracy shall fulfil the requirements in clause 10.1.12.2.1.

#### A.19.6.8.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

##### A.19.6.8.2.1 Test Purpose and Environment

The purpose of this test is to verify that the CSI-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.14.2.1 and 10.1.14.2.2.

##### A.19.6.8.2.2 Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.19.6.8.2.2-1. Both absolute accuracy and relative accuracy requirements of CSI-SINR inter-frequency measurement are tested by using test parameters in table A.6.7.12.2.2-2, except those described in the Table A.19.6.8.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.8.2.2-1: CSI-SINR Inter frequency CSI-SINR supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR 15 kHz SSB and CSI-RS SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR 15 kHz SSB and CSI-RS SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR 30 kHz SSB and CSI-RS SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.19.6.8.2.2-2: CSI-SINR Inter frequency test parameters

| Parameter | Test configuration | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Propagation Condition | Config 1,2 | - | AWGN+220 Hz |  | AWGN+220 Hz |  | AWGN+220 Hz |  |
|  | Config 3 | - | AWGN+500 Hz |  | AWGN+500 Hz |  | AWGN+500 Hz |  |

##### A.19.6.8.2.3 Test Requirements

The CSI-SINR measurement accuracy shall fulfil the requirements in clause 10.1.14.2.1 and 10.1.14.2.2.

# A.20 NR standalone tests for RedCap UE with Satellite Access

## A.20.1 RRC_IDLE state mobility

### A.20.1.1 Cell reselection to FR1 intra-frequency NR case for 1Rx RedCap UE

#### A.20.1.1.1 Test Purpose and Environment

Test purpose and environment in clause A.14.1.1.1 shall apply for 1Rx RedCap UE.

#### A.20.1.1.2 Test Parameters

Test parameters in clause A.14.1.1.2 shall apply except that:

- Table A.14.1.1.2-1 is replaced with A.20.1.1.2-1, and

- NR cell specific test parameters in Table A.20.1.1.2-2 replace the corresponding parameters in Table A.14.1.1.2-3, and

- Table A.14.1.1.2-2 and Table A.14.1.1.2-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.1.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.1.1.2-2: Cell specific test parameters for intra frequency NR cell re-selection test case

| Parameter | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | SSC.1 for Config 1,3SSC.2 for Config 2,4 |  |  | NSC.1 for Config 1,3NSC.2 for Config 2,4 |  |  |

#### A.20.1.1.3 Test Requirements

Test requirements in clause A.14.1.1.3 shall apply for 1Rx RedCap UEs.

### A.20.1.2 Cell reselection to FR1 intra-frequency NR case  for 2Rx RedCap UE

#### A.20.1.2.1 Test Purpose and Environment

Test purpose and environment in clause A.14.1.1.1 shall apply for 2Rx RedCap UE.

#### A.20.1.2.2 Test Parameters

Test parameters in clause A.14.1.1.2 shall apply except that:

- Table A.14.1.1.2-1 is replaced with A.20.1.1.2-1, and

- NR cell specific test parameters in Table A.20.1.1.2-2 replace the corresponding parameters in Table A.14.1.1.2-3, and

- Table A.14.1.2.2-2 and Table A.14.1.2.2-3 shall apply to configurations 1, 2, 3 and 4.

#### A.20.1.2.3 Test Requirements

Test requirements in clause A.14.1.1.3 shall apply for 2Rx RedCap UEs.

### A.20.1.3 Cell reselection to FR1 intra-frequency NR cell for 1Rx RedCap UE configured with the feature for enhanced requirements

#### A.20.1.3.1 Test Purpose and Environment

Test purpose and environment in clause A.14.1.2.1 shall apply for 1Rx RedCap UE.

#### A.20.1.3.2 Test Parameters

Test parameters in clause A.14.1.2.2 shall apply except that:

- Table A.14.1.2.2-1 is replaced with A.20.1.1.2-1, and

- NR cell specific test parameters in Table A.20.1.3.2-1 replace the corresponding parameters in Table A.14.1.2.2-3, and

- Table A.14.1.2.2-2 and Table A.14.1.2.2-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.1.3.2-1: Cell specific test parameters for intra frequency NR cell re-selection test case

| Parameter | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | SSC.1 for Config 1,3SSC.2 for Config 2,4 |  |  | NSC.1 for Config 1,3NSC.2 for Config 2,4 |  |  |

#### A.20.1.3.3 Test Requirements

Test requirements in clause A.14.1.2.3 shall apply for 1Rx RedCap UEs.

### A.20.1.4 Cell reselection to FR1 intra-frequency NR cell for 2Rx RedCap UE configured with the feature for enhanced requirements

#### A.20.1.4.1 Test Purpose and Environment

Test purpose and environment in clause A.14.1.2.1 shall apply for 2Rx RedCap UE.

#### A.20.1.4.2 Test Parameters

Test parameters in clause A.14.1.2.2 shallapply except that:

Table A.14.1.2.2-1 is replaced with A.20.1.1.2-1, and

NR cell specific test parameters in Table A.20.1.3.2-1 replace the corresponding parameters in Table A.14.1.2.2-3, and

- Table A.14.1.2.2-2 and Table A.14.1.2.2-3 shall apply to configurations 1, 2, 3 and 4.

#### A.20.1.4.3 Test Requirements

Test requirements in clause A.14.1.2.3 shall apply for 2Rx RedCap UEs.

### A.20.1.5 Time-based measurement initiation to FR1 intra-frequency NR cell reselection for 1Rx RedCap UE

#### A.20.1.5.1 Test Purpose and Environment

Test purpose and environment in clause A.14.1.3.1 shall apply for 1Rx RedCap UE.

#### A.20.1.5.2 Test Parameters

Test parameters in clause A.14.1.3.2 shall apply except that:

Table A.14.1.3.2-1 is replaced with A.20.1.1.2-1, and

NR cell specific test parameters in Table A.20.1.5.2-1 replace the corresponding parameters in Table A.14.1.2.2-3, and

Table A.14.1.3.2-2 and Table A.14.1.3.2-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.1.5.2-1: Cell specific test parameters for intra frequency NR cell re-selection test case

| Parameter | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | SSC.1 for Config 1,3SSC.2 for Config 2,4 |  | NSC.1 for Config 1,3NSC.2 for Config 2,4 |  |

#### A.20.1.5.3 Test Requirements

Test requirements in clause A.14.1.3.3 shall apply for 1Rx RedCap UEs.

### A.20.1.6 Time-based measurement initiation to FR1 intra-frequency NR cell reselection for 2Rx RedCap UE

#### A.20.1.6.1 Test Purpose and Environment

Test purpose and environment in clause A.14.1.3.1 shall apply for 2Rx RedCap UE.

#### A.20.1.6.2 Test Parameters

Test parameters in clause A.14.1.3.2 shall apply except that:

Table A.14.1.3.2-1 is replaced with A.20.1.1.2-1, and

NR cell specific test parameters in Table A.20.1.5.2-1 replace the corresponding parameters in Table A.14.1.3.2-3, and

- Table A.14.1.3.2-2 and Table A.14.1.3.2-3 shall apply to configurations 1, 2, 3 and 4.

#### A.20.1.6.3 Test Requirements

Test requirements in clause A.14.1.3.3 shall apply for 2Rx RedCap UEs.

### A.20.1.7 Location-based measurement initiation to FR1 inter-frequency NR cell reselection for 1Rx RedCap UE

#### A.20.1.7.1 Test Purpose and Environment

Test purpose and environment in clause A.14.1.8.1 shall apply for 1Rx RedCap UE.

#### A.20.1.7.2 Test Parameters

Test parameters in clause A.14.1.8.2 shall apply except that:

Table A.14.1.8.2-1 is replaced with A.20.1.1.2-1, and

NR cell specific test parameters in Table A.20.1.7.2-1 replace the corresponding parameters in Table A.14.1.3.2-3, and

Table A.14.1.8.2-2 and Table A.14.1.8.2-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.1.7.2-1: Cell specific test parameters for inter frequency NR cell re-selection test case

| Parameter | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | SSC.1 for Config 1,3SSC.2 for Config 2,4 |  | NSC.1 for Config 1,3NSC.2 for Config 2,4 |  |
| PDSCH RMC configuration |  | SR.1.1 FDD |  | SR.1.1 FDD |  |
| RMSI CORESET configuration |  | CR.1.1 FDD |  | CR.1.1 FDD |  |
| Dedicated CORESET configuration |  | CCR.1.1 FDD |  | CCR.1.1 FDD |  |
| OCNG Pattern |  | OP.1 defined in A.3.2.1 |  | OP.1 defined in A.3.2.1 |  |
| Initial DL BWP configuration |  | DLBWP.0.1 |  | DLBWP.0.1 |  |
| Initial UL BWP configuration |  | ULBWP.0.1 |  | ULBWP.0.1 |  |
| SSB configuration |  | SSB.1 FR1 |  | SSB.1 FR1 |  |
| SMTC configuration |  | #1: SMTC.2 for Cell 1#2: SMTC.6 for Cell 2 |  | #1: SMTC.2 for Cell 1#2: SMTC.6 for Cell 2 |  |
| RLM-RS |  | SSB |  | SSB |  |
| Qrxlevmin | dBm/SCS | -130 |  | -130 |  |
| Pcompensation | dB | 0 |  | 0 |  |
| Qhysts | dB | 0 |  | 0 |  |
| Qoffsets, n | dB | 0 |  | 0 |  |
| Cell_selection_and_reselection_quality_measurement |  | SS-RSRP |  | SS-RSRP |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 16 | 13 | -infinity | 16 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | -98 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | -98 |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 16 | 13 | -infinity | 16 |
| SS-RSRP Note3 | dBm/SCS | -82 | -85 | -infinity | -82 |
| Io | dBm/9.36 MHz | -53.94 | -56.84 | -70.05 | -53.94 |
| Treselection | s | 0 | 0 | 0 | 0 |
| SnonIntrasearchP | dB | 50 |  | 50 |  |
| Threshx, highP | dB | 48 |  | 48 |  |
| Threshserving, lowP | dB | 54 |  | 44 |  |
| Threshx, lowP | dB | 50 |  | 40 |  |
| Propagation Condition |  | AWGN |  |  |  |

#### A.20.1.7.3 Test Requirements

Test requirements in clause A.14.1.8.3 shall apply for 1Rx RedCap UEs.

### A.20.1.8 Location-based measurement initiation to FR1 inter-frequency NR cell reselection for 2Rx RedCap UE

#### A.20.1.8.1 Test Purpose and Environment

Test purpose and environment in clause A.14.1.8.1 shall apply for 2Rx RedCap UE.

#### A.20.1.8.2 Test Parameters

Test parameters in clause A.14.1.8.2 shall apply except that:

Table A.14.1.8.2-1 is replaced with A.20.1.1.2-1, and

NR cell specific test parameters in Table A.20.1.7.2-1 replace the corresponding parameters in Table A.14.1.3.2-3, and

- Table A.14.1.8.2-2 and Table A.14.1.8.2-3 shall apply to configurations 1, 2, 3 and 4.

#### A.20.1.8.3 Test Requirements

Test requirements in clause A.14.1.8.3 shall apply for 2Rx RedCap UEs.

### A.20.1.9 Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion for 1Rx RedCap UE

#### A.20.1.9.1 Test Purpose and Environment

Test purpose and environment in clause A.14.1.9.1 shall apply for 1Rx RedCap UE.

#### A.20.1.9.2 Test Parameters

Test parameters in clause A.14.1.9.2 shall apply except that:

Table A.14.1.9.2-1 is replaced with A.20.1.1.2-1, and

Table A.14.1.9.2-2 is replaced with A.20.1.9.2-1, and,

Table A.14.1.9.2-3 is replaced with A.20.1.9.2-2.


Table A.20.1.9.2-1: General test parameters for FR1 inter frequency NR cell re-selection test case for UE fulfilling low mobility criterion

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2,3,4 | Cell 2 | The UE camps on Cell 2 in the initial phase, it fulfills Low Mobility relaxation measurements criterion, and during T1 period the UE reselects to Cell 1 |
|  | Neighbour cells |  | 1, 2,3,4 | Cell 1 |  |
| T1 end condition | Active cell |  | 1, 2,3,4 | Cell 1 | The UE shall perform reselection to Cell 1 during T1 |
|  | Neighbour cells |  | 1, 2,3,4 | Cell 2 |  |
| T2 end condition | Active cell |  | 1, 2,3,4 | Cell 2 | The UE shall perform reselection to Cell 2 with higher priority during T2 |
|  | Neighbour cells |  | 1, 2,3,4 | Cell 1 |  |
| RF Channel Number |  |  | 1, 2,3,4 | 1, 2 |  |
| Time offset between cells |  |  | 1, 2,3,4 | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | 1, 2,3,4 | Not Sent | No additional delays in random access procedure. |
| SSB Configuration |  |  | 1, 2,3,4 | SSB.1 FR1 |  |
| SMTC configuration |  |  | 1, 2,3,4 | SMTC pattern 2 | Configured in SIB4 of Cell 1 |
|  |  |  |  | SMTC pattern 6 | Configured in SIB4 of Cell 2 |
| DRX cycle length |  | s | 1, 2,3,4 | 0.64 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2,3,4 | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2,3,4 | Not configured |  |
| T1 |  | s | 1, 2,3,4 | 25 s | T1 is defined so that cell re-selection reaction time is taken into account. |
| T2 |  | s | 1, 2,3,4 | 25 s | T2 is defined so that cell re-selection reaction time is taken into account. |

Table A.20.1.9.2-2: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case in AWGN for UE fulfilling low mobility criterion

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 |  | T2 |
| Satellite information |  | 1,3 | SSC.1 |  | NSC.1 |  |  |
|  |  | 2,4 | SSC.2 |  | NSC.2 |  |  |
| PDSCH RMC  configuration |  | 1, 2,3,4 | SR.1.1 FDD |  | SR.1.1 FDD |  |  |
| RMSI CORESET  RMC configuration |  | 1, 2,3,4 | CR.1.1 FDD |  | CR.1.1 FDD |  |  |
| Dedicated CORESET  RMC configuration |  | 1, 2,3,4 | CCR.1.1 FDD |  | CCR.1.1 FDD |  |  |
| OCNG Pattern |  | 1, 2,3,4 | OP.1 defined in A.3.2.1 |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1, 2,3,4 | DLBWP.0.1 |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2,3,4 | ULBWP.0.1 |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1, 2,3,4 | SSB |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1, 2,3,4 | -140 |  | -140 |  |  |
| Pcompensation | dB | 1, 2,3,4 | 0 |  | 0 |  |  |
| Qhysts | dB | 1, 2,3,4 | 0 |  | 0 |  |  |
| Qoffsets, n | dB | 1, 2,3,4 | 0 |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2,3,4 | SS-RSRP |  | SS-RSRP |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2,3,4 | 14 | 14 | -4 | 12 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1, 2,3,4 | -98 |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 2,3,4 | -98 |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2,3,4 | 14 | 14 | -4 |  | 12 |
| SS-RSRP Note3 | dBm/SCS | 1, 2,3,4 | -84 | -84 | -102 |  | -86 |
| Io | dBm/9.36 MHz | 1, 2,3,4 | -55.88 | -55.88 | -68.60 |  | -57.78 |
| Treselection | s | 1, 2,3,4 | 0 | 0 | 0 |  | 0 |
| SnonintersearchP | dB | 1, 2,3,4 | Not sent |  | Not sent |  |  |
| Threshx, highP | dB | 1, 2,3,4 | 48 |  | 48 |  |  |
| Threshserving, lowP | dB | 1, 2,3,4 | 44 |  | 44 |  |  |
| Threshx, lowP | dB | 1, 2,3,4 | 50 |  | 50 |  |  |
| SSearchDeltaP | dB | 1, 2,3,4 | 3 |  | 3 |  |  |
| TSearchDeltaP | s | 1, 2,3,4 | 5 |  | 5 |  |  |
| Propagation Condition |  | 1, 2,3,4 | AWGN |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |

#### A.20.1.9.3 Test Requirements

Test requirements in clause A.14.1.9.3 shall apply for 1Rx RedCap UEs.

### A.20.1.10 Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion for 2Rx RedCap UE

#### A.20.1.10.1 Test Purpose and Environment

Test purpose and environment in clause A.14.1.9.1 shall apply for 2Rx RedCap UE.

#### A.20.1.10.2 Test Parameters

Test parameters in clause A.14.1.9.2 shall apply except that:

Table A.14.1.9.2-1 is replaced with A.20.1.1.2-1, and

Table A.14.1.9.2-2 is replaced with A.20.1.9.2-1, and,

- Table A.14.1.9.2-3 is replaced with A.20.1.9.2-2.

#### A.20.1.10.3 Test Requirements

Test requirements in clause A.14.1.9.3 shall apply for 2Rx RedCap UEs.

### A.20.1.11 Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion for 1Rx RedCap UEs

#### A.20.1.11.1 Test Purpose and Environment

Test purpose and environment in clause A.14.1.10.1 shall apply for 1Rx RedCap UE.

#### A.20.1.11.2 Test Parameters

Test parameters in clause A.14.1.10.2 shall apply except that:

Table A.14.1.3.2-1 is replaced with A.20.1.1.2-1, and

Table A.14.1.10.2-2 is replaced with A.20.1.11.2-1, and,

Table A.14.1.10.2-3 is replaced with A.20.1.11.2-2.

Table A.20.1.11.2-1: General test parameters for FR1 inter frequency NR cell re-selection test case for UE fulfilling not-at-cell edge criterion

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2,3,4 | Cell 2 | The UE camps on Cell 2 in the initial phase, it fulfills Not-at-cell edge relaxation measurements criterion, and during T1 period the UE reselects to Cell 1 |
|  | Neighbour cells |  | 1, 2,3,4 | Cell 1 |  |
| T1 end condition | Active cell |  | 1, 2,3,4 | Cell 1 | The UE shall perform reselection to Cell 1 during T1 |
|  | Neighbour cells |  | 1, 2,3,4 | Cell 2 |  |
| T2 end condition | Active cell |  | 1, 2,3,4 | Cell 2 | The UE shall perform reselection to Cell 2 with higher priority during T2 |
|  | Neighbour cells |  | 1, 2,3,4 | Cell 1 |  |
| RF Channel Number |  |  | 1, 2,3,4 | 1, 2 |  |
| Time offset between cells |  |  | 1, 2,3,4 | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | 1, 2,3,4 | Not Sent | No additional delays in random access procedure. |
| SSB Configuration |  |  | 1, 2,3,4 | SSB.1 FR1 |  |
| SMTC configuration |  |  | 1, 2,3,4 | SMTC pattern 2 | Configured in SIB4 of Cell 1 |
|  |  |  |  | SMTC pattern 6 | Configured in SIB4 of Cell 2 |
| DRX cycle length |  | s | 1, 2,3,4 | 0.64 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2,3,4 | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2,3,4 | Not configured |  |
| T1 |  | s | 1, 2,3,4 | 20 s | T1 is defined so that cell re-selection reaction time is taken into account. |
| T2 |  | s | 1, 2,3,4 | 20 s | T2 is defined so that cell re-selection reaction time is taken into account. |

Table A.20.1.11.2-2: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case in AWGN for UE fulfilling not-at-cell edge criterion

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 |  | T2 |
| Satellite information |  | 1,3 | SSC.1 |  | NSC.1 |  |  |
|  |  | 2,4 | SSC.2 |  | NSC.2 |  |  |
| PDSCH RMC  configuration |  | 1, 2,3,4 | SR.1.1 FDD |  | SR.1.1 FDD |  |  |
| RMSI CORESET  RMC configuration |  | 1, 2,3,4 | CR.1.1 FDD |  | CR.1.1 FDD |  |  |
| Dedicated CORESET  RMC configuration |  | 1, 2,3,4 | CCR.1.1 FDD |  | CCR.1.1 FDD |  |  |
| OCNG Pattern |  | 1, 2,3,4 | OP.1 defined in A.3.2.1 |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1, 2,3,4 | DLBWP.0.1 |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2,3,4 | ULBWP.0.1 |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1, 2,3,4 | SSB |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1, 2,3,4 | -140 |  | -140 |  |  |
| Pcompensation | dB | 1, 2,3,4 | 0 |  | 0 |  |  |
| Qhysts | dB | 1, 2,3,4 | 0 |  | 0 |  |  |
| Qoffsets, n | dB | 1, 2,3,4 | 0 |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2,3,4 | SS-RSRP |  | SS-RSRP |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2,3,4 | 14 | 14 | -4 | 12 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1, 2,3,4 | -98 |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 2,3,4 | -98 |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2,3,4 | 14 | 14 | -4 |  | 12 |
| SS-RSRP Note3 | dBm/SCS | 1, 2,3,4 | -84 | -84 | -102 |  | -86 |
| Io | dBm/9.36 MHz | 1, 2,3,4 | -55.88 | -55.88 | -68.60 |  | -57.78 |
| Treselection | s | 1, 2,3,4 | 0 | 0 | 0 |  | 0 |
| SnonintersearchP | dB | 1, 2,3,4 | Not sent |  | Not sent |  |  |
| Threshx, highP | dB | 1, 2,3,4 | 48 |  | 48 |  |  |
| Threshserving, lowP | dB | 1, 2,3,4 | 44 |  | 44 |  |  |
| Threshx, lowP | dB | 1, 2,3,4 | 50 |  | 50 |  |  |
| SSearchThresholdP | dB | 1, 2,3,4 | 50 |  | 50 |  |  |
| SSearchThresholdQ | s | 1, 2,3,4 | Not Configured |  |  |  |  |
| Propagation Condition |  | 1, 2,3,4 | AWGN |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |

#### A.20.1.11.3 Test Requirements

Test requirements in clause A.14.1.10.3 shall apply for 1Rx RedCap UEs.

### A.20.1.12 Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion for 2Rx RedCap UEs

#### A.20.1.12.1 Test Purpose and Environment

Test purpose and environment in clause A.14.1.10.1 shall apply for 2Rx RedCap UE.

#### A.20.1.12.2 Test Parameters

Test parameters in clause A.14.1.10.2 shall apply except that:

Table A.14.1.3.2-1 is replaced with A.20.1.1.2-1, and

Table A.14.1.10.2-2 is replaced with A.20.1.11.2-1, and,

- Table A.14.1.10.2-3 is replaced with A.20.1.11.2-2.

#### A.20.1.12.3 Test Requirements

Test requirements in clause A.14.1.10.3 shall apply for 2Rx RedCap UEs.

### A.20.1.13 Cell reselection to FR1 inter-RAT for NR NTN carrier for 1Rx RedCap UE

#### A.20.1.13.1 Test purpose and Environment

Test purpose and environment in clause A.14.1.11.1 shall apply for 1Rx RedCap UE.

#### A.20.1.13.2 Test Parameters

- Table A.14.1.11.2-1 is replaced with A.20.1.13.2-1, and

- Table A.14.1.11.2-2 is replaced with A.20.1.13.2-2, and,

- Table A.14.1.11.2-3 is replaced with A.20.1.13.2-3, and,

- Table A.14.1.11.2-4 is replaced with A.20.1.13.2-4.

A.20.1.13.2-1: Supported test configurations

| Configuration | Description of serving cell | Description of target cell |
| --- | --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz | LTE 10 MHz bandwidth, TDD duplex mode |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz | LTE 10 MHz bandwidth, TDD duplex mode |
| 3 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz | LTE 10 MHz bandwidth, FDD duplex mode |
| 4 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz | LTE 10 MHz bandwidth, FDD duplex mode |
| 5 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz | LTE 10 MHz bandwidth, TDD duplex mode |
| 6 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz | LTE 10 MHz bandwidth, FDD duplex mode |
| NOTE 1: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases, and the UE is only required to be tested in one of the supported test configurations of the applicable scenario (GSO or NGSO).NOTE2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |  |

Table A.20.1.13.2-2: General test parameters for NR to E-UTRAN cell re-selection test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1-6 | Cell 1 | The UE camps on Cell 1 in the initial phase and during T2 period the UE reselects to Cell 2. |
| T2 end | Active cell |  | 1-6 | Cell 2 | The UE shall perform reselection to cell |
| condition | Neighbour cell |  | 1-6 | Cell 1 | 2 during T2. |
| Access Barring Information |  | - | 1-6 | Not Sent | No additional delays in random access procedure. |
| DRX cycle length |  | s | 1-6 | 1.28 | The value shall be used for all cells in the test. |
| NR PRACH configuration index |  |  | 1-6 | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| E-UTRAN PRACH configuration index |  |  | 1-6 | 53 | As specified in table 5.7.1-2 in TS 36.211 [23] |
| T1 |  | s | 1-6 | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed. The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2. |
| T2 |  | s | 1-6 | 70 | T2 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.20.1.13.2-3: Cell specific test parameters for NR Cell 1

| Parameter | Unit | Test configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| Satellite information |  | 1,3,5 | SSC.1 |  |
|  |  | 2,4,6 | SSC.2 |  |
| TDD configuration |  | 1-6 | N/A |  |
| PDSCH parameters |  | 1-6 | SR.1.1 FDD |  |
| RMSI CORESET parameters |  | 1-6 | CR.1.1 FDD |  |
| Dedicated CORESET parameters |  | 1-6 | CCR.1.1 FDD |  |
| SSB parameters |  | 1-6 | SSB.1 FR1 |  |
| NR SMTC parameters |  | 1-6 | SMTC.2 |  |
| OCNG Pattern |  | 1-6 | OP.1 defined in A.3.2.1 |  |
| Initial DL BWP configuration |  | 1-6 | DLBWP.0.1 |  |
| Initial UL BWP configuration |  | 1-6 | ULBWP.0.1 |  |
| RLM-RS |  | 1-6 | SSB |  |
| Qrxlevmin | dBm/SCS | 1-6 | -140 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] | dBm/SCS | 1-6 | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] | dBm/15 kHz | 1-6 | -98 |  |
| SS-RSRP | dBm/SCS | 1-6 | -84 | -84 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1-6 | 14 | 14 |
| ![](media_svg/image20.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1-6 | 14 | 14 |
| Io | dBm/9.36 MHz | 1-6 | -55.88 | -55.88 |
| Treselection | s | 1-6 | 0 |  |
| SnonintrasearchP | dB | 1-6 | 50 |  |
| Threshx, highP (Note 2) | dB | 1-6 | 48 |  |
| Threshserving, lowP | dB | 1-6 | 44 |  |
| Threshx, lowP | dB | 1-6 | 50 |  |
| Propagation Condition |  | 1-6 | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: This refers to the value of  Threshx, high  which is included in NR system information, and is a threshold for the E-UTRA target cell |  |  |  |  |

Table A.20.1.13.2-4: Cell specific test parameters for E-UTRA Cell 2

| Parameter | Unit | Cell 2 |  |
| --- | --- | --- | --- |
|  |  | T1 | T2 |
| E-UTRA RF Channel number |  | 1 |  |
| BWchannel | MHz | 10 |  |
| OCNG Patterns defined in TS 36.133 [15] clause A.3.2 |  | OP.2 TDD for test configuration 1, 2,5OP.2 FDD for test configuration 3, 4,6 |  |
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
| RSRP | dBm/15 KHz | -infinity | -86 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | -infinity | 12 |
| ![](media_svg/image20.svg) [公式≈: ^{Ê}s^{N}oc] | dB | -infinity | 12 |
| TreselectionEUTRAN | s | 0 |  |
| SnonintrasearchP | dB | Not sent |  |
| Threshx, highP | dB | 48 |  |
| Threshserving, lowP | dB | 44 |  |
| Threshx, lowP (Note 2) | dB | 50 |  |
| Propagation Condition |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: This refers to the value of  Threshx, Low  which is included in E-UTRA system information, and is a threshold for the NR target cell |  |  |  |

#### A.20.1.13.3 Test requirements

Test requirements in clause A.14.1.11.3 shall apply for 1Rx RedCap UEs.

### A.20.1.14 Cell reselection to FR1 inter-RAT for NR NTN carrier for 2Rx RedCap UE

#### A.20.1.14.1 Test purpose and Environment

Test purpose and environment in clause A.14.1.11.1 shall apply for 2Rx RedCap UE.

#### A.20.1.14.2 Test Parameters

- Table A.14.1.11.2-1 is replaced with A.20.1.13.2-1, and

- Table A.14.1.11.2-2 is replaced with A.20.1.13.2-2, and,

- Table A.14.1.11.2-3 is replaced with A.20.1.13.2-3, and,

- Table A.14.1.11.2-4 is replaced with A.20.1.13.2-4.



#### A.20.1.14.3 Test requirements

Test requirements in clause A.14.1.11.3 shall apply for 2Rx RedCap UEs.

### A.20.1.15 Cell re-selection to FR1 inter-frequency NR case with TN carrier for 1Rx RedCap UE

#### A.20.1.15.1 Test purpose and Environment

Test purpose and environment in clause A.14.1.12.1 shall apply for 1Rx RedCap UE.

#### A.20.1.15.2 Test parameters

- Table A.14.1.12.2-1 is replaced with A.20.1.15.2-1, and

- Table A.14.1.12.2-2 is replaced with A.20.1.15.2-2, and,

- Table A.14.1.12.2-3 is replaced with A.20.1.15.2-3.

Table A.20.1.15.2-1: Supported test configurations

| Configuration | Description of serving cell | Description of target cell |
| --- | --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 4 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 5 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 6 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 7 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 8 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 9 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 10 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 11 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 12 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases, and the UE is only required to be tested in one of the supported test configurations of the applicable scenario (GSO or NGSO). NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |  |

Table A.20.1.15.2-2: General test parameters for inter frequency NR cell re-selection test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
| Initial condition | Active cell |  | 1-12 | Cell 1 |  |
| T2 end condition | Active cell |  | 1-12 | Cell 2 |  |
|  | Neighbour cells |  | 1-12 | Cell 1 |  |
| RF Channel Number |  |  | 1-12 | 1,2 | Cell 1 is on RF channel 1Cell 2 is on RF channel 2 |
| Time offset between cells |  |  | 1-12 | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | 1-12 | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | 1-12 | SSB.1 FR1 |  |
| SMTC configuration |  |  | 1-12 | SMTC.6 | Configured in SIB4 for Cell 1 and Cell 2 |
| DRX cycle length |  | s | 1-12 | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1-12 | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | 1-12 | Not configured |  |
| Ephemeris information |  |  | 1-12 | Note 1 | The detailed configuration is specified in SIB19 |
| T1 |  | s | 1-12 | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2 |
| T2 |  | s | 1-12 | 70 | T2 needs to be defined so that cell re-selection reaction time is taken into account. |
| Note 1: Detailed ephemeris information is provided in TS 38.508-1 [38] |  |  |  |  |  |

Table A.20.1.15.2-3: Cell specific test parameters for inter frequency NR cell re-selection test case

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1,2,3,7,8,9 | SSC.1 |  | N/A |  |
|  |  | 4,5,6,10,11,12 | SSC.2 |  |  |  |
| TDD configuration |  | 1,4,7,10 | N/A |  | N/A |  |
|  |  | 2,5,8,11 |  |  | TDDConf.1.1 |  |
|  |  | 3,6,9,12 |  |  | TDDConf.2.1 |  |
| PDSCH RMC |  | 1,4,7,10 | SR.1.1 FDD |  | SR.1.1 FDD |  |
| configuration |  | 2,5,8,11 |  |  | SR.1.1 TDD |  |
|  |  | 3,6,9,12 |  |  | SR.2.1 TDD |  |
| RMSI CORESET |  | 1,4,7,10 | CR.1.1 FDD |  | CR.1.1 FDD |  |
| RMC configuration |  | 2,5,8,11 |  |  | CR.1.1 TDD |  |
|  |  | 3,6,9,12 |  |  | CR.2.1 TDD |  |
| Dedicated CORESET |  | 1,4,7,10 | CCR.1.1 FDD |  | CCR.1.1 FDD |  |
| RMC configuration |  | 2,5,8,11 |  |  | CCR.1.1 TDD |  |
|  |  | 3,6,9,12 |  |  | CCR.2.1 TDD |  |
| OCNG Pattern |  | 1-12 | OP.1 defined in clause A.3.2.1 |  | OP.1 defined in clause A.3.2.1 |  |
| Initial DL BWP configuration |  | 1-12 | DLBWP.0.1 |  | DLBWP.0.1 |  |
| Initial UL BWP configuration |  | 1-12 | ULBWP.0.1 |  | ULBWP.0.1 |  |
| RLM-RS |  | 1-12 | SSB |  | SSB |  |
| Qrxlevmin | dBm/SCS | 1,2,4,5,7,8,10,11 | -140 |  | -140 |  |
|  |  | 3,6,9,12 |  |  | -137 |  |
| Pcompensation | dB | 1-12 | 0 |  | 0 |  |
| Cell_selection_and_reselection_quality_measurement |  | 1-12 | SS-RSRP |  | SS-RSRP |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1-6 | 14 | 14 | -infinity | 12 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1,2,4,5,7,8,10,11 | -98 |  | -98 |  |
|  |  | 3,6,9,12 |  |  | -95 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1-12 | -98 |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1-12 | 14 | 14 | -infinity | 12 |
| SS-RSRP Note3 | dBm/SCS | 1,2,4,5,7,8,10,11 | -84 | -84 | -infinity | -86 |
|  |  | 3,6,9,12 |  |  | -infinity | -83 |
| Io | dBm/Ch BW | 1,2,4,5,7,8,10,11 | -55.88 | -55.88 | -70.05 | -57.78 |
|  |  | 3,6,9,12 |  |  | -63.96 | -51.69 |
| Treselection | s | 1-12 | 0 | 0 | 0 | 0 |
| SnonintrasearchP | dB | 1-12 | 50 |  | 50 |  |
| Threshx, highP | dB | 1-12 | 48 |  | 48 |  |
| Threshserving, lowP | dB | 1-12 | 44 |  | 44 |  |
| Threshx, lowP | dB | 1-12 | 50 |  | 50 |  |
| Propagation Condition |  | 1-12 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

#### A.20.1.15.3 Test requirements

Test requirements in clause A.14.1.12.3 shall apply for 1Rx RedCap UEs.

### A.20.1.16 Cell re-selection to FR1 inter-frequency NR case with TN carrier for 2Rx RedCap UE

#### A.20.1.16.1 Test purpose and Environment

Test purpose and environment in clause A.14.1.12.1 shall apply for 2Rx RedCap UE.

#### A.20.1.16.2 Test parameters

- Table A.14.1.12.2-1 is replaced with A.20.1.15.2-1, and

- Table A.14.1.12.2-2 is replaced with A.20.1.15.2-2, and,

- Table A.14.1.12.2-3 is replaced with A.20.1.15.2-3.

#### A.20.1.16.3 Test requirements

Test requirements in clause A.14.1.12.3 shall apply for 2Rx RedCap UEs.

## A.20.2 RRC_CONNECTED state mobility

### A.20.2.1 Handover

#### A.20.2.1.1 Intra-frequency SAN Handover from FR1 to FR1 for 1Rx RedCap UE

##### A.20.2.1.1.1 Test Purpose and Environment

This test is to verify the requirement for Intra-frequency SAN Handover from FR1 to FR1 specified in clause 6.1F.1 for 1Rx RedCap UE.

##### A.20.2.1.1.2 Test Parameters

Test parameters in clause A.14.2.1.1.2 shall apply except that the supported test configurations are defined in table A.20.2.1.1.2-1, and NR Cell specific test parameters in Table A.20.2.1.1.2-2 replace the corresponding parameters in Table A.14.2.1.1.2-3. Other parameters in Table A.14.2.1.1.2-2 and Table A.14.2.1.1.2-3 shall apply to test configurations 1, 2, 3 and 4.


In the test, the target cell is known by the UE and carries only CD-SSB.

Table A.20.2.1.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.1.1.2-2: Cell specific test parameters for Intra frequency SAN handover test case

| Parameter | Test configuration | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information | Config 1,3 |  | SSC.1 |  |  | NSC.1 |  |  |
|  | Config 2,4 |  | SSC.2 |  |  | NSC.2 |  |  |
| Koffset | Config 1,3 | ms | 239 |  |  | 239 |  |  |
|  | Config 2,4 |  | 4 |  |  | 4 |  |  |
| Antenna Configuration | 1Rx |  | 1x1 |  |  |  |  |  |

##### A.20.2.1.1.3 Test Requirements


Test requirements in clause A.14.2.1.1.3 shall apply for 1Rx RedCap UEs.

#### A.20.2.1.2 Intra-frequency SAN Handover from FR1 to FR1 for 2Rx RedCap UE

##### A.20.2.1.2.1 Test Purpose and Environment

This test is to verify the requirement for Intra-frequency SAN Handover from FR1 to FR1 specified in clause 6.1F.1 for 2Rx RedCap UE.

##### A.20.2.1.2.2 Test Parameters

Test parameters in clause A.20.2.1.1.2 shall apply. The antenna configuration for 2Rx RedCap UE is 1x2.

##### A.20.2.1.2.3 Test Requirements

Test requirements in clause A.14.2.1.1.3 shall apply for 2Rx RedCap UEs.

#### A.20.2.1.3 Inter-frequency SAN Handover from FR1 to FR1 for 1Rx RedCap UE

##### A.20.2.1.3.1 Test Purpose and Environment

This test is to verify the requirement for Inter-frequency SAN Handover from FR1 to FR1 specified in clause 6.1F.1 for 1Rx RedCap UE.

##### A.20.2.1.3.2 Test Parameters

Test parameters in clause A.14.2.1.2.2 shall apply except that the supported test configurations are defined in table A.20.2.1.1.2-1, and NR Cell specific test parameters in Table A.20.2.1.1.2-2 replace the corresponding parameters in Table A.14.2.1.2.2-3. Other parameters in Table A.14.2.1.2.2-2 and Table A.14.2.1.2.2-3 shall apply to test configurations 1, 2, 3 and 4.

In the test, the target cell is known by the UE and carries only CD-SSB. The antenna configuration for 1Rx RedCap UE is 1x1.

##### A.20.2.1.3.3 Test Requirements

Test requirements in clause A.14.2.1.2.3 shall apply for 1Rx RedCap UEs.

#### A.20.2.1.4 Inter-frequency SAN Handover from FR1 to FR1 for 2Rx RedCap UE

##### A.20.2.1.4.1 Test Purpose and Environment

This test is to verify the requirement for Inter-frequency SAN Handover from FR1 to FR1 specified in clause 6.1F.1 for 2Rx RedCap UE.

##### A.20.2.1.4.2 Test Parameters

Test parameters in clause A.20.2.1.3.2 shall apply. The antenna configuration for 2Rx RedCap UE is 1x2.

##### A.20.2.1.4.3 Test Requirements

Test requirements in clause A.14.2.1.2.3 shall apply for 2Rx RedCap UEs.

#### A.20.2.1.5 Intra-frequency SAN RACH-less Handover from FR1 to FR1 for 1Rx RedCap UE

##### A.20.2.1.5.1 Test Purpose and Environment

This test is to verify the requirement for Intra-frequency SAN RACH-less Handover from FR1 to FR1 specified in clause 6.1F.1 for 1Rx RedCap UE.

##### A.20.2.1.5.2 Test Parameters

Test parameters in clause A.14.2.1.8.2 shall apply except that the supported test configurations are defined in table A.20.2.1.1.2-1, and NR Cell specific test parameters in Table A.20.2.1.1.2-2 replace the corresponding parameters in Table A.14.2.1.8.2-3. Other parameters in Table A.14.2.1.8.2-2 and Table A.14.2.1.8.2-3 shall apply to test configurations 1, 2, 3 and 4.

In the test, the target cell is known by the UE and carries only CD-SSB. The antenna configuration for 1Rx RedCap UE is 1x1.

##### A.20.2.1.5.3 Test Requirements

Test requirements in clause A.14.2.1.8.3 shall apply for 1Rx RedCap UE.


#### A.20.2.1.6 Intra-frequency SAN RACH-less Handover from FR1 to FR1 for 2Rx RedCap UE

##### A.20.2.1.6.1 Test Purpose and Environment

This test is to verify the requirement for Intra-frequency SAN RACH-less Handover from FR1 to FR1 specified in clause 6.1F.1 for 2Rx RedCap UE.

##### A.20.2.1.6.2 Test Parameters

Test parameters in clause A.20.2.1.5.2 shall apply. The antenna configuration for 2Rx RedCap UE is 1x2.

##### A.20.2.1.6.3 Test Requirements

Test requirements in clause A.14.2.1.8.3 shall apply for 2Rx RedCap UE.

#### A.20.2.1.7 Intra-frequency SAN time-based conditional Handover from FR1 to FR1 for 1Rx RedCap UE

##### A.20.2.1.7.1 Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN time-based conditional handover from FR1 to FR1 specified in clause 6.1F.2 for 1Rx RedCap UE.

##### A.20.2.1.7.2 Test Parameters

Test parameters in clause A.14.2.1.3.2 shall apply except that the supported test configurations are defined in table A.20.2.1.7.2-1, and NR Cell specific test parameters in Table A.20.2.1.7.2-2 replace the corresponding parameters in Table A.14.2.1.3.2-3. Other parameters in Table A.14.2.1.3.2-2 and Table A.14.2.1.3.2-3 shall apply to test configurations 1, 2, 3 and 4.

In the test, the target cell is known by the UE and carries only CD-SSB.

Table A.20.2.1.7.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.1.7.2-2: Cell specific test parameters for Intra-frequency SAN time-based conditional handover from FR1 to FR1

| Parameter | Test configuration | Unit | Cell 1 |  |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 |  | T2 | T1 | T2 |
| Satellite information | Config 1,3 |  | SSC.1 |  |  | NSC.1 |  |
|  | Config 2,4 |  | SSC.2 |  |  | NSC.2 |  |
| Koffset | Config 1,3 | ms | 239 |  |  | 239 |  |
|  | Config 2,4 | ms | 4 |  |  | 4 |  |
| Antenna Configuration | 1Rx |  |  | 1x1 |  |  |  |

##### A.20.2.1.7.3 Test Requirements

Test requirements in clause A.14.2.1.3.3 shall apply for 1Rx RedCap UE.

#### A.20.2.1.8 Intra-frequency SAN time-based conditional Handover from FR1 to FR1 for 2Rx RedCap UE

##### A.20.2.1.8.1 Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN time-based conditional handover from FR1 to FR1 specified in clause 6.1F.2 for 2Rx RedCap UE.

##### A.20.2.1.8.2 Test Parameters

Test parameters in clause A.20.2.1.7.2 shall apply. The antenna configuration for 2Rx RedCap UE is 1x2.

##### A.20.2.1.8.3 Test Requirements

Test requirements in clause A.14.2.1.3.3 shall apply for 2Rx RedCap UE.

#### A.20.2.1.9 Inter-frequency SAN distance-based conditional Handover from FR1 to FR1 for 1Rx RedCap UE

##### A.20.2.1.9.1 Test Purpose and Environment

This test is to verify the requirement for inter-frequency SAN distance-based conditional handover from FR1 to FR1 specified in clause 6.1F.2 for 1Rx RedCap UE.

##### A.20.2.1.9.2 Test Parameters

Test parameters in clause A.14.2.1.6.2 shall apply except that the supported test configurations are defined in table A.20.2.1.7.2-1, and NR Cell specific test parameters in Table A.20.2.1.7.2-2 replace the corresponding parameters in Table A.14.2.1.6.2-3. Other parameters in Table A.14.2.1.6.2-2 and Table A.14.2.1.6.2-3 shall apply to test configurations 1, 2, 3 and 4.

In the test, the target cell is known by the UE and carries only CD-SSB. The antenna configuration for 1Rx RedCap UE is 1x1.

##### A.20.2.1.9.3 Test Requirements

Test requirements in clause A.14.2.1.6.3 shall apply for 1Rx RedCap UE.

#### A.20.2.1.10 Inter-frequency SAN distance-based conditional Handover from FR1 to FR1 for 2Rx RedCap UE

##### A.20.2.1.10.1 Test Purpose and Environment

This test is to verify the requirement for inter-frequency SAN distance-based conditional handover from FR1 to FR1 specified in clause 6.1F.2 for 2Rx RedCap UE.

##### A.20.2.1.10.2 Test Parameters

Test parameters in clause A.20.2.1.9.2 shall apply. The antenna configuration for 2Rx RedCap UE is 1x2.

##### A.20.2.1.10.3 Test Requirements

Test requirements in clause A.14.2.1.6.3 shall apply for 2Rx RedCap UE.

#### A.20.2.1.11 Intra-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 1Rx RedCap UE

##### A.20.2.1.11.1 Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN time-based conditional handover without L3 measurement criteria from FR1 to FR1 specified in clause 6.1F.2.3 for 1Rx RedCap UE.

##### A.20.2.1.11.2 Test Parameters

Test parameters in clause A.14.2.3.2 shall apply except that the supported test configurations are defined in table A.20.2.1.11.2-1. Parameters in Table A.14.2.3.2-2 and Table A.14.2.3.2-3 shall apply to test configurations 1 and 2.

In the test, the target cell is known by the UE and carries only CD-SSB. The antenna configuration for 1Rx RedCap UE is 1x1.

Table A.20.2.1.11.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.2.1.11.3 Test Requirements

Test requirements in clause A.14.2.3.3 shall apply for 1Rx RedCap UE.

#### A.20.2.1.12 Intra-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 2Rx RedCap UE

##### A.20.2.1.12.1 Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN time-based conditional handover without L3 measurement criteria from FR1 to FR1 specified in clause 6.1F.2.3 for 2Rx RedCap UE.

##### A.20.2.1.12.2 Test Parameters

Test parameters in clause A.20.2.1.11.2 shall apply. The antenna configuration for 2Rx RedCap UE is 1x2.

##### A.20.2.1.12.3 Test Requirements

Test requirements in clause A.14.2.3.3 shall apply for 2Rx RedCap UE.

#### A.20.2.1.13 Inter-frequency SAN distance-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 1Rx RedCap UE

##### A.20.2.1.13.1 Test Purpose and Environment

This test is to verify the requirement for inter-frequency SAN distance-based conditional handover without L3 measurement criteria from FR1 to FR1 specified in clause 6.1F.2.3 for 1Rx RedCap UE.

##### A.20.2.1.13.2 Test Parameters

Test parameters in clause A.14.2.1.6.2 shall apply except that the supported test configurations are defined in table A.20.2.1.11.2-1 and except that general test parameters are defined in A.20.2.1.13.2-1; NR Cell specific test parameters in Table A.20.2.1.13.2-2 replace the corresponding parameters in Table A.14.2.1.6.2-3. Other parameters in Table A.14.2.1.6.2-3 shall apply to test configurations 1 and 2.

The test scenario comprises of 2 NR FDD carriers and one cell on each carrier. Both handover delay and interruption length are tested. The target cell is known by the UE and carries only CD-SSB.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure inter-frequency neighbour cell with Gap pattern ID gp0. The RRC message implying distance-based handover to Cell 2 with Event D1 shall be sent to UE, at a time earlier than TRRC (10 ms) before the beginning of T2.

Starting T2, Cell 2 becomes detectable and after 11670 ms of T2, location condition event condEventD1-r17 is fulfilled.

Table A.20.2.1.13.2-1: General test parameters for Inter-frequency SAN distance-based conditional handover without L3 measurement criteria from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1, 2 | Two NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 |  |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) at T1 start |  |  | (0, 0, 0) | Set by any pre-configured means (L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| UE moving speed |  | km/h | (108, 0, 0) | Set by any pre-configured means |
| referenceLocation1-r17.condEventD1-r17 |  | m | (-700, 0, 0) | Reference location for serving cell |
| referenceLocation2-r17.condEventD1-r17 |  | m | (1300, 0, 0) | Reference location for target cell |
| distanceThreshFromReference1-r17.condEventD1-r17 |  | 50m | 20 | D1-1 Location condition is fulfilled at T2 |
| distanceThreshFromReference2-r17.condEventD1-r17 |  | 50m | 20 | D1-2 Location condition is fulfilled at T2 |
| hysteresis-r17.condEventD1-r17 |  | 10m | 0 |  |
| timeToTrigger-r17.condEventD1-r17 |  | s | 0 |  |
| Gap Pattern Id |  |  | 0 |  |
| Measurement gap offset |  |  | 9 |  |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 1 |  |
| T2 |  | s | 12 |  |

Table A.20.2.1.13.2-2: Cell specific test parameters for Inter-frequency SAN distance-based conditional handover without L3 measurement criteria from FR1 to FR1

| Parameter | Test configuration | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information | Config 1,2 |  | SSC.2 |  | NSC.2 |  |
| Koffset | Config 1,2 | ms | 4 |  | 4 |  |
| Antenna Configuration | 1Rx |  | 1x1 |  |  |  |

##### A.20.2.1.13.3 Test Requirements

Test requirements in clause A.14.2.1.6.3 shall apply for 1Rx RedCap UE.

#### A.20.2.1.14 Inter-frequency SAN distance-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 2Rx RedCap UE

##### A.20.2.1.14.1 Test Purpose and Environment

This test is to verify the requirement for inter-frequency SAN distance-based conditional handover without L3 measurement criteria from FR1 to FR1 specified in clause 6.1F.2.3 for 2Rx RedCap UE.

##### A.20.2.1.14.2 Test Parameters

Test parameters in clause A.20.2.1.Y7.2 shall apply. The antenna configuration for 2Rx RedCap UE is 1x2.

##### A.20.2.1.14.3 Test Requirements

Test requirements in clause A.14.2.1.6.3 shall apply for 2Rx RedCap UE.

### A.20.2.2 RRC Connection Mobility Control

#### A.20.2.2.1 SA: RRC Re-establishment for SAN

##### A.20.2.2.1.1 Intra-frequency RRC Re-establishment in FR1 for 1 Rx RedCap UE

A.20.2.2.1.1.1 Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR1 with known target cell is within the specified limits. These tests will verify the requirements in clause 6.2E.1.

The test parameters are given in table A.20.2.2.1.1.1-1, table A.20.2.2.1.1.1-2 and table A.20.2.2.1.1.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.2.2.1.1.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.2.1.1.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR1 for 1 Rx RedCap UE

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2,3,4 | Cell 1 |  |
|  | Neighbour cells |  | 1, 2,3,4 | Cell 2 |  |
| Final condition | Active cell |  | 1, 2,3,4 | Cell 2 |  |
| RF Channel Number |  |  | 1, 2,3,4 | 1 |  |
| Time offset between cells |  |  | 1,3 | 3 ms | Asynchronous cells |
| N310 |  | - | 1, 2,3,4 | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1, 2,3,4 | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 1, 2,3,4 | 0 | Radio link failure timer; |
| T311 |  | ms | 1, 2,3,4 | 3000 | RRC re-establishment timer |
| Access Barring Information |  | - | 1, 2,3,4 | Not Sent | No additional delays in random access procedure. |
| SMTC configuration |  |  | 1, 2,3,4 | SMTC.2 |  |
| DRX cycle length |  | s | 1, 2,3,4 | OFF |  |
| PRACH configuration |  |  | 1, 2,3,4 | FR1 PRACH configuration 1 | Table A.3.8.2.1-1 |
| T1 |  | s | 1, 2,3,4 | 5 |  |
| T2 |  | ms | 1, 2,3,4 | 640 | Time for the UE to detect RLF(Summation of TEvaluate_out_SSB defined in clause 8.1C in TS 38.133, T310 and the period for UE turns off transmitter defined in clause 8.1C.5 in TS 38.133 ) |
| T3 |  | s | 1, 2,3,4 | 2 |  |

Table A.20.2.2.1.1.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR1

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | 1,3 | SSC.1 |  |  | NSC.1 |  |  |
|  |  | 2,4 | SSC.2 |  |  | NSC.2 |  |  |
| PDSCH RMC configuration |  | 1, 2,3,4 | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |
| RMSI CORESET RMC configuration |  | 1, 2,3,4 | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |
| Dedicated CORESET RMC configuration |  | 1, 2,3,4 | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |
| OCNG Pattern |  | 1, 2,3,4 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| TRS configuration |  | 1, 2,3,4 | TRS.1.1 FDD |  |  | TRS.1.1 FDD |  |  |
| Initial DL BWP configuration |  | 1, 2,3,4 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2,3,4 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Active DL BWP confgiuration |  | 1, 2,3,4 | DLBWP.1.1 | N/A | N/A | N/A | N/A | DLBWP.1.1 |
| Active UL BWP configuration |  | 1, 2,3,4 | ULBWP.1.1 | N/A | N/A | N/A | N/A | ULBWP.1.1 |
| SSB configuration |  | 1, 2,3,4 | SSB.1 FR1 |  |  | SSB.1 FR1 |  |  |
| RLM-RS |  | 1, 2,3,4 | SSB |  |  | SSB |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2,3,4 | 1.54 | -infinity | -infinity | -3.79 | 4 | 4 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1, 2,3,4 | -98 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 2,3,4 | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2,3,4 | 7 | -infinity | -infinity | 4 | 4 | 4 |
| SS-RSRP Note3 | dBm/SCS | 1, 2,3,4 | -91 | -infinity | -infinity | -94 | -94 | -94 |
| Io | dBm/9.36 MHz | 1, 2,3,4 | -60.74 | -64.59 | -64.59 | -60.74 | -64.59 | -64.59 |
| Propagation Condition |  | 1, 2,3,4 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

A.20.2.2.1.1.2 Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to a known NR intra frequency cell shall be less than 1.6 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE: The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

$ T_{UE\_re-establish\_delay}=50 ms+T_{identify\_intra\_NR}+\sum  _{i=1}^{Nfreq-1}T_{identify\_inter\_NR,i}+T_{SI-NR}+T_{PRACH}$

Nfreq = 1

Tidentify_intra_NR = 200 ms

TSI = 1280 ms, provided that SIB1 and SIB19 are scheduled with 20 ms period; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1545 ms, allow 1.6 s in the test case.

##### A.20.2.2.1.2 Intra-frequency RRC Re-establishment in FR1 for 2 Rx RedCap UE

A.20.2.2.1.2.1 Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR1 with known target cell is within the specified limits. These tests will verify the requirements in clause 6.2E.1.

The test parameters are given in table A.20.2.2.1.2.1-1, table A.20.2.2.1.2.1-2 and table A.20.2.2.1.2.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.2.2.1.2.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.2.1.2.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR1 for 2 Rx RedCap UE

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2,3,4 | Cell 1 |  |
|  | Neighbour cells |  | 1, 2,3,4 | Cell 2 |  |
| Final condition | Active cell |  | 1, 2,3,4 | Cell 2 |  |
| RF Channel Number |  |  | 1, 2,3,4 | 1 |  |
| Time offset between cells |  |  | 1,3 | 3 ms | Asynchronous cells |
| N310 |  | - | 1, 2,3,4 | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1, 2,3,4 | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 1, 2,3,4 | 0 | Radio link failure timer; |
| T311 |  | ms | 1, 2,3,4 | 3000 | RRC re-establishment timer |
| Access Barring Information |  | - | 1, 2,3,4 | Not Sent | No additional delays in random access procedure. |
| SMTC configuration |  |  | 1, 2,3,4 | SMTC.2 |  |
| DRX cycle length |  | s | 1, 2,3,4 | OFF |  |
| PRACH configuration |  |  | 1, 2,3,4 | FR1 PRACH configuration 1 | Table A.3.8.2.1-1 |
| T1 |  | s | 1, 2,3,4 | 5 |  |
| T2 |  | ms | 1, 2,3,4 | 640 | Time for the UE to detect RLF(Summation of TEvaluate_out_SSB defined in clause 8.1C in TS 38.133, T310 and the period for UE turns off transmitter defined in clause 8.1C.5 in TS 38.133 ) |
| T3 |  | s | 1, 2,3,4 | 2 |  |

Table A.20.2.2.1.2.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR1 for 2 Rx RedCap UE

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | 1,3 | SSC.1 |  |  | NSC.1 |  |  |
|  |  | 2,4 | SSC.2 |  |  | NSC.2 |  |  |
| PDSCH RMC configuration |  | 1, 2,3,4 | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |
| RMSI CORESET RMC configuration |  | 1, 2,3,4 | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |
| Dedicated CORESET RMC configuration |  | 1, 2,3,4 | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |
| OCNG Pattern |  | 1, 2,3,4 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| TRS configuration |  | 1, 2,3,4 | TRS.1.1 FDD |  |  | TRS.1.1 FDD |  |  |
| Initial DL BWP configuration |  | 1, 2,3,4 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2,3,4 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Active DL BWP confgiuration |  | 1, 2,3,4 | DLBWP.1.1 | N/A | N/A | N/A | N/A | DLBWP.1.1 |
| Active UL BWP configuration |  | 1, 2,3,4 | ULBWP.1.1 | N/A | N/A | N/A | N/A | ULBWP.1.1 |
| SSB configuration |  | 1, 2,3,4 | SSB.1 FR1 |  |  | SSB.1 FR1 |  |  |
| RLM-RS |  | 1, 2,3,4 | SSB |  |  | SSB |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2,3,4 | 1.54 | -infinity | -infinity | -3.79 | 4 | 4 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1, 2,3,4 | -98 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 2,3,4 | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2,3,4 | 7 | -infinity | -infinity | 4 | 4 | 4 |
| SS-RSRP Note3 | dBm/SCS | 1, 2,3,4 | -91 | -infinity | -infinity | -94 | -94 | -94 |
| Io | dBm/9.36 MHz | 1, 2,3,4 | -60.74 | -64.59 | -64.59 | -60.74 | -64.59 | -64.59 |
| Propagation Condition |  | 1, 2,3,4 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

A.20.2.2.1.2.2 Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to a known NR intra frequency cell shall be less than 1.6 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE: The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

$ T_{UE\_re-establish\_delay}=50 ms+T_{identify\_intra\_NR}+\sum  _{i=1}^{Nfreq-1}T_{identify\_inter\_NR,i}+T_{SI-NR}+T_{PRACH}$

Nfreq = 1

Tidentify_intra_NR = 200 ms

TSI = 1280 ms, provided that SIB1 and SIB19 are scheduled with 20 ms period; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1545 ms, allow 1.6 s in the test case.









##### A.20.2.2.1.3 Inter-frequency RRC Re-establishment in FR1 for 1 Rx RedCap UE

A.20.2.2.1.3.1 Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR1 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2E.1.

The test parameters are given in table A.20.2.2.1.3.1-1, table A.20.2.2.1.3.1-2 and table A.20.2.2.1.3.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.2.2.1.3.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.2.1.3.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1 for 1 Rx RedCap UE

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2,3,4 | Cell 1 |  |
|  | Neighbour cells |  | 1, 2,3,4 | Cell 2 |  |
| Final condition | Active cell |  | 1, 2,3,4 | Cell 2 |  |
| RF Channel Number |  |  | 1, 2,3,4 | 1, 2 |  |
| Time offset between cells |  |  | 1, 2,3,4 | 3 ms | Asynchronous cells |
| N310 |  | - | 1, 2,3,4 | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1, 2,3,4 | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 1, 2,3,4 | 0 | Radio link failure timer; |
| T311 |  | ms | 1, 2,3,4 | 5000 | RRC re-establishment timer |
| Access Barring Information |  | - | 1, 2,3,4 | Not Sent | No additional delays in random access procedure. |
| SMTC configuration |  |  | 1, 2,3,4 | SMTC.2 |  |
| DRX cycle length |  | s | 1, 2,3,4 | OFF |  |
| PRACH configuration |  |  | 1, 2,3,4 | FR1 PRACH configuration 1 | Table A.3.8.2.1-1 |
| T1 |  | s | 1, 2,3,4 | 5 |  |
| T2 |  | ms | 1, 2,3,4 | 640 | Time for the UE to detect RLF(Summation of TEvaluate_out_SSB defined in clause 8.1C in TS 38.133, T310 and the period for UE turns off transmitter defined in clause 8.1C.5 in TS 38.133 ) |
| T3 |  | s | 1, 2,3,4 | 5 |  |

Table A.20.2.2.1.3.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1 for 1 Rx RedCap UE

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | 1,3 | SSC.1 |  |  | NSC.1 |  |  |
|  |  | 2,4 | SSC.2 |  |  | NSC.2 |  |  |
| RF Channel Number |  | 1, 2,3,4 | 1 |  |  | 2 |  |  |
| PDSCH RMC configuration |  | 1, 2,3,4 | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |
| RMSI CORESET RMC configuration |  | 1, 2,3,4 | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |
| Dedicated CORESET RMC configuration |  | 1, 2,3,4 | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |
| OCNG Pattern |  | 1, 2,3,4 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| TRS configuration |  | 1, 2,3,4 | TRS.1.1 FDD |  |  | TRS.1.1 FDD |  |  |
| Initial DL BWP configuration |  | 1, 2,3,4 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2,3,4 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Active DL BWP confgiuration |  | 1, 2,3,4 | DLBWP.1.1 | N/A | N/A | N/A | N/A | DLBWP.1.1 |
| Active UL BWP configuration |  | 1, 2,3,4 | ULBWP.1.1 | N/A | N/A | N/A | N/A | ULBWP.1.1 |
| SSB configuration |  | 1, 2,3,4 | SSB.1 FR1 |  |  | SSB.1 FR1 |  |  |
| RLM-RS |  | 1, 2,3,4 | SSB |  |  | SSB |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2,3,4 | 4 | -infinity | -infinity | -infinity | -infinity | 7 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1, 2,3,4 | -98 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 2,3,4 | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2,3,4 | 4 | -infinity | -infinity | -infinity | -infinity | 7 |
| SS-RSRP Note3 | dBm/SCS | 1, 2,3,4 | -94 | -infinity | -infinity | -infinity | -infinity | -91 |
| Io | dBm/9.36 MHz | 1, 2,3,4 | -64.59 | -70. 05 | -70. 05 | -70. 05 | -70. 05 | -62.26 |
| Propagation Condition |  | 1, 2,3,4 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

A.20.2.2.1.3.2 Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell shall be less than 3 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE: The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

$ T_{UE\_re-establish\_delay}=50ms+T_{identify\_intra\_NR}+\sum  _{i=1}^{Nfreq-1}T_{identify\_inter\_NR,i}+T_{SI-NR}+T_{PRACH}$

Nfreq = 2

Tidentify_intra_NR = 800 ms

Tidentify_inter_NR = 800 ms

TSI = 1280 ms, provided that SIB1 and SIB19 are scheduled with 20 ms period; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 2945 ms, allow 3 s in the test case.

##### A.20.2.2.1.4 Inter-frequency RRC Re-establishment in FR1 for 2 Rx RedCap UE

A.20.2.2.1.4.1 Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR1 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2E.1.

The test parameters are given in table A.20.2.2.1.4.1-1, table A.20.2.2.1.4.1-2 and table A.20.2.2.1.4.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.2.2.1.4.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.2.1.4.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1 for 2 Rx RedCap UE

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2,3,4 | Cell 1 |  |
|  | Neighbour cells |  | 1, 2,3,4 | Cell 2 |  |
| Final condition | Active cell |  | 1, 2,3,4 | Cell 2 |  |
| RF Channel Number |  |  | 1, 2,3,4 | 1, 2 |  |
| Time offset between cells |  |  | 1, 2,3,4 | 3 ms | Asynchronous cells |
| N310 |  | - | 1, 2,3,4 | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1, 2,3,4 | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 1, 2,3,4 | 0 | Radio link failure timer; |
| T311 |  | ms | 1, 2,3,4 | 5000 | RRC re-establishment timer |
| Access Barring Information |  | - | 1, 2,3,4 | Not Sent | No additional delays in random access procedure. |
| SMTC configuration |  |  | 1, 2,3,4 | SMTC.2 |  |
| DRX cycle length |  | s | 1, 2,3,4 | OFF |  |
| PRACH configuration |  |  | 1, 2,3,4 | FR1 PRACH configuration 1 | Table A.3.8.2.1-1 |
| T1 |  | s | 1, 2,3,4 | 5 |  |
| T2 |  | ms | 1, 2,3,4 | 640 | Time for the UE to detect RLF(Summation of TEvaluate_out_SSB defined in clause 8.1C in TS 38.133, T310 and the period for UE turns off transmitter defined in clause 8.1C.5 in TS 38.133 ) |
| T3 |  | s | 1, 2,3,4 | 5 |  |

Table A.20.2.2.1.4-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1 for 2 Rx RedCap UE

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | 1,3 | SSC.1 |  |  | NSC.1 |  |  |
|  |  | 2,4 | SSC.2 |  |  | NSC.2 |  |  |
| RF Channel Number |  | 1, 2,3,4 | 1 |  |  | 2 |  |  |
| PDSCH RMC configuration |  | 1, 2,3,4 | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |
| RMSI CORESET RMC configuration |  | 1, 2,3,4 | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |
| Dedicated CORESET RMC configuration |  | 1, 2,3,4 | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |
| OCNG Pattern |  | 1, 2,3,4 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| TRS configuration |  | 1, 2,3,4 | TRS.1.1 FDD |  |  | TRS.1.1 FDD |  |  |
| Initial DL BWP configuration |  | 1, 2,3,4 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2,3,4 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Active DL BWP confgiuration |  | 1, 2,3,4 | DLBWP.1.1 | N/A | N/A | N/A | N/A | DLBWP.1.1 |
| Active UL BWP configuration |  | 1, 2,3,4 | ULBWP.1.1 | N/A | N/A | N/A | N/A | ULBWP.1.1 |
| SSB configuration |  | 1, 2,3,4 | SSB.1 FR1 |  |  | SSB.1 FR1 |  |  |
| RLM-RS |  | 1, 2,3,4 | SSB |  |  | SSB |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2,3,4 | 4 | -infinity | -infinity | -infinity | -infinity | 7 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1, 2,3,4 | -98 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 2,3,4 | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2,3,4 | 4 | -infinity | -infinity | -infinity | -infinity | 7 |
| SS-RSRP Note3 | dBm/SCS | 1, 2,3,4 | -94 | -infinity | -infinity | -infinity | -infinity | -91 |
| Io | dBm/9.36 MHz | 1, 2,3,4 | -64.59 | -70. 05 | -70. 05 | -70. 05 | -70. 05 | -62.26 |
| Propagation Condition |  | 1, 2,3,4 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

A.20.2.2.1.4.2 Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell shall be less than 3 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE: The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

$ T_{UE\_re-establish\_delay}=50ms+T_{identify\_intra\_NR}+\sum  _{i=1}^{Nfreq-1}T_{identify\_inter\_NR,i}+T_{SI-NR}+T_{PRACH}$

Nfreq = 2

Tidentify_intra_NR = 800 ms

Tidentify_inter_NR = 800 ms

TSI = 1280 ms, provided that SIB1 and SIB19 are scheduled with 20 ms period; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 2945 ms, allow 3 s in the test case.

#### A.20.2.2.2 Random Access

##### A.20.2.2.2.1 4-step RA type contention based random access test in FR1 for NR standalone for 1 Rx RedCap UE

A.20.2.2.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2C.2.2 and clause 7.1E.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.20.2.2.2.1.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.20.2.2.2.1.1-2.

Table A.20.2.2.2.1.1-1: Supported test configurations for contention based random access test for satellite access

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.2.2.1.1-2: General test parameters for contention based random access test for satellite access for 1 Rx RedCap UE

| Parameter |  |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- | --- |
| SSB Configuration |  | Config 1,3 |  | SSB pattern 1 in FR1 | As defined in A.3.10, except for number of SSBs per SS-burst and SS/PBCH block index as below |
|  |  | Config 2,4 |  | SSB pattern 2 in FR1 |  |
| Number of SSBs per SS-burst |  |  |  | 2 | Different from the definition in A.3.10 |
| SS/PBCH block index |  |  |  | 0,1 | Different from the definition in A.3.10 |
| Duplex Mode for Cell 1 |  | Config 1,3 |  | FDD |  |
|  |  | Config 2,4 |  | FDD |  |
| CSI-RS for tracking |  | Config 1, 2,3,4 |  | TRS.1.1 FDD |  |
| OCNG Pattern Note 1 |  |  |  | OP.1 | As defined in A.3.2.1. |
| PDSCH parameters Note 4 |  | Config 1, 2,3,4 |  | SR.1.1 FDD | As defined in A.3.1.1. |
| RMSI CORESET Reference Channel |  | Config 1, 2,3,4 |  | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1, 2,3,4 |  | CCR.1.1 FDD |  |
| NR RF Channel Number |  |  |  | 1 |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  | dB |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  | dB |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  | dB |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  | dB |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  | dB |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  | dB |  |  |
| SSB with index 0 | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 3 | Power of SSB with index 0 is set to be above configured rsrp-ThresholdSSB+1 |
|  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] | Config 1, 2,3,4 | dBm/15 kHz | -98 |  |
|  | ![](media_svg/image14.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 3 |  |
|  | SS-RSRP Note 3 |  | dBm/ SCS | -95 |  |
| SSB with index 1 | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | -17 | Power of SSB with index 1 is set to be below configured rsrp-ThresholdSSB +1dB |
|  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] | Config 1, 2,3,4 | dBm/15 kHz | -98 |  |
|  | ![](media_svg/image14.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | -17 |  |
|  | SS-RSRP Note 3 |  | dBm/ SCS | -115 |  |
| Io Note 2 |  | Config 1, 2,3,4 | dBm | -65.3/9.36 MHz | For symbols without SSB index 1 |
| ss-PBCH-BlockPower |  |  | dBm/ SCS | -5 | As defined in clause 6.3.2 in TS 38.331 [2]. |
| Configured UE transmitted power (![](media_svg/image21.svg) [公式≈: ^{P}CMAX,f,c]) |  |  | dBm | 23 | As defined in clause 6.2.4 in TS 38.101-1. |
| PRACH Configuration |  |  |  | FR1 PRACH configuration 1 | As defined in A.3.8. |
| Propagation Condition |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters.NOTE 3: VoidNOTE 4: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required. |  |  |  |  |  |

A.20.2.2.2.1.2 Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.20.2.2.2.1.2.1 Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2C.2.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB+1 dB.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.1.2.2 Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.1.2.3 No Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.1.2.4 Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2C.2.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

A.20.2.2.2.1.2.5 Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2C.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.20.2.2.2.1.2.6 Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2C.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.20.2.2.2.1.2.7 Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2C.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

##### A.20.2.2.2.2 4-step RA type contention based random access test in FR1 for NR standalone for 2 Rx RedCap UE

A.20.2.2.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2C.2.2 and clause 7.1E.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.20.2.2.2.2.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.20.2.2.2.2.1-2.

Table A.20.2.2.2.2.1-1: Supported test configurations for contention based random access test for satellite access

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.2.2.2.1-2: General test parameters for contention based random access test for satellite access

| Parameter |  |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- | --- |
| SSB Configuration |  | Config 1,3 |  | SSB pattern 1 in FR1 | As defined in A.3.10, except for number of SSBs per SS-burst and SS/PBCH block index as below |
|  |  | Config 2,4 |  | SSB pattern 2 in FR1 |  |
| Number of SSBs per SS-burst |  |  |  | 2 | Different from the definition in A.3.10 |
| SS/PBCH block index |  |  |  | 0,1 | Different from the definition in A.3.10 |
| Duplex Mode for Cell 1 |  | Config 1,3 |  | FDD |  |
|  |  | Config 2,4 |  | FDD |  |
| CSI-RS for tracking |  | Config 1, 2,3,4 |  | TRS.1.1 FDD |  |
| OCNG Pattern Note 1 |  |  |  | OP.1 | As defined in A.3.2.1. |
| PDSCH parameters Note 4 |  | Config 1, 2,3,4 |  | SR.1.1 FDD | As defined in A.3.1.1. |
| RMSI CORESET Reference Channel |  | Config 1, 2,3,4 |  | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1, 2,3,4 |  | CCR.1.1 FDD |  |
| NR RF Channel Number |  |  |  | 1 |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  | dB |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  | dB |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  | dB |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  | dB |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  | dB |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  | dB |  |  |
| SSB with index 0 | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 3 | Power of SSB with index 0 is set to be above configured rsrp-ThresholdSSB |
|  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] | Config 1, 2,3,4 | dBm/15 kHz | -98 |  |
|  | ![](media_svg/image14.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 3 |  |
|  | SS-RSRP Note 3 |  | dBm/ SCS | -95 |  |
| SSB with index 1 | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | -17 | Power of SSB with index 1 is set to be below configured rsrp-ThresholdSSB |
|  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] | Config 1, 2,3,4 | dBm/15 kHz | -98 |  |
|  | ![](media_svg/image14.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | -17 |  |
|  | SS-RSRP Note 3 |  | dBm/ SCS | -115 |  |
| Io Note 2 |  | Config 1, 2,3,4 | dBm | -65.3/9.36 MHz | For symbols without SSB index 1 |
| ss-PBCH-BlockPower |  |  | dBm/ SCS | -5 | As defined in clause 6.3.2 in TS 38.331 [2]. |
| Configured UE transmitted power (![](media_svg/image21.svg) [公式≈: ^{P}CMAX,f,c]) |  |  | dBm | 23 | As defined in clause 6.2.4 in TS 38.101-1. |
| PRACH Configuration |  |  |  | FR1 PRACH configuration 1 | As defined in A.3.8. |
| Propagation Condition |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters.NOTE 3: VoidNOTE 4: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required. |  |  |  |  |  |

A.20.2.2.2.2.2 Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.20.2.2.2.2.2.1 Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2C.2.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.2.2.2 Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.2.2.3 No Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.2.2.4 Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2C.2.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

A.20.2.2.2.2.2.5 Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2C.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.20.2.2.2.2.2.6 Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2C.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.20.2.2.2.2.2.7 Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2C.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

##### A.20.2.2.2.3 4-step RA type non-contention based random access test in FR1 for NR standalone for 1 Rx RedCap UE

A.20.2.2.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2C.2.2 and clause 7.1E.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.20.2.2.2.3.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.20.2.2.2.3.1-2 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2). Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

Table A.20.2.2.2.3.1-1: Supported test configurations for non-contention based random access test for satellite access

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.2.2.3.1-2: General test parameters for non-contention based random access test satellite access

| Parameter |  |  | Unit | Test-1 | Test-2 | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| SSB Configuration |  | Config 1,3 |  | SSB pattern 1 in FR1 | SSB pattern 1 in FR1 | As defined in A.3.10, except for number of SSBs per SS-burst and SS/PBCH block index as below |
|  |  | Config 2,4 |  | SSB pattern 2 in FR1 | SSB pattern 2 in FR1 |  |
| Number of SSBs per SS-burst |  |  |  | 2 | 2 | Different from the definition in A.3.10 |
| SS/PBCH block index |  |  |  | 0,1 | 0,1 | Different from the definition in A.3.10 |
| CSI-RS Configuration |  | Config 1, 2,3,4 |  | N/A | CSI-RS.1.1 FDD | As defined in A.3.1.4 |
| Duplex Mode for Cell 1 |  | Config 1, 2,3,4 |  | FDD | FDD |  |
| CSI-RS for tracking |  | Config 1, 2,3,4 |  | TRS.1.1 FDD | TRS.1.1 FDD |  |
| OCNG Pattern Note 1 |  |  |  | OP.1 | OP.1 | As defined in A.3.2.1. |
| PDSCH parameters Note 4 |  | Config 1, 2,3,4 |  | SR.1.1 FDD | SR.1.1 FDD | As defined in A.3.1.1. |
| RMSI CORESET Reference Channel |  | Config 1, 2,3,4 |  | CR.1.1 FDD | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1, 2,3,4 |  | CCR.1.1 FDD | CCR.1.1 FDD |  |
| NR RF Channel Number |  |  |  | 1 | 1 |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  | dB |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  | dB |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  | dB |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  | dB |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  | dB |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  | dB |  |  |  |
| SSB with index 0 | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 3 | 3 | Power of SSB with index 0 is set to be above configured rsrp-ThresholdSSB + [1] |
|  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] | Config 1, 2,3,4 | dBm/15 kHz | -98 | -98 |  |
|  | ![](media_svg/image14.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 3 | 3 |  |
|  | SS-RSRP Note 3 |  | dBm/ SCS | -95 | -95 |  |
| SSB with index 1 | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | -17 | -17 | Power of SSB with index 1 is set to be below configured rsrp-ThresholdSSB +1dB |
|  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] | Config 1, 2,3,4 | dBm/15 kHz | -98 | -98 |  |
|  | ![](media_svg/image14.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | -17 | -17 |  |
|  | SS-RSRP Note 3 |  | dBm/ SCS | -115 | -115 |  |
| Io Note 2 |  | Config 1, 2,3,4 | dBm | -65.3/9.36 MHz | -65.3/9.36 MHz | For symbols without SSB index 1 |
| ss-PBCH-BlockPower |  |  | dBm/ SCS | -5 | -5 | As defined in clause 6.3.2 in TS 38.331 [2]. |
| Configured UE transmitted power (![](media_svg/image21.svg) [公式≈: ^{P}CMAX,f,c]) |  |  | dBm | 23 | 23 | As defined in clause 6.2.4 in TS 38.101-1. |
| PRACH Configuration |  |  |  | FR1 PRACH configuration 2 | FR1 PRACH configuration 3 | As defined in A.3.8.2. |
| Propagation Condition |  |  | - | AWGN | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters.NOTE 3: VoidNOTE 4: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required. |  |  |  |  |  |  |

A.20.2.2.2.3.2 Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.20.2.2.2.3.2.1 SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2C.2.2.2.1 for SSB-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.3.2.2 CSI-RS-based Random Access Preamble Transmission

In Test-2, to test the UE behavior specified in clause 6.2C.2.2.2.1 for CSI-RS-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with CSI-RSs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the CSI-RS configured.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the CSI-RS configured, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-OccasionList.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.3.2.3 Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.3.2.4 No Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

##### A.20.2.2.2.4 4-step RA type non-contention based random access test in FR1 for NR standalone for 2 Rx RedCap UE

A.20.2.2.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2C.2.2 and clause 7.1E.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.20.2.2.2.4.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.20.2.2.2.4.1-2 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2). Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

Table A.20.2.2.2.4.1-1: Supported test configurations for non-contention based random access test for satellite access

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.2.2.4.1-2: General test parameters for non-contention based random access test satellite access

| Parameter |  |  | Unit | Test-1 | Test-2 | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| SSB Configuration |  | Config 1,3 |  | SSB pattern 1 in FR1 | SSB pattern 1 in FR1 | As defined in A.3.10, except for number of SSBs per SS-burst and SS/PBCH block index as below |
|  |  | Config 2,4 |  | SSB pattern 2 in FR1 | SSB pattern 2 in FR1 |  |
| Number of SSBs per SS-burst |  |  |  | 2 | 2 | Different from the definition in A.3.10 |
| SS/PBCH block index |  |  |  | 0,1 | 0,1 | Different from the definition in A.3.10 |
| CSI-RS Configuration |  | Config 1, 2,3,4 |  | N/A | CSI-RS.1.1 FDD | As defined in A.3.1.4 |
| Duplex Mode for Cell 1 |  | Config 1, 2,3,4 |  | FDD | FDD |  |
| CSI-RS for tracking |  | Config 1, 2,3,4 |  | TRS.1.1 FDD | TRS.1.1 FDD |  |
| OCNG Pattern Note 1 |  |  |  | OP.1 | OP.1 | As defined in A.3.2.1. |
| PDSCH parameters Note 4 |  | Config 1, 2,3,4 |  | SR.1.1 FDD | SR.1.1 FDD | As defined in A.3.1.1. |
| RMSI CORESET Reference Channel |  | Config 1, 2,3,4 |  | CR.1.1 FDD | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1, 2,3,4 |  | CCR.1.1 FDD | CCR.1.1 FDD |  |
| NR RF Channel Number |  |  |  | 1 | 1 |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  | dB |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  | dB |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  | dB |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  | dB |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  | dB |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  | dB |  |  |  |
| SSB with index 0 | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 3 | 3 | Power of SSB with index 0 is set to be above configured rsrp-ThresholdSSB |
|  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] | Config 1, 2,3,4 | dBm/15 kHz | -98 | -98 |  |
|  | ![](media_svg/image14.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 3 | 3 |  |
|  | SS-RSRP Note 3 |  | dBm/ SCS | -95 | -95 |  |
| SSB with index 1 | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | -17 | -17 | Power of SSB with index 1 is set to be below configured rsrp-ThresholdSSB |
|  | ![](media_svg/image2.svg) [公式≈: ^{N}oc] | Config 1, 2,3,4 | dBm/15 kHz | -98 | -98 |  |
|  | ![](media_svg/image14.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | -17 | -17 |  |
|  | SS-RSRP Note 3 |  | dBm/ SCS | -115 | -115 |  |
| Io Note 2 |  | Config 1, 2,3,4 | dBm | -65.3/9.36 MHz | -65.3/9.36 MHz | For symbols without SSB index 1 |
| ss-PBCH-BlockPower |  |  | dBm/ SCS | -5 | -5 | As defined in clause 6.3.2 in TS 38.331 [2]. |
| Configured UE transmitted power (![](media_svg/image21.svg) [公式≈: ^{P}CMAX,f,c]) |  |  | dBm | 23 | 23 | As defined in clause 6.2.4 in TS 38.101-1. |
| PRACH Configuration |  |  |  | FR1 PRACH configuration 2 | FR1 PRACH configuration 3 | As defined in A.3.8.2. |
| Propagation Condition |  |  | - | AWGN | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters.NOTE 3: VoidNOTE 4: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required. |  |  |  |  |  |  |

A.20.2.2.2.4.2 Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.20.2.2.2.4.2.1 SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2C.2.2.2.1 for SSB-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.4.2.2 CSI-RS-based Random Access Preamble Transmission

In Test-2, to test the UE behavior specified in clause 6.2C.2.2.2.1 for CSI-RS-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with CSI-RSs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the CSI-RS configured.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the CSI-RS configured, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-OccasionList.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.4.2.3 Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.4.2.4 No Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

#### A.20.2.2.3 RRC Connection Release with Redirection

##### A.20.2.2.3.1 Redirection from NR in FR1 to NR in FR1 for 1 Rx RedCap UE

A.20.2.2.3.1.1 Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements specified in clause 6.2E.3.2.1.

A.20.2.2.3.1.2 Test Parameters

Supported test configurations are shown in table A.20.2.2.3.1.2-1. The time delay is tested by using the parameters in table A.20.2.2.3.1.2-2, and A.20.2.2.3.1.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2. Cell 1 and Cell 2 belong to different tracking areas.

Table A.20.2.2.3.1.2-1: Redirection from NR to NR test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.2.3.1.2-2: General test parameters for Redirection from NR to NR test case

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 |  |
| Final condition | Active cell |  | Cell 2 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 2.3 |  |

Table A.20.2.2.3.1.2-3: Cell specific test parameters for Redirection from NR to NR test case

| Parameter |  |  | Unit | Cell 1 |  |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 |  | T2 |  | T1 |  | T2 |
| Satellite information |  |  | Config 1,3 |  |  |  |  | SSC.1 |  |  |
|  |  |  | Config 2,4 |  |  |  |  | SSC.2 |  |  |
| NR RF Channel Number |  |  |  | 1 |  |  |  | 2 |  |  |
| Duplex mode |  | Config 1, 2,3,4 |  | FDD |  |  |  |  |  |  |
| SSB Configuration |  | Config 1, 2,3,4 |  | SSB.1 FR1 |  |  |  |  |  |  |
| CSI-RS for tracking |  | Config 1, 2,3,4 |  | TRS.1.1 FDD |  |  |  |  |  |  |
| BWchannel |  | Config 1,3 | MHz | 10: NRB,c = 52 |  |  |  |  |  |  |
|  |  | Config 2,4 |  | 10: NRB,c = 52 |  |  |  |  |  |  |
| BWP BW |  | Config 1,3 | MHz | 10: NRB,c = 52 |  |  |  |  |  |  |
|  |  | Config 2,4 |  | 10: NRB,c = 52 |  |  |  |  |  |  |
| DRx Cycle |  |  | ms | Not Applicable |  |  |  |  |  |  |
| PDSCH Reference measurement channel |  | Config 1, 2,3,4 |  | SR.1.1 FDD |  |  |  |  |  |  |
| CORESET Reference Channel |  | Config 1, 2,3,4 |  | CR.1.1 FDD |  |  |  |  |  |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |  |  |  |
| SMTC configuration |  | Config 1,2,3,4 |  | SMTC.1 FR1 |  |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2,3,4 | kHz | 15 kHz |  |  |  |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1,2,3,4 | kHz | 15 kHz |  |  |  |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 |  |  |  |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15kHz | -98 |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 |  | dBm/SCS | -98 |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 4 | 4 |  | -infinity |  | 4 |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4 | 4 |  | -infinity |  | 4 |  |
| IoNote3 | Config 1,2,3,4 |  | dBm/9.36MHz | -64.59 | -64.59 |  | -70.05 |  | -64.59 |  |
| Propagation condition |  |  | - | AWGN |  |  |  |  |  |  |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.Note 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.Note 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |  |  |

A.20.2.2.3.1.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2240 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE: The redirection delay can be expressed as:

Tconnection_release_redirect_NR = TRRC_procedure_delay + Tidentify-NR + TSI-NR + TRACH,

Where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR = 680 ms in the test.

TSI-NR = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH = 170 ms in the test.

This gives a total of 2240 ms.

##### A.20.2.2.3.2 Redirection from NR in FR1 to NR in FR1 for 2 Rx RedCap UE

A.20.2.2.3.2.1 Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements specified in clause 6.2E.3.2.1.

A.20.2.2.3.2.2 Test Parameters

Supported test configurations are shown in table A.20.2.2.3.2.2-1. The time delay is tested by using the parameters in table A.20.2.2.3.2.2-2, and A.20.2.2.3.2.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2. Cell 1 and Cell 2 belong to different tracking areas.

Table A.20.2.2.3.2.2-1: Redirection from NR to NR test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.2.3.2.2-2: General test parameters for Redirection from NR to NR test case

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 |  |
| Final condition | Active cell |  | Cell 2 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 2.3 |  |

Table A.20.2.2.3.2.2-3: Cell specific test parameters for Redirection from NR to NR test case

| Parameter |  |  | Unit | Cell 1 |  |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 |  | T2 |  | T1 |  | T2 |
| Satellite information |  |  | Config 1,3 |  |  |  |  | SSC.1 |  |  |
|  |  |  | Config 2,4 |  |  |  |  | SSC.2 |  |  |
| NR RF Channel Number |  |  |  | 1 |  |  |  | 2 |  |  |
| Duplex mode |  | Config 1, 2,3,4 |  | FDD |  |  |  |  |  |  |
| SSB Configuration |  | Config 1, 2,3,4 |  | SSB.1 FR1 |  |  |  |  |  |  |
| CSI-RS for tracking |  | Config 1, 2,3,4 |  | TRS.1.1 FDD |  |  |  |  |  |  |
| BWchannel |  | Config 1,3 | MHz | 10: NRB,c = 52 |  |  |  |  |  |  |
|  |  | Config 2,4 |  | 10: NRB,c = 52 |  |  |  |  |  |  |
| BWP BW |  | Config 1,3 | MHz | 10: NRB,c = 52 |  |  |  |  |  |  |
|  |  | Config 2,4 |  | 10: NRB,c = 52 |  |  |  |  |  |  |
| DRx Cycle |  |  | ms | Not Applicable |  |  |  |  |  |  |
| PDSCH Reference measurement channel |  | Config 1, 2,3,4 |  | SR.1.1 FDD |  |  |  |  |  |  |
| CORESET Reference Channel |  | Config 1, 2,3,4 |  | CR.1.1 FDD |  |  |  |  |  |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |  |  |  |
| SMTC configuration |  | Config 1,2,3,4 |  | SMTC.1 FR1 |  |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2,3,4 | kHz | 15 kHz |  |  |  |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1,2,3,4 | kHz | 15 kHz |  |  |  |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 |  |  |  |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15kHz | -98 |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 |  | dBm/SCS | -98 |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 4 | 4 |  | -infinity |  | 4 |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4 | 4 |  | -infinity |  | 4 |  |
| IoNote3 | Config 1,2,3,4 |  | dBm/9.36MHz | -64.59 | -64.59 |  | -70.05 |  | -64.59 |  |
| Propagation condition |  |  | - | AWGN |  |  |  |  |  |  |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.Note 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.Note 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |  |  |

A.20.2.2.3.2.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2240 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE: The redirection delay can be expressed as:

Tconnection_release_redirect_NR = TRRC_procedure_delay + Tidentify-NR + TSI-NR + TRACH,

Where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR = 680 ms in the test.

TSI-NR = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH = 170 ms in the test.

This gives a total of 2240 ms.

### A.20.2.3 Satellite switching with re-synchronization from FR1 to FR1 for RedCap UE with Satellite Access

#### A.20.2.3.1 RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 for RedCap UEs with 2Rx RedCap UE

##### A.20.2.3.1.1 Test Purpose and Environment

This test is to verify the requirement for RACH-based hard satellite switching with re-synchronization from SAN FR1 to SAN FR1 for RedCap UEs, which is specified in clause 6.1F.3. The test is applicable for UEs that support RedCap operation in NTN. The test procedure is applicable for UEs supporting 2 Rx Antenna.

##### A.20.2.3.1.2 Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells with same PCI as given in table A.20.2.3.1.2-1, A.20.2.3.1.2-2, A.20.2.3.1.2-3 and A.20.2.3.1.2-4. Both satellite switching delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively.

At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, The SIB19 implying t-service-r17 and target satellite configuration SatSwitchWithReSync-r18 shall be sent to UE. The target satellite configuration is in table A.20.2.3.1.2-3.

At the start of time duration T2, Cell 2 becomes detectable and t-service-r17 of Cell 1 is fulfilled.

Table A.20.2.3.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.3.1.2-2: General test parameters for RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 | One NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 |  |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) |  |  | (0, 0, 0) | Set by any pre-configured means(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| Access Barring Information |  | - | Not barred | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |

Table A.20.2.3.1.2-3: Target Satellite configuration pattern for hard satellite switching scenario

| Parameter | TSC.1 |
| --- | --- |
| Interval between adjacent epoch time | 2.56 s |
| ntn-UlSyncValidityDuration | 5 s |
| cellSpecificKoffset | 14 slots |
| ta-Common | 0 |
| ta-CommonDrift | 0 |
| ta-CommonDriftVariant | 0 |
| ntn-PolarizationDL | linear |
| ntn-PolarizationUL | linear |
| ephemerisInfo | Detailed ephemeris information is provided in TS 38.508-1 [38] |
| ssb-TimeOffset | 0 |

Table A.20.2.3.1.2-4: Cell specific test parameters for RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 test case

| Parameter |  | Unit | Cell 1Note1 |  | Cell 2Note1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite configurationNote2 |  |  | SSC.2 | N/A | N/A | SSC.2 |
| BWchannel |  | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |
| BWP BW |  | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |
| Kmac |  | ms | 0 |  |  | 0 |
| DRX Cycle |  | ms | Not Applicable |  |  | Not Applicable |
| PDSCH Reference measurement channel |  |  | SR.1.1 FDD |  |  | SR.1.1 FDD |
| CORESET Reference Channel |  |  | CR.1.1 FDD |  |  | CR.1.1 FDD |
| TRS configuration |  |  | TRS.1.1 FDD |  |  | TRS.1.1 FDD |
| OCNG Patterns |  |  | OP.1 |  |  | OP.1 |
| SMTC Configuration |  |  | SMTC.2 |  |  | SMTC.2 |
| SSB Configuration |  |  | SSB.4 Redcap FR1 |  |  | SSB.4 Redcap FR1 |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 15 kHz |  |  | 15 kHz |
| PUCCH/PUSCH subcarrier spacing |  | kHz | 15 kHz |  |  | 15 kHz |
| PRACH configuration |  |  | FR1 PRACH configuration 1 |  |  | FR1 PRACH configuration 1 |
| BWP configuration | Initial DL BWP |  | DLBWP.0.1 |  |  | DLBWP.0.1 |
|  | Dedicated DL BWP |  | DLBWP.1.1 |  |  | DLBWP.1.1 |
|  | Initial UL BWP |  | ULBWP.0.1 |  |  | ULBWP.0.1 |
|  | Dedicated UL BWP |  | ULBWP.1.1 |  |  | ULBWP.1.1 |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |  | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |
| ![](media_svg/image22.svg) [公式≈: ^{N}oc]Note3 |  | dBm/ 15 kHz | -98 |  |  |  |
| ![](media_svg/image22.svg) [公式≈: ^{N}oc]Note3 |  | dBm/ SCS | -98 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 8 | -Infinity | -Infinity | 8 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 8 | -Infinity | -Infinity | 8 |
| SSB_RP |  | dBm/ SCS | -90 | -Infinity | -Infinity | -90 |
| IoNote4 |  | dBm/ 9.36 MHz | -61.41 | -61.41 | -61.41 | -61.41 |
| Propagation condition |  | - | AWGN |  |  |  |
| NOTE 1: Cell 1 and Cell 2 have same PCI. Satellite serving for Cell 1 and Satellite serving for Cell 2 are two different NGSO satellites.NOTE 2: SSB transmit timing from TE should fit the SSB-timeOffset and the nominal propagation delay difference between serving satellite and target satellite. The nominal propagation delay is counted from the SSB-TimeOffset reference point to UE, which based on satellite locations and UE location known to the TE in this test case.NOTE 3: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image22.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 4: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 5: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all ,OFDM symbols. |  |  |  |  |  |  |

##### A.20.2.3.1.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 52.5 ms from the beginning of time period T2.

The rate of correct satellite switch observed during repeated tests shall be at least 90 %.

NOTE: The hard satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tinterrupt, where:

Tinterrupt is defined in clause 6.1C.3.2.2.

Dswitch_unchangedPCI = Tinterrupt = Tsearch + Tprocessing  + T∆ + Tmargin ms

Here: Tprocessing = 10ms; T∆ = 20ms; Tmargin = 2ms. And Tsearch is equal to Tfirst_SSB = 10.5ms, for UEs with 2Rx;

Besides, interruption uncertainty TIU = 20ms in acquiring the first PRACH transmission resource is needed.

This gives a total of 42.5 ms.

#### A.20.2.3.2 RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 for RedCap UEs with 1 Rx RedCap UE

##### A.20.2.3.2.1 Test Purpose and Environment

This test is to verify the requirement for RACH-based hard satellite switching with re-synchronization from SAN FR1 to SAN FR1 for RedCap UEs, which is specified in clause 6.1F.3. The test is applicable for UEs that support RedCap operation in NTN. The test procedure is applicable for UEs supporting 1 Rx Antenna.

##### A.20.2.3.2.2 Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells with same PCI as given in tables A.20.2.3.2.2-1, A.20.2.3.2.2-2, A.20.2.3.2.2-3 and A.20.2.3.2.2-4. Both satellite switching delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively.

At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, The SIB19 implying t-service-r17 and target satellite configuration SatSwitchWithReSync-r18 shall be sent to UE. The target satellite configuration is in table A.20.2.3.2.2-3.

At the start of time duration T2, Cell 2 becomes detectable and t-service-r17 of Cell 1 is fulfilled.

Table A.20.2.3.2.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.3.2.2-2: General test parameters for RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 | One NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 |  |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) |  |  | (0, 0, 0) | Set by any pre-configured means(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| Access Barring Information |  | - | Not barred | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |

Table A.20.2.3.2.2-3: Target Satellite configuration pattern for hard satellite switching scenario

| Parameter | TSC.1 |
| --- | --- |
| Interval between adjacent epoch time | 2.56 s |
| ntn-UlSyncValidityDuration | 5 s |
| cellSpecificKoffset | 14 slots |
| ta-Common | 0 |
| ta-CommonDrift | 0 |
| ta-CommonDriftVariant | 0 |
| ntn-PolarizationDL | linear |
| ntn-PolarizationUL | linear |
| ephemerisInfo | Detailed ephemeris information is provided in TS 38.508-1 [38] |
| ssb-TimeOffset | 0 |

Table A.20.2.3.2.2-4: Cell specific test parameters for RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 test case

| Parameter |  | Unit | Cell 1Note1 |  | Cell 2Note1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite configurationNote2 |  |  | SSC.2 | N/A | N/A | SSC.2 |
| BWchannel |  | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |
| BWP BW |  | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |
| Kmac |  | ms | 0 |  |  | 0 |
| DRX Cycle |  | ms | Not Applicable |  |  | Not Applicable |
| PDSCH Reference measurement channel |  |  | SR.1.1 FDD |  |  | SR.1.1 FDD |
| CORESET Reference Channel |  |  | CR.1.1 FDD |  |  | CR.1.1 FDD |
| TRS configuration |  |  | TRS.1.1 FDD |  |  | TRS.1.1 FDD |
| OCNG Patterns |  |  | OP.1 |  |  | OP.1 |
| SMTC Configuration |  |  | SMTC.2 |  |  | SMTC.2 |
| SSB Configuration |  |  | SSB.4 Redcap FR1 |  |  | SSB.4 Redcap FR1 |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 15 kHz |  |  | 15 kHz |
| PUCCH/PUSCH subcarrier spacing |  | kHz | 15 kHz |  |  | 15 kHz |
| PRACH configuration |  |  | FR1 PRACH configuration 1 |  |  | FR1 PRACH configuration 1 |
| BWP configuration | Initial DL BWP |  | DLBWP.0.1 |  |  | DLBWP.0.1 |
|  | Dedicated DL BWP |  | DLBWP.1.1 |  |  | DLBWP.1.1 |
|  | Initial UL BWP |  | ULBWP.0.1 |  |  | ULBWP.0.1 |
|  | Dedicated UL BWP |  | ULBWP.1.1 |  |  | ULBWP.1.1 |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |  | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |
| ![](media_svg/image22.svg) [公式≈: ^{N}oc]Note3 |  | dBm/ 15 kHz | -98 |  |  |  |
| ![](media_svg/image22.svg) [公式≈: ^{N}oc]Note3 |  | dBm/ SCS | -98 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 8 | -Infinity | -Infinity | 8 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 8 | -Infinity | -Infinity | 8 |
| SSB_RP |  | dBm/ SCS | -90 | -Infinity | -Infinity | -90 |
| IoNote4 |  | dBm/ 9.36 MHz | -61.41 | -61.41 | -61.41 | -61.41 |
| Propagation condition |  | - | AWGN |  |  |  |
| NOTE 1: Cell 1 and Cell 2 have same PCI. Satellite serving for Cell 1 and Satellite serving for Cell 2 are two different NGSO satellites.NOTE 2: SSB transmit timing from TE should fit the SSB-timeOffset and the nominal propagation delay difference between serving satellite and target satellite. The nominal propagation delay is counted from the SSB-TimeOffset reference point to UE, which based on satellite locations and UE location known to the TE in this test case.NOTE 3: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image22.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 4: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 5: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all ,OFDM symbols. |  |  |  |  |  |  |

##### A.20.2.3.2.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 52.5 ms from the beginning of time period T2.

The rate of correct satellite switch observed during repeated tests shall be at least 90 %.

NOTE: The hard satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tinterrupt, where:

Tinterrupt is defined in clause 6.1C.3.2.2.

Dswitch_unchangedPCI = Tinterrupt = Tsearch + Tprocessing  + T∆ + Tmargin ms

Here: Tprocessing = 10ms; T∆ = 20ms; Tmargin = 2ms. And Tsearch is equal to 2*Trs = 40 ms, for UEs with 1 Rx;

Besides, interruption uncertainty TIU = 20ms in acquiring the first PRACH transmission resource is needed.

This gives a total of 72 ms.

#### A.20.2.3.3 RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1 for 2Rx RedCap UEs

##### A.20.2.3.3.1 Test Purpose and Environment

This test is to verify the requirement for RACH-less soft satellite switching with re-synchronization from SAN FR1 to SAN FR1 for RedCap UEs which is specified in clause 6.1F.3. The test is applicable for UEs that support RedCap operation in NTN. The test procedure is applicable for UEs supporting 2 Rx Antenna. The requirements to be met depend on the number of supported Rx Antenna at UE side.

##### A.20.2.3.3.2 Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells with same PCI as given in tables A.20.2.3.3.2-1, A.20.2.3.3.2-2, A.20.2.3.3.2-3 and A.20.2.3.3.2-4. Satellite switching delay is tested.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively.

At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, The SIB19 implying t-service-r17 and target satellite configuration SatSwitchWithReSync-r18 shall be sent to UE. The target satellite configuration is in table A.20.2.3.3.2-3. The configured grant PUSCH transmission in the Cell 2 is configured in the RRC message from Cell 1.

At the start of time duration T2, Cell 2 becomes detectable and t-ServiceStart-r18 is fulfilled.

At the start of time duration T3, t-service-r17 of Cell 1 is fulfilled.

Table A.20.2.3.3.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.2.3.3.2-2: General test parameters for RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 | One NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 |  |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) |  |  | (0, 0, 0) | Set by any pre-configured means(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| Access Barring Information |  | - | Not barred | No additional delays in random access procedure. |
| timeDomainOffset |  |  | 0 |  |
| timeDomainAllocation |  |  | 0 | PUSCH MappingType AstartSymbol S=0Length L=14 |
| timeReferenceSFN-r16 |  |  | sfn512 |  |
| Periodcity |  |  | sym10x14 |  |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | ms | 100 |  |
| T3 |  | s | 5 |  |

Table A.20.2.3.3.2-3: Target Satellite configuration pattern for soft satellite switching scenario

| Parameter | TSC.2 |
| --- | --- |
| Interval between adjacent epoch time | 2.56 s |
| ntn-UlSyncValidityDuration | 5 s |
| cellSpecificKoffset | 14 slots |
| ta-Common | 0 |
| ta-CommonDrift | 0 |
| ta-CommonDriftVariant | 0 |
| ntn-PolarizationDL | linear |
| ntn-PolarizationUL | linear |
| ephemerisInfo | Detailed ephemeris information is provided in TS 38.508-1 [38] |
| ssb-TimeOffset | 10 |
| t-ServiceStart | T2 |

Table A.20.2.3.3.2-4: Cell specific test parameters for Inter frequency SAN handover test case

| Parameter |  | Unit | Cell 1Note1 |  |  | Cell 2Note1 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite configurationNote2 |  |  | SSC.2 |  | N/A | N/A | SSC.2 |  |
| BWchannel |  | MHz | 10: NPRB,c = 52 |  |  |  | 10: NPRB,c = 52 |  |
| BWP BW |  | MHz | 10: NPRB,c = 52 |  |  |  | 10: NPRB,c = 52 |  |
| Kmac |  | ms | 0 |  |  |  | 0 |  |
| DRX Cycle |  | ms | Not Applicable |  |  |  | Not Applicable |  |
| PDSCH Reference measurement channel |  |  | SR.1.1 FDD |  |  |  | SR.1.1 FDD |  |
| CORESET Reference Channel |  |  | CR.1.1 FDD |  |  |  | CR.1.1 FDD |  |
| TRS configuration |  |  | TRS.1.1 FDD |  |  |  | TRS.1.1 FDD |  |
| OCNG Patterns |  |  | OP.1 |  |  |  | OP.1 |  |
| SMTC Configuration |  |  | SMTC.2 |  |  |  | SMTC.2 |  |
| SSB Configuration |  |  | SSB.4 Redcap FR1 |  |  |  | SSB.4 Redcap FR1 |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 15 kHz |  |  |  | 15 kHz |  |
| PUCCH/PUSCH subcarrier spacing |  | kHz | 15 kHz |  |  |  | 15 kHz |  |
| PRACH configuration |  |  | FR1 PRACH configuration 1 |  |  |  | FR1 PRACH configuration 1 |  |
| BWP configuration | Initial DL BWP | DLBWP.0.1 | DLBWP.0.1 |  |  | DLBWP.0.1 | DLBWP.0.1 |  |
|  | Dedicated DL BWP | DLBWP.1.1 | DLBWP.1.1 |  |  | DLBWP.1.1 | DLBWP.1.1 |  |
|  | Initial UL BWP | ULBWP.0.1 | ULBWP.0.1 |  |  | ULBWP.0.1 | ULBWP.0.1 |  |
|  | Dedicated UL BWP | ULBWP.1.1 | ULBWP.1.1 |  |  | ULBWP.1.1 | ULBWP.1.1 |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |  |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image22.svg) [公式≈: ^{N}oc]Note2 |  | dBm/ 15 kHz | -98 |  |  |  |  |  |
| ![](media_svg/image22.svg) [公式≈: ^{N}oc]Note2 |  | dBm/ SCS | -98 |  |  |  |  |  |
| ![](media_svg/image23.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 4 | 4 | -Infinity | -Infinity | 9 | 9 |
| ![](media_svg/image24.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 4 | 4 | -Infinity | -Infinity | 9 | 9 |
| SSB_RP |  | dBm/ SCS | -94 | -94 | -Infinity | -Infinity | -89 | -89 |
| IoNote3 |  | dBm/ 9.36 MHz | -64.59 | -64.59 | -70.05 | -70.05 | -60.53 | -60.53 |
| Propagation condition |  | - | AWGN |  |  |  |  |  |
| NOTE 1: Cell 1 and Cell 2 have same PCI. Satellite serving for Cell 1 and Satellite serving for Cell 2 are two different NGSO satellites.NOTE 2: SSB transmit timing from TE should fit the SSB-timeOffset and the nominal propagation delay difference between serving satellite and target satellite. The nominal propagation delay is counted from the SSB-TimeOffset reference point to UE, which based on satellite locations and UE location known to the TE in this test case.NOTE 3: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image22.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 4: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 5: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |  |  |  |  |  |

##### A.20.2.3.3.3 Test Requirements

The UE shall start to transmit the PUSCH to Cell 2 less than 130 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tsoft_switch, where:

Tsoft_switch = max(t-service-t-seviceStart, Tsearch + T∆ + Tmargin) + TIU + Tprocessing  ms

Here: t-service-t-seviceStart= 100ms; Tsearch = 10.5ms; T∆ = 20ms; Tmargin = 2ms, Tprocessing = 10ms.

Besides, interruption uncertainty TIU = 20ms in acquiring the first configured grant based PUSCH transmission resource is needed.

This gives a total of 130 ms.

#### A.20.2.3.4 RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1 for 1Rx RedCap UEs

##### A.20.2.3.4.1 Test Purpose and Environment

This test is to verify the requirement for RACH-less soft satellite switching with re-synchronization from SAN FR1 to SAN FR1 for RedCap UEs which is specified in clause 6.1F.3. The test is applicable for UEs that support RedCap operation in NTN. The test procedure is applicable for UEs supporting 1 Rx Antenna. The requirements to be met depend on the number of supported Rx Antenna at UE side.

##### A.20.2.3.4.2 Test Parameters

The test parameters defined in A.20.2.3.3.2 for 2Rx RedCap UE shall apply for 1Rx RedCap UE.

##### A.20.2.3.4.3 Test Requirements

The test requirements defined in A.20.2.3.3.3 for 2Rx RedCap UE shall apply for 1Rx RedCap UE.

## A.20.3 Timing for RedCap UE with Satellite Access

### A.20.3.1 UE transmit timing for RedCap UE with Satellite Access

#### A.20.3.1.1 NR UE Transmit Timing Test for FR1

##### A.20.3.1.1.1 Test Purpose and environment

Test purpose and environment in clause A.14.3.1.1.1 apply for RedCap UE except that:

- Table A.14.3.1.1.1-1 is replaced with A.20.3.1.1.1-1, and,

- Table A.14.3.1.1.1-2 is replaced with A.20.3.1.1.1-2.

Table A.20.3.1.1.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.3.1.1.1-2: Cell Specific Test Parameters for UL Transmit Timing test

| Parameter | Unit | Config | Test1 | Test2 |
| --- | --- | --- | --- | --- |
| SSB ARFCN |  | 1,2,3,4 | 1 | 1 |
| Serving satellite configuration |  | 1,3 | SSC.1 |  |
|  |  | 2,4 | SSC.2 |  |
| BWchannel | MHz | 1,2,3,4 | 10: NPRB,c = 52 |  |
| Initial BWP Configuration |  | 1,2,3,4 | DLBWP.0.1ULBWP.0.1 |  |
| Dedicated BWP Configuration |  | 1,2,3,4 | DLBWP.1.1ULBWP.1.1 |  |
| DRX Cycle | ms | 1,2,3,4 | N/A | DRX.8Note5 |
| PDSCH Reference measurement channel |  | 1,2,3,4 | SR.1.1 FDD |  |
| RMSI CORESET Reference Channel |  | 1,2,3,4 | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | 1,2,3,4 | CCR.1.1 FDD |  |
| OCNG Patterns |  | 1,2,3,4 | OP.1 |  |
| SSB configuration |  | 1,2,3,4 | SSB.1 FR1 |  |
| SMTC Configuration |  | 1,2,3,4 | SMTC.1 FR1 |  |
| TRS configuration |  | 1,2,3,4 | TRS.1.1 FDD |  |
| EPRE ratio of PSS to SSS | dB | 1,2,3,4 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1,2,3,4 | -98 | -98 |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1,2,3,4 | -98 | -98 |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  | 1,2,3,4 | 3 | 3 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | 1,2,3,4 | 3 | 3 |
| SS-RSRPNote3 | dBm/SCS | 1,2,3,4 | -95 | -95 |
| IoNote3 | dBm/9.36 MHz | 1,2,3,4 | -65.2 | -65.2 |
| Propagation condition |  | 1,2,3,4 | AWGN |  |
| SRS Config |  | 1,2,3,4 | SRSConf.1Note6 | SRSConf.2Note6 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: DRX related parameters are given in table A.3.3.8-1NOTE 6: SRS configs are given in table A.14.3.1.1.1-3 |  |  |  |  |

##### A.20.3.1.1.2 Test requirements

Test requirements in clause A.14.3.1.1.2 apply for RedCap UEs.

### A.20.3.2 Timing advance for RedCap UE with Satellite Access

#### A.20.3.2.1 SA FR1 timing advance adjustment accuracy for RedCap UE

##### A.20.3.2.1.1 Test Purpose and Environment

The test purpose and environment in clause A.14.3.2.1.1 shall apply for RedCap UE.

##### A.20.3.2.1.2 Test Parameters

The test parameters in clause A.14.3.2.1.2 shall apply for RedCap UE except that:

- Table A.14.3.2.1.2-1 is replaced with A.20.3.2.1.2-1, and,

- Table A.14.3.2.1.2-3 is replaced with A.20.3.2.1.2-2, and,

- Table A.14.3.2.1.2-4 is replaced with A.20.3.2.1.2-3,

- Table A.14.3.2.1.2-2 shall apply to configurations 1, 2, 3 and 4.

Table A.20.3.2.1.2-1: Timing advance supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.3.2.1.2-2: Cell specific test parameters for timing advance

| Parameter |  |  | Unit | Test1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 |
| Duplex mode |  | Config 1,2,3,4 |  | FDD |  |
| Satellite information |  | Config 1,3 |  | SSC.1 |  |
|  |  | Config 2,4 |  | SSC.2 |  |
| BWchannel |  | Config 1,2,3,4 | MHz | 10: NPRB,c = 52 |  |
| BWP BW |  | Config 1,2,3,4 | MHz | 10: NPRB,c = 52 |  |
| DRX Cycle |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  | Config 1,2,3,4 |  | SR.1.1 FDD |  |
| RMSI CORESET Reference Channel |  | Config 1,2,3,4 |  | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1,2,3,4 |  | CCR.1.1 FDD |  |
| TRS configuration |  | Config 1,2,3,4 |  | TRS.1.1 FDD |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |
| SMTC configuration |  | Config 1,2,3,4 |  | SMTC.1 FR1 |  |
| SSB configuration |  | Config 1,2,3,4 |  | SSB.1 FR1 |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2,3,4 | kHz | 15 kHz |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1,2,3,4 | kHz | 15 kHz |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 |  | dBm/SCS | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 3 |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 |  |
| IoNote3 | Config 1,2,3,4 |  | dBm/9.36 MHz | -67.57 |  |
| Propagation condition |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |

Table A.20.3.2.1.2-3: Sounding Reference Symbol Configuration for timing advance

| Field |  | Value | Comment |
| --- | --- | --- | --- |
| c-SRS | Config 1,2,3,4 | 12 | Frequency hopping is disabled |
| b-SRS |  | 0 |  |
| b-hop |  | 0 |  |
| freqDomainPosition |  | 0 | Frequency domain position of SRS |
| freqDomainShift |  | 0 |  |
| groupOrSequenceHopping |  | neither | No group or sequence hopping |
| SRS-PeriodicityAndOffset |  | sl5=2 for SCS 15 kHz | Once every 5 slots |
| pathlossReferenceRS |  | ssb-Index=0 | SSB #0 is used for SRS path loss estimation |
| usage |  | Codebook | Codebook based UL transmission |
| startPosition |  | 0 | resourceMapping setting. SRS on last symbol of slot, and 1 symbols for SRS without repetition. |
| nrofSymbols |  | n1 |  |
| repetitionFactor |  | n1 |  |
| combOffset-n2 |  | 0 | transmissionComb setting |
| cyclicShift-n2 |  | 0 |  |
| nrofSRS-Ports |  | port1 | Number of antenna ports used for SRS transmission |
| NOTE: For further information see clause 6.3.2 in TS 38.331 [2]. |  |  |  |

##### A.20.3.2.1.3 Test Requirements

Test requirements in clause A.14.3.2.1.3 apply for RedCap UEs with NTN.

## A.20.4 Signalling characteristics for RedCap UE with Satellite Access

### A.20.4.1 Radio link Monitoring

#### A.20.4.1.1 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode for 2Rx RedCap UE with NTN

##### A.20.4.1.1.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.1.1 shall apply for 2Rx RedCap UE except that:

- Table A.14.4.1.1.1-1 is replaced with A.20.4.1.1.1-1, and

- Table A.14.4.1.1.1-2, Table A.14.4.1.1.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.4.1.1.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.4.1.1.2 Test Requirements

The test requirement in clause A.14.4.1.1.2 shall apply for RedCap.

#### A.20.4.1.2 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode for 1Rx RedCap UE with NTN

##### A.20.4.1.2.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.1.1 shall apply for 1Rx RedCap UE except that:

- Table A.14.4.1.1.1-1 is replaced with A.20.4.1.1.1-1, and

- Table A.14.4.1.1.1-2 is replaced with A.20.4.1.2.1-1, and

- Table A.14.4.1.1.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.4.1.2.1-1: General test parameters for FR1 out-of-sync testing in non-DRX mode for 1Rx RedCap UE

| Parameter |  |  | Unit | Value |
| --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |
| Active PCell |  |  |  | Cell 1 |
| RF Channel Number |  |  |  | 1 |
| BWchannel |  | Config 1, 2, 3, 4 | MHz | 10: NPRB,c = 52 |
| DL initial BWP configuration |  | Config 1, 2, 3, 4 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  | Config 1, 2, 3, 4 |  | DLBWP.1.1 |
| UL initial BWP configuration |  | Config 1, 2, 3, 4 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  | Config 1, 2, 3, 4 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel |  | Config 1, 2, 3, 4 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel |  | Config 1, 2, 3, 4 |  | CCR.3.2 FDD |
| SSB Configuration |  | Config 1, 2, 3, 4 |  | SSB.1 FR1 |
| SMTC Configuration |  | Config 1, 2, 3, 4 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2, 3, 4 |  | 15 kHz |
| PRACH Configuration |  | Config 1, 2, 3, 4 |  | Table  A.3.8.2.1-1 |
| SSB index assigned as RLM RS |  |  |  | 0 |
| OCNG parameters |  |  |  | OP.1 |
| CP length |  |  |  | Normal |
| Correlation Matrix and Antenna Configuration |  |  |  | 2x1 Low |
| Out of sync transmission parameters | DCI format |  |  | 1-0 |
|  | Number of Control OFDM symbols |  |  | 2 |
|  | Aggregation level |  | CCE | 16 |
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
| CSI-RS configuration for CSI reporting |  | Config 1, 2, 3, 4 |  | CSI-RS.1.1 FDD |
| CSI-RS for tracking |  | Config 1, 2, 3, 4 |  | TRS.1.1 FDD |
| T1 |  |  | s | 0.2 |
| T2 |  |  | s | 0.88 |
| T3 |  |  | s | 0.88 |
| D1 |  |  | s | 0.84 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |

##### A.20.4.1.2.2 Test Requirements

The test requirement in clause A.14.4.1.1.2 shall apply for 1Rx RedCap UE.

#### A.20.4.1.3 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode for 2Rx RedCap UE with NTN

##### A.20.4.1.3.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.4.1 shall apply for 2Rx RedCap UE except that:

- Table A.14.4.1.4.1-1 is replaced with A.20.4.1.1.1-1, and

-  Table A.14.4.1.4.1-2, Table A.14.4.1.1.1-3 shall apply to configurations 1, 2, 3 and 4.

##### A.20.4.1.3.2 Test Requirements

The test requirement in clause A.14.4.1.4.2 shall apply for 2Rx RedCap UE.

#### A.20.4.1.4 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode for 1Rx RedCap UE with NTN

##### A.20.4.1.4.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.4.1 shall apply for 1Rx RedCap UE except that:

- Table A.14.4.1.4.1-1 is replaced with A.20.4.1.1.1-1, and

- Table A.14.4.1.4.1-2 is replaced with A.20.4.1.4.1-1, and

- Table A.14.4.1.1.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.4.1.4.1-1: General test parameters for FR1 in-sync testing in DRX mode

| Parameter |  |  |  | Unit | Value |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Test 1 |
| Active PCell |  |  |  |  | Cell 1 |
| RF Channel Number |  |  |  |  | 1 |
| BWchannel |  |  | Config 1, 2, 3, 4 | MHz | 10: NPRB,c = 52 |
| DL initial BWP configuration |  |  | Config 1, 2, 3, 4 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  |  | Config 1, 2, 3, 4 |  | DLBWP.1.1 |
| UL initial BWP configuration |  |  | Config 1, 2, 3, 4 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  |  | Config 1, 2, 3, 4 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel |  |  | Config 1, 2, 3, 4 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel |  |  | Config 1, 2, 3, 4 |  | CCR.3.1 FDD |
| SSB Configuration |  |  | Config 1, 2, 3, 4 |  | SSB.1 FR1 |
| SMTC Configuration |  |  | Config 1, 2, 3, 4 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing |  |  | Config 1, 2, 3, 4 |  | 15 kHz |
| PRACH Configuration |  |  | Config 1, 2, 3, 4 |  | Table  A.3.8.2.1-1 |
| SSB index assigned as RLM RS |  |  |  |  | 0 |
| OCNG parameters |  |  |  |  | OP.1 |
| CP length |  |  |  |  | Normal |
| Correlation Matrix and Antenna Configuration |  |  |  |  | 2x1 Low |
| In sync transmission parameters | DCI format |  |  |  | 1-0 |
|  | Number of Control OFDM symbols |  |  |  | 2 |
|  | Aggregation level |  |  | CCE | 4 |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  |  | dB | 0 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  |  | dB | 0 |
|  | DMRS precoder granularity |  |  |  | REG bundle size |
|  | REG bundle size |  |  |  | 6 |
| Out of sync transmission parameters | DCI format |  |  |  | 1-0 |
|  | Number of Control OFDM symbols |  |  |  | 2 |
|  | Aggregation level |  |  | CCE | 16 |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  |  | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  |  | dB | 4 |
|  | DMRS precoder granularity |  |  |  | REG bundle size |
|  | REG bundle size |  |  |  | 6 |
| DRX Configuration |  |  |  |  | DRX.3 |
| Gap pattern ID |  |  |  |  | N.A. |
| Layer 3 filtering |  |  |  |  | Enabled |
| T310 timer |  |  |  | ms | 2000 |
| T311 timer |  |  |  | ms | 1000 |
| N310 |  |  |  |  | 1 |
| N311 |  |  |  |  | 1 |
| CSI-RS configuration for CSI reporting |  | Config 1, 2, 3, 4 |  |  | CSI-RS.1.1 FDD |
| CSI-RS for tracking |  | Config 1, 2, 3, 4 |  |  | TRS.1.1 FDD |
| T1 |  |  |  | s | 0.2 |
| T2 |  |  |  | s | 0.2 |
| T3 |  |  |  | s | 1.24 |
| T4 |  |  |  | s | 0.2 |
| T5 |  |  |  | s | 0.88 |
| D1 |  |  |  | s | 0.84 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |

##### A.20.4.1.4.2 Test Requirements

The test requirement in clause A.14.4.1.4.2 shall apply for 1Rx RedCap UE.

#### A.20.4.1.5 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode for 2Rx RedCap UE with NTN

##### A.20.4.1.5.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.5.1 shall apply for 2Rx RedCap UE except that:

- Table A.14.4.1.5.1-1 is replaced with A.20.4.1.1.1-1, and

- Table A.14.4.1.5.1-2, Table A.14.4.1.5.1-3 shall apply to configurations 1, 2, 3 and 4.

##### A.20.4.1.5.2 Test Requirements

The test requirement in clause A.14.4.1.5.2 shall apply for 2Rx RedCap UE.

#### A.20.4.1.6 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode for 1Rx RedCap UE with NTN

##### A.20.4.1.6.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.5.1 shall apply for 1Rx RedCap UE except that:

- Table A.14.4.1.5.1-1 is replaced with A.20.4.1.1.1-1, and

- Table A.14.4.1.5.1-2 is replaced with A.20.4.1.6.1-1, and

- Table A.14.4.1.5.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.4.1.6.1-1: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in non-DRX mode

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| Active PCell |  |  | Cell 1 |
| RF Channel Number |  |  | 1 |
| Satellite information | Config 1,3 |  | SSC.1 |
|  | Config 2,4 |  | SSC.2 |
| DL initial BWP configuration | Config 1, 2, 3, 4 |  | DLBWP.0.1 |
| DL dedicated BWP configuration | Config 1, 2, 3, 4 |  | DLBWP.1.1 |
| UL initial BWP configuration | Config 1, 2, 3, 4 |  | ULBWP.0.1 |
| UL dedicated BWP configuration | Config 1, 2, 3, 4 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel | Config 1, 2, 3, 4 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel | Config 1, 2, 3, 4 |  | CCR.3.2 FDD |
| SSB Configuration | Config 1, 2, 3, 4 |  | SSB.1 FR1 |
| SMTC Configuration | Config 1, 2, 3, 4 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing | Config 1, 2, 3, 4 |  | 15 kHz |
| TRS configuration | Config 1, 2, 3, 4 |  | TRS.1.1 FDD |
| CSI-RS for RLM | Config 1, 2, 3, 4 |  | Resource #4 in TRS.1.1 FDD |
| TCI configuration for PDCCH/PDSCH |  |  | TCI.State. 2 |
| OCNG parameters |  |  | OP.1 |
| CP length |  |  | Normal |
| Correlation Matrix and Antenna Configuration |  |  | 2x1 Low |
| Out of sync transmission parameters | DCI format |  | 1-0 |
|  | Number of Control OFDM symbols |  | 2 |
|  | Aggregation level | CCE | 16 |
|  | Ratio of hypothetical PDCCH RE energy to average CSI-RS RE energy | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average CSI-RS RE energy | dB | 4 |
|  | DMRS precoder granularity |  | REG bundle size |
|  | REG bundle size |  | 6 |
| DRX |  |  | OFF |
| Gap pattern ID |  |  | gp0 |
| Layer 3 filtering |  |  | Enabled |
| T310 timer |  | ms | 0 |
| T311 timer |  | ms | 1000 |
| N310 |  |  | 1 |
| N311 |  |  | 1 |
| CSI-RS configuration for CSI reporting | Config 1, 2, 3, 4 |  | CSI-RS.1.1 FDD |
| T1 |  | s | 0.2 |
| T2 |  | s | 0.88 |
| T3 |  | s | 0.88 |
| D1 |  | s | 0.84 |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |

##### A.20.4.1.6.2 Test Requirements

The test requirement in clause A.14.4.1.5.2 shall apply for 1Rx RedCap UE.

#### A.20.4.1.7 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode for 2Rx RedCap UE with NTN

##### A.20.4.1.7.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.8.1 shall apply for 2Rx RedCap UE except that:

- Table A.14.4.1.8.1-1 is replaced with A.20.4.1.1.1-1, and

- Table A.14.4.1.5.1-2, Table A.14.4.1.5.1-3 shall apply to configurations 1, 2, 3 and 4.

##### A.20.4.1.7.2 Test Requirements

The test requirement in clause A.14.4.1.8.2 shall apply for 2Rx RedCap UE.

#### A.20.4.1.8 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode for 1Rx RedCap UE with NTN

##### A.20.4.1.8.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.8.1 shall apply for 1Rx RedCap UE except that:

- Table A.14.4.1.8.1-1 is replaced with A.20.4.1.1.1-1, and

- Table A.14.4.1.8.1-2 is replaced with A.20.4.1.8.1-1, and

- Table A.14.4.1.8.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.4.1.8.1-1: General test parameters for FR1 PCell for CSI-RS in-sync testing in non-DRX mode

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| Active PCell |  |  | Cell 1 |
| RF Channel Number |  |  | 1 |
| Satellite information | Config 1, 3 |  | SSC.1 |
|  | Config 2, 4 |  | SSC.2 |
| DL initial BWP configuration | Config 1, 2, 3, 4 |  | DLBWP.0.1 |
| DL dedicated BWP configuration | Config 1, 2, 3, 4 |  | DLBWP.1.1 |
| UL initial BWP configuration | Config 1, 2, 3, 4 |  | ULBWP.0.1 |
| UL dedicated BWP configuration | Config 1, 2, 3, 4 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel | Config 1, 2, 3, 4 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel | Config 1, 2, 3, 4 |  | CCR.3.1 FDD |
| SSB Configuration | Config 1, 2, 3, 4 |  | SSB.1 FR1 |
| SMTC Configuration | Config 1, 2, 3, 4 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing | Config 1, 2, 3, 4 |  | 15 kHz |
| TRS configuration | Config 1, 2, 3, 4 |  | TRS.1.1 FDD |
| CSI-RS for RLM | Config 1, 2, 3, 4 |  | Resource #4 in TRS.1.1 FDD |
| TCI configuration for PDCCH/PDSCH |  |  | TCI.State. 2 |
| OCNG parameters |  |  | OP.1 |
| CP length |  |  | Normal |
| Correlation Matrix and Antenna Configuration |  |  | 2x1 Low |
| Out of sync transmission parameters | DCI format |  | 1-0 |
|  | Number of Control OFDM symbols |  | 2 |
|  | Aggregation level | CCE | 16 |
|  | Ratio of hypothetical PDCCH RE energy to average CSI-RS RE energy | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average CSI-RS RE energy | dB | 4 |
|  | DMRS precoder granularity |  | REG bundle size |
|  | REG bundle size |  | 6 |
| In sync transmission parameters | DCI format |  | 1-0 |
|  | Number of Control OFDM symbols |  | 2 |
|  | Aggregation level | CCE | 8 |
|  | Ratio of hypothetical PDCCH RE energy to average CSI-RS RE energy | dB | 0 |
|  | Ratio of hypothetical PDCCH DMRS energy to average CSI-RS RE energy | dB | 0 |
|  | DMRS precoder granularity |  | REG bundle size |
|  | REG bundle size |  | 6 |
| DRX |  |  | DRX.3 |
| Gap pattern ID |  |  | gp0 |
| Layer 3 filtering |  |  | Enabled |
| T310 timer |  | ms | 2000 |
| T311 timer |  | ms | 1000 |
| N310 |  |  | 1 |
| N311 |  |  | 1 |
| CSI-RS configuration for CSI reporting | Config 1, 2, 3, 4 |  | CSI-RS.1.1 FDD |
| T1 |  | s | 0.2 |
| T2 |  | s | 0.2 |
| T3 |  | s | 0.488 |
| T4 |  | s | 0.2 |
| T5 |  | s | 1.88 |
| T6 |  | s | 1.84 |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |

##### A.20.4.1.8.2 Test Requirements

The test requirement in clause A.14.4.1.8.2 shall apply for 1Rx RedCap UE with NTN.

### A.20.4.2 Beam Failure Detection and Link recovery procedures for RedCap UE with satellite access

#### A.20.4.2.1 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode for 1Rx RedCap UE

##### A.20.4.2.1.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.1.1 shall apply for 1Rx RedCap UE except that:

- Clause 8.5 is replaced with clause 8.5E

- Table A.14.4.2.1.1-1 is replaced with A.20.4.2.1.1-1

- Table A.14.4.2.1.1-2, Table A.14.4.2.1.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.1.1-2.

Table A.20.4.2.1.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.4.2.1.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| NTN reference Serving satellite configuration | Config 1, 3 |  | SSC.1 |  |
|  | Config 2, 4 |  | SSC.2 |  |
| Duplex mode | Config 1, 2 |  | FDD |  |
|  | Config 3, 4 |  | HD-FDD |  |
| Dedicated CORESET Reference Channel | Config 1, 2, 3, 4 |  | CCR.3.2 FDD |  |
| Correlation Matrix and Antenna Configuration |  |  | 2x1 Low |  |
| Beam failure detection transmission parameters | Aggregation level | CCE | 16 |  |
| T3 |  | s | 0.44 |  |

##### A.20.4.2.1.2 Test Requirements

The test requirements defined in A.14.4.2.1.2 are reused for 1Rx RedCap UE with NTN.

#### A.20.4.2.2 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode for 2Rx RedCap UE

##### A.20.4.2.2.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.1.1 shall apply for 2Rx RedCap UE except that:

- Clause 8.5 is replaced with clause 8.5E

- Table A.14.4.2.1.1-1 is replaced with A.20.4.2.1.1-1

- Table A.14.4.2.1.1-2, Table A.14.4.2.1.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.2.1-1.

Table A.20.4.2.2.1-1: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| NTN reference Serving satellite configuration | Config 1, 3 |  | SSC.1 |  |
|  | Config 2, 4 |  | SSC.2 |  |
| Duplex mode | Config 1, 2 |  | FDD |  |
|  | Config 3, 4 |  | HD-FDD |  |
| Dedicated CORESET Reference Channel | Config 1, 2, 3, 4 |  | CCR.1.3 FDD |  |

##### A.20.4.2.2.2 Test Requirements

The test requirements defined in A.14.4.2.1.2 are reused for 2Rx RedCap UE with NTN.

#### A.20.4.2.3 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in DRX mode for 1Rx RedCap UE

##### A.20.4.2.3.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.2.1 shall apply for 1Rx RedCap UE except that:

- Clause 8.5 is replaced with clause 8.5E

- Table A.14.4.2.2.1-1 is replaced with A.20.4.2.1.1-1

- Table A.14.4.2.2.1-2, Table A.14.4.2.2.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.3.1-1.

Table A.20.4.2.3.1-1: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| NTN reference Serving satellite configuration | Config 1, 3 |  | SSC.1 |  |
|  | Config 2, 4 |  | SSC.2 |  |
| Duplex mode | Config 1, 2 |  | FDD |  |
|  | Config 3, 4 |  | HD-FDD |  |
| Dedicated CORESET Reference Channel | Config 1, 2, 3, 4 |  | CCR.3.2 FDD |  |
| Correlation Matrix and Antenna Configuration |  |  | 2x1 Low |  |
| Beam failure detection transmission parameters | Aggregation level | CCE | 16 |  |
| T3 |  | s | 6.44 |  |

##### A.20.4.2.3.2 Test Requirements

The test requirements defined in A.14.4.2.2.2 are reused for 1Rx RedCap UE with NTN.

#### A.20.4.2.4 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in DRX mode for 2Rx RedCap UE

##### A.20.4.2.4.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.2.1 shall apply for 2Rx RedCap UE except that:

- Clause 8.5 is replaced with clause 8.5E,

- Table A.14.4.2.2.1-1 is replaced with A.20.4.2.1.1-1,

- Table A.14.4.2.2.1-2, Table A.14.4.2.2.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.4.1-1.

Table A.20.4.2.4.1-1: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| NTN reference Serving satellite configuration | Config 1, 3 |  | SSC.1 |  |
|  | Config 2, 4 |  | SSC.2 |  |
| Duplex mode | Config 1, 2 |  | FDD |  |
|  | Config 3, 4 |  | HD-FDD |  |
| Dedicated CORESET Reference Channel | Config 1, 2, 3, 4 |  | CCR.1.3 FDD |  |

##### A.20.4.2.4.2 Test Requirements

The test requirements defined in A.14.4.2.2.2 are reused for 2Rx RedCap UE with NTN.

#### A.20.4.2.5 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in non-DRX mode for 1Rx RedCap UE

##### A.20.4.2.5.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.3.1 shall apply for 1Rx RedCap UE except that:

- Clause 8.5 is replaced with clause 8.5E,

- Table A.14.4.2.3.1-1 is replaced with A.20.4.2.1.1-1,

- Table A.14.4.2.3.1-2, Table A.14.4.2.3.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.5.1-1.

Table A.20.4.2.5.1-1: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| NTN reference Serving satellite configuration | Config 1, 3 |  | SSC.1 |  |
|  | Config 2, 4 |  | SSC.2 |  |
| Duplex mode | Config 1, 2 |  | FDD |  |
|  | Config 3, 4 |  | HD-FDD |  |
| Dedicated CORESET Reference Channel | Config 1, 2, 3, 4 |  | CCR.3.2 FDD |  |
| Correlation Matrix and Antenna Configuration |  |  | 2x1 Low |  |
| Beam failure detection transmission parameters | Aggregation level | CCE | 16 |  |
| T3 |  | s | 0.27 |  |

##### A.20.4.2.5.2 Test Requirements

The test requirements defined in A.14.4.2.3.2 are reused for 1Rx RedCap UE with NTN.

#### A.20.4.2.6 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in non-DRX mode for 2Rx RedCap UE

##### A.20.4.2.6.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.3.1 shall apply for 2Rx RedCap UE except that:

- Clause 8.5 is replaced with clause 8.5E,

- Table A.14.4.2.3.1-1 is replaced with A.20.4.2.1.1-1,

- Table A.14.4.2.3.1-2, Table A.14.4.2.3.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.6.1-1.

Table A.20.4.2.6.1-1: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| NTN reference Serving satellite configuration | Config 1, 3 |  | SSC.1 |  |
|  | Config 2, 4 |  | SSC.2 |  |
| Duplex mode | Config 1, 2 |  | FDD |  |
|  | Config 3, 4 |  | HD-FDD |  |
| Dedicated CORESET Reference Channel | Config 1, 2, 3, 4 |  | CCR.1.3 FDD |  |

##### A.20.4.2.6.2 Test Requirements

The test requirements defined in A.14.4.2.3.2 are reused for 2Rx RedCap UE with NTN.

#### A.20.4.2.7 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in DRX mode for 1Rx RedCap UE

##### A.20.4.2.7.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.4.1 shall apply for 1Rx RedCap UE except that:

- Clause 8.5 is replaced with clause 8.5E,

- Table A.14.4.2.4.1-1 is replaced with A.20.4.2.1.1-1,

- Table A.14.4.2.4.1-2, Table A.14.4.2.4.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.7.1-1.

Table A.20.4.2.7.1-1: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| NTN reference Serving satellite configuration | Config 1, 3 |  | SSC.1 |  |
|  | Config 2, 4 |  | SSC.2 |  |
| Duplex mode | Config 1, 2 |  | FDD |  |
|  | Config 3, 4 |  | HD-FDD |  |
| Dedicated CORESET Reference Channel | Config 1, 2, 3, 4 |  | CCR.3.2 FDD |  |
| Correlation Matrix and Antenna Configuration |  |  | 2x1 Low |  |
| Beam failure detection transmission parameters | Aggregation level | CCE | 16 |  |
| T3 |  | s | 12.24 |  |

##### A.20.4.2.7.2 Test Requirements

The test requirements defined in A.14.4.2.4.2 are reused for 1Rx RedCap UE with NTN.

#### A.20.4.2.8 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in DRX mode for 2Rx RedCap UE

##### A.20.4.2.8.1 Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.4.1 shall apply for 2Rx RedCap UE except that:

- Clause 8.5 is replaced with clause 8.5E

- Table A.14.4.2.4.1-1 is replaced with A.20.4.2.1.1-1

- Table A.14.4.2.4.1-2, Table A.14.4.2.4.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.8.1-1.

Table A.20.4.2.8.1-1: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| NTN reference Serving satellite configuration | Config 1, 3 |  | SSC.1 |  |
|  | Config 2, 4 |  | SSC.2 |  |
| Duplex mode | Config 1, 2 |  | FDD |  |
|  | Config 3, 4 |  | HD-FDD |  |
| Dedicated CORESET Reference Channel | Config 1, 2, 3, 4 |  | CCR.1.3 FDD |  |

##### A.20.4.2.8.2 Test Requirements

The test requirements defined in A.14.4.2.4.2 are reused for 2Rx RedCap UE with NTN.

### A.20.4.3 Active BWP switch for RedCap UE with Satellite Access

#### A.20.4.3.1 DCI-based and Timer-based Active BWP Switch

##### A.20.4.3.1.1 NR FR1 DL active BWP switch with non-DRX in SA

A.20.4.3.1.1.1 Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6E.

The supported test configurations are shown in table A.20.4.3.1.1.1-1 below.

The test procedure and environment in clause A.14.4.3.1.1.1 shall apply.

Table A.20.4.3.1.1.1-1: DL BWP switch supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

A.20.4.3.1.1.2 Test Requirements

The test requirements in clause A.14.4.3.1.1.2 shall apply.

#### A.20.4.3.2 RRC-based Active BWP Switch

##### A.20.4.3.2.1 NR FR1 DL active BWP switch of Cell with non-DRX in SA

A.20.4.3.2.1.1 Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6E.

The supported test configurations are shown in table A.20.4.3.2.1.1-1 below.

The test procedure and environment in clause A.14.4.3.2.1.1 shall apply.

Table A.20.4.3.2.1.1-1: DL BWP switch supported test configurations in SA scenario

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.4.3.2.1.2 Test Requirements

The test requirements in clause A.14.4.3.1.1.2 shall apply.



### A.20.4.4 UE specific CBW change for RedCap UE with Satellite Access

#### A.20.4.4.1 UE specific CBW change on PCell in FR1 in non-DRX

##### A.20.4.4.1.1 Test Purpose and Environment

The purpose of this test is to verify the UE specific CBW change delay requirement defined in clause 8.13E.

The supported test configurations are shown in table A.20.4.4.1.1-1. The test scenario comprises of one Cell (Cell 1), which is PCell as given in table A.20.4.4.1.1-2. Cell-specific parameters are specified in table A.20.4.4.1.1-3.

The test procedure in clause A.14.4.4.1.1.1 shall apply.

Table A.20.4.4.1.1-1: Supported test configurations for UE specific CBW change in SA scenario

| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| --- | --- |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.4.4.1.1-2: General test parameters for UE specific CBW change in SA scenario

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active Cell |  | Cell 1 | Cell on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| T1 | s | 0.2 |  |

Table A.20.4.4.1.1-3: NR Cell specific test parameters for UE specific CBW change in SA scenario

| Parameter |  |  | Unit | Cell 1 |
| --- | --- | --- | --- | --- |
| Frequency Range |  |  |  | FR1 |
| Duplex mode |  | Config 1, 2 |  | FDD |
|  |  | Config 3, 4 |  | HD-FDD |
| BWchannel |  | Config 1, 2, 3, 4 |  | 10 MHz: NPRB,c = 52 |
| Satellite information |  | Config 1, 3 |  | SSC.1 |
|  |  | Config 2, 4 |  | SSC.2 |
| Active DL BWP ID |  | Config 1, 2, 3, 4 |  | 1 |
| Initial DL BWP Configuration (BWP-1) |  | Config 1, 2, 3, 4 |  | DLBWP.0.1 |
| Initial UL BWP Configuration |  | Config 1, 2, 3, 4 |  | ULBWP.0.1 |
| Initial Condition | Active DLCBW-1 Configureation | Config 1, 2, 3, 4 |  | DLCBW.1.1 |
|  | Active UL CBW-1Configuration | Config 1, 2, 3, 4 |  | ULCBW.1.1 |
| Final Condition | Active DLCBW-1 Configureation | Config 1, 2, 3, 4 |  | DLCBW.1.2 |
|  | Active UL CBW-1Configuration | Config 1, 2, 3, 4 |  | ULCBW.1.2 |
| PDSCH Reference measurement channel |  | Config 1, 2, 3, 4 |  | SR.1.1 FDD |
| RMSI CORESET parameters |  | Config 1, 2, 3, 4 |  | CR.1.1 FDD |
| Dedicated CORESET parameters |  | Config 1, 2, 3, 4 |  | CCR.1.1 FDD |
| OCNG Patterns |  |  |  | OP.1 |
| SSB Configuration |  | Config 1, 2, 3, 4 |  | SSB.1 FR1 |
| SMTC Configuration |  |  |  | SMTC.1 |
| TRS Configuration |  | Config 1, 2, 3, 4 |  | TRS.1.1 FDD |
| Antenna Configuration |  |  |  | 1x1 |
| Propagation Condition |  |  |  | AWGN |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS(Note 1) |  |  |  |  |
| NocNote 2 |  | Config 1, 2, 3, 4 | dBm/SCS | -104 |
| SS-RSRP Note 3 |  | Config 1, 2, 3, 4 | dBm/SCS | -87 |
| Ês/Iot |  |  | dB | 17 |
| Ês/Noc |  |  | dB | 17 |
| IoNote3 |  | Config 1, 2, 3, 4 | dBm/9.36 MHz | -58.96 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |

##### A.20.4.4.1.2 Test Requirements

The test requirements in clause A.14.4.4.1.2 shall apply.

### A.20.4.5 Pathloss reference signal switching delay for RedCap UE with Satellite Access

#### A.20.4.5.1 MAC-CE based pathloss reference signal switch delay

##### A.20.4.5.1.1 Test Purpose and Environment

The purpose of this test is to verify the MAC-CE based pathloss reference signal switch delay requirement defined in clause 8.14E.

The supported test configurations are shown in table A.20.4.5.1.1-1 below.

The test procedure and environment in clause A.14.4.5.1.1 shall apply.

Table A.20.4.5.1.1-1: MAC-CE based pathloss reference signal switch supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.4.5.1.2 Test Requirements

The test requirements in clause A.14.4.5.1.2 shall apply.

## A.20.5 Measurement procedure

### A.20.5.1 Intra-frequency Measurements

#### A.20.5.1.1 SA event triggered reporting tests without gap under non-DRX for 1Rx RedCap UE

##### A.20.5.1.1.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2E.5.1 and 9.2E.5.2.

##### A.20.5.1.1.2 Test parameters

The test parameters and procedure in clause A.14.5.1.1.2 apply, except that the supported test configurtions are defined in table A.20.5.1.1.2-1, and NR Cell specific test parameters in Table A.20.5.1.1.2-2 replace the corresponding parameters in Table A.14.5.1.1.2-3. Other parameters in Table A.14.5.1.1.2-2 and Table A.14.5.1.1.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.5.1.1.2-2: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1, 3 | SSC.1 |  | NSC.1 |  |
|  |  | 2, 4 | SSC.2 |  | NSC.2 |  |

##### A.20.5.1.1.3 Test Requirements

The test requirements in clause A.14.5.1.1.3 apply for this test.

#### A.20.5.1.2 SA event triggered reporting tests without gap under non-DRX for 2Rx RedCap UE

##### A.20.5.1.2.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2E.5.1 and 9.2E.5.2.

##### A.20.5.1.2.2 Test parameters

The test parameters and procedure in clause A.14.5.1.1.2 apply, except that the supported test configurtions are defined in table A.20.5.1.2.2-1, and NR Cell specific test parameters in Table A.20.5.1.2.2-2 replace the corresponding parameters in Table A.14.5.1.1.2-3. Other parameters in Table A.14.5.1.1.2-2 and Table A.14.5.1.1.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.2.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.5.1.2.2-2: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1, 3 | SSC.1 |  | NSC.1 |  |
|  |  | 2, 4 | SSC.2 |  | NSC.2 |  |

##### A.20.5.1.2.3 Test Requirements

The test requirements in clause A.14.5.1.1.3 apply for this test.

#### A.20.5.1.3 SA event triggered reporting tests without gap under DRX for 1Rx RedCap UE

##### A.20.5.1.3.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2E.5.1 and 9.2E.5.2.

##### A.20.5.1.3.2 Test parameters

The test parameters and procedure in clause A.14.5.1.2.2 apply, except that the supported test configurtions are defined in table A.20.5.1.3.2-1, and NR Cell specific test parameters in Table A.20.5.1.3.2-2 replace the corresponding parameters in Table A.14.5.1.2.2-3. Other parameters in Table A.14.5.1.2.2-2 and Table A.14.5.1.2.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.3.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.5.1.3.2-2: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1, 3 | SSC.1 |  | NSC.1 |  |
|  |  | 2, 4 | SSC.2 |  | NSC.2 |  |

##### A.20.5.1.3.3 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. X=1520 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise X=920.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Y ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. Y=15360 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise Y=7680.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.20.5.1.4 SA event triggered reporting tests without gap under DRX for 2Rx RedCap UE

##### A.20.5.1.4.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2E.5.1 and 9.2E.5.2.

##### A.20.5.1.4.2 Test parameters

The test parameters and procedure in clause A.14.5.1.2.2 apply, except that the supported test configurtions are defined in table A.20.5.1.4.2-1, and NR Cell specific test parameters in Table A.20.5.1.4.2-2 replace the corresponding parameters in Table A.14.5.1.2.2-3. Other parameters in Table A.14.5.1.2.2-2 and Table A.14.5.1.2.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.4.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.5.1.4.2-2: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1, 3 | SSC.1 |  | NSC.1 |  |
|  |  | 2, 4 | SSC.2 |  | NSC.2 |  |

##### A.20.5.1.4.3 Test Requirements

The test requirements in clause A.14.5.1.2.3 apply for this test.

#### A.20.5.1.5 SA event triggered reporting tests without gap under non-DRX with SSB index reading for 1Rx RedCap UE

##### A.20.5.1.5.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2E.5.1 and 9.2E.5.2.

##### A.20.5.1.5.2 Test parameters

The test parameters and procedure in clause A.14.5.1.3.2 apply, except that the supported test configurtions are defined in table A.20.5.1.5.2-1, and NR Cell specific test parameters in Table A.20.5.1.5.2-2 replace the corresponding parameters in Table A.14.5.1.3.2-3. Other parameters in Table A.14.5.1.3.2-2 and Table A.14.5.1.3.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.5.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.5.1.5.2-2: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1, 3 | SSC.1 |  | NSC.1 |  |
|  |  | 2, 4 | SSC.2 |  | NSC.2 |  |

##### A.20.5.1.5.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X = 1040 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.20.5.1.6 SA event triggered reporting tests without gap under non-DRX with SSB index reading for 2Rx RedCap UE

##### A.20.5.1.6.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2E.5.1 and 9.2E.5.2.

##### A.20.5.1.6.2 Test parameters

The test parameters and procedure in clause A.14.5.1.3.2 apply, except that the supported test configurtions are defined in table A.20.5.1.6.2-1, and NR Cell specific test parameters in Table A.20.5.1.6.2-2 replace the corresponding parameters in Table A.14.5.1.3.2-3. Other parameters in Table A.14.5.1.3.2-2 and Table A.14.5.1.3.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.6.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.5.1.6.2-2: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1, 3 | SSC.1 |  | NSC.1 |  |
|  |  | 2, 4 | SSC.2 |  | NSC.2 |  |

##### A.20.5.1.6.3 Test Requirements

The test requirements in clause A.14.5.1.3.3 apply for this test.

#### A.20.5.1.7 SA event triggered reporting tests with single measurement gap under non-DRX for satellite access for 1Rx RedCap UE

##### A.20.5.1.7.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2E.6.1 and 9.2E.6.2.

##### A.20.5.1.7.2 Test parameters

The test parameters and procedure in clause A.14.5.1.4.2 apply, except that the supported test configurtions are defined in table A.20.5.1.7.2-1, and NR Cell specific test parameters in Table A.20.5.1.7.2-2 replace the corresponding parameters in Table A.14.5.1.4.2-3. Other parameters in Table A.14.5.1.4.2-2 and Table A.14.5.1.4.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.7.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.5.1.7.2-2: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1, 3 | SSC.1 |  | NSC.1 |  |
|  |  | 2, 4 | SSC.2 |  | NSC.2 |  |

##### A.20.5.1.7.3 Test Requirements

The test requirements in clause A.14.5.1.4.3 apply for this test.

#### A.20.5.1.8 SA event triggered reporting tests with single measurement gap under non-DRX for satellite access for 2Rx RedCap UE

##### A.20.5.1.8.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2E.6.1 and 9.2E.6.2.

##### A.20.5.1.8.2 Test parameters

The test parameters and procedure in clause A.14.5.1.4.2 apply, except that the supported test configurtions are defined in table A.20.5.1.8.2-1, and NR Cell specific test parameters in Table A.20.5.1.8.2-2 replace the corresponding parameters in Table A.14.5.1.4.2-3. Other parameters in Table A.14.5.1.4.2-2 and Table A.14.5.1.4.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.8.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.5.1.8.2-2: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1, 3 | SSC.1 |  | NSC.1 |  |
|  |  | 2, 4 | SSC.2 |  | NSC.2 |  |

##### A.20.5.1.8.3 Test Requirements

The test requirements in clause A.14.5.1.4.3 apply for this test.

#### A.20.5.1.9 SA event triggered reporting tests with FNO concurrent gaps under DRX for satellite access for 1Rx RedCap UE

##### A.20.5.1.9.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2E.6.1 and 9.2E.6.2.

##### A.20.5.1.9.2 Test parameters

The test parameters and procedure in clause A.14.5.1.5.2 apply, except that the supported test configurtions are defined in table A.20.5.1.9.2-1, and NR Cell specific test parameters in Table A.20.5.1.9.2-2 replace the corresponding parameters in Table A.14.5.1.5.2-3. Other parameters in Table A.14.5.1.5.2-2 and Table A.14.5.1.5.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.9.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.5.1.9.2-2: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1, 3 | SSC.1 |  | NSC.1 |  |
|  |  | 2, 4 | SSC.2 |  | NSC.2 |  |

##### A.20.5.1.9.3 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 7680 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.20.5.1.10 SA event triggered reporting tests with FNO concurrent gaps under DRX for satellite access for 2Rx RedCap UE

##### A.20.5.1.10.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2E.6.1 and 9.2E.6.2.

##### A.20.5.1.10.2 Test parameters

The test parameters and procedure in clause A.14.5.1.5.2 apply, except that the supported test configurtions are defined in table A.20.5.1.10.2-1, and NR Cell specific test parameters in Table A.20.5.1.10.2-2 replace the corresponding parameters in Table A.14.5.1.5.2-3. Other parameters in Table A.14.5.1.5.2-2 and Table A.14.5.1.5.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.10.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.5.1.10.2-2: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1, 3 | SSC.1 |  | NSC.1 |  |
|  |  | 2, 4 | SSC.2 |  | NSC.2 |  |

##### A.20.5.1.10.3 Test Requirements

The test requirements in clause A.14.5.1.5.3 apply for this test.

#### A.20.5.1.11 SA event triggered reporting tests with PPO concurrent gaps under non-DRX with SSB index reading for satellite access for 1Rx RedCap UE

##### A.20.5.1.11.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2E.6.1 and 9.2E.6.2.

##### A.20.5.1.11.2 Test parameters

The test parameters and procedure in clause A.14.5.1.6.2 apply, except that the supported test configurtions are defined in table A.20.5.1.11.2-1, and NR Cell specific test parameters in Table A.20.5.1.11.2-2 replace the corresponding parameters in Table A.14.5.1.6.2-3. Other parameters in Table A.14.5.1.6.2-2 and Table A.14.5.1.6.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.11.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.5.1.11.2-2: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1, 3 | SSC.1 |  | NSC.1 |  |
|  |  | 2, 4 | SSC.2 |  | NSC.2 |  |

##### A.20.5.1.11.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1480 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.20.5.1.12 SA event triggered reporting tests with PPO concurrent gaps under non-DRX with SSB index reading for satellite access for 2Rx RedCap UE

##### A.20.5.1.12.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2E.6.1 and 9.2E.6.2.

##### A.20.5.1.12.2 Test parameters

The test parameters and procedure in clause A.14.5.1.6.2 apply, except that the supported test configurtions are defined in table A.20.5.1.12.2-1, and NR Cell specific test parameters in Table A.20.5.1.12.2-2 replace the corresponding parameters in Table A.14.5.1.6.2-3. Other parameters in Table A.14.5.1.6.2-2 and Table A.14.5.1.6.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.12.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.5.1.12.2-2: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1, 3 | SSC.1 |  | NSC.1 |  |
|  |  | 2, 4 | SSC.2 |  | NSC.2 |  |

##### A.20.5.1.12.3 Test Requirements

The test requirements in clause A.14.5.1.5.3 apply for this test.

### A.20.5.2 Inter-frequency Measurements

#### A.20.5.2.1 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used with single gap for 2Rx RedCap UE with satellite access

##### A.20.5.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.2.1 shall apply for 2Rx RedCap UE except that:

- Table A.14.5.2.2.1-1 is replaced with A.20.5.2.1.1-1, and

- Table A.14.5.2.2.1-2, Table A.14.5.2.2.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.5.2.1.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 3 | GSO, HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 4 | NGSO, HD-FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.5.2.1.2 Test Requirements

The test requirement in clause A.14.5.2.2.2 shall apply for 2Rx RedCap UE with NTN.

#### A.20.5.2.2 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used with single gap for 1Rx RedCap UE with satellite access

##### A.20.5.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.2.1 shall apply for 1Rx RedCap UE except that:

- Table A.14.5.2.2.1-1 is replaced with A.20.5.2.1.1-1, and

- Table A.14.5.2.2.1-2 is replaced with A.20.5.2.2.1-1, and

- Table A.14.5.2.2.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.5.2.2.1-1: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| NR RF Channel Number |  | Config 1,2,3,4 | 1, 2 |  | Two FR1 NR carrier frequencies is used. |
| Active cell |  | Config 1,2,3,4 | NR Cell 1 (Pcell) |  | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2,3,4 | NR Cell 2 |  | NR Cell 2 is on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1,2,3,4 | 0 |  | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2,3,4 | 9 |  |  |
| A3-Offset | dB | Config 1,2,3,4 | -6 |  |  |
| Hysteresis | dB | Config 1,2,3,4 | 0 |  |  |
| CP length |  | Config 1,2,3,4 | Normal |  |  |
| TimeToTrigger | s | Config 1,2,3,4 | 0 |  |  |
| Filter coefficient |  | Config 1,2,3,4 | 0 |  | L3 filtering is not used |
| DRX |  | Config 1,2,3,4 | DRX.1 | DRX. 7 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | Config 1,2,3,4 | 3 ms |  | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
| T1 | s | Config 1,2,3,4 | 5 |  |  |
| T2 | s | Config 1,2,3,4 | 1.1 | 12 |  |

##### A.20.5.2.2.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1080 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 11520 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2 UE is not required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.20.5.2.3 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used with single gap for 2Rx RedCap UE with satellite access

##### A.20.5.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.3.1 shall apply for 2Rx RedCap UE except that:

- Table A.14.5.2.3.1-1 is replaced with A.20.5.2.1.1-1, and

- Table A.14.5.2.3.1-2, Table A.14.5.2.3.1-3 shall apply to configurations 1, 2, 3 and 4.

##### A.20.5.2.3.2 Test Requirements

The test requirement in clause A.14.5.2.3.2 shall apply for 2Rx RedCap UE with NTN.

#### A.20.5.2.4 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used with single gap for 1Rx RedCap UE with satellite access

##### A.20.5.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.3.1 shall apply for 1Rx RedCap UE except that:

- Table A.14.5.2.3.1-1 is replaced with A.20.5.2.1.1-1, and

- Table A.14.5.2.3.1-2 is replaced with A.20.5.2.4.1-1, and

- Table A.14.5.2.3.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.5.2.4.1-1: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| NR RF Channel Number |  | Config 1,2,3,4 | 1, 2 | Two FR1 NR carrier frequencies is used. |
| Active cell |  | Config 1,2,3,4 | NR Cell 1 (Pcell) | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2,3,4 | NR Cell 2 | NR Cell 2 is on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1,2,3,4 | 0 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2,3,4 | 9 |  |
| A3-Offset | dB | Config 1,2,3,4 | -6 |  |
| Hysteresis | dB | Config 1,2,3,4 | 0 |  |
| CP length |  | Config 1,2,3,4 | Normal |  |
| TimeToTrigger | s | Config 1,2,3,4 | 0 |  |
| Filter coefficient |  | Config 1,2,3,4 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2,3,4 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | Config 1,2,3,4 | 3 ms | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
| T1 | s | Config 1,2,3,4 | 5 |  |
| T2 | s | Config 1,2,3,4 | 1.4 |  |

##### A.20.5.2.4.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1240 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 UE is required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.20.5.2.5 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in fully non-overlapped for 2Rx RedCap UE with satellite access

##### A.20.5.2.5.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.4.1 shall apply for 2Rx RedCap UE except that:

- Table A.14.5.2.4.1-1 is replaced with A.20.5.2.1.1-1, and

- Table A.14.5.2.4.1-2, Table A.14.5.2.4.1-3 shall apply to configurations 1, 2, 3 and 4.

##### A.20.5.2.5.2 Test Requirements

The test requirement in clause A.14.5.2.4.2 shall apply for 2Rx RedCap UE with NTN.

#### A.20.5.2.6 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in fully non-overlapped for 1Rx RedCap UE with satellite access

##### A.20.5.2.6.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.4.1 shall apply for 1Rx RedCap UE except that:

- Table A.14.5.2.4.1-1 is replaced with A.20.5.2.1.1-1, and

- Table A.14.5.2.4.1-2 is replaced with A.20.5.2.6.1-1, and

- Table A.14.5.2.4.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.5.2.6.1-1: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1,2,3,4 | 1, 2 | Two FR1 NR carrier frequencies is used. |
| Active cell |  | Config 1,2,3,4 | NR Cell 1 (Pcell) | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2,3,4 | NR Cell 2 and NR Cell 3 | NR Cell 2 and NR Cell 3 are on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1,2,3,4 | 0 for MeasGapId #10 for MeasGapId #2 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2,3,4 | 9 for MeasGapId #119 for MeasGapId #2 |  |
| A3-Offset | dB | Config 1,2,3,4 | -6 |  |
| Hysteresis | dB | Config 1,2,3,4 | 0 |  |
| CP length |  | Config 1,2,3,4 | Normal |  |
| TimeToTrigger | s | Config 1,2,3,4 | 0 |  |
| Filter coefficient |  | Config 1,2,3,4 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2,3,4 | OFF | DRX is not used |
| Time offset between serving and neighbour Cell 2,3 |  | Config 1,2,3,4 | 3 ms | Asynchronous cells.The timing of Cell 2 and Cell 3 is 3 ms later than the timing of Cell 1. |
| T1 | s | Config 1,2,3,4 | 5 |  |
| T2 | s | Config 1,2,3,4 | 1.2 |  |

##### A.20.5.2.6.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1000 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 UE is not required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.20.5.2.7 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in partially partial overalpping for 2Rx RedCap UE with satellite access

##### A.20.5.2.7.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.6.1 shall apply for 2Rx RedCap UE except that:

- Table A.14.5.2.6.1-1 is replaced with A.20.5.2.1.1-1, and

- Table A.14.5.2.6.1-2, Table A.14.5.2.6.1-3 shall apply to configurations 1, 2, 3 and 4.

##### A.20.5.2.7.2 Test Requirements

The test requirement in clause A.14.5.2.6.2 shall apply for RedCap.

#### A.20.5.2.8 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in partially partial overalpping for 1Rx RedCap UE with satellite access

##### A.20.5.2.8.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.6.1 shall apply for 1Rx RedCap UE except that:

- Table A.14.5.2.6.1-1 is replaced with A.20.5.2.1.1-1, and

- Table A.14.5.2.6.1-2 is replaced with A.20.5.2.8.1-1, and

- Table A.14.5.2.6.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.5.2.8.1-1: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1,2,3,4 | 1, 2 | Two FR1 NR carrier frequencies is used. |
| Active cell |  | Config 1,2,3,4 | NR Cell 1 (Pcell) | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2,3,4 | NR Cell 2 and NR Cell 3 | NR Cell 2 and NR Cell 3 are on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1,2,3,4 | 0 for MeasGapId #11 for MeasGapId #2 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2,3,4 | 39 for MeasGapId #14 for MeasGapId #2 |  |
| A3-Offset | dB | Config 1,2,3,4 | -6 |  |
| Hysteresis | dB | Config 1,2,3,4 | 0 |  |
| CP length |  | Config 1,2,3,4 | Normal |  |
| TimeToTrigger | s | Config 1,2,3,4 | 0 |  |
| Filter coefficient |  | Config 1,2,3,4 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2,3,4 | OFF | DRX is not used |
| Time offset between serving and neighbour Cell 1 |  | Config 1,2,3,4 | 3s | Synchronous. |
| Time offset between serving and neighbour Cell 2 |  | Config 1,2,3,4 | 5 ms | Asynchronous.The timing of Cell 3 is 5 ms later than the timing of Cell 1. |
| T1 | s | Config 1,2,3,4 | 5 |  |
| T2 | s | Config 1,2,3,4 | 1.6 |  |

##### A.20.5.2.8.2 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1440 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.20.5.2.9 Event triggered reporting test without gap under non-DRX for 2Rx RedCap UE with satellite access

##### A.20.5.2.9.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the inter-frequency cell search requirements in clause 9.3E.7.

##### A.20.5.2.9.2 Test parameters

The test environment in clause A.14.5.2.7.1 shall apply for 2Rx RedCap UE except that:

- Table A.14.5.2.7.2-1 is replaced with A.20.5.2.1.1-1, and

- Table A.14.5.2.7.2-2, Table A.14.5.2.7.2-3 shall apply to configurations 1, 2, 3 and 4.

##### A.20.5.2.9.3 Test Requirements

The test requirement in clause A.14.5.2.7.3 shall apply for 2Rx RedCap UE with NTN.

#### A.20.5.2.10 Event triggered reporting test without gap under non-DRX for 1Rx RedCap UE with satellite access

##### A.20.5.2.10.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the inter-frequency cell search requirements in clause 9.3E.7.

##### A.20.5.2.10.2 Test parameters

The test environment in clause A.14.5.2.7.2 shall apply for 1Rx RedCap UE except that:

- Table A.14.5.2.7.2-1 is replaced with A.20.5.2.1.1-1, and

- Table A.14.5.2.7.2-2, Table A.14.5.2.7.2-3 shall apply to configurations 1, 2, 3 and 4.

##### A.20.5.2.10.3 Test Requirements

The test requirement in clause A.14.5.2.7.3 shall apply for 1Rx RedCap UE with NTN.

#### A.20.5.2.11 Event triggered reporting tests without gap under DRX for 2Rx RedCap UE with satellite access

##### A.20.5.2.11.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the inter-frequency cell search requirements in clauses 9.3E.7.

##### A.20.5.2.11.2 Test parameters

The test environment in clause A.14.5.2.8.2 shall apply for 2Rx RedCap UE except that:

- Table A.14.5.2.8.2-1 is replaced with A.20.5.2.1.1-1, and

- Table A.14.5.2.8.2-2, Table A.14.5.2.8.2-3 shall apply to configurations 1, 2, 3 and 4.

##### A.20.5.2.11.3 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. X=1280 for test configuration 2,4 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise X=920.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Y ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. Y=12800 for test configuration 2, 4 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise Y=6400.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.20.5.2.12 Event triggered reporting tests without gap under DRX for 1Rx RedCap UE with satellite access

##### A.20.5.2.12.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the inter-frequency cell search requirements in clause 9.3E.7.

##### A.20.5.2.12.2 Test parameters

The test environment in clause A.14.5.2.8.2 shall apply for 1Rx RedCap UE except that:

- Table A.14.5.2.8.2-1 is replaced with A.20.5.2.1.1-1, and

- Table A.14.5.2.8.2-2 is replaced with A.20.5.2.12.2-1, and

- Table A.14.5.2.8.2-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.5.2.12.2-1: General test parameters for inter-frequency event triggered reporting without gap for PCell in FR1 with DRX

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| Active cell |  | 1, 2, 3, 4 | Cell 1 |  |  |
| Neighbour cell |  | 1, 2, 3, 4 | Cell 2 and Cell 3 |  | Cell to be identified. |
| RF Channel Number |  | 1, 2, 3, 4 | 1: Cell 12:  Cell 2 and Cell 3 |  |  |
| SMTC configuration |  | 1, 2, 3, 4 | SMTC.2 |  |  |
| A3-Offset | dB | 1, 2, 3, 4 | -4.5 |  |  |
| CP length |  | 1, 2, 3, 4 | Normal |  |  |
| Hysteresis | dB | 1, 2, 3, 4 | 0 |  |  |
| Time To Trigger | s | 1, 2, 3, 4 | 0 |  |  |
| Filter coefficient |  | 1, 2, 3, 4 | 0 |  | L3 filtering is not used |
| DRX |  | 1, 2, 3, 4 | DRX.1 | DRX. 7 |  |
| Time offset between serving and neighbour cells |  | 1, 2, 3, 4 | 3 s |  | Synchronous cells |
| T1 | s | 1, 2, 3, 4 | 5 |  |  |
| T2 | s | 1, 2, 3, 4 | 5 | 16 |  |

##### A.20.5.2.12.3 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. X=1520 for test configuration 2,4 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise X=920.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Y ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. Y=15360 for test configuration 2,4 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise Y=7680.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

### A.20.5.3 L1-RSRP measurement for beam reporting for (e)RedCap UE with Satellite Access

#### A.20.5.3.1 SSB based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is not used for 1Rx (e)RedCap UE with NTN

##### A.20.5.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5E.4.1, with the testing configurations for NR cells served by satellite access node (SAN) in Table A.20.5.3.1.1-1.

Table A.20.5.3.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test for satellite access

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. Note 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.5.3.1.2 Test parameters

There is one cells in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.20.5.3.1.2-1 and table A.20.5.3.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.20.5.3.1.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB ARFCN | 1~4 |  | freq1 |
| Duplex mode | 1, 2 |  | FDD |
|  | 3, 4 |  | HD-FDD |
| TDD Configuration | 1~4 |  | N/A |
| BWchannel | 1~4 | MHz | 10: NPRB,c = 52 |
|  |  |  |  |
| Satellite information | 1, 3 |  | SSC.1 |
|  | 2, 4 |  | SSC.2 |
| PDSCH Reference measurement channel | 1~4 |  | SR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| RMSI CORESET Reference Channel | 1~4 |  | CR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| Dedicated CORESET Reference Channel | 1~4 |  | CCR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| SSB configuration | 1~4 |  | SSB.3 FR1 |
|  |  |  |  |
|  |  |  |  |
| OCNG Patterns | 1~4 |  | OP.1 |
| Initial BWP Configuration | 1~4 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1~4 |  | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration | 1~4 |  | SMTC.1 |
| TRS Configuration | 1~4 |  | TRS.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| DRX configuration | 1~4 |  | Off |
| reportConfigType | 1~4 |  | periodic |
| reportQuantity | 1~4 |  | ssb-Index-RSRP |
| Number of reported RS | 1~4 |  | 2 |
| L1-RSRP reporting period | 1~4 | slot | 80 |
| T1 | 1~4 | s | 5 |
| T2 | 1~4 | s | 1 |
| EPRE ratio of PSS to SSS | 1~4 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1~4 |  | AWGN |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |

Table A.20.5.3.1.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Note2 | 1~4 | dBm/15 kHz | -94.65 |  |  |  |
| Note2 | 1~4 | dBm/SSB SCS | -94.65 |  |  |  |
|  | 1~4 | dB | 0 | 0 | -Infinity | 3 |
| SSB RSRP Note3 | 1~4 | dBm/SSB SCS | -94.65 | -94.65 | -Infinity | -91.65 |
| Io Note3 | 1~4 | dBm/9.36 MHz | -63.69 | -63.69 | -66.70 | -61.93 |
|  | 1~4 | dB | 0 | 0 | -Infinity | 3 |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.20.5.3.1.3 Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19F.1.1 and relative accuracy requirement in clause 10.1.19F.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.20.5.3.2 SSB based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is not used for 2Rx (e)RedCap UE with NTN

##### A.20.5.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5E.4.1, with the testing configurations for NR cells served by satellite access node (SAN) in table A.20.5.3.2.1-1.

Table A.20.5.3.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test for satellite access

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. Note 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.5.3.2.2 Test parameters

There is one cell in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.20.5.3.2.2-1 and table A.20.5.3.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.20.5.3.2.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB ARFCN | 1~4 |  | freq1 |
| Duplex mode | 1, 2 |  | FDD |
|  | 3, 4 |  | HD-FDD |
| TDD Configuration | 1~4 |  | N/A |
| BWchannel | 1~4 | MHz | 10: NPRB,c = 52 |
|  |  |  |  |
| Satellite information | 1, 3 |  | SSC.1 |
|  | 2, 4 |  | SSC.2 |
| PDSCH Reference measurement channel | 1~4 |  | SR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| RMSI CORESET Reference Channel | 1~4 |  | CR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| Dedicated CORESET Reference Channel | 1~4 |  | CCR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| SSB configuration | 1~4 |  | SSB.3 FR1 |
|  |  |  |  |
|  |  |  |  |
| OCNG Patterns | 1~4 |  | OP.1 |
| Initial BWP Configuration | 1~4 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1~4 |  | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration | 1~4 |  | SMTC.1 |
| TRS Configuration | 1~4 |  | TRS.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| DRX configuration | 1~4 |  | Off |
| reportConfigType | 1~4 |  | periodic |
| reportQuantity | 1~4 |  | ssb-Index-RSRP |
| Number of reported RS | 1~4 |  | 2 |
| L1-RSRP reporting period | 1~4 | slot | 80 |
| T1 | 1~4 | s | 5 |
| T2 | 1~4 | s | 1 |
| EPRE ratio of PSS to SSS | 1~4 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1~4 |  | AWGN |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |

Table A.20.5.3.2.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Note2 | 1~4 | dBm/15 kHz | -94.65 |  |  |  |
| Note2 | 1~4 | dBm/SSB SCS | -94.65 |  |  |  |
|  | 1~4 | dB | 0 | 0 | -Infinity | 3 |
| SSB RSRP Note3 | 1~4 | dBm/SSB SCS | -94.65 | -94.65 | -Infinity | -91.65 |
| Io Note3 | 1~4 | dBm/9.36 MHz | -63.69 | -63.69 | -66.70 | -61.93 |
|  | 1~4 | dB | 0 | 0 | -Infinity | 3 |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.20.5.3.2.3 Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19F.1.1 and relative accuracy requirement in clause 10.1.19F.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.20.5.3.3 CSI-RS based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is used for 1Rx (e)RedCap UE with NTN

##### A.20.5.3.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5E.4.2, with the testing configurations for NR cells served by satellite access node (SAN)  in table A.20.5.3.3.1-1.

Table A.20.5.3.3.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test for satellite access

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. Note 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.5.3.3.2 Test parameters

There is one cells in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.20.5.3.3.2-1 and table A.20.5.3.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (0 for Config 1, 2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.20.5.3.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.20.5.3.3.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB GSCN | 1~4 |  | freq1 |
| Duplex mode | 1, 2 |  | FDD |
|  | 3, 4 |  | HD-FDD |
| TDD Configuration | 1~4 |  | N/A |
| BWchannel | 1~4 | MHz | 10: NRB,c = 52 |
| Satellite information | 1, 3 |  | SSC.1 |
|  | 2, 4 |  | SSC.2 |
| PDSCH Reference measurement channel | 1~4 |  | SR.1.1 FDD |
| RMSI CORESET Reference Channel | 1~4 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel | 1~4 |  | CCR.1.1 FDD |
| SSB configuration | 1~4 |  | SSB.3 FR1 |
| CSI-RS configuration | 1~4 |  | CSI-RS 1.3 FDD |
| OCNG Patterns | 1~4 |  | OP.1 |
| TRS Configuration | 1~4 |  | TRS.1.1 FDD |
| DRX configuration | 1~4 |  | DRX.3 |
| Initial BWP Configuration | 1~4 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1~4 |  | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration | 1~4 |  | SMTC.1 |
| DRX configuration | 1~4 |  | Off |
| reportConfigType | 1~4 |  | aperiodic |
| reportQuantity | 1~4 |  | cri-RSRP |
| Number of reported RS | 1~4 |  | 2 |
| qcl-Info | 1~4 |  | SSB#0 for resource#0 |
|  |  |  | SSB#1 for resource#1 |
| reportSlotOffsetList | 1~4 | slots | 8 |
| T1 | 1~4 | s | 5 |
| EPRE ratio of PSS to SSS | 1~4 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1~4 |  | AWGN |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |

Table A.20.5.3.3.2-2: CSI-RS specific test parameters

| Parameter | Config | Unit | CSI-RS#0 | CSI-RS#1 |
| --- | --- | --- | --- | --- |
| Note1 | 1~4 | dBm/15 kHz | -94.65 |  |
| Note1 | 1~4 | dBm/SSB SCS | -94.65 |  |
|  |  |  |  |  |
|  | 1~4 | dB | 0 | 3 |
| CSI-RS RSRP Note2 | 1~4 | dBm/SSB SCS | -94.65 | -91.65 |
|  |  |  |  |  |
| Io Note2 | 1~4 | dBm/9.36 MHz | -63.69 | -61.93 |
|  |  |  |  |  |
|  | 1~4 | dB | 0 | 3 |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: CSI-RS RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |

##### A.20.5.3.3.3 Test Requirements

After 80ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.19F.1.1 and relative accuracy requirement in clause 10.1.19F.1.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.20.5.3.4 CSI-RS based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is used for 2Rx (e)RedCap UE with NTN

##### A.20.5.3.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5E.4.2, with the testing configurations for NR cells served by satellite access node (SAN) in table A.20.5.3.4.1-1.

Table A.20.5.3.4.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test for satellite access

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 3 | GSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 4 | NGSO, NR HD-FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. Note 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.5.3.4.2 Test parameters

There is one cells in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.20.5.3.4.2-1 and table A.20.5.3.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (0 for Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.20.5.3.4.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.20.5.3.4.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB GSCN | 1~4 |  | freq1 |
| Duplex mode | 1, 2 |  | FDD |
|  | 3, 4 |  | HD-FDD |
| TDD Configuration | 1~4 |  | N/A |
| BWchannel | 1~4 | MHz | 10: NRB,c = 52 |
| Satellite information | 1, 3 |  | SSC.1 |
|  | 2, 4 |  | SSC.2 |
| PDSCH Reference measurement channel | 1~4 |  | SR.1.1 FDD |
| RMSI CORESET Reference Channel | 1~4 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel | 1~4 |  | CCR.1.1 FDD |
| SSB configuration | 1~4 |  | SSB.3 FR1 |
| CSI-RS configuration | 1~4 |  | CSI-RS 1.3 FDD |
| OCNG Patterns | 1~4 |  | OP.1 |
| TRS Configuration | 1~4 |  | TRS.1.1 FDD |
| Initial BWP Configuration | 1~4 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1~4 |  | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration | 1~4 |  | SMTC.1 |
| DRX configuration | 1~4 |  | DRX.3 |
| reportConfigType | 1~4 |  | aperiodic |
| reportQuantity | 1~4 |  | cri-RSRP |
| Number of reported RS | 1~4 |  | 2 |
| qcl-Info | 1~4 |  | SSB#0 for resource#0 |
|  |  |  | SSB#1 for resource#1 |
| reportSlotOffsetList | 1~4 | slots | 8 |
| T1 | 1~4 | s | 5 |
| EPRE ratio of PSS to SSS | 1~4 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1~4 |  | AWGN |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |

Table A.20.5.3.4.2-2: CSI-RS specific test parameters

| Parameter | Config | Unit | CSI-RS#0 | CSI-RS#1 |  |
| --- | --- | --- | --- | --- | --- |
| Note1 | 1, 2 | dBm/15 kHz | -94.65 |  |  |
| Note1 | 1, 2 | dBm/SSB SCS | -94.65 |  |  |
|  |  |  |  |  |  |
|  | 1, 2 | dB | 0 | 3 |  |
| CSI-RS RSRP Note2 | 1, 2 | dBm/SSB SCS | -94.65 | -91.65 |  |
|  |  |  |  |  |  |
| Io Note2 | 1, 2 | dBm/9.36 MHz | -63.69 | -61.93 |  |
|  |  |  |  |  |  |
|  | 1, 2 | dB | 0 | 3 |  |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2:  CSI-RS RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |

##### A.20.5.3.4.3 Test Requirements

After 80ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.19F.1.1 and relative accuracy requirement in clause 10.1.19F.1.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.6 Measurement Performance requirements

### A.20.6.1 SS-RSRP for SAN

#### A.20.6.1.1 SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE

##### A.20.6.1.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clauses 10.1.2D.1.1 and 10.1.2D.1.2 for intra-frequency measurements.

##### A.20.6.1.1.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.20.6.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.20.6.1.1.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.6.1.1.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.6.1.1.2-2: SS-RSRP Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Cell ID |  |  |  | 489 | 0 | 489 | 0 | 489 | 0 |
| SSB ARFCN |  |  |  | freq1 |  | freq1 |  | freq1 |  |
| BWchannel |  | Config 1,2,3,4 | MHz | 10: NPRB,c = 52 |  |  |  |  |  |
| BWP BW |  | Config 1,2,3,4 |  | 10: NPRB,c = 52 |  |  |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |  |  |
| Satellite information |  | Config 1,3 |  | SSC.1 | NSC.1 | SSC.1 | NSC.1 | SSC.1 | NSC.1 |
|  |  | Config 2,4 |  | SSC.2 | NSC.2 | SSC.2 | NSC.2 | SSC.2 | NSC.2 |
| TRS configuration |  | Config 1,2,3,4 |  | TRS.1.1 FDD | NA | TRS.1.1 FDD | NA | TRS.1.1 FDD | NA |
| DRX Cycle |  | Config 1,2,3,4 | ms | Not Applicable |  |  |  |  |  |
| PDSCH Reference measurement channel |  | Config 1,2,3,4 |  | SR.1.1 FDD | - | SR.1.1 FDD | - | SR.1.1 FDD | - |
| RMSI CORESET Reference Channel |  | Config 1,2,3,4 |  | CR.1.1 FDD | - | CR.1.1 FDD | - | CR.1.1 FDD | - |
| Control channel RMC |  | Config 1,2,3,4 |  | CCR.1.1 FDD | - | CCR.1.1 FDD | - | CCR.1.1 FDD | - |
| SSB configuration |  | Config 1,2,3,4 |  | SSB.1 FR1 | SSB.1 FR1 | SSB.1 FR1 | SSB.1 FR1 | SSB.1 FR1 | SSB.1 FR1 |
| Time offset with Cell 1 |  | Config 1,2,3,4 | ms | - | 3 | - | 3 | - | 3 |
| SMTC configuration |  | Config 1,2,3,4 |  | SMTC.2 |  |  |  |  |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2,3,4 | kHz | 15 kHz |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 | R_FDD_SAB_FR1_A | dBm/15Khz | -106 |  | -88 |  | -114 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 |  | dBm/SCS | -106 |  | -88 |  | Same as Noc/15 kHz |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 2.46 | -5.97 | 2.46 | -5.97 | -0.01 | -4.76 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 6 | 1 | 6 | 1 | 3 | 0 |
| SS-RSRPNote3 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/SCS | -100 | -105 | -82 | -87 | -111.00 | -114.00 |
| IoNote3 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/9.36 MHz | -70.09 |  | -52.09 |  | -80.03 |  |
| Propagation condition |  |  | - | AWGN |  |  |  |  |  |
| Antenna configuration |  |  |  | 1x1 |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |  |  |  |  |  |

##### A.20.6.1.1.3 Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.2D.1.1 and relative requirement in clause 10.1D.2.1.2 for 1Rx (e)RedCap UE.

#### A.20.6.1.2 SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE

##### A.20.6.1.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clauses 10.1.2D.1.1 and 10.1.2D.1.2 for intra-frequency measurements.

##### A.20.6.1.2.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.20.6.1.2.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.20.6.1.2.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.6.1.2.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.6.1.2.2-2: SS-RSRP Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Cell ID |  |  |  | 489 | 0 | 489 | 0 | 489 | 0 |
| SSB ARFCN |  |  |  | freq1 |  | freq1 |  | freq1 |  |
| BWchannel |  | Config 1,2,3,4 | MHz | 10: NPRB,c = 52 |  |  |  |  |  |
| BWP BW |  | Config 1,2,3,4 |  | 10: NPRB,c = 52 |  |  |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |  |  |
| Satellite information |  | Config 1,3 |  | SSC.1 | NSC.1 | SSC.1 | NSC.1 | SSC.1 | NSC.1 |
|  |  | Config 2,4 |  | SSC.2 | NSC.2 | SSC.2 | NSC.2 | SSC.2 | NSC.2 |
| TRS configuration |  | Config 1,2,3,4 |  | TRS.1.1 FDD | NA | TRS.1.1 FDD | NA | TRS.1.1 FDD | NA |
| DRX Cycle |  | Config 1,2,3,4 | ms | Not Applicable |  |  |  |  |  |
| PDSCH Reference measurement channel |  | Config 1,2,3,4 |  | SR.1.1 FDD | - | SR.1.1 FDD | - | SR.1.1 FDD | - |
| RMSI CORESET Reference Channel |  | Config 1,2,3,4 |  | CR.1.1 FDD | - | CR.1.1 FDD | - | CR.1.1 FDD | - |
| Control channel RMC |  | Config 1,2,3,4 |  | CCR.1.1 FDD | - | CCR.1.1 FDD | - | CCR.1.1 FDD | - |
| SSB configuration |  | Config 1,2,3,4 |  | SSB.1 FR1 | SSB.1 FR1 | SSB.1 FR1 | SSB.1 FR1 | SSB.1 FR1 | SSB.1 FR1 |
| Time offset with Cell 1 |  | Config 1,2,3,4 | ms | - | 3 | - | 3 | - | 3 |
| SMTC configuration |  | Config 1,2,3,4 |  | SMTC.2 |  |  |  |  |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2,3,4 | kHz | 15 kHz |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 | R_FDD_SAB_FR1_A | dBm/15Khz | -106 |  | -88 |  | -114 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 |  | dBm/SCS | -106 |  | -88 |  | Same as Noc/15 kHz |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 2.46 | -5.97 | 2.46 | -5.97 | -0.01 | -4.76 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 6 | 1 | 6 | 1 | 3 | 0 |
| SS-RSRPNote3 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/SCS | -100 | -105 | -82 | -87 | -111.00 | -114.00 |
| IoNote3 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/9.36 MHz | -70.09 |  | -52.09 |  | -80.03 |  |
| Propagation condition |  |  | - | AWGN |  |  |  |  |  |
| Antenna configuration |  |  |  | 1x2 |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |  |  |  |  |  |

##### A.20.6.1.2.3 Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.2D.1.1 and relative requirement in clause 10.1.2D.1.2 for 2Rx (e)RedCap UE.

#### A.20.6.1.3 SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE

##### A.20.6.1.3.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clauses 10.1.4D.1.1 and 10.1.4D.1.2 for inter-frequency measurements with the testing configurations for NR cells in table A.20.6.1.3.1-1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.6.1.3.1-1: Applicable NR configurations for FR1 inter-frequency SS-RSRP accuracy test

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.6.1.3.2 Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.20.6.1.3.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.20.6.1.3.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.20.6.1.3.2-1: SS-RSRP inter-frequency test parameters

| Parameter |  | Config | Unit | Test 1 |  |  | Test 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 |  | Cell 2 | Cell 1 |  | Cell 2 |
| SSB ARFCN |  | 1, 2, 3, 4 |  | freq1 |  | freq2 | freq1 |  | freq2 |
| BWchannel |  | 1, 2, 3, 4 | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |  |  |
| PDSCH Reference measurement channel |  | 1, 2, 3, 4 |  | SR.1.1 FDD |  | - | SR.1.1 FDD |  | - |
| RMSI CORESET Reference Channel |  | 1, 2, 3, 4 |  | CR.1.1 FDD |  | - | CR.1.1 FDD |  | - |
| Dedicated CORESET Reference Channel |  | 1, 2, 3, 4 |  | CCR.1.1 FDD |  | - | CCR.1.1 FDD |  | - |
| SSB configuration |  | 1, 2, 3, 4 |  | SSB.1 FR1 |  |  | SSB.1 FR1 |  |  |
| OCNG Patterns |  | 1, 2, 3, 4 |  | OP.1 |  |  | OP.1 |  |  |
| TRS configuration |  | 1, 2, 3, 4 |  | TRS.1.1 FDD |  | - | TRS.1.1 FDD |  |  |
| Initial BWP Configuration |  | 1, 2, 3, 4 |  | DLBWP.0.1ULBWP.0.1 |  |  | DLBWP.0.1ULBWP.0.1 |  |  |
| Dedicated BWP configuration |  | 1, 2, 3, 4 |  | DLBWP.1.1ULBWP.1.1 |  |  | DLBWP.1.1ULBWP.1.1 |  |  |
| Satellite information |  | 1, 3 |  | SSC.1 | NSC.1 |  | SSC.1 | NSC.1 |  |
|  |  | 2, 4 |  | SSC.2 | NSC.2 |  | SSC.2 | NSC.2 |  |
| Time offset with Cell 1 |  | 1, 2, 3, 4 | ms | - | 3 |  | - | 3 |  |
| SMTC configuration |  | 1, 2, 3, 4 |  | SMTC.2 |  |  | SMTC.2 |  |  |
| EPRE ratio of PSS to SSS |  | 1, 2, 3, 4 | dB | 0 |  | 0 | 0 |  | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |  |  |  |  |
| Note2 | NR_FDD_SAB_FR1_A | 1,2,3,4 | dBm/15 kHz | -94.65 |  |  | (![](media_svg/image2.svg) [公式≈: ^{N}oc] for Channel 2 +8 dB) |  | -115 |
| Note2 | NR_FDD_SAB_FR1_A | 1,2,3,4 | dBm/SSB SCS | -94.65 |  |  | (![](media_svg/image2.svg) [公式≈: ^{N}oc] for Channel 2 +8 dB) |  | -115 |
|  |  | 1,2,3,4 | dB | 10 |  | 10 | 13 |  | -3 |
| SS-RSRPNote3 | NR_FDD_SAB_FR1_A | 1,2,3,4 | dBm/SCS | -84.65 |  |  | (RSRP for Cell 2 +25 dB) |  | -118.00 |
| IoNote3 | NR_FDD_SAB_FR1_A | 1,2,3,4 | dBm/9.36 MHz | -56.28 |  |  | (Io for Channel 2 +19.75 dB) |  | -85.28 |
|  |  | 1,2,3,4 | dB | 10 |  | 10 | 13 |  | -3 |
| Propagation condition |  | 1,2,3,4 | - | AWGN |  |  | AWGN |  |  |
| Antenna configuration |  | 1,2,3,4 |  | 1x1 |  |  | 1x1 |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |  |  |  |  |  |

##### A.20.6.1.3.3 Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.4D.1.1 and relative requirement in clause 10.1.4D.1.2 for 1Rx (e)RedCap UE.

#### A.20.6.1.4 SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE

##### A.20.6.1.4.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clauses 10.1.4D.1.1 and 10.1.4D.1.2 for inter-frequency measurements with the testing configurations for NR cells in table A.20.6.1.4.1-1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.6.1.4.1-1: Applicable NR configurations for FR1 inter-frequency SS-RSRP accuracy test

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.6.1.4.2 Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.20.6.1.4.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.20.6.1.4.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.20.6.1.4.2-1: SS-RSRP inter-frequency test parameters

| Parameter |  | Config | Unit | Test 1 |  |  | Test 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 |  | Cell 2 | Cell 1 |  | Cell 2 |
| SSB ARFCN |  | 1, 2, 3, 4 |  | freq1 |  | freq2 | freq1 |  | freq2 |
| BWchannel |  | 1, 2, 3, 4 | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |  |  |
| PDSCH Reference measurement channel |  | 1, 2, 3, 4 |  | SR.1.1 FDD |  | - | SR.1.1 FDD |  | - |
| RMSI CORESET Reference Channel |  | 1, 2, 3, 4 |  | CR.1.1 FDD |  | - | CR.1.1 FDD |  | - |
| Dedicated CORESET Reference Channel |  | 1, 2, 3, 4 |  | CCR.1.1 FDD |  | - | CCR.1.1 FDD |  | - |
| SSB configuration |  | 1, 2, 3, 4 |  | SSB.1 FR1 |  |  | SSB.1 FR1 |  |  |
| OCNG Patterns |  | 1, 2, 3, 4 |  | OP.1 |  |  | OP.1 |  |  |
| TRS configuration |  | 1, 2, 3, 4 |  | TRS.1.1 FDD |  | - | TRS.1.1 FDD |  |  |
| Initial BWP Configuration |  | 1, 2, 3, 4 |  | DLBWP.0.1ULBWP.0.1 |  |  | DLBWP.0.1ULBWP.0.1 |  |  |
| Dedicated BWP configuration |  | 1, 2, 3, 4 |  | DLBWP.1.1ULBWP.1.1 |  |  | DLBWP.1.1ULBWP.1.1 |  |  |
| Satellite information |  | 1, 3 |  | SSC.1 | NSC.1 |  | SSC.1 | NSC.1 |  |
|  |  | 2, 4 |  | SSC.2 | NSC.2 |  | SSC.2 | NSC.2 |  |
| Time offset with Cell 1 |  | 1, 2, 3, 4 | ms | - | 3 |  | - | 3 |  |
| SMTC configuration |  | 1, 2, 3, 4 |  | SMTC.2 |  |  | SMTC.2 |  |  |
| EPRE ratio of PSS to SSS |  | 1, 2, 3, 4 | dB | 0 |  | 0 | 0 |  | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |  |  |  |  |
| Note2 | NR_FDD_SAB_FR1_A | 1,2,3,4 | dBm/15 kHz | -94.65 |  |  | (![](media_svg/image2.svg) [公式≈: ^{N}oc] for Channel 2 +8 dB) |  | -115 |
| Note2 | NR_FDD_SAB_FR1_A | 1,2,3,4 | dBm/SSB SCS | -94.65 |  |  | (![](media_svg/image2.svg) [公式≈: ^{N}oc] for Channel 2 +8 dB) |  | -115 |
|  |  | 1,2,3,4 | dB | 10 |  | 10 | 13 |  | -3 |
| SS-RSRPNote3 | NR_FDD_SAB_FR1_A | 1,2,3,4 | dBm/SCS | -84.65 |  |  | (RSRP for Cell 2 +25 dB) |  | -118.00 |
| IoNote3 | NR_FDD_SAB_FR1_A | 1,2,3,4 | dBm/9.36 MHz | -56.28 |  |  | (Io for Channel 2 +19.75 dB) |  | -85.28 |
|  |  | 1,2,3,4 | dB | 10 |  | 10 | 13 |  | -3 |
| Propagation condition |  | 1,2,3,4 | - | AWGN |  |  | AWGN |  |  |
| Antenna configuration |  | 1,2,3,4 |  | 1x2 |  |  | 1x2 |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |  |  |  |  |  |

##### A.20.6.1.4.3 Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.4D.1.1 and relative requirement in clause 10.1.4D.1.2 for 2Rx (e)RedCap UE.


### A.20.6.2 SS-RSRQ

#### A.20.6.2.1 SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 1Rx RedCap UE

##### A.20.6.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 10.1.7D.

##### A.20.6.2.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.20.6.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.20.6.2.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.20.6.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.6.2.1.2-2: SS-RSRQ Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |  |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 |  | Cell 2 |  | Cell 1 | Cell 2 |
| SSB ARFCN |  |  |  | freq1 |  | freq1 |  |  |  | freq1 |  |
| Duplex mode |  | Config 1,2 |  | FDD |  |  |  |  |  |  |  |
|  |  | Config 3,4 |  | HD-FDD |  |  |  |  |  |  |  |
| BWchannel |  | Config 1,2,3,4 | MHz | 10: NPRB,c = 52 |  |  |  |  |  |  |  |
| Gap Pattern ID |  |  |  | 0 |  |  |  |  |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |  |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |  |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |  |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |  |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |  |  |  |
| Satellite information |  | Config 1,3 |  | SSC.1 | NSC.1 | SSC.1 |  | NSC.1 |  | SSC.1 | NSC.1 |
|  |  | Config 2,4 |  | SSC.2 | NSC.2 | SSC.2 |  | NSC.2 |  | SSC.2 | NSC.2 |
| PDSCH Reference measurement channel |  | Config 1,2,3,4 |  | SR.1.1 FDD | - | SR.1.1 FDD |  | - |  | SR.1.1 FDD | - |
| RMSI CORESET Reference Channel |  | Config 1,2,3,4 |  | CR.1.1 FDD | - | CR.1.1 FDD |  | - |  | CR.1.1 FDD |  |
| Control Channel RMC |  | Config 1,2,3,4 |  | CCR.1.1 FDD | - | CCR.1.1 FDD |  | - |  | CCR.1.1 FDD | - |
| TRS Configuration |  | Config 1,2,3,4 |  | TRS.1.1 FDD | - | TRS.1.1 FDD |  | - |  | TRS.1.1 FDD | - |
| OCNG Patterns |  |  |  | OP. 1 |  |  |  |  |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |  |  |  |  |
| Time offset with Cell 1 |  | Config 1,2,3,4 | ms | - | 3 | - | 3 |  | - |  | 3 |
| SMTC configuration |  | Config 1,2,3,4 |  | SMTC.2 |  |  |  |  |  |  |  |
| SSB configuration |  | Config 1,2,3,4 |  | SSB.1 FR1 |  |  |  |  |  |  |  |
| CSI-RS for tracking |  | Config 1,2,3,4 |  | TRS.1.1 FDD |  |  |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2,3,4 | kHz | 15 kHz |  |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 |  | 0 |  | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/15 kHz | -85 |  | -101 |  |  |  | -114 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/SCS | -85 |  | -101 |  |  |  | -114 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.76 |  | -4.7 |  |  |  | -5..46 | -5.46 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 | 3 | -2.9 |  | -2.9 |  | -4 | -4 |
| SS-RSRPNote3 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/SCS | -82 | -82 | -103.9 |  | -103.9 |  | -118 | -118 |
| SS-RSRQ Note3 |  | NR_FDD_SAB_FR1_A | dB | -14.84 | -14.84 | -14.84 |  | -16.76 |  | -16.76 | -17.34 |
| IoNote3 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/9.36 MHz | -50 |  | -70 |  |  |  | -83.5 |  |
| Propagation condition |  |  | - | AWGN | AWGN | AWGN |  | AWGN |  | AWGN | AWGN |
| Antenna configuration |  |  |  | 1x1 | 1x1 | 1x1 |  | 1x1 |  | 1x1 | 1x1 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRQ, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRQ, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2.NOTE 6: void |  |  |  |  |  |  |  |  |  |  |  |

##### A.20.6.2.1.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirement in clause 10.1.7D.1.1 for 1Rx (e)RedCap UE.

#### A.20.6.2.2 SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 2Rx RedCap UE

##### A.20.6.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 10.1.7D.

##### A.20.6.2.2.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.20.6.2.2.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.20.6.2.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.20.6.2.2.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.6.2.2.2-2: SS-RSRQ Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |  |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 |  | Cell 2 |  | Cell 1 | Cell 2 |
| SSB ARFCN |  |  |  | freq1 |  | freq1 |  |  |  | freq1 |  |
| Duplex mode |  | Config 1,2,3,4 |  | FDD |  |  |  |  |  |  |  |
| BWchannel |  | Config 1,2,3,4 | MHz | 10: NPRB,c = 52 |  |  |  |  |  |  |  |
| Gap Pattern ID |  |  |  | 0 |  |  |  |  |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |  |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |  |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |  |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |  |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |  |  |  |
| Satellite information |  | Config 1,3 |  | SSC.1 | NSC.1 | SSC.1 |  | NSC.1 |  | SSC.1 | NSC.1 |
|  |  | Config 2,4 |  | SSC.2 | NSC.2 | SSC.2 |  | NSC.2 |  | SSC.2 | NSC.2 |
| PDSCH Reference measurement channel |  | Config 1,2,3,4 |  | SR.1.1 FDD | - | SR.1.1 FDD |  | - |  | SR.1.1 FDD | - |
| RMSI CORESET Reference Channel |  | Config 1,2,3,4 |  | CR.1.1 FDD | - | CR.1.1 FDD |  | - |  | CR.1.1 FDD |  |
| Control Channel RMC |  | Config 1,2,3,4 |  | CCR.1.1 FDD | - | CCR.1.1 FDD |  | - |  | CCR.1.1 FDD | - |
| TRS Configuration |  | Config 1,2,3,4 |  | TRS.1.1 FDD | - | TRS.1.1 FDD |  | - |  | TRS.1.1 FDD | - |
| OCNG Patterns |  |  |  | OP. 1 |  |  |  |  |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |  |  |  |  |
| Time offset with Cell 1 |  | Config 1,2,3,4 | ms | - | 3 | - | 3 |  | - |  | 3 |
| SMTC configuration |  | Config 1,2,3,4 |  | SMTC.2 |  |  |  |  |  |  |  |
| SSB configuration |  | Config 1,2,3,4 |  | SSB.1 FR1 |  |  |  |  |  |  |  |
| CSI-RS for tracking |  | Config 1,2,3,4 |  | TRS.1.1 FDD |  |  |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2,3,4 | kHz | 15 kHz |  |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 |  | 0 |  | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/15 kHz | -85 |  | -101 |  |  |  | -114 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/SCS | -85 |  | -101 |  |  |  | -114 |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.76 |  | -4.7 |  |  |  | -5..46 | -5.46 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 | 3 | -2.9 |  | -2.9 |  | -4 | -4 |
| SS-RSRPNote3 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/SCS | -82 | -82 | -103.9 |  | -103.9 |  | -118 | -118 |
| SS-RSRQ Note3 |  | NR_FDD_SAB_FR1_A | dB | -14.84 | -14.84 | -14.84 |  | -16.76 |  | -16.76 | -17.34 |
| IoNote3 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/9.36 MHz | -50 |  | -70 |  |  |  | -83.5 |  |
| Propagation condition |  |  | - | AWGN | AWGN | AWGN |  | AWGN |  | AWGN | AWGN |
| Antenna configuration |  |  |  | 1x2 | 1x2 | 1x2 |  | 1x2 |  | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRQ, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRQ, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2.NOTE 6: void |  |  |  |  |  |  |  |  |  |  |  |

##### A.20.6.2.2.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirement in clause 10.1.7D.1.1 for 2Rx (e)RedCap UE.

#### A.20.6.2.3 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 1Rx RedCap UE

##### A.20.6.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 10.1.7D.

##### A.20.6.2.3.2 Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.20.6.2.3.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.20.6.2.3.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.20.6.2.3.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.6.2.3.2-2: SS-RSRQ Inter frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |  | Test 3 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |  | Cell 1 |  | Cell 2 |
| SSB ARFCN |  |  |  | freq1 | freq2 | freq1 | freq2 |  | freq1 |  | freq2 |
| Duplex mode |  | Config 1,2 |  | FDD |  |  |  |  |  |  |  |
|  |  | Config 3,4 |  | HD-FDD |  |  |  |  |  |  |  |
| BWchannel |  | Config 1,2,3,4 | MHz | 10: NPRB,c = 52 |  |  |  |  |  |  |  |
| Gap pattern ID |  | Config 1,2,3,4 |  | 0 |  |  |  |  |  |  |  |
| BWP BW |  | Config 1,2,3,4 |  | 10: NPRB,c = 52 |  |  |  |  |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |  |  |  |
| Satellite information |  | Config 1,3 |  | SSC.1 | NSC.1 | SSC.1 | NSC.1 |  | SSC.1 |  | NSC.1 |
|  |  | Config 2,4 |  | SSC.2 | NSC.2 | SSC.2 | NSC.2 |  | SSC.2 |  | NSC.2 |
| PDSCH Reference measurement channel |  | Config 1,2,3,4 |  | SR.1.1 FDD | - | SR.1.1 FDD | - |  | SR.1.1 FDD |  | - |
| RMSI CORESET Reference Channel |  | Config 1,2,3,4 |  | CR.1.1 FDD | - | R.1.1 FDD | - |  | CR.1.1 FDD |  |  |
| Dedicated CORESET Reference Channel |  | Config 1,2,3,4 |  | CCR.1.1 FDD | - | CCR.1.1 FDD | - |  | CCR.1.1 FDD |  | - |
| TRS Configuration |  | Config 1,2,3,4 |  | TRS.1.1 FDD | - | TRS.1.1 FDD | - |  | TRS.1.1 FDD |  | - |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |  |  |  |  |
| Time offset with Cell 1 |  | Config 1,2,3,4 | ms | - | 3 | - | 3 | - |  | 3 |  |
| SMTC configuration |  | Config 1,2,3,4 |  | SMTC pattern 2 |  |  |  |  |  |  |  |
| SSB configuration |  | Config 1,2,3,4 |  | SSB pattern 1 in FR1 |  |  |  |  |  |  |  |
| CSI-RS for tracking |  | Config 1,2,3,4 |  | TRS.1.1 FDD |  |  |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2,3,4 | kHz | 15 kHz |  |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 |  | 0 |  | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/15 kHz | -80.18 |  | -106 |  |  | -116 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/15 kHz | -80.18 |  | -106 |  |  | -116 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.75 |  | -1.75 |  |  | 3 |  | -1.75 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -1.75 |  | -1.75 |  |  | 3 |  | -1.75 |
| SS-RSRPNote3 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/SCS | -81.93 | -81.93 | -107.75 | -107.75 |  | -113 |  | -117.75 |
| SS-RSRQNote3 |  | NR_FDD_SAB_FR1_A | dB | -14.77 | -14.77 | -14.76 | -14.76 |  | -12.56 |  | -14.76 |
| IoNote3 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/9.36 MHz | -50 |  | -75.83 |  |  | -83.28 |  | -85.83 |
| Propagation condition |  |  | - | AWGN | AWGN | AWGN | AWGN |  | AWGN |  | AWGN |
| Antenna configuration |  |  |  | 1x1 | 1x1 | 1x1 | 1x1 |  | 1x1 |  | 1x1 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRQ, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRQ, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2. |  |  |  |  |  |  |  |  |  |  |  |

##### A.20.6.2.3.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil absolute requirement in clause 10.1.9D.1.1 and relative requirement in clause 10.1.9D.1.2 for 1Rx (e)RedCap UE.

#### A.20.6.2.4 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 2Rx RedCap UE

##### A.20.6.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 10.1.7D.

##### A.20.6.2.4.2 Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.20.6.2.4.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.20.6.2.4.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.20.6.2.4.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.6.2.4.2-2: SS-RSRQ Inter frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |  | Test 3 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |  | Cell 1 |  | Cell 2 |
| SSB ARFCN |  |  |  | freq1 | freq2 | freq1 | freq2 |  | freq1 |  | freq2 |
| Duplex mode |  | Config 1,2 |  | FDD |  |  |  |  |  |  |  |
|  |  | Config 3,4 |  | HD-FDD |  |  |  |  |  |  |  |
| BWchannel |  | Config 1,2,3,4 | MHz | 10: NPRB,c = 52 |  |  |  |  |  |  |  |
| Gap pattern ID |  | Config 1,2,3,4 |  | 0 |  |  |  |  |  |  |  |
| BWP BW |  | Config 1,2,3,4 |  | 10: NPRB,c = 52 |  |  |  |  |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |  |  |  |
| Satellite information |  | Config 1,3 |  | SSC.1 | NSC.1 | SSC.1 | NSC.1 |  | SSC.1 |  | NSC.1 |
|  |  | Config 2,4 |  | SSC.2 | NSC.2 | SSC.2 | NSC.2 |  | SSC.2 |  | NSC.2 |
| PDSCH Reference measurement channel |  | Config 1,2,3,4 |  | SR.1.1 FDD | - | SR.1.1 FDD | - |  | SR.1.1 FDD |  | - |
| RMSI CORESET Reference Channel |  | Config 1,2,3,4 |  | CR.1.1 FDD | - | R.1.1 FDD | - |  | CR.1.1 FDD |  |  |
| Dedicated CORESET Reference Channel |  | Config 1,2,3,4 |  | CCR.1.1 FDD | - | CCR.1.1 FDD | - |  | CCR.1.1 FDD |  | - |
| TRS Configuration |  | Config 1,2,3,4 |  | TRS.1.1 FDD | - | TRS.1.1 FDD | - |  | TRS.1.1 FDD |  | - |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |  |  |  |  |
| Time offset with Cell 1 |  | Config 1,2,3,4 | ms | - | 3 | - | 3 | - |  | 3 |  |
| SMTC configuration |  | Config 1,2,3,4 |  | SMTC pattern 2 |  |  |  |  |  |  |  |
| SSB configuration |  | Config 1,2,3,4 |  | SSB pattern 1 in FR1 |  |  |  |  |  |  |  |
| CSI-RS for tracking |  | Config 1,2,3,4 |  | TRS.1.1 FDD |  |  |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2,3,4 | kHz | 15 kHz |  |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 |  | 0 |  | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/15 kHz | -80.18 |  | -106 |  |  | -116 |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/15 kHz | -80.18 |  | -106 |  |  | -116 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.75 |  | -1.75 |  |  | 3 |  | -1.75 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -1.75 |  | -1.75 |  |  | 3 |  | -1.75 |
| SS-RSRPNote3 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/SCS | -81.93 | -81.93 | -107.75 | -107.75 |  | -113 |  | -117.75 |
| SS-RSRQNote3 |  | NR_FDD_SAB_FR1_A | dB | -14.77 | -14.77 | -14.76 | -14.76 |  | -12.56 |  | -14.76 |
| IoNote3 | Config 1,2,3,4 | NR_FDD_SAB_FR1_A | dBm/9.36 MHz | -50 |  | -75.83 |  |  | -83.28 |  | -85.83 |
| Propagation condition |  |  | - | AWGN | AWGN | AWGN | AWGN |  | AWGN |  | AWGN |
| Antenna configuration |  |  |  | 1x2 | 1x2 | 1x2 | 1x2 |  | 1x2 |  | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRQ, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRQ, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2. |  |  |  |  |  |  |  |  |  |  |  |

##### A.20.6.2.4.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil absolute requirement in clause 10.1.9D.1.1 and relative requirement in clause 10.1.9D.1.2 for 2Rx (e)RedCap UE.

### A.20.6.3 SS-SINR

#### A.20.6.3.1 SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE

##### A.20.6.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 10.1.12D.1.1.

##### A.20.6.3.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.20.6.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.20.6.3.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.20.6.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2:  If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.6.3.1.2-2: SS-SINR Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| SSB ARFCN |  |  |  | freq1 |  | freq1 |  |
| Duplex mode |  | Config 1, 2 |  | FDD |  |  |  |
|  |  | Config 3, 4 |  | HD-FDD |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |  |  |
| Satellite information |  | Config 1, 3 |  | SSC.1 | NSC.1 | SSC.1 | NSC.1 |
|  |  | Config 2, 4 |  | SSC.2 | NSC.2 | SSC.2 | NSC.2 |
| TRS configuration |  | Config 1, 2, 3, 4 |  | TRS.1.1 FDD |  | TRS.1.1 FDD |  |
| PDSCH Reference measurement channel |  | Config 1, 2, 3, 4 |  | SR.1.1 FDD | - | SR.1.1 FDD | - |
| RMSI CORESET Reference Channel |  | Config 1, 2, 3, 4 |  | CR.1.1 FDD | - | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1, 2, 3, 4 |  | CCR.1.1 FDD | - | CCR.1.1 FDD | - |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |
| SMTC configuration |  | Config 1, 2, 3, 4 |  | SMTC.2 |  |  |  |
| Time offset with Cell 1 |  | Config 1, 2, 3, 4 | ms | - | 3 | - | 3 |
| SSB configuration |  | Config 1, 2, 3, 4 |  | SSB.1 FR1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2, 3, 4 | kHz | 15 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | NR_FDD_SAB_FR1_A | dBm/15 kHz | -93 |  | -116 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2, 3, 4 |  | dBm/SCS | -93 |  | Same as Noc for 15 kHz |  |
| ![](media_svg/image25.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 0 | -3.19 | -5.46 | -5.46 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4.54 | 2.66 | -4 | -4 |
| SS-RSRPNote3 | Config 1, 2, 3, 4 | NR_FDD_SAB_FR1_A | dBm/SCS | -88.46 | -90.34 | -120 | -120 |
| SS-SINR Note3 |  | NR_FDD_SAB_FR1_A | dB | 0 | -3.19 | -5.46 | -5.46 |
| IoNote3 | Config 1, 2, 3, 4 | NR_FDD_SAB_FR1_A | dBm/9.36 MHz | -57.5 |  | -85.51 |  |
| Propagation condition |  |  | - | AWGN |  |  |  |
| Antenna configuration |  |  | - | 1x1 |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2. |  |  |  |  |  |  |  |

##### A.20.6.3.1.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirement in clause 10.1.12D.1.1-1 for 1Rx (e)RedCap UE.

#### A.20.6.3.2 SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE

##### A.20.6.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 10.1.12D.1.1.

##### A.20.6.3.2.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.20.6.3.2.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.20.6.3.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.20.6.3.2.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.6.3.2.2-2: SS-SINR Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| SSB ARFCN |  |  |  | freq1 |  | freq1 |  |
| Duplex mode |  | Config 1, 2 |  | FDD |  |  |  |
|  |  | Config 3, 4 |  | HD-FDD |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |  |  |
| Satellite information |  | Config 1, 3 |  | SSC.1 | NSC.1 | SSC.1 | NSC.1 |
|  |  | Config 2, 4 |  | SSC.2 | NSC.2 | SSC.2 | NSC.2 |
| TRS configuration |  | Config 1, 2, 3, 4 |  | TRS.1.1 FDD |  | TRS.1.1 FDD |  |
| PDSCH Reference measurement channel |  | Config 1, 2, 3, 4 |  | SR.1.1 FDD | - | SR.1.1 FDD | - |
| RMSI CORESET Reference Channel |  | Config 1, 2, 3, 4 |  | CR.1.1 FDD | - | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1, 2, 3, 4 |  | CCR.1.1 FDD | - | CCR.1.1 FDD | - |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |
| SMTC configuration |  | Config 1, 2, 3, 4 |  | SMTC.2 |  |  |  |
| Time offset with Cell 1 |  | Config 1, 2, 3, 4 | ms | - | 3 | - | 3 |
| SSB configuration |  | Config 1, 2, 3, 4 |  | SSB.1 FR1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2, 3, 4 | kHz | 15 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 |  | NR_FDD_SAB_FR1_A | dBm/15 kHz | -93 |  | -116 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2, 3, 4 |  | dBm/SCS | -93 |  | Same as Noc for 15 kHz |  |
| ![](media_svg/image25.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 0 | -3.19 | -5.46 | -5.46 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4.54 | 2.66 | -4 | -4 |
| SS-RSRPNote3 | Config 1, 2, 3, 4 | NR_FDD_SAB_FR1_A | dBm/SCS | -88.46 | -90.34 | -120 | -120 |
| SS-SINR Note3 |  | NR_FDD_SAB_FR1_A | dB | 0 | -3.19 | -5.46 | -5.46 |
| IoNote3 | Config 1, 2, 3, 4 | NR_FDD_SAB_FR1_A | dBm/9.36 MHz | -57.5 |  | -85.51 |  |
| Propagation condition |  |  | - | AWGN |  |  |  |
| Antenna configuration |  |  | - | 1x2 |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2. |  |  |  |  |  |  |  |

##### A.20.6.3.2.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirement in clause 10.1.12D.1.1 for 2Rx (e)RedCap UE.

#### A.20.6.3.3 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE

##### A.20.6.3.3.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clauses 10.1.14D.1.1 and 10.1.14D.1.2.

##### A.20.6.3.3.2 Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.20.6.3.3.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.20.6.3.3.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.20.6.3.3.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.6.3.3.2-2: SS-SINR Inter frequency test parameters

| Parameter |  |  |  | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| SSB ARFCN |  |  |  |  | freq1 | freq2 | freq1 | freq2 | freq1 | freq2 |
| Duplex mode |  | Config 1, 2 |  |  | FDD |  |  |  |  |  |
|  |  | Config 3, 4 |  |  | HD-FDD |  |  |  |  |  |
| Downlink initial BWP configuration |  |  |  |  | DLBWP.0.1 |  |  |  |  |  |
| Downlink dedicated BWP configuration |  |  |  |  | DLBWP.1.1 |  |  |  |  |  |
| Uplink initial BWP configuration |  |  |  |  | ULBWP.0.1 |  |  |  |  |  |
| Uplink dedicated BWP configuration |  |  |  |  | ULBWP.1.1 |  |  |  |  |  |
| DRX Cycle configuration |  |  |  | ms | Not Applicable |  |  |  |  |  |
| Satellite information |  |  | Config 1, 3 |  | SSC.1 | NSC.1 | SSC.1 | NSC.1 | SSC.1 | NSC.1 |
|  |  |  | Config 2, 4 |  | SSC.2 | NSC.2 | SSC.2 | NSC.2 | SSC.2 | NSC.2 |
| Gap pattern ID |  |  |  |  | 0 | - | 0 | - | 0 | - |
| TRS configuration |  | Config 1, 2, 3, 4 |  |  | TRS.1.1 FDD |  | TRS.1.1 FDD |  | TRS.1.1 FDD |  |
| PDSCH Reference measurement channel |  | Config 1, 2, 3, 4 |  |  | SR.1.1 FDD | - | SR.1.1 FDD | - | SR.1.1 FDD | - |
| RMSI CORESET Reference Channel |  | Config 1, 2, 3, 4 |  |  | CR.1.1 FDD | - | CR.1.1 FDD | - | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1, 2, 3, 4 |  |  | CCR.1.1 FDD | - | CCR.1.1 FDD | - | CCR.1.1 FDD | - |
| OCNG Patterns |  |  |  |  | OP.1 |  |  |  |  |  |
| SS-RSSI-Measurement |  |  |  |  | Not Applicable |  |  |  |  |  |
| Time offset with Cell 1 |  | Config 1, 2, 3, 4 |  | ms | - | 3 | - | 3 | - | 3 |
| SMTC configuration |  | Config 1, 2, 3, 4 |  |  | SMTC pattern 2 |  |  |  |  |  |
| SSB configuration |  | Config 1, 2, 3, 4 |  |  | SSB.1 FR1 |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2, 3, 4 |  | kHz | 15 |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  |  | dB | 0 | 0 | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2, 3, 4 | NR_FDD_SAB_FR1_A |  | dBm/15 kHz | -88 |  | -108.5 |  | -119.5 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2, 3, 4 |  |  | dBm/SCS | -88 |  | -108.5 |  | Same as Noc for 15 kHz |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image26.svg) [公式≈: ^{Ê}s^{I}ot] |  |  |  | dB | -1.75 | -1.75 | 20 | 20 | -4.0 | -4.0 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  |  | dB | -1.75 |  | 20 |  | -4.0 |  |
| SS-RSRP Note3 | Config 1, 2, 3, 4 | NR_FDD_SAB_FR1_A |  | dBm/SCS | -89.75 |  | -88.5 |  | -123.5 |  |
| SS-SINRNote3 |  | NR_FDD_SAB_FR1_A |  | dB | -1.75 |  | 20 |  | -4.0 |  |
| IoNote3 | Config 1, 2, 3, 4 | NR_FDD_SAB_FR1_A |  | dBm/9.36 MHz | -57.83 |  | -60.5 |  | -90.09 |  |
| Propagation condition |  |  |  | - | AWGN |  |  |  |  |  |
| Antenna configuration |  |  |  | - | 1x1 |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2. |  |  |  |  |  |  |  |  |  |  |

##### A.20.6.3.3.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil absolute requirement in clause 10.1.14D.1.1-1 and relative requirement in clause 10.1.14D.1.2-1 for 1Rx (e)RedCap UE.

#### A.20.6.3.4 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE

##### A.20.6.3.4.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clauses 10.1.14D.1.1 and 10.1.14D.1.2.

##### A.20.6.3.4.2 Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.20.6.3.4.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.20.6.3.4.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.20.6.3.4.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

Table A.20.6.3.4.2-2: SS-SINR Inter frequency test parameters

| Parameter |  |  |  | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| SSB ARFCN |  |  |  |  | freq1 | freq2 | freq1 | freq2 | freq1 | freq2 |
| Duplex mode |  | Config 1, 2 |  |  | FDD |  |  |  |  |  |
|  |  | Config 3, 4 |  |  | HD-FDD |  |  |  |  |  |
| Downlink initial BWP configuration |  |  |  |  | DLBWP.0.1 |  |  |  |  |  |
| Downlink dedicated BWP configuration |  |  |  |  | DLBWP.1.1 |  |  |  |  |  |
| Uplink initial BWP configuration |  |  |  |  | ULBWP.0.1 |  |  |  |  |  |
| Uplink dedicated BWP configuration |  |  |  |  | ULBWP.1.1 |  |  |  |  |  |
| DRX Cycle configuration |  |  |  | ms | Not Applicable |  |  |  |  |  |
| Satellite information |  |  | Config 1, 3 |  | SSC.1 | NSC.1 | SSC.1 | NSC.1 | SSC.1 | NSC.1 |
|  |  |  | Config 2, 4 |  | SSC.2 | NSC.2 | SSC.2 | NSC.2 | SSC.2 | NSC.2 |
| Gap pattern ID |  |  |  |  | 0 | - | 0 | - | 0 | - |
| TRS configuration |  | Config 1, 2, 3, 4 |  |  | TRS.1.1 FDD |  | TRS.1.1 FDD |  | TRS.1.1 FDD |  |
| PDSCH Reference measurement channel |  | Config 1, 2, 3, 4 |  |  | SR.1.1 FDD | - | SR.1.1 FDD | - | SR.1.1 FDD | - |
| RMSI CORESET Reference Channel |  | Config 1, 2, 3, 4 |  |  | CR.1.1 FDD | - | CR.1.1 FDD | - | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1, 2, 3, 4 |  |  | CCR.1.1 FDD | - | CCR.1.1 FDD | - | CCR.1.1 FDD | - |
| OCNG Patterns |  |  |  |  | OP.1 |  |  |  |  |  |
| SS-RSSI-Measurement |  |  |  |  | Not Applicable |  |  |  |  |  |
| Time offset with Cell 1 |  | Config 1, 2, 3, 4 |  | ms | - | 3 | - | 3 | - | 3 |
| SMTC configuration |  | Config 1, 2, 3, 4 |  |  | SMTC pattern 2 |  |  |  |  |  |
| SSB configuration |  | Config 1, 2, 3, 4 |  |  | SSB.1 FR1 |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2, 3, 4 |  | kHz | 15 |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  |  | dB | 0 | 0 | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2, 3, 4 | NR_FDD_SAB_FR1_A |  | dBm/15 kHz | -88 |  | -108.5 |  | -119.5 |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2, 3, 4 |  |  | dBm/SCS | -88 |  | -108.5 |  | Same as Noc for 15 kHz |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image26.svg) [公式≈: ^{Ê}s^{I}ot] |  |  |  | dB | -1.75 | -1.75 | 20 | 20 | -4.0 | -4.0 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  |  | dB | -1.75 |  | 20 |  | -4.0 |  |
| SS-RSRP Note3 | Config 1, 2, 3, 4 | NR_FDD_SAB_FR1_A |  | dBm/SCS | -89.75 |  | -88.5 |  | -123.5 |  |
| SS-SINRNote3 |  | NR_FDD_SAB_FR1_A |  | dB | -1.75 |  | 20 |  | -4.0 |  |
| IoNote3 | Config 1, 2, 3, 4 | NR_FDD_SAB_FR1_A |  | dBm/9.36 MHz | -57.83 |  | -60.5 |  | -90.09 |  |
| Propagation condition |  |  |  | - | AWGN |  |  |  |  |  |
| Antenna configuration |  |  |  | - | 1x2 |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2. |  |  |  |  |  |  |  |  |  |  |

##### A.20.6.3.4.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil absolute requirement in clause 10.1.14D.1.1 and relative requirement in clause 10.1.14D.1.2 for 2Rx (e)RedCap UE.

### A.20.6.4 L1-RSRP measurement for beam reporting

#### A.20.6.4.1 SSB based L1-RSRP measurement for 1Rx RedCap UE

##### A.20.6.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 9.5E.4 and clause 10.1.19F.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.20.6.4.1.1-1.

Table A.20.6.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.6.4.1.2 Test parameters

In this set of test cases, there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.20.6.4.1.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.20.6.4.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.20.6.4.1.2-1: FR1 SSB based L1-RSRP test parameters

| Parameter |  | Config | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- | --- | --- |
| SSB ARFCN |  | 1, 2, 3, 4 |  | freq1 | freq1 |
| Duplex mode |  | 1, 2 |  | FDD | FDD |
|  |  | 3, 4 |  | HD-FDD | HD-FDD |
| TDD Configuration |  | 1, 2, 3, 4 |  | N/A | N/A |
| BWchannel |  | 1, 2, 3, 4 | MHz | 10: NPRB,c = 52 | 10: NPRB,c = 52 |
| Satellite information |  | 1, 3 |  | SSC.1 | NSC.1 |
|  |  | 2, 4 |  | SSC.2 | NSC.2 |
| PDSCH Reference measurement channel |  | 1, 2, 3, 4 |  | SR.1.1 FDD | SR.1.1 FDD |
| RMSI CORESET Reference Channel |  | 1, 2, 3, 4 |  | CR.1.1 FDD | CR.1.1 FDD |
| Dedicated CORESET Reference Channel |  | 1, 2, 3, 4 |  | CCR.1.1 FDD | CCR.1.1 FDD |
| SSB configuration |  | 1, 2, 3, 4 |  | SSB.3 FR1 | SSB.3 FR1 |
| OCNG Patterns |  | 1, 2, 3, 4 |  | OP.1 | OP.1 |
| Initial BWP Configuration |  | 1, 2, 3, 4 |  | DLBWP.0.1ULBWP.0.1 | DLBWP.0.1ULBWP.0.1 |
| TRS configuration |  | 1, 2, 3, 4 |  | TRS.1.1 FDD | TRS.1.1 FDD |
| Dedicated BWP configuration |  | 1, 2, 3, 4 |  | DLBWP.1.1ULBWP.1.1 | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration |  | 1, 2, 3, 4 |  | SMTC.1 | SMTC.1 |
| reportConfigType |  | 1, 2, 3, 4 |  | periodic | periodic |
| reportQuantity |  | 1, 2, 3, 4 |  | ssb-Index-RSRP | ssb-Index-RSRP |
| Number of reported RS |  | 1, 2, 3, 4 |  | 2 | 2 |
| L1-RSRP reporting period |  | 1, 2, 3, 4 |  | slot80 | slot80 |
| EPRE ratio of PSS to SSS |  | 1, 2, 3, 4 | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Note2 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/15 kHz | -94.65 | -117 |
| Note2 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/SSB SCS | -94.65 | -117 |
|  |  | 1, 2, 3, 4 | dB | 10 | -3 |
| SSB RSRP Note3 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/SSB SCS | -84.65 | -120 |
| Io Note3 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/9.36 MHz | -56.28 | -87.28 |
|  |  | 1, 2, 3, 4 | dB | 10 | -3 |
| Propagation condition |  | 1, 2, 3, 4 |  | AWGN | AWGN |
| Antenna configuration |  | 1, 2, 3, 4 |  | 1x1 | 1x1 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |  |

##### A.20.6.4.1.3 Test Requirements

The L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 1 shall fulfil the requirement in clause 10.1.19F.1 for 1Rx (e)RedCap UE.

#### A.20.6.4.2 SSB based L1-RSRP measurement for 2Rx RedCap UE

##### A.20.6.4.2.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 9.5E.4 and clause 10.1.19F.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.20.6.4.2.1-1.

Table A.20.6.4.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.6.4.2.2 Test parameters

In this set of test cases, there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.20.6.4.2.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.20.6.4.2.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.20.6.4.2.2-1: FR1 SSB based L1-RSRP test parameters

| Parameter |  | Config | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- | --- | --- |
| SSB ARFCN |  | 1, 2, 3, 4 |  | freq1 | freq1 |
| Duplex mode |  | 1, 2 |  | FDD | FDD |
|  |  | 3, 4 |  | HD-FDD | HD-FDD |
| TDD Configuration |  | 1, 2, 3, 4 |  | N/A | N/A |
| BWchannel |  | 1, 2, 3, 4 | MHz | 10: NPRB,c = 52 | 10: NPRB,c = 52 |
| Satellite information |  | 1, 3 |  | SSC.1 | NSC.1 |
|  |  | 2, 4 |  | SSC.2 | NSC.2 |
| PDSCH Reference measurement channel |  | 1, 2, 3, 4 |  | SR.1.1 FDD | SR.1.1 FDD |
| RMSI CORESET Reference Channel |  | 1, 2, 3, 4 |  | CR.1.1 FDD | CR.1.1 FDD |
| Dedicated CORESET Reference Channel |  | 1, 2, 3, 4 |  | CCR.1.1 FDD | CCR.1.1 FDD |
| SSB configuration |  | 1, 2, 3, 4 |  | SSB.3 FR1 | SSB.3 FR1 |
| OCNG Patterns |  | 1, 2, 3, 4 |  | OP.1 | OP.1 |
| Initial BWP Configuration |  | 1, 2, 3, 4 |  | DLBWP.0.1ULBWP.0.1 | DLBWP.0.1ULBWP.0.1 |
| TRS configuration |  | 1, 2, 3, 4 |  | TRS.1.1 FDD | TRS.1.1 FDD |
| Dedicated BWP configuration |  | 1, 2, 3, 4 |  | DLBWP.1.1ULBWP.1.1 | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration |  | 1, 2, 3, 4 |  | SMTC.1 | SMTC.1 |
| reportConfigType |  | 1, 2, 3, 4 |  | periodic | periodic |
| reportQuantity |  | 1, 2, 3, 4 |  | ssb-Index-RSRP | ssb-Index-RSRP |
| Number of reported RS |  | 1, 2, 3, 4 |  | 2 | 2 |
| L1-RSRP reporting period |  | 1, 2, 3, 4 |  | slot80 | slot80 |
| EPRE ratio of PSS to SSS |  | 1, 2, 3, 4 | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Note2 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/15 kHz | -94.65 | -117 |
| Note2 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/SSB SCS | -94.65 | -117 |
|  |  | 1, 2, 3, 4 | dB | 10 | -3 |
| SSB RSRP Note3 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/SSB SCS | -84.65 | -120 |
| Io Note3 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/9.36 MHz | -56.28 | -87.28 |
|  |  | 1, 2, 3, 4 | dB | 10 | -3 |
| Propagation condition |  | 1, 2, 3, 4 |  | AWGN | AWGN |
| Antenna configuration |  | 1, 2, 3, 4 |  | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |  |

##### A.20.6.4.2.3 Test Requirements

The L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 1 shall fulfil the requirement in clause 10.1.19F.1 for 2Rx (e)RedCap UE.

#### A.20.6.4.3 CSI-RS based L1-RSRP measurement on resource set with repetition off for 1Rx RedCap UE

##### A.20.6.4.3.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 9.5E.4 and clause 10.1.19F.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.20.6.4.3.1-1.

Table A.20.6.4.3.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.6.4.3.2 Test parameters

In this set of test cases, there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.20.6.4.3.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.20.6.4.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.20.6.4.3.2-1: FR1 CSI-RS based L1-RSRP test parameters

| Parameter |  | Config | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- | --- | --- |
| SSB ARFCN |  | 1, 2, 3, 4 |  | freq1 | freq1 |
| Duplex mode |  | 1, 2 |  | FDD | FDD |
|  |  | 3, 4 |  | HD-FDD | HD-FDD |
| TDD Configuration |  | 1, 2, 3, 4 |  | N/A | N/A |
| BWchannel |  | 1, 2, 3, 4 | MHz | 10: NPRB,c = 52 | 10: NPRB,c = 52 |
| Satellite information |  | 1, 3 |  | SSC.1 | NSC.1 |
|  |  | 2, 4 |  | SSC.2 | NSC.2 |
| PDSCH Reference measurement channel |  | 1, 2, 3, 4 |  | SR.1.1 FDD | SR.1.1 FDD |
| RMSI CORESET Reference Channel |  | 1, 2, 3, 4 |  | CR.1.1 FDD | CR.1.1 FDD |
| Dedicated CORESET Reference Channel |  | 1, 2, 3, 4 |  | CCR.1.1 FDD | CCR.1.1 FDD |
| SSB configuration |  | 1, 2, 3, 4 |  | SSB.3 FR1 | SSB.3 FR1 |
| OCNG Patterns |  | 1, 2, 3, 4 |  | OP.1 | OP.1 |
| TRS configuration |  | 1, 2, 3, 4 |  | TRS.1.1 FDD | TRS.1.1 FDD |
| Initial BWP Configuration |  | 1, 2, 3, 4 |  | DLBWP.0.1ULBWP.0.1 | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration |  | 1, 2, 3, 4 |  | DLBWP.1.1ULBWP.1.1 | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration |  | 1, 2, 3, 4 |  | SMTC.1 | SMTC.1 |
| CSI-RS |  | 1, 2, 3, 4 |  | CSI-RS 1.2 FDD | CSI-RS 1.2 FDD |
| reportConfigType |  | 1, 2, 3, 4 |  | periodic | periodic |
| reportQuantity |  | 1, 2, 3, 4 |  | cri-RSRP | cri-RSRP |
| Number of reported RS |  | 1, 2, 3, 4 |  | 2 | 2 |
| L1-RSRP reporting period |  | 1, 2, 3, 4 |  | slot80 | slot80 |
| EPRE ratio of PSS to SSS |  | 1, 2, 3, 4 | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Note2 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/15 kHz | -94.65 | -117 |
| Note2 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/CSI-RS SCS | -94.65 | -117 |
|  |  | 1, 2, 3, 4 | dB | 10 | -3 |
| CSI-RS RSRP Note3 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/CSI-RS SCS | -84.65 | -120 |
| Io Note3 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/9.36 MHz | -56.28 | -87.28 |
|  |  | 1, 2, 3, 4 | dB | 10 | -3 |
| Propagation condition |  | 1, 2, 3, 4 |  | AWGN | AWGN |
| Antenna configuration |  | 1, 2, 3, 4 |  | 1x1 | 1x1 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |  |

##### A.20.6.4.3.3 Test Requirements

The L1-RSRP measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirement in clause 10.1.19F.2 for 1Rx (e)RedCap UE.

#### A.20.6.4.4 CSI-RS based L1-RSRP measurement on resource set with repetition off for 2Rx RedCap UE

##### A.20.6.4.4.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 9.5E.4 and clause 10.1.19F.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.20.6.4.4.1-1.

Table A.20.6.4.4.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | GSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR HD-FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE 1: If (e)RedCap UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases.NOTE 2: If (e)RedCap UE supports both FDD and HD-FDD operation, the UE is only required to be tested in one of both. |  |

##### A.20.6.4.4.2 Test parameters

In this set of test cases, there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.20.6.4.4.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.20.6.4.4.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.20.6.4.4.2-1: FR1 CSI-RS based L1-RSRP test parameters

| Parameter |  | Config | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- | --- | --- |
| SSB ARFCN |  | 1, 2, 3, 4 |  | freq1 | freq1 |
| Duplex mode |  | 1, 2 |  | FDD | FDD |
|  |  | 3, 4 |  | HD-FDD | HD-FDD |
| TDD Configuration |  | 1, 2, 3, 4 |  | N/A | N/A |
| BWchannel |  | 1, 2, 3, 4 | MHz | 10: NPRB,c = 52 | 10: NPRB,c = 52 |
| Satellite information |  | 1, 3 |  | SSC.1 | NSC.1 |
|  |  | 2, 4 |  | SSC.2 | NSC.2 |
| PDSCH Reference measurement channel |  | 1, 2, 3, 4 |  | SR.1.1 FDD | SR.1.1 FDD |
| RMSI CORESET Reference Channel |  | 1, 2, 3, 4 |  | CR.1.1 FDD | CR.1.1 FDD |
| Dedicated CORESET Reference Channel |  | 1, 2, 3, 4 |  | CCR.1.1 FDD | CCR.1.1 FDD |
| SSB configuration |  | 1, 2, 3, 4 |  | SSB.3 FR1 | SSB.3 FR1 |
| OCNG Patterns |  | 1, 2, 3, 4 |  | OP.1 | OP.1 |
| TRS configuration |  | 1, 2, 3, 4 |  | TRS.1.1 FDD | TRS.1.1 FDD |
| Initial BWP Configuration |  | 1, 2, 3, 4 |  | DLBWP.0.1ULBWP.0.1 | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration |  | 1, 2, 3, 4 |  | DLBWP.1.1ULBWP.1.1 | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration |  | 1, 2, 3, 4 |  | SMTC.1 | SMTC.1 |
| CSI-RS |  | 1, 2, 3, 4 |  | CSI-RS 1.2 FDD | CSI-RS 1.2 FDD |
| reportConfigType |  | 1, 2, 3, 4 |  | periodic | periodic |
| reportQuantity |  | 1, 2, 3, 4 |  | cri-RSRP | cri-RSRP |
| Number of reported RS |  | 1, 2, 3, 4 |  | 2 | 2 |
| L1-RSRP reporting period |  | 1, 2, 3, 4 |  | slot80 | slot80 |
| EPRE ratio of PSS to SSS |  | 1, 2, 3, 4 | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Note2 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/15 kHz | -94.65 | -117 |
| Note2 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/CSI-RS SCS | -94.65 | -117 |
|  |  | 1, 2, 3, 4 | dB | 10 | -3 |
| CSI-RS RSRP Note3 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/CSI-RS SCS | -84.65 | -120 |
| Io Note3 | NR_FDD_SAB_FR1_A | 1, 2, 3, 4 | dBm/9.36 MHz | -56.28 | -87.28 |
|  |  | 1, 2, 3, 4 | dB | 10 | -3 |
| Propagation condition |  | 1, 2, 3, 4 |  | AWGN | AWGN |
| Antenna configuration |  | 1, 2, 3, 4 |  | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |  |

##### A.20.6.4.4.3 Test Requirements

The L1-RSRP measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirement in clause 10.1.19F.2 for 2Rx (e)RedCap UE.

# A.21 NR standalone tests for LP-WUR

## A.21.1 RRC_IDLE state mobility

### A.21.1.1 UE exits offloading mode to legacy mode with LR using LP-SS signal

#### A.21.1.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE correctly exists from offloading mode to legacy mode based on the evaluation requirement defined in clause 4.8.2.2.3 with LR using LP-SS signal.

#### A.21.1.1.2 Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.21.1.1.2-1, A.21.1.1.2-2 and A.21.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

The LP-SS configuration 1 in is A.3.X.1 will be used in the test.

Table A.21.1.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.21.1.1.2-2: General test parameters for FR1 UE exit from offloading mode to legacy with LP-SS based LR

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2, 3 | Cell 1 | The UE camps on Cell 1 in the initial phase and enters into offloading mode before the end of T1 period |
|  |  |  |  |  |  |
| T2 end condition | Active cell |  | 1, 2, 3 | Cell 1 | The UE shall leave offloading mode at the end of T2 period |
|  | Neighbour cells |  | 1, 2, 3 | Cell 2 |  |
| T3 end condition | Active cell |  | 1, 2, 3 | Cell 2 | The UE reselects to Cell 2 during T3 period |
|  | Neighbour cells |  | 1, 2, 3 | Cell 1 |  |
| RF Channel Number |  |  | 1, 2, 3 | 1 |  |
| Time offset between cells |  |  | 1 | 3 ms | Asynchronous cells |
|  |  |  | 2 | 3 s | Synchronous cells |
|  |  |  | 3 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1, 2, 3 | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | 1 | SSB.1 FR1 |  |
|  |  |  | 2 | SSB.1 FR1 |  |
|  |  |  | 3 | SSB.2 FR1 |  |
| SMTC configuration |  |  | 1 | SMTC pattern 2 | Configured in SIB2 of Cell 1 |
|  |  |  |  | SMTC pattern 6 | Configured in SIB2 of Cell 2 |
|  |  |  | 2 | SMTC pattern 1 |  |
|  |  |  | 3 | SMTC pattern 1 |  |
| DRX cycle length |  | s | 1, 2, 3 | 0.64 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2, 3 | 102 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2, 3 | Not configured |  |
| T1 |  | s | 1, 2, 3 | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, the intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2 Before the end of T1, the UE enters offloading mode defined in [1], i.e., serving cell measurement is fully offloaded to LR and no serving cell measurement via MR is required |
| T2 |  | s | 1, 2, 3 | 2.72 | T2 is based on the LR evaluation period based on LP-SS plus MR wake up period. During T2, only LP-SS signal is transmitted and the SSB signal from Cell 1 will not be transmitted |
| T3 |  | s | 1, 2, 3 | 43 | T3 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.21.1.1.2-3: Cell specific test parameters for FR1 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling low mobility criterion

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| TDD configuration |  | 1 | N/A |  |  | N/A |  |  |
|  |  | 2 | TDDConf.1.1 |  |  | TDDConf.1.1 |  |  |
|  |  | 3 | TDDConf.2.1 |  |  | TDDConf.2.1 |  |  |
| PDSCH RMC |  | 1 | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |
| configuration |  | 2 | SR.1.1 TDD |  |  | SR.1.1 TDD |  |  |
|  |  | 3 | SR.2.1 TDD |  |  | SR.2.1 TDD |  |  |
| RMSI CORESET |  | 1 | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |
| RMC configuration |  | 2 | CR.1.1 TDD |  |  | CR.1.1 TDD |  |  |
|  |  | 3 | CR.2.1 TDD |  |  | CR.2.1 TDD |  |  |
| Dedicated CORESET |  | 1 | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |
| RMC configuration |  | 2 | CCR.1.1 TDD |  |  | CCR.1.1 TDD |  |  |
|  |  | 3 | CCR.2.1 TDD |  |  | CCR.2.1 TDD |  |  |
| OCNG Pattern |  | 1, 2, 3 | OP.1 defined in clause A.3.2.1 |  |  | OP.1 defined in clause A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1, 2, 3 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2, 3 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1, 2, 3 | SSB |  |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1, 2 | -130 |  |  | -130 |  |  |
|  |  | 3 | -127 |  |  | -127 |  |  |
| Pcompensation | dB | 1, 2, 3 | 0 |  |  | 0 |  |  |
| Qhysts | dB | 1, 2, 3 | 0 |  |  | 0 |  |  |
| Qoffsets, n | dB | 1, 2, 3 | 0 |  |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2, 3 | SS-RSRP |  |  | SS-RSRP |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1 | 16 | -3.11 | 2.79 | -infinity | 2.79 | -3.11 |
|  |  | 2 |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -98 |  |  |  |  |  |
|  |  | 2 | -98 |  |  |  |  |  |
|  |  | 3 | -95 |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -98 |  |  |  |  |  |
|  |  | 2 |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 16 | 13 | 16 | -infinity | 16 | 13 |
|  |  | 2 |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |
| SS-RSRP Note3 | dBm/SCS | 1 | -82 | -85 | -82 | -infinity | -82 | -85 |
|  |  | 2 | -82 | -85 | -82 | -infinity | -82 | -85 |
|  |  | 3 | -79 | -82 | -79 | -infinity | -79 | -82 |
| Io | dBm/9.36 MHz | 1 | -53.94 | -52.21 | -52.21 | Same as parameters specified in Cell 1 columns- |  |  |
|  | dBm/9.36 MHz | 2 | -53.94 | -52.21 | -52.21 |  |  |  |
|  | dBm/38.16 MHz | 3 | -47.85 | -46.12 | -46.12 |  |  |  |
| Treselection | s | 1, 2, 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| SintrasearchP | dB | 1, 2, 3 | 60 |  |  | 60 |  |  |
| SLP_WUS_offloadingEntryThresholdP_MR | dB | 1, 2, 3 | 60 |  |  | 60 |  |  |
| Propagation Condition |  | 1, 2, 3 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

#### A.21.1.1.3 Test Requirements

The duration for a UE exiting the offloading mode to the legacy mode and performing a cell reselection to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The total delay till to reslect to a newly detectable cell shall be the same or less than 36 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The total delay from a UE exits offloading mode till cell re-selection delay to a newly detectable cell can be expressed as: Tevaluate-LP-WUR-LP-SS + 800ms + Tdetect, NR_Intra + TSI-NR

Where:

Tevaluate-LP-WUR-LP-SS See Table 4.8.2.3-1 in clause 4.8.2.2.3

800ms is the MR wake up duration

Tdetect, NR_Intra See table .3 clause 4.2.2.3

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 36s from exiting the offloading mode till the cell re-selection delay to a newly detectable cell.

### A.21.1.2 UE exits from relaxed measurement mode with LR using PSS/SSS in FR1

#### A.21.1.2.1 Test Procedure and Environment

The purpose of this test is to verify that the UE correctly exits from relaxation mode to legacy mode based on the evaluation requirements defined in clause 4.8.2.2.2 with LR using PSS/SSS signal.

#### A.21.1.2.2 Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.21.1.2.2-1, A.21.1.2.2-2 and A.21.1.2.2-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.21.1.2.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.21.1.2.2-2: General test parameters for FR1 UE exit from relaxation mode to legacy with PSS/SSS based LR

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2, 3 | Cell 1 | The UE camps on Cell 1 in the initial phase and enter into relaxation mode at the end of T1 period |
|  |  |  |  |  |  |
| T2 end condition | Active cell |  | 1, 2, 3 | Cell 1 | The UE leave relaxation mode at the end of T2 period |
|  | Neighbour cells |  | 1, 2, 3 | Cell 2 |  |
| T3 end condition | Active cell |  | 1, 2, 3 | Cell 2 | The UE reselects to Cell 2 during T3 period |
|  | Neighbour cells |  | 1, 2, 3 | Cell 1 |  |
| RF Channel Number |  |  | 1, 2, 3 | 1 |  |
| Time offset between cells |  |  | 1 | 3 ms | Asynchronous cells |
|  |  |  | 2 | 3 s | Synchronous cells |
|  |  |  | 3 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1, 2, 3 | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | 1 | SSB.1 FR1 |  |
|  |  |  | 2 | SSB.1 FR1 |  |
|  |  |  | 3 | SSB.2 FR1 |  |
| SMTC configuration |  |  | 1 | SMTC pattern 2 | Configured in SIB2 of Cell 1 |
|  |  |  |  | SMTC pattern 6 | Configured in SIB2 of Cell 2 |
|  |  |  | 2 | SMTC pattern 1 |  |
|  |  |  | 3 | SMTC pattern 1 |  |
| DRX cycle length |  | s | 1, 2, 3 | 0.64 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2, 3 | 102 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2, 3 | Not configured |  |
| T1 |  | s | 1, 2, 3 | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2Before the end of T1, the UE enters relaxed measurement mode defined in [1] |
| T2 |  | s | 1, 2, 3 | 3.36 | T2 is based on the LR evaluation period base don PSS/SSS plus MR wake up period. |
| T3 |  | s | 1, 2, 3 | Y | T3 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.21.1.2.2-3: Cell specific test parameters for FR1 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling low mobility criterion

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| TDD configuration |  | 1 | N/A |  |  | N/A |  |  |
|  |  | 2 | TDDConf.1.1 |  |  | TDDConf.1.1 |  |  |
|  |  | 3 | TDDConf.2.1 |  |  | TDDConf.2.1 |  |  |
| PDSCH RMC |  | 1 | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |
| configuration |  | 2 | SR.1.1 TDD |  |  | SR.1.1 TDD |  |  |
|  |  | 3 | SR.2.1 TDD |  |  | SR.2.1 TDD |  |  |
| RMSI CORESET |  | 1 | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |
| RMC configuration |  | 2 | CR.1.1 TDD |  |  | CR.1.1 TDD |  |  |
|  |  | 3 | CR.2.1 TDD |  |  | CR.2.1 TDD |  |  |
| Dedicated CORESET |  | 1 | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |
| RMC configuration |  | 2 | CCR.1.1 TDD |  |  | CCR.1.1 TDD |  |  |
|  |  | 3 | CCR.2.1 TDD |  |  | CCR.2.1 TDD |  |  |
| OCNG Pattern |  | 1, 2, 3 | OP.1 defined in clause A.3.2.1 |  |  | OP.1 defined in clause A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1, 2, 3 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2, 3 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1, 2, 3 | SSB |  |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1, 2 | -130 |  |  | -130 |  |  |
|  |  | 3 | -127 |  |  | -127 |  |  |
| Pcompensation | dB | 1, 2, 3 | 0 |  |  | 0 |  |  |
| Qhysts | dB | 1, 2, 3 | 0 |  |  | 0 |  |  |
| Qoffsets, n | dB | 1, 2, 3 | 0 |  |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2, 3 | SS-RSRP |  |  | SS-RSRP |  |  |
| ![](media/C:\Users\103347~1.WIN\AppData\Local\Temp\ksohtml7608\wps14.png) | dB | 1 | 16 | -3.11 | 2.79 | -infinity | 2.79 | -3.11 |
|  |  | 2 |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |
| ![](media/C:\Users\103347~1.WIN\AppData\Local\Temp\ksohtml7608\wps15.png) Note2 | dBm/SCS | 1 | -98 |  |  |  |  |  |
|  |  | 2 | -98 |  |  |  |  |  |
|  |  | 3 | -95 |  |  |  |  |  |
| ![](media/C:\Users\103347~1.WIN\AppData\Local\Temp\ksohtml7608\wps16.png) Note2 | dBm/15 kHz | 1 | -98 |  |  |  |  |  |
|  |  | 2 |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |
| ![](media/C:\Users\103347~1.WIN\AppData\Local\Temp\ksohtml7608\wps17.png) | dB | 1 | 16 | 13 | 16 | -infinity | 16 | 13 |
|  |  | 2 |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |
| SS-RSRP Note3 | dBm/SCS | 1 | -82 | -85 | -82 | -infinity | -82 | -85 |
|  |  | 2 | -82 | -85 | -82 | -infinity | -82 | -85 |
|  |  | 3 | -79 | -82 | -79 | -infinity | -79 | -82 |
| Io | dBm/9.36 MHz | 1 | -53.94 | -52.21 | -52.21 | Same as parameters specified in Cell 1 columns- |  |  |
|  | dBm/9.36 MHz | 2 | -53.94 | -52.21 | -52.21 |  |  |  |
|  | dBm/38.16 MHz | 3 | -47.85 | -46.12 | -46.12 |  |  |  |
| Treselection | s | 1, 2, 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| SintrasearchP | dB | 1, 2, 3 | 60 |  |  | 60 |  |  |
| SLP_WUS_offloadingEntryThresholdP_MR | dB | 1, 2, 3 | 50 |  |  | 50 |  |  |
| Propagation Condition |  | 1, 2, 3 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media/C:\Users\103347~1.WIN\AppData\Local\Temp\ksohtml7608\wps18.png) to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

#### A.21.1.2.3 Test Requirements

The duration for a UE exiting the relaxation mode to the legacy mode and performing a cell reselection to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The total delay till to reslect to a newly detectable cell shall be the same or less than 32.64 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The total delay from a UE exits offloading mode till cell re-selection delay to a newly detectable cell can be expressed as: Tevaluate-LP-WUR-PSS/SSS + 800ms + Tdetect, NR_Intra + TSI-NR

Where:

Tevaluate-LP-WUR-PSS/SSS See Table 4.8.2.2-1 in clause 4.8.2.2.2

800ms is the MR wake up duration

Tdetect, NR_Intra See table 4.2.2.3-1 in clause 4.2.2.3

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 32.64 from exiting the relaxation mode till the cell re-selection delay to a newly detectable cell.

### A.21.1.3 UE exits relaxed measurement mode to legacy mode with LR using LP-SS signal

#### A.21.1.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE correctly exists the relaxed measurement mode to legacy mode with LR using LP-SS signal. This test will verify the evaluation requirement for the exit condition of RRM relaxation based on LP-SS for UEs configured with relaxed measurement criterion specified in clause 4.8.2.2.3.

#### A.21.1.3.2 Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.21.1.3.2-1, A.21.1.3.2-2 and A.21.1.3.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. The LP-SS configuration 2 in A.3.X.2 will be used for LP-SS configuration.

Table A.21.1.3.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.21.1.3.2-2: General test parameters for FR1 intra-frequency NR cell re-selection test case for UE fulfilling not-at-cell edge criterion

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initialcondition | Active Cell |  | 1, 2, 3 | Cell 1 | The UE camps on Cell 1 in the initial phase and enters into relaxed measurement mode before the end of T1 period |
|  | Neighbour Cells |  | 1, 2, 3 | Cell 2 |  |
| T2 end condition | Active Cell |  | 1, 2, 3 | Cell 1 | The UE shall fulfil the relaxed measurement criterion based on measurement and evaluation by MR during T1 period |
|  | Neighbour Cells |  | 1, 2, 3 | Cell 2 |  |
| T3 end condition | Active Cell |  | 1, 2, 3 | Cell 1 | During T2 period, the UE shall exist the relaxed measurement mode based on measurement and evaluation by LP-WUR using LP-SS, and reselect to Cell 2 based on measurement and evaluation by MR |
|  | Neighbour Cells |  | 1, 2, 3 | Cell 2 |  |
| RF Channel Number |  |  | 1, 2, 3 | 1 |  |
| Time offset between Cells |  |  | 1 | 3 ms | Asynchronous Cells |
|  |  |  | 2 | 3 s | Synchronous Cells |
|  |  |  | 3 | 3 s | Synchronous Cells |
| Access Barring Information |  | - | 1, 2, 3 | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | 1 | SSB.1 FR1 |  |
|  |  |  | 2 | SSB.1 FR1 |  |
|  |  |  | 3 | SSB.2 FR1 |  |
| LP-SS configuration |  |  | 1, 2, 3 | LP-SS.2 |  |
| SMTC configuration |  |  | 1 | SMTC pattern 2 | Configured in SIB2 of Cell 1 |
|  |  |  |  | SMTC pattern 6 | Configured in SIB2 of Cell 2 |
|  |  |  | 2 | SMTC pattern 1 |  |
|  |  |  | 3 | SMTC pattern 1 |  |
| DRX cycle length |  | s | 1, 2, 3 | 0.64 | The value shall be used for all Cells in the test. |
| PRACH configuration index |  |  | 1, 2, 3 | 102 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2, 3 | Not configured |  |
| T1 |  | s | 1, 2, 3 | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, the intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2.Before the end of T1, the UE enters relaxed measurement mode. |
| T2 |  | s | 1, 2, 3 | 15 | T2 is based on the LR evaluation period based on LP-SS plus MR wake up period. During T2, only LP-SS signal is transmitted and the SSB signal from Cell 1 will not be transmitted |
| T3 |  | s | 1, 2, 3 | 11 | T3 needs to be defined so that cell re-selection time is taken into account. |

Table A.21.1.3.2-3: Cell specific test parameters for FR1 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling not-at-cell edge criterion

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| TDD configuration |  | 1 | N/A |  | N/A |  |
|  |  | 2 | TDDConf.1.1 |  | TDDConf.1.1 |  |
|  |  | 3 | TDDConf.2.1 |  | TDDConf.2.1 |  |
| PDSCH RMC configuration |  | 1 | SR.1.1 FDD |  | N/A |  |
|  |  | 2 | SR.1.1 TDD |  |  |  |
|  |  | 3 | SR.2.1 TDD |  |  |  |
| RMSI CORESET RMC configuration |  | 1 | CR.1.1 FDD |  | CR.1.1 FDD |  |
|  |  | 2 | CR.1.1 TDD |  | CR.1.1 TDD |  |
|  |  | 3 | CR.2.1 TDD |  | CR.2.1 TDD |  |
| Dedicated CORESET RMC configuration |  | 1 | CCR.1.1 FDD |  | CCR.1.1 FDD |  |
|  |  | 2 | CCR.1.1 TDD |  | CCR.1.1 TDD |  |
|  |  | 3 | CCR.2.1 TDD |  | CCR.2.1 TDD |  |
| OCNG Pattern |  | 1, 2, 3 | OP.1 defined in clause A.3.2.1 |  | OP.1 defined in clause A.3.2.1 |  |
| Initial DL BWP configuration |  | 1, 2, 3 | DLBWP.0.1 |  | DLBWP.0.1 |  |
| Initial UL BWP configuration |  | 1, 2, 3 | ULBWP.0.1 |  | ULBWP.0.1 |  |
| RLM-RS |  | 1, 2, 3 | SSB |  | SSB |  |
| Qrxlevmin | dBm/SCS | 1, 2 | -140 |  | -140 |  |
|  |  | 3 | -137 |  | -137 |  |
| Pcompensation | dB | 1, 2, 3 | 0 |  | 0 |  |
| Qhysts | dB | 1, 2, 3 | 0 |  | 0 |  |
| Qoffsets, n | dB | 1, 2, 3 | 0 |  | 0 |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2, 3 | SS-RSRP |  | SS-RSRP |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot]for MR | dB | 1 | 2.79 | -3.11 | -3.11 | 2.79 |
|  |  | 2 |  |  |  |  |
|  |  | 3 |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{Ê}s^{I}ot]for LR |  | 1 | 8.21 | -9.11 | -9.11 | 8.21 |
|  |  | 2 |  |  |  |  |
|  |  | 3 |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -98 |  |  |  |
|  |  | 2 | -98 |  |  |  |
|  |  | 3 | -95 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -98 |  |  |  |
|  |  | 2 |  |  |  |  |
|  |  | 3 |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] for MR | dB | 1 | 16 | 13 | 13 | 16 |
|  |  | 2 |  |  |  |  |
|  |  | 3 |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] for LR |  | 1 | 16 | 7 | 7 | 16 |
|  |  | 2 |  |  |  |  |
|  |  | 3 |  |  |  |  |
| SS-RSRP Note3 | dBm/SCS | 1 | -82 | -85 | -85 | -82 |
|  |  | 2 | -82 | -85 | -85 | -82 |
|  |  | 3 | -79 | -82 | -82 | -79 |
| LP-RSRP Note3 | dBm/SCS | 1 | -82 | -91 | -91 | -82 |
|  |  | 2 | -82 | -91 | -91 | -82 |
|  |  | 3 | -78.99 | -87.99 | -87.99 | -78.99 |
| Io | dBm/9.36 MHz | 1 | -52.21 | -52.21 | -52.21 | -52.21 |
|  | dBm/9.36 MHz | 2 | -52.21 | -52.21 | -52.21 | -52.21 |
|  | dBm/38.16 MHz | 3 | -46.12 | -46.12 | -46.12 | -46.12 |
| Treselection | s | 1, 2, 3 | 0 | 0 | 0 | 0 |
| SintrasearchP | dB | 1,2,3 | 60 | 60 | 60 | 60 |
| SLP_WUS_RelaxThresholdP_MR | dB | 1, 2, 3 | 50 |  | 50 |  |
| QLP_WUS_RelaxThresholdP_LR | dB | 1, 2, 3 | 50 |  | 50 |  |
| Propagation Condition |  | 1, 2, 3 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both Cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other Cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image2.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and LP-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

#### A.21.1.3.3 Test Requirements

The delay for a UE existing the relaxed measurement mode to the legacy mode and performing cell re-selection to an already detected cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The delay for a UE existing the relaxed measurement mode to the legacy mode and performing cell re-selection to an already detected cell shall be less than 10 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to an already detected cell for UE fulfilling with relaxed measurement criterion can be expressed as: 800ms + Tevaluate-LP-WUR-LP-SS + Tevaluate,NR_Intra + TSI-NR,

Where:

Tevaluate-LP-WUR-LP-SS See table 4.8.2.3-1 in clause 4.8.2.2.3

Tevaluate,NR_Intra See table 4.2.2.3-1 in clause 4.2.2.3

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a Cell; 1280 ms is assumed in this test case.

This gives a total of 9.6 s, allow 10 s for the cell re-selection delay to an already detected cell for UE fulfilling not-at-cell edge criterion in the test case.

### A.21.1.4 UE exit from relaxed measurement mode with LR using PSS/SSS in FR2

#### A.21.1.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE correctly exits from the relaxed measurement mode to legacy mode in FR2 based on the evaluation requirement for the exit condition for PSS/SSS specified in clause 4.8.2.2.2.

#### A.21.1.4.2 Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.21.1.4.2-1, A.21.1.4.2-2 and A.21.1.4.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. During T1 and T2, entry/exit conditions for RRM measurement relaxation is configured but the conditions are met only during T1. UE has not registered with network for the tracking area containing Cell 2.

Table A.21.1.4.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | 120 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| 2 | 240 kHz SSB SCS, 100 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.21.1.4.2-2: General test parameters

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2 | Cell 1 | The UE camps on cell 1 in the initial phase and enter intor relaxation mode at the end of T1 period |
|  | Neighbour cells |  | 1, 2 | Cell 2 |  |
| T1 end condition | Active cell |  | 1, 2 | Cell 2 | Sufficient time to allow the UE to evaluate and enter the relaxed measurement mode |
|  | Neighbour cells |  | 1, 2 | Cell 1 |  |
| Final condition | Active cell |  | 1, 2 | Cell 1 | The UE evaluates and fulfils the exit criteria for relaxed measurements and reselects to cell 2 during T2 period |
|  | Neighbour cells |  | 1,2 | Cell 2 |  |
| RF Channel Number |  |  | 1, 2 | 1 |  |
| Time offset between cells |  |  | 1, 2 | 3 s | Synchronous cells |
| Access Barring Information |  | - | 1, 2 | Not Sent | No additional delays in random access procedure. |
| SMTC configuration |  |  | 1, 2 | SMTC pattern 1 |  |
| DRX cycle length |  | s | 1, 2 | 0.64 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2 | 190 | The detailed configuration is specified in TS 38.211 clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2 | Not configured |  |
| T1 |  | s | 1, 2 | 100 |  |
| T2 |  | s | 1, 2 | 100 |  |

Table A.21.1.4.2-3: Cell specific test parameters

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| TDD configuration |  | 1, 2 | TDDConf.3.1 |  | TDDConf.3.1 |  |
| PDSCH RMC |  | 1 | SR.3.1 TDD |  | SR.3.1 TDD |  |
| configuration |  | 2 | SR.3.1 TDD |  | SR.3.1 TDD |  |
| RMSI CORESET |  | 1 | CR.3.1 TDD |  | CR.3.1 TDD |  |
| RMC configuration |  | 2 | CR.3.1 TDD |  | CR.3.1 TDD |  |
| Dedicated CORESET |  | 1 | CCR.3.1 TDD |  | CCR.3.1 TDD |  |
| RMC configuration |  | 2 | CCR.3.1 TDD |  | CCR.3.1 TDD |  |
| SSB configuration |  | 1 | SSB.3 FR2 |  | SSB.7 FR2 |  |
|  |  | 2 | SSB.4 FR2 |  | SSB.8 FR2 |  |
| OCNG Pattern |  | 1, 2 | OP.4 |  | OP.4 |  |
| BWchannel | MHz | 1, 2 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
| Data PRBs allocated |  | 1, 2 | 66 |  | 66 |  |
| Initial DL BWP configuration |  | 1, 2 | DLBWP.0.1 |  | DLBWP.0.1 |  |
| Initial UL BWP configuration |  | 1, 2 | ULBWP.0.1 |  | ULBWP.0.1 |  |
| RLM-RS |  | 1, 2 | SSB |  | SSB |  |
| Qrxlevmin | dBm/SCS | 1 | -140 |  | -140 |  |
|  |  | 2 | -137 |  | -137 |  |
| SSearchDeltaP | dB | 1, 2 | 6 |  | 6 |  |
| TSearchDeltaP | s | 1,2 | 5 |  | 5 |  |
| Pcompensation | dB | 1, 2 | 0 |  | 0 |  |
| Qhysts | dB | 1, 2 | 0 |  | 0 |  |
| Qoffsets, n | dB | 1, 2 | 0 |  | 0 |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2 | SS-RSRP |  | SS-RSRP |  |
| AoA setup |  | 1, 2 | Setup 1 defined in A.3.15.1 |  | Setup 1 defined in A.3.15.1 |  |
| Beam assumptionNote 4 |  | 1,2 | Rough |  | Rough |  |
| $\hat  {E}_{s}/I_{otBB}$ Note 5 | dB | 1 | 0.95 | -3.55 | -3.55 | 0.95 |
|  |  | 2 |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -93 |  |  |  |
|  |  | 2 | -90 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -102 |  |  |  |
|  |  | 2 |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 1.5 | -3 | -3 | 1.5 |
|  |  | 2 |  |  |  |  |
| SS-RSRP Note3 | dBm/SCS | 1 | -91.5 | -96 | -96 | -91.5 |
|  |  | 2 | -88.5 | -93 | -93 | -88.5 |
| Io on SSB symbols of each cell | dBm/95.04 MHz | 1 | -65.34 | -67.40 | -67.40 | -65.34 |
|  |  | 2 | -62.34 | -64.40 | -64.40 | -62.34 |
| Treselection | s | 1, 2 | 0 | 0 | 0 | 0 |
| SintrasearchP | dB | 1, 2 | 50 |  | 50 |  |
| SLP_WUS_RelaxThresholdP_MR | dB | 1,2 | 35 |  | 35 |  |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for NOC to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in clause B.2.1.3, and does not limit UE implementation or test system implementationNOTE 5: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] Table 6.2.1.3-4. |  |  |  |  |  |  |

#### A.21.1.4.3 Test Requirements

The delay for a UE exiting the relaxed measurement mode to the legacy mode and performing cell re-selection to an already detected cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The delay for a UE exiting the relaxed measurement mode to the legacy mode and performing cell re-selection to an already detected cell shall be less than 40 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to an already detected cell for UE fulfilling with relaxed measurement criterion can be expressed as: Tevaluate-LP-WUR-PSS/SSS + Tevaluate,NR_Intra + TSI-NR,

Where:

Tevaluate-LP-WUR-PSS/SSS See table 4.8.2.2-1 in clause 4.8.2.2.2

Tevaluate,NR_Intra See table 4.2.2.3-1 in clause 4.2.2.3

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a Cell; 1280 ms is assumed in this test case.

This gives a total of 12.8+25.6+1.28 = 39.68s, allow 40 s for the cell re-selection delay to an already detected cell for UE fulfilling not-at-cell edge criterion in the test case.
