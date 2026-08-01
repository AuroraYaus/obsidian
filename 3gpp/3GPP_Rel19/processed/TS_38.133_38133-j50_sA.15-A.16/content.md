---
type: spec
aliases:
  - 38.133_38133-j50_sA.15-A.16
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.15-A.16/content.md"
---
# TS 38.133 38133-j50_sA.15-A.16

## A.15NR standalone tests with one or more NR cells in FR2-2

## A.15.1SA: RRC_IDLE state mobility

## A.15.1.1Cell re-selection to NR

## A.15.1.1.1Cell re-selection to FR2-2 intra-frequency NR case

## A.15.1.1.1.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell re-selection requirements specified in clause 4.2.2.3.

## A.15.1.1.1.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.15.1.1.1.2-1, A.15.1.1.1.2-2 and A.15.1.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.15.1.1.1.2-1: Supported test configurations

Table A.15.1.1.1.2-2: General test parameters for intra-frequency NR cell re-selection test case

Table A.15.1.1.1.2-3: Cell specific test parameters for intra-frequency NR cell re-selection test case in AWGN

## A.15.1.1.1.3Test Requirements

The cell re-selection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration updateon Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 386 s.

The cell re-selection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration updateon Cell 1.

The cell re-selection delay to an already detected cell shall be less than 78 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_IntraSee table 4.2.2.3-1 in clause 4.2.2.3

Tevaluate, NR_ intraSee table 4.2.2.3-1 in clause 4.2.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 385.28 s, allow 386 s for the cell re-selection delay to a newly detectable cell and 78.08 s for the cell re-selection delay to an already detected cell in the test case, which we allow 78 s.

## A.15.1.2Cell re-selection to FR2-2 inter-frequency NR case

## A.15.1.2.1Test Purpose and Environment

This test is to verify the requirement for the inter-frequency NR cell re-selection requirements specified in clause 4.2.2.4.

## A.15.1.2.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.15.1.2.2-1, A.15.1.2.2-2 and A.15.1.2.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.15.1.2.2-1: Supported test configurations

Table A.15.1.2.2-2: General test parameters for FR2-2 inter-frequency NR cell re-selection test case

Table A.15.1.2.2-3: Cell specific test parameters for FR2-2 inter-frequency NR cell re-selection test case in AWGN

## A.15.1.2.3Test Requirements

The cell re-selection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration updateon Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 138 s.

The cell re-selection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to a lower priority cell shall be less than 78 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Thigher_priority_searchSee clause 4.2.2.7

Tevaluate, NR_ interSee table 4.2.2.4-1 in clause 4.2.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 138.08 s, allow 138 s for the cell re-selection delay to a higher priority cell and 78.08 s for the cell re-selection delay to a lower priority cell in the test case, which we allow 78 s.

## A.15.1.3Cell re-selection to FR2-2 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion

## A.15.1.3.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell re-selection requirements for UE configured with relaxed measurement criterion specified in clause 4.2.2.9.2.

## A.15.1.3.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.15.1.3.2-1, A.15.1.3.2-2 and A.15.1.3.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. During T1 and T2, only criteria lowMobilityEvalutation is configured and fulfilled, where (SrxlevRef – Srxlev) < SSearchDeltaP. UE has not registered with network for the tracking area containing Cell 2.

Table A.15.1.3.2-1: Supported test configurations

Table A.15.1.3.2-2: General test parameters for FR2-2 intra-frequency NR cell re-selection test case for UE fulfilling low mobility criterion

Table A.15.1.3.2-3: Cell specific test parameters for FR2-2 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling low mobility criterion

## A.15.1.3.3Test Requirements

The cell re-selection delay to an already detected cell for UE fulfilling low mobility relaxed criterion is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected cell shall be less than 232 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to an already detectable cell can be expressed as: Tevaluate, NR_Intra + TSI-NR,

Where:

Tevaluate, NR_IntraSee table 4.2.2.9.2-1 in clause 4.2.2.9,

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 231.68 s, allow 232 s for the cell re-selection delay to an already detected cell for UE fulfilling low mobility criterion in the test case.

## A.15.1.4Cell re-selection to FR2-2 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion

## A.15.1.4.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell re-selection requirements for UE configured with relaxed measurement criterion specified in clause 4.2.2.9.3.

## A.15.1.4.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.15.1.4.2-1, A.15.1.4.2-2 and A.15.1.4.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. During T1 and T2, only criteria cellEdgeEvaluation is configured and fulfilled, where Srxlev> SSearchThresholdP. UE has not registered with network for the tracking area containing Cell 2.

Table A.15.1.4.2-1: Supported test configurations

Table A.15.1.4.2-2: General test parameters for FR2-2 intra-frequency NR cell re-selection test case for UE fulfilling not-at-cell edge criterion

Table A.15.1.4.2-3: Cell specific test parameters for FR2-2 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling not-at-cell edge criterion

## A.15.1.4.3Test Requirements

The cell re-selection delay to an already detected cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 232 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to an already detected cell can be expressed as: Tevaluate, NR_Intra + TSI-NR,

Where:

Tevaluate, NR_IntraSee table 4.2.2.9.3-1 in clause 4.2.2.9,

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 231.68 s, allow 232 s for the cell re-selection delay to an already detected cell for UE fulfilling  not-at-cell edge criterion in the test case.

## A.15.1.5Cell re-selection to FR2-2 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion

## A.15.1.5.1Test Purpose and Environment

This test is to verify the requirement for the inter-frequency NR cell re-selection requirements for UE fulfilling low mobility criterion specified in clause 4.2.2.10.2.

## A.15.1.5.2Test Parameters

The test scenario comprises of 2 cells (Cell 1 and Cell 2) on 2 different NR carriers respectively as given in tables A.15.1.5.2-1, A.15.1.5.2-2 and A.15.1.5.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. Cell 2 is of higher priority than Cell 1. The UE is configured with lowMobilityEvalutation criterion [2].

Table A.15.1.5.2-1: Supported test configurations

Table A.15.1.5.2-2: General test parameters for FR2-2 inter-frequency NR cell re-selection test case for UE fulfilling low mobility criterion

Table A.15.1.5.2-3: Cell specific test parameters for FR2-2 inter-frequency NR cell re-selection test case in AWGN for UE fulfilling low mobility criterion

## A.15.1.5.3Test Requirements

The cell re-selection delay to an already detected low priority cell (Cell 1) for UE fulfilling low mobility criterion is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected low priority cell, Cell 1, shall be less than 232 s.

The cell re-selection delay to an already detected high priority cell (Cell 2) for UE fulfilling low mobility criterion is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected high priority cell, Cell 2, shall be less than 232 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE 1:The cell re-selection delay to an already detected low priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR

NOTE 2:The cell re-selection delay to an already detected higher priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR

Where:

Tevaluate, NR_ interSee table 4.2.2.10.2-1 in clause 4.2.2.10.2

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 231.68 s, allow 232 s for the cell re-selection delay to an already detected low priority cell for UE fulfilling low mobility criterion in the test case.

This gives a total of 231.68 s, allow 232 s for the cell re-selection delay to an already detected high priority cell for UE fulfilling low mobility criterion in the test case.

## A.15.1.6Cell re-selection to FR2-2 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion

## A.15.1.6.1Test Purpose and Environment

This test is to verify the requirement for the inter-frequency NR cell re-selection requirements for UE fulfilling not-at-cell edge criterion specified in clause 4.2.2.10.3.

## A.15.1.6.2Test Parameters

The test scenario comprises of 2 cells (Cell 1 and Cell 2) on 2 different NR carriers respectively as given in tables A.15.1.6.2-1, A.15.1.6.2-2 and A.15.1.6.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. Cell 2 is of higher priority than Cell 1. The UE is configured with cellEdgeEvaluation criterion [2].

Table A.15.1.6.2-1: Supported test configurations

Table A.15.1.6.2-2: General test parameters for FR2-2 inter-frequency NR cell re-selection test case for UE fulfilling not-at-cell edge criterion

Table A.15.1.6.2-3: Cell specific test parameters for FR2-2 inter-frequency NR cell re-selection test case in AWGN for UE fulfilling not-at-cell edge criterion

## A.15.1.6.3Test Requirements

The cell re-selection delay to an already detected low priority cell (Cell 1) for UE fulfilling not-at-cell edge criterion is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected low priority cell, Cell 1, shall be less than 232 s.

The cell re-selection delay to an already detected high priority cell (Cell 2) for UE fulfilling not-at-cell edge criterion is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected high priority cell, Cell 2, shall be less than 232 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE 1:The cell re-selection delay to an already detected low priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR

NOTE 2:The cell re-selection delay to an already detected higher priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR

Where:

Tevaluate, NR_ interSee table 4.2.2.10.3-1 in clause 4.2.2.10.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 231.68 s, allow 232 s for the cell re-selection delay to an already detected low priority cell for UE fulfilling not-at-cell edge criterion in the test case.

This gives a total of 231.68 s, allow 232 s for the cell re-selection delay to an already detected high priority cell for UE fulfilling not-at-cell edge criterion in the test case.

## A.15.2Signaling characteristics

## A.15.2.1SCell Activation and Deactivation Delay

## A.15.2.1.1SCell Activation and deactivation for SCell in FR2-2 intra-band in non-DRX

## A.15.2.1.1.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.6.5.3.1.1 except the PCell and SCell are in FR2-2 intra-band.

The supported test configurations are shown in table A.15.2.1.1.1-1 below. The general test parameters are the same as defined in table A.6.5.3.1.1-2 except those described in tables A.14.X.3.1.1-2, and cell specific test parameters are described in tables A.15.2.1.1.1-3. OTA related test parameters are shown in table A.15.2.1.1.1-4 below.

Table A.15.2.1.1.1-1: Supported test configurations for FR2-2 SCell activation case

Table A.15.2.1.1.1-2: General test parameters for FR2-2 SCell activation case

Table A.15.2.1.1.1-3: Cell specific test parameters for FR2-2 SCell activation case

Table A.15.2.1.1.1-4: OTA related test parameters for FR2-2 SCell activation case

## A.15.2.1.1.2Test Requirements

The test requirements defined in clause A.6.5.3.1.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstSSB + 5 ms as defined in clause 8.3.

## A.15.2.1.2SCell Activation and deactivation for FR1+FR2-2 inter-band with target SCell in FR2-2

## A.15.2.1.2.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.15.2.1.1.1 except the PCell is in FR1 and SCell is in FR2-2.

The supported test configurations are defined in table A.15.2.1.2.1-1. The general test parameters are the same as defined in table A.15.2.1.1.1-2 except that the length of T2 is 2 s. And cell specific test parameters are described in table A.15.2.1.2.1-2. OTA related test parameters are defined in table A.15.2.1.2.1-3.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on NR. During T1 the SCell is powered off and UE is not aware of SCell.

A MAC message for activation of SCell is sent by the test equipment 100 ms after the RRC message, in a slot # denoted m. The point in time at which the MAC message for activation of SCell is received at the UE antenna connector defines the start of time period T2.

During T2, the test equipment monitors the L1-RSRP measurement reporting for the SCell. The time when test equipment receives a valid L1-RSRP report is denoted as slot m+TL1-RSRP. In the next DL slot after slot m+TL1-RSRP, the test equipment sends a MAC message for the activation of the TCI state of the RMC CORESET of the SCell. In the same slot, the test equipment also sends an RRC message to configure the CSI-RS resources for SCell.

Time period T3 starts when a MAC message for deactivation of the SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell and PCell during activation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell 1 deactivation command is sent until CSI reporting for SCell 1 is discontinued.

Table A.15.2.1.2.1-1: Supported test configurations for FR2-2 SCell activation case

Table A.15.2.1.2.1-2: Cell specific test parameters for FR2-2 SCell activation case

Table A.15.2.1.2.1-3: OTA related test parameters for FR1 PCell activation case with FR2-2 SCell

## A.15.2.1.2.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.  Whether CSI report in a slot was interrupted is checked by monitoring ACK/NACK sent in PCell in the slot.

During T2 the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than

## 3 ms + TFirstSSB_MAX + 23*TSMTC_MAX + 12*Trs + TL1-RSRP, measure + TL1-RSRP, report

as defined in clause 8.3.2. For this test case, TFirstSSB_MAX=TSMTC_MAX=Trs=20 ms; TL1-RSRP, measure=240 ms and TL1-RSRP, report=5 ms, which allows TL1-RSRP [980] ms.

During T2 the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

- THARQ is defined in table A.5.5.3.1.1-2

- Tactivation_time = 3 ms + TFirstSSB_MAX + 23*TSMTC_MAX + 12*Trs + TL1-RSRP, measure + TL1-RSRP, report + max {(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)}, which allows [1100] ms

- TCSI_Reporting = 10 ms

- NR slot length is 0.125 ms for this test case.

During T3 the UE shall stop sending CSI reports for both SCells no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

During T2 interruption of PCell during SCell activation shall not happen outside the slot   to , as defined in clause 8.3, where TX =20 ms. m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

The interruption of PCell due to activation of SCell shall not be more than the values specified for SA in clause 8.2.2.2.7.

## A.15.2.1.3SCell Activation and deactivation for SCell in FR2-2 inter-band in non-DRX

## A.15.2.1.3.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.15.2.1.1.1 except the PCell and SCell are in FR2-2 inter-band.

The supported test configurations are shown in table A.15.2.1.3.1-1 below. The general test parameters are described in tables A.15.2.1.3.1-2, and cell specific test parameters are described in tables A.15.2.1.3.1-3. OTA related test parameters are shown in table A.15.2.1.3.1-4 below.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on NR. During T1 the SCell is powered off and UE is not aware of SCell. A MAC message for activation of SCell is sent by the test equipment 100 ms after the RRC message, in a slot # denoted m.

The point in time at which the MAC message for activation of SCell is received at the UE antenna connector defines the start of time period T2. Immediately at beginning of T2 the transmission power of Cell 2 is increased to same level as for Cell 2. During T2, the test equipment monitors the L1-RSRP measurement reporting for the SCell. The time when test equipment receives a valid L1-RSRP report is denoted as slot m+TL1-RSRP. In the next DL slot after slot m+TL1-RSRP, the test equipment sends a MAC message for the activation of the TCI state of the RMC CORESET of the SCell. In the same slot, the test equipment also sends an RRC message to configure the CSI-RS resources for SCell.

Time period T3 starts when a MAC message for deactivation of the SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell and PSCell during activation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell 1 deactivation command is sent until CSI reporting for SCell 1 is discontinued.

Table A.15.2.1.3.1-1: Supported test configurations for FR2-2 SCell activation in FR2-2 inter-band

Table A.15.2.1.3.1-2: General test parameters for FR2-2 SCell activation in FR2-2 inter-band

Table A.15.2.1.3.1-3: Cell specific test parameters for FR2-2 SCell activation in FR2-2 inter-band

Table A.15.2.1.3.1-4: OTA related test parameters for FR2-2 SCell activation in FR2-2 inter-band

## A.15.2.1.3.2Test Requirements

During T2 the UE shall start sending CSI report for the SCell in the configured slots for CSI reporting after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k). UE shall send the first CSI report for SCell after receiving at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k), or in the next available uplink resource for CSI reporting if the slot was subject to interruption. Whether CSI report in a slot was interrupted is checked by monitoring ACK/NACK sent in PCell in the slot.

During T2, the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than 3 ms + TFirstSSB_MAX + 23*TSMTC_MAX +12*Trs + TL1-RSRP, measure + TL1-RSRP, report as defined in clause 8.3.2. For this test case, TFirstSSB_MAX=TSMTC_MAX=Trs=20 ms; TL1-RSRP, measure=480 ms and TL1-RSRP, report=5 ms, which allows TL1-RSRP =1480 ms.

During T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

-THARQ is defined in table A.14.X.3.3.1-2

-Tactivation_time = 3 ms + TFirstSSB_MAX + 23*TSMTC_MAX + 12*Trs + TL1-RSRP, measure + TL1-RSRP, report + max {(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)}, which allows 1510 ms

-TCSI_Reporting = 10 ms

-NR slot length is 0.125 ms for this test case.

During T2, the interruption of PCell during SCell activation shall not happen outside the slot   to , where TX =20 ms. m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length

During T3, the UE shall stop sending CSI reports for SCell no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

During T3, the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to  as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

## A.15.2.1.4Direct SCell activation at SCell addition of known SCell in FR2-2

## A.15.2.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the delay and interruption for direct SCell activation delay at SCell addition are within the requirements stated in clause 8.3.4.

The supported test configurations are shown in table A.15.2.1.4.1-1 below. The general test parameters are given in table A.15.2.1.4.1-2 and cell-specific test parameters in table A.15.2.1.4.1-3. OTA related test parameters are shown in table A.15.2.1.4.1-4.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two FR2-2 carriers and two NR cells. Before the test starts the UE is connected to Cell 1 (PCell) on carrier #1, but is not aware of Cell 2 on NR carrier #2. Cell 1 and Cell 2 have constant signal levels throughout the test. The UE is monitoring the PCell. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the Cell 2 is monitored by the UE. During T1, Cell 2 should be detected and measured by the UE such that it meets the condition for known cell defined in clause 8.3.4 for direct SCell activation.

Time period T2 starts when the RRCReconfiguration message for the configuration and activation of Cell 2 (the SCell), which is sent from the test equipment, is received at the UE antenna connector in a slot # denoted m. The test equipment shall set the parameter sCellState to activated for the SCell, which causes Cell 2 to become configured and activated.

Time period T3 starts at (m + Ndirect), at which point UE shall be reporting a valid CQI for both PCell and SCell.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during the activation of SCell. The test equipment verifies the activation time by counting the slots from the time when the SCell activation message is sent until a CQI report with other than CQI index 0 is received.

Table A.15.2.1.4.1-1: Supported test configurations

Table A.15.2.1.4.1-2: General test parameters

Table A.15.2.1.4.1-3: Cell specific test parameters

Table A.15.2.1.4.1-4: OTA related test parameters

## A.15.2.1.4.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after slot (m+k). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.  Whether CSI report in a slot was interrupted is checked by monitoring ACK/NACK sent in PCell in the slot.

During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot  , wherem+NdirectNR slot length

Ndirect = TRRC_Process + T1 + Tactivation_time + TCSI_Reporting - 3 ms,

- TRRC_Process = 16 ms, which is the RRC procedure delay defined for SCell addition in clause 12 of TS 38.331 [2],

- T1 is the delay from slot m + TRRC_Process until the transmission of RRCReconfigurationComplete message,

- Tactivation_time = TFirstSSB+ 5 ms = 25 ms,

- TCSI_Reporting = 10 ms

This gives a total of Ndirect = 16 + T1 + 25 + 10 - 3 = (48 + T1) ms, and NR slot length is 0.125 ms.

During T3 the UE shall send CSI reports for SCell with non-zero CQI index and continue to send CSI reports for SCell  with non-zero CQI index until the end of T3.

During T2 interruption of PSCell during SCell activation shall not happen outside the window from slot m+1 to slot  m+1+ as defined in clause 8.3.4, where TX =20 ms. TRRC_Process+T1+TXNR slot length

The interruption of PCell due to activation of SCell shall not be more than the values specified for NR SA in clause 8.2.2.2.11.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3.4 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.m+NdirectNR slot length

## A.15.2.1.5Direct SCell activation at handover with known SCell in FR2-2

## A.15.2.1.5.1Test Purpose and Environment

This test is to verify the requirements specified in sub clause 8.3.5 for the FR2-2 handover with direct SCell activation.

The test scenario comprises of three FR2-2 cells, one source PCell (Cell 1), one target PCell (Cell 2) and one SCell (Cell 3). The test consists of three successive time periods, with time durations of T1, T2, and T3 respectively.

At the start of time duration T1, the UE is in connected mode with PCell (Cell 1). Both Cell 2 and Cell 3 are known to UE and UE is reporting CQI for all Cell 1.

Time period T2 starts when UE receives a handover command that initiate handover of UE to Cell 2 and also activates Cell 3. This is done using an RRCConnectionReconfiguration message with parameter sCellState set to activated for the Cell 3. The message is sent from the test equipment to the UE and is received in a slot number n at the UE antenna connector. The UE shall accomplish the handover, addition and activation of the SCell no later than slot (n +). NdirectNR slot length

Time period T3 starts at (n +), at which point UE shall be reporting a valid CSI for both Cell 2 and Cell 3 as given in tables A.15.2.1.5.1-1 and A.15.2.1.5.1-2.NdirectNR slot length

Table A.15.2.1.5.1-1: Supported test configurations for FR2-2 handover with direct SCell activation case

Table A.15.2.1.5.1-2: General test parameters for FR2-2 handover with direct SCell activation case

Table A.15.2.1.5.1-3: Cell specific test parameters for FR2-2 SCell activation case

Table A.15.2.1.5.1-4: OTA related test parameters for FR2-2 SCell activation case

## A.15.2.1.5.2Test Requirements

The UE shall be capable to transmit valid CSI report for PCell (Cell 2) and to the directly activated SCell 1 no later than in slot n+ Ndirect.

The SCell activation delay, Ndirect, can be expressed as: Ndirect = TRRC_process + Tinterrupt + T2 + T3 + Tactivation_time + TCSI_Reporting - 3 ms; Where:

-TRRC_Process: RRC procedure delay defined in clause 12 of TS 38.331 and it is equal to 16 ms,

-Tinterrupt: Interruption time during handover as specified in clause 6.1.1. The value to be verified in the test is 52 ms (Tinterrupt = 0 ms for Tsearch + 10 ms for TIU + 20 ms for Tprocessing + 20 ms for T∆ + 2 ms for Tmargin ms) by assuming known SCell and SMTC.1 configuration.

-T2: Delay from slot  until UE has obtained a valid TA command for the target PCell,n+TRRC_Process+TinterruptNR slot length

-T3: Delay for applying the received TA for uplink transmission in the target PCell, and greater than or equal to k+1 slot, where k is defined in clause 4.2 in TS 38.213,

-Tactivation_time and TCSI_Reporting are specified in clause 8.3.2, where the following definitions of TFirstSSB and TFirstSSB_MAX as defined in clause 8.3.5 shall apply:

During time period T2 of the test, the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , Tactivation_time = TSMTC_SCell + 5 ms, as defined in clause 8.3.n+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

During time period T3 of the test, the UE shall stop sending CSI reports for SCell at latest in a slot , as defined in clause 8.3.m+THARQ+3 msNR slot length

During time period T2 of the test, interruption of PCell / PSCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

During time period T3 of the test, the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During time period T2 of the test, if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.15.3RRC_CONNECTED state mobility

## A.15.3.1Handover

## A.15.3.1.1Intra-frequency handover from FR2-2 carrier with CCA to FR2-2 carrier with CCA; unknown target cell

## A.15.3.1.1.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-2-NR FR2-2 intra-frequency handover on carrier with CCA requirements specified in clause 6.1.1.4.

## A.15.3.1.1.2Test Parameters

Supported test configurations are shown in table A.15.3.1.1.2-1. Both handover delay and interruption length are tested by using the parameters in tables A.15.3.1.1.2-2, and A.15.3.1.1.2-3.

The test scenario comprises of 1 carrier and two cells on the carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.15.3.1.1.2-1: Intra-frequency handover from FR2-2 carrier with CCA to FR2-2 carrier with CCA test configurations

Table A.15.3.1.1.2-2: General test parameters for Intra-frequency handover from FR2-2 carrier with CCA to FR2-2 carrier with CCA

Table A.15.3.1.1.2-3: Cell specific test parameters for Intra-frequency handover from FR2-2 carrier with CCA to FR2-2 carrier with CCA

## A.15.3.1.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than RRC procedure delay + Tinterrupt from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt is defined in clause 6.1B.1.3.2.

## A.15.3.1.2Inter-frequency handover from FR1 to FR2-2 carrier with CCA; unknown target cell

## A.15.3.1.2.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR2-2 inter frequency handover on carrier with CCA requirements specified in clause 6.1.1.4.

## A.15.3.1.2.2Test Parameters

Supported test configurations are shown in table A.15.3.1.2.2-1. Both handover delay and interruption length are tested by using the parameters in table A.15.3.1.2.2-2, and A.15.3.1.2.2-3.

The test scenario comprises of 2 carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.15.3.1.2.2-1: Inter-frequency handover from FR1 to FR2-2 carrier with CCA test configurations

Table A.15.3.1.2.2-2: General test parameters Inter-frequency handover from FR1 to FR2-2 carrier with CCA

Table A.15.3.1.2.2-3: Cell specific test parameters for NR FR1-FR2-2 carrier with CCA Inter frequency handover test case

## A.15.3.1.2.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than RRC procedure delay + Tinterrupt from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt is defined in clause 6.1B.1.4.2.

## A.15.4Measurement procedure

## A.15.4.1Intra-frequency Measurements

## A.15.4.1.1SA event triggered reporting test without gap under non-DRX for FR2-2 with CCA

## A.15.4.1.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2A.5.1 and 9.2A.5.2. Supported test configurations are shown in table A.15.4.1.1.1-1.

Table A.15.4.1.1.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2-2 neighbour cell (Cell 2) on the same frequency as the PCell with CCA transmitting SSBs according to DL CCA model. The test parameters for the Cell 1 and Cell 2 are given in table A.15.4.1.1.1-2, A.15.4.1.1.1-3 and A.15.4.1.1.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.15.4.1.1.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 without gap without DRX

Table A.15.4.1.1.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 without gap without DRX

Table A.15.4.1.1.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2-2 without gap without DRX

Figure A.15.4.1.1.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.15.4.1.1.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

For Configuration 1，

-TBD for a UE supporting power class 1,

-TBD for a UE supporting power class 2 and 3

For Configuration 2，

