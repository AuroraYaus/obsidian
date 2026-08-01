---
type: spec
aliases:
  - 38.133_38133-j50_sA.17-A.18
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.17-A.18/content.md"
---
# TS 38.133 38133-j50_sA.17-A.18

## A.17NR standalone tests with one or more NR cells in FR2 for RedCap

## A.17.1SA: RRC_IDLE state mobility for RedCap

## A.17.1.1Cell re-selection to NR

## A.17.1.1.1Cell reselection to FR2 intra-frequency NR case for 2 Rx

## A.17.1.1.1.1Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements specified in clause 4.2B.2.3.

## A.17.1.1.1.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.17.1.1.1.2-1, A.17.1.1.1.2-2 and A.17.1.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.17.1.1.1.2-1: Supported test configurations

Table A.17.1.1.1.2-2: General test parameters for RedCap UE intra frequency NR cell re-selection test case

Table A.17.1.1.1.2-3: Cell specific test parameters for RedCap UE intra frequency NR cell re-selection test case in AWGN

## A.17.1.1.1.3Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2 and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration updateon Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 130 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1 and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration updateon Cell 1.

The cell re-selection delay to an already detected cell shall be less than 27 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_IntraSee Table 4.2B.2.3-1 in clause 4.2B.2.3

Tevaluate, NR_ intraSee Table 4.2B.2.3-1 in clause 4.2B.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 129.28 s, allow 130 s for the cell re-selection delay to a newly detectable cell and 26.88 s for the cell re-selection delay to an already detected cell in the test case, which we allow 27 s.

## A.17.1.1.2Cell reselection to FR2 inter-frequency NR case

## A.17.1.1.2.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements specified in clause 4.2B.2.4.

## A.17.1.1.2.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.17.1.1.2.2-1, A.17.1.1.2.2-2 and A.17.1.1.2.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.17.1.1.2.2-1: Supported test configurations

Table A.17.1.1.2.2-2: General test parameters for RedCap UE FR2 inter frequency NR cell re-selection test case

Table A.17.1.1.2.2-3: Cell specific test parameters for RedCap UE FR2 inter frequency NR cell re-selection test case in AWGN

## A.17.1.1.2.3Test Requirements

The cell reselection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 2 and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration updateon Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 87 s.

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1 and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration updateon Cell 1.

The cell re-selection delay to a lower priority cell shall be less than 27 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Thigher_priority_searchSee clause 4.2B.2.7

Tevaluate, NR_ interSee Table 4.2B.2.4-1 in clause 4.2B.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 86.88 s, allow 87 s for the cell re-selection delay to a higher priority cell and 26.88 s for the cell re-selection delay to a lower priority cell in the test case, which we allow 27 s.

## A.17.1.1.3Cell reselection to FR2 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE

## A.17.1.1.3.1Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for UE configured with stationary relaxed measurement criterion specified in clause 4.2B.2.9.2.

## A.17.1.1.3.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.17.1.1.3.2-1, A.17.1.1.3.2-2 and A.17.1.1.3.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. During T1 and T2, only criteria stationaryMobilityEvaluation is configured and fulfilled. UE has not registered with network for the tracking area containing cell2.

Table A.17.1.1.3.2-1: Supported test configurations

Table A.17.1.1.3.2-2: General test parameters for FR2 intra-frequency NR cell re-selection test case for UE fulfilling stationary criterion for 2 Rx UE

Table A.17.1.1.3.2-3: Cell specific test parameters for FR2 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling stationary mobility criterion for 2 Rx UE

## A.17.1.1.3.3Test Requirements

The cell reselection delay to an already detected cell for UE fulfilling stationary relaxed criterion is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected cell shall be less than 155 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to an already detectable cell can be expressed as: Tevaluate,NR_Intra_RedCap_Relax + TSI-NR,

Where:

Tevaluate,NR_Intra_RedCap_RelaxSee Table 4.2B.2.9.2-2 in clause 4.2B.2.9.2,

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 154.88 s, allow 155 s for the cell re-selection delay to an already detected cell for UE fulfilling stationary criterion in the test case.

## A.17.1.1.4Cell reselection to FR2 inter-frequency NR case for UE fulfilling stationary mobility relaxed measurement criterion for 2 Rx UE

## A.17.1.1.4.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for UE fulfilling stationary relaxed measurement criterion specified in clause 4.2B.2.10.2.

## A.17.1.1.4.2Test Parameters

The test scenario comprises of 2 cells (Cell 1 and Cell 2) on 2 different NR carriers respectively as given in tables A.17.1.1.4.2-1, A.17.1.1.4.2-2 and A.17.1.1.4.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. Cell 2 is of higher priority than Cell 1. The UE is configured with stationaryMobilityEvaluation criterion [2].

Table A.17.1.1.4.2-1: Supported test configurations

Table A.17.1.1.4.2-2: General test parameters for FR2 inter frequency NR cell re-selection test case for UE fulfilling stationary criterion for 2 Rx UE

Table A.17.1.1.4.2-3: Cell specific test parameters for FR2 inter frequency NR cell re-selection test case in AWGN for UE fulfilling stationary criterion for 2 Rx UE

## A.17.1.1.4.3Test Requirements

The cell reselection delay to an already detected low priority cell (Cell 1) for UE fulfilling stationary criterion is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected low priority cell, Cell 1, shall be less than 155 s.

The cell reselection delay to an already detected high priority cell (Cell 2) for UE fulfilling stationary criterion is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected high priority cell, Cell 2, shall be less than 155 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE 1:The cell re-selection delay to an already detected low priority cell can be expressed as: Tevaluate,NR_Inter_RedCap_Relax + TSI-NR

NOTE 2:The cell re-selection delay to an already detected higher priority cell can be expressed as: Tevaluate,NR_Inter_RedCap_Relax + TSI-NR

Where:

Tevaluate,NR_Inter_RedCap_RelaxSee Table 4.2B.2.10.2-2 in clause 4.2B.2.10.2

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 154.88 s, allow 155 s for the cell re-selection delay to an already detected low priority cell for UE fulfilling stationary criterion in the test case.

This gives a total of 154.88 s, allow 155 s for the cell re-selection delay to an already detected high priority cell for UE fulfilling stationary criterion in the test case.

## A.17.2SA: RRC_INACTIVE state mobility for RedCap

## A.17.2.1Configured Grant based Small Data Transmissions (CG-SDT) for RedCap

## A.17.2.1.1TA validation for CG-SDT in FR2 for RedCap

## A.17.2.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly perform TA validation for CG-SDT transmission in clause 5.2B.3. The test includes two sub-tests, Sub-test#1 for testing valid TA where UE can initiate CG-SDT transmission, and Sub-test#2 for testing invalid TA where UE does not initiate CG-SDT transmission. Sub-test#2 is only tested if Sub-test#1 is passed. For each sub-test, UE is configured with CG-SDT configurations when entering RRC Inactive state. Sub-test#1 consists of four successive time periods, with time duration of T1, T2, T3 and T4 respectively. Sub-test#2 consists of two successive time periods, with time duration of T5 and T6 respectively. There is one cell, which is the active NR cell in FR2. Figure A.17.1.1.2.1-1 shows the variation of the RSRP over the duration of Sub-test#1 and Figure A.17.1.1.2.1-2 shows the variation of the RSRP over the duration of Sub-test#2.

In Sub-test#1:

-Prior to the time point TA, the UE shall be fully synchronized to PCell (Cell 1), be registered to the cell and have entered RRC connected mode.

-Before starting the test at time point TA, test equipment configures RSRP to P0.

-At time point TB, RSRP is changed from P0 to P1.

-At time point TC which is W1 after time point TB, UE expect to receive RRC release with CG-SDT configuration and RRC status is changed to INACTIVE status.

-At time point TD, RSRP is changed from P1 to P0.

-At time point TE, RSRP is changed from P0 to P2. TE must be W2 before TF.

-Test equipment triggers UL data arrival at UE lower layer at time point TF. After time point TF, test equipment observes whether UE transmits with CG-SDT no later than TG which is W3 after TF.

-After time point TG, RRC status is changed from RRC INACTIVE to RRC CONNECTED.

In Sub-test#2:

-Prior to the time point TA, the UE shall pass Sub-test#1 and have entered RRC connected mode. Otherwise, Sub-test#2 shall not be executed.

-From time point TA to time point TD, RSRP is set to P2.

-At time point TC, which is W1 after time point TB, UE expect to receive RRC release with CG SDT configuration and RRC status is changed to INACTIVE status.

-At time point TD, RSRP is changed from P2 to P0.

-Test equipment triggers UL data arrival at UE lower layer at time point TF. TF is 3520 ms after TD. After time point TF, test equipment observes whether UE transmits with CG-SDT no later than TG which is W3 after TF.

W1 equals to 480 ms and W2 equals to 480 ms based on requirements in clause 5.2.B2.1. W3 is 1060 ms.

Table A.17.2.1.1.1-1: Supported test configurations for FR2 PCell

Table A.17.2.1.1.1-2: General test parameters for TA validation for CG-SDT in FR2

Table A.17.2.1.1.1-3: Cell specific test parameters TA validation for CG-SDT in FR2

Figure A.17.2.1.1.1-1: RSRP variation model for CG-SDT Sub-test#1

Figure A.17.2.1.1.1-2: RSRP variation model for CG-SDT Sub-test#2

## A.17.2.1.1.2Test Requirements

The UE behaviour in each test during time durations shall be as follows:

During Sub-test#1, UE shall transmit UL data with CG-SDT within 1060 ms after time point TF.

During Sub-test#2, after passing Sub-test#1, UE shall not transmit PUSCH at CG-SDT resources after TF until the end of the test at time point TG.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.2.2Cell Reselection for Positioning

## A.17.2.2.1Cell reselection to FR2 intra-frequency NR case with RRC_INACTIVE eDRX and positioning SRS

## A.17.2.2.1.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell reselection requirements specified in clause 5.6A.2.2, when a RedCap UE is in RRC_INACTIVE and configured with eDRX and to transmit SRS for positioning.

## A.17.2.2.1.2Test Parameters

The test procedure, supported test configurations, and test parameters in clause A.7.2.2.1.2 apply for this test.

## A.17.2.2.1.3Test Requirements

The test requirements in A.7.2.2.1.3 apply for this test.

## A.17.3RRC_CONNECTED state mobility for RedCap

## A.17.3.1Handover for RedCap

## A.17.3.1.1Intra-frequency handover from FR2 to FR2; unknown target cell for 2 Rx

## A.17.3.1.1.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 intra frequency handover requirements specified in clause 6.1D.1.3.

## A.17.3.1.1.2Test Parameters

Supported test configurations are shown in table A.17.3.1.1.2-1. Both handover delay and interruption length are tested by using the parameters in table A.17.3.1.1.2-2, and A.17.3.1.1.2-3.

NR shall send a RRC message implying handover to Cell 2, then UE handover to Cell 2’s intial BWP associated with CD-SSB.The test scenario comprises of carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.17.3.1.1.2-1: Intra-frequency handover from FR2 to FR2 test configurations

Table A.17.3.1.1.2-2: General test parameters Intra-frequency handover from FR2 to FR2

Table A.17.3.1.1.2-3: Cell specific test parameters for NR FR2-FR2 Intra frequency handover test case

## A.17.3.1.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 232 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 222 ms in the test. Tinterrupt is defined in clause 6.1D.1.3.

This gives a total of 232 ms.

## A.17.3.1.2Inter-frequency handover from FR2 to FR2; unknown target cell for 2 Rx

## A.17.3.1.2.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2 NCD-SSB to NR FR2 NCD-SSB inter frequency handover requirements specified in clause 6.1D.1.3.

## A.17.3.1.2.2Test Parameters

Supported test configurations are shown in table A.17.3.1.2.2-1. Both handover delay and interruption length are tested by using the parameters in table A.17.3.1.2.2-2, and A.17.3.1.2.2-3.

NR shall send a RRC message implying handover to Cell 2, then UE handover from Cell 1’s NCD-SSB to Cell 2’s specific RedCap BWP associated with NCD-SSB.The test scenario comprises of carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.17.3.1.2.2-1: Inter-frequency handover from FR2 to FR2 test configurations

Table A.17.3.1.2.2-2: General test parameters Inter-frequency handover from FR2 to FR2

Table A.17.3.1.2.2-3: Cell specific test parameters for NR FR2-FR2 Inter frequency handover test case

## A.17.3.1.2.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2052 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 2042 ms in the test. Tinterrupt is defined in clause 6.1D.1.3.

This gives a total of 2052 ms.

## A.17.3.2RRC Connection Mobility Control for RedCap

## A.17.3.2.1SA: RRC Re-establishment

## A.17.3.2.1.1Intra-frequency RRC Re-establishment in FR2

## A.17.3.2.1.1.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR2 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1B.

The test parameters are given in table A.17.3.2.1.1.1-1, table A.17.3.2.1.1.1-2 and table A.17.3.2.1.1.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure.

Table A.17.3.2.1.1.1-1: Supported test configurations

Table A.17.3.2.1.1.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR2

Table A.17.3.2.1.1.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR2

A.17.3.2.1.1.2Test Requirements

he RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR intra frequency cell shall be less than 5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 1

Tidentify_intra_NR = 3520 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 4865 ms, allow 5 s in the test case.

## A.17.3.2.1.2Inter-frequency RRC Re-establishment in FR2

## A.17.3.2.1.2.1Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR2 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1B.

The test parameters are given in table A.17.3.2.1.2.1-1, table A.17.3.2.1.2.1-2 and table A.17.3.2.1.2.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

Table A.17.3.2.1.2.1-1: Supported test configurations

Table A.17.3.2.1.2.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR2

Table A.17.3.2.1.2.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR2

A.17.3.2.1.2.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell shall be less than 6 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 2

Tidentify_intra_NR = 1600 ms

Tidentify_inter_NR = 2080 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 5025 ms, allow 6 s in the test case.

## A.17.3.2.1.3Intra-frequency RRC Re-establishment in FR2 without serving cell timing

## A.17.3.2.1.3.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR2 without serving cell timing is within the specified limits. These tests will verify the requirements in clause 6.2.1B.

The test parameters are given in table A.17.3.2.1.3.1-1, table A.17.3.2.1.3.1-2 and table A.17.3.2.1.3.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.17.3.2.1.3.1-1: Supported test configurations

Table A.17.3.2.1.3.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR2

Table A.17.3.2.1.3.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR2

## A.17.3.2.1.3.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR intra frequency cell without serving cell timing shall be less than 5 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 1

Tidentify_intra_NR = 3520 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 [2] for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 4865 ms, allow 5 s in the test case.

## A.17.3.2.2Random Access

## A.17.3.2.2.14-step RA type contention based random access test in FR2 for NR Standalone

## A.17.3.2.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2B.2 and clause 7.1A.2 in an AWGN model.

For this test one cell is used, with the configuration of Cell 1 configured as PCell in FR2. Supported test parameters are shown in table A.17.3.2.2.1.1-1. UE capable of SA with PCell in FR2 needs to be tested by using the parameters in table A.17.3.2.2.1.1-2 and table A.17.3.2.2.1.1-3.

Table A.17.3.2.2.1.1-1: Supported test configurations for contention based random access test in FR2 for NR Standalone

Table A.17.3.2.2.1.1-2: General test parameters for contention based random access test in FR2 for NR Standalone

Table A.17.3.2.2.1.1-3: OTA-related test parameters for contention based random access test in FR2 for NR Standalone

## A.17.3.2.2.1.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.17.3.2.2.1.2.1Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2.2.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.17.3.2.2.1.2.2Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.17.3.2.2.1.2.3No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 2 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.17.3.2.2.1.2.4Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2.2.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

A.17.3.2.2.1.2.5Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.17.3.2.2.1.2.6Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.17.3.2.2.1.2.7Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.17.3.2.2.24-step RA type non-contention based random access test in FR2 for NR Standalone

## A.17.3.2.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.2 and clause 7.1.2 in an AWGN model.

For this test one cell is used, with the configuration of Cell 1 configured as PCell in FR2. Supported test parameters are shown in table A.17.3.2.2.2.1-1. UE capable of SA with PCell or SCell in FR2 needs to be tested by using the parameters in table A.17.3.2.2.2.1-2 and table A.17.3.2.2.2.1-3 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2). Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

Table A.17.3.2.2.2.1-1: Supported test configurations for non-contention based random access test in FR2 for NR Standalone

Table A.17.3.2.2.2.1-2: General test parameters for non-contention based random access test in FR2 for NR Standalone

Table A.17.3.2.2.2.1-3: OTA-related test parameters for non-contention based random access test in FR2 for NR Standalone

