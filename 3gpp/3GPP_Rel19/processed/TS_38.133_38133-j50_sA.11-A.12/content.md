---
type: spec
aliases:
  - 38.133_38133-j50_sA.11-A.12
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.11-A.12/content.md"
---
# TS 38.133 38133-j50_sA.11-A.12

## A.11NR Standalone Tests with NR PCell under CCA and Other NR Cells in FR1

Editor’s note: Test cases for NR SA with NR PCell under CCA and SCell under CCA are also included here.

## A.11.1RRC_IDLE state mobility

## A.11.1.1Cell re-selection with both source and target NR carrier frequencies under CCA

## A.11.1.1.1Cell reselection to FR1 intra-frequency NR cells when subject to CCA on the serving and target cell

## A.11.1.1.1.1Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements subject to CCA specified in clause 4.2A.2.3. Supported test configurations are shown in table A.11.1.1.1.2-1.

## A.11.1.1.1.2Test Parameters

The test scenario comprises of 1 NR carrier that is subject to CCA and 2 cells as given in tables A.11.1.1.1.2-1, A.11.1.1.1.2-2 and A.11.1.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.11.1.1.1.2-1: Supported test configurations

Table A.11.1.1.1.2-2: General test parameters for intra frequency NR cell re-selection test case when subject to CCA

Table A.11.1.1.1.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case in AWGN when subject to CCA

## A.11.1.1.1.3Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than (25 + Md)*1.28 + TSI_CCA s. Md is the number of DRX cycles with at least one SMTC where there are no SSBs available during the Tdetect,NR_Intra_CCA. If Md > Md,max the UE is required to restart the detection of Cell 2.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than (5+Me)*1.28 + TSI_CCA s. Me is the number of DRX cycles with at least one SMTC where there are no SSBs available during the Tevaluate,NR_Intra_CCA. If Me > Me,max the UE is required to restart the evaluation of Cell 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra_CCA + TSI_CCA, and to an already detected cell can be expressed as: Tevaluate, NR_ intra_CCA + TSI_CCA,

Where:

-Tdetect, NR_Intra_CCASee Table 4.2A.2.3-1 in clause 4.2A.2.3

-Tevaluate, NR_ intra_CCASee Table 4.2A.2.3-1 in clause 4.2A.2.3

-TSI_CCAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell.

This gives a total of (25 + Md)*1.28 + TSI_CCA s for the cell re-selection delay to a newly detectable cell and (5+Me)*1.28 + TSI_CCA s for the cell re-selection delay to an already detected cell in the test case.

## A.11.1.1.2Cell reselection to FR1 inter-frequency NR case when subject to CCA on the serving and target cell

## A.11.1.1.2.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements subject to CCA specified in clause 4.2A.2.4. Supported test configurations are shown in table A.11.1.1.2.2-1.

## A.11.1.1.2.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers that are subject to CCA respectively as given in tables A.11.1.1.2.2-1, A.11.1.1.2.2-2 and A.11.1.1.2.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

Table A.11.1.1.2.2-1: Supported test configurations

Table A.11.1.1.2.2-2: General test parameters for FR1 inter frequency NR cell re-selection test case when subject to CCA

Table A.11.1.1.2.2-3: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case in AWGN

## A.11.1.1.2.3Test Requirements

The cell reselection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps again on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 60 + 1.28 x (5 + Me) + TSI_CCA s. Me is the number of DRX cycles with at least one SMTC where there are no SSBs available during the Tevaluate,NR_Intra_CCA. If Me > Me,max the UE is required to restart the evaluation of Cell 2.

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to a lower priority cell shall be less than 1.28 x (5 + Me) + TSI_CCA s. Me is the number of DRX cycles with at least one SMTC where there are no SSBs available during the Tevaluate,NR_Intra_CCA. If Me > Me,max the UE is required to restart the evaluation of Cell 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter_CCA + TSI_CCA, and to a lower priority cell can be expressed as: Tevaluate, NR_ inter_CCA + TSI_CCA,

Where:

-Thigher_priority_searchSee clause 4.2.2.7

-Tevaluate, NR_ inter_CCASee Table 4.2A.2.4-1 in clause 4.2A.2.4

-TSI_CCAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell.

This gives a total of 60 + 1.28 x (5 + Me) + TSI_CCA s for the cell re-selection delay to a higher priority cell and 1.28 x (5 + Me) + TSI_CCA s for the cell re-selection delay to a lower priority cell in the test case.

## A.11.1.2Cell re-selection to NR with source NR carrier frequency under CCA

## A.11.1.2.1Cell reselection to FR1 inter-frequency NR case when serving cell is subject to CCA

## A.11.1.2.1.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements specified in clause 4.2.2.4 when the serving cell is subject to CCA. Supported test configurations are shown in table A.11.1.2.1.2-1.

## A.11.1.2.1.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers where the first carrier is subject to CCA as given in tables A.11.1.2.1.2-1, A.11.1.2.1.2-2 and A.11.1.2.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

Table A.11.1.2.1.2-1: Supported test configurations

Table A.11.1.2.1.2-2: General test parameters for FR1 inter frequency NR cell re-selection test case when serving cell is subject to CCA

Table A.11.1.2.1.2-3: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case in AWGN when serving cell is subject to CCA

## A.11.1.2.1.3Test Requirements

The cell reselection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps again on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 60 + 1.28 x (5 + Me) + TSI_CCA s. Me is the number of DRX cycles with at least one SMTC where there are no SSBs available during the Tevaluate,NR_Intra_CCA. If Me > Me,max the UE is required to restart the evaluation of Cell 2.

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to a lower priority cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter_CCA + TSI_CCA, and to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR.

Where:

-Thigher_priority_searchSee clause 4.2.2.7

-Tevaluate, NR_ inter_CCASee Table 4.2A.2.4-1 in clause 4.2A.2.4

-TSI_CCAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell.

-Tevaluate, NR_ interSee Table 4.2.2.4-1 in clause 4.2.2.4

-TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test cases.

This gives a total of 60 + 1.28 x (5 + Me) + TSI_CCA s for the cell re-selection delay to a higher priority cell and 7.68 s for the cell re-selection delay to a lower priority cell in the test case, which we allow 8 s.

## A.11.1.3Cell re-selection from NR carrier with target NR carrier frequency under CCA

## A.11.1.3.1Cell reselection to FR1 inter-frequency NR case when target cell is subject to CCA

## A.11.1.3.1.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements specified in clause  4.2A.2.4 when the target cell is subject to CCA. Supported test configurations are shown in table A. 11.1.3.1.2-1.

## A.11.1.3.1.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers where the second carrier is subject to CCA as given in tables A.11.1.3.1.2-1, A.11.1.3.1.2-2 and A.11.1.3.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

Table A.11.1.3.1.2-1: Supported test configurations

Table A.11.1.3.1.2-2: General test parameters for FR1 inter frequency NR cell re-selection test case when target cell is subject to CCA

Table A.11.1.3.1.2-3: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case in AWGN when target cell is subject to CCA

## A.11.1.3.1.3Test Requirements

The cell reselection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps again on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

## 1.28 x (5 + Me) + TSI_CCA s. Me is the number of DRX cycles with at least one SMTC where there are no SSBs available during the Tevaluate,NR_Intra_CCA. If Me > Me,max the UE is required to restart the evaluation of Cell 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR.

Where:

-Thigher_priority_searchSee clause 4.2.2.7

-Tevaluate, NR_ inter_CCASee Table 4.2A.2.4-1 in clause 4.2A.2.4

-TSI_CCAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell.

-Tevaluate, NR_ interSee Table 4.2.2.4-1 in clause 4.2.2.4

-TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority cell and 1.28 x (5 + Me) + TSI_CCA s for the cell re-selection delay to a lower priority cell in the test case.

## A.11.1.4Inter-RAT cell re-selection to E-UTRAN with source NR carrier frequency under CCA

## A.11.1.4.1Cell reselection to higher priority E-UTRAN when serving cell is subject to CCA

## A.11.1.4.1.1Test Purpose and Environment

This test is to verify the requirement for the NR cell subject to CCA to E-UTRAN inter-RAT cell reselection requirements specified in clause 4.2A.2.5 when the E-UTRAN cell is of higher priority.

## A.11.1.4.1.2Test Parameters

The test scenario comprises of one NR cell which is subject to CCA and one E-UTRAN cell as given in tables A.11.1.4.1.2-1, A.11.1.4.1.2-2, A.11.1.4.1.2-3 and A.11.1.4.1.2-4. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. NR Cell 1 is already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of higher priority than Cell 1.

Table A.11.1.4.1.2-1: Supported test configurations

Table A.11.1.4.1.2-2: General test parameters for NR cell subject to CCA to E-UTRAN cell re-selection test case

Table A.11.1.4.1.2-3: Cell specific test parameters for NR Cell 1 subject to CCA

Table A.11.1.4.1.2-4: Cell specific test parameters for E-UTRA Cell 2

## A.11.1.4.1.3Test Requirements

The cell reselection delay to a higher priority E-UTRAN cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, E-UTRAN + TSI-E-UTRA,

Where:

-Thigher_priority_searchSee clause 4.2.2.7

-Tevaluate, E-UTRANSee Table 4.2.2.5-1 in clause 4.2.2.5

-TSI-E-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority E-UTRAN cell.

## A.11.1.4.2Cell reselection to lower priority E-UTRAN when serving cell is subject to CCA

## A.11.1.4.2.1Test Purpose and Environment

This test is to verify the requirement for the NR cell subject to CCA to E-UTRAN inter-RAT cell reselection requirements specified in clause 4.2A.2.5 when the E-UTRAN cell is of lower priority.

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A.11.1.4.2.1-1, A.11.1.4.2.1-2, A.11.1.4.2.1-3 and A.11.1.4.2.1-4. The test consists of three successive time periods, with time duration of T1 and T2 respectively. Both NR Cell 1 and E-UTRAN Cell 2 are already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of lower priority than Cell 1.

Table A.11.1.4.2.1-1: Supported test configurations

Table A.11.1.4.2.1-2: General test parameters for NR cell subject to CCA to E-UTRAN cell re-selection test case

Table A.11.1.4.2.1-3: Cell specific test parameters for NR Cell 1 subject to CCA

Table A.11.1.4.2.1-4: Cell specific test parameters for E-UTRA Cell 2

## A.11.1.4.2.2Test Requirements

The cell reselection delay to a lower priority E-UTRAN cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a lower priority cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, E-UTRAN + TSI-E-UTRA,

Where:

-Tevaluate, E-UTRANSee Table 4.2.2.5-1 in clause 4.2.2.5

-TSI-E-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 7.68 s, allow 8 s for the cell re-selection delay to a lower priority E-UTRAN cell.

## A.11.2RRC_CONNECTED state mobility

## A.11.2.1Handover

## A.11.2.1.1Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; known target cell

## A.11.2.1.1.1Test Purpose and Environment

This test is to verify the requirement for the NR intra frequency handover requirements from FR1 carrier under CCA to FR1 carrier under CCA specified in clause 6.1B.1.2.

## A.11.2.1.1.2Test Parameters

Supported test configurations are shown in table A.11.2.1.1.2-1. Both handover delay and interruption length are tested by using the parameters in table A.11.2.1.1.2-2, and A.11.2.1.1.2-3.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

NR shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.11.2.1.1.2-1: Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA test configurations

Table A.11.2.1.1.2-2: General test parameters Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA

Table A.11.2.1.1.2-3: Cell specific test parameters for NR FR1-FR1 Intra frequency handover test case

## A.11.2.1.1.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than Tinterrupt from the beginning of time period T3, where Tinterrupt is defined in clause 6.1B.1.2

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin

Tsearch = 0.

Tprocessing = 20 ms.

Tmargin = 2 ms.

T∆ = (1+ L2) *20 ms.

TIU = (1+ L3)*10 + 10 ms

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2], L2 is the number of SMTC occasions not available at the UE during the time tracking period where L2  LCCA_DL, and L3 is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure, where L3  LCCA_UL. L3 = 0 for Type 2C UL channel access procedure as defined in TS 37.213 [33]. The interruption time considering the potential extensions caused by L1, L2 , L3  and by the UL CCA failure detection/recovery mechanism is limited by the T304 timer. The UE behaviour at the T304 timer expiry is detailed in TS 38.331 [2]. Test equipment should make sure that LCCA_DL and LCCA_UL are not exceeded during a test by monitoring the number of CCA failures and preventing additional CCA failures from happening after LCCA_DL or LCCA_UL is reached.

## A.11.2.1.2Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; unknown target cell

## A.11.2.1.2.1Test Purpose and Environment

This test is to verify the requirement intra frequency handover requirements from FR1 carrier under CCA to FR1 carrier under CCA specified in clause 6.1B.1.2.

## A.11.2.1.2.2Test Parameters

Supported test configurations are shown in table A.11.2.1.2.2-1. Both handover delay and interruption length are tested by using the parameters in table A.11.2.1.2.2-2, and A.11.2.1.2.2-3.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.11.2.1.2.2-1: Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA test configurations

Table A.11.2.1.2.2-2: General test parameters Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA

Table A.11.2.1.2.2-3: Cell specific test parameters for NR FR1-FR1 Intra frequency handover test case

## A.11.2.1.2.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than Tinterrupt from the beginning of time period T3, where Tinterrupt is defined in clause 6.1B.1.2

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin

Tsearch = (1+L1)* 20 ms.

Tprocessing = 20 ms.

Tmargin = 2 ms.

T∆ = (1+ L2) *20 ms.

TIU = (1+ L3)*10 + 10 ms

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2], L1 is the number of SMTC occasions not available at the UE during the intra-frequency detection period, L2 is the number of SMTC occasions not available at the UE during the time tracking period, where L1 + L2  LCCA_DL, and L3 is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure, where L3  LCCA_UL. L3 = 0 for Type 2C UL channel access procedure as defined in TS 37.213 [33]. The interruption time considering the potential extensions caused by L1, L2 , L3  and by the UL CCA failure detection/recovery mechanism is limited by the T304 timer.

## A.11.2.1.3Inter-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; unknown target cell

## A.11.2.1.3.1Test Purpose and Environment

This test is to verify the requirement for inter frequency handover requirements from FR1 carrier under CCA to FR1 carrier under CCA specified in clause 6.1B.1.2.

## A.11.2.1.3.2Test Parameters

Supported test configurations are shown in table A.11.2.1.3.2-1. Both handover delay and interruption length are tested by using the parameters in table A.11.2.1.3.2-2, and A.11.2.1.3.2-3.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.11.2.1.3.2-1: Inter-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA test configurations

Table A.11.2.1.3.2-2: General test parameters Inter-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA

Table A.11.2.1.3.2-3: Cell specific test parameters for NR FR1-FR1 Inter frequency handover test case

## A.11.2.1.3.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than Tinterrupt from the beginning of time period T3, where Tinterrupt is defined in clause 6.1B.1.2

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin

Tsearch = (3+L1’)* 20 ms.

Tprocessing = 20 ms.

Tmargin = 2 ms.

T∆ = (1+ L2) *20 ms.

TIU = (1+ L3)*10 + 10 ms

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2], L1’ is the number of SMTC occasions not available at the UE during the inter-frequency detection period, L2 is the number of SMTC occasions not available at the UE during the time tracking period, where L1’ + L2  LCCA_DL, and L3 is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure, where L3  LCCA_UL. L3 = 0 for Type 2C UL channel access procedure as defined in TS 37.213 [33]. The interruption time considering the potential extensions caused by , L1, L2 , L3  and by the UL CCA failure detection/recovery mechanism is limited by the T304 timer.

## A.11.2.1.4Inter-frequency handover from FR1 carrier under CCA to FR1; known target cell

## A.11.2.1.4.1Test Purpose and Environment

This test is to verify the requirement for the NR with CCA FR1-NR FR1 handover requirements specified in clause 6.1.1.2.

## A.11.2.1.4.2Test Parameters

Supported test configurations are shown in table A.11.2.1.4.2-1. Both handover delay and interruption length are tested by using the parameters in table A.11.2.1.4.2-2, and A.11.2.1.4.2-3.

The test consists of three successive time periods, with time durations of T1 T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

NR with CCA shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.11.2.1.4.2-1: Handover from NR with CCA FR1 to NR FR1 test configuration

Table A.11.2.1.4.2-2: General test parameters handover from NR with CCA FR1 to NR FR1

Table A.11.2.1.4.2-3: Cell specific test parameters for NR with CCA FR1 – NR FR1 handover test case

## A.11.2.1.4.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 112 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 102 ms in the test. Tinterrupt is defined in clause 6.1.1.2.2.

This gives a total of 112 ms.

## A.11.2.1.5Inter-frequency handover from FR1 carrier under CCA to FR1; unknown target cell

## A.11.2.1.5.1Test Purpose and Environment

This test is to verify the requirement for the NR with CCA FR1-NR FR1 handover requirements specified in clause 6.1.1.2.

## A.11.2.1.5.2Test Parameters

Supported test configurations are shown in table A.11.2.1.5.2-1. Both handover delay and interruption length are tested by using the parameters in table A.11.2.1.5.2-2, and A.12.2.1.7.2-3.

The test scenario comprises of two carriers and one cell on each carrier. Cell 1 is the NR with CCA cell and Cell 2 is an NR neighbour cell. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2.

Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.11.2.1.5.2-1: Handover from NR with CCA FR1 to NR FR1 test configuration

Table A.11.2.1.5.2-2: General test parameters handover from NR with CCA FR1 to NR FR1

Table A.11.2.1.5.2-3: Cell specific test parameters for NR with CCA FR1 – NR FR1 handover test case

## A.11.2.1.5.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 132 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 122 ms in the test. Tinterrupt is defined in clause 6.1.1.2.2.

This gives a total of 132 ms.

## A.11.2.1.6Inter-frequency handover from FR1 to FR1 carrier under CCA; unknown target cell

## A.11.2.1.6.1Test Purpose and Environment

This test is to verify the requirement for inter frequency handover requirements from FR1 to FR1 carrier under CCA specified in clause 6.1B.1.2.

## A.11.2.1.6.2Test Parameters

Supported test configurations are shown in table A.11.2.1.6.2-1. Both handover delay and interruption length are tested by using the parameters in table A.11.2.1.6.2-2, and A.11.2.1.6.2-3.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.11.2.1.6.2-1: Inter-frequency handover from FR1 to FR1 carrier under CCA test configurations

Table A.11.2.1.6.2-2: General test parameters Inter-frequency handover from FR1 to FR1 carrier under CCA

Table A.11.2.1.6.2-3: Cell specific test parameters for NR FR1-FR1 Inter frequency handover test case

## A.11.2.1.6.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than Tinterrupt from the beginning of time period T3, where Tinterrupt is defined in clause 6.1B.1.2

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

Tinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin

Tsearch = (3+L1’)* 20 ms.

Tprocessing = 20 ms.

Tmargin = 2 ms.

T∆ = (1+ L2) *20 ms.

TIU = (1+ L3)*10 + 10 ms

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2], L1’ is the number of SMTC occasions not available at the UE during the inter-frequency detection period, L2 is the number of SMTC occasions not available at the UE during the time tracking period, and L3 is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure. L3 = 0 for Type 2C UL channel access procedure as defined in TS 37.213 [33]. The interruption time considering the potential extensions caused by L1, L1´, L2, L3  and by the UL CCA failure detection/recovery mechanism is limited by the T304 timer. The UE behaviour at the T304 timer expiry is detailed in TS 38.331 [2].

## A.11.2.1.7 SA NR FR1 carrier under CCA - E-UTRAN handover with known target cell

## A.11.2.1.7.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE can make correct inter-RAT E-UTRAN handover when operating in standalone (SA) operation with PCell in FR1 carrier under CCA. This test shall verify the NR to E-UTRAN handover requirements as specified in clause 6.1.2.1.

The test comprises of one NR carrier under CCA and one E-UTRA carrier. There are two cells and one cell on each carrier. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in table 9.1.2-1 is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2 after the UE has reported Event B2. The start of T3 is the next instant after the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.11.2.1.7-1. General test parameters are provided in table A.11.2.1.7-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.11.2.1.7-3 and A.11.2.1.7-4 respectively.

Table A.11.2.1.7-1: Supported test configurations for SA inter-RAT E-UTRAN handover tests

Table A.11.2.1.7-2: General test parameters for SA inter-RAT E-UTRAN handover

Table A.11.2.1.7-3: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 1)

Table A.11.2.1.7-4: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 2)

## A.11.2.1.7.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 85 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and is specified in clause 6.1.2.1.

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 6.1.2.1.

This gives a total of 85 ms.

## A.11.2.1.8SA NR FR1 carrier under CCA - E-UTRAN handover with unknown target cell

## A.11.2.1.8.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE can make correct inter-RAT E-UTRAN handover when operating in standalone (SA) operation with PCell in FR1 carrier under CCA. This test shall verify the NR to E-UTRAN handover requirements for the case when the target E-UTRAN cell is unknown as specified in clause 6.1.2.1.

The test comprises of one NR carrier under CCA and one E-UTRA carrier. There are two cells and one cell on each carrier. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable. No Gap pattern shall be configured.

A RRC message implying handover shall be sent to the UE during period T1. The start of T2 is the next instant after the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.11.2.1.8-1. General test parameters are provided in table A.11.2.1.8-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.11.2.1.8-3 and A.11.2.1.8-4 respectively.

Table A.11.2.1.8-1: Supported test configurations for SA inter-RAT E-UTRAN handover tests

Table A.11.2.1.8-2: General test parameters for SA inter-RAT E-UTRAN handover

Table A.11.2.1.8-3: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 1)

Table A.11.2.1.8-4: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 2)

## A.11.2.1.8.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 165 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and is specified in clause 6.1.2.1.

Tinterrupt = 115 ms in the test; Tinterrupt is defined in clause 6.1.2.1.

This gives a total of 165 ms.

## A.11.2.1.9Handover with PSCell from NR SA to EN-DC with known target PSCell using CCA

## A.11.2.1.9.1Test Purpose and Environment

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

Table A.11.2.1.9.1-2: General test parameters for SA inter-RAT E-UTRAN handover with FR1 PSCell addition

Table A.11.2.1.9.1-3: Cell specific test parameters for SA inter-RAT E-UTRA handover with FR1 PSCell addition (NR Cell 1)

Table A.11.2.1.9.1-4: Cell specific test parameters for SA inter-RAT E-UTRA handover with FR1 PSCell addition (E-UTRA Cell 2)

Table A.11.2.1.9.1-5: General test parameters for NR FR1 PSCell carrier with CCA addition

Table A.11.2.1.9.1-6: Cell specific test parameters for PSCell addition of FR1 carrier under CCA

## A.11.2.1.9.2Test Requirements

In this test, the UE shall start to transmit the PRACH to E-UTRA Cell 2 less than 55 ms Note1 from the beginning of time period T3.

The above test requirements shall be fulfilled in order of T1, T2, T3 for the observed inter-RAT handover delay from NR to E-UTRAN to be counted as correct, and in order of T1, T2‘, T3‘, T4‘ for the observed PSCell addition delay to be counted as correct.

The rate of correct handovers and correct PSCell addition delay during repeated tests shall be at least 90 %.

NOTE1:The handover delay can be expressed as specified in clause 6.1.5.2:

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

## A.11.2.2RRC connection mobility control

## A.11.2.2.1RRC re-establishment

## A.11.2.2.1.1Intra-frequency RRC Re-establishment with CCA in FR1

A.11.2.2.1.1.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay with CCA in FR1 with known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1A.

The test parameters are given in table A.11.2.2.1.1.1-1, table A.11.2.2.1.1.1-2 and table A.11.2.2.1.1.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell with CCA, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.11.2.2.1.1.1-1: Supported test configurations

Table A.11.2.2.1.1.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case with CCA

Table A.11.2.2.1.1.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case with CCA

A.11.2.2.1.1.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to a known NR intra frequency cell with CCA shall be less than 1350 + MAX (200, (5+K1) x 20) ms.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay_CCA=TUE_re-establish_delay_CCA+TUL_grant

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay_CCA=50 ms+Tidentify_intra_NR_CCA+i=1Nfreq-1Tidentify_inter_NR_CCA,i+TSI-NR_CCA+TPRACH_CCA

Where

Nfreq = 1

Tidentify_intra_NR_CCA = MAX (200 ms, (5+K1) x TSMTC), where

K1 is the number of SMTC occasions not available at the UE due to DL CCA failures during RRC re-establishment period on the carrier with CCA.

TSMTC = 20 ms is the SMTC periodicity.

Tidentify_inter_NR_CCA = 0 ms

TSI-NR_CCA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target intra-frequency NR cell.

TPRACH_CCA = TSSB,RO + 10 ms, where:

-TSSB,RO is the SSB to PRACH occasion association period as defined in table 8.1-1 of TS 38.213 [39], which is TSSB,RO=10 ms for FR1 PRACH configuration 1 under CCA.

This gives a total of 1350 + MAX (200, (5+K1) x 20) ms, allow 1870 + MAX (200, (5+K1) x 20) ms from the beginning of T2 in the test case.

## A.11.2.2.1.2Inter-frequency RRC Re-establishment with CCA in FR1

A.11.2.2.1.2.1Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay with CCA in FR1 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1A.

The test parameters are given in table A.11.2.2.1.2.1-1, table A.11.2.2.1.2.1-2 and table A.11.2.2.1.2.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell with CCA, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

Table A.11.2.2.1.2.1-1: Supported test configurations

Table A.11.2.2.1.2.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1

Table A.11.2.2.1.2.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1

A.11.2.2.1.2.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell shall be less than .Tre-establishdelayCCA

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establishdelayCCA=TUEre-establishdelayCCA+TULgrant

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay_CCA=50 ms+Tidentify_intra_NR_CCA+i=1Nfreq-1Tidentify_inter_NR_CCA,i+TSI-NR_CCA+TPRACH_CCA

Where

Tidentify_intra_NR_CCA: 0 ms