-TBD for a UE supporting power class 1,

-TBD for a UE supporting power class 2 and 3

For Configuration 3，

-TBD for a UE supporting power class 1,

-TBD for a UE supporting power class 2 and 3

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.15.4.2Inter-frequency Measurements

## A.15.4.2.1SA event triggered reporting tests for FR2-2 with CCA without SSB time index detection when DRX is not used (PCell in FR2-2)

## A.15.4.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4.

In this test, there are two cells: NR Cell 1 as PCell in FR2-2 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR2-2 on NR RF channel 2 with CCA transmitting SSBs according to DL CCA model. The test parameters and configurations are given in tables A.15.4.2.1.1-1, A.15.4.2.1.1-2, and A.15.4.2.1.1-3.

Measurement gap pattern configuration # 13 as defined in table A.15.4.2.1.1-2 is provided for UE that does not support per-FR gap and for UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Supported test configurations are shown in table A.15.4.2.1.1-1.

Table A.15.4.2.1.1-1 SA event triggered reporting tests without SSB index reading for FR2-FR2

Table A.15.4.2.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2-2 without SSB time index detection

Table A.15.4.2.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2-2 without SSB time index detection

## A.15.4.2.1.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

For Configuration 1,

TBD for UE supporting power class 1, or

TBD for UE supporting other power class.

For Configuration 2,

TBD for UE supporting power class 1, or

TBD for UE supporting other power class.

For Configuration 3,

TBD for UE supporting power class 1, or

TBD for UE supporting other power class.

The UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16NR standalone tests with all NR cells in FR1 for RedCap

## A.16.1SA: RRC_IDLE state mobility for RedCap

## A.16.1.1Cell re-selection to NR

## A.16.1.1.1Cell re-selection to FR1 intra-frequency NR case for 1 Rx UE

## A.16.1.1.1.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequencyintra-frequency NR cell re-selection requirements specified in clause 4.2B.2.3.

## A.16.1.1.1.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.16.1.1.1.2-1, A.16.1.1.1.2-2 and A.16.1.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.16.1.1.1.2-1: Supported test configurations

Table A.16.1.1.1.2-2: General test parameters for intra-frequencyintra-frequency NR cell re-selection test case for 1 Rx UE

Table A.16.1.1.1.2-3: Cell specific test parameters for intra-frequency NR cell re-selection test case in AWGN for 1 Rx UE

## A.16.1.1.1.3Test Requirements

The cell re-selection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell re-selection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 8 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,NR_Intra_RedCap + TSI-NR, and to an already detected cell can be expressed as: Tevaluate,NR_Intra_RedCap + TSI-NR,

Where:

Tdetect,NR_Intra_RedCapSee table 4.2B.2.3-1 in clause 4.2B.2.3

Tevaluate,NR_Intra_RedCapSee table 4.2B.2.3-1 in clause 4.2B.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 7.68 s for the cell re-selection delay to an already detected cell in the test case, which we allow 8 s.

## A.16.1.1.2Cell re-selection to FR1 intra-frequency NR case for 2 Rx UE

## A.16.1.1.2.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell re-selection requirements specified in clause 4.2B.2.3.

## A.16.1.1.2.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.16.1.1.2.2-1, A.16.1.1.2.2-2 and A.16.1.1.2.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.16.1.1.2.2-1: Supported test configurations

Table A.16.1.1.2.2-2: General test parameters for intra-frequency NR cell re-selection test case for 2 Rx UE

Table A.16.1.1.2.2-3: Cell specific test parameters for intra-frequency NR cell re-selection test case in AWGN for 2 Rx UE

## A.16.1.1.2.3Test Requirements

The cell re-selection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell re-selection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 8 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_IntraSee table 4.2.2.3-1 in clause 4.2.2.3

Tevaluate, NR_ intraSee table 4.2.2.3-1 in clause 4.2.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 7.68 s for the cell re-selection delay to an already detected cell in the test case, which we allow 8 s.

## A.16.1.1.3Cell re-selection to FR1 inter-frequency NR case for 1 Rx UE

## A.16.1.1.3.1Test Purpose and Environment

This test is to verify the requirement for the inter-frequency NR cell re-selection requirements specified in clause 4.2B.2.4.

## A.16.1.1.3.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.16.1.1.3.2-1, A.16.1.1.3.2-2 and A.16.1.1.3.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

Table A.16.1.1.3.2-1: Supported test configurations

Table A.16.1.1.3.2-2: General test parameters for FR1 inter-frequency NR cell re-selection test case for 1 Rx UE

Table A.16.1.1.3.2-3: Cell specific test parameters for FR1 inter-frequency NR cell re-selection test case in AWGN for 1 Rx UE

## A.16.1.1.3.3Test Requirements

The cell re-selection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps again on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The cell re-selection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to a lower priority cell shall be less than 8 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate,NR_Inter_RedCap + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate,NR_Inter_RedCap + TSI-NR,

Where:

Thigher_priority_searchSee clause 4.2B.2.7

Tevaluate,NR_Inter_RedCapSee table 4.2B.2.4-1 in clause 4.2B.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority cell and 7.68 s for the cell re-selection delay to a lower priority cell in the test case, which we allow 8 s.

## A.16.1.1.4Cell re-selection to FR1 inter-frequency NR case for 2 Rx UE

## A.16.1.1.4.1Test Purpose and Environment

This test is to verify the requirement for the inter-frequency NR cell re-selection requirements specified in clause 4.2B.2.4.

## A.16.1.1.4.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.16.1.1.4.2-1, A.16.1.1.4.2-2 and A.16.1.1.4.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

Table A.16.1.1.4.2-1: Supported test configurations

Table A.16.1.1.4.2-2: General test parameters for FR1 inter-frequency NR cell re-selection test case for 2 Rx UE

Table A.16.1.1.4.2-3: Cell specific test parameters for FR1 inter-frequency NR cell re-selection test case in AWGN for 2 Rx UE

## A.16.1.1.4.3Test Requirements

The cell re-selection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps again on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The cell re-selection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to a lower priority cell shall be less than 8 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate,NR_Inter_RedCap + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate,NR_Inter_RedCap + TSI-NR,

Where:

Thigher_priority_searchSee clause 4.2B.2.7

Tevaluate,NR_Inter_RedCapSee table 4.2B.2.4-1 in clause 4.2B.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority cell and 7.68 s for the cell re-selection delay to a lower priority cell in the test case, which we allow 8 s.

## A.16.1.1.5Cell re-selection to FR1 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE

## A.16.1.1.5.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell re-selection requirements for UE fulfilling stationary relaxed measurement criterion specified in clause 4.2B.2.9.2.

## A.16.1.1.5.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.16.1.1.5.2-1, A.16.1.1.5.2-2 and A.16.1.1.5.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.16.1.1.5.2-1: Supported test configurations

Table A.16.1.1.5.2-2: General test parameters for FR1 intra-frequency NR cell re-selection test case for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE

Table A.16.1.1.5.2-3: Cell specific test parameters for FR1 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE

## A.16.1.1.5.3Test Requirements

The cell re-selection delay to an already detected cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected cell shall be less than 32 s.

The cell re-selection delay to an already detected cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 32 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to an already detected cell can be expressed as: Tevaluate,NR_Intra_RedCap_Relax + TSI-NR,

Where:

Tevaluate,NR_Intra_RedCap_RelaxSee table 4.2B.2.9.2-1 in clause 4.2B.2.9.2 for re-selection to Cell 2 during T1 with UE fulfilling stationary criterion, 30.72 s.

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 32 s for the cell re-selection delay to an already detected cell for UE fulfilling stationary criterion in the test case.

## A.16.1.1.6Cell re-selection to FR1 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE

## A.16.1.1.6.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell re-selection requirements for UE fulfilling stationary relaxed measurement criterion specified in clause 4.2B.2.9.2.

## A.16.1.1.6.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.16.1.1.6.2-1, A.16.1.1.6.2-2 and A.16.1.1.6.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.16.1.1.6.2-1: Supported test configurations

Table A.16.1.1.6.2-2: General test parameters for FR1 intra-frequency NR cell re-selection test case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE

Table A.16.1.1.6.2-3: Cell specific test parameters for FR1 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE

## A.16.1.1.6.3Test Requirements

The cell re-selection delay to an already detected cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected cell shall be less than 32 s.

The cell re-selection delay to an already detected cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 32 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to an already detected cell can be expressed as: Tevaluate,NR_Intra_RedCap_Relax + TSI-NR,

Where:

Tevaluate,NR_Intra_RedCap_RelaxSee table 4.2B.2.9.2-2 in clause 4.2B.2.9.2 for re-selection to Cell 2 during T1 with UE fulfilling stationary criterion, 30.72 s.

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 32 s for the cell re-selection delay to an already detected cell for UE fulfilling stationary criterion in the test case.

## A.16.1.1.7Cell re-selection to FR1 inter-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE

## A.16.1.1.7.1Test Purpose and Environment

This test is to verify the requirement for the inter-frequency NR cell re-selection requirements specified in clause 4.2B.2.10.2, for UE fulfilling stationary relaxed measurement criterion.

## A.16.1.1.7.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.16.1.1.7.2-1, A.16.1.1.7.2-2 and A.16.1.1.7.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

As specified in the Test Purpose, the UE is configured with the stationary relaxed measurement criterion for UE defined in clause 5.2.4.9.1 in [1]. So, Cell 2 and Cell 1 configure the UE as follows:

-stationaryMobilityEvaluation [2] criterion is configured according to the parameters listed in table A.16.1.1.7.2-3;

-cellEdgeEvaluationWhileStationary [2] criterion is not configured;

-combineRelaxedMeasCondition2 [2] is not configured;

Table A.16.1.1.7.2-1: Supported test configurations

Table A.16.1.1.7.2-2: General test parameters for FR1 inter-frequency NR cell re-selection test case for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE

Table A.16.1.1.7.2-3: Cell specific test parameters for FR1 inter-frequency NR cell re-selection test case in AWGN for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE

## A.16.1.1.7.3Test Requirements

The cell re-selection delay to an already detected lower priority cell for UE fulfilling stationary relaxed measurements is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to a lower priority cell for UE fulfilling stationary relaxed measurements shall be less than 32 s.

The cell re-selection delay to an already detected higher priority cell for UE fulfilling stationary relaxed measurements is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected higher priority cell for UE fulfilling stationary relaxed measurements shall be less than 32 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a known lower priority cell can be expressed as: Tevaluate,NR_Inter_RedCap_Relax + TSI-NR,

Where:

Tevaluate,NR_Inter_RedCap_RelaxSee table 4.2B.2.10.2-1 in clause 4.2B.2.10.2

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 32 s for the cell re-selection delay to an already detected lower priority cell and 32 s for the cell re-selection delay to an already detected higher priority cell, for UE fulfilling stationary relaxed measurements in the test case.

## A.16.1.1.8Cell re-selection to FR1 inter-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE

## A.16.1.1.8.1Test Purpose and Environment

This test is to verify the requirement for the inter-frequency NR cell re-selection requirements specified in clause 4.2B.2.10.2, for UE fulfilling stationary relaxed measurement criterion.

## A.16.1.1.8.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.16.1.1.8.2-1, A.16.1.1.8.2-2 and A.16.1.1.8.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

As specified in the Test Purpose, the UE is configured with the stationary relaxed measurement criterion for UE defined in clause 5.2.4.9.1 in [1]. So, Cell 2 and Cell 1 configure the UE as follows:

-stationaryMobilityEvaluation [2] criterion is configured according to the parameters listed in table A.16.1.1.8.2-3;

-cellEdgeEvaluationWhileStationary [2] criterion is not configured;

-combineRelaxedMeasCondition2 [2] is not configured;

Table A.16.1.1.8.2-1: Supported test configurations

Table A.16.1.1.8.2-2: General test parameters for FR1 inter-frequency NR cell re-selection test case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE

Table A.16.1.1.8.2-3: Cell specific test parameters for FR1 inter-frequency NR cell re-selection test case in AWGN for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE

## A.16.1.1.8.3Test Requirements

The cell re-selection delay to an already detected lower priority cell for UE fulfilling stationary relaxed measurements is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to a lower priority cell for UE fulfilling stationary relaxed measurements shall be less than 32 s.

The cell re-selection delay to an already detected higher priority cell for UE fulfilling stationary relaxed measurements is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected higher priority cell for UE fulfilling stationary relaxed measurements shall be less than 32 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a known lower priority cell can be expressed as: Tevaluate,NR_Inter_RedCap_Relax + TSI-NR,

Where:

Tevaluate,NR_Inter_RedCap_RelaxSee table 4.2B.2.10.2-2 in clause 4.2B.2.10.2

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 32 s for the cell re-selection delay to an already detected lower priority cell and 32 s for the cell re-selection delay to an already detected higher priority cell, for UE fulfilling stationary relaxed measurements in the test case.

## A.16.1.2Inter-RAT E-UTRAN cell re-selection for RedCap

## A.16.1.2.1Cell re-selection to higher priority E-UTRAN for 1 RX

## A.16.1.2.1.1Test Purpose and Environment

This test is to verify the requirement for the NR to E-UTRAN inter-RAT cell re-selection requirements specified in clause 4.2B.2.5 when the E-UTRAN cell is of higher priority.

## A.16.1.2.1.2Test Parameters

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A.16.1.2.1.2-1, A.16.1.2.1.2-2, A.16.1.2.1.2-3 and A.16.1.2.1.2-4. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. NR Cell 1 is already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of higher priority than Cell 1.

Table A.16.1.2.1.2-1: Supported test configurations

Table A.16.1.2.1.2-2: General test parameters for NR to E-UTRAN cell re-selection test case

Table A.16.1.2.1.2-3: Cell specific test parameters for NR Cell 1

Table A.16.1.2.1.2-4: Cell specific test parameters for E-UTRA Cell 2

## A.16.1.2.1.3Test Requirements

The cell re-selection delay to a higher priority E-UTRAN cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search_RedCap + Tevaluate, E-UTRAN_RedCap + TSI-E-UTRA,

Where:

Thigher_priority_search_RedCapSee clause 4.2B.2.7

Tevaluate, E-UTRAN_RedCap See table 4.2B.2.5-1 in clause 4.2B.2.5

TSI-E-UTRA_Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority E-UTRAN cell.

## A.16.1.2.2Cell re-selection to higher priority E-UTRAN for 2 RX

## A.16.1.2.2.1Test Purpose and Environment

This test is to verify the requirement for the NR to E-UTRAN inter-RAT cell re-selection requirements specified in clause 4.2.2.5 when the E-UTRAN cell is of higher priority.

## A.16.1.2.2.2Test Parameters

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A.16.1.2.2.2-1, A. 16.1.2.2.2-2, A. 16.1.2.2.2-3 and A. 16.1.2.2.2-4. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. NR Cell 1 is already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of higher priority than Cell 1.

Table A.16.1.2.2.2-1: Supported test configurations

Table A. 16.1.2.2.2-2: General test parameters for NR to E-UTRAN cell re-selection test case

Table A. 16.1.2.2.2-3: Cell specific test parameters for NR Cell 1

Table A. 16.1.2.2.2-4: Cell specific test parameters for E-UTRA Cell 2

## A.16.1.2.2.3Test Requirements

The cell re-selection delay to a higher priority E-UTRAN cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search_RedCap + Tevaluate, E-UTRAN_RedCap + TSI-E-UTRA,

Where:

Thigher_priority_search_RedCapSee clause 4.2B.2.7

Tevaluate, E-UTRAN_RedCap See table 4.2B.2.5-1 in clause 4.2B.2.5

TSI-E-UTRA_Maximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority E-UTRAN cell.

A.16.1.2.3Cell re-selection to lower priority E-UTRAN for 1 RX

## A.16.1.2.3.1Test Purpose and Environment

This test is to verify the requirement for the NR to E-UTRAN inter-RAT cell re-selection requirements specified in clause 4.2B.2.5 when the E-UTRAN cell is of lower priority.

## A. 16.1.2.3.2Test Parameters

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A16.1.2.3.2-1, A16.1.2.3.2-2, A16.1.2.3.2-3 and A16.1.2.3.2-4. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both NR Cell 1 and E-UTRAN Cell 2 are already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of lower priority than Cell 1.

Table A.16.1.2.3.2-1: Supported test configurations

Table A.16.1.2.3.2-2: General test parameters for NR to E-UTRAN cell re-selection test case

Table A. 16.1.2.3.2-3: Cell specific test parameters for NR Cell 1

Table A.16.1.2.3.2-4: Cell specific test parameters for E-UTRA Cell 2

## A.16.1.2.3.3Test Requirements

The cell re-selection delay to a lower priority E-UTRAN cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a lower priority cell shall be less than 8 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, E-UTRAN + TSI-E-UTRA,

Where:

Thigher_priority_search_RedCapSee clause 4.2B.2.7

Tevaluate, E-UTRAN_RedCap See table 4.2B.2.5-1 in clause 4.2B.2.5

TSI-E-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 7.68 s, allow 8 s for the cell re-selection delay to a lower priority E-UTRAN cell.

A.16.1.2.4Cell re-selection to lower priority E-UTRAN for 2 RX

## A.16.1.2.4.1Test Purpose and Environment

This test is to verify the requirement for the NR to E-UTRAN inter-RAT cell re-selection requirements specified in clause 4.2B.2.5 when the E-UTRAN cell is of lower priority.

## A.16.1.2.4.2Test Parameters

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A16.1.2.4.2-1, A16.1.2.4.2-2, A16.1.2.4.2-3 and A16.1.2.4.2-4. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both NR Cell 1 and E-UTRAN Cell 2 are already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of lower priority than Cell 1.

Table A.16.1.2.4.2-1: Supported test configurations

Table A. 16.1.2.4.2-2: General test parameters for NR to E-UTRAN cell re-selection test case

Table A. 16.1.2.4.2-3: Cell specific test parameters for NR Cell 1

Table A. 16.1.2.4.2-4: Cell specific test parameters for E-UTRA Cell 2

## A.16.1.3.1.3Test Requirements

The cell re-selection delay to a lower priority E-UTRAN cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a lower priority cell shall be less than 8 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, E-UTRAN + TSI-E-UTRA,

Where:

Thigher_priority_search_RedCapSee clause 4.2B.2.7

Tevaluate, E-UTRAN_RedCap See table 4.2B.2.5-1 in clause 4.2B.2.5

TSI-E-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 7.68 s, allow 8 s for the cell re-selection delay to a lower priority E-UTRAN cell.

## A.16.1.2.5Cell re-selection to lower priority E-UTRAN for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE

## A.16.1.2.5.1Test Purpose and Environment

This test is to verify the requirement for the NR to E-UTRAN inter-RAT cell re-selection when UE fulfills the stationary relaxed measurement criterion specified in clause 4.2B.2.11.2 and the E-UTRAN cell is of lower priority.

## A.16.1.2.5.2Test Parameters

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A.16.1.2.5.2-1, A.16.1.2.5.2-2, A.16.1.2.5.2-3 and A.16.1.2.5.2-4. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both NR Cell 1 and E-UTRAN Cell 2 are already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of lower priority than Cell 1.

As specified in the Test Purpose, the UE is configured with the stationary relaxed measurement criterion defined in clause 5.2.4.9.1 in [1]. So, Cell 1 configures the UE as follows:

-stationaryMobilityEvaluation [2] criterion is configured according to the parameters listed in table A.16.1.1.8.2-3;

-cellEdgeEvaluationWhileStationary [2] criterion is not configured;

-combineRelaxedMeasCondition2 [2] is not configured;

Table A.16.1.2.5.2-1: Supported test configurations

Table A.16.1.2.5.2-2: General test parameters for NR to E-UTRAN cell re-selection test case for UE fulfilling stationary criterion for 1 Rx UE

Table A.16.1.2.5.2-3: Cell specific test parameters for NR Cell 1 for 1 Rx UE

Table A.16.1.2.5.2-4: Cell specific test parameters for E-UTRA Cell 2 for 1 Rx UE

## A.16.1.2.5.3Test Requirements

The cell re-selection delay to a lower priority E-UTRAN cell with UE fulfilling stationary relaxed measurement criterion is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCConnectionRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a lower priority cell shall be less than 32 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate,EUTRAN_Relax + TSI-E-UTRA,

Where:

Tevaluate,EUTRAN_RelaxSee table 4.2B.2.11.2-1 in clause 4.2B.2.11.2

TSI-E-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 30.72 (Tevaluate,EUTRAN_Relax) + 1.28 (TSI-E-UTRA) = 32 s for the cell re-selection delay to a lower priority E-UTRAN cell for stationary relaxed measurement criterion.

## A.16.1.2.6Cell re-selection to lower priority E-UTRAN for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE

## A.16.1.2.6.1Test Purpose and Environment

This test is to verify the requirement for the NR to E-UTRAN inter-RAT cell re-selection when UE fulfills the stationary relaxed measurement criterion specified in clause 4.2B.2.11.2 and the E-UTRAN cell is of lower priority.

## A.16.1.2.6.2Test Parameters

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A.16.1.2.6.2-1, A.16.1.2.6.2-2, A.16.1.2.6.2-3 and A.16.1.2.6.2-4. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both NR Cell 1 and E-UTRAN Cell 2 are already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of lower priority than Cell 1.

As specified in the Test Purpose, the UE is configured with the stationary relaxed measurement criterion defined in clause 5.2.4.9.1 in [1]. So, Cell 1 configures the UE as follows:

-stationaryMobilityEvaluation [2] criterion is configured according to the parameters listed in table A.16.1.1.8.2-3;

-cellEdgeEvaluationWhileStationary [2] criterion is not configured;

-combineRelaxedMeasCondition2 [2] is not configured;

Table A.16.1.2.6.2-1: Supported test configurations

Table A.16.1.2.6.2-2: General test parameters for NR to E-UTRAN cell re-selection test case for UE fulfilling stationary criterion for 2 Rx UE

Table A.16.1.2.6.2-3: Cell specific test parameters for NR Cell 1 for 2 Rx UE

Table A.16.1.2.6.2-4: Cell specific test parameters for E-UTRA Cell 2 for 2 Rx UE

## A.16.1.2.6.3Test Requirements

The cell re-selection delay to a lower priority E-UTRAN cell with UE fulfilling stationary relaxed measurement criterion is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCConnectionRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a lower priority cell shall be less than 32 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate,EUTRAN_Relax + TSI-E-UTRA,

Where:

Tevaluate,EUTRAN_RelaxSee table 4.2B.2.11.2-1 in clause 4.2B.2.11.2

TSI-E-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 30.72 (Tevaluate,EUTRAN_Relax) + 1.28 (TSI-E-UTRA) = 32 s for the cell re-selection delay to a lower priority E-UTRAN cell for stationary relaxed measurement criterion.

## A.16.2SA: RRC_INACTIVE state mobility for RedCap

## A.16.2.1Configured Grant based Small Data Transmissions (CG-SDT) for RedCap

## A.16.2.1.1NR UE CG-SDT Test in FR1 for 1 Rx RedCap UE

## A.16.2.1.1.1Test purpose and Environment

The purpose of this test is to verify that the UE properly perform TA validation for CG-SDT transmission in clause 5.2B.3. The test includes two sub-tests, Sub-test#1 for testing valid TA where UE can initiate CG-SDT transmission, and Sub-test#2 for testing invalid TA where UE does not initiate CG-SDT transmission. Subtest#2 is only tested if Sub-test#1 is passed. For each sub-test, UE is configured with CG-SDT configurations when entering RRC Inactive state. Sub-test#1 consists of four successive time periods, with time duration of T1, T2, T3 and T4 respectively. Sub-test#2 consists of two successive time periods, with time duration of T5 and T6 respectively. There is one cell, which is the active NR cell in FR1. Figure A.16.2.1.1.1-1 shows the variation of the RSRP over the duration of Sub-test#1 and Figure A.16.2.1.1.1-2 shows the variation of the RSRP over the duration of Sub-test#2.

In Sub-test#1:

-Prior to the time point TA, the UE shall be fully synchronized to PCell (Cell 1), be registered to the cell and have entered RRC connected mode.

-Before starting the test at time point TA, test equipment configures RSRP to P0.

-At time point TB, RSRP is changed from P0 to P1.

-At time point TC, which is W1 after time point TB, UE expect to receive RRC release with CG-SDT configuration and RRC status is changed to INACTIVE status.

-At time point TD, RSRP is changed from P1 to P0.

-At time point TE, RSRP is changed from P0 to P2. TE must be W2 before TF.

-Test equipment triggers UL data arrival at UE lower layer at time point TF. After time point TF, test equipment observes whether UE transmits with CG-SDT no later than TG which is W3 after TF.

-After time point TG, RRC status is changed from RRC INACTIVE to RRC CONNECTED.

In Sub-test#2:

-Prior to the time point TA, the UE shall pass Sub-test#1 and have entered RRC connected mode. Otherwise, Sub-test#2 shall not be executed.

-From time point TA to time point TD, RSRP is set to P2.

-At time point TC, which is W1 after time point TB, UE expect to receive RRC release with CG SDT configuration and RRC status is changed to INACTIVE status.

-At time point TD, RSRP is changed from P2 to P0.

-Test equipment triggers UL data arrival at UE lower layer at time point TF. TF is 3360 ms after TD. After time point TF, test equipment observes whether UE transmits with CG-SDT no later than TG which is W3 after TF.

W1 equals to 640 ms and W2 equals to 640 ms based on requirements in clause 5.2B.2.1. W3 is 860 ms.

Figure A.16.2.1.1.1-1: RSRP variation model for CG-SDT Sub-test#1

Figure A.16.2.1.1.1-2: RSRP variation model for CG-SDT Sub-test#2

## A.16.2.1.1.2Test Parameters