## A.17.3.2.2.2.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.17.3.2.2.2.2.1SSB-based Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2.2.2.2.1 for SSB-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.7.3.2.2.2.2.2CSI-RS-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2.2.2.1 for CSI-RS-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with CSI-RSs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the CSI-RS configured.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the CSI-RS configured, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-OccasionList.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.17.3.2.2.2.2.3Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.17.3.2.2.2.2.4No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 2 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.17.3.2.2.32-step RA type contention based random access test in FR2 for NR Standalone

## A.17.3.2.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the 2-step RA type random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2B.2 and clause 7.1A.2 in an AWGN model.

For this test one cell is used, with the configuration of Cell 1 configured as PCell or SCell in FR2. Supported test parameters are shown in table A.17.3.2.2.3.1-1. UE capable of SA with PCell or SCell in FR2 needs to be tested by using the parameters in table A.17.3.2.2.3.1-2 and table A.17.3.2.2.3.1-3.

Table A.17.3.2.2.3.1-1: Supported test configurations for 2-step RA type contention based random access test in FR2 for NR Standalone

Table A.17.3.2.2.3.1-2: General test parameters for 2-step RA type contention based random access test in FR2 for NR Standalone

Table A.17.3.2.2.3.1-3: OTA-related test parameters for 2-step RA type contention based random access test in FR2 for NR Standalone

## A.17.3.2.2.3.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.17.3.2.2.3.2.1MsgA Transmission

To test the UE behavior specified in clause 6.2.2.3.1.1 the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured msgA-RSRP-ThresholdSSB.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first MsgA preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

A.17.3.2.2.3.2.2MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.1.2 the System Simulator shall transmit a MsgB containing a fallbackRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit MsgA with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB’s contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first MsgA PRACH shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

A.17.3.2.2.3.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.1.3 the System Simulator shall transmit a MsgB containing a fallbackRAR message and Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 2 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if no MsgB is received within the MsgB Response window.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in Clause 6.2.2.3. The power of the first MsgA PRACH shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

## A.17.3.2.2.42-step RA type non-contention based random access test in FR2 for NR Standalone

## A.17.3.2.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2B.2 and clause 7.1A.2 in an AWGN model.

For this test one cell is used, with the configuration of Cell 1 configured as PCell or SCell in FR2. Supported test parameters are shown in table A.17.3.2.2.4.1-1. UE capable of SA with PCell or SCell in FR2 needs to be tested by using the parameters in table A.17.3.2.2.4.1-2 and table A.17.3.2.2.4.1-3.

Table A.17.3.2.2.4.1-1: Supported test configurations for non-contention based random access test for 2-step RA type in FR2 for NR Standalone

Table A.17.3.2.2.4.1-2: General test parameters for non-contention based random access test for 2-step RA type in FR2 for NR Standalone

Table A.17.3.2.2.4.1-3: OTA-related test parameters for non-contention based random access test for 2-step RA type in FR2 for NR Standalone

## A.17.3.2.2.4.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.17.3.2.2.4.2.1MsgA Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2.3.2.1 for MsgA transmission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the MsgA which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the MsgA on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given first by the msgA-SSB-SharedRO-MaskIndex if configured, or next by the ra-ssb-OccasionMaskIndex if configured.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

A.17.3.2.2.4.2.2MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.2 the System Simulator shall transmit a MsgB containing a successRAR MAC subPDU corresponding to the transmitted Random Access Preamble after 3 MsgA transmissions have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB if the MsgB contains a successRAR MAC subPDU corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA transmission power if all received Random Access Response Reception has not been considered as successful.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

A.17.3.2.2.4.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.3 the System Simulator shall transmit a MsgB corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 2 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA transmission power when the backoff time expires if no MsgB is received within the MsgB Response window configured in RACH-ConfigGenericTwoStepRA.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA preamble with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1A.2.

## A.17.3.2.3SA: RRC Connection Release with Redirection

## A.17.3.2.3.1Redirection from NR in FR2 to NR in FR2

## A.17.3.2.3.1.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements specified in clause 6.2.3A.2.1.

## A.17.3.2.3.1.2Test Parameters

Supported test configurations are shown in table A.17.3.2.3.1.2-1. The time delay is tested by using the parameters in table A.17.3.2.3.1.2-2, and A.17.3.2.3.1.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.17.3.2.3.1.2-1: Redirection from NR to NR test configurations

Table A.17.3.2.3.1.2-2: General test parameters for Redirection from NR to NR test case

Table A.17.3.2.3.1.2-3: Cell specific test parameters for Redirection from NR to NR test case

## A.17.3.2.3.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 3160 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_NR = TRRC_procedure_delay + Tidentify-NR + TSI-NR + TRACH,

where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR = 1760 ms in the test.

TSI-NR = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH = 10 ms in the test.

This gives a total of 3160 ms.

## A.17.4Timing

## A.17.4.1UE transmit timing

## A.17.4.1.1NR UE Transmit Timing Test for FR2

## A.17.4.1.1.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeb and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1.2.

Supported test configurations are shown in table A.17.4.1.1.1-1.

Table A.17.4.1.1.1-1: Supported test configurations for FR2 PCell

For this test a single NR cell is used. Tables A.17.4.1.1.1-2 and A.17.4.1.1.1-2A define the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.17.4.1.1.1-3.

Table A.17.4.1.1.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.17.4.1.1.1-2A: OTA related test parameters

Table A.17.4.1.1.1-3: SRS Configuration for Timing Accuracy Test

Table A.17.4.1.1.1-4: Void

## A.17.4.1.1.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test:

1)Setup NR PCell according to parameters given in table A.17.4.1.1.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB.

a.The NTA offset value (in Tc units) is 13792

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.17.4.1.1.2-1

Table A.17.4.1.1.2-1 Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 Table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first detected path (in time) of DL SSB.  Skip this step for test 2 with DRX confiured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.17.4.2UE timer accuracy

## A.17.4.3Timing advance

## A.17.4.3.1SA FR2 timing advance adjustment accuracy

## A.17.4.3.1.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3A.

## A.17.4.3.1.2Test Parameters

Supported test configurations are shown in table A.17.4.3.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.17.4.3.1.2-2, A.17.4.3.1.2-3 and A.17.4.3.1.2-4.

In all test cases, single cell is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.17.4.3.1.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.17.4.3.1.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.17.4.3.1.2-1: Timing advance supported test configurations

Table A.17.4.3.1.2-2: General test parameters for timing advance

Table A.17.4.3.1.2-3: Cell specific test parameters for timing advance

Table A.17.4.3.1.2-3A: OTA related test parameters

Table A.17.4.3.1.2-4: Sounding Reference Symbol Configuration for timing advance

## A.17.4.3.1.3 Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k = 11.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.17.5Signaling characteristics for RedCap

## A.17.5.1Radio link Monitoring for RedCap

## A.17.5.1.1Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode

## A.17.5.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1B.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.17.5.1.1 .1-1. The test parameters are given in tables A.17.5.1.1 .1-2, A.17.5.1.1 .1-3, and A.17.5.1.1 .1-4 below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.17.5.1.1 .1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states, and Figure A.17.5.1.1 .1-2 shows the Time multiplexed downlink transmissions from each Angle of Arrival. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In addition to RLM-RS radio link monitoring using SSB index 0 and SSB index 1, the UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

Table A.17.5.1.1 .1-1: Supported test configurations for FR2 PCell

Table A.17.5.1.1 .1-2: General test parameters for FR2 out-of-sync testing in non-DRX mode

Table A.17.5.1.1 .1-3: OTA related cell specific test parameters for FR2 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode

Table A.17.5.1.1 .1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

Figure A.17.5.1.1 .1-1: SNR variation for out-of-sync testing

Figure A.17.5.1.1 .1-2: Time multiplexed downlink transmissions

## A.17.5.1.1.2Test Requirements

The UE behavior in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.5.1.2Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode

## A.17.5.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1B.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.17.5.1.2.1-1.The test parameters are given in tables A.17.5.1.2.1-2, and A.17.5.1.2.1-3 below. There is one cell (Cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.1.2.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states, and Figure A.17.5.1.2.1-2 shows the Time multiplexed downlink transmissions from each Angle of Arrival. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

Table A.17.5.1.2.1-1: Supported test configurations for FR2 PCell

Table A.17.5.1.2.1-2: General test parameters for FR2 in-sync testing in non-DRX mode

Table A.17.5.1.2.1-3: OTA related cell specific test parameters for FR2 (Cell 1) for in-sync radio link monitoring tests in non-DRX mode

Table A.17.5.1.2.1-4: Void

Figure A.17.5.1.2.1-1: SNR variation for in-sync testing

Figure A.17.5.1.2.1-2: Time multiplexed downlink transmissions

## A.17.5.1.2.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.5.1.3Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode

## A.17.5.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1B.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.17.5.1.3.1-1. The test parameters are given in tables A.17.5.1.3.1-2, and A.17.5.1.3.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.17.5.1.3.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states, and Figure A.17.5.1.3.1-2 shows the Time multiplexed downlink transmissions from each Angle of Arrival. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.17.5.1.3.1-1: Supported test configurations for FR2 PCell

Table A.17.5.1.3.1-2: General test parameters for FR2 out-of-sync testing in DRX mode

Table A.17.5.1.3.1-3: OTA related cell specific test parameters for FR2 (Cell 1) for out-of-sync radio link monitoring tests in DRX mode

Figure A.17.5.1.3.1-1: SNR variation for out-of-sync testing

Figure A.17.5.1.3.1-2: Time multiplexed downlink transmissions

## A.17.5.1.3.2Test Requirements

The UE behavior in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.5.1.4Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode

## A.17.5.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1B.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.17.5.1.4.1-1. The test parameters are given in tables A.17.5.1.4.1-2, and A.17.5.1.4.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.1.4.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.17.5.1.4.1-1: Supported test configurations for FR2 PCell

Table A.17.5.1.4.1-2: General test parameters for FR2 in-sync testing in DRX mode

Table A.17.5.1.4.1-3: OTA related cell specific test parameters for FR2 (Cell 1) for in-sync radio link monitoring test in DRX mode

Table A.17.5.1.4.1-4: Void

Table A.17.5.1.4.1-5: Void

Figure A.17.5.1.4.1-1: SNR variation for in-sync testing

## A.17.5.1.4.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.5.1.5Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode

## A.17.5.1.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used. This test will partly verify the FR2 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1B.3.

The test parameters are given in tables A.17.5.1.5.1-1, A.17.5.1.5.1-2, A.17.5.1.5.1-3 and A.17.5.1.5.1-4 below. There is one cell, Cell 1 which is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.17.5.1.5.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 10 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 and SSB1 are configured as BFD-RS.

Table A.17.5.1.5.1-1: Supported test configurations for FR2 PCell

Table A.17.5.1.5.1-2: General test parameters for FR2 PCell for CSI-RS out-of-sync testing in non-DRX mode

Table A.17.5.1.5.1-3: Cell specific test parameters for FR2 for CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.17.5.1.5.1-4: Measurement gap configuration for FR2 CSI-RS out-of-sync radio link monitoring in non-DRX mode

Figure A.17.5.1.5.1-1: SNR variation for CSI-RS out-of-sync testing

## A.17.5.1.5.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During time durations T1, T2 and T3, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 no later than time point C (D1 second after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.5.1.6Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode

## A.17.5.1.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used. This test will partly verify the FR2 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1B.3.

The test parameters are given in tables A.17.5.1.6.1-1, A.17.5.1.6.1-2 and A.17.5.1.6.1-3 below. There is one cells, Cell 1which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.1.6.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 10 ms. In the test, DRX configuration is not enabled. In the test, SSB0 and SSB1 are configured as BFD-RS.

Table A.17.5.1.6.1-1: Supported test configurations for FR2 PCell

Table A.17.5.1.6.1-2: General test parameters for FR2 PCell for CSI-RS in-sync testing in non-DRX mode

Table A.17.5.1.6.1-3: Cell specific test parameters for FR2 for CSI-RS in-sync radio link monitoring in non-DRX mode

Figure A.17.5.1.6.1-1: SNR variation for CSI-RS in-sync testing

## A.17.5.1.6.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.5.1.7Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode

## A.17.5.1.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when DRX is used. This test will partly verify the FR2 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1B.3.

The test parameters are given in tables A.17.5.1.7.1-1, A.17.5.1.7.1-2, and A.17.5.1.7.1-3 below. There is one cell, Cell 1 is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.17.5.1.7.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 10 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test. In the test, SSB0 and SSB1 are configured as BFD-RS.

Table A.17.5.1.7.1-1: Supported test configurations for FR2 PCell

Table A.17.5.1.7.1-2: General test parameters for FR2 PCell for CSI-RS out-of-sync testing in DRX mode

Table A.17.5.1.7.1-3: Cell specific test parameters for FR2 for CSI-RS out-of-sync radio link monitoring in DRX mode

Figure A.17.5.1.7.1-1: SNR variation for CSI-RS out-of-sync testing

## A.17.5.1.7.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During time durations T1, T2 and T3, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on PCell.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 (PCell) at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 (PCell) no later than time point C (D1 secondafter the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.5.1.8Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode

## A.17.5.1.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when DRX is used. This test will partly verify the FR2 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1B.

The test parameters are given in tables A.17.5.1.8.1-1, A.17.5.1.8.1-2, A.17.5.1.8.1-3 and A.17.5.1.8.1-4 below. There is one cells, Cell 1which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.1.8.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 10 ms. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 and SSB1 are configured as BFD-RS.

Table A.17.5.1.8.1-1: Supported test configurations for FR2 PSCell

Table A.17.5.1.8.1-2: General test parameters for FR2 PCell for CSI-RS in-sync testing in DRX mode

Table A.17.5.1.8.1-3: Cell specific test parameters for FR2 for CSI-RS in-sync radio link monitoring in non-DRX mode

Table A.17.5.1.8.1-4: Measurement gap configuration for FR2 CSI-RS in-sync radio link monitoring in non-DRX mode

Figure A.17.5.1.8.1-1: SNR variation for CSI-RS in-sync testing

## A.17.5.1.8.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.5.1.9UE Radio Link Monitoring Scheduling Restrictions on FR2

## A.17.5.1.9.1Test Purpose and Environment

The purpose is to verify that the NR UE correctly follows the RLM scheduling restrictions requirements defined in clause 8.1B.7. This test verifies that the UE correctly receive the PDCCH scheduled on the symbols right before the RLM SSB symbols without overlap so that it sends ACK/NACK correctly. The test case is only applicable to UE which supports pdcch-MonitoringAnyOccasions or pdcch-MonitoringAnyOccasionsWithSpanGap.

The test parameters are given in table A.17.5.1.9.1-1, table A.17.5.1.9.1-2 and table A.17.5.1.9.1-3 below. The UE is required during time period T1 to transmit ACK/NACK correctly upon scheduling of PDSCH.

Table A.17.5.1.9.1-1: Supported test configurations

Table A.17.5.1.9.1-2: General test parameters for NR RLM scheduling restriction test case in FR2

Table A.17.5.1.9.1-3: Cell specific test parameters for NR RLM scheduling restriction test case in FR2

Figure A.17.5.1.9.1-1: Time multiplexed downlink transmissions

## A.17.5.1.9.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.1B.7.3.

## A.17.5.2Beam Failure Detection and Link recovery procedures

## A.17.5.2.1Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode

## A.17.5.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5B.

The test parameters are given in tables A.17.5.2.1.1-1, A.17.5.2.1.1-2 and A.17.5.2.1.1-3 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.2.1.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.17.5.2.1.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

Table A.17.5.2.1.1-1: Supported test configurations for FR2 PCell

Table A.17.5.2.1.1-2: General test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.17.5.2.1.1-3: Cell specific test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.17.5.2.1.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.17.5.2.1.1-2: SSB_RP level variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.17.5.2.1.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 960+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.5.2.2Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in DRX mode

## A.17.5.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5.

The test parameters are given in tables A.17.5.2.2.1-1, A.17.5.2.2.1-2 and A.17.5.2.2.1-3 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.2.2.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.17.5.2.2.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.17.5.2.2.1-1: Supported test configurations for FR2 PCell

Table A.17.5.2.2.1-2: General test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.17.5.2.2.1-3: Cell specific test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Figure A.17.5.2.2.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in DRX mode

Figure A.17.5.2.2.1-2: SSB_RP level variation for SSB-based beam failure detection and link recovery testing in DRX mode

## A.17.5.2.2.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 560+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.5.2.3Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode

## A.17.5.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5B.