Tidentify_inter_NR_CCA,i: MAX (200 ms, ([6]+K2,i) x TSMTC, i),

where

K2,i is the number of SMTC not available at the UE during RRC re-establishment period on the “i” th carrier with CCA

TSMTC,i: It is the periodicity of the SMTC occasion configured for the inter-frequency carrier i.

Nfreq = 2

TSI-NR_CCA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH_CCA = (1+ K3)*TSSB,RO + 10 ms, where:

-TSSB,RO is the SSB to PRACH occasion association period as defined in table 8.1-1 of TS 38.213 [3].

-K3 is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure. K3 = 0 for Type 2C UL channel access procedure as defined in TS 37.213 [33].

This gives a total of  = 50 + MAX (200 ms, (6+K2,1) x TSMTC, 1) + 1280 + (1+ K3)*TSSB,RO + 10 ms, allow 1860 + MAX (200 ms, (6+K2,1) x TSMTC, 1) + (1+ K3)*TSSB,RO ms from the beginning of T2 in the test case.Tre-establishdelayCCA

A.11.2.2.1.3Intra-frequency RRC Re-establishment with CCA in FR1 without serving cell timing

A.11.2.2.1.3.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay with CCA in FR1 without serving cell timing is within the specified limits. These tests will verify the requirements in clause 6.2.1A.

The test parameters are given in table A.11.2.2.1.3.1-1, table A.11.2.2.1.3.1-2 and table A.11.2.2.1.3.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell with CCA, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.11.2.2.1.3.1-1: Supported test configurations

Table A.11.2.2.1.3.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR1

Table A.11.2.2.1.3.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR1

A.11.2.2.1.3.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR intra frequency cell without serving cell timing shall be less than 1350 + MAX (800 ms, (10+ K1) x 20) ms.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay_CCA=TUE_re-establish_delay_CCA+TUL_grant

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay_CCA=50 ms+Tidentify_intra_NR_CCA+i=1Nfreq-1Tidentify_inter_NR_CCA,i+TSI-NR_CCA+TPRACH_CCA

Where,

Nfreq = 1

Tidentify_intra_NR = MAX (800 ms, (10+ K1) x TSMTC), where

K1 is the number of SMTC occasions not available at the UE due to DL CCA failures during RRC re-establishment period on the carrier with CCA.

TSMTC is the SMTC periodicity which is 20 ms.

Tidentify_inter_NR_CCA = 0 ms

TSI-NR_CCA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 [2] for the target intra-frequency NR cell.

TPRACH_CCA = (1+ K3)*TSSB,RO + 10 ms, where:

-TSSB,RO is the SSB to PRACH occasion association period as defined in table 8.1-1 of TS 38.213 [39]. It is 10 ms for FR1 PRACH configuration 1 under CCA.

-K3 = 0.

This gives total =1350 + MAX (800 ms, (10+ K1) x 20) ms, allow 1870 + MAX (800 ms, (10+ K1) x 20) ms from the beginning of T2 in the test case.TUE_re-establish_delay_CCA

## A.11.2.2.1.4Inter-frequency RRC Re-establishment from NR FR1 carrier without CCA to NR FR1 carrier under CCA

A.11.2.2.1.4.1Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay requirement for RRC re-establishment from NR FR1 carrier without CCA to NR FR1 inter-frequency carrier under CCA with unknown target cell. These tests will verify the requirements in clause 6.2.1A.

The test parameters are given in table A.11.2.2.1.4.1-1, table A.11.2.2.1.4.1-2 and table A.11.2.2.1.4.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

Table A.11.2.2.1.4.1-1: Supported test configurations inter-frequency RRC re-establishment from NR FR1 without under CCA to NR FR1 inter-frequency carrier under CCA

Table A.11.2.2.1.4.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case from NR FR1 carrier without CCA to NR FR1 inter-frequency carrier under CCA

Table A.11.2.2.1.4.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case from NR FR1 carrier without CCA to NR FR1 inter-frequency carrier under CCA

A.11.2.2.1.4.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell shall be less .TUE_re-establish_delay_CCA

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay_CCA=TUE_re-establish_delay_CCA+TUL_grant

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay_CCA=50 ms+Tidentify_intra_NR_CCA+i=1Nfreq-1Tidentify_inter_NR_CCA,i+TSI-NR_CCA+ TPRACH_CCA

Nfreq = 2

Tidentify_intra_NR_CCA = MAX (800 ms, (10+ K1) x 20) ms

Tidentify_inter_NR_CCA = MAX (800 ms, (13+K2,2) x 20) ms

TSI-NR_CCA = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH_CCA = It is the delay uncertainty in acquiring the first available PRACH occasion in the target NR cell. TPRACH_CCA = (1+ K3)*TSSB,RO + 10 ms; where K3=0 and TSSB,RO=10 ms for FR1 PRACH configuration 1 under CCA.

K1 is the number of SMTC occasions not available at the UE due during RRC re-establishment period on the carrier with CCA and with RF channel number # 1.

K2,2 is the number of SMTC occasions not available at the UE during RRC re-establishment period on the carrier with CCA and with RF channel number # 2.

This gives total =1350+MAX (800 ms, (10+ K1) x 20) ms+MAX (800 ms, ([13]+K2,2) x 20) ms, allow 1870 + MAX (800 ms, (10+ K1) x 20) ms+MAX (800 ms, ([13]+K2,2) x 20) ms from the beginning of T2 in the test case.TUE_re-establish_delay_CCA

## A.11.2.2.2Random Access

## A.11.2.2.2.14-step RA type contention-based random access for NR PCell with CCA

## A.11.2.2.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause 6.2.2A.2 and clause 7.1.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1, which operates on a carrier frequency with CCA.  Supported test parameters are shown in table A.11.2.2.2.1.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.11.2.2.2.1.1-2.

Table A.11.2.2.2.1.1-1: Supported test configurations for contention based random access test for FR1 PCell with CCA

Table A.11.2.2.2.1.1-2: General test parameters for contention based random access test for FR1 PCell with CCA

## A.11.2.2.2.1.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.11.2.2.2.1.2.1Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2.2A.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB, if the UL CCA is successful.

The three requirements below are relevant for all cases of PRACH transmissions described within the whole clause A.11.2.2.2.1.2:

-The System Simulator shall implement the UL CCA model of A.3.26.2 for the RACH occasions where PRACH transmissions are expected. The System Simulator shall monitor the RACH occasions to detect if the UE is transmitting PRACH preambles. If a PRACH transmission is detected on a RACH occasion that is expected to have UL CCA failure, the test is considered as failed.

-In case of CCA DL failure, the test equipment should verify that the UE does not transmit PRACH for semi-static channel access mode; for dynamic channel access mode it is assumed that RACH occasions are always scheduled within a UE-initiated COT.

-In case of UL CCA failure, The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.11.2.2.2.1.2.2Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 transmission is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.11.2.2.2.1.2.3No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.11.2.2.2.1.2.4Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2.2A.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

## A.11.2.2.2.1.2.5Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2.2A.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

## A.11.2.2.2.1.2.6Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2.2A.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

## A.11.2.2.2.1.2.7Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2.2A.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.11.2.2.2.24-step RA type non-contention based random access for NR PSCell with CCA

## A.11.2.2.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause 6.2.2A.2 and clause 7.1.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1, which operates on a carrier frequency with CCA. Supported test parameters are shown in table A.11.2.2.2.2.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.11.2.2.2.2.1-2.

Table A.11.2.2.2.2.1-1: Supported test configurations for non-contention based random access test for FR1 PCell with CCA

Table A.11.2.2.2.2.1-2: General test parameters for non-contention based random access test for FR1 PCell with CCA

## A.11.2.2.2.2.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

## A.11.2.2.2.2.2.1SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2A.2.2.1 for SSB-based Random Access Preamble transmission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

The three requirements below are relevant for all cases of PRACH transmissions described within the clause A.11.2.2.2.2.2:

-The System Simulator shall implement the UL CCA model of A.3.26.2 for the RACH occasions where PRACH transmissions are expected. The System Simulator shall monitor the RACH occasions to detect if the UE is transmitting PRACH preambles. If a PRACH transmission is detected on a RACH occasion that is expected to have UL CCA failure, the test is considered as failed.

-In case of CCA DL failure, the test equipment should verify that the UE does not transmit PRACH for semi-static channel access mode; for dynamic channel access mode it is assumed that RACH occasions are always scheduled within a UE-initiated COT.

-In case of UL CCA failure The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS38.321 [7], and transmit with the calculated PRACH transmission power.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belong to the PRACH occasions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.11.2.2.2.2.2.2Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.11.2.2.2.2.2.3No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2A.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of Random Access Response.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.2. The power of the first preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.11.2.2.2.32-step RA type contention-based random access for NR PCell with CCA

## A.11.2.2.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the 2-step RA type random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause 6.2.2A.3 and clause 7.1.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1, which operates on a carrier frequency with CCA. Supported test parameters are shown in table A.11.2.2.2.3.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.11.2.2.2.3.1-2.

Table A.11.2.2.2.3.1-1: Supported test configurations for 2-step RA type contention based random access with successRAR test for FR1 PCell with CCA

Table A.11.2.2.2.3.1-2: General test parameters for 2-step RA type contention based random access with successRAR test for FR1 PCell with CCA

## A.11.2.2.2.3.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

## A.11.2.2.2.3.2.1MsgA Transmission

To test the UE behavior specified in clause 6.2.2A.3.1.1 the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured msgA-RSRP-ThresholdSSB, if the UL CCA is successful.

The three requirements below are relevant for all cases of MsgA transmissions described within the clause A.11.2.2.2.3.2:

-The System Simulator shall implement the UL CCA model for the MsgA occasions (i.e. both MsgA PRACH and MsgA PUSCH occasions) where MsgA transmissions are expected. The System Simulator shall monitor the MsgA occasions to detect if the UE is transmitting MsgA. If a MsgA transmission is detected on MsgA occasions that are expected to have UL CCA failure, the test is considered as failed.

-In case of CCA DL failure, the test equipment should verify that the UE does not transmit MsgA for semi-static channel access mode; for dynamic channel access mode it is assumed that MsgA occasions are always scheduled within a UE-initiated COT.

-The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated PRACH transmission power in case of UL CCA failure.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble transmission shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where  indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18]. 0.6+3μ+2μ

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.11.2.2.2.3.2.2MsgB Reception

To test the UE behavior specified in clause 6.2.2A.3.1.2 the System Simulator shall transmit a MsgB containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE may stop monitoring for MsgB(s) and shall transmit an ACK if the MsgB with a successRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble and if the Contention Resolution is successful and if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting ACK in the case of CCA UL failure. If ACK transmission is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 is detected on a grant expected to have UL CCA failure, the test is considered as failed.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB(s) contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where  indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18]. 0.6+3μ+2μ

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.11.2.2.2.3.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2A.3.1.3 the System Simulator shall transmit a MsgB containing a successRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if no MsgB is received within the MsgB Response window.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where  indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18]. 0.6+3μ+2μ

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.11.2.2.2.42-step RA type non-contention-based random access for NR PCell with CCA

## A.11.2.2.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits when subject to CCA. This test will verify the requirements in clause 6.2.2A.3 and clause 7.1.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1, which operates on a carrier frequency with CCA. Supported test parameters are shown in table A.11.2.2.2.4.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.11.2.2.2.4.1-2.

Table A.11.2.2.2.4.1-1: Supported test configurations for non-contention based random access test for FR1 PCell with CCA

Table A.11.2.2.2.4.1-2: General test parameters for non-contention based random access test for FR1 PCell with CCA

## A.11.2.2.2.4.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

## A.11.2.2.2.4.2.1MsgA Transmission

To test the UE behavior specified in clause 6.2.2A.3.2.1, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0.

In addition, the System Simulator shall receive the MsgA PRACH on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belong to the PRACH occasions permitted by the restrictions given first by the msgA-SSB-SharedRO-MaskIndex if configured, or next by the ra-ssb-OccasionMaskIndex if configured.

The three requirements below are relevant for all cases of MsgA transmissions described within the clause A.11.2.2.2.4.2:

-The System Simulator shall implement the UL CCA model for the MsgA occasions (i.e. both MsgA PRACH and MsgA PUSCH occasions) where MsgA transmissions are expected. The System Simulator shall monitor the MsgA occasions to detect if the UE is transmitting MsgA. If a MsgA transmission is detected on MsgA occasions that are expected to have UL CCA failure, the test is considered as failed.

-In case of CCA DL failure, the test equipment should verify that the UE does not transmit MsgA for semi-static channel access mode; for dynamic channel access mode it is assumed that MsgA occasions are always scheduled within a UE-initiated COT.

-The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated PRACH transmission power in case of UL CCA failure.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where  indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].0.6+3μ+2μ

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.11.2.2.2.4.2.2MsgB Reception

To test the UE behavior specified in clause 6.2.2A.3.2.2 the System Simulator shall transmit a MsgB containing a fallbackRAR containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 containing the payload of MsgA PUSCH if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble if UL CCA is successful. The System Simulator shall monitor if the UE is transmitting msg3 when CCA UL failure. If a msg3 is detected on a grant expected to have UL CCA failure, the test is considered as failed. The UE shall monitor contention resolution as described in clause 8.2A in TS 38.213 [3].

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB’s contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