Supported test configurations are shown in table A.16.2.1.1.2-1. The test parameters for the PCell are given in table A.16.2.1.1.2-2 and table A.16.2.1.1.2-3.

Table A.16.2.1.1.2-1: NR configuration for FR1 SSB

Table A.16.2.1.1.2-2: General test parameters

Table A.16.2.1.1.2-3: SSB specific test parameters

## A.16.2.1.1.3Test requirements

The UE behaviour in each test during time durations shall be as follows:

During Sub-test#1, UE shall transmit PUSCH at CG-SDT resource within 860 ms after time point TF.

During Sub-test#2, after passing Sub-test#1, UE shall not transmit PUSCH at CG-SDT resources after TF until the end of the test at time point TG.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.2.1.2NR UE CG-SDT Test in FR1 for 2 Rx RedCap UE

## A.16.2.1.2.1Test purpose and Environment

The purpose of this test is to verify that the UE properly perform TA validation for CG-SDT transmission in clause 5.2B.3. The test includes two sub-tests, Sub-test#1 for testing valid TA where UE can initiat CG-SDT transmission, and Sub-test#2 for testing invalid TA where UE does not initiate CG-SDT transmission. Subtest#2 is only tested if Sub-test#1 is passed. For each sub-test, UE is configured with CG-SDT configurations when entering RRC Inactive state. Sub-test#1 consists of four successive time periods, with time duration of T1, T2, T3 and T4 respectively. Sub-test#2 consists of two successive time periods, with time duration of T5 and T6 respectively. There is one cell, which is the active NR cell in FR1. Figure A.16.2.1.2.1-1 shows the variation of the RSRP over the duration of Sub-test#1 and Figure A.16.2.1.2.1-2 shows the variation of the RSRP over the duration of Sub-test#2.

In Sub-test#1:

-Prior to the time point TA, the UE shall be fully synchronized to PCell (Cell 1), be registered to the cell and have entered RRC connected mode.

-Before starting the test at time point TA, test equipment configures RSRP to P0.

-At time point TB, RSRP is changed from P0 to P1.

-At time point TC which is W1 after time point TB, UE expect to receive RRC release with CG-SDT configuration and RRC status is changed to INACTIVE status.

-At time point TD, RSRP is changed from P1 to P0.

-At time point TE, RSRP is changed from P0 to P2. TE must be W2 before TF.

Test equipment triggers UL data arrival at UE lower layer at time point TF. After time point TF, test equipment observes whether UE transmits with CG-SDT no later than TG which is W3 after TF.

-After time point TG, RRC status is changed from RRC INACTIVE to RRC CONNECTED.

In Sub-test#2:

-Prior to the time point TA, the UE shall pass Sub-test#1 and have entered RRC connected mode. Otherwise, Sub-test#2 shall not be executed.

-From time point TA to time point TD, RSRP is set to P2.

-At time point TC, which is W1 after time point TB, UE expect to receive RRC release with CG SDT configuration and RRC status is changed to INACTIVE status.

-At time point TD, RSRP is changed from P2 to P0.

-Test equipment triggers UL data arrival at UE lower layer at time point TF. TF is 3360 ms after TD. After time point TF, test equipment observes whether UE transmits with CG-SDT no later than TG which is W3 after TF.

W1 equals to 640 ms and W2 equals to 640 ms based on requirements in clause 5.2B.2.1. W3 is 860 ms.

Figure A.16.2.1.2.1-1: RSRP variation model for CG-SDT Sub-test#1

Figure A.16.2.1.2.1-2: RSRP variation model for CG-SDT Sub-test#2

## A.16.2.1.2.2Test Parameters

Supported test configurations are shown in table A.16.2.1.2.2-1. The test parameters for the PCell are given in table A.16.2.1.2.2-2 and table A.16.2.1.2.2-3.

Table A.16.2.1.2.2-1: NR configuration for FR1 SSB

Table A.16.2.1.2.2-2: General test parameters

Table A.16.2.1.2.2-3: SSB specific test parameters

## A.16.2.1.2.3Test requirements

The UE behaviour in each test during time durations shall be as follows:

During Sub-test#1, UE shall transmit PUSCH at CG-SDT resource within 860 ms after time point TF.

During Sub-test#2, after passing Sub-test#1, UE shall not transmit PUSCH at CG-SDT resources after TF until the end of the test at time point TG.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.2.2Cell Reselection for Positioning

## A.16.2.2.1Cell re-selection to FR1 intra-frequency NR case with RRC_INACTIVE eDRX and positioning SRS

## A.16.2.2.1.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell re-selection requirements specified in clause 5.6A.2.2, when a RedCap UE is in RRC_INACTIVE and configured with eDRX and to transmit SRS for positioning.

## A.16.2.2.1.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.16.2.2.1.2-1, A.16.2.2.1.2-2 and A.16.2.2.1.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. UE is configured with transmit SRS for positioning in Cell 1.

Table A.16.2.2.1.2-1: Supported test configurations

Table A.16.2.2.1.2-2: General test parameters for intra-frequency NR cell re-selection test case

Table A.16.2.2.1.2-3: Cell specific test parameters for intra-frequency NR cell re-selection test case in AWGN

## A.16.2.2.1.3Test Requirements

The cell re-selection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2 and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 119 s.

The rate of correct cell re-selections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra + TSI-NR,

where:

Tdetect, NR_IntraSee table 5.6.1A.2-1 in clause 5.6.1A.2,

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280ms is assumed in this test case.

This gives a total of 119.04 s, allow 120 s for the cell re-selection delay to a newly detectable cell.

## A.16.3RRC_CONNECTED state mobility for RedCap

## A.16.3.1Handover

## A.16.3.1.1Intra-frequency handover from FR1 to FR1; known target cell for 1 Rx UE

## A.16.3.1.1.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-frequency handover requirements for 1 Rx RedCap UE as specified in clause 6.1D.1.2.

## A.16.3.1.1.2Test Parameters

Supported test configurations are shown in table A.16.3.1.1.2-1. Both handover delay and interruption length are tested by using the parameters in table A.16.3.1.1.2-2, and A.16.3.1.1.2-3.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

NR shall send an RRC message implying handover to Cell 2, then UE handover to Cell 2’s initial BWP associated with CD-SSB. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.16.3.1.1.2-1: Intra-frequency handover from FR1 to FR1 test configurations

Table A.16.3.1.1.2-2: General test parameters Intra-frequency handover from FR1 to FR1

Table A.16.3.1.1.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency handover test case

## A.16.3.1.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 62 ms in the test. Tinterrupt is defined in clause 6.1D.1.2.

This gives a total of 72 ms.

## A.16.3.1.2Intra-frequency handover from FR1 to FR1; known target cell for 2 Rx UE

## A.16.3.1.2.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-frequency handover requirements for 2 Rx RedCap UE as specified in clause 6.1D.1.2.

## A.16.3.1.2.2Test Parameters

Supported test configurations are shown in table A.16.3.1.2.2-1. Both handover delay and interruption length are tested by using the parameters in table A.16.3.1.2.2-2, and A.16.3.1.2.2-3.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

NR shall send an RRC message implying handover to Cell 2, then UE handover to Cell 2’s initial BWP associated with CD-SSB. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.16.3.1.2.2-1: Intra-frequency handover from FR1 to FR1 test configurations

Table A.16.3.1.2.2-2: General test parameters Intra-frequency handover from FR1 to FR1

Table A.16.3.1.2.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency handover test case

## A.16.3.1.2.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 62 ms in the test. Tinterrupt is defined in clause 6.1D.1.2.

This gives a total of 72 ms.

## A.16.3.1.3Intra-frequency handover from FR1 to FR1; unknown target cell for 1 Rx UE

## A.16.3.1.3.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-frequency handover requirements for 1 Rx RedCap UE as specified in clause 6.1D.1.2.

## A.16.3.1.3.2Test Parameters

Supported test configurations are shown in table A.16.3.1.3.2-1. Both handover delay and interruption length are tested by using the parameters in table A.16.3.1.3.2-2, and A.16.3.1.3.2-3.

Before the test starts,

-UE is connected to Cell 1 with active DL BWP and active UL BWP;

-UE is configured with nonCellDefiningSSB-r17 under BWP-DownlinkDedicated which serves as the reference SSB for the serving cell. The nonCellDefiningSSB-r17 corresponds to the NCD-SSB within the active DL BWP.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network indicating the UE to handover to Cell 2 with firstActiveDownlinkBWP-Id configured to DL BWP and firstActiveUplinkBWP-Id configured to UL BWP. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.16.3.1.3.2-1: Intra-frequency handover from FR1 to FR1 test configurations

Table A.16.3.1.3.2-2: General test parameters Intra-frequency handover from FR1 to FR1

Table A.16.3.1.3.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency handover test case

## A.16.3.1.3.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 292 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 282 ms in the test. Tinterrupt is defined in clause 6.1.1.2.2 and Tsearch defined in caluse 6.1D.1.2.

This gives a total of 292 ms.

## A.16.3.1.4Intra-frequency handover from FR1 to FR1; unknown target cell for 2 Rx UE

## A.16.3.1.4.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-frequency handover requirements for 2 Rx RedCap UE as specified in clause 6.1D.1.2.

## A.16.3.1.4.2Test Parameters

Supported test configurations are shown in table A.16.3.1.4.2-1. Both handover delay and interruption length are tested by using the parameters in table A.16.3.1.4.2-2, and A.16.3.1.4.2-3.

Before the test starts,

-UE is connected to Cell 1 with active DL BWP and active UL BWP

-UE is configured with nonCellDefiningSSB-r17 under BWP-DownlinkDedicated which serves as the reference SSB for the serving cell. The nonCellDefiningSSB-r17 corresponds to the NCD-SSB within the active DL BWP.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network indicating the UE to handover to Cell 2 with firstActiveDownlinkBWP-Id configured to DL BWP and firstActiveUplinkBWP-Id configured to UL BWP. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.16.3.1.4.2-1: Intra-frequency handover from FR1 to FR1 test configurations

Table A.16.3.1.4.2-2: General test parameters Intra-frequency handover from FR1 to FR1

Table A.16.3.1.4.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency handover test case

The UE shall start to transmit the PRACH to Cell 2 less than 212 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 202 ms in the test. Tinterrupt is defined in clause 6.1.1.2.2 and Tsearch defined in caluse 6.1D.1.2.

This gives a total of 212 ms.

## A.16.3.1.5Inter-frequency handover from FR1 to FR1; unknown target cell for 1 Rx UE

## A.16.3.1.5.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 inter-frequency handover requirements for 1 Rx RedCap UE as specified in clause 6.1D.1.2.

## A.16.3.1.5.2Test Parameters

Supported test configurations are shown in table A.16.3.1.5.2-1. Both handover delay and interruption length are tested by using the parameters in table A.16.3.1.5.2-2, and A.16.3.1.5.2-3.

Before the test starts,

-UE is connected to Cell 1 with active DL BWP and active UL BWP;

-UE is not configured with nonCellDefiningSSB-r17 under BWP-DownlinkDedicated, and CD-SSB serves as the reference SSB for the serving cell.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network indicating the UE to handover to Cell 2 with firstActiveDownlinkBWP-Id configured to DL BWP and firstActiveUplinkBWP-Id configured to UL BWP, where Cell 2’s DL BWP is the Redcap specific BWP associated with NCD-SSB. The UE then performs handover from Cell 1’s active DL BWP associated with the CD-SSB to Cell 2’s Redcap specific BWP associated with NCD-SSB. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.16.3.1.5.2-1: Inter-frequency handover from FR1 to FR1 test configurations

Table A.16.3.1.5.2-2: General test parameters Inter-frequency handover from FR1 to FR1

Table A.16.3.1.5.2-3: Cell specific test parameters for NR FR1-FR1 inter-frequency handover test case

## A.16.3.1.5.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 532 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 522 ms in the test. Tinterrupt is defined in clause 6.1D.1.2.

This gives a total of 532 ms.

## A.16.3.1.6Inter-frequency handover from FR1 to FR1; unknown target cell for 2 Rx UE

## A.16.3.1.6.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 inter-frequency handover requirements for 2 Rx RedCap UE as specified in clause 6.1D.1.2.

## A.16.3.1.6.2Test Parameters

Supported test configurations are shown in table A.16.3.1.6.2-1. Both handover delay and interruption length are tested by using the parameters in table A.16.3.1.6.2-2, and A.16.3.1.6.2-3.

Before the test starts,

-UE is connected to Cell 1 with active DL BWP and active UL BWP;

-UE is not configured with nonCellDefiningSSB-r17 under BWP-DownlinkDedicated, and CD-SSB serves as the reference SSB for the serving cell.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network indicating the UE to handover to Cell 2 with firstActiveDownlinkBWP-Id configured to DL BWP and firstActiveUplinkBWP-Id configured to UL BWP, where Cell 2’s DL BWP is the Redcap specific BWP associated with NCD-SSB. The UE then performs handover from Cell 1’s active DL-BWP associated with the CD-SSB to Cell 2’s Redcap specific BWP associated with NCD-SSB. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.16.3.1.6.2-1: Inter-frequency handover from FR1 to FR1 test configurations

Table A.16.3.1.6.2-2: General test parameters Inter-frequency handover from FR1 to FR1

Table A.16.3.1.6.2-3: Cell specific test parameters for NR FR1-FR1 Inter frequency handover test case

## A.16.3.1.6.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 372 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 362 ms in the test. Tinterrupt is defined in clause 6.1D.1.2.

This gives a total of 372 ms.

## A.16.3.1.7SA NR - E-UTRAN handover for 1 Rx UE

## A.16.3.1.7.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE can make correct inter-RAT E-UTRAN handover when operating in standalone (SA) operation with PCell in FR1. This test shall verify the NR to E-UTRAN handover requirements as specified in clause 6.1D.2.1.

The test comprises of one NR carrier and one E-UTRA carrier. There are two cells and one cell on each carrier. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in table 9.1.2-1 is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2 after the UE has reported Event B2. The start of T3 is the next instant after the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.16.3.1.7.1-1. General test parameters are provided in table A.16.3.1.7.1-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.16.3.1.7.1-3 and A.16.3.1.7.1-4 respectively.

Table A.16.3.1.7.1-1: Supported test configurations for SA inter-RAT E-UTRAN handover tests

Table A.16.3.1.7.1-2: General test parameters for SA inter-RAT E-UTRAN handover

Table A.16.3.1.7.1-3: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 1)

Table A.16.3.1.7.1-4: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 2)

## A.16.3.1.7.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 85 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and Tinterrupt = 35 ms in the test based on requirements specified in clause 6.1D.2.1.

This gives a total of 85 ms.

## A.16.3.1.8SA NR - E-UTRAN handover for 2 Rx UE

## A.16.3.1.8.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE can make correct inter-RAT E-UTRAN handover when operating in standalone (SA) operation with PCell in FR1. This test shall verify the NR to E-UTRAN handover requirements as specified in clause 6.1D.2.1.

The test comprises of one NR carrier and one E-UTRA carrier. There are two cells and one cell on each carrier. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in table 9.1.2-1 is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2 after the UE has reported Event B2. The start of T3 is the next instant after the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.16.3.1.8.1-1. General test parameters are provided in table A.16.3.1.8.1-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.16.3.1.8.1-3 and A.16.3.1.8.1-4 respectively.

Table A.16.3.1.8.1-1: Supported test configurations for SA inter-RAT E-UTRAN handover tests

Table A.16.3.1.8.1-2: General test parameters for SA inter-RAT E-UTRAN handover

Table A.16.3.1.8.1-3: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 1)

Table A.16.3.1.8.1-4: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 2)

## A.16.3.1.8.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 85 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and is specified in clause 6.1.2.1.

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 6.1.2.1.

This gives a total of 85 ms.

## A.16.3.1.9SA NR - E-UTRAN handover with unknown target cell for 1 Rx UE

## A.16.3.1.9.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE can make correct inter-RAT E-UTRAN handover when operating in standalone (SA) operation with PCell in FR1. This test shall verify the NR to E-UTRAN handover requirements for the case when the target E-UTRAN cell is unknown as specified in clause 6.1D.2.1.

The test comprises of one NR carrier and one E-UTRA carrier. There are two cells and one cell on each carrier. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable. No Gap pattern shall be configured.

A RRC message implying handover shall be sent to the UE during period T1. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.16.3.1.9-1. General test parameters are provided in table A.16.3.1.9.1-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.16.3.1.9.1-3 and A.16.3.1.9.1-4 respectively.

Table A.16.3.1.9.1-1: Supported test configurations for SA inter-RAT E-UTRAN handover tests

Table A.16.3.1.9.1-2: General test parameters for SA inter-RAT E-UTRAN handover

Table A.16.3.1.9.1-3: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 1)

Table A.16.3.1.9.1-4: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 2)

## A.16.3.1.9.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 165 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and Tinterrupt = 115 ms in the test based on requirements specified in clause 6.1D.2.1.

This gives a total of 165 ms.

## A.16.3.1.10SA NR - E-UTRAN handover with unknown target cell for 2 Rx UE

## A.16.3.1.10.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE can make correct inter-RAT E-UTRAN handover when operating in standalone (SA) operation with PCell in FR1. This test shall verify the NR to E-UTRAN handover requirements for the case when the target E-UTRAN cell is unknown as specified in clause 6.1D.2.1.

The test comprises of one NR carrier and one E-UTRA carrier. There are two cells and one cell on each carrier. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable. No Gap pattern shall be configured.

A RRC message implying handover shall be sent to the UE during period T1. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.16.3.1.10.1-1. General test parameters are provided in table A.16.3.1.10.12. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.16.3.1.10.1-3 and A.16.3.1.10.1-4 respectively.

Table A.16.3.1.10.1-1: Supported test configurations for SA inter-RAT E-UTRAN handover tests

Table A.16.3.1.10.1-2: General test parameters for SA inter-RAT E-UTRAN handover

Table A.16.3.1.10.1-3: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 1)

Table A.16.3.1.10.1-4: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 2)

## A.16.3.1.10.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 165 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and is specified in clause 6.1.2.1.

Tinterrupt = 115 ms in the test; Tinterrupt is defined in clause 6.1.2.1.

This gives a total of 165 ms.

## A.16.3.2RRC Connection Mobility Control

## A.16.3.2.1SA: RRC Re-establishment

## A.16.3.2.1.1Intra-frequency RRC Re-establishment in FR1 for 1 Rx UE

A.16.3.2.1.1.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR1 with known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1B.

The test parameters are given in table A.16.3.2.1.1.1-1, table A.16.3.2.1.1.1-2 and table A.16.3.2.1.1.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.16.3.2.1.1.1-1: Supported test configurations

Table A.16.3.2.1.1.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR1 for 1 Rx UE

Table A.16.3.2.1.1.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR1 for 1 Rx UE

A.16.3.2.1.1.2Test Requirements

The RRC re-establishment delay is defined as the time from the moment UE declares RLF, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to a known NR intra-frequency cell shall be less than 1.6 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 1

Tidentify_intra_NR = 200 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1545 ms for RRC re-establishment delay, allow 440 ms + 1.6 s from the beginning of T2 in the test case.

## A.16.3.2.1.2Intra-frequency RRC Re-establishment in FR1 for 2 Rx UE

A.16.3.2.1.2.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR1 with known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1B.

The test parameters are given in table A.16.3.2.1.2.1-1, table A.16.3.2.1.2.1-2 and table A.16.3.2.1.2.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.16.3.2.1.2.1-1: Supported test configurations

Table A.16.3.2.1.2.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR1

Table A.16.3.2.1.2.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR1

A.16.3.2.1.2.2 Test Requirements

The RRC re-establishment delay is defined as the time from the moment UE declares RLF, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to a known NR intra-frequency cell shall be less than 1.6 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 1

Tidentify_intra_NR = 200 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1545 ms for RRC re-establishment delay, allow 240 ms + 1.6 s from the beginning of T2 in the  test case.

## A.16.3.2.1.3Inter-frequency RRC Re-establishment in FR1 for 1 Rx UE

A.16.3.2.1.3.1Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR1 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1B.

The test parameters are given in table A.16.3.2.1.3.1-1, table A.16.3.2.1.3.1-2 and table A.16.3.2.1.3.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

Table A.16.3.2.1.3.1-1: Supported test configurations

Table A.16.3.2.1.3.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1 for 1 Rx UE

Table A.16.3.2.1.3.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1

A.16.3.2.1.3.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter-frequency cell shall be less than 3 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 2

Tidentify_intra_NR = 800 ms

Tidentify_inter_NR = 800 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 2945 ms, allow 3 s in the test case.

## A.16.3.2.1.4Inter-frequency RRC Re-establishment in FR1 for 2 Rx UE

A.16.3.2.1.4.1Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR1 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1B.

The test parameters are given in table A.16.3.2.1.4.1-1, table A.16.3.2.1.4.1-2 and table A.16.3.2.1.4.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

Table A.16.3.2.1.4.1-1: Supported test configurations

Table A.16.3.2.1.4.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1 for 2 Rx UE

Table A.16.3.2.1.4.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1 for 2 Rx UE

A.16.3.2.1.4.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter-frequency cell shall be less than 3 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 2

Tidentify_intra_NR = 800 ms

Tidentify_inter_NR = 800 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 2945 ms, allow 3 s in the test case.

## A.16.3.2.1.5Intra-frequency RRC Re-establishment in FR1 for 1 Rx UE without serving cell timing

A.16.3.2.1.5.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR1 without serving cell timing is within the specified limits. These tests will verify the requirements in clause 6.2.1B.

The test parameters are given in table A.16.3.2.1.5.1-1, table A.16.3.2.1.5.1-2 and table A.16.3.2.1.5.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.16.3.2.1.5.1-1: Supported test configurations

Table A.16.3.2.1.5.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR1

Table A.16.3.2.1.5.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR1

A.16.3.2.1.5.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR intra-frequency cell without serving cell timing shall be less than 2.2 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 1

Tidentify_intra_NR = 800 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 [2] for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 2145 ms, allow 2.2 s in the test case.

## A.16.3.2.1.6Intra-frequency RRC Re-establishment in FR1 for 2 Rx UE without serving cell timing

A.16.3.2.1.6.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR1 without serving cell timing is within the specified limits. These tests will verify the requirements in clause 6.2.1B.

The test parameters are given in table A.16.3.2.1.6.1-1, table A.16.3.2.1.6.1-2 and table A.16.3.2.1.6.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.16.3.2.1.6.1-1: Supported test configurations

Table A.16.3.2.1.6.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR1

Table A.16.3.2.1.6.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR1

A.16.3.2.1.6.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR intra-frequency cell without serving cell timing shall be less than 2.2 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 1

Tidentify_intra_NR = 800 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 [2] for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 2145 ms, allow 2.2 s in the test case.

## A.16.3.2.2Random Access

## A.16.3.2.2.14-step RA type contention based random access test in FR1 for NR standalone for 1 Rx UE

A.16.3.2.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2B.2 and clause 7.1A.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.16.3.2.2.1.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.16.3.2.2.1.1-2.

Table A.16.3.2.2.1.1-1: Supported test configurations for contention based random access test in FR1 for NR standalone

Table A.16.3.2.2.1.1-2: General test parameters for contention based random access test in FR1 for NR Standalone

A.16.3.2.2.1.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.16.3.2.2.1.2.1Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2.2.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB+1 dB.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.1.2.2Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.1.2.3No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.1.2.4Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2.2.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

A.16.3.2.2.1.2.5Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.16.3.2.2.1.2.6Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.16.3.2.2.1.2.7Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.16.3.2.2.24-step RA type contention based random access test in FR1 for NR standalone for 2 Rx UE

A.16.3.2.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2B.2 and clause 7.1A.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.16.3.2.2.2.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.16.3.2.2.2.1-2.

Table A.16.3.2.2.2.1-1: Supported test configurations for contention based random access test in FR1 for NR standalone

Table A.16.3.2.2.2.1-2: General test parameters for contention based random access test in FR1 for NR Standalone

A.16.3.2.2.2.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.16.3.2.2.2.2.1Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2.2.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.2.2.2Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.2.2.3No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 22  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.2.2.4Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2.2.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

A.16.3.2.2.2.2.5Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.16.3.2.2.2.2.6Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.16.3.2.2.2.2.7Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.16.3.2.2.34-step RA type non-contention based random access test in FR1 for NR standalone for 1 Rx UE

A.16.3.2.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.2B and clause 7.1A.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.16.3.2.2.3.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.16.3.2.2.3.1-2 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2). Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

Table A.16.3.2.2.3.1-1: Supported test configurations for non-contention based random access test in FR1 for NR standalone

Table A.16.3.2.2.3.1-2: General test parameters for non-contention based random access test in FR1 for NR Standalone

A.16.3.2.2.3.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.16.3.2.2.3.2.1SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2.2.2.1 for SSB-based Random Access Preamble transmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.3.2.2CSI-RS-based Random Access Preamble Transmission

In Test-2, to test the UE behavior specified in clause 6.2.2.2.2.1 for CSI-RS-based Random Access Preamble transmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with CSI-RSs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the CSI-RS configured.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the CSI-RS configured, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-OccasionList.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be 25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2.

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.3.2.3Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.3.2.4No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.44-step RA type non-contention based random access test in FR1 for NR standalone for 2 Rx UE

A.16.3.2.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.2B and clause 7.1A.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.16.3.2.2.4.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.16.3.2.2.4.1-2 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2). Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

Table A.16.3.2.2.4.1-1: Supported test configurations for non-contention based random access test in FR1 for NR standalone

Table A.16.3.2.2.4.1-2: General test parameters for non-contention based random access test in FR1 for NR Standalone

A.16.3.2.2.4.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.16.3.2.2.4.2.1SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2.2.2.1 for SSB-based Random Access Preamble transmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.4.2.2CSI-RS-based Random Access Preamble Transmission