The test parameters are given in tables A.17.5.2.3.1-1, A.17.5.2.3.1-2, and A.17.5.2.3.1-3 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.2.3.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.17.5.2.3.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

Table A.17.5.2.3.1-1: Supported test configurations for FR2 PCell

Table A.17.5.2.3.1-2: General test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.17.5.2.3.1-3: Cell specific test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Editor notes: The Figure A.17.5.2.3.1-1 is missing

Figure A.17.5.2.3.1-1: SNR variation for CSI-RS based beam failure detection and link recovery testing in non-DRX mode

Figure A.17.5.2.3.1-2: CSI-RS_RP level variation for CSI-RS based beam failure detection and link recovery testing in non-DRX mode

## A.17.5.2.3.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.5.2.4Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode

## A.17.5.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5B.

The test parameters are given in tables A.17.5.2.4.1-1, A.17.5.2.4.1-2, A.17.5.2.4.1-3, and A.17.5.2.4.1-4 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.2.4.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.17.5.2.4.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.17.5.2.4.1-1: Supported test configurations for FR2 PCell

Table A.17.5.2.4.1-2: General test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.17.5.2.4.1-3: Cell specific test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Figure A.17.5.2.4.1-1: SNR variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Figure A.17.5.2.4.1-2: CSI-RS_RP level variation for CSI-RS based beam failure detection and link recovery testing in DRX mode

## A.17.5.2.4.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.5.2.5Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode for 2 Rx UE

## A.17.5.2.5.1Test Purpose and Environment

The purpose is to test scheduling availability restrictions when the UE is performing beam failure detection or when the UE is performing L1-RSRP measurement for candidate beam detection, when no DRX is used. This test will verify the scheduling availability restriction requirements in clause 8.5B.7 and 8.5B.8.

The test parameters are given in tables A.17.5.2.5.1-1, A.17.5.2.5.1-2 and A.17.5.2.5.1-3 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.17.5.2.5.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.17.5.2.5.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. This test will focus on the scheduling availability during beam failure detection) and candidate beam detection. In the test, DRX configuration is not enabled. Test is to test the scheduling availability restriction of UE performing beam failure detection and candidate beam detection when SSB RS configured for Beam failure detection and candidate beam detection. During the test the UE is scheduled to transmit continuously in UL.

Table A.17.5.2.5.1-1: Supported test configurations for FR2 PCell

Table A.17.5.2.5.1-2: General test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.17.5.2.5.1-3: Cell specific test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.17.5.2.5.1-1: SNR variation SSB for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.17.5.2.5.1-2: SSB_RP level variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.17.5.2.5.2Test Requirements

The UE behaviour during time duration T3 follows the requirements defined in clause 8.5B.7.3:

-The UE is not expected to transmit PUCCH/PUSCH/SRS or receive PDCCH/PDSCH/CSI-RS for tracking/CSI-RS for CQI on BFD-RS symbols to be measured for beam failure detection.

The UE behaviour during time durations T4 and T5 follows the requirements defined in clause 8.5B.8.3:

-The UE is not expected to transmit PUCCH/PUSCH or receive PDCCH/PDSCH on reference symbols to be measured for candidate beam detection.

## A.17.5.3Active BWP switch for RedCap

## A.17.5.3.1DCI-based and Timer-based Active BWP Switch

## A.17.5.3.1.1NR FR2 DL active BWP switch with non-DRX in SA

## A.17.5.3.1.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6A. Supported test configurations are shown in table A.17.5.3.1.1.1-1.

The test scenario comprises of one cell (Cell 1) as given in table A.17.5.3.1.1.1-2. Cell-specific parameters of NR PCell is specified in table A.17.5.3.1.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.17.5.3.1.1.1-4.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE is configured with 2 different UE-specific downlink bandwidth parts, BWP-1 and BWP-2 before starting the test. BWP-1 include bandwidth of the initial DL BWP and SSB.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1.

-UE is configured with a bwp-InactivityTimer timer value for Cell 1.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for DL BWP switch, sent from the test equipment to the UE, is received at the UE side in Cell 1’s slot # denoted i. The UE should switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6A and starts to report valid ACK/NACK for the Cell 1 no later than the first UL slot that occurs after the beginning of slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on Cell 1’s BWP-2 starting from the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).

During T2, the test equipment won’t transmit DCI format for PDSCH reception on Cell 1.

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the half subframe immediately after bwp-InactivityTimer timer expires. The UE should switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s DL slot (j+TBWPswitchDelay) as defined in clause 8.6A and starts to report valid ACK/NACK for the Cell 1 at latest on the first UL slot that occurs after the beginning of slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on Cell 1’s BWP-1 starting from the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

The test equipment verifies the DL BWP switch time by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK is received.

Table A.17.5.3.1.1.1-1: DL BWP switch supported test configurations

Table A.17.5.3.1.1.1-2: General test parameters for DL BWP switch in SA

Table A.17.5.3.1.1.1-3: NR Cell specific test parameters for DL BWP switch in SA

Table A.17.5.3.1.1.1-4: OTA related test parameters for DL BWP switch in SA

## A.17.5.3.1.1.2Test Requirements