The system simulator shall implement the UL CCA model of A.3.26.2 for the MsgA occasions where MsgA System Simulator transmissions are expected. The System Simulator shall monitor the MsgA occasions to detect if the UE is transmitting MsgA. If a MsgA transmission is detected on a MsgA occasion that is expected to have UL CCA failure, the test is considered as failed.

In case of CCA DL failure, the test equipment should verify that the UE does not transmit MsgA for semi-static channel access mode.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated MsgA transmission power in case UL CCA failure.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where  indicates the MsgA PUSCH numerology. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].0.6+3μ+2μ

The transmit timing of all MsgA and msg3 transmissions shall be within the accuracy specified in clause 7.1.2.

## A.11.2.2.2.4.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2A.3.2.3 the System Simulator shall transmit a MsgB containing a successRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles. In case of CCA DL failure, the test equipment should delay the transmission of MsgB.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA transmission power when the backoff time expires if no MsgB is received within the MsgB Response window.

The System Simulator shall implement the UL CCA model of A.3.26.2 for the MsgA occasions where MsgA transmissions are expected. The System Simulator shall monitor the MsgA occasions to detect if the UE is transmitting MsgA. If a MsgA transmission is detected on a MsgA occasion that is expected to have UL CCA failure, the test is considered as failed.

In case of CCA DL failure, the test equipment should verify that the UE does not transmit MsgA for semi-static channel access mode.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS38.321 [7], and transmit with the calculated MsgA transmission power in case UL CCA failure.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2A.3. The power of the first MsgA preamble shall be -16 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18], where  indicates the MsgA PUSCH numerology. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].0.6+3μ+2μ

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.11.2.2.3RRC connection release with redirection

## A.11.2.2.3.1Redirection from NR FR1 carrier under CCA to NR FR1 carrier under CCA

A.11.2.2.3.1.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR FR1 carrier under CCA to NR FR1 carrier under CCA specified in clause 6.2.3.2.3.

A.11.2.2.3.1.2Test Parameters

Supported test configurations are shown in table A.11.2.2.3.1.2-1. The time delay is tested by using the parameters in table A.11.2.2.3.1.2-2, and A.11.2.2.3.1.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.11.2.2.3.1.2-1: Redirection from NR to NR test configurations

Table A.11.2.2.3.1.2-2: General test parameters for Redirection from NR to NR test case

Table A.11.2.2.3.1.2-3: Cell specific test parameters for Redirection from NR to NR test case

A.11.2.2.3.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than Tconnection_release_redirect_NR_CCA ms from the beginning of time period T2, where Tconnection_release_redirect_NR_CCA is defined in clause 6.2.3.2.3.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_NR_CCA = TRRC_procedure_delay + Tidentify-NR_CCA + TSI-NR_CCA + TRACH_CCA,

where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR_CCA = MAX (680 ms, (L1+11)  20 ms) in the test.

TSI-NR =  1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH_CCA is the delay uncertainty in acquiring the first available PRACH occasion in the target NR cell.

L1 is the number of SMTC occasions not available at the UE due to DL CCA failures. The test equipment ensure that number of L1 in target cell does not exceed L1,max using the configured LCCA_DL as in clause A.3.26.2.1;

## A.11.2.2.3.2Redirection from NR FR1 carrier without CCA to NR FR1 carrier with CCA

A.11.2.2.3.2.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR FR1 carrier without CCA to NR FR1 carrier with CCA specified in clause 6.2.3.2.3.

A.11.2.2.3.2.2Test Parameters

Supported test configurations are shown in table A.11.2.2.3.2.2-1. The time delay is tested by using the parameters in table A.11.2.2.3.2.2-2, and A.11.2.2.3.2.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.11.2.2.3.2.2-1: Redirection from NR to NR test configurations

Table A.11.2.2.3.2.2-2: General test parameters for Redirection from NR to NR test case

Table A.11.2.2.3.2.2-3: Cell specific test parameters for Redirection from NR to NR test case

A.11.2.2.3.2.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than Tconnection_release_redirect_NR_CCA ms from the beginning of time period T2, where Tconnection_release_redirect_NR_CCA is defined in clause 6.2.3.2.3.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_NR_CCA = TRRC_procedure_delay + Tidentify-NR_CCA + TSI-NR_CCA + TRACH_CCA,

where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR_CCA = MAX (680 ms, (L1+11)  20 ms) in the test.

TSI-NR_CCA = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH_CCA is the delay uncertainty in acquiring the first available PRACH occasion in the target NR cell. TRACH_CCA = (1+L2)´TSSB,RO + 10 ms; where TSSB,RO = 10 ms for FR1 PRACH configuration 1.

L1 is the number of SMTC occasions not available at the UE due to DL CCA failures. The test equipment shall ensure that L1 does not exceed L1,max. In the test L1,max= LCCA_DL which is defined in clause A.3.26.2.1.

L2 is the consecutive number of SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failures. L2 = 0 in the test.

The total delay, Tconnection_release_redirect_NR_CCA, shall be less than 1410 + MAX (680, (L1+11)´20) ms.

## A.11.3Timing

## A.11.3.1UE transmit timing

## A.11.3.1.1UE Transmit Timing Test with PCell under DL CCA

## A.11.3.1.1.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeb when PCell is subject to DL CCA and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1.2.

Supported test configurations are shown in table 11.3.1.1.1-1

Table A.11.3.1.1.1-1: Supported test configuration for UE transmit timing test

For this test a single NR cell is used. Table A.11.3.1.1.1-2 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.11.3.1.1.1-3.

Table A.11.3.1.1.1-2: Cell Specific Test Parameters for UE transmit timing test

Table A.11.3.1.1.1-3: SRS Configuration for UE transmit timing test

## A.11.3.1.1.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1)Setup NR PCell according to parameters given in table A.11.3.1.1.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB.

a.The NTA offset value (in Tc units) is 25600

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.11.3.1.1.2-1

Table A.11.3.1.1.2-1: Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 Table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first detected path (in time) of DL SSB.  Skip this step for test 2 with DRX configured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment

## A.11.3.2UE timing advance

## A.11.3.2.1UE Timing Advance Adjustment Accuracy with PCell under DL CCA

## A.11.3.2.1.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3.

## A.11.3.2.1.2Test Parameters

Supported test configurations are shown in table A.11.3.2.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.11.3.2.1.2-2, A.11.3.2.1.2-3 and A.11.3.2.1.2-4.

In all test cases, single cell is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.11.3.2.1.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.11.3.2.1.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.11.3.2.1.2-1: Supported test configuration for timing advance test

Table A.11.3.2.1.2-2: General test parameters for timing advance test

Table A.11.3.2.1.2-3: Cell specific test parameters for timing advance test

Table A.11.3.2.1.2-4: Sounding Reference Symbol Configuration for Timing Advance Accuracy Test

## A.11.3.2.1.3Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k=5.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.11.4Signalling characteristics

## A.11.4.1Radio link monitoring

## A.11.4.1.1Introduction

In the test cases specified in clause A.11.4.1, any uplink signal transmitted by the UE is used for detecting the in-/out-of-sync state of the UE. In terms of measurement, the uplink signal is verified based on the UE output power:

-UE output power higher than Transmit OFF power -50 dBm (as defined in TS 38.101-1 [18]) means uplink signal.

-UE output power equal to or less than Transmit OFF power -50 dBm (as defined in TS 38.101-1 [18]) means no uplink signal.

For intra-band contiguous carrier aggregation, transmit OFF power is measured as the mean power per component carrier.

For UE with multiple transmit antennas, transmit OFF power is measured as the mean power at each transmit connector.

## A.11.4.1.2Radio link monitoring out-of-sync test for PCell configured with SSB-based RLM RS in non-DRX mode

## A.11.4.1.2.1Test purpose and environment

The purpose of this test is to verify that the UE properly detects the out-of-sync and in-sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR1 PCell radio link monitoring requirements in clause 8.1A.

In the test, UE is configured to perform RLM based on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.11.4.1.2.1-1. The test parameters are given in tables A.11.4.1.2.1-2, A.11.4.1.2.1-3, and A.11.4.1.2.1-4 below. There is one cell (Cell 1), which is the active NR cell in FR1, in the test. Cell 1 operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model.

The test consists of three successive time periods, with time duration of T1, T2 and T3, respectively. Figure A.11.4.1.2.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE transmits according to UL CCA model. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in the test.

Table A.11.4.1.2.1-1: Supported test configurations.

Table A.11.4.1.2.1-2: General test parameters for PCell out-of-sync testing in non-DRX mode.

Table A.11.4.1.2.1-3: Cell-specific test parameters for PCell out-of-sync testing in non-DRX mode.

Table A.11.4.1.2.1-4: Measurement gap configuration for PCell out-of-sync testing in non-DRX mode.

Figure A.11.4.1.2.1-1: SNR variation for out-of-sync testing.

## A.11.4.1.2.2Test requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

-During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

-The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.11.4.1.3Radio link monitoring in-sync test for PCell configured with SSB-based RLM RS in non-DRX mode

## A.11.4.1.3.1Test purpose and environment

The purpose of this test is to verify that the UE properly detects the out-of-sync and in-sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR1 PCell radio link monitoring requirements in clause 8.1A.

In the test, UE is configured to perform RLM based on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.11.4.1.3.1-1. The test parameters are given in tables A.11.4.1.3.1-2, and A.11.4.1.3.1-3 below. There is one cell (Cell 1), which is the active NR cell in FR1, in the test. Cell 1 operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model.

The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5, respectively. Figure A.11.4.1.3.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE transmits according to UL CCA model.

Table A.11.4.1.3.1-1: Supported test configurations.

Table A.11.4.1.3.1-2: General test parameters for PCell in-sync testing in non-DRX mode.

Table A.11.4.1.3.1-3: Cell-specific test parameters for PCell in-sync testing in non-DRX mode.

Figure A.11.4.1.3.1-1: SNR variation for in-sync testing.

## A.11.4.1.3.2Test requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

-During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.11.4.1.4Void

## A.11.4.1.4.1Void

## A.11.4.1.4.2Void

## A.11.4.1.5Void

## A.11.4.1.5.1Void

## A.11.4.1.5.2Void

## A.11.4.2Void

## A.11.4.3SCell activation and deactivation delay

## A.11.4.3.1SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 160 ms SCell measurement cycle

## A.11.4.3.1.1Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for SCell, with PCell and SCell both under CCA, are within the requirements stated in clause 8.3A, when the SCell is known by the UE at the time of activation and the configured SCell measurement cycle is 160 ms.

The supported test configurations are shown in table A.11.4.3.1.1-1.