In Test-2, to test the UE behavior specified in clause 6.2.2.2.2.1 for CSI-RS-based Random Access Preamble transmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with CSI-RSs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the CSI-RS configured.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the CSI-RS configured, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-OccasionList.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.4.2.3Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.4.2.4No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1A.2.

## A.16.3.2.2.52-step RA type contention based random access test in FR1 for NR standalone for 1 Rx UE

A.16.3.2.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the 2-step RA type random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2B.2 and clause 7.1A.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.16.3.2.2.5.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.16.3.2.2.5.1-2.

Table A.16.3.2.2.5.1-1: Supported test configurations for 2-step RA type contention based random access with successRAR test in FR1 for NR standalone

Table A.16.3.2.2.5.1-2: General test parameters for 2-step RA type contention based random access with successRAR test in FR1 for NR standalone

A.16.3.2.2.5.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.16.3.2.2.5.2.1MsgA Transmission

To test the UE behavior specified in clause 6.2.2.3.1.1 the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured msgA-RSRP-ThresholdSSB+1 dB.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first MsgA preamble transmission shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The power of the first MsgA PUSCH transmission shall be 3dB lower than the first MsgA preamble for test configuration 1 & 4 and same as the first MsgA preamble for test configuration 2 & 3 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.5.2.2MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.1.2 the System Simulator shall transmit a MsgB containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB(s) and shall transmit an ACK if the MsgB with a successRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble and if the Contention Resolution is successful.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB(s) contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The power of the first MsgA PUSCH transmission shall be 3dB lower than the first MsgA preamble for test configuration 1 & 4 and same as the first MsgA preamble for test configuration 2 & 3 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.5.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.1.3 the System Simulator shall transmit a MsgB containing a successRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if no MsgB  is received within the MsgB Response window.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The power of the first MsgA PUSCH transmission shall be 3dB lower than the first MsgA preamble for test configuration 1 & 4 and same as the first MsgA preamble for test configuration 2 & 3 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

## A.16.3.2.2.62-step RA type contention based random access test in FR1 for NR standalone for 2 Rx UE

A.16.3.2.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the 2-step RA type random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2B.2 and clause 7.1A.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.16.3.2.2.6.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.16.3.2.2.6.1-2.

Table A.16.3.2.2.6.1-1: Supported test configurations for 2-step RA type contention based random access with successRAR test in FR1 for NR standalone

Table A.16.3.2.2.6.1-2: General test parameters for 2-step RA type contention based random access with successRAR test in FR1 for NR standalone

A.16.3.2.2.6.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.16.3.2.2.6.2.1MsgA Transmission

To test the UE behavior specified in clause 6.2.2.3.1.1 the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured msgA-RSRP-ThresholdSSB.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first MsgA preamble transmission shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The power of the first MsgA PUSCH transmission shall be 3dB lower than the first MsgA preamble for test configuration 1 & 4 and same as the first MsgA preamble for test configuration 2 & 3 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.6.2.2MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.1.2 the System Simulator shall transmit a MsgB containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB(s) and shall transmit an ACK if the MsgB with a successRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble and if the Contention Resolution is successful.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB(s) contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The power of the first MsgA PUSCH transmission shall be 3dB lower than the first MsgA preamble for test configuration 1 & 4 and same as the first MsgA preamble for test configuration 2 & 3 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.6.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.1.3 the System Simulator shall transmit a MsgB containing a successRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if no MsgB  is received within the MsgB Response window.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 1,3 and 4, and be -25 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18] for test configuration 2. The power of the first MsgA PUSCH transmission shall be 3dB lower than the first MsgA preamble for test configuration 1 & 4 and same as the first MsgA preamble for test configuration 2 & 3 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

## A.16.3.2.2.72-step RA type non-contention based test in FR1 for NR standalone for 1 RX UE

A.16.3.2.2.7.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2B.2 and clause 7.1A.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.16.3.2.2.7.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.16.3.2.2.7.1-2.

Table A.16.3.2.2.7.1-1: Supported test configurations for non-contention based random access test in FR1 for NR standalone

Table A.16.3.2.2.7.1-2: General test parameters for non-contention based random access test in FR1 for NR Standalone

A.16.3.2.2.7.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.16.3.2.2.7.2.1MsgA Transmission

To test the UE behavior specified in clause 6.2.2.3.2.1, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0.

In addition, the System Simulator shall receive the MsgA PRACH on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given first by the msgA-SSB-SharedRO-MaskIndex if configured, or next by the ra-ssb-OccasionMaskIndex if configured.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble for test configuration 1 and 3dB lower than the first MsgA preamble for test configuration 2 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.7.2.2MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.2 the System Simulator shall transmit a MsgB containing a fallbackRAR containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 containing the payload of MsgA PUSCH if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble. The UE shall monitor contention resolution as described in clause 8.2A in TS 38.213 [3].

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB’s contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble for test configuration 1 and 3dB lower than the first MsgA preamble for test configuration 2 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA and msg3 transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.7.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.3 the System Simulator shall transmit a MsgB containing a successRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA transmission power when the backoff time expires if no MsgB  is received within the MsgB Response window.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble for test configuration 1 and 3dB lower than the first MsgA preamble for test configuration 2 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

## A.16.3.2.2.82-step RA type non-contention based test in FR1 for NR standalone for 2 RX UE

A.16.3.2.2.8.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2B.2 and clause 7.1A.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.16.3.2.2.8.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.16.3.2.2.8.1-2.

Table A.16.3.2.2.8.1-1: Supported test configurations for non-contention based random access test in FR1 for NR standalone

Table A.16.3.2.2.8.1-2: General test parameters for non-contention based random access test in FR1 for NR Standalone

A.16.3.2.2.8.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.16.3.2.2.8.2.1MsgA Transmission

To test the UE behavior specified in clause 6.2.2.3.2.1, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0.

In addition, the System Simulator shall receive the MsgA PRACH on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given first by the msgA-SSB-SharedRO-MaskIndex if configured, or next by the ra-ssb-OccasionMaskIndex if configured.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble for test configuration 1 and 3dB lower than the first MsgA preamble for test configuration 2 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.8.2.2MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.2 the System Simulator shall transmit a MsgB containing a fallbackRAR containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 containing the payload of MsgA PUSCH if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble. The UE shall monitor contention resolution as described in clause 8.2A in TS 38.213 [3].

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB’s contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble for test configuration 1 and 3dB lower than the first MsgA preamble for test configuration 2 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA and msg3 transmissions shall be within the accuracy specified in clause 7.1A.2.

A.16.3.2.2.8.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.3 the System Simulator shall transmit a MsgB containing a successRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA transmission power when the backoff time expires if no MsgB  is received within the MsgB Response window.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble for test configuration 1 and 3dB lower than the first MsgA preamble for test configuration 2 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

## A.16.3.2.3SA: RRC Connection Release with Redirection

## A.16.3.2.3.1Redirection from NR in FR1 to NR in FR1 for 1 Rx UE

A.16.3.2.3.1.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements specified in clause 6.2.3A.2.1.

A.16.3.2.3.1.2Test Parameters

Supported test configurations are shown in table A.16.3.2.3.1.2-1. The time delay is tested by using the parameters in table A.16.3.2.3.1.2-2, and A.16.3.2.3.1.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2. Cell 1 and Cell 2 belong to different tracking areas.

Table A.16.3.2.3.1.2-1: Redirection from NR to NR test configurations

Table A.16.3.2.3.1.2-2: General test parameters for Redirection from NR to NR test case

Table A.16.3.2.3.1.2-3: Cell specific test parameters for Redirection from NR to NR test case

A.16.3.2.3.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2240 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_NR = TRRC_procedure_delay + Tidentify-NR + TSI-NR + TRACH,

where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR = 680 ms in the test.

TSI-NR = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH = 170 ms in the test.

This gives a total of 2240 ms.

## A.16.3.2.3.2Redirection from NR in FR1 to NR in FR1 for 2 Rx UE

A.16.3.2.3.2.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements specified in clause 6.2.3A.2.1.

A.16.3.2.3.2.2Test Parameters

Supported test configurations are shown in table A.16.3.2.3.2.2-1. The time delay is tested by using the parameters in table A.16.3.2.3.2.2-2, and A.16.3.2.3.2.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2. Cell 1 and Cell 2 belong to different tracking areas.

Table A.16.3.2.3.2.2-1: Redirection from NR to NR test configurations

Table A.16.3.2.3.2.2-2: General test parameters for Redirection from NR to NR test case

Table A.16.3.2.3.2.2-3: Cell specific test parameters for Redirection from NR to NR test case

A.16.3.2.3.2.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2240 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_NR = TRRC_procedure_delay + Tidentify-NR + TSI-NR + TRACH,

where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR = 680 ms in the test.

TSI-NR = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH = 170 ms in the test.

This gives a total of 2240 ms.

## A.16.3.2.3.3Redirection from NR in FR1 to E-UTRAN for 1 Rx UE

A.16.3.2.3.3.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to E-UTRAN requirements specified in clause 6.2.3A.2.2.

A.16.3.2.3.3.2Test Parameters

Supported test configurations are shown in table A.16.3.2.3.3.2-1. The time delay is tested by using the parameters in table A.16.3.2.3.3.2-2, A.16.3.2.3.3.2-3 and A.16.3.2.3.3.2-4.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.16.3.2.3.3.2-1: Redirection from NR to E-UTRAN test configurations

Table A.16.3.2.3.3.2-2: General test parameters for Redirection from NR to E-UTRAN test case

Table A.16.3.2.3.3.2-3: Cell specific test parameters for Redirection from NR to E-UTRAN (Cell 1)

Table A.16.3.2.3.3.2-4: Cell specific test parameters for Redirection from NR to E-UTRAN (Cell 2)

A.16.3.2.3.3.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2205 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to E-UTRAN observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_E-UTRA = TRRC_procedure_delay + Tidentify-E-UTRA + TSI-E-UTRA + TRACH,

where:

TRRC_procedure_delay = 110 ms  in the test.

Tidentify-E-UTRA = 800 ms in the test.

TSI-E-UTRA = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRA cell.

TRACH = 15 ms in the test.

This gives a total of 2205 ms.

## A.16.3.2.3.4Redirection from NR in FR1 to E-UTRAN for 2 Rx UE

A.16.3.2.3.4.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to E-UTRAN requirements specified in clause 6.2.3A.2.2.

A.16.3.2.3.4.2Test Parameters

Supported test configurations are shown in table A.16.3.2.3.4.2-1. The time delay is tested by using the parameters in table A.16.3.2.3.4.2-2, A.16.3.2.3.4.2-3 and A.16.3.2.3.4.2-4.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.16.3.2.3.4.2-1: Redirection from NR to E-UTRAN test configurations

Table A.16.3.2.3.4.2-2: General test parameters for Redirection from NR to E-UTRAN test case

Table A.16.3.2.3.4.2-3: Cell specific test parameters for Redirection from NR to E-UTRAN (Cell 1)

Table A.16.3.2.3.4.2-4: Cell specific test parameters for Redirection from NR to E-UTRAN (Cell 2)

A.16.3.2.3.4.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2205 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to E-UTRAN observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_E-UTRA = TRRC_procedure_delay + Tidentify-E-UTRA + TSI-E-UTRA + TRACH,

where:

TRRC_procedure_delay = 110 ms  in the test.

Tidentify-E-UTRA = 800 ms in the test.

TSI-E-UTRA = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 36.331 for the target E-UTRA cell.

TRACH = 15 ms in the test.

This gives a total of 2205 ms.

## A.16.4Timing for RedCap

## A.16.4.1UE transmit timing

## A.16.4.1.1NR UE Transmit Timing Test for FR1 for 1 Rx RedCap UE

## A.16.4.1.1.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNB and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1A.2.

Supported test configurations are shown in table A.16.4.1.1.1-1.

Table A.16.4.1.1.1-1: Supported test configurations for FR1 PCell

For this test a single NR cell is used. Table A.16.4.1.1.1-2 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.16.4.1.1.1-3.

Table A.16.4.1.1.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.16.4.1.1.1-3: SRS Configuration for Timing Accuracy Test

## A.16.4.1.1.2Test requirements

The test requirements are the same as in clause A.6.4.1.1.2.

## A.16.4.1.2NR UE Transmit Timing Test for FR1 for 2 Rx RedCap UE

## A.16.4.1.2.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNB and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1A.2.

Supported test configurations are shown in table A.16.4.1.2.1-1.

Table A.16.4.1.2.1-1: Supported test configurations for FR1 PCell

For this test a single NR cell is used. Table A.16.4.1.2.1-2 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.16.4.1.1.1-3.

Table A.16.4.1.2.1-2: Cell Specific Test Parameters for UL Transmit Timing test

## A.16.4.1.2.2Test requirements

The test requirements are the same as in clause A.6.4.1.1.2.

## A.16.4.2Void

## A.16.4.3Timing advance

## A.16.4.3.1SA FR1 timing advance adjustment accuracy for 1 Rx UE

## A.16.4.3.1.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3A.

## A.16.4.3.1.2Test Parameters

Supported test configurations are shown in table A.16.4.3.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.16.4.3.1.2-2, A.16.4.3.1.2-3 and A.16.4.3.1.2-4.

In all test cases, single cell is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.16.4.3.1.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.16.4.3.1.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.16.4.3.1.2-1: Timing advance supported test configurations

Table A.16.4.3.1.2-2: General test parameters for timing advance

Table A.16.4.3.1.2-3: Cell specific test parameters for timing advance

Table A.16.4.3.1.2-4: Sounding Reference Symbol Configuration for timing advance

## A.16.4.3.1.3Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k=5.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.16.4.3.2SA FR1 timing advance adjustment accuracy for 2 Rx UE

## A.16.4.3.2.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3A.

## A.16.4.3.2.2Test Parameters

Supported test configurations are shown in table A.16.4.3.2.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.16.4.3.2.2-2, A.16.4.3.2.2-3 and A.16.4.3.2.2-4.

In all test cases, single cell is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.16.4.3.2.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.16.4.3.2.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.16.4.3.2.2-1: Timing advance supported test configurations

Table A.16.4.3.2.2-2: General test parameters for timing advance

Table A.16.4.3.2.2-3: Cell specific test parameters for timing advance

Table A.16.4.3.2.2-4: Sounding Reference Symbol Configuration for timing advance

## A.16.4.3.2.3Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k=5.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.16.5Signalling characteristics for RedCap

## A.16.5.1Radio link Monitoring

## A.16.5.1.1Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 1 Rx UE

## A.16.5.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the 1 Rx RedCap UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell for 1 Rx RedCap UE. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1B.2.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.16.5.1.1.1-1. The test parameters are given in tables A.16.5.1.1.1-2, A.16.5.1.1.1-3, and A.16.5.1.1.1-4 below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.16.5.1.1 .1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

Table A.16.5.1.1.1-1: Supported test configurations for FR1 PCell

Table A.16.5.1.1.1-2: General test parameters for FR1 out-of-sync testing in non-DRX mode for 1 Rx UE

Table A.16.5.1.1.1-3: Cell specific test parameters for FR1 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode for 1 Rx UE

Table A.16.5.1.1.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode for 1 Rx UE

Figure A.16.5.1.1.1-1: SNR variation for out-of-sync testing

## A.16.5.1.1.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.2Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 2 Rx UE

## A.16.5.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell for 2 Rx RedCap UE. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1B.2.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.16.5.1.2.1-1. The test parameters are given in tables A.16.5.1.2.1-2, A.16.5.1.2.1-3, and A.16.5.1.2.1-4 below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.16.5.1.2.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

Table A.16.5.1.2.1-1: Supported test configurations for FR1 PCell for 2 Rx Redcap UE

Table A.16.5.1.2.1-2: General test parameters for FR1 out-of-sync testing in non-DRX mode for 2 Rx Redcap UE

Table A.16.5.1.2.1-3: Cell specific test parameters for FR1 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode for 2 Rx Redcap UE

Table A.16.5.1.2.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

Figure A.16.5.1.2.1-1: SNR variation for out-of-sync testing

## A.16.5.1.2.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.3Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 1 Rx UE

## A.16.5.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1B.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.16.5.1.3.1-1. The test parameters are given in tables A.16.5.1.3.1-2, and A.16.5.1.3.1-3 below. There is one cell (Cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.1.3.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

Table A.16.5.1.3.1-1: Supported test configurations for FR1 PCell

Table A.16.5.1.3.1-2: General test parameters for FR1 in-sync testing in non-DRX mode

Table A.16.5.1.3.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in non-DRX mode

Table A.16.5.1.3.1-4: Void

Figure A.16.5.1.3.1-1: SNR variation for in-sync testing

## A.16.5.1.3.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.4Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 2 Rx UE

## A.16.5.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1B.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.16.5.1.4.1-1. The test parameters are given in tables A.16.5.1.4.1-2, and A.16.5.1.4.1-3 below. There is one cell (Cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.1.4.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

Table A.16.5.1.4.1-1: Supported test configurations for FR1 PCell

Table A.16.5.1.4.1-2: General test parameters for FR1 in-sync testing in non-DRX mode

Table A.16.5.1.4.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in non-DRX mode

Table A.16.5.1.4.1-4: Void

Figure A.16.5.1.4.1-1: SNR variation for in-sync testing

## A.16.5.1.4.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.5Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 1 Rx UE

## A.16.5.1.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1B.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.16.5.1.5.1-1. The test parameters are given in tables A.16.5.1.5.1-2, and A.16.5.1.5.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.16.5.1.5.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.16.5.1.5.1-1: Supported test configurations for FR1 PCell

Table A.16.5.1.5.1-2: General test parameters for FR1 out-of-sync testing in DRX mode

Table A.16.5.1.5.1-3: Cell specific test parameters for FR1 (Cell 1) for out-of-sync radio link monitoring tests in DRX mode

Figure A.16.5.1.5.1-1: SNR variation for out-of-sync testing

## A.16.5.1.5.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.6Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 2 Rx UE

## A.16.5.1.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1B.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.16.5.1.6.1-1. The test parameters are given in tables A.16.5.1.6.1-2, and A.16.5.1.6.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.16.5.1.6.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.16.5.1.6.1-1: Supported test configurations for FR1 PCell

Table A.16.5.1.6.1-2: General test parameters for FR1 out-of-sync testing in DRX mode

Table A.16.5.1.6.1-3: Cell specific test parameters for FR1 (Cell 1) for out-of-sync radio link monitoring tests in DRX mode

Figure A.16.5.1.6.1-1: SNR variation for out-of-sync testing

## A.16.5.1.6.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.7Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 1 Rx UE

## A.16.5.1.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1B.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.16.5.1.7.1-1. The test parameters are given in tables A.16.5.1.7.1-2, and A.16.5.1.7.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.1.7.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.16.5.1.7.1-1: Supported test configurations for FR1 PCell

Table A.16.5.1.7.1-2: General test parameters for FR1 in-sync testing in DRX mode

Table A.16.5.1.7.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in DRX mode

Table A.16.5.1.7.1-4: Void

Table A.16.5.1.7.1-5: Void

Figure A.16.5.1.7.1-1: SNR variation for in-sync testing.

## A.16.5.1.7.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.8Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 2 Rx UE

## A.16.5.1.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1B.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.16.5.1.8.1-1. The test parameters are given in tables A.16.5.1.8.1-2, and A.16.5.1.8.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.1.8.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.16.5.1.8.1-1: Supported test configurations for FR1 PCell

Table A.16.5.1.8.1-2: General test parameters for FR1 in-sync testing in DRX mode

Table A.16.5.1.8.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in DRX mode

Table A.16.5.1.8.1-4: Void

Table A.16.5.1.8.1-5: Void

Figure A.16.5.1.8.1-1: SNR variation for in-sync testing.

## A.16.5.1.8.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.9Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 1 Rx UE

## A.16.5.1.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used for 1 Rx RedCap UE. This test will partly verify the FR1 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1B.3.

The test parameters are given in tables A.16.5.1.9.1-1, A.16.5.1.9.1-2, A.16.5.1.9.1-3, and A.16.5.1.9.1-3A below. There is one cell, Cell 1 which is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.16.5.1.9.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting of 5 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 is configured as the BFD-RS.

Table A.16.5.1.9.1-1: Supported test configurations for FR1 PCell

Table A.16.5.1.9.1-2: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in non-DRX mode

Table A.16.5.1.9.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.16.5.1.9.1-3A: Measurement gap configuration for FR1 CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.16.5.1.9.1-4: Void

Figure A.16.5.1.9.1-1: SNR variation for CSI-RS out-of-sync testing

## A.16.5.1.9.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During time durations T1, T2 and T3, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 no later than time point C (D1 ms after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.10Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 2 Rx UE

## A.16.5.1.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used for 2 Rx RedCap UE. This test will partly verify the FR1 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1B.3.

The test parameters are given in tables A.16.5.1.10.1-1, A.16.5.1.10.1-2, A.16.5.1.10.1-3, and A.16.5.1.10.1-3A below. There is one cell, Cell 1 which is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.16.5.1.10.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting of 5 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 is configured as the BFD-RS and is not same as RLM-RS to avoid triggering the beam failure during the RLM test.

Table A.16.5.1.10.1-1: Supported test configurations for FR1 PCell

Table A.16.5.1.10.1-2: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in non-DRX mode

Table A.16.5.1.10.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.16.5.1.10.1-3A: Measurement gap configuration for FR1 CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.16.5.1.10.1-4: Void

Figure A.16.5.1.10.1-1: SNR variation for CSI-RS out-of-sync testing

## A.16.5.1.10.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During time durations T1, T2 and T3, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 no later than time point C (D1 ms after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.11Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 1 Rx UE

## A.16.5.1.11.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used. This test will partly verify the FR1 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1B.3.

The test parameters are given in tables A.16.5.1.11.1-1, A.16.5.1.11.1-2, and A.16.5.1.11.1-3 below. There is one cells, Cell 1which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.1.11.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled. In the test, SSB0 is configured as the BFD-RS.

Table A.16.5.1.11.1-1: Supported test configurations for FR1 PCell

Table A.16.5.1.11.1-2: General test parameters for FR1 PCell for CSI-RS in-sync testing in non-DRX mode

Table A.16.5.1.11.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in non-DRX mode

Table A.16.5.1.11.1-4: Void

Figure A.16.5.1.11.1-1: SNR variation for CSI-RS in-sync testing

## A.16.5.1.11.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.12Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 2 Rx UE

## A.16.5.1.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used. This test will partly verify the FR1 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1B.3.

The test parameters are given in tables A.16.5.1.12.1-1, A.16.5.1.12.1-2, and A.16.5.1.12.1-3 below. There is one cells, Cell 1which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.1.12.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled. In the test, SSB0 is configured as the BFD-RS and is not same as RLM-RS to avoid triggering the beam failure during the RLM test.

Table A.16.5.1.12.1-1: Supported test configurations for FR1 PCell

Table A.16.5.1.12.1-2: General test parameters for FR1 PCell for CSI-RS in-sync testing in non-DRX mode

Table A.16.5.1.12.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in non-DRX mode

Table A.16.5.1.12.1-4: Void

Figure A.16.5.1.12.1-1: SNR variation for CSI-RS in-sync testing

## A.16.5.1.12.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.13Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 1 Rx UE

## A.16.5.1.13.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when DRX is used. This test will partly verify the FR1 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1B.3.

The test parameters are given in tables A.16.5.1.13.1-1, A.16.5.1.13.1-2, and A.16.5.1.13.1-3 below. There is one cell, Cell 1 is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.16.5.1.13.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test. In the test, SSB0 is configured as the BFD-RS.

Table A.16.5.1.13.1-1: Supported test configurations for FR1 PCell

Table A.16.5.1.13.1-2: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in DRX mode

Table A.16.5.1.13.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in DRX mode

Figure A.16.5.1.13.1-1: SNR variation for CSI-RS out-of-sync testing

## A.16.5.1.13.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During time durations T1, T2 and T3, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on PCell.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 (PCell) at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 (PCell) no later than time point C (D1 ms after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.14Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 2 Rx UE

## A.16.5.1.14.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when DRX is used. This test will partly verify the FR1 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in tables A.16.5.1.14.1-1, A.16.5.1.14.1-2, and A.16.5.1.14.1-3 below. There is one cell, Cell 1 is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.16.5.1.14.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test. In the test, SSB0 is configured as the BFD-RS and is not same as RLM-RS to avoid triggering the beam failure during the RLM test.

Table A.16.5.1.14.1-1: Supported test configurations for FR1 PCell

Table A.16.5.1.14.1-2: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in DRX mode

Table A.16.5.1.14.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in DRX mode

Figure A.16.5.1.14.1-1: SNR variation for CSI-RS out-of-sync testing

## A.16.5.1.14.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During time durations T1, T2 and T3, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on PCell.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 (PCell) at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 (PCell) no later than time point C (D1 ms after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.15Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 1 Rx UE

## A.16.5.1.15.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when DRX is used. This test will partly verify the FR1 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1B.3.

The test parameters are given in tables A.16.5.1.15.1-1, A.16.5.1.151-2, A.16.5.1.15.1-3 and A.16.5.1.15.1-3A below. There is one cells, Cell 1which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.1.15.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 is configured as the BFD-RS.

Table A.16.5.1.15.1-1: Supported test configurations for FR1 PSCell

Table A.16.5.1.15.1-2: General test parameters for FR1 PCell for CSI-RS in-sync testing in non-DRX mode

Table A.16.5.1.15.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in non-DRX mode

Table A.16.5.1.15.1-3A: Measurement gap configuration for FR1 CSI-RS in-sync radio link monitoring in non-DRX mode