During T1, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6A.2-1.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first UL slot that occurs after the beginning of DL slot (i+ TBWPswitchDelay+k1), (j+ TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

## A.17.5.3.2RRC-based Active BWP Switch

## A.17.5.3.2.1NR FR2 DL active BWP switch of PCell with non-DRX in SA

## A.17.5.3.2.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6A.3. Supported test configurations are shown in table A.17.5.3.2.1.1-1.

The test scenario comprises of one Cell (Cell 1) as given in table A.17.5.3.2.1.1-2. Cell-specific parameters of Cell 1 are specified in table A.17.5.3.2.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in Cell 1.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is received at the UE side in PSCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition.

The UE shall be able to completely receive PDSCH on Cell 1 from the first DL slot that occurs after the beginning of DL slot  as defined in clause 8.6A.3 and starts to report valid ACK/NACK for the Cell 1 from the first UL slot that occurs after the beginning of DL slot. The UE shall be continuously scheduled on PSCell’s BWP-1 starting from the first DL slot that occurs after the beginning of DL slot .i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length

TRRCprocessingDelay and TBWPswitchDelayRRC are defined in clause 8.6A.3.

The test equipment verifies the DL BWP switch time in PSCell by counting the time from the time when the RRC Reconfiguration message including updated BWP configurationis sent till the time when RRC Reconfiguration Complete message is received.

Table A.17.5.3.2.1.1-1: DL BWP switch supported test configurations

Table A.17.5.3.2.1.1-2: General test parameters for DL BWP switch in SA

Table A.17.5.3.2.1.1-3: NR Cell specific test parameters for DL BWP switch in SA

Table A.17.5.3.2.1.1-4: OTA related test parameters for BWP switching test case

## A.17.5.3.2.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PCell from the first DL slot that occurs after the beginning of slot  and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot.i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.5.4Active TCI state switch delay

## A.17.5.4.1MAC-CE based active TCI state switch

## A.17.5.4.1.1NR PCell FR2 active TCI state switch for a known TCI state

## A.17.5.4.1.1.1Test Purpose and Environment

The purpose of this test is to verify the active TCI state switch delay requirement defined in clause 8.10B.3. Supported test configuration is shown in table A.17.5.4.1.1.1-1.

The test scenario comprises of one NR PCell (Cell 1) as given in table A.17.5.4.1.1.1-2. Cell-specific parameters of NR PCell are specified in table A.17.5.4.1.1.1-3 below. The OTA related test parameters for FR2 are shown in table A.17.5.4.1.1.1-4.

PDCCHs indicating new transmissions shall be sent continuously on PCell to ensure that the UE would have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is configured with 2 different TCI states for PCell, PDCCH TCI state 0 (QCL’d to SSB0) and TCIstate 1 (QCL’d to SSB1), in Cell 1 before starting the test.

-UE is indicated in TCI state 0 as the active PDCCH TCI state

The test consists of two time periods, T1 and T2. Figure A.17.5.4.1.1.1-1 and Figure A.17.5.4.1.1.1-2 show the Time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival. During T1 only SSB to which PDCCH-TCI-state0 is QCL’d is transmitted. At the beginning of T2, the SSB corresponding to TCI state 1 starts transmitting. The UE is configured to provide periodic L1-RSRP reports. In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 and SSB1, UE receives a MAC-CE command indicating a switch to TCI state 1. tci-PresentInDCI is not configured in the PDSCH configuration, i.e. TCI state for the PDSCH is identical to the PDCCH TCI state.

The test equipment verifies that UE can be scheduled on PCell on TCI state 0 till n+ THARQ +3 ms. The test equipment also verifies the TCI state switch time in PCell by scheduling the UE on TCI state 1 after n+ THARQ +3 ms + (Tfirst-SSB + TSSB-proc).

Table A.17.5.4.1.1.1-1: Supported test configurations

Table A.17.5.4.1.1.1-2: General test parameters for TCI state switch

Table A.17.5.4.1.1.1-3: NR Cell specific test parameters for TCI state switch

Table A.17.5.4.1.1.1-4: OTA related test parameters for TCI state switch

Figure A.17.5.4.1.1.1-1: Time multiplexed downlink transmissions during T1

Figure A.17.5.4.1.1.1-2: Time multiplexed downlink transmissions during T2

## A.17.5.4.1.1.2Test Requirements

During T2, UE shall send L1-RSRP report with results for both SSB0 and SSB1.

After receiving MAC-CE command in slot n, UE shall:

-be able to continue to receive on TCI state 0 till   n+ THARQ +3 ms

-be able to start receiving on TCI state 1 after n+ THARQ +5 ms + Tfirst-SSB

## A.17.5.4.2RRC based active TCI state switch

## A.17.5.4.2.1NR PCell FR2 active TCI state switch for a known TCI state

## A.17.5.4.2.1.1Test Purpose and Environment

The purpose of this test is to verify the active TCI state switch delay requirement defined in clause 8.10B.5. Supported test configuration is shown in table A.17.5.4.2.1.1-1.

The test scenario comprises of one NR PCell as given in table A.17.5.4.2.1.1-2. Cell-specific parameters of NR PCell is specified in table A.17.5.4.2.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.17.5.4.2.1.1-4.

PDCCHs indicating new transmissions shall be sent continuously on PCell to ensure that the UE would have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is configured with 1 TCI state for PCell, PDCCH-TCI-state0 (QCL’d to SSB0)

-UE is indicated in TCI state0 as the active TCI state

The test consists of two time periods, T1 and T2. Figure A.17.5.4.2.1.1-1-1 and Figure A.17.5.4.2.1.1-1-2 show the Time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival. During T1 only SSB to which TCI-state0 is QCL’d is transmitted. At the beginning of T2, the SSB corresponding to TCI-state1 starts transmitting. The UE is configured to provide periodic L1-RSRP reports.  In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 and SSB1, UE receives a RRC command indicating a switch to TCI-state1.

The test equipment verifies the TCI state switch time in PCell by scheduling the UE on TCI state 1 after n+ TRRC_processing  + Tfirst-SSB + 2 ms.

Table A.17.5.4.2.1.1-1-1: Supported test configurations

Table A.17.5.4.2.1.1-1-2: General test parameters for TCI state switch

Table A.17.5.4.2.1.1-1-3: NR Cell specific test parameters for TCI state switch

Table A.17.5.4.2.1.1-1-4: OTA related test parameters for TCI state switch

Figure A.17.5.4.2.1.1-1-1: Time multiplexed downlink transmissions during T1

Figure A.17.5.4.2.1.1-1-2: Time multiplexed downlink transmissions during T2

## A.17.5.4.2.1.2Test Requirements

During T2, UE shall send L1-RSRP report with both SSB0 and SSB1.

After receiving RRC command in slot n, UE shall be able to start receiving on TCI state 1 after n+ TRRC_processing  + Tfirst-SSB + 2 ms.

## A.17.5.5Uplink spatial relation switch delay

## A.17.5.5.1MAC-CE based Spatial Relation switch

## A.17.5.5.1.1NR PCell FR2 spatial relation associated with known DL-RS

## A.17.5.5.1.1.1Test Purpose and Environment

The purpose of this test is to verify fulfillment of the uplink spatial relation switch delay requirement defined in clause 8.12A.3 by a UE capable of beam correspondence without the need for UL beam sweeping. The supported test configurations are shown in table A.17.5.5.1.1.1-1.

The test scenario comprises one PCell (Cell 1) as outlined in table A.17.5.5.1.1.1-2. Cell-specific parameters are provided in table A.17.5.5.1.1.1-3. OTA-related test parameters are provided in table A.17.5.5.1.1.1-4.

Throughout the test, PDCCH indicating new transmissions shall ge sent continuously on PCell to ensure that the UE will send ACK/NACKs on PUCCH.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE is configured with a single TCI state, TCI State-0, which is QCLed with SSB0.

-UE is configured with two spatial relation information configurations Spatial Relation Info-0 and Spatial Relation Info-1 for PUCCH, each associated with SSB0 and SSB1, respectively.

-UE is indicated via MAC-CE activation of PUCCH-SpatialRelationInfoId corresponding to Spatial Relation Info-0

-UE is configured with a CSI measurement configuration indicating L1-RSRP measurements on SSB0 and SSB1 with periodic reporting. The L1-RSRP measurement period is influenced by the following: the higher layer parameter timeRestrictionForChannelMeasurement is configured, measured SSBs are fully overlapping with SMTC window, and there are no conflicts with measurement gaps.

The test consists of two time periods, T1 and T2. During T1 only the SSB associated with PDCCH TCI state-0 and PUCCH Spatial Relation Info-0 is transmitted. At the beginning of T2, transmission of the SSB associated with PUCCH Spatial Relation Info-1 starts. The UE conducts periodic L1-RSRP measurements and SSB-Index-RSRP reporting for SSB0 and SSB1. In slot n, which is within 1280 ms after UE receiving both SSB0 and SSB1, and after reporting valid results for both the SSB0 and the SSB1, the UE receives a MAC-CE indicating a switch of spatial relation to PUCCH Spatial Relation Info 1.

The test equipment verifies that the UE transmits according to PUCCH Spatial Relation Info 0 up until slot n + THARQ/NR slot length + , and according to PUCCH Spatial Relation Info 1 from slot n + THARQ/NR slot length +  + 1 and onwards.3Nslotsubframe,µ3Nslotsubframe,µ

Table A.17.5.5.1.1.1-1: Supported test configurations

Table A.17.5.5.1.1.1-2: General test parameters

A.17.5.5.1.1.1: NR Cell specific test parameters

Table A.17.5.5.1.1.1-4: OTA related test parameters

## A.17.5.5.1.1.2Test Requirements

During T2, the UE shall send L1-RSRP report with results for SSB0 and SSB1.

After receiving MAC-CE command in slot n, the UE shall:

-Continue transmitting using PUCCH spatial relation associated with SSB0 up to and including slot n + THARQ/NR slot length + 3Nslotsubframe,µ

-Start transmitting using PUCCH spatial relation associated with SSB1 from slot n + THARQ/NR slot length +  + 1 and onwards.3Nslotsubframe,µ

The rate of correct events observed during repeated tests shall be at least [90]%.

## A.17.5.5.2RRC based spatial relation switch

## A.17.5.5.2.1NR PCell FR2 spatial relation switch associated with a known DL-RS

A.17.5.5.2.1.1Test Purpose and Environment

The purpose of this test is to verify the RRC based spatial relation switch delay requirement defined in clause 8.12A.5 by a UE capable of beam correspondence without the need for UL beam sweeping. In the test the higher layer parameter timeRestrictionForChannelMeasurements is configured. Supported test configuration is shown in table A.17.5.5.2.1.1-1.

The test scenario comprises of one PCell (Cell 1) as given in table A.17.5.5.2.1.1-2. Cell-specific parameters of PCell is specified in table A.17.5.5.2.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.17.5.5.2.1.1-4.

Periodic SRS is transmitted on PCell (Cell 1), and the SRS configuration is SRSConf.1 given in table A.5.4.1.1.1-3.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is configured with 1 SRS-SpatialRelation0 associated with SSB0.

-UE is indicated SRS-SpatialRelation0 as the active SRS spatial relation.

The test consists of two time periods, T1 and T2. During T1 only SSB0 to which SRS-SpatialRelation0 associated is transmitted. UE shall transmit periodic SRS with SRS-SpatialRelation0 on the UL of the PCell.

T2 start when the tester initiates transmission of SSB1 corresponding to SRS-SpatialRelation1. The UE is configured to transmit periodic L1-RSRP reports.

In slot n, which is within [1280]ms of UE providing the L1-RSRP report with results for both SSB0 and SSB1, the UE receives an RRC command indicating a switch to transmit periodic SRS with target SRS-SpatialRelation1. The UE shall be able to transmit periodic SRS with target spatial relation (SRS-SpatialRelation1) on PCell in slot n + TRRC_processing/NR slot length +1.

Table A.17.5.5.2.1.1-1: Supported test configurations

Table A.17.5.5.2.1.1-2: General test parameters for spatial relation switch associated with a known DL-RS

Table A.17.5.5.2.1.1-3: NR Cell specific test parameters for spatial relation switch associated with a known DL-RS

Table A.17.5.5.2.1.1-4: OTA related test parameters for spatial relation switch associated with a known DL-RS

## A.17.5.5.2.1.2Test Requirements

During T1 UE shall send L1-RSRP report with SSB0 to which SRS-SpatialRelation0 is associated. During T2, UE shall send L1-RSRP report with SSB1 to which SRS-SpatialRelation1 is associated.

After receiving RRC command in slot n, UE shall be able to transmit target periodic SRS with SRS-SpatialRelation1 on the PCell in the slot n +  TRRC_processing/NR slot length + 1.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.5.6UE specific CBW change

## A.17.5.6.1NR FR2 UE specific CBW change of PCell with non-DRX in SA

## A.17.5.6.1.1Test Purpose and Environment

The purpose of this test is to verify the UE specific CBW change delay requirement defined in clause 8.13A. Supported test configurations are shown in table A.17.5.6.1.1-1.

The test scenario comprises of one PCell (Cell 1) as given in table A.17.5.6.1.1-2. Cell-specific parameters of PCell are specified in table A.17.5.6.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK transmission.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1 (PCell).

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PCell.

-UE has been configured with UE-specific CBW (CBW-1)

-UE is indicated in SCS-SpecificCarrier [2] that the UE-specific CBW is CBW-1 as the initial condition in Cell 1 (PCell).

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated CBW configuration, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its CBW with the updated CBW of final condition.

The UE shall be able to completely receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot  as defined in clause 8.13.2 and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot. The UE shall be continuously scheduled on PCell’s new CBW starting from the first DL slot that occurs after the beginning of DL slot .i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length+k1i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length

TRRCprocessingDelay and TCBWchangeDelayRRC are defined in clause 8.13A.

The test equipment verifies the UE specific CBW switch time in PCell by counting the time from the time when the RRC Reconfiguration message including updated CBW configurations sent till the time when RRC Reconfiguration Complete message is received.

Table A.17.5.6.1.1-1: UE specific CBW change supported test configurations

Table A.17.5.6.1.1-2: General test parameters for UE specific CBW change in NR SA

Table A.17.5.6.1.1-3: NR Cell specific test parameters for UE specific CBW change in NR SA

Table A.17.5.6.1.1-4: OTA related test parameters for UE specific CBW change test case

## A.17.5.6.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PCell from the first DL slot that occurs after the beginning of slot  and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot.i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed PCell UE specific CBW change delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.6Measurement procedure for RedCap

## A.17.6.1Intra-frequency Measurements

## A.17.6.1.1SA event triggered reporting test without gap under non-DRX

## A.17.6.1.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements for RedCap in clause 9.2B.5.1 and 9.2B.5.2. Supported test configurations are shown in table A.17.6.1.1.1-1.

Table A.17.6.1.1.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.17.6.1.1.1-2, A.17.6.1.1.1-3 and A.17.6.1.1.1-4 below.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.17.6.1.1.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX for RedCap

Table A.17.6.1.1.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX for RedCap

Table A.17.6.1.1.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 without gap without DRX for RedCap

Figure A.17.6.1.1.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.17.6.1.1.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-2.4 s for a UE supporting power class 1 or 5,

-1.44 s for a UE supporting power class 2, 3, 4 or 7.

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.17.6.1.2SA event triggered reporting test without gap under DRX

## A.17.6.1.2.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2B.5.1 and 9.2B.5.2. Supported test configurations are shown in table A.7.6.1.2.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.7.6.1.2.1-2, A.7.6.1.2.1-3 and A.7.6.1.2.1-4.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

## A.7.6.1.2.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-7.2 s for a UE supporting power class 1 or 5,

-4.32 s for a UE supporting power class 2, 3, 4, or 7.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-51.2 s for a UE supporting power class 1 or 5,

-30.72 s for a UE supporting power class 2, 3 4, or 7.

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.17.6.1.3SA event triggered reporting test with per-UE gaps under non-DRX

## A.17.6.1.3.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2B.6.1 and 9.2B.6.2. Supported test configurations are shown in table A.17.6.1.3.1-1.

Table A.17.6.1.3.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.17.6.1.3.1-2 ~ 4 below.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

Table A.17.6.1.3.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps without DRX

Table A.17.6.1.3.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps without DRX

Table A.17.6.1.3.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps without DRX

Figure A.17.6.1.3.1-1: Time multiplexed downlink transmissions (Config 1 example)

## A.17.6.1.3.2Test Requirements

In the test, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-3.2 s for a UE supporting power class 1 or 5,

-1.92 s for a UE supporting power class 2, 3 4 or 7

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.17.6.1.4SA event triggered reporting test with per-UE gaps under DRX

## A.17.6.1.4.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the TDD intra-frequency cell search requirements in clause 9.2B.6.1 and 9.2B.6.2. Supported test configurations are shown in table A.17.6.1.4.1-1.

Table A.17.6.1.4.1-1: supported test configurations

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.17.6.1.4.1-2, A.17.6.1.4.1-3 and A.17.6.1.4.1-4 below.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.17.6.1.4.1-2: General test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps with DRX

Table A.17.6.1.4.1-3: NR Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps with DRX

Table A.17.6.1.4.1-4: NR OTA Cell specific test parameters for intra-frequency event triggered reporting for SA with TDD PCell in FR2 with per-UE gaps with DRX

Table A.17.6.1.4.1-5: Void

Table A.17.6.1.4.1-6:Void

## A.17.6.1.4.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-7.2 s for a UE supporting power class 1 or 5,

-4.32 s for a UE supporting power class 2, 3 4 or 7

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

-51.2 s for a UE supporting power class 1 or 5,

-30.72 s for a UE supporting power class 2, 3 4 or 7

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.17.6.2Inter-frequency Measurements

## A.17.6.2.1SA event triggered reporting tests For FR2 without SSB time index detection when DRX is not used (PCell in FR2)

## A.17.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR2 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.17.6.2.1.1-1, A.17.6.2.1.1-2, and A.17.6.2.1.1-3.

Measurement gap pattern configuration # 13 as defined in table A.17.6.2.1.1-2 is provided for UE that does not support per-FR gap and for UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Supported test configurations are shown in table A.17.6.2.1.1-1.

Table A.17.6.2.1.1-1 SA event triggered reporting tests without SSB index reading for FR2-FR2

Table A.17.6.2.1.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

Table A.17.6.2.1.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

## A.17.6.2.1.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 5120 for UE supporting power class 1, or

## 3200 for UE supporting other power class.

The  UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.17.6.2.2SA event triggered reporting tests For FR2 without SSB time index detection when DRX is used (PCell in FR2)

## A.17.6.2.2.1Test Purpose and Environment

The purpose of this test is to verify that RedCap UE makes correct reporting of an event in FR2. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR2 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 2. The test parameters and configurations are given in tables A.17.6.2.2.1-1, A.17.6.2.2.1-2, and A.17.6.2.2.1-3.

In test 1&2 measurement gap pattern configuration # 13 as defined in table A.17.6.2.2.1-2 is provided for RedCap UE that does not support per-FR gap and for RedCap UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Supported test configurations are shown in table A.17.6.2.2.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.17.6.2.2.1-1: SA event triggered reporting tests without SSB index reading for FR2-FR2

Table A.17.6.2.2.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 without SSB time index detection

Table A.17.6.2.2.1-3: Cell specific test parameters for CA inter-frequency event triggered reporting without SSB time index detection

## A.17.6.2.2.2Test Requirements

In test 1 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 7680 for UE supporting power class 1, or

## 4800 for UE supporting other power class.

In test 2 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

## 81920 for UE supporting power class 1, or

## 51200 for UE supporting other power class.

In test 1 and 2 UE is not required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.17.6.2.3SA event triggered reporting tests For FR2 with SSB time index detection when DRX is not used (PCell in FR2)

## A.17.6.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR2 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.17.6.2.3.1-1, A.17.6.2.3.1-2, and A.17.6.2.3.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Supported test configurations are shown in table A.17.6.2.3.1-1.

Table A.17.6.2.3.1-1: SA event triggered reporting tests with SSB index reading for FR2-FR2

Table A.17.6.2.3.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection

Table A.17.6.2.3.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection

## A.17.6.2.3.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2, where X is

## 6720 for UE supporting power class 1, or

## 4160 for UE supporting other power class.

The UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.17.6.2.4SA event triggered reporting tests For FR2 with SSB time index detection when DRX is used (PCell in FR2) for 2 RX UE

## A.17.6.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3B.4.

In this test, there are two cells: NR Cell 1 as PCell in FR2 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.17.6.2.4.1-1, A.17.6.2.4.1-2, and A.17.6.2.4.1-3.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Supported test configurations are shown in table A.17.6.2.4.1-1.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furhtermore UE is allocated with PUSCH resource at every DRX cycle.

Table A.17.6.2.4.1-1: SA event triggered reporting tests with SSB index reading for FR2-FR2

Table A.17.6.2.4.1-2: General test parameters for SA inter-frequency event triggered reporting for FR2 with SSB time index detection

Table A.17.6.2.4.1-3: Cell specific test parameters for CA inter-frequency event triggered reporting with SSB time index detection

## A.17.6.2.4.2Test Requirements

In test 1 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X1 ms from the beginning of time period T2, where X1 is

## 10080 for UE supporting power class 1, or

## 6240 for UE supporting other power class.

In test 1 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X2 ms from the beginning of time period T2, where X2 is

## 107520 for UE supporting power class 1, or

## 66560 for UE supporting other power class.

In test 1 and 2 UE is required to report SSB time index. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.17.6.3L1-RSRP measurement for beam reporting

## A.17.6.3.1SSB based L1-RSRP measurement when DRX is not used

## A.17.6.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.1, with the testing configurations for NR cells in table A.7.6.3.1.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

## A.17.6.3.1.2Test parameters

Test parameters are the same as in clause A.7.6.3.1.2.

## A.17.6.3.1.3Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than X ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in clause [10.xx.xx.1], where X is

-1680 for UE supporting power class 1 or 5.

-1200 for UE supporting power class 2,3, 4 or 7.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.6.3.2SSB based L1-RSRP measurement when DRX is used

## A.17.6.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.1, with the testing configurations for NR cells in table A.17.6.3.2.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15

Table A.17.6.3.2.1-1: Applicable NR configurations for FR2 SSB based L1-RSRP test

## A.17.6.3.2.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.17.6.3.2.2-1 and table A.17.6.3.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.17.6.3.2.2-1: General test parameters

Table A.17.6.3.2.2-2: SSB specific test parameters

## A.17.6.3.2.3Test Requirements

The UE shall send L1-RSRP report every 320 slots. No later than X ms plus 320 slots from the beginning of time period T2, UE shall send L1-RSRP report including the results for both SSB#0 and SSB#1 while meeting the accuracy requirements defined in clause 10.1.20.1, where X is

-2880 for UE supporting power class 1

-1920 for UE supporting power class 2,3 or 4.

The reported L1-RSRP value shall include the Rx antenna gain in the range of -10 to +20 dB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.17.6.3.3CSI-RS based L1-RSRP measurement when DRX is not used

## A.17.6.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.2, with the testing configurations for NR cells in table A.17.6.3.3.1-1.

Table A.17.6.3.3.1-1: Applicable NR configurations for FR2 CSI-RS based L1-RSRP test

## A.17.6.3.3.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.17.6.3.3.2-1 and table A.17.6.3.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 480 ms from the beginning of the test, the DCI trigger comes in slot 1  of a frame and UE provides the report back based on the reporting configuration as defined in table A.17.6.3.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.17.6.3.3.2-1: General test parameters

Table A.17.6.3.3.2-1: CSI-RS specific test parameters

## A.17.6.3.3.3Test Requirements

After 480 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the accuracy requirements defined in clause 10.1.20.1. The reported L1-RSRP value shall include the Rx antenna gain in the range of [-10 ~ +20] dB.

For absolute accuracy of CSI-RS0 and absolute accuracy of CSI-RS1, the UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.17.6.3.3.3-1.

For relative accuracy of CSI-RS0 compared with CSI-RS1, the UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

Table A.17.6.3.3.3-1: L1-RSRP absolute accuracy test requirement

## A.17.6.3.4CSI-RS based L1-RSRP measurement when DRX is used

## A.17.6.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5B.4.2, with the testing configurations for NR cells in table A.17.6.3.4.1-1.

Table A.17.6.3.4.1-1: Applicable NR configurations for FR2 CSI-RS based L1-RSRP test

## A.17.6.3.4.2Test parameters

There is one cells in the test, the FR2 PCell (Cell 1). The test parameters for the Cell 1 are given in table A.17.6.3.4.2-1 and table A.17.6.3.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 1440 ms from the beginning of the test, the DCI trigger comes in slot 1  of a frame and UE provides the report back based on the reporting configuration as defined in table A.17.6.3.4.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.17.6.3.4.2-1: General test parameters

Table A.17.6.3.4.2-1: CSI-RS specific test parameters

## A.7.6.3.3.3Test Requirements

After 1440 ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the accuracy requirements defined in clause 10.1.20.1. The reported L1-RSRP value shall include the Rx antenna gain in the range of [-10 ~ +20] dB.

For absolute accuracy of CSI-RS0 and absolute accuracy of CSI-RS1, the UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.17.6.3.4.3-1.

For relative accuracy of CSI-RS0 compared with CSI-RS1, the UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table 10.1.20.2.2-1.

Table A.17.6.3.4.3-1: L1-RSRP absolute accuracy test requirement

A.17.6.4NR Measurements with autonomous gaps

## A.17.6.4.1SA interfrequency CGI reporting in autonomous gaps test (PCell in FR2) for 2 RX UE

## A.17.6.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an CGI. This test will partly verify the SA inter-frequency NR cell search requirements in clause 8.2.1.2.16 and 9.11

In this test, there are two cells: NR Cell 1 as PCell in FR2 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 2.  The test parameters and configurations are given in tables A.17.6.4.1.1-1, A.17.6.4.1.1-2, and A.17.6.4.1.1-3.

Measurement gap patterns are configured. During T1 the UE shall report event A3 for Cell 2. Within 3 seconds of the event report, the test equipment shall add a measurement reporting configuration using ReportConfigNR which containsa ReportCGI IE with cellForWhichToReportCGI set to the physical Cell ID of Cell 2 and including the optional IE useAutonomousGaps-r16

In the measurement control information, it is indicated to the UE to decode the CGI of the neighbour cell using autonomous gaps. The test consists of two time phases, T1 and T2. Time period T2 begins 10 ms after the test equipment has transmitted the RRC reconfiguration message containing the ReportCGI IE.

Supported test configurations are shown in table A.17.6.4.1.1-1.

Table A.17.6.4.1.1-1 SA interfrequency CGI reporting test in autonomous gaps

Table A.17.6.4.1.1-2: General test parameters for SA interfrequency CGI reporting in autonomous gaps

Table A.17.6.4.1.1-3: Cell specific test parameters SA interfrequency CGI reporting in autonomous gaps

## A.17.6.4.1.2Test Requirements

The UE shall report the CGI of Cell 2 within 25*Tsmtc + 6*Tsi-rnti+20 ms +2 ms= 762 ms from the start of T2, allow 765 ms. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall be scheduled continuously throughout the test, and from the start of T3 until 775 ms the number of interrupted slots shall not exceed the allowed number as defined in clause 8.2.2.2.14.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.17.6.5RSTD measurements

## A.17.6.5.1NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA

## A.17.6.5.1.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC CONNECTED state meets the requirements specified in clause 9.9A.2 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

Supported test configurations are shown in table A.17.6.5.1.1-1. The test parameters are as given in table A.17.6.5.1.1-2, Table A.17.6.5.1.1-3, and table A.17.6.5.1.1-4.

Table A.17.6.5.1.1-1: Supported test configurations for NR RSTD

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layers.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the RedCap UE during T1. The measurement reporting delay test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #13 before T2.

Table A.17.6.5.1.1-2: General test parameters for RSTD measurement reporting delay

Table A.17.6.5.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.17.6.5.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.17.6.5.1.2Test Requirements

The RSTD measurement time without FH for RedCap fulfils the requirements specified in clause 9.9A.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 9.9.2A.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD_1970049.

## A.17.6.5.2NR RSTD measurement reporting delay test case with PRS frequency hopping

## A.17.6.5.2.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 9.9A.2.6 in FR2 in standalone scenario when PRS frequency hopping is configured.

Supported test configurations are shown in table A.17.6.5.2.1-1. The test parameters are as given in table A.17.6.5.2.1-2, table A.17.6.5.2.1-3, and table A.17.6.5.2.1-4.

Table A.17.6.5.2.1-1: Supported test configurations for NR RSTD

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layers.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall not have any timing information of Cell 2 and Cell 3. All three cells transmit PRS during T2.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The test requirements apply when frequencyHopping is configured to UE.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID # 24 or #13 before T2.

Table A.17.6.5.2.1-2: General test parameters for RSTD measurement reporting delay

Table A.17.6.5.2.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.17.6.5.2.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.17.6.5.2.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 9.9A.2.6.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 9.9A.2.6 starting from the beginning of time interval T2.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD_1970049.

## A.17.6.6UE Rx-Tx Measurements

## A.17.6.6.1UE Rx-Tx measurement reporting delay for single positioning frequency layer in FR2 SA without RX FH in RRC_CONNECTED mode

## A.17.6.6.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement without RX FH in RRC_CONNECTED mode meets the requirements specified in clause 9.9A.4.5 in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configuration is listed in table A.17.6.6.1.1-1.

Table A.17.6.6.1.1-1: Supported test configurations.

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. In nr-Multi-RTT-RequestLocationInformation, nr-DL-PRS-RxHoppingRequest is not present.

The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID #13 or ID #24 before T2.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.17.6.6.1.1-2 and table A.17.6.6.1.1-3 respectively.

Table A.17.6.6.1.1-2: General test parameters

Table A.17.6.6.1.1-3: Cell specific test parameters

## A.17.6.6.1.2Test requirements

The UE Rx-Tx time difference measurement time fulfills the requirements specified in clause 9.9A.4.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1A.18.3.

## A.17.6.6.2UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR2 SA in RRC_CONNECTED state

## A.17.6.6.2.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement with Rx FH meets the requirements specified in clause 9.9A.4.8 in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.17.6.6.2.1-1.

Table A.17.6.6.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the multi-RTT assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources.

The UE is configured with measurement gap pattern ID #13 or ID #24 before T2.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.17.6.6.2.1-2 and table A.17.6.6.2.1-3, respectively.

Table A.17.6.6.2.1-2: General test parameters

Table A.17.6.6.2.1-3: Cell specific test parameters

## A.17.6.6.2.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 9.9A.4.8.

The RedCap UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1A.18.3.

## A.17.6.7PRS-RSRP measurements

## A.17.6.7.1PRS-RSRP measurement delay test case for RedCap positioning without Rx FH in RRC_CONNECTED state in FR2

## A.17.6.7.1.1PRS-RSRP measurement delay test case for single positioning frequency layer

## A.17.6.7.1.1.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements specified in clause 9A.9.3.5 for single positioning frequency layer under AWGN propagation conditions in standalone scenario. Supported test configurations are shown in table A.17.6.7.1.1.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. The measurement reporting delay test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform PRS-RSRP measurement with RX FH via NR-DL-AoD-RequestLocationInformation or the UE is configured by the LMF to perform PRS-RSRP measurement with RX FH but reports the PRS-RSRP measurement based on the single hop in NR-DL-AoD-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is DT after slot #n, where DT = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.6.7.1.1.1-2 and table A.17.6.7.1.1.1-3.

Table A.17.6.7.1.1.1-1: supported test configurations for PRS RSRP measurement for FR2

Table A.17.6.7.1.1.1-2: General test parameters for PRS RSRP measurement reporting delay

Table A.17.6.7.1.1.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

## A.17.6.7.1.1.2Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 9.9A.3.5. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9A.3.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1A.17.3.

## A.17.6.7.1.2PRS-RSRP measurement delay test case for dual positioning frequency layer

## A.17.6.7.1.2.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements specified in clause 9.9A.3.5 for dual positioning frequency layers under AWGN propagation conditions in standalone scenario. Supported test configurations are shown in table A.17.6.7.1.2.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the different frequency from the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is DT after slot #n, where DT = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.6.7.1.2.1-2, and table A.17.6.7.1.2.1-3.

Table A.17.6.7.1.2.1-1: supported test configurations for PRS RSRP measurement for FR2

Table A.17.6.7.1.2.1-2: General test parameters for PRS RSRP measurement reporting delay

Table A.17.6.7.1.2.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

## A.17.6.7.1.2.2Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 9.9A.3.5.The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9A.3.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1A.17.3.

## A.17.6.7.2PRS-RSRP measurement delay with FH in RRC_CONNECTED state in FR2

## A.17.6.7.2.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement with FH by a RedCap UE meets requirements specified in clause 9.9A.3.6 for single positioning frequency layer under AWGN propagation conditions in standalone scenario. Supported test configurations are shown in table A.17.6.7.2.1-1

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.6.7.2.1-2, and table A.17.6.7.2.1-3.

Table A.17.6.7.2.1-1: Supported test configurations for PRS RSRP measurement

Table A.17.6.7.2.1-2: General test parameters for PRS RSRP measurement reporting delay

Table A.17.6.7.2.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

## A.17.6.7.2.2Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 9.9A.3.6. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9A.3.6 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1A.17.3, i.e., between PRS RSRP_0 and PRS RSRP_126.

## A.17.6.8PRS-RSRPP Measurements

## A.17.6.8.1PRS-RSRPP measurement delay without FH in RRC_CONNECTED state in FR2

## A.17.6.8.1.1Test Purpose and Environment

The purpose of the test is to verify that the PRS RSRPP measurement without FH by a RedCap UE meets requirements specified in clause 9.9A.5.5 for single positioning frequency layer under 2-tap channel propagation conditions in standalone scenario. Supported test configurations are shown in table A.17.6.8.1.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.6.8.1.1-2, and table A.17.6.8.1.1-3.

Table A.17.6.8.1.1-1: supported test configurations for PRS RSRPP measurement for FR2

Table A.17.6.8.1.1-2: General test parameters for PRS RSRPP measurement reporting delay

Table A.17.6.8.1.1-3: Cell-specific test parameters for PRS RSRPP measurement reporting delay

## A.17.6.8.1.2Test Requirements

The PRS RSRPP measurement time fulfils the requirements specified in clause 9.9A.5.5. The UE shall perform and report the PRS RSRPP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9A.5.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRPP measurement for each correct event shall be within the PRS RSRPP reporting range specified in clause 10.1A.19, i.e., between PRS RSRPP_0 and PRS RSRPP_126.

## A.17.6.8.2PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR2 SA in RRC_CONNECTED state

## A.17.6.8.2.1Test Purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement requirements with Rx FH in RRC_CONNECTED state meets the delay requirements specified in clause 9.9A.5.8 in an environment with two-tap channel propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.17.6.8.2.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the Pcell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.6.8.2.1-2, and table A.17.6.8.2.1-3.

Table A.17.6.8.2.1-1: supported test configurations for PRS-RSRPP measurement for FR2

Table A.17.6.8.2.1-2: General test parameters for PRS-RSRPP measurement reporting delay

Table A.17.6.8.2.1-3: Cell-specific test parameters for PRS-RSRPP measurement reporting delay

## A.17.6.8.2.2Test Requirements

The PRS-RSRPP measurement time fulfils the requirements specified in clause 9.9A.5.8. The UE shall perform and report the PRS-RSRPP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9A.5.8 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS-RSRPP measurement for each correct event shall be within the PRS-RSRPP reporting range specified in clause 10.1A.19, i.e., between PRS RSRPP_0 and PRS RSRPP_126.

## A.17.7Measurement Performance requirements

## A.17.7.1SS-RSRP

## A.17.7.1.1SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

## A.17.7.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy for RedCap UE is within the specified limits. This test will verify the requirements in clauses 10.1.3A.3 for intra-frequency measurements.

## A.17.7.1.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.7.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in table A.17.7.1.1.2-2 and A.17.7.1.1.2-3. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1. The test consists of two time phases T1 and T2.

Table A.17.7.1.1.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

Table A.17.7.1.1.2-2: SS-RSRP  Intra frequency general test parameters

Table A.17.7.1.1.2-3: SS-RSRP Intra frequency OTA related test parameters

## A.17.7.1.1.3Test Requirements

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

## A.17.7.1.2SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell

## A.17.7.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1A.5.1.1 and 10.1.5A.1.2 for intrer-frequency measurements with the testing configurations for NR cells in table A.17.7.1.2.1-1.

Table A.17.7.1.2.1-1: Applicable NR configurations for FR2 inter-frequency SS-RSRP accuracy test

## A.17.7.1.2.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters and applicability for Cell 1 are defined in A.3.7.2. The test parameters for the Cell 1 and Cell 2 are given in table A.17.7.1.2.2-1 and table A.17.7.1.2.2-2 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in A.17.7.1.2.2-1

The inter-frequency measurements are supported by a measurement gap.

Table A.17.7.1.2.2-1: SS-RSRP inter-frequency test parameters

Table A.17.7.1.2.2-2: SS-RSRP inter frequency OTA related test parameters

## A.17.7.1.2.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil the absolute requirements in clause 10.1A.5.1.1 and the relative requirements in clause 10.1.5A.1.2.

Test 1:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.17.7.1.2.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table A.17.7.1.2.3-2.

Test 2:

Absolute accuracy of Cell 1 and absolute accuracy of Cell 2. The UE is deemed to meet the requirement if the reported SS-RSRP is in the range shown in table A.17.7.1.2.3-1.

Relative accuracy of Cell 2 compared with Cell 1. The UE is deemed to meet the requirement if the difference in reported SS-RSRP meets the requirements in table A.17.7.1.2.3-2.

Table A.17.7.1.2.3-1: SS-RSRP absolute accuracy test requirement

Table A.17.7.1.2.3-2: SS-RSRP relative accuracy test requirement

## A.17.7.2SS-RSRQ

## A.17.7.2.1SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell

## A.17.7.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1A.7.

## A.17.7.2.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.7.2.1.2-1. . The absolute accuracy of SS-RSRQ intra-frequency measurement is test by using the parameters in table A.17.7.2.1.2-2 and table A.17.7.2.1.2-3. In all test cases, Cell 1 is the PCell and Cell 2 the target cell.

Table A.17.7.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

Table A.17.7.2.1.2-2: SS-RSRQ Intra frequency test parameters

Table A.17.7.2.1.2-3: SS-RSRQ Intra frequency OTA related test parameters

## A.17.7.2.1.3Test Requirements

The SS-RSRQ absolute measurement accuracy in test 1 shall be within the range Nominal SS-RSRQ+2.5 dB to Nominal SS-RSRQ-2.5 dB and the SS-RSRQ measurement accuracy in test 2 shall be within the range Nominal RSRQ+3.5 dB to Nominal RSRQ-3.5 dB  according to the requirements in clause 10.1.8.1.1.Nominal RSRQ is the value shown in table A.17.7.2.1.2-3.

## A.17.7.2.2SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell for 2 Rx UE

## A.17.7.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1A.9.1.1 and 10.1A.9.1.2 for inter-frequency measurement.

## A.17.7.2.2.2Test parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.17.7.2.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.17.7.2.2.2-2 and table A.17.7.2.2.2-3. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.17.7.2.2.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

Table A.17.7.2.2.2-2: SS-RSRQ Inter frequency test parameters

Table A.17.7.2.2.2-3 SS-RSRQ Inter frequency OTA related test parameters

## A.17.7.2.2.3Test Requirements

The SS-RSRQ absolute measurement accuracy in test 1 shall be within the range Nominal SS-RSRQ+2.5 dB to Nominal SS-RSRQ -2.5 dB and the SS-RSRQ measurement accuracy in test 2 shall be within the range Nominal SS-RSRQ +3.5 dB to Nominal SS-RSRQ -3.5 dB according to the requirements in clause 10.1A.10.1.1.

The SS-RSRQ relative measurement accuracy shall fulfil the requirements in clause 10.1A.10.1.2.

## A.17.7.2.3SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell

## A.17.7.3L1-RSRP measurement for beam reporting

## A.17.7.3.1SSB based L1-RSRP measurement

## A.17.7.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.5B.2 and clause [10.xx.xx.1] for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.7.7.4.1.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

## A.17.7.3.1.2Test parameters

Test parameters are the same as in clause A.7.7.4.1.2.

## A.17.7.3.1.3Test Requirements

After 320 ms from the beginning of the test, the L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 2 shall fulfil the requirements in clauses [10.xx.xx.1]. The following requirements are to be verified:

For Test 1:

Absolute accuracy of SSB0 and absolute accuracy of SSB1. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.17.7.3.1.3-1.

Relative accuracy of SSB0 compared with SSB1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table [10.xx.xx.1.2-1].

For Test 2:

Absolute accuracy of SSB0 and absolute accuracy of SSB1. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.17.7.3.1.3-1.

Relative accuracy of SSB0 compared with SSB1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table [10.xx.xx.1.2-1].

Table A.17.7.3.1.3-1: L1-RSRP absolute accuracy test requirement

## A.17.7.3.2CSI-RS based L1-RSRP measurement on resource set with repetition off

## A.17.7.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 9.5.3 and clause [10.1.xx.2] for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.7.7.4.2.1-1.

The AoA setup for this test is Setup 1 as defined in clause A.3.15.

## A.17.7.3.2.2Test parameters

Test parameters are the same as in clause A.7.7.4.2.2.

## A.17.7.3.2.3Test Requirements

After 640 ms from the beginning of the test, the L1-RSRP measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirements in clause [10.1.xx.2]. The following requirements are to be verified:

For Test 1:

Absolute accuracy of CSI-RS0 and absolute accuracy of CSI-RS1. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.17.7.3.2.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table [10.1.xx.2.2-1].

For Test 2:

Absolute accuracy of CSI-RS0 and absolute accuracy of CSI-RS1. The UE is deemed to meet the requirement if the reported L1-RSRP is in the range shown in table A.17.7.3.2.3-1.

Relative accuracy of CSI-RS0 compared with CSI-RS1. The UE is deemed to meet the requirement if the difference in reported L1-RSRP meets the requirements in table [10.1.xx.2.2-1].

Table A.17.7.3.2.3-1: L1-RSRP absolute accuracy test requirement

## A.17.7.4SS-SINR

## A.17.7.4SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell for 2Rx UE

## A.17.7.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1A.13.1.1.

## A.17.7.4.1.2Test parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A A.17.7.4.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is test by using the parameters in table A.17.7.4.1.2-2 and table Table A.17.7.4.1.2-3. In all test cases, Cell 1 is the PCell and Cell 2 the target cell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.17.7.4.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

Table A.17.7.4.1.2-2: SS-SINR Intra frequency test parameters

Table A.17.7.4.1.2-3: SS-SINR Intra frequency OTA related test parameters

## A.17.7.4.1.3Test Requirements

The SS-SINR absolute measurement accuracy in test 1 shall be within the range Nominal SS-SINR+3B to Nominal SS-SINR -3 dB and the SS-SINR measurement accuracy in test 2 shall be within the range Nominal SS-SINR +3.5 dB to Nominal SS-SINR -3.5 dB according to the requirements in clause 10.1A.10.13.1.

## A.17.7.5RSTD measurements

## A.17.7.5.1RSTD measurement accuracy test case for RedCap UE without FH

## A.17.7.5.1.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC CONNECTED state meets the accuracy requirements specified in clause 10.1A.16.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.17.7.5.1.1-1.

Table A.17.7.5.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cells. Both cells are on the same NR RF channel in FR2. GP#24 is configured if UE supports GP#24, otherwise, GP#13 is configured for the test. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the RedCap UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 9.9A.2.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The accuracy test parameters and OTA related test parameters are as given in table A.17.7.5.1.1-2 and table A.17.7.5.1.1-3, respectively.

Table A.17.7.5.1.1-2: RSTD accuracy test parameters

Table A.17.7.5.1.1-3: RSTD accuracy OTA related test parameters

## A.17.7.5.1.2Test Requirements

The RSTD measurement accuracy shall fulfil the absolute requirement in clause 10.1A.16.2.

A.17.7.5.2RSTD measurement accuracy test case for RedCap UE with FH in RRC_CONNECTED state

A.17.7.5.2.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the accuracy requirements specified in clause 10.1A.16.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.17.7.5.2.1-1. The test parameters are as given in table A.17.7.5.2.1-2, table A.17.7.5.2.1-3, and table A.17.7.5.2.1-4.

Table A.17.7.5.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2. GP#24 is configured if UE supports GP#24, otherwise, GP#13 is configured for the test. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the UE before the start of the test.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation as specified in TS 37.355 [34], clause 6.5.12. The frequency hopping configurations are specified in clause A.3.31.

Table A.17.7.5.2.1-2: RSTD accuracy test parameters

Table A.17.7.5.2.1-3: RSTD accuracy OTA related test parameters

A.17.7.5.2.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1A.16.2.

## A.17.7.6UE Rx-Tx Measurements

## A.17.7.6.1UE Rx-Tx measurement accuracy for single positioning frequency layer in FR2 SA without RX FH in RRC_CONNECTED mode

## A.17.7.6.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy without RX FH in RRC_CONNECTED state is within the specified limits. This test will verify the requirements in clause 10.1A.18.2. The test is conducted in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configuration is listed in table A.17.7.6.1.1-1.

Table A.17.7.6.1.1-1: Supported test configurations.

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test. In nr-Multi-RTT-RequestLocationInformation, nr-DL-PRS-RxHoppingRequest is not present.

The UE is configured with measurement gap pattern ID #13 or ID #24 before the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.17.7.6.1.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.17.7.6.1.2-1.

Table A.17.7.6.1.2-1: UE Rx-Tx time difference measurement accuracy test parameters

## A.17.7.6.1.3Test requirements

The UE Rx-Tx time difference measurement fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1A.18.3 for both Cell 1 and Cell 2.

## A.17.7.6.2SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC_CONNECTED state in FR2

## A.17.7.6.2.1Test purpose and Environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy with FH by a RedCap UE in RRC_CONNECTED is within the specified limits. This test will verify the requirements in clause 10.1A.18.2.3. The test is conducted in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configuration is listed in table A.17.7.6.2.1-1.

Table A.17.7.6.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test. The test requirements apply when frequencyHopping is configured to UE.

The UE is configured with measurement gap pattern ID #13 or ID #24 before the test.

The UE is configured to transmit positioning SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.17.7.6.2.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.17.7.6.2.2-1.

Table A.17.7.6.2.2-1: UE Rx-Tx time difference measurement accuracy test parameters

## A.17.7.6.2.3Test requirements

The UE Rx-Tx time difference measurement fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1A.18.2.3 for both Cell 1 and Cell 2.

## A.17.7.7PRS-RSRP Measurements

## A.17.7.7.1PRS-RSRP measurement accuracy without FH in RRC_CONNECTED state in FR2

## A.17.7.7.1.1Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRP measurement without FH by a RedCap UE is within the specified limits. This test will verify the requirements in clauses 10.1A.17.2.1 and 10.1A.17.2.2.

## A.17.7.7.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.7.7.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in table A.17.7.7.1.2-2 and A.17.7.7.1.2-3. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.17.7.7.1.2-1: PRS-RSRP supported test configurations

Table A.17.7.7.1.2-2: PRS-RSRP general test parameters

Table A.17.7.7.1.2-3: PRS-RSRP OTA related test parameters

## A.17.7.7.1.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1 if the reported PRS-RSRP is in the range shown in table A.17.7.7.1.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2.

Table A.17.7.7.1.3-1: PRS-RSRP absolute accuracy test requirement

## A.17.7.7.2PRS-RSRP measurement accuracy with FH in RRC_CONNECTED state in FR2

## A.17.7.7.2.1Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRP measurement with FH by a RedCap UE is within the specified limits. This test will verify the requirements in clauses 10.1A.17.2.1 and 10.1A.17.2.2.

## A.17.7.7.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.7.7.2.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in table A.17.7.7.2.2-2 and A.17.7.7.2.2-3. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1. PRS RX hopping is present in NR-DL-AoD-RequestLocationInformation.

Table A.17.7.7.2.2-1: PRS-RSRP supported test configurations

Table A.17.7.7.2.2-2: PRS-RSRP general test parameters

Table A.17.7.7.2.2-3: PRS-RSRP OTA related test parameters

## A.17.7.7.2.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1 if the reported PRS-RSRP is in the range shown in table A.17.7.7.2.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2.

Table A.17.7.7.2.3-1: PRS-RSRP absolute accuracy test requirement

## A.17.7.8PRS-RSRPP Measurements

## A.17.7.8.1PRS-RSRPP measurement accuracy without FH in RRC_CONNECTED state in FR2

## A.17.7.8.1.1Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRPP measurement without FH by a RedCap UE in RRC_CONNECTED is within the specified limits. This test will verify the requirements in clauses 10.1A.19.2.

## A.17.7.8.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.7.8.1.2-1. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.17.7.8.1.2-1: PRS-RSRPP supported test configurations

Table A.17.7.8.1.2-2: PRS-RSRPP general test parameters

Table A.17.7.8.1.2-3: PRS-RSRPP OTA related test parameters

## A.17.7.8.1.3Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.19.2 if the reported PRS-RSRPP is in the range shown in table A.17.7.8.1.3-1.

Table A.17.7.8.1.3-1: PRS-RSRPP absolute accuracy test requirement

## A.17.7.8.2SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_CONNECTED state in FR2

## A.17.7.8.2.1Test purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRPP measurement with FH by a RedCap UE in RRC_CONNECTED is within the specified limits. This test will verify the requirements in clauses 10.1A.19.2.

## A.17.7.8.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.7.8.2.2-1. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.3.17.2.1-1.

Table A.17.7.8.2.2-1: PRS-RSRPP supported test configurations

Table A.17.7.8.2.2-2: PRS-RSRPP general test parameters

Table A.17.7.8.2.2-3: PRS-RSRPP OTA related test parameters

## A.17.7.8.2.3Test requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1.38.2 if the reported PRS-RSRPP is in the range shown in table A.17.7.8.2.3-1.

Table A.17.7.8.2.3-1: PRS-RSRPP absolute accuracy test requirement

## A.17.8Measurement Procedure for RedCap in RRC_INACTIVE

## A.17.8.1RSTD Measurements

## A.17.8.1.1NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA in RRC_INACTIVE state

## A.17.8.1.1.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC INACTIVE state meets the requirements specified in clause 5.6A.4.5 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.17.8.1.1.1-1.

Table A.17.8.1.1.1-1: Supported test configurations for NR RSTD

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layers.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell3. During T2 UE shall be in RRC_INACTIVE state and all cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the RedCap UE during T1. The measurement reporting delay test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The last TTI containing the two messages shall be provided to the RedCap UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s).