The test parameters are given in table A.11.4.3.1.1-2 and cell-specific parameters in table A.11.4.3.1.1-3 below. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two carriers, each with one cell: Cell 1 (PCell) on radio channel 1 (PCC) in NR with CCA, and Cell 2 (SCell) on radio channel 2 (SCC) in NR with CCA. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2, as the UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. At the end of T1, the test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m, defines the start of time period T2. The UE shall be able to report a valid CSI in PCell for the activated SCell at latest in slot m + (THARQ+Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, as defined in clause 8.3A.2. The UE shall start reporting CSI in PCell in first available uplink resource for CSI reporting after at least one CSI-RS transmission occasion for channel measurement and reporting following slot m+  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption shall fall within the time window specified in clause 8.3.2. THARQ+3 msNR slot length

The point in time at which the MAC message is received by at the UE antenna connector, in a slot # denoted n, defines the start of time period T3. The UE shall complete the activation at latest in slot . Any PCell interruption shall fall within the time window specified in clause 8.3A.3.n+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received, while taking into account CCA failures on SCC.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.11.4.3.1.1-1: Supported test configurations for SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 160 ms SCell measurement cycle

Table A.11.4.3.1.1-2: General test parameters for known SCell activation with PCell and SCell under CCA, 160 ms SCell measurement cycle

Table A.11.4.3.1.1-3: Cell specific test parameters for known SCell activation case with PCell and SCell under CCA, 160 ms SCell measurement cycle

## A.11.4.3.1.2Test Requirements

During T2, starting after at least one CSI-RS transmission occasion for channel measurement and reporting from the slot specified in clause 4.3 of TS 38.213 [3] and until the UE has completed the SCell activation, the UE shall report out of range if the UE has available uplink resources to report CQI for the SCell.

During T2, the UE shall send the first valid CSI report (non-zero CQI) for the SCell in first available uplink resource for CSI reporting no later than slot m + (THARQ+Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB + L1*Trs + 5 ms, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot , as defined in clause 8.3A.3.n+THARQ+3 msNR slot length

During T2, interruption on PCell shall not occur outside slot m +1+  to slot m +1+ with TX = TFirstSSB.THARQNR slot lengthTHARQ+3+TXNR slot length

During T3, interruption on PCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PCell shall not be more than specified for SA in clause 8.2.2.2.2.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

## A.11.4.3.2SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 640 ms SCell measurement cycle

## A.11.4.3.2.1Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for SCell, with PCell and SCell under CCA, are within the requirements stated in clause 8.3A, when the SCell is known by the UE at the time of activation and the configured SCell measurement cycle is 640 ms.

The supported test configurations are same as in table A.11.4.3.1.1-1 above.

The test parameters are same as in table A.11.4.3.1.1-2 above, except for parameters listed below in table A.11.4.3.2.1-1. The cell-specific parameters are same as in table A.11.4.3.1.1-3 above.

The test execution is the same as described in clause A.11.4.3.1 above.

Table A.11.4.3.2.1-1: General test parameters for known SCell activation with PCell and SCell under CCA, 640 ms SCell measurement cycle

## A.11.4.3.2.2Test Requirements

During T2, starting after at least one CSI-RS transmission occasion for channel measurement and reporting from the slot specified in clause 4.3 of TS 38.213 [3] and until the UE has completed the SCell activation, the UE shall report out of range if the UE has available uplink resources to report CQI for the SCell.

During T2, the UE shall send the first valid CSI report (non-zero CQI) for the SCell in first available uplink resource for CSI reporting no later than slot m + (THARQ+Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB_MAX + L2,1*TSMTC_MAX + (1 +L2,2)*Trs + 5 ms, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot , as defined in clause 8.3A.3.n+THARQ+3 msNR slot length

During T2, interruption on PCell shall not occur outside slot m +1+  to slot m +1+ with TX = TFirstSSB_MAX + L2,1* TSMTC_MAX.THARQNR slot lengthTHARQ+3+TXNR slot length

During T3, interruption on PCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PCell shall not be more than specified for SA in clause 8.2.2.2.2.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

## A.11.4.3.3SCell Activation and Deactivation of unknown SCell with PCell and SCell under CCA

## A.11.4.3.3.1Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation delays for SCell, with PCell and SCell under CCA, are within the requirements stated in clause 8.3A, when the SCell is unknown to the UE at the time of activation.

The supported test configurations are same as in table A.11.4.3.1.1-1 above.

The test parameters are same as in table A.11.4.3.1.1-2 above, except for parameters listed below in table A.11.4.3.3.1-1. The cell-specific parameters are same as in table A.11.4.3.1.1-3 above.

The test execution is the same as described in clause A.11.4.3.1 above.

Table A.11.4.3.3.1-1: General test parameters for unknown SCell activation with PCell ans SCell under CCA

## A.11.4.3.3.2Test Requirements

During T2, starting after at least one CSI-RS transmission occasion for channel measurement and reporting from the slot specified in clause 4.3 of TS 38.213 [3] and until the UE has completed the SCell activation, the UE shall report out of range if the UE has available uplink resources to report CQI for the SCell.

During T2, the UE shall send the first valid CSI report (non-zero CQI) for the SCell in first available uplink resource for CSI reporting no later than slot m + (THARQ+Tactivation_time_withCCA + TCSI_Reporting_withCCA)/NR_slot_length, where Tactivation_time_withCCA = TFirstSSB_MAX + (1 + L3,1)*TSMTC_MAX + (2 + L3,2)*Trs + 5 ms, as specified in clause 8.3A.2.

During T3, the UE shall stop sending CSI reports for SCell at latest in slot , as defined in clause 8.3A.3.n+THARQ+3 msNR slot length

During T2, interruption on PCell shall not occur outside slot m +1+  to slot m +1+ with TX = TFirstSSB_MAX + L3,1* TSMTC_MAX.THARQNR slot lengthTHARQ+3+TXNR slot length

During T3, interruption on PCell shall not occur outside slot n +1+THARQ/NR_slot_length to slot n+1+(THARQ +3 ms)/NR_slot_length.

The interruption on PCell shall not be more than specified for SA in clause 8.2.2.2.2.

The rate of correctly observed SCell activation delays and SCell deactivation delays shall for repeated tests be at least 90 %.

## A.11.4.4Beam failure detection and link recovery procedures

## A.11.4.4.1Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode

## A.11.4.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5A.

The test parameters are given in tables A.11.4.4.1.1-1, A.11.4.4.1.1-2, A.11.4.4.1.1-3 and A.11.4.4.1.1-4 below. There is one cell, Cell 1 which is the active cell, in the test. Cell 1 operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.11.4.4.1.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.11.4.4.1.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 2 ms. The UE transmits the reporting according to UL CCA mode. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

Table A.11.4.4.1.1-1: Supported test configurations for FR1 PCell with CCA

Table A.11.4.4.1.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.11.4.4.1.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.11.4.4.1.1-1: SNR and L1-RSRP variation SSB for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.11.4.4.1.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 410 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.11.4.4.2Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode

## A.11.4.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5A.

The test parameters are given in tables A.11.4.4.2.1-1, A.11.4.4.2.1-2, and A.11.4.4.2.1-3 below. There is one cell, Cell 1 which is the active cell, in the test. Cell 1 operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.11.4.4.2.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.11.4.4.2.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 2 ms. The UE transmits the reporting according to UL CCA mode. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.11.4.4.2.1-1: Supported test configurations for FR1 PCell with CCA

Table A.11.4.4.2.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.11.4.4.2.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Figure A.11.4.4.2.1-1: SNR and L1-RSRP variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.11.4.4.2.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 3850 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.11.4.5Active BWP switching

## A.11.4.5.1UL active BWP switch delay with consistent UL LBT failure on PCell subject to UL CCA

## A.11.4.5.1.1Test Purpose and Environment

The purpose of this test is to verify the UL BWP switch delay requirement defined in clause 8.6.4.

The supported test configurations are shown in table A.11.4.5.1.1-1. The test scenario comprises of one cell (Cell 1), which is Pcell as given in table A.11.4.5.1.1-2. Cell-specific parameters of the cell are specified in table A.11.4.5.1.1-3 below. SRS configuration used in the test is specified in table A.11.4.5.1.1-4.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE is configured with 2 different UE-specific downlink and uplink bandwidth parts: DL BWP-1, DL BWP-2, UL BWP-1 and UL BWP-2 before starting the test. DL BWP-1 and DL BWP-2 always include bandwidth of the initial DL BWP and SSB. UL BWP-1 and UL BWP-2 always include bandwidth of the SRS.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is DL BWP-1.

-UE is indicated in firstActiveUplinkBWP-Id that the active UL BWP is UL BWP-1.

-UE is configured with LBT-FailureRecoveryConfig parameters for Cell 1.

The cell has constant signal levels throughout the test. The test consists of 2 successive time periods, with durations of T1 and T2, respectively.

During T1,

-Time period T1 starts when the UE has received the SRS configuration for periodic SRS transmission on active UL BWP-1.

-The UE shall perform UL CCA before SRS transmission.

-The parameter UL CCA probability PCCA is set to 0 during T1. This requires the test system to set energy level above the detection level during portion of the UL slot where the UE performs UL CCA. This in turn forces the UE to fail the UL CCA. The UE consistently fails UL CCA during T1 and is therefore unable to transmit SRS.

During T2,

-T2 starts when the UE detects consistent UL LBT failures i.e. when total number of UL LBT failures in Cell 1 on active UL BWP-1 exceeds lbt-FailureInstanceMaxCount during lbt-FailureDetectionTimer.

-The UE upon detected consistent UL LBT failure starts the LBT recovery mechanism, which requires the UE to switch to active UL BWP-2 in Cell 1 and to send PRACH in the active UL BWP-2.

-Staring from T2, the UE shall be able to send PRACH in the active UL BWP-2 within the delay specified in clause 8.6.4.

Table A.11.4.5.1.1-1: Supported test configurations for UL BWP switch test in SA

Table A.11.4.5.1.1-2: General test parameters for UL BWP switch test in SA

Table A.11.4.5.1.1-3: NR Cell specific test parameters for UL BWP switch test in SA

Table A.11.4.5.1.1-4: Sounding Reference Symbol Configuration for UL BWP Switch Test

## A.11.4.5.1.2Test Requirements

The UE capable of bwp-SwitchingDelay type1 [2] shall start to transmit the PRACH on active UL BWP-2 of Cell 1 (PCell) less than 21.5 ms from the beginning of time period T1.

The UE capable of bwp-SwitchingDelay type2 [2] shall start to transmit the PRACH on active UL BWP-2 of Cell 1 (PCell) less than 23 ms from the beginning of time period T1.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE: The above delay is calculated as follows:’

The active UL BWP switch delay from UL BWP-1 to UL BWP-2 can be expressed as:

TBWPswitchDelay*Tslot +1*Tslot + (1+ L3)*TSSB,RO + 10 ms

Where:

TBWPswitchDelay = 1 ms (2 slots) and 2.5 ms (5 slots) for bwp-SwitchingDelay [2] type1 and type2 UE capabilities according to clause 8.6.4.

Tslot = It is the slot length. It is 0.5 ms for 30 kHz.

L3 = It is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure. L3= 0 during T2 since PCCA = 1.

TSSB,RO = 10 ms according to FR1 PRACH configuration 1.

This gives a total of 21.5 ms and 23 ms for type1 and type2 UE respectively.

## A.11.4.5.2DCI-based and Timer-based Active BWP Switch

## A.11.4.5.2.1NR FR1- NR FR1 DL active BWP switch of PCell with non-DRX in SA

A.11.4.5.2.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6, and interruption requirement on other active serving cell defined in clause 8.2.2.2.5.

The supported test configurations are shown in table A.11.4.5.2.1.1-1 below. The test scenario comprises of one PCell (Cell 1) and one SCell (Cell 2) as given in table A.11.4.5.2.1.1-2. NR Cell-specific parameters are specified in table A.11.4.5.2.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 1 and the time duration of T2.

PDCCHs indicating new transmissions shall be sent continuously on SCell (Cell 2) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (SCell) on radio channel 2 (SCC).

-UE is configured with 2 different UE-specific downlink bandwidth parts for PCell, BWP-1 and BWP-2, in Cell 1 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is configured with 1 UE-specific downlink bandwidth parts the same as initial BWP for SCell, BWP-0 in Cell 2 before starting the test.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in PCell.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in SCell.

-UE is configured with a bwp-InactivityTimer timer value for PCell.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for PCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH no later than the first DL slot that occurs after the beginning of PCell’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the PCell no later than the first UL slot that occurs after the beginning of slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PCell’s BWP-2 no later than the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).

The starting time of SCell (Cell 2) interruption due to BWP switch on PCell shall occur within the BWP switch delay.

During T2, the test equipment won’t transmit DCI format for PDSCH reception on PCell (Cell 1).

During T3,

The time period T3 starts from the slot #j, where j is the first  slot of the subframe immediately after bwp-InactivityTimer timer expires. The UE should switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH no later than the first DL slot that occurs after the beginning of PCell’s slot (j+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the SCell at latest on the first UL slot that occurs after the beginning of slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on PCell’s BWP-1 no later than the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

The starting time of SCell (Cell 2) interruption due to BWP switch of PCell shall occur within the BWP switch delay.

The test equipment verifies the DL BWP switch time in PCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK/NACK is received.

The test equipment verifies that potential interruption to SCell is carried out in the correct time span by monitoring ACK/NACK sent in SCell during BWP switch of PCell, respectively.

Table A.11.4.5.2.1.1-1: DL BWP switch supported test configurations

Table A.11.4.5.2.1.1-2: General test parameters for DL BWP switch in SA

Table A.11.4.5.2.1.1-3: NR Cell specific test parameters for DL BWP switch in SA

A.11.4.5.2.1.2Test Requirements

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

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first DL slot that occurs after the beginning of DL slot (i+ TBWPswitchDelay+k1), (j+ TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

## A.11.4.5.2.2NR FR1 DL active BWP switch with non-DRX in SA

A.11.4.5.2.2.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6.

The supported test configurations are shown in table A.11.4.5.2.2.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.11.4.5.2.2.1-2. Cell-specific parameters of the cell are specified in table A.11.4.5.2.2.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE is configured with 2 different UE-specific downlink bandwidth parts, BWP-1 and BWP-2 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1.

-UE is configured with a bwp-InactivityTimer timer value for Cell 1.

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

Table A.11.4.5.2.2.1-2: General test parameters for DL BWP switch in SA

Table A.11.4.5.2.2.1-3: NR Cell specific test parameters for DL BWP switch in SA

A.11.4.5.2.2.2Test Requirements

During T1, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed Cell 1 active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first UL slot that occurs after beginning of DL slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

## A.11.4.5.3RRC-based Active BWP Switch

## A.11.4.5.3.1NR FR1 DL active BWP switch of Cell with non-DRX in SA

A.11.4.5.3.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6.

The supported test configurations are shown in table A.11.4.5.3.1.1-1. The test scenario comprises of one Cell (Cell 1) as given in table A.11.4.5.3.1.1-2. Cell-specific parameters of Cell are specified in table A.11.4.5.3.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in Cell 1.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is completely received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition.

The UE shall be able to receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot as defined in clause 8.6.3 and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot on BWP-1 of final condition. The UE shall be continuously scheduled on PCell’s BWP-1 of final condition starting from the first DL slot right after slot . i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length

TRRCprocessingDelay and TBWPswitchDelayRRC are defined in clause 8.6.3.

The test equipment verifies the DL BWP switch time in Cell by counting the time from the time when the RRC Reconfiguration message including updated BWP configuration is sent till the time when a vaild ACK/NACK is received is received.

Table A.11.4.5.3.1.1-1: DL BWP switch supported test configurations in SA scenario

Table A.11.4.5.3.1.1-2: General test parameters for DL BWP switch in SA scenario

Table A.11.4.5.3.1.1-3: NR Cell specific test parameters for DL BWP switch in SA scenario

A.11.4.5.3.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the Cell from the first DL slot that occurs right after the begining of slot  and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot. i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed Cell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.11.4.6Void

## A.11.5Measurement procedure

## A.11.5.1Intra-frequency measurements

## A.11.5.1.1Event-triggered reporting tests on PCC without gaps under non-DRX

## A.11.5.1.1.1Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.5.1 and 9.2A.5.2.

## A.11.5.1.1.2Test parameters

Two cells are deployed in the test, which are PCell (Cell 1) and a neighbour cell (Cell 2) on the same carrier frequency with CCA transmitting SSBs in DBT windows according to DL CCA model. The test parameters for the two cells are given in table A.11.5.1.1.2-1 and A.11.5.1.1.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

Table A.11.5.1.1.2-1: Supported test configurations

Table A.11.5.1.1.2-2: General test parameters for intra-frequency event triggered reporting without gaps

Table A.11.5.1.1.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gaps

## A.11.5.1.1.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 840 ms from the beginning of time period T2.

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.11.5.1.2Event-triggered reporting tests on PCC without gaps under DRX

## A.11.5.1.2.1Test purpose and environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2A.5.1 and 9.2A.5.2.

## A.11.5.1.2.2Test parameters

Two cells are deployed in the test, which are PCell (Cell 1) and a neighbour cell (Cell 2) on the same carrier frequency with CCA transmitting SSBs in DBT windows according to DL CCA model. The test parameters for the two cells are given in table A.11.5.1.2.2-1 and A.11.5.1.2.2-2 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1 and T2, respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, the UE is allocated with PUSCH resource at every DRX cycle.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

Table A.11.5.1.2.2-1: Supported test configurations

Table A.11.5.1.2.2-2: General test parameters for intra-frequency event triggered reporting without gaps

Table A.11.5.1.2.2-3: Cell-specific test parameters for intra-frequency event-triggered reporting without gaps

## A.11.5.1.2.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report with a measurement reporting delay less than 1200 ms from the beginning of time period T2.

In test 2, the UE shall send one Event A3 triggered measurement report with a measurement reporting delay less than 10240 ms from the beginning of time period T2.

The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.11.5.1.3Void

## A.11.5.1.4Void

## A.11.5.1.5Void

## A.11.5.1.6Void

## A.11.5.1.7Void

## A.11.5.1.8Void

## A.11.5.1.9Void

## A.11.5.1.10Void

## A.11.5.1.11Void

## A.11.5.1.12Void

## A.11.5.2Inter-frequency measurements

## A.11.5.2.1Void

## A.11.5.2.2Void

## A.11.5.2.3Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is not used

## A.11.5.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements for NR cell with CCA in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 with CCA as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters are given in tables A.11.5.2.3.1-1, A.11.5.2.3.1-2 and A.11.5.2.3.1-3.

In this test, measurement gap pattern configuration # 0 as defined in table A.11.5.2.3.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

Table A.11.5.2.3.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1 with CCA

Table A.11.5.2.3.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

Table A.11.5.2.3.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

## A.11.5.2.3.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2 UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.11.5.2.4Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is used

## A.11.5.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 as PCell in FR1 with CCA on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters are given in tables A.11.5.2.4.1-1, A.11.5.2.4.1-2 and A.11.5.2.4.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.11.5.2.4.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.11.5.2.4.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1 with CCA

Table A.11.5.2.4.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

Table A.11.5.2.4.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

Table A.11.5.2.4.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

Table A.11.5.2.4.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

## A.11.5.2.4.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2, the UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1, DRX cycle = 40 ms and for test 2, DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.11.5.2.5Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is not used

## A.11.5.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 as PCell in FR1 with CCA on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 with CCA on NR RF channel 2. The test parameters are given in tables A.11.5.2.5.1-1, A.11.5.2.5.1-2 and A.11.5.2.5.1-3.

In this test, measurement gap pattern configuration # 0 as defined in table A.11.5.2.5.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

Table A.11.5.2.5.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1 with CCA

Table A.11.5.2.5.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

Table A.11.5.2.5.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

## A.11.5.2.5.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.11.5.2.6Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is used

## A.11.5.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 as PCell in FR1 with CCA on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 with CCA on NR RF channel 2.  The test parameters are given in tables A.11.5.2.6.1-1, A.11.5.2.6.1-2 and A.11.5.2.6.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.11.5.2.6.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.11.5.2.6.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1 with CCA

Table A.11.5.2.6.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

Table A.11.5.2.6.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

Table A.11.5.2.6.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

Table A.11.5.2.6.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

## A.11.5.2.6.2Test Requirements

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

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of

## A.11.5.2.7Event triggered reporting tests for FR1 without SSB time index detection when DRX is not used

## A.11.5.2.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements for NR cell with CCA in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 with CCA as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.11.5.2.7.1-1, A.11.5.2.7.1-2 and A.11.5.2.7.1-3.

In this test, measurement gap pattern configuration # 0 as defined in table A.11.5.2.7.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

Table A.11.5.2.7.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1 with CCA

Table A.11.5.2.7.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.11.5.2.7.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

## A.11.5.2.7.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.11.5.2.8Event triggered reporting tests for FR1 without SSB time index detection when DRX is used

## A.11.5.2.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 with CCA as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.11.5.2.8.1-1, A.11.5.2.8.1-2 and A.11.5.2.8.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.11.5.2.8.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.11.5.2.8.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1 with CCA

Table A.11.5.2.8.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

Table A.11.5.2.8.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA without SSB time index detection

Table A.11.5.2.8.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

Table A.11.5.2.8.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

## A.11.5.2.8.2Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_without_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2, the UE is not required to report SSB time index.

Tidentify_inter_cca_without_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

For test 1, DRX cycle = 40 ms and for test 2, DRX cycle = 640 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.11.5.2.9Event triggered reporting tests for FR1 with SSB time index detection when DRX is not used

## A.11.5.2.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 with CCA as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.11.5.2.9.1-1, A.11.5.2.9.1-2 and A.11.5.2.9.1-3.

In this test, measurement gap pattern configuration # 0 as defined in table A.11.5.2.9.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

Table A.11.5.2.9.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1 with CCA

Table A.11.5.2.9.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

Table A.11.5.2.9.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

## A.11.5.2.9.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Tidentify_inter_cca_with_index from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is required to report SSB time index.

Tidentify_inter_cca_with_index = (TPSS/SSS_sync_inter_cca + T SSB_measurement_period_inter_cca + TSSB_time_index_inter_cca) ms, where

TPSS/SSS_sync_inter_cca: it is the time period used in PSS/SSS detection given in table 9.3A.4-1.

TSSB_time_index_inter_cca: it is the time period used to acquire the index of the SSB being measured given in table 9.3A.4-2.

T SSB_measurement_period_inter_cca: equal to a measurement period of SSB based measurement given in table 9.3A.5-1.

MGRP = 40 ms.

SMTC period = 20 ms.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.11.5.2.10Event triggered reporting tests for FR1 with SSB time index detection when DRX is used

## A.11.5.2.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3A.4 and 9.3A.5.

In this test, there are two cells: NR Cell 1 with CCA as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test parameters are given in tables A.11.5.2.10.1-1, A.11.5.2.10.1-2 and A.11.5.2.10.1-3.

In test 1&2 measurement gap pattern configuration # 0 as defined in table A.11.5.2.10.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 3.

UE needs to be provided at least once every 500 ms with new Timing Advance Command MAC control element to restart the Time alignment timer to keep UE uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

Table A.11.5.2.10.1-1: SA event triggered reporting tests with SSB index reading for FR1-FR1 with CCA

Table A.11.5.2.10.1-2: General test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

Table A.11.5.2.10.1-3: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with CCA with SSB time index detection

Table A.11.5.2.10.1-4: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

Table A.11.5.2.10.1-5: TimeAlignmentTimer -Configuration SA inter-frequency event triggered reporting without SSB time index detection

## A.11.5.2.10.2Test Requirements

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

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.11.5.3Inter-RAT E-UTRAN measurements

## A.11.5.3.1SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1

## A.11.5.3.1.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE makes correct event-triggered reporting of inter-RAT E-UTRAN measurements when operating in standalone (SA) operation with PCell in FR1. This test shall partly verify the cell search and measurement requirements in clauses 9.4.2 and 9.4.3.

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell on a frequency carrier with CCA and Cell 2 is an inter-RAT E-UTRAN inter-RAT neighbour cell. In the measurement control information from the PCell it is indictated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

Supported test configurations are shown in table A.11.5.3.1.1-1. General test parameters are provided in table A.11.5.3.1.1-2 below. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.11.5.3.1.1-3 and A.11.5.3.1.1-4, respectively.

Table A.11.5.3.1.1-1: Supported test configurations in SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

Table A.11.5.3.1.1-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

Table A.11.5.3.1.1-3: PCell specific test parameters for SA inter-RAT E-UTRA event triggered reporting in non-DRX with PCell in FR1

Table A.11.5.3.1.1-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in non-DRX with PCell in FR1

## A.11.5.3.1.2Test Requirements

The UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 3.84 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.11.5.3.2SA NR - E-UTRAN event-triggered reporting in DRX in FR1

## A.11.5.3.2.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE makes correct event-triggered reporting of inter-RAT E-UTRAN measurements when operating in standalone (SA) operation with PCell in FR1 when DRX is used. This test shall partly verify the cell search and measurement requirements in clauses 9.4.2 and 9.4.3. There are two test cases. In test 1 the UE shall be configured with DRX cycle of 40 ms. In test 2 the UE shall be configured with DRX cycle of 640 ms.

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the NR PCell with CCA and Cell 2 is an inter-RAT E-UTRAN inter-RAT neighbour cell. In the measurement control information from the PCell it is indctated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) is to be used. Each test consists of two consecutive time periods, with durations T1 and T2, respectively. Prior to the start of time duration T1, the UE shall be fully synchronized to Cell 1. During T1, the UE shall not have any information on Cell 2.

In each test the UE shall be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, the UE shall be allocated with PUSCH resource at every DRX cycle.

Supported test configurations are shown in table A.11.5.3.2.1-1. General test parameters are provided in table A.11.5.3.2.1-2 below. Test parameters for Cell 1 and Cell 2, valid for both time duration T1 and T2, are provided in tables A.11.5.3.2.1-3 and A.11.5.3.2.1-4, respectively.

Table A.11.5.3.2.1-1: Supported test configurations in SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

Table A.11.5.3.2.1-2: General test parameters for SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

Table A.11.5.3.2.1-3: PCell specific test parameters for SA inter-RAT E-UTRA event triggered reporting in DRX with PCell in FR1

Table A.11.5.3.2.1-4: E-UTRAN neighbour cell specific test parameters for SA inter-RAT E-UTRAN event triggered reporting in DRX with PCell in FR1

## A.11.5.3.2.2Test Requirements

In test 1, the UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 3.84 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

In test 2, the UE shall send one Event B2 triggered measurement report for Cell 2 to the PCell, with a measurement reporting delay less than 12.8 s from the start of period T2. The measurement reporting delay is defined as the time from the beginning of time period T2 to the moment when the UE sends the measurement report on PUSCH.

The UE shall not send event-triggered measurement reports as long as the reporting criteria is not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.11.5.4L1-RSRP measurements for beam reporting

## A.11.5.4.1SSB based L1-RSRP measurement when DRX is not used

## A.11.5.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.11.5.4.1.1-1.

Table A.11.5.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.11.5.4.1.2Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). Cell 1 operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The test parameters for the Cell 1 are given in table A.11.5.4.1.2-1 and table A.11.5.4.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.11.5.4.1.2-1: General test parameters

Table A.11.5.4.1.2-2: SSB specific test parameters

## A.11.5.4.1.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.11.5.4.2SSB based L1-RSRP measurement when DRX is used

## A.11.5.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.11.5.4.2.1-1.

Table A.11.5.4.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.11.5.4.2.2Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). Cell 1 operates on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The test parameters for the Cell 1 are given in table A.11.5.4.2.2-1 and table A.11.5.4.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.11.5.4.2.2-1: General test parameters