Figure A.16.5.1.15.1-1: SNR variation for CSI-RS in-sync testing

## A.16.5.1.15.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.1.16Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 2 Rx UE

## A.16.5.1.16.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when DRX is used. This test will partly verify the FR1 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1B.3.

The test parameters are given in tables A.16.5.1.15.1-1, A.16.5.1.151-2, A.16.5.1.15.1-3 and A.16.5.1.15.1-3A below. There is one cells, Cell 1which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.1.15.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 is configured as the BFD-RS and is not same as RLM-RS to avoid triggering the beam failure during the RLM test.

Table A.16.5.1.16.1-1: Supported test configurations for FR1 PSCell

Table A.16.5.1.16.1-2: General test parameters for FR1 PCell for CSI-RS in-sync testing in non-DRX mode

Table A.16.5.1.16.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in non-DRX mode

Table A.16.5.1.16.1-3A: Measurement gap configuration for FR1 CSI-RS in-sync radio link monitoring in non-DRX mode

Figure A.16.5.1.15.1-1: SNR variation for CSI-RS in-sync testing

## A.16.5.1.16.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.2Beam Failure Detection and Link recovery procedures

## A.16.5.2.1Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode for 1 Rx UE

## A.16.5.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5B.

The test parameters are given in tables A.16.5.2.1.1-1, A.16.5.2.1.1-2, A.16.5.2.1.1-3 and A.16.5.2.1.1-4 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.2.1.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.16.5.2.1.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 2 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

Table A.16.5.2.1.1-1: Supported test configurations for FR1 PCell

Table A.16.5.2.1.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.16.5.2.1.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.16.5.2.1.1-4: Void

Figure A.16.5.2.1.1-1: SNR and L1-RSRP variation SSB for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.16.5.2.1.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 120+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.2.2Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode for 2 Rx UE

## A.16.5.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5B.

The test parameters are given in tables A.16.5.2.2.1-1, A.16.5.2.2.1-2, A.16.5.2.2.1-3 and A.16.5.2.2.1-4 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.2.2.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.16.5.2.2.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 2 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

Table A.16.5.2.2.1-1: Supported test configurations for FR1 PCell

Table A.16.5.2.2.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.16.5.2.2.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.16.5.2.2.1-4: Void

Figure A.16.5.2.2.1-1: SNR and L1-RSRP variation SSB for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.16.5.2.2.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 120+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.2.3Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode for 1 Rx UE

## A.16.5.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery requirements for an FR1 serving cell in clause 8.5B.2.

The test parameters are given in tables A.16.5.2.3.1-1, A.16.5.2.3.1-2, and A.16.5.2.3.1-3 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.2.3.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.16.5.2.3.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.16.5.2.3.1-1: Supported test configurations for FR1 PCell

Table A.16.5.2.3.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.16.5.2.3.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Figure A.16.5.2.2.1-1: SNR and L1-RSRP variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.16.5.2.3.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 1920+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.2.4Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode for 2 Rx UE

## A.16.5.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery requirements for an FR1 serving cell in clause 8.5B.2.

The test parameters are given in tables A.16.5.2.4.1-1, A.16.5.2.4.1-2, and A.16.5.2.4.1-3 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.2.4.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.16.5.2.4.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.16.5.2.4.1-1: Supported test configurations for FR1 PCell

Table A.16.5.2.4.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.16.5.2.4.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Figure A.16.5.2.4.1-1: SNR and L1-RSRP variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.16.5.2.4.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 1920+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.2.5Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode for 1 Rx UE

## A.16.5.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery requirements for an FR1 serving cell in clause 8.5B.3.

The test parameters are given in tables A.16.5.2.5.1-1, A.16.5.2.5.1-2, and below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.2.5.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.16.5.2.5.1-1 additionally shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

Table A.16.5.2.5.1-1: Supported test configurations for FR1 PCell

Table A.16.5.2.5.1-2: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.16.5.2.5.1-3: Cell specific test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Figure A.16.5.2.5.1-1: SNR and L1-RSRP variation for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

## A.16.5.2.5.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 30+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.2.6Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode for 2 Rx UE

## A.16.5.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5B.3.

The test parameters are given in tables A.16.5.2.6.1-1, A.16.5.2.6.1-2, and below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.2.6.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.16.5.2.6.1-1 additionally shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

Table A.16.5.2.6.1-1: Supported test configurations for FR1 PCell

Table A.16.5.2.6.1-2: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.16.5.2.6.1-3: Cell specific test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Figure A.16.5.2.6.1-1: SNR and L1-RSRP variation for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

## A.16.5.2.6.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 30+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.2.7Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode for 1 Rx UE

## A.16.5.2.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery requirements for an FR1 serving cell in clause 8.5B.3.

The test parameters are given in tables A.16.5.2.7.1-1, A.16.5.2.7.1-2, and A.16.5.2.7.1-3 below.  There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.2.7.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.16.5.2.7.1-1 additionally shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.16.5.2.7.1-1: Supported test configurations for FR1 PCell

Table A.16.5.2.7.1-2: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.16.5.2.7.1-3: Cell specific test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Figure A.16.5.2.7.1-1: SNR and L1-RSRP variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

## A.16.5.2.7.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 1920+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.2.8Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode for 2 Rx UE

## A.16.5.2.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery requirements for an FR1 serving cell in clause 8.5B.3.

The test parameters are given in Tables A.16.5.2.8.1-1, A.16.5.2.8.1-2, and A.16.5.2.8.1-3 below.There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.16.5.2.8.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.16.5.2.8.1-1 additionally shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.16.5.2.8.1-1: Supported test configurations for FR1 PCell

Table A.16.5.2.8.1-2: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.16.5.2.8.1-3: Cell specific test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Figure A.16.5.2.8.1-1: SNR and L1-RSRP variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

## A.16.5.2.8.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 1920+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.3Active BWP switch

## A.16.5.3.1DCI-based and Timer-based Active BWP Switch

## A.16.5.3.1.1NR FR1 DL active BWP switch with non-DRX in SA for 1 Rx UE

## A.16.5.3.1.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for 1 Rx RedCap defined in clause 8.6A.

The supported test configurations are shown in table A.16.5.3.1.1.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.16.5.3.1.1.1-2. Cell-specific parameters of the cell are specified in table A.16.5.3.1.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE is configured with 2 different UE-specific downlink bandwidth parts, BWP-1 and BWP-2 before starting the test.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1.

-UE is configured with a bwp-InactivityTimer timer value for Cell 1.

The cell has constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for DL BWP switch, sent from the test equipment to the UE, is received at the UE side in Cell 1’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6A and starts to report valid ACK/NACK for the Cell 1 no later than the first UL slot that occurs after the beginning of slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on Cell 1’s BWP-2 starting from the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).

During T2, the test equipment won’t transmit DCI format for PDSCH reception on Cell 1.

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the subframe immediately after bwp-InactivityTimer timer expires. The UE shall switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s slot (j+TBWPswitchDelay) as defined in clause 8.6A and starts to report valid ACK/NACK for the Cell 1 at latest on the first UL slot that occurs after the beginning of slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on Cell 1’s BWP-1 starting from the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

The test equipment verifies the DL BWP switch time by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK/NACK is received.

Table A.16.5.3.1.1.1-1: DL BWP switch supported test configurations

Table A.16.5.3.1.1.1-2: General test parameters for DL BWP switch in SA

Table A.16.5.3.1.1.1-3: NR Cell specific test parameters for DL BWP switch in SA

## A.16.5.3.1.1.2Test Requirements

During T1, the UE shall start to send the ACK/NACK for Cell 1 from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for Cell 1 from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6A.2-1.

All of the above test requirements shall be fulfilled in order for the observed Cell 1 active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first UL slot that occurs after beginning of DL slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

## A.16.5.3.1.2NR FR1 DL active BWP switch with non-DRX in SA for 2 Rx UE

## A.16.5.3.1.2.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for 2 Rx RedCap defined in clause 8.6A.

The supported test configurations are shown in table A.16.5.3.1.2.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.16.5.3.1.2.1-2. Cell-specific parameters of the cell are specified in table A.16.5.3.1.2.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE is configured with 2 different UE-specific downlink bandwidth parts, BWP-1 and BWP-2 before starting the test.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1.

-UE is configured with a bwp-InactivityTimer timer value for Cell 1.

The cell has constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for DL BWP switch, sent from the test equipment to the UE, is received at the UE side in Cell 1’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6A and starts to report valid ACK/NACK for the Cell 1 no later than the first UL slot that occurs after the beginning of slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on Cell 1’s BWP-2 starting from the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).

During T2, the test equipment won’t transmit DCI format for PDSCH reception on Cell 1.

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the subframe immediately after bwp-InactivityTimer timer expires. The UE shall switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s slot (j+TBWPswitchDelay) as defined in clause 8.6A and starts to report valid ACK/NACK for the Cell 1 at latest on the first UL slot that occurs after the beginning of slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on Cell 1’s BWP-1 starting from the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

The test equipment verifies the DL BWP switch time by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK/NACK is received.

Table A.16.5.3.1.2.1-1: DL BWP switch supported test configurations

Table A.16.5.3.1.2.1-2: General test parameters for DL BWP switch in SA

Table A.16.5.3.1.2.1-3: NR Cell specific test parameters for DL BWP switch in SA

## A.16.5.3.1.2.2Test Requirements

During T1, the UE shall start to send the ACK/NACK for Cell 1 from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for Cell 1 from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6A.2-1.

All of the above test requirements shall be fulfilled in order for the observed Cell 1 active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first UL slot that occurs after beginning of DL slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

## A.16.5.3.2RRC-based Active BWP Switch

## A.16.5.3.2.1NR FR1 DL active BWP switch of Cell with non-DRX in SA for 1 Rx UE

## A.16.5.3.2.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6A.

The supported test configurations are shown in table A.16.5.3.2.1.1-1. The test scenario comprises of one Cell (Cell 1) as given in table A.16.5.3.2.1.1-2. Cell-specific parameters of Cell are specified in table A.16.5.3.2.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE has bandwidth part BWP-1 in its RRCReconfiguration for Cell 1.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in Cell 1.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is completely received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition.

The UE shall be able to receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot as defined in clause 8.6A.3 and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot on BWP-1 of final condition. The UE shall be continuously scheduled on PCell’s BWP-1 of final condition starting from the first DL slot right after slot . i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length

TRRCprocessingDelay and TBWPswitchDelayRRC are defined in clause 8.6A.3.

The test equipment verifies the DL BWP switch time in Cell by counting the time from the time when the RRCReconfiguration message including updated BWP configuration is sent till the time when a valid ACK/NACK is received is received.

Table A.16.5.3.2.1.1-1: DL BWP switch supported test configurations in SA scenario

Table A.16.5.3.2.1.1-2: General test parameters for DL BWP switch in SA scenario

Table A.16.5.3.2.1.1-3: NR Cell specific test parameters for DL BWP switch in SA scenario

## A.16.5.3.2.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the Cell from the first DL slot that occurs right after the beginning of slot  and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot. i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed Cell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.3.2.2NR FR1 DL active BWP switch of Cell with non-DRX in SA for 2 Rx UE

## A.16.5.3.2.2.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6A.

The supported test configurations are shown in table A.16.5.3.2.2.1-1. The test scenario comprises of one Cell (Cell 1) as given in table A.16.5.3.2.2.1-2. Cell-specific parameters of Cell are specified in table A.16.5.3.2.2.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE has bandwidth part BWP-1 in its RRCReconfiguration for Cell 1.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in Cell 1.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is completely received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition.

The UE shall be able to receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot as defined in clause 8.6A.3 and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot on BWP-1 of final condition. The UE shall be continuously scheduled on PCell’s BWP-1 of final condition starting from the first DL slot right after slot . i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length

TRRCprocessingDelay and TBWPswitchDelayRRC are defined in clause 8.6A.3.

The test equipment verifies the DL BWP switch time in Cell by counting the time from the time when the RRCReconfiguration message including updated BWP configuration is sent till the time when a valid ACK/NACK is received is received.

Table A.16.5.3.2.2.1-1: DL BWP switch supported test configurations in SA scenario

Table A.16.5.3.2.2.1-2: General test parameters for DL BWP switch in SA scenario

Table A.16.5.3.2.2.1-3: NR Cell specific test parameters for DL BWP switch in SA scenario

## A.16.5.3.2.2.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the Cell from the first DL slot that occurs right after the beginning of slot  and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot. i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed Cell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.4UE specific CBW change

## A.16.5.4.1UE specific CBW change on PCell in FR1 in non-DRX for 1 Rx UE

## A.16.5.4.1.1Test Purpose and Environment

The purpose of this test is to verify the UE specific CBW change delay requirement defined in clause 8.13A.

The supported test configurations are shown in table A.16.5.4.1.1-1. The test scenario comprises of one Cell (Cell 1) as given in table A.16.5.4.1.1-2. Cell-specific parameters are specified in table A.16.5.4.1.1-3.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE sends ACK/NACK during the test.

Before the test starts:

-UE is connected to Cell 1 on radio channel 1.

-UE has bandwidth part BWP-1 in its RRCReconfiguration for Cell 1.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in Cell 1.

-UE has been configured with UE specific CBW (CBW-1).

-UE is indicated in SCS-SpecificCarrier [2] that the UE specific CBW is CBW-1 as the initial condition in Cell 1.

Cell 1 has constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration containing SCS-SpecificCarrier with updated UE specific CBW, sent from the test equipment to the UE, is completely received at the UE side in Cell 1’s slot # denoted i. The UE shall reconfigure its UE specific CBW with the updated CBW-2 for the final condition.

The UE shall be able to receive PDSCH on Cell 1 from the first DL slot that occurs after the beginning of DL slot as defined in clause 8.13A and starts to report valid ACK/NACK for Cell 1from the first UL slot that occurs after the beginning of DL slot on the Cell 1’s BWP-1 on CBW-2 for the final condition. The UE shall be continuously scheduled on the Cell 1’s BWP-1 on CBW-2  for the final condition starting from the first DL slot right after slot . i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length+k1i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length

and  are defined in clause 8.13A.TRRCprocessingDelayTCBWchangeDelayRRC

The test equipment verifies the UE specific CBW switching delay in Cell 1 by estimating the time from the moment the RRCReconfiguration message including updated UE specific CBW configuration is sent until the moment a valid ACK/NACK is received.

Table A.16.5.4.1.1-1: Supported test configurations for UE specific CBW change in SA scenario

Table A.16.5.4.1.1-2: General test parameters for UE specific CBW change in SA scenario

Table A.16.5.4.1.1-3: NR Cell specific test parameters for UE specific CBW change in SA scenario

## A.16.5.4.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the Cell 1 from the first DL slot that occurs right after the beginning of slot  and starts to report valid ACK/NACK for Cell 1 from the first UL slot that occurs after the beginning of DL slot.i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed UE specific CBW change delay on the Cell 1 to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.5.4.2UE specific CBW change on PCell in FR1 in non-DRX for 2 Rx UE

## A.16.5.4.2.1Test Purpose and Environment

The purpose of this test is to verify the UE specific CBW change delay requirement defined in clause 8.13A.

The supported test configurations are shown in table A.16.5.4.2.1-1. The test scenario comprises of one Cell (Cell 1) as given in table A.16.5.4.2.1-2. Cell-specific parameters are specified in table A.16.5.4.2.1-3.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE sends ACK/NACK during the test.

Before the test starts:

-UE is connected to Cell 1 on radio channel 1.

-UE has bandwidth part BWP-1 in its RRCReconfiguration for Cell 1.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in Cell 1.

-UE has been configured with UE specific CBW (CBW-1).

-UE is indicated in SCS-SpecificCarrier [2] that the UE specific CBW is CBW-1 as the initial condition in Cell 1.

Cell 1 has constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration containing SCS-SpecificCarrier with updated UE specific CBW, sent from the test equipment to the UE, is completely received at the UE side in Cell 1’s slot # denoted i. The UE shall reconfigure its UE specific CBW with the updated CBW-2 for the final condition.

The UE shall be able to receive PDSCH on Cell 1 from the first DL slot that occurs after the beginning of DL slot as defined in clause 8.13A and starts to report valid ACK/NACK for Cell 1from the first UL slot that occurs after the beginning of DL slot on the Cell 1’s BWP-1 on CBW-2 for the final condition. The UE shall be continuously scheduled on the Cell 1’s BWP-1 on CBW-2  for the final condition starting from the first DL slot right after slot . i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length+k1i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length

and  are defined in clause 8.13A.TRRCprocessingDelayTCBWchangeDelayRRC

The test equipment verifies the UE specific CBW switching delay in Cell 1 by estimating the time from the moment the RRCReconfiguration message including updated UE specific CBW configuration is sent until the moment a valid ACK/NACK is received.

Table A.16.5.4.2.1-1: Supported test configurations for UE specific CBW change in SA scenario

Table A.16.5.4.2.1-2: General test parameters for UE specific CBW change in SA scenario

Table A.16.5.4.2.1-3: NR Cell specific test parameters for UE specific CBW change in SA scenario

## A.16.5.4.2.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the Cell 1 from the first DL slot that occurs right after the beginning of slot  and starts to report valid ACK/NACK for Cell 1 from the first UL slot that occurs after the beginning of DL slot.i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed UE specific CBW change delay on the Cell 1 to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.6Measurement procedure for RedCap

## A.16.6.1Intra-frequency Measurements

## A.16.6.1.1SA event triggered reporting tests without gap under non-DRX for 1 Rx UE

## A.16.6.1.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2B.5.1 and 9.2B.5.2.

## A.16.6.1.1.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell and neighbour cell are given in table A.16.6.1.1.1-1 and A.16.6.1.1.1-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.16.6.1.1.1.2-1: Supported test configurations

Table A.16.6.1.1.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FR1

Table A.16.6.1.1.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

## A.16.6.1.1.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1000 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.1.2SA event triggered reporting tests without gap under non-DRX for 2 Rx UE

## A.16.6.1.2.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2B.5.1 and 9.2B.5.2.

## A.16.6.1.2.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell and neighbour cell are given in table A.16.6.1.2.1-1 and A.16.6.1.2.1-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.16.6.1.2.1.2-1: Supported test configurations

Table A.16.6.1.2.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FR1

Table A.16.6.1.2.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

## A.16.6.1.2.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1000 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.1.3SA event triggered reporting tests without gap under DRX for 1 Rx UE

## A.16.6.1.3.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell identification and measurement period requirements in clauses 9.2B.5.1 and 9.2B.5.2.

## A.16.6.1.3.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.16.6.1.3.2-1, A.16.6.1.3.2-2 and A.16.6.1.3.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.16.6.1.3.2-1: Supported test configurations for NR Redcap UE

Table A.16.6.1.3.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for PCell in FR1 with DRX

Table A.16.6.1.3.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for PCell in FR1 with DRX

## A.16.6.1.3.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 7680 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.1.4SA event triggered reporting tests without gap under DRX for 2 Rx UE

## A.16.6.1.4.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell identification and measurement period requirements in clauses 9.2B.5.1 and 9.2B.5.2.

## A.16.6.1.4.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.16.6.1.4.2-1, A.16.6.1.4.2-2 and A.16.6.1.4.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.16.6.1.4.2-1: Supported test configurations for NR Redcap UE

Table A.16.6.1.3.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for PCell in FR1 with DRX

Table A.16.6.1.4.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for PCell in FR1 with DRX

## A.16.6.1.4.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 6400 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.1.5SA event triggered reporting tests with per-UE gaps under non-DRX for 1 Rx UE

## A.16.6.1.5.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2B.6.1 and 9.2B.6.2.

## A.16.6.1.5.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.16.6.1.5.2-1 and A.16.6.1.5.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

Table A.16.6.1.5.2-1: Supported test configurations

Table A.16.6.1.5.2-2: General test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1

Table A.16.6.1.5.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1

## A.16.6.1.5.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.1.6SA event triggered reporting tests with per-UE gaps under non-DRX for 2 Rx UE

## A.16.6.1.6.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2B.6.1 and 9.2B.6.2.

## A.16.6.1.6.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.16.6.1.6.2-1 and A.16.6.1.6.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

Table A.16.6.1.6.2-1: Supported test configurations

Table A.16.6.1.6.2-2: General test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1

Table A.16.6.1.6.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1

## A.16.6.1.6.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.1.7SA event triggered reporting tests with per-UE gaps under DRX for 1 Rx UE

## A.16.6.1.7.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell identification and measurement period requirements in clauses 9.2B.6.1 and 9.2B.6.2.

## A.16.6.1.7.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.16.6.1.7.2-1, A.16.6.1.7.2-2 and A.16.6.1.7.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.16.6.1.7.2-1: Supported test configurations for NR Redcap UE

Table A.16.6.1.7.2-2: General test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1 with DRX

Table A.16.6.1.7.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with per-UE gap for PCell in FR1 with DRX

## A.16.6.1.7.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 7680 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.1.8SA event triggered reporting tests with per-UE gaps under DRX for 2 Rx UE

## A.16.6.1.8.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell identification and measurement period requirements in clauses 9.2B.6.1 and 9.2B.6.2.

## A.16.6.1.8.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.16.6.1.8.2-1, A.16.6.1.8.2-2 and A.16.6.1.8.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.16.6.1.8.2-1: Supported test configurations for NR Redcap UE

Table A.16.6.1.8.2-2: General test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1 with DRX

Table A.16.6.1.8.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with per-UE gap for PCell in FR1 with DRX

## A.16.6.1.8.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 6400 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.1.9SA event triggered reporting tests without gap under non-DRX with SSB index reading for 1 Rx UE

## A.16.6.1.9.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2B.5.1 and 9.2B.5.2.

## A.16.6.1.9.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for FDD PCell and neighbour cell are given in table A.16.6.1.9.2-1 and A.16.6.1.9.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.16.6.1.9.2-1: Supported test configurations

Table A.16.6.1.9.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

Table A.16.6.1.9.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

## A.16.6.1.9.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1480 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.1.10SA event triggered reporting tests without gap under non-DRX with SSB index reading for 2 Rx UE

## A.16.6.1.10.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2.5.1 and 9.2.5.2.

## A.16.6.1.10.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for FDD PCell and neighbour cell are given in table A.16.6.1.10.2-1 and A.16.6.1.10.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.16.6.1.10.2-1: Supported test configurations

Table A.16.6.1.10.2-2: General test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

Table A.16.6.1.10.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FDD PCell in FR1 with SSB index reading

## A.16.6.1.10.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1240 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.1.11SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading for 1 Rx UE

## A.16.6.1.11.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell identification and measurement period requirements in clauses 9.2B.6.1 and 9.2B.6.2.

## A.16.6.1.11.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.16.6.1.11.2-1, A.16.6.1.11.2-2 and A.16.6.1.11.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

Table A.16.6.1.11.2-1: Supported test configurations for NR Redcap UE

Table A.16.6.1.11.2-2: General test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1 with SSB index reading

Table A.16.6.1.11.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with per-UE gap for PCell in FR1 with SSB index reading

## A.16.6.1.11.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1040 ms from the beginning of time period T2. The UE isrequired to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.1.12SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading for 2 Rx UE

## A.16.6.1.12.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell identification and measurement period requirements in clauses 9.2B.6.1 and 9.2B.6.2.

## A.16.6.1.12.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for PCell are given in table A.16.6.1.12.2-1, A.16.6.1.12.2-2 and A.16.6.1.12.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

Table A.16.6.1.12.2-1: Supported test configurations for NR Redcap UE

Table A.16.6.1.12.2-2: General test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR1 with SSB index reading

Table A.16.6.1.11.2-3: NR Cell specific test parameters for SA intra-frequency event triggered reporting with per-UE gap for PCell in FR1 with SSB index reading

## A.16.6.1.12.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.2Inter-frequency Measurements

## A.16.6.2.1SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for 1 Rx UE

## A.16.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.16.6.2.1.1-1, A.16.6.2.1.1-2 and A.16.6.2.1.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.16.6.2.1.1-1: Supported test configurations

Table A.16.6.2.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.16.6.2.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.16.6.2.1.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

Table A.16.6.2.1.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

## A.16.6.2.1.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1080 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 11520 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1and 2 UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.2.2SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for 2 Rx UE

## A.16.6.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.16.6.2.22.2.1-1, A.16.6.2.2.1-2 and A.16.6.2.2.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.16.6.2.2.1-1: Supported test configurations

Table A.16.6.2.2.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.16.6.2.2.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.16.6.2.2.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

Table A.16.6.2.2.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

## A.16.6.2.2.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1080 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 10240 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2 UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.2.3SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used for 1 Rx UE

## A.16.6.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.16.6.2.3.1-1, A.16.6.2.3.1-2 and A.16.6.2.3.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.16.6.2.3.1-1: Supported test configurations

Table A.16.6.2.3.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.16.6.2.3.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

## A.16.6.2.3.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1000 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.2.4SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used for 2 Rx UE

## A.16.6.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.16.6.2.4.1-1, A.16.6.2.4.1-2 and A.16.6.2.4.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.16.6.2.4.1-1: Supported test configurations

Table A.16.6.2.4.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.16.6.2.4.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

## A.16.6.2.4.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.2.5SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used for 1 Rx UE

## A.16.6.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.16.6.2.5.1-1, A.16.6.2.5.1-2 and A.16.6.2.5.1-3.7

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.16.6.2.5.1-1: Supported test configurations

Table A.16.6.2.5.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

Table A.16.6.2.5.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

## A.16.6.2.5.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1240 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.2.6SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used for 2 Rx UE

## A.16.6.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.16.6.2.6.1-1, A.16.6.2.6.1-2 and A.16.6.2.6.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.16.6.2.6.1-1: Supported test configurations