The UE is configured with DRX cycle of 0.64 s.

The general test parameters are listed in table A.17.8.1.1.1-2, and cell specific test parameters are listed in table A.17.8.1.1.1-3 and table A.17.8.1.1.1-4.

Table A.17.8.1.1.1-2: General test parameters for RSTD measurement reporting delay

Table A.17.8.1.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.17.8.1.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.17.8.1.1.2Test Requirements

The RSTD measurement time without FH for RedCap fulfils the requirements specified in clause 5.6A.4.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 5.6A.4.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD_1970049.

## A.17.8.1.2NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state

## A.17.8.1.2.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement meets the requirements specified in clause 5.6A.4.6 in FR2 in standalone scenario when PRS frequency hopping is configured.

The supported test configurations are specified in table A.17.8.1.2.1-1.

Table A.17.8.1.2.1-1: Supported test configurations for NR RSTD

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layers.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell3. During T2 UE shall be in RRC_INACTIVE state and all cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. The last TTI containing the two messages shall be provided to the UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The test requirements apply when frequencyHopping is configured to UE.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s).

The UE is configured with DRX cycle of 0.64 s.

The general test parameters are listed in table A.17.8.1.2.1-2, and cell specific test parameters are listed in table A.17.8.1.2.1-3 and table A.17.8.1.2.1-4.