Table A.11.5.4.2.2-2: SSB specific test parameters

## A.11.5.4.2.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.11.5.4.3SSB based L1-RSRP measurement on SCC when DRX is not used

## A.11.5.4.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.11.5.4.3.1-1.

Table A.11.5.4.3.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.11.5.4.3.2Test parameters

There are two cells in the test, the FR1 PCell (Cell 1) and FR1 SCell (Cell 2). Both Cell 1 and Cell 2 operate on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The test parameters for the Cell 1 are given in table A.11.5.4.3.2-1 and table A.11.5.4.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.11.5.4.3.2-1: General test parameters

Table A.11.5.4.3.2-2: SSB specific test parameters

## A.11.5.4.3.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.11.5.4.4SSB based L1-RSRP measurement on SCC when DRX is used

## A.11.5.4.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5A.4.1, with the testing configurations for NR cells in table A.11.5.4.4.1-1.

Table A.11.5.4.4.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.11.5.4.4.2Test parameters

There are two cells in the test, the FR1 PCell (Cell 1) and FR1 SCell (Cell 2). Both Cell 1 and Cell 2 operate on a carrier frequency with CCA and transmits SSBs in DBT windows according to DL CCA model. The test parameters for the Cell 1 are given in table A.11.5.4.4.2-1 and table A.11.5.4.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The UE transmits the reporting according to UL CCA model. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.11.5.4.4.2-1: General test parameters