Table A.16.6.2.5.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

Table A.16.6.2.6.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

## A.16.6.2.6.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1040 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.2.7SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used for 1 Rx UE

## A.16.6.2.7.1Test Purpose and Environment

The purpose of this test is to verify that 1 Rx RedCap UE makes correct reporting of an event in FR1. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.16.6.2.7.1-1, A.16.6.2.7.1-2 and A.16.6.2.7.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.16.6.2.7.1-1: Supported test configurations

Table A.16.6.2.7.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

Table A.16.6.2.7.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

## A.16.6.2.7.2Test Requirements

In test 1 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1440 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2  the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 15360 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1and 2 UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.2.8SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used for 2 Rx UE

## A.16.6.2.8.1Test Purpose and Environment

The purpose of this test is to verify that 2 Rx RedCap UE makes correct reporting of an event in FR1. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3.4.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.16.6.2.8.1-1, A.16.6.2.8.1-2 and A.16.6.2.8.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.16.6.2.8.1-1: Supported test configurations

Table A.16.6.2.8.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

Table A.16.6.2.8.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

## A.16.6.2.8.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1280 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 12160 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2 UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.2.9SA event triggered reporting tests with additional mandatory gap pattern for 1 Rx UE

## A.16.6.2.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event when mandatory gap pattern with 3 ms MGL is configured.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.16.6.2.9.1-1, A.16.6.2.9.1-2 and A.16.6.2.9.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.16.6.2.9.1-1: Supported test configurations

Table A.16.6.2.9.1-2: General test parameters for SA inter-frequency event triggered reporting with additional mandatory gap pattern

Table A.16.6.2.9.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting with additional mandatory gap pattern

## A.16.6.2.9.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1440 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.2.10SA event triggered reporting tests with additional mandatory gap pattern for 2 Rx UE

## A.16.6.2.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event when mandatory gap pattern with 3 ms MGL is configured.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The test parameters are given in tables A.16.6.2.10.1-1, A.16.6.2.10.1-2 and A.16.6.2.10.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.16.6.2.10.1-1: Supported test configurations

Table A.16.6.2.10.1-2: General test parameters for SA inter-frequency event triggered reporting with additional mandatory gap pattern

Table A.16.6.2.10.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting with additional mandatory gap pattern

## A.16.6.2.10.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1440 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.2.11SA event triggered reporting tests for FR1 when DRX is used for 1 Rx UE

## A.16.6.2.11.1Test Purpose and Environment

The purpose of this test is to verify that the UE which supports interFrequencyMeas-Nogap-r16 makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search without measurement gap requirements in clause 9.3B.7.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on RF channel 2. The SSB of Cell 2 is completely within UE’s active BWP BW. The PRBs containing SSB from Cell 1 and Cell 2 should be different in frequency location within the cell bandwidth. The test parameters are given in tables A.16.6.2.11.1-1, A.16.6.2.11.1-2 and A.16.6.2.11.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.16.6.2.11.1-1: Supported test configurations

Table A.16.6.2.11.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 when DRX is used

Table A.16.6.2.11.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 when DRX is used

Table A.16.6.2.11.1-4: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting when DRX is used

## A.16.6.2.11.2Test Requirements

In test config 1, UE is required to report SSB time index. The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1280 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test config 2 and 3, UE is not required to report SSB time index. The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.2.12SA event triggered reporting tests for FR1 when DRX is used for 2 Rx UE

## A.16.6.2.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE which supports interFrequencyMeas-Nogap-r16 makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search without measurement gap requirements in clause 9.3B.7.

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on RF channel 2. The SSB of Cell 2 is completely within UE’s active BWP BW. The PRBs containing SSB from Cell 1 and Cell 2 should be different in frequency location within the cell bandwidth. The test parameters are given in tables A.16.6.2.12.1-1, A.16.6.2.12.1-2 and A.16.6.2.12.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.16.6.2.12.1-1: Supported test configurations

Table A.16.6.2.12.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 when DRX is used

Table A.16.6.2.12.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 when DRX is used

Table A.16.6.2.12.1-4: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting when DRX is used

## A.16.6.2.12.2Test Requirements

In test config 1 and 4, UE is required to report SSB time index. The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1120 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test config 2 and 3, UE is not required to report SSB time index. The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.3Inter-RAT Measurements

## A.16.6.3.1SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 for 1 Rx UE

## A.16.6.3.1.1Test purpose and Environment

The purpose of this set of tests is to verify that the 1 Rx redcap UE makes correct event-triggered reporting of inter-RAT E-UTRAN measurements when operating in standalone (SA) operation with PCell in FR1. This test shall partly verify the cell search and measurement requirements in clauses 9.4A.2 and 9.4A.3.

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. In the measurement control information from the PCell it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively.  Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

Supported test configurations are shown in table A.16.6.3.1.1-1. General test parameters are provided in table A.16.6.3.1.1-2 below. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.16.6.3.1.1-3 and A.16.6.3.1.1-4, respectively.

Table A.16.6.3.1.1-1: Supported test configurations in SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

Table A.16.6.3.1.1-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

Table A.16.6.3.1.1-3: PCell specific test parameters for SA inter-RAT E-UTRA event triggered reporting in non-DRX with PCell in FR1

Table A.16.6.3.1.1-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

## A.16.6.3.1.2Test Requirements

The UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 3.84 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.3.2SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 for 2 Rx UE

## A.16.6.3.2.1Test purpose and Environment

The purpose of this set of tests is to verify that the 2 Rx redcap UE makes correct event-triggered reporting of inter-RAT E-UTRAN measurements when operating in standalone (SA) operation with PCell in FR1. This test shall partly verify the cell search and measurement requirements in clauses 9.4A.2 and 9.4A.3.

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. In the measurement control information from the PCell it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

Supported test configurations are shown in table A.16.6.3.2.1-1. General test parameters are provided in table A.16.6.3.2.1-2 below. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.16.6.3.2.1-3 and A.16.6.3.2.1-4, respectively.

Table A.16.6.3.2.1-1: Supported test configurations in SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1 for 1 Rx UE

Table A.16.6.3.2.1-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

Table A.16.6.3.1.1-3: PCell specific test parameters for SA inter-RAT E-UTRA event triggered reporting in non-DRX with PCell in FR1

Table A.16.6.3.2.1-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

## A.16.6.3.2.2Test Requirements

The UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 3.84 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.3.3SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for 1 Rx UE

## A.16.6.3.3.1Test purpose and Environment

The purpose of this set of tests is to verify that the 1 Rx redcap UE makes correct event-triggered reporting of inter-RAT E-UTRAN measurements when operating in standalone (SA) operation with PCell in FR1 when DRX is used. This test shall partly verify the cell search and measurement requirements in clauses 9.4A.2 and 9.4A.3. There are two test cases. In test 1 the UE shall be configured with DRX cycle of 40 ms. In test 2 the UE shall be configured with DRX cycle of 640 ms.

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. In the measurement control information from the PCell it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2..

In each test the UE shall be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore the UE shall be allocated with PUSCH resource at every DRX cycle.

Supported test configurations are shown in table A.16.6.3.3.1-1. General test parameters are provided in table A.16.6.3.3.1-2 below. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.16.6.3.3.1-3 and A.16.6.3.3.1-4, respectively.

Table A.16.6.3.3.1-1: Supported test configurations in SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

Table A.16.6.3.3.1-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

Table A.16.6.3.3.1-3: PCell specific test parameters for SA inter-RAT E-UTRA event triggered reporting in DRX with PCell in FR1

Table A.16.6.3.3.1-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

## A.16.6.3.3.2Test Requirements

In test 1, the UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 3.84 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

In test 2, the UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 12.8 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.3.4SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for 2 Rx UE

## A.16.6.3.4.1Test purpose and Environment

The purpose of this set of tests is to verify that the 2 Rx redcap UE makes correct event-triggered reporting of inter-RAT E-UTRAN measurements when operating in standalone (SA) operation with PCell in FR1 when DRX is used. This test shall partly verify the cell search and measurement requirements in clauses 9.4A.2 and 9.4A.3. There are two test cases. In test 1 the UE shall be configured with DRX cycle of 40 ms. In test 2 the UE shall be configured with DRX cycle of 640 ms.

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN inter-RAT neighbour cell. In the measurement control information from the PCell it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

In each test the UE shall be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore the UE shall be allocated with PUSCH resource at every DRX cycle.

Supported test configurations are shown in table A.16.6.3.4.1-1. General test parameters are provided in table A.16.6.3.4.1-2 below. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.16.6.3.4.1-3 and A.16.6.3.4.1-4, respectively.

Table A.16.6.3.4.1-1: Supported test configurations in SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

Table A.16.6.3.4.1-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

Table A.16.6.3.4.1-3: PCell specific test parameters for SA inter-RAT E-UTRA event triggered reporting in DRX with PCell in FR1

Table A.16.6.3.4.1-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

## A.16.6.3.4.2Test Requirements

In test 1, the UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 3.84 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

In test 2, the UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 12.8 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.4L1-RSRP measurement for beam reporting

## A.16.6.4.1SSB based L1-RSRP measurement when DRX is not used for 1 Rx UE

## A.16.6.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.1, with the testing configurations for NR cells in table A.16.6.4.1.1-1.

Table A.16.6.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.16.6.4.1.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.16.6.4.1.2-1 and table A.16.6.4.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.16.6.4.1.2-1: General test parameters

Table A.16.6.4.1.2-2: SSB specific test parameters

## A.16.6.4.1.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.4.2SSB based L1-RSRP measurement when DRX is not used for 2 Rx UE

## A.16.6.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.1, with the testing configurations for NR cells in table A.16.6.4.2.1-1.

Table A.16.6.4.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.16.6.4.2.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.16.6.4.2.2-1 and table A.16.6.4.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.16.6.4.2.2-1: General test parameters

Table A.16.6.4.2.2-2: SSB specific test parameters

## A.16.6.4.2.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.4.3SSB based L1-RSRP measurement when DRX is used for 1 Rx UE

## A.16.6.4.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.1, with the testing configurations for NR cells in table A.16.6.4.3.1-1.

Table A.16.6.4.3.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.16.6.4.3.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.16.6.4.3.2-1 and table A.16.6.4.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.16.6.4.3.2-1: General test parameters

Table A.16.6.4.3.2-2: SSB specific test parameters

## A.16.6.4.3.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.4.4SSB based L1-RSRP measurement when DRX is used for 2 Rx UE

## A.16.6.4.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.1, with the testing configurations for NR cells in table A.16.6.4.4.1-1.

Table A.16.6.4.4.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.16.6.4.4.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.16.6.4.4.2-1 and table A.16.6.4.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.16.6.4.34.2-1: General test parameters

Table A.16.6.4.34.2-2: SSB specific test parameters

## A.16.6.4.4.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.4.5CSI-RS based L1-RSRP measurement when DRX is not used for 1 Rx UE

## A.16.6.4.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.2, with the testing configurations for NR cells in table A.16.6.4.5.1-1.