Table A.17.8.1.2.1-2: General test parameters for RSTD measurement reporting delay

Table A.17.8.1.2.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.17.8.1.2.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.17.8.1.2.2Test Requirements

The RSTD measurement time fulfils the requirements specified in clause 5.6A.4.6.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 5.6A.4.6 starting from the beginning of time interval T2.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD_1970049.

## A.17.8.1.3NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state with eDRX > 10.24s

## A.17.8.1.3.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 5.6A.4.5 for RSTD measurements in RRC_INACTIVE with eDRX. Refer to clause A.7.8.1.4.1 for test configuration and procedure.

## A.17.8.1.3.2Test requirements

The RSTD measurement time shall fulfill the requirements specified in clause 5.6A.4.5.

The UE shall perform and report the RSTD measurements for Cell 1, Cell 2 and Cell 3 within the specified measurement period duration starting from the beginning of time interval T2. The requirement shall be evaluated based on the first measurement report received from the UE.

NOTE 1:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3.

## A.17.8.2UE Rx-Tx Measurements

## A.17.8.2.1UE Rx-Tx measurement reporting delay for single positioning frequency layer in FR2 SA without RX FH in RRC_INACTIVE mode

## A.17.8.2.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement without RX FH in RRC_INACTIVE state meets the requirements specified in clause 5.6A.6.5 in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configuration is listed in table A.17.8.2.1.1-1.

Table A.17.8.2.1.1-1: Supported test configurations.

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE during T1. In nr-Multi-RTT-RequestLocationInformation, nr-DL-PRS-RxHoppingRequest is not present.

The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE state.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.17.8.2.1.1-2 and table A.17.8.2.1.1-3, respectively.

Table A.17.8.2.1.1-2: General test parameters

Table A.17.8.2.1.1-3: Cell specific test parameters

## A.17.8.2.1.2Test requirements

The UE Rx-Tx time difference measurement time in RRC_INACTIVE state fulfills the requirements specified in clause 5.6A.6.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time specified in clause 5.6A.6 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1A.18.3.

## A.17.8.2.2UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR2 SA in RRC_INACTIVE state

## A.17.8.2.2.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx measurement with Rx FH meets the requirements specified in clause 5.6A.6.6 in AWGN propagation condition in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are listed in table A.17.8.2.2.1-1.

Table A.17.8.2.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). Both cells are on the same RF channel in FR2.

The test consists of two consecutive time intervals, with duration of T1 and T2. Cell 1 and Cell 2 mute PRS transmission during T1 and transmit PRS during T2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the RedCap UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, RedCap UE is released into RRC_INACTIVE state.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The UE is configured to transmit positioning SRS during T2.

The general test parameters and cell specific test parameters are as given in table A.17.8.2.2.1-2 and table A.17.8.2.2.1-3, respectively.

Table A.17.8.2.2.1-2: General test parameters

Table A.17.8.2.2.1-3: Cell specific test parameters

## A.17.8.2.2.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 5.6A.6.6.

The RedCap UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1A.18.3.

## A.17.8.2.3UE Rx-Tx time difference measurements for single positioning frequency layer with eDRX > 10.24s in FR2 SA

## A.17.8.2.3.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 5.6A.6.5 for UE Rx-Tx measurements in RRC_INACTIVE with eDRX. Refer to clause A.7.8.3.3.1 for test configuration and procedure.

## A.17.8.2.3.2Test requirements

The UE Rx-Tx time difference measurement time fulfils the requirements specified in clause 5.6A.6.5.

The UE shall perform and report the UE Rx-Tx time difference measurements for Cell 1 and Cell 2 within the specified UE Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE 1:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported UE Rx-Tx measurement for each correct event shall be within the UE Rx-Tx reporting range specified in clause 10.1A.18.3.

## A.17.8.3PRS-RSRP Measurements

## A.17.8.3.1PRS-RSRP reporting delay test case for single positioning frequency layer in RRC_INACTIVE

## A.17.8.3.1.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements specified in clause 9.9A.3.5 for single positioning frequency layer under AWGN propagation conditions in RRC_INACTIVE. Supported test configurations are shown in table A.17.8.3.1.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

During T1 UE is in RRC_CONNECTED, the NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The measurement reporting delay test in this clause is valid in the cases where the RedCap UE is either not configured by the LMF to perform PRS-RSRP measurement with RX FH via NR-DL-AoD-RequestLocationInformation or the UE is configured by the LMF to perform PRS-RSRP measurement with RX FH and reports the PRS-RSRP measurement based on the single hop in NR-DL-AoD-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.8.3.1.1-2, and table A.17.8.3.1.1-3.

Table A.17.8.3.1.1-1: supported test configurations for PRS RSRP measurement for FR2

Table A.17.8.3.1.1-2: General test parameters for PRS RSRP measurement reporting delay

Table A.17.8.3.1.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

## A.17.8.3.1.2Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 9.9A.3.5. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 9.9A.3.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1A.17, i.e., between PRS RSRP_0 and PRS RSRP_126.

A.17.8.3.2PRS-RSRP measurement delay with FH in RRC_INACTIVE state in FR2

A.17.8.3.2.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement with FH by a RedCap UE meets requirements specified in clause 5.6A.5.5 for single positioning frequency layer under AWGN propagation conditions in RRC_INACTIVE. Supported test configurations are shown in table A.17.8.3.2.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

During T1 UE is in RRC_CONNECTED, the NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.7.8.1.2.1.1-2, and table A.17.8.3.2.1-3.

Table A.17.8.3.2.1-1: supported test configurations for PRS RSRP measurement for FR2-FR2

Table A.17.8.3.2.1-2: General test parameters for PRS RSRP measurement reporting delay

Table A.17.8.3.2.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

## A.17.8.3.2.2Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 5.6A.5.5. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 5.6A.5.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1A.17.3, i.e., between PRS RSRP_0 and PRS RSRP_126.

## A.17.8.3.3PRS-RSRP reporting delay in RRC_INACTIVE with eDRX

## A.17.8.3.3.1Test Purpose and Environment

The purpose of the test is to verify a RedCap UE can meet the PRS RSRP measurement requirements specified in clause 5.6A.5.5 for single positioning frequency layer under AWGN propagation conditions in RRC_INACTIVE, when configured with eDRX and without FH. Supported test configurations are shown in table A.17.8.3.3.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

During T1 UE is in RRC_CONNECTED, the NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The beginning of the time interval T2 is the first PRS resource occasion occurring T after the slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.8.3.3.1-2, and table A.17.8.3.3.1-3.

Table A.17.8.3.3.1-1: supported test configurations for PRS RSRP measurement for FR2

Table A.17.8.3.3.1-2: General test parameters for PRS RSRP measurement reporting delay

Table A.17.8.3.3.1-3: Cell-specific test parameters for PRS RSRP measurement reporting delay

## A.17.8.3.3.2Test Requirements

The PRS RSRP measurement time fulfils the requirements specified in clause 5.6A.5.5. The UE shall perform and report the PRS RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 5.6A.5.5 with Tavailable_PRS = 0.64 s starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

A test is considered complete after the UE reports the first set of positioning measurements based on the configured reportingInterval.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRP measurement for each correct event shall be within the PRS RSRP reporting range specified in clause 10.1A.17.3.

## A.17.8.4PRS-RSRPP Measurements

## A.17.8.4.1PRS-RSRPP measurement delay without FH in RRC_INACTIVE state in FR2

## A.17.8.4.1.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRPP measurement without FH by a RedCap UE meets requirements specified in clause 5.6A.7.5 for single positioning frequency layer under a 2-tap channel propagation conditions in standalone scenario. Supported test configurations are shown in table A.17.8.4.1.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the Pcell.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2. During T2 UE shall be in RRC_INACTIVE state and both cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n.

The beginning of the time interval T2 shall be aligned with the beginning of the first DRX cycle containing the PRS resources that is T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.8.4.1.1-2, and table A.17.8.4.1.1-3.

Table A.17.8.4.1.1-1: supported test configurations for PRS RSRPP measurement for FR2

Table A.17.8.4.1.1-2: General test parameters for PRS RSRPP measurement reporting delay

Table A.17.8.4.1.1-3: Cell-specific test parameters for PRS RSRPP measurement reporting delay

A.17.8.4.1.2Test Requirements

The PRS RSRPP measurement time fulfils the requirements specified in clause 5.6A.7.5. The UE shall perform and report the PRS RSRPP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 5.6A.7.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS RSRPP measurement for each correct event shall be within the PRS RSRPP reporting range specified in clause 10.1A.19.3, i.e., between PRS RSRPP_0 and PRS RSRPP_126.

## A.17.8.4.2PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR2 SA in RRC_INACTIVE state

## A.17.8.4.2.1Test Purpose and Environment

The purpose of the test is to verify that the PRS-RSRPP measurement requirements with Rx FH in RRC_INACTIVE state meets the delay requirements specified in clause 5.6A.7.6 in an environment with two-tap channel propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.17.8.4.2.1-1.

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2. The test consists of two consecutive time intervals, with duration of T1 and T2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the next DL slot after slot #n, UE is released into RRC_INACTIVE.

