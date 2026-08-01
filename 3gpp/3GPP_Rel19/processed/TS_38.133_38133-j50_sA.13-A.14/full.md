# A.13 NR Standalone Tests with NR SCell under CCA and All Other NR Cells in FR1

## A.13.1 Void

### A.13.1.1 Void

### A.13.1.2 Void

## A.13.2 Signalling characteristics

### A.13.2.1 Void

### A.13.2.2 SCell activation and deactivation delay

#### A.13.2.2.1 SCell Activation and Deactivation of known SCell under CCA, 160 ms SCell measurement cycle

##### A.13.2.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for SCell on NR-U SCC with CCA are within the requirements stated in clause 8.3A, when the SCell is known by the UE at the time of activation and the configured SCell measurement cycle is 160 ms.

The supported test configurations are shown in table A.13.2.2.1.1-1.

The test parameters are given in table A.13.2.2.1.1-2 and cell-specific parameters in table A.13.2.2.1.1-3 below. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two carriers, each with one cell: Cell 1 (PCell) on radio channel 1 (PCC) in NR FR1, and Cell 2 (SCell) on radio channel 2 (SCC) in NR with CCA. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2, as the UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. At the end of T1, the test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2. The UE shall be able to report a valid CSI in PCell for the activated SCell at latest in slot m + $\frac {T_{HARQ}+T_{activation\_time\_withCCA}+T_{CSI\_Reporting\_withCCA}}{NR slot length}$, as defined in clause 8.3A.2. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot m+ $\frac {T_{HARQ}+3 ms}{NR slot length}$ and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption shall fall within the time window specified in clause 8.3A.2. At the end of T2 the test equipment sends a MAC message for deactivation of the SCell.

The point in time at which the MAC message is received by at the UE antenna connector, in a slot # denoted n, defines the start of time period T3. The UE shall complete the activation at latest in slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$. Any PCell interruption shall fall within the time window specified in clause 8.3A.3.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received, while taking into account CCA failures on SCC.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.13.2.2.1.1-1: Supported test configurations for SCell Activation and Deactivation of known SCell under CCA, 160 ms SCell measurement cycle

| Configuration | Description |
| --- | --- |
| 1 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode; With CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode; With CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode; With CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.13.2.2.1.1-2: General test parameters for known SCell activation with SCell under CCA, 160 ms SCell measurement cycle

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| RF Channel Number |  | 1,2 | Two radio channels (1, 2) are used for this test |
| Active PCell |  | Cell 1 | Primary cell on NR RF channel number 1. |
| Configured deactivated SCell |  | Cell 2 | Configured deactivated secondary cell on NR RF channel number 2 |
| CP length |  | Normal |  |
| DRX |  | OFF | Continuous monitoring of primary cell |
| CQI/PMI periodicity and offset configuration index |  | 0 | CQI reporting for SCell every fourth slot |
| SCell measurement cycle (measCycleSCell) | ms | 160 |  |
| Cell 2 timing offset to Cell 1 | s | 0 |  |
| Time alignment error between Cell 2 and Cell 1 | s | TAE as specified in TS 38.104 [13] clause 6.5.3.1. | The value of time alignment error depends upon the type of carrier aggregation. |
| T1 | s | 7 | During this time the PCell shall be known and the SCell configured and detected. |
| T2 | s | 1 | During this time the UE shall activate the SCell. |
| T3 | s | 1 | During this time the UE shall deactivate the SCell. |
| THARQ | ms | k1 $\times  $ NR slot length | k1 is a number of slots and is indicated by the PDSCH-to-HARQ-timing-indicator field in the DCI format, if present, or provided by dl-DataToUL-ACK, the value of k should be the minimum value defined in TS 38.213 [3] depends on UE’s capability |
| TCSI_Reporting | ms | $ 10+5\cdot  2^{µ_{DL}}$ | the delay (in ms) including uncertainty in acquiring the first available downlink CSI reference resource, UE processing time for CSI reporting (clause 5.2.2.5 in TS 38.214) and uncertainty in acquiring the first available CSI reporting resources as specified in TS 38.331 [2]$µ_{DL}$ is the subcarrier spacing configuration for DL |

Table A.13.2.2.1.1-3: Cell specific test parameters for known FR1 SCell activation case with SCell under CCA, 160 ms SCell measurement cycle

| Parameter |  | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Duplex mode | Config 1 |  | FDD |  |  | TDD |  |  |
|  | Config 2,3 |  | TDD |  |  |  |  |  |
| TDD configuration | Config 1 |  | --- |  |  | TDDConf.1.1 CCA |  |  |
|  | Config 2 |  | TDDConf.1.1 |  |  |  |  |  |
|  | Config 3 |  | TDDConf.2.1 |  |  |  |  |  |
| BWchannel | Config 1,2 | MHz | 10: NPRB,c = 52 |  |  | 40: NPRB,c = 106 |  |  |
|  | Config 3 |  | 40: NPRB,c = 106 |  |  |  |  |  |
| DL CCA model |  |  | --- |  |  | As specified in clause A.3.26.2.1 |  |  |
| DL CCA probability for semi-static channel accessNote5,7 | PCCA_DL |  | --- |  |  | 0.9357 |  |  |
| DL CCA probability for dynamic channel accessNote6,7 | PCCA_DL_1 |  | --- |  |  | 0.75 |  |  |
|  | PCCA_DL_2 |  | --- |  |  | 0.75 |  |  |
| PCCA_UL |  |  |  |  |  | 1 |  |  |
| LCCA_DL Note 8 |  |  |  |  |  | 2 |  |  |
| WCCA_DL Note 8 |  | ms |  |  |  | Tactivation_time_withCCA |  |  |
| Initial downlink BWP configuration |  |  | DLBWP.0.2 |  |  | DLBWP.0.2 |  |  |
| Initial uplink BWP configuration |  |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Dedicated downlink BWP configuration |  |  | DLBWP.0.2 |  |  | DLBWP.0.2 |  |  |
| Dedicated uplink BWP configuration |  |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| TCI state |  |  | TCI.State.0 |  |  | TCI.State.0 |  |  |
| TRS Configuration | Config 1 |  | TRS.1.1 FDD |  |  | TRS.1.2 TDD |  |  |
|  | Config 2 |  | TRS.1.1 TDD |  |  |  |  |  |
|  | Config 3 |  | TRS.1.2 TDD |  |  |  |  |  |
| PDSCH Reference measurement channel | Config 1 |  | SR.1.1 FDD |  |  | SR.1.1 CCA |  |  |
|  | Config 2 |  | SR.1.1 TDD |  |  |  |  |  |
|  | Config 3 |  | SR.2.1 TDD |  |  |  |  |  |
| Dedicated CORESET parameters | Config 1 |  | CCR.1.1 FDD |  |  | CCR.1.3 CCA |  |  |
|  | Config 2 |  | CCR.1.1 TDD |  |  |  |  |  |
|  | Config 3 |  | CCR.2.1 TDD |  |  |  |  |  |
| RMSI CORESET parameters | Config 1 |  | CR.1.1 FDD |  |  | CR.1.1 CCA |  |  |
|  | Config 2 |  | CR.1.1 TDD |  |  |  |  |  |
|  | Config 3 |  | CR.2.1 TDD |  |  |  |  |  |
| OCNG Patterns Note1 |  |  | OP.1 |  |  | OP.1 |  |  |
| SSB Configuration for semi-static channel accessNote5,7 | Config 1,2 |  | SSB.1 FR1 |  |  | SSB.1 CCA |  |  |
|  | Config 3 |  | SSB.2 FR1 |  |  |  |  |  |
| SSB Configuration for dynamic channel accessNote6,7 | Config 1,2 |  | SSB.1 FR1 |  |  | SSB.2 CCA |  |  |
|  | Config 3 |  | SSB.2 FR1 |  |  |  |  |  |
| SMTC configuration |  |  | SMTC.1 |  |  | SMTC.1 |  |  |
| DBT window configuration |  |  | --- |  |  | DBT.1 |  |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |  | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote1 |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRSNote1 |  |  |  |  |  |  |  |  |
| Noc Note2 | Config 1,2 | dBm/15 kHz | -104 |  |  | -104 |  |  |
|  | Config 3 |  |  |  |  |  |  |  |
| Noc Note2 | Config 1,2 | dBm/SCS | -104 |  |  | -101 |  |  |
|  | Config 3 |  | -101 |  |  |  |  |  |
| Ês/Iot |  | dB | 17 |  |  | 17 |  |  |
| Ês/Noc |  | dB | 17 |  |  | 17 |  |  |
| SS-RSRP Note3 | Config 1,2 | dBm/SCS | -87 |  |  | -84 |  |  |
|  | Config 3 |  | -84 |  |  | -84 |  |  |
| IoNote3 | Config 1,2 |  | -58.96 |  |  | -52.87 |  |  |
|  | Config 3 |  | -52.87 |  |  | -52.87 |  |  |
| Propagation condition |  | - | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For Cell 2 with CCA model, OCNG is transmitted only in slots with downlink transmission bursts and is not transmitted during muted slots or during DBT windows.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP, SCH_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T2.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations.NOTE 8: As specified in clause 8.3A for L1,max, L2,1,max, L2,2,max, L3,1,max, and L3,2,max |  |  |  |  |  |  |  |  |

##### A.13.2.2.1.2 Test Requirements

During T2, the UE shall send the first CSI report for SCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot m+1+$\frac {T_{HARQ}+3 ms}{NR slot length}.$

During T2, conditioned on that downlink CCA failures L1 and L2,2 experienced in the SCell fulfill L1 ≤ L1,max and L2,2 ≤ L2,2,max with L1,max = 2 and L2,2,max = 2, respectively, the UE shall send the first valid CSI report (non-zero CQI) for the SCell no later than slot m + (THARQ+Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB + L1*Trs + 5 ms and TCSI_reporting_withCCA = TCSI_reporting + L2,2*TCSI-RS + TCSI_ReportingDelay, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$, as defined in clause 8.3A.3.

During T2, interruption on PCell shall not occur outside slot m +1+$\frac {T_{HARQ}}{NR slot length}$  to slot m +1+$\frac {T_{HARQ}+3+T_{X}}{NR slot length}$ with TX = TFirstSSB.

During T3, interruption on PCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PCell shall not be more than specified for SA in clause 8.2.2.2.2.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

#### A.13.2.2.2 SCell Activation and Deactivation of known SCell under CCA, 640 ms SCell measurement cycle

##### A.13.2.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for SCell on NR-U SCC with CCA are within the requirements stated in clause 8.3A, when the SCell is known by the UE at the time of activation and the configured SCell measurement cycle is 640 ms.

The supported test configurations are same as in table A.13.2.2.1.1-1 above.

The test parameters are same as in table A.13.2.2.1.1-2 above, except for parameters listed below in table A.13.2.2.2.1-1. The cell-specific parameters are same as in table A.13.2.2.1.1-3 above.

The test execution is the same as described in clause A.13.2.2.1 above, except that downlink CCA failures L2,1 and L2,2 with limits L2,1 ≤ L2,1,max and L2,2 ≤ L2,2,max replace L1 as described in clause 8.3A.2 for activation of known SCell with a measurement cycle larger than 160 ms.

Table A.13.2.2.2.1-1: General test parameters for known SCell activation with SCell under CCA, 640 ms SCell measurement cycle

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| SCell measurement cycle (measCycleSCell) | ms | 640 |  |

##### A.13.2.2.2.2 Test Requirements

During T2, the UE shall send the first CSI report for SCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot m+1+$\frac {T_{HARQ}+3 ms}{NR slot length}.$

During T2, conditioned on that downlink CCA failures L2,1 and L2,2 experienced in the SCell fulfill L2,1 ≤ L2,1,max and L2,2 ≤ L2,2,max with L2,1,max = 2 and L2,2,max = 2, respectively, the UE shall send the first valid CSI report (non-zero CQI) for the SCell no later than slot m + (THARQ+Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB_MAX + L2,1*TSMTC_MAX + (1 +L2,2)*Trs + 5 ms and TCSI_reporting_withCCA = TCSI_reporting + TCSI_ReportingDelay, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$, as defined in clause 8.3A.3.

During T2, interruption on PCell shall not occur outside slot m +1+$\frac {T_{HARQ}}{NR slot length}$  to slot m +1+$\frac {T_{HARQ}+3+T_{X}}{NR slot length}$ with TX = TFirstSSB.

During T3, interruption on PCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PCell shall not be more than specified for SA in clause 8.2.2.2.2.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

#### A.13.2.2.3 SCell Activation and Deactivation of unknown SCell under CCA

##### A.13.2.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for SCell on NR-U SCC with CCA are within the requirements stated in clause 8.3A, when the SCell is unknown to the UE at the time of activation.

The supported test configurations are same as in table A.13.2.2.1.1-1 above.

The test parameters are same as in table A.13.2.2.1.1-2 above, except for parameters listed below in table A.13.2.2.3.1-1. The cell-specific parameters are same as in table A.13.2.2.1.1-3 above.

The test execution is the same as described in clause A.13.2.2.1 above, except that downlink CCA failures L3,1 and L3,2 with limits L3,1 ≤ L3,1,max and L3,2 ≤ L3,2,max replace L1 as described in clause 8.3A.2 for activation of unknown SCell.

Table A.13.2.2.3.1-1: General test parameters for unknown SCell activation with SCell under CCA

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| T1 | s | 0.1 | During this time period the PCell shall be known and the SCell configured, but not detected. |

##### A.13.2.2.3.2 Test Requirements

During T2, the UE shall send the first CSI report for SCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot m+1+$\frac {T_{HARQ}+3 ms}{NR slot length}.$

During T2, conditioned on that downlink CCA failures L3,1 and L3,2 experienced in the SCell fulfill L3,1 ≤ L3,1,max and L3,2 ≤ L3,2,max with L3,1,max = 2 and L3,2,max = 2, respectively, the UE shall send the first valid CSI report (non-zero CQI) for the SCell no later than slot m + (THARQ+Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB_MAX + (1 + L3,1)*TSMTC_MAX + (2 + L3,2)*Trs + 5 ms and TCSI_reporting_withCCA = TCSI_reporting + TCSI_ReportingDelay, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot $ n+\frac {T_{HARQ}+3 ms}{NR slot length}$, as defined in clause 8.3A.3.

During T2, interruption on PCell shall not occur outside slot m +1+$\frac {T_{HARQ}}{NR slot length}$  to slot m +1+$\frac {T_{HARQ}+3+T_{X}}{NR slot length}$ with TX = TFirstSSB.

During T3, interruption on PCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PCell shall not be more than specified for SA in clause 8.2.2.2.2.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

### A.13.2.3 Void

## A.13.3 Measurement procedure

### A.13.3.1 Intra-frequency measurements

#### A.13.3.1.1 Event-triggered reporting tests on SCC without gaps under non-DRX

##### A.13.3.1.1.1 Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.5.1 and 9.2A.5.2.

##### A.13.3.1.1.2 Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), and two cells on the same carrier frequency with CCA and transmit SSBs in DBT windows according to DL CCA model: SCell (Cell 2) and a neighbour cell (Cell 3). The test parameters for the three cells are given in table A.13.3.1.1.2-1 and A.13.3.1.1.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

Table A.13.3.1.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.13.3.1.1.2-2: General test parameters for intra-frequency event triggered reporting without gaps

| Paramater | Unit | Test Configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active PCell |  | 1, 2, 3 | Cell 1 |  |
| Active SCell |  | 1, 2, 3 | Cell 2 |  |
| Neighbour cell |  | 1, 2, 3 | Cell 3 | Cell to be identified. |
| RF Channel Number |  | 1, 2, 3 | 1: Cell 12: Cell 2 and Cell 3 |  |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |
| DBT window configuration |  | 1, 2, 3 | Cell 1: N/ACell 2,3: DBT.1 |  |
| A3-Offset | dB | 1, 2, 3 | -4.5 |  |
| Event A3 measurement quantity |  |  | SS-RSRP |  |
| CP length |  | 1, 2, 3 | Normal |  |
| Hysteresis | dB | 1, 2, 3 | 0 |  |
| Time To Trigger | s | 1, 2, 3 | 0 |  |
| Filter coefficient |  | 1, 2, 3 | 0 | L3 filtering is not used |
| DRX |  | 1, 2, 3 |  | OFF |
| Time offset between Cell 1 and Cell 2 |  | 1 | 3 ms | Asynchronous cells.The timing of Cell 2 is 3ms later than the timing of Cell 1. |
|  |  | 2 | 3 ms | Synchronous cells |
|  |  | 3 | 3 ms | Synchronous cells |
| deriveSSB-IndexFromCell |  | 1 | False |  |
|  |  | 2 | True |  |
|  |  | 3 | True |  |
| T1 | s | 1, 2, 3 | 5 |  |
| T2 | s | 1, 2, 3 | 5 |  |

Table A.13.3.1.1.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gaps

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1,2,3 | 1 |  | 2 |  | 2 |  |
| Duplex mode |  |  |  | Config 1 | FDD |  | TDD |  | TDD |  |
|  |  |  |  | Config 2,3 | TDD |  | TDD |  | TDD |  |
| TDD configuration |  |  |  | Config 1 | Not Applicable |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 2 | TDDConf.1.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 3 | TDDConf.2.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  |  | Config 1,2,3 | Not Applicable |  | 12 |  | 12 |  |
| WCCA_DL |  |  | ms | Config 1,2,3 | Not Applicable |  | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| BWchannel |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP configuration | Initial DL BWP |  |  | Config 1,2,3 | DLBWP.0.1 |  | DLBWP.0.1 |  |  |  |
|  | Initial UL BWP |  |  |  | ULBWP.0.1 |  | ULBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  |  | DLBWP.1.1 |  | DLBWP.1.1 |  |  |  |
|  | Dedicated UL BWP |  |  |  | ULBWP.1.1 |  | ULBWP.1.1 |  |  |  |
| TRS configuration |  |  |  | Config 1 | TRS.1.1 FDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 2 | TRS.1.1 TDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 3 | TRS.1.2 TDD |  | TRS.1.2 TDD |  |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1,2,3 | OP.1 |  | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1 | SR.1.1 FDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | SR.1.1 TDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | SR2.1 TDD |  | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1 | CR.1.1 FDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | CR.1.1 TDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | CR2.1 TDD |  | CR.1.1 CCA |  |  |  |
| SSB |  | Semi- |  | Config 1 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
| parameters |  | static channel Note 5,7 |  | Config 2 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  |  |  | Config 3 | SSB.2 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  | Dynamic |  | Config 1 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | channel |  | Config 2 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | Access Note 6,7 |  | Config 3 | SSB.2 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  |  | Config 1,2,3 | Not Applicable |  | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1,2,3 | SMTC.1 |  | SMTC.1 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 2 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 3 | 30 |  | 30 |  | 30 |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1,2,3 | 0 |  | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1,2,3 | -98 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1,2 | -98 |  | -95 |  | -95 |  |
|  |  |  |  | Config 3 | -95 |  | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1,2 | -94 | -94 | -91 | -91 | -Infinity | -88 |
|  |  |  |  | Config 3 | -91 | -91 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1,2,3 | 4 | 4 | 4 | -3.79 | -Infinity | 1.54 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1,2,3 | 4 | 4 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/ChBW | Config 1,2 | -64.59 | -64.59 | -58.49 | -54.64 | -58.49 | -54.64 |
|  |  |  | dBm/ChBW | Config 3 | -58.49 | -58.49 | -58.49 | -54.64 | -58.49 | -54.64 |
| Propagation Condition |  |  |  | Config 1,2,3 | AWGN |  | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |  |  |

##### A.13.3.1.1.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_intra_without_index_CCA ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

Tidentify_intra_cca_without_index = (TPSS/SSS_sync_intra_cca + T SSB_measurement_period_intra_cca) ms, where

TPSS/SSS_sync_intra_cca: it is the time period used in PSS/SSS detection given in table 9.2A.5.1-1.

T SSB_measurement_period_intra_cca: equal to a measurement period of SSB based measurement given in table 9.2A.5.2-1.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.13.3.1.2 Event-triggered reporting tests on SCC without gaps under DRX

##### A.13.3.1.2.1 Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.5.1 and 9.2A.5.2.

##### A.13.3.1.2.2 Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), and two cells on the same carrier frequency with CCA and transmit SSBs in DBT windows according to DL CCA model: SCell (Cell 2) and a neighbour cell (Cell 3). The test parameters for the three cells are given in table A.13.3.1.2.2-1 and A.13.3.1.2.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.13.3.1.2.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.13.3.1.2.2-2: General test parameters for intra-frequency event triggered reporting without gaps with DRX

| Parameter | Unit | Test Configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| Active PCell |  | 1, 2, 3 | Cell 1 |  |  |
| Active SCell |  | 1, 2, 3 | Cell 2 |  |  |
| Neighbour cell |  | 1, 2, 3 | Cell 3 |  | Cell to be identified. |
| RF Channel Number |  | 1, 2, 3 | 1: Cell 12: Cell 2 and Cell 3 |  |  |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |  |
| DBT window configuration |  | 1, 2, 3 | Cell 1: N/ACell 2,3: DBT.1 |  |  |
| A3-Offset | dB | 1, 2, 3 | -4.5 |  |  |
| Event A3 measurement quantity |  |  | SS-RSRP |  |  |
| CP length |  | 1, 2, 3 | Normal |  |  |
| Hysteresis | dB | 1, 2, 3 | 0 |  |  |
| Time To Trigger | s | 1, 2, 3 | 0 |  |  |
| Filter coefficient |  | 1, 2, 3 | 0 |  | L3 filtering is not used |
| DRX |  | 1, 2, 3 | DRX.1 | DRX.2 |  |
| Time offset between Cell 1 and Cell 2 |  | 1 | 3 ms |  | Asynchronous cells.The timing of Cell 2 is 3ms later than the timing of Cell 1. |
|  |  | 2 | 3 ms |  | Synchronous cells |
|  |  | 3 | 3 ms |  | Synchronous cells |
| deriveSSB-IndexFromCell |  | 1 | False |  |  |
|  |  | 2 | True |  |  |
|  |  | 3 | True |  |  |
| T1 | s | 1, 2, 3 | 5 |  |  |
| T2 | s | 1, 2, 3 | 5 | 20 |  |

Table A.13.3.1.2.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gaps

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1,2,3 | 1 |  | 2 |  | 2 |  |
| Duplex mode |  |  |  | Config 1 | FDD |  | TDD |  | TDD |  |
|  |  |  |  | Config 2,3 | TDD |  | TDD |  | TDD |  |
| TDD configuration |  |  |  | Config 1 | Not Applicable |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 2 | TDDConf.1.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 3 | TDDConf.2.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  |  | Config 1,2,3 | Not Applicable |  | 12 |  | 12 |  |
| WCCA_DL |  |  | ms | Config 1,2,3 | Not Applicable |  | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| BWchannel |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP configuration | Initial DL BWP |  |  | Config 1,2,3 | DLBWP.0.1 |  | DLBWP.0.1 |  |  |  |
|  | Initial UL BWP |  |  |  | ULBWP.0.1 |  | ULBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  |  | DLBWP.1.1 |  | DLBWP.1.1 |  |  |  |
|  | Dedicated UL BWP |  |  |  | ULBWP.1.1 |  | ULBWP.1.1 |  |  |  |
| TRS configuration |  |  |  | Config 1 | TRS.1.1 FDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 2 | TRS.1.1 TDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 3 | TRS.1.2 TDD |  | TRS.1.2 TDD |  |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1,2,3 | OP.1 |  | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1 | SR.1.1 FDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | SR.1.1 TDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | SR2.1 TDD |  | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1 | CR.1.1 FDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | CR.1.1 TDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | CR2.1 TDD |  | CR.1.1 CCA |  |  |  |
| SSB |  | Semi- |  | Config 1 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
| parameters |  | static channel Note 5,7 |  | Config 2 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  |  |  | Config 3 | SSB.2 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  | Dynamic |  | Config 1 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | channel |  | Config 2 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | Access Note 6,7 |  | Config 3 | SSB.2 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  |  | Config 1,2,3 | Not Applicable |  | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1,2,3 | SMTC.1 |  | SMTC.1 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 2 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 3 | 30 |  | 30 |  | 30 |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1,2,3 | 0 |  | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1,2,3 | -98 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1,2 | -98 |  | -95 |  | -95 |  |
|  |  |  |  | Config 3 | -95 |  | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1,2 | -94 | -94 | -91 | -91 | -Infinity | -88 |
|  |  |  |  | Config 3 | -91 | -91 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1,2,3 | 4 | 4 | 4 | -3.79 | -Infinity | 1.54 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1,2,3 | 4 | 4 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/ChBW | Config 1,2 | -64.59 | -64.59 | -58.49 | -54.64 | -58.49 | -54.64 |
|  |  |  | dBm/ChBW | Config 3 | -58.49 | -58.49 | -58.49 | -54.64 | -58.49 | -54.64 |
| Propagation Condition |  |  |  | Config 1,2,3 | AWGN |  | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |  |  |

##### A.13.3.1.2.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_intra_without_index_CCA ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

Tidentify_intra_cca_without_index = (TPSS/SSS_sync_intra_cca + T SSB_measurement_period_intra_cca) ms, where

TPSS/SSS_sync_intra_cca: it is the time period used in PSS/SSS detection given in table 9.2A.5.1-1.

T SSB_measurement_period_intra_cca: equal to a measurement period of SSB based measurement given in table 9.2A.5.2-1.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.13.3.1.3 Event-triggered reporting tests on SCC with per-UE gaps under non-DRX

##### A.13.3.1.3.1 Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.6.1 and 9.2A.6.2.

##### A.13.3.1.3.2 Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), and two cells on the same carrier frequency with CCA and transmit SSBs in DBT windows according to DL CCA model: SCell (Cell 2) and a neighbour cell (Cell 3). The test parameters for the three cells are given in table A.13.3.1.3.2-1 and A.13.3.1.3.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There are two BWPs configured in Cell 1, BWP0 which contains the cell defining SSB, and BWP1 which does not contain any SSB of Cell 1. During the whole test, BWP1 is always scheduled as the active BWP for the UE.

Table A.13.3.1.3.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.13.3.1.3.2-2: General test parameters for intra-frequency event triggered reporting with per-UE gaps

| Paramater | Unit | Test Configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active PCell |  | 1, 2, 3 | Cell 1 |  |
| Active SCell |  | 1, 2, 3 | Cell 2 |  |
| Neighbour cell |  | 1, 2, 3 | Cell 3 | Cell to be identified. |
| RF Channel Number |  | 1, 2, 3 | 1: Cell 12: Cell 2 and Cell 3 |  |
| Measurement gap type |  | 1, 2, 3 | Per-UE gaps |  |
| Measurement gap repitition periodicity | ms | 1, 2, 3 | 40 |  |
| Measurement gap length | ms | 1, 2, 3 | 6 |  |
| Measurement gap offset | ms | 1, 2, 3 | 39 |  |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |
| DBT window configuration |  | 1, 2, 3 | Cell 1: N/ACell 2,3: DBT.1 |  |
| CSI-RS parameters in Cell 1 |  | 1 | CSI-RS.1.2 FDD resource #0 |  |
|  |  | 2 | CSI-RS.1.2 TDD resource #0 |  |
|  |  | 3 | CSI-RS.2.2 TDD resource #0 |  |
| A3-Offset | dB | 1, 2, 3 | -4.5 |  |
| Event A3 measurement quantity |  |  | SS-RSRP |  |
| CP length |  | 1, 2, 3 | Normal |  |
| Hysteresis | dB | 1, 2, 3 | 0 |  |
| Time To Trigger | s | 1, 2, 3 | 0 |  |
| Filter coefficient |  | 1, 2, 3 | 0 | L3 filtering is not used |
| DRX |  | 1, 2, 3 |  | OFF |
| Time offset between Cell 1 and Cell 2 |  | 1 | 3 ms | Asynchronous cells.The timing of Cell 2 is 3ms later than the timing of Cell 1. |
|  |  | 2 | 3 ms | Synchronous cells |
|  |  | 3 | 3 ms | Synchronous cells |
| deriveSSB-IndexFromCell |  | 1 | False |  |
|  |  | 2 | True |  |
|  |  | 3 | True |  |
| T1 | s | 1, 2, 3 | 5 |  |
| T2 | s | 1, 2, 3 | 5 |  |

Table A.13.3.1.3.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gap

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1,2,3 | 1 |  | 2 |  | 2 |  |
| Duplex mode |  |  |  | Config 1 | FDD |  | TDD |  | TDD |  |
|  |  |  |  | Config 2,3 | TDD |  | TDD |  | TDD |  |
| TDD configuration |  |  |  | Config 1 | Not Applicable |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 2 | TDDConf.1.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 3 | TDDConf.2.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  |  | Config 1,2,3 | Not Applicable |  | 12 |  | 12 |  |
| WCCA_DL |  |  | ms | Config 1,2,3 | Not Applicable |  | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| BWchannel |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP configuration | Initial DL BWP |  |  | Config 1,2,3 | DLBWP.0.1 |  | DLBWP.0.1 |  |  |  |
|  | Initial UL BWP |  |  |  | ULBWP.0.1 |  | ULBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  |  | DLBWP.1.1 |  | DLBWP.1.1 |  |  |  |
|  | Dedicated UL BWP |  |  |  | ULBWP.1.1 |  | ULBWP.1.1 |  |  |  |
| TRS configuration |  |  |  | Config 1 | TRS.1.1 FDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 2 | TRS.1.1 TDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 3 | TRS.1.2 TDD |  | TRS.1.2 TDD |  |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1,2,3 | OP.1 |  | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1 | SR.1.1 FDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | SR.1.1 TDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | SR2.1 TDD |  | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1 | CR.1.1 FDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | CR.1.1 TDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | CR2.1 TDD |  | CR.1.1 CCA |  |  |  |
| SSB |  | Semi- |  | Config 1 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
| parameters |  | static channel Note 5,7 |  | Config 2 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  |  |  | Config 3 | SSB.2 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  | Dynamic |  | Config 1 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | channel |  | Config 2 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | Access Note 6,7 |  | Config 3 | SSB.2 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  |  | Config 1,2,3 | Not Applicable |  | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1,2,3 | SMTC.1 |  | SMTC.1 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 2 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 3 | 30 |  | 30 |  | 30 |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1,2,3 | 0 |  | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1,2,3 | -98 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1,2 | -98 |  | -95 |  | -95 |  |
|  |  |  |  | Config 3 | -95 |  | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1,2 | -94 | -94 | -91 | -91 | -Infinity | -88 |
|  |  |  |  | Config 3 | -91 | -91 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1,2,3 | 4 | 4 | 4 | -3.79 | -Infinity | 1.54 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1,2,3 | 4 | 4 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/ChBW | Config 1,2 | -64.59 | -64.59 | -58.49 | -54.64 | -58.49 | -54.64 |
|  |  |  | dBm/ChBW | Config 3 | -58.49 | -58.49 | -58.49 | -54.64 | -58.49 | -54.64 |
| Propagation Condition |  |  |  | Config 1,2,3 | AWGN |  | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |  |  |

##### A.13.3.1.3.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_intra_without_index_CCA ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

Tidentify_intra_cca_without_index = (TPSS/SSS_sync_intra_cca + T SSB_measurement_period_intra_cca) ms, where

TPSS/SSS_sync_intra_cca: it is the time period used in PSS/SSS detection given in table 9.2A.6.1-1.

T SSB_measurement_period_intra_cca: equal to a measurement period of SSB based measurement given in table 9.2A.6.2-1.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.13.3.1.4 Event-triggered reporting tests on SCC with per-UE gaps under DRX

##### A.13.3.1.4.1 Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.6.1 and 9.2A.6.2.

##### A.13.3.1.4.2 Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), and two cells on the same carrier frequency with CCA and transmit SSBs in DBT windows according to DL CCA model: SCell (Cell 2) and a neighbour cell (Cell 3). The test parameters for the three cells are given in table A.13.3.1.4.2-1 and A.13.3.1.4.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 3.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There are two BWPs configured in Cell 1, BWP0 which contains the cell defining SSB, and BWP1 which does not contain any SSB of Cell 1. During the whole test, BWP1 is always scheduled as the active BWP for the UE.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.13.3.1.4.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.13.3.1.4.2-2: General test parameters for intra-frequency event triggered reporting without gap with DRX

| Parameter | Unit | Test Configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| Active PCell |  | 1, 2, 3 | Cell 1 |  |  |
| Active SCell |  | 1, 2, 3 | Cell 2 |  |  |
| Neighbour cell |  | 1, 2, 3 | Cell 3 |  | Cell to be identified. |
| RF Channel Number |  | 1, 2, 3 | 1: Cell 12: Cell 2 and Cell 3 |  |  |
| Measurement gap type |  | 1, 2, 3 | Per-UE gaps |  |  |
| Measurement gap repitition periodicity | ms | 1, 2, 3 | 40 |  |  |
| Measurement gap length | ms | 1, 2, 3 | 6 |  |  |
| Measurement gap offset | ms | 1, 2, 3 | 39 |  |  |
| DL CCA model |  |  | As specified in clause A.3.26.2.1 |  |  |
| UL CCA model |  |  | As specified in clause A.3.26.2.2 |  |  |
| DBT window configuration |  | 1, 2, 3 | Cell 1: N/ACell 2,3: DBT.1 |  |  |
| CSI-RS parameters in Cell 1 |  | 1 | CSI-RS.1.2 FDD resource #0 |  |  |
|  |  | 2 | CSI-RS.1.2 TDD resource #0 |  |  |
|  |  | 3 | CSI-RS.2.2 TDD resource #0 |  |  |
| A3-Offset | dB | 1, 2, 3 | -4.5 |  |  |
| Event A3 measurement quantity |  |  | SS-RSRP |  |  |
| CP length |  | 1, 2, 3 | Normal |  |  |
| Hysteresis | dB | 1, 2, 3 | 0 |  |  |
| Time To Trigger | s | 1, 2, 3 | 0 |  |  |
| Filter coefficient |  | 1, 2, 3 | 0 |  | L3 filtering is not used |
| DRX |  | 1, 2, 3 | DRX.1 | DRX.2 |  |
| Time offset between Cell 1 and Cell 2 |  | 1 | 3 ms |  | Asynchronous cells.The timing of Cell 2 is 3ms later than the timing of Cell 1. |
|  |  | 2 | 3 ms |  | Synchronous cells |
|  |  | 3 | 3 ms |  | Synchronous cells |
| deriveSSB-IndexFromCell |  | 1 | False |  |  |
|  |  | 2 | True |  |  |
|  |  | 3 | True |  |  |
| T1 | s | 1, 2, 3 | 5 |  |  |
| T2 | s | 1, 2, 3 | 5 | 20 |  |

Table A.13.3.1.4.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gap

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1,2,3 | 1 |  | 2 |  | 2 |  |
| Duplex mode |  |  |  | Config 1 | FDD |  | TDD |  | TDD |  |
|  |  |  |  | Config 2,3 | TDD |  | TDD |  | TDD |  |
| TDD configuration |  |  |  | Config 1 | Not Applicable |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 2 | TDDConf.1.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 3 | TDDConf.2.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  |  | Config 1,2,3 | Not Applicable |  | 12 |  | 12 |  |
| WCCA_DL |  |  | ms | Config 1,2,3 | Not Applicable |  | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| BWchannel |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP configuration | Initial DL BWP |  |  | Config 1,2,3 | DLBWP.0.1 |  | DLBWP.0.1 |  |  |  |
|  | Initial UL BWP |  |  |  | ULBWP.0.1 |  | ULBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  |  | DLBWP.1.1 |  | DLBWP.1.1 |  |  |  |
|  | Dedicated UL BWP |  |  |  | ULBWP.1.1 |  | ULBWP.1.1 |  |  |  |
| TRS configuration |  |  |  | Config 1 | TRS.1.1 FDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 2 | TRS.1.1 TDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 3 | TRS.1.2 TDD |  | TRS.1.2 TDD |  |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1,2,3 | OP.1 |  | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1 | SR.1.1 FDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | SR.1.1 TDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | SR2.1 TDD |  | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1 | CR.1.1 FDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | CR.1.1 TDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | CR2.1 TDD |  | CR.1.1 CCA |  |  |  |
| SSB |  | Semi- |  | Config 1 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
| parameters |  | static channel Note 5,7 |  | Config 2 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  |  |  | Config 3 | SSB.2 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  | Dynamic |  | Config 1 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | channel |  | Config 2 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | Access Note 6,7 |  | Config 3 | SSB.2 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  |  | Config 1,2,3 | Not Applicable |  | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1,2,3 | SMTC.1 |  | SMTC.1 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 2 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 3 | 30 |  | 30 |  | 30 |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1,2,3 | 0 |  | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1,2,3 | -98 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1,2 | -98 |  | -95 |  | -95 |  |
|  |  |  |  | Config 3 | -95 |  | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1,2 | -94 | -94 | -91 | -91 | -Infinity | -88 |
|  |  |  |  | Config 3 | -91 | -91 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1,2,3 | 4 | 4 | 4 | -3.79 | -Infinity | 1.54 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1,2,3 | 4 | 4 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/ChBW | Config 1,2 | -64.59 | -64.59 | -58.49 | -54.64 | -58.49 | -54.64 |
|  |  |  | dBm/ChBW | Config 3 | -58.49 | -58.49 | -58.49 | -54.64 | -58.49 | -54.64 |
| Propagation Condition |  |  |  | Config 1,2,3 | AWGN |  | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |  |  |

##### A.13.3.1.4.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_intra_without_index_CCA ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

Tidentify_intra_cca_without_index = (TPSS/SSS_sync_intra_cca + T SSB_measurement_period_intra_cca) ms, where

TPSS/SSS_sync_intra_cca: it is the time period used in PSS/SSS detection given in table 9.2A.6.1-1.

T SSB_measurement_period_intra_cca: equal to a measurement period of SSB based measurement given in table 9.2A.6.2-1.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.13.3.1.5 Void

#### A.13.3.1.6 Void

### A.13.3.2 Inter-frequency measurements

#### A.13.3.2.1 Void

#### A.13.3.2.2 Void

#### A.13.3.2.3 Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is not used

##### A.13.3.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements for NR cell with CCA in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1, NR Cell 2 as SCell in FR1 with CCA on NR RF channel 2 and NR Cell 3 as neighbour cell in FR1 with CCA on NR RF channel 3.  The test parameters are given in tables A.13.3.2.3.1-1, A.13.3.2.3.1-2 and A.13.3.2.3.1-3.

In this test, measurement gap pattern configuration # 0 as defined in table A.13.3.2.3.1-2 is provided

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

Table A.13.3.2.3.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1 with CCA

| Config | Description |
| --- | --- |
| 1 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode NR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode NR cell without CCA:  15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode,NR cell without CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.13.3.2.3.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| NR RF Channel Number |  | Config 1,2,3 | 1, 2, 3 | Three FR1 NR carrier frequencies are used. Channels 2 and 3 are with CCA. |
| Active cells |  | Config 1,2,3 | NR Cell 1 (PCell), NR Cell 2 with CCA (SCell) | NR Cell 1 is on NR RF channel number 1. NR Cell 2 is on NR RF channel number 2 with CCA. |
| Neighbour cell |  | Config 1,2,3 | NR Cell 3 with CCA | NR Cell 3 is on NR RF channel number 3 with CCA. |
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
| Time offset between serving and neighbour cells |  | Config 1,2,3 | 3s | Synchronous cells. |
| T1 | s | Config 1,2,3 | 5 |  |
| T2 | s | Config 1,2,3 | 1.7 |  |

Table A.13.3.2.3.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1,2,3 | 1 |  | 2 |  | 3 |  |
| Duplex mode |  |  |  | Config 1 | FDD |  | TDD |  | TDD |  |
|  |  |  |  | Config 2,3 | TDD |  | TDD |  | TDD |  |
| TDD configuration |  |  |  | Config 1 | Not Applicable |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 2 | TDDConf.1.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 3 | TDDConf.2.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  |  | Config 1,2,3 | Not Applicable |  | 12 |  | 12 |  |
| WCCA_DL |  |  | ms | Config 1,2,3 | Not Applicable |  | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| BWchannel |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP configuration | Initial DL BWP |  |  | Config 1,2,3 | DLBWP.0.1 |  | DLBWP.0.1 |  |  |  |
|  | Initial UL BWP |  |  |  | ULBWP.0.1 |  | ULBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  |  | DLBWP.1.1 |  | DLBWP.1.1 |  |  |  |
|  | Dedicated UL BWP |  |  |  | ULBWP.1.1 |  | ULBWP.1.1 |  |  |  |
| TRS configuration |  |  |  | Config 1 | TRS.1.1 FDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 2 | TRS.1.1 TDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 3 | TRS.1.2 TDD |  | TRS.1.2 TDD |  |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1,2,3 | OP.1 |  | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1 | SR.1.1 FDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | SR.1.1 TDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | SR2.1 TDD |  | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1 | CR.1.1 FDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | CR.1.1 TDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | CR2.1 TDD |  | CR.1.1 CCA |  |  |  |
| SSB |  | Semi- |  | Config 1 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
| parameters |  | static channel Note 5,7 |  | Config 2 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  |  |  | Config 3 | SSB.2 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  | Dynamic |  | Config 1 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | channel |  | Config 2 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | Access Note 6,7 |  | Config 3 | SSB.2 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  |  | Config 1,2,3 | Not Applicable |  | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1,2,3 | SMTC.1 |  | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 2 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 3 | 30 |  | 30 |  | 30 |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1,2,3 | 0 |  | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1,2,3 | -98 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1,2 | -98 |  | -95 |  | -95 |  |
|  |  |  |  | Config 3 | -95 |  | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1,2 | -94 | -94 | -91 | -91 | -Infinity | -88 |
|  |  |  |  | Config 3 | -91 | -91 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1,2 | 4 | 4 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1,2 | 4 | 4 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/ChBW | Config 1,2 | -64.59 | -64.59 | -58.49 | -58.49 | -63.94 | -56.15 |
|  |  |  | dBm/ChBW | Config 3 | -58.49 | -58.49 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  |  | Config 1,2,3 | AWGN |  | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |  |  |

##### A.13.3.2.3.2 Test Requirements

In this test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

For test 1, MGRP = 40 ms and for test 2 MGRP = 20 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.13.3.2.4 Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is used

##### A.13.3.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1, NR Cell 2 as SCell in FR1 with CCA on NR RF channel 2 and NR Cell 3 as neighbour cell in FR1 with CCA on NR RF channel 3.  The test parameters are given in tables A.13.3.2.4.1-1, A.13.3.2.4.1-2 and A.13.3.2.4.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.13.3.2.4.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.13.3.2.4.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1 with CCA

| Config | Description |
| --- | --- |
| 1 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode NR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode NR cell without CCA:  15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode,NR cell without CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.13.3.2.4.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| NR RF Channel Number |  | Config 1,2,3 | 1, 2, 3 |  | Three FR1 NR carrier frequencies are used. Channels 2 and 3 are with CCA. |
| Active cells |  | Config 1,2,3 | NR Cell 1 (PCell), NR Cell 2 with CCA (SCell) |  | NR Cell 1 is on NR RF channel number 1. NR Cell 2 is on NR RF channel number 2 with CCA. |
| Neighbour cell |  | Config 1,2,3 | NR Cell 3 with CCA |  | NR Cell 3 is on NR RF channel number 3 with CCA. |
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
| Time offset between serving and neighbour cells |  | Config 1,2,3 | 3s |  | Synchronous cells. |
| T1 | s | Config 1,2,3 | 5 |  |  |
| T2 | s | Config 1,2,3 | 2.5 | 17 |  |

Table A.13.3.2.4.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1,2,3 | 1 |  | 2 |  | 3 |  |
| Duplex mode |  |  |  | Config 1 | FDD |  | TDD |  | TDD |  |
|  |  |  |  | Config 2,3 | TDD |  | TDD |  | TDD |  |
| TDD configuration |  |  |  | Config 1 | Not Applicable |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 2 | TDDConf.1.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 3 | TDDConf.2.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  |  | Config 1,2,3 | Not Applicable |  | 5 |  | 5 |  |
| WCCA_DL |  |  | ms | Config 1,2,3 | Not Applicable |  | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| BWchannel |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP configuration | Initial DL BWP |  |  | Config 1,2,3 | DLBWP.0.1 |  | DLBWP.0.1 |  |  |  |
|  | Initial UL BWP |  |  |  | ULBWP.0.1 |  | ULBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  |  | DLBWP.1.1 |  | DLBWP.1.1 |  |  |  |
|  | Dedicated UL BWP |  |  |  | ULBWP.1.1 |  | ULBWP.1.1 |  |  |  |
| TRS configuration |  |  |  | Config 1 | TRS.1.1 FDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 2 | TRS.1.1 TDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 3 | TRS.1.2 TDD |  | TRS.1.2 TDD |  |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1,2,3 | OP.1 |  | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1 | SR.1.1 FDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | SR.1.1 TDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | SR2.1 TDD |  | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1 | CR.1.1 FDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | CR.1.1 TDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | CR2.1 TDD |  | CR.1.1 CCA |  |  |  |
| SSB |  | Semi- |  | Config 1 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
| parameters |  | static channel Note 5,7 |  | Config 2 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  |  |  | Config 3 | SSB.2 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  | Dynamic |  | Config 1 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | channel |  | Config 2 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | Access Note 6,7 |  | Config 3 | SSB.2 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  |  | Config 1,2,3 | Not Applicable |  | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1,2,3 | SMTC.1 |  | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 2 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 3 | 30 |  | 30 |  | 30 |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1,2,3 | 0 |  | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1,2,3 | -98 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1,2 | -98 |  | -95 |  | -95 |  |
|  |  |  |  | Config 3 | -95 |  | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1,2 | -94 | -94 | -91 | -91 | -Infinity | -88 |
|  |  |  |  | Config 3 | -91 | -91 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1,2 | 4 | 4 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1,2 | 4 | 4 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/ChBW | Config 1,2 | -64.59 | -64.59 | -58.49 | -58.49 | -63.94 | -56.15 |
|  |  |  | dBm/ChBW | Config 3 | -58.49 | -58.49 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  |  | Config 1,2,3 | AWGN |  | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |  |  |

Table A.13.3.2.4.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

| Field | Test1&3 | Test2&4 | Comment |
| --- | --- | --- | --- |
|  | Value | Value |  |
| drx-onDurationTimer | ms1 | ms1 | As specified in clause 6.3.2 in TS 38.331 [2] |
| drx-InactivityTimer | ms1 | ms1 |  |
| drx-RetransmissionTimerDL | sl1 | sl1 |  |
| drx-RetransmissionTimerUL | sl1 | sl1 |  |
| drx-LongCycleStartOffset | ms40 | Ms640 |  |
| shortDRX | disable | disable |  |

Table A.13.3.2.4.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value | Comment |
| --- | --- | --- |
| TimeAlignmentTimer | ms500 | As specified in clause 6.3.2 in TS 38.331 [2] |

##### A.13.3.2.4.2 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2 UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1 DRX cycle = 40 ms and for test 2 DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.13.3.2.5 Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is not used

##### A.13.3.2.5.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1, NR Cell 2 as SCell in FR1 with CCA on NR RF channel 2 and NR Cell 3 as neighbour cell in FR1 with CCA on NR RF channel 3.   The test parameters are given in tables A.13.3.2.5.1-1, A.13.3.2.5.1-2 and A.13.3.2.5.1-3.

Measurement gap pattern configuration # 0 as defined in table A.13.3.2.5.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

Table A.13.3.2.5.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1 with CCA

| Config | Description |
| --- | --- |
| 1 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode NR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode NR cell without CCA:  15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode,NR cell without CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.13.3.2.5.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| NR RF Channel Number |  | Config 1,2,3 | 1, 2, 3 | Three FR1 NR carrier frequencies are used. Channels 2 and 3 are with CCA. |
| Active cells |  | Config 1,2,3 | NR Cell 1 (PCell), NR Cell 2 with CCA (SCell) | NR Cell 1 is on NR RF channel number 1. NR Cell 2 is on NR RF channel number 2 with CCA. |
| Neighbour cell |  | Config 1,2,3 | NR Cell 3 with CCA | NR Cell 3 is on NR RF channel number 3 with CCA. |
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
| Time offset between serving and neighbour cells |  | Config 1,2,3 | 3s | Synchronous cells. |
| T1 | s | Config 1,2,3 | 5 |  |
| T2 | s | Config 1,2,3 | 2 |  |

Table A.13.3.2.5.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1,2,3 | 1 |  | 2 |  | 3 |  |
| Duplex mode |  |  |  | Config 1 | FDD |  | TDD |  | TDD |  |
|  |  |  |  | Config 2,3 | TDD |  | TDD |  | TDD |  |
| TDD configuration |  |  |  | Config 1 | Not Applicable |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 2 | TDDConf.1.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 3 | TDDConf.2.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  |  | Config 1,2,3 | Not Applicable |  | 5 |  | 5 |  |
| WCCA_DL |  |  | ms | Config 1,2,3 | Not Applicable |  | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| BWchannel |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP configuration | Initial DL BWP |  |  | Config 1,2,3 | DLBWP.0.1 |  | DLBWP.0.1 |  |  |  |
|  | Initial UL BWP |  |  |  | ULBWP.0.1 |  | ULBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  |  | DLBWP.1.1 |  | DLBWP.1.1 |  |  |  |
|  | Dedicated UL BWP |  |  |  | ULBWP.1.1 |  | ULBWP.1.1 |  |  |  |
| TRS configuration |  |  |  | Config 1 | TRS.1.1 FDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 2 | TRS.1.1 TDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 3 | TRS.1.2 TDD |  | TRS.1.2 TDD |  |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1,2,3 | OP.1 |  | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1 | SR.1.1 FDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | SR.1.1 TDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | SR2.1 TDD |  | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1 | CR.1.1 FDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | CR.1.1 TDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | CR2.1 TDD |  | CR.1.1 CCA |  |  |  |
| SSB |  | Semi- |  | Config 1 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
| parameters |  | static channel Note 5,7 |  | Config 2 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  |  |  | Config 3 | SSB.2 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  | Dynamic |  | Config 1 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | channel |  | Config 2 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | Access Note 6,7 |  | Config 3 | SSB.2 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  |  | Config 1,2,3 | Not Applicable |  | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1,2,3 | SMTC.1 |  | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 2 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 3 | 30 |  | 30 |  | 30 |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1,2,3 | 0 |  | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1,2,3 | -98 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1,2 | -98 |  | -95 |  | -95 |  |
|  |  |  |  | Config 3 | -95 |  | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1,2 | -94 | -94 | -91 | -91 | -Infinity | -88 |
|  |  |  |  | Config 3 | -91 | -91 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1,2 | 4 | 4 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1,2 | 4 | 4 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/ChBW | Config 1,2 | -64.59 | -64.59 | -58.49 | -58.49 | -63.94 | -56.15 |
|  |  |  | dBm/ChBW | Config 3 | -58.49 | -58.49 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  |  | Config 1,2,3 | AWGN |  | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration |  |  |  |  |  |  |  |  |  |  |

##### A.13.3.2.5.2 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In this test UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.13.3.2.6 Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is used

##### A.13.3.2.6.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1, NR Cell 2 as SCell in FR1 with CCA on NR RF channel 2 and NR Cell 3 as neighbour cell in FR1 with CCA on NR RF channel 3.  The test parameters are given in tables A.13.3.2.6.1-1, A.13.3.2.6.1-2 and A.13.3.2.6.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.13.3.2.6.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.13.3.2.6.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1 with CCA

| Config | Description |
| --- | --- |
| 1 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode NR cell without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode NR cell without CCA:  15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR cell with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode,NR cell without CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE 1: The UE is only required to be tested in one of the supported test configurations |  |

Table A.13.3.2.6.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| NR RF Channel Number |  | Config 1,2,3 | 1, 2, 3 |  | Three FR1 NR carrier frequencies are used. Channels 2 and 3 are with CCA. |
| Active cells |  | Config 1,2,3 | NR Cell 1 (PCell), NR Cell 2 with CCA (SCell) |  | NR Cell 1 is on NR RF channel number 1. NR Cell 2 is on NR RF channel number 2 with CCA. |
| Neighbour cell |  | Config 1,2,3 | NR Cell 3 with CCA |  | NR Cell 3 is on NR RF channel number 3 with CCA. |
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
| Time offset between serving and neighbour cells |  | Config 1,2,3 | 3s |  | Synchronous cells. |
| T1 | s | Config 1,2,3 | 5 |  |  |
| T2 | s | Config 1,2,3 | 3 | 20 |  |

Table A.13.3.2.6.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

| Parameter |  |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  | Cell 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | T1 | T2 | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  |  | Config 1,2,3 | 1 |  | 2 |  | 3 |  |
| Duplex mode |  |  |  | Config 1 | FDD |  | TDD |  | TDD |  |
|  |  |  |  | Config 2,3 | TDD |  | TDD |  | TDD |  |
| TDD configuration |  |  |  | Config 1 | Not Applicable |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 2 | TDDConf.1.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
|  |  |  |  | Config 3 | TDDConf.2.1 |  | TDDConf.1.1 CCA |  | TDDConf.1.1 CCA |  |
| DL CCA probability PCCA_DL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL=0.9375 |  | PCCA_DL=0.9375 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |
| UL CCA probability PCCA_UL |  | Semi-static channel access Note 5,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
|  |  | Dynamic channel access Note 6,7 |  | Config 1,2,3 | Not Applicable |  | PCCA_UL=1 |  | PCCA_UL=1 |  |
| LCCA_DL |  |  |  | Config 1,2,3 | Not Applicable |  | 2 |  | 2 |  |
| WCCA_DL |  |  | ms | Config 1,2,3 | Not Applicable |  | TPSS/SSS_sync_inter_cca |  | TPSS/SSS_sync_inter_cca |  |
| BWchannel |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP BW |  |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
|  |  |  |  | Config 3 | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  | 40: NPRB,c = 106 |  |
| BWP configuration | Initial DL BWP |  |  | Config 1,2,3 | DLBWP.0.1 |  | DLBWP.0.1 |  |  |  |
|  | Initial UL BWP |  |  |  | ULBWP.0.1 |  | ULBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  |  | DLBWP.1.1 |  | DLBWP.1.1 |  |  |  |
|  | Dedicated UL BWP |  |  |  | ULBWP.1.1 |  | ULBWP.1.1 |  |  |  |
| TRS configuration |  |  |  | Config 1 | TRS.1.1 FDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 2 | TRS.1.1 TDD |  | TRS.1.2 TDD |  |  |  |
|  |  |  |  | Config 3 | TRS.1.2 TDD |  | TRS.1.2 TDD |  |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  |  | Config 1,2,3 | OP.1 |  | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  |  | Config 1 | SR.1.1 FDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | SR.1.1 TDD |  | SR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | SR2.1 TDD |  | SR.1.1 CCA |  |  |  |
| CORESET Reference Channel |  |  |  | Config 1 | CR.1.1 FDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 2 | CR.1.1 TDD |  | CR.1.1 CCA |  |  |  |
|  |  |  |  | Config 3 | CR2.1 TDD |  | CR.1.1 CCA |  |  |  |
| SSB |  | Semi- |  | Config 1 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
| parameters |  | static channel Note 5,7 |  | Config 2 | SSB.1 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  |  |  | Config 3 | SSB.2 FR1 |  | SSB.1 CCA |  | SSB.1 CCA |  |
|  |  | Dynamic |  | Config 1 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | channel |  | Config 2 | SSB.1 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
|  |  | Access Note 6,7 |  | Config 3 | SSB.2 FR1 |  | SSB.2 CCA |  | SSB.2 CCA |  |
| DBT window configuration |  |  |  | Config 1,2,3 | Not Applicable |  | As defined in A.3.28.1 |  | As defined in A.3.28.1 |  |
| SMTC configuration defined in A.3.11 |  |  |  | Config 1,2,3 | SMTC.1 |  | SMTC.1 |  | SMTC.4 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | Config 1 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 2 | 15 |  | 30 |  | 30 |  |
|  |  |  |  | Config 3 | 30 |  | 30 |  | 30 |  |
| EPRE ratio of PSS to SSS |  |  |  | Config 1,2,3 | 0 |  | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15 kHz | Config 1,2,3 | -98 |  | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/SCS | Config 1,2 | -98 |  | -95 |  | -95 |  |
|  |  |  |  | Config 3 | -95 |  | -95 |  | -95 |  |
| SS-RSRP Note 3 |  |  | dBm/SCS | Config 1,2 | -94 | -94 | -91 | -91 | -Infinity | -88 |
|  |  |  |  | Config 3 | -91 | -91 | -91 | -91 | -Infinity | -88 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | Config 1,2 | 4 | 4 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | Config 1,2 | 4 | 4 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  |  | dBm/ChBW | Config 1,2 | -64.59 | -64.59 | -58.49 | -58.49 | -63.94 | -56.15 |
|  |  |  | dBm/ChBW | Config 3 | -58.49 | -58.49 | -58.49 | -58.49 | -63.94 | -56.15 |
| Propagation Condition |  |  |  | Config 1,2,3 | AWGN |  | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 6: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 7: For UE supporting both semi-static and dynamic channel access, the UE must be tested under dynamic channel access configuration. |  |  |  |  |  |  |  |  |  |  |

Table A.13.3.2.6.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

| Field | Test1 | Test2 | Comment |
| --- | --- | --- | --- |
|  | Value | Value |  |
| drx-onDurationTimer | ms1 | ms1 | As specified in clause 6.3.2 in TS 38.331 [2] |
| drx-InactivityTimer | ms1 | ms1 |  |
| drx-RetransmissionTimerDL | sl1 | sl1 |  |
| drx-RetransmissionTimerUL | sl1 | sl1 |  |
| drx-LongCycleStartOffset | ms40 | Ms640 |  |
| shortDRX | disable | disable |  |

Table A.13.3.2.6.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value | Comment |
| --- | --- | --- |
| TimeAlignmentTimer | ms500 | As specified in clause 6.3.2 in TS 38.331 [2] |

##### A.13.3.2.6.2 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.In test 2 with per-FR gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2 UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1 DRX cycle = 40 ms and for test 2 DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

### A.13.3.3 L1-RSRP measurements for beam reporting

#### A.13.3.3.1 SSB based L1-RSRP measurement when DRX is not used

##### A.13.3.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.13.3.3.1.1-1.

Table A.13.3.3.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

##### A.13.3.3.1.2 Test parameters

There are two cells in the tests, FR1 PCell (Cell 1) and FR1 SCell (Cell 2). Cell 2 operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model. The test parameters and applicability for Cell 1 and Cell 2 are given in table A.13.3.3.1.2-1 and table A.13.3.3.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.13.3.3.1.2-1: General test parameters

| Parameter | Configuration | Unit | Value |  |
| --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 |
| Active PCell/SCell Configuration |  |  | PCell | SCell |
| RF Channel Number |  |  | 1 | 2 |
| DL CCA model | 1~3 |  | N/A | As specifieed in A.3.26.2.1 |
| UL CCA model | 1~3 |  | N/A | As specified in A.3.26.2.2 |
| Duplex mode | 1 |  | FDD | TDD |
|  | 2 |  | TDD |  |
|  | 3 |  | TDD |  |
| TDD Configuration | 1 |  | N/A | TDDConf.1.1 CCA |
|  | 2 |  | TDDConf.1.1 |  |
|  | 3 |  | TDDConf.2.1 |  |
| BWchannel | 1 | MHz | 10: NPRB,c = 52 | 40: NPRB,c = 106 |
|  | 2 |  | 10: NPRB,c = 52 |  |
|  | 3 |  | 40: NPRB,c = 106 |  |
| PDSCH Reference measurement channel | 1 |  | SR.1.1 FDD | SR.1.1 CCA |
|  | 2 |  | SR.1.1 TDD |  |
|  | 3 |  | SR.2.1 TDD |  |
| RMSI CORESET Reference Channel | 1 |  | CR.1.1 FDD | CR.1.1 CCA |
|  | 2 |  | CR.1.1 TDD |  |
|  | 3 |  | CR.2.1 TDD |  |
| Dedicated CORESET Reference Channel | 1 |  | CCR.1.1 FDD | CCR.1.1 CCA |
|  | 2 |  | CCR.1.1 TDD |  |
|  | 3 |  | CCR.2.1 TDD |  |
| SSB configuration | 1 |  | SSB.3 FR1 | SSB.3 CCA for semi-static channel access |
|  | 2 |  | SSB.3 FR1 | SSB.4 CCA for dynamic channel access |
|  | 3 |  | SSB.4 FR1 |  |
| OCNG Patterns | 1~3 |  | OP.1 | OP.1 |
| Initial BWP Configuration | 1~3 |  | DLBWP.0.1ULBWP.0.1 | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1~3 |  | DLBWP.1.1ULBWP.1.1 | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration | 1~3 |  | SMTC.1 | N/A |
| DBT Window Configuration | 1~3 |  | N/A | DBT.1 |
| TRS Configuration | 1 |  | TRS.1.1 FDD | TRS.1.2 TDD |
|  | 2 |  | TRS.1.1 TDD |  |
|  | 3 |  | TRS.1.2 TDD |  |
| DRX configuration | 1~3 |  | Off | Off |
| reportConfigType | 1~3 |  | periodic | periodic |
| reportQuantity | 1~3 |  | ssb-Index-RSRP | ssb-Index-RSRP |
| Number of reported RS | 1~3 |  | 2 | 2 |
| L1-RSRP reporting period | 1~3 | slot | 80 | 80 |
| T1 | 1~3 | s | 5 | 5 |
| T2 | 1~3 | s | 1 | 1 |
| EPRE ratio of PSS to SSS | 1~3 | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |
| Propagation condition | 1~3 |  | AWGN | AWGN |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window. |  |  |  |  |

Table A.13.3.3.1.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |  |
| DL CCA Probability PCCA_DL Note 4,6 | 1,2,3 |  | 0.9375 | 0.9375 | 0.9375 | 0.9375 |  |
| DL CCA Probability PCCA_DL Note 4.7 | 1,2,3 |  | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 |  |
| UL CCA probability PCCA_UL | 1,2,3 |  | 1.0 | 1.0 | 1.0 | 1.0 |  |
| Note2 | 1,2,3 | dBm/15 kHz | -94.65 |  |  |  |  |
| Note2 | 1,2,3 | dBm/SSB SCS | -91.65 |  |  |  |  |
|  | 1,2,3 | dB | 0 | 0 | -Infinity | 3 |  |
| SSB RSRP Note3 | 1,2,3 | dBm/SSB SCS | -91.65 | -91.65 | -Infinity | -88.65 |  |
| Io Note3 | 1,2,3 | dBm/38.16 MHz | -57.59 | -57.59 | -60.61 | -55.84 |  |
|  | 1,2,3 | dB | 0 | 0 | -Infinity | 3 |  |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: DL and UL CCA probabilities apply for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.NOTE 5: The signal levels apply for SSS Res when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2. |  |  |  |  |  |  |  |

##### A.13.3.3.1.3 Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 2.

NOTE: The actual overall delays measured in the test may be up to 2xTTI DCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.13.3.3.2 SSB based L1-RSRP measurement when DRX is used

##### A.13.3.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.13.3.3.1.1-1.

Table A.13.3.3.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

##### A.13.3.3.2.2 Test parameters

There are two cells in the tests, FR1 Pcell (Cell 1) and FR1 Scell (Cell 2). Cell 2 operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model. The test parameters and applicability for Cell 1  and Cell 2 are given in table A.13.3.3.2.2-1 and table A.13.3.3.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.13.3.3.2.2-1: General test parameters

| Parameter | Configuration | Unit | Value |  |
| --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 |
| Active Pcell/Scell Configuration |  |  | Pcell | Scell |
| RF Channel Number |  |  | 1 | 2 |
| DL CCA model | 1~3 |  | N/A | As specifieed in A.3.26.2.1 |
| UL CCA model | 1~3 |  | N/A | As specified in A.3.26.2.2 |
| Duplex mode | 1 |  | FDD | TDD |
|  | 2 |  | TDD |  |
|  | 3 |  | TDD |  |
| TDD Configuration | 1 |  | N/A | TDDConf.1.1 CCA |
|  | 2 |  | TDDConf.1.1 |  |
|  | 3 |  | TDDConf.2.1 |  |
| BWchannel | 1 | MHz | 10: NPRB,c = 52 | 40: NPRB,c = 106 |
|  | 2 |  | 10: NPRB,c = 52 |  |
|  | 3 |  | 40: NPRB,c = 106 |  |
| PDSCH Reference measurement channel | 1 |  | SR.1.1 FDD | SR.1.1 CCA |
|  | 2 |  | SR.1.1 TDD |  |
|  | 3 |  | SR.2.1 TDD |  |
| RMSI CORESET Reference Channel | 1 |  | CR.1.1 FDD | CR.1.1 CCA |
|  | 2 |  | CR.1.1 TDD |  |
|  | 3 |  | CR.2.1 TDD |  |
| Dedicated CORESET Reference Channel | 1 |  | CCR.1.1 FDD | CCR.1.1 CCA |
|  | 2 |  | CCR.1.1 TDD |  |
|  | 3 |  | CCR.2.1 TDD |  |
| SSB configuration | 1 |  | SSB.3 FR1 | SSB.3 CCA for semi-static channel access |
|  | 2 |  | SSB.3 FR1 | SSB.4 CCA for dynamic channel access |
|  | 3 |  | SSB.4 FR1 |  |
| OCNG Patterns | 1~3 |  | OP.1 | OP.1 |
| Initial BWP Configuration | 1~3 |  | DLBWP.0.1ULBWP.0.1 | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1~3 |  | DLBWP.1.1ULBWP.1.1 | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration | 1~3 |  | SMTC.1 | N/A |
| DBT Window Configuration | 1~3 |  | N/A | DBT.1 |
| TRS Configuration | 1 |  | TRS.1.1 FDD | TRS.1.2 TDD |
|  | 2 |  | TRS.1.1 TDD |  |
|  | 3 |  | TRS.1.2 TDD |  |
| DRX configuration | 1~3 |  | DRX.3 | DRX.3 |
| reportConfigType | 1~3 |  | periodic | periodic |
| reportQuantity | 1~3 |  | ssb-Index-RSRP | ssb-Index-RSRP |
| Number of reported RS | 1~3 |  | 2 | 2 |
| L1-RSRP reporting period | 1~3 | slot | 80 | 80 |
| T1 | 1~3 | s | 5 | 5 |
| T2 | 1~3 | s | 1 | 1 |
| EPRE ratio of PSS to SSS | 1~3 | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |
| Propagation condition | 1~3 |  | AWGN | AWGN |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window. |  |  |  |  |

Table A.13.3.3.2.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |  |
| DL CCA Probability PCCA_DL Note 4,6 | 1,2,3 |  | 0.9375 | 0.9375 | 0.9375 | 0.9375 |  |
| DL CCA Probability PCCA_DL Note 4.7 | 1,2,3 |  | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 | 0.75/0.75 |  |
| UL CCA probability PCCA_UL | 1,2,3 |  | 1.0 | 1.0 | 1.0 | 1.0 |  |
| Note2 | 1,2,3 | dBm/15 kHz | -94.65 |  |  |  |  |
| Note2 | 1,2,3 | dBm/SSB SCS | -91.65 |  |  |  |  |
|  | 1,2,3 | dB | 0 | 0 | -Infinity | 3 |  |
| SSB RSRP Note3 | 1,2,3 | dBm/SSB SCS | -91.65 | -91.65 | -Infinity | -88.65 |  |
| Io Note3 | 1,2,3 | dBm/38.16 MHz | -57.59 | -57.59 | -60.61 | -55.84 |  |
|  | 1,2,3 | dB | 0 | 0 | -Infinity | 3 |  |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: DL and UL CCA probabilities apply for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.NOTE 5: The signal levels apply for SSS Res when the discovery burst is transmitted during DBT windows.NOTE 6: For UE supporting semi-static channel access and network configuring semi-static channel occupancy. NOTE 7: For UE supporting dynamic channel access and network configuring dynamic channel occupancy. The first value corresponds PCCA_DL1 and the second value corresponds to the PCCA_DL2. |  |  |  |  |  |  |  |

##### A.13.3.3.2.3 Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 2.

NOTE: The actual overall delays measured in the test may be up to 2xTTI DCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.13.4 Measurement performance

### A.13.4.1 SS-RSRP

#### A.13.4.1.1 Intra-frequency measurement accuracy on a carrier frequency with CCA

##### A.13.4.1.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy on the carrier frequency with CCA is within the specified limits. This test will verify the requirements in clauses 10.1.36.1.1 and 10.1.36.1.2 for intra-frequency measurements under CCA.

##### A.13.4.1.1.2 Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), and two cells on the same carrier frequency with CCA and transmit SSBs in DBT windows according to DL CCA model: SCell (Cell 2) and a neighbour cell (Cell 3). Supported test configurations are shown in table A.13.4.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.13.4.1.1.2-2.

Table A.13.4.1.1.2-1: SS-RSRP  Intra frequency SS-RSRP supported test configurations

| Config | Description |
| --- | --- |
| 1 | NR carrier with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR carrier without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NR carrier with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR carrier without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | NR carrier with CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeNR carrier without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations for each supported band |  |

Table A.13.4.1.1.2-2: SS-RSRP Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 | Cell 3 | Cell 2 | Cell 3 | Cell 2 | Cell 3 |
| Cell ID |  |  |  | 489 | 0 | 489 | 0 | 489 | 0 |
| SSB ARFCN |  |  |  | freq1 |  | freq1 |  | freq1 |  |
| DL CCA model |  |  |  | As specified in clause A.3.26.2.1 |  |  |  |  |  |
| UL CCA model |  |  |  | As specified in clause A.3.26.2.2 |  |  |  |  |  |
| PCCA_DL for dynamic channel access Note 7,9 |  |  |  | PCCA_DL_1=0.75PCCA_DL_2=0.75 |  |  |  |  |  |
| PCCA_DL for semi-static channel access Note 8,9 |  |  |  | PCCA_DL=0.9375 |  |  |  |  |  |
| PCCA_UL |  |  |  | 1 |  |  |  |  |  |
| TDD configuration |  | Config 1,2,3 |  | TDDConf.1.1 CCA |  |  |  |  |  |
| BWchannel |  | Config 1,2,3 | MHz | 40: NPRB,c = 106 |  |  |  |  |  |
| BWP BW |  | Config 1,2,3 |  | 40: NPRB,c = 106 |  |  |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |  |  |
| TRS configuration |  | Config 1,2,3 |  | TRS.1.2 TDD | NA | TRS.1.2 TDD | NA | TRS.1.2 TDD | NA |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |  |
| PDSCH Reference measurement channel |  | Config 1,2,3 |  | SR.1.1 CCA | - | SR.1.1 CCA | - | SR.1.1 CCA | - |
| RMSI CORESET Reference Channel |  | Config 1,2,3 |  | CR.1.1 CCA | - | CR.1.1 CCA | - | CR.1.1 CCA | - |
| Control channel RMC |  | Config 1,2,3 |  | CR.1.1 CCA | - | CR.1.1 CCA | - | CR.1.1 CCA | - |
| SSB configuration for semi-static channel access |  | Config 1,2,3 |  | SSB.1 CCA | SSB.1 CCA | SSB.1 CCA | SSB.1 CCA | SSB.1 CCA | SSB.1 CCA |
| SSB configuration for dynamic channel access |  | Config 1,2,3 |  | SSB.2 CCA | SSB.2 CCA | SSB.2 CCA | SSB.2 CCA | SSB.2 CCA | SSB.2 CCA |
| DBT window configuration |  | Config 1,2,3 |  | DBT.1 | DBT.1 | DBT.1 | DBT.1 | DBT.1 | DBT.1 |
| Time offset with Cell 1 |  | Config 1,2,3 | s | - | 3 | - | 3 | - | 3 |
| SMTC configuration |  | Config 1,2,3 |  | SMTC.1 |  |  |  |  |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2,3 | kHz | 30 kHz |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3 | NR_CCA_FR1_I |  | Not applicableNote 5 |  | -94 |  | -110 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -109.5 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1,2,3 | NR_CCA_FR1_I | dBm/SCS | Not applicableNote 5 |  | -91 |  | -107.0 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -106.5 |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] Note6 |  |  | dB | 2.46 | -5.97 | 2.46 | -5.97 | -2.01 | -3.54 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] Note6 |  |  | dB | 6 | 1 | 6 | 1 | 1 | 0 |
| SS-RSRPNote3,6 | Config 1,2,3 | NR_TDD_FR1_I | dBm/SCS | Not applicableNote 5 | Not applicableNote 5 | -85 | -90 | -106.00 | -107.00 |
|  |  |  |  |  |  |  |  | -105.50 | -106.50 |
| IoNote3 | Config 1,2,3 | NR_CCA_FR1_I | dBm/38.16 MHz | Not applicableNote 5- |  | -51.99 |  | -70.82 |  |
|  |  | NR_CCA_FR1_J |  |  |  |  |  | -70.32 |  |
| Propagation condition |  |  | - | AWGN |  |  |  |  |  |
| Antenna configuration |  |  |  | 1x2 |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: Subtest 1 is not used when testing with 30 kHz SSB SCS.NOTE 6: The signal levels apply for SSS REs when the discovery burst is transmitted during DBT windows.NOTE 7:  For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 8:  For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 9:  For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |  |  |  |  |

##### A.13.4.1.1.3 Test Requirements

The SS-RSRP measurement accuracy for Cell 2 and Cell 3 shall fulfil absolute requirement in clause 10.1.36.1.1 and relative requirement in clause 10.1.36.1.2.

### A.13.4.2 SS-RSRQ

#### A.13.4.2.1 Intra-frequency measurement accuracy on SCC

##### A.13.4.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.29.1.1.

##### A.13.4.2.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.13.4.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.13.4.2.1.2-2 and table A.13.4.2.1.2-3. In all test cases, Cell 1 is the PCell, Cell 2 is the SCell with CCA, and Cell 3 is the target cell with CCA. Three sub-tests (Test 1, Test 2, and Test 3) are provided different Noc on Cells 1, 2, and 3.

Table A.13.4.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

| Config | Description |
| --- | --- |
| 1 | Without CCA: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

Table A.13.4.2.1.2-2: SS-RSRQ Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 | Cell 3 | Cell 2 | Cell 3 |
| SSB ARFCN |  |  |  | freq2 | freq2 | freq2 | freq2 |
| DL CCA model |  | Config 1, 2, 3 |  | As specified in clause A.3.26.2.1 |  |  |  |
| UL CCA model |  | Config 1, 2, 3 |  | As specified in clause A.3.26.2.2 |  |  |  |
| DL CCA probability for semi-static channel access Note 7, 8 |  | PCCA_UL |  | 1.0 | - | 1.0 | - |
|  |  | PCCA_DL |  | 0.9375 | - | 0.9375 | - |
| DL CCA probability fordynamic channel access Note 8, 9 |  | PCCA_DL_1 |  | 0.75 | - | 0.75 | - |
|  |  | PCCA_DL_2 |  | 0.75 | - | 0.75 | - |
| Duplex mode |  | Config 1, 2, 3 |  | TDD |  |  |  |
| TDD configuration |  | Config 1, 2, 3 |  | TDDConf.1.1 CCA |  |  |  |
| BWchannel |  | Config 1, 2, 3 | MHz | 40: NRB,c = 106 |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  | Config 1, 2, 3 |  | SR.1.1 CCA |  | SR.1.1 CCA |  |
| RMSI CORESET Reference Channel |  | Config 1, 2, 3 |  | CR.1.1 CCA |  | CR.1.1 CCA |  |
| Control Channel RMC |  | Config 1, 2, 3 |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  |
| TRS configuration |  | Config 1, 2, 3 |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  |
| OCNG Patterns |  |  |  | OP. 1 |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |
| Time offset with Cell 1 |  | Config 1, 2, 3 | s | 3 | 3 | 3 | 3 |
| DBT Window Configuration |  | Config 1, 2, 3 |  | DBT.1 |  |  |  |
| SSB configuration |  | Config 1, 2, 3 |  | SSB.1 CCA for semi-static channel accessSSB.2 CCA for dynamic channel access |  |  |  |
| SMTC configuration |  | Config 1, 2, 3 |  | SMTC.1 |  |  |  |
| CSI-RS for tracking |  | Config 1, 2, 3 |  | TRS.1.2 TDD |  |  |  |
| PDSCH/PDCCH |  | Config 1, 2, 3 | kHz | 30kHz |  |  |  |
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
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2, 3 | NR_CCA_FR1_I | dBm/15kHz | -91 |  | -110 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -109.5 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2, 3 | NR_CCA_FR1_I | dBm/SCS | -88 |  | -107 |  |
|  |  | NR_CCA_FR1_J |  |  |  | -106.5 |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.76 |  | -5.46 | -5.46 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 | 3 | -4 | -4 |
| SS-RSRPNote3 | Config 1, 2, 3 | NR_CCA_FR1_I | dBm/SCS | -85 | -85 | -111 | -111 |
|  |  | NR_CCA_FR1_J |  |  |  | -110.5 | -110.5 |
| SS-RSRQ Note3 |  | NR_CCA_FR1_I | dB | -14.77 | -14.77 | -17.34 | -17.34 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| IoNote3 | Config 1, 2, 3 | NR_CCA_FR1_I | dBm/38.16MHz | -50 |  | -73.4 | -73.4 |
|  |  | NR_CCA_FR1_J |  |  |  | -72.9 | -72.9 |
| Propagation condition |  |  | - | AWGN | AWGN | AWGN | AWGN |
| Antenna configuration |  |  |  | 1x2 | 1x2 | 1x2 | 1x2 |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.Note 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.Note 3: SS-RSRQ, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.Note 4: SS-RSRQ, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.Note 5: NR operating band groups are as defined in clause 3.5.2.Note 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations.Note 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.Note 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.Note 9: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |

Table A.13.4.2.1.2-3: SS-RSRQ Intra frequency test parameters for NR PCell

| Parameter |  |  |  |  |  | Unit |  | Test 1 |  | Test 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  | Cell 1 |  | Cell 1 |
| SSB ARFCN |  |  |  |  |  |  |  | freq1 |  | freq1 |
| Duplex mode |  |  | Config 1 |  |  |  |  | FDD |  | FDD |
|  |  |  | Config 2,3 |  |  |  |  | TDD |  | TDD |
| TDD configuration |  |  | Config 1 |  |  |  |  | Not Applicable |  | Not Applicable |
|  |  |  | Config 2 |  |  |  |  | TDDConf.1.1 |  | TDDConf.1.1 |
|  |  |  | Config 3 |  |  |  |  | TDDConf.2.1 |  | TDDConf.2.1 |
| BWchannel |  |  | Config 1 |  |  | MHz |  | 10: NRB,c = 52 |  | 10: NRB,c = 52 |
|  |  |  | Config 2 |  |  |  |  | 10: NRB,c = 52 |  | 10: NRB,c = 52 |
|  |  |  | Config 3 |  |  |  |  | 40: NRB,c = 106 |  | 40: NRB,c = 106 |
| Gap Pattern ID |  |  |  |  |  |  |  | 0 |  | 0 |
| Downlink initial BWP configuration |  |  |  |  |  |  |  | DLBWP.0.1 |  | DLBWP.0.1 |
| Downlink dedicated BWP configuration |  |  |  |  |  |  |  | DLBWP.1.1 |  | DLBWP.1.1 |
| Uplink initial BWP configuration |  |  |  |  |  |  |  | ULBWP.0.1 |  | ULBWP.0.1 |
| Uplink dedicated BWP configuration |  |  |  |  |  |  |  | ULBWP.1.1 |  | ULBWP.1.1 |
| DRX Cycle configuration |  |  |  |  |  | ms |  | Not Applicable |  | Not Applicable |
| TRS configuration |  |  | Config 1 |  |  |  |  | TRS.1.1 FDD |  | TRS.1.1 FDD |
|  |  |  | Config 2 |  |  |  |  | TRS.1.1 TDD |  | TRS.1.1 TDD |
|  |  |  | Config 3 |  |  |  |  | TRS.1.2 TDD |  | TRS.1.2 TDD |
| PDSCH Reference measurement channel |  |  | Config 1 |  |  |  |  | SR.1.1 FDD |  | SR.1.1 FDD |
|  |  |  | Config 2 |  |  |  |  | SR.1.1 TDD |  | SR.1.1 TDD |
|  |  |  | Config 3 |  |  |  |  | SR.2.1 TDD |  | SR.2.1 TDD |
| RMSI CORESET Reference Channel |  |  | Config 1 |  |  |  |  | CR.1.1 FDD |  | CR.1.1 FDD |
|  |  |  | Config 2 |  |  |  |  | CR.1.1 TDD |  | CR.1.1 TDD |
|  |  |  | Config 3 |  |  |  |  | CR.2.1 TDD |  | CR.2.1 TDD |
| Dedicated CORESET Reference Channel |  |  | Config 1 |  |  |  |  | CCR.1.1 FDD |  | CCR.1.1 FDD |
|  |  |  | Config 2 |  |  |  |  | CCR.1.1 TDD |  | CCR.1.1 TDD |
|  |  |  | Config 3 |  |  |  |  | CCR.2.1 TDD |  | CCR.2.1 TDD |
| OCNG Patterns |  |  |  |  |  |  |  | OP.1 |  | OP.1 |
| SS-RSSI-Measurement |  |  |  |  |  |  |  | Not Applicable |  | Not Applicable |
| SMTC configuration |  |  | Config 1Config 2,3 |  |  |  |  | SMTC.2 |  | SMTC.2 |
|  |  |  |  |  |  |  |  | SMTC.1 |  | SMTC.1 |
| SSB configuration |  |  | Config 1,2 |  |  |  |  | SSB.1 FR1 |  | SSB.1 FR1 |
|  |  |  | Config 3 |  |  |  |  | SSB.2 FR1 |  | SSB.2 FR1 |
| PDSCH/PDCCH subcarrier spacing |  |  | Config 1,2 |  |  | kHz |  | 15 |  | 15 |
|  |  |  | Config 3 |  |  |  |  | 30 |  | 30 |
| EPRE ratio of PSS to SSS |  |  |  |  |  | dB |  | 0 |  | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | Config 1, 2 | NR_FDD_FR1_A |  |  | dBm/15kHz |  | -85 |  | -114 |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  | -113.5 |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  | -113 |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  | -112.5 |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  | -112 |
|  | NR_FDD_FR1_G |  |  |  |  |  | -111 |  |  |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  | -110.5 |
|  |  | Config 3 | NR_FDD_FR1_A |  |  |  |  | -91 |  | -114 |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  | -113.5 |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  | -113 |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  | -112.5 |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  | -112 |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  |  | -111 |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  | -110.5 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | Config 1,2 | NR_FDD_FR1_A |  |  | dBm/SCS |  | -85 |  | -114 |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  | -113.5 |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  | -113 |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  | -112.5 |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  | -112 |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  |  | -111 |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  | -110.5 |
|  |  | Config 3 | NR_FDD_FR1_A |  |  |  |  | -88 |  | -111 |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  | -110.5 |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  | -110 |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  | -109.5 |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  | -109 |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  |  | -108 |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  | -107.5 |
| ![](media_svg/image7.svg) [公式≈: ^{Ê}s^{I}ot] |  |  |  |  |  | dB |  | -1.76 |  | -5.46 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  |  |  |  | dB |  | 3 |  | -4 |
| SS-RSRPNote3 |  | Config 1,2 | NR_FDD_FR1_A |  |  | dBm/SCS |  | -82 |  | -118 |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  | -117.5 |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  | -117 |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  | -116.5 |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  | -116 |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  |  | -115 |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  | -114.5 |
| Config 3 | NR_FDD_FR1_A |  |  |  | -85 |  | -115 |  |  |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  | -114.5 |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  | -114 |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  | -113.5 |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  | -113 |
|  | NR_FDD_FR1_G |  |  |  |  |  | -112 |  |  |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  | -111.5 |
| SS-RSRQ Note3 |  |  | NR_FDD_FR1_A |  |  | dB |  | -14.77 |  | -17.34 |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  |  |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  |  |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  |  |
| IoNote3 |  | Config 1,2 | NR_FDD_FR1_A |  |  | dBm/9.36MHz |  | -50 |  | -83.5 |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  | -83 |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  | -82.5 |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  | -82 |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  | -81.5 |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  |  | -80.5 |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  | -80 |
| Config 3 | NR_FDD_FR1_A |  |  | dBm/38.16MHz | -50 |  | -77.4 |  |  |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  | -76.9 |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  | -76.4 |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  | -75.9 |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  | -75.4 |
|  | NR_FDD_FR1_G |  |  |  |  |  | -74.4 |  |  |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  | -73.9 |
| Propagation condition |  |  |  |  |  | - |  | AWGN |  | AWGN |
| Antenna configuration |  |  |  |  |  | - |  | 1x2 |  | 1x2 |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.Note 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.Note 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.Note 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.Note 5: NR operating band groups are as defined in clause 3.5.2. |  |  |  |  |  |  |  |  |  |  |

##### A.13.4.2.1.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.29.1.1.

### A.13.4.3 SS-SINR

#### A.13.4.3.1 Intra-frequency measurement accuracy on SCC

##### A.13.4.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.31.1.1.

##### A.13.4.3.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.13.4.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.13.4.3.1.2-2 and table A.13.4.3.1.2-3. In all test cases, Cell 1 is the PCell, Cell 2 is the SCell with CCA, and Cell 3 is the target cell with CCA. Two sub-tests (Test 1 and Test 2) are provided different Noc on Cells 1, 2, and 3.

Table A.13.4.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

| Config | Description |
| --- | --- |
| 1 | Without CCA: NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: NR 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: NR 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

A.13.4.3.1.2-2: SS-SINR Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 2 | Cell 3 | Cell 2 |  | Cell 3 |
| SSB ARFCN |  |  |  | freq2 | freq2 | freq2 |  | freq2 |
| DL CCA model |  | Config 1, 2, 3 |  | As specified in clause A.3.26.2.1 |  |  |  |  |
| UL CCA model |  | Config 1, 2, 3 |  | As specified in clause A.3.26.2.2 |  |  |  |  |
| UL CCA probability |  | PCCA_UL |  | 1.0 | - | 1.0 | - |  |
| DL CCA probability for semi-static channel access Note 7, 8 |  | PCCA_DL |  | 0.9375 | - | 0.9375 | - |  |
| DL CCA probability fordynamic channel access Note 8, 9 |  | PCCA_DL_1 |  | 0.75 | - | 0.75 | - |  |
|  |  | PCCA_DL_2 |  | 0.75 | - | 0.75 | - |  |
| Duplex mode |  | Config 1, 2, 3 |  | TDD |  |  |  |  |
| TDD configuration |  | Config 1, 2, 3 |  | TDDConf.1.1 CCA |  |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |  |  |  |
| TRS configuration |  | Config 1, 2, 3 |  | TRS.1.2 TDD |  | TRS.1.2 TDD |  |  |
| PDSCH Reference measurement channel |  | Config 1, 2, 3 |  | SR.1.1 CCA |  | SR.1.1 CCA |  |  |
| RMSI CORESET Reference Channel |  | Config 1, 2, 3 |  | CR.1.1 CCA |  | CR.1.1 CCA |  |  |
| Dedicated CORESET Reference Channel |  | Config 1, 2, 3 |  | CCR.1.1 CCA |  | CCR.1.1 CCA |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |  |
| DBT Window configuration |  | Config 1, 2, 3 |  | DBT.1 |  |  |  |  |
| Time offset with Cell 1 |  | Config 1, 2, 3 | s | 3 (for Cell 2) | 3 | 3 (for Cell 2) |  | 3 |
| SSB configuration |  | Config 1, 2, 3 |  | SSB.1 CCA for semi-static channel accessSSB.2 CCA for dynamic channel access |  |  |  |  |
| SMTC configuration |  | Config 1, 2, 3 |  | SMTC.1 |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2, 3 | kHz | 30 |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 |  | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | NR_CCA_FR1_I | dBm/15 kHz | -93 |  | -112 |  |  |
|  |  | NR_CCA_FR1_J |  |  |  | -111.5 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2, 3 | NR_CCA_FR1_I | dBm/SCS | -90 |  | -109 |  |  |
|  |  | NR_CCA_FR1_J |  |  |  | -108.5 |  |  |
| ![](media_svg/image7.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 0 | -3.19 | -5.46 |  | -5.46 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4.54 | 2.66 | -4 |  | -4 |
| SS-RSRPNote3 | Config 1, 2, 3 | NR_CCA_FR1_I | dBm/SCS | -85.46 | -87.34 | -113 |  | -113 |
|  |  | NR_CCA_FR1_J |  |  |  | -112.5 |  | -112.5 |
| SS-SINR Note3 |  | NR_CCA_FR1_I | dB | 0 | -3.19 | -5.46 |  | -5.46 |
|  |  | NR_CCA_FR1_J |  |  |  |  |  |  |
| IoNote3 | Config 1, 2, 3 | NR_CCA_FR1_I | dBm/38.16 MHz | -51.41 |  | -75.41 |  |  |
|  |  | NR_CCA_FR1_J |  |  |  | -74.91 |  |  |
| Propagation condition |  |  | - | AWGN |  |  |  |  |
| Antenna configuration |  |  | - | 1x2 |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2. NOTE 6: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configuration.NOTE 7: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 8: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 9: For UE supporting both semi-static and dynamic cannel access, the UE must be tested under both dynamic and semi-static channel occupancy configurations. |  |  |  |  |  |  |  |  |

A.13.4.3.1.2-3: SS-SINR Intra frequency test parameters for NR PCell

| Parameter |  |  |  |  |  |  | Unit |  |  | Test 1 |  |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  | Cell 1 |  |  | Cell 1 |  |
| SSB ARFCN |  |  |  |  |  |  |  |  |  | freq1 |  |  | freq1 |  |
| Duplex mode |  |  | Config 1 |  |  |  |  |  |  | FDD |  |  | FDD |  |
|  |  |  | Config 2,3 |  |  |  |  |  |  | TDD |  |  | TDD |  |
| TDD configuration |  |  | Config 1 |  |  |  |  |  |  | Not Applicable |  |  | Not Applicable |  |
|  |  |  | Config 2 |  |  |  |  |  |  | TDDConf.1.1 |  |  | TDDConf.1.1 |  |
|  |  |  | Config 3 |  |  |  |  |  |  | TDDConf.2.1 |  |  | TDDConf.2.1 |  |
| Downlink initial BWP configuration |  |  |  |  |  |  |  |  |  | DLBWP.0.1 |  |  | DLBWP.0.1 |  |
| Downlink dedicated BWP configuration |  |  |  |  |  |  |  |  |  | DLBWP.1.1 |  |  | DLBWP.1.1 |  |
| Uplink initial BWP configuration |  |  |  |  |  |  |  |  |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |
| Uplink dedicated BWP configuration |  |  |  |  |  |  |  |  |  | ULBWP.1.1 |  |  | ULBWP.1.1 |  |
| DRX Cycle configuration |  |  |  |  |  |  | ms |  |  | Not Applicable |  |  | Not Applicable |  |
| TRS configuration |  |  | Config 1 |  |  |  |  |  |  | TRS.1.1 FDD |  |  | TRS.1.1 FDD |  |
|  |  |  | Config 2 |  |  |  |  |  |  | TRS.1.1 TDD |  |  | TRS.1.1 TDD |  |
|  |  |  | Config 3 |  |  |  |  |  |  | TRS.1.2 TDD |  |  | TRS.1.2 TDD |  |
| PDSCH Reference measurement channel |  |  | Config 1 |  |  |  |  |  |  | SR.1.1 FDD |  |  | SR.1.1 FDD |  |
|  |  |  | Config 2 |  |  |  |  |  |  | SR.1.1 TDD |  |  | SR.1.1 TDD |  |
|  |  |  | Config 3 |  |  |  |  |  |  | SR.2.1 TDD |  |  | SR.2.1 TDD |  |
| RMSI CORESET Reference Channel |  |  | Config 1 |  |  |  |  |  |  | CR.1.1 FDD |  |  | CR.1.1 FDD |  |
|  |  |  | Config 2 |  |  |  |  |  |  | CR.1.1 TDD |  |  | CR.1.1 TDD |  |
|  |  |  | Config 3 |  |  |  |  |  |  | CR.2.1 TDD |  |  | CR.2.1 TDD |  |
| Dedicated CORESET Reference Channel |  |  | Config 1 |  |  |  |  |  |  | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |
|  |  |  | Config 2 |  |  |  |  |  |  | CCR.1.1 TDD |  |  | CCR.1.1 TDD |  |
|  |  |  | Config 3 |  |  |  |  |  |  | CCR.2.1 TDD |  |  | CCR.2.1 TDD |  |
| OCNG Patterns |  |  |  |  |  |  |  |  |  | OP.1 |  |  | OP.1 |  |
| SS-RSSI-Measurement |  |  |  |  |  |  |  |  |  | Not Applicable |  |  | Not Applicable |  |
| SMTC configuration |  |  | Config 1Config 2,3 |  |  |  |  |  |  | SMTC.2 |  |  | SMTC.2 |  |
|  |  |  |  |  |  |  |  |  |  | SMTC.1 |  |  | SMTC.1 |  |
| SSB configuration |  |  | Config 1,2 |  |  |  |  |  |  | SSB.1 FR1 |  |  | SSB.1 FR1 |  |
|  |  |  | Config 3 |  |  |  |  |  |  | SSB.2 FR1 |  |  | SSB.2 FR1 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | Config 1,2 |  |  |  | kHz |  |  | 15 |  |  | 15 |  |
|  |  |  | Config 3 |  |  |  |  |  |  | 30 |  |  | 30 |  |
| EPRE ratio of PSS to SSS |  |  |  |  |  |  | dB |  |  | 0 |  |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | NR_FDD_FR1_A |  |  |  | dBm/15 kHz |  |  | -93 |  |  | -116 |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  |  |  |  | -115.5 |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  |  |  |  | -115 |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  |  |  |  | -114.5 |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  |  |  |  | -114 |  |
| NR_FDD_FR1_G |  |  |  |  |  |  |  |  | -113 |  |  |  |  |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  |  |  |  | -112.5 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 |  |  |  |  |  | dBm/SCS |  |  | -93 |  |  | Same as Noc for 15 kHz |  |
|  | Config 3 |  | NR_FDD_FR1_A |  |  |  |  |  |  | -90 |  |  | -113 |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  |  |  |  | -112.5 |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  |  |  |  | -112 |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  |  |  |  | -111.5 |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  |  |  |  | -111 |  |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  |  |  |  |  | -110 |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  |  |  |  | -109.5 |  |
| ![](media_svg/image7.svg) [公式≈: ^{Ê}s^{I}ot] |  |  |  |  |  |  | dB |  |  | 0 |  |  | -5.46 |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  |  |  |  |  | dB |  |  | 4.54 |  |  | -4 |  |
| SS-RSRPNote3 | Config 1,2 |  | NR_FDD_FR1_A |  |  |  | dBm/SCS |  |  | -88.46 |  |  | -120 |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  |  |  |  | -119.5 |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  |  |  |  | -119 |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  |  |  |  | -118.5 |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  |  |  |  | -118 |  |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  |  |  |  |  | -117 |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  |  |  |  | -116.5 |  |
| Config 3 |  | NR_FDD_FR1_A |  |  |  |  |  | -85.46 |  |  | -117 |  |  |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  |  |  |  | -116.5 |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  |  |  |  | -116 |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  |  |  |  | -115.5 |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  |  |  |  | -115 |  |
|  |  | NR_FDD_FR1_G |  |  |  |  |  |  |  |  | -114 |  |  |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  |  |  |  | -113.5 |  |
| SS-SINR Note3 |  |  | NR_FDD_FR1_A |  |  |  | dB |  |  | 0 |  |  | -5.46 |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  |  |  |  |  |  |
| IoNote3 | Config 1,2 |  | NR_FDD_FR1_A |  |  |  | dBm/9.36 MHz |  |  | -57.5 |  |  | -85.51 |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  |  |  |  | -85.01 |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  |  |  |  | -84.51 |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  |  |  |  | -84.01 |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  |  |  |  | -83.51 |  |
|  |  |  | NR_FDD_FR1_G |  |  |  |  |  |  |  |  |  | -82.51 |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  |  |  |  | -82.01 |  |
| Config 3 |  | NR_FDD_FR1_A |  |  | dBm/38.16 MHz |  |  | -51.41 |  |  | -79.41 |  |  |  |
|  |  |  | NR_FDD_FR1_B |  |  |  |  |  |  |  |  |  | -78.91 |  |
|  |  |  | NR_TDD_FR1_C |  |  |  |  |  |  |  |  |  | -78.41 |  |
|  |  |  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  |  |  |  | -77.91 |  |
|  |  |  | NR_FDD_FR1_E |  |  |  |  |  |  |  |  |  | -77.41 |  |
|  |  | NR_FDD_FR1_G |  |  |  |  |  |  |  |  | -76.41 |  |  |  |
|  |  |  | NR_FDD_FR1_H |  |  |  |  |  |  |  |  |  | -75.91 |  |
| Propagation condition |  |  |  |  |  |  | - |  |  | AWGN |  |  | AWGN |  |
| Antenna configuration |  |  |  |  |  |  | - |  |  | 1x2 |  |  | 1x2 |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

##### A.13.4.3.1.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.31.1.1.

### A.13.4.4 L1-RSRP measurement for beam reporting with CCA serving cell

#### A.13.4.4.1 SSB based L1-RSRP measurement

##### A.13.4.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.33.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.13.4.4.1.1-1.

Table A.13.4.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Config | Description |
| --- | --- |
| 1 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations |  |

##### A.13.4.4.1.2 Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a SCell under CCA (Cell 2). Cell 2 operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model.

Two sub-tests (Test 1 and Test 2) are provided with different Noc  on Cell 2. The test parameters for the Cell 1 and Cell 2 are given in table A.13.4.4.1.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.13.4.4.1.2-1.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. On Cell 2, UE is configured to perform L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.13.4.4.1.2-1: FR1 SSB based L1-RSRP test parameters

| Parameter |  | Config | Unit | Test 1 |  |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 |  | Cell 1 | Cell 2 |
| Active PCell/SCell Configuration |  | 1~3 |  | PCell | SCell |  | PCell | SCell |
| SSB ARFCN |  | 1~3 |  | freq1 | freq2 |  | freq1 | freq2 |
| DL CCA model |  | 1~3 |  | N/A | As specifieed in A.3.26.2.1 |  | N/A | As specifieed in A.3.26.2.1 |
| UL CCA model |  | 1~3 |  | N/A | As specified in A.3.26.2.2 |  | N/A | As specified in A.3.26.2.2 |
| Duplex mode |  | 1 |  | FDD | TDD |  | FDD | TDD |
|  |  | 2,3 |  | TDD |  |  | TDD |  |
| TDD configuration |  | 1 |  | N/A | TDDConf.1.1 CCA |  | N/A | TDDConf.1.1 CCA |
|  |  | 2 |  | TDDConf.1.1 |  |  | TDDConf.1.1 |  |
|  |  | 3 |  | TDDConf.2.1 |  |  | TDDConf.2.1 |  |
| BWchannel |  | 1 | MHz | 10: NPRB,c = 52 | 40: NPRB,c = 106 |  | 10: NPRB,c = 52 | 40: NPRB,c = 106 |
|  |  | 2 |  | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |  |
|  |  | 3 |  | 40: NPRB,c = 106 |  |  | 40: NPRB,c = 106 |  |
| PDSCH Reference measurement channel |  | 1 |  | SR.1.1 FDD | SR.1.1 CCA |  | SR.1.1 FDD | SR.1.1 CCA |
|  |  | 2 |  | SR.1.1 TDD |  |  | SR.1.1 TDD |  |
|  |  | 3 |  | SR.2.1 TDD |  |  | SR.2.1 TDD |  |
| RMSI CORESET Reference Channel |  | 1 |  | CR.1.1 FDD | CR.1.1 CCA |  | CR.1.1 FDD | CR.1.1 CCA |
|  |  | 2 |  | CR.1.1 TDD |  |  | CR.1.1 TDD |  |
|  |  | 3 |  | CR.2.1 TDD |  |  | CR.2.1 TDD |  |
| Dedicated CORESET Reference Channel |  | 1 |  | CCR.1.1 FDD | CCR.1.1 CCA |  | CCR.1.1 FDD | CCR.1.1 CCA |
|  |  | 2 |  | CCR.1.1 TDD |  |  | CCR.1.1 TDD |  |
|  |  | 3 |  | CCR.2.1 TDD |  |  | CCR.2.1 TDD |  |
| SSB configuration for Semi-static channel access |  | 1 |  | SSB.3 FR1 | SSB.3 CCA |  | SSB.3 FR1 | SSB.3 CCA |
|  |  | 2 |  | SSB.3 FR1 |  |  | SSB.3 FR1 |  |
|  |  | 3 |  | SSB.4 FR1 |  |  | SSB.4 FR1 |  |
| SSB configuration for Dynamic channel access |  | 1 |  | SSB.3 FR1 | SSB.4 CCA |  | SSB.3 FR1 | SSB.4 CCA |
|  |  | 2 |  | SSB.3 FR1 |  |  | SSB.3 FR1 |  |
|  |  | 3 |  | SSB.4 FR1 |  |  | SSB.4 FR1 |  |
| TRS configuration |  | 1 |  | TRS.1.1 FDD | TRS.1.2 TDD |  | TRS.1.1 FDD | TRS.1.2 TDD |
|  |  | 2 |  | TRS.1.1 TDD |  |  | TRS.1.1 TDD |  |
|  |  | 3 |  | TRS.1.2 TDD |  |  | TRS.1.2 TDD |  |
| OCNG Patterns |  | 1~3 |  | OP.1 |  |  | OP.1 |  |
| Initial BWP Configuration |  | 1~3 |  | DLBWP.0.1ULBWP.0.1 |  |  | DLBWP.0.1ULBWP.0.1 |  |
| Dedicated BWP configuration |  | 1~3 |  | DLBWP.1.1ULBWP.1.1 |  |  | DLBWP.1.1ULBWP.1.1 |  |
| SMTC configuration |  | 1~3 |  | SMTC.1 |  | N/A | SMTC.1 | N/A |
| DBT Window Configuration |  | 1~3 |  | N/A |  | DBT.1 | N/A | DBT.1 |
| reportConfigType |  | 1~3 |  | periodic |  |  | periodic |  |
| reportQuantity |  | 1~3 |  | ssb-Index-RSRP |  |  | ssb-Index-RSRP |  |
| Number of reported RS |  | 1~3 |  | 2 |  |  | 2 |  |
| L1-RSRP reporting period |  | 1~3 |  | slot80 |  |  | slot80 |  |
| EPRE ratio of PSS to SSS |  | 1~3 | dB | 0 |  |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |  |  |  |
| Note2 | NR_FDD_FR1_A | 1~3 | dBm/15 kHz | -94.65 |  |  | -94.65 | - |
|  | NR_FDD_FR1_B |  |  |  |  |  |  | - |
|  | NR_TDD_FR1_C |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_E |  |  |  |  |  |  | - |
|  |  |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_G |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_H |  |  |  |  |  |  | - |
|  |  |  |  |  |  |  |  | - |
|  |  |  |  |  |  |  | - | -113 |
| Note2 | NR_FDD_FR1_A | 1~3 | dBm/SSB SCS | -91.65 |  |  | -91.65 | - |
|  | NR_FDD_FR1_B |  |  |  |  |  |  | - |
|  | NR_TDD_FR1_C |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_E |  |  |  |  |  |  | - |
|  |  |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_G |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_H |  |  |  |  |  |  | - |
|  |  |  |  |  |  |  |  | - |
|  |  |  |  |  |  |  | - | -110 |
|  |  | 1~3 | dB | 10 |  |  | 10 | -3 |
| SS-RSRPNote3 | NR_FDD_FR1_A | 1~3 | dBm/SCS | -81.65 |  |  | -81.65 | - |
|  | NR_FDD_FR1_B |  |  |  |  |  |  | - |
|  | NR_TDD_FR1_C |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_E |  |  |  |  |  |  | - |
|  |  |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_G |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_H |  |  |  |  |  |  | - |
|  |  |  |  |  |  |  |  | - |
|  |  |  |  |  |  |  | - | -113 |
| IoNote3 | NR_FDD_FR1_A | 1~3 | dBm/38.16 MHz | -50.19 |  |  | -50.19 | - |
|  | NR_FDD_FR1_B |  |  |  |  |  |  | - |
|  | NR_TDD_FR1_C |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_D, NR_TDD_FR1_D |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_E |  |  |  |  |  |  | - |
|  |  |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_G |  |  |  |  |  |  | - |
|  | NR_FDD_FR1_H |  |  |  |  |  |  | - |
|  |  |  |  |  |  |  |  | - |
|  |  |  |  |  |  |  | - | -77.19 |
|  |  | 1~3 | dB | 10 |  |  | 10 | -3 |
| Propagation condition |  | 1~3 |  | AWGN |  |  | AWGN |  |
| Antenna configuration |  | 1~3 |  | 1x2 |  |  | 1x2 |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. For cells with CCA model, OCNG is transmitted only in the slots with downlink transmission burst and is not transmitted during the muted slots or during DBT window.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |  |  |  |  |

##### A.13.4.4.1.3 Test Requirements

In both Test 1 and Test 2, the L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 2 shall fulfil the requirements in clauses 10.1.33.1.

### A.13.4.5 RSSI

#### A.13.4.5.1  Intra-frequency RSSI measurement accuracy on a carrier with CCA

##### A.13.4.5.1.1 Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.1.

##### A.13.4.5.1.2 Test parameters

In all test cases, Cell 1 is the PCell on a licensed FR1 band and Cell 2 is the SCell with CCA. RSSI is measured on channel number 2. Supported test configurations are shown in table A.13.4.5.1.2-1. The accuracy of RSSI intra-frequency measurements is tested by using the parameters in A.13.4.5.1.2-2 and A.13.4.5.1.2-3.

Table A.13.4.5.1.2-1: Intra frequency RSSI supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.13.4.5.1.2-2: RSSI Intra frequency test parameters

| Parameter |  | Configurations | Unit | Test 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 |
| RF Channel Number |  |  |  | 1 | 2 |
| BWchannel |  |  | MHz | 40 | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1,2,3 |  | Configuration 1,2: SSB.1 FR1Configuration 3: SSB.2 FR1 | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1,2,3 |  | Configuration 1,2: SSB.1 FR1Configuration 3: SSB.2 FR1 | SSB.2 CCA |
| PCCA_DL for dynamic channel access Note 1,3 |  | 1,2,3 |  | 1 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |
| PCCA_DL for semi-static channel access Note 2,3 |  | 1,2,3 |  | 1 | PCCA_DL=0.9375 |
| PCCA_UL |  |  |  | 1 | 1 |
| DL CCA model |  |  |  | N/A | As specifieed in A.3.26.2.1 |
| UL CCA model |  |  |  | N/A | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image8.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |  |
| Channel access bandwidth |  |  | MHz | 20 |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  | 1 |  | SR.1.1 FDD | SR.1.1 CCA |
|  |  | 2,3 |  | SR.1.1 TDD |  |
| RMSI CORESET Reference Channel |  | 1 |  | CR.1.1 FDD | CR.1.1 CCA |
|  |  | 2,3 |  | CR.1.1 TDD |  |
| Dedicated CORESET Reference Channel |  | 1 |  | CCR.1.1 FDD | CCR.1.1 CCA |
|  |  | 2,3 |  | CCR.1.1 TDD |  |
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
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -106 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -87 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | 2.5 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -103.5 | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -58.96 |
| Propagation condition |  |  | - | AWGN |  |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.13.4.5.1.2-3: RSSI RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.13.4.5.1.3 Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.1. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

#### A.13.4.5.2 Inter-frequency RSSI measurement accuracy on a carrier with CCA

##### A.13.4.5.2.1 Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.2.

##### A.13.4.5.2.2 Test parameters

In all test cases, Cell 1 is the PCell on a licensed FR1 band and Cell 2 is the neighbour with CCA. RSSI is measured on channel number 2. Supported test configurations are shown in table A.13.4.5.2.2-1. The accuracy of RSSI inter-frequency measurements is tested by using the parameters in A.13.4.5.2.2-2 and A.13.4.5.2.3.

Table A.13.4.5.2.2-1: Inter frequency RSSI supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.13.4.5.2.2-2: RSSI Inter frequency test parameters

| Parameter |  | Configurations | Unit | Test 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 |
| RF Channel Number |  |  |  | 1 | 2 |
| BWchannel |  |  | MHz | 40 | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1,2,3 |  | Configuration 1,2: SSB.1 FR1Configuration 3: SSB.2 FR1 | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1,2,3 |  | Configuration 1,2: SSB.1 FR1Configuration 3: SSB.2 FR1 | SSB.2 CCA |
| PCCA_DL for dynamic channel access Note 1,3 |  | 1,2,3 |  | 1 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |
| PCCA_DL for semi-static channel access Note 2,3 |  | 1,2,3 |  | 1 | PCCA_DL=0.9375 |
| PCCA_UL |  |  |  | 1 | 1 |
| DL CCA model |  |  |  | N/A | As specifieed in A.3.26.2.1 |
| UL CCA model |  |  |  | N/A | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image8.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |  |
| Channel access bandwidth |  |  | MHz | 20 |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  | 1 |  | SR.1.1 FDD | NA |
|  |  | 2,3 |  | SR.1.1 TDD |  |
| RMSI CORESET Reference Channel |  | 1 |  | CR.1.1 FDD | NA |
|  |  | 2,3 |  | CR.1.1 TDD |  |
| Dedicated CORESET Reference Channel |  | 1 |  | CCR.1.1 FDD | NA |
|  |  | 2,3 |  | CCR.1.1 TDD |  |
| OCNG Patterns |  |  |  | OP.1 | NA |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | NA |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -106 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -87 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | 2.5 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -103.5 | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -58.96 |
| Propagation condition |  |  | - | AWGN |  |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.13.4.5.2.2-3: RSSI RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.13.4.5.2.3 Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.2. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

### A.13.4.6 Channel occupancy

#### A.13.4.6.1 Intra-frequency channel occupancy measurement accuracy on SCC with CCA

##### A.13.4.6.1.1 Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.1.

##### A.13.4.6.1.2 Test parameters

In all test cases, Cell 1 is the PCell on a licensed FR1 band and Cell 2 is the SCell with CCA. Channel occupancy is measured on channel number 2. Supported test configurations are shown in table A.13.4.6.1.2-1. The accuracy of channel occupancy intra-frequency measurements is tested by using the parameters in A.13.4.6.1.2-2 and A.13.4.6.1.2-3.

Table A.13.4.6.1.2-1: Intra frequency CO supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.13.4.6.1.2-2: CO Intra frequency test parameters

| Parameter |  | Configurations | Unit | Test 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 |
| RF Channel Number |  |  |  | 1 | 2 |
| BWchannel |  |  | MHz | 40 | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1,2,3 |  | Configuration 1,2: SSB.1 FR1Configuration 3: SSB.2 FR1 | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1,2,3 |  | Configuration 1,2: SSB.1 FR1Configuration 3: SSB.2 FR1 | SSB.2 CCA |
| PCCA_DL for dynamic channel access Note 1,3 |  | 1,2,3 |  | 1 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |
| PCCA_DL for semi-static channel access Note 2,3 |  | 1,2,3 |  | 1 | PCCA_DL=0.9375 |
| PCCA_UL |  |  |  | 1 | 1 |
| DL CCA model |  |  |  | N/A | As specifieed in A.3.26.2.1 |
| UL CCA model |  |  |  | N/A | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image8.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |  |
| Channel access bandwidth |  |  | MHz | 20 |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  | 1 |  | SR.1.1 FDD | SR.1.1 CCA |
|  |  | 2,3 |  | SR.1.1 TDD |  |
| RMSI CORESET Reference Channel |  | 1 |  | CR.1.1 FDD | CR.1.1 CCA |
|  |  | 2,3 |  | CR.1.1 TDD |  |
| Dedicated CORESET Reference Channel |  | 1 |  | CCR.1.1 FDD | CCR.1.1 CCA |
|  |  | 2,3 |  | CCR.1.1 TDD |  |
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
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -106 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -87 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | 2.5 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -103.5 | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -58.96 |
| Propagation condition |  |  | - | AWGN |  |
| channelOccupancyThreshold |  |  | dBm | -83 |  |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.13.4.6.1.2-3: CO RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.13.4.6.1.3 Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.

#### A.13.4.6.2 Inter-frequency channel occupancy measurement accuracy on a carrier with CCA

##### A.13.4.6.2.1 Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.2.

##### A.13.4.6.2.2 Test parameters

In all test cases, Cell 1 is the PCell on a licensed FR1 band and Cell 2 is the neighbour with CCA. Channel occupancy is measured on channel number 2. Supported test configurations are shown in table A.13.4.6.2.2-1. The accuracy of channel occupancy inter-frequency measurements is tested by using the parameters in A.13.4.6.2.2-2 and A.13.4.6.2.3.

Table A.13.4.6.2.2-1: Inter frequency CO supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 2 | Without CCA: 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 3 | Without CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex modeWith CCA: 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: The UE is only required to be tested in one of the supported test configurations. |  |

Table A.13.4.6.2.2-2: CO Inter frequency test parameters

| Parameter |  | Configurations | Unit | Test 1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 |
| RF Channel Number |  |  |  | 1 | 2 |
| BWchannel |  |  | MHz | 40 | 40 |
| SSB configuration | Semi-static channel access Note 1, 3 | 1,2,3 |  | Configuration 1,2: SSB.1 FR1Configuration 3: SSB.2 FR1 | SSB.1 CCA |
|  | Dynamic channel access Note 2, 3 | 1,2,3 |  | Configuration 1,2: SSB.1 FR1Configuration 3: SSB.2 FR1 | SSB.2 CCA |
| PCCA_DL for dynamic channel access Note 1,3 |  | 1,2,3 |  | 1 | PCCA_DL_1=0.75PCCA_DL_2=0.75 |
| PCCA_DL for semi-static channel access Note 2,3 |  | 1,2,3 |  | 1 | PCCA_DL=0.9375 |
| PCCA_UL |  |  |  | 1 | 1 |
| DL CCA model |  |  |  | N/A | As specified in A.3.26.2.1 |
| UL CCA model |  |  |  | N/A | As specified in A.3.26.2.2 |
| Measurement bandwidth |  |  | ![](media_svg/image8.svg) [公式≈: ^{n}PRB] | Same as channel access bandwidth |  |
| Channel access bandwidth |  |  | MHz | 20 |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  | 1 |  | SR.1.1 FDD | NA |
|  |  | 2,3 |  | SR.1.1 TDD |  |
| RMSI CORESET Reference Channel |  | 1 |  | CR.1.1 FDD | NA |
|  |  | 2,3 |  | CR.1.1 TDD |  |
| Dedicated CORESET Reference Channel |  | 1 |  | CCR.1.1 FDD | NA |
|  |  | 2,3 |  | CCR.1.1 TDD |  |
| OCNG Patterns |  |  |  | OP.1 | NA |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | NA |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -106 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -106 | -87 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | 2.5 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dB | 2.5 | -Infinity |
| SS-RSRP in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/SCS | -103.5 | -103.5 |
| SS-RSRP in slots corresponding to RSSI measurement time configuration (RMTC) |  |  |  | -103.5 | -Infinity |
| Io within measurement bandwidth in slots not corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -77.96 |
| Io within measurement bandwidth in slots corresponding to RSSI measurement time configuration (RMTC) |  |  | dBm/measBW | -77.96 | -58.96 |
| Propagation condition |  |  | - | AWGN |  |
| channelOccupancyThreshold |  |  | dBm | -83 |  |
| NOTE 1: For UE supporting semi-static channel access and network configuring semi-static channel occupancy.NOTE 2: For UE supporting dynamic channel access and network configuring dynamic channel occupancy.NOTE 3: For a UE supporting both semi-static and dynamic channel access, the UE can be tested under dynamic channel occupancy only. |  |  |  |  |  |

Table A.13.4.6.2.2-3: CO RMTC parameters

| measDurationSymbols-r16 | sym14or12 |
| --- | --- |
| rmtc-Periodicity-r16 | ms40 |
| rmtc-SubframeOffset-r16 | 20 |
| ref-SCS-CP-r16 | kHz15 |
| ReportInterval | ms120 |

##### A.13.4.6.2.3 Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.

# A.14 NR standalone tests for Satellite access

## A.14.1 RRC_IDLE state mobility

### A.14.1.1 Cell reselection to FR1 intra-frequency NR case

#### A.14.1.1.1 Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.3, including the SSB periodicity of the target cell is 160ms.

#### A.14.1.1.2 Test Parameters

The test scenario comprises of 2 cells on 1 NR carrier configured each in a different satellite as given in tables A.14.1.1.2-1, A.14.1.1.2-2 and A.14.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.14.1.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 3 | NGSO with varying Doppler and delay shift NTN channel model, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.1.1.2-2: General test parameters for intra frequency NR cell re-selection test case

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Initial condition | Active cell |  | Cell 1 |  |
| T2 end condition | Active cell |  | Cell 2 |  |
|  | Neighbour cells |  | Cell 1 |  |
| Final condition | Active cell |  | Cell 1 |  |
|  | Neighbour cells |  | Cell 2 |  |
| RF Channel Number |  |  | 1 |  |
| Time offset between cells |  |  | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| DRX cycle length |  | s | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | Not configured |  |
| T1 |  | s | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2 |
| T2 |  | s | 40(NOTE 1) | T2 needs to be defined so that cell re-selection reaction time is taken into account. |
| T3 |  | s | 15(NOTE 1, 3) | T3 needs to be defined so that cell re-selection reaction time is taken into account. |
| UE position |  |  | NOTE 2 |  |
| NOTE 1: If the test is performed in a NGSO configuration, and the scaling factor Kmulti_SMTC defined in clause 4.2C.2.3 is greater than 1, according to UE capabilities, the duration of times T2 and T3 shall be scaled for the same factor to allow the UE to complete the cell reselection within the duration of the test case.NOTE 2: For Config 3, the UE position is set by AT command according to G.4.2 of TS 38.101-5 [43] at the beginning if the test, and remains unchanged during the test.NOTE 3: For Config 3, UE can reselect from cell 1 to cell 2 during T2 only.The testing procedure in T3 can be skipped. |  |  |  |  |

Table A.14.1.1.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case

| Parameter | Unit | Cell 1 |  |  | Cell 2 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 | T1 | T2 |  | T3 |
| Satellite information |  | SSC.1 for Config 1SSC.2 for Config 2,3 |  |  | NSC.1 for Config 1NSC.2 for Config 2,3 |  |  |  |
| PDSCH RMC configuration |  | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |  |
| RMSI CORESET configuration |  | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |  |
| Dedicated CORESET configuration |  | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |  |
| OCNG Pattern |  | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |  |
| Initial DL BWP configuration |  | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |  |
| Initial UL BWP configuration |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |  |
| SSB configuration |  | SSB.1 FR1 |  |  | SSB.5 FR1 |  | SSB.14 FR1 |  |
| SMTC configuration |  | #1: SMTC.2 for Cell 1#2: SMTC.5 for Cell 2 |  |  | #1: SMTC.6 for Cell 1#2: SMTC.5 for Cell 2 |  |  |  |
| RLM-RS |  | SSB |  |  | SSB |  |  |  |
| Qrxlevmin | dBm/SCS | -130 |  |  | -130 |  |  |  |
| Pcompensation | dB | 0 |  |  | 0 |  |  |  |
| Qhysts | dB | 0 |  |  | 0 |  |  |  |
| Qoffsets, n | dB | 0 |  |  | 0 |  |  |  |
| Cell_selection_and_reselection_quality_measurement |  | SS-RSRP |  |  | SS-RSRP |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 16 | -3.11 | 2.79 | -infinity | 2.79 |  | -3.11 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | -98 |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | -98 |  |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 16 | 13 | 16 | -infinity | 16 |  | 13 |
| SS-RSRP Note3 | dBm/SCS | -82 | -85 | -82 | -infinity | -82 |  | -85 |
| Io | dBm/9.36 MHz | -53.94 | -52.21 | -52.21 | Same as parameters specified in Cell 1 columns- |  |  |  |
| Treselection | s | 0 | 0 | 0 | 0 | 0 |  | 0 |
| SintrasearchP | dB | 60 |  |  | 60 |  |  |  |
| Propagation Condition |  | AWGN for Config 1,2, AWGN with time varying Doppler and delay shifts for Config 3 |  |  |  |  |  |  |
| NOTE 1: For Config 3, the initial ephemerisInfo of SSC.2 and NSC.2 refers to Table G.4.1-1 of TS 38.101-5 [43], while SSC.2 is propagated with a different epoch time, corresponding to approximately 90 degrees. |  |  |  |  |  |  |  |  |

#### A.14.1.1.3 Test Requirements

For test configuration 1, 2 and 3, the cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than:

## 34 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.1.2-2); or

## 66 s if Kmulti_SMTC is equal to 2.

For test configuration 1 and 2, the cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to an already detected cell shall be less than:

## 8 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.1.2-2); or

## 14.5 s if Kmulti_SMTC is equal to 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a newly detectable cell can be expressed as: Kmulti_SMTC *Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Kmulti_SMTC *Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_Intra See Table 4.2C.2.3-1 in clause 4.2C.2.3

Tevaluate, NR_ intra See Table 4.2C.2.3-1 in clause 4.2C.2.3

Kmulti_SMTC  is described in clause 4.2C.2.3

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB19 are scheduled with 20 ms period and 80 ms period, respectively.

If Kmulti_SMTC = 1, Kmulti_SMTC *Tevaluate, NR_Intra + TSI-NR = 7.68 s; allow 8 s. And Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 33.28 s, allow 34 s.

If K_multi_SMTC = 2,  Kmulti_SMTC *Tevaluate, NR_Intra + TSI-NR = 14.08 s; allow 14.5 s. And Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 65.28 s, allow 66 s.

### A.14.1.2 Cell reselection to FR1 intra-frequency NR cell for UE configured with the feature for enhanced requirements

#### A.14.1.2.1 Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.3.

#### A.14.1.2.2 Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.14.1.2.2-1, A.14.1.2.2-2 and A.14.1.2.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. The flag enhancedMeasurementNGSO-r17 should be set.

Table A.14.1.2.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |

Table A.14.1.2.2-2: General test parameters for intra frequency NR cell re-selection test case

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Initial condition | Active cell |  | Cell 1 |  |
| T2 end condition | Active cell |  | Cell 2 |  |
|  | Neighbour cells |  | Cell 1 |  |
| Final condition | Active cell |  | Cell 1 |  |
|  | Neighbour cells |  | Cell 2 |  |
| RF Channel Number |  |  | 1 |  |
| Time offset between cells |  |  | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| DRX cycle length |  | s | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | Not configured |  |
| T1 |  | s | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2 |
| T2 |  | s | 40(NOTE 1) | T2 needs to be defined so that cell re-selection reaction time is taken into account. |
| T3 |  | s | 15(NOTE 1) | T3 needs to be defined so that cell re-selection reaction time is taken into account. |
| NOTE 1: If the test is performed in a NGSO configuration, and the scaling factor Kmulti_SMTC defined in clause 4.2C.2.3 is greater than 1, according to UE capabilities, the duration of times T2 and T3 shall be scaled for the same factor to allow the UE to complete the cell reselection within the duration of the test case. |  |  |  |  |

Table A.14.1.2.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case

| Parameter | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | SSC.2 for Config 1 |  |  | NSC.2 for Config 1 |  |  |
| PDSCH RMC configuration |  | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |
| RMSI CORESET configuration |  | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |
| Dedicated CORESET configuration |  | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |
| OCNG Pattern |  | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| SSB configuration |  | SSB.1 FR1 |  |  | SSB.5 FR1 |  |  |
| SMTC configuration |  | #1: SMTC.2 for Cell 1#2: SMTC.5 for Cell 2 |  |  | #1: SMTC.6 for Cell 1#2: SMTC.5 for Cell 2 |  |  |
| RLM-RS |  | SSB |  |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | -130 |  |  | -130 |  |  |
| Pcompensation | dB | 0 |  |  | 0 |  |  |
| Qhysts | dB | 0 |  |  | 0 |  |  |
| Qoffsets, n | dB | 0 |  |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | SS-RSRP |  |  | SS-RSRP |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 16 | -3.11 | 2.79 | -infinity | 2.79 | -3.11 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | -98 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 16 | 13 | 16 | -infinity | 16 | 13 |
| SS-RSRP Note3 | dBm/SCS | -82 | -85 | -82 | -infinity | -82 | -85 |
| Io | dBm/9.36 MHz | -53.94 | -52.21 | -52.21 | Same as parameters specified in Cell 1 columns- |  |  |
| Treselection | s | 0 | 0 | 0 | 0 | 0 | 0 |
| SintrasearchP | dB | 60 |  |  | 60 |  |  |
| Propagation Condition |  | AWGN |  |  |  |  |  |

#### A.14.1.2.3 Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than:

## 11 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.2.2-2); or

## 20 s if Kmulti_SMTC is equal to 2.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to an already detected cell shall be less than:

## 6 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.2.2-2); or

## 9 s if Kmulti_SMTC is equal to 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a newly detectable cell can be expressed as: Kmulti_SMTC *Tdetect, NR_Intra_enh + TSI-NR, and to an already detected cell can be expressed as: Kmulti_SMTC *Tevaluate, NR_ intra_enh + TSI-NR,

Where:

Tdetect, NR_Intra_enh See Table 4.2C.2.3-2 in clause 4.2C.2.3

Tevaluate, NR_ Intra_enh See Table 4.2C.2.3-2 in clause 4.2C.2.3

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB19 are scheduled with 20 ms period and 80 ms period, respectively.

If Kmulti_SMTC = 1, Kmulti_SMTC *Tevaluate, NR_Intra_enh + TSI-NR = 5.12 s; allow 6 s. And Kmulti_SMTC *Tdetect, NR_ Intra_enh + TSI-NR = 10.24 s, allow 11 s.

If K_multi_SMTC = 2,  Kmulti_SMTC *Tevaluate, NR_Intra_enh + TSI-NR = 8.96 s; allow 9 s. And Kmulti_SMTC *Tdetect, NR_Intra_enh + TSI-NR = 19.2 s, allow 20 s.

### A.14.1.3 Time-based measurement initiation to FR1 intra-frequency NR cell reselection

#### A.14.1.3.1 Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.3.

#### A.14.1.3.2 Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.14.1.3.2-1, A.14.1.3.2-2 and A.14.1.3.2-3. The test consists of two successive time periods, with time duration of T1 and T2, respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. t-Service broadcasted in SIB19 of Cell 1 is set to the time point that is 36 s after start of T2.

Table A.14.1.3.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.1.3.2-2: General test parameters for intra frequency NR cell re-selection test case

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Initial condition | Active cell |  | Cell 1 |  |
| T2 end condition | Active cell |  | Cell 2 |  |
|  | Neighbour cells |  | Cell 1 |  |
| RF Channel Number |  |  | 1 |  |
| Time offset between cells |  |  | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| DRX cycle length |  | s | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | Not configured |  |
| T1 |  | s | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2 |
| T2 |  | s | 40(NOTE 1) | T2 needs to be defined so that cell re-selection reaction time is taken into account. |
| NOTE 1: If the test is performed in a NGSO configuration, and the scaling factor Kmulti_SMTC defined in clause 4.2C.2.3 is greater than 1, according to UE capabilities, the duration of time T2 shall be scaled for the same factor to allow the UE to complete the cell reselection within the duration of the test case. |  |  |  |  |

Table A.14.1.3.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case

| Parameter | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | SSC.1 for Config 1SSC.2 for Config 2 |  | NSC.1 for Config 1cNSC.2 for Config 2 |  |
| PDSCH RMC configuration |  | SR.1.1 FDD |  | SR.1.1 FDD |  |
| RMSI CORESET configuration |  | CR.1.1 FDD |  | CR.1.1 FDD |  |
| Dedicated CORESET configuration |  | CCR.1.1 FDD |  | CCR.1.1 FDD |  |
| OCNG Pattern |  | OP.1 defined in A.3.2.1 |  | OP.1 defined in A.3.2.1 |  |
| Initial DL BWP configuration |  | DLBWP.0.1 |  | DLBWP.0.1 |  |
| Initial UL BWP configuration |  | ULBWP.0.1 |  | ULBWP.0.1 |  |
| SSB configuration |  | SSB.1 FR1 |  | SSB.1 FR1 |  |
| SMTC configuration |  | #1: SMTC.2 |  | #1: SMTC.6 |  |
| RLM-RS |  | SSB |  | SSB |  |
| Qrxlevmin | dBm/SCS | -130 |  | -130 |  |
| Pcompensation | dB | 0 |  | 0 |  |
| Qhysts | dB | 0 |  | 0 |  |
| Qoffsets, n | dB | 0 |  | 0 |  |
| Cell_selection_and_reselection_quality_measurement |  | SS-RSRP |  | SS-RSRP |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 16 | -3.11 | -infinity | 2.79 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | -98 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | -98 |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 16 | 13 | -infinity | 16 |
| SS-RSRP Note3 | dBm/SCS | -82 | -85 | -infinity | -82 |
| Io | dBm/9.36 MHz | -53.94 | -52.21 | Same as parameters specified in Cell 1 columns- |  |
| Treselection | s | 0 | 0 | 0 | 0 |
| SintrasearchP | dB | 40 |  | 40 |  |
| Propagation Condition |  | AWGN |  |  |  |

#### A.14.1.3.3 Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than :

## 36 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.3.2-2); or

## 66 s if Kmulti_SMTC is equal to 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a newly detectable cell can be expressed as: Kmulti_SMTC *Tdetect, NR_Intra + TSI-NR,

Where:

Tdetect, NR_Intra See Table 4.2C.2.3 clause 4.2C.2.3

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB19 are scheduled with 20 ms period and 80 ms period, respectively.

If Kmulti_SMTC = 1, Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 33.28 s, allow 34 s.

If Kmulti_SMTC = 2, Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 65.28 s, allow 66 s.

### A.14.1.4 Location-based measurement initiation to FR1 intra-frequency NR cell reselection

#### A.14.1.4.1 Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.3.

#### A.14.1.4.2 Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.14.1.a4.2-1, A.14.1.a4.2-2 and A.14.1.a4.2-3. The test consists of two successive time periods, with time duration of T1 and T2, respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

At 4 s after the start of T2, the UE location is changed such that the distance to the reference location broadcasted in SIB19 of Cell 1 is exceeded by the configured value in distanceThresh plus 50m.

Table A.14.1.4.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.1.4.2-2: General test parameters for intra frequency NR cell re-selection test case

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Initial condition | Active cell |  | Cell 1 |  |
| T2 end condition | Active cell |  | Cell 2 |  |
|  | Neighbour cells |  | Cell 1 |  |
| RF Channel Number |  |  | 1 |  |
| Time offset between cells |  |  | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| DRX cycle length |  | s | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | Not configured |  |
| T1 |  | s | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2 |
| T2 |  | s | 40(NOTE 1) | T2 needs to be defined so that cell re-selection reaction time is taken into account. |
| NOTE 1: If the test is performed in a NGSO configuration, and the scaling factor Kmulti_SMTC defined in clause 4.2C.2.3 is greater than 1, according to UE capabilities, the duration of time T2 shall be scaled for the same factor to allow the UE to complete the cell reselection within the duration of the test case. |  |  |  |  |

Table A.14.1.4.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case

| Parameter | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | SSC.1 for Config 1SSC.2 for Config 2 |  | NSC.1 for Config 1NSC.2 for Config 2 |  |
| PDSCH RMC configuration |  | SR.1.1 FDD |  | SR.1.1 FDD |  |
| RMSI CORESET configuration |  | CR.1.1 FDD |  | CR.1.1 FDD |  |
| Dedicated CORESET configuration |  | CCR.1.1 FDD |  | CCR.1.1 FDD |  |
| OCNG Pattern |  | OP.1 defined in A.3.2.1 |  | OP.1 defined in A.3.2.1 |  |
| Initial DL BWP configuration |  | DLBWP.0.1 |  | DLBWP.0.1 |  |
| Initial UL BWP configuration |  | ULBWP.0.1 |  | ULBWP.0.1 |  |
| SSB configuration |  | SSB.1 FR1 |  | SSB.1 FR1 |  |
| SMTC configuration |  | #1: SMTC.2 |  | #1: SMTC.6 |  |
| RLM-RS |  | SSB |  | SSB |  |
| Qrxlevmin | dBm/SCS | -130 |  | -130 |  |
| Pcompensation | dB | 0 |  | 0 |  |
| Qhysts | dB | 0 |  | 0 |  |
| Qoffsets, n | dB | 0 |  | 0 |  |
| Cell_selection_and_reselection_quality_measurement |  | SS-RSRP |  | SS-RSRP |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 16 | -3.11 | -infinity | 2.79 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | -98 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | -98 |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 16 | 13 | -infinity | 16 |
| SS-RSRP Note3 | dBm/SCS | -82 | -85 | -infinity | -82 |
| Io | dBm/9.36 MHz | -53.94 | -52.21 | Same as parameters specified in Cell 1 columns- |  |
| Treselection | s | 0 | 0 | 0 | 0 |
| SintrasearchP | dB | 40 |  | 40 |  |
| Propagation Condition |  | AWGN |  |  |  |

#### A.14.1.4.3 Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than:

## 34 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.3.2-2); or

## 66 s if Kmulti_SMTC is equal to 2.

The UE starts searching for the cell only after 4 s after the start of T2 when the UE location is changed such that the distance to the reference location broadcasted in SIB19 of Cell 1 is exceeded by the configured value in distanceThresh plus 50m. Consideing that the cell re-selection delay to a newly detectable cell shall be less than 38 s if Kmulti_SMTC  is  equal to 1 or 70 s if Kmulti_SMTC is equal to 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a newly detectable cell can be expressed as: Kmulti_SMTC *Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Kmulti_SMTC *Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_Intra See Table 4.2C.2.3 clause 4.2C.2.3

Tevaluate, NR_ intra See Table 4.2C.2.3-1 in clause 4.2C.2.3

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB19 are scheduled with 20 ms period and 80 ms period, respectively.

If Kmulti_SMTC = 1, Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 33.28 s, allow 34 s.

If Kmulti_SMTC = 2, Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 65.28 s, allow 66 s.

### A.14.1.5 Cell reselection to FR1 inter-frequency NR case

#### A.14.1.5.1 Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.4.

#### A.14.1.5.2 Test Parameters

The test scenario comprises of 2 NR carriers and 2 cells as given in tables A.14.1.5.2-1, A.14.1.5.2-2 and A.14.1.5.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

Table A.14.1.5.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.1.5.2-2: General test parameters for inter frequency NR cell re-selection test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
| Initial condition | Active cell |  | 1, 2 | Cell 2 | The UE camps on Cell 2 in the initial phase and during T1 period the UE reselects to Cell 1 |
|  | Neighbour cell |  | 1, 2 | Cell 1 |  |
| T1 end condition | Active cell |  | 1, 2 | Cell 1 | The UE shall perform reselection to Cell 1 during T1 |
|  | Neighbour cells |  | 1, 2 | Cell 2 |  |
| T3 end condition | Active cell |  | 1, 2 | Cell 2 | The UE shall perform reselection to Cell 2 during T3 |
|  | Neighbour cells |  | 1, 2 | Cell 1 |  |
| RF Channel Number |  |  | 1, 2 | 1 |  |
| Time offset between cells |  |  | 1, 2 | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | 1, 2 | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | 1, 2 | SSB.1 FR1 |  |
| SMTC configuration#1 |  |  | 1, 2 | SMTC.2 | Configured in SIB2 of Cell 1 |
|  |  |  |  | SMTC.6 | Configured in SIB2 of Cell 2 |
| SMTC configuration#2 |  |  | 1, 2 | SMTC.2 | Configured in SIB4  of Cell 1 |
|  |  |  |  | SMTC.6 | Configured in SIB4  of Cell 2 |
| DRX cycle length |  | s | 1, 2 | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2 | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2 | Not configured |  |
| T1 |  | s | 1, 2 | 15 | T1 needs to be defined so that cell re-selection reaction time is taken into account. |
| T2 |  | s | 1, 2 | >7 | During T2, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed. The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T3. |
| T3 |  | s | 1, 2 | 75 | T3 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.14.1.5.2-3: Cell specific test parameters for inter frequency NR cell re-selection test case

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | 1 | SSC.1 |  |  | SSC.1 |  |  |
|  |  | 2 | SSC.2 |  |  | SSC.2 |  |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |
| OCNG Pattern |  | 1, 2 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1, 2 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1, 2 | SSB |  |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1, 2 | -140 |  |  | -140 |  |  |
| Pcompensation | dB | 1, 2 | 0 |  |  | 0 |  |  |
| Qhysts | dB | 1, 2 | 0 |  |  | 0 |  |  |
| Qoffsets, n | dB | 1, 2 | 0 |  |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1, 2 | SS-RSRP |  |  | SS-RSRP |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2 | 14 | 14 | 14 | -4 | -infinity | 12 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1, 2 | -98 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 2 | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2 | 14 | 14 | 14 | -4 | -infinity | 12 |
| SS-RSRP Note3 | dBm/SCS | 1, 2 | -84 | -84 | -84 | -102 | -infinity | 86 |
| Io | dBm/9.36 MHz | 1, 2 | -55.88 | -55.88 | -55.88 | -68.60 | -70.05 | -57.78 |
| Treselection | s | 1, 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| SnonIntraSearchP | dB | 1, 2 | 50 |  |  | 50 |  |  |
| Threshx, highP | dB | 1, 2 | 48 |  |  | 48 |  |  |
| Threshserving, lowP | dB | 1, 2 | 44 |  |  | 44 |  |  |
| Threshx, lowP | dB | 1, 2 | 50 |  |  | 50 |  |  |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

#### A.14.1.5.3 Test Requirements

The cell reselection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps again on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to a lower priority cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Thigher_priority_search See clause4.2C.2.9

Tevaluate, NR_ inter See tables 4.2C.2.4-1 in clause 4.2C.2.4

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority

### A.14.1.6 Cell re-selection to FR1 inter-frequency NR cell for UE configured with feature for enhanced requirements

#### A.14.1.6.1 Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell re-selection requirements for satellite access specified in clause 4.2C.2.4.

#### A.14.1.6.2 Test Parameters

The test scenario comprises of 2 NR carriers and 2 cells as given in tables A.14.1.6.2-1, A.14.1.6.2-2 and A.14.1.6.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3, respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1. The flag enhancedMeasurementNGSO-r17 should be set.

Table A.14.1.6.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |

Table A.14.1.6.2-2: General test parameters for inter frequency NR cell re-selection test case

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Initial condition | Active cell |  | Cell2 | The UE camps on Cell 2 in the initial phase and during T1 period the UE reselects to Cell 1 |
| T1 end condition | Active cell |  | Cell1 | The UE shall perform reselection to Cell 1 during T1 |
|  | Neighbour cells |  | Cell2 |  |
| T3 end condition | Active cell |  | Cell2 | The UE shall perform reselection to Cell 2 during T3 |
|  | Neighbour cells |  | Cell1 |  |
| RF Channel Number |  |  | 1 |  |
| Time offset between cells |  |  | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | SSB.1 FR1 |  |
| SMTC configuration#1 |  |  | SMTC.2 | Configured in SIB2 of Cell 1 |
|  |  |  | SMTC.6 | Configured in SIB2 of Cell 2 |
| SMTC configuration#2 |  |  | SMTC.2 | Configured in SIB4 of Cell 1 |
|  |  |  | SMTC.6 | Configured in SIB4 of Cell 2 |
| DRX cycle length |  | s | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | Not configured |  |
| T1 |  | s | 15 | T1 needs to be defined so that cell re-selection reaction time is taken into account. |
| T2 |  | s | >7 | During T2, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed. The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T3. |
| T3 |  | s | 75 | T3 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.14.1.6.2-3: Cell specific test parameters for inter frequency NR cell re-selection test case

| Parameter | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | SSC.2 for Config 1 |  |  | SSC.2 for Config 1 |  |  |
| PDSCH RMC configuration |  | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |
| RMSI CORESET RMC configuration |  | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |
| Dedicated CORESET RMC configuration |  | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |
| OCNG Pattern |  | OP.1 |  |  | OP.1 |  |  |
| Initial DL BWP configuration |  | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| RLM-RS |  | SSB |  |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | -130 |  |  | -130 |  |  |
| Pcompensation | dB | 0 |  |  | 0 |  |  |
| Qhysts | dB | 0 |  |  | 0 |  |  |
| Qoffsets, n | dB | 0 |  |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | SS-RSRP |  |  | SS-RSRP |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 14 | 14 | 14 | -4 | -infinity | 12 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | -98 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 14 | 14 | 14 | -4 | -infinity | 12 |
| SS-RSRP Note3 | dBm/SCS | -84 | -84 | -84 | -102 | -infinity | -86 |
| Io | dBm/9.36 MHz | -55.88 | -55.88 | -55.88 | -68.60 | -70.05 | -57.78 |
| Treselection | s | 0 | 0 | 0 | 0 | 0 | 0 |
| SnonIntrasearchP | dB | 50 |  |  | 50 |  |  |
| Threshx, highP | dB | 48 |  |  | 48 |  |  |
| Threshserving, lowP | dB | 44 |  |  | 44 |  |  |
| Threshx, lowP | dB | 50 |  |  | 50 |  |  |
| Propagation Condition |  | AWGN |  |  |  |  |  |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.Note 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.Note 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |

#### A.14.1.6.3 Test Requirements

The cell re-selection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps again on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 66 s.

The cell re-selection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to a lower priority cell shall be less than 6 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_inter_enh + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, NR_inter_enh + TSI-NR,

Where:

Thigher_priority_search See clause 4.2C.9

Tevaluate, NR_inter_enh See tables 4.2C.2.4-2 in clause 4.2C.2.4

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 65.12 s, allow 66 s for the cell re-selection delay to a higher priority

### A.14.1.7 Time-based measurement initiation to FR1 inter-frequency cell reselection

#### A.14.1.7.1 Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.4.

#### A.14.1.7.2 Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.14.1.7.2-1, A.14.1.7.2-2 and A.14.1.7.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas, and Cell 2 is of lower priority than Cell 1. Furthermore, UE has not registered with network for the tracking area containing Cell 2. t-Service broadcasted in SIB19 of Cell 1 is set to the time point that is 36 s after start of T2.

Table A.14.1.7.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.1.7.2-2: General test parameters for inter frequency NR cell re-selection test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
| Initial condition | Active cell |  | 1, 2 | Cell 1 |  |
| T2 end condition | Active cell |  | 1, 2 | Cell 2 |  |
|  | Neighbour cells |  | 1, 2 | Cell 1 |  |
| RF Channel Number |  |  | 1, 21 | 1 |  |
| Time offset between cells |  |  | 1, 2 | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | 1, 2 | Not Sent | No additional delays in random access procedure. |
| DRX cycle length |  | s | 1, 2 | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2 | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2 | Not configured |  |
| T1 |  | s | 1, 2 | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2 |
| T2 |  | s | 1, 2 | 40 | T2 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.14.1.7.2-3: Cell specific test parameters for inter frequency NR cell re-selection test case

| Parameter | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | SSC.1 for Config 1SSC.2 for Config 2 |  | NSC.1 for Config 1NSC.2 for Config 2 |  |
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
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 16 | 13 | -infinity | 16 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | -98 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | -98 |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 16 | 13 | -infinity | 16 |
| SS-RSRP Note3 | dBm/SCS | -82 | -85 | -infinity | -82 |
| Io | dBm/9.36 MHz | -53.94 | -56.84 | -70.05 | -53.94 |
| Treselection | s | 0 | 0 | 0 | 0 |
| SnonIntrasearchP | dB | 40 |  | 50 |  |
| Threshx, highP | dB | 48 |  | 48 |  |
| Threshserving, lowP | dB | 54 |  | 44 |  |
| Threshx, lowP | dB | 40 |  | 40 |  |
| Propagation Condition |  | AWGN |  |  |  |

#### A.14.1.7.3 Test Requirements

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a lower priority cell shall be less than 36 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Tevaluate, NR_ inter See Table 4.2C.2.4-1 in clause 4.2C.2.4

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB19 are scheduled with 80 ms period.

### A.14.1.8 Location-based measurement initiation to FR1 inter-frequency NR cell reselection

#### A.14.1.8.1 Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.4.

#### A.14.1.8.2 Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.14.1.8.2-1, A.14.1.8.2-2 and A.14.1.8.2-3. The test consists of two successive time periods, with time duration of T1and T2, respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas, and Cell 2 is of lower priority than Cell 1. Furthermore, UE has not registered with network for the tracking area containing Cell 2.At 4 s after the start of T2, the UE location is changed such that the distance to the reference location broadcasted in SIB19 of Cell 1 is exceeded by the configured value in distanceThresh plus 50m.

Table A.14.1.8.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.1.8.2-2: General test parameters for inter frequency NR cell re-selection test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
| Initial condition | Active cell |  | 1, 2 | Cell 1 |  |
| T2 end condition | Active cell |  | 1, 2 | Cell 2 |  |
|  | Neighbour cells |  | 1, 2 | Cell 1 |  |
| RF Channel Number |  |  | 1, 2 | 1 |  |
| Time offset between cells |  |  | 1, 2 | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | 1, 2 | Not Sent | No additional delays in random access procedure. |
| DRX cycle length |  | s | 1, 2 | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1, 2 | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | 1, 2 | Not configured |  |
| T1 |  | s | 1, 2 | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2 |
| T2 |  | s | 1, 2 | 40 | T2 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.14.1.8.2-3: Cell specific test parameters for inter frequency NR cell re-selection test case

| Parameter | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | SSC.1 for Config 1SSC.2 for Config 2 |  | NSC.1 for Config 1NSC.2 for Config 2 |  |
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
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 16 | 13 | -infinity | 16 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | -98 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | -98 |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 16 | 13 | -infinity | 16 |
| SS-RSRP Note3 | dBm/SCS | -82 | -85 | -infinity | -82 |
| Io | dBm/9.36 MHz | -53.94 | -56.84 | -70.05 | -53.94 |
| Treselection | s | 0 | 0 | 0 | 0 |
| SnonIntrasearchP | dB | 40 |  | 50 |  |
| Threshx, highP | dB | 48 |  | 48 |  |
| Threshserving, lowP | dB | 54 |  | 44 |  |
| Threshx, lowP | dB | 40 |  | 40 |  |
| Propagation Condition |  | AWGN |  |  |  |

#### A.14.1.8.3 Test Requirements

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a lower priority cell shall be less than 36 s.The UE starts searching for the cell only after 4 s after the start of T2 when the UE location is changed such that the distance to the reference location broadcasted in SIB19 of Cell 1 is exceeded by the configured value in distanceThresh plus 50m. Consideing that the cell re-selection delay to a newly detectable cell shall be less than 40 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Tevaluate, NR_ inter See Table 4.2C.2.4-1 in clause 4.2C.2.4

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB19 are scheduled with 80 ms period.

### A.14.1.9 Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion

#### A.14.1.9.1 Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements specified in clause 4.2C.2.8, for UEs that support Relaxed cell reselection on GSO feature, as defined in clause 5.4 in 38.306 [14], and fulfilling low mobility relaxed measurement criterion.

#### A.14.1.9.2 Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.14.1.9.2-1, A.14.1.9.2-2 and A.14.1.9.2-3. The test consists of two successive time periods, with time duration of T1 and T2, respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

As specified in the Test Purpose, the UE is configured with the relaxed measurement criterion for UE with low mobility defined in clause 5.2.4.9.1 in TS 38.304 [1]. So, Cell 2 and Cell 1 configure the UE as follows:

lowMobilityEvalutation TS 38.331 [2] criterion is configured according to the parameters listed in table A.14.1.9.2-3;

cellEdgeEvaluation TS 38.331 [2] criterion is not configured;

combineRelaxedMeasCondition TS 38.331 [2] is not configured;

Table A.14.1.9.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |

Table A.14.1.9.2-2: General test parameters for FR1 inter frequency NR cell re-selection test case for UE fulfilling low mobility criterion

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1 | Cell 2 | The UE camps on Cell 2 in the initial phase, it fulfills Low Mobility relaxation measurements criterion, and during T1 period the UE reselects to Cell 1 |
|  | Neighbour cells |  | 1 | Cell 1 |  |
| T1 end condition | Active cell |  | 1 | Cell 1 | The UE shall perform reselection to Cell 1 during T1 |
|  | Neighbour cells |  | 1 | Cell 2 |  |
| T2 end condition | Active cell |  | 1 | Cell 2 | The UE shall perform reselection to Cell 2 with higher priority during T2 |
|  | Neighbour cells |  | 1 | Cell 1 |  |
| RF Channel Number |  |  | 1 | 1, 2 |  |
| Time offset between cells |  |  | 1 | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | 1 | Not Sent | No additional delays in random access procedure. |
| SSB Configuration |  |  | 1 | SSB.1 FR1 |  |
| SMTC configuration |  |  | 1 | SMTC pattern 2 | Configured in SIB4 of Cell 1 |
|  |  |  |  | SMTC pattern 6 | Configured in SIB4 of Cell 2 |
| DRX cycle length |  | s | 1 | 0.64 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1 | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | 1 | Not configured |  |
| T1 |  | s | 1 | 25 s | T1 is defined so that cell re-selection reaction time is taken into account. |
| T2 |  | s | 1 | 25 s | T2 is defined so that cell re-selection reaction time is taken into account. |

Table A.14.1.9.2-3: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case in AWGN for UE fulfilling low mobility criterion

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 |  | T2 |
| Satellite information |  | 1 | SSC.1 |  | NSC.1 |  |  |
|  |  |  |  |  |  |  |  |
| PDSCH RMC  configuration |  | 1 | SR.1.1 FDD |  | SR.1.1 FDD |  |  |
| RMSI CORESET  RMC configuration |  | 1 | CR.1.1 FDD |  | CR.1.1 FDD |  |  |
| Dedicated CORESET  RMC configuration |  | 1 | CCR.1.1 FDD |  | CCR.1.1 FDD |  |  |
| OCNG Pattern |  | 1 | OP.1 defined in A.3.2.1 |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1 | DLBWP.0.1 |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1 | ULBWP.0.1 |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1 | SSB |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1 | -140 |  | -140 |  |  |
| Pcompensation | dB | 1 | 0 |  | 0 |  |  |
| Qhysts | dB | 1 | 0 |  | 0 |  |  |
| Qoffsets, n | dB | 1 | 0 |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1 | SS-RSRP |  | SS-RSRP |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1 | 14 | 14 | -4 | 12 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -98 |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -98 |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 14 | 14 | -4 |  | 12 |
| SS-RSRP Note3 | dBm/SCS | 1 | -84 | -84 | -102 |  | -86 |
| Io | dBm/9.36 MHz | 1 | -55.88 | -55.88 | -68.60 |  | -57.78 |
| Treselection | s | 1 | 0 | 0 | 0 |  | 0 |
| SnonintersearchP | dB | 1 | Not sent |  | Not sent |  |  |
| Threshx, highP | dB | 1 | 48 |  | 48 |  |  |
| Threshserving, lowP | dB | 1 | 44 |  | 44 |  |  |
| Threshx, lowP | dB | 1 | 50 |  | 50 |  |  |
| SSearchDeltaP | dB | 1 | 3 |  | 3 |  |  |
| TSearchDeltaP | s | 1 | 5 |  | 5 |  |  |
| Propagation Condition |  | 1 | AWGN |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |

#### A.14.1.9.3 Test Requirements

The cell reselection delay to an already detected lower priority cell for UE fulfilling low mobility relaxed measurements is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to a lower priority cell for UE fulfilling low mobility relaxed measurements shall be less than 17 s.

The cell reselection delay to an already detected higher priority cell for UE fulfilling low mobility relaxed measurements is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected higher priority cell for UE fulfilling low mobility relaxed measurements shall be less than 17 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a known lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Tevaluate, NR_ inter See Table 4.2.2.10.2-1 in clause 4.2.2.10.2

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 16.64 s, allow 17 s for the cell re-selection delay to an already detected lower priority cell and 16.64 s for the cell re-selection delay to an already detected higher priority cell, which we allow 17 s for UE fulfilling low mobility relaxed measurements in the test case.

### A.14.1.10 Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion

#### A.14.1.10.1 Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements specified in clause 4.2C.2.8, for UEs that support Relaxed cell reselection on GSO feature, as defined in clause 5.4 in 38.306 [14], and fulfilling not-at-cell edge relaxed measurement criterion.

#### A.14.1.10.2 Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.14.1.10.2-1, A.14.1.10.2-2 and A.14.1.10.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

As specified in the Test Purpose, the UE is configured with the relaxed measurement criterion for UE not-at-cell edge as defined in clause 5.2.4.9.2 in TS 38.304 [1]. So, Cell 2 and Cell 1configures the UE as follows:

cellEdgeEvaluation TS 38.331 [2] criterion is configured according to the parameters listed in table A.14.1.9.2-3;

lowMobilityEvalutation TS 38.331 [2] criterion is not configured;

combineRelaxedMeasCondition TS 38.331 [2] is not configured;

Table A.14.1.10.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |

Table A.14.1.10.2-2: General test parameters for FR1 inter frequency NR cell re-selection test case for UE fulfilling not-at-cell edge criterion

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1 | Cell 2 | The UE camps on Cell 2 in the initial phase, it fulfills Not-at-cell edge relaxation measurements criterion, and during T1 period the UE reselects to Cell 1 |
|  | Neighbour cells |  | 1 | Cell 1 |  |
| T1 end condition | Active cell |  | 1 | Cell 1 | The UE shall perform reselection to Cell 1 during T1 |
|  | Neighbour cells |  | 1 | Cell 2 |  |
| T2 end condition | Active cell |  | 1 | Cell 2 | The UE shall perform reselection to Cell 2 with higher priority during T2 |
|  | Neighbour cells |  | 1 | Cell 1 |  |
| RF Channel Number |  |  | 1 | 1, 2 |  |
| Time offset between cells |  |  | 1 | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | 1 | Not Sent | No additional delays in random access procedure. |
| SSB Configuration |  |  | 1 | SSB.1 FR1 |  |
| SMTC configuration |  |  | 1 | SMTC pattern 2 | Configured in SIB4 of Cell 1 |
|  |  |  |  | SMTC pattern 6 | Configured in SIB4 of Cell 2 |
| DRX cycle length |  | s | 1 | 0.64 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1 | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | 1 | Not configured |  |
| T1 |  | s | 1 | 20 s | T1 is defined so that cell re-selection reaction time is taken into account. |
| T2 |  | s | 1 | 20 s | T2 is defined so that cell re-selection reaction time is taken into account. |

Table A.14.1.10.2-3: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case in AWGN for UE fulfilling not-at-cell edge criterion

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 |  | T2 |
| Satellite information |  | 1 | SSC.1 |  | NSC.1 |  |  |
|  |  |  |  |  |  |  |  |
| PDSCH RMC  configuration |  | 1 | SR.1.1 FDD |  | SR.1.1 FDD |  |  |
| RMSI CORESET  RMC configuration |  | 1 | CR.1.1 FDD |  | CR.1.1 FDD |  |  |
| Dedicated CORESET  RMC configuration |  | 1 | CCR.1.1 FDD |  | CCR.1.1 FDD |  |  |
| OCNG Pattern |  | 1 | OP.1 defined in A.3.2.1 |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | 1 | DLBWP.0.1 |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1 | ULBWP.0.1 |  | ULBWP.0.1 |  |  |
| RLM-RS |  | 1 | SSB |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | 1 | -140 |  | -140 |  |  |
| Pcompensation | dB | 1 | 0 |  | 0 |  |  |
| Qhysts | dB | 1 | 0 |  | 0 |  |  |
| Qoffsets, n | dB | 1 | 0 |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | 1 | SS-RSRP |  | SS-RSRP |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1 | 14 | 14 | -4 | 12 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1 | -98 |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1 | -98 |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1 | 14 | 14 | -4 |  | 12 |
| SS-RSRP Note3 | dBm/SCS | 1 | -84 | -84 | -102 |  | -86 |
| Io | dBm/9.36 MHz | 1 | -55.88 | -55.88 | -68.60 |  | -57.78 |
| Treselection | s | 1 | 0 | 0 | 0 |  | 0 |
| SnonintersearchP | dB | 1 | Not sent |  | Not sent |  |  |
| Threshx, highP | dB | 1 | 48 |  | 48 |  |  |
| Threshserving, lowP | dB | 1 | 44 |  | 44 |  |  |
| Threshx, lowP | dB | 1 | 50 |  | 50 |  |  |
| SSearchThresholdP | dB | 1 | 50 |  | 50 |  |  |
| SSearchThresholdQ | s | 1 | Not Configured |  |  |  |  |
| Propagation Condition |  | 1 | AWGN |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |

#### A.14.1.10.3 Test Requirements

The cell reselection delay to an already detected lower priority cell for UE fulfilling not-at-cell edge relaxed measurements is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected lower priority cell for UE fulfilling not-at-cell edge relaxed measurements shall be less than 17 s.

The cell reselection delay to an already detected higher priority cell for UE fulfilling not-at-cell-edge relaxed measurements is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected higher priority cell for UE fulfilling not-at-cell-edge relaxed measurements shall be less than 17 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Tevaluate, NR_ inter See Table 4.2.2.10.3-1 in clause 4.2.2.10

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 16.64 s, allow 17 s for the cell re-selection delay to an already detected lower priority cell and 16.64 s for the cell re-selection delay to an already higher priority cell, which we allow 17 s for UE fulfilling not-at-cell edge relaxed measurements in the test case.

### A.14.1.11 Cell reselection to FR1 inter-RAT E-UTRAN cells with TN carrier

#### A.14.1.11.1 Test purpose and Environment

This test is to verify the requirement for the NR NTN to E-UTRAN TN inter-RAT cell reselection requirements specified in clause 4.2C.2.11 when the E-UTRAN cell is of higher priority.

#### A.14.1.11.2 Test parameters

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A.14.1.11.2-1, A.14.1.11.2-2, A.14.1.11.2-3 and A.14.1.11.2-4. The test consists of two successive time periods, with time duration of T1 and T2, respectively. NR Cell 1 is already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of higher priority than Cell 1.

A.14.1.11.2-1: Supported test configurations

| Configuration | Description of serving cell | Description of target cell |
| --- | --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz | LTE 10 MHz bandwidth, TDD duplex mode |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz | LTE 10 MHz bandwidth, TDD duplex mode |
| 3 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz | LTE 10 MHz bandwidth, FDD duplex mode |
| 4 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz | LTE 10 MHz bandwidth, FDD duplex mode |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases, and the UE is only required to be tested in one of the supported test configurations of the applicable scenario (GSO or NGSO). |  |  |

Table A.14.1.11.2-2: General test parameters for NR to E-UTRAN cell re-selection test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1-4 | Cell 1 | The UE camps on Cell 1 in the initial phase and during T2 period the UE reselects to Cell 2. |
| T2 end | Active cell |  | 1-4 | Cell 2 | The UE shall perform reselection to cell |
| condition | Neighbour cell |  | 1-4 | Cell 1 | 2 during T2. |
| Access Barring Information |  | - | 1-4 | Not Sent | No additional delays in random access procedure. |
| DRX cycle length |  | s | 1-4 | 1.28 | The value shall be used for all cells in the test. |
| NR PRACH configuration index |  |  | 1-4 | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| E-UTRAN PRACH configuration index |  |  | 1-4 | 53 | As specified in table 5.7.1-2 in TS 36.211 [23] |
| T1 |  | s | 1-4 | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed. The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2. |
| T2 |  | s | 1-4 | 70 | T2 needs to be defined so that cell re-selection reaction time is taken into account. |

Table A.14.1.11.2-3: Cell specific test parameters for NR Cell 1

| Parameter | Unit | Test configuration | Cell 1 |  |
| --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 |
| Satellite information |  | 1,3 | SSC.1 |  |
|  |  | 2,4 | SSC.2 |  |
| TDD configuration |  | 1-4 | N/A |  |
| PDSCH parameters |  | 1-4 | SR.1.1 FDD |  |
| RMSI CORESET parameters |  | 1-4 | CR.1.1 FDD |  |
| Dedicated CORESET parameters |  | 1-4 | CCR.1.1 FDD |  |
| SSB parameters |  | 1-4 | SSB.1 FR1 |  |
| NR SMTC parameters |  | 1-4 | SMTC.2 |  |
| OCNG Pattern |  | 1-4 | OP.1 defined in A.3.2.1 |  |
| Initial DL BWP configuration |  | 1-4 | DLBWP.0.1 |  |
| Initial UL BWP configuration |  | 1-4 | ULBWP.0.1 |  |
| RLM-RS |  | 1-4 | SSB |  |
| Qrxlevmin | dBm/SCS | 1-4 | -140 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] | dBm/SCS | 1-4 | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] | dBm/15 kHz | 1-4 | -98 |  |
| SS-RSRP | dBm/SCS | 1-4 | -84 | -84 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1-4 | 14 | 14 |
| ![](media_svg/image9.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1-4 | 14 | 14 |
| Io | dBm/9.36 MHz | 1-4 | -55.88 | -55.88 |
| Treselection | s | 1-4 | 0 |  |
| SnonintrasearchP | dB | 1-4 | 50 |  |
| Threshx, highP (Note 2) | dB | 1-4 | 48 |  |
| Threshserving, lowP | dB | 1-4 | 44 |  |
| Threshx, lowP | dB | 1-4 | 50 |  |
| Propagation Condition |  | 1-4 | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: This refers to the value of  Threshx, high  which is included in NR system information, and is a threshold for the E-UTRA target cell |  |  |  |  |

Table A.14.1.11.2-4: Cell specific test parameters for E-UTRA Cell 2

| Parameter | Unit | Cell 2 |  |
| --- | --- | --- | --- |
|  |  | T1 | T2 |
| E-UTRA RF Channel number |  | 1 |  |
| BWchannel | MHz | 10 |  |
| OCNG Patterns defined in TS 36.133 [15] clause A.3.2 |  | OP.2 TDD for test configuration 1, 2OP.2 FDD for test configuration 3, 4 |  |
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
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] | dBm/15 kHz | -98 |  |
| RSRP | dBm/15 KHz | -infinity | -86 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | -infinity | 12 |
| ![](media_svg/image9.svg) [公式≈: ^{Ê}s^{N}oc] | dB | -infinity | 12 |
| TreselectionEUTRAN | s | 0 |  |
| SnonintrasearchP | dB | Not sent |  |
| Threshx, highP | dB | 48 |  |
| Threshserving, lowP | dB | 44 |  |
| Threshx, lowP (Note 2) | dB | 50 |  |
| Propagation Condition |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: This refers to the value of  Threshx, Low  which is included in E-UTRA system information, and is a threshold for the NR target cell |  |  |  |

#### A.14.1.11.3 Test requirements

The cell reselection delay to a higher priority E-UTRAN cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, E-UTRAN + TSI-E-UTRA,

Where:

Thigher_priority_search See clause 4.2C.2.9

Tevaluate, NR_ inter See clause 4.2C.2.11

TSI-E-UTRA Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority E-UTRAN cell.

### A.14.1.12 Cell re-selection to FR1 inter-frequency NR case with TN carrier

#### A.14.1.12.1 Test purpose and Environment

This test is to verify the requirement for the inter frequency NR NTN to TN cell re-selection requirements specified in clause 4.2C.2.10.

#### A.14.1.12.2 Test parameters

The test scenario comprises of 2 cells on 2 different NR carriers, including NR NTN cell 1 on RF channel 1 and NR TN cell 2 on RF channel 2, respectively as given in tables A.14.1.12.2-1, A.14.1.12.2-2 and A.14.1.12.3-3. The test consists of two successive time periods, with time duration of T1 and T2, respectively. Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

Table A.14.1.12.2-1: Supported test configurations

| Configuration | Description of serving cell | Description of target cell |
| --- | --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 3 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| 4 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 5 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 15 kHz SSB SCS, 10 MHz bandwidth, TDD duplex mode |
| 6 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10 MHz | 30 kHz SSB SCS, 40 MHz bandwidth, TDD duplex mode |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases, and the UE is only required to be tested in one of the supported test configurations of the applicable scenario (GSO or NGSO). |  |  |

TableA.14.1.12.2-2: General test parameters for inter frequency NR cell re-selection test case

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
| Initial condition | Active cell |  | 1-6 | Cell 1 |  |
| T2 end condition | Active cell |  | 1-6 | Cell 2 |  |
|  | Neighbour cells |  | 1-6 | Cell 1 |  |
| RF Channel Number |  |  | 1-6 | 1,2 | Cell 1 is on RF channel 1Cell 2 is on RF channel 2 |
| Time offset between cells |  |  | 1-6 | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | 1-6 | Not Sent | No additional delays in random access procedure. |
| SSB configuration |  |  | 1-6 | SSB.1 FR1 |  |
| SMTC configuration |  |  | 1-6 | SMTC.6 | Configured in SIB4 for Cell 1 and Cell 2 |
| DRX cycle length |  | s | 1-6 | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 1-6 | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | 1-6 | Not configured |  |
| Ephemeris information |  |  | 1-6 | Note 1 | The detailed configuration is specified in SIB19 |
| T1 |  | s | 1-6 | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2 |
| T2 |  | s | 1-6 | 70 | T2 needs to be defined so that cell re-selection reaction time is taken into account. |
| Note 1: Detailed ephemeris information is provided in TS 38.508-1 [38] |  |  |  |  |  |

Table A.14.1.12.3-3: Cell specific test parameters for inter frequency NR cell re-selection test case

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1,2,3 | SSC.1 |  | N/A |  |
|  |  | 4,5,6 | SSC.2 |  |  |  |
| TDD configuration |  | 1,4 | N/A |  | N/A |  |
|  |  | 2,5 |  |  | TDDConf.1.1 |  |
|  |  | 3,6 |  |  | TDDConf.2.1 |  |
| PDSCH RMC |  | 1,4 | SR.1.1 FDD |  | SR.1.1 FDD |  |
| configuration |  | 2,5 |  |  | SR.1.1 TDD |  |
|  |  | 3,6 |  |  | SR.2.1 TDD |  |
| RMSI CORESET |  | 1,4 | CR.1.1 FDD |  | CR.1.1 FDD |  |
| RMC configuration |  | 2,5 |  |  | CR.1.1 TDD |  |
|  |  | 3,6 |  |  | CR.2.1 TDD |  |
| Dedicated CORESET |  | 1,4 | CCR.1.1 FDD |  | CCR.1.1 FDD |  |
| RMC configuration |  | 2,5 |  |  | CCR.1.1 TDD |  |
|  |  | 3,6 |  |  | CCR.2.1 TDD |  |
| OCNG Pattern |  | 1-6 | OP.1 defined in clause A.3.2.1 |  | OP.1 defined in clause A.3.2.1 |  |
| Initial DL BWP configuration |  | 1-6 | DLBWP.0.1 |  | DLBWP.0.1 |  |
| Initial UL BWP configuration |  | 1-6 | ULBWP.0.1 |  | ULBWP.0.1 |  |
| RLM-RS |  | 1-6 | SSB |  | SSB |  |
| Qrxlevmin | dBm/SCS | 1,2,4,5 | -140 |  | -140 |  |
|  |  | 3,6 |  |  | -137 |  |
| Pcompensation | dB | 1-6 | 0 |  | 0 |  |
| Cell_selection_and_reselection_quality_measurement |  | 1-6 | SS-RSRP |  | SS-RSRP |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1-6 | 14 | 14 | -infinity | 12 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1,2,4,5 | -98 |  | -98 |  |
|  |  | 3,6 |  |  | -95 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1-6 | -98 |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1-6 | 14 | 14 | -infinity | 12 |
| SS-RSRP Note3 | dBm/SCS | 1,2,4,5 | -84 | -84 | -infinity | -86 |
|  |  | 3,6 |  |  | -infinity | -83 |
| Io | dBm/Ch BW | 1,2,4,5 | -55.88 | -55.88 | -70.05 | -57.78 |
|  |  | 3,6 |  |  | -63.96 | -51.69 |
| Treselection | s | 1-6 | 0 | 0 | 0 | 0 |
| SnonintrasearchP | dB | 1-6 | 50 |  | 50 |  |
| Threshx, highP | dB | 1-6 | 48 |  | 48 |  |
| Threshserving, lowP | dB | 1-6 | 44 |  | 44 |  |
| Threshx, lowP | dB | 1-6 | 50 |  | 50 |  |
| Propagation Condition |  | 1-6 | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

#### A.14.1.12.3 Test requirements

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter_TN + TSI-NR

Where:

Thigher_priority_search See clause 4.2C.2.9

Tevaluate, NR_ inter_TN See clause 4.2C.2.10

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority

### A.14.1.13 Cell reselection to FR1 intra-frequency NR case for UE operating on a cell with less than 5 MHz BW

#### A.14.1.13.1 Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for satellite access specified in clause 4.2C.2.3 for UE capable of operating on a cell with less than 5 MHz BW.

#### A.14.1.13.2 Test Parameters

The test scenario comprises of 2 cells on 1 NR carrier configured each in a different satellite as given in tables A.14.1.13.2-1, A.14.1.13.2-2 and A.14.1.13.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.14.1.13.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 3MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 3MHz |
| Note: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.1.13.2-2: General test parameters for intra frequency NR cell re-selection test case

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Initial condition | Active cell |  | Cell 1 |  |
| T2 end condition | Active cell |  | Cell 2 |  |
|  | Neighbour cells |  | Cell 1 |  |
| Final condition | Active cell |  | Cell 1 |  |
|  | Neighbour cells |  | Cell 2 |  |
| RF Channel Number |  |  | 1 |  |
| BWchannel |  | MHz | NPRB,c = 15 |  |
| Time offset between cells |  |  | 3 ms | Asynchronous cells |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| DRX cycle length |  | s | 1.28 | The value shall be used for all cells in the test. |
| PRACH configuration index |  |  | 102 | The detailed configuration is specified in TS 38.211 [6] clause 6.3.3.2 |
| rangeToBestCell |  |  | Not configured |  |
| T1 |  | s | >7 | During T1, Cell 2 shall be powered off, and during the off time the physical cell identity shall be changed, The intention is to ensure that Cell 2 has not been detected by the UE prior to the start of period T2 |
| T2 |  | s | 40(NOTE 1) | T2 needs to be defined so that cell re-selection reaction time is taken into account. |
| T3 |  | s | 15(NOTE 1) | T3 needs to be defined so that cell re-selection reaction time is taken into account. |
| NOTE 1: If the test is performed in a NGSO configuration, and the scaling factor Kmulti_SMTC defined in clause 4.2C.2.3 is greater than 1, according to UE capabilities, the duration of times T2 and T3 shall be scaled for the same factor to allow the UE to complete the cell reselection within the duration of the test case. |  |  |  |  |

Table A.14.1.13.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case

| Parameter | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | SSC.1 for Config 1SSC.2 for Config 2 |  |  | NSC.1 for Config 1NSC.2 for Config 2 |  |  |
| PDSCH RMC configuration |  | SR.1.2 FDD |  |  | SR.1.2 FDD |  |  |
| RMSI CORESET configuration |  | CR.1.3 FDD |  |  | CR.1.3 FDD |  |  |
| Dedicated CORESET configuration |  | CCR.1.6 FDD |  |  | CCR.1.6 FDD |  |  |
| OCNG Pattern |  | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| Initial DL BWP configuration |  | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| SSB configuration |  | SSB.13 FR1 |  |  | SSB.13 FR1 |  |  |
| SMTC configuration |  | #1: SMTC.2 for Cell 1#2: SMTC.5 for Cell 2 |  |  | #1: SMTC.6 for Cell 1#2: SMTC.2 for Cell 2 |  |  |
| RLM-RS |  | SSB |  |  | SSB |  |  |
| Qrxlevmin | dBm/SCS | -130 |  |  | -130 |  |  |
| Pcompensation | dB | 0 |  |  | 0 |  |  |
| Qhysts | dB | 0 |  |  | 0 |  |  |
| Qoffsets, n | dB | 0 |  |  | 0 |  |  |
| Cell_selection_and_reselection_quality_measurement |  | SS-RSRP |  |  | SS-RSRP |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 16 | -3.11 | 2.79 | -infinity | 2.79 | -3.11 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | -98 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 16 | 13 | 16 | -infinity | 16 | 13 |
| SS-RSRP Note3 | dBm/SCS | -82 | -85 | -82 | -infinity | -82 | -85 |
| Io | dBm/2.7 MHz | -59.34 | -57.61 | -57.61 | Same as parameters specified in Cell 1 columns- |  |  |
| Treselection | s | 0 | 0 | 0 | 0 | 0 | 0 |
| SintrasearchP | dB | 60 |  |  | 60 |  |  |
| Propagation Condition |  | AWGN |  |  |  |  |  |

#### A.14.1.13.3 Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than:

## 34 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.13.2-2); or

## 66 s if Kmulti_SMTC is equal to 2.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to an already detected cell shall be less than:

## 8 s if Kmulti_SMTC  is  equal to 1 (see note on Table A.14.1.13.2-2); or

## 14.5 s if Kmulti_SMTC is equal to 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE: The cell re-selection delay to a newly detectable cell can be expressed as: Kmulti_SMTC *Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Kmulti_SMTC *Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_Intra + 40ms  See Table 4.2C.2.3-1 in clause 4.2C.2.3

Tevaluate, NR_ intra See Table 4.2C.2.3-1 in clause 4.2C.2.3

Kmulti_SMTC  is described in clause 4.2C.2.3

TSI-NR Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1320 ms is assumed in this test case provided that SIB1 and SIB19 are scheduled with 20 ms period and 80 ms period, respectively.

If Kmulti_SMTC = 1, Kmulti_SMTC *Tevaluate, NR_Intra + TSI-NR = 7.68 s; allow 8 s. And Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 33.36 s, allow 34 s.

If K_multi_SMTC = 2, Kmulti_SMTC *Tevaluate, NR_Intra + TSI-NR = 14.08 s; allow 14.5 s. And Kmulti_SMTC *Tdetect, NR_ intra + TSI-NR = 65.4 s, allow 66 s.

## A.14.2 RRC_CONNECTED state mobility

### A.14.2.1 Handover

#### A.14.2.1.1 Intra-frequency SAN Handover from FR1 to FR1

##### A.14.2.1.1.1 Test Purpose and Environment

This test is to verify the requirement for Intra-frequency SAN Handover from FR1 to FR1 specified in clause 6.1C.1.

##### A.14.2.1.1.2 Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells as given in table A.14.2.1.1.2-1, A.14.2.1.1.2-2, and A.14.2.1.1.2-3. Both handover delay and interruption length are tested.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure intra-frequency neighbour cell with Event A3 report.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1. The RRC message implying handover to Cell 2 shall be sent to the UE during period T2, after the UE has reported Event A3. The start of T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.14.2.1.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 3 | NGSO with varying Doppler and delay shift NTN channel model, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.1.1.2-2: General test parameters Intra-frequency SAN handover from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 | One NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 |  |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) |  |  | (0, 0, 0) | Set by any pre-configured means(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| A3-Offset |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |
| T3 |  | s | 1 |  |
| NOTE 1: For Config 3, the UE position is set by AT command according to G.4.2 of TS 38.101-5 [43] at the beginning if the test, and remains unchanged during the test. |  |  |  |  |

Table A.14.2.1.1.2-3: Cell specific test parameters for Intra frequency SAN handover test case

| Parameter |  | Test configuration | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | Config 1 |  | SSC.1 |  |  | NSC.1 |  |  |
|  |  | Config 2,3 |  | SSC.2 |  |  | NSC.2 |  |  |
| NR RF Channel Number |  | Config 1,2,3 |  | 1 |  |  | 1 |  |  |
| BWchannel |  |  | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |  |  |
| BWP BW |  |  | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |  |  |
| DRX Cycle |  | Config 1,2,3 | ms | Not Applicable |  |  |  |  |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 FDD |  |  |  |  |  |
| CORESET Reference Channel |  |  |  | CR.1.1 FDD |  |  |  |  |  |
| TRS configuration |  |  |  | TRS.1.1 FDD |  |  |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |  |  |
| SSB Configuration |  |  |  | SSB.1 FR1 |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 |  |  |  |  |  |
| BWP configuration | Initial DL BWP | Config 1,2,3 |  | DLBWP.0.1 |  |  |  |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | Config 1,2,3 | dB | 0 |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | Config 1,2,3 | dBm/ 15 kHz | -98 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/ SCS | -98 |  |  |  |  |  |
| ![](media_svg/image10.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 8 | -3.3 | -3.3 | -Infinity | 2.36 | 2.36 |
| ![](media_svg/image11.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 8 | 8 | 8 | -Infinity | 11 | 11 |
| SSB_RP |  |  | dBm/ SCS | -90 | -90 | -90 | -Infinity | -87 | -87 |
| IoNote3 |  |  | dBm/ 9.36 MHz | -61.41 | -57.06 | -57.06 | -61.41 | -57.06 | -57.06 |
| Propagation condition |  |  | - | AWGN for Config 1,2, AWGN with time varying Doppler and delay shifts for Config 3 |  |  | AWGN for Config 1,2, AWGN with time varying Doppler and delay shifts for Config 3 |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: For Config 3, the initial ephemerisInfo of SSC.2 and NSC.2 refers to Table G.4.1-1 of TS 38.101-5 [43], while SSC.2 is propagated with a different epoch time, corresponding to approximately 90 degrees. |  |  |  |  |  |  |  |  |  |

##### A.14.2.1.1.3 Test Requirements


The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2]. Tinterrupt is defined in clause 6.1C.1.2.2.

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin ms

Here: Tsearch = 0; TIU = 20 ms; Tprocessing = 20 ms; T∆ = 20 ms; Tmargin = 2 ms.

This gives a total of 72 ms.

#### A.14.2.1.2 Inter-frequency SAN Handover from FR1 to FR1

##### A.14.2.1.2.1 Test Purpose and Environment

This test is to verify the requirement for Inter-frequency SAN Handover from FR1 to FR1 specified in clause 6.1C.1.

##### A.14.2.1.2.2 Test Parameters

The test scenario comprises of 2 NR FDD carriers and one cell on each carrier as given in table A.14.2.1.2.2-1, A.14.2.1.2.2-2 and A.14.2.1.2.2-3. Both handover delay and interruption length are tested.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure inter frequency neighbour cell with Event A3 report and Gap Pattern 0 is configured in the test case.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1. The RRC message implying handover to Cell 2 shall be sent to the UE during period T2, after the UE has reported Event A3. The start of T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.14.2.1.2.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.1.2.2-2: General test parameters Inter-frequency SAN handover from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1, 2 | Two NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 |  |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) |  |  | (0, 0, 0) | Set by any pre-configured means(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| Gap Pattern Id |  |  | 0 |  |
| Measurement gap offset |  |  | 9 |  |
| A3-Offset |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |
| T3 |  | s | 1 |  |

Table A.14.2.1.2.2-3: Cell specific test parameters for Inter frequency SAN handover test case

| Parameter |  | Test configuration | Unit | Cell 1 |  |  | Cell 2 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 | T1 |  | T2 | T3 |
| Satellite information |  | Config 1 |  | SSC.1 |  |  | NSC.1 |  |  |  |
|  |  | Config 2 |  | SSC.2 |  |  | NSC.2 |  |  |  |
| NR RF Channel Number |  | Config 1,2 |  | 1 |  |  | 2 |  |  |  |
| BWchannel |  |  | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |  |  |  |
| BWP BW |  |  | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |  |  |  |
| DRX Cycle |  | Config 1,2 | ms | Not Applicable |  |  |  |  |  |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 FDD |  |  |  |  |  |  |
| CORESET Reference Channel |  |  |  | CR.1.1 FDD |  |  |  |  |  |  |
| TRS configuration |  |  |  | TRS.1.1 FDD |  |  |  |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |  |  |  |
| SMTC Configuration |  |  |  | SMTC.2 |  |  |  | SMTC.5 |  |  |
| SSB Configuration |  |  |  | SSB.1 FR1 |  |  |  | SSB.5 FR1 |  |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 |  |  |  |  |  |  |
| BWP configuration | Initial DL BWP | Config 1,2 |  | DLBWP.0.1 |  |  |  |  |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |  |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |  |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | Config 1,2 | dB | 0 |  |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | Config 1,2 | dBm/ 15 kHz | -98 |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/ SCS | -98 |  |  |  |  |  |  |
| ![](media_svg/image10.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 4 | 4 | 4 | -Infinity |  | 9 | 9 |
| ![](media_svg/image11.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4 | 4 | 4 | -Infinity |  | 9 | 9 |
| SSB_RP |  |  | dBm/ SCS | -94 | -94 | -94 | -Infinity |  | -89 | -89 |
| IoNote3 |  |  | dBm/ 9.36 MHz | -64.59 | -64.59 | -64.59 | -70.05 |  | -60.53 | -60.53 |
| Propagation condition |  |  | - | AWGN |  |  | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |  |  |

##### A.14.2.1.2.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2]. Tinterrupt is defined in clause 6.1C.1.2.2.

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin ms

Here: Tsearch = 0; TIU = 20 ms; Tprocessing = 20 ms; T∆ = 20 ms; Tmargin = 2 ms.

This gives a total of 72 ms.

#### A.14.2.1.3 Intra-frequency SAN time-based conditional Handover from FR1 to FR1

##### A.14.2.1.3.1 Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN time-based conditional handover from FR1 to FR1 specified in clause 6.1C.2.

##### A.14.2.1.3.2 Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells as given in table A.14.2.1.3.2-1, and A.14.2.1.3.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. Immediately before the start of T1, the UE is configured to measure intra-frequency neighbour cell with a time-based handover trigger to Cell 2 with Event CondEvent T1 shall be sent to UE.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and time condition event CondEvent T1 is fulfilled.

Table A.14.2.1.3.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.1.3.2-2: General test parameters for Intra-frequency SAN time-based conditional handover from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 | One NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 | FDD duplex mode cell |
|  | Neighbouring cell |  | Cell 2 | FDD duplex mode cell |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) |  |  | (0, 0, 0) | Set by any pre-configured means(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| t1-Threshold-r17.condEventT1-r17 |  | s | T1 | Entering condition at start of T2 (end of T1) |
| duration-r17.condEventT1-r17 |  | slot | 1000 | Give 1 s search duration |
| A3-Offset in condition |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 2 |  |

Table A.14.2.1.3.2-3: Cell specific test parameters for Intra-frequency SAN time-based conditional handover from FR1 to FR1

| Parameter |  | Test configuration | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | Config 1 |  | SSC.1 |  | NSC.1 |  |
|  |  | Config 2 |  | SSC.2 |  | NSC.2 |  |
| NR RF Channel Number |  | Config 1,2 |  | 1 |  | 1 |  |
| BWchannel |  |  | MHz | 10: NPRB,c = 52 |  | 10: NPRB,c = 52 |  |
| BWP BW |  |  | MHz | 10: NPRB,c = 52 |  | 10: NPRB,c = 52 |  |
| DRX Cycle |  | Config 1,2 | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 FDD |  |  |  |
| CORESET Reference Channel |  |  |  | CR.1.1 FDD |  |  |  |
| TRS configuration |  |  |  | TRS.1.1 FDD |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |
| SSB Configuration |  |  |  | SSB.1 FR1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 |  |  |  |
| BWP configuration | Initial DL BWP | Config 1,2 |  | DLBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  | Config 1,2 | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | Config 1,2 | dBm/ 15 kHz | -98 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/ SCS | -98 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 8 | -3.3 | -Infinity | 2.36 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 8 | 8 | -Infinity | 11 |
| SSB_RP |  |  | dBm/ SCS | -90 | -90 | -Infinity | -87 |
| IoNote3 |  |  | dBm/ 9.36 MHz | -61.41 | -57.06 | -61.41 | -57.06 |
| Propagation condition |  |  | - | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |

##### A.14.2.1.3.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 872 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay is defined in clause 6.1C.2, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

Tmeasure = 600 + 200 ms; Tinterrupt = 62 ms; TCHO_execution = 10 ms.

This gives a total of 872 ms.

#### A.14.2.1.4 Inter-frequency SAN time-based conditional Handover from FR1 to FR1

##### A.14.2.1.4.1 Test Purpose and Environment

This test is to verify the requirement for inter -frequency SAN time-based conditional handover from FR1 to FR1 specified in clause 6.1C.2.

##### A.14.2.1.4.2 Test Parameters

The test scenario comprises of 2 NR FDD carrier and one cell on each carrier as given in table A.14.2.1.4.2-1, and A.14.2.1.4.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. Immediately before the start of T1, the UE is configured to measure inter-frequency neighbour cell with Gap pattern ID gp0 and time-based handover trigger to Cell 2 with Event CondEvent T1.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and after 1000 ms of T2, time condition event CondEvent T1 is fulfilled.

Table A.14.2.1.4.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.1.4.2-2: General test parameters for Inter-frequency SAN time-based conditional handover from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1, 2 | Two NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 | FDD duplex mode cell |
|  | Neighbouring cell |  | Cell 2 | FDD duplex mode cell |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) |  |  | (0, 0, 0) | Set by any pre-configured means(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| t1-Threshold-r17.condEventT1-r17 |  | s | T1+1 | Entering condition 1000ms after the start of T2 |
| duration-r17.condEventT1-r17 |  | slot | 1000 | Give 1 s search duration |
| Gap Pattern Id |  |  | 0 |  |
| Measurement gap offset |  |  | 9 |  |
| A3-Offset in condition |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 2 |  |

Table A.14.2.1.4.2-3: Cell specific test parameters for Inter-frequency SAN time-based conditional handover from FR1 to FR1

| Parameter |  | Test configuration | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | Config 1 |  | SSC.1 |  | NSC.1 |  |
|  |  | Config 2 |  | SSC.2 |  | NSC.2 |  |
| NR RF Channel Number |  | Config 1, 2 |  | 1 |  | 2 |  |
| BWchannel |  |  | MHz | 10: NPRB,c = 52 |  | 10: NPRB,c = 52 |  |
| BWP BW |  |  | MHz | 10: NPRB,c = 52 |  | 10: NPRB,c = 52 |  |
| DRX Cycle |  | Config 1, 2 | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 FDD |  |  |  |
| CORESET Reference Channel |  |  |  | CR.1.1 FDD |  |  |  |
| TRS configuration |  |  |  | TRS.1.1 FDD |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SMTC Configuration |  |  |  | SMTC.2 |  | SMTC.5 |  |
| SSB Configuration |  |  |  | SSB.1 FR1 |  | SSB.5 FR1 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 |  |  |  |
| BWP configuration | Initial DL BWP | Config 1, 2 |  | DLBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  | Config 1, 2 | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | Config 1, 2 | dBm/ 15 kHz | -98 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/ SCS | -98 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 4 | 4 | -Infinity | 9 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4 | 4 | -Infinity | 9 |
| SSB_RP |  |  | dBm/ SCS | -94 | -94 | -Infinity | -89 |
| IoNote3 |  |  | dBm/ 9.36 MHz | -64.59 | -64.59 | -70.05 | -60.53 |
| Propagation condition |  |  | - | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |

##### A.14.2.1.4.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 later than 1000 ms and less than 1072 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay is defined in clause 6.1C.2, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

Tmeasure = max(600 + 200, 1000) ms; Tinterrupt = 62 ms; TCHO_execution = 10 ms.

This gives a total of 1072 ms.

#### A.14.2.1.5 Intra-frequency SAN distance-based conditional Handover from FR1 to FR1

##### A.14.2.1.5.1 Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN distance-based conditional handover from FR1 to FR1 specified in clause 6.1C.2.

##### A.14.2.1.5.2 Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells as given in table A.14.2.1.5.2-1, and A.14.2.1.5.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure intra-frequency neighbour cell. The RRC message implying distance-based handover to Cell 2 with Event D1 shall be sent to UE, at a time earlier than TRRC (10 ms) before the beginning of T2.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and location condition event condEventD1-r17 is fulfilled.

Table A.14.2.1.5.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.1.5.2-2: General test parameters for Intra-frequency SAN distance-based conditional handover from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 | One NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 | FDD duplex mode cell |
|  | Neighbouring cell |  | Cell 2 | FDD duplex mode cell |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) at T1 start |  |  | (0, 0, 0) | Set by any pre-configured means(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| UE moving speed |  | km/h | (108, 0, 0) | Set by any pre-configured means |
| referenceLocation1-r17.condEventD1-r17 |  | m | (-700, 0, 0) | Reference location for serving cell |
| referenceLocation2-r17.condEventD1-r17 |  | m | (1300, 0, 0) | Reference location for target cell |
| distanceThreshFromReference1-r17.condEventD1-r17 |  | 50m | 20 | D1-1 Location condition is fulfilled at T2 |
| distanceThreshFromReference2-r17.condEventD1-r17 |  | 50m | 20 | D1-2 Location condition is fulfilled at T2 |
| hysteresis-r17.condEventD1-r17 |  | 10m | 0 |  |
| timeToTrigger-r17.condEventD1-r17 |  | s | 0 |  |
| A3-Offset in condition |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 12 |  |
| T2 |  | s | 6 |  |

Table A.14.2.1.5.2-3: Cell specific test parameters for Intra-frequency SAN distance-based conditional handover from FR1 to FR1

| Parameter |  | Test configuration | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | Config 1 |  | SSC.1 |  | NSC.1 |  |
|  |  | Config 2 |  | SSC.2 |  | NSC.2 |  |
| NR RF Channel Number |  | Config 1, 2 |  | 1 |  | 1 |  |
| BWchannel |  |  | MHz | 10: NPRB,c = 52 |  | 10: NPRB,c = 52 |  |
| BWP BW |  |  | MHz | 10: NPRB,c = 52 |  | 10: NPRB,c = 52 |  |
| DRX Cycle |  | Config 1, 2 | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 FDD |  |  |  |
| CORESET Reference Channel |  |  |  | CR.1.1 FDD |  |  |  |
| TRS configuration |  |  |  | TRS.1.1 FDD |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |
| SSB Configuration |  |  |  | SSB.1 FR1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 |  |  |  |
| BWP configuration | Initial DL BWP | Config 1, 2 |  | DLBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  | Config 1, 2 | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | Config 1, 2 | dBm/ 15 kHz | -98 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/ SCS | -98 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 8 | -3.3 | -Infinity | 2.36 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 8 | 8 | -Infinity | 11 |
| SSB_RP |  |  | dBm/ SCS | -90 | -90 | -Infinity | -87 |
| IoNote3 |  |  | dBm/ 9.36 MHz | -61.41 | -57.06 | -61.41 | -57.06 |
| Propagation condition |  |  | - | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |

##### A.14.2.1.5.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 872 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay is defined in clause 6.1C.2, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

UE moving speed, v = (108km/h*1000/3600) = 30m/s.

At start of T2,

distance to source cell reference location is 30 m/s * 12 s – (-700)m = 1060m, and D1-1 = 1000m

distance to target cell reference location is 30 m/s * 12 s – 1300m = -940m, and D1-2 = 1000m

i.e. D1-1 and D1-2 conditions are fulfilled at start of T2 with >=50m location margin.

Tmeasure = max(600 + 200 ms, 0) = 800 ms;

Tinterrupt = 62 ms; TCHO_execution = 10 ms.

This gives a total of 800 ms + 62 ms + 10 ms = 872 ms.

#### A.14.2.1.6 Inter-frequency SAN distance-based conditional Handover from FR1 to FR1

##### A.14.2.1.6.1 Test Purpose and Environment

This test is to verify the requirement for inter -frequency SAN distance-based conditional handover from FR1 to FR1 specified in clause 6.1C.2.

##### A.14.2.1.6.2 Test Parameters

The test scenario comprises of 2 NR FDD carrier and one cell on each carrier as given in table A.14.2.1.6.2-1, and A.14.2.1.6.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure inter-frequency neighbour cell and Gap pattern ID gp0. The RRC message implying distance-based handover to Cell 2 with Event D1 shall be sent to UE, at a time earlier than TRRC (10 ms) before the beginning of T2.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and after 11670 ms of T2, location condition event condEventD1-r17 is fulfilled.

Table A.14.2.1.6.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.1.6.2-2: General test parameters for Inter -frequency SAN distance-based conditional handover from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1, 2 | Two NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 | FDD duplex mode cell |
|  | Neighbouring cell |  | Cell 2 | FDD duplex mode cell |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) at T1 start |  |  | [(0, 0, 0)] | Set by any pre-configured means (L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| UE moving speed |  | km/h | (108, 0, 0) | Set by any pre-configured means |
| referenceLocation1-r17.condEventD1-r17 |  | m | (-700, 0, 0) | Reference location for serving cell |
| referenceLocation2-r17.condEventD1-r17 |  | m | (1300, 0, 0) | Reference location for target cell |
| distanceThreshFromReference1-r17.condEventD1-r17 |  | 50m | 20 | D1-1 Location condition is fulfilled at T2 |
| distanceThreshFromReference2-r17.condEventD1-r17 |  | 50m | 20 | D1-2 Location condition is fulfilled at T2 |
| hysteresis-r17.condEventD1-r17 |  | 10m | 0 |  |
| timeToTrigger-r17.condEventD1-r17 |  | s | 0 |  |
| Gap Pattern Id |  |  | 0 |  |
| Measurement gap offset |  |  | 9 |  |
| A3-Offset in condition |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 1 |  |
| T2 |  | s | 12 |  |

Table A.14.2.1.6.2-3: Cell specific test parameters for Inter-frequency SAN distance-based conditional handover from FR1 to FR1

| Parameter |  | Test configuration | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | Config 1 |  | SSC.1 |  | NSC.1 |  |
|  |  | Config 2 |  | SSC.2 |  | NSC.2 |  |
| NR RF Channel Number |  | Config 1, 2 |  | 1 |  | 2 |  |
| BWchannel |  |  | MHz | 10: NPRB,c = 52 |  | 10: NPRB,c = 52 |  |
| BWP BW |  |  | MHz | 10: NPRB,c = 52 |  | 10: NPRB,c = 52 |  |
| DRX Cycle |  | Config 1, 2 | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 FDD |  |  |  |
| CORESET Reference Channel |  |  |  | CR.1.1 FDD |  |  |  |
| TRS configuration |  |  |  | TRS.1.1 FDD |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SMTC Configuration |  |  |  | SMTC.2 |  | SMTC.5 |  |
| SSB Configuration |  |  |  | SSB.1 FR1 |  | SSB.5 FR1 |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 |  |  |  |
| BWP configuration | Initial DL BWP | Config 1, 2 |  | DLBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  | Config 1, 2 | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | Config 1, 2 | dBm/ 15 kHz | -98 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/ SCS | -98 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 4 | 4 | -Infinity | 9 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4 | 4 | -Infinity | 9 |
| SSB_RP |  |  | dBm/ SCS | -94 | -94 | -Infinity | -89 |
| IoNote3 |  |  | dBm/ 9.36 MHz | -64.59 | -64.59 | -70.05 | -60.53 |
| Propagation condition |  |  | - | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |

##### A.14.2.1.6.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 later than 11670ms and less than 11742 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay is defined in clause 6.1C.2, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

UE moving speed, v = (108km/h*1000/3600) = 30m/s.

At 11670 ms after start of T2,

distance to source cell reference location is 30 m/s * 11.67 s – (-700)m = 1050m, and D1-1 = 1000m

distance to target cell reference location is 30 m/s * 11.67 s – 1300m = -950m, and D1-2 = 1000m

i.e. D1-1 and D1-2 conditions are fulfilled at T2 + 11670 ms with >=50m location margin.

Tmeasure = max(600 + 200 ms, 11670 ms) = 11670 ms;

Tinterrupt = 62 ms; TCHO_execution = 10 ms.

This gives a total of 11670ms + 62ms + 10ms = 11742 ms.

#### A.14.2.1.7 Intra-frequency intra-satellite Handover from FR2-NTN to FR2-NTN

##### A.14.2.1.7.1 Test Purpose and Environment

This test is to verify the requirement for intra-frequency intra-satellite handover from FR2-NTN to FR2-NTN specified in clause 6.1C.3.

##### A.14.2.1.7.2 Test Parameters

The test scenario comprises of one NR FDD carrier and 2 cells as given in table A.14.2.1.7.2-1, A.14.2.1.7.2-2, and A.14.2.1.7.2-3. Both handover delay and interruption length are tested.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure intra-frequency neighbour cell with Event A3 report. Starting T2, Cell 2 becomes detectable and offset better than Cell 1. The RRC message implying handover to Cell 2 shall be sent to the UE during period T2, after the UE has reported Event A3. The start of T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.14.2.1.7.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 120 kHz SSB SCS, 100 MHz BW |
| 2 | NGSO, NR FDD, 120 kHz SSB SCS, 100 MHz BW |
| 3 | GSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.1.7.2-2: General test parameters Intra-frequency intra-satellite handover from FR2-NTN to FR2-NTN

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 | One NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 |  |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) |  |  | (0, 0, 0) | Set by any pre-configured means(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| A3-Offset |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 0 s | Synchronous cells belonging to the same satellite |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |
| T3 |  | s | 1 |  |

Table A.14.2.1.7.2-3: Cell specific test parameters for intra-frequency intra-satellite handover from FR2-NTN to FR2-NTN

| Parameter |  | Test configuration | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | Config 1 |  | SSC.1 |  |  | NSC.1 |  |  |
|  |  | Config 2 |  | SSC.2 |  |  | NSC.2 |  |  |
|  |  | Config 3 |  | SSC.1 |  |  | NSC.1 |  |  |
|  |  | Config 4 |  | SSC.2 |  |  | NSC.2 |  |  |
| Assumption for UE beamsNote4 |  |  |  | Rough |  |  | Rough |  |  |
| AoA setup |  |  |  | Setup 1 as defined in A.3.15 |  |  |  |  |  |
| NR RF Channel Number |  | Config 1,2 |  | 1 |  |  | 1 |  |  |
| Duplex mode |  |  |  | FDD |  |  |  |  |  |
| BWchannel |  | Config 1,2 | MHz | 100: NPRB,c = 66 |  |  | 100: NPRB,c = 66 |  |  |
|  |  | Config 3,4 | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |  |  |
| BWP BW |  | Config 1,2 | MHz | 100: NPRB,c = 66 |  |  | 100: NPRB,c = 66 |  |  |
|  |  | Config 3,4 | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |  |  |
| Data PRBs allocated |  | Config 1,2 |  | 66 |  |  |  |  |  |
|  |  | Config 3,4 |  |  |  |  |  |  |  |
| TACommon |  | Config 1,2,3,4 | s | 0 |  |  | 0 |  |  |
| TACommonDrift |  |  | s | 0 |  |  | 0 |  |  |
| TACommonDriftVariation |  |  | s | 0 |  |  | 0 |  |  |
| Koffset |  | Config 1,3 | ms | 239 |  |  | 239 |  |  |
|  |  | Config 2,4 |  | 4 |  |  | 4 |  |  |
| Kmac |  | Config 1,2,3,4 | ms | 0 |  |  | 0 |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |  |
| PDSCH Reference measurement channel |  | Config 1,2 |  | SR3.1 TDD |  |  |  |  |  |
|  |  | Config 3,4 |  | SR.2.1 TDD |  |  |  |  |  |
| CORESET Reference Channel |  | Config 1,2 |  | CR3.1 TDD |  |  |  |  |  |
|  |  | Config 3,4 |  | CCR.2.1 TDD |  |  |  |  |  |
| TRS configuration |  | Config 1,2 |  | TRS.2.1 TDD |  |  |  |  |  |
|  |  | Config 3,4 |  | TRS.1.2 TDD |  |  |  |  |  |
| OCNG Patterns |  | Config 1,2,3,4 |  | OP.1 |  |  |  |  |  |
| SMTC Configuration |  | Config 1,2,3,4 |  | SMTC.1 |  |  |  |  |  |
| SSB Configuration |  | Config 1,2 |  | SSB. 3 FR2 |  |  |  |  |  |
|  |  | Config 3,4 |  | SSB.1 FR1 |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 | kHz | 120 |  |  |  |  |  |
|  |  | Config 3,4 |  | 15 |  |  |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1,2 |  | 120 |  |  |  |  |  |
|  |  | Config 3,4 |  | 15 |  |  |  |  |  |
| PRACH configuration |  | Config 1,2 |  | FR2 PRACH configuration 1 |  |  |  |  |  |
|  |  | Config 3,4 |  | FR1 PRACH Configuration 1 |  |  |  |  |  |
| BWP configuration | Initial DL BWP | Config 1,2,3,4 |  | DLBWP.0.1 |  |  |  |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | Config 1,2,3,4 | dB | 0 |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | Config 1,2,3,4 | dBm/ 15 kHz | -104.7 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/ SCS | -95.7 |  |  |  |  |  |
| ![](media_svg/image10.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 6 | -1.8 | -1.8 | -Infinity | 0 | 0 |
| ![](media_svg/image11.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 6 | 6 | 6 | -Infinity | 7 | 7 |
| IoNote3 |  |  | dBm/ 9.36 MHz | -59.7 | -56.7 | -56.7 | -61.41 | -59.7 | -56.7 |
| Propagation condition |  |  | - | AWGN |  |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in [B.2.1.3], and does not limit UE implementation or test system implementation. |  |  |  |  |  |  |  |  |  |

##### A.14.2.1.7.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 no later than 72 ms from the beginning of T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2]. Tinterrupt is defined in clause 6.1C.1.3.2.

Tinterrupt_inter_sat = Tsearch + TIU + Tprocessing  + Tsat_beam + T∆ + Tmargin ms

Here: Tsearch = 0; TIU = 20 ms; Tprocessing = 20 ms; Tsat_beam = 0; T∆ = 20 ms; Tmargin = 2 ms.

This gives a total of 72 ms.

#### A.14.2.1.8 Intra-frequency SAN Handover from FR1 to FR1

##### A.14.2.1.8.1 Test Purpose and Environment

This test is to verify the requirement for Intra-frequency SAN RACH-less Handover from FR1 to FR1 specified in clause 6.1C.1.1.

##### A.14.2.1.8.2 Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells as given in table A.14.2.1.8.2-1, A.14.2.1.8.2-2, and A.14.2.1.8.2-3. Both handover delay and interruption length are tested.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure intra-frequency neighbour cell with Event A3 report.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1. The RRC message implying handover to Cell 2 shall be sent to the UE during period T2, after the UE has reported Event A3. The start of T3 is defined as the end of the last TTI containing the RRC message implying handover. During T3, Cell 2 continuously schedules PUSCH for the UE.

Table A.14.2.1.8.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.1.8.2-2: General test parameters Intra-frequency SAN handover from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 | One NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 |  |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) |  |  | (0, 0, 0) | Set by any pre-configured means(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| A3-Offset |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |
| T3 |  | s | 1 |  |

Table A.14.2.1.8.2-3: Cell specific test parameters for Intra frequency SAN handover test case

| Parameter |  | Test configuration | Unit | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | Config 1 |  | SSC.1 |  |  | NSC.1 |  |  |
|  |  | Config 2 |  | SSC.2 |  |  | NSC.2 |  |  |
| NR RF Channel Number |  | Config 1,2 |  | 1 |  |  | 1 |  |  |
| BWchannel |  |  | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |  |  |
| BWP BW |  |  | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |  |  |
| TACommon |  | Config 1,2 | s | 0 |  |  | 0 |  |  |
| TACommonDrift |  |  | s | 0 |  |  | 0 |  |  |
| TACommonDriftVariation |  |  | s | 0 |  |  | 0 |  |  |
| Koffset |  | Config 1 | ms | 258 |  |  | 258 |  |  |
|  |  | Config 2 |  | 14 |  |  | 14 |  |  |
| Kmac |  | Config 1,2 | ms | 0 |  |  | 0 |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 FDD |  |  |  |  |  |
| CORESET Reference Channel |  |  |  | CR.1.1 FDD |  |  |  |  |  |
| TRS configuration |  |  |  | TRS.1.1 FDD |  |  |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |  |  |
| SSB Configuration |  |  |  | SSB.1 FR1 |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |  |  |
| BWP configuration | Initial DL BWP | Config 1,2 |  | DLBWP.0.1 |  |  |  |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | Config 1,2 | dB | 0 |  |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | Config 1,2 | dBm/ 15 kHz | -98 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/ SCS | -98 |  |  |  |  |  |
| ![](media_svg/image10.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 8 | -3.3 | -3.3 | -Infinity | 2.36 | 2.36 |
| ![](media_svg/image11.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 8 | 8 | 8 | -Infinity | 11 | 11 |
| SSB_RP |  |  | dBm/ SCS | -90 | -90 | -90 | -Infinity | -87 | -87 |
| IoNote3 |  |  | dBm/ 9.36 MHz | -61.41 | -57.06 | -57.06 | -61.41 | -57.06 | -57.06 |
| Propagation condition |  |  | - | AWGN |  |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |  |

##### A.14.2.1.8.3 Test Requirements

The UE shall start to transmit the PUSCH to Cell 2 less than 52 + TIU ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2]. Tinterrupt is defined in clause 6.1C.1.2.2.2.

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin ms

Here: Tsearch = 0; TIU is the interruption uncertainty in acquiring the first UL transmission resource for PUSCH, which is scheduled by Cell 2 at the fist DL slot not earlier than 52 ms after the beginning of T3; Tprocessing = 20 ms; T∆ = 20 ms; Tmargin = 2 ms.

This gives a total of 52 + TIU ms.

#### A.14.2.1.9 Intra-frequency inter-satellite handover from FR2-NTN to FR2-NTN

##### A.14.2.1.9.1 Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NTN – NR FR2-NTN intra-frequency handover requirements specified in clause6.1C.1.3.

##### A.14.2.1.9.2 Test Parameters

The test consists two sub-tests. Sub-test 1 is applicable for UE indicating ‘electronic’ via ntn-VSAT-AntennaType-r18, and sub-test 2 is applicable for UE indicating ‘mechanical’ via ntn-VSAT-AntennaType-r18. The test configurations are same for the two sub-tests unless specified otherwise.

Supported test configurations are shown in table A.14.2.1.9.2-1. Both handover delay and interruption length are tested by using the parameters in table A.14.2.1.9.2-2, and A.14.2.1.9.2-3.

The test scenario comprises of one carrier and two cells on the carrier. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network to handover from Cell 1 to Cell 2. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.14.2.1.9.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 120 kHz SSB SCS, 100 MHz BW |
| 2 | NGSO, NR FDD, 120 kHz SSB SCS, 100 MHz BW |
| 3 | GSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.1.9.2-2: General test parameters

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 |  |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B,H) |  |  | (0, 0, 0) | Set by any pre-configured means(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| A3-Offset |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Time offset between cells |  | s | 3 | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 1 for sub-test 1TBD for sub-test 2 |  |

Table A.14.2.1.9.2-3: Cell specific test parameters for NR FR2-FR2 Intra frequency handover test case

| Parameter |  | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| AoA setup |  |  | Setup X1 for sub-test 1Setup X2 for sub-test 1 |  |  |  |
| Satellite information | Config 1,3 |  | SSC.1 |  | NSC.1 |  |
|  | Config 2,4 |  | SSC.2 |  | NSC.2 |  |
| NR RF Channel Number |  |  | 1 |  | 1 |  |
| Duplex mode |  |  | FDD |  |  |  |
| BWchannel |  | MHz | 100: NPRB,c = 66 (Config 1,2)10 NPRB,c = 24 (Config 3,4) |  |  |  |
| BWP BW |  | MHz | 100: NPRB,c = 66 (Config 1,2)10 NPRB,c = 24 (Config 3,4) |  |  |  |
| TACommon |  | s | 0 |  |  |  |
| TACommonDrift |  | s | 0 |  |  |  |
| TACommonDriftVariation |  | s | 0 |  |  |  |
| Koffset | Config 1,3 | ms | 239 |  |  |  |
|  | Config 2,4 | ms | 4 |  |  |  |
| Kmac |  | ms | 0 |  |  |  |
| Data PRBs allocated |  |  | 66 |  |  |  |
| DRX Cycle |  | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  |  | SR3.1 FDD (Config 1,2)SR.2.1 TDD (Config 3,4) |  |  |  |
| RMSI CORESET Reference Channel |  |  | CR3.1 FDD (Config 1,2)CR.2.1 TDD (Config 3,4) |  |  |  |
| Control Channel RMC |  |  | CCR.3.1 FDDCCR.2.1 TDD |  |  |  |
| OCNG Patterns |  |  | OP.1 |  |  |  |
| SMTC Configuration |  |  | SMTC.1 |  |  |  |
| SSB Configuration |  |  | SSB.3 FR2 (Config 1,2)SSB.1 FR1 (Config 3,4) |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 120 kHz (Config 1,2)30 kHz (Config 3,4) |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  | kHz | 120 kHz (Config 1,2)30 kHz (Config 3,4) |  |  |  |
| PRACH configuration |  |  | FR2 PRACH configuration 1 (Config 1,2)FR1 PRACH Configuration 1 (Config 3,4) |  |  |  |
| TRS configuration |  |  | TRS.2.1 TDD (Config 1,2)TRS 1.2 TDD (Config 3,4) |  |  |  |
| PDSCH/PDCCH TCI state |  |  | TCI.State.2 (Config 1,2) |  |  |  |
| BWP configuraiton | Initial DL BWP |  | DLBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |
|  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |
|  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | -104.7 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | -95.7 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 6 | -1.8 | -Infinity | 0 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 6 | 6 | -Infinity | 7 |
| IoNote3 |  | dBm/BW | -59.7 | -56.7 | -59.7 | -56.7 |
| Propagation condition |  | - | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the centre of the quiet zone |  |  |  |  |  |  |

##### A.14.2.1.9.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than X ms from the beginning of time period T2.

X = 152 ms for sub-test 1, and

X = TBD ms for sub-test 2, and

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 142 ms in sub-test 1 and TBD in sub-test 2. Tinterrupt is defined in clause 6.1C.1.3.2.

This gives a total of 152 ms sub-test 1 and TBD in sub-test 2.

##### A.14.2.1.10 Intra-frequency SAN Handover from FR1 to FR1 for UE operating on a cell with less than 5 MHz BWA.14.2.1.10.1 Test Purpose and Environment

This test is to verify the requirement for NR FR1 NTN- NR FR1 NTN intra-frequency SAN handover requirements for unknown target cell operating with 12 PRB SSB bandwidth specified in clause 6.1C.1.

##### A.14.2.1.10.2 Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells as given in table A.14.2.1.10.2-1, A.14.2.1.10.2-2, and A.14.X.1.1.2-3. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1, UE receives a RRC handover command from the network. The start of T2 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.14.2.1.10.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 3 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 3 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.1.10.2-2: General test parameters Intra-frequency SAN handover from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 | One NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 |  |
|  | Neighbouring cell |  | Cell 2 | Unknown target cell operating with 12PRB SSB bandwidth |
| Final condition | Active cell |  | Cell 2 | Unknown target cell operating with 12PRB SSB bandwidth |
| UE position (N,S, H) |  |  | (0, 0, 0) | Set by any pre-configured means |
| A3-Offset |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |

Table A.14.2.1.10.2-3: Cell specific test parameters for Intra frequency SAN handover test case

| Parameter |  | Test configuration | Unit | Cell 1 |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 |  | T2 |
| Satellite information |  | Config 1 |  | SSC.1 |  | NSC.1 |  |  |
|  |  | Config 2 |  | SSC.2 |  | NSC.2 |  |  |
| NR RF Channel Number |  | Config 1,2 |  | 1 |  | 1 |  |  |
| BWchannel |  |  | MHz | 3: NPRB,c = 15 |  | 3: NPRB,c = 15 |  |  |
| BWP BW |  |  | MHz | 3: NPRB,c = 15 |  | 3: NPRB,c = 15 |  |  |
| TACommon |  | Config 1,2 | s | 0 |  | 0 |  |  |
| TACommonDrift |  |  | s | 0 |  | 0 |  |  |
| TACommonDriftVariation |  |  | s | 0 |  | 0 |  |  |
| Koffset |  | Config 1 | ms | 239 |  | 239 |  |  |
|  |  | Config 2 |  | 4 |  | 4 |  |  |
| Kmac |  | Config 1,2 | ms | 0 |  | 0 |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.3 FDD |  |  |  |  |
| CORESET Reference Channel |  |  |  | CR.1.2 FDD |  |  |  |  |
| TRS configuration |  |  |  | TRS.1.1 FDD |  |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |  |
| SSB Configuration |  |  |  | SSB.13 FR1 |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 |  |  |  |  |
| BWP configuration | Initial DL BWP | Config 1,2 |  | DLBWP.0.1 |  |  |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |  |
| EPRE ratio of PSS to SSS |  | Config 1,2 | dB | 0 |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | Config 1,2 | dBm/ 15 kHz | -98 |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/ SCS | -98 |  |  |  |  |
| ![](media_svg/image10.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 8 | -3.3 | 2.36 | 2.36 |  |
| ![](media_svg/image11.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 8 | 8 | 11 | 11 |  |
| SSB_RP |  |  | dBm/ SCS | -90 | -90 | -87 | -87 |  |
| IoNote3 |  |  | dBm/ 2.7 MHz | - 62.46 | -62.46 | -62.46 | -62.46 |  |
| Propagation condition |  |  | - | AWGN |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

##### A.14.2.1.10.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 132 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2]. Tinterrupt is defined in clause 6.1C.1.2.2.

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin ms

Here: Tsearch = 20ms; TIU = 20 ms; Tprocessing = 20 ms; T∆ = 60 ms; Tmargin = 2 ms.

This gives a total of 132 ms.

#### A.14.2.1.11 Intra-frequency SAN time-based conditional Handover from FR1 to FR1 for UE operating on a cell with less than 5 MHz BW

##### A.14.2.11.1 Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN time-based conditional handover from FR1 to FR1 specified in clause 6.1C.2.2.

##### A.14.2.11.2 Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells as given in table A.14.2. 11.2-1, and A.14.2.1.11.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. Immediately before the start of T1, the UE is configured to measure intra-frequency neighbour cell with a time-based handover trigger to Cell 2 with Event CondEvent T1 shall be sent to UE.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and time condition event CondEvent T1 is fulfilled.

Table A.14.2. 11.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 3 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 3 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.1.11.2-2: General test parameters for Intra-frequency SAN time-based conditional handover from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 | One NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 | FDD duplex mode cell |
|  | Neighbouring cell |  | Cell 2 | FDD duplex mode cell |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (N,S, H) |  |  | (0, 0, 0) | Set by any pre-configured means |
| t1-Threshold-r17.condEventT1-r17 |  | s | T1 | Entering condition at start of T2 (end of T1) |
| duration-r17.condEventT1-r17 |  | slot | 1000 | Give 1 s search duration |
| A3-Offset in condition |  | dB | 0 |  |
| Hysteresis |  | dB | 0 |  |
| Time To Trigger |  | s | 0 |  |
| Filter coefficient |  |  | 0 | L3 filtering is not used |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 2 |  |

Table A.14.2. 11.2-3: Cell specific test parameters for Intra-frequency SAN time-based conditional handover from FR1 to FR1

| Parameter |  | Test configuration | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | Config 1 |  | SSC.1 |  | NSC.1 |  |
|  |  | Config 2 |  | SSC.2 |  | NSC.2 |  |
| NR RF Channel Number |  | Config 1,2 |  | 1 |  | 1 |  |
| BWchannel |  |  | MHz | 3: NPRB,c = 15 |  | 3: NPRB,c = 15 |  |
| BWP BW |  |  | MHz | 3: NPRB,c = 15 |  | 3: NPRB,c = 15 |  |
| TACommon |  | Config 1,2 | s | 0 |  | 0 |  |
| TACommonDrift |  |  | s | 0 |  | 0 |  |
| TACommonDriftVariation |  |  | s | 0 |  | 0 |  |
| Koffset |  | Config 1 | ms | 239 |  | 239 |  |
|  |  | Config 2 | ms | 4 |  | 4 |  |
| Kmac |  | Config 1,2 | ms | 0 |  | 0 |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.2 FDD |  |  |  |
| CORESET Reference Channel |  |  |  | CR.1.3 FDD |  |  |  |
| TRS configuration |  |  |  | TRS.1.1 FDD |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |
| SSB Configuration |  |  |  | SSB.13 FR1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 |  |  |  |
| BWP configuration | Initial DL BWP | Config 1,2 |  | DLBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  | Config 1,2 | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | Config 1,2 | dBm/ 15 kHz | -98 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/ SCS | -98 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 8 | -3.3 | -Infinity | 2.36 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 8 | 8 | -Infinity | 11 |
| SSB_RP |  |  | dBm/ SCS | -90 | -90 | -Infinity | -87 |
| IoNote3 |  |  | dBm/ 2.7 MHz | -66.81 | -62.46 | -66.81 | -62.46 |
| Propagation condition |  |  | - | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |

##### A.14.2.11.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 892 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay is defined in clause 6.1C.2, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

Tmeasure = 600 + 200 ms; Tinterrupt = 82 ms; TCHO_execution = 10 ms.

This gives a total of 892 ms.

### A.14.2.2 RRC Connection Mobility Control

#### A.14.2.2.1 SA: RRC Re-establishment for SAN

##### A.14.2.2.1.1 Intra-frequency RRC Re-establishment in FR1

A.14.2.2.1.1.1 Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR1 with known target cell is within the specified limits. These tests will verify the requirements in clause 6.2C.1.

The test parameters are given in table A.14.2.2.1.1.1-1, table A.14.2.2.1.1.1-2 and table A.14.2.2.1.1.1-3  below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.2.2.1.1.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.2.1.1.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR1

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2 | Cell 1 |  |
|  | Neighbour cells |  | 1, 2 | Cell 2 |  |
| Final condition | Active cell |  | 1, 2 | Cell 2 |  |
| RF Channel Number |  |  | 1, 2 | 1 |  |
| Time offset between cells |  |  | 1 | 3 ms | Asynchronous cells |
| N310 |  | - | 1, 2 | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1, 2 | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 1, 2 | 0 | Radio link failure timer; |
| T311 |  | ms | 1, 2 | 3000 | RRC re-establishment timer |
| Access Barring Information |  | - | 1, 2 | Not Sent | No additional delays in random access procedure. |
| SMTC configuration |  |  | 1, 2 | SMTC.2 |  |
| DRX cycle length |  | s | 1, 2 | OFF |  |
| PRACH configuration |  |  | 1, 2 | FR1 PRACH configuration 1 | Table A.3.8.2.1-1 |
| T1 |  | s | 1, 2 | 5 |  |
| T2 |  | ms | 1, 2 | 240 | Time for the UE to detect RLF(Summation of TEvaluate_out_SSB defined in clause 8.1C in TS 38.133, T310 and the period for UE turns off transmitter defined in clause 8.1C.5 in TS 38.133 ) |
| T3 |  | s | 1, 2 | 2 |  |

Table A.14.2.2.1.1.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR1

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | 1 | SSC.1 |  |  | NSC.1 |  |  |
|  |  | 2 | SSC.2 |  |  | NSC.2 |  |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |
| OCNG Pattern |  | 1, 2 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| TRS configuration |  | 1, 2 | TRS.1.1 FDD |  |  | TRS.1.1 FDD |  |  |
| Initial DL BWP configuration |  | 1, 2 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Active DL BWP confgiuration |  | 1, 2 | DLBWP.1.1 | N/A | N/A | N/A | N/A | DLBWP.1.1 |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.1 | N/A | N/A | N/A | N/A | ULBWP.1.1 |
| SSB configuration |  | 1, 2 | SSB.1 FR1 |  |  | SSB.1 FR1 |  |  |
| RLM-RS |  | 1, 2 | SSB |  |  | SSB |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2 | 1.54 | -infinity | -infinity | -3.79 | 4 | 4 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1, 2 | -98 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 2 | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2 | 7 | -infinity | -infinity | 4 | 4 | 4 |
| SS-RSRP Note3 | dBm/SCS | 1, 2 | -91 | -infinity | -infinity | -94 | -94 | -94 |
| Io | dBm/9.36 MHz | 1, 2 | -60.74 | -64.59 | -64.59 | -60.74 | -64.59 | -64.59 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

A.14.2.2.1.1.2 Test Requirements

The RRC re-establishment delay is defined as the time from the moment UE declares RLF, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

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

TPRACH = 15 ms; it is the additional delay caused by the random access procedure, allow 1840 ms (240 ms + 1.6 s) from the beginning of T2 in the test case.

This gives a total of 1545 ms, allow 1.6 s in the test case.

##### A.14.2.2.1.2 Inter-frequency RRC Re-establishment in FR1

A.14.2.2.1.2.1 Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR1 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2C.1.

The test parameters are given in table A.14.2.2.1.2.1-1, table A.14.2.2.1.2.1-2 and table A.14.2.2.1.2.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.2.2.1.2.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.2.1.2.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2 | Cell 1 |  |
|  | Neighbour cells |  | 1, 2 | Cell 2 |  |
| Final condition | Active cell |  | 1, 2 | Cell 2 |  |
| RF Channel Number |  |  | 1, 2 | 1, 2 |  |
| Time offset between cells |  |  | 1, 2 | 3 ms | Asynchronous cells |
| N310 |  | - | 1, 2 | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1, 2 | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 1, 2 | 0 | Radio link failure timer; |
| T311 |  | ms | 1, 2 | 5000 | RRC re-establishment timer |
| Access Barring Information |  | - | 1, 2 | Not Sent | No additional delays in random access procedure. |
| SMTC configuration |  |  | 1, 2 | SMTC.2 |  |
| DRX cycle length |  | s | 1, 2 | OFF |  |
| PRACH configuration |  |  | 1, 2 | FR1 PRACH configuration 1 | Table A.3.8.2.1-1 |
| T1 |  | s | 1, 2 | 5 |  |
| T2 |  | ms | 1, 2 | 240 | Time for the UE to detect RLF(Summation of TEvaluate_out_SSB defined in clause 8.1C in TS 38.133, T310 and the period for UE turns off transmitter defined in clause 8.1C.5 in TS 38.133 ) |
| T3 |  | s | 1, 2 | 5 |  |

Table A.14.2.2.1.2.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | 1 | SSC.1 |  |  | NSC.1 |  |  |
|  |  | 2 | SSC.2 |  |  | NSC.2 |  |  |
| RF Channel Number |  | 1, 2 | 1 |  |  | 2 |  |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |
| OCNG Pattern |  | 1, 2 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| TRS configuration |  | 1, 2 | TRS.1.1 FDD |  |  | TRS.1.1 FDD |  |  |
| Initial DL BWP configuration |  | 1, 2 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Active DL BWP configuration |  | 1, 2 | DLBWP.1.1 | N/A | N/A | N/A | N/A | DLBWP.1.1 |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.1 | N/A | N/A | N/A | N/A | ULBWP.1.1 |
| SSB configuration |  | 1, 2 | SSB.1 FR1 |  |  | SSB.1 FR1 |  |  |
| RLM-RS |  | 1, 2 | SSB |  |  | SSB |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2 | 4 | -infinity | -infinity | -infinity | -infinity | 7 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1, 2 | -98 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 2 | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2 | 4 | -infinity | -infinity | -infinity | -infinity | 7 |
| SS-RSRP Note3 | dBm/SCS | 1, 2 | -94 | -infinity | -infinity | -infinity | -infinity | -91 |
| Io | dBm/9.36 MHz | 1, 2 | -64.59 | -70. 05 | -70. 05 | -70. 05 | -70. 05 | -62.26 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

A.14.2.2.1.2.2 Test Requirements

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

##### A.14.2.2.1.3 Inter-frequency RRC Re-establishment in FR1 with 160ms SSB periodicity

A.14.2.2.1.3.1 Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR1 without known target cell is within the specified limits, where the SSB periodicity of the target cell is 160ms. The test will verify the requirements in clause 6.2C.1.

The test parameters are given in table A.14.2.2.1.3.1-1, table A.14.2.2.1.3.1-2 and table A.14.2.2.1.3.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.2.2.1.3.1-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.2.1.3.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1

| Parameter |  | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- | --- |
| Initial condition | Active cell |  | 1, 2 | Cell 1 |  |
|  | Neighbour cells |  | 1, 2 | Cell 2 |  |
| Final condition | Active cell |  | 1, 2 | Cell 2 |  |
| RF Channel Number |  |  | 1, 2 | 1, 2 |  |
| Time offset between cells |  |  | 1, 2 | 3 ms | Asynchronous cells |
| N310 |  | - | 1, 2 | 1 | Maximum consecutive out-of-sync indications from lower layers |
| N311 |  | - | 1, 2 | 1 | Minimum consecutive in-sync indications from lower layers |
| T310 |  | ms | 1, 2 | 0 | Radio link failure timer; |
| T311 |  | ms | 1, 2 | 5000 | RRC re-establishment timer |
| Access Barring Information |  | - | 1, 2 | Not Sent | No additional delays in random access procedure. |
| SMTC configuration |  |  | 1, 2 | SMTC.2 SMTC.3 | SMTC.2 for RF Channel Number #1SMTC.3 for RF Channel Number #2 |
| DRX cycle length |  | s | 1, 2 | OFF |  |
| PRACH configuration |  |  | 1, 2 | FR1 PRACH configuration 1 | Table A.3.8.2.1-1 |
| T1 |  | s | 1, 2 | 5 |  |
| T2 |  | ms | 1, 2 | 640 | Time for the UE to detect RLF(Summation of TEvaluate_out_SSB defined in clause 8.1C in TS 38.133, T310 and the period for UE turns off transmitter defined in clause 8.1C.5 in TS 38.133 ) |
| T3 |  | s | 1, 2 | 6 |  |

Table A.14.2.2.1.3.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1

| Parameter | Unit | Test configuration | Cell 1 |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite information |  | 1 | SSC.1 |  |  | NSC.1 |  |  |
|  |  | 2 | SSC.2 |  |  | NSC.2 |  |  |
| RF Channel Number |  | 1, 2 | 1 |  |  | 2 |  |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 FDD |  |  | SR.1.1 FDD |  |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CR.1.1 FDD |  |  | CR.1.1 FDD |  |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | CCR.1.1 FDD |  |  | CCR.1.1 FDD |  |  |
| OCNG Pattern |  | 1, 2 | OP.1 defined in A.3.2.1 |  |  | OP.1 defined in A.3.2.1 |  |  |
| TRS configuration |  | 1, 2 | TRS.1.1 FDD |  |  | TRS.1.1 FDD |  |  |
| Initial DL BWP configuration |  | 1, 2 | DLBWP.0.1 |  |  | DLBWP.0.1 |  |  |
| Initial UL BWP configuration |  | 1, 2 | ULBWP.0.1 |  |  | ULBWP.0.1 |  |  |
| Active DL BWP confgiuration |  | 1, 2 | DLBWP.1.1 | N/A | N/A | N/A | N/A | DLBWP.1.1 |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.1 | N/A | N/A | N/A | N/A | ULBWP.1.1 |
| SSB configuration |  | 1, 2 | SSB.1 FR1 |  |  | SSB.14 FR1 |  |  |
| RLM-RS |  | 1, 2 | SSB |  |  | SSB |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 1, 2 | 4 | -infinity | -infinity | -infinity | -infinity | 7 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/SCS | 1, 2 | -98 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc] Note2 | dBm/15 kHz | 1, 2 | -98 |  |  |  |  |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 1, 2 | 4 | -infinity | -infinity | -infinity | -infinity | 7 |
| SS-RSRP Note3 | dBm/SCS | 1, 2 | -94 | -infinity | -infinity | -infinity | -infinity | -91 |
| Io | dBm/9.36 MHz | 1, 2 | -64.59 | -70. 05 | -70. 05 | -70. 05 | -70. 05 | -62.26 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |

A.14.2.2.1.3.2 Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell shall be less than 6 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE: The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

$ T_{UE\_re-establish\_delay}=50ms+T_{identify\_intra\_NR}+\sum  _{i=1}^{Nfreq-1}T_{identify\_inter\_NR,i}+T_{SI-NR}+T_{PRACH}$

Nfreq = 2

Tidentify_intra_NR = 800 ms

Tidentify_inter_NR = 3520 ms

TSI = 1280 ms, provided that SIB1 and SIB19 are scheduled with 160 ms period; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 5665 ms, allow 6 s in the test case.

#### A.14.2.2.2 Random Access

##### A.14.2.2.2.1 4-step RA type contention based random access test in FR1 for NR standalone

###### A.14.2.2.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause6.2C.2.2 and clause7.1C.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.14.2.2.2.1.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.14.2.2.2.1.1-2.

Table A.14.2.2.2.1.1-1: Supported test configurations for contention based random access test for satellite access

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.2.2.1.1-2: General test parameters for contention based random access test for satellite access

| Parameter |  |  | Unit | Test-1 | Comments |
| --- | --- | --- | --- | --- | --- |
| SSB Configuration |  | Config 1 |  | SSB.1 FR1 | As defined in A.3.10, except for number of SSBs per SS-burst and SS/PBCH block index as below |
|  |  | Config 2 |  | SSB.1 FR1 |  |
| Number of SSBs per SS-burst |  |  |  | 2 | Different from the definition in A.3.10 |
| SS/PBCH block index |  |  |  | 0,1 | Different from the definition in A.3.10 |
| Duplex Mode for Cell 1 |  | Config 1 |  | FDD |  |
|  |  | Config 2 |  | FDD |  |
| CSI-RS for tracking |  | Config 1, 2 |  | TRS.1.1 FDD |  |
| OCNG Pattern Note 1 |  |  |  | OP.1 | As defined in A.3.2.1. |
| PDSCH parameters Note 4 |  | Config 1, 2 |  | SR.1.1 FDD | As defined in A.3.1.1. |
| RMSI CORESET Reference Channel |  | Config 1, 2 |  | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1, 2 |  | CCR.1.1 FDD |  |
| NR RF Channel Number |  |  |  | 1 |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  | dB |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  | dB |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  | dB |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  | dB |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  | dB |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  | dB |  |  |
| SSB with index 0 | ![](media_svg/image12.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 3 | Power of SSB with index 0 is set to be above configured rsrp-ThresholdSSB |
|  | ![](media_svg/image1.svg) [公式≈: ^{N}oc] | Config 1, 2 | dBm/15 kHz | -98 |  |
|  | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 3 |  |
|  | SS-RSRP Note 3 |  | dBm/ SCS | -95 |  |
| SSB with index 1 | ![](media_svg/image12.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | -17 | Power of SSB with index 1 is set to be below configured rsrp-ThresholdSSB |
|  | ![](media_svg/image1.svg) [公式≈: ^{N}oc] | Config 1, 2 | dBm/15 kHz | -98 |  |
|  | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | -17 |  |
|  | SS-RSRP Note 3 |  | dBm/ SCS | -115 |  |
| Io Note 2 |  | Config 1, 2 | dBm | -65.3/9.36 MHz | For symbols without SSB index 1 |
| ss-PBCH-BlockPower |  |  | dBm/ SCS | -5 | As defined in clause 6.3.2 in TS 38.331 [2]. |
| Configured UE transmitted power (![](media_svg/image14.svg) [公式≈: ^{P}CMAX,f,c]) |  |  | dBm | 23 | As defined in clause 6.2.4 in TS 38.101-1. |
| PRACH Configuration |  |  |  | FR1 PRACH configuration 1 | As defined in A.3.8. |
| Propagation Condition |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters.NOTE 3: VoidNOTE 4: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required. |  |  |  |  |  |

###### A.14.2.2.2.1.2 Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.14.2.2.2.1.2.1 Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2C.2.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1C.2.

A.14.2.2.2.1.2.2 Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1C.2.

A.14.2.2.2.1.2.3 No Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1C.2.

A.14.2.2.2.1.2.4 Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2C.2.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

A.14.2.2.2.1.2.5 Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2C.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.14.2.2.2.1.2.6 Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2C.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.14.2.2.2.1.2.7 Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2C.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

##### A.14.2.2.2.2 4-step RA type non-contention based random access test in FR1 for NR standalone

###### A.14.2.2.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause6.2C.2.2 and clause7.1C.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.14.2.2.2.2.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.14.2.2.2.2.1-2 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2). Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

Table A.14.2.2.2.2.1-1: Supported test configurations for non-contention based random access test for satellite access

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.2.2.2.1-2: General test parameters for non-contention based random access test satellite access

| Parameter |  |  | Unit | Test-1 | Test-2 | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| SSB Configuration |  | Config 1 |  | SSB.1 FR1 | SSB.1 FR1 | As defined in A.3.10, except for number of SSBs per SS-burst and SS/PBCH block index as below |
|  |  | Config 2 |  | SSB.1 FR1 | SSB.1 FR1 |  |
| Number of SSBs per SS-burst |  |  |  | 2 | 2 | Different from the definition in A.3.10 |
| SS/PBCH block index |  |  |  | 0,1 | 0,1 | Different from the definition in A.3.10 |
| CSI-RS Configuration |  | Config 1, 2 |  | N/A | CSI-RS.1.1 FDD | As defined in A.3.1.4 |
| Duplex Mode for Cell 1 |  | Config 1, 2 |  | FDD | FDD |  |
| CSI-RS for tracking |  | Config 1, 2 |  | TRS.1.1 FDD | TRS.1.1 FDD |  |
| OCNG Pattern Note 1 |  |  |  | OP.1 | OP.1 | As defined in A.3.2.1. |
| PDSCH parameters Note 4 |  | Config 1, 2 |  | SR.1.1 FDD | SR.1.1 FDD | As defined in A.3.1.1. |
| RMSI CORESET Reference Channel |  | Config 1, 2 |  | CR.1.1 FDD | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1, 2 |  | CCR.1.1 FDD | CCR.1.1 FDD |  |
| NR RF Channel Number |  |  |  | 1 | 1 |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 |  |
| EPRE ratio of PBCH_DMRS to SSS |  |  | dB |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  | dB |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  | dB |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  | dB |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  | dB |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  | dB |  |  |  |
| SSB with index 0 | ![](media_svg/image12.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 3 | 3 | Power of SSB with index 0 is set to be above configured rsrp-ThresholdSSB |
|  | ![](media_svg/image1.svg) [公式≈: ^{N}oc] | Config 1, 2 | dBm/15 kHz | -98 | -98 |  |
|  | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 3 | 3 |  |
|  | SS-RSRP Note 3 |  | dBm/ SCS | -95 | -95 |  |
| SSB with index 1 | ![](media_svg/image12.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | -17 | -17 | Power of SSB with index 1 is set to be below configured rsrp-ThresholdSSB |
|  | ![](media_svg/image1.svg) [公式≈: ^{N}oc] | Config 1, 2 | dBm/15 kHz | -98 | -98 |  |
|  | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | -17 | -17 |  |
|  | SS-RSRP Note 3 |  | dBm/ SCS | -115 | -115 |  |
| Io Note 2 |  | Config 1, 2 | dBm | -65.3/9.36 MHz | -65.3/9.36 MHz | For symbols without SSB index 1 |
| ss-PBCH-BlockPower |  |  | dBm/ SCS | -5 | -5 | As defined in clause 6.3.2 in TS 38.331 [2]. |
| Configured UE transmitted power (![](media_svg/image14.svg) [公式≈: ^{P}CMAX,f,c]) |  |  | dBm | 23 | 23 | As defined in clause 6.2.4 in TS 38.101-1. |
| PRACH Configuration |  |  |  | FR1 PRACH configuration 2 | FR1 PRACH configuration 3 | As defined in A.3.8.2. |
| Propagation Condition |  |  | - | AWGN | AWGN |  |
| NOTE 1: OCNG shall be used such that the cell is fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. The OCNG pattern is chosen during the test according to the presence of a DL reference measurement channel.NOTE 2: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters.NOTE 3: VoidNOTE 4: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required. |  |  |  |  |  |  |

###### A.14.2.2.2.2.2 Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.14.2.2.2.2.2.1 SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2C.2.2.2.1 for SSB-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1C.2.

A.14.2.2.2.2.2.2 CSI-RS-based Random Access Preamble Transmission

In Test-2, to test the UE behavior specified in clause 6.2C.2.2.2.1 for CSI-RS-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with CSI-RSs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the CSI-RS configured.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the CSI-RS configured, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-OccasionList.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1C.2.

A.14.2.2.2.2.2.3 Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1C.2.

A.14.2.2.2.2.2.4 No Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1C.2.

#### A.14.2.2.3 RRC Connection Release with Redirection

##### A.14.2.2.3.1 Redirection from NR in FR1 to NR in FR1

###### A.14.2.2.3.1.1 Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements specified in clause 6.2C.3.2.1.

###### A.14.2.2.3.1.2 Test Parameters

Supported test configurations are shown in table A.14.2.2.3.1.2-1. The time delay is tested by using the parameters in table A.14.2.2.3.1.2-2, and A.14.2.2.3.1.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2. Cell 1 and Cell 2 belong to different tracking areas.

Table A.14.2.2.3.1.2-1: Redirection from NR to NR test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.2.2.3.1.2-2: General test parameters for Redirection from NR to NR test case

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

Table A.14.2.2.3.1.2-3: Cell specific test parameters for Redirection from NR to NR test case

| Parameter |  |  | Unit | Cell 1 |  |  |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 |  | T2 |  | T1 |  | T2 |
| Satellite information |  |  | Config 1 |  |  |  |  | SSC.1 |  |  |
|  |  |  | Config 2 |  |  |  |  | SSC.2 |  |  |
| NR RF Channel Number |  |  |  | 1 |  |  |  | 2 |  |  |
| Duplex mode |  | Config 1, 2 |  | FDD |  |  |  |  |  |  |
| SSB Configuration |  | Config 1, 2 |  | SSB.1 FR1 |  |  |  |  |  |  |
| CSI-RS for tracking |  | Config 1, 2 |  | TRS.1.1 FDD |  |  |  |  |  |  |
| BWchannel |  | Config 1 | MHz | 10: NRB,c = 52 |  |  |  |  |  |  |
|  |  | Config 2 |  | 10: NRB,c = 52 |  |  |  |  |  |  |
| BWP BW |  | Config 1 | MHz | 10: NRB,c = 52 |  |  |  |  |  |  |
|  |  | Config 2 |  | 10: NRB,c = 52 |  |  |  |  |  |  |
| DRx Cycle |  |  | ms | Not Applicable |  |  |  |  |  |  |
| PDSCH Reference measurement channel |  | Config 1, 2 |  | SR.1.1 FDD |  |  |  |  |  |  |
| CORESET Reference Channel |  | Config 1, 2 |  | CR.1.1 FDD |  |  |  |  |  |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |  |  |  |
| SMTC configuration |  | Config 1,2 |  | SMTC.1 FR1 |  |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 | kHz | 15 kHz |  |  |  |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1,2 | kHz | 15 kHz |  |  |  |  |  |  |
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
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/15kHz | -98 |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 |  | dBm/SCS | -98 |  |  |  |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 4 | 4 |  | -infinity |  | 4 |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4 | 4 |  | -infinity |  | 4 |  |
| IoNote3 | Config 1,2 |  | dBm/9.36MHz | -64.59 | -64.59 |  | -70.05 |  | -64.59 |  |
| Propagation condition |  |  | - | AWGN |  |  |  |  |  |  |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.Note 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.Note 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |  |  |  |

###### A.14.2.2.3.1.3 Test Requirements

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

#### A.14.2.2.4 RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1

##### A.14.2.2.4.1 Test Purpose and Environment

This test is to verify the requirement for RACH-based hard satellite switching with re-synchronization from SAN FR1 to SAN FR1 specified in clause 6.1C.3.

##### A.14.2.2.4.2 Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells with same PCI as given in table A.14.2.2.4.2-1, A.14.2.2.4.2-2, A.14.2.2.4.2-3 and A.14.2.2.4.2-4. Both satellite switching delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively.

At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, The SIB19 implying t-service-r17 and target satellite configuration SatSwitchWithReSync-r18 shall be sent to UE. The target satellite configuration is in table A.14.2.2.4.2-3.

At the start of time duration T2, Cell 2 becomes detectable and t-service-r17 of Cell 1 is fulfilled.

Table A.14.2.2.4.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |

Table A.14.2.2.4.2-2: General test parameters for RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 | One NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 |  |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) |  |  | (0, 0, 0) | Set by any pre-configured means.(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| Access Barring Information |  | - | Not barred | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |

Table A.14.2.2.4.2-3: Target Satellite configuration pattern for hard satellite switching scenario

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

Table A.14.2.2.4.2-4: Cell specific test parameters for RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 test case

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
| SMTC Configuration |  |  | SMTC.1 |  |  | SMTC.1 |
| SSB Configuration |  |  | SSB.1 FR1 |  |  | SSB.1 FR1 |
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
| ![](media_svg/image15.svg) [公式≈: ^{N}oc]Note3 |  | dBm/ 15 kHz | -98 |  |  |  |
| ![](media_svg/image15.svg) [公式≈: ^{N}oc]Note3 |  | dBm/ SCS | -98 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 8 | -Infinity | -Infinity | 8 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 8 | -Infinity | -Infinity | 8 |
| SSB_RP |  | dBm/ SCS | -90 | -Infinity | -Infinity | -90 |
| IoNote4 |  | dBm/ 9.36 MHz | -61.41 | -61.41 | -61.41 | -61.41 |
| Propagation condition |  | - | AWGN |  |  |  |
| NOTE 1: Cell 1 and Cell 2 have same PCI. Satellite serving for Cell 1 and Satellite serving for Cell 2 are two different NGSO satellites.NOTE 2: SSB transmit timing from TE should fit the SSB-timeOffset and the nominal propagation delay difference between serving satellite and target satellite. The nominal propagation delay is counted from the SSB-TimeOffset reference point to UE, which based on satellite locations and UE location known to the TE in this test case.NOTE 3: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image15.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 4: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 5: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |  |  |  |

##### A.14.2.2.4.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 52.5 ms from the beginning of time period T2.

The rate of correct satellite switch observed during repeated tests shall be at least 90 %.

NOTE: The hard satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tinterrupt, where:

Tinterrupt is defined in clause 6.1C.3.2.2.

Dswitch_unchangedPCI = Tinterrupt = Tsearch + Tprocessing  + T∆ + Tmargin ms

Here: Tsearch = Tfirst_SSB = 0.5ms; Tprocessing = 10ms; T∆ = 20ms; Tmargin = 2ms.

Besides, interruption uncertainty TIU = 20ms in acquiring the first PRACH transmission resource is needed.

This gives a total of 52.5 ms.

#### A.14.2.2.5 RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1

##### A.14.2.2.5.1 Test Purpose and Environment

This test is to verify the requirement for RACH-less soft satellite switching with re-synchronization from SAN FR1 to SAN FR1 specified in clause 6.1C.3.

##### A.14.2.2.5.2 Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells with same PCI as given in tables A.14.2.2.5.2-1, A.14.2.2.5.2-2, A.14.2.2.5.2-3 and A.14.2.2.5.2-4. Satellite switching delay is tested.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively.

At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, The SIB19 implying t-service-r17 and target satellite configuration SatSwitchWithReSync-r18 shall be sent to UE. The target satellite configuration is in table A.14.2.2.5.2-3. The configured grant PUSCH transmission in the Cell 2 is configured in the RRC message from Cell 1.

At the start of time duration T2, Cell 2 becomes detectable and t-ServiceStart-r18 is fulfilled.

At the start of time duration T3, t-service-r17 of Cell 1 is fulfilled.

Table A.14.2.2.5.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |

Table A.14.2.2.5.2-2: General test parameters for RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 | One NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 |  |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) |  |  | (0, 0, 0) | Set by any pre-configured means.(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| Access Barring Information |  | - | Not barred | No additional delays in random access procedure. |
| timeDomainOffset |  |  | 0 |  |
| timeDomainAllocation |  |  | 0 | PUSCH MappingType AstartSymbol S=0Length L=14 |
| timeReferenceSFN-r16 |  |  | sfn512 |  |
| Periodcity |  |  | sym10x14 |  |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | ms | 100 |  |
| T3 |  | s | 5 |  |

Table A.14.2.2.5.2-3: Target Satellite configuration pattern for soft satellite switching scenario

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

Table A.14.2.2.5.2-4: Cell specific test parameters for Inter frequency SAN handover test case

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
| SMTC Configuration |  |  | SMTC.1 |  |  |  | SMTC.5 |  |
| SSB Configuration |  |  | SSB.1 FR1 |  |  |  | SSB.5 FR1 |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 15 kHz |  |  |  | 15 kHz |  |
| PUCCH/PUSCH subcarrier spacing |  | kHz | 15 kHz |  |  |  | 15 kHz |  |
| PRACH configuration |  |  | FR1 PRACH configuration 1 |  |  |  | N/A |  |
| BWP configuration | Initial DL BWP |  | DLBWP.0.1 |  |  |  | DLBWP.0.1 |  |
|  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  | DLBWP.1.1 |  |
|  | Initial UL BWP |  | ULBWP.0.1 |  |  |  | ULBWP.0.1 |  |
|  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  | ULBWP.1.1 |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |  |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image15.svg) [公式≈: ^{N}oc]Note2 |  | dBm/ 15 kHz | -98 |  |  |  |  |  |
| ![](media_svg/image15.svg) [公式≈: ^{N}oc]Note2 |  | dBm/ SCS | -98 |  |  |  |  |  |
| ![](media_svg/image10.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 4 | 4 | -Infinity | -Infinity | 9 | 9 |
| ![](media_svg/image11.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 4 | 4 | -Infinity | -Infinity | 9 | 9 |
| SSB_RP |  | dBm/ SCS | -94 | -94 | -Infinity | -Infinity | -89 | -89 |
| IoNote3 |  | dBm/ 9.36 MHz | -64.59 | -64.59 | -70.05 | -70.05 | -60.53 | -60.53 |
| Propagation condition |  | - | AWGN |  |  |  |  |  |
| NOTE 1: Cell 1 and Cell 2 have same PCI. Satellite serving for Cell 1 and Satellite serving for Cell 2 are two different NGSO satellites.NOTE 2: SSB transmit timing from TE should fit the SSB-timeOffset and the nominal propagation delay difference between serving satellite and target satellite. The nominal propagation delay is counted from the SSB-TimeOffset reference point to UE, which based on satellite locations and UE location known to the TE in this test case.NOTE 3: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image15.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 4: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 5: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |  |  |  |  |  |

##### A.14.2.2.5.3 Test Requirements

The UE shall start to transmit the PUSCH to Cell 2 less than 130 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tsoft_switch, where:

Tsoft_switch = max(t-service-t-seviceStart, Tsearch + T∆ + Tmargin) + TIU + Tprocessing  ms

Here: t-service-t-seviceStart= 100ms; Tsearch = 10.5ms; T∆ = 20ms; Tmargin = 2ms, Tprocessing = 10ms.

Besides, interruption uncertainty TIU = 20ms in acquiring the first configured grant based PUSCH transmission resource is needed.

This gives a total of 130 ms.

#### A.14.2.2.6 RACH-based hard Satellite switching with re-synchronization from FR1 to FR1 for less than 5MHz with NTN

##### A.14.2.2.6.1 Test Purpose and Environment

This test is to verify the requirement for RACH-based hard satellite switching with re-synchronization from SAN FR1 to SAN FR1 for unknown target cell operating with 12 PRB SSB bandwidth specified in clause 6.1C.3.

##### A.14.2.2.6.2 Test Parameters

Supported test configurations are shown in table A.14.2.2.6.2-1. General test parameters as specified in table A.14.2.2.6.2-2 apply except those specified in table A.14.2.2.4.2-2. Target Satellite configuration pattern specified in table A.14.2.2.4.2-3 shall apply. Cell specific test parameters as specified in table A.14.2.2.6.2-4 apply except those specified in table A.14.2.2.4.2-4.

The test procedure specified in clause A.14.2.2.4.2 applies to this test. The Cell 2 is the unknown target cell operating with 12 PRB SSB bandwidth.

Table A.14.2.2.6.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, 15 kHz SSB SCS, 3 MHz BW |
| 2 | NGSO, NR FDD, 15 kHz SSB SCS, 3 MHz BW |

Table A.14.2.2.6.2-2: General test parameters for RACH-based hard Satellite switching with re-synchronization from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Initial conditions | Active cell |  | Cell 1 |  |
| Final condition | Active cell |  | Cell 2 | unknown target cell operating with 12 PRB SSB bandwidth |

Table A.14.2.2.6.2-3: Cell specific test parameters for RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 test case

| Parameter |  | Unit | Cell 1Note1 |  | Cell 2Note1 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |  |
| BWchannel | Config 1,2 | MHz | 3: NPRB,c = 15 |  |  | 3: NPRB,c = 15 |  |
| BWP BW |  | MHz | 3: NPRB,c = 15 |  |  | 3: NPRB,c = 15 |  |
| PDSCH Reference measurement channel |  |  | SR.1.2 FDD |  |  | SR.1.2 FDD |  |
| CORESET Reference Channel |  |  | CR.1.3 FDD |  |  | CR.1.3 FDD |  |
| SSB Configuration |  |  | SSB.13 FR1 |  |  | SSB.13 FR1 |  |
| IoNote1 | Config 1, 2 | dBm/2.7 MHz | -66.81 | -66.81 | -66.81 | -66.81 |  |
| NOTE 1: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |

##### A.14.2.2.6.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 52.5 ms from the beginning of time period T2.

The rate of correct satellite switch observed during repeated tests shall be at least 90 %.

NOTE: The hard satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tinterrupt, where:

Tinterrupt is defined in clause 6.1C.3.2.2.

Dswitch_unchangedPCI = Tinterrupt = Tsearch + Tprocessing + T∆ + Tmargin ms

Here: Tsearch = Tfirst_SSB = 0.5ms; Tprocessing = 10ms; T∆ = 20ms; Tmargin = 2ms.

This gives a total of 52.5 ms.

#### A.14.2.2.7 RACH-based Hard Satellite switching with re-synchronization from FR2 to FR2

##### A.14.2.2.7.1 Test Purpose and Environment

This test is to verify the requirements for RACH-based hard satellite switching with re-synchronization from SAN FR2 to SAN FR2 specified in clause 6.1C.3.

##### A.14.2.2.7.2 Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells with same PCI as given in table A.14.2.2.7.2-1, A.14.2.2.7.2-2, A.14.2.2.7.2-3 and A.14.2.2.7.2-4. Both satellite switching delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively.

At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, The SIB19 implying t-service-r17 and target satellite configuration SatSwitchWithReSync-r18 shall be sent to UE. The target satellite configuration is in table A.14.2.2.7.2-3.

At the start of time duration T2, Cell 2 becomes detectable and t-service-r17 of Cell 1 is fulfilled.

Table A.14.2.2.7.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NGSO, NR FDD, 120 kHz SSB SCS, 100 MHz BW |
| 2 | NGSO, NR FDD, 30 kHz SSB SCS, 20 MHz BW |

Table A.14.2.2.7.2-2: General test parameters for RACH-based Hard Satellite switching with re-synchronization from FR2 to FR2

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 | One NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 |  |
| Final condition | Active cell |  | Cell 2 |  |
| UE position (L,B, H) |  |  | (0, 0, 0) | Set by any pre-configured means.(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| Access Barring Information |  | - | Not barred | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 5 |  |

Table A.14.2.2.7.2-3: Target Satellite configuration pattern for hard satellite switching scenario

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

Table A.14.2.2.7.2-4: Cell specific test parameters for RACH-based Hard Satellite switching with re-synchronization from FR2 to FR2 test case

| Parameter |  | Unit | Cell 1Note1 |  | Cell 2Note1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite configurationNote2 |  |  | SSC.2 | N/A | N/A | SSC.2 |
| BWchannel |  | MHz | 100: NPRB,c = 66 (Config 1)20: NPRB,c = 51 (Config 2) |  |  | 100: NPRB,c = 66 (Config 1)20: NPRB,c = 51 (Config 2) |
| BWP BW |  | MHz | 100: NPRB,c = 66 (Config 1)20: NPRB,c = 51 (Config 2) |  |  | 100: NPRB,c = 66 (Config 1)20: NPRB,c = 51 (Config 2) |
| Kmac |  | ms | 0 |  |  | 0 |
| DRX Cycle |  | ms | Not Applicable |  |  | Not Applicable |
| PDSCH Reference measurement channel |  |  | SR.3.1 TDD (Config 1)SR.2.1 TDD (Config 2) |  |  | SR.3.1 TDD (Config 1)SR.2.1 TDD (Config 2) |
| CORESET Reference Channel |  |  | CR.3.1 TDD (Config 1)CR.2.1 TDD (Config 2) |  |  | CR.3.1 TDD (Config 1)CR.2.1 TDD (Config 2) |
| TRS configuration |  |  | TRS.2.1 FDD (Config 1)TRS.1.2 FDD (Config 2) |  |  | TRS.2.1 FDD (Config 1)TRS.1.2 FDD (Config 2) |
| OCNG Patterns |  |  | OP.1 |  |  | OP.1 |
| SMTC Configuration |  |  | SMTC.1 |  |  | SMTC.1 |
| SSB Configuration |  |  | SSB.1 FR2 (Config 1)SSB.2 FR1 (Config 2) |  |  | SSB.1 FR2 (Config 1)SSB.2 FR1 (Config 2) |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 120 kHz (Config 1)30 kHz (Config 2) |  |  | 120 kHz (Config 1)30 kHz (Config 2) |
| PUCCH/PUSCH subcarrier spacing |  | kHz | 120 kHz (Config 1)30 kHz (Config 2) |  |  | 120 kHz (Config 1)30 kHz (Config 2) |
| PRACH configuration |  |  | FR2 PRACH configuration 1 (Config 1)FR1 PRACH configuration 1 (Config 2) |  |  | FR2 PRACH configuration 1 (Config 1)FR1 PRACH configuration 1 (Config 2) |
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
| ![](media_svg/image15.svg) [公式≈: ^{N}oc]Note3 |  | dBm/ 15 kHz | -98 |  |  |  |
| ![](media_svg/image15.svg) [公式≈: ^{N}oc]Note3 |  | dBm/ SCS | -89 (Config 1)-95 (Config 2) |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 8 | -Infinity | -Infinity | 8 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 8 | -Infinity | -Infinity | 8 |
| SSB_RP |  | dBm/ SCS | -81 (Config 1)-87 (Config 2) | -Infinity | -Infinity | -81 (Config 1)-87 (Config 2) |
| IoNote4 |  | dBm/ 95.04 MHz (Config 1)dBm/ 18.36 MHz (Config 2) | -57.37 (Config 1)-52.49 (Config 2) |  | -57.37 (Config 1)-52.49 (Config 2) |  |
| Propagation condition |  | - | AWGN |  |  |  |
| NOTE 1: Cell 1 and Cell 2 have same PCI. Satellite serving for Cell 1 and Satellite serving for Cell 2 are two different NGSO satellites.NOTE 2: SSB transmit timing from TE should fit the SSB-timeOffset and the nominal propagation delay difference between serving satellite and target satellite. The nominal propagation delay is counted from the SSB-TimeOffset reference point to UE, which based on satellite locations and UE location known to the TE in this test case.NOTE 3: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image15.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 4: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 5: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |  |  |  |

##### A.14.2.2.7.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 112.5ms or (52.5+ 1000*Oangle / 22.5) ms from the beginning of time period T2.

The rate of correct satellite switch observed during repeated tests shall be at least 90 %.

NOTE: The hard satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tinterrupt, where:

Tinterrupt is defined in clause 6.1C.3.3.2.

Dswitch_unchangedPCI = Tinterrupt = Tsearch + Tprocessing  + T∆ +Tsat_beam+ Tmargin ms

Here: Tsearch = Tfirst_SSB = 0.5ms; Tprocessing = 10ms; T∆ = 20ms; Tmargin = 2ms,  Tsat_beam =60ms or Oangle / 22.5 s

Besides, interruption uncertainty TIU = 20ms in acquiring the first PRACH transmission resource is needed.

This gives a total of 112.5ms or (52.5+ 1000*Oangle / 22.5) ms.

#### A.14.2.2.8 RACH-less Soft Satellite switching with re-synchronization from FR2 to FR2

##### A.14.2.2.8.1 Test Purpose and Environment

This test is to verify the requirements for RACH-less soft satellite switching with re-synchronization from SAN FR2 to SAN FR2 specified in clause 6.1C.3.

##### A.14.2.2.8.2 Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells with same PCI as given in tables A.14.2.2.8.2-1, A.14.2.2.8.2-2, A.14.2.2.8.2-3 and A.14.2.2.8.2-4. Satellite switching delay is tested.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively.

At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, The SIB19 implying t-service-r17 and target satellite configuration SatSwitchWithReSync-r18 shall be sent to UE. The target satellite configuration is in table A.14.2.2.8.2-3. The configured grant PUSCH transmission in the Cell 2 is configured in the RRC message from Cell 1.

At the start of time duration T2, Cell 2 becomes detectable and t-ServiceStart-r18 is fulfilled.

At the start of time duration T3, t-service-r17 of Cell 1 is fulfilled.

Table A.14.2.2.8.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NGSO, NR FDD, 120 kHz SSB SCS, 10 MHz BW |
| 2 | NGSO, NR FDD, 30 kHz SSB SCS, 20 MHz BW |

Table A.14.2.2.8.2-2: General test parameters for RACH-less Soft Satellite switching with re-synchronization with FR2 numerology

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

Table A.14.2.2.8.2-3: Target Satellite configuration pattern for soft satellite switching scenario

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

Table A.14.2.2.8.2-4: Cell specific test parameters for Inter frequency SAN handover test case

| Parameter |  | Unit | Cell 1Note1 |  |  | Cell 2Note1 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T1 | T2 | T3 |
| Satellite configurationNote2 |  |  | SSC.2 |  | N/A | N/A | SSC.2 |  |
| BWchannel |  | MHz | 100: NPRB,c = 66 (Config 1)20: NPRB,c = 51 (Config 2) |  |  |  | 100: NPRB,c = 66 (Config 1)20: NPRB,c = 51 (Config 2) |  |
| BWP BW |  | MHz | 100: NPRB,c = 66 (Config 1)20: NPRB,c = 51 (Config 2) |  |  |  | 100: NPRB,c = 66 (Config 1)20: NPRB,c = 51 (Config 2) |  |
| Kmac |  | ms | 0 |  |  |  | 0 |  |
| DRX Cycle |  | ms | Not Applicable |  |  |  | Not Applicable |  |
| PDSCH Reference measurement channel |  |  | SR.3.1 FDD (Config 1)SR.2.1 TDD (Config 2) |  |  |  | SR.3.1 FDD (Config 1)SR.2.1 TDD (Config 2) |  |
| CORESET Reference Channel |  |  | CR.3.1 FDD (Config 1)CR.2.1 TDD (Config 2) |  |  |  | CR.3.1 FDD (Config 1)CR.2.1 TDD (Config 2) |  |
| TRS configuration |  |  | TRS.2.1 FDD (Config 1)TRS.1.2 FDD (Config 2) |  |  |  | TRS.2.1 FDD (Config 1)TRS.1.2 FDD (Config 2) |  |
| OCNG Patterns |  |  | OP.1 |  |  |  | OP.1 |  |
| SMTC Configuration |  |  | SMTC.1 |  |  |  | SMTC.5 |  |
| SSB Configuration |  |  | SSB.3 FR2 (Config 1)SSB.2 FR1 (Config 2) |  |  |  | SSB.5 FR2 (Config 1)SSB.2 FR1 (Config 2) |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | 120 kHz (Config 1)30 kHz (Config 2) |  |  |  | 120 kHz (Config 1)30 kHz (Config 2) |  |
| PUCCH/PUSCH subcarrier spacing |  | kHz | 120 kHz (Config 1)30 kHz (Config 2) |  |  |  | 120 kHz (Config 1)30 kHz (Config 2) |  |
| PRACH configuration |  |  | FR2 PRACH configuration 1 (Config 1)FR1 PRACH configuration 1 (Config 2) |  |  |  | N/A |  |
| BWP configuration | Initial DL BWP |  | DLBWP.0.1 |  |  |  | DLBWP.0.1 |  |
|  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  | DLBWP.1.1 |  |
|  | Initial UL BWP |  | ULBWP.0.1 |  |  |  | ULBWP.0.1 |  |
|  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  | ULBWP.1.1 |  |
| EPRE ratio of PSS to SSS |  | dB | 0 |  |  |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/ 15 kHz | -98 |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/ SCS | -89 (Config 1)-95 (Config 2) |  |  |  |  |  |
| ![](media_svg/image10.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | 4 | 4 | -Infinity | -Infinity | 9 | 9 |
| ![](media_svg/image11.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 4 | 4 | -Infinity | -Infinity | 9 | 9 |
| SSB_RP |  | dBm/ SCS | -85 (Config 1)-91 (Config 2) | -85 (Config 1)-91 (Config 2) | -Infinity | -Infinity | -76 (Config 1)-83 (Config 2) | -76 (Config 1)-83 (Config 2) |
| IoNote3 |  | dBm/ 95.04 MHz (Config 1)dBm/ 18.36 MHz (Config 2) | -54.56 (Config 1)-61.68 (Config 2) | -54.56 (Config 1)-61.68 (Config 2) | -60.01 (Config 1)-67.13 (Config 2) | -60.01 (Config 1)-67.13 (Config 2) | -46.80 (Config 1)-54.87 (Config 2) | -46.80 (Config 1)-54.87 (Config 2) |
| Propagation condition |  | - | AWGN |  |  |  |  |  |
| NOTE 1: Cell 1 and Cell 2 have same PCI. Satellite serving for Cell 1 and Satellite serving for Cell 2 are two different NGSO satellites.NOTE 2: SSB transmit timing from TE should fit the SSB-timeOffset and the nominal propagation delay difference between serving satellite and target satellite. The nominal propagation delay is counted from the SSB-TimeOffset reference point to UE, which based on satellite locations and UE location known to the TE in this test case.NOTE 3: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 4: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 5: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |  |  |  |  |  |

##### A.14.2.2.8.3 Test Requirements

The UE shall start to transmit the PUSCH to Cell 2 less than 190 ms or (130+1000* Oangle / 22.5) ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tsoft_switch, where:

Tsoft_switch = max(t-service-t-seviceStart, Tsearch + T∆+Tsat_beam + Tmargin) + TIU + Tprocessing  ms

Here: t-service-t-seviceStart= 100ms; Tsearch = 10.5ms; T∆ = 20ms; Tmargin = 2ms, Tprocessing = 10ms, Tsat_beam =60ms or Oangle / 22.5 s

Besides, interruption uncertainty TIU = 20ms in acquiring the first configured grant based PUSCH transmission resource is needed.

This gives a total of 190 ms or (130+1000* Oangle / 22.5) ms.

### A.14.2.3 Intra-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1

#### A.14.2.3.1 Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN time-based conditional handover without L3 measurement criteria from FR1 to FR1 specified in clause 6.1C.2.3.

#### A.14.2.3.2 Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells as given in table A.14.2.3.2-1, and A.14.2.3.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure intra-frequency neighbour cell. The RRC message implying time-based handover to Cell 2 with Event CondEvent T1 shall be sent to UE, at a time earlier than TRRC (10 ms) before the beginning of T2.

Starting T2, Cell 2 becomes detectable and time condition event CondEvent T1 is fulfilled.

Table A.14.2.3.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |

Table A.14.2.3.2-2: General test parameters for Intra-frequency SAN time-based conditional handover without L3 measurement criteria from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1 | One NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 | FDD duplex mode cell |
|  | Neighbouring cell |  | Cell 2 | FDD duplex mode cell |
| Final condition | Active cell |  | Cell 2 |  |
| Satellite configuration | Config 1 |  | RMC in [A.x] | For NGSO satellite configuration |
| UE position (L,B, H) |  |  | (0, 0, 0) | Set by any pre-configured means.(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| t1-Threshold-r17.condEventT1-r17 |  | s | T2 | Entering condition |
| duration-r17.condEventT1-r17 |  | slot | 1000 | Give 1 s search duration |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 2 |  |

Table A.14.2.3.2-3: Cell specific test parameters for Intra-frequency SAN time-based conditional handover without L3 measurement criteria from FR1 to FR1

| Parameter |  | Test configuration | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  | Config 1 |  | 1 |  | 1 |  |
| BWchannel |  |  | MHz | 10: NPRB,c = 52 |  | 10: NPRB,c = 52 |  |
| BWP BW |  |  | MHz | 10: NPRB,c = 52 |  | 10: NPRB,c = 52 |  |
| TACommon |  | Config 1 | s | 0 |  | 0 |  |
| TACommonDrift |  |  | s | 0 |  | 0 |  |
| TACommonDriftVariation |  |  | s | 0 |  | 0 |  |
| Koffset |  | Config 1 | ms | [4] |  | [4] |  |
| Kmac |  | Config 1 | ms | 0 |  | 0 |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 FDD |  |  |  |
| CORESET Reference Channel |  |  |  | CR.1.1 FDD |  |  |  |
| TRS configuration |  |  |  | TRS.1.1 FDD |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |
| SSB Configuration |  |  |  | SSB.1 FR1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 |  |  |  |
| BWP configuration | Initial DL BWP | Config 1 |  | DLBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  | Config 1 | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | Config 1 | dBm/ 15 kHz | -98 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/ SCS | -98 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 8 | -3.3 | -Infinity | 2.36 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 8 | 8 | -Infinity | 11 |
| SSB_RP |  |  | dBm/ SCS | -90 | -90 | -Infinity | -87 |
| IoNote3 |  |  | dBm/ 9.36 MHz | -61.41 | -57.06 | -61.41 | -57.06 |
| Propagation condition |  |  | - | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |

#### A.14.2.3.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 92 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay is defined in clause 6.1C.2.3, can be expressed as:

DCHO = TRRC + TEvent_DU + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

Tinterrupt = 82 ms; TCHO_execution = 10 ms.

This gives a total of 92 ms.

### A.14.2.4 Inter-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1

#### A.14.2.4.1 Test Purpose and Environment

This test is to verify the requirement for inter -frequency SAN time-based conditional handover without L3 measurement criteria from FR1 to FR1 specified in clause 6.1C.2.

#### A.14.2.4.2 Test Parameters

The test scenario comprises of 2 NR FDD carrier and one cell on each carrier as given in table A.14.2.4.2-1, and A.14.2.4.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure inter-frequency neighbour cell and Gap pattern ID gp0. The RRC message implying time-based handover to Cell 2 with Event CondEvent T1 shall be sent to UE, at a time earlier than TRRC (10 ms) before the beginning of T2.

Starting T2, Cell 2 becomes detectable and time condition event CondEvent T1 is fulfilled.

Table A.14.2.4.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | NGSO, NR FDD, 15 kHz SSB SCS, 10 MHz BW |

Table A.14.2.4.2-2: General test parameters for Inter-frequency SAN time-based conditional handover from FR1 to FR1

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| RF Channel Number |  |  | 1, 2 | Two NR NTN satellite RF channel |
| Initial conditions | Active cell |  | Cell 1 | FDD duplex mode cell |
|  | Neighbouring cell |  | Cell 2 | FDD duplex mode cell |
| Final condition | Active cell |  | Cell 2 |  |
| Satellite configuration | Config 1 |  | RMC in [A.x] | For NGSO satellite configuration |
| UE position (L,B, H) |  |  | (0, 0, 0) | Set by any pre-configured means.(L,B,H) is Geodetic coordinate, where L is latitude, B is longitude, and H is height. |
| t1-Threshold-r17.condEventT1-r17 |  | s | T2 | Entering condition |
| duration-r17.condEventT1-r17 |  | slot | 1000 | Give 1 s search duration |
| Access Barring Information |  | - | Not Sent | No additional delays in random access procedure. |
| Time offset between cells |  |  | 3 s | Synchronous cells |
| T1 |  | s | 5 |  |
| T2 |  | s | 2 |  |

Table A.14.2.4.2-3: Cell specific test parameters for Inter-frequency SAN time-based conditional handover from FR1 to FR1

| Parameter |  | Test configuration | Unit | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  | Config 1 |  | 1 |  | 2 |  |
| BWchannel |  |  | MHz | 10: NPRB,c = 52 |  | 10: NPRB,c = 52 |  |
| BWP BW |  |  | MHz | 10: NPRB,c = 52 |  | 10: NPRB,c = 52 |  |
| TACommon |  | Config 1 | s | 0 |  | 0 |  |
| TACommonDrift |  |  | s | 0 |  | 0 |  |
| TACommonDriftVariation |  |  | s | 0 |  | 0 |  |
| Koffset |  | Config 1 | ms | [4] |  | [4] |  |
| Kmac |  | Config 1 | ms | 0 |  | 0 |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |
| PDSCH Reference measurement channel |  |  |  | SR.1.1 FDD |  |  |  |
| CORESET Reference Channel |  |  |  | CR.1.1 FDD |  |  |  |
| TRS configuration |  |  |  | TRS.1.1 FDD |  |  |  |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SMTC Configuration |  |  |  | SMTC.1 |  |  |  |
| SSB Configuration |  |  |  | SSB.1 FR1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |
| PUCCH/PUSCH subcarrier spacing |  |  | kHz | 15 kHz |  |  |  |
| PRACH configuration |  |  |  | FR1 PRACH configuration 1 |  |  |  |
| BWP configuration | Initial DL BWP | Config 1 |  | DLBWP.0.1 |  |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  |  |  |
| EPRE ratio of PSS to SSS |  | Config 1 | dB | 0 |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | Config 1 | dBm/ 15 kHz | -98 |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  |  | dBm/ SCS | -98 |  |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 4 | 4 | -Infinity | 9 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4 | 4 | -Infinity | 9 |
| SSB_RP |  |  | dBm/ SCS | -94 | -94 | -Infinity | -89 |
| IoNote3 |  |  | dBm/ 9.36 MHz | -64.59 | -64.59 | -70.05 | -60.53 |
| Propagation condition |  |  | - | AWGN |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |  |

#### A.14.2.4.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 132 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE: The handover delay is defined in clause 6.1C.2.3, can be expressed as:

DCHO = TRRC + TEvent_DU + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

Tinterrupt = 122 ms; TCHO_execution = 10 ms.

This gives a total of 132 ms.

## A.14.3 Timing for Satellite Access

### A.14.3.1 UE transmit timing for Satellite Access

#### A.14.3.1.1 NR UE Transmit Timing Test for FR1

##### A.14.3.1.1.1 Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the reference cell and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1C.2. Supported test configurations are shown in table A.14.3.1.1.1-1.

Table A.14.3.1.1.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | void |
| 3 | NGSO with varying Doppler and delay shift NTN channel model, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 3. |  |

The test consists a single NR cell (PCell). Table A.14.3.1.1.1-2 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.14.3.1.1.1-3.

Table A.14.3.1.1.1-2: Cell Specific Test Parameters for UL Transmit Timing test

| Parameter | Unit | Config | Test1 | Test2 |
| --- | --- | --- | --- | --- |
| SSB ARFCN |  | 1,3 | 1 | 1 |
| Serving satellite configuration |  | 1 | SSC.1 |  |
|  |  | 3 | SSC.2 |  |
| BWchannel | MHz | 1,3 | 10: NPRB,c = 52 |  |
| Initial BWP Configuration |  | 1,3 | DLBWP.0.1ULBWP.0.1 |  |
| Dedicated BWP Configuration |  | 1,3 | DLBWP.1.1ULBWP.1.1 |  |
| DRX Cycle | ms | 1,3 | N/A | DRX.8Note5 |
| PDSCH Reference measurement channel |  | 1,3 | SR.1.1 FDD |  |
| RMSI CORESET Reference Channel |  | 1,3 | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | 1,3 | CCR.1.1 FDD |  |
| OCNG Patterns |  | 1,3 | OP.1 |  |
| SSB configuration |  | 1,3 | SSB.1 FR1 |  |
| SMTC Configuration |  | 1,3 | SMTC.1 |  |
| TRS configuration |  | 1,3 | TRS.1.1 FDD |  |
| EPRE ratio of PSS to SSS | dB | 1,3 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | 1,3 | -98 | -98 |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | 1,3 | -98 | -98 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  | 1,3 | 3 | 3 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | 1,3 | 3 | 3 |
| SS-RSRPNote3 | dBm/SCS | 1,3 | -95 | -95 |
| IoNote3 | dBm/9.36 MHz | 1,3 | -65.2 | -65.2 |
| Propagation condition |  | 1 | AWGN |  |
|  |  | 3 | AWGN with time varying Doppler and delay shifts |  |
| SRS Config |  | 1,3 | SRSConf.1Note6 | SRSConf.2Note6 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: DRX related parameters are given in table A.3.3.8-1NOTE 6: SRS configs are given in table A.14.3.1.1.1-3NOTE 7: For Config 3, the initial ephemerisInfo of SSC.2 refers to Table G.4.1-1 of TS 38.101-5 [43].NOTE 8: For Config 3, the UE position is set by AT command according to G.4.2 of TS 38.101-5 [43] at the beginning if the test, and remains unchanged during the test. |  |  |  |  |

Table A.14.3.1.1.1-3: SRS Configuration for Timing Accuracy Test

|  | Field | SRSConf.1 | SRSConf.2 | Comments |
| --- | --- | --- | --- | --- |
| SRS- | srs-ResourceSetId | 0 | 0 |  |
| ResourceSet | srs-ResourceIdList | 0 | 0 |  |
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
|  | freqHoppingc-SRS | 14 | 14 | Matches NPRB,c |
|  | freqHoppingb-SRS | 0 | 0 |  |
|  | freqHoppingb-hop | 0 | 0 |  |
|  | groupOrSequenceHopping | Neither | Neither |  |
|  | resourceType | Periodic | Periodic |  |
|  | periodicityAndOffset-p | sl1, 0 | sl320, 3 | Offset to align with DRX periodicity |
|  | sequenceId | 0 | 0 | Any 10 bit number |

##### A.14.3.1.1.2 Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1) Set up PCell according to parameters given in table A.14.3.1.1.1-2.

2) After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within $\left ( N_{TA}+N_{TA-offset}+N_{TA,adj}^{common}+N_{TA,adj}^{UE}\right ) \times  T_{c}\pm  (T_{e\_NTN}-T_{GNSS\_margin})$  of the first detected path of DL SSB.

a. The NTA_offset value (in Tc units) is 25600

b. The $ N_{TA,adj}^{common}$ value is derived from the higher-layer parameters TACommon, TACommonDrift, and TACommonDriftVariation.

c. The $ N_{TA,adj}^{UE}$ value is computed by the UE based on UE position and serving-satellite-ephemeris-related higher-layers parameters. For Config 3, $ N_{TA,adj}^{UE}$ is calculated based on the generated UL channel with time varying Doppler and delay shifts.

d. The $ T_{e\_NTN}$ values depend on the DL and UL SCS for which the test is being run and are given in table 7.1C.2-1

e. The $ T_{GNSS\_margin}$ counts for the margin for the GNSS position definition error considered in the core requirement, which needs to be substracted for the test requirement, due to the usage of AT commands or any other pre-configured means in the test. $ T_{GNSS\_margin}=327,68\times  T_{c}$

3) If the NTN parameters are configured as GSO scenario, the test system shall adjust the timing of the DL path by values given in table A.14.3.1.1.2-1. If the NTN parameters are configured as NGSO scenario, the test system shall adjust the timing of the DL path according to the serving-satellite-ephemeris-related higher-layers parameters.

Table A.14.3.1.1.2-1: Adjustment Value for DL Timing

| SCS of SSB signals (kHz) | Adjustment Value |  |
| --- | --- | --- |
|  | Test1 | Test2 |
| 15 | +64*64Tc | +32*64Tc |

4) The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1C.2 Table 7.1C.2.1-1 until the UE transmit timing offset is within $\left ( N_{TA}+N_{TA-offset}+N_{TA,adj}^{common}+N_{TA,adj}^{UE}\right ) \times  T_{c}\pm  (T_{e\_NTN}-T_{GNSS\_margin})$ respective to the first detected path (in time) of DL SSB. Skip this step for test 2 with DRX configured.

5) The test system shall verify that the UE transmit timing offset stays within $\left ( N_{TA}+N_{TA-offset}+N_{TA,adj}^{common}+N_{TA,adj}^{UE}\right ) \times  T_{c}\pm  (T_{e\_NTN}-T_{GNSS\_margin})$ of the first detected path of DL SSB. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

#### A.14.3.1.2 NR UE Transmit Timing Test for FR2-NTN

##### A.14.3.1.2.1 Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the reference cell and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1C.2. Supported test configurations are shown in table A.14.3.1.2.1-1.

Table A.14.3.1.2.1-1: Supported test configurations for FR2-NTN PCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 2 | NGSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 3 | GSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 4 | GSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| 5 | NGSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| NOTE: For mobile VSAT UE type, it is only requied to pass test config 3. |  |

The test consists a single NR cell (PCell). Table A.14.3.1.2.1-2 and A.14.3.1.2.1-2A defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.14.3.1.2.1-3.

Table A.14.3.1.2.1-2: Cell Specific Test Parameters for UL Transmit Timing test

| Parameter | Unit | Config | Test1 | Test2 |  |
| --- | --- | --- | --- | --- | --- |
| SSB ARFCN |  | 1,2,3 | Freq1 | Freq1 |  |
| Serving satellite configuration |  | 1,3,5 | SSC.1. |  |  |
|  |  | 2,4 | SSC.2 |  |  |
|  |  |  |  |  |  |
| BWchannel | MHz | 1,2,3 | 100: NPRB,c = 66 |  |  |
|  |  | 4,5 | 10: NPRB,c = 24 |  |  |
| Initial BWP Configuration |  | 1,2,3,4,5 | DLBWP.0.1ULBWP.0.1 |  |  |
| Dedicated BWP Configuration |  | 1,2,3,4,5 | DLBWP.1.1ULBWP.1.1 |  |  |
| DRX Cycle | ms | 1,2,3 | N/A | DRX.8Note5 |  |
| PDSCH Reference measurement channel |  | 1,2,3 | SR.3.1 TDD |  |  |
|  |  | 4,5 | SR.2.1 TDD |  |  |
| RMSI CORESET Reference Channel |  | 1,2,3 | CR.3.1 TDD |  |  |
|  |  | 4,5 | CR.2.1 TDD |  |  |
| Dedicated CORESET Reference Channel |  | 1,2,3 | CCR.2.1 TDD |  |  |
|  |  | 4,5 | CCR.2.1 TDD |  |  |
| OCNG Patterns |  | 1,2,3 | OP.1 |  |  |
| SSB configuration |  | 1,2,3 | SSB.1 FR2 |  |  |
|  |  | 4,5 | SSB.1 FR1 |  |  |
| SMTC Configuration |  | 1,2,3,4,5 | SMTC.1 |  |  |
| TRS configuration |  | 1,2,3 | TRS.2.1 FDD |  |  |
|  |  |  | TRS.1.2 TDD |  |  |
| EPRE ratio of PSS to SSS | dB | 1,2,3,4,5 | 0 | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| Propagation condition |  | 1,2,3,4,5 | AWGN |  |  |
| SRS Config |  | 1,2,3 | SRSConf.1Note6 | SRSConf.2Note6 |  |
|  |  | 4,5 | SRS.1 | SRS.1 |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: VoidNOTE 3: VoidNOTE 4: VoidNOTE 5: DRX related parameters are given in table A.3.3.8-1NOTE 6: SRS configs are given in table A.14.3.1.2.1-3 |  |  |  |  |  |

Table A.14.3.1.2.1-2A: OTA related test parameters

| Parameter | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |
| Assumption for UE beamsNote 6 |  | Fine (For electronic steering antenna type)RX beam of RX beam peak direction (For mechanical steering antenna type) |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15 kHzNote4 | -112 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote3 | -103 |  |
| ![](media_svg/image16.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 4 |  |
| SS-RSRPNote2 | dBm/SCS Note4 | -96 |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 4 |  |
| IoNote2 | dBm/95.04 MHz Note4 | -68.5 |  |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: SS B_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: VoidNOTE 4: VoidNOTE 5: VoidNOTE 6: Information about types of UE beam is given in B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |

Table A.14.3.1.2.1-3: SRS Configuration for Timing Accuracy Test

|  | Field | SRSConf.1 | SRSConf.2 | Comments |
| --- | --- | --- | --- | --- |
| SRS- | srs-ResourceSetId | 0 | 0 |  |
| ResourceSet | srs-ResourceIdList | 0 | 0 |  |
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
|  | periodicityAndOffset-p | sl1, 0 | Sl2560, 4 | Offset to align with DRX periodicity |
|  | sequenceId | 0 | 0 | Any 10 bit number |

##### A.14.3.1.2.2 Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1) Set up PCell according to parameters given in table A.14.3.1.2.1-2.

2) After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within $\left ( N_{TA}+N_{TA-offset}+N_{TA,adj}^{common}+N_{TA,adj}^{UE}\right ) \times  T_{c}\pm  (T_{e\_NTN}-T_{GNSS\_margin})$  of the first detected path of DL SSB.

a. The NTA_offset value (in Tc units) is 0

b. The $ N_{TA,adj}^{common}$ value is derived from the higher-layer parameters TACommon, TACommonDrift, and TACommonDriftVariation.

c. The $ N_{TA,adj}^{UE}$ value is computed by the UE based on UE position and serving-satellite-ephemeris-related higher-layers parameters.

d. The $ T_{e\_NTN}$ values depend on the DL and UL SCS for which the test is being run and are given in table 7.1C.2-2 and 7.1C.2-3 for test configuration 1, 2 and 3, and in table 7.1C.2-1 for test configuration 4 and 5.

e. The $ T_{GNSS\_margin}$ counts for the margin for the GNSS position definition error considered in the core requirement, which needs to be subtracted for the test requirement, due to the usage of AT commands or any pre-configured means in the test. $ T_{GNSS\_margin}=98.304\times  T_{c}$

3) If the NTN parameters are configured as GSO scenario, the test system shall adjust the timing of the DL path by values given in table A.14.3.1.2.2-1. If the NTN parameters are configured as NGSO scenario, the test system shall adjust the timing of the DL path according to the serving-satellite-ephemeris-related higher-layers parameters.

Table A.14.3.1.2.2-1: Adjustment Value for DL Timing

| SCS of SSB signals (kHz) | Adjustment Value |  |
| --- | --- | --- |
|  | Test1 | Test2 |
| 120 | +8*64Tc | +4*64Tc |
| 30 | +32*64Tc | +16*64Tc |

4) The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1C.2 Table 7.1C.2.1-1 until the UE transmit timing offset is within $\left ( N_{TA}+N_{TA-offset}+N_{TA,adj}^{common}+N_{TA,adj}^{UE}\right ) \times  T_{c}\pm  (T_{e\_NTN}-T_{GNSS\_margin})$ respective to the first detected path (in time) of DL SSB. Skip this step for test 2 with DRX configured.

5) The test system shall verify that the UE transmit timing offset stays within $\left ( N_{TA}+N_{TA-offset}+N_{TA,adj}^{common}+N_{TA,adj}^{UE}\right ) \times  T_{c}\pm  (T_{e\_NTN}-T_{GNSS\_margin})$ of the first detected path of DL SSB. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

### A.14.3.2 Timing advance for satellite access

#### A.14.3.2.1 SA FR1 timing advance adjustment accuracy

##### A.14.3.2.1.1 Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3C.

##### A.14.3.2.1.2 Test Parameters

Supported test configurations are shown in table A.14.3.2.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.14.3.2.1.2-2, A.14.3.2.1.2-3 and A.14.3.2.1.2-4.

In all test cases, single cell served by SAN is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.14.3.2.1.2-4, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

The UE shall be provided with the valid information about the SAN serving cell before the test.During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.14.3.2.1.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause7.3C.2.1, the UE adjusts its uplink timing at slot n+k+1+2µ$\cdot  K_{offset}$ for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.14.3.2.1.2-1: Timing advance supported test configurations

| Config | Description |
| --- | --- |
| 1 | GSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NGSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

Table A.14.3.2.1.2-2: General test parameters for timing advance

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| RF channel number |  | 1 |  |
| Initial DL BWP |  | DLBWP.0.1 | As specified in table A.3.9.2.1-1 |
| Dedicated DL BWP |  | DLBWP.1.1 | As specified in table A.3.9.2.2-1 |
| Initial UL BWP |  | ULBWP.0.1 | As specified in table A.3.9.3.1-1 |
| Dedicated UL BWP |  | ULBWP.1.1 | As specified in table A.3.9.3.2-1 |
| Timing Advance Command (TA) value during T1 |  | 31 | NTA_new = NTA_old  for the purpose of establishing a reference value from which the timing advance adjustment accuracy can be measured during T2 |
| Timing Advance Command (TA) value during T2 |  | 39 | For 15 kHz SCS NTA_new = NTA_old  + 8192*Tc (based on equation in clause 4.2 of TS 38.213 [3]) |
| T1 | s | 5 |  |
| T2 | s | 5 |  |

Table A.14.3.2.1.2-3: Cell specific test parameters for timing advance

| Parameter |  |  | Unit | Test1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 |
| Duplex mode |  | Config 1,2 |  | FDD |  |
| Satellite information |  | Config 1 |  | SSC.1 |  |
|  |  | Config 2 |  | SSC.2 |  |
| BWchannel |  | Config 1,2 | MHz | 10: NPRB,c = 52 |  |
| BWP BW |  | Config 1,2 | MHz | 10: NPRB,c = 52 |  |
| DRX Cycle |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel |  | Config 1,2 |  | SR.1.1 FDD |  |
| RMSI CORESET Reference Channel |  | Config 1,2 |  | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1,2 |  | CCR.1.1 FDD |  |
| TRS configuration |  | Config 1,2 |  | TRS.1.1 FDD |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |
| SMTC configuration |  | Config 1,2 |  | SMTC.1 FR1 |  |
| SSB configuration |  | Config 1,2 |  | SSB.1 FR1 |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 | kHz | 15 kHz |  |
| PUCCH/PUSCH subcarrier spacing |  | Config 1,2 | kHz | 15 kHz |  |
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
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 |  | dBm/SCS | -98 |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 3 |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 |  |
| IoNote3 | Config 1,2 |  | dBm/9.36 MHz | -67.57 |  |
| Propagation condition |  |  | - | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |

Table A.14.3.2.1.2-4: Sounding Reference Symbol Configuration for timing advance

| Field |  | Value | Comment |
| --- | --- | --- | --- |
| c-SRS | Config 1,2 | 12 | Frequency hopping is disabled |
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

##### A.14.3.2.1.3 Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1+2µ$\cdot  K_{offset}$ slots after the reception of the timing advance command, where k=5.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3C.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

#### A.14.3.2.3 SA FR2-NTN timing advance adjustment accuracy

##### A.14.3.2.3.1 Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3C.

##### A.14.3.2.3.2 Test Parameters

Supported test configurations are shown in table A.14.3.2.3.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.14.3.2.3.2-2, A.14.3.2.3.2-3 and A.14.3.2.3.2-4.

In all test cases, single cell served by SAN is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.14.3.2.3.2-4, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

The UE shall be provided with the valid information about the SAN serving cell before the test. During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.14.3.2.3.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause7.3C.2.1, the UE adjusts its uplink timing at slot n+k+1+2µ$\cdot  K_{offset}$ for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.14.3.2.3.2-1: Timing advance supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 2 | NGSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 3 | GSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 4 | GSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| 5 | NGSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| NOTE: For mobile VSAT UE type, it is only requied to pass test config 3. |  |

Table A.14.3.2.3.2-2: General test parameters for timing advance

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

Table A.14.3.2.3.2-3: Cell specific test parameters for timing advance

| Parameter |  |  | Unit | Test1 |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 |
| Duplex mode | Config 1,2,3,4,5 |  |  | FDD |  |
| Satellite information | Config 1,3,4 |  |  | SSC.1 |  |
|  | Config 2,5 |  |  | SSC.2 |  |
|  | Config 3 |  |  | SSC.1 |  |
| BWchannel | Config 1,2,3 |  | MHz | 100: NPRB,c = 66 |  |
|  | Config 4,5 |  |  | 10: NPRB,c = 24 |  |
| BWP BW | Config 1,2,3 |  | MHz | 100: NPRB,c = 66 |  |
|  | Config 4,5 |  |  | 10: NPRB,c = 24 |  |
| DRX Cycle |  |  | ms | Not Applicable |  |
| PDSCH Reference measurement channel | Config 1,2,3 |  |  | SR.X.X FDD |  |
|  | Config 4,5 |  |  | SR.2.1 TDD |  |
| RMSI CORESET Reference Channel | Config 1,2,3 |  |  | CR.X.X FDD |  |
|  | Config 4,5 |  |  | CR.2.1 TDD |  |
| Dedicated CORESET Reference Channel | Config 1,2,3 |  |  | CCR.X.X FDD |  |
|  | Config 4,5 |  |  | CCR.2.1 TDD |  |
| TRS configuration | Config 1,2,3 |  |  | TRS.2.1 FDD |  |
|  | Config 4,5 |  |  | TRS.1.2 TDD |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |
| SMTC configuration | Config 1,2,3 |  |  | SMTC.1 |  |
| SSB configuration | Config 1,2,3 |  |  | SSB.1 FR2 |  |
|  | Config 4,5 |  |  | SSB.1 FR1 |  |
| PDSCH/PDCCH subcarrier spacing | Config 1,2,3 |  | kHz | 120 kHz |  |
|  | Config 4,5 |  |  | 30 kHz |  |
| PUCCH/PUSCH subcarrier spacing | Config 1,2,3 |  | kHz | 120 kHz |  |
|  | Config 4,5 |  |  | 30 kHz |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |
| Propagation condition |  | Config 1, 2, 3 | - | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: VoidNOTE 3: Void |  |  |  |  |  |

Table A.14.3.2.3.2-3A: OTA related test parameters

| Parameter | Unit | Test 1 |  |
| --- | --- | --- | --- |
|  |  | T1 | T2 |
| Angle of arrival configuration |  | Setup 1 according to clause A.3.15.1 |  |
| Assumption for UE beamsNote 6 |  | Fine (For electronic steering antenna type)RX beam of RX beam peak direction (For mechanical steering antenna type) |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/15 kHzNote4 | -112 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 | dBm/SCSNote3 | -103 |  |
| ![](media_svg/image16.svg) [公式≈: ^{Ê}s^{N}oc] | dB | 4 |  |
| SS-RSRPNote2 | dBm/SCS Note4 | -99 |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | 4 |  |
| IoNote2 | dBm/95.04 MHz Note4 | -68.5 |  |
| NOTE 1: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 2: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 3: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 4: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 5: As observed with 0 dBi gain antenna at the centre of the quiet zoneNOTE 6: Information about types of UE beam is given in B.2.1.3, and does not limit UE implementation or test system implementation |  |  |  |

Table A.14.3.2.3.2-4: Sounding Reference Symbol Configuration for timing advance

| Field | Value | Comment |
| --- | --- | --- |
| c-SRS | 16 | Frequency hopping is disabled |
| b-SRS | 0 |  |
| b-hop | 0 |  |
| freqDomainPosition | 0 | Frequency domain position of SRS |
| freqDomainShift | 0 |  |
| groupOrSequenceHopping | neither | No group or sequence hopping |
| SRS-PeriodicityAndOffset | sl5=4 for SCS 120 kHz | Once every 5 slots |
| pathlossReferenceRS | ssb-Index=0 | SSB #0 is used for SRS path loss estimation |
| usage | Codebook | Codebook based UL transmission |
| startPosition | 0 | resourceMapping setting. SRS on last symbol of slot, and 1 symbols for SRS without repetition. |
| nrofSymbols | n1 |  |
| repetitionFactor | n1 |  |
| combOffset-n2 | 0 | transmissionComb setting |
| cyclicShift-n2 | 0 |  |
| nrofSRS-Ports | port1 | Number of antenna ports used for SRS transmission |
| NOTE: For further information see clause 6.3.2 in TS 38.331 [2]. |  |  |

##### A.14.3.2.1.3 Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1+2µ$\cdot  K_{offset}$ slots after the reception of the timing advance command, where k=11.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3C.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.14.4 Signalling characteristics

### A.14.4.1 Radio link Monitoring

#### A.14.4.1.1 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode

##### A.14.4.1.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1C.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.14.4.1.1.1-1. The test parameters are given in tables A.14.4.1.1.1-2, A.14.4.1.1.1-3, and A.14.4.1.1.1-4 below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.14.4.1.1.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.4.1.1.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.1.1.1-2: General test parameters for FR1 out-of-sync testing in non-DRX mode

| Parameter |  |  | Unit | Value |
| --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |
| Active PCell |  |  |  | Cell 1 |
| RF Channel Number |  |  |  | 1 |
| BWchannel |  | Config 1, 2 | MHz | 10: NPRB,c = 52 |
| DL initial BWP configuration |  | Config 1, 2 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  | Config 1, 2 |  | DLBWP.1.1 |
| UL initial BWP configuration |  | Config 1, 2 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  | Config 1, 2 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel |  | Config 1, 2 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel |  | Config 1, 2 |  | CCR.1.3 FDD |
| SSB Configuration |  | Config 1, 2 |  | SSB.1 FR1 |
| SMTC Configuration |  | Config 1, 2 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2 |  | 15 kHz |
| PRACH Configuration |  | Config 1, 2 |  | Table  A.3.8.2.1-1 |
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
| CSI-RS configuration for CSI reporting |  | Config 1, 2 |  | CSI-RS.1.1 FDD |
| CSI-RS for tracking |  | Config 1, 2 |  | TRS.1.1 FDD |
| T1 |  |  | s | 0.2 |
| T2 |  |  | s | 0.48 |
| T3 |  |  | s | 0.48 |
| D1 |  |  | s | 0.44 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |

Table A.14.4.1.1.1-3: Cell specific test parameters for FR1 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode

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
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15 kHz | -98 |  |  |
|  | Config 2 |  | -98 |  |  |
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1 | dBm/SCS | -98 |  |  |
|  | Config 2 |  | -98 |  |  |
| Propagation condition |  |  | NTN-TDLC5-200 |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 4: The SNR in time periods T1, T2 and T3 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.6.5.1C.1.1-1.NOTE 5: Void. |  |  |  |  |  |

Table A.14.4.1.1.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

| Field | Test 1 |
| --- | --- |
|  | Value |
| gapOffset | 0 |
| NOTE: Ensure that RLM RS is partially overlapped with measurement gap |  |

Figure A.14.4.1.1.1-1: SNR variation for out-of-sync testing

##### A.14.4.1.1.2 Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.1.2 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode

##### A.14.4.1.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1C.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.14.4.1.2.1-1. The test parameters are given in tables A.14.4.1.2.1-2, and A.14.4.1.2.1-3 below. There is one cell (Cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.1.2.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.4.1.2.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.1.2.1-2: General test parameters for FR1 in-sync testing in non-DRX mode

| Parameter |  |  | Unit | Value |
| --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |
| Active PCell |  |  |  | Cell 1 |
| RF Channel Number |  |  |  | 1 |
| BWchannel |  | Config 1, 2 | MHz | 10: NPRB,c = 52 |
| DL initial BWP configuration |  | Config 1, 2 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  | Config 1, 2 |  | DLBWP.1.1 |
| UL initial BWP configuration |  | Config 1, 2 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  | Config 1, 2 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel |  | Config 1, 2 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel |  | Config 1, 2 |  | CCR.1.1 FDD |
| SSB Configuration |  | Config 1, 2 |  | SSB.1 FR1 |
| SMTC Configuration |  | Config 1, 2 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2 |  | 15 kHz |
| PRACH Configuration |  | Config 1, 2 |  | Table  A.3.8.2.1-1 |
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
| Gap pattern ID |  |  |  | N.A. |
| Layer 3 filtering |  |  |  | Enabled |
| T310 timer |  |  | ms | 1000 |
| T311 timer |  |  | ms | 1000 |
| N310 |  |  |  | 1 |
| N311 |  |  |  | 1 |
| CSI-RS configuration for CSI reporting | Config 1, 2 |  |  | CSI-RS.1.1 FDD |
| CSI-RS for tracking | Config 1, 2 |  |  | TRS.1.1 FDD |
| T1 |  |  | s | 0.2 |
| T2 |  |  | s | 0.2 |
| T3 |  |  | s | 0.24 |
| T4 |  |  | s | 0.2 |
| T5 |  |  | s | 0.88 |
| D1 |  |  | s | 0.84 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |

Table A.14.4.1.2.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in non-DRX mode

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
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15 kHz | -98 |  |  |  |  |
|  | Config 2 |  | -98 |  |  |  |  |
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1 | dBm/SCS | -98 |  |  |  |  |
|  | Config 2 |  | -98 |  |  |  |  |
| Propagation condition |  |  | NTN-TDLC5-200 |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 4: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2, SNR3, SNR4 and SNR5 respectively in figure A.6.5.1C.2.1-1.NOTE 5: Void. |  |  |  |  |  |  |  |

Figure A.14.4.1.2.1-1: SNR variation for in-sync testing

##### A.14.4.1.2.2 Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.1.3 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode

##### A.14.4.1.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell when DRX is used. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1C.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.14.4.1.3.1-1. The test parameters are given in tables A.14.4.1.3.1-2, and A.14.4.1.3.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.14.4.1.3.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.4.1.3.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.1.3.1-2: General test parameters for FR1 out-of-sync testing in DRX mode

| Parameter |  |  | Unit | Value |
| --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |
| Active PCell |  |  |  | Cell 1 |
| RF Channel Number |  |  |  | 1 |
| BWchannel |  | Config 1, 2 | MHz | 10: NPRB,c = 52 |
| DL initial BWP configuration |  | Config 1, 2 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  | Config 1, 2 |  | DLBWP.1.1 |
| UL initial BWP configuration |  | Config 1, 2 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  | Config 1, 2 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel |  | Config 1, 2 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel |  | Config 1, 2 |  | CCR.1.3 FDD |
| SSB Configuration |  | Config 1, 2 |  | SSB.1 FR1 |
| SMTC Configuration |  | Config 1, 2 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2 |  | 15 kHz |
| PRACH Configuration |  | Config 1, 2 |  | Table  A.3.8.2.1-1 |
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
| DRX Configuration |  |  |  | DRX.3 |
| Gap pattern ID |  |  |  | N.A. |
| Layer 3 filtering |  |  |  | Enabled |
| T310 timer |  |  | ms | 0 |
| T311 timer |  |  | ms | 1000 |
| N310 |  |  |  | 1 |
| N311 |  |  |  | 1 |
| CSI-RS configuration for CSI reporting |  | Config 1, 2 |  | CSI-RS.1.1 FDD |
| CSI-RS for tracking |  | Config 1, 2 |  | TRS.1.1 FDD |
| T1 |  |  | s | 0.2 |
| T2 |  |  | s | 0.68 |
| T3 |  |  | s | 0.68 |
| D1 |  |  | s | 0.64 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |

Table A.14.4.1.3.1-3: Cell specific test parameters for FR1 (Cell 1) for out-of-sync radio link monitoring tests in DRX mode

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
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15 kHz | -98 |  |  |
|  | Config 2 |  | -98 |  |  |
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1 | dBm/SCS | -98 |  |  |
|  | Config 2 |  | -98 |  |  |
| Propagation condition |  |  | NTN-TDLC5-200 |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 4: The SNR in time periods T1, T2 and T3 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.6.5.1C.3.1-1.NOTE 5: Void. |  |  |  |  |  |

Figure A.14.4.1.3.1-1: SNR variation for out-of-sync testing

##### A.14.4.1.3.2 Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.1.4 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode

##### A.14.4.1.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell when DRX is used. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1C.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.14.4.1.4.1-1. The test parameters are given in tables A.14.4.1.4.1-2, and A.14.4.1.4.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.1.4.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.4.1.4.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.1.4.1-2: General test parameters for FR1 in-sync testing in DRX mode

| Parameter |  |  |  | Unit | Value |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Test 1 |
| Active PCell |  |  |  |  | Cell 1 |
| RF Channel Number |  |  |  |  | 1 |
| BWchannel |  |  | Config 1 | MHz | 10: NPRB,c = 52 |
| DL initial BWP configuration |  |  | Config 1, 2 |  | DLBWP.0.1 |
| DL dedicated BWP configuration |  |  | Config 1, 2 |  | DLBWP.1.1 |
| UL initial BWP configuration |  |  | Config 1, 2 |  | ULBWP.0.1 |
| UL dedicated BWP configuration |  |  | Config 1, 2 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel |  |  | Config 1 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel |  |  | Config 1 |  | CCR.1.1 FDD |
| SSB Configuration |  |  | Config 1 |  | SSB.1 FR1 |
| SMTC Configuration |  |  | Config 1, 2 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing |  |  | Config 1, 2 |  | 15 kHz |
| PRACH Configuration |  |  | Config 1, 2 |  | Table  A.3.8.2.1-1 |
| SSB index assigned as RLM RS |  |  |  |  | 0 |
| OCNG parameters |  |  |  |  | OP.1 |
| CP length |  |  |  |  | Normal |
| Correlation Matrix and Antenna Configuration |  |  |  |  | 2x2 Low |
| In sync transmission parameters | DCI format |  |  |  | 1-0 |
|  | Number of Control OFDM symbols |  |  |  | 2 |
|  | Aggregation level |  |  | CCE | 4 |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy |  |  | dB | 0 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy |  |  | dB | 0 |
|  | DMRS precoder granularity |  |  |  | REG bundle size |
|  | REG bundle size |  |  |  | 6 |
| Out of sync transmission parameters | DCI format |  |  |  | 1-0 |
|  | Number of Control OFDM symbols |  |  |  | 2 |
|  | Aggregation level |  |  | CCE | 8 |
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
| CSI-RS configuration for CSI reporting |  | Config 1 |  |  | CSI-RS.1.1 FDD |
| CSI-RS for tracking |  | Config 1 |  |  | TRS.1.1 FDD |
| T1 |  |  |  | s | 0.2 |
| T2 |  |  |  | s | 0.2 |
| T3 |  |  |  | s | 0.64 |
| T4 |  |  |  | s | 0.2 |
| T5 |  |  |  | s | 0.88 |
| D1 |  |  |  | s | 0.84 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |

Table A.14.4.1.4.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in DRX mode

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
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15 kHz | -98 |  |  |  |  |
|  | Config 2 |  | -98 |  |  |  |  |
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1 | dBm/SCS | -98 |  |  |  |  |
|  | Config 2 |  | -98 |  |  |  |  |
| Propagation condition |  |  | NTN-TDLC5-200 |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 4: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2, SNR3, SNR4 and SNR5 respectively in figure A.6.5.1C.4.1-1.NOTE 5: Void. |  |  |  |  |  |  |  |

Table A.6.5.1C.4.1-4: Void

Table A.6.5.1C.4.1-5: Void

Figure A.14.4.1.4.1-1: SNR variation for in-sync testing.

##### A.14.4.1.4.2 Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.1.5 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode

##### A.14.4.1.5.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the SAN PCell when no DRX is used. This test will partly verify the FR1 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1C.

The test parameters are given in tables A.14.4.1.5.1-1, A.14.4.1.5.1-2, A.14.4.1.5.1-3, and A.14.4.1.5.1-3A below. There is one cell, Cell 1 which is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.14.4.1.5.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting of 5 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 is configured as the BFD-RS.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.4.1.5.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, FDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| 2 | NGSO, FDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

Table A.14.4.1.5.1-2: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in non-DRX mode

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| Active PCell |  |  | Cell 1 |
| RF Channel Number |  |  | 1 |
| Satellite information | Config 1 |  | SSC.1 |
|  | Config 2 |  | SSC.2 |
| Duplex mode | Config 1, 2 |  | FDD |
| DL initial BWP configuration | Config 1, 2 |  | DLBWP.0.1 |
| DL dedicated BWP configuration | Config 1, 2 |  | DLBWP.1.1 |
| UL initial BWP configuration | Config 1, 2 |  | ULBWP.0.1 |
| UL dedicated BWP configuration | Config 1, 2 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel | Config 1, 2 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel | Config 1, 2 |  | CCR.1.3 FDD |
| SSB Configuration | Config 1, 2 |  | SSB.1 FR1 |
| SMTC Configuration | Config 1, 2 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing | Config 1, 2 |  | 15 kHz |
| TRS configuration | Config 1, 2 |  | TRS.1.1 FDD |
| CSI-RS for RLM | Config 1, 2 |  | Resource #4 in TRS.1.1 FDD |
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
| CSI-RS configuration for CSI reporting | Config 1, 2 |  | CSI-RS.1.1 FDD |
| T1 |  | s | 0.2 |
| T2 |  | s | 0.48 |
| T3 |  | s | 0.48 |
| D1 |  | s | 0.44 |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |

Table A.14.4.1.5.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in non-DRX mode

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
| SNR on RLM-RS | Config 1, 2 | dB | 1 | -7 | -15 |
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1, 2 | dBm/15 kHz | -98 |  |  |
| Propagation condition |  |  | NTN-TDLC5-200 |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2 and T3 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.14.4.1.5.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4RX on all bands, the SNR during T3 is A.3.6. |  |  |  |  |  |

Table A.14.4.1.5.1-3A: Measurement gap configuration for FR1 CSI-RS out-of-sync radio link monitoring in non-DRX mode

| Field | Test 1 |
| --- | --- |
|  | Value |
| gapOffset | 0 |
| NOTE 1: Void |  |



![](media/image20.emf)

Figure A.14.4.1.5.1-1: SNR variation for CSI-RS out-of-sync testing

##### A.14.4.1.5.2 Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 no later than time point C (D1 ms after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.1.6 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode

##### A.14.4.1.6.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the SAN PCell when no DRX is used. This test will partly verify the FR1 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1C.

The test parameters are given in tables A.14.4.1.6.1-1, A.14.4.1.6.1-2, and A.14.4.1.6.1-3 below. There is one cells, Cell 1 which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.1.6.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled. In the test, SSB0 is configured as the BFD-RS.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.4.1.6.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, FDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| 2 | NGSO, FDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

Table A.14.4.1.6.1-2: General test parameters for FR1 PCell for CSI-RS in-sync testing in non-DRX mode

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| Active PCell |  |  | Cell 1 |
| RF Channel Number |  |  | 1 |
| Satellite information | Config 1 |  | SSC.1 |
|  | Config 2 |  | SSC.2 |
| Duplex mode | Config 1, 2 |  | FDD |
| DL initial BWP configuration | Config 1, 2 |  | DLBWP.0.1 |
| DL dedicated BWP configuration | Config 1, 2 |  | DLBWP.1.1 |
| UL initial BWP configuration | Config 1, 2 |  | ULBWP.0.1 |
| UL dedicated BWP configuration | Config 1, 2 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel | Config 1, 2 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel | Config 1, 2 |  | CCR.1.1 FDD |
| SSB Configuration | Config 1, 2 |  | SSB.1 FR1 |
| SMTC Configuration | Config 1, 2 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing | Config 1, 2 |  | 15 kHz |
| TRS configuration | Config 1, 2 |  | TRS.1.1 FDD |
| CSI-RS for RLM | Config 1, 2 |  | Resource #4 in TRS.1.1 FDD |
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
| CSI-RS configuration for CSI reporting | Config 1, 2 |  | CSI-RS.1.1 FDD |
| T1 |  | s | 0.2 |
| T2 |  | s | 0.2 |
| T3 |  | s | 0.44 |
| T4 |  | s | 0.2 |
| T5 |  | s | 0.88 |
| T6 |  | s | 0.84 |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |

Table A.14.4.1.6.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in non-DRX mode

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
| SNR on RLM-RS | Config 1, 2 | dB | 1 | -7 | -15 | -4.5 | 1 |
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1, 2 | dBm/15 kHz | -98 |  |  |  |  |
| Propagation condition |  |  | NTN-TDLC5-200 |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2, SNR3, SNR4 and SNR5 respectively in figure A.14.4.1.6.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4RX on all bands, the SNR during T3 is specified in clause A.3.6.1.1. |  |  |  |  |  |  |  |

Figure A.14.4.1.6.1-1: SNR variation for CSI-RS in-sync testing

##### A.14.4.1.6.2 Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.1.7 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode

##### A.14.4.1.7.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the SAN PCell when DRX is used. This test will partly verify the FR1 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1C.

The test parameters are given in tables A.14.4.1.7.1-1, A.14.4.1.7.1-2, and A.6.5.1.7C.1-3 below. There is one cell, Cell 1 is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.14.4.1.7.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test. In the test, SSB0 is configured as the BFD-RS.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.4.1.7.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, FDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| 2 | NGSO, FDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

Table A.14.4.1.7.1-2: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in DRX mode

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| Active PCell |  |  | Cell 1 |
| RF Channel Number |  |  | 1 |
| Satellite information | Config 1 |  | SSC.1 |
|  | Config 2 |  | SSC.2 |
| Duplex mode | Config 1, 2 |  | FDD |
| DL initial BWP configuration | Config 1, 2 |  | DLBWP.0.1 |
| DL dedicated BWP configuration | Config 1, 2 |  | DLBWP.1.1 |
| UL initial BWP configuration | Config 1, 2 |  | ULBWP.0.1 |
| UL dedicated BWP configuration | Config 1, 2 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel | Config 1, 2 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel | Config 1, 2 |  | CCR.1.3 FDD |
| SSB Configuration | Config 1, 2 |  | SSB.1 FR1 |
| SMTC Configuration | Config 1, 2 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing | Config 1, 2 |  | 15 kHz |
| TRS configuration | Config 1, 2 |  | TRS.1.1 FDD |
| CSI-RS for RLM | Config 1, 2 |  | Resource #4 in TRS.1.1 FDD |
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
| DRX |  |  | DRX.3 |
| Gap pattern ID |  |  | N.A. |
| Layer 3 filtering |  |  | Enabled |
| T310 timer |  | ms | 0 |
| T311 timer |  | ms | 1000 |
| N310 |  |  | 1 |
| N311 |  |  | 1 |
| CSI-RS configuration for CSI reporting | Config 1, 2 |  | CSI-RS.1.1 FDD |
| T1 |  | s | 0.2 |
| T2 |  | s | 1.28 |
| T3 |  | s | 1.28 |
| D1 |  | s | 1.24 |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |

Table A.14.4.1.7.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in DRX mode

| Parameter |  | Unit | Test 1 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| EPRE ratio of PDCCH DMRS to SSSPDCCH_beta |  | dB | 4 |  |  |
| EPRE ratio of PDCCH to PDCCH DMRSPDCCH_DMRS_beta |  | dB | 4 |  |  |
| EPRE ratio of PBCH DMRS to SSSPBCH_beta |  | dB | 0 |  |  |
| EPRE ratio of PBCH to PBCH DMRSPSS_beta |  | dB |  |  |  |
| EPRE ratio of PSS to SSSSSS_beta |  | dB |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS PDSCH_beta |  | dB |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |
| SNR on RLM-RS | Config 1, 2 | dB | 1 | -7 | -15 |
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1, 2 | dBm/15 kHz | -98 |  |  |
| Propagation condition |  |  | NTN-TDLC5-200 |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2 and T3 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.14.4.1.7.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4RX on all bands, the SNR during T3 is specified in clause A.3.6.1.1. |  |  |  |  |  |



![](media/image22.emf)

Figure A.14.4.1.7.1-1: SNR variation for CSI-RS out-of-sync testing

##### A.14.4.1.7.2 Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 (PCell) at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 (PCell) no later than time point C (D1 ms after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.1.8 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode

##### A.14.4.1.8.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the SAN PCell when DRX is used. This test will partly verify the FR1 Pcell CSI-RS In-sync radio link monitoring requirements in clause 8.1C.

The test parameters are given in tables A.14.4.1.8.1-1, A.14.4.1.8.1-2, A.14.4.1.8.1-3 and A.14.4.1.8.1-3A below. There is one cells, Cell 1 which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.1.8.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 is configured as the BFD-RS.

The UE shall be provided with the valid information about the SAN serving cells before the test.

Table A.14.4.1.8.1-1: Supported test configurations for FR1 PSCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, FDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| 2 | NGSO, FDD duplex mode, 15 kHz SSB SCS, 10 MHz bandwidth |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

Table A.14.4.1.8.1-2: General test parameters for FR1 PCell for CSI-RS in-sync testing in non-DRX mode

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| Active PCell |  |  | Cell 1 |
| RF Channel Number |  |  | 1 |
| Satellite information | Config 1 |  | SSC.1 |
|  | Config 2 |  | SSC.2 |
| Duplex mode | Config 1, 2 |  | FDD |
| DL initial BWP configuration | Config 1, 2 |  | DLBWP.0.1 |
| DL dedicated BWP configuration | Config 1, 2 |  | DLBWP.1.1 |
| UL initial BWP configuration | Config 1, 2 |  | ULBWP.0.1 |
| UL dedicated BWP configuration | Config 1, 2 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel | Config 1, 2 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel | Config 1, 2 |  | CCR.1.1 FDD |
| SSB Configuration | Config 1, 2 |  | SSB.1 FR1 |
| SMTC Configuration | Config 1, 2 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing | Config 1, 2 |  | 15 kHz |
| TRS configuration | Config 1, 2 |  | TRS.1.1 FDD |
| CSI-RS for RLM | Config 1, 2 |  | Resource #4 in TRS.1.1 FDD |
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
| DRX |  |  | DRX.3 |
| Gap pattern ID |  |  | gp0 |
| Layer 3 filtering |  |  | Enabled |
| T310 timer |  | ms | 2000 |
| T311 timer |  | ms | 1000 |
| N310 |  |  | 1 |
| N311 |  |  | 1 |
| CSI-RS configuration for CSI reporting | Config 1, 2 |  | CSI-RS.1.1 FDD |
| T1 |  | s | 0.2 |
| T2 |  | s | 0.2 |
| T3 |  | s | 1.24 |
| T4 |  | s | 0.2 |
| T5 |  | s | 1.88 |
| T6 |  | s | 1.84 |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |

Table A.14.4.1.8.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in non-DRX mode

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
| SNR on RLM-RS | Config 1, 2 | dB | 1 | -7 | -15 | -4.5 | 1 |
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1, 2 | dBm/15 kHz | -98 |  |  |  |  |
| Propagation condition |  |  | NTN-TDLC5-200 |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2, SNR3, SNR4 and SNR5 respectively in figure A.14.4.1.8.1-1.NOTE 9: The SNR values are specified for testing a UE which supports 2RX on at least one band. For testing of a UE which supports 4RX on all bands, the SNR during T3 is specified in clause A.3.6.1.1. |  |  |  |  |  |  |  |

Table A.6.5.1.8.1-3A: Measurement gap configuration for FR1 CSI-RS in-sync radio link monitoring in non-DRX mode

| Field | Test 1 |
| --- | --- |
|  | Value |
| gapOffset | 0 |
| NOTE 1: Void |  |

Figure A.14.4.1.8.1-1: SNR variation for CSI-RS in-sync testing

##### A.14.4.1.8.2 Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.1.9 Radio Link Monitoring Out-of-sync Test for FR2 SAN PCell configured with SSB-based RLM RS in non-DRX mode

##### A.14.4.1.9.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1C.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.14.4.1.9.1-1. The test parameters are given in tables A.14.4.1.9.1-2, A.14.4.1.9.1-3, and A.14.4.1.9.1-4 below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.14.4.1.9.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

The UE shall be provided with the valid information about the SAN serving each cell in the test before the test.

Table A.14.4.1.9.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 2 | NGSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 3 | GSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.1.9.1-2: General test parameters for FR2 out-of-sync testing in non-DRX mode

| Parameter |  | Unit | Value |  |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| Active PCell |  |  | Cell 1 |  |
| RF Channel Number |  |  | 1 |  |
| BWchannel | Config 1, 2 | MHz | 100: NPRB,c = 66 |  |
|  | Config 3, 4 |  | 10: NPRB,c = 24 |  |
| Data PRBs allocated | Config 1, 2, 3, 4 |  | 24 |  |
| DL initial BWP configuration | Config 1, 2, 3, 4 |  | DLBWP.0.1 |  |
| DL dedicated BWP configuration | Config 1, 2, 3, 4 |  | DLBWP.1.1 |  |
| UL initial BWP configuration | Config 1, 2, 3, 4 |  | ULBWP.0.1 |  |
| UL dedicated BWP configuration | Config 1, 2, 3, 4 |  | ULBWP.1.1 |  |
| RMSI CORESET Reference Channel | Config 1, 2 |  | [CR.2.1 FDD] |  |
|  | Config 3, 4 |  | CR.2.1 TDD |  |
| Dedicated CORESET Reference Channel | Config 1, 2 |  | [CCR.2.1 FDD] |  |
|  | Config 3, 4 |  | CCR 2.1 TDD |  |
| SSB Configuration | Config 1, 2 |  | SSB.1 FR2 |  |
|  | Config 3, 4 |  | SSB.1 FR1 |  |
| SMTC Configuration | Config 1, 2, 3, 4 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing | Config 1, 2 |  | 120 kHz |  |
|  | Config 3, 4 |  | 30 kHz |  |
| PRACH Configuration | Config 1, 2 |  | FR2 PRACH Configuration 1 |  |
|  | Config 3, 4 |  | FR1 PRACH Configuration 1 |  |
| SSB index assigned as RLM RS |  |  | 0 |  |
| OCNG parameters |  |  | OP.1 |  |
| CP length |  |  | Normal |  |
| Out of sync transmission parameters | DCI format |  | 1-0 |  |
|  | Number of Control OFDM symbols |  | 2 |  |
|  | Aggregation level | CCE | 8 |  |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy | dB | 4 |  |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy | dB | 4 |  |
|  | DMRS precoder granularity |  | REG bundle size |  |
|  | REG bundle size |  | 6 |  |
| DRX |  |  | OFF |  |
| Gap pattern ID |  |  | N.A. |  |
| Layer 3 filtering |  |  | Enabled |  |
| T310 timer |  | ms | 0 |  |
| T311 timer |  | ms | 1000 |  |
| N310 |  |  | 1 |  |
| N311 |  |  | 1 |  |
| CSI-RS configuration for CSI reporting | Config 1, 2 |  | [CSI-RS.2.1 FDD] |  |
|  | Config 3,4 |  | CSI-RS.1.1 FDD |  |
| CSI-RS for tracking | Config 1, 2 |  | [TRS.2.1 FDD] |  |
|  | Config 3, 4 |  | TRS1.2 TDD |  |
| T1 |  | s | 0.2 |  |
| T2 |  | s | 0.48 |  |
| T3 |  | s | 0.48 |  |
| D1 |  | s | 0.44 |  |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |

Table A.14.4.1.9.1-3: Cell specific test parameters for FR2 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| AoA setup |  |  | TBD |  |  |
| Assumption for UE beams |  |  | TBD |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 4 |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB | 0 |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |
| SNR on RLM-RS | Config 1 | dB | 2 | -6 | -15 |
|  | Config 2 |  | 2 | -6 | -15 |
| ![](media_svg/image23.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15 kHz | -92.1 |  |  |
|  | Config 2 |  | -92.1 |  |  |
| Propagation condition |  |  | TBD |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 4: The SNR in time periods T1, T2 and T3 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.6.5.1C.1.1-1. |  |  |  |  |  |

Table A.14.4.1.9.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

| Field | Test 1 |
| --- | --- |
|  | Value |
| gapOffset | 0 |

Figure A.14.4.1.9.1-1: SNR variation for out-of-sync testing

##### A.14.4.1.9.2 Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.1.10 Radio Link Monitoring In-sync Test for FR2 SAN PCell configured with SSB-based RLM RS in non-DRX mode

##### A.14.4.1.10.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the SAN PCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1C.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.14.4.1.10.1-1. The test parameters are given in tables A.14.4.1.10.1-2, and A.14.4.1.10.1-3 below. There is one cell (Cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.1.10.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.4.1.10.1-1: Supported test configurations for FR2 PCell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 2 | NGSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 3 | GSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.1.10.1-2: General test parameters for FR2 in-sync testing in non-DRX mode

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| Active PCell |  |  | Cell 1 |
| RF Channel Number |  |  | 1 |
| BWchannel | Config 1, 2 | MHz | 100: NPRB,c = 66 |
|  | Config 3, 4 |  | 10: NPRB,c = 24 |
| Data PRBs allocated | Config 1, 2, 3, 4 |  | 24 |
| DL initial BWP configuration | Config 1, 2, 3, 4 |  | DLBWP.0.1 |
| DL dedicated BWP configuration | Config 1, 2, 3, 4 |  | DLBWP.1.1 |
| UL initial BWP configuration | Config 1, 2, 3, 4 |  | ULBWP.0.1 |
| UL dedicated BWP configuration | Config 1, 2, 3, 4 |  | ULBWP.1.1 |
| RMSI CORESET Reference Channel | Config 1, 2 |  | [CR.2.1 FDD] |
|  | Config 3, 4 |  | CR.2.1 FDD |
| Dedicated CORESET Reference Channel | Config 1, 2 |  | [CCR.2.1 fDD] |
|  | Config 3, 4 |  | CCR.2.1 TDD |
| SSB Configuration | Config 1, 2 |  | SSB.1 FR2 |
|  | Config 3, 4 |  | SSB.1 FR1 |
| SMTC Configuration | Config 1, 2 |  | SMTC.1 |
| PDSCH/PDCCH subcarrier spacing | Config 1, 2 |  | 120 kHz |
|  | Config 3, 4 |  | 30 kHz |
| PRACH Configuration | Config 1, 2 |  | FR2 PRACH Configuration 1 |
|  | Config 3, 4 |  | FR1 PRACH Configuration 1 |
| SSB index assigned as RLM RS |  |  | 0 |
| OCNG parameters |  |  | OP.1 |
| CP length |  |  | Normal |
| In sync transmission parameters | DCI format |  | 1-0 |
|  | Number of Control OFDM symbols |  | 2 |
|  | Aggregation level | CCE | 4 |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy | dB | 0 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy | dB | 0 |
|  | DMRS precoder granularity |  | REG bundle size |
|  | REG bundle size |  | 6 |
| Out of sync transmission parameters | DCI format |  | 1-0 |
|  | Number of Control OFDM symbols |  | 2 |
|  | Aggregation level | CCE | 8 |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy | dB | 4 |
|  | DMRS precoder granularity |  | REG bundle size |
|  | REG bundle size |  | 6 |
| DRX |  |  | OFF |
| Gap pattern ID |  |  | N.A. |
| Layer 3 filtering |  |  | Enabled |
| T310 timer |  | ms | 1000 |
| T311 timer |  | ms | 1000 |
| N310 |  |  | 1 |
| N311 |  |  | 1 |
| CSI-RS configuration for CSI reporting | Config 1, 2 |  | [CSI-RS.2.1 FDD] |
|  | Config 3,4 |  | CSI-RS.1.1 FDD |
| CSI-RS for tracking | Config 1, 2 |  | [TRS.2.1 FDD] |
|  | Config 3, 4 |  | TRS 1.2 TDD |
| T1 |  | s | 0.2 |
| T2 |  | s | 0.2 |
| T3 |  | s | 0.24 |
| T4 |  | s | 0.2 |
| T5 |  | s | 0.88 |
| D1 |  | s | 0.84 |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |

Table A.14.4.1.10.1-3: Cell specific test parameters for FR2 (Cell 1) for in-sync radio link monitoring tests in non-DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 |
| AoA setup |  |  | TBD |  |  |  |  |
| Assumption for UE beams |  |  | TBD |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PBCH DMRS to SSS |  | dB | 0 |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS |  | dB |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS |  | dB |  |  |  |  |  |
| SNR on RLM-RS | Config 1 | dB | 2 | -6 | -15 | -4.5 | 2 |
|  | Config 2 |  | 2 | -6 | -15 | -4.5 | 2 |
| ![](media_svg/image23.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15 kHz | -98 |  |  |  |  |
|  | Config 2 |  | -98 |  |  |  |  |
| ![](media_svg/image23.svg) [公式≈: ^{N}oc] | Config 1 | dBm/SCS | -98 |  |  |  |  |
|  | Config 2 |  | -98 |  |  |  |  |
| Propagation condition |  |  | TBD |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 4: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2, SNR3, SNR4 and SNR5 respectively in figure A.6.5.1C.2.1-1. |  |  |  |  |  |  |  |

Figure A.14.4.1.10.1-1: SNR variation for in-sync testing

##### A.14.4.1.10.2 Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.1.11 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode

##### A.14.4.1.11.1 Test Purpose and Environment

The purpose of this test is to verify that the UE supporting support-3MHz-ChannelBW-r18 properly detects the out of sync for the purpose of monitoring downlink radio link quality of the PCell operating on a 3 MHz channel bandwidth. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1C.

Supported test configurations are specified in table A.14.4.1.11.1-1. General test parameters as specified in table A.14.4.1.1.1-2 with config 1 apply except those specified in table A.14.4.1.11.1-2. Cell specific test parameters as specified in table A.14.4.1.1.1-3 apply except those specified in table A.14.4.1.11.1-3.

The test procedure specified in clause A.14.4.1.1.1 applies to this test.

Table A.14.4.1.11.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | FDD duplex mode, 15 kHz SSB SCS, 3 MHz bandwidth |

Table A.14.4.1.11.1-2: General test parameters for FR1 OOS 15 PRB in non-DRX mode

| Parameter |  | Unit | Value |
| --- | --- | --- | --- |
|  |  |  | Test 1 |
| BWchannel | Config 1 | MHz | 3: NPRB,c = 15 |
| RMSI CORESET Reference Channel | Config 1 |  | CR.1.3 FDD |
| Dedicated CORESET Reference Channel | Config 1 |  | CCR.1.7 FDD |
| SSB Configuration | Config 1 |  | SSB.13 FR1 |
|  | DCI format |  | 1-0 |
|  | Number of Control OFDM symbols |  | 3 |
|  | Aggregation level | CCE | 4 |
| In sync transmission parameters | Ratio of hypothetical PDCCH RE energy to average SSS RE energy | dB | 0 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy | dB | 0 |
|  | Number of Control OFDM symbols |  | 3 |
|  | Aggregation level | CCE | 8 |
| Out of sync transmission parameters | Ratio of hypothetical PDCCH RE energy to average SSS RE energy | dB | 4 |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy | dB | 4 |
|  | REG bundle size |  | 6 |
|  | CP length |  | Normal |
|  | Mapping from REG to CCE |  | Non-Distributed |

Table A.14.4.1.11.1-3: Cell specific test parameters for FR1 PCell

| Parameter |  | Unit | Test 1 |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 |
| SNR_SSB of set q0 | Config 1 | dB | 2 | -6 | -14 |

##### A.14.4.1.11.2 Test Requirements

Test requirements specified in clause A.14.4.1.1.2 apply to this test.

#### A.14.4.1.12 Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode for less than 5 MHz BW


##### A.14.4.1.12.1 Test Purpose and Environment

The purpose of this test is to verify that the UE supporting support-3MHz-ChannelBW-r18 properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell operating on a 3 MHz channel bandwidth. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1C.

Supported test configurations are specified in table A.14.4.1.12.1-1. General test parameters as specified in table A.14.4.1.4.1-2 with config 1 apply to this test, except those specified in table A.14.4.1.12.1-2. Cell specific test parameters as specified in table A.14.4.1.4.1-3 apply except those specified in table A.14.4.1.12.1-3.

The test procedure specified in clause A.14.4.1.4.1 applies to this test.

Table A.14.4.1.12.1-1: Supported test configurations for FR1 PCell

| Configuration | Description |
| --- | --- |
| 1 | FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 3 MHz (15PRB) |
| NOTE: The UE is required to pass the test with configuration 1 for every supported 3 MHz band in FR1. |  |

Table A.14.4.1.12.1-2: General test parameters for FR1 in-sync testing in DRX mode

| Parameter |  |  | Unit | Value |  |
| --- | --- | --- | --- | --- | --- |
| Parameter |  | Unit |  |  | Value |
|  |  |  |  |  | Test 1 |
| BWchannel | Config 1 | MHz |  |  | 3: NRB,c = 15 |
| RMSI CORESET Reference Channel | Config 1 |  |  |  | CR.1.3 FDD |
| Dedicated CORESET Reference Channel | Config 1 |  |  |  | CCR.1.7 FDD |
| SSB Configuration | Config 1 |  |  |  | SSB.13 FR1 |
| In sync transmission parameters | Number of Control OFDM symbols, Config 1 |  |  |  | 3 |
|  | Aggregation level, Config 1 | CCE |  |  | 4 |
|  | Mapping from REG to CCE, Config 1 | Config 1 |  |  | Non-Distributed |
| Out of sync transmission parameters | Number of Control OFDM symbols, Config 1 |  |  |  | 3 |
|  | Aggregation level, Config 1 | CCE |  |  | 8 |
|  | Mapping from REG to CCE, Config 1 | Config 1 |  |  | Non-Distributed |

Table A.14.4.1.12.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in DRX mode

| Parameter |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 |
| SNR on RLM-RS | Config 1 | dB | 2 | -6 | -14 | -2.5 | 3 |

##### A.14.4.1.12.2 Test Requirements

Test requirements specified in clause A.14.4.1.4.2 apply to this test.

### A.14.4.2 Beam Failure Detection and Link recovery procedures for satellite access

#### A.14.4.2.1 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode

##### A.14.4.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell which is served by satellite access node (SAN) and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.14.4.2.1.1-1, A.14.4.2.1.1-2, A.14.4.2.1.1-3 and A.14.4.2.1.1-4 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.2.1.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.14.4.2.1.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

Table A.14.4.2.1.1-1: Supported test configurations for FR1 Pcell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.2.1.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |  |
| NTN reference Serving satellite configuration |  | Config 1 |  | SSC.1 |  |
|  |  | Config 2 |  | SSC.2 |  |
| Active PSCell |  |  |  | Cell 1 |  |
| RF Channel Number |  |  |  | 1 |  |
| Duplex mode |  | Config 1,2 |  | FDD |  |
| BWchannel |  | Config 1,2 | MHz | 10: NRB,c = 52 |  |
| DL initial BWP configuration |  | Config 1,2 |  | DLBWP.0.1 |  |
| DL dedicated BWP configuration |  | Config 1,2 |  | DLBWP.1.1 |  |
| UL initial BWP configuration |  | Config 1,2 |  | ULBWP.0.1 |  |
| UL dedicated BWP configuration |  | Config 1,2 |  | ULBWP.1.1 |  |
| TDD Configuration |  | Config 1,2 |  | Not Applicable |  |
| RMSI CORESET Reference Channel |  | Config 1,2 |  | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1,2 |  | CCR.1.1 FDD |  |
| SSB Configuration |  | Config 1,2 |  | SSB.3 FR1 |  |
| SMTC Configuration |  | Config 1,2 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 |  | 15 KHz |  |
| PRACH Configuration |  | Config 1,2 |  | Table  A.3.8.2.2-1 |  |
| SSB Index assigned as BFD RS (q0) |  |  |  | 0 |  |
| SSB Index assigned as CBD RS (q1) |  |  |  | 1 |  |
| OCNG parameters |  |  |  | OP.1 |  |
| CP length |  |  |  | Normal |  |
| Correlation Matrix and Antenna Configuration |  |  |  | 2x2 Low |  |
| Beam failure detection transmission parameters |  | DCI format |  | 1-0 |  |
|  |  | Number of Control OFDM symbols |  | 2 |  |
|  |  | Aggregation level | CCE | 8 |  |
|  |  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy | dB | 0 |  |
|  |  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy | dB | 0 |  |
|  |  | DMRS precoder granularity |  | REG bundle size |  |
|  |  | REG bundle size |  | 6 |  |
| DRX |  |  |  | OFF |  |
| Gap pattern ID |  |  |  | gp0 |  |
| gapOffset |  |  |  | 0 |  |
| rlmInSyncOutOfSyncThreshold |  |  |  | absent | When the field is absent, the UE applies the value 0. (Table 8.1.1-1). |
| rsrp-ThresholdSSB | Config 1, 2 |  | dBm/SCS kHz | -98 | Threshold used for Qin_LR_SSB |
|  |  |  |  |  |  |
| powerControlOffsetSS |  |  |  | db0 | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  |  |  | n1 | see clause 5.17 of TS 38.321 [7] |
| beamFailureDetectionTimer |  |  |  | pbfd4 | see clause 5.17 of TS 38.321 [7] |
| CSI-RS configuration  for CSI reporting |  | Config 1,2 |  | CSI-RS.1.1 FDD |  |
| CSI-RS for tracking |  | Config 1,2 |  | TRS.1.1 FDD |  |
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

Table A.14.4.2.1.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

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
| SNR_SSB of set q0 | Config 1,2 | dB | 5 | -3 | -12 | -12 | -12 |
| SNR_SSB of set q1 | Config 1,2 | dB | -10 | -10 | 10 | 10 | 10 |
| SSB_RP of set q1 | Config 1,2 | dBm/SCS kHz | -108 | -108 | -88 | -88 | -88 |
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1,2 | dBm/15 KHz | -98 |  |  |  |  |
| Propagation condition |  |  | NTN-TDLC5-200 |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: Measurement gap configuration is assigned to the UE prior to the start of time period T1.NOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.4.5.5.1.1-1.NOTE 9: Void. |  |  |  |  |  |  |  |

![](media/C:\Users\w00527694\Pictures\图片28.png)

Figure A.14.4.2.1.1-1: SNR and L1-RSRP variation SSB for SSB-based beam failure detection and link recovery testing in non-DRX mode

##### A.14.4.2.1.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 120+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.2.2 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in DRX mode

##### A.14.4.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell which is served by satellite access node (SAN) and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.14.4.2.2.1-1, A.14.4.2.2.1-2, A.14.4.2.2.1-3, A.14.4.2.2.1-4 and A.14.4.2.2.1-5 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.2.2.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.14.4.2.2.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.14.4.2.2.1-1: Supported test configurations for FR1 Pcell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.2.2.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| NTN reference Serving satellite configuration | Config 1 |  | SSC.1 |  |
|  | Config 2 |  | SSC.2 |  |
| Active PSCell |  |  | Cell 1 |  |
| RF Channel Number |  |  | 1 |  |
| Duplex mode | Config 1,2 |  | FDD |  |
| BWchannel | Config 1,2 | MHz | 10: NRB,c = 52 |  |
| DL initial BWP configuration | Config 1,2 |  | DLBWP.0.1 |  |
| DL dedicated BWP configuration | Config 1,2 |  | DLBWP.1.1 |  |
| UL initial BWP configuration | Config 1,2 |  | ULBWP.0.1 |  |
| UL dedicated BWP configuration | Config 1,2 |  | ULBWP.1.1 |  |
| TDD Configuration | Config 1,2 |  | Not Applicable |  |
| RMSI CORESET Reference Channel | Config 1,2 |  | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel | Config 1,2 |  | CCR.1.1 FDD |  |
| SSB Configuration | Config 1,2 |  | SSB.3 FR1 |  |
| SMTC Configuration | Config 1,2 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing | Config 1,2 |  | 15 KHz |  |
| PRACH Configuration | Config 1,2 |  | Table  A.3.8.2.2-1 |  |
| SSB Index assigned as BFD RS (q0) |  |  | 0 |  |
| SSB Index assigned as CBD RS (q1) |  |  | 1 |  |
| OCNG parameters |  |  | OP.1 |  |
| CP length |  |  | Normal |  |
| Correlation Matrix and Antenna Configuration |  |  | 2x2 Low |  |
| Beam failure detection transmission parameters | DCI format |  | 1-0 |  |
|  | Number of Control OFDM symbols |  | 2 |  |
|  | Aggregation level | CCE | 8 |  |
|  | Ratio of hypothetical PDCCH RE energy to average SSS RE energy | dB | 0 |  |
|  | Ratio of hypothetical PDCCH DMRS energy to average SSS RE energy | dB | 0 |  |
|  | DMRS precoder granularity |  | REG bundle size |  |
|  | REG bundle size |  | 6 |  |
| DRX |  |  | DRX.7 | A.3.3.7 |
| Gap pattern ID |  |  | N.A. |  |
| rlmInSyncOutOfSyncThreshold |  |  | Absent | When the field is absent, the UE applies the value 0. (Table 8.1.1-1). |
| rsrp-ThresholdSSB | Config 1,2 | dBm/SCS kHz | -98 | Threshold used for Qin_LR_SSB |
| powerControlOffsetSS |  |  | db0 | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  |  | n1 | see clause 5.17 of TS 38.321 [7] |
| beamFailureDetectionTimer |  |  | pbfd4 | see clause 5.17 of TS 38.321 [7] |
| CSI-RS configuration for CSI reporting | Config 1,2 |  | CSI-RS.1.1 FDD |  |
| CSI-RS for tracking | Config 1,2 |  | TRS.1.1 FDD |  |
| SSB Index assigned as RLM RS |  |  | 0, 1 |  |
| T310 Timer |  | ms | 1000 |  |
| N310 |  |  | 2 |  |
| T1 |  | s | 1 | During this time the the UE shall be fully synchronized to Cell 1 |
| T2 |  | s | 5.17 |  |
| T3 |  | s | 3.24 |  |
| T4 |  | s | 0 |  |
| T5 |  | s | 1.97 |  |
| D1 |  | s | 1.93 |  |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |

Table A.14.4.2.2.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

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
| SNR_SSB of set q0 | Config 1,2 | dB | 5 | -3 | -12 | -12 | -12 |
| SNR_SSB of set q1 | Config 1,2 | dB | -10 | -10 | 10 | 10 | 10 |
| SSB_RP of set q1 | Config 1,2 | dBm/SCS kHz | -108 | -108 | -88 | -88 | -88 |
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1,2 | dBm/15 KHz | -98 |  |  |  |  |
| Propagation condition |  |  | NTN-TDLC5-200 |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: VoidNOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.4.5.5.1.1-1.NOTE 9: Void. |  |  |  |  |  |  |  |

![](media/C:\Users\w00527694\Pictures\图片28.png)

Figure A.14.4.2.2.1-1: SNR and L1-RSRP variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

##### A.14.4.2.2.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 1920+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.2.3 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in non-DRX mode

##### A.14.4.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell which is served by satellite access node (SAN) and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.14.4.2.3.1-1, A.14.4.2.3.1-2, and below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.2.3.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.14.4.2.3.1-1 additionally shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

Table A.14.4.2.3.1-1: Supported test configurations for FR1 Pcell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.2.3.1-2: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

| Parameter |  |  |  |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | Test 1 |  |
| NTN reference Serving satellite configuration | Config 1 |  |  |  |  | SSC.1 |  |
|  | Config 2 |  |  |  |  | SSC.2 |  |
| Active PCell |  |  |  |  |  | Cell 1 |  |
| RF Channel Number |  |  |  |  |  | 1 |  |
| Duplex mode |  |  | Config 1,2 |  |  | FDD |  |
| TDD Configuration |  |  | Config 1,2 |  |  | Not Applicable |  |
| RMSI CORESET Reference Channel |  |  | Config 1,2 |  |  | CR.1.1 FDD | A.3.1.2 |
| Dedicated CORESET Reference Channel |  |  | Config 1,2 |  |  | CCR.1.1 FDD | A.3.1.3 |
| SSB Configuration |  |  | Config 1,2 |  |  | SSB.3 FR1 | A.3.10 |
| SSB Configuration |  |  | Config 1,2 |  |  | SSB. 3  FR1 | A.3.10 |
| SMTC Configuration |  |  | Config 1,2 |  |  | SMTC.1 | A.3.11 |
| PDSCH/PDCCH subcarrier spacing |  |  | Config 1,2 |  |  | 15 KHz |  |
| PRACH Configuration |  |  | Config 1,2 |  |  | FR1 PRACH configuration 4 | A.3.8.2 |
| csi-RS-Index assigned as beam failure detection RS in set q0 |  |  |  |  |  | 0 |  |
| OCNG parameters |  |  |  |  |  | OP.1 | A.3.2.1 |
| CP length |  |  |  |  |  | Normal |  |
| Correlation Matrix and Antenna Configuration |  |  |  |  |  | 2x2 Low |  |
| Beam failure detection transmission parameters |  |  | DCI format |  |  | 1-0 |  |
|  |  |  | Number of Control OFDM symbols |  |  | 2 |  |
|  |  |  | Aggregation level |  | CCE | 8 |  |
|  |  |  | Ratio of hypothetical PDCCH RE energy to average CSI-RS RE energy |  | dB | 0 |  |
|  |  |  | Ratio of hypothetical PDCCH DMRS energy to average CSI-RS RE energy |  | dB | 0 |  |
|  |  |  | DMRS precoder granularity |  |  | REG bundle size |  |
|  |  |  | REG bundle size |  |  | 6 |  |
| DRX |  |  |  |  |  | OFF |  |
| Gap pattern ID |  |  |  |  |  | N.A. |  |
| csi-RS-Index assigned as candidate beam detection RS in set q1 |  |  |  |  |  | 1 | N |
| rlmInSyncOutOfSyncThreshold |  |  |  |  |  | absent | When the field is absent, the UE applies the value 0. (Table 8.1.1-1). |
| rsrp-ThresholdSSB |  | Config 1,2 |  |  | dBm/SCS kHz | -98 | Threshold used for Qin_LR_SSB |
| powerControlOffsetSS |  |  |  |  |  | db0 | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  |  |  |  |  | n1 | see clause 5.17 of TS 38.321 [7] |
| beamFailureDetectionTimer |  |  |  |  |  | pbfd4 | see clause 5.17 of TS 38.321 [7] |
| CSI-RS configuration for q0 and q1 |  |  |  | Config 1,2 |  | CSI-RS.1.2 FDD | A.3.14 |
| CSI-RS configuration for CSI reporting |  |  |  | Config 1,2 |  | CSI-RS.1.1 FDD | A.3.14 |
| TRS configuration |  |  |  | Config 1,2 |  | TRS.1.1 FDD |  |
| CSI-RS-Index assigned as RLM RS |  |  |  | Config 1,2 |  | CSI-RS.1.2 FDD | A.3.14 |
| T310 Timer |  |  |  |  | ms | 1000 |  |
| N310 |  |  |  |  |  | 2 |  |
| T1 |  |  |  |  | s | 0.2 | During this time the the UE shall be fully synchronized to Cell 1 |
| T2 |  |  |  |  | s | 0.18 |  |
| T3 |  |  |  |  | s | 0.14 |  |
| T4 |  |  |  |  | s | 0 |  |
| T5 |  |  |  |  | s | 0.08 |  |
| D1 |  |  |  |  | s | 0.04 |  |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |  |  |

Table A.14.4.2.3.1-3 Cell specific test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

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
| SNR_CSI-RS of set q0 | Config 1,2 | dB | 5 | -3 | -12 | -12 | -12 |
| SNR_CSI-RS of set q1 | Config 1,2 | dB | -10 | -10 | 10 | 10 | 10 |
| CSI-RS_RP of set q1 | Config 1,2 | dBm/SCS kHz | -108 | -108 | -88 | -88 | -88 |
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1,2 | dBm/15 KHz | -98 |  |  |  |  |
| Propagation condition |  |  | NTN-TDLC5-200 |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: VoidNOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the REs carrying CSI-RS.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.4.5.5.1.1-1.NOTE 9: Void. |  |  |  |  |  |  |  |

![](media/C:\Users\w00527694\Pictures\图片29.png)

Figure A.14.4.2.3.1-1: SNR and L1-RSRP variation for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

##### A.14.4.2.3.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 30+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.2.4 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in DRX mode

##### A.14.4.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell which is served by satellite access node (SAN) and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.14.4.2.4.1-1, A.14.4.2.4.1-2, A.14.4.2.4.1-3, and A.14.4.2.4.1-4 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.14.4.2.4.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.14.4.2.4.1-1 additionally shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.14.4.2.4.1-1: Supported test configurations for FR1 Pcell

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.2.4.1-2: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

| Parameter |  |  |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Test 1 |  |
| NTN reference Serving satellite configuration | Config 1 |  |  |  | SSC.1 |  |
|  | Config 2 |  |  |  | SSC.2 |  |
| Active PCell |  |  |  |  | Cell 1 |  |
| RF Channel Number |  |  |  |  | 1 |  |
| Duplex mode |  | Config 1,2 |  |  | FDD |  |
| TDD Configuration |  | Config 1,2 |  |  | Not Applicable |  |
| RMSI CORESET Reference Channel |  | Config 1,2 |  |  | CR.1.1 FDD | A.3.1.2 |
| Dedicated CORESET Reference Channel |  | Config 1,2 |  |  | CCR.1.1 FDD | A.3.1.3 |
| SSB Configuration |  | Config 1,2 |  |  | SSB. 3  FR1 | A.3.10 |
| SMTC Configuration |  | Config 1,2 |  |  | SMTC.1 | A.3.11 |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 |  |  | 15 KHz |  |
| PRACH Configuration |  | Config 1,2 |  |  | FR1 PRACH configuration 4 | A.3.8.2 |
| csi-RS-Index assigned as beam failure detection RS in set q0 |  |  |  |  | 0 |  |
| OCNG parameters |  |  |  |  | OP.1 | A.3.2.1 |
| CP length |  |  |  |  | Normal |  |
| Correlation Matrix and Antenna Configuration |  |  |  |  | 2x2 Low |  |
| Beam failure detection transmission parameters |  | DCI format |  |  | 1-0 |  |
|  |  | Number of Control OFDM symbols |  |  | 2 |  |
|  |  | Aggregation level |  | CCE | 8 |  |
|  |  | Ratio of hypothetical PDCCH RE energy to average CSI-RS RE energy |  | dB | 0 |  |
|  |  | Ratio of hypothetical PDCCH DMRS energy to average CSI-RS RE energy |  | dB | 0 |  |
|  |  | DMRS precoder granularity |  |  | REG bundle size |  |
|  |  | REG bundle size |  |  | 6 |  |
| DRX |  |  |  |  | DRX.7 | A.3.3.7 |
| Gap pattern ID |  |  |  |  | N.A. |  |
| csi-RS-Index assigned as candidate beam detection RS in set q1 |  |  |  |  | 1 |  |
| rlmInSyncOutOfSyncThreshold |  |  |  |  | absent | When the field is absent, the UE applies the value 0. (Table 8.1.1-1). |
| rsrp-ThresholdSSB |  |  | Config 1,2 | dBm/SCS kHz | -98 | Threshold used for Qin_LR_SSB |
| powerControlOffsetSS |  |  |  |  | db0 | Used for deriving rsrp-ThresholdCSI-RS |
| beamFailureInstanceMaxCount |  |  |  |  | n1 | see clause 5.17 of TS 38.321 [7] |
| beamFailureDetectionTimer |  |  |  |  | pbfd4 | see clause 5.17 of TS 38.321 [7] |
| CSI-RS configuration for q0 and q1 |  | Config 1,2 |  |  | CSI-RS.1.2 FDD | A.3.14.1 |
| CSI-RS configuration for CSI reporting |  | Config 1,2 |  |  | CSI-RS.1.1 FDD | A.3.14.1 |
| TRS configuration |  | Config 1,2 |  |  | TRS.1.1 FDD |  |
| CSI-RS-Index assigned as RLM RS |  | Config 1,2 |  |  | CSI-RS.1.2 FDD |  |
| T310 Timer |  |  |  | ms | 1000 |  |
| N310 |  |  |  |  | 2 |  |
| T1 |  |  |  | s | 1 | During this time the the UE shall be fully synchronized to Cell 1 |
| T2 |  |  |  | s | 8.37 |  |
| T3 |  |  |  | s | 6.44 |  |
| T4 |  |  |  | s | 0 |  |
| T5 |  |  |  | s | 1.97 |  |
| D1 |  |  |  | s | 1.93 |  |
| NOTE 1: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |  |

Table A.14.4.2.4.1-3: Cell specific test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

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
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| SNR_CSI-RS of set q1 | Config 1 | dB | -10 | -10 | 10 | 10 | 10 |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| CSI-RS_RP of set q1 | Config 1 | dB/SCS kHz | -108 | -108 | -88 | -88 | -88 |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| ![](media_svg/image17.svg) [公式≈: ^{N}oc] | Config 1 | dBm/15 KHz | -98 |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| Propagation condition |  |  | NTN-TDLC5-200 |  |  |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The uplink resources for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 3: NZP CSI-RS resource set configuration for CSI reporting are assigned to the UE prior to the start of time period T1.NOTE 4: VoidNOTE 5: The timers and layer 3 filtering related parameters are configured prior to the start of time period T1.NOTE 6: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 7: SNR levels correspond to the signal to noise ratio over the REs carrying CSI-RS.NOTE 8: The SNR in time periods T1, T2, T3, T4 and T5 is denoted as SNR1, SNR2 and SNR3 respectively in figure A.4.5.5.1.1-1.NOTE 9: Void. |  |  |  |  |  |  |  |

![](media/C:\Users\w00527694\Pictures\图片29.png)

Figure A.14.4.2.4.1-1: SNR and L1-RSRP variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

##### A.14.4.2.4.2 Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 1920+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.2.5 Void

#### A.14.4.2.6 Void

#### A.14.4.2.7 Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode for a UE operating on a cell with less than 5 MHz BW

##### A.14.4.2.7.1 Test Purpose and Environment

The purpose of this test is to verify that the UE supporting support-3MHz-ChannelBW-r18 properly detects SSB-based beam failure in the set q0 configured for a serving cell which is served by satellite access node (SAN) and operatw on a less than 5 MHz bandwidth, and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell which is served by satellite access node (SAN) requirements in clause 8.5C for a UE operating on a cell with less than 5 MHz BW.

Supported test configurations are specified in table A.14.4.2.7.1-1. General test parameters as specified in table A.14.4.2.2.1-2 with config 1 apply except those specified in table A.14.4.2.7.1-2. Cell specific test parameters as specified in table A.14.4.2.2.1-3 apply except those specified in table A.14.4.2.7.1-3.

The test procedure specified in clause A.14.4.2.2.1 applies to this test.

Table A.14.4.2.7.1-1: Supported test configurations for FR1 Pcell with less than 5 MHz BW

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.2.7.1-2: General test parameters for FR1 PCell with less than 5 MHz BW

| Parameter |  |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Test 1 |  |
| BWchannel |  | Config 1 | MHz | 3: NPRB,c = 15 |  |
| SSB Configuration |  | Config 1 |  | SSB.13 FR1 |  |
| PRACH Configuration |  | Config 1 |  | 1 |  |
| Beam failure detection transmission parameters | Number of Control OFDM symbols |  |  | 3 |  |
|  | Aggregation level |  | CCE | 8 |  |
|  | Mapping from REG to CCE |  |  | Non-Distributed |  |
| T1 |  |  | s | 1 | During this time the the UE shall be fully synchronized to Cell 1 |
| T2 |  |  | s | 5.17 |  |
| T3 |  |  | s | 3.24 |  |
| T4 |  |  | s | 0 |  |
| T5 |  |  | s | 1.97 |  |
| D1 |  |  | s | 1.94 |  |
| NOTE 1: All configurations are assigned to the UE prior to the start of time period T1.NOTE 2: UE-specific PDCCH is not transmitted after T1 starts. |  |  |  |  |  |

Table A.14.4.2.7.1-3: Cell specific test parameters for FR1 PCell with less than 5 MHz BW

| Parameter |  | Unit | Test 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T3 | T4 | T5 |
| SNR_SSB of set q0 | Config 1 | dB | 6 | -2 | -11 | -11 | -11 |

##### A.14.4.2.7.2 Test Requirements

Test requirements specified in clause A.14.4.2.2.1 apply to this test.


### A.14.4.3 Active BWP switch for satellite access


#### A.14.4.3.1 DCI-based and Timer-based Active BWP Switch

##### A.14.4.3.1.1 NR FR1 DL active BWP switch with non-DRX in SA

###### A.14.4.3.1.1.1 Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6C.

The supported test configurations are shown in table A.14.4.3.1.1.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.14.4.3.1.1.1-2. Cell-specific parameters of the cell are specified in table A.14.4.3.1.1.1-3 below.

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

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6C and starts to report valid ACK/NACK for the Cell 1 no later than the first UL slot that occurs after the beginning of slot ($ i+T_{BWPswitchDelay}+k1+2^{µ-µ_{K_{offset}}}K_{offset}$). The UE shall be continuously scheduled on Cell 1’s BWP-2 starting from the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).

During T2, the test equipment won’t transmit DCI format for PDSCH reception on Cell 1.

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the subframe immediately after bwp-InactivityTimer timer expires. The UE shall switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s slot (j+TBWPswitchDelay) as defined in clause 8.6C and starts to report valid ACK/NACK for the Cell 1 at latest on the first UL slot that occurs after the beginning of slot ($ j+T_{BWPswitchDelay}+k1+2^{µ-µ_{K_{offset}}}K_{offset}$). The UE shall be continuously scheduled on Cell 1’s BWP-1 starting from the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

The test equipment verifies the DL BWP switch time by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK/NACK is received.

Table A.14.4.3.1.1.1-1: DL BWP switch supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.3.1.1.1-2: General test parameters for DL BWP switch in SA

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active Cell |  | Cell 1 | Cell 1 on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| bwp-InactivityTimer | ms | 200 |  |
| T1 | s | 0.2 |  |
| T2 | s | 0.2 |  |
| T3 | s | 0.2 |  |

Table A.14.4.3.1.1.1-3 : NR Cell specific test parameters for DL BWP switch in SA

| Parameter |  |  | Unit | Cell 1 |
| --- | --- | --- | --- | --- |
| Frequency Range |  |  |  | FR1 |
| Duplex mode |  | Config 1, 2 |  | FDD |
| BWchannel |  | Config 1, 2 |  | 10 MHz: NPRB,c = 52 |
| Satellite information |  | Config 1 |  | SSC.1 |
|  |  | Config 2 |  | SSC.2 |
| Active BWP ID |  |  |  | 1, 2 |
| Initial DL BWP Configuration |  | Config 1, 2 |  | DLBWP.0.2 Note 4 |
| Active DL BWP-1 Configuration |  | Config 1, 2 |  | DLBWP.1.1 Note 4 |
| Active DL BWP-2 Configuration |  | Config 1, 2 |  | DLBWP.1.3 Note 4 |
| Initial UL BWP Configuration |  | Config 1, 2 |  | ULBWP.0.2 Note 4 |
| Active UL BWP-1 Configuration |  | Config 1, 2 |  | ULBWP.1.1 Note 4 |
| Active UL BWP-2 Configuration |  | Config 1, 2 |  | N/A |
| PDSCH Reference measurement channel |  | Config 1, 2 |  | SR.1.1 FDD |
| RMSI CORESET parameters |  | Config 1, 2 |  | CR.1.1 FDD |
| Dedicated CORESET parameters |  | Config 1, 2 |  | CCR.1.2 FDD |
| OCNG Patterns |  |  |  | OP.1 |
| SSB Configuration |  | Config 1, 2 |  | SSB.1 FR1 |
| SMTC Configuration |  | Config 1, 2 |  | SMTC.1 |
| Correlation Matrix and Antenna Configuration |  |  |  | 1x2 Low |
| TRS Configuration |  | Config 1, 2 |  | TRS.1.1 FDD |
| EPRE ratio of PSS to SSS |  |  | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |
| NocNote 2 | Config 1, 2 |  | dBm/SCS | -104 |
| NocNote 2 |  |  | dBm/15 kHz | -104 |
| SS-RSRP Note 3 | Config 1, 2 |  | dBm/SCS | -87 |
| Ês/Iot |  |  | dB | 17 |
| Ês/Noc |  |  | dB | 17 |
| IoNote3 |  | Config 1, 2 | dBm/9.36 MHz | -58.96 |
| Propagation Condition |  |  |  | AWGN |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |

###### A.14.4.3.1.1.2 Test Requirements

During T1, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot ($ i+T_{BWPswitchDelay}+k1+2^{µ-µ_{K_{offset}}}K_{offset}$).

During T3, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot ($ j+T_{BWPswitchDelay}+k1+2^{µ-µ_{K_{offset}}}K_{offset}$.

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6C.2-1.

All of the above test requirements shall be fulfilled in order for the observed Cell 1 active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

#### A.14.4.3.2 RRC-based Active BWP Switch

##### A.14.4.3.2.1 NR FR1 DL active BWP switch of Cell with non-DRX in SA

###### A.14.4.3.2.1.1 Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6C.

The supported test configurations are shown in table A.14.4.3.2.1.1-1. The test scenario comprises of one Cell (Cell 1) as given in table A.14.4.3.2.1.1-2. Cell-specific parameters of Cell are specified in table A.14.4.3.2.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.


Before the test starts,

- UE is connected to Cell 1 on radio channel 1.

- UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1.

- UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in Cell 1.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is completely received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition.

The UE shall be able to receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot ($ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}$) as defined in clause8.6C.3 and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot ($ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}+k1+2^{µ-µ_{K_{offset}}}K_{offset}$) on BWP-1 of final condition. The UE shall be continuously scheduled on PCell’s BWP-1 of final condition starting from the first DL slot right after slot ($ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}$).

TRRCprocessingDelay and TBWPswitchDelayRRC are defined in clause 8.6C.3.

The test equipment verifies the DL BWP switch time in Cell by counting the time from the time when the RRC Reconfiguration message including updated BWP configuration is sent till the time when a vaild ACK/NACK is received is received.

Table A.14.4.3.2.1.1-1: DL BWP switch supported test configurations in SA scenario

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.3.2.1.1-2: General test parameters for DL BWP switch in SA scenario

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active Cell |  | Cell 1 | Cell on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| T1 | s | 0.2 |  |

Table A.14.4.3.2.1.1-3: NR Cell specific test parameters for DL BWP switch in SA scenario

| Parameter |  |  | Unit | Cell 1 |
| --- | --- | --- | --- | --- |
| Frequency Range |  |  |  | FR1 |
| Duplex mode |  | Config 1, 2 |  | FDD |
| BWchannel |  | Config 1, 2 |  | 10 MHz: NPRB,c = 52 |
| Satellite information |  | Config 1 |  | SSC.1 |
|  |  | Config 2 |  | SSC.2 |
| Active BWP ID |  |  |  | 1 |
| Initial DL BWP Configuration |  | Config 1, 2 |  | DLBWP.0.2 |
| Initial UL BWP Configuration |  | Config 1, 2 |  | ULBWP.0.2 |
| Initial Condition | Active DL BWP-1 Configuration | Config 1, 2 |  | DLBWP.1.3 |
|  | Active UL BWP-1 Configuration | Config 1, 2 |  | ULBWP.1.3 |
| FinalCondition | Active DL BWP-1 Configuration | Config 1, 2 |  | DLBWP.1.1 |
|  | Active UL BWP-1 Configuration | Config 1, 2 |  | ULBWP.1.1 |
| PDSCH Reference measurement channel |  | Config 1, 2 |  | SR.1.1 FDD |
| RMSI CORESET parameters |  | Config 1, 2 |  | CR.1.1 FDD |
| Dedicated CORESET parameters |  | Config 1, 2 |  | CCR.1.2 FDD |
| OCNG Patterns |  |  |  | OP.1 |
| SSB Configuration |  | Config 1, 2 |  | SSB.1 FR1 |
| SMTC Configuration |  |  |  | SMTC.1 |
| TRS Configuration |  | Config 1, 2 |  | TRS.1.1 FDD |
| Antenna Configuration |  |  |  | 1x2 Low |
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
| NocNote 2 |  | Config 1, 2 | dBm/SCS | -104 |
| SS-RSRP Note 3 |  | Config 1, 2 | dBm/SCS | -87 |
| Ês/Iot |  |  | dB | 17 |
| Ês/Noc |  |  | dB | 17 |
| IoNote3 |  | Config 1, 2 | dBm/9.36 MHz | -58.96 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |

###### A.14.4.3.2.1.2 Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the Cell from the first DL slot that occurs right after the begining of slot ($ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}$) and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot ($ i+\frac {T_{RRCprocessingDelay}+T_{BWPswitchDelayRRC}}{NR Slot length}+k1+2^{µ-µ_{K_{offset}}}K_{offset}$).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed Cell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

### A.14.4.4 UE specific CBW change for satellite access

#### A.14.4.4.1 UE specific CBW change on PCell in FR1 in non-DRX

##### A.14.4.4.1.1 Test Purpose and Environment

The purpose of this test is to verify the UE specific CBW change delay requirement defined in clause 8.13C.

The supported test configurations are shown in table A.14.4.4.1.1-1. The test scenario comprises of one Cell (Cell 1), which is PCell as given in table A.14.4.4.1.1-2. Cell-specific parameters are specified in table A.14.4.4.1.1-3.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE sends ACK/NACK during the test.

Before the test starts:

UE is connected to Cell 1 (PCell) on radio channel 1.

UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1 (PCell).

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PCell.

UE has been configured with UE specific CBW (CBW-1).

UE is indicated in SCS-SpecificCarrier [2] that the UE specific CBW is CBW-1 as the initial condition in Cell 1 (PCell).

Cell 1 (PCell) has constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration containing SCS-SpecificCarrier with updated UE specific CBW, sent from the test equipment to the UE, is completely received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its UE specific CBW with the updated CBW-2 for the final condition.

The UE shall be able to receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot ($ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}$) as defined in clause8.13C and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot ($ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}+k1+2^{µ-µ_{K_{offset}}}K_{offset}$) on the PCell’s BWP-1 on CBW-2 for the final condition. The UE shall be continuously scheduled on the PCell’s BWP-1 on CBW-2  for the final condition starting from the first DL slot right after slot ($ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}$).

$ T_{RRCprocessingDelay}$ and $ T_{CBWchangeDelayRRC}$ are defined in clause 8.13C.

The test equipment verifies the UE specific CBW switching delay in PCell by estimating the time from the moment the RRC Reconfiguration message including updated UE specific CBW configuration is sent until the moment a vaild ACK/NACK is received.

Table A.14.4.4.1.1-1: Supported test configurations for UE specific CBW change in SA scenario

| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| --- | --- |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.4.1.1-2: General test parameters for UE specific CBW change in SA scenario

| Parameter | Unit | Value | Comment |
| --- | --- | --- | --- |
| NR RF Channel Number |  | 1 | One NR radio channel is used for this test |
| Active Cell |  | Cell 1 | Cell on RF channel number 1. |
| CP length |  | Normal |  |
| DRX |  | OFF |  |
| T1 | s | 0.2 |  |

Table A.14.4.4.1.1-3: NR Cell specific test parameters for UE specific CBW change in SA scenario

| Parameter |  |  | Unit | Cell 1 |
| --- | --- | --- | --- | --- |
| Frequency Range |  |  |  | FR1 |
| Duplex mode |  | Config 1, 2 |  | FDD |
| BWchannel |  | Config 1, 2 |  | 10 MHz: NPRB,c = 52 |
| Satellite information |  | Config 1 |  | SSC.1 |
|  |  | Config 2 |  | SSC.2 |
| Active DL BWP ID |  | Config 1, 2 |  | 0 |
| Initial DL BWP Configuration (BWP-1) |  | Config 1, 2 |  | DLBWP.0.2 |
| Initial UL BWP Configuration |  | Config 1, 2 |  | ULBWP.0.2 |
| Initial Condition | Active DLCBW-1 Configureation | Config 1, 2 |  | DLCBW.1.1 |
|  | Active UL CBW-1Configuration | Config 1, 2 |  | ULCBW.1.1 |
| Final Condition | Active DLCBW-1 Configureation | Config 1, 2 |  | DLCBW.1.2 |
|  | Active UL CBW-1Configuration | Config 1, 2 |  | ULCBW.1.2 |
| PDSCH Reference measurement channel |  | Config 1, 2 |  | SR.1.1 FDD |
| RMSI CORESET parameters |  | Config 1, 2 |  | CR.1.1 FDD |
| Dedicated CORESET parameters |  | Config 1, 2 |  | CCR.1.2 FDD |
| OCNG Patterns |  |  |  | OP.1 |
| SSB Configuration |  | Config 1, 2 |  | SSB.1 FR1 |
| SMTC Configuration |  |  |  | SMTC.1 |
| TRS Configuration |  | Config 1, 2 |  | TRS.1.1 FDD |
| Antenna Configuration |  |  |  | 1x2 Low |
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
| NocNote 2 |  | Config 1, 2 | dBm/SCS | -104 |
| SS-RSRP Note 3 |  | Config 1, 2 | dBm/SCS | -87 |
| Ês/Iot |  |  | dB | 17 |
| Ês/Noc |  |  | dB | 17 |
| IoNote3 |  | Config 1, 2 | dBm/9.36 MHz | -58.96 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for Noc to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |

##### A.14.4.4.1.2 Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the PCell from the first DL slot that occurs right after the begining of slot ($ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}$) and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot ($ i+\frac {T_{RRCprocessingDelay}+T_{CBWchangeDelayRRC}}{NR Slot length}+k1+2^{µ-µ_{K_{offset}}}K_{offset}$).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed UE specific CBW change delay on the PCell to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

### A.14.4.5 Pathloss reference signal switching delay

#### A.14.4.5.1 MAC-CE based pathloss reference signal switch delay

##### A.14.4.5.1.1 Test Purpose and Environment

The purpose of this test is to verify the MAC-CE based pathloss reference signal switch delay requirement defined in clause 8.14C.

The supported test configurations are shown in table A.14.4.5.1.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.14.4.5.1.1-2. Cell-specific parameters of the cell are specified in table A.14.4.5.1.1-3 below.

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

Table A.14.4.5.1.1-1: MAC-CE based pathloss reference signal switch supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.4.5.1.1-2: General test parameters for MAC-CE based pathloss reference signal switch

| Parameter |  | Unit | Value | Comment |
| --- | --- | --- | --- | --- |
| Active PCell |  |  | Cell 1 |  |
| RF Channel Number |  |  | 1 |  |
| Duplex mode | Config 1, 2 |  | FDD |  |
| Satellite information | Config 1 |  | SSC.1 |  |
|  | Config 2 |  | SSC.2 |  |
| DL initial BWP configuration | Config 1, 2 |  | DLBWP.0.1 |  |
| DL dedicated BWP configuration | Config 1, 2 |  | DLBWP.1.1 |  |
| UL initial BWP configuration | Config 1, 2 |  | ULBWP.0.1 |  |
| UL dedicated BWP configuration | Config 1, 2 |  | ULBWP.1.1 |  |
| CORESET Reference Channel | Config 1, 2 |  | CR.1.1 FDD |  |
| SSB Configuration | Config 1, 2 |  | SSB.3 FR1 |  |
| SMTC Configuration | Config 1, 2 |  | SMTC.1 |  |
| PDSCH/PDCCH subcarrier spacing | Config 1, 2 |  | 15 kHz |  |
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

Table A.14.4.5.1.1-3: NR Cell specific test parameters for MAC-CE based pathloss reference signal switch

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
| SSB with index 0 | ![](media_svg/image12.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 7 |  |  |
|  | ![](media_svg/image1.svg) [公式≈: ^{N}oc] | Config 1, 2 |  | -101 | -101 |  |  |
|  | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 7 |  |  |
|  | SS-RSRP Note 4 |  | Config 1 | -94-94 | -94 |  |  |
|  |  |  | Config 2 |  | -94 |  |  |
| SSB with index 1 | ![](media_svg/image12.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -3 |  |  |
|  | ![](media_svg/image1.svg) [公式≈: ^{N}oc] | Config 1, 2 |  | -101 | -101 |  |  |
|  | ![](media_svg/image13.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -3 |  |  |
|  | SS-RSRP Note 4 |  | Config 1 | -104 | -104 |  |  |
|  |  |  | Config 2 |  | -104 |  |  |
| Io Note 5 | Config 1 |  |  | dBm | -65.3/9.36MHz |  |  |
|  | Config 2 |  |  |  | -65.3/9.36MHz |  |  |
| Propagation condition |  |  |  |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that the resources in Cell 1 are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: The signal contains PDCCH for UEs other than the device under test as part of OCNG.NOTE 3: SNR levels correspond to the signal to noise ratio over the SSS REs.NOTE 4: The DL PDSCH reference measurement channel is used in the test only when a downlink transmission dedicated to the UE under test is required.NOTE 5: SS-RSRP, Es/Iot and Io levels have been derived from other parameters for information purpose. They are not settable parameters. |  |  |  |  |  |  |  |

##### A.14.4.5.1.2 Test Requirements

During T3, the UE shall start to send the PHR for PCell no later than the slot i + $ T_{HARQ}$+ $\lceil  \frac {3 ms + 5*T_{target\_PL-RS}+ 2 ms}{NRslotlength}\rceil  $.

During T3, the UE shall start to send the PHR for PCell no earlier than the slot i + $ T_{HARQ}$+ $ 3N_{slot}^{subframe,µ}$.

Where, $ T_{HARQ}$ is the timing between pathloss reference MAC-CE activation command and acknowledgement as specified in [7], $ T_{target\_PL-RS}$ is the periodicity of the target pathloss reference signal which is SSB in this test.

During T3, UE shall send L1-RSRP report with measurement results for both SSB0 and SSB1.

All of the above test requirements shall be fulfilled in order for the observed pathloss RS switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The UE shall be given proper uplink transmission grant during T2 and T3.

## A.14.5 Measurement procedure

### A.14.5.1 Intra-frequency Measurements

#### A.14.5.1.1 SA event triggered reporting tests without gap under non-DRX

##### A.14.5.1.1.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2C.5.1 and 9.2C.5.2.

##### A.14.5.1.1.2 Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell and neighbour cell are given in table A.14.5.1.1.2-1 and A.14.5.1.1.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

UE is configured with 2 non-overlapping SMTCs for the intra-frequency measurement. The SMTC periodicity is 20 ms, and SMTC1 is associated with Cell 1 with offset 0, and SMTC2 is associated with Cell 2 with offset 10 ms.

Table A.14.5.1.1.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.5.1.1.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FR1

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1, 2 | Cell 1 |  |
| Neighbour cell |  | 1, 2 | Cell 2 | Cell to be identified. |
| RF Channel Number |  | 1, 2 | 1: Cell 1 and Cell 2 |  |
| SMTC1 configuration |  | 1, 2 | SMTC.1 | Period: 20 ms, offset: 0 |
| SMTC2 configuration |  | 1, 2 | SMTC.4 | Period: 20 ms, offset: 10 ms |
| A3-Offset | dB | 1, 2 | -4.5 |  |
| CP length |  | 1, 2 | Normal |  |
| Hysteresis | dB | 1, 2 | 0 |  |
| Time To Trigger | s | 1, 2 | 0 |  |
| Filter coefficient |  | 1, 2 | 0 | L3 filtering is not used |
| DRX |  | 1, 2 |  | OFF |
| Time offset between serving and neighbour cells |  | 1, 2 | 10 ms | Asynchronous cells.The timing of Cell 2 is 10 ms later than the timing of Cell 1. |
| T1 | s | 1, 2 | 5 |  |
| T2 | s | 1, 2 | 5 |  |

Table A.14.5.1.1.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1 | SSC.1 |  | NSC.1 |  |
|  |  | 2 | SSC.2 |  | NSC.2 |  |
| SSB configuration |  | 1, 2 | SSB.1 FR1 |  | SSB.1 FR1 |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 FDD |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CR.1.1 FDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | CCR.1.1 FDD |  | N/A |  |
| OCNG Patterns |  | 1, 2 | OP.1 |  | OP.1 |  |
| TRS Configuration |  | 1, 2 | TRS.1.1 FDD |  | N/A |  |
| IInitial BWP configuration |  | 1, 2 | DLBWP.0.1 ULBWP.0.1 |  | DLBWP.0.1 ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1, 2 | DLBWP.1.1 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.1 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1, 2 | SSB |  | SSB |  |
| Note 2 | dBm/SCS | 1, 2 | -98 |  |  |  |
| Note 2 | dBm/15 kHz | 1, 2 | -98 |  |  |  |
|  | dB | 1, 2 | 4 | -1.46 | -Infinity | -1.46 |
|  | dB | 1, 2 | 4 | 4 | -Infinity | 4 |
| SS-RSRP Note 3 | dBm/SCS kHz | 1, 2 | -94 | -94 | -Infinity | -94 |
| Io | dBm/9.36 MHz | 1, 2 | -64.60 | -62.25 | --64.60 | -62.25 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.14.5.1.1.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.1.2 SA event triggered reporting tests without gap under DRX

##### A.14.5.1.2.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2C.5.1 and 9.2C.5.2.

##### A.14.5.1.2.2 Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.14.5.1.2.2-1, A.14.5.1.2.2-2 and A.14.5.1.2.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

The UE shall be provided with the valid information about the SAN serving cell in the test before the test.

UE is configured with 1 SMTC for the intra-frequency measurement. Both Cell 1 and Cell 2 are associated with the configured SMTC.

Table A.14.5.1.2.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.5.1.2.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for PCell in FR1 with DRX

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| Active cell |  | 1, 2 | Cell 1 |  |  |
| Neighbour cell |  | 1, 2 | Cell 2 |  | Cell to be identified. |
| RF Channel Number |  | 1, 2 | 1: Cell 1 and Cell 2 |  |  |
| SMTC configuration |  | 1, 2 | SMTC.2 |  |  |
| A3-Offset | dB | 1, 2 | -4.5 |  |  |
| CP length |  | 1, 2 | Normal |  |  |
| Hysteresis | dB | 1, 2 | 0 |  |  |
| Time To Trigger | s | 1, 2 | 0 |  |  |
| Filter coefficient |  | 1, 2 | 0 |  | L3 filtering is not used |
| DRX |  | 1, 2 | DRX.1 | DRX. 7 |  |
| Time offset between serving and neighbour cells |  | 1, 2 | 3 s |  | Synchronous cells |
| T1 | s | 1, 2 | 5 |  |  |
| T2 | s | 1, 2 | 5 | 15 |  |

Table A.14.5.1.2.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for PCell in FR1 with DRX

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1 | SSC.1 |  | NSC.1 |  |
|  |  | 2 | SSC.2 |  | NSC.2 |  |
| SSB configuration |  | 1, 2 | SSB.1 FR1 |  | SSB.1 FR1 |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 FDD |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CR.1.1 FDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | CCR.1.1 FDD |  | N/A |  |
| OCNG Patterns |  | 1, 2 | OP.1 |  | OP.1 |  |
| TRS configuration |  | 1, 2 | TRS.1.1 FDD |  | N/A |  |
| IInitial BWP configuration |  | 1, 2 | DLBWP.0.1 ULBWP.0.1 |  | DLBWP.0.1 ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1, 2 | DLBWP.1.1 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.1 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1, 2 | SSB |  | SSB |  |
| Note 2 | dBm/SCS | 1, 2 | -98 |  |  |  |
| Note 2 | dBm/15 kHz | 1, 2 | -98 |  |  |  |
|  | dB | 1, 2 | 4 | -1.46 | -Infinity | -1.46 |
|  | dB | 1, 2 | 4 | 4 | -Infinity | 4 |
| SS-RSRP Note 3 | dBm/SCS kHz | 1, 2 | -94 | -94 | -Infinity | -94 |
| Io | dBm/9.36 MHz | 1, 2 | -64.60 | -62.25 | -64.60 | -62.25 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.14.5.1.2.3 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. X=1280 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC and supports parallelMeasurementWithoutRestriction-r17, X=1920 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC and not supports parallelMeasurementWithoutRestriction-r17, X=1080 for test configuration 2 and if UE indicates other than ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC and not supports parallelMeasurementWithoutRestriction-r17, otherwise X=920.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Y ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. Y=12800 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC and supports parallelMeasurementWithoutRestriction-r17, Y=20480 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC and not supports parallelMeasurementWithoutRestriction-r17, Y=10240 for test configuration 2 and if UE indicates other than ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC and not supports parallelMeasurementWithoutRestriction-r17, otherwise Y=6400.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.1.3 SA event triggered reporting tests without gap under non-DRX with SSB index reading

##### A.14.5.1.3.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2C.5.1 and 9.2C.5.2.

##### A.14.5.1.3.2 Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for FDD PCell and neighbour cell are given in table A.14.5.1.3.2-1 and A.14.5.1.3.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

UE is configured with 2 overlapping SMTC for the intra-frequency measurement. The SMTC periodicity is 20 ms, and SMTC1 is associated with Cell 1 with offset 0, and SMTC2 is associated with Cell 2 with offset 17 ms.

Table A.14.5.1.3.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.5.1.3.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1, 2 | Cell 1 |  |
| Neighbour cell |  | 1, 2 | Cell 2 | Cell to be identified. |
| RF Channel Number |  | 1, 2 | 1: Cell 1 and Cell 2 |  |
| SSB configuration |  | 1, 2 | SSB.1 FR1 |  |
| SMTC1 configuration |  | 1, 2 | SMTC.6 |  |
| SMTC2 configuration |  | 1, 2 | SMTC.2 |  |
| A3-Offset | dB | 1, 2 | -4.5 |  |
| CP length |  | 1, 2 | Normal |  |
| Hysteresis | dB | 1, 2 | 0 |  |
| Time To Trigger | s | 1, 2 | 0 |  |
| Filter coefficient |  | 1, 2 | 0 | L3 filtering is not used |
| DRX | ms | 1, 2 |  | OFF |
| Time offset between serving and neighbour cells |  | 1, 2 | 3 ms | Asynchronous cells.The timing of Cell 2 is 3ms earlier than the timing of Cell 1. |
| T1 | s | 1, 2 | 5 |  |
| T2 | s | 1, 2 | 5 |  |

Table A.14.5.1.3.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1 | SSC.1 |  | NSC.1 |  |
|  |  | 2 | SSC.2 |  | NSC.2 |  |
| SSB configuration |  | 1, 2 | SSB.1 FR1 |  | SSB.1 FR1 |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 FDD |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CR.1.1 FDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | CCR.1.1 FDD |  | N/A |  |
| OCNG Patterns |  | 1, 2 | OP.1 |  | OP.1 |  |
| TRS configuration |  | 1, 2 | TRS.1.1 FDD |  | N/A |  |
| IInitial BWP configuration |  | 1, 2 | DLBWP.0,1 ULBWP.0.1 |  | DLBWP.0.1 ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1, 2 | DLBWP.1.1 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.1 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1, 2 | SSB |  | SSB |  |
| Note 2 | dBm/SCS | 1, 2 | -98 |  |  |  |
| Note 2 | dBm/15 kHz | 1, 2 | -98 |  |  |  |
|  | dB | 1, 2 | 4 | -1.46 | -Infinity | -1.46 |
|  | dB | 1, 2 | 4 | 4 | -Infinity | 4 |
| SS-RSRP Note 3 | dBm/SCS kHz | 1, 2 | -94 | -94 | -Infinity | -94 |
| Io | dBm/9.36 MHz | 1, 2 | -64.60 | -62.25 | -64.60 | -62.25 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.14.5.1.3.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test. X=920 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise X=920.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.1.4 SA event triggered reporting tests with single measurement gap under non-DRX for satellite access

##### A.14.5.1.4.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2C.6.1 and 9.2C.6.2.

##### A.14.5.1.4.2 Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters are given in table A.14.5.1.4.2-1 and A.14.5.1.4.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP0 which contains the cell defining SSB, and BWP1 which does not contain any SSB of Cell 1. During the whole test, BWP1 is always scheduled as the active BWP for the UE.

The UE shall be provided with the valid information about the SAN serving each cell before the test.

UE is configured with 1 SMTC for the intra-frequency measurement. Both Cell 1 and Cell 2 are associated with the configured SMTC.

Table A.14.5.1.4.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.5.1.4.2-2: General test parameters for SA intra-frequency event triggered reporting with single measurement gap for PCell in FR1

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1, 2 | Cell 1 |  |
| Neighbour cell |  | 1, 2 | Cell 2 | Cell to be identified. |
| RF Channel Number |  | 1, 2 | 1: Cell 1 and Cell 2 |  |
| Measurement gap type |  | 1, 2 | Per-UE gaps |  |
| Gap Pattern ID |  | 1, 2 | 0 | As specified in clause 9.1.2-1. |
| Measurement gap repetition periodicity | ms | 1, 2 | 40 |  |
| Measurement gap length | ms | 1, 2 | 6 |  |
| Measurement gap offset | ms | 1, 2 | 39 |  |
| A3-Offset | dB | 1, 2 | -4.5 |  |
| CP length |  | 1, 2 | Normal |  |
| Hysteresis | dB | 1, 2 | 0 |  |
| Time To Trigger | s | 1, 2 | 0 |  |
| Filter coefficient |  | 1, 2 | 0 | L3 filtering is not used |
| DRX | ms | 1, 2 |  | OFF |
| Time offset between serving and neighbour cells |  | 1,2 | 3 ms | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
| T1 | s | 1, 2 | 5 |  |
| T2 | s | 1, 2 | 5 |  |

Table A.14.5.1.4.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with single measurement gap for PCell in FR1

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1 | SSC.1 |  | NSC.1 |  |
|  |  | 2 | SSC.2 |  | NSC.2 |  |
| SSB configuration |  | 1, 2 | SSB.1 FR1 |  | SSB.1 FR1 |  |
| SMTC configuration |  | 1, 2 | SMTC.2 |  | SMTC.2 |  |
| CSI-RS parameters |  | 1, 2 | CSI-RS.1.2 FDD resource #0 |  | N/A |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 FDD |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CR.1.1 FDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | CCR.1.2 FDD |  | N/A |  |
| OCNG Patterns |  | 1, 2 | OP.1 |  | OP.1 |  |
| TRS configuration |  | 1, 2 | TRS.1.1 FDD |  | N/A |  |
| Initial BWP configuration |  | 1, 2 | DLBWP.0.1 ULBWP.0.1 |  | DLBWP.0.1 ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1, 2 | DLBWP.1.2 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.2 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1, 2 | CSI-RS |  | SSB |  |
| Note 2 | dBm/SCS | 1, 2 | -98 |  |  |  |
| Note 2 | dBm/15 kHz | 1, 2 | -98 |  |  |  |
|  | dB | 1, 2 | 4 | -1.46 | -Infinity | -1.46 |
|  | dB | 1, 2 | 4 | 4 | -Infinity | 4 |
| SS-RSRP Note 3 | dBm/SCS kHz | 1, 2 | -94 | -94 | -Infinity | -94 |
| Io | dBm/9.36 MHz | 1, 2 | -64.60 | -62.25 | -64.60 | -62.25 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.14.5.1.4.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. X=1600 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise X=1000.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.1.5 SA event triggered reporting tests with FNO concurrent gaps under DRX for satellite access

##### A.14.5.1.5.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2C.6.1 and 9.2C.6.2.

##### A.14.5.1.5.2 Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters are given in table A.14.5.1.5.2-1, A. 14.5.1.5.2-2 and A. 14.5.1.5.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3.

There are two BWPs configured in Cell 1, BWP0 which contains the cell defining SSB, and BWP1 which does not contain any SSB of Cell 1. During the whole test, BWP1 is always scheduled as the active BWP for the UE.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

The UE shall be provided with the valid information about the SAN serving each cell before the test.

The UE is configured with 2 FNO concurrent measurement gaps for the intra-frequency measurement. Serving Cell 1 is expected to be measured within MeasGapId #0 and Neighbour Cell 2 is expected to be measured within MeasGapId #1.

Table A.14.5.1.5.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.5.1.5.2-2: General test parameters for SA intra-frequency event triggered reporting with FNO concurrent gaps for PCell in FR1 with DRX

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| Active cell |  | 1, 2 | Cell 1 |  |  |
| Neighbour cell |  | 1, 2 | Cell 2 |  | Cell to be identified. |
| RF Channel Number |  | 1, 2 | 1: Cell 1 and Cell 2 |  |  |
| Measurement gap type |  | 1, 2 | Per-UE gap |  |  |
| Gap Pattern ID |  | 1 | 0 |  | As specified in clause 9.1.2-1. |
| Measurement gap repetition periodicity | ms | 1, 2 | 40 |  |  |
| Measurement gap length | ms | 1, 2 | 6 |  |  |
| Measurement gap offset | ms | 1, 2 | 19 for MeasGapId #04 for MeasGapId #1 |  |  |
| A3-Offset | dB | 1, 2 | -4.5 |  |  |
| CP length |  | 1, 2 | Normal |  |  |
| Hysteresis | dB | 1, 2 | 0 |  |  |
| Time To Trigger | s | 1, 2 | 0 |  |  |
| Filter coefficient |  | 1, 2 | 0 |  | L3 filtering is not used |
| DRX |  | 1, 2 | DRX.1 | DRX. 7 |  |
| Time offset between serving and neighbour cells |  | 1, 2 | 3 ms |  | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
| T1 | s | 1, 2 | 5 |  |  |
| T2 | s | 1, 2 | 5 | 10 |  |

Table A.14.5.1.5.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with FNO concurrent gaps for PCell in FR1 with DRX

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1 | SSC.1 |  | NSC.1 |  |
|  |  | 2 | SSC.2 |  | NSC.2 |  |
| SSB configuration |  | 1, 2 | SSB.1 FR1 |  | SSB.7 FR1 |  |
| SMTC configuration |  | 1, 2 | SMTC.2 |  | SMTC.12 |  |
| CSI-RS parameters |  | 1, 2 | CSI-RS.1.2 FDD resource #0 |  | N/A |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 FDD |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CR.1.1 FDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | CCR.1.2 FDD |  | N/A |  |
| OCNG Patterns |  | 1, 2 | OP.1 |  | OP.1 |  |
| TRS configuration |  | 1, 2 | TRS.1.1 FDD |  | N/A |  |
| Initial BWP configuration |  | 1, 2 | DLBWP.0.1 ULBWP.0.1 |  | DLBWP.0.1 ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1, 2 | DLBWP.1.2 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.2 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1, 2 | CSI-RS |  | SSB |  |
| Note 2 | dBm/SCS | 1, 2 | -98 |  |  |  |
| Note 2 | dBm/15 kHz | 1, 2 | -98 |  |  |  |
|  | dB | 1, 2 | 4 | -1.46 | -Infinity | -1.46 |
|  | dB | 1, 2 | 4 | 4 | -Infinity | 4 |
| SS-RSRP Note 3 | dBm/SCS kHz | 1, 2 | -94 | -94 | -Infinity | -94 |
| Io | dBm/9.36 MHz | 1, 2 | -64.60 | -62.25 | -64.60 | -62.25 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

Table A.14.5.1.5.2-4: Void

Table A.14.5.1.5.2-5: Void

##### A.15.5.1.5.3 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 6400 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.1.6 SA event triggered reporting tests with PPO concurrent gaps under non-DRX with SSB index reading for satellite access

##### A.14.5.1.6.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2C.6.1 and 9.2C.6.2.

##### A.14.5.1.6.2 Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for FDD PCell and neighbour cells are given in table A.14.5.1.6.2-1 and A.14.5.1.6.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP0 which contains the cell defining SSB, and BWP1 which does not contain any SSB of Cell 1. During the whole test, BWP1 is always scheduled as the active BWP for the UE.

The UE shall be provided with the valid information about the SAN serving each cell before the test.

The UE is configured with 2 PPO concurrent measurement gaps for the intra-frequency measurement. Serving Cell 1 is expected to be measured within MeasGapId #0 and Neighbour Cell 2 is expected to be measured within MeasGapId #1. And the priority for MeasGapId #1 is higher than the priority for MeasGapId #0.

Table A.14.5.1.6.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.5.1.6.2-2: General test parameters for SA intra-frequency event triggered reporting with PPO concurrent gaps for FDD PCell in FR1 with SSB index reading

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1, 2 | Cell 1 |  |
| Neighbour cell |  | 1, 2 | Cell 2 | Cell to be identified. |
| RF Channel Number |  | 1, 2 | 1: Cell 1 and Cell 2 |  |
| Measurement gap type |  | 1, 2 | Per-UE gap |  |
| Gap Pattern ID |  | 1, 2 | 0 for MeasGapId #11 for MeasGapId #2 | As specified in clause 9.1.2-1. |
| Measurement gap repetition periodicity | ms | 1, 2 | 40 ms for MeasGapId #180 ms for MeasGapId #2 |  |
| Measurement gap length | ms | 1, 2 | 6 |  |
| Measurement gap offset | ms | 1, 2 | 39 for MeasGapId #14 for MeasGapId #2 |  |
| A3-Offset | dB | 1, 2 | -4.5 |  |
| CP length |  | 1, 2 | Normal |  |
| Hysteresis | dB | 1, 2 | 0 |  |
| Time To Trigger | s | 1, 2 | 0 |  |
| Filter coefficient |  | 1, 2 | 0 | L3 filtering is not used |
| DRX | ms | 1, 2 |  | OFF |
| Time offset between serving and neighbour cells |  | 1, 2 | 5 ms | Asynchronous cells.The timing of Cell 2 is 5 ms later than the timing of serving Cell 1. |
| T1 | s | 1, 2 | 5 |  |
| T2 | s | 1, 2 | 5 |  |

Table A.14.5.1.6.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with PPO concurrent gaps for FDD PCell in FR1 with SSB index reading

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1 | SSC.1 |  | NSC.1 |  |
|  |  | 2 | SSC.2 |  | NSC.2 |  |
| SSB configuration |  | 1, 2 | SSB.1 FR1 |  | SSB.1 FR1 |  |
| SMTC configuration |  | 1, 2 | SMTC.2 |  | SMTC.12 |  |
| CSI-RS parameters |  | 1, 2 | CSI-RS.1.2 FDD resource #0 |  | N/A |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 FDD |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CR.1.1 FDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | CCR.1.2 FDD |  | N/A |  |
| OCNG Patterns |  | 1, 2 | OP.1 |  | OP.1 |  |
| TRS configuration |  | 1, 2 | TRS.1.1 FDD |  | N/A |  |
| Initial BWP configuration |  | 1, 2 | DLBWP.0.1 ULBWP.0.1 |  | DLBWP.0.1 ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1, 2 | DLBWP.1.2 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.2 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1, 2 | CSI-RS |  | SSB |  |
| Note 2 | dBm/SCS | 1, 2 | -98 |  |  |  |
| Note 2 | dBm/15 kHz | 1, 2 | -98 |  |  |  |
|  | dB | 1, 2 | 4 | -1.46 | -Infinity | -1.46 |
|  | dB | 1, 2 | 4 | 4 | -Infinity | 4 |
| SS-RSRP Note 3 | dBm/SCS kHz | 1, 2 | -94 | -94 | -Infinity | -94 |
| Io | dBm/9.36 MHz | 1, 2 | -64.60 | -62.25 | -64.60 | -62.25 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.14.5.1.6.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1240 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.1.7 SA event triggered reporting test with SSB time index reading without gap under non-DRX for FR2-NTN

##### A.14.5.1.7.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in FR2-NTN in clause 9.2C.7.1 and 9.2C.7.2.

##### A.14.5.1.7.2 Test parameters

Two cells are deployed in the test, which are FR2 PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for FDD PCell and neighbour cell are given in table A.14.5.1.7.2-1 and A.14.5.1.7.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

UE is configured with 1 SMTC for the intra-frequency measurement. Both Cell 1 and Cell 2 are associated with the configured SMTC.

Table A.14.5.1.7.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 2 | NGSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 3 | GSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.5.1.7.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR2-NTN with SSB index reading

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1, 2, 3, 4 | Cell 1 |  |
| Neighbour cell |  | 1, 2, 3, 4 | Cell 2 | Cell to be identified. |
| RF Channel Number |  | 1, 2, 3, 4 | 1: Cell 1 and Cell 2 |  |
| SMTC configuration |  | 1, 2, 3, 4 | SMTC.2 |  |
| A3-Offset | dB | 1, 2, 3, 4 | -11 |  |
| CP length |  | 1, 2, 3, 4 | Normal |  |
| Hysteresis | dB | 1, 2, 3, 4 | 0 |  |
| Time To Trigger | s | 1, 2, 3, 4 | 0 |  |
| Filter coefficient |  | 1, 2, 3, 4 | 0 | L3 filtering is not used |
| DRX | ms | 1, 2, 3, 4 |  | OFF |
| Time offset between serving and neighbour cells |  | 1, 2, 3, 4 | 3 s | Synchronous cells |
| T1 | s | 1, 2, 3, 4 | 5 |  |
| T2 | s | 1, 2, 3, 4 | 5 |  |

Table A.14.5.1.7.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR2-NTN with SSB index reading

| Parameter | Unit | Config | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| BWchannel | MHz | 1, 2 | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
|  |  | 3, 4 | 10: NPRB,c = 24 |  | 10: NPRB,c = 24 |  |
| Data PRBs allocated |  | 1, 3, 4 | 24 |  | 24 |  |
|  |  | 2 | 48 |  | 48 |  |
| Intial BWP configuration |  | 1, 2, 3, 4 | DLBWP.0.1ULBWP.0.1 |  | DLBWP.0.1ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1, 2, 3, 4 | DLBWP.1.1 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1, 2, 3, 4 | ULBWP.1.1 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1, 2, 3, 4 | SSB |  | SSB |  |
| PDSCH RMC configuration |  | 1, 2 | TBD |  | N/A |  |
|  |  | 3, 4 | SR.2.1 TDD |  |  |  |
| RMSI CORESET RMC configuration |  | 1, 2 | TBD |  | N/A |  |
|  |  | 3, 4 | CCR.2.1TDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | TBD |  | N/A |  |
|  |  | 3, 4 | CCR.2.1TDD |  | N/A |  |
| TRS configuration |  | 1, 2 | TBD |  | N/A |  |
|  |  | 3,4 | TRS.1.2 TDD |  |  |  |
| PDSCH/PDCCH TCI states |  | 1, 2 | TCI.State.2 |  | N/A |  |
| PDSCH/PDCCH subcarrier spacing | kHz | 1, 2 | 120 |  | 120 |  |
|  |  | 3, 4 | 30 |  | 30 |  |
| OCNG Patterns |  | 1, 2, 3, 4 | OP.5 |  | N/A |  |
| cellIndividualOffset | dB | 1~2, 3, 4 | N/A |  | 16 |  |
| SSB |  | 1 | SSB.1 FR2 |  | SSB.7 FR2 |  |
|  |  | 2 | SSB.2 FR2 |  | SSB.8 FR2 |  |
|  |  | 3, 4 | SSB.1 FR1 |  | SSB.5 |  |
| Propagation Condition |  | 1, 2 | No external noise (Note 1) |  | No external noise (Note 1) |  |
| NOTE 1: The downlink connection between the System Simulator and the UE is without Additive White Gaussian Noise, and has no fading or multipath effects as specified in TS 38.521-2 B.0 [40]. |  |  |  |  |  |  |

Table 14.5.1.7.2-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with FDD PCell in FR2-NTN without gap without DRX

| Parameter | Unit | Config | Cell 1 |  | Cell 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 |  | T2 |
| Satellite information |  | 1, 3 | SSC.1 |  | NSC.1 |  |  |
|  |  | 2, 4 | SSC.2 |  | NSC.2 |  |  |
| AoA setup |  | 1, 2 | TBD |  |  |  |  |
| Beam assumptionNote 4 |  | 1,2 | TBD |  | TBD |  |  |
| Es | dBm/SCS | 1 | -89 | -89 |  | -Infinity | -89 |
|  |  | 2 | -86 | -86 |  | -Infinity | -86 |
| BB Note 5 | dB | 1, 2, 3, 4 | -0.12 | -0.12 |  | -Infinity | -0.12 |
| SSB_RP | dBm/SCS | 1, 3 | -89 | -89 | -Infinity |  | -89 |
|  |  | 2, 4 | -86 | -86 | -Infinity |  | -86 |
|  | dBm/95.04 MHz | 1, 3 | -64.41 | -64.41 | -Infinity |  | -64.41 |
|  |  | 2, 4 | -61.41 | -61.41 | -Infinity |  | -61.41 |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: VoidNOTE 3: Es/Iot, SSB_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in B.2.1.3, and does not limit UE implementation or test system implementationNOTE 5: Calculation of Es/IotBB includes the effect of UE internal noise up to the value assumed for the associated Refsens requirement in clause 7.3.2 of TS 38.101-2 [19], and an allowance of 1 dB for UE multi-band relaxation factor ΔMBP from TS 38.101-2 [19] Table 6.2.1.3-4. |  |  |  |  |  |  |  |

##### A.14.5.1.7.3 Test Requirements

For both UE indicating [Type 1] and [Type 2] via UE capability [Beam steering], the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.1.8 SA event triggered reporting tests without gap under non-DRX with SSB index reading under less 5MHz BW

##### A.14.5.1.8.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2C.5.1 and 9.2C.5.2.

##### A.14.5.1.8.2 Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for FDD PCell and neighbour cell are given in table A.14.5.1.8.2-1 and A.14.5.1.8.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

UE is configured with 2 overlapping SMTC for the intra-frequency measurement. The SMTC periodicity is 20 ms, and SMTC1 is associated with Cell 1 with offset 0, and SMTC2 is associated with Cell 2 with offset 17 ms.

Table A.14.5.1.8.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 3 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 3 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.5.1.8.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1, 2 | Cell 1 |  |
| Neighbour cell |  | 1, 2 | Cell 2 | Cell to be identified. |
| RF Channel Number |  | 1, 2 | 1: Cell 1 and Cell 2 |  |
| SSB configuration |  | 1, 2 | SSB.13 FR1 |  |
| SMTC1 configuration |  | 1, 2 | SMTC.2 |  |
| SMTC2 configuration |  | 1, 2 | SMTC.6 |  |
| A3-Offset | dB | 1, 2 | -4.5 |  |
| CP length |  | 1, 2 | Normal |  |
| Hysteresis | dB | 1, 2 | 0 |  |
| Time To Trigger | s | 1, 2 | 0 |  |
| Filter coefficient |  | 1, 2 | 0 | L3 filtering is not used |
| DRX | ms | 1, 2 |  | OFF |
| Time offset between serving and neighbour cells |  | 1, 2 | 3 ms | Asynchronous cells.The timing of Cell 2 is 3 ms earlier than the timing of Cell 1. |
| T1 | s | 1, 2 | 5 |  |
| T2 | s | 1, 2 | 5 |  |

Table A.14.5.1.8.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1 | SSC.1 |  | NSC.1 |  |
|  |  | 2 | SSC.2 |  | NSC.2 |  |
| SSB configuration |  | 1, 2 | SSB.13 FR1 |  | SSB.13 FR1 |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 FDD |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CR.1.3 FDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | CCR.1.7 FDD |  | N/A |  |
| OCNG Patterns |  | 1, 2 | OP.1 |  | OP.1 |  |
| TRS configuration |  | 1, 2 | TRS.1.1 FDD |  | N/A |  |
| IInitial BWP configuration |  | 1, 2 | DLBWP.0,1 ULBWP.0.1 |  | DLBWP.0.1 ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1, 2 | DLBWP.1.1 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.1 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1, 2 | SSB |  | SSB |  |
| Note 2 | dBm/SCS | 1, 2 | -98 |  |  |  |
| Note 2 | dBm/15 kHz | 1, 2 | -98 |  |  |  |
|  | dB | 1, 2 | 4 | -1.46 | -Infinity | -1.46 |
|  | dB | 1, 2 | 4 | 4 | -Infinity | 4 |
| SS-RSRP Note 3 | dBm/SCS kHz | 1, 2 | -94 | -94 | -Infinity | -94 |
| Io | dBm/2.7 MHz | 1, 2 | -64.60 | -62.25 | -64.60 | -62.25 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.14.5.1.8.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test. X=1000 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise X=880.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.1.9 SA event triggered reporting tests without gap under non-DRX

##### A.14.5.1.9.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event when configured with two different SMTC configurations. This test will partly verify the intra-frequency cell search requirements in clauses 9.2C.5.1 and 9.2C.5.2 for UEs that support the configuration of different SMTC periodicities for different cells.

##### A.14.5.1.9.2 Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The supported test configurations and general test configurations are given in table A.14.5.1.9.2-1 and A.14.5.1.9.2-2 below, respectively. The cell specific test parameters for PCell and neighbour cell are given in table A.14.5.1.9.2-3. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

UE is configured with 2 non-overlapping SMTCs for the intra-frequency measurement. The SMTC periodicity is 20 ms, for Cell 1 (serving cell at the beginning of the test case) with SMTC Config.1 is associated with Cell 1 with offset 0, and the SMTC periodicity for the neighbor cell is 160 ms, with SMTC Config.2 is associated with Cell 2 with offset 10 ms. The two cells are associated to the same satellite

Table A.14.5.1.9.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.5.1.9.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FR1

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1, 2 | Cell 1 |  |
| Neighbour cell |  | 1, 2 | Cell 2 | Cell to be identified. |
| RF Channel Number |  | 1, 2 | 1: Cell 1 and Cell 2 |  |
| SMTC Config. 1 |  | 1,2 | SMTC.1 | Period: 20 ms, offset: 0, SMTC duration:1 ms |
| SMTC Config. 2 |  |  | SMTC.13 | Period: 160 ms, offset: 10 ms,SMTC duration: 1 ms |
| A3-Offset | dB | 1, 2 | -4.5 |  |
| CP length |  | 1, 2 | Normal |  |
| Hysteresis | dB | 1, 2 | 0 |  |
| Time To Trigger | s | 1, 2 | 0 |  |
| Filter coefficient |  | 1, 2 | 0 | L3 filtering is not used |
| DRX |  | 1, 2 |  | OFF |
| Time offset between serving and neighbour cells |  | 1, 2 | 10 ms | Asynchronous cells.The timing of Cell 2 is 10 ms later than the timing of Cell 1. |
| T1 | s | 1, 2 | 5 |  |
| T2 | s | 1, 2 | 5 |  |

Table A.14.5.1.9.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1 | SSC.1 |  | SSC.1 |  |
|  |  | 2 | SSC.2 |  | SSC.2 |  |
| SSB configuration |  | 1, 2 | SSB.1 FR1 |  | SSB.14 FR1 |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 FDD |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CR.1.1 FDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | CCR.1.1 FDD |  | N/A |  |
| OCNG Patterns |  | 1, 2 | OP.1 |  | OP.1 |  |
| TRS Configuration |  | 1, 2 | TRS.1.1 FDD |  | N/A |  |
| IInitial BWP configuration |  | 1, 2 | DLBWP.0.1 ULBWP.0.1 |  | DLBWP.0.1 ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1, 2 | DLBWP.1.1 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.1 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1, 2 | SSB |  | SSB |  |
| Note 2 | dBm/SCS | 1, 2 | -98 |  |  |  |
| Note 2 | dBm/15 kHz | 1, 2 | -98 |  |  |  |
|  | dB | 1, 2 | 4 | -1.46 | -Infinity | -1.46 |
|  | dB | 1, 2 | 4 | 4 | -Infinity | 4 |
| SS-RSRP Note 3 | dBm/SCS kHz | 1, 2 | -94 | -94 | -Infinity | -94 |
| Io | dBm/9.36 MHz | 1, 2 | -64.60 | -62.25 | --64.60 | -62.25 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.14.5.1.9.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1600 ms from the beginning of the period T2. The UE is not required to read the neighbour cell SSB index in this test. The test requirement was obtained from:

Tidentify_intra_without_index = (TPSS/SSS_sync_intra + TSSB_measurement_period_intra) ms

Where:

- TPSS/SSS_sync_intra   = max( 600 ms, ceil( 5 x Kp x Klayer1_measurement) x Kmulti_SMTC x SMTC period ) x CSSFintra =

max(600 ms, ceil(5x 1 x 1) x 1 x 160) x 1

= 800 ms.

- max(200 ms, ceil( 5 x Kp x Klayer1_measurement) x Kmulti_SMTC x SMTC period) x CSSFintra

= 800 ms

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

### A.14.5.2 Inter-frequency Measurements

#### A.14.5.2.1 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with single gap for satellite access

##### A.14.5.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3C.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.14.5.2.1.1-1, A.14.5.2.1.1-2 and A.14.5.2.1.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in table A.14.5.2.1.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.14.5.2.1.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

| Config | Description |
| --- | --- |
| 1 | GSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NGSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| NOTE 1: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2.NOTE 2: target NR cell has the same SCS, BW and duplex mode as NR serving cell |  |

Table A.14.5.2.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| NR RF Channel Number |  | Config 1,2 | 1, 2 | Two FR1 NR carrier frequencies is used. |
| Active cell |  | Config 1,2 | NR Cell 1 (Pcell) | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2 | NR Cell 2 | NR Cell 2 is on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1,2 | 0 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2 | 9 |  |
| A3-Offset | dB | Config 1,2 | -6 |  |
| Hysteresis | dB | Config 1,2 | 0 |  |
| CP length |  | Config 1,2 | Normal |  |
| TimeToTrigger | s | Config 1,2 | 0 |  |
| Filter coefficient |  | Config 1,2 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | Config 1,2 | 3 ms | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
| T1 | s | Config 1,2 | 5 |  |
| T2 | s | Config 1,2 | 1 |  |

Table A.14.5.2.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  | Config 1,2 | 1 |  | 2 |  |
| Satellite information |  |  | Config 1 | SSC.1 |  | NSC.1 |  |
|  |  |  | Config 2 | SSC.2 |  | NSC.2 |  |
| Duplex mode |  |  | Config 1,2 | FDD |  |  |  |
| BWchannel |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  |  |  |
| BWP BW |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  |  |  |
| BWP configuration | Initial DL BWP | Config 1 | Config 1,2 | DLBWP.0.1 |  | NA |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | NA |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | NA |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  | Config 1,2 | TRS.1.1 FDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1,2 | SR.1.1 FDD |  |  |  |
| RMSI CORESET Reference Channel |  |  | Config 1,2 | CR.1.1 FDD |  |  |  |
| Dedicated CORESET Reference Channel |  |  | Config 1,2 | CCR.1.1 FDD |  |  |  |
| SSB parameters |  |  | Config 1,2 | SSB.1 FR1 |  | SSB.5 FR1 |  |
| SMTC configuration defined in A.3.11 |  |  | Config 1,2 | SMTC.2 |  | SMTC.5 |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1,2 | 15 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | Config 1,2 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2 | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2 | -98 |  | -98 |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2 | -94 | -94 | -Infinity | -91 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  | dBm/9.36 MHz | Config 1,2 | -64.59 | -64.59 | -70.05 | -62.26 |
| Propagation Condition |  |  | Config 1,2 | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |  |  |  |

##### A.14.5.2.1.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 UE is not required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.2.2 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used with single gap for satellite access

##### A.14.5.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3C.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.14.5.2.2.1-1, A.14.5.2.2.1-2 and A.14.5.2.2.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.14.5.2.2.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.14.5.2.2.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

| Config | Description |
| --- | --- |
| 1 | GSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NGSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| NOTE 1: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2.NOTE 2: target NR cell has the same SCS, BW and duplex mode as NR serving cell |  |

Table A.14.5.2.2.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| NR RF Channel Number |  | Config 1,2 | 1, 2 |  | Two FR1 NR carrier frequencies is used. |
| Active cell |  | Config 1,2 | NR Cell 1 (Pcell) |  | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2 | NR Cell 2 |  | NR Cell 2 is on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1,2 | 0 |  | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2 | 9 |  |  |
| A3-Offset | dB | Config 1,2 | -6 |  |  |
| Hysteresis | dB | Config 1,2 | 0 |  |  |
| CP length |  | Config 1,2 | Normal |  |  |
| TimeToTrigger | s | Config 1,2 | 0 |  |  |
| Filter coefficient |  | Config 1,2 | 0 |  | L3 filtering is not used |
| DRX |  | Config 1,2 | DRX.1 | DRX. 7 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | Config 1,2 | 3 ms |  | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
| T1 | s | Config 1,2 | 5 |  |  |
| T2 | s | Config 1,2 | 1.1 | 11 |  |

Table A.14.5.2.2.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  | Config 1,2 | 1 |  | 2 |  |
| Satellite information |  |  | Config 1 | SSC.1 |  | NSC.1 |  |
|  |  |  | Config 2 | SSC.2 |  | NSC.2 |  |
| Duplex mode |  |  | Config 1,2 | FDD |  |  |  |
| BWchannel |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  |  |  |
| BWP BW |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  |  |  |
| BWP configuration | Initial DL BWP |  | Config 1,2 | DLBWP.0.1 |  | NA |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | NA |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | NA |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  | Config 1,2 | TRS.1.1 FDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1,2 | SR.1.1 FDD |  |  |  |
| RMSI CORESET Reference Channel |  |  | Config 1,2 | CR.1.1 FDD |  |  |  |
| Dedicated CORESET Reference Channel |  |  | Config 1,2 | CCR.1.1 FDD |  |  |  |
| SSB parameters |  |  | Config 1,2 | SSB.1 FR1 |  | SSB.5 FR1 |  |
| SMTC configuration defined in A.3.11 |  |  | Config 1,2 | SMTC.2 |  | SMTC.5 |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1,2 | 15 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | Config 1,2 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2 | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2 | -98 |  | -98 |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2 | -94 | -94 | -Infinity | -91 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  | dBm/9.36 MHz | Config 1,2 | -64.59 | -64.59 | -70.05 | -62.2 |
| Propagation Condition |  |  | Config 1,2 | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |  |  |  |

Table A.14.5.2.2.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

| Field | Test1 | Test2 | Comment |
| --- | --- | --- | --- |
|  | Value | Value |  |
| drx-onDurationTimer | ms1 | ms1 | As specified in clause 6.3.2 in TS 38.331 [2] |
| drx-InactivityTimer | ms1 | ms1 |  |
| drx-RetransmissionTimerDL | sl1 | sl1 |  |
| drx-RetransmissionTimerUL | sl1 | sl1 |  |
| drx-LongCycleStartOffset | ms40 | Ms640 |  |
| shortDRX | disable | disable |  |

Table A.14.5.2.2.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

| Field | Value | Comment |
| --- | --- | --- |
| TimeAlignmentTimer | ms500 | As specified in clause 6.3.2 in TS 38.331 [2] |

##### A.14.5.2.2.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1080 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 10240 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2 UE is not required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.2.3 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used with single gap for satellite access

##### A.14.5.2.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3C.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.14.5.2.3.1-1, A.14.5.2.3.1-2 and A.14.5.2.3.1-3.

In test 1 measurement gap pattern configuration # 0 as defined in table A.14.5.2.3.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.14.5.2.3.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1

| Config | Description |
| --- | --- |
| 1 | GSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NGSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| NOTE 1: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2.NOTE 2: target NR cell has the same SCS, BW and duplex mode as NR serving cell |  |

Table A.14.5.2.3.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
|  |  |  | Test 1 |  |
| NR RF Channel Number |  | Config 1,2 | 1, 2 | Two FR1 NR carrier frequencies is used. |
| Active cell |  | Config 1,2 | NR Cell 1 (Pcell) | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2 | NR Cell 2 | NR Cell 2 is on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1,2 | 0 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2 | 9 |  |
| A3-Offset | dB | Config 1,2 | -6 |  |
| Hysteresis | dB | Config 1,2 | 0 |  |
| CP length |  | Config 1,2 | Normal |  |
| TimeToTrigger | s | Config 1,2 | 0 |  |
| Filter coefficient |  | Config 1,2 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2 | OFF | DRX is not used |
| Time offset between serving and neighbour cells |  | Config 1,2 | 3 ms | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
| T1 | s | Config 1,2 | 5 |  |
| T2 | s | Config 1,2 | 1.1 |  |

Table A.14.5.2.3.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 |
| NR RF Channel Number |  |  | Config 1,2 | 1 |  | 2 |  |
| Satellite information |  |  | Config 1 | SSC.1 |  |  |  |
|  |  |  | Config 2 | SSC.2 |  |  |  |
| Duplex mode |  |  | Config 1,2 | FDD |  |  |  |
| BWchannel |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  |  |  |
| BWP BW |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  |  |  |
| BWP configuration | Initial DL BWP | Config 1 | Config 1,2 | DLBWP.0.1 |  | NA |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | NA |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | NA |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | NA |  |
| TRS configuration |  |  | Config 1,2 | TRS.1.1 FDD |  | NA |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2 | OP.1 |  | OP.1 |  |
| PDSCH Reference measurement channel |  |  | Config 1,2 | SR.1.1 FDD |  |  |  |
| RMSI CORESET Reference Channel |  |  | Config 1,2 | CR.1.1 FDD |  |  |  |
| Dedicated CORESET Reference Channel |  |  | Config 1,2 | CCR.1.1 FDD |  |  |  |
| SSB parameters |  |  | Config 1,2 | SSB.1 FR1 |  | SSB.5 FR1 |  |
| SMTC configuration defined in A.3.11 |  |  | Config 1,2 | SMTC.2 |  | SMTC.5 |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1,2 | 15 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | Config 1,2 | 0 |  | 0 |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2 | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2 | -98 |  | -98 |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2 | -94 | -94 | -Infinity | -91 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| IoNote3 |  | dBm/9.36 MHz | Config 1,2 | -64.59 | -64.59 | -70.05 | -62.2 |
| Propagation Condition |  |  | Config 1,2 | AWGN |  | AWGN |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |  |  |  |

##### A.14.5.2.3.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1040 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 UE is required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.2.4 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in fully non-overlapped for satellite access

##### A.14.5.2.4.1 Test Purpose and Environment

The purpose of this test is to verify that the multiple gaps capable UE makes correct reporting of events. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3C.4.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2, and NR Cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.14.5.2.4.1-1, A.14.5.2.4.1-2 and A.14.5.2.4.1-3.

In this test measurement gap pattern configuration # 0 as defined in table A.14.5.2.4.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2 and NR Cell 3.

Table A.14.5.2.4.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

| Config | Description |
| --- | --- |
| 1 | GSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NGSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| NOTE 1: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2.NOTE 2: target NR cell has the same SCS, BW and duplex mode as NR serving cell |  |

Table A.14.5.2.4.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1,2 | 1, 2 | Two FR1 NR carrier frequencies is used. |
| Active cell |  | Config 1,2 | NR Cell 1 (Pcell) | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2 | NR Cell 2 and NR Cell 3 | NR Cell 2 and NR Cell 3 are on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1,2 | 0 for MeasGapId #10 for MeasGapId #2 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2 | 9 for MeasGapId #119 for MeasGapId #2 |  |
| A3-Offset | dB | Config 1,2 | -6 |  |
| Hysteresis | dB | Config 1,2 | 0 |  |
| CP length |  | Config 1,2 | Normal |  |
| TimeToTrigger | s | Config 1,2 | 0 |  |
| Filter coefficient |  | Config 1,2 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2 | OFF | DRX is not used |
| Time offset between serving and neighbour Cell 2,3 |  | Config 1,2 | 3 ms | Asynchronous cells.The timing of Cell 2 and Cell 3 is 3 ms later than the timing of Cell 1. |
| T1 | s | Config 1,2 | 5 |  |
| T2 | s | Config 1,2 | 1 |  |

Table A.14.5.2.4.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  | Cell 3 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 | T1 | T2 |  |
| NR RF Channel Number |  |  | Config 1,2 | 1 |  | 2 |  | 2 |  |  |
| Satellite information |  |  | Config 1 | SSC.1 |  | NSC.1 |  |  |  |  |
|  |  |  | Config 2 | SSC.2 |  | NSC.2 |  |  |  |  |
| Duplex mode |  |  | Config 1,2 | FDD |  |  |  |  |  |  |
| BWchannel |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  |  |  |  |  |  |
| BWP BW |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  |  |  |  |  |  |
| BWP configuration | Initial DL BWP |  | Config 1,2 | DLBWP.0.1 |  | NA |  | NA |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | NA |  | NA |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | NA |  | NA |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | NA |  | NA |  |  |
| TRS configuration |  |  | Config 1,2 | TRS.1.1 FDD |  | NA |  | NA |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2 | OP.1 |  | OP.1 |  | OP.1 |  |  |
| PDSCH Reference measurement channel |  |  | Config 1,2 | SR.1.1 FDD |  |  |  |  |  |  |
| RMSI CORESET Reference Channel |  |  | Config 1,2 | CR.1.1 FDD |  |  |  |  |  |  |
| Dedicated CORESET Reference Channel |  |  | Config 1,2 | CCR.1.1 FDD |  |  |  |  |  |  |
| SSB parameters |  |  | Config 1,2 | SSB.1 FR1 |  | SSB.5 FR1 |  | SSB.1 FR1 |  |  |
| SMTC configuration defined in A.3.11 |  |  | Config 1,2 | SMTC.2 |  | SMTC.5 |  | SMTC.1 |  |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1,2 | 15 |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | Config 1,2 | 0 |  | 0 |  | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2 | -98 |  | -98 |  | -98 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2 | -98 |  | -98 |  | -98 |  |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2 | -94 | -94 | -Infinity | -91 | -Infinity |  | -91 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2 | 4 | 4 | -Infinity | -0.79 | -Infinity |  | -0.79 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 | -Infinity |  | 7 |
| IoNote3 |  | dBm/9.36 MHz | Config 1,2 | -64.59 | -64.59 | -70.05 | -59.62 | -70.05 |  | -59.62 |
| Propagation Condition |  |  | Config 1,2 | AWGN |  | AWGN |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |  |  |  |  |  |  |

##### A.14.5.2.4.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 UE is not required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.


#### A.14.5.2.5 void

##### A.14.5.2.5.1 void

##### A.14.5.2.5.2 void

#### A.14.5.2.6 SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in partially partial overalpping for satellite access

##### A.14.5.2.6.1 Test Purpose and Environment

The purpose of this test is to verify that the multiple gaps capable UE makes correct reporting of events. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3C.4.

In this test, there are three cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2, and NR Cell 3 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.14.5.2.6.1-1, A.14.5.2.6.1-2 and A.14.5.2.6.1-3.

In test 1 measurement gap pattern configuration # 0 and #1 as defined in table A.14.5.2.6.1-2 are provided. MeasGapId #2 is configured with a higher priority than MeasGapId #1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2 and NR Cell 3.

Table A.14.5.2.6.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

| Config | Description |
| --- | --- |
| 1 | GSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NGSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| NOTE 1: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2.NOTE 2: target NR cells have the same SCS, BW and duplex mode as NR serving cell |  |

Table A.14.5.2.6.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1,2 | 1, 2 | Two FR1 NR carrier frequencies is used. |
| Active cell |  | Config 1,2 | NR Cell 1 (Pcell) | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2 | NR Cell 2 and NR Cell 3 | NR Cell 2 and NR Cell 3 are on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1,2 | 0 for MeasGapId #11 for MeasGapId #2 | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2 | 39 for MeasGapId #14 for MeasGapId #2 |  |
| A3-Offset | dB | Config 1,2 | -6 |  |
| Hysteresis | dB | Config 1,2 | 0 |  |
| CP length |  | Config 1,2 | Normal |  |
| TimeToTrigger | s | Config 1,2 | 0 |  |
| Filter coefficient |  | Config 1,2 | 0 | L3 filtering is not used |
| DRX |  | Config 1,2 | OFF | DRX is not used |
| Time offset between serving and neighbour Cell 1 |  | Config 1,2 | 3s | Synchronous. |
| Time offset between serving and neighbour Cell 2 |  | Config 1,2 | 5 ms | Asynchronous.The timing of Cell 3 is 5 ms later than the timing of Cell 1. |
| T1 | s | Config 1,2 | 5 |  |
| T2 | s | Config 1,2 | 1.5 |  |

Table A.14.5.2.6.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

| Parameter |  | Unit | Test configuration | Cell 1 |  | Cell 2 |  | Cell 3 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | T1 | T2 | T1 | T2 | T1 | T2 |  |
| NR RF Channel Number |  |  | Config 1,2 | 1 |  | 2 |  | 2 |  |  |
| Satellite information |  |  | Config 1 | SSC.1 |  | NSC.1 |  |  |  |  |
|  |  |  | Config 2 | SSC.2 |  | NSC.2 |  |  |  |  |
| Duplex mode |  |  | Config 1,2 | FDD |  |  |  |  |  |  |
| BWchannel |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  |  |  |  |  |  |
| BWP BW |  | MHz | Config 1,2 | 10: NPRB,c = 52 |  |  |  |  |  |  |
| BWP configuration | Initial DL BWP |  | Config 1,2 | DLBWP.0.1 |  | NA |  | NA |  |  |
|  | Initial UL BWP |  |  | ULBWP.0.1 |  | NA |  | NA |  |  |
|  | Dedicated DL BWP |  |  | DLBWP.1.1 |  | NA |  | NA |  |  |
|  | Dedicated UL BWP |  |  | ULBWP.1.1 |  | NA |  | NA |  |  |
| TRS configuration |  |  | Config 1,2 | TRS.1.1 FDD |  | NA |  | NA |  |  |
| OCNG Patterns defined in A.3.2.1.1 (OP.1) |  |  | Config 1,2 | OP.1 |  | OP.1 |  | OP.1 |  |  |
| PDSCH Reference measurement channel |  |  | Config 1,2 | SR.1.1 FDD |  |  |  |  |  |  |
| RMSI CORESET Reference Channel |  |  | Config 1,2 | CR.1.1 FDD |  |  |  |  |  |  |
| Dedicated CORESET Reference Channel |  |  | Config 1,2 | CCR.1.1 FDD |  |  |  |  |  |  |
| SSB parameters |  |  | Config 1,2 | SSB.1 FR1 |  | SSB.1 FR1 |  | SSB.1 FR1 |  |  |
| SMTC configuration defined in A.3.11 |  |  | Config 1,2 | SMTC.2 |  | SMTC.2 |  | SMTC.12 |  |  |
| PDSCH/PDCCH subcarrier spacing |  | kHz | Config 1,2 | 15 |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | Config 1,2 | 0 |  | 0 |  | 0 |  |  |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/15 kHz | Config 1,2 | -98 |  | -98 |  | -98 |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 |  | dBm/SCS | Config 1,2 | -98 |  | -98 |  | -98 |  |  |
| SS-RSRP Note 3 |  | dBm/SCS | Config 1,2 | -94 | -94 | -Infinity | -91 | -Infinity |  | -91 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  | dB | Config 1,2 | 4 | 4 | -Infinity | -0.79 | -Infinity |  | -0.79 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | Config 1,2 | 4 | 4 | -Infinity | 7 | -Infinity |  | 7 |
| IoNote3 |  | dBm/9.36 MHz | Config 1,2 | -64.59 | -64.59 | -70.05 | -59.62 | -70.05 |  | -59.62 |
| Propagation Condition |  |  | Config 1,2 | AWGN |  | AWGN |  | AWGN |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port. |  |  |  |  |  |  |  |  |  |  |

##### A.14.5.2.6.2 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1280 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.2.7 Event triggered reporting test without gap under non-DRX

##### A.14.5.2.7.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the inter-frequency cell search requirements in clauses 9.3C.7.

##### A.14.5.2.7.2 Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) on NR RF channel 1 and a FR1 neighbour cell (Cell 2) on NR RF channel 2. The test parameters for PCell and neighbour cell are given in table A.14.5.2.7.2-1, A.14.5.2.7.2-2 and A.14.5.2.7.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The UE shall be provided with the valid information about the SAN serving each cell in the test before the test.

UE is configured with 2 non-overlapping SMTCs. The SMTC periodicity is 20 ms, and SMTC1 is associated with Cell 1 with offset 0, and SMTC2 is associated with Cell 2 with offset 10 ms.

Table A.14.5.2.7.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

Table A.14.5.2.7.2-2: General test parameters for inter-frequency event triggered reporting without gap for FR1

| Parameter | Unit | Test configuration | Value | Comment |
| --- | --- | --- | --- | --- |
| Active cell |  | 1, 2 | Cell 1 |  |
| Neighbour cell |  | 1, 2 | Cell 2 | Cell to be identified. |
| RF Channel Number |  | 1, 2 | 1: Cell 12: Cell 2 |  |
| SMTC1 configuration |  | 1 | SMTC.1 | Period: 20 ms, offset: 0 |
| SMTC2 configuration |  | 2 | SMTC.4 | Period: 20 ms, offset: 10 ms |
| A3-Offset | dB | 1, 2 | -4.5 |  |
| CP length |  | 1, 2 | Normal |  |
| Hysteresis | dB | 1, 2 | 0 |  |
| Time To Trigger | s | 1, 2 | 0 |  |
| Filter coefficient |  | 1, 2 | 0 | L3 filtering is not used |
| DRX |  | 1, 2 |  | OFF |
| Time offset between serving and neighbour cells |  | 1, 2 | 10 ms | Asynchronous cells.The timing of Cell 2 is 10 ms later than the timing of Cell 1. |
| T1 | s | 1, 2 | 5 |  |
| T2 | s | 1, 2 | 5 |  |

Table A.14.5.2.7.2-3: NR Cell specific test parameters for inter-frequency event triggered reporting without gap for FR1

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1 | SSC.1 |  | NSC.1 |  |
|  |  | 2 | SSC.2 |  | NSC.2 |  |
| SSB configuration |  | 1, 2 | SSB.1 FR1 |  | SSB.1 FR1 |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 FDD |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CR.1.1 FDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | CCR.1.1 FDD |  | N/A |  |
| OCNG Patterns |  | 1, 2 | OP.1 |  | OP.1 |  |
| TRS Configuration |  | 1, 2 | TRS.1.1 FDD |  | N/A |  |
| IInitial BWP configuration |  | 1, 2 | DLBWP.0.1 ULBWP.0.1 |  | DLBWP.0.1 ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1, 2 | DLBWP.1.1 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.1 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1, 2 | SSB |  | SSB |  |
| Note 2 | dBm/SCS | 1, 2 | -98 |  |  |  |
| Note 2 | dBm/15 kHz | 1, 2 | -98 |  |  |  |
|  | dB | 1, 2 | 4 | 4 | -Infinity | 4 |
|  | dB | 1, 2 | 4 | 4 | -Infinity | 4 |
| SS-RSRP Note 3 | dBm/SCS kHz | 1, 2 | -94 | -94 | -Infinity | -94 |
| Io | dBm/9.36 MHz | 1, 2 | -64.60 | -64.60 | -70.05 | -64.60 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.14.5.2.7.3 Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.2.8 Event triggered reporting tests without gap under DRX

##### A.14.5.2.8.1 Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the inter-frequency cell search requirements in clauses 9.3C.7.

##### A.14.5.2.8.2 Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) on NR RF channel 1 and a FR1 neighbour cell (Cell 2) on NR RF channel 2. The test parameters for PCell and neighbour cell are given in table A.14.5.2.8.2-1, A.14.5.2.8.2-2 and A.14.5.2.8.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

The UE shall be provided with the valid information about the SAN serving each cell in the test before the test.

UE is configured with 2 non-overlapping SMTCs. The SMTC periodicity is 20 ms, and SMTC1 is associated with Cell 1 with offset 0, and SMTC2 is associated with Cell 2 with offset 10 ms.

Table A.14.5.2.8.2-1: Supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

Table A.14.5.2.8.2-2: General test parameters for inter-frequency event triggered reporting without gap for PCell in FR1 with DRX

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Test 1 | Test 2 |  |
| Active cell |  | 1, 2 | Cell 1 |  |  |
| Neighbour cell |  | 1, 2 | Cell 2 |  | Cell to be identified. |
| RF Channel Number |  | 1, 2 | 1: Cell 12: Cell 2 |  |  |
| SMTC1 configuration |  | 1 | SMTC.1 |  | Period: 20 ms, offset: 0 |
| SMTC2 configuration |  | 2 | SMTC.4 |  | Period: 20 ms, offset: 10 ms |
| A3-Offset | dB | 1, 2 | -4.5 |  |  |
| CP length |  | 1, 2 | Normal |  |  |
| Hysteresis | dB | 1, 2 | 0 |  |  |
| Time To Trigger | s | 1, 2 | 0 |  |  |
| Filter coefficient |  | 1, 2 | 0 |  | L3 filtering is not used |
| DRX |  | 1, 2 | DRX.1 | DRX. 7 |  |
| Time offset between serving and neighbour cells |  | 1, 2 | 3 s |  | Synchronous cells |
| T1 | s | 1, 2 | 5 |  |  |
| T2 | s | 1, 2 | 5 | 15 |  |

Table A.14.5.2.8.2-3: NR Cell specific test parameters for inter-frequency event triggered reporting without gap for PCell in FR1 with DRX

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Satellite information |  | 1 | SSC.1 |  | NSC.1 |  |
|  |  | 2 | SSC.2 |  | NSC.2 |  |
| SSB configuration |  | 1, 2 | SSB.1 FR1 |  | SSB.1 FR1 |  |
| PDSCH RMC configuration |  | 1, 2 | SR.1.1 FDD |  | N/A |  |
| RMSI CORESET RMC configuration |  | 1, 2 | CR.1.1 FDD |  | N/A |  |
| Dedicated CORESET RMC configuration |  | 1, 2 | CCR.1.1 FDD |  | N/A |  |
| OCNG Patterns |  | 1, 2 | OP.1 |  | OP.1 |  |
| TRS configuration |  | 1, 2 | TRS.1.1 FDD |  | N/A |  |
| Initial BWP configuration |  | 1, 2 | DLBWP.0.1 ULBWP.0.1 |  | DLBWP.0.1 ULBWP.0.1 |  |
| Active DL BWP configuration |  | 1, 2 | DLBWP.1.1 |  | DLBWP.1.1 |  |
| Active UL BWP configuration |  | 1, 2 | ULBWP.1.1 |  | ULBWP.1.1 |  |
| RLM-RS |  | 1, 2 | SSB |  | SSB |  |
| Note 2 | dBm/SCS | 1, 2 | -98 |  |  |  |
| Note 2 | dBm/15 kHz | 1, 2 | -98 |  |  |  |
|  | dB | 1, 2 | 4 | 4 | -Infinity | 4 |
|  | dB | 1, 2 | 4 | 4 | -Infinity | 4 |
| SS-RSRP Note 3 | dBm/SCS kHz | 1, 2 | -94 | -94 | -Infinity | -94 |
| Io | dBm/9.36 MHz | 1, 2 | -64.60 | -64.60 | -70.05 | -64.60 |
| Propagation Condition |  | 1, 2 | AWGN |  |  |  |
| NOTE 1: The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: SS-RSRP levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.14.5.2.8.3 Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. X=1280 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise X=920.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Y ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. Y=12800 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise Y=6400.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.2.9 SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used with single gap for 3 MHz channel bandwidth in satellite access

##### A.14.5.2.9.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3C.4. This test is applicable for UEs that support less than 5 MHz operation.

The test procedure in clause A.14.5.2.3 applies for this test. Supported test configurations are specified in Table A.14.5.2.9.1-1. The list of general and NR specific test configuration reuse those in test clause A.14.5.2.3, except for those provided in Tables A.14.5.2.9.1-2 and A.14.5.2.9.1-3.

Table A.14.5.2.9.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1

| Config | Description |
| --- | --- |
| 1 | GSO, NR 15 kHz SSB SCS, 3 MHz bandwidth, FDD duplex mode |
| 2 | NGSO, NR 15 kHz SSB SCS, 3 MHz bandwidth, FDD duplex mode |
| NOTE 1: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2.NOTE 2: target NR cell has the same SCS, BW and duplex mode as NR serving cell |  |

Table A.14.5.2.9.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection in operation with 3 MHz Channel Bandwith

| Parameter | Unit | Test configuration | Value |  | Comment |
| --- | --- | --- | --- | --- | --- |
| NR RF Channel Number |  | Config 1,2 | 1, 2 |  | Two FR1 NR carrier frequencies is used. |
| Active cell |  | Config 1,2 | NR Cell 1 (Pcell) |  | NR Cell 1 is on NR RF channel number 1. |
| Neighbour cell |  | Config 1,2 | NR Cell 2 |  | NR Cell 2 is on NR RF channel number 2. |
| Gap Pattern Id |  | Config 1,2 | 0 |  | As specified in clause 9.1.2-1. |
| Measurement gap offset |  | Config 1,2 | 9 |  |  |
| A3-Offset | dB | Config 1,2 | -6 |  |  |
| Hysteresis | dB | Config 1,2 | 0 |  |  |
| CP length |  | Config 1,2 | Normal |  |  |
| TimeToTrigger | s | Config 1,2 | 0 |  |  |
| Filter coefficient |  | Config 1,2 | 0 |  | L3 filtering is not used |
| DRX |  | Config 1,2 | DRX.1 | DRX. 7 | As specified in clause A.3.3 |
| Time offset between serving and neighbour cells |  | Config 1,2 | 3 ms |  | Asynchronous cells.The timing of Cell 2 is 3 ms later than the timing of Cell 1. |
| T1 | s | Config 1,2 | 5 |  |  |
| T2 | s | Config 1,2 | 1.1 | 11 |  |

Table A.14.5.2.9.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection in operation with 3 MHz Channel Bandwith

| Parameter | Unit | Test configuration | Cell 1 |  | Cell 2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| PDSCH Reference measurement channel |  | Config 1,2 | SR.1.2FDD |  |  |  |
| RMSI CORESET Reference Channel |  | Config 1,2 | CR.1.3 FDD |  |  |  |
| Dedicated CORESET Reference Channel |  | Config 1,2 | CCR.1.7 FDD |  |  |  |
| SSB parameters |  | Config 1,2 | SSB.13 FR1 |  | SSB.13 FR1 |  |
| SMTC configuration defined in A.3.11 |  | Config 1,2 | SMTC.2 |  | SMTC.2 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | dBm/15 kHz | Config 1,2 | -98 |  | -98 |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | dBm/SCS | Config 1,2 | -98 |  | -98 |  |
| SS-RSRP Note 3 | dBm/SCS | Config 1,2 | -94 | -94 | -Infinity | -91 |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] | dB | Config 1,2 | 4 | 4 | -Infinity | 7 |
| IoNote3 | dBm/2.7 MHz | Config 1,2 | -69.99 | -69.99 | -75.44 | -67.60 |

##### A.14.5.2.9.2 Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1440 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

### A.14.5.3 L1-RSRP measurement for beam reporting for satellite access

#### A.14.5.3.1 SSB based L1-RSRP measurement for satellite access when DRX is not used

##### A.14.5.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4C.1, with the testing configurations for NR cells served by satellite access node (SAN) in Table A.14.5.3.1.1-1.

Table A.14.5.3.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test for satellite access

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 3 | NGSO with varying Doppler and delay shift NTN channel model, NR FDD, 15 kHz SSB SCS, 10 MHz BW |
| Note: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

##### A.14.5.3.1.2 Test parameters

There is one cells in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.14.5.3.1.2-1 and table A.14.5.3.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.14.5.3.1.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB ARFCN | 1, 2, 3 |  | freq1 |
| Duplex mode | 1, 2, 3 |  | FDD |
|  |  |  |  |
|  |  |  |  |
| TDD Configuration | 1, 2, 3 |  | N/A |
|  |  |  |  |
|  |  |  |  |
| BWchannel | 1, 2, 3 | MHz | 10: NPRB,c = 52 |
|  |  |  |  |
|  |  |  |  |
| Satellite information | 1 |  | SSC.1 |
|  | 2, 3 |  | SSC.2 |
| PDSCH Reference measurement channel | 1, 2, 3 |  | SR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| RMSI CORESET Reference Channel | 1, 2, 3 |  | CR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| Dedicated CORESET Reference Channel | 1, 2, 3 |  | CCR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| SSB configuration | 1, 2, 3 |  | SSB.3 FR1 |
|  |  |  |  |
|  |  |  |  |
| OCNG Patterns | 1, 2, 3 |  | OP.1 |
| Initial BWP Configuration | 1, 2, 3 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1, 2, 3 |  | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration | 1, 2, 3 |  | SMTC.1 |
| TRS Configuration | 1, 2, 3 |  | TRS.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| DRX configuration | 1, 2, 3 |  | Off |
| reportConfigType | 1, 2, 3 |  | periodic |
| reportQuantity | 1, 2, 3 |  | ssb-Index-RSRP |
| Number of reported RS | 1, 2, 3 |  | 2 |
| L1-RSRP reporting period | 1, 2, 3 | slot | 80 |
| T1 | 1, 2, 3 | s | 5 |
| T2 | 1, 2, 3 | s | 1 |
| EPRE ratio of PSS to SSS | 1, 2, 3 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1, 2 |  | AWGN |
|  | 3 |  | AWGN with time varying Doppler and delay shifts |
| UE position | 1, 2, 3 |  | NOTE 3 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: For Config 3, the initial ephemerisInfo of SSC.2 refers to Table G.4.1-1 of TS 38.101-5 [43].NOTE 3: For Config 3, the UE position is set by AT command according to G.4.2 of TS 38.101-5 [43] at the beginning if the test, and remains unchanged during the test. |  |  |  |

Table A.14.5.3.1.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Note2 | 1, 2, 3 | dBm/15 kHz | -94.65 |  |  |  |
| Note2 | 1, 2, 3 | dBm/SSB SCS | -94.65 |  |  |  |
|  | 1, 2, 3 | dB | 0 | 0 | -Infinity | 3 |
| SSB RSRP Note3 | 1, 2, 3 | dBm/SSB SCS | -94.65 | -94.65 | -Infinity | -91.65 |
|  |  |  |  |  |  |  |
| Io Note3 | 1, 2, 3 | dBm/9.36 MHz | -63.69 | -63.69 | -66.70 | -61.93 |
|  | 1, 2, 3 | dB | 0 | 0 | -Infinity | 3 |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.14.5.3.1.3 Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19C.1.1 and relative accuracy requirement in clause 10.1.19C.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.3.2 SSB based L1-RSRP measurement for satellite access when DRX is used

##### A.14.5.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.1, with the testing configurations for NR cells served by satellite access node (SAN)in table A.14.5.3.2.1-1.

Table A.14.5.3.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test for satellite access

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

##### A.14.5.3.2.2 Test parameters

There is one cells in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.14.5.3.2.2-1 and table A.14.5.3.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.14.5.3.2.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB ARFCN | 1, 2 |  | freq1 |
| Duplex mode | 1, 2 |  | FDD |
|  |  |  |  |
|  |  |  |  |
| TDD Configuration | 1, 2 |  | N/A |
|  |  |  |  |
|  |  |  |  |
| BWchannel | 1, 2 | MHz | 10: NPRB,c = 52 |
|  |  |  |  |
|  |  |  |  |
| Satellite information | 1 |  | SSC.1 |
|  | 2 |  | SSC.2 |
| PDSCH Reference measurement channel | 1, 2 |  | SR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| RMSI CORESET Reference Channel | 1, 2 |  | CR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| Dedicated CORESET Reference Channel | 1, 2 |  | CCR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| SSB configuration | 1, 2 |  | SSB.3 FR1 |
|  |  |  |  |
|  |  |  |  |
| OCNG Patterns | 1, 2 |  | OP.1 |
| Initial BWP Configuration | 1, 2 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1, 2 |  | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration | 1, 2 |  | SMTC.1 |
| TRS Configuration | 1, 2 |  | TRS.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| DRX configuration | 1, 2 |  | DRX.3 |
| reportConfigType | 1, 2 |  | periodic |
| reportQuantity | 1, 2 |  | ssb-Index-RSRP |
| Number of reported RS | 1, 2 |  | 2 |
| L1-RSRP reporting period | 1, 2 | slot | 80 |
| T1 | 1, 2 | s | 5 |
| T2 | 1, 2 | s | 1 |
| EPRE ratio of PSS to SSS | 1, 2 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1, 2 |  | AWGN |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |

Table A.14.5.3.2.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |
| Note2 | 1, 2 | dBm/15 kHz | -94.65 |  |  |  |
| Note2 | 1, 2 | dBm/SSB SCS | -94.65 |  |  |  |
|  | 1, 2 | dB | 0 | 0 | -Infinity | 3 |
| SSB RSRP Note3 | 1, 2 | dBm/SSB SCS | -94.65 | -94.65 | -Infinity | -91.65 |
| Io Note3 | 1, 2 | dBm/9.36 MHz | -63.69 | -63.69 | -66.70 | -61.93 |
|  | 1, 2 | dB | 0 | 0 | -Infinity | 3 |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |  |

##### A.14.5.3.2.3 Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19C.1.1 and relative accuracy requirement in clause 10.1.19C.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.3.3 CSI-RS based L1-RSRP measurement for satellite access when DRX is not used

##### A.14.5.3.3.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells served by satellite access node (SAN)  in table A.14.5.3.3.1-1.

Table A.14.5.3.3.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test for satellite access

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

##### A.14.5.3.3.2 Test parameters

There is one cells in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.14.5.3.3.2-1 and table A.14.5.3.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot 2 of a frame and UE provides the report back based on the reporting configuration as defined in table A.14.5.3.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.14.5.3.3.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB GSCN | 1, 2 |  | freq1 |
| Duplex mode | 1, 2 |  | FDD |
| TDD Configuration | 1, 2 |  | N/A |
| BWchannel | 1, 2 | MHz | 10: NRB,c = 52 |
| Satellite information | 1 |  | SSC.1 |
|  | 2 |  | SSC.2 |
| PDSCH Reference measurement channel | 1, 2 |  | SR.1.1 FDD |
| RMSI CORESET Reference Channel | 1, 2 |  | CR.1.1 FDD |
| Dedicated CORESET Reference Channel | 1, 2 |  | CCR.1.1 FDD |
| SSB configuration | 1, 2 |  | SSB.3 FR1 |
| CSI-RS configuration | 1, 2 |  | CSI-RS 1.3 FDD |
| OCNG Patterns | 1, 2 |  | OP.1 |
| TRS Configuration | 1, 2 |  | TRS.1.1 FDD |
| Initial BWP Configuration | 1, 2 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1, 2 |  | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration | 1, 2 |  | SMTC.1 |
| DRX configuration | 1, 2 |  | Off |
| reportConfigType | 1, 2 |  | aperiodic |
| reportQuantity | 1, 2 |  | cri-RSRP |
| Number of reported RS | 1, 2 |  | 2 |
| qcl-Info | 1, 2 |  | SSB#0 for resource#0 |
|  |  |  | SSB#1 for resource#1 |
| reportSlotOffsetList | 1, 2 | slots | 8 |
| T1 | 1, 2 | s | 5 |
| EPRE ratio of PSS to SSS | 1, 2 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1, 2 |  | AWGN |
| Note 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |

Table A.14.5.3.3.2-2: CSI-RS specific test parameters

| Parameter | Config | Unit | CSI-RS#0 | CSI-RS#1 |
| --- | --- | --- | --- | --- |
| Note1 | 1, 2 | dBm/15 kHz | -94.65 |  |
| Note1 | 1, 2 | dBm/SSB SCS | -94.65 |  |
|  |  |  |  |  |
|  | 1, 2 | dB | 0 | 3 |
| CSI-RS RSRP Note2 | 1, 2 | dBm/SSB SCS | -94.65 | -91.65 |
|  | 1, 2 |  |  |  |
| Io Note2 | 1, 2 | dBm/9.36 MHz | -63.69 | -61.93 |
|  | 1, 2 |  |  |  |
|  | 1, 2 | dB | 0 | 3 |
| NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: CSI-RS RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |

##### A.14.5.3.3.3 Test Requirements

After 80ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.19C.1.1 and relative accuracy requirement in clause 10.1.19C.1.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.3.4 CSI-RS based L1-RSRP measurement for satellite access when DRX is used

##### A.14.5.3.4.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5.4.2, with the testing configurations for NR cells served by satellite access node (SAN) in table A.14.5.3.4.1-1.

Table A.14.5.3.4.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test for satellite access

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15kHz, BW 10MHz |
| Note: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

##### A.14.5.3.4.2 Test parameters

There is one cells in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.14.5.3.4.2-1 and table A.14.5.3.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot 2 of a frame and UE provides the report back based on the reporting configuration as defined in table A.14.5.3.4.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.14.5.3.4.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB ARFCN | 1, 2 |  | freq1 |
| Duplex mode | 1, 2 |  | FDD |
|  |  |  |  |
|  |  |  |  |
| TDD Configuration | 1, 2 |  | N/A |
|  |  |  |  |
|  |  |  |  |
| BWchannel | 1, 2 | MHz | 10: NPRB,c = 52 |
|  |  |  |  |
|  |  |  |  |
| Satellite information | 1 |  | SSC.1 |
|  | 2 |  | SSC.2 |
| PDSCH Reference measurement channel | 1, 2 |  | SR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| RMSI CORESET Reference Channel | 1, 2 |  | CR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| Dedicated CORESET Reference Channel | 1, 2 |  | CCR.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| SSB configuration | 1, 2 |  | SSB.3 FR1 |
|  |  |  |  |
|  |  |  |  |
| CSI-RS configuration | 1, 2 |  | CSI-RS 1.3 FDD |
|  |  |  |  |
|  |  |  |  |
| OCNG Patterns | 1, 2 |  | OP.1 |
| TRS Configuration | 1, 2 |  | TRS.1.1 FDD |
|  |  |  |  |
|  |  |  |  |
| Initial BWP Configuration | 1, 2 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1, 2 |  | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration | 1, 2 |  | SMTC.1 |
| DRX configuration | 1, 2 |  | DRX.3 |
| reportConfigType | 1, 2 |  | aperiodic |
| reportQuantity | 1, 2 |  | cri-RSRP |
| Number of reported RS | 1, 2 |  | 2 |
| qcl-Info | 1, 2 |  | SSB#0 for resource#0 |
|  |  |  | SSB#1 for resource#1 |
| reportSlotOffsetList | 1, 2 | slots | 8 |
| T1 | 1, 2 | s | 5 |
| EPRE ratio of PSS to SSS | 1, 2 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1, 2 |  | AWGN |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |

Table A.14.5.3.4.2-2: CSI-RS specific test parameters

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
| NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3:  CSI-RS RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves. |  |  |  |  |  |

##### A.14.5.3.4.3 Test Requirements

After 80ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.19C.1.1 and relative accuracy requirement in clause 10.1.19C.1.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

#### A.14.5.3.5 SSB based L1-RSRP measurement when DRX is not used in FR2-NTN

##### A.14.5.3.5.1 Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5C.4.1, with the testing configurations for NR cells in table A.14.5.3.5.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15C.1.

Table A.14.5.3.5.1-1: Applicable NR configurations for FR2-NTN SSB based L1-RSRP test

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 2 | NGSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 3 | GSO, NR FDD, 30 kHz SSB SCS, 20 MHz BW |
| 4 | NGSO, NR FDD, 30 kHz SSB SCS, 20 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

##### A.14.5.3.5.2 Test parameters

There is one cells in the test, the FR2-NTN PCell (Cell 1). The test parameters for the Cell 1 are given in table A.14.5.3.5.2-1 and table A.14.5.3.5.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.14.5.3.5.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| Satellite configuration | 1, 3 |  | SSC.1 |
|  | 2, 4 |  | SSC.2 |
| SSB ARFCN | 1~4 |  | freq1 |
| Duplex mode | 1~4 |  | FDD |
| BWchannel | 1~2 | MHz | 100: NPRB,c = 66 |
|  | 3~4 |  | 20: NPRB,c = 51 |
| Data PRBs allocated | 1~4 |  | 66 |
| PDSCH Reference measurement channel | 1~2 |  | SR.3.1 TDD |
|  | 3~4 |  | SR.2.1 TDD |
| RMSI CORESET Reference Channel | 1~2 |  | CR.3.1 TDD |
|  | 3~4 |  | CR.2.1 TDD |
| Dedicated CORESET Reference Channel | 1~2 |  | CCR.3.1 TDD |
|  | 3~4 |  | CCR.2.1 TDD |
| SSB configuration | 1~2 |  | SSB.1 FR2 |
|  | 3~4 |  | SSB.1 FR1 |
| OCNG Patterns | 1~4 |  | OP.1 |
| Initial BWP Configuration | 1~4 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1~4 |  | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration | 1~4 |  | SMTC.1 |
| TRS Configuration | 1~2 |  | TRS.2.1 FDD |
|  | 3~4 |  | TRS.1.2 FDD |
| PDCCH/PDSCH TCI Configuration | 1~4 |  | TCI.State.0 |
| DRX configuration | 1~4 |  | Off |
| reportConfigType | 1~4 |  | periodic |
| reportQuantity | 1~4 |  | ssb-Index-RSRP |
| Number of reported RS | 1~4 |  | 2 |
| L1-RSRP reporting period | 1~2 | slot | 320 |
|  | 3~4 |  | 80 |
| T1 | 1~4 | s | 5 |
| T2 | 1~4 | s | 2 |
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

Table A.14.5.3.5.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |  |
| Angle of arrival configuration |  |  | Setup 1 according to A.3.15.1 |  |  |  |  |
| Beam AssumptionNote 4 | 1~4 |  | Rough |  |  |  |  |
| Note2 | 1~4 | dBm/15 kHz | -103.2 |  |  |  |  |
| Note2 | 1~4 | dBm/SSB SCS | -94.2 |  |  |  |  |
|  | 3~4 |  | -100.2 |  |  |  |  |
|  | 1~4 | dB | 0 | 0 | -Infinity | 9 |  |
| SSB_RP Note3 | 1,2 | dBm/SSB SCS | -94.2 | -94.2 | -Infinity | -85.2 |  |
|  | 3~4 |  | -100.2 | -100.2 | -Infinity | -85.2 |  |
|  | 1~4 | dB | 0 | 0 | -Infinity | 9 |  |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled. The Noc is calculated using -145 dBm/Hz (clause 11.1.3.4.2 in [42])NOTE 3: SSB_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in B.2.1.7, and does not limit UE implementation or test system implementation |  |  |  |  |  |  |  |

##### A.14.5.3.5.3 Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than 1200 ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in clause 10.1.20C.1

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.14.6 Measurement Performance requirements

### A.14.6.1 SS-RSRP for SAN

#### A.14.6.1.1 SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

##### A.14.6.1.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.2C.1.1 and 10.1.2C.1.2 for intra-frequency measurements.

##### A.14.6.1.1.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.14.6.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.14.6.1.1.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.6.1.1.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

Table A.14.6.1.1.2-2: SS-RSRP Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Cell ID |  |  |  | 489 | 0 | 489 | 0 | 489 | 0 |
| SSB ARFCN |  |  |  | freq1 |  | freq1 |  | freq1 |  |
| BWchannel |  | Config 1,2 | MHz | 10: NPRB,c = 52 |  |  |  |  |  |
| BWP BW |  | Config 1,2 |  | 10: NPRB,c = 52 |  |  |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |  |  |
| Satellite information |  | Config 1 |  | SSC.1 | NSC.1 | SSC.1 | NSC.1 | SSC.1 | NSC.1 |
|  |  | Config 2 |  | SSC.2 | NSC.2 | SSC.2 | NSC.2 | SSC.2 | NSC.2 |
| TRS configuration |  | Config 1,2 |  | TRS.1.1 FDD | NA | TRS.1.1 FDD | NA | TRS.1.1 FDD | NA |
| DRX Cycle |  | Config 1,2 | ms | Not Applicable |  |  |  |  |  |
| PDSCH Reference measurement channel |  | Config 1,2 |  | SR.1.1 FDD | - | SR.1.1 FDD | - | SR.1.1 FDD | - |
| RMSI CORESET Reference Channel |  | Config 1,2 |  | CR.1.1 FDD | - | CR.1.1 FDD | - | CR.1.1 FDD | - |
| Control channel RMC |  | Config 1,2 |  | CCR.1.1 FDD | - | CCR.1.1 FDD | - | CCR.1.1 FDD | - |
| SSB configuration |  | Config 1,2 |  | SSB.1 FR1 | SSB.1 FR1 | SSB.1 FR1 | SSB.1 FR1 | SSB.1 FR1 | SSB.1 FR1 |
| Time offset with Cell 1 |  | Config 1,2 | ms | - | 3 | - | 3 | - | 3 |
| SMTC configuration |  | Config 1,2 |  | SMTC.2 |  |  |  |  |  |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 | kHz | 15 kHz |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 | Depending on band group | dBm/15Khz | -106 |  | -88 |  | -114 + ΔBG_offset |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 | Depending on band group | dBm/SCS | -106 |  | -88 |  | -144 + ΔBG_offset |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 2.46 | -5.97 | 2.46 | -5.97 | -0.01 | -4.76 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 6 | 1 | 6 | 1 | 3 | 0 |
| SS-RSRPNote3 | Config 1,2 | Depending on band group | dBm/SCS | -100 | -105 | -82 | -87 | -111.00 + ΔBG_offset | -114.00 + ΔBG_offset |
| IoNote3 | Config 1,2 | Depending on band group | dBm/9.36 MHz | -70.09 |  | -52.09 |  | -80.03 + ΔBG_offset |  |
| Propagation condition |  |  | - | AWGN |  |  |  |  |  |
| Antenna configuration |  |  |  | 1x2 |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: The band group offset, ΔBG_offset , is defined in TS 38.533 [5] Table 3A.4.1A-2. |  |  |  |  |  |  |  |  |  |

##### A.14.6.1.1.3 Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.2C.1.1 and relative requirement in clause 10.1.2C.1.2.

#### A.14.6.1.2 SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

##### A.14.6.1.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.4C.1.1 and 10.1.4C.1.2 for inter-frequency measurements with the testing configurations for NR cells in table A.14.6.1.2.1-1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.14.6.1.2.1-1: Applicable NR configurations for FR1 inter-frequency SS-RSRP accuracy test

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

##### A.14.6.1.2.2 Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.14.6.1.2.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.14.6.1.2.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.14.6.1.2.2-1: SS-RSRP inter-frequency test parameters

| Parameter |  | Config | Unit | Test 1 |  |  | Test 2 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 |  | Cell 2 | Cell 1 |  | Cell 2 |
| SSB ARFCN |  | 1, 2 |  | freq1 |  | freq2 | freq1 |  | freq2 |
| BWchannel |  | 1, 2 | MHz | 10: NPRB,c = 52 |  |  | 10: NPRB,c = 52 |  |  |
| PDSCH Reference measurement channel |  | 1, 2 |  | SR.1.1 FDD |  | - | SR.1.1 FDD |  | - |
| RMSI CORESET Reference Channel |  | 1, 2 |  | CR.1.1 FDD |  | - | CR.1.1 FDD |  | - |
| Dedicated CORESET Reference Channel |  | 1, 2 |  | CCR.1.1 FDD |  | - | CCR.1.1 FDD |  | - |
| SSB configuration |  | 1, 2 |  | SSB.1 FR1 |  |  | SSB.1 FR1 |  |  |
| OCNG Patterns |  | 1, 2 |  | OP.1 |  |  | OP.1 |  |  |
| TRS configuration |  | 1, 2 |  | TRS.1.1 FDD |  | - | TRS.1.1 FDD |  |  |
| Initial BWP Configuration |  | 1, 2 |  | DLBWP.0.1ULBWP.0.1 |  |  | DLBWP.0.1ULBWP.0.1 |  |  |
| Dedicated BWP configuration |  | 1, 2 |  | DLBWP.1.1ULBWP.1.1 |  |  | DLBWP.1.1ULBWP.1.1 |  |  |
| Satellite information |  | 1 |  | SSC.1 | NSC.1 |  | SSC.1 | NSC.1 |  |
|  |  | 2 |  | SSC.2 | NSC.2 |  | SSC.2 | NSC.2 |  |
| Time offset with Cell 1 |  | 1, 2 | ms | - | 3 |  | - | 3 |  |
| SMTC configuration |  | 1, 2 |  | SMTC.2 |  |  | SMTC.2 |  |  |
| EPRE ratio of PSS to SSS |  | 1, 2 | dB | 0 |  | 0 | 0 |  | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |  |  |  |  |
| Note2 | Depending on band group | 1,2 | dBm/15 kHz | -94.65 |  |  | (![](media_svg/image1.svg) [公式≈: ^{N}oc] for Channel 2 +8 dB) |  | -115 + ΔBG_offset |
| Note2 | Depending on band group | 1,2 | dBm/SSB SCS | -94.65 |  |  | (![](media_svg/image1.svg) [公式≈: ^{N}oc] for Channel 2 +8 dB) |  | -115 + ΔBG_offset |
|  |  | 1,2 | dB | 10 |  | 10 | 13 |  | -3 |
| SS-RSRPNote3 | Depending on band group | 1,2 | dBm/SCS | -84.65 |  |  | (RSRP for Cell 2 +25 dB) |  | -118.00 + ΔBG_offset |
| IoNote3 | Depending on band group | 1,2 | dBm/9.36 MHz | -56.28 |  |  | (Io for Channel 2 +19.75 dB) |  | -85.28 + ΔBG_offset |
|  |  | 1,2 | dB | 10 |  | 10 | 13 |  | -3 |
| Propagation condition |  | 1,2 | - | AWGN |  |  | AWGN |  |  |
| Antenna configuration |  | 1,2 |  | 1x2 |  |  | 1x2 |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: The band group offset, ΔBG_offset , is defined in TS 38.533 [5] Table 3A.4.1A-2. |  |  |  |  |  |  |  |  |  |

##### A.14.6.1.2.3 Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil the absolute requirement in clause 10.1.4C.1.1 and relative requirement in clause 10.1.4C.1.2.

#### A.14.6.1.3 SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

##### A.14.6.1.3.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.3C.1.1 and 10.1.3C.1.2 for intra-frequency measurements.

##### A.14.6.1.3.2 Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.14.6.1.3.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in table A.14.6.1.3.2-2 and A.14.6.1.3.2-3. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. The TCI status for Cell 1 is defined in table [TBD] and TRS configuration for Cell 1 is defined in [TBD]. The test consists of two time phases T1 and T2.

Table A.14.6.1.3.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 2 | NGSO, NR FDD, SSB SCS 120 kHz, data SCS 120 kHz, BW 100 MHz |
| 3 | GSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

Table A.14.6.1.3.2-2: SS-RSRP Intra frequency general test parameters

| Parameter | Config | Unit | T1 |  | T2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Cell ID |  |  | 489 | 0 | 489 | 0 |
| SSB ARFCN |  |  | 1 |  | 1 |  |
| BWchannel | 1,2 | MHz | 100: NPRB,c = 66 |  | 100: NPRB,c = 66 |  |
|  | 3,4 |  | 10: NPRB,c = 24 |  | 10: NPRB,c = 24 |  |
| Data PRBs allocated | 1,2,3,4 |  | 24 |  | 24 |  |
| Downlink initial BWP configuration | 1,2,3,4 |  | DLBWP.0.1 | - | DLBWP.0.1 | - |
| Downlink dedicated BWP configuration | 1,2,3,4 |  | DLBWP.1.1 | - | DLBWP.1.1 | - |
| Uplink initial BWP configuration | 1,2,3,4 |  | ULBWP.0.1 | - | ULBWP.0.1 | - |
| Uplink dedicated BWP configuration | 1,2,3,4 |  | ULBWP.1.1 | - | ULBWP.1.1 | - |
| DRX cycle configuration | 1,2,3,4 |  | Not applicable | - | Not applicable | - |
| TRS configuration | 1,2 |  | TBD | - | TBD | - |
|  | 3,4 |  | TRS.1.2 |  | TRS.1.2 |  |
| TCI state |  |  | TBD | - | TBD | - |
| PDSCH Reference measurement channel |  |  | TBD | - | TBD | - |
|  |  |  | SR.2.1 |  | SR.2.1 TDD |  |
| RMSI CORESET Reference Channel |  |  | TBD | - | TBD | - |
|  |  |  | CR.2.1 |  | CR.2.1 FDD |  |
| Dedicated CORESET Reference channel |  |  | TBD | - | TBD | - |
|  |  |  | CCR.4.1 |  | CCR.2.1 TDD |  |
| OCNG Patterns | 1,2,3,4 |  | OP.3 | OP.3 | OP.3 | OP.3 |
| SSB configuration | 1,2 |  | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 | SSB.3 FR2 |
|  | 3,4 |  | SSB.1 | SSB.5 | SSB.1 | SSB.5 |
| SMTC configuration | 1,2,3,4 |  | SMTC.1 | SMTC.1 | SMTC.1 | SMTC.1 |
| Time offset with Cell 1 | 1,2,3,4 | s | - | 3 | - | 3 |
| PDSCH/PDCCH subcarrier spacing | 1,2 | kHz | 120 | 120 | 120 | 120 |
| EPRE ratio of PSS to SSS |  | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH_DMRS to SSS | 1,2,3,4 |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of PDCCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of PDSCH_DMRS to SSS |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH_DMRS |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |  |
| Propagation conditions | 1,2,3,4 |  | AWGN | AWGN | AWGN | AWGN |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |  |  |  |

Table A.14.6.1.3.2-3: SS-RSRP Intra frequency OTA related test parameters

| Parameter | Config | Unit | T1 |  | T2 |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| Satellite Configuration | 1,3 |  | SSC.1 | SSC.1 | NSC.1 | NSC.1 |
|  | 2,4 |  | SSC.2 | SSC.2 | NSC.1 | NSC.2 |
| Angle of arrival configuration |  |  | TBD |  |  |  |
| Assumption for UE beamsNote 3 |  |  | Rough |  | Rough |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 |  | dBm/15 kHzNote2 | -103.2 |  | N/A |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note1 |  | dBm/SCSNote2 | -94.2 |  | N/A |  |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  | dB | 6.0 | 1.0 | N/A | N/A |
| Es |  | dBm/SCSNote2 |  |  | (clause B.2.17 Rx Beam Peak +2.1 dB)NOTE 4 | (clause B.2.17 Rx Beam Peak +2.1 dB)NOTE 4 |
| NOTE 1: Where used, interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled. The Noc is calculated using -145 dBm/Hz (clause 11.1.3.4.2 in [42])NOTE 2: Equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zoneNOTE 3: Information about types of UE beam is given in TBD, and does not limit UE implementation or test system implementationNOTE 4: The actual calculation depends on the actual band and VSAT Type and UE Refsens. |  |  |  |  |  |  |

##### A.14.6.1.3.3 Test Requirements

The SS-RSRP measurement accuracy shall fulfil the absolute accuracy requirements in clauses 10.1.3.1.1 and relative accuracy requirements in clause 10.1.3.1.2. The following requirements are to be verified:

During T1:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.14.6.1.3.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3C.1.2-1.

During T2:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.14.6.1.3.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3C.1.2-1.

During T1 and T2:

Relative accuracy of Cell 1 during T2 compared with Cell 1 during T1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3C.1.2-1.

Relative accuracy of Cell 2 during T2 compared with Cell 2 during T1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table 10.1.3C.1.2-1.

Table A.14.6.1.3.3-1: SS-RSRP absolute accuracy test requirement

|  | Test requirement Notes1,2,3,4 |
| --- | --- |
| Cell 1 | SSB_RP1 -δ +Gmin – NTNmargin/2 ≤ Reported RSRP(dBm) ≤ SSB_RP1 +δ +Gmax + NTNmargin/2 |
| Cell 2 | SSB_RP2 -δ +Gmin - NTNmargin/2 ≤ Reported RSRP(dBm) ≤ SSB_RP2 +δ +Gmax + NTNmargin/2 |
| NOTE 1: SSB_RPn is the  equivalent power received by an antenna with 0 dBi gain at the centre of the quiet zone configured in the test for the cell n under considerationNOTE 2: δ is the RSRP absolute accuracy requirement from Table 10.1.3.1.1-1, selected according to the Io used in the testNOTE 3: Gmin and Gmax are the minimum and maximum UE gain values from table B.2.1.8.1-1, selected according to the UE power classNOTE 4: NTNmargin is the relaxation margin for FR2-NTN and equals 1 dB. |  |

### A.14.6.2 SS-RSRQ

#### A.14.6.2.1 SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access

##### A.14.6.2.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.7C.

##### A.14.6.2.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.14.6.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.14.6.2.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.14.6.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

| Config | Description |
| --- | --- |
| 1 | GSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NGSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

Table A.14.6.2.1.2-2: SS-RSRQ Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |  |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 |  | Cell 2 |  | Cell 1 | Cell 2 |
| SSB ARFCN |  |  |  | freq1 |  | freq1 |  |  |  | freq1 |  |
| Duplex mode |  | Config 1,2 |  | FDD |  |  |  |  |  |  |  |
| BWchannel |  | Config 1,2 | MHz | 10: NPRB,c = 52 |  |  |  |  |  |  |  |
| Gap Pattern ID |  |  |  | 0 |  |  |  |  |  |  |  |
| BWP configuration |  | Initial DL BWP |  | DLBWP.0.1 |  |  |  |  |  |  |  |
|  |  | Dedicated DL BWP |  | DLBWP.1.1 |  |  |  |  |  |  |  |
|  |  | Initial UL BWP |  | ULBWP.0.1 |  |  |  |  |  |  |  |
|  |  | Dedicated UL BWP |  | ULBWP.1.1 |  |  |  |  |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |  |  |  |
| Satellite information |  | Config 1 |  | SSC.1 | NSC.1 | SSC.1 |  | NSC.1 |  | SSC.1 | NSC.1 |
|  |  | Config 2 |  | SSC.2 | NSC.2 | SSC.2 |  | NSC.2 |  | SSC.2 | NSC.2 |
| PDSCH Reference measurement channel |  | Config 1,2 |  | SR.1.1 FDD | - | SR.1.1 FDD |  | - |  | SR.1.1 FDD | - |
| RMSI CORESET Reference Channel |  | Config 1,2 |  | CR.1.1 FDD | - | CR.1.1 FDD |  | - |  | CR.1.1 FDD |  |
| Control Channel RMC |  | Config 1,2 |  | CCR.1.1 FDD | - | CCR.1.1 FDD |  | - |  | CCR.1.1 FDD | - |
| TRS Configuration |  | Config 1,2 |  | TRS.1.1 FDD | - | TRS.1.1 FDD |  | - |  | TRS.1.1 FDD | - |
| OCNG Patterns |  |  |  | OP. 1 |  |  |  |  |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |  |  |  |  |
| Time offset with Cell 1 |  | Config 1,2 | ms | - | 3 | - | 3 |  | - |  | 3 |
| SMTC configuration |  | Config 1,2 |  | SMTC.2 |  |  |  |  |  |  |  |
| SSB configuration |  | Config 1,2 |  | SSB.1 FR1 |  |  |  |  |  |  |  |
| CSI-RS for tracking |  | Config 1,2 |  | TRS.1.1 FDD |  |  |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 | kHz | 15 kHz |  |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 |  | 0 |  | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 | Depending on band group | dBm/15 kHz | -85 |  | -101 |  |  |  | -114 + ΔBG_offset |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 | Depending on band group | dBm/SCS | -85 |  | -101 |  |  |  | -114 + ΔBG_offset |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.76 |  | -4.7 |  |  |  | -5..46 | -5.46 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 3 | 3 | -2.9 |  | -2.9 |  | -4 | -4 |
| SS-RSRPNote3 | Config 1,2 | Depending on band group | dBm/SCS | -82 | -82 | -103.9 |  | -103.9 |  | -118 + ΔBG_offset | -118 + ΔBG_offset |
| SS-RSRQ Note3 |  |  | dB | -14.84 | -14.84 | -14.84 |  | -16.76 |  | -16.76 | -17.34 |
| IoNote3 | Config 1,2 | Depending on band group | dBm/9.36 MHz | -50 |  | -70 |  |  |  | -83.5 + ΔBG_offset |  |
| Propagation condition |  |  | - | AWGN | AWGN | AWGN |  | AWGN |  | AWGN | AWGN |
| Antenna configuration |  |  |  | 1x2 | 1x2 | 1x2 |  | 1x2 |  | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRQ, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRQ, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2.NOTE 6: voidNOTE 7: The band group offset, ΔBG_offset , is defined in TS 38.533 [5] Table 3A.4.1A-2. |  |  |  |  |  |  |  |  |  |  |  |

##### A.14.6.2.1.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.7C.1.1.

#### A.14.6.2.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access

##### A.14.6.2.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.7C.

##### A.14.6.2.2.2 Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.14.6.2.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.14.6.2.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.14.6.2.2.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

| Config | Description |
| --- | --- |
| 1 | GSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| 2 | NGSO, NR 15 kHz SSB SCS, 10 MHz bandwidth, FDD duplex mode |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

Table A.14.6.2.2.2-2: SS-RSRQ Inter frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |  | Test 3 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |  | Cell 1 |  | Cell 2 |
| SSB ARFCN |  |  |  | freq1 | freq2 | freq1 | freq2 |  | freq1 |  | freq2 |
| Duplex mode |  | Config 1,2 |  | FDD |  |  |  |  |  |  |  |
| BWchannel |  | Config 1,2 | MHz | 10: NPRB,c = 52 |  |  |  |  |  |  |  |
| Gap pattern ID |  | Config 1,2 |  | 0 |  |  |  |  |  |  |  |
| BWP BW |  | Config 1,2 |  | 10: NPRB,c = 52 |  |  |  |  |  |  |  |
| DRX Cycle |  |  | ms | Not Applicable |  |  |  |  |  |  |  |
| Satellite information |  | Config 1 |  | SSC.1 | NSC.1 | SSC.1 | NSC.1 |  | SSC.1 |  | NSC.1 |
|  |  | Config 2 |  | SSC.2 | NSC.2 | SSC.2 | NSC.2 |  | SSC.2 |  | NSC.2 |
| PDSCH Reference measurement channel |  | Config 1,2 |  | SR.1.1 FDD | - | SR.1.1 FDD | - |  | SR.1.1 FDD |  | - |
| RMSI CORESET Reference Channel |  | Config 1,2 |  | CR.1.1 FDD | - | R.1.1 FDD | - |  | CR.1.1 FDD |  |  |
| Dedicated CORESET Reference Channel |  | Config 1,2 |  | CCR.1.1 FDD | - | CCR.1.1 FDD | - |  | CCR.1.1 FDD |  | - |
| TRS Configuration |  | Config 1,2 |  | TRS.1.1 FDD | - | TRS.1.1 FDD | - |  | TRS.1.1 FDD |  | - |
| OCNG Patterns |  |  |  | OCNG pattern 1 |  |  |  |  |  |  |  |
| Time offset with Cell 1 |  | Config 1,2 | ms | - | 3 | - | 3 | - |  | 3 |  |
| SMTC configuration |  | Config 1,2 |  | SMTC pattern 2 |  |  |  |  |  |  |  |
| SSB configuration |  | Config 1,2 |  | SSB pattern 1 in FR1 |  |  |  |  |  |  |  |
| CSI-RS for tracking |  | Config 1,2 |  | TRS.1.1 FDD |  |  |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1,2 | kHz | 15 kHz |  |  |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 |  | 0 |  | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 | Depending on band group | dBm/15 kHz | -80.18 |  | -106 |  |  | -116 + ΔBG_offset |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1,2 | Depending on band group | dBm/15 kHz | -80.18 |  | -106 |  |  | -116 + ΔBG_offset |  |  |
| ![](media_svg/image2.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | -1.75 |  | -1.75 |  |  | 3 |  | -1.75 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | -1.75 |  | -1.75 |  |  | 3 |  | -1.75 |
| SS-RSRPNote3 | Config 1,2 | Depending on band group | dBm/SCS | -81.93 | -81.93 | -107.75 | -107.75 |  | -113 + ΔBG_offset |  | -117.75 + ΔBG_offset |
| SS-RSRQNote3 |  |  | dB | -14.77 | -14.77 | -14.76 | -14.76 |  | -12.56 |  | -14.76 |
| IoNote3 | Config 1,2 | Depending on band group | dBm/9.36 MHz | -50 |  | -75.83 |  |  | -83.28 + ΔBG_offset |  | -85.83 + ΔBG_offset |
| Propagation condition |  |  | - | AWGN | AWGN | AWGN | AWGN |  | AWGN |  | AWGN |
| Antenna configuration |  |  |  | 1x2 | 1x2 | 1x2 | 1x2 |  | 1x2 |  | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-RSRQ, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-RSRQ, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2.NOTE 6: The band group offset, ΔBG_offset , is defined in TS 38.533 [5] Table 3A.4.1A-2. |  |  |  |  |  |  |  |  |  |  |  |

##### A.14.6.2.2.3 Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.9C.1.1 and 10.1.9C.1.2.

### A.14.6.3 SS-SINR

#### A.14.6.3.1 SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

##### A.14.6.3.1.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.12C.1.1.

##### A.14.6.3.1.2 Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.14.6.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.14.6.3.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.14.6.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

Table A.14.6.3.1.2-2: SS-SINR Intra frequency test parameters

| Parameter |  |  | Unit | Test 1 |  | Test 2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| SSB ARFCN |  |  |  | freq1 |  | freq1 |  |
| Duplex mode |  | Config 1, 2 |  | FDD |  |  |  |
| Downlink initial BWP configuration |  |  |  | DLBWP.0.1 |  |  |  |
| Downlink dedicated BWP configuration |  |  |  | DLBWP.1.1 |  |  |  |
| Uplink initial BWP configuration |  |  |  | ULBWP.0.1 |  |  |  |
| Uplink dedicated BWP configuration |  |  |  | ULBWP.1.1 |  |  |  |
| DRX Cycle configuration |  |  | ms | Not Applicable |  |  |  |
| Satellite information |  | Config 1 |  | SSC.1 | NSC.1 | SSC.1 | NSC.1 |
|  |  | Config 2 |  | SSC.2 | NSC.2 | SSC.2 | NSC.2 |
| TRS configuration |  | Config 1, 2 |  | TRS.1.1 FDD |  | TRS.1.1 FDD |  |
| PDSCH Reference measurement channel |  | Config 1, 2 |  | SR.1.1 FDD | - | SR.1.1 FDD | - |
| RMSI CORESET Reference Channel |  | Config 1, 2 |  | CR.1.1 FDD | - | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1, 2 |  | CCR.1.1 FDD | - | CCR.1.1 FDD | - |
| OCNG Patterns |  |  |  | OP.1 |  |  |  |
| SS-RSSI-Measurement |  |  |  | Not Applicable |  |  |  |
| SMTC configuration |  | Config 1, 2 |  | SMTC.2 |  |  |  |
| Time offset with Cell 1 |  | Config 1, 2 | ms | - | 3 | - | 3 |
| SSB configuration |  | Config 1, 2 |  | SSB.1 FR1 |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2 | kHz | 15 |  |  |  |
| EPRE ratio of PSS to SSS |  |  | dB | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2 | Depending on band group | dBm/15 kHz | -93 |  | -116 + ΔBG_offset |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2 | Depending on band group | dBm/SCS | -93 |  | Same as Noc for 15 kHz |  |
| ![](media_svg/image7.svg) [公式≈: ^{Ê}s^{I}ot] |  |  | dB | 0 | -3.19 | -5.46 | -5.46 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  | dB | 4.54 | 2.66 | -4 | -4 |
| SS-RSRPNote3 | Config 1, 2 | Depending on band group | dBm/SCS | -88.46 | -90.34 | -120 + ΔBG_offset | -120 + ΔBG_offset |
| SS-SINR Note3 |  |  | dB | 0 | -3.19 | -5.46 | -5.46 |
| IoNote3 | Config 1, 2 | Depending on band group | dBm/9.36 MHz | -57.5 |  | -85.51 + ΔBG_offset |  |
| Propagation condition |  |  | - | AWGN |  |  |  |
| Antenna configuration |  |  | - | 1x2 |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2.NOTE 6: The band group offset, ΔBG_offset , is defined in TS 38.533 [5] Table 3A.4.1A-2. |  |  |  |  |  |  |  |

##### A.14.6.3.1.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.12C.1.1.

#### A.14.6.3.2 SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

##### A.14.6.3.2.1 Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.14C.1.1 and 10.1.14C.1.2.

##### A.14.6.3.2.2 Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.14.6.3.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.14.6.3.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.14.6.3.2.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

Table A.14.6.3.2.2-2: SS-SINR Inter frequency test parameters

| Parameter |  |  |  | Unit | Test 1 |  | Test 2 |  | Test 3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Cell 1 | Cell 2 | Cell 1 | Cell 2 | Cell 1 | Cell 2 |
| SSB ARFCN |  |  |  |  | freq1 | freq2 | freq1 | freq2 | freq1 | freq2 |
| Duplex mode |  | Config 1, 2 |  |  | FDD |  |  |  |  |  |
| Downlink initial BWP configuration |  |  |  |  | DLBWP.0.1 |  |  |  |  |  |
| Downlink dedicated BWP configuration |  |  |  |  | DLBWP.1.1 |  |  |  |  |  |
| Uplink initial BWP configuration |  |  |  |  | ULBWP.0.1 |  |  |  |  |  |
| Uplink dedicated BWP configuration |  |  |  |  | ULBWP.1.1 |  |  |  |  |  |
| DRX Cycle configuration |  |  |  | ms | Not Applicable |  |  |  |  |  |
| Satellite information |  |  | Config 1 |  | SSC.1 | NSC.1 | SSC.1 | NSC.1 | SSC.1 | NSC.1 |
|  |  |  | Config 2 |  | SSC.2 | NSC.2 | SSC.2 | NSC.2 | SSC.2 | NSC.2 |
| Gap pattern ID |  |  |  |  | 0 | - | 0 | - | 0 | - |
| TRS configuration |  | Config 1, 2 |  |  | TRS.1.1 FDD |  | TRS.1.1 FDD |  | TRS.1.1 FDD |  |
| PDSCH Reference measurement channel |  | Config 1, 2 |  |  | SR.1.1 FDD | - | SR.1.1 FDD | - | SR.1.1 FDD | - |
| RMSI CORESET Reference Channel |  | Config 1, 2 |  |  | CR.1.1 FDD | - | CR.1.1 FDD | - | CR.1.1 FDD |  |
| Dedicated CORESET Reference Channel |  | Config 1, 2 |  |  | CCR.1.1 FDD | - | CCR.1.1 FDD | - | CCR.1.1 FDD | - |
| OCNG Patterns |  |  |  |  | OP.1 |  |  |  |  |  |
| SS-RSSI-Measurement |  |  |  |  | Not Applicable |  |  |  |  |  |
| Time offset with Cell 1 |  | Config 1, 2 |  | ms | - | 3 | - | 3 | - | 3 |
| SMTC configuration |  | Config 1, 2 |  |  | SMTC pattern 2 |  |  |  |  |  |
| SSB configuration |  | Config 1, 2 |  |  | SSB.1 FR1 |  |  |  |  |  |
| PDSCH/PDCCH subcarrier spacing |  | Config 1, 2 |  | kHz | 15 |  |  |  |  |  |
| EPRE ratio of PSS to SSS |  |  |  | dB | 0 | 0 | 0 | 0 | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSS(Note 1) |  |  |  |  |  |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS (Note 1) |  |  |  |  |  |  |  |  |  |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2 | Depending on band group |  | dBm/15 kHz | -88 |  | -108.5 |  | -119.5 + ΔBG_offset |  |
| ![](media_svg/image1.svg) [公式≈: ^{N}oc]Note2 | Config 1, 2 | Depending on band group |  | dBm/SCS | -88 |  | -108.5 |  | Same as Noc for 15 kHz |  |
| ![](media_svg/image27.svg) [公式≈: ^{Ê}s^{I}ot] |  |  |  | dB | -1.75 | -1.75 | 20 | 20 | -4.0 | -4.0 |
| ![](media_svg/image3.svg) [公式≈: ^{Ê}s^{N}oc] |  |  |  | dB | -1.75 |  | 20 |  | -4.0 |  |
| SS-RSRP Note3 | Config 1, 2 | Depending on band group |  | dBm/SCS | -89.75 |  | -88.5 |  | -123.5 + ΔBG_offset |  |
| SS-SINRNote3 |  |  |  | dB | -1.75 |  | 20 |  | -4.0 |  |
| IoNote3 | Config 1, 2 | Depending on band group |  | dBm/9.36 MHz | -57.83 |  | -60.5 |  | -90.09 + ΔBG_offset |  |
| Propagation condition |  |  |  | - | AWGN |  |  |  |  |  |
| Antenna configuration |  |  |  | - | 1x2 |  |  |  |  |  |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SS-SINR, SS-RSRP, and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: SS-SINR, SS-RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: NR operating band groups are as defined in clause 3.5.2.NOTE 6: The band group offset, ΔBG_offset , is defined in TS 38.533 [5] Table 3A.4.1A-2. |  |  |  |  |  |  |  |  |  |  |

##### A.14.6.3.2.3 Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.14C.1.1 and 10.1.14C.1.2.

### A.14.6.4 L1-RSRP measurement for beam reporting

#### A.14.6.4.1 SSB based L1-RSRP measurement

##### A.14.6.4.1.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.5C.4 and clause 10.1.19C.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.14.6.4.1.1-1.

Table A.14.6.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

##### A.14.6.4.1.2 Test parameters

In this set of test cases there one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.14.6.4.1.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.14.6.4.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.14.6.4.1.2-1: FR1 SSB based L1-RSRP test parameters

| Parameter |  | Config | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- | --- | --- |
| SSB ARFCN |  | 1, 2 |  | freq1 | freq1 |
| Duplex mode |  | 1, 2 |  | FDD | FDD |
| TDD Configuration |  | 1, 2 |  | N/A | N/A |
| BWchannel |  | 1, 2 | MHz | 10: NPRB,c = 52 | 10: NPRB,c = 52 |
| Satellite information |  | 1 |  | SSC.1 | NSC.1 |
|  |  | 2 |  | SSC.2 | NSC.2 |
| PDSCH Reference measurement channel |  | 1, 2 |  | SR.1.1 FDD | SR.1.1 FDD |
| RMSI CORESET Reference Channel |  | 1, 2 |  | CR.1.1 FDD | CR.1.1 FDD |
| Dedicated CORESET Reference Channel |  | 1, 2 |  | CCR.1.1 FDD | CCR.1.1 FDD |
| SSB configuration |  | 1, 2 |  | SSB.3 FR1 | SSB.3 FR1 |
| OCNG Patterns |  | 1, 2 |  | OP.1 | OP.1 |
| Initial BWP Configuration |  | 1, 2 |  | DLBWP.0.1ULBWP.0.1 | DLBWP.0.1ULBWP.0.1 |
| TRS configuration |  | 1, 2 |  | TRS.1.1 FDD | TRS.1.1 FDD |
| Dedicated BWP configuration |  | 1, 2 |  | DLBWP.1.1ULBWP.1.1 | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration |  | 1, 2 |  | SMTC.1 | SMTC.1 |
| reportConfigType |  | 1, 2 |  | periodic | periodic |
| reportQuantity |  | 1, 2 |  | ssb-Index-RSRP | ssb-Index-RSRP |
| Number of reported RS |  | 1, 2 |  | 2 | 2 |
| L1-RSRP reporting period |  | 1, 2 |  | slot80 | slot80 |
| EPRE ratio of PSS to SSS |  | 1, 2 | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Note2 | Depending on band group | 1, 2 | dBm/15 kHz | -94.65 | -117 + ΔBG_offset |
| Note2 | Depending on band group | 1, 2 | dBm/SSB SCS | -94.65 | -117 + ΔBG_offset |
|  |  | 1, 2 | dB | 10 | -3 |
| SSB RSRP Note3 | Depending on band group | 1, 2 | dBm/SSB SCS | -84.65 | -120 + ΔBG_offset |
| Io Note3 | Depending on band group | 1, 2 | dBm/9.36 MHz | -56.28 | -87.28 + ΔBG_offset |
|  |  | 1, 2 | dB | 10 | -3 |
| Propagation condition |  | 1, 2 |  | AWGN | AWGN |
| Antenna configuration |  | 1, 2 |  | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: The band group offset, ΔBG_offset , is defined in TS 38.533 [5] Table 3A.4.1A-2. |  |  |  |  |  |

##### A.14.6.4.1.3 Test Requirements

The L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 2 shall fulfil the requirements in clauses 10.1.19C.1.

#### A.14.6.4.2 CSI-RS based L1-RSRP measurement on resource set with repetition off

##### A.14.6.4.2.1 Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.5C.4 and clause 10.1.19C.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.14.6.4.2.1-1.

Table A.14.6.4.2.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

| Configuration | Description |
| --- | --- |
| 1 | GSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| 2 | NGSO, NR FDD, SSB SCS 15 kHz, data SCS 15 kHz, BW 10 MHz |
| NOTE: If UE supports both NGSO and GSO, the test case Config 1 can be skipped if the UE passes test case Config 2. |  |

##### A.14.6.4.2.2 Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.14.6.4.2.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.14.6.4.2.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.14.6.4.2.2-1: FR1 CSI-RS based L1-RSRP test parameters

| Parameter |  | Config | Unit | Test 1 | Test 2 |
| --- | --- | --- | --- | --- | --- |
| SSB ARFCN |  | 1, 2 |  | freq1 | freq1 |
| Duplex mode |  | 1, 2 |  | FDD | FDD |
| TDD Configuration |  | 1, 2 |  | N/A | N/A |
| BWchannel |  | 1, 2 | MHz | 10: NPRB,c = 52 | 10: NPRB,c = 52 |
| Satellite information |  | 1 |  | SSC.1 | NSC.1 |
|  |  | 2 |  | SSC.2 | NSC.2 |
| PDSCH Reference measurement channel |  | 1, 2 |  | SR.1.1 FDD | SR.1.1 FDD |
| RMSI CORESET Reference Channel |  | 1, 2 |  | CR.1.1 FDD | CR.1.1 FDD |
| Dedicated CORESET Reference Channel |  | 1, 2 |  | CCR.1.1 FDD | CCR.1.1 FDD |
| SSB configuration |  | 1, 2 |  | SSB.3 FR1 | SSB.3 FR1 |
| OCNG Patterns |  | 1, 2 |  | OP.1 | OP.1 |
| TRS configuration |  | 1, 2 |  | TRS.1.1 FDD | TRS.1.1 FDD |
| Initial BWP Configuration |  | 1, 2 |  | DLBWP.0.1ULBWP.0.1 | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration |  | 1, 2 |  | DLBWP.1.1ULBWP.1.1 | DLBWP.1.1ULBWP.1.1 |
| SMTC configuration |  | 1, 2 |  | SMTC.1 | SMTC.1 |
| CSI-RS |  | 1, 2 |  | CSI-RS 1.2 FDD | CSI-RS 1.2 FDD |
| reportConfigType |  | 1, 2 |  | periodic | periodic |
| reportQuantity |  | 1, 2 |  | cri-RSRP | cri-RSRP |
| Number of reported RS |  | 1, 2 |  | 2 | 2 |
| L1-RSRP reporting period |  | 1, 2 |  | slot80 | slot80 |
| EPRE ratio of PSS to SSS |  | 1, 2 | dB | 0 | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |  |  |
| Note2 | Depending on band group | 1, 2 | dBm/15 kHz | -94.65 | -117 + ΔBG_offset |
| Note2 | Depending on band group | 1, 2 | dBm/CSI-RS SCS | -94.65 | -117 + ΔBG_offset |
|  |  | 1, 2 | dB | 10 | -3 |
| CSI-RS RSRP Note3 | Depending on band group | 1, 2 | dBm/CSI-RS SCS | -84.65 | -120 + ΔBG_offset |
| Io Note3 | Depending on band group | 1, 2 | dBm/9.36 MHz | -56.28 | -87.28 + ΔBG_offset |
|  |  | 1, 2 | dB | 10 | -3 |
| Propagation condition |  | 1, 2 |  | AWGN | AWGN |
| Antenna configuration |  | 1, 2 |  | 1x2 | 1x2 |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for  to be fulfilled.NOTE 3: RSRP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: RSRP minimum requirements are specified assuming independent interference and noise at each receiver antenna port.NOTE 5: The band group offset, ΔBG_offset , is defined in TS 38.533 [5] Table 3A.4.1A-2. |  |  |  |  |  |

##### A.14.6.4.2.3 Test Requirements

The L1-RSRP measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirements in clause 10.1.19C.2.

#### A.14.6.4.3 SSB based L1-RSRP measurement for VSAT UE in FR2-NTN when DRX is not used

##### A.14.6.4.3.1 Test Purpose and Environment

The purpose of this test is to verify that the VSAT UE makes correct reporting of L1-RSRP measurement in FR2-NTN. This test will partly verify the L1-RSRP measurement requirements in clause 9.5C.4.1, with the testing configurations for NR cells in table A.14.6.4.3.1-1.

The AoA setup for this test is [TBD] as defined in [clause TBD].

Table A.14.6.4.3.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test for VSAT UE

| Config | Description |
| --- | --- |
| 1 | NR 120 kHz SSB SCS, 100 MHz bandwidth, FDD duplex mode |
| 2 | NR 240 kHz SSB SCS, 100 MHz bandwidth, FDD duplex mode |
| 3 | GSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| 4 | NGSO, NR FDD, 30 kHz SSB SCS, 10 MHz BW |
| NOTE: If UE supports both NGSO and GSO, the GSO-based test cases can be skipped if the UE passes NGSO-based test cases. |  |

##### A.14.6.4.3.2 Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.14.6.4.3.2-1 and table A.14.6.4.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.14.6.4.3.2-1: General test parameters

| Parameter | Config | Unit | Value |
| --- | --- | --- | --- |
| SSB ARFCN | 1~2 |  | freq1 |
| Duplex mode | 1~2 |  | FDD |
| FDD Configuration | 1~2 |  | TBD |
| BWchannel | 1~2 | MHz | 100: NPRB,c = 66 |
| Data PRBs allocated | 1~4 |  | 66 |
| PDSCH Reference measurement channel | 1,2 |  | TBD |
|  | 3,4 |  | SR.2.1 TDD |
| RMSI CORESET Reference Channel | 1,2 |  | TBD |
|  | 3,4 |  | CC.2.1 TDD |
| Dedicated CORESET Reference Channel | 1,2 |  | TBD |
|  | 3,4 |  | CCR.2.1 TDD |
| SSB configuration | 1,2 |  | SSB.1 FR2 |
|  | 3,4 |  | SSB.1  FR1 |
| OCNG Patterns | 1,2,3,4 |  | OP.1 |
| Initial BWP Configuration | 1,2,3,4 |  | DLBWP.0.1ULBWP.0.1 |
| Dedicated BWP configuration | 1,2,3,4 |  | DLBWP.1.3ULBWP.1.3 |
| SMTC configuration | 1~2 |  | SMTC.1 |
| TRS Configuration | 1~2 |  | TBD |
|  | 3,4 |  | TRS.1.2 |
| PDCCH/PDSCH TCI Configuration | 1~2 |  | TCI.State.2 |
| DRX configuration | 1~2 |  | Off |
| reportConfigType | 1,2,3,4 |  | periodic |
| reportQuantity | 1,2,3,4 |  | ssb-Index-RSRP |
| Number of reported RS | 1,2,3,4 |  | 2 |
| L1-RSRP reporting period | 1,2,3,4 | slot | 320 |
| T1 | 1,2,3,4 | s | 5 |
| T2 | 1,2,3,4 | s | 2 |
| EPRE ratio of PSS to SSS | 1,2,3,4 | dB | 0 |
| EPRE ratio of PBCH DMRS to SSS |  |  |  |
| EPRE ratio of PBCH to PBCH DMRS |  |  |  |
| EPRE ratio of PDCCH DMRS to SSS |  |  |  |
| EPRE ratio of PDCCH to PDCCH DMRS |  |  |  |
| EPRE ratio of PDSCH DMRS to SSS |  |  |  |
| EPRE ratio of PDSCH to PDSCH DMRS |  |  |  |
| EPRE ratio of OCNG DMRS to SSSNote 1 |  |  |  |
| EPRE ratio of OCNG to OCNG DMRS Note 1 |  |  |  |
| Propagation condition | 1,2,3,4 |  | AWGN |
| NOTE 1: OCNG shall be used such that both cells are fully allocated and a constant total transmitted power spectral density is achieved for all OFDM symbols. |  |  |  |

Table A.14.6.4.3.2-2: SSB specific test parameters

| Parameter | Config | Unit | SSB#0 |  | SSB#1 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | T1 | T2 | T1 | T2 |  |
| Angle of arrival configuration |  |  | TBD |  |  |  |  |
| Beam AssumptionNote 4 | 1-2 |  | TBD |  |  |  |  |
| Note2 | 1~2 | dBm/15 kHz | -105 |  |  |  |  |
| Note2 | 1 | dBm/SSB SCS | -96 |  |  |  |  |
|  | 2 |  | -93 |  |  |  |  |
|  | 1~2 | dB | 0 | 0 | -Infinity | 9 |  |
| SSB_RP Note3 | 1 | dBm/SSB SCS | -96 | -96 | -Infinity | -87 |  |
|  | 2 |  | -93 | -93 | -Infinity | -84 |  |
| Io Note3 | 1 | dBm/95.04 MHz | -63.97 | -63.97 | -66.98 | -57.47 |  |
|  | 2 |  | -63.97 | -63.97 | -66.98 | -57.47 |  |
|  | 1~2 | dB | 0 | 0 | -Infinity | 9 |  |
| NOTE 1:  The resources for uplink transmission are assigned to the UE prior to the start of time period T2.NOTE 2: Interference from other cells and noise sources not specified in the test is assumed to be constant over subcarriers and time and shall be modelled as AWGN of appropriate power for ![](media_svg/image1.svg) [公式≈: ^{N}oc] to be fulfilled.NOTE 3: SSB_RP and Io levels have been derived from other parameters for information purposes. They are not settable parameters themselves.NOTE 4: Information about types of UE beam is given in [TBD], and does not limit UE implementation or test system implementation |  |  |  |  |  |  |  |

##### A.14.6.4.3.3 Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than 640 ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in [clause TBD].

The reported L1-RSRP value shall include the Rx antenna gain in the range of table B.2.1.8.1-1.

The rate of correct events observed during repeated tests shall be at least 90 %.