Table A.16.6.4.5.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.16.6.4.5.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.16.6.4.5.2-1 and table A.16.6.4.5.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (0 for Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.16.6.4.5.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.16.6.4.5.2-1: General test parameters

Table A.16.6.4.5.2-2: CSI-RS specific test parameters

## A.16.6.4.5.3Test Requirements

After 80 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8 from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.19.2.1 and relative accuracy requirement in clause 10.1.19.2.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.4.6CSI-RS based L1-RSRP measurement when DRX is not used for 2 Rx UE

## A.16.6.4.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.2, with the testing configurations for NR cells in table A.16.6.4.6.1-1.

Table A.16.6.4.6.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.16.6.4.6.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.16.6.4.6.2-1 and table A.16.6.4.6.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (0 for Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.16.6.4.6.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.16.6.4.6.2-1: General test parameters

Table A.16.6.4.6.2-2: CSI-RS specific test parameters

## A.16.6.4.6.3Test Requirements

After 80 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8 from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.19.2.1 and relative accuracy requirement in clause 10.1.19.2.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.4.7CSI-RS based L1-RSRP measurement when DRX is used for 1 Rx UE

## A.16.6.4.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.2, with the testing configurations for NR cells in table A.16.6.4.7.1-1.

Table A.16.6.4.7.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.16.6.4.7.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.16.6.4.7.2-1 and table A.16.6.4.7.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (0 for Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.16.6.4.7.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.16.6.4.7.2-1: General test parameters

Table A.16.6.4.7.2-2: CSI-RS specific test parameters

## A.16.6.4.7.3Test Requirements

After 80 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8 from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.19.2.1 and relative accuracy requirement in clause 10.1.19.2.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.4.8CSI-RS based L1-RSRP measurement when DRX is used for 2 Rx UE

## A.16.6.4.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.2, with the testing configurations for NR cells in table A.16.6.4.8.1-1.

Table A.16.6.4.8.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.16.6.4.8.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.16.6.4.8.2-1 and table A.16.6.4.8.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (0 for Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.16.6.4.8.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.16.6.4.8.2-1: General test parameters

Table A.16.6.4.8.2-2: CSI-RS specific test parameters

## A.16.6.4.8.3Test Requirements

After 80 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8 from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.19.2.1 and relative accuracy requirement in clause 10.1.19.2.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.16.6.5NR measurements with autonomous gaps

## A.16.6.5.1SA intra-frequency CGI identification of NR neighbor cell in FR1 for 1 Rx UE

## A.16.6.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of intra-frequency CGI identification of an NR neighbour cell in FR1 with autonomous gaps. This test shall partly verify the measurement requirements in clause 9.11A.

## A.16.6.5.1.2Test Parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the FR1 PCell and Cell 2 is an FR1 neighbour cell on the same frequency as the PCell. The test parameters for PCell and neighbour cell are given in table A.16.6.5.1.2-1, A.16.6.5.1.2-2 and A.16.6.5.1.2-3 below. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable.  A measurement object is configured for the frequency of the PCell and it is indicated to the UE that event-triggered reporting with Event A3 is used. The UE is expected to detect and send a measurement report with Event A3.

A new RRC message triggering CGI identification shall be sent to the UE during period T2, after the UE has reported Event A3. The RRC message shall create a measurement report configuration with purpose reportCGI and useAutonomousGaps set to setup. The start of T3 is the instant when the last TTI containing the RRC message implying CGI identification is sent to the UE.

The test equipment verifies that potential interruption is carried out correctly by monitoring ACK/NACK sent in PCell during T3 until a measurement report with CGI is sent.

Table A.16.6.5.1.2-1: Supported test configurations

Table A.16.6.5.1.2-2: General test parameters for SA intra-frequency CGI identification of NR neighbor cell in FR1

Table A.16.6.5.1.2-3: NR Cell specific test parameters for SA intra-frequency CGI identification of NR neighbor cell in FR1

## A.16.6.5.1.3Test Requirements

The UE shall send a measurement report containing the CGI of Cell 2 within 375 ms from the start of time period T3.

Test requirement = RRC Procedure delay + Tidentify_CGI_redcap + reporting delay

-= 10 + 360 + 2 ms from the start of T3

-= 372 ms, allow 375 ms

The UE shall be scheduled continuously throughout the test. From the start of T3 until 372 ms, the interruption on PCell shall not be more than the values specified for SA in clause 9.11A.4.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.6.5.2SA intra-frequency CGI identification of NR neighbor cell in FR1 for 2 Rx UE

## A.16.6.5.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of intra-frequency CGI identification of an NR neighbour cell in FR1 with autonomous gaps. This test shall partly verify the measurement requirements in clause 9.11A.

## A.16.6.5.2.2Test Parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the FR1 PCell and Cell 2 is an FR1 neighbour cell on the same frequency as the PCell. The test parameters for PCell and neighbour cell are given in table A.16.6.5.2.2-1, A.16.6.5.2.2-2 and A.16.6.5.2.2-3 below. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable.  A measurement object is configured for the frequency of the PCell and it is indicated to the UE that event-triggered reporting with Event A3 is used. The UE is expected to detect and send a measurement report with Event A3.

A new RRC message triggering CGI identification shall be sent to the UE during period T2, after the UE has reported Event A3. The RRC message shall create a measurement report configuration with purpose reportCGI and useAutonomousGaps set to setup. The start of T3 is the instant when the last TTI containing the RRC message implying CGI identification is sent to the UE.

The test equipment verifies that potential interruption is carried out correctly by monitoring ACK/NACK sent in PCell during T3 until a measurement report with CGI is sent.

Table A.16.6.5.2.2-1: Supported test configurations

Table A.16.6.5.2.2-2: General test parameters for SA intra-frequency CGI identification of NR neighbor cell in FR1

Table A.16.6.5.2.2-3: NR Cell specific test parameters for SA intra-frequency CGI identification of NR neighbor cell in FR1

## A.16.6.5.2.3Test Requirements

The UE shall send a measurement report containing the CGI of Cell 2 within 255 ms from the start of time period T3.

Test requirement = RRC Procedure delay + Tidentify_CGI + reporting delay

-= 10 + 240 + 2 ms from the start of T3

-= 252 ms, allow 255 ms

The UE shall be scheduled continuously throughout the test. From the start of T3 until 252 ms, the interruption on PCell shall not be more than the values specified for SA in clause 9.11A.4.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.16.6.5.3Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA for 1 Rx UE

## A.16.6.5.3.1Test Purpose and Environment

This test is to verify the requirement for identification of a new CGI of E-UTRA cell with autonomous gaps in NR SA in clause 9.4A.4.

The test scenario comprises of one NR carrier and an E-UTRA carrier and two cells as given in tables A.16.6.5.3.1-1, A.16.6.5.3.1-2, A.16.6.5.3.1-3 and A.16.6.5.3.1-4. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would have ACK/NACK sending during identifying a new CGI of E-UTRAN cell. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report.

A RRC message implying SI reading shall be sent to the UE during period T2, after the UE has reported Event B2. The RRC message shall create a measurement report configuration with purpose reportCGI and useAutonomousGaps set to setup. The start of T3 is the instant when the last TTI containing the RRC message implying SI reading is sent to the UE.

Table A.16.6.5.3.1-1: Supported test configurations of inter-RAT E-UTRAN cell using autonomous gap in SA

Table A.16.6.5.3.1-2: General test parameters for identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA

Table A.16.6.5.3.1-3: PCell specific test parameters for identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR

Table A.16.6.5.3.1-4: Cell specific test parameters for inter-RAT E-UTRAN cell for identification of a new CGI of E-UTRA cell using autonomous gaps

## A.16.6.5.3.2Test Requirements

The UE shall transmit a measurement report containing the cell global identifier of Cell 2 within 240 milliseconds from the start of T3.

Test requirement = RRC Procedure delay with additional margin + Tidentify_CGI_LC-UE + TTI insertion uncertainty

= 15 + 30 + 190 + 2 ms from the start of T3

= 237 ms, allow 240 ms.

-The UE shall be scheduled continuously throughout the test, and from the start of T3 until 240 ms at least the number of ACK/NACK specified in NOTE 2 shall be detected as being transmitted by the UE.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE 1:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

NOTE 2:The overall ACK/NACK number is caused by two parts. Firstly, at least X ACK/NACK shall be sent during identifying the cell global identifier of Cell 2, where X is defined in table 9.4A.4.3-1. Secondly, given that continuous DL data allocation, additional 43, 14 and 34 ACK/NACK shall be sent for FDD 15 kHz, TDD 15 kHz and TDD 30 kHz, respectively, from the start of T3 until 240 ms excludes 190 ms for identifying the cell global identifier of Cell 2.

## A.16.6.5.4Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA for 2 Rx UE

## A.16.6.5.4.1Test Purpose and Environment

This test is to verify the requirement for identification of a new CGI of E-UTRA cell with autonomous gaps in NR SA in clause 9.4A.4.

The test scenario comprises of one NR carrier and an E-UTRA carrier and two cells as given in tables A.16.6.5.4.1-1, A.16.6.5.4.1-2, A.16.6.5.4.1-3 and A.16.6.5.4.1-4. PDCCHs indicating new transmissions shall be sent continuously to ensure that the UE would have ACK/NACK sending during identifying a new CGI of E-UTRAN cell. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report.

A RRC message implying SI reading shall be sent to the UE during period T2, after the UE has reported Event B2. The RRC message shall create a measurement report configuration with purpose reportCGI and useAutonomousGaps set to setup. The start of T3 is the instant when the last TTI containing the RRC message implying SI reading is sent to the UE.

Table A.16.6.5.4.1-1: Supported test configurations of inter-RAT E-UTRAN cell using autonomous gap in SA

Table A.16.6.5.4.1-2: General test parameters for identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA

Table A.16.6.5.4.1-3: PCell specific test parameters for identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR

Table A.16.6.5.4.1-4: Cell specific test parameters for inter-RAT E-UTRAN cell for identification of a new CGI of E-UTRA cell using autonomous gaps

## A.16.6.5.4.2Test Requirements

The UE shall transmit a measurement report containing the cell global identifier of Cell 2 within 200 milliseconds from the start of T3.

Test requirement = RRC Procedure delay with additional margin + Tidentify_CGI,E-UTRAN + TTI insertion uncertainty

= 15 + 30 + 150 + 2 ms from the start of T3

= 197 ms, allow 200 ms.

-The UE shall be scheduled continuously throughout the test, and from the start of T3 until 200 ms at least the number of ACK/NACK specified in NOTE 2 shall be detected as being transmitted by the UE.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE 1:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

NOTE 2:The overall ACK/NACK number is caused by two parts. Firstly, at least X ACK/NACK shall be sent during identifying the cell global identifier of Cell 2, where X is defined in table 9.4A.4.3-1. Secondly, given that continuous DL data allocation, additional 43, 14 and 34 ACK/NACK shall be sent for FDD 15 kHz, TDD 15 kHz and TDD 30 kHz, respectively, from the start of T3 until 200 ms excludes 150 ms for identifying the cell global identifier of Cell 2.

## A.16.6.6RSTD Measurements

## A.16.6.6.1NR RSTD measurement reporting delay test case for RedCap UE without FH in FR1 SA

## A.16.6.6.1.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC CONNECTED state meets the requirements specified in clause 9.9A.2 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.16.6.6.1.1-1.

Table A.16.6.6.1.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and NR-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the RedCap UE during T1. The measurement reporting delay test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request. The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #0 before T2.

The general test parameters are listed in table A.16.6.6.1.1-2, and cell specific test parameters are listed in table A.16.6.6.1.1-3.

Table A.16.6.6.1.1-2: General test parameters for RSTD measurement reporting delay

Table A.16.6.6.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.16.6.6.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.16.6.6.1.2Test Requirements

The RSTD measurement time without FH for RedCap fulfils the requirements specified in clause 9.9A.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 9.9A.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD1970049.

## A.16.6.6.2NR RSTD measurement reporting delay test case with PRS frequency hopping

## A.16.6.6.2.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 9.9A.2.6 in an environment with AWGN propagation conditions in FR1 in standalone scenario when frequency hopping is configured.

The supported test configurations are specified in table A.16.6.6.2.1-1.

Table A.16.6.6.2.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The test requirements apply when frequencyHopping is configured to UE.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #0 before T2.

The general test parameters are listed in table A.16.6.6.2.1-2, and cell specific test parameters are listed in table A.16.6.6.2.1-3.

Table A.16.6.6.2.1-2: General test parameters for RSTD measurement reporting delay

Table A.16.6.6.2.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.16.6.6.2.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.16.6.6.2.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 9.9A.2.6.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 9.9A.2.6 starting from the beginning of time interval T2.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD1970049.

## A.16.6.7UE Rx-Tx Measurements

## A.16.6.7.1UE Rx-Tx measurement reporting delay test case for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC_CONNECTED mode

## A.16.6.7.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement without RX FH reported by the RedCap UE meets the requirements specified in clause 9.9A.4.5 in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured. The measurement reporting delay test defined in this clause is valid for both 1 Rx and 2 Rx RedCap UEs.

The supported test configurations are listed in table A.16.6.7.1.1-1.

Table A.16.6.7.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and NR-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE during T1. The measurement reporting delay test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform UE Rx-Tx time difference measurement with RX FH via NR-Multi-RTT-RequestLocationInformation or the UE is configured by the LMF to perform UE Rx-Tx time difference measurement with RX FH via NR-Multi-RTT-RequestLocationInformation but reports the UE Rx-Tx time difference measurement based on the single hop in NR-Multi-RTT-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The last TTI containing the two messages shall be provided to the RedCap UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request. The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The RedCap UE is configured with measurement gap pattern ID #0 or ID #24 before T2.

The RedCap UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.16.6.7.1.1-2 and table A.16.6.7.1.1-3, respectively.

Table A.16.6.7.1.1-2: General test parameters

Table A.16.6.7.1.1-3: Cell specific test parameters

## A.16.6.7.1.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9A.4.5.

The UE shall perform and report the UE Rx-Tx time difference measurements without RX FH for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1A.18.3.

## A.16.6.7.2UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR1 SA in RRC_CONNECTED state

## A.16.6.7.2.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement with Rx FH in RRC_CONNECTED state meets the requirements specified in clause 9.9A.4.8 in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.16.6.7.2.1-1.

Table A.16.6.7.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID #0 or ID #24 before T2.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.16.6.7.2.1-2 and table A.16.6.7.2.1-3, respectively.

Table A.16.6.7.2.1-2: General test parameters

Table A.16.6.7.2.1-3: Cell specific test parameters

## A.16.6.7.2.2Test requirements

The UE Rx-Tx time difference measurement time in RRC_CONNECTED state fulfils the requirements specified in clause 9.9A.4.8.

The RedCap UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1A.18.3.

## A.16.6.8PRS-RSRP measurements

## A.16.6.8.1PRS-RSRP measurement delay test case for single positioning frequency layer

## A.16.6.8.1.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement meets the delay requirements specified in clause 9.9A.3.5 in an environment with AWGN propagation conditions. The test is applicable to 1 Rx or 2 Rx RedCap UE.

The supported test configurations are specified in table A.16.6.8.1.1-1.

Table A.16.6.8.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. The measurement reporting delay test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform PRS-RSRP measurement with RX FH via NR-DL-AoD-RequestLocationInformation or the UE is configured by the LMF to perform PRS-RSRP measurement with RX FH but reports the PRS-RSRP measurement based on the single hop in NR-DL-AoD-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.16.6.8.1.1-2, and cell specific test parameters are listed in table A.16.6.8.1.1-3.

Table A.16.6.8.1.1-2: General test parameters

Table A.16.6.8.1.1-3: Cell specific test parameters

## A.16.6.8.1.2Test Requirements

The UE shall perform and report the PRS-RSRP measurements for Cell 1 and Cell 2, within the time limit specified in clause 9.9A.3.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time limit above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of correct events observed during repeated tests shall be at least 90%, where the reported PRS-RSRP measurement for each correct event shall be within the reporting range specified in clause 10.1A.17.3.

## A.16.6.8.2PRS-RSRP measurement delay with FH in RRC_CONNECTED state in FR1

## A.16.6.8.2.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement with FH by a RedCap UE meets the delay requirements specified in clause 9.9A.3.6 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.16.6.8.2.1-1.

Table A.16.6.8.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.16.6.8.2.1-2, and cell specific test parameters are listed in table A.16.6.8.2.1-3.

Table A.16.6.8.2.1-2: General test parameters

Table A.16.6.8.2.1-3: Cell specific test parameters

## A.16.6.8.2.2Test Requirements

The UE shall perform and report the PRS-RSRP measurements for Cell 1 and Cell 2, within the time limit specified in clause 9.9A.3.6, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time limit above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of correct events observed during repeated tests shall be at least 90%, where the reported PRS-RSRP measurement for each correct event shall be within the reporting range specified in clause 10.1A.17.3.

## A.16.6.9PRS-RSRPP Measurements

## A.16.6.9.1PRS-RSRPP measurement delay without FH in RRC_CONNECTED state in FR1

## A.16.6.9.1.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement without FH by a RedCap UE meets the delay requirements specified in clause 9.9A.5.5 in an environment with a 2-tap channel propagation condition.

The supported test configurations are specified in table A.16.6.9.1.1-1.

Table A.16.6.9.1.11: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.16.6.9.1.1-2, and cell specific test parameters are listed in table A.16.6.9.1.1-3.

Table A.16.6.9.1.1-2: General test parameters

Table A.16.6.9.1.1-3: Cell specific test parameters

## A.16.6.9.1.2Test Requirements

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2, within the time limit specified in clause 9.9A.5.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of correct events observed during repeated tests shall be at least 90%, where the reported PRS-RSRPP measurement for each correct event shall be within the reporting range specified in clause 10.1A.19.3.

## A.16.6.9.2PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR1 SA in RRC_CONNECTED state

## A.16.6.9.2.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement with Rx FH in RRC_CONNECTED state meets the delay requirements specified in clause 9.9A.5.8 in an environment with two-tap channel propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.16.6.9.2.1-1.

Table A.16.6.9.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.16.6.9.2.1-2, and cell specific test parameters are listed in table A.16.6.9.2.1-3.

Table A.16.6.9.2.1-2: General test parameters

Table A.16.6.9.2.1-3: Cell specific test parameters

## A.16.6.9.2.2Test Requirements

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2, within the time limit specified in clause 9.9A.5.8, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each cell observed during repeated tests shall be at least 90%, where the reported PRS-RSRPP measurement for each correct event shall be within the PRS-RSRPP reporting range specified in clause 10.1A.19.3, i.e., between PRS RSRPP_0 and PRS RSRPP_126.

## A.16.7Measurement Performance requirements for RedCap

## A.16.7.1SS-RSRP

## A.16.7.1.1SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE

## A.16.7.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1A.2.1 and 10.1A.2.2 for intra-frequency measurements for 1 RX RedCap UE.

## A.16.7.1.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.16.7.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.16.7.1.1.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

Table A.16.7.1.1.2-1: SS-RSRP Intra-frequency SS-RSRP supported test configurations

Table A.16.7.1.1.2-2: SS-RSRP Intra-frequency test parameters

## A.16.7.1.1.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1A.2.1 and relative requirement in clause 10.1A.2.2 for 1 RX RedCap UE.

## A.16.7.1.2SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2 RX UE

## A.16.7.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1A.2.1 and 10.1A.2.2 for intra-frequency measurements for 2 RX RedCap UE.

## A.16.7.1.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.16.7.1.2.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.16.7.1.2.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

Table A.16.7.1.2.2-1: SS-RSRP Intra-frequency SS-RSRP supported test configurations

Table A.16.7.1.2.2-2: SS-RSRP Intra-frequency test parameters

## A.16.7.1.2.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1A.2.1 and relative requirement in clause 10.1A.2.2 for 2 RX RedCap UE.

## A.16.7.1.3SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE

## A.16.7.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1A.4.1.1 and 10.1A.4.1.2 for inter-frequency measurements with the testing configurations for NR cells in table A.16.7.1.3.1-1.

Table A.16.7.1.3.1-1: Applicable NR configurations for FR1 inter-frequency SS-RSRP accuracy test

## A.16.7.1.3.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.16.7.1.3.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements is tested by using the parameters in table A.16.7.1.3.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.16.7.1.3.2-1: SS-RSRP inter-frequency test parameters

## A.16.7.1.3.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil the absolute requirement in clause 10.1A.4.1.1 and relative requirement in clause 10.1A.4.1.2.

## A.16.7.1.4SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE

## A.16.7.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1A.4.1.1 and 10.1A.4.1.2 for inter-frequency measurements with the testing configurations for NR cells in table A.16.7.1.4.1-1.

Table A.16.7.1.4.1-1: Applicable NR configurations for FR1 inter-frequency SS-RSRP accuracy test

## A.16.7.1.4.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.16.7.1.4.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements is tested by using the parameters in table A.16.7.1.4.1-1. The inter-frequency measurements are supported by a measurement gap.

Table A.16.7.1.4.2-1: SS-RSRP inter-frequency test parameters

## A.16.7.1.4.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil the absolute requirement in clause 10.1A.4.1.1 and relative requirement in clause 10.1A.4.1.2.

## A.16.7.2SS-RSRQ

## A.16.7.2.1SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE

## A.16.7.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1A.6.

## A.16.7.2.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.16.7.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.16.7.2.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.16.7.2.1.2-1: SS-RSRQ Intra-frequency SS-RSRQ supported test configurations

Table A.16.7.2.1.2-2: SS-RSRQ Intra-frequency test parameters

## A.16.7.2.1.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1A.6.

## A.16.7.2.2SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE

## A.16.7.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1A.6.

## A.16.7.2.2.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.16.7.2.2.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.16.7.2.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.16.7.2.2.2-1: SS-RSRQ Intra-frequency SS-RSRQ supported test configurations

Table A.16.7.2.2.2-2: SS-RSRQ Intra-frequency test parameters

## A.16.7.2.2.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1A.6.

## A.16.7.2.3SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE

## A.16.7.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1A.8.1.1 and 10.1A.8.1.2.

## A.16.7.2.3.2Test parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.16.7.2.3.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.16.7.2.3.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.16.7.2.3.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

Table A.16.7.2.3.2-2: SS-RSRQ Inter frequency test parameters

## A.16.7.2.3.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1A.8.1.1 and 10.1A.8.1.2.

## A.16.7.2.4SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE

## A.16.7.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1A.8.1.1 and 10.1A.8.1.2.

## A.16.7.2.4.2Test parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.16.7.2.4.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.16.7.2.4.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.16.7.2.4.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

Table A.16.7.2.4.2-2: SS-RSRQ Inter frequency test parameters

## A.16.7.2.4.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1A.8.1.1 and 10.1A.8.1.2.

## A.16.7.3SS-SINR

## A.16.7.3.1SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE

## A.16.7.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1A.10.1.

## A.16.7.3.1.2Test parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.16.7.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.16.7.3.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.16.7.3.1.2-1: SS-SINR Intra-frequency supported test configurations

Table A.16.7.3.1.2-2: SS-SINR Intra-frequency test parameters

## A.16.7.3.1.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1A.10.1.1 and 10.1A.10.1.2

## A.16.7.3.2SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE

## A.16.7.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1A.10.1.

## A.16.7.3.2.2Test parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.16.7.3.2.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.16.7.3.2.22. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.16.7.3.2.2-1: SS-SINR Intra-frequency supported test configurations

Table A.16.7.3.2.2-2: SS-SINR Intra-frequency test parameters

## A.16.7.3.3SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE

## A.16.7.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1A.12.1.

## A.16.7.3.3.2Test parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.16.7.3.3.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.16.7.3.3.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.16.7.3.3.2-1: SS-SINR Inter frequency supported test configurations

Table A.16.7.3.3.2-2: SS-SINR Inter frequency test parameters

## A.16.7.3.3.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1A.12.1.1 and 10.1A.12.1.2.

## A.16.7.3.4SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE

## A.16.7.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1A.12.1.

## A.16.7.3.4.2Test parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.16.7.3.4.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.16.7.3.4.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.16.7.3.4.2-1: Inter frequency SS-SINR supported test configurations

Table A.16.7.3.4.2-2: SS-SINR Inter frequency test parameters

## A.16.7.3.4.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1A.12.1.1 and 10.1A.12.1.2.

## A.16.7.4L1-RSRP measurement for beam reporting

## A.16.7.4.1SSB based L1-RSRP measurement for 1 Rx UE

## A.16.7.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.5B.3 and clause 10.1A.14.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.16.7.4.1.1-1.

Table A.16.7.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.16.7.4.1.2Test parameters

In this set of test cases there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.16.7.4.1.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.16.7.4.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured with one SSB resource set containing two SSB resources (SSB#0) and 1 (SSB#1). UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0.

Table A.16.7.4.1.2-1: FR1 SSB based L1-RSRP test parameters

## A.16.7.4.1.3Test Requirements

The L1-RSRP measurement accuracy for SSB resource reported by UE in L1-RSRP report (SSB#0 or SSB#1) of Cell 2 shall fulfil the requirements in clauses 10.1A.14.1.

## A.16.7.4.2SSB based L1-RSRP measurement for 2 Rx UE

## A.16.7.4.2.1Test Purpose and Environment

Test purpose and environment defined in clause A.16.7.4.1.1 apply in this clause.

## A.16.7.4.2.2Test parameters

Test parameters defined in clause A.16.7.4.1.2 apply in this clause except the antenna configuration defined in table A.16.7.4.2.2-1.

Table A.16.7.4.2.2-1: FR1 SSB based L1-RSRP test parameters

## A.16.7.4.2.3Test Requirements

The L1-RSRP measurement accuracy for SSB resource reported by UE in L1-RSRP report (SSB#0 or SSB#1) of Cell 2 shall fulfil the requirements in clauses 10.1A.14.1.

## A.16.7.4.3CSI-RS based L1-RSRP measurement on resource set with repetition off for 1 Rx UE

## A.16.7.4.3.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.5B.3 and clause 10.1A.14.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.16.7.4.3.1-1.

Table A.16.7.4.3.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.16.7.4.3.2Test parameters

In this set of test cases there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.16.7.4.3.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.16.7.4.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set containing two CSI-RS resources (CSI-RS#0 or CSI-RS#1). UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.16.7.4.3.2-1: FR1 CSI-RS based L1-RSRP test parameters

## A.16.7.4.3.3Test Requirements

The L1-RSRP measurement accuracy for CSI-RS resource reported by UE in L1-RSRP report (CSI-RS#0 or CSI-RS#1) of Cell 1 shall fulfil the requirements in clause 10.1A.14.2.

## A.16.7.4.4CSI-RS based L1-RSRP measurement on resource set with repetition off for 2 Rx UE

## A.16.7.4.4.1Test Purpose and Environment

Test purpose and environment defined in clause A.16.7.4.3.1 apply in this clause.

## A.16.7.4.4.2Test parameters

Test parameters defined in clause A.16.7.4.3.2 apply in this clause except the antenna configuration defined in table A.16.7.4.2.2-1.

Table A.16.7.4.2.2-1: FR1 SSB based L1-RSRP test parameters

## A.16.7.4.4.3Test Requirements

The L1-RSRP measurement accuracy for CSI-RS resource reported by UE in L1-RSRP report (CSI-RS#0 or CSI-RS#1) of Cell 1 shall fulfil the requirements in clause 10.1A.14.2.

## A.16.7.5E-UTRAN RSRP

## A.16.7.5.1SA: inter-RAT measurement accuracy with FR1 serving cell for 1 Rx UE

## A.16.7.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the E-UTRAN RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.2A.2 for SA inter-RAT E-UTRAN RSRP measurements.

## A.16.7.5.1.2Test parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an E-UTRAN inter-RAT neighbour cell. Supported test configurations are shown in table A.16.7.5.1.2-1. The measurement accuracy of SA inter-RAT E-UTRAN RSRP are tested by using the parameters in A.16.7.5.1.2-2 and A.16.7.5.1.2-3.

Table A.16.7.5.1.2-1: Inter-RAT E-UTRAN RSRP supported test configurations with FR1 serving cell

Table A.16.7.5.1.2-2: NR Cell specific test parameters for SA Inter-RAT E-UTRAN RSRP test parameters

Table A.16.7.5.1.2-3: E-UTRAN Cell specific test parameters for SA Inter-RAT E-UTRAN RSRP test parameters

## A.16.7.5.1.3Test Requirements

The SA inter-RAT E-UTRAN RSRP measurement accuracy for Cell 2 shall fulfil absolute requirement in clause 9.4A.2 and 9.4A.3.

## A.16.7.5.2SA: inter-RAT measurement accuracy with FR1 serving cell for 2 Rx UE

## A.16.7.5.2.1Test Purpose and Environment

The purpose of this test is to verify that the E-UTRAN RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.2A.2 for SA inter-RAT E-UTRAN RSRP measurements.

## A.16.7.5.2.2Test parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an E-UTRAN inter-RAT neighbour cell. Supported test configurations are shown in table A.16.7.5.2.2-1. The measurement accuracy of SA inter-RAT E-UTRAN RSRP are tested by using the parameters in A.16.7.5.2.2-2 and A.16.7.5.2.2-3.

Table A.16.7.5.2.2-1: Inter-RAT E-UTRAN RSRP supported test configurations with FR1 serving cell

Table A.16.7.5.2.2-2: NR Cell specific test parameters for SA Inter-RAT E-UTRAN RSRP test parameters

Table A.16.7.5.2.2-3: E-UTRAN Cell specific test parameters for SA Inter-RAT E-UTRAN RSRP test parameters

## A.16.7.5.2.3Test Requirements

The SA inter-RAT E-UTRAN RSRP measurement accuracy for Cell 2 shall fulfil absolute requirement in clause 9.4A.2 and 9.4A.3.

## A.16.7.6E-UTRAN RSRQ

## A.16.7.6.1SA: inter-RAT measurement accuracy with FR1 serving cell for 1 Rx UE

## A.16.7.6.1.1Test Purpose and Environment

The purpose of this test is to verify that the E-UTRAN RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.2A.3 for SA inter-RAT E-UTRAN RSRQ measurements.

## A.16.7.6.1.2Test parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an E-UTRAN inter-RAT neighbour cell. Supported test configurations are shown in table A.16.7.6.1.2-1. The measurement accuracy of SA inter-RAT E-UTRAN RSRQ are tested by using the parameters in A.16.7.6.1.2-2 and A.16.7.6.1.2-3.

Table A.16.7.6.1.2-1: Inter-RAT E-UTRAN RSRQ supported test configurations with FR1 serving cell

Table A.16.7.6.1.2-2: NR Cell specific test parameters for SA Inter-RAT E-UTRAN RSRQ test parameters

Table A.16.7.6.1.2-3: E-UTRAN Cell specific test parameters for SA Inter-RAT E-UTRAN RSRQ test parameters

## A.16.7.6.1.3Test Requirements

The SA inter-RAT E-UTRAN RSRQ measurement accuracy for Cell 2 shall fulfil absolute requirement in clause 10.2A.3.

## A.16.7.6.2SA: inter-RAT measurement accuracy with FR1 serving cell for 2 Rx UE

## A.16.7.6.2.1Test Purpose and Environment

The purpose of this test is to verify that the E-UTRAN RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.2A.3 for SA inter-RAT E-UTRAN RSRQ measurements.

## A.16.7.6.2.2Test parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell and Cell 2 is an E-UTRAN inter-RAT neighbour cell. Supported test configurations are shown in table A.16.7.6.2.2-1. The measurement accuracy of SA inter-RAT E-UTRAN RSRQ are tested by using the parameters in A.16.7.6.2.22-2 and A.16.7.6.2.2-3.

Table A.16.7.6.2.2-1: Inter-RAT E-UTRAN RSRQ supported test configurations with FR1 serving cell

Table A.16.7.6.2.2-2: NR Cell specific test parameters for SA Inter-RAT E-UTRAN RSRQ test parameters

Table A.16.7.6.2.2-3: E-UTRAN Cell specific test parameters for SA Inter-RAT E-UTRAN RSRQ test parameters

## A.16.7.6.2.3Test Requirements

The SA inter-RAT E-UTRAN RSRQ measurement accuracy for Cell 2 shall fulfil absolute requirement in clause 10.2A.3.

## A.16.7.7RSTD measurements

## A.16.7.7.1RSTD measurement accuracy test case for RedCap UE without FH

## A.16.7.7.1.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC CONNECTED state meets the accuracy requirements specified in clause 10.1A.16.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.16.7.7.1.1-1.

Table A.16.7.7.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. GP#24 is configured if UE supports MG#24, otherwise GP#0 is configured. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the RedCap UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 9.9A.2.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

Table A.16.7.7.1.1-2: RSTD accuracy test parameters

## A.16.7.7.1.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1A.16.2.

A.16.7.7.2RSTD measurement accuracy test case for RedCap UE with FH in RRC_CONNECTED state

A.16.7.7.2.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE with FH in RRC CONNECTED state meets the accuracy requirements specified in clause 10.1A.16.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.16.7.7.2.1-1.

Table A.16.7.7.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. GP#24 is configured if UE supports MG#24, otherwise GP#0 is configured. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the RedCap UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 9.9A.2.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation as specified in TS 37.355 [34], clause 6.5.12. The frequency hopping configurations are specified in clause A.3.31.

Table A.16.7.7.2.1-2: RSTD accuracy test parameters

A.16.7.7.2.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1A.16.2.

## A.16.7.8UE Rx-Tx measurements

## A.16.7.8.1UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC_CONNECTED mode

## A.16.7.8.1.1Test purpose and environment

The purpose of the test is to verify that the accuracy of the UE Rx-Tx time difference measurement without RX FH reported by the RedCap UE is within the specified limits in clause 10.1A.18.2. The test is conducted in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.16.7.8.1.1-1.

Table A.16.7.8.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE before the start of the test. The UE Rx-Tx measurement accuracy test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform UE Rx-Tx time difference measurement with RX FH via NR-Multi-RTT-RequestLocationInformation or the UE is configured by the LMF to perform UE Rx-Tx time difference measurement with RX FH via NR-Multi-RTT-RequestLocationInformation but reports the UE Rx-Tx time difference measurement based on the single hop in NR-Multi-RTT-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The UE is configured with measurement gap pattern ID #0 or ID #24 before the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.16.7.8.1.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.16.7.8.1.2-1.

Table A.16.7.8.1.2-1: UE Rx-Tx time difference measurement accuracy test parameters

## A.16.7.8.1.3Test requirements

The UE Rx-Tx time difference measurement without RX FH fulfils the UE Rx-Tx measurement accuracy requirements for AWGN propagation condition specified in the clause 10.1A.18.2.

## A.16.7.8.2SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC_CONNECTED state in FR1

## A.16.7.8.2.1 Test purpose and Environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy in RRC_CONNECTED with FH by a RedCap UE is within the specified limits. This test will verify the requirements in clause 10.1A.18.2.3 and 10.1A.18.2.4. The test is conducted in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.16.7.8.2.1-1.

Table A.16.7.8.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test. The test requirements apply when frequencyHopping is configured to UE.

The UE is configured with measurement gap pattern ID #0 or ID #24 before the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.16.7.8.2.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.16.7.8.2.2-1.

Table A.16.7.8.2.2-1: UE Rx-Tx time difference measurement accuracy test parameters

## A.16.7.8.2.3Test requirements

The UE Rx-Tx time difference measurement fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1A.18.2.3 and 10.1A.18.2.4 for both Cell 1 and Cell 2.

## A.16.7.9PRS-RSRP Measurements

## A.16.7.9.1PRS-RSRP measurement accuracy without FH in RRC_CONNECTED state in FR1

## A.16.7.9.1.1Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRP measurement in RRC_CONNECTED without FH by a RedCap UE is within the specified limits. This test will verify the requirements in clauses 10.1A.17.2.

## A.16.7.9.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.16.7.9.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in A.16.7.9.1.2-2. In all test cases, Cell 1 is the PCell. PRS RX hopping is not requested in NR-DL-AoD-RequestLocationInformation.

Table A.16.7.9.1.2-1: PRS-RSRP supported test configurations

Table A.16.7.9.1.2-2: PRS-RSRP test parameters

## A.16.7.9.1.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2.

## A.16.7.9.2PRS-RSRP measurement accuracy with FH in RRC_CONNECTED state in FR1

## A.16.7.9.2.1Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRP measurement in RRC_CONNECTED with FH by a RedCap UE is within the specified limits. This test will verify the requirements in clauses 10.1A.17.2.

## A.16.7.9.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.16.7.9.2.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in A.16.7.9.2.2-2. In all test cases, Cell 1 is the PCell. PRS RX hopping is present in NR-DL-AoD-RequestLocationInformation.

Table A.16.7.9.2.2-1: PRS-RSRP supported test configurations

Table A.16.7.9.2.2-2: PRS-RSRP test parameters

## A.16.7.9.2.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2.

## A.16.7.10PRS-RSRPP measurements

## A.16.7.10.1PRS-RSRPP measurement accuracy without FH in RRC_CONNECTED state in FR1

## A.16.7.10.1.1Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRPP measurement in RRC_CONNECTED without FH by a RedCap UE is within the specified limits. This test will verify the requirements in clauses 10.1A.19.2.

## A.16.7.10.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.16.7.10.1.2-1. Both absolute accuracy of PRS-RSRPP measurements are tested by using the parameters in A.16.7.10.1.2-2. In all test cases, Cell 1 is the PCell. PRS RX hopping is not requested in NR-DL-AoD-RequestLocationInformation.

Table A.16.7.10.1.2-1: PRS-RSRPP supported test configurations

Table A.16.7.10.1.2-2: PRS-RSRPP test parameters

## A.16.7.10.1.3Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.19.2.

## A.16.7.10.2SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_CONNECTED state in FR1

## A.16.7.10.2.1Test purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRPP measurement in RRC_CONNECTED with FH by a RedCap UE is within the specified limits. This test will verify the requirements in clauses 10.1A.19.2.

## A.16.7.10.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.16.7.10.2.2-1. Both absolute and relative accuracy of PRS-RSRPP measurements are tested by using the parameters in A.16.7.10.2.2-2. In all test cases, Cell 1 is the PCell. PRS RX hopping is requested in NR-DL-AoD-RequestLocationInformation.

Table A.16.7.10.2.2-1: PRS-RSRPP supported test configurations

Table A.16.7.10.2.2-2: PRS-RSRPP test parameters

## A.16.7.10.2.3Test requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.19.2.

## A.16.8Measurement Procedure for RedCap in RRC_INACTIVE

## A.16.8.1RSTD Measurements

## A.16.8.1.1NR RSTD measurement reporting delay test case for for RedCap UE without FH in FR1 SA in RRC_INACTIVE state

## A.16.8.1.1.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC INACTIVE state meets the requirements specified in clause 5.6A.4.5 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.16.8.1.1.1-1.

Table A.16.8.1.1.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell 3. During T2 UE shall be in RRC_INACTIVE state and all three cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the RedCap UE during T1. The measurement reporting delay test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The last TTI containing the two messages shall be provided to the RedCap UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request. The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s).

The UE is configured with DRX cycle of 1.28s.

The general test parameters are listed in table A.16.8.1.1.1-2, and cell specific test parameters are listed in table A.16.8.1.1.1-3 and table A.16.8.1.1.1-4.

Table A.16.8.1.1.1-2: General test parameters for RSTD measurement reporting delay

Table A.16.8.1.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.16.8.1.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.16.8.1.1.2Test Requirements

The RSTD measurement time without FH for RedCap fulfils the requirements specified in clause 5.6A.4.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 5.6A.4.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD1970049.

## A.16.8.1.2NR RSTD measurement reporting delay test case with PRS frequency hopping

## A.16.8.1.2.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 5.6A.4.6 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.16.8.1.2.1-1.

Table A.16.8.1.2.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell 3. During T2 UE shall be in RRC_INACTIVE state and all three cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The test requirements apply when frequencyHopping is configured to UE.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s).

The UE is configured with DRX cycle of 1.28s.

The general test parameters are listed in table A.16.8.1.2.1-2, and cell specific test parameters are listed in table A.16.8.1.2.1-3 and table A.16.8.1.2.1-4.

Table A.16.8.1.2.1-2: General test parameters for RSTD measurement reporting delay

Table A.16.8.1.2.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.16.8.1.2.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.16.8.1.2.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 5.6A.4.6.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 5.6A.4.6 starting from the beginning of time interval T2.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD1970049.

## A.16.8.1.3NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state when eDRX cycle > 10.24s for RedCap UE

## A.16.8.1.3.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement, reported by RedCap UE with 1 Rx or 2 Rx branches, meets the requirements specified in clause 5.6A.4.5 when the RedCap UE is configured with eDRX cycle longer than 10.24 s in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.16.8.1.3.1-1.

Table A.16.8.1.3.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell 3. During T2 UE shall be in RRC_INACTIVE state and all three cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.10, shall be provided to the UE during T1. The UE is configured to report positioning measurements every 20s via reportingInterval in nr-DL-TDOA-RequestLocationInformation such the value of reportingInterval is set to "ri20". The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 is not limited to PTW.

The UE is configured with eDRX cycle of 40.96 s.

The general test parameters are listed in table A.16.8.1.3.1-2, and cell specific test parameters are listed in table A.16.8.1.3.1-3 and table A.16.8.1.3.1-4.

Table A.16.8.1.3.1-2: General test parameters for RSTD measurement reporting delay

Table A.16.8.1.3.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.16.8.1.3.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.16.8.1.3.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 5.6A.4.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 5.6A.4.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during the repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in the clause 10.1A.16.3, i.e., between RSTD_000000000 and RSTD_126083073.

## A.16.8.2UE Rx-Tx Measurements

## A.16.8.2.1UE Rx-Tx measurement reporting delay test case for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC_INACTIVE mode

## A.16.8.2.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement without RX FH reported by the RedCap UE meets the requirements specified in clause 5.6A.6.5 in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured. The measurement reporting delay test defined in this clause is valid for both 1 Rx and 2 Rx RedCap UEs.

The supported test configurations are listed in table A.16.8.2.1.1-1.

Table A.16.8.2.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE. The measurement reporting delay test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform UE Rx-Tx time difference measurement with RX FH via NR-Multi-RTT-RequestLocationInformation or the UE is configured by the LMF to perform UE Rx-Tx time difference measurement with RX FH via NR-Multi-RTT-RequestLocationInformation but reports the UE Rx-Tx time difference measurement based on the single hop in NR-Multi-RTT-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The RedCap UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.16.8.2.1.1-2 and table A.16.8.2.1.1-3, respectively.

Table A.16.8.2.1.1-2: General test parameters

Table A.16.8.2.1.1-3: Cell specific test parameters

## A.16.8.2.1.2Test requirements

The UE Rx-Tx time difference measurement time in RRC_INACTIVE state fulfils the requirements specified in clause 5.6A.6.5.

The UE shall perform and report the UE Rx-Tx time difference measurements without RX FH for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1A.18.3 for both Cell 1 and Cell 2.

## A.16.8.2.2UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR1 SA in RRC_INACTIVE state

## A.16.8.2.2.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement with Rx FH in RRC_INACTIVE state meets the requirements specified in clause 5.6A.6.6 in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.16.8.2.2.1-1.

Table A.16.8.2.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE state.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.16.8.2.2.1-2 and table A.16.8.2.2.1-3 respectively.

Table A.16.8.2.2.1-2: General test parameters

Table A.16.8.2.2.1-3: Cell specific test parameters

## A.16.8.2.2.2Test requirements

The UE Rx-Tx time difference measurement time in RRC_INACTIVE state fulfils the requirements specified in clause 5.6A.6.6.

The RedCap UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10. 1A.18.3 for both Cell 1 and Cell 2.

## A.16.8.2.3.UE Rx-Tx time difference measurement for single positioning frequency layer with eDRX > 10.24s in FR1 SA

## A.16.8.2.3.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 5.6A.6.5 for UE Rx-Tx measurements in RRC_INACTIVE with eDRX. The tests are conducted under AWGN propagation condition with the UE operating in FR1 stand-alone mode and configured to perform UE Rx-Tx measurements on a single positioning frequency layer (PFL) in FR1.

The supported test configuration in listed in table A.16.8.2.3.1-1.

Table A.16.8.2.3.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. The UE shall be in RRC_CONNECTED state during T1 and in RRC_INACTIVE state during T2. Cell 1 and Cell 2 transmit PRS only during the second time interval of duration T2. Similarly, the UE is configured to transmit positioning SRS during only during the second time interval of duration T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI of the last message shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle in RRC_INACTIVE.

The general test parameters and cell specific test parameters are as given in table A.16.8.2.3.1-2 and table A.16.8.2.3.1-3, respectively.

Table A.16.8.2.3.1-2: General test parameters

Table A.16.8.2.3.1-2: Cell specific test parameters

## A.16.8.2.3.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 5.6A.6.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE 1:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

A test is considered complete after the UE has reported first set of measurement based on the configured reporting periodicity. The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1A.18.3.

## A.16.8.3PRS-RSRP Measurements

## A.16.8.3.1PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_INACTIVE

## A.16.8.3.1.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement in RRC_INACTIVE meets the delay requirements specified in clause 9.9A.3.5 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.16.8.3.1.1-1.

Table A.16.8.3.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

During T1 UE is in RRC_CONNECTED, the NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. The measurement reporting delay test in this clause is valid in the cases where the RedCap UE is either not configured by the LMF to perform PRS-RSRP measurement with RX FH via NR-DL-AoD-RequestLocationInformation or the UE is configured by the LMF to perform PRS-RSRP measurement with RX FH and reports the PRS-RSRP measurement based on the single hop in NR-DL-AoD-SignalMeasurementInformation as specified in TS 37.355 [34, clause 6.5.12]. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.16.8.3.1.1-2, and cell specific test parameters are listed in table A.16.8.3.1.1-3.

Table A.16.8.3.1.1-2: General test parameters

Table A.16.8.3.1.1-3: Cell specific test parameters

## A.16.8.3.1.2Test Requirements

The UE shall perform and report the PRS-RSRP measurements for Cell 1 and Cell 2, within the time limit specified in clause 9.9A.3.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of correct events observed during repeated tests shall be at least 90%, where the reported PRS-RSRP measurement for each correct event shall be within the reporting range specified in clause 10.1A.17.3.

## A.16.8.3.3PRS-RSRP reporting delay test case in RRC_INACTIVE state in FR1 when eDRX cycle > 10.24s

## A.16.8.3.3.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement for RedCap UE in RRC_INACTIVE with eDRX meets the delay requirements specified in clause 5.6A.3.5 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.16.8.3.3.1-1.

Table A.16.8.3.3.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

During T1 UE is in RRC_CONNECTED, the NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.16.8.3.3.1-2, and cell specific test parameters are listed in table A.16.8.3.3.1-3.

Table A.16.8.3.3.1-2: General test parameters

Table A.16.8.3.3.1-3: Cell specific test parameters

## A.16.8.3.3.2Test Requirements

The UE shall perform and report the PRS-RSRP measurements for Cell 1 and Cell 2, within the time limit specified in clause 5.6A.5.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

A test is considered complete after the UE has reported first set of measurement based on the configured reporting periodicity. The rate of correct events observed during repeated tests shall be at least 90%, where the reported PRS-RSRP measurement for each correct event shall be within the reporting range specified in clause 10.1A.17.3.

## A.16.8.4PRS-RSRPP Measurements

## A.16.8.4.1PRS-RSRPP measurement delay without FH in RRC_INACTIVE state in FR1

## A.16.8.4.1.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement without FH by a RedCap UE meets the delay requirements specified in clause 5.6A.7.5 in an environment with a 2-tap channel propagation condition.

The supported test configurations are specified in table A.16.8.4.1.1-1.

Table A.16.8.4.1.1-1: Supported test configurations

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2. During T2 UE shall be in RRC_INACTIVE state and all both cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.16.8.4.1.1-2, and cell specific test parameters are listed in table A.16.8.4.1.1-3.

Table A.16.8.4.1.1-2: General test parameters

Table A.16.8.4.1.1-3: Cell specific test parameters

A.16.8.4.1.2Test Requirements

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2, within the time limit specified in clause 5.6A.7.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of correct events observed during repeated tests shall be at least 90%, where the reported PRS-RSRPP measurement for each correct event shall be within the PRS-RSRPP reporting range specified in clause 10.1A.19.3.

## A.16.8.4.2PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR1 SA in RRC_INACTIVE state

## A.16.8.4.2.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement with Rx FH in RRC_INACTIVE state meets the delay requirements specified in clause 5.6A.7.6 in an environment with two-tap channel propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.16.8.4.2.1-1.

Table A.16.8.4.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The test requirements apply when frequencyHopping is configured to UE.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource occasion occuring T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.16.8.4.2.1-2, and cell specific test parameters are listed in table A.16.8.4.2.1-3.

Table A.16.8.4.2.1-2: General test parameters

Table A.16.8.4.2.1-3: Cell specific test parameters

## A.16.8.4.2.2Test Requirements

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2, within the time limit specified in clause 5.6A.7.6, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each cell observed during repeated tests shall be at least 90%, where the reported PRS-RSRPP measurement for each correct event shall be within the PRS-RSRPP reporting range specified in clause 10.1A.19.3, i.e., between PRS RSRPP_0 and PRS RSRPP_126.

A.16.8.4.3PRS-RSRPP reporting delay in RRC_INACTIVE with eDRX

A.16.8.4.3.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement by a RedCap UE meets the delay requirements specified in clause 5.6A.7.5 in an environment with a 2-tap channel propagation condition in RRC_INACTIVE, when configured with eDRX and without FH.

The supported test configurations are specified in table A.16.8.4.3.1-1.

Table A.16.8.4.3.1-1: Supported test configurations

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2. During T2 UE shall be in RRC_INACTIVE state and all both cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.16.8.4.3.1-2, and cell specific test parameters are listed in table A.16.8.4.3.1-3.

Table A.16.8.4.3.1-2: General test parameters

Table A.16.8.4.3.1-3: Cell specific test parameters

A.16.8.4.3.2Test Requirements

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2, within the time limit specified in clause 5.6A.7.5 with Tavailable_PRS = 1.28s, starting from the beginning of time interval T2.

NOTE 1:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2:The test is considered complete after the UE reports the first set of positioning measurements based on the configured reportingInterval.

A test is considered complete after the UE has reported first set of results based on the configured reporting periodicity. The rate of correct events observed during repeated tests shall be at least 90%, where the reported PRS-RSRPP measurement for each correct event shall be within the PRS-RSRPP reporting range specified in clause 10.1A.19.3.

## A.16.9Measurement Performance Requirements for RedCap in RRC_INACTIVE

## A.16.9.1RSTD Measurements

## A.16.9.1.1RSTD measurement accuracy test case for RedCap UE without FH in FR1 in RRC_INACTIVE state

## A.16.9.1.1.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC_INACTIVE state meets the accuracy requirements specified in clause 10.1A.16.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.16.9.1.1.1-1.

Table A.16.9.1.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The UE is configured with DRX cycle of 1.28 s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the RedCap UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 5.6A.4.5.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

Table A.16.9.1.1.1-2: RSTD accuracy test parameters

## A.16.9.1.1.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1A.16.2.

## A.16.9.1.2RSTD measurement accuracy test case for RedCap UE with FH in FR1 in RRC_INACTIVE state

## A.16.9.1.2.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE with FH in RRC_INACTIVE state meets the accuracy requirements specified in clause 10.1A.16.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.16.9.1.2.1-1.

Table A.16.9.1.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The UE is configured with DRX cycle of 1.28 s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the RedCap UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 5.6A.4.5.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation as specified in TS 37.355 [34], clause 6.5.12. The frequency hopping configurations are specified in clause A.3.31.

Table A.16.9.1.2.1-2: RSTD accuracy test parameters

## A.16.9.1.2.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1A.16.2.

## A.16.9.2UE Rx-Tx measurements

## A.16.9.2.1UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC_INACTIVE mode

## A.16.9.2.1.1Test purpose and environment

The purpose of the test is to verify that the accuracy of the UE Rx-Tx time difference measurement without RX FH reported by the RedCap UE is within the specified limits in clause 10.1A.18.2. The test is conducted in AWGN propagation condition in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.16.9.2.1.1-1.

Table A.16.9.2.1.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR1.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12, shall be provided to the UE before the start of the test. The UE Rx-Tx measurement accuracy test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform UE Rx-Tx time difference measurement with RX FH via NR-Multi-RTT-RequestLocationInformation or the UE is configured by the LMF to perform UE Rx-Tx time difference measurement with RX FH via NR-Multi-RTT-RequestLocationInformation but reports the UE Rx-Tx time difference measurement based on the single hop in NR-Multi-RTT-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The UE is configured to transmit SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.16.9.2.1.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.16.9.2.1.2-1.

Table A.16.9.2.1.2-1: UE Rx-Tx time difference measurement accuracy test parameters

## A.16.9.2.1.3Test requirements

The UE Rx-Tx time difference measurement without RX FH fulfils the UE Rx-Tx measurement absolute accuracy requirements for AWGN propagation condition specified in clause 10.1A.18.2 for both Cell 1 and Cell 2.

## A.16.9.2.2SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC_INACTIVE state in FR1

## A.16.9.2.2.1Test purpose and Environment

The purpose of this test is to verify that the UE Rx-Tx measurement accuracy in FR1 with FH by a RedCap UE in RRC_INACTIVE state is within the specified limits. This test will verify the requirements in clauses 10.1A.18.2.3 and 10.1A.18.2.4.

The supported test configurations are listed in table A.16.9.2.2.1-1.

Table A.16.9.2.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR1.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test. The test requirements apply when frequencyHopping is configured to UE.

The UE is configured to transmit SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.16.9.2.2.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.16.9.2.2.2-1.

Table A.16.9.2.2.2-1: UE Rx-Tx time difference test parameters

## A.16.9.2.2.3Test requirements

The UE Rx-Tx time difference measurement time fulfils the UE Rx-Tx measurement absolute and relative accuracy requirements specified in clause 10.1A.18.2 for both Cell 1 and Cell 2.

## A.16.9.3PRS-RSRP Measurements

## A.16.9.3.1PRS-RSRP measurement accuracy without FH in RRC_INACTIVE state in FR1

## A.16.9.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRP measurement in RRC_INACTIVE without FH by a RedCap UE is within the specified limits. This test will verify the requirements in clauses 10.1A.17.2.1 for absolute accuracy and 10.1A.17.2.1 for relative accuracy.

## A.16.9.3.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.16.9.3.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in A.16.9.3.1.2-2. In all test cases, Cell 1 is the PCell. PRS RX hopping is not requested in NR-DL-AoD-RequestLocationInformation.

Table A.16.9.3.1.2-1: PRS-RSRP supported test configurations

Table A.16.9.3.1.2-2: PRS-RSRP test parameters

## A.16.9.3.1.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2.

## A.16.9.3.2PRS-RSRP measurement accuracy with FH in RRC_INACTIVE state in FR1

## A.16.9.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRP measurement in RRC_INACTIVE with FH by a RedCap UE is within the specified limits. This test will verify the requirements in clauses 10.1A.17.2.1 for absolute accuracy and 10.1A.17.2.1 for relative accuracy.

## A.16.9.3.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.16.9.3.2.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in A.16.9.3.2.2-2. In all test cases, Cell 1 is the PCell. PRS RX hopping is present in NR-DL-AoD-RequestLocationInformation.

Table A.16.9.3.2.2-1: PRS-RSRP supported test configurations

Table A.16.9.3.2.2-2: PRS-RSRP test parameters

## A.16.9.3.2.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2.

## A.16.9.4PRS-RSRPP measurements

## A.16.9.4.1PRS-RSRPP measurement accuracy without Rx FH in RRC_INACTIVE state in FR1

## A.16.9.4.1.1Test purpose and Environment

The purpose of this test is to verify that the PRS-RSRPP measurement accuracy in FR1 without FH by a RedCap UE in RRC_INACTIVE state is within the specified limits. This test will verify the requirements in clauses 10.1A.19.2.

## A.16.9.4.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.16.9.4.1.2-1. Absolute accuracy of PRS-RSRPP measurements are tested by using the parameters in A.16.9.4.1.2-2. In all test cases, Cell 1 is the PCell, and PRS RX hopping is not requested in NR-DL-AoD-RequestLocationInformation.

Table A.16.9.4.1.2-1: PRS-RSRPP supported test configurations

Table A.16.9.4.1.2-2: PRS-RSRPP test parameters

## A.16.9.4.1.3Test requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.19.2.

## A.16.9.4.2SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_INACTIVE state in FR1

## A.16.9.4.2.1Test purpose and Environment

The purpose of this test is to verify that the PRS-RSRPP measurement accuracy in FR1 with FH by a RedCap UE in RRC_INACTIVE state is within the specified limits. This test will verify the requirements in clauses 10.1A.19.2.

## A.16.9.4.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.16.9.4.2.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in A.16.9.4.2.2-2. In all test cases, Cell 1 is the PCell, and PRS RX hopping is requested in NR-DL-AoD-RequestLocationInformation.

Table A.16.9.4.2.2-1: PRS-RSRPP supported test configurations

Table A.16.9.4.2.2-2: PRS-RSRPP test parameters

## A.16.9.4.2.3Test requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.19.2.

## A.16.10Measurement procedure for RedCap in RRC_IDLE

## A.16.10.1RSTD measurements

## A.16.10.1.1NR RSTD measurement reporting delay test case for RedCap UE without FH in FR1 SA in RRC_IDLE state without eDRX

## A.16.10.1.1.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC IDLE state and without eDRX meets the requirements specified in clause 4.6.2.5 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.16.10.1.1.1-1.

Table A.16.10.1.1.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell 3. During T2 UE shall be in RRC_IDLE state and all three cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the RedCap UE during T1. The measurement reporting delay test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The last TTI containing the two messages shall be provided to the RedCap UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request. The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s).

The UE is configured with DRX cycle of 1.28 s.

The general test parameters are listed in table A.16.10.1.1.1-2, and cell specific test parameters are listed in table A.16.10.1.1.1-3 and table A.16.10.1.1.1-4.

Table A.16.10.1.1.1-2: General test parameters for RSTD measurement reporting delay

Table A.16.10.1.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.16.10.1.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.16.10.1.1.2Test Requirements

The RSTD measurement time without FH for RedCap fulfils the requirements specified in clause 4.6.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 4.6.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD1970049.

## A.16.10.1.2NR RSTD measurement reporting delay test case for RedCap UE without RX FH in FR1 SA in RRC_IDLE state when eDRX > 10.24s

## A.16.10.1.2.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement, reported by RedCap UE with 1 Rx or 2 Rx branches, meets the requirements specified in clause 4.6.2.5 when the RedCap UE is configured with eDRX cycle longer than 10.24 s in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.16.10.1.2.1-1.

Table A.16.10.1.2.1-1: Supported test configurations

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All 3 cells are on the same RF channel in FR1.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell 3. During T2 UE shall be in RRC_IDLE state and all three cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

NOTE: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.10, shall be provided to the UE during T1. The UE is configured to report positioning measurements every 20s by setting the value of reportingInterval to "ri20" in nr-DL-TDOA-RequestLocationInformation. The UE is not configured by the LMF to perform RSTD measurement with RX FH in NR-DL-TDOA-RequestLocationInformation. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 is not limited to PTW.

The UE is configured with eDRX cycle of 40.96 s.

The general test parameters are listed in table A.16.10.1.2.1-2, and cell specific test parameters are listed in table A.16.10.1.2.1-3 and table A.16.10.1.2.1-4.

Table A.16.10.1.2.1-2: General test parameters for RSTD measurement reporting delay

Table A.16.10.1.2.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.16.10.1.2.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.16.10.1.2.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 4.6.2.5. The test is considered complete after the UE reports the first set of positioning measurements based on the configured reportingInterval.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 4.6.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during the repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in the clause 10.1A.16.3, i.e., between RSTD_000000000 and RSTD_126083073.

## A.16.10.2PRS-RSRP Measurements

## A.16.10.2.1PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_IDLE

## A.16.10.2.1.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement without RX FH in RRC_IDLE in FR1 meets the delay requirements specified in clause 4.6.3.5 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.16.10.2.1.1-1.

Table A.16.10.2.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the DL slot next to slot #n, UE is released into RRC_IDLE. PRS RX FH is not requested in NR-DL-AoD-RequestLocationInformation.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is DT after slot #n, where DT = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.16.10.2.1.1-2, and cell specific test parameters are listed in table A.16.10.2.1.1-3.

Table A.16.10.2.1.1-2: General test parameters

Table A.16.10.2.1.1-3: Cell specific test parameters

## A.16.10.2.1.2Test Requirements

The UE shall perform and report the PRS-RSRP measurements for Cell 1 and Cell 2, within the time limit specified in clause 4.6.3.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of correct events observed during repeated tests shall be at least 90%, where the reported PRS-RSRP measurement for each correct event shall be within the reporting range specified in clause 10.1A.17.3.

## A.16.10.2.2PRS-RSRP measurement without Rx FH reporting delay test case for single positioning frequency layer in FR1 SA in RRC_IDLE state with eDRX cycle > 10.24s

## A.16.10.2.2.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement without Rx FH for RedCap UE in RRC_IDLE state with eDRX cycle > 10.24s meets the delay requirements specified in clause 4.6.3.5 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.16.10.2.2.1-1.

Table A.16.10.2.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_IDLE. PRS RX hopping is not requested in NR-DL-AoD-RequestLocationInformation.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource occasion occuring T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.16.10.2.2.1-2, and cell specific test parameters are listed in table A.16.10.2.2.1-3.

Table A.16.10.2.2.1-2: General test parameters

Table A.16.10.2.2.1-3: Cell specific test parameters

## A.16.10.2.2.2Test Requirements

The UE shall perform and report the PRS-RSRP measurements for Cell 1 and Cell 2, within the time limit specified in clause 4.6.3.5, starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

A test is considered complete after the UE has reported first set of results based on the configured reporting periodicity. The rate of the correct events for each cell observed during repeated tests shall be at least 90%, where the reported PRS-RSRP measurement for each correct event shall be within the reporting range specified in clause 10.1A.17.3.

## A.16.11Measurement Performance Requirements for RedCap in RRC_IDLE

## A.16.11.1RSTD Measurements

## A.16.11.1.1RSTD measurement accuracy test case for RedCap UE without FH in FR1 in RRC_IDLE state without eDRX

## A.16.11.1.1.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC_IDLE state and without eDRX meets the accuracy requirements specified in clause 10.1A.16.2 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.16.11.1.1.1-1.

Table A.16.11.1.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The UE is configured with DRX cycle of 1.28 s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the RedCap UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 4.6.2.5.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

Table A.16.11.1.1.1-2: RSTD accuracy test parameters

## A.16.11.1.1.2Test Requirements

The RSTD measurement accuracy shall fulfil the absolute requirement in clause 10.1A.16.2.

## A.16.11.1.2RSTD measurement accuracy test case for RedCap UE without FH in FR1 in RRC_IDLE state with eDRX > 10.24s

## A.16.11.1.2.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC_IDLE state with eDRX > 10.24s meets the accuracy requirements specified in clause 10.1A.16.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.16.11.1.2.1-1.

Table A.16.11.1.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The UE is configured with eDRX cycle of 40.96 s. The UE is configured to report positioning measurements every 20 s by setting the value of reportingInterval to "ri20" in nr-DL-TDOA-RequestLocationInformation. The NR-DL-TDOA-ProvideAssistanceData and NR-DL-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the RedCap UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 4.6.2.5.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is not configured by the LMF to perform RSTD measurement with RX FH in NR-DL-TDOA-RequestLocationInformation.

Table A.16.11.1.2.1-2: RSTD accuracy test parameters.

## A.16.11.1.2.2Test Requirements

The test is considered complete after the UE reports the first set of positioning measurements based on the configured reportingInterval. The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1A.16.2.

## A.16.11.2PRS-RSRP Measurements

## A.16.11.2.1PRS-RSRP measurement accuracy test case for RedCap UE in FR1 in RRC_IDLE state

## A.16.11.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRP measurement accuracy for 1 Rx RedCap UE and 2 Rx RedCap UE, respectively, in RRC_IDLE is within the specified limits in FR1. This test will verify the requirements in clauses 10.1.A.17.2.1 for absolute accuracy and 10.1.A.17.2.2 for relative accuracy, when the PRS-RSRP measurement is performed without RX FH.

## A.16.11.2.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.16.11.2.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in A.16.11.2.1.2-2. In all test cases, Cell 1 is the PCell.

Table A.16.11.2.1.2-1: PRS-RSRP supported test configurations

Table A.16.11.2.1.2-2: PRS-RSRP test parameters

## A.16.11.2.1.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1 when the PRS-RSRP measurement is performed without RX FH. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2 when the PRS-RSRP measurement is performed without RX FH.

## A.16.11.2.2PRS-RSRP measurement without Rx FH accuracy test case for single positioning frequency layer in FR1 SA in RRC_IDLE state with eDRX cycle > 10.24s

## A.16.11.2.2.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement without Rx FH for RedCap UE in RRC_IDLE state with eDRX cycle > 10.24s meets the accuracy requirements specified in clause 10.1A.17.2 in an environment with AWGN propagation conditions in FR1 in standalone scenario when single positioning frequency layer is configured. And both absolute and relative accuracy of PRS-RSRP measurements are tested.

The supported test configurations are specified in table A.16.11.2.2.1-1.

Table A.16.11.2.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR1. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_IDLE. PRS RX hopping is not requested in NR-DL-AoD-RequestLocationInformation.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource occasion occuring T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The general test parameters are listed in table A.16.11.2.2.1-2, and cell specific test parameters are listed in table A.16.11.2.2.1-3.

Table A.16.11.2.2.1-2: General test parameters

Table A.16.11.2.2.1-3: Cell specific test parameters

## A.16.11.2.2.2Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2.