The test requirements apply when frequencyHopping is configured to UE.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource occasion occuring T after slot #n, where T = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.8.4.2.1-2, and table A.17.8.4.2.1-3.

Table A.17.8.4.2.1-1: supported test configurations for PRS-RSRPP measurement for FR2

Table A.17.8.4.2.1-2: General test parameters for PRS-RSRPP measurement reporting delay

Table A.17.8.4.2.1-3: Cell-specific test parameters for PRS-RSRPP measurement reporting delay

## A.17.8.4.2.2Test Requirements

The PRS-RSRPP measurement time fulfils the requirements specified in clause 5.6A.7.6. The UE shall perform and report the PRS-RSRPP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 5.6A.7.6 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS-RSRPP measurement for each correct event shall be within the PRS-RSRPP reporting range specified in clause 10.1A.19.3, i.e., between PRS RSRPP_0 and PRS RSRPP_126.

## A.17.8.4.3PRS-RSPP reporting delay in RRC_INACTIVE state with eDRX > 10.24s

## A.17.8.4.3.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 5.6A.7.5 for PRS-RSRPP measurements in RRC_INACTIVE with eDRX. Refer to clause A.7.8.4.3.1 for test configuration and procedure.

## A.17.8.4.3.2Test requirements

The PRS-RSRPP measurement time fulfils the requirements specified in clause 5.6A.7.5.

The UE shall perform and report the PRS-RSRPP measurements for Cell 1 and Cell 2 within the specified measurement period duration starting from the beginning of time interval T2. The requirement shall be evaluated based on the first measurement report received from the UE.

NOTE 1:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS-RSRPP measurement for each correct event shall be within the PRS-RSRPP reporting range specified in clause 10.1A.19.3.

## A.17.9Measurement Performance Requirements for RedCap in RRC_INACTIVE

## A.17.9.1RSTD Measurements

## A.17.9.1.1RSTD measurement accuracy test case for RedCap UE without FH in FR2 in RRC_INACTIVE state

## A.17.9.1.1.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC_INACTIVE state meets the accuracy requirements specified in clause 10.1A.16.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.17.9.1.1.1-1.

Table A.17.9.1.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2. The UE is configured with DRX cycle of 0.64 s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the RedCap UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 5.6A.4.5.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The accuracy test parameters and OTA related test parameters are as given in table A.17.9.1.1.1-2 and table A.17.9.1.1.1-3, respectively.

Table A.17.9.1.1.1-2: RSTD accuracy test parameters

Table A.17.9.1.1.1-3: RSTD accuracy OTA related test parameters

## A.17.9.1.1.2Test Requirements

The RSTD measurement accuracy shall fulfil the absolute requirement in clause 10.1A.16.2.

## A.17.9.1.2RSTD measurement accuracy test case for RedCap UE with FH in FR2 in RRC_INACTIVE state

## A.17.9.1.2.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement in RRC_INACTIVE state meets the accuracy requirements specified in clause 10.1A.16.2 in an environment with AWGN propagation conditions.

The supported test configurations are specified in table A.17.9.1.2.1-1. The test parameters are as given in table A.17.9.1.2.1-2, table A.17.9.1.2.1-3 and table A.17.9.1.2.1-4.

Table A.17.9.1.2.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2. The UE is configured with DRX cycle of 0.64s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the UE before the start of the test.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation as specified in TS 37.355 [34], clause 6.5.12. The frequency hopping configurations are specified in clause A.3.31.

Table A.17.9.1.2.1-2: RSTD accuracy test parameters

Table A.17.9.1.2.1-3: RSTD accuracy OTA related test parameters

## A.17.9.1.2.2Test Requirements

The RSTD measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1A.16.2.

## A.17.9.2UE Rx-Tx Measurements

## A.17.9.2.1UE Rx-Tx measurement accuracy for single positioning frequency layer in FR2 SA without RX FH in RRC_INACTIVE mode

## A.17.9.2.1.1Test purpose and environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement accuracy without RX FH in RRC_INACTIVE mode is within the specified limits. This test will verify the requirements in clause 10.1A.18.2. The test is conducted in AWGN propagation condition in FR2 in standalone scenario.

The supported test configuration is listed in table A.17.9.2.1.1-1.

Table A.17.9.2.1.1-1: Supported test configurations.

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test. In nr-Multi-RTT-RequestLocationInformation, nr-DL-PRS-RxHoppingRequest is not present.

The UE is configured to transmit SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.17.9.2.1.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.17.9.2.1.2-1.

Table A.17.9.2.1.2-1: UE Rx-Tx time difference measurement accuracy test parameters

## A.17.9.2.1.3Test requirements

The UE Rx-Tx time difference measurement time fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1A.18.2 for both Cell 1 and Cell 2.

## A.17.9.2.2SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC_INACTIVE state in FR2

## A.17.9.2.2.1Test purpose and Environment

The purpose of the test is to verify that the UE Rx-Tx time difference measurement requirements with FH by RedCap UE in RRC_INACTIVE state are within the specified limits. This test will verify the requirements in clause 10.1A.18.2.3. The test is conducted in AWGN propagation condition in FR2 in standalone scenario.

The supported test configuration is listed in table A.17.9.2.2.1-1.

Table A.17.9.2.2.1-1: Supported test configurations

There are two cells in the test: PCell (Cell 1) and a neighbour cell (Cell 2). All cells are on the same RF channel in FR2.

The NR-Multi-RTT-ProvideAssistanceData and nr-Multi-RTT-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the UE before the start of the test. The test requirements apply when frequencyHopping is configured to UE.

The UE is configured to transmit SRS on Cell 1 during the test.

The test equipment measures the transmit timing of the UE using the transmitted SRS and measures the receive timing using the PRS. The test equipment then compares the difference of these two timings to the UE Rx-Tx measurement reported by the UE for each cell.

## A.17.9.2.2.2Test parameters

The UE Rx-Tx time difference accuracy test parameters are given in table A.17.9.2.2.2-1.

Table A.17.9.2.2.2-1: UE Rx-Tx time difference measurement accuracy test parameters

## A.17.9.2.2.3Test requirements

The UE Rx-Tx time difference measurement time fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.1A.18.2.3for both Cell 1 and Cell 2.

## A.17.9.3PRS-RSRP Measurements

A.17.9.3.1PRS-RSRP measurement accuracy without FH in RRC_INACTIVE state in FR2

A.17.9.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRP measurement without FH by a RedCap UE in RRC_INACTIVE is within the specified limits. This test will verify the requirements in clauses 10.1A.17.2.1 for absolute accuracy and 10.1A.17.2.2 for relative accuracy.

A.17.9.3.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.9.3.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in table A.17.9.3.1.2-2 and A.17.9.3.1.2-3. In all test cases, Cell 1 is the PCell.

Table A.17.9.3.1.2-1: PRS-RSRP supported test configurations

Table A.17.9.3.1.2-2: PRS-RSRP general test parameters

Table A.17.9.3.1.2-3: PRS-RSRP OTA related test parameters

A.17.9.3.1.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1 if the reported PRS-RSRP is in the range shown in table A.17.9.3.1.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2.

Table A.17.9.3.1.3-1: PRS-RSRP absolute accuracy test requirement

## A.17.9.3.2PRS-RSRP measurement accuracy with FH in RRC_INACTIVE state in FR2

## A.17.9.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the accuracy of PRS-RSRP measurement with FH by a RedCap UE in RRC_INACTIVE is within the specified limits. This test will verify the requirements in clauses 10.1A.17.2.1 for absolute accuracy and 10.1A.17.2.2 for relative accuracy.

## A.17.9.3.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.9.3.2.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in table A.17.9.3.2.2-2 and A.17.9.3.2.2-3. In all test cases, Cell 1 is the PCell. PRS RX hopping is present in NR-DL-AoD-RequestLocationInformation.

Table A.17.9.3.2.2-1: PRS-RSRP supported test configurations

Table A.17.9.3.2.2-2: PRS-RSRP general test parameters

Table A.17.9.3.2.2-3: PRS-RSRP OTA related test parameters

## A.17.9.3.2.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1 if the reported PRS-RSRP is in the range shown in table A.17.9.3.2.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2.

Table A.17.9.3.2.3-1: PRS-RSRP absolute accuracy test requirement

## A.17.9.4PRS-RSRPP Measurements

## A.17.9.4.1SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_INACTIVE state in FR2

## A.17.9.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRPP measurement accuracy in RRC_INACTIVE state is within the specified limits. This test will verify the requirements in clauses 10.1A.19.2.

## A.17.9.4.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.9.4.1.2-1. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.17.9.4.1.2-2 and TRS configuration for Cell 1 is defined in table A.17.9.4.1.2-2.

Table A.17.9.4.1.2-1: PRS-RSRPP supported test configurations

Table A.17.9.4.1.2-2: PRS-RSRPP general test parameters

TableA.17.9.4.1.2-3: PRS-RSRPP OTA related test parameters

## A.17.9.4.1.3Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.19.2. if the reported PRS-RSRPP is in the range shown in table A.17.9.4.1.3-1.

Table A.17.9.4.1.3-1: PRS-RSRPP absolute accuracy test requirement

## A.17.9.4.2SA: PRS-RSRPP measurement accuracy with Rx FH in RRC_INACTIVE state in FR2

## A.17.9.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRPP measurement accuracy in RRC_INACTIVE state with FH by a RedCap UE is within the specified limits. This test will verify the requirements in clauses 10.1A.19.2.

## A.17.9.4.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.9.4.2.2-1. In all test cases, Cell 1 is the PCell. The TCI status for Cell 1 is defined in table A.3.16.2-1 and TRS configuration for Cell 1 is defined in table A.17.9.4.2.2-1.

Table A.17.9.4.2.2-1: PRS-RSRPP supported test configurations

Table A.17.9.4.2.2-2: PRS-RSRPP general test parameters

Table A.17.9.4.2.2-3: PRS-RSRPP OTA related test parameters

## A.17.9.4.2.3Test Requirements

In each test, the absolute PRS-RSRPP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.19.2, if the reported PRS-RSRPP is in the range shown in table A.17.9.4.2.3-1.

Table A.17.9.4.2.3-1: PRS-RSRPP absolute accuracy test requirement

## A.17.10Measurement Procedure for RedCap in RRC_IDLE

## A.17.10.1RSTD Measurements

## A.17.10.1.1NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA in RRC_IDLE state without eDRX

## A.17.10.1.1.1Test Purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC IDLE state and without eDRX meets the requirements specified in clause 4.6.2.5 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.17.10.1.1.1-1.

Table A.17.10.1.1.1-1: Supported test configurations for NR RSTD

In the test there are three synchronous cells: Cell 1, Cell 2 and Cell 3. Cell 1 is the reference as well as the PCell. Cell 2 and Cell 3 are the neighbour cells. All cells are on the same RF channel distributed in single positioning frequency layers.

The test consists of two consecutive time intervals, with duration of T1 and T2. During time duration T1, the UE shall be in RRC_CONNECTED state and shall not have any timing information of Cell 2 and Cell3. During T2 UE shall be in RRC_IDLE state and all cells transmit PRS resources within initial DL BWP of the UE and with the same numerology as the initial DL BWP.

Note: The information on when PRS is muted is conveyed to the UE using PRS muting information.

The NR-DL-TDOA-ProvideAssistanceData and nr-DL-TDOA-RequestLocationInformation as defined in TS 37.355 [34], clause 6.5.12.1, shall be provided to the RedCap UE during T1. The measurement reporting delay test in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The last TTI containing the two messages shall be provided to the RedCap UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the DL-TDOA assistance data and location information request.

The beginning of the time interval T2 shall be aligned with the first DRX cycle containing a DL PRS resource(s).

The UE is configured with DRX cycle of 0.64 s.

The general test parameters are listed in table A.17.10.1.1.1-2, and cell specific test parameters are listed in table A.17.10.1.1.1-3 and table A.17.10.1.1.1-4.

Table A.17.10.1.1.1-2: General test parameters for RSTD measurement reporting delay

Table A.17.10.1.1.1-3: Cell-specific test parameters for RSTD measurement reporting delay during T1

Table A.17.10.1.1.1-4: Cell-specific test parameters for RSTD measurement reporting delay during T2

## A.17.10.1.1.2Test Requirements

The RSTD measurement time without FH for RedCap fulfils the requirements specified in clause 4.6.2.5.

The UE shall perform and report the RSTD measurements for Cell 2 and Cell 3 with respect to the reference cell in the DL-TDOA assistance data, Cell 1, within the time duration specified in clause 4.6.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3, i.e., between RSTD_0000000 and RSTD_1970049.

## A.17.10.1.2NR RSTD without FH measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC_IDLE state with eDRX > 10.24s

## A.17.10.1.2.1Test purpose and environment

The purpose of the test is to verify the measurement requirements specified in clause 4.6.2.5 for RSTD measurements in RRC_IDLE with eDRX and periodic reporting. Refer to clause A.7.10.1.2.1 for test configuration and procedure.

## A.17.10.1.2.2Test requirements

The RSTD measurement time shall fulfill the requirements specified in clause 4.6.2.5.

The UE shall perform and report the RSTD measurements for Cell 1, Cell 2 and Cell 3 within the specified measurement period duration starting from the beginning of time interval T2. The requirement shall be evaluated based on the first measurement report received from the UE.

NOTE 1:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

NOTE 2:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each neighbour cell observed during repeated tests shall be at least 90%, where the reported RSTD measurement for each correct event shall be within the RSTD reporting range specified in clause 10.1A.16.3.

## A.17.10.2PRS-RSRP Measurements

## A.17.10.2.1PRS-RSRP measurement delay test case for single positioning frequency layer in RRC_IDLE

## A.17.10.2.1.1Test Purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement without RX FH in RRC_IDLE in FR2 meets the delay requirements specified in clause 4.6.3.5 for single positioning frequency layer under AWGN propagation conditions in standalone scenario. Supported test configurations are shown in table A.17.10.2.1.1-1.

There are two cells in the test, PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2. Both cells transmit PRS during T2.

The NR-DL-AoD-RequestLocationInformation message and NR-DL-AoD-ProvideAssistanceData message as defined in TS 37.355 [34] shall be provided to the UE during T1. The last slot containing the two messages for the assistance data and location information request is denoted as #n. In the DL slot next to slot #n, UE is released into RRC_IDLE. PRS RX FH is not requested in NR-DL-AoD-RequestLocationInformation.

The beginning of the time interval T2 shall be aligned with the beginning of the first MG instance containing the PRS resources that is DT after slot #n, where DT = 50 ms is the maximum processing time of the assistance data and location information request.

The test parameters are as given in table A.17.10.2.1.1-2 and table A.17.10.2.1.1-3.

Table A.17.10.2.1.1-1: Supported test configurations for PRS-RSRP measurement reporting delay

Table A.17.10.2.1.1-2: General test parameters for PRS-RSRP measurement reporting delay

Table A.17.10.2.1.1-3: Cell-specific test parameters for PRS-RSRP measurement reporting delay

## A.17.10.2.1.2Test Requirements

The PRS-RSRP measurement time fulfils the requirements specified in clause 4.6.3.5. The UE shall perform and report the PRS-RSRP measurements for Cell 2 with respect to the reference cell in the DL-AoD assistance data, Cell 1, within the time duration specified in clause 4.6.3.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be higher than the time duration above because of the uncertainty in acquiring the first available PRACH occasion to transition to RRC_CONNECTED state to report the measurements.

The rate of the correct events for the neighbour cell observed during repeated tests shall be at least 90%, where the reported PRS-RSRP measurement for each correct event shall be within the PRS-RSRP reporting range specified in clause 10.1.24.3, i.e., between PRS-RSRP_0 and PRS-RSRP_126.

## A.17.10.2.2PRS-RSRP reporting delay test case in RRC_IDLE state in FR2 when eDRX cycle > 10.24s

## A.17.10.2.2.1Test Purpose and Environment

The purpose of the test is to verify the PRS RSRP measurement requirements specified in clause 4.6.3.5 for single positioning frequency layer under AWGN propagation conditions in RRC_IDLE when configured with eDRX.

The supported test configurations in table A.17.8.3.3.1-1 apply for this test.

The test procedure in clause A.17.8.3.3.1 apply for this test, except that during T2, UE is in RRC_IDLE state.

The general test parameters as specified in table A.17.8.3.3.1-2 apply for this test, except those specified in table A.17.10.2.2.1-1.

The cell specific test parameters as specified in table A.17.8.3.3.1-3 apply for this test.