Table A.11.5.4.4.2-2: SSB specific test parameters

## A.11.5.4.4.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19.1.1 and relative accuracy requirement in clause 10.1.19.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE shall send L1-RSRP report of both SSB0 and SSB1 in Cell 2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.11.6Measurement performance

## A.11.6.1SS-RSRP

## A.11.6.1.1Intra-frequency measurement accuracy on a carrier frequency with CCA

## A.11.6.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy on the carrier frequency with CCA is within the specified limits. This test will verify the requirements in clauses 10.1.36.1.1 and 10.1.36.1.2 for intra-frequency measurements under CCA.

## A.11.6.1.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency with CCA and transmit SSBs in DBT windows according to DL CCA model. Supported test configurations are shown in table A.11.6.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.11.6.1.1.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

Table A.11.6.1.1.2-1: SS-RSRP  Intra frequency SS-RSRP supported test configurations

Table A.11.6.1.1.2-2: SS-RSRP Intra frequency test parameters

## A.11.6.1.1.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.36.1.1 and relative requirement in clause 10.1.36.1.2.

## A.11.6.1.2Intra-frequency measurement accuracy on SCC on a carrier frequency with CCA

## A.11.6.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy on the carrier frequency with CCA is within the specified limits. This test will verify the requirements in clauses 10.1.36.1.1 and 10.1.36.1.2 for intra-frequency measurements under CCA.

## A.11.6.1.2.2Test parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1) on the carrier frequency with CCA, and two cells on the same carrier frequency with CCA and transmit SSBs in DBT windows according to DL CCA model: SCell (Cell 2) and a neighbour cell (Cell 3).  Supported test configurations are shown in table A.11.6.1.2.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.11.6.1.2.2-2.

Table A.11.6.1.2.2-1: SS-RSRP  Intra frequency SS-RSRP supported test configurations

Table A.11.6.1.2.2-2: SS-RSRP Intra frequency test parameters

## A.11.6.1.2.3Test Requirements

The SS-RSRP measurement accuracy for Cell 2 and Cell 3 shall fulfil absolute requirement in clause 10.1.36.1.1 and relative requirement in clause 10.1.36.1.2.

## A.11.6.2SS-RSRQ

## A.11.6.2.1Intra-frequency measurement accuracy

## A.11.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.29.1.1.

## A.11.6.2.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.11.6.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.11.6.2.1.2-2. In all test cases, Cell 1 is the PCell with CCA and Cell 2 is the target cell with CCA. Three sub-tests (Test 1, Test 2, and Test 3) are provided different Noc on Cells 1 and 2.

Table A.11.6.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

Table A.11.6.2.1.2-2: SS-RSRQ Intra frequency test parameters

## A.11.6.2.1.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.29.1.1.

## A.11.6.2.2Inter-frequency measurement accuracy

## A.11.6.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.30.1.1 and 10.1.30.1.2.

## A.11.6.2.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.11.6.2.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.11.6.2.2.2-2. In all test cases, Cell 1 is the PCell with CCA and Cell 2 is target cell with CCA. Two sub-tests (Test 1 and Test 2) are provided different Noc on Cells 1 and 2.

Table A.11.6.2.2.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

Table A.11.6.2.2.2-2: SS-RSRQ Inter frequency test parameters

## A.11.6.2.2.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.30.1.1 and 10.1.30.1.2.

## A.11.6.2.3Intra-frequency measurement accuracy on SCC

## A.11.6.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.29.1.1.

## A.11.6.2.3.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.11.6.2.3.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.11.6.2.3.2-2. In all test cases, Cell 1 is the PCell with CCA, Cell 2 is the SCell with CCA, and Cell 3 is the target cell with CCA. Three sub-tests (Test 1, Test 2, and Test 3) are provided different Noc on Cells 1, 2, and 3.

Table A.11.6.2.3.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

Table A.11.6.2.3.2-2: SS-RSRQ Intra frequency test parameters

## A.11.6.2.3.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.29.1.1.

## A.11.6.2.4Inter-frequency measurement accuracy

## A.11.6.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.30.1.1 and 10.1.30.1.2.

## A.11.6.2.4.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.11.6.2.4.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.11.6.2.4.2-2 and A.11.6.2.4.2-3. In all test cases, Cell 1 is the PCell and Cell 2 is target cell with CCA. Two sub-tests (Test 1 and Test 2) are provided different Noc on Cells 1 and 2.

Table A.11.6.2.4.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

Table A.11.6.2.4.2-2: SS-RSRQ Inter frequency test parameters

Table A.11.6.2.4.2-3: SS-RSRQ Intra frequency test parameters for NR PCell

## A.11.6.2.4.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.30.1.1 and 10.1.30.1.2.

## A.11.6.3SS-SINR

## A.11.6.3.1Intra-frequency measurement accuracy

## A.11.6.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.31.1.1.

## A.11.6.3.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.11.6.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.11.6.3.1.2-2. In all test cases, Cell 1 is the PCell with CCA and Cell 2 is the target cell with CCA. Two sub-tests (Test 1 and Test 2) are provided different Noc on Cells 1 and 2.

Table A.11.6.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

Table A.11.6.3.1.2-2: SS-SINR Intra frequency test parameters

## A.11.6.3.1.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.31.1.1.

## A.11.6.3.2Inter-frequency measurement accuracy

## A.11.6.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.32.1.1 and 10.1.32.1.2.

## A.11.6.3.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.11.6.3.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.11.6.3.2.2-2. In all test cases, Cell 1 is the PCell with CCA and Cell 2 is target cell with CCA. Three sub-tests (Test 1, Test 2, and Test 3) are provided different Noc on Cells 1 and 2.

Table A.11.6.3.2.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

Table A.11.6.3.2.2-2: SS-SINR Inter frequency test parameters

## A.11.6.3.2.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.32.1.1 and 10.1.32.1.2.

## A.11.6.3.3Intra-frequency measurement accuracy on SCC

## A.11.6.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.31.1.1.

## A.11.6.3.3.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.11.6.3.3.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.11.6.3.3.2-2. In all test cases, Cell 1 is the PCell with CCA, Cell 2 is the SCell with CCA, and Cell 3 is the target cell with CCA. Two sub-tests (Test 1 and Test 2) are provided different Noc on Cells 1, 2, and 3.

Table A.11.6.3.3.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

Table A.11.6.3.3.2-2: SS-SINR Intra frequency test parameters

## A.11.6.3.3.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.31.1.1.

## A.11.6.3.4Inter-frequency measurement accuracy

## A.11.6.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.32.1.1 and 10.1.32.1.2.

## A.11.6.3.4.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.11.6.3.4.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.11.6.3.4.2-2 and table A.11.6.3.4.2-3. In all test cases, Cell 1 is the PCell and Cell 2 is target cell with CCA. Three sub-tests (Test 1, Test 2, and Test 3) are provided different Noc on Cells 1 and 2.

Table A.11.6.3.4.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

Table A.11.6.3.4.2-2: SS-SINR Inter frequency test parameters

Table A.11.6.3.4.2-3: SS-SINR Inter frequency test parameters for NR PCell

## A.11.6.3.4.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.32.1.1 and 10.1.32.1.2.

## A.11.6.4L1-RSRP measurement for beam reporting with CCA serving cell

## A.11.6.4.1SSB based L1-RSRP measurement

## A.11.6.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.33.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.11.6.4.1.1-1.

Table A.11.6.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.11.6.4.1.2Test parameters

In this set of test cases there one cell in the test, PCell under CCA (Cell 1). Cell 1 operates on a carrier frequency with CCA and transmits SSBs in DBT window according to DL CCA model.

Two sub-tests (Test 1 and Test 2) are provided with different Noc  on Cell 1. The test parameters for the Cell 1 are given in table A.11.6.4.1.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.11.6.4.1.2-1.

The same test is applicable for UE supporting any one or both semi-static channel access or dynamic channel access and for network configuring any of semi-static channel occupancy or dynamic channel occupancy.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.11.6.4.1.2-1: FR1 SSB based L1-RSRP test parameters

## A.11.6.4.1.3Test Requirements

In both Test 1 and Test 2, the L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 1 shall fulfil the requirements in clauses 10.1.33.1.

## A.11.6.5RSSI

## A.11.6.5.1Intra-frequency RSSI measurement accuracy on PCC with CCA

## A.11.6.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.1.

## A.11.6.5.1.2Test parameters

In all test cases, Cell 1 is the PCell with CCA. RSSI is measured on channel number 1. Supported test configurations are shown in table A.11.6.5.1.2-1. The accuracy of RSSI intra-frequency measurements is tested by using the parameters in A.11.6.5.1.2-2 and A.11.6.5.1.2-3.

Table A.11.6.5.1.2-1: Intra frequency RSSI supported test configurations

Table A.11.6.5.1.2-2: RSSI Intra frequency test parameters

Table A.11.6.5.1.2-3: RSSI RMTC parameters

## A.11.6.5.1.3Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.1. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

## A.11.6.5.2Intra-frequency RSSI measurement accuracy on SCC with CCA

## A.11.6.5.2.1Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.1.

## A.11.6.5.2.2Test parameters

In all test cases, Cell 1 which is PCell operating on a carrier frequency under CCA, and Cell 2 which is SCell operating on a carrier frequency under CCA. RSSI is measured on channel number 2. Supported test configurations are shown in table A.11.6.5.2.2-1. The accuracy of RSSI intra-frequency measurements is tested by using the parameters in A.11.6.5.2.2-2 and A.11.6.5.2.2-3.

Table A.11.6.5.2.2-1: Intra frequency RSSI supported test configurations

Table A.11.6.5.2.2-2: RSSI Intra frequency test parameters

Table A.11.6.5.2.2-3: RSSI RMTC parameters

## A.11.6.5.2.3Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.1. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

## A.11.6.5.3Inter-frequency RSSI measurement accuracy on a carrier with CCA

## A.11.6.5.3.1Test Purpose and Environment

The purpose of this test is to verify that the RSSI measurement accuracy is within the specified limits. This test will partially verify the RSSI measurement accuracy requirements in section 10.1.34.2.

## A.11.6.5.3.2Test parameters

In all test cases, Cell 1 which is PCell operating on a carrier frequency under CCA, and Cell 2 which is neighbor cell operating on a carrier frequency under CCA. RSSI is measured on channel number 2. Supported test configurations are shown in table A.11.6.5.3.2-1. The accuracy of RSSI intra-frequency measurements is tested by using the parameters in A.11.6.5.3.2-2 and A.11.6.5.3.2-3.

Table A.11.6.5.3.2-1: Inter frequency RSSI supported test configurations

Table A.11.6.5.3.2-2: RSSI Inter frequency test parameters

Table A.11.6.5.3.2-3: RSSI RMTC parameters

## A.11.6.5.3.3Test Requirements

The average RSSI measurement accuracy shall fulfil the requirements in sections 10.1.34.2. The nominal RSSI used to evaluate the requirement shall be based on Io in slots corresponding to RSSI measurement time configuration (RMTC).

## A.11.6.6Channel occupancy

## A.11.6.6.1Intra-frequency channel occupancy measurement accuracy on PCC with CCA

## A.11.6.6.1.1Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.1.

## A.11.6.6.1.2Test parameters

In all test cases, Cell 1 is the PCell with CCA. channel occupancy is measured on channel number 1. Supported test configurations are shown in table A.11.6.6.1.2-1. The accuracy of channel occupancy intra-frequency measurements is tested by using the parameters in A.11.6.6.1.2-2 and A.11.6.6.1.2-3.

Table A.11.6.6.1.2-1: Intra frequency CO supported test configurations

Table A.11.6.6.1.2-2: CO Intra frequency test parameters

Table A.11.6.6.1.2-3: CO RMTC parameters

## A.11.6.6.1.3Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.

## A.11.6.6.2Intra-frequency channel occupancy measurement accuracy on SCC with CCA

## A.11.6.6.2.1Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.1.

## A.11.6.6.2.2Test parameters

In all test cases, Cell 1 which is PCell operating on a carrier frequency under CCA, and Cell 2 which is SCell operating on a carrier frequency under CCA. Channel occupancy is measured on channel number 2. Supported test configurations are shown in table A.11.6.6.2.2-1. The accuracy of channel occupancy intra-frequency measurements is tested by using the parameters in A.11.6.6.2.2-2 and A.11.6.6.2.2-3.