Table A.17.10.2.2.1-1: General test parameters for PRS RSRP measurement reporting delay

## A.17.10.2.2.2Test Requirements

The test requirements in clause A.17.8.3.3.2 apply for this test, except that the time limits are specified in clause 4.6.3.5.

## A.17.11Measurement Performance Requirements for RedCap in RRC_IDLE

## A.17.11.1RSTD Measurements

## A.17.11.1.1RSTD measurement accuracy test case for RedCap UE without FH in FR2 in RRC_IDLE state without eDRX

## A.17.11.1.1.1Test purpose and Environment

The purpose of the test is to verify that the RSTD measurement for RedCap UE without FH in RRC_IDLE state and without eDRX meets the accuracy requirements specified in clause 10.1A.16.2 in an environment with AWGN propagation conditions in FR2 in standalone scenario when single positioning frequency layer is configured.

The supported test configurations are specified in table A.17.11.1.1.1-1.

Table A.17.11.1.1.1-1: Supported test configurations

In the test there are two synchronous cells: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2. The UE is configured with DRX cycle of 0.64 s. The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the RedCap UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 4.6.2.5.

The RSTD measurement accuracy in this clause is valid for the cases where the RedCap UE is either not configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation or the RedCap UE is configured by the LMF to perform RSTD measurement with RX FH via NR-DL-TDOA-RequestLocationInformation but reports the RSTD measurement based on the single hop in NR-DL-TDOA-SignalMeasurementInformation as specified in TS 37.355 [34], clause 6.5.12.

The accuracy test parameters and OTA related test parameters are as given in table A.17.11.1.1.1-2 and table A.17.11.1.1.1-3, respectively.

Table A.17.11.1.1.1-2: RSTD accuracy test parameters

Table A.17.11.1.1.1-3: RSTD accuracy OTA related test parameters

## 11.1.1.2Test Requirements

The RSTD measurement accuracy shall fulfil the absolute requirement in clause 10.1A.16.2.

## A.17.11.1.2RSTD without FH measurement accuracy test case for single positioning frequency layer in FR2 SA in RRC_IDLE state with eDRX > 10.24s

## A.17.11.1.2.1Test purpose and environment

The purpose of this test is to verify that RSTD measurements performed in RRC_IDLE with eDRX and periodic reporting satisfy the measurement accuracy requirements specified in clause 10.1A.16.2. The tests are conducted under AWGN propagation condition with the UE operating in FR2 stand-alone mode and configured to perform RSTD measurements on a single positioning frequency layer (PFL) in FR2.

The supported test configurations are listed in table A.17.11.1.2.1-1.

Table A.17.11.1.2.1-1: Supported test configurations

There are two synchronous cells in the test: Cell 1 and Cell 2. Cell 1 is the reference as well as the PCell. Cell 2 is a neighbour cell. Both cells are on the same NR RF channel in FR2.

The NR-TDOA-ProvideAssistanceData and NR-TDOA-RequestLocationInformation message as defined in TS 37.355 [34] shall be provided to the UE before the start of the test. The test duration should be larger than the UE measurement period as defined in clause 4.5.2.5.

The general test parameters and cell specific test parameters are as given in table A.17.11.1.2.1-2 and table A.17.11.1.2.1-3, respectively.

Table A.17.11.1.2.1-2: General test parameters

Table A.17.11.1.2.1-3: Cell specific test parameters

## A.17.11.1.2.2Test requirements

The reported RSTD measurements shall fulfill the absolute accuracy requirements specified in clause 10.1A.16.2.

## A.17.11.2PRS-RSRP Measurements

## A.17.11.2.1PRS-RSRP measurement accuracy test case for RedCap UE in FR2 in RRC_IDLE state

## A.17.11.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the PRS-RSRP measurement accuracy for 2Rx RedCap UE in RRC_IDLE is within the specified limits in FR2. This test will verify the requirements in clauses 10.1A.17.2.1 and 10.1A.17.2.2, when the PRS-RSRP measurement is performed without RX FH.

## A.17.11.2.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.17.11.2.1.2-1. Both absolute and relative accuracy of PRS-RSRP measurements are tested by using the parameters in table A.17.11.2.1.2-2 and A.17.11.2.1.2-3. In all test cases, Cell 1 is the PCell.

Table A.17.11.2.1.2-1: PRS-RSRP supported test configurations

Table A.17.11.2.1.2-2: PRS-RSRP general test parameters.

Table A.17.11.2.1.2-3: PRS-RSRP OTA related test parameters

A.17.11.2.1.3Test Requirements

In each test, the absolute PRS-RSRP measurement for each cell shall fulfil the absolute accuracy requirement in clause 10.1A.17.2.1 when the PRS-RSRP measurement is performed without RX FH and if the reported PRS-RSRP is in the range shown in table A.17.11.2.1.3-1. The relative PRS-RSRP measurement between the two PRS resources within the same cell shall fulfil the relative accuracy requirement in clause 10.1A.17.2.2 when the PRS-RSRP measurement is performed without RX FH.

Table A.17.11.2.1.3-1: PRS-RSRP absolute accuracy test requirement

## A.17.11.2.2PRS-RSRP measurement accuracy test case in RRC_IDLE state in FR2 when eDRX cycle > 10.24s

## A.17.11.2.2.1Test purpose and Environment

The purpose of the test is to verify that the PRS-RSRP measurement in RRC_IDLE with eDRX meets the accuracy requirements specified in clause 10.1A.17.2.1 and 10.1A.17.2.2 in an environment with AWGN propagation conditions.

## A.17.11.2.2.1Test parameters

The supported test configurations in table A.17.9.3.1.2-1 apply for this test.

The test procedure in clause A.17.9.3.1.2 apply for this test, except that UE is in RRC_IDLE state.

The general test parameters as specified in table A.17.9.3.1.2-2 apply for this test, except those additionally specified in table A.17.11.2.2.1-1.

The OTA related test parameters in table A.17.9.3.1.2-3 apply for this test.

Table A.17.11.2.2.1-1: PRS-RSRP test parameters

## A.17.11.2.2.2Test Requirements

The test requirements in clause A.17.9.3.1.3 apply for this test.

## A.18E-UTRA standalone tests for NR RRM for RedCap

## A.18.1RRC_IDLE state mobility

## A.18.1.1Inter-RAT NR Cell re-selection

## A.18.1.1.1E-UTRA Cell reselection to higher priority NR target Cell in FR1

## A.18.1.1.1.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN to NR inter-RAT cell reselection requirements for 2Rx RedCap specified in clause 4.2.2.5.8 in TS 36.133 [15].

The test scenario comprises of 1 E-UTRA cell and 1 NR cell as given in tables A.18.1.1.1.1-1, A.18.1.1.1.1-2, A.18.1.1.1.1-3 and A.18.1.1.1.1-4. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. E-UTRA Cell 1 is already identified by the UE prior to the start of the test. Cell 2 is of higher priority than Cell 1.

Table A.18.1.1.1.1-1: Supported test configurations

Table A.18.1.1.1.1-2: General test parameters for E-UTRA cell re-selection FR1 NR cell test case

Table A.18.1.1.1.1-3: Cell specific test parameters for NR Cell 2

Table A.18.1.1.1.1-4: Cell specific test parameters for E-UTRA Cell 1

## A.18.1.1.1.2Test Requirements

The cell reselection delay to a higher priority NR cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 2 and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, NR + TSI-NR,

Where:

Thigher_priority_searchSee clause 4.2.2 in TS 36.133 [15]

Tevaluate, NRSee Table 4.2.2.5.6-1 in clause 4.2.2.5.6 in TS 36.133 [15]

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority NR cell and 7.68 s for the cell re-selection delay to a lower priority cell in the test case, which we allow 8 s.

## A.18.2RRC_CONNECTED state mobility

## A.18.2.1Handover

## A.18.2.1.1E-UTRAN - NR handover in FR1

## A.18.2.1.1.1Test Purpose and Environment

This test shall verify the E-UTRAN to NR FR1 handover requirements for 2RX RedCap as specified in clause 5.3.4B in TS 36.133 [15].

The test comprises of one E-UTRA carrier and one NR carrier. There are two cells and one cell on each carrier. Cell 1 is the E-UTRAN and Cell 2 is an inter-RAT NR neighbour cell. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in table 8.1.2.1-1 of TS 36.133 [15] is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2 after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.18.2.1.1-1. General test parameters are provided in table A.18.2.1.1-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.18.2.1.1-3 and A.18.2.1.1-4 respectively.

Table A.18.2.1.1-1: Supported test configurations for E-UTRAN inter-RAT NR handover

Table A.18.2.1.1-2: General test parameters for E-UTRAN inter-RAT NR handover

Table A.18.2.1.1-3: Cell specific test parameters for E-UTRAN inter-RAT NR handover (Cell 1)

Table A.18.2.1.1-4: Cell specific test parameters E-UTRAN inter-RAT NR handover (Cell 2)

## A.18.2.1.1.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 112 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and is specified in TS36.133.

Tinterrupt = 62 ms in the test; Tinterrupt is defined in TS36.133 clause 5.3.4.3.

This gives a total of 112 ms.

## A.18.2.2RRC connection release with redirection

## A.18.2.2.1Redirection from E-UTRA to NR FR1 for redcap UE

## A.18.2.2.1.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from E-UTRA to NR requirements for 2Rx RedCap specified in 36.133 clause 6.3.2.6.

## A.18.2.2.1.2Test Parameters

Supported test configurations are shown in table A.18.2.2.1.2-1. The time delay is tested by using the parameters in table A.18.2.2.1.2-2, A.18.2.2.1.2-3, and A.18.2.2.1.2-4.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCConnectionRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.18.2.2.1.2-1: Redirection from E-UTRAN to NR test configurations

Table A.18.2.2.1.2-2: General test parameters for Redirection from E-UTRAN to NR test case

Table A.18.2.2.1.2-3: Cell specific test parameters for Redirection from E-UTRAN to NR test case (Cell 1)

Table A.18.2.2.1.2-4: Cell specific test parameters for Redirection from E-UTRAN to NR test case (Cell 2)

## A.18.2.2.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2240 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_NR_RedCap = TRRC_procedure_delay + Tidentify-NR_Redcap + TSI-NR_RedCap + TRACH_RedCap,

where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR_Redcap = 680 ms.

TSI-NR_RedCap = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH_RedCap = 170 ms in the test.

This gives a total of 2240 ms.

## A.18.3Measurement procedure

## A.18.3.1E-UTRA – NR Inter-RAT Measurements

## A.18.3.1.1NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used

## A.18.3.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements for 2Rx RedCap specified in clause 8.20.2.2 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1. The test parameters are given in tables A.18.3.1.1.1-1, A.18.3.1.1.1-2, A.18.3.1.1.1-3 and A.18.3.1.1.1-4.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.18.3.1.1.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

Table A.18.3.1.1.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

Table A.18.3.1.1.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

Table A.18.3.1.1.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

## A.18.3.1.1.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1, the UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.18.3.1.2NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used

## A.18.3.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements for 2Rx RedCap specified in clause 8.20.2.2 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1. The test parameters are given in tables A.18.3.1.2.1-1, A.18.3.1.2.1-2, A.18.3.1.2.1-3 and A.18.3.1.2.1-4.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.18.3.1.2.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

Table A.18.3.1.2.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

Table A.18.3.1.2.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

Table A.18.3.1.2.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

## A.18.3.1.2.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement In test 1 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 1080 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 10240 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.18.3.1.3NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used

## A.18.3.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements for 2Rx RedCap specified in clause 8.20.2.2of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1.  The test parameters are given in tables A.18.3.1.3.1-1, A.18.3.1.3.1-2, A.18.3.1.3.1-3 and A.18.3.1.3.1-4.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2..

Table A.18.3.1.3.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

Table A.18.3.1.3.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

Table A.18.3.1.3.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

Table A.18.3.1.3.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

## A.18.3.1.3.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 1040 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1, the UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.18.3.1.4NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used

## A.18.3.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements for 2Rx RedCap specified in clause 8.20.2.2of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1. The test parameters are given in tables A.18.3.1.4.1-1, A.18.3.1.4.1-2, A.18.3.1.4.1-3 and A.18.3.1.4.1-4.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2

Table A.18.3.1.4.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

Table A.18.3.1.4.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

Table A.18.3.1.4.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

Table A.18.3.1.4.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

## A.18.3.1.4.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 1280 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 12160 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.18.3.1.5NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is not used

## A.18.3.1.5.1Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.20.2.2 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 1. The test parameters are given in tables A.18.3.1.5.1-1, A.18.3.1.5.1-2 and A.18.3.1.5.1-3.

The cell specific test parameters for E-UTRA cell1 as PCell are defined in clause A.3.7.2.2.

In test 1 measurement gap pattern configuration # 0 as defined in table A.18.3.1.5.1-2 is provided for RedCap UE that does not support per-FR gap and in test 2 no measurement gap pattern configuration  is provided for RedCap UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B1 (Inter RAT neighbour becomes better than threshold) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have timing information of NR Cell 2.

Table A.18.3.1.5.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR2 in non-DRX

Table A.18.3.1.5.1-2: General test parameters for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in non-DRX

Table A.18.3.1.5.1-3: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in non-DRX

## A.18.3.1.5.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D1 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-FR gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D2 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and test 2, the UE is not required to report SSB time index.

Table A.18.3.1.5.2-1: Test requirements for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in non-DRX

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.18.3.1.6NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is used

## A.18.3.1.6.1Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.20.2.2 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 1.  The test parameters are given in tables A.18.3.1.6.1-1, A.18.3.1.6.1-2 and A.18.3.1.6.1-3.

The cell specific test parameters for E-UTRA cell1 as PCell are defined in clause A.3.7.2.2.

In tests 1 and 2, measurement gap pattern configuration # 0 as defined in table A.18.3.1.6.1-2 is provided for RedCap UE that does not support per-FR gap and in tests 3 and 4, no measurement gap pattern configuration is provided for RedCap UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B1 (Inter RAT neighbour becomes better than threshold) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have timing information of NR Cell 2.

Table A.18.3.1.6.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR2 in DRX

Table A.18.3.1.6.1-2: General test parameters for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in DRX

Table A.18.3.1.6.1-3: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in DRX

## A.18.3.1.6.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D1 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D2 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 3 with per-FR gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D3 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 4 with per-FR gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D4 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1, 2, 3 and 4, the UE is not required to report SSB time index.

Table A.18.3.1.6.2-1: Test requirements for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in DRX

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.18.3.1.7NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is not used

## A.18.3.1.7.1Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.20.2.2 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 1. The test parameters are given in tables A.18.3.1.7.1-1, A.18.3.1.7.1-2 and A.18.3.1.7.1-3.

The cell specific test parameters for E-UTRA cell1 as PCell are defined in clause A.3.7.2.2.

In test 1 measurement gap pattern configuration # 0 as defined in table A.18.3.1.7.1-2 is provided for RedCap UE that does not support per-FR gap and in test 2 no measurement gap pattern configuration is provided for RedCap UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B1 (Inter RAT neighbour becomes better than threshold) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.18.3.1.7.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR2 in non-DRX

Table A.18.3.1.7.1-2: General test parameters for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in non-DRX

Table A.18.3.1.7.1-3: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in non-DRX

## A.18.3.1.7.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D1 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-FR gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D2 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and test 2, the UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

Table A.18.3.1.7.2-1: Test requirements for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in non-DRX

## A.18.3.1.8NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is used

## A.18.3.1.8.1Test Purpose and Environment

The purpose of this test is to verify that the RedCap UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.20.2.2 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.20.2.3 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 1. The test parameters are given in tables A.18.3.1.8.1-1, A.18.3.1.8.1-2 and A.18.3.1.8.1-3.

The cell specific test parameters for E-UTRA cell1 as PCell are defined in clause A.3.7.2.2.

In tests 1 and 2, measurement gap pattern configuration # 0 as defined in table A.18.3.1.8.1-2 is provided for RedCap UE that does not support per-FR gap and in tests 3 and 4, no measurement gap pattern configuration #4 is provided for RedCap UE that supports per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B1 (Inter RAT neighbour becomes better than threshold) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.18.3.1.8.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR2 in DRX

Table A.18.3.1.8.1-2: General test parameters for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in DRX

Table A.18.3.1.8.1-3: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR2 with SSB time index detection

## A.18.3.1.8.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D1 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D2 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 3 with per-FR gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D3 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 4 with per-FR gap, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D4 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1, 2, 3 and 4, the UE is required to report SSB time index.

Table A.18.3.1.8.2-1: Test requirements for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in DRX

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.