Table A.11.6.6.2.2-1: Intra frequency CO supported test configurations

Table A.11.6.6.2.2-2: CO Intra frequency test parameters

Table A.11.6.6.2.2-3: CO RMTC parameters

## A.11.6.6.2.3Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.

## A.11.6.6.3Inter-frequency channel occupancy measurement accuracy on a carrier with CCA

## A.11.6.6.3.1Test Purpose and Environment

The purpose of this test is to verify that the channel occupancy measurement accuracy is within the specified limits. This test will partially verify the channel occupancy measurement accuracy requirements in section 10.1.35.2.

## A.11.6.6.3.2Test parameters

In all test cases, Cell 1 which is PCell operating on a carrier frequency under CCA, and Cell 2 which is neighbor cell operating on a carrier frequency under CCA. Channel occupancy is measured on channel number 2. Supported test configurations are shown in table A.11.6.6.3.2-1. The accuracy of channel occupancy intra-frequency measurements is tested by using the parameters in A.11.6.6.3.2-2 and A.11.6.6.3.2-3.

Table A.11.6.6.3.2-1: Inter frequency CO supported test configurations

Table A.11.6.6.3.2-2: CO Inter frequency test parameters

Table A.11.6.6.3.2-3: CO RMTC parameters

## A.11.6.6.3.3Test Requirements

The nominal reported channelOccupancy shall be 100 %. At least 90 % of channel occupancy reports made by the UE shall indicate this value.

## A.11.6.7E-UTRAN RSRP

## A.11.6.8E-UTRAN RSRQ

## A.11.6.9E-UTRAN SINR

## A.12E-UTRA Standalone Tests with at Least One NR Cell under CCA

## A.12.1RRC_IDLE state mobility

## A.12.1.1Inter-RAT cell re-selection to NR on a carrier frequency with CCA

## A.12.1.1.1E-UTRA Cell reselection to higher priority NR target Cell in FR1 when target cell is subject to CCA

## A.12.1.1.1.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN to NR inter-RAT cell subject to CCA reselection requirements specified in clause 4.2.2.5.7 in TS 36.133 [15].

The test scenario comprises of 1 E-UTRA cell and 1 NR cell subject to CCA as given in tables A.12.1.1.1.1-1, A.8.2.1.1.1-2, A.8.2.1.1.1-3 and A.8.2.1.1.1-4. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. E-UTRA Cell 1 is already identified by the UE prior to the start of the test. Cell 2 is of higher priority than Cell 1.

Table A.12.1.1.1.1-1: Supported test configurations

Table A.12.1.1.1.1-2: General test parameters for E-UTRA cell re-selection FR1 NR cell subject to CCA test case

Table A.12.1.1.1.1-3: Cell specific test parameters for NR Cell 2 subject to CCA

Table A.12.1.1.1.1-4: Cell specific test parameters for E-UTRA Cell 1

## A.12.1.1.1.2Test Requirements

The cell reselection delay to a higher priority NR cell subject to CCA is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration updateon Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 60 + 1.28 x (5 + Me) + TSI_CCA s. Me is the number of DRX cycles with at least one SMTC where there are no SSBs available during the Tevaluate,NR_Intra_CCA. If Me > Me,max the UE is required to restart the evaluation of Cell 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter_CCA + TSI_CCA, and to a lower priority cell can be expressed as: Tevaluate, NR + TSI-NR,

Where:

Thigher_priority_searchSee clause 4.2.2 in TS 36.133 [15]

Tevaluate, NR_ inter_CCASee Table 4.2.2.5.7-1 in clause 4.2.2.5.7

TSI_CCAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell.

Tevaluate, NRSee Table 4.2.2.5.6-1 in clause 4.2.2.5.6 in TS 36.133 [15]

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority NR cell and 7.68 s for the cell re-selection delay to a lower priority cell in the test case, which we allow 8 s.

## A.12.2RRC_CONNECTED state mobility

## A.12.2.1Handover

## A.12.2.1.1E-UTRAN - NR with CCA handover

## A.12.2.1.1.1Test Purpose and Environment

This test shall verify the E-UTRAN to NR FR1 handover requirements specified in clause 5.3.4A in TS 36.133 [15].

The test comprises of one E-UTRA carrier and one NR carrier with CCA. There are two cells and one cell on each carrier. Cell 1 is the E-UTRAN cell and Cell 2 is an inter-RAT NR neighbour cell with CCA.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in table 8.1.2.1-1 of TS 36.133 [15] is configured before T2 begins to enable inter-RAT frequency monitoring. A RRC message implying handover shall be sent to the UE during period T2 after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.12.2.1.1-1. General test parameters are provided in table A.12.2.1.1-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.12.2.1.1-3 and A.12.2.1.1-4 respectively.

Table A.12.2.1.1-1: Supported test configurations for E-UTRAN inter-RAT NR handover

Table A.12.2.1.1-2: General test parameters for E-UTRAN inter-RAT NR handover

Table A.12.2.1.1-3: Cell specific test parameters for E-UTRAN inter-RAT NR handover with CCA (Cell 1)

Table A.12.2.1.1-4: Cell specific test parameters E-UTRAN inter-RAT NR with CCA handover (Cell 2)

## A.12.2.1.1.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 112 + (L1´ + L3)*20 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and is specified in TS36.331.

Tinterrupt = 62 + ( L1´ + L3) * TSMTC; Tinterrupt is defined in TS36.133 clause 5.3.4A.3 where

-L1´ is the number of SMTC occasions not available at the UE during the inter-RAT detection period.

-L3 is the number of consecutive SSB to PRACH occasion association periods during which no PRACH occasion is available for PRACH transmission due to UL CCA failure.  L3 = 0 for Type 2C UL channel access procedure as defined in TS 37.213 [33].

TSMTC = 20 ms is the SMTC periodicity ms in the test.

This gives a total of 112 +( L1´ + L3 )*20 ms.

## A.12.3Void

## A.12.4Measurement procedure

## A.12.4.1E-UTRANNR inter-RAT SFTD measurements

## A.12.4.1.1E-UTRA – NR Inter-RAT SFTD Measurement Delay with NR under CCA in non-DRX

## A.12.4.1.1.1Test Purpose and Environment

The purpose of this test is to partly verify that measurement reporting delay for SFTD between E-UTRA PCell and inter-RAT NR neighbour cell under CCA is within the requirements stated in clauses 8.1.2.4.25 and 8.1.2.4.26 of TS 36.133 [15] for E-UTRA FDD and TDD, respectively, when no measurement gaps are provided and no DRX is configured.

The tests consist of a single time period of duration T1. Two carriers are used in the tests: one E-UTRA carrier with the PCell (Cell 1), and one NR carrier under CCA with the NR neighbour cell (Cell 2).

Prior to the start of time duration T1, the UE is connected to Cell 1 and configured to carry out intra-frequency measurements only. The point in time at which the UE receives, at the UE antenna connector(s), a RRC message containing a measurement configuration for SFTD measurements on RF channel 2 defines the start of time duration T1. Following the start of T1 the UE shall detect Cell 2, determine the SFN and frame time difference of Cell 2 relative to Cell 1, and send a measurement report.

The supported test configurations are listed in table A.12.4.1.1.1-1 below. General test parameters and cell-specific parameters for the NR cell are provided in tables A.12.4.1.1.1-2 and A.12.4.1.1.1-3 below, respectively. Cell-specific parameters for the E-UTRA cell are provided in clause A.3.7.2.1.

Table A.12.4.1.1.1-1: Applicable test configurations for inter-RAT SFTD measurement delay test with NR under CCA

Table A.12.4.1.1.1-2: General test parameters for inter-RAT SFTD measurement delay test with NR under CCA

Table A.12.4.1.1.1-3: Cell specific test parameters for Cell 2 in inter-RAT SFTD measurement delay test with NR under CCA

## A.12.4.1.1.2Test Requirements

Following the start of T1, the UE shall detect Cell 2 and determine the relative time difference between Cell 1 and Cell 2. At latest at TRRC_procedure_delay + Tmeasure_SFTD_LBT_max after the beginning of time duration T1, the UE shall send a measurement report on SFTD between Cell 1 and Cell 2.

The observed rate of successful SFTD reports in repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2×TTIDCCH longer than the measurement reporting delays above due to TTI insertion uncertainty of the measurement report in DCCH.

## A.12.4.2E-UTRANNR inter-RAT measurements on NR carrier frequency under CCA

## A.12.4.2.1E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used

## A.12.4.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21A of TS 36.133 [15] for E-UTRAN FDD-NR measurements under CCA and clause 8.1.2.4.22A of TS 36.133 [15] for E-UTRAN TDD-NR measurements under CCA.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1 on a carrier frequency with CCA. The test parameters are given in tables A.12.4.2.1.1-1, A.12.4.2.1.1-2, A.12.4.2.1.1-3 and A.12.4.2.1.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In this test, measurement gap pattern configuration # 0 as defined in table A.12.4.2.1.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.12.4.2.1.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

Table A.12.4.2.1.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

Table A.12.4.2.1.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

Table A.12.4.2.1.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

## A.12.4.2.1.2Test Requirements

The UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_without_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index. Tidentify_irat_cca_without_index is defined in defined in clause 8.1.2.4.21A.1 and 8.1.2.4.22A.1 in TS 36.133.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.12.4.2.2E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used

## A.12.4.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21A of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22A of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1 on a carrier frequency with CCA. The test parameters are given in tables A.12.4.2.2.1-1, A.12.4.2.2.1-2, A.12.4.2.2.1-3 and A.12.4.2.2.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In this test, measurement gap pattern configuration # 0 as defined in table A.12.4.2.2.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.12.4.2.2.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

Table A.12.4.2.2.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

Table A.12.4.2.2.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

Table A.12.4.2.2.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

## A.12.4.2.2.2Test Requirements

In test 1, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_without_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_without_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.12.4.2.3NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used

## A.12.4.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21A of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22A of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1 on a carrier frequency with CCA.  The test parameters are given in tables A.12.4.2.3.1-1, A.12.4.2.3.1-2, A.12.4.2.3.1-3 and A.12.4.2.3.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In this test, measurement gap pattern configuration # 0 as defined in table A.12.4.2.3.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.12.4.2.3.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR1

Table A.12.4.2.3.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

Table A.12.4.2.3.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 with SSB time index detection

Table A.12.4.2.3.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

## A.12.4.2.3.2Test Requirements

The UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_with_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.12.4.2.4NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used

## A.12.4.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21A of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22A of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA Cell 1 as PCell on E-UTRA RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 1 on a carrier frequency with CCA. The test parameters are given in tables A.12.4.2.4.1-1, A.12.4.2.4.1-2, A.12.4.2.4.1-3 and A.12.4.2.4.1-4. Cell transmits SSBs in DBT windows according to DL CCA model.

In this test, measurement gap pattern configuration # 0 as defined in table A.12.4.2.4.1-2 is provided.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

Table A.12.4.2.4.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR1

Table A.12.4.2.4.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

Table A.12.4.2.4.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 with SSB time index detection

Table A.12.4.2.4.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection

## A.12.4.2.4.2Test Requirements

In test 1, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_with_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than Tidentify_irat_cca_with_index ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.12.4.2.5Void

## A.12.4.2.6Void

## A.12.5Measurement performance

## A.12.5.1E-UTRANNR SFTD

## A.12.5.1.1Inter-RAT SFTD accuracy with NR target cell under CCA

## A.12.5.1.1.1Test Purpose

The purpose of this set of tests is to verify that the SFTD measurement accuracy is within the specified limits. This test will verify the requirements as specified in clause 9.1.28 in TS 36.133 [15] for inter-RAT SFTD measurements between E-UTRA PCell and NR target cell under CCA.

## A.12.5.1.1.2Test Environment

Supported test configurations are shown in table A.12.5.1.1.2-1. In this set of test cases there are two cells on different carriers. Cell 1 is E-UTRAN PCell and Cell 2 is inter-RAT NR target cell under CCA. The test parameters of Cell 1 are given in clause A.12.5.1.1.2-2. The test parameters of Cell 2 are given in table A.12.5.1.1.2-3. The SFTD between PCell and NR target cell shall be set by the test equipment to one of the time differences in table A.12.5.1.1.2-4.

Table A.12.5.1.1.2-1: Supported test configurations for SFTD accuracy with NR target cell under CCA

Table A.12.5.1.1.2-2: Test parameters for inter-RAT SFTD accuracy with NR target cell under CCA (Cell 1)

Table A.12.5.1.1.2-3: Test parameters for inter-RAT SFTD accuracy with NR target cell under CCA (Cell 2)

Table A.12.5.1.1.2-4: Timing offsets for inter-RAT SFTD accuracy test with NR target cell under CCA

## A.12.5.1.1.3Test Requirements

The SFTD reported by the UE consists of 2 elements, SFN offset and frame boundary offset between PCell and inter-RAT NR target cell. The reported SFTD accuracy shall fulfil the requirement in clause 9.1.27 in TS 36.133 [15].

## A.12.5.2Void

## A.12.5.3Void

## A.12.5.4Void

## A.12.5.5Void

## A.12.5.6Void
