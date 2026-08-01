---
type: spec
aliases:
  - 38.133_38133-j50_sA.7-A.704
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.7-A.704/content.md"
---
# TS 38.133 38133-j50_sA.7-A.704

## A.7NR standalone tests with one or more NR cells in FR2

## A.7.1SA: RRC_IDLE state mobility

## A.7.1.1Cell re-selection to NR

## A.7.1.1.1Cell reselection to FR2 intra-frequency NR case

## A.7.1.1.1.1Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements specified in clause 4.2.2.3.

## A.7.1.1.1.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.7.1.1.1.2-1, A.7.1.1.1.2-2 and A.7.1.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only cell 1 is already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.7.1.1.1.2-1: Supported test configurations

Table A.7.1.1.1.2-2: General test parameters for intra frequency NR cell re-selection test case

Table A.7.1.1.1.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case in AWGN

## A.7.1.1.1.3Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration updateon Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 130 s for PC2/3/4 devices and less than 258 s for PC1 devices.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration updateon cell 1.

The cell re-selection delay to an already detected cell shall be less than 27 s for PC2/3/4 devices and less than 53 s for PC1 devices.

The cell re-selection delay to an already detected cell shall be less than 27 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_IntraSee table 4.2.2.3-1 in clause 4.2.2.3

Tevaluate, NR_ intraSee table 4.2.2.3-1 in clause 4.2.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

For the cell re-selection delay to a newly detectable in this test case, this gives:

-129.28 s, allow 130 s, for PC2/3/4 devices

-257.28 s, allow 258 s, for PC1 devices

For the cell re-selection delay to an already detected cell in this test case, this gives

-26.88 s, allow 27 s, for PC2/3/4 devices

-52.48 s, allow 53 s, for PC1 devices

## A.7.1.1.2Cell reselection to FR2 inter-frequency NR case

## A.7.1.1.2.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements specified in clause 4.2.2.4.

## A.7.1.1.2.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.7.1.1.2.2-1, A.7.1.1.2.2-2 and A.7.1.1.2.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.7.1.1.2.2-1: Supported test configurations

Table A.7.1.1.2.2-2: General test parameters for FR2 inter frequency NR cell re-selection test case

Table A.7.1.1.2.2-3: Cell specific test parameters for FR2 inter frequency NR cell re-selection test case in AWGN

## A.7.1.1.2.3Test Requirements

The cell reselection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps  on cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration updateon cell 2.

The cell re-selection delay to a higher priority cell shall be less than 87 s for PC2/3/4 devices and less than 113 s for PC1 devices.

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration updateon cell 1.

The cell re-selection delay to a lower priority cell shall be less than 27 s for PC2/3/4 devices and less than 53 s for PC1 devices.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Thigher_priority_searchSee clause 4.2.2.7

Tevaluate, NR_ interSee table 4.2.2.4-1 in clause 4.2.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

For the cell re-selection delay to a higher priority cell in this test case, this gives:

-86.88 s, allow 87 s, for PC2/3/4 devices

-112.48 s, allow 113 s, for PC1 devices

For the cell re-selection delay to a lower priority cell in the test case, this gives

-26.88 s, allow 27 s, for PC2/3/4 devices

-52.48 s, allow 53 s, for PC1 devices

## A.7.1.1.3Cell reselection to FR2 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion

## A.7.1.1.3.1Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for UE configured with relaxed measurement criterion specified in clause 4.2.2.9.2.

## A.7.1.1.3.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.7.1.1.3.2-1, A.7.1.1.3.2-2 and A.7.1.1.3.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. During T1 and T2, only criteria lowMobilityEvalutation is configured and fulfilled, where (SrxlevRef – Srxlev) < SSearchDeltaP. UE has not registered with network for the tracking area containing Cell 2.

Table A.7.1.1.3.2-1: Supported test configurations

Table A.7.1.1.3.2-2: General test parameters for FR2 intra-frequency NR cell re-selection test case for UE fulfilling low mobility criterion

Table A.7.1.1.3.2-3: Cell specific test parameters for FR2 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling low mobility criterion

## A.7.1.1.3.3Test Requirements

The cell reselection delay to an already detected cell for UE fulfilling low mobility relaxed criterion is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected cell shall be less than 79 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to an already detectable cell can be expressed as: Tevaluate, NR_Intra + TSI-NR,

Where:

Tevaluate, NR_IntraSee table 4.2.2.9.2-1 in clause 4.2.2.9,

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 78.08 s, allow 79 s for the cell re-selection delay to an already detected cell for UE fulfilling low mobility criterion in the test case.

## A.7.1.1.4Cell reselection to FR2 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion

## A.7.1.1.4.1Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for UE configured with relaxed measurement criterion specified in clause 4.2.2.9.3.

## A.7.1.1.4.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.7.1.1.4.2-1, A.7.1.1.4.2-2 and A.7.1.1.4.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. During T1 and T2, only criteria cellEdgeEvaluation is configured and fulfilled, where Srxlev> SSearchThresholdP. UE has not registered with network for the tracking area containing Cell 2.

Table A.7.1.1.4.2-1: Supported test configurations

Table A.7.1.1.4.2-2: General test parameters for FR2 intra-frequency NR cell re-selection test case for UE fulfilling not-at-cell edge criterion

Table A.7.1.1.4.2-3: Cell specific test parameters for FR2 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling not-at-cell edge criterion

## A.7.1.1.4.3Test Requirements

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 79 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to an already detected cell can be expressed as: Tevaluate, NR_Intra + TSI-NR,

Where:

Tevaluate, NR_IntraSee table 4.2.2.9.3-1 in clause 4.2.2.9,

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 78.08 s, allow 79 s for the cell re-selection delay to an already detected cell for UE fulfilling  not-at-cell edge criterion in the test case.

## A.7.1.1.5Cell reselection to FR2 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion

## A.7.1.1.5.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for UE fulfilling low mobility criterion specified in clause 4.2.2.10.2.

## A.7.1.1.5.2Test Parameters

The test scenario comprises of 2 cells (Cell 1 and Cell 2) on 2 different NR carriers respectively as given in tables A.7.1.1.5.2-1, A.7.1.1.5.2-2 and A.7.1.1.5.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. Cell 2 is of higher priority than Cell 1. The UE is configured with lowMobilityEvalutation criterion [2].

Table A.7.1.1.5.2-1: Supported test configurations

Table A.7.1.1.5.2-2: General test parameters for FR2 inter frequency NR cell re-selection test case for UE fulfilling low mobility criterion

Table A.7.1.1.5.2-3: Cell specific test parameters for FR2 inter frequency NR cell re-selection test case in AWGN for UE fulfilling low mobility criterion

## A.7.1.1.5.3Test Requirements

The cell reselection delay to an already detected low priority cell (Cell 1) for UE fulfilling low mobility criterion is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected low priority cell, Cell 1, shall be less than 79 s.

The cell reselection delay to an already detected high priority cell (Cell 2) for UE fulfilling low mobility criterion is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected high priority cell, Cell 2, shall be less than 79 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE 1:The cell re-selection delay to an already detected low priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR

NOTE 2:The cell re-selection delay to an already detected higher priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR

Where:

Tevaluate, NR_ interSee table 4.2.2.10.2-1 in clause 4.2.2.10.2

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 78.08 s, allow 79 s for the cell re-selection delay to an already detected low priority cell for UE fulfilling low mobility criterion in the test case.

This gives a total of 78.08 s, allow 79 s for the cell re-selection delay to an already detected high priority cell for UE fulfilling low mobility criterion in the test case.

## A.7.1.1.6Cell reselection to FR2 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion

## A.7.1.1.6.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for UE fulfilling not-at-cell edge criterion specified in clause 4.2.2.10.3.

## A.7.1.1.6.2Test Parameters

The test scenario comprises of 2 cells (Cell 1 and Cell 2) on 2 different NR carriers respectively as given in tables A.7.1.1.6.2-1, A.7.1.1.6.2-2 and A.7.1.1.6.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. Cell 2 is of higher priority than Cell 1. The UE is configured with cellEdgeEvaluation criterion [2].

Table A.7.1.1.6.2-1: Supported test configurations

Table A.7.1.1.6.2-2: General test parameters for FR2 inter frequency NR cell re-selection test case for UE fulfilling not-at-cell edge criterion

Table A.7.1.1.6.2-3: Cell specific test parameters for FR2 inter frequency NR cell re-selection test case in AWGN for UE fulfilling not-at-cell edge criterion

## A.7.1.1.6.3Test Requirements

The cell reselection delay to an already detected low priority cell (Cell 1) for UE fulfilling not-at-cell edge criterion is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected low priority cell, Cell 1, shall be less than 79 s.

The cell reselection delay to an already detected high priority cell (Cell 2) for UE fulfilling not-at-cell edge criterion is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected high priority cell, Cell 2, shall be less than 79 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE 1:The cell re-selection delay to an already detected low priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR

NOTE 2:The cell re-selection delay to an already detected higher priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR

Where:

Tevaluate, NR_ interSee table 4.2.2.10.3-1 in clause 4.2.2.10.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 78.8 s, allow 79 s for the cell re-selection delay to an already detected low priority cell for UE fulfilling not-at-cell edge criterion in the test case.

This gives a total of 78.08 s, allow 79 s for the cell re-selection delay to an already detected high priority cell for UE fulfilling not-at-cell edge criterion in the test case.

## A.7.1.1.7Cell reselection to FR2 intra-frequency NR case for FR2 power class 6 UE configured with highSpeedMeasFlagFR2-r17

## A.7.1.1.7.1Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements specified in clause 4.2.2.3 for FR2 power class 6 UE configured with highSpeedMeasFlagFR2-r17.

## A.7.1.1.7.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.7.1.1.7.2-1, A.7.1.1.7.2-2 and A.7.1.1.7.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only cell 1 is already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2.

Table A.7.1.1.7.2-1: Supported test configurations

Table A.7.1.1.7.2-2: General test parameters for intra frequency NR cell re-selection test case

Table A.7.1.1.7.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case in AWGN

## A.7.1.1.7.3Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration updateon Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 7 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration updateon cell 1.

The cell re-selection delay to an already detected cell shall be less than 4 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_IntraSee table 4.2.2.3-3 in clause 4.2.2.3

Tevaluate, NR_ intraSee table 4.2.2.3-3 in clause 4.2.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 6.4 s, allow 7 s for the cell re-selection delay to a newly detectable cell and 3.2 s for the cell re-selection delay to an already detected cell in the test case, which we allow 4 s.

## A.7.1.1.8Cell reselection to FR2 inter-frequency NR case for UE configured with highSpeedMeasFlagFR2-r17

## A.7.1.1.8.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for UE that supports measEnhCAInterFreqFR2-r18 and configured with highSpeedMeasFlagFR2-r17 specified in clause 4.2.2.4.

## A.7.1.1.8.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.7.1.1.8.2-1, A.7.1.1.8.2-2 and A.7.1.1.8.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas and cell 2 is of higher priority than cell 1. Note that the value of configured highSpeedMeasFlagFR2-r17 is set to set2.

Table A.7.1.1.8.2-1: Supported test configurations

Table A.7.1.1.8.2-2: General test parameters for FR2 inter frequency NR cell re-selection test case

Table A.7.1.1.8.2-3: Cell specific test parameters for FR2 inter frequency NR cell re-selection test case in AWGN

## A.7.1.1.8.3Test Requirements

The cell reselection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2 and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 1 and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on cell 1.

The cell re-selection delay to a lower priority cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter_HST + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, NR_ inter_HST + TSI-NR,

Where:

Thigher_priority_searchSee clause 4.2.2.7

Tevaluate, NR_ inter_HSTSee table 4.2.2.4-2a in clause 4.2.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.04 s, allow 68 s for the cell re-selection delay to a higher priority cell and 7.04 s for the cell re-selection delay to a lower priority cell in the test case, which we allow 8 s.

## A.7.1.1.9Cell reselection to FR2 intra-frequency NR case for FR2 cell supporting OD-SIB1

## A.7.1.1.9.1Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for UE capable of on- demand SIB1 acquisition and reselecting to an NES cell as described in [2, TS 38.331].

## A.7.1.1.9.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.7.1.1.9.2-1, A.7.1.1.9.2-2 and A.7.1.1.9.2-3. The test consists of one time period with time duration of T1. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. UE has not registered with network for the tracking area containing cell 2. The UE has received the SIB26 IE to assist OD-SIB1 acquisition to cell 2 according to [2, TS 38.331]. During T1 the UE reselects to cell 2 supporting on-demand SIB1.

Table A.7.1.1.9.2-1: Supported test configurations

Table A.7.1.1.9.2-2: General test parameters for FR2 intra-frequency NR cell re-selection test case for UE reselecting to OD-SIB1 based cell

Table A.7.1.1.9.2-3: Cell specific test parameters for FR2 intra-frequency NR cell re-selection test case in AWGN for UE reselecting to OD-SIB1 based cell

## A.7.1.1.9.3Test Requirements

The cell reselection delay to the already detected OD-SIB1 based cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 2 and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on cell 2.

The cell re-selection delay to an already detected OD-SIB1 based cell shall be less than [28]s for PC2/3/4 and [54]s for PC1 for the reselection from cell 1 to cell 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to an already detected OD-SIB1 based cell can be expressed as: Tevaluate, NR_Intra + TSI-NR + TOD-SIB1,

Where:

Tevaluate, NR_ intraSee table 4.2.2.3-1 in clause 4.2.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280ms is assumed in this test case.

TOD-SIB1   Maximum time for performing OD-SIB1 request and OD-SIB1 acquisition; 1s is assumed in this case.

For the cell re-selection delay including TOD-SIB1 to an already detected OD-SIB1 based cell during T1 in this test case, this gives

-27.88 s, allow 28s, for PC2/3/4 devices

-53.48 s, allow 54s, for PC1 devices

## A.7.1.1.10Cell reselection to FR2 inter-frequency NR case for FR2 cell supporting OD- SIB1

## A.7.1.1.10.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for UE capable of on- demand SIB1 acquisition and reselecting to an NES cell as described in [2, TS 38.331].

## A.7.1.1.10.2Test Parameters

The test scenario comprises of 2 cells (cell 1 and cell 2) on 2 different NR carriers respectively as given in tables A.7.1.1.10.2-1, A.7.1.1.10.2-2 and A.7.1.1.10.2-3. The test consists of one time period with time duration of T1. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. UE has not registered with network for the tracking area containing cell 2. The UE has received the SIB26 IE to assist OD-SIB1 acquisition to cell 2 according to [2, TS 38.331]. During T1 the UE reselects to cell 2 supporting on-demand SIB1.

Table A.7.1.1.10.2-1: Supported test configurations

Table A.7.1.1.10.2-2: General test parameters for FR2 inter-frequency NR cell re-selection test case for UE reselecting to OD-SIB1 based cell

Table A.7.1.1.10.2-3: Cell specific test parameters for FR2 inter frequency NR cell re-selection test case in AWGN for UE reselecting to OD-SIB1 based cell

## A.7.1.1.10.3Test Requirements

The cell reselection delay to a lower priority OD-SIB1 based cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on cell 2.

The cell re-selection delay to an already detected lower priority OD-SIB1 based cell shall be less than [28]s for PC2/3/4 and [54]s for PC1 for the reselection from cell 1 to cell 2.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to an already detected lower priority OD-SIB1 based cell can be expressed as: Tevaluate, NR_Inter + TSI-NR + TOD-SIB1,

Where:

Tevaluate, NR_ interSee table 4.2.2.4-1 in clause 4.2.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280ms is assumed in this test case.

TOD-SIB1   Maximum time for performing OD-SIB1 request and OD-SIB1 acquisition; 1s is assumed in this case.

For the cell re-selection delay including TOD-SIB1 to an already detected OD-SIB1 based cell during T1 in this test case, this gives

-27.88 s, allow 28s, for PC2/3/4 devices

-53.48 s, allow 54s, for PC1 devices

## A.7.2SA: RRC_INACTIVE state mobility

## A.7.2.1Small Data Transmission

## A.7.2.1.1TA validation for CG-SDT in FR2

## A.7.2.1.1.1Test Purpose and Environment

The purpose of this test is to partly verify that the UE properly perform TA validation for CG-SDT transmission in clause 5.5.3. The test includes two sub-tests, Sub-test#1 for testing valid TA where UE can initiat CG-SDT transmission, and Sub-test#2 for testing invalid TA where UE does not initiate CG-SDT transmission. Subtest#2 is only tested if Sub-test#1 is passed. For each sub-test, UE is configured with CG-SDT configurations when entering RRC Inactive state. Sub-test#1 consists of four successive time periods, with time duration of T1, T2, T3 and T4 repectively. Sub-test#2 consists of two successive time periods, with time duration of T5 and T6 repectively. There is one cell, which is the active NR cell in FR2. Figure A.7.2.1.1.1-1 shows the variation of the RSRP over the duration of Sub-test#1, and figure A.7.2.1.1.1-2 shows the variation of the RSRP over the duration of Sub-test#2.

In Sub-test#1:

-Prior to the time point TA, the UE shall be fully synchronized to PCell (Cell 1), be registered to the cell and have entered RRC connected mode.

-Before starting the test at time point TA, test equipment configures RSRP to P0. At time point TB, RSRP is changed from P0 to P1.

-At time point TC which is W1 after time point TB, UE expect to receive RRC release with CG SDT configuration and RRC status is changed to INACTIVE status.

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

W1 equals to 480 ms and W2 equals to 480 ms based on requirements in clause 5.5.3. W3 is 1060 ms.

Supported test configurations are shown in table A.7.2.1.1.1-1. The test parameters are given in tables A.7.2.1.1.1-2 and A.7.2.1.1.1-3.

Table A.7.2.1.1.1-1: Supported test configurations for FR2 PCell

Table A.7.2.1.1.1-2: General test parameters for TA validation for CG-SDT in FR2

Table A.7.2.1.1.1-3: Cell specific test parameters TA validation for CG-SDT in FR2

Figure A.7.2.1.1.1-1: RSRP variation for TA validation for CG-SDT Sub-test#1

Figure A.7.2.1.1.1-2: RSRP variation for TA validation for CG-SDT Sub-test#2

## A.7.2.1.1.2Test Requirements

The UE behaviour in each test during time durations shall be as follows:

During Sub-test#1, UE shall transmit UL data with CG-SDT within 1060 ms after time point TF.

During Sub-test#2, after passing Sub-test#1, UE shall not transmit UL data with CG-SDT.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.2.2Cell reselection for positioning

## A.7.2.2.1Cell reselection to FR2 intra-frequency NR case with RRC_ INACTIVE eDRX and positioning SRS

## A.7.2.2.1.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell reselection requirements specified in clause 5.6.1A.2, when UE is in RRC_INACTIVE and configured with eDRX and to transmit SRS for positioning.

## A.7.2.2.1.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.7.2.2.1.2-1, A.7.2.2.1.2-2 and A.7.2.2.1.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Only cell 1 is already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing cell 2. UE is configured with transmit SRS for positioning in cell 1.

Table A.7.2.2.1.2-1: Supported test configurations

Table A.7.2.2.1.2-2: General test parameters for intra frequency NR cell re-selection test case

Table A.7.2.2.1.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case in AWGN

## A.7.2.2.1.3Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration updateon Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 355 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra + TSI-NR,

Where:

Tdetect, NR_IntraSee table 5.6.1A.2-2 in clause 5.6.1A.2

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 354.56 s, allow 355 s for the cell re-selection delay to a newly detectable cell.

## A.7.3RRC_CONNECTED state mobility

## A.7.3.1Handover

## A.7.3.1.1Inter-frequency handover from FR1 to FR2; unknown target cell

## A.7.3.1.1.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR2 inter frequency handover requirements specified in clause 6.1.1.5.

## A.7.3.1.1.2Test Parameters

Supported test configurations are shown in table A.7.3.1.2.2-1. Both handover delay and interruption length are tested by using the parameters in table A.7.3.1.1.2-2, and A.7.3.1.1.2-3.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Starting T2, cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.7.3.1.1.2-1: Inter-frequency handover from FR1 to FR2 test configurations

Table A.7.3.1.1.2-2: General test parameters Inter-frequency handover from FR1 to FR2

Table A.7.3.1.1.2-3: Cell specific test parameters for NR FR1-FR2 Inter frequency handover test case

## A.7.3.1.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 572 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 562 ms in the test. Tinterrupt is defined in clause 6.1.1.5.2.

This gives a total of 572 ms.

## A.7.3.1.2Intra-frequency handover from FR2 to FR2; unknown target cell

## A.7.3.1.2.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 intra frequency handover requirements specified in clause 6.1.1.4.

## A.7.3.1.2.2Test Parameters

Supported test configurations are shown in table A.7.3.1.2.2-1. Both handover delay and interruption length are tested by using the parameters in table A.7.3.1.2.2-2, and A.7.3.1.2.2-3.

The test scenario comprises of two cells on same carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Starting T2, cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.7.3.1.2.2-1: Intra-frequency handover from FR2 to FR2 test configurations

Table A.7.3.1.2.2-2: General test parameters Intra-frequency handover from FR2 to FR2

Table A.7.3.1.2.2-3: Cell specific test parameters for NR FR2-FR2 Intra frequency handover test case

## A.7.3.1.2.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 232  ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 222 ms in the test. Tinterrupt is defined in clause 6.1.1.4.2.

This gives a total of 232 ms.

## A.7.3.1.3Inter-frequency handover from FR2 to FR2; unknown target cell

## A.7.3.1.3.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 inter frequency handover requirements specified in clause 6.1.1.4.

## A.7.3.1.3.2Test Parameters

Supported test configurations are shown in table A.7.3.1.3.2-1. Both handover delay and interruption length are tested by using the parameters in table A.7.3.1.3.2-2, and A.7.3.1.3.2-3.

The test scenario comprises of carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Starting T2, cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.7.3.1.3.2-1: Inter-frequency handover from FR2 to FR2 test configurations

Table A.7.3.1.3.2-2: General test parameters Inter-frequency handover from FR2 to FR2

Table A.7.3.1.3.2-3: Cell specific test parameters for NR FR2-FR2 Inter frequency handover test case

## A.7.3.1.3.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 552 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 542 ms in the test. Tinterrupt is defined in clause 6.1.1.4.2.

This gives a total of 552 ms.

## A.7.3.1.4Inter-band inter-frequency synchronous DAPS handover from FR1 to FR2

## A.7.3.1.4.1Test Purpose and Environment

This test is to verify the requirement for the FR1-to-FR2 Inter-band inter-frequency synchronous DAPS handover requirements specified in clause 6.1.3.4.

## A.7.3.1.4.2Test Parameters

Supported test configurations are shown in table A.7.3.1.4.2-1. Both handover delay and interruption length are tested by using the parameters in table A.7.3.1.4.2-2, A.7.3.1.4.2-3 and A.7.3.1.4.2-4.

The test scenario comprises of two bands each with one cell. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively.

Before the start of T1, the UE is connected to Cell 1 (source PCell) on radio channel 1 but is not aware of Cell 2 (neighbour cell) on radio channel 2. The UE shall be configured with periodic CSI reporting for Cell 1. During T1, the UE shall not have any timing information of Cell 2.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event A4 is configured for neighbour cell (Cell 2), and the UE is configured with the measurement gaps (gap pattern ID # 0). Starting T2, Cell 2 becomes known to the UE. During T2, the UE shall report Event A4. After receiving the Event A4, the test system shall send a RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the test system receives the ACK of the PDSCH corresponding to the last TTI containing the RRC message implying DAPS handover to Cell 2 (target PCell) sent to the UE. During T3, the UE shall be able to perform random access to Cell 2. DL schedule and UL feedback to cell 1 shall be avoided when UE is required to perform DL reception or UL transmission in PRACH procedure in cell 2, except preamble transmission. After the RACH procedure is completed, the test system shall send a RRC message to the UE to release Cell 1 (source cell) on radio channel 1.

The start of T4 is the instant when the test system receives the ACK of the PDSCH corresponding to the last TTI containing the RRC message implying source cell release sent to the UE. During T4, the UE shall perform source cell release.

Starting T5, the UE shall stop sending CSI report to the source cell.

Table A.7.3.1.4.2-1: Inter-band inter-frequency synchronous DAPS handover from FR1 to FR2 test configurations

Table A.7.3.1.4.2-2: General test parameters for Inter-band inter-frequency synchronous DAPS handover from FR1 to FR2

Table A.7.3.1.4.2-3: Cell specific test parameters for Inter-band inter-frequency synchronous DAPS handover from FR1 to FR2 (Cell 1 in FR1)

Table A.7.3.1.4.2-4: Cell specific test parameters for Inter-band inter-frequency synchronous DAPS handover from FR1 to FR2 (Cell 2 in FR2)

## A.7.3.1.4.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 92 ms from the beginning of time period T3. During Dhandover1, the interruption on Cell 1 shall not exceed Tinterrupt1 as defined in table 6.1.3.4.2-1 for synchronous DAPS HO.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay Dhandover1 can be expressed as: TRRC_procedure + TIU + Tprocessing + T∆ + Tmargin, where:

TRRC_procedure = 10 ms and is specified in clause 12 in TS 38.331 [2].

TIU = 20 ms in the test. TIU is defined in clause 6.1.1.2.2.

T∆ = 20 ms in the test. T∆ is defined in clause 6.1.1.2.2.

Tprocessing = 40 ms in the test. Tprocessing is defined in clause 6.1.1.2.2.

Tmargin = 2 ms in the test. Tmargin is defined in clause 6.1.1.2.2.

This gives a total of 92 ms.

The UE shall complete to release Cell 1 less than (10 ms + Tinterrupt2) from the beginning of time period T4. During Dhandover2, the interruption on Cell 2 shall not exceed Tinterrupt2 as defined in table 6.1.3.4.2-2 for synchronous DAPS HO.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay Dhandover2 can be expressed as: TRRC_procedure + Tinterrupt2, where:

TRRC_procedure = 10 ms and is specified in clause 12 in TS 38.331 [2].

## A.7.3.1.5Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR2

## A.7.3.1.5.1Test Purpose and Environment

This test is to verify the requirement for the FR1-to-FR2 Inter-band inter-frequency asynchronous DAPS handover requirements specified in clause 6.1.3.4.

## A.7.3.1.5.2Test Parameters

Supported test configurations are shown in table A.7.3.1.5.2-1. Both handover delay and interruption length are tested by using the parameters in table A.7.3.1.5.2-2, A.7.3.1.5.2-3 and A.7.3.1.5.2-4.

The test scenario comprises of two bands each with one cell. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively.

Before the start of T1, the UE is connected to Cell 1 (source PCell) on radio channel 1 but is not aware of Cell 2 (neighbour cell) on radio channel 2. The UE shall be configured with periodic CSI reporting for Cell 1. During T1, the UE shall not have any timing information of Cell 2.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event A4 is configured for neighbour cell (Cell 2), and the UE is configured with the measurement gaps (gap pattern ID # 0). Starting T2, Cell 2 becomes known to the UE. During T2, the UE shall report Event A4. After receiving the Event A4, the test system shall send a RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the test system receives the ACK of the PDSCH corresponding to the last TTI containing the RRC message implying DAPS handover to Cell 2 (target PCell) sent to the UE. During T3, the UE shall be able to perform random access to Cell 2. DL schedule and UL feedback to cell 1 shall be avoided when UE is required to perform DL reception or UL transmission in PRACH procedure in cell 2, except preamble transmission. After the RACH procedure is completed, the test system shall send a RRC message to the UE to release Cell 1 (source cell) on radio channel 1.

The start of T4 is the instant when the the test system receives the ACK of the PDSCH corresponding to last TTI containing the RRC message implying source cell release sent to the UE. During T4, the UE shall perform source cell release.

Starting T5, the UE shall stop sending CSI report to the source cell.

Table A.7.3.1.5.2-1: Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR2 test configurations

Table A.7.3.1.5.2-2: General test parameters for Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR2

Table A.7.3.1.5.2-3: Cell specific test parameters for Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR2 (Cell 1 in FR1)

Table A.7.3.1.5.2-4: Cell specific test parameters for Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR2 (Cell 2 in FR2)

## A.7.3.1.5.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 92 ms from the beginning of time period T3. During Dhandover1, the interruption on Cell 1 shall not exceed Tinterrupt1 as defined in table 6.1.3.4.2-1 for asynchronous DAPS HO.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay Dhandover1 can be expressed as: TRRC_procedure + TIU + Tprocessing + T∆ + Tmargin, where:

TRRC_procedure = 10 ms and is specified in clause 12 in TS 38.331 [2].

TIU = 20 ms in the test. TIU is defined in clause 6.1.1.2.2.

T∆ = 20 ms in the test. T∆ is defined in clause 6.1.1.2.2.

Tprocessing = 40 ms in the test. Tprocessing is defined in clause 6.1.1.2.2.

Tmargin = 2 ms in the test. Tmargin is defined in clause 6.1.1.2.2.

This gives a total of 792 ms.

The UE shall complete to release Cell 1 less than (10 ms + Tinterrupt2) from the beginning of time period T4. During Dhandover2, the interruption on Cell 2 shall not exceed Tinterrupt2 as defined in table 6.1.3.4.2-2 for asynchronous DAPS HO.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay Dhandover2 can be expressed as: TRRC_procedure + Tinterrupt2, where:

TRRC_procedure = 10 ms and is specified in clause 12 in TS 38.331 [2].

## A.7.3.1.6Handover with PSCell from SA to EN-DC with unknown FR2 target PScell

## A.7.3.1.6.1Test Purpose and Environment

This test is to verify the PSCell addition delay requirements specified in clause 6.1.5.2 for handover with PSCell from NR SA to EN-DC with sequential processing when the SMTC of target unknown PSCell is present in RRCConnectionReconfiguration and the target PSCell is in FR2.

## A.7.3.1.6.2Test Parameters

The test scenario comprises of three carriers and one cell on each carrier. Cell 1 is the NR PCell, Cell 2 is an inter-RAT E-UTRAN neighbour cell and Cell 3 is an NR neighbour cell, on radio channel 1 in FR1, radio channel 2 in E-UTRAN in FR1 and radio channel 3 in FR2, respectively.

The test consists of three successive time periods, with time durations of T1, T2, T3 and T4 respectively. No gap patterns are configured in the test case.

At the start of time duration T1, the UE does not have any timing information of cell 2 and cell 3, and the UE is only monitoring Cell 1. During T1, only Cell 1 is known to the UE.

Starting T2, cell 2 and cell 3 become detectable. The RRC message implying handover with PSCell shall be sent to the UE during period T2 after the UE has reported Event B2 and Event B1. The start of T2 is the instant when the last TTI containing the RRC message implying handover with PSCell is sent to the UE. The handover with PSCell message shall contain Cell 2 as the target cell and Cell 3 as PSCell-to-be added. The RRC message (to add PSCell) also includes a request for the UE to start periodic CSI reporting for the PSCell after the PSCell has been successfully added.

The point in time at which the RRC message implying HO (Cell 2) with PSCell (Cell 3) is received at the UE antenna connector defines the start of period T3.

During T3, the UE shall carry out random access (i.e., transmit the PRACH) towards the Cell 2 and Cell 3. The test system shall observe the UE sends PRACH to E-UTRAN Cell 2 and PSCell (Cell 3) during period T3. Reception by the test system of the PRACH preambles defines the end of T3.

During T4, the UE shall send periodic CSI reports in PSCell and the test system shall observe the periodic reporting of CSI for PSCell.

Supported test configurations are shown in table A.7.3.1.6.2-1. General test parameters are provided in table A.6.3.1.14.1-2. Cell specific test parameters for NR Cell 1, E-UTRAN PCell Cell 2 and NR PScell Cell 3 are provided in tables A.6.3.1.14.1-3, A.6.3.1.14.1-4 and A.6.3.1.14.1-5 respectively.

Table A.7.3.1.6.2-1: Handover with PSCell from NR SA to EN-DC test configurations

Table A.7.3.1.6.2-2: General test parameters for handover with PSCell from NR SA to EN-DC

Table A.7.3.1.6.2-3: Cell specific test parameters for NR Cell 1

Table A.7.3.1.6.2-4: Cell specific test parameters for E-UTRA Cell 2

Table A.7.3.1.6.2-5: Cell specific test parameters for NR Cell 3

Table A.7.3.1.6.2-6: OTA related test parameters

## A.7.3.1.6.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 175 ms Note1 from the beginning of time period T3.

The UE shall start to transmit the PRACH to Cell 3 less than 692 ms Note2 from the beginning of time period T3.

The rate of correct PSCell addition observed during repeated tests shall be at least 90 %.

NOTE1:The handover delay can be expressed as specified in clause 6.1.5.2:

-DHOwithPSCell_PCell = RRC procedure delay + Tinterrupt, where

-RRC procedure delay = 50 ms.

-Tinterrupt = 125 ms.

NOTE2:The PSCell addition delay can be expressed as follows as specified in clause 6.1.5.2.2:

RRC procedure delay = 50 ms and is specified in clause 12 in TS 38.331 [2].

Tprocessing is as defined as 50 ms in the test.

Tsearch_HO is as defined as 80 ms in the test.

Tsearch_PSCell is as defined as 480 ms in the test.

T∆ is defined as 20 ms in the test.

TPSCell_ DU is defined as 10 ms in the test.

This gives a total of 692 ms.

## A.7.3.1.7HO with PSCell from FR1 NR-SA to EN-DC with known E-UTRA PCell and known FR2 PSCell

## A.7.3.1.7.1Test purpose and environment

The purpose of this test is to verify that the delay of HO with PSCell from FR1 NR-SA to EN-DC with known E-UTRA PCell and known FR2 PSCell are within the requirements stated in clause 6.1.5.2.2 of TS 36.133 [15] for the case when the E-UTRA PCell and FR2 PSCell are known by the UE at the time of handover with PSCell.

The test consists of three successive time periods with duration of T1, T2, and T3. There are three carriers each with one cell. Before the test starts the UE is connected to Cell 1 (source FR1 PCell) on radio channel 1 (FR1 PCC) and is aware of Cell 2 (target E-UTRA PCell) on radio channel 2 and Cell 3 (FR2 target PSCell) on radio channel 3. The UE is monitoring both cell 2 and cell 3 before receives a RRC message implying handover with PSCell.

At the start of time duration T1, the UE does not have any timing information of Cell 2 and Cell 3. Starting T2, Cell 2 and Cell 3 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in table 9.1.2-1 is configured before T2 begins to enable inter-RAT frequency monitoring. The test system shall send a RRC message to the UE to trigger HO (Cell 2) with PSCell (Cell 3) during period T2, after UE has reported Event B2 and Event B1. The handover with PSCell message shall contain Cell 2 as the target cell and Cell 3 as PSCell-to-be added. The RRC message (to add PSCell) also includes a request for the UE to start periodic CSI reporting for the PSCell after the PSCell has been successfully added.

The point in time at which the RRC message implying HO (Cell 2) with PSCell (Cell 3) is received at the UE antenna connector defines the start of period T3. During T3, the UE shall carry out random access (i.e., transmit the PRACH) towards the Cell 2 and Cell 3. The test system shall observe the UE sends PRACH to Cell 2 and Cell 3 during period T3. Reception by the test system of the PRACH preambles defines the end of T3.

The test system shall observe the UE sends PRACH to E-UTRAN Cell 2 and PSCell (Cell 3) during period T3.

During T4, the UE shall send periodic CSI reports in PSCell and the test system shall observe the periodic reporting of CSI for PSCell.

Supported test configurations are shown in A.7.3.1.7.1-1. The test parameters for the E-UTRA cell are given in table A.3.7.2.2-1. The E-UTRA cell once set up is not changed across time. The test parameters for NR cell are given in tables A.7.3.1.7.1-2, cell-specific parameters in A.7.3.1.7.1-3, A.7.3.1.7.1-4, A.7.3.1.7.1-5 and OTA parameters in A.7.3.1.7.1-6 below.

Table A.7.3.1.7.1-1: Supported test configurations for FR2 PSCell

Table A.7.3.1.7.1-2: General Test Parameters for HO with PSCell

Table A.7.3.1.7.1-3: Cell specific test parameters for Cell 1

Table A.7.3.1.7.1-4: Cell specific test parameters for Cell 2

Table A.7.3.1.7.1-5: Cell specific test parameters for Cell 3

Table A.7.3.1.7.1-6: OTA related test parameters

## A.7.3.1.7.2Test Requirements

In this test, the UE shall start to transmit the PRACH to E-UTRA Cell 2 less than 105 ms Note1 from the beginning of time period T3.

The UE shall transmit the PRACH to PSCell at latest 137 msNote2 from the beginning of time period T3.

The rate of correct observed PSCell addition delay in HO with PSCell during repeated tests shall be at least 90 %.

NOTE1:The handover delay can be expressed as specified in clause 6.1.5.2:

DHOwithPSCell_PCell = RRC procedure delay + Tinterrupt,

Where RRC procedure delay = 50 ms, Tinterrupt = Tsearch_HO + TIU + Tprocessing is defined in clause 6.1.5.2.1, where

Tsearch = 0 ms,

TIU = 10 ms,

Tprocessing = 45 ms.

Note2:The PSCell addition delay can be expressed as follows as specified in clause 6.1.5.2:

DHOwithPSCell_PSCell = TRRC_delay + Tprocessing + Tsearch_HO + Tsearch_PSCell + T∆ + TPSCell_ DU + 2 ms

Where:

TRRC_delay = 50 ms

Tprocessing = 45 ms

Tsearch_HO = 0 ms

Tsearch_PSCell = 0 ms

T∆ = 20 ms

TPSCell_ DU = 1*10+10 = 20 ms

## A.7.3.1.8NR PSCell change delay in HO with PSCell from NR-DC to NR-DC

## A.7.3.1.8.1Test Purpose and Environment

The purpose of this test is to verify the PSCell change delay requirements in HO with PSCell from NR-DC to NR-DC defined in clauses 6.1.5.4.2. The requirements are applicable to NR FR1-FR1 inter-frequency PCell handover and NR FR2-FR2 intra-frequency PSCell change. Gap pattern ID gp0 is configured for PCell FR1-FR1 Inter frequency handover in the test case.

The supported test configurations are given in table A.7.3.1.8.1-1. The test scenario comprises four NR cells, source PCell(Cell 1) and source PSCell(Cell 2), target PCell(Cell 3), target PSCell(Cell 4).

Cell 1 and Cell 3 are on radio channel 1 in FR1.Cell 2 and Cell 4 are on radio channel 2 in FR2. Test parameters are given in tables A.7.3.1.8.1-2, A.7.3.1.8.1-3, A.7.3.1.8.1-4 and A.7.3.1.8.1-5 below. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of T1, the UE shall be connected to Cell 1 on radio channel 1 and Cell 2 on radio channel 2. UE is not aware of Cell 3 and Cell 4. Starting T2, cell 3 and Cell 4 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.7.3.1.8.1-1: Supported test configurations for HO with PSCell from NR-DC to NR-DC

Table A.7.3.1.8.1-2: General test parameters for PCell FR1-FR1 Inter frequency handover

Table A.7.3.1.8.1-3: Cell specific test parameters for PCell FR1-FR1 Inter frequency handover

Table A.7.3.1.8.1-4: General test parameters Intra-frequency FR2-FR2 PSCell change

Table A.7.3.1.8.1-5: Cell specific test parameters for Intra-frequency FR2-FR2 PSCell change

## A.7.3.1.8.2Test Requirements

The UE shall start to transmit the PRACH to target PSCell (Cell 4) less than 83 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

## A.7.3.1.9Intra-frequency handover from FR2-2 to FR2-2; unknown target cell

## A.7.3.1.9.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-2-NR FR2-2 intra frequency handover requirements specified in clause 6.1.1.4.

## A.7.3.1.9.2Test Parameters

Supported test configurations are shown in table A.7.3.1.9.2-1. Both handover delay and interruption length are tested by using the parameters in table A.7.3.1.9.2-2 and A.7.3.1.9.2-3.

The test scenario comprises of carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Starting T2, cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.7.3.1.9.2-1: Intra-frequency handover from FR2-2 to FR2-2 test configurations

Table A.7.3.1.9.2-2: General test parameters Intra-frequency handover from FR2-2 to FR2-2

Table A.7.3.1.9.2-3: Cell specific test parameters for NR FR2-2-FR2-2 Intra frequency handover test case

## A.7.3.1.9.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 772 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 762 ms in the test. Tinterrupt is defined in clause 6.1.1.4.2.

This gives a total of 772 ms.

## A.7.3.1.10Inter-frequency handover from FR2-2 to FR2-2; unknown target cell

## A.7.3.1.10.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-2-NR FR2-2 Inter frequency handover requirements specified in clause 6.1.1.4.

## A.7.3.1.10.2Test Parameters

Supported test configurations are shown in table A.7.3.1.10.2-1. Both handover delay and interruption length are tested by using the parameters in table A.7.3.1.10.2-2 and A.7.3.1.10.2-3.

The test scenario comprises of carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Starting T2, cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.7.3.1.10.2-1: Inter-frequency handover from FR2-2 to FR2-2 test configurations

Table A.7.3.1.10.2-2: General test parameters Inter-frequency handover from FR2-2 to FR2-2

Table A.7.3.1.10.2-3: Cell specific test parameters for NR FR2-2-FR2-2 Inter frequency handover test case

## A.7.3.1.10.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 772 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 762 ms in the test. Tinterrupt is defined in clause 6.1.1.4.2.

This gives a total of 772 ms.

## A.7.3.1.11Inter-frequency handover from FR1 to FR2-2; unknown target cell

## A.7.3.1.11.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR2-2 Inter frequency handover requirements specified in clause 6.1.1.4.

## A.7.3.1.11.2Test Parameters

Supported test configurations are shown in table A.7.3.1.11.2-1 and A.7.3.1.11.2-1A, and the configuration for NR Cell 1 and NR Cell 2 are chosen independently. Both handover delay and interruption length are tested by using the parameters in table A.7.3.1.11.2-2 and A.7.3.1.11.2-3.

The test scenario comprises of carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Starting T2, cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.7.3.1.11.2-1: Inter-frequency handover from FR1 to FR2-2 test configurations for Cell 1

Table A.7.3.1.11.2-1A: Inter-frequency handover from FR1 to FR2-2 test configurations for Cell 2

Table A.7.3.1.11.2-2: General test parameters Inter-frequency handover from FR1 to FR2-2

Table A.7.3.1.11.2-3: Cell specific test parameters for NR FR1-FR2-2 Inter frequency handover test case

## A.7.3.1.11.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 772 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 762 ms in the test. Tinterrupt is defined in clause 6.1.1.4.2.

This gives a total of 772 ms.

## A.7.3.1.12Intra-frequency handover from FR2 to FR2; known target cell configured with NCD-SSB

## A.7.3.1.12.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 intra-frequency handover requirements specified in clause 6.1.1.4, when the target cell is configured with NCD-SSB.

## A.7.3.1.12.2Test Parameters

Supported test configurations are shown in table A.7.3.1.12.2-1. Both handover delay and interruption length are tested by using the parameters in table A.7.3.1.12.2-2 and A.7.3.1.12.2-3.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

Before the test starts,

-UE is connected to Cell 1 with active DL BWP and active UL BWP;

-UE is configured with nonCellDefiningSSB-r17 under BWP-DownlinkDedicated, and NCD-SSB serves as the reference SSB for the serving cell, and is contained in the active DL BWP.

During T2, Cell 2 is switched ON, and transmits two SSBs, i.e. CD-SSB at SSB frequency 1 and NCD-SSB at SSB frequency 2. Before the test, UE is configured to measure SSB frequency 2. The test equipment shall send an RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3.

The start of T3 is defined as the end of the last TTI containing the RRC message implying handover. The handover command indicates the UE to handover to Cell 2 with firstActiveDownlinkBWP-Id configured to BWP-1. The UE then performs handover from Cell 1’s active DL-BWP associated with the NCD-SSB of Cell 1 to Cell 2’s BWP-1 which is associated with NCD-SSB of Cell 2.

Table A.7.3.1.12.2-1: Intra-frequency handover from FR2 to FR2 test configurations

Table A.7.3.1.12.2-2: General test parameters Intra-frequency handover from FR2 to FR2

Table A.7.3.1.12.2-3: Cell specific test parameters for NR FR2-FR2 Intra frequency handover test case

## A.7.3.1.12.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 92 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 82 ms in the test. Tinterrupt is defined in clause 6.1.1.4.2.

This gives a total of 92 ms.

## A.7.3.1.13Inter-frequency handover from FR2 to FR2; known target cell configured with NCD-SSB

## A.7.3.1.13.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 inter-frequency handover requirements specified in clause 6.1.1.4, when the target cell is configured with NCD-SSB.

## A.7.3.1.13.2Test Parameters

Supported test configurations are shown in table A.7.3.1.13.2-1. Both handover delay and interruption length are tested by using the parameters in table A.7.3.1.13.2-2 and A.7.3.1.13.2-3.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of cell 2.

Before the test starts,

-UE is connected to Cell 1 with active DL BWP and active UL BWP;

-UE is not configured with nonCellDefiningSSB-r17 under BWP-DownlinkDedicated, and CD-SSB serves as the reference SSB for the serving cell, and is contained in the active DL BWP.

During T2, Cell 2 is switched ON, and transmits two SSBs, i.e. CD-SSB at SSB frequency 1 and NCD-SSB at SSB frequency 2. Before the test, UE is configured to measure SSB frequency 1. The test equipment shall send an RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3.

The start of T3 is defined as the end of the last TTI containing the RRC message implying handover. The handover command indicates the UE to handover to Cell 2 with firstActiveDownlinkBWP-Id configured to BWP-1. The UE then performs handover from Cell 1’s active DL-BWP associated with the CD-SSB of Cell 1 to Cell 2’s BWP-1 which is associated with NCD-SSB of Cell 2.

Table A.7.3.1.13.2-1: Inter-frequency handover from FR2 to FR2 test configurations

Table A.7.3.1.13.2-2: General test parameters Inter-frequency handover from FR2 to FR2

Table A.7.3.1.13.2-3: Cell specific test parameters for NR FR2-FR2 Inter frequency handover test case

## A.7.3.1.13.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 132 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 122 ms in the test. Tinterrupt is defined in clause 6.1.1.4.2.

This gives a total of 132 ms.

## A.7.3.1.14Handover with PSCell from FR1-FR2 NR-DC to FR1-FR1 NR-DC with target PSCell in FR1

## A.7.3.1.14.1Test Purpose and Environment

The purpose of this test is to verify the PSCell change delay requirements in HO with PSCell in parellal processing from FR1-FR2 NR-DC to FR1-FR1 NR-DC defined in clauses 6.1.5.4.2. The requirements are applicable to NR FR1-FR2 inter-frequency PCell handover and NR FR1-FR1 inter-frequency PSCell change. Gap pattern ID gp0 is configured for PCell FR1-FR1 Inter frequency handover in the test case.

The supported test configurations are given in table A.7.3.1.14.1-1. The test scenario comprises four NR cells, source PCell (Cell 1) and source PSCell (Cell 2), target PCell (Cell 3), target PSCell (Cell 4).

Cell 1, Cell 3 and Cell 4 are on radio channel 1 in FR1.Cell 2 are on radio channel 2 in FR2. Test parameters are given in tables A.7.3.1.14.1-2, A.7.3.1.14.1-3, A.7.3.14.1-4 and A.7.3.1.14.1-5 below. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of T1, the UE shall be connected to Cell 1 on radio channel 1 and Cell 2 on radio channel 2. UE is not aware of Cell 3 and Cell 4. Starting T2, cell 3 and Cell 4 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.7.3.1.14.1-1: Supported test configurations for HO with PSCell from FR1-FR2 NR-DC to FR1-FR1 NR-DC

Table A.7.3.1.14.1-2: General test parameters for PCell FR1-FR1 Inter frequency handover

Table A.7.3.1.14.1-3: Cell specific test parameters for PCell FR1-FR1 Inter frequency handover

Table A.7.3.1.14.1-4: General test parameters FR2-FR1 PSCell change

Table A.7.3.1.14.1-5: Cell specific test parameters for FR2-FR1 PSCell change

## A.7.3.1.14.2Test Requirements

The UE shall start to transmit the PRACH to Cell 3 less than 77 ms from the beginning of time period T2.

The UE shall transmit the PRACH preamble to Cell 4 less than 107 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

The rate of correct PSCell addition observed during repeated tests shall be at least 90 %.

NOTE:The handover requirements for handover with PSCell is defined in clause 6.1.5.4 in [15] as:

DHOwithPSCel_PSCell = TRRC_delay + Tsearch + TIU + Tprocessing+ T∆ + Tmargin

Where:

TRRC_delay = 20 ms for ‘RRC connection reconfiguration (NR SCG establishment/ /modification/release)’.

Tsearch = 0 ms for known cell.

TIU = 15 ms in the test configuration.

Tprocessing = 20 ms.

T∆ = 20 ms.

Tmargin = 2 ms.

This gives a total of 77 ms for handover delay.

NOTE:The PSCell change delay for handover with PSCell for NR-DC is defined in clause 6.1.5.4.2 in [15] as:

DHOwithPSCel_PSCell = TRRC_delay + Tprocessing + Tsearch + T∆ + TPSCell_ DU + TPCell_DU + 2 ms

Where:

TRRC_delay = 20 ms for ‘RRC connection reconfiguration (NR SCG establishment/ /modification/release)’.

Tprocessing = 45 ms for source Cell and target Cell are in the different FR.

Tsearch = 0 ms for known cell.

T∆ = 20 ms for fine time tracking and acquiring full timing information of the target cell.

TPSCell_ DU = 20 ms.

TPCell_ DU = 0 ms,.

This gives a total of 107 ms for handover delay.

## A.7.3.1.15HO with PSCell from FR1-FR1 NR-DC to FR1-FR2 NR-DC

## A.7.3.1.15.1Test Purpose and Environment

The purpose of this test is to verify the Handover with PSCell change delay requirements from FR1-FR1 NR-DC to FR1-FR2 NR-DC defined in clauses 6.1.5.4.2. The requirements are applicable to NR FR1-FR1 intra-frequency PCell handover and NR FR1-FR2 inter-frequency PSCell change. Gap pattern ID gp0 is configured for PCell FR1-FR1 Inter frequency handover in the test case.

The supported test configurations are given in table A.7.3.1.15.1-1. The test scenario comprises four NR cells, source PCell(Cell 1) and source PSCell(Cell 2), target PCell(Cell 3), target PSCell(Cell 4).

Cell 1 and Cell 3 are on radio channel 1 in FR1.Cell 2 is on radio channel 2 in FR1. Cell 4 is on radio channel 3 in FR2. Test parameters are given in tables A.7.3.1.15.1-2, A.7.3.1.15.1-3, A.7.3.1.15.1-4, A.7.3.1.15.1-5 and A.7.3.1.15.1-6 below. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of T1, the UE shall be connected to Cell 1 on radio channel 1 and Cell 2 on radio channel 2. UE is not aware of Cell 3 and Cell 4. Starting T2, cell 3 and Cell 4 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The SMTC of Cell 4 is provided in targetcellSMTC-SCG-r16 but not configured in reconfigurationWithSync.

Table A.7.3.1.15.1-1: Supported test configurations for HO with PSCell from NR-DC to NR-DC

Table A.7.3.1.15.1-2: General test parameters for PCell FR1-FR1 Inter frequency handover

Table A.7.3.1.15.1-3: Cell specific test parameters for PCell FR1-FR1 Inter frequency handover

Table A.7.3.1.15.1-4: General test parameters Inter-frequency FR1-FR2 PSCell change

Table A.7.3.1.15.1-5: Cell specific test parameters for Inter-frequency FR1-FR2 PSCell change (Cell 2)

Table A.7.3.1.15.1-6: Cell specific test parameters for Inter-frequency FR1-FR2 PSCell change (Cell 4)

## A.7.3.1.15.2Test Requirements

The UE shall start to transmit the PRACH to target PSCell (Cell 4) less than 636 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover with PSCell delay can be expressed as: DHOwithPSCell_PSCell = TRRC_delay + Tprocessing + Tsearch_HO + Tsearch_PSCell + T∆ + TPSCell_ DU + 2 ms, where:

RRC procedure delay = 16 ms and is specified in clause 12 in TS 38.331 [2].

Tprocessing is as defined as 50 ms in the test.

Tsearch_HO is as defined as 60 ms in the test.

Tsearch_PSCell is as defined as 480 ms in the test.

T∆ is defined as 20 ms in the test.

TPSCell_ DU is defined as 10 ms in the test.

This gives a total of 636 ms.

## A.7.3.1.16Intra-frequency handover from FR2 to FR2; unknown target cell; for UE supporting fast beam sweeping

## A.7.3.1.16.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 intra frequency handover for the UE supporting fastRx-BSF-MeasDelayReduction-r19 specified in clause 6.1.1.4.

## A.7.3.1.16.2Test Parameters

Supported test configurations are shown in table A.7.3.1.16.2-1. Both handover delay and interruption length are tested by using the parameters in table A.7.3.1.16.2-2, and A.7.3.1.16.2-3.

The test scenario comprises of two cells on same carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Starting from T2, cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.7.3.1.16.2-1: Intra-frequency handover from NR FR2 to FR2 test configurations

Table A.7.3.1.16.2-2: General test parameters Intra-frequency handover from NR FR2 to FR2

Table A.7.3.1.16.2-3: Cell specific test parameters for NR FR2-FR2 Intra frequency handover test case

## A.7.3.1.16.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than (N*20+72) ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = (N*20+62) ms in the test where N is the UE reported value via capability fastRx-BSF-MeasDelayReduction-r19. Tinterrupt is defined in clause 6.1.1.4.2.

This gives a total of (N*20+72) ms.

## A.7.3.1.17Inter-frequency handover from FR2 to FR2; unknown target cell; for UE supporting fast beam sweeping

## A.7.3.1.17.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 inter frequency handover for the UE supporting fastRx-BSF-MeasDelayReduction-r19 specified in clause 6.1.1.4.

## A.7.3.1.17.2Test Parameters

Supported test configurations are shown in table A.7.3.1.17.2-1. Both handover delay and interruption length are tested by using the parameters in table A.7.3.1.17.2-2, and A.7.3.1.17.2-3.

The test scenario comprises of carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. Starting T2, cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.7.3.1.17.2-1: Inter-frequency handover from FR2 to FR2 test configurations

Table A.7.3.1.17.2-2: General test parameters Inter-frequency handover from FR2 to FR2

Table A.7.3.1.17.2-3: Cell specific test parameters for NR FR2-FR2 Inter frequency handover test case

## A.7.3.1.17.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than (60*N+72) ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = (60*N+62) ms in the test where N is the UE reported value via capability fastRx-BSF-MeasDelayReduction-r19. Tinterrupt is defined in clause 6.1.1.4.2.

This gives a total of (60*N+72) ms.

## A.7.3.2RRC Connection Mobility Control

## A.7.3.2.1SA: RRC Re-establishment

## A.7.3.2.1.1Intra-frequency RRC Re-establishment in FR2

A.7.3.2.1.1.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR2 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1.

The test parameters are given in table A.7.3.2.1.1.1-1, table A.7.3.2.1.1.1-2 and table A.7.3.2.1.1.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure.

Table A.7.3.2.1.1.1-1: Supported test configurations

Table A.7.3.2.1.1.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR2

Table A.7.3.2.1.1.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR2

A.7.3.2.1.1.2Test Requirements

The RRC re-establishment delay is defined as the time from the moment UE declares RLF, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCReestablishmentRequest message to cell 2.

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

This gives a total of 4865 ms for RRC re-establishment delay, allow 9.84 s (4.84 s + 5 s) from the beginning of T2 in the test case.

## A.7.3.2.1.2Inter-frequency RRC Re-establishment in FR2

A.7.3.2.1.2.1Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR2 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1.

The test parameters are given in table A.7.3.2.1.2.1-1, table A.7.3.2.1.2.1-2 and table A.7.3.2.1.2.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of cell 2 by the end of T1.

Table A.7.3.2.1.2.1-1: Supported test configurations

Table A.7.3.2.1.2.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR2

Table A.7.3.2.1.2.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR2

A.7.3.2.1.2.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCReestablishmentRequest message to cell 2.

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

## A.7.3.2.1.3Intra-frequency RRC Re-establishment in FR2 without serving cell timing

## A.7.3.2.1.3.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR2 without serving cell timing is within the specified limits. These tests will verify the requirements in clause 6.2.1.

The test parameters are given in table A.7.3.2.1.3.1-1, table A.7.3.2.1.3.1-2 and table A.7.3.2.1.3.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.7.3.2.1.3.1-1: Supported test configurations

Table A.7.3.2.1.3.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR2

Table A.7.3.2.1.3.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR2

## A.7.3.2.1.3.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCReestablishmentRequest message to cell 2.

The RRC re-establishment delay to an unknown NR intra frequency cell without serving cell timing shall be less than 5 s.

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

## A.7.3.2.1.4Intra-frequency RRC Re-establishment in FR2-2

## A.7.3.2.1.4.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR2-2 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1.

The test parameters are given in table A.7.3.2.1.4.1-1, table A.7.3.2.1.4.1-2 and table A.7.3.2.1.4.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure.

Table A.7.3.2.1.4.1-1: Supported test configurations

Table A.7.3.2.1.4.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR2-2

Table A.7.3.2.1.4.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR2-2

## A.7.3.2.1.4.2Test Requirements

he RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCReestablishmentRequest message to cell 2.

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

## A.7.3.2.1.5Inter-frequency RRC Re-establishment in FR2-2

## A.7.3.2.1.5.1Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR2-2 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1.

The test parameters are given in table A.7.3.2.1.5.1-1, table A.7.3.2.1.5.1-2 and table A.7.3.2.1.5.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of cell 2 by the end of T1.

Table A.7.3.2.1.5.1-1: Supported test configurations

Table A.7.3.2.1.5.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR2-2

Table A.7.3.2.1.5.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR2-2

## A.7.3.2.1.5.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCReestablishmentRequest message to cell 2.

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

## A.7.3.2.1.6Intra-frequency RRC Re-establishment in FR2-2 without serving cell timing

## A.7.3.2.1.6.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR2-2 without serving cell timing is within the specified limits. These tests will verify the requirements in clause 6.2.1.

The test parameters are given in table A.7.3.2.1.6.1-1, table A.7.3.2.1.6.1-2 and table A.7.3.2.1.6.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.7.3.2.1.6.1-1: Supported test configurations

Table A.7.3.2.1.6.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR2-2

Table A.7.3.2.1.6.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR2-2

## A.7.3.2.1.6.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCReestablishmentRequest message to cell 2.

The RRC re-establishment delay to an unknown NR intra frequency cell without serving cell timing shall be less than 5 s.

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

## A.7.3.2.1.7Intra-frequency RRC Re-establishment in FR2 with UE capable of reduced beam sweeping factor

## A.7.3.2.1.7.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR2 without known target cell is within the specified limits, where the UE is capable of reduced beam sweeping factor. These tests will verify the requirements in clause 6.2.1. While inter-frequency RRC re-establishment delay for UE capable of reduced beam sweeping factor is tested under the condition that the serving cell timing is not available to the UE in clause A.7.3.2.1.8, intra-frequency RRC re-establishment delay test case for UE capable of reduced beam sweeping factor is tested under the condition that the serving cell timing is still available to UE in this clause.

The test parameters are given in table A.7.3.2.1.7.1-1, table A.7.3.2.1.7.1-2 and table A.7.3.2.1.7.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure.

Table A.7.3.2.1.7.1-1: Supported test configurations

Table A.7.3.2.1.7.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR2

Table A.7.3.2.1.7.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR2

## A.7.3.2.1.7.2Test Requirements

The RRC re-establishment delay is defined as the time from the moment UE declares RLF, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCReestablishmentRequest message to cell 2.

The RRC re-establishment delay to an unknown NR intra frequency cell shall be less than 3 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 1.

Tidentify_intra_NR = N1*440 + Tproc ms, where N1 = reduced N and Tproc = 2 ms.

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of:

-1747 ms for N1=2, which allows 7.84 s (4.84 s + 3 s) from the beginning of T2 in the test case, or

-2147 ms for N1=4, which allows 7.84 s (4.84 s + 3 s) from the beginning of T2 in the test case, or

-2547 ms for N1=6, which allows 7.84 s (4.84 s + 3 s) from the beginning of T2 in the test case.

## A.7.3.2.1.8Inter-frequency RRC Re-establishment in FR2 without serving cell timing with UE capable of reduced beam sweeping factor

## A.7.3.2.1.8.1Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR2 without serving cell timing is within the specified limits, when the UE is capable of reduced beam sweeping factor. These tests will verify the requirements in clause 6.2.1. While intra-frequency RRC re-establishment delay for UE capable of reduced beam sweeping factor is tested under the condition that the serving cell timing is still available to the UE in clause A.7.3.2.1.7, inter-frequency RRC re-establishment delay test case for UE capable of reduced beam sweeping factor is tested under the condition that the serving cell timing is not available to UE in this clause.

The test parameters are given in table A.7.3.2.1.8.1-1, table A.7.3.2.1.8.1-2 and table A.7.3.2.1.8.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of cell 2 by the end of T1. During T1 and T2, cell 2 is not detectable to the UE.

Table A.7.3.2.1.8.1-1: Supported test configurations

Table A.7.3.2.1.8.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR2

Table A.7.3.2.1.8.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR2

## A.7.3.2.1.8.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to cell 2 for sending the RRCReestablishmentRequest message to cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell shall be less than the delay specified below for Tre-establish_delay.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 2.

Tidentify_intra_NR = MAX (1000, (N1 x 10 x TSMTC + Tproc)) ms, where N1 = reduced N and Tproc = 2 ms.

Tidentify_inter_NR = MAX (1000, (N1 x 13 x TSMTC, i + Tproc)) ms, where N1 = reduced N and Tproc = 2 ms.

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of:

-3345 ms for N1=2, which allows 5 s in the test case, or

-3385 ms for N1=4, which allows 5 s in the test case, or

-4107 ms for N1=6, which allows 5 s in the test case.

## A.7.3.2.2Random Access

## A.7.3.2.2.14-step RA type c ontention based random access test in FR2 for NR Standalone

A.7.3.2.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in Clause 6.2.2.2 and Clause 7.1.2 in an AWGN model.

For this test one cell is used, with the configuration of Cell 1 configured as PCell or SCell in FR2. Supported test parameters are shown in table A.7.3.2.2.1.1-1. UE capable of SA with PCell or SCell in FR2 needs to be tested by using the parameters in table A.7.3.2.2.1.1-2 and table A.7.3.2.2.1.1-3.

Table A.7.3.2.2.1.1-1: Supported test configurations for contention based random access test in FR2 for NR Standalone

Table A.7.3.2.2.1.1-2: General test parameters for contention based random access test in FR2 for NR Standalone

Table A.7.3.2.2.1.1-3: OTA-related test parameters for contention based random access test in FR2 for NR Standalone

A.7.3.2.2.1.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.7.3.2.2.1.2.1Random Access Preamble Transmission

To test the UE behavior specified in Clause 6.2.2.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB.

In addition, the power applied to all preambles shall be in accordance with what is specified in Clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Clause 7.1.2.

A.7.3.2.2.1.2.2Random Access Response Reception

To test the UE behavior specified in Clause 6.2.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Clause 7.1.2.

A.7.3.2.2.1.2.3No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 2 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in Clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Clause 7.1.2.

A.7.3.2.2.1.2.4Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2.2.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

A.7.3.2.2.1.2.5Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in Clause 6.2.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.7.3.2.2.1.2.6Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in Clause 6.2.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.7.3.2.2.1.2.7Contention Resolution Timer expiry

To test the UE behavior specified in Clause 6.2.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.7.3.2.2.24-step RA type n on-contention based random access test in FR2 for NR Standalone

A.7.3.2.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in Clause 6.2.2.2 and Clause 7.1.2 in an AWGN model.

For this test one cell is used, with the configuration of Cell 1 configured as PCell or SCell in FR2. Supported test parameters are shown in table A.7.3.2.2.2.1-1. UE capable of SA with PCell or SCell in FR2 needs to be tested by using the parameters in table A.7.3.2.2.2.1-2 and table A.7.3.2.2.2.1-3 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2). Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

Table A.7.3.2.2.2.1-1: Supported test configurations for non-contention based random access test in FR2 for NR Standalone

Table A.7.3.2.2.2.1-2: General test parameters for non-contention based random access test in FR2 for NR Standalone

Table A.7.3.2.2.2.1-3: OTA-related test parameters for non-contention based random access test in FR2 for NR Standalone

A.7.3.2.2.2.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.7.3.2.2.2.2.1SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in Clause 6.2.2.2.2.1 for SSB-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in Clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Clause 7.1.2.

A.7.3.2.2.2.2.2CSI-RS-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in Clause 6.2.2.2.2.1 for CSI-RS-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with CSI-RSs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the CSI-RS configured.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the CSI-RS configured, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-OccasionList.

In addition, the power applied to all preambles shall be in accordance with what is specified in Clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Clause 7.1.2.

A.7.3.2.2.2.2.3Random Access Response Reception

To test the UE behavior specified in Clause 6.2.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in Clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Clause 7.1.2.

A.7.3.2.2.2.2.4No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 2 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in Clause 6.2.2.2. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in Clause 7.1.2.

## A.7.3.2.2.32-step RA type contention based random access test in FR2 for NR Standalone

A.7.3.2.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the 2-step RA type random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits. This test will verify the requirements in Clause 6.2.2.3 and Clause 7.1.2 in an AWGN model.

For this test one cell is used, with the configuration of Cell 1 configured as PCell or SCell in FR2. Supported test parameters are shown in table A.7.3.2.2.3.1-1. UE capable of SA with PCell or SCell in FR2 needs to be tested by using the parameters in table A.7.3.2.2.3.1-2 and table A.7.3.2.2.3.1-3.

Table A.7.3.2.2.3.1-1: Supported test configurations for 2-step RA type contention based random access test in FR2 for NR Standalone

Table A.7.3.2.2.3.1-2: General test parameters for 2-step RA type contention based random access test in FR2 for NR Standalone

Table A.7.3.2.2.3.1-3: OTA-related test parameters for 2-step RA type contention based random access test in FR2 for NR Standalone

A.7.3.2.2.3.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.7.3.2.2.3.2.1MsgA Transmission

To test the UE behavior specified in Clause 6.2.2.3.1.1 the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured msgA-RSRP-ThresholdSSB.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first MsgA preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].The transmit timing of all MsgA transmissions shall be within the accuracy specified in Clause 7.1.2.

A.7.3.2.2.3.2.2MsgB Reception

To test the UE behavior specified in Clause 6.2.2.3.1.2 the System Simulator shall transmit a MsgB containing a fallbackRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit MsgA with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB’s contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first MsgA PRACH shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in Clause 7.1.2.

A.7.3.2.2.3.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.1.3 the System Simulator shall transmit a MsgB containing a fallbackRAR message and Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 2 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if no MsgB is received within the MsgB Response window.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first MsgA PRACH shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in Clause 7.1.2.

## A.7.3.2.2.42-step RA type n on-contention based random access test in FR2 for NR Standalone

A.7.3.2.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits. This test will verify the requirements in Clause 6.2.2.3 and Clause 7.1.2 in an AWGN model.

For this test one cell is used, with the configuration of Cell 1 configured as PCell or SCell in FR2. Supported test parameters are shown in table A.7.3.2.2.4.1-1. UE capable of SA with PCell or SCell in FR2 needs to be tested by using the parameters in table A.7.3.2.2.4.1-2 and table A.7.3.2.2.4.1-3.

Table A.7.3.2.2.4.1-1: Supported test configurations for non-contention based random access test for 2-step RA type in FR2 for NR Standalone

Table A.7.3.2.2.4.1-2: General test parameters for non-contention based random access test for 2-step RA type in FR2 for NR Standalone

Table A.7.3.2.2.4.1-3: OTA-related test parameters for non-contention based random access test for 2-step RA type in FR2 for NR Standalone

A.7.3.2.2.4.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.7.3.2.2.4.2.1MsgA Transmission

In Test-1, to test the UE behavior specified in Clause 6.2.2.3.2.1 for MsgA transmission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the MsgA which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the MsgA on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given first by the msgA-SSB-SharedRO-MaskIndex if configured, or next by the ra-ssb-OccasionMaskIndex if configured.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in Clause 7.1.2.

A.7.3.2.2.4.2.2MsgB Reception

To test the UE behavior specified in Clause 6.2.2.3.2.2 the System Simulator shall transmit a MsgB containing a successRAR MAC subPDU corresponding to the transmitted Random Access Preamble after 3 MsgA transmissions have been received by the System Simulator. In response to the first 2 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB if the MsgB contains a successRAR MAC subPDU corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA transmission power if all received Random Access Response Reception has not been considered as successful.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in Clause 7.1.2.

A.7.3.2.2.4.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.3 the System Simulator shall transmit a MsgB corresponding to the transmitted Random Access Preamble after 3 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 2 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA transmission power when the backoff time expires if no MsgB is received within the MsgB Response window configured in RACH-ConfigGenericTwoStepRA.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be 0.6 dBm to be received at TE with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-2 [19]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-2 [19].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in Clause 7.1.2.

## A.7.3.2.3SA: RRC Connection Release with Redirection

## A.7.3.2.3.1Redirection from NR in FR2 to NR in FR2

A.7.3.2.3.1.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements specified in clause 6.2.3.2.1.

A.7.3.2.3.1.2Test Parameters

Supported test configurations are shown in table A.7.3.2.3.1.2-1. The time delay is tested by using the parameters in table A.7.3.2.3.1.2-2, and A.7.3.2.3.1.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.7.3.2.3.1.2-1: Redirection from NR to NR test configurations

Table A.7.3.2.3.1.2-2: General test parameters for Redirection from NR to NR test case

Table A.7.3.2.3.1.2-3: Cell specific test parameters for Redirection from NR to NR test case

A.7.3.2.3.1.3Test Requirements

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

## A.7.3.2.3.2Redirection from NR in FR2 to NR in FR2 with UE capable of reduced beam sweeping factor

A.7.3.2.3.2.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements when the UE is capable of reduced beam sweeping factor, which are specified in clause 6.2.3.2.1.

A.7.3.2.3.2.2Test Parameters

Supported test configurations are shown in table A.7.3.2.3.2.2-1. The time delay is tested by using the parameters in table A.7.3.2.3.2.2-2, and A.7.3.2.3.2.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.7.3.2.3.2.2-1: Redirection from NR to NR test configurations

Table A.7.3.2.3.2.2-2: General test parameters for Redirection from NR to NR test case

Table A.7.3.2.3.2.2-3: Cell specific test parameters for Redirection from NR to NR test case

A.7.3.2.3.2.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than the below specified delay Tconnection_release_redirect_NR from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_NR = TRRC_procedure_delay + Tidentify-NR + TSI-NR + TRACH,

where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR = MAX (880, N x 11 x Trs + Tproc) ms, where N = reduced beam sweeping factor, Trs = 20 ms, Tproc = 2 ms.

TSI-NR = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH = 10 ms in the test.

This gives a total of:

-2280 ms for N=2, allow 3 s in the test case for T2, or

-2282 ms for N=4, allow 3 s in the test case for T2, or

-2722 ms for N=6, allow 3 s in the test case for T2.

## A.7.3.2.4LTM PDCCH-order Random Access

## A.7.3.2.4.1PDCCH-order RACH on neighbor cell in FR2 when RACH BW is within active BWP

A.7.3.2.4.1.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 PDCCH-ordered RACH to an intra-frequency candidate cell in FR2 for LTM. The interruption requirements specified in clause 8.2.2.2.20. This test is for UE supporting PDCCH-ordered RACH to an intra-frequency candidate cell, whose SSB is within active BWPs of the UE.

A.7.3.2.4.1.2Test Parameters

Two cells are deployed in the test, which are FR2 PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. Test configurations are given in table A.7.3.2.4.1.2-1. Both PDCCH order RACH delay and transmit timing requirement are tested by using the parameters in table A.7.3.2.4.1.2-2, and A.7.3.2.4.1.2-3.

There are two tests in the test case, test 1 and test 2:

-In test 1, joint TCI state configuration as defined in table A.7.3.2.4.1.2-2 is provided for UE that supports ltm-BeamIndicationJointTCI-r18.

-In test 2, separate TCI state configuration as defined in table A.7.3.2.4.1.2-2 for test 2 is provided for UE that supports ltm-BeamIndicationSeparateTCI-r18 and does not support ltm-BeamIndicationJointTCI-r18.

If a UE supports ltm-BeamIndicationSeparateTCI-r18 and does not support ltm-BeamIndicationJointTCI-r18, it is only required to pass test 2. Otherwise, it is only required to pass test 1.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. No gap patterns are configured in the test case.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is provided with LTM-Candidate-r18 for Cell 2.

-A measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

-The UE has performed L3 measurement and SSB based L1-RSRP measurement on Cell 2.

T1 starts from UE transmitting a valid L1 report on Cell 2. After receiving the first L1 report on Cell 2 during T1, the network sends TCI state activation MAC CE to active TCI state of Cell 2 in no later than 100 ms.

-In test 1, CandidateTCI-State#1 is activated.

-In test 2, CandidateTCI-State#1 and CandidateTCI-UL-State#1 are activated.

-For UE incapable of early TCI state activation, network shall not send TCI state activation MAC CE to active TCI state of Cell 2.

The start of T2 is the instant when PDCCH order to trigger PRACH transmission on Cell 2 is sent to the UE.

Table A.7.3.2.4.1.2-1: PDCCH order RACH on Neighbor cell in FR1 test configurations

Table A.7.3.2.4..2.2-2: General test parameters for PDCCH order RACH in FR2

Table A.7.3.2.4..2.2-3: Cell specific test parameters for PDCCH order RACH test case in FR2

A.7.3.2.4.1.3Test Requirements

The UE shall transmit the PRACH to Cell 2 in the first available PRACH occasion after  + 0.25 ms +  from the beginning of time period T2. After transmitting PRACH on Cell 2, UE shall be back to Cell 1.NT,2 TSSB

NOTE:The PDCCH order RACH delay can be expressed as: , where:NT,2+TBWPswitchDelay+∆Delay+Tswitch+TSSB+∆RF/BB preparation

- is a time duration of  symbols corresponding to a PUSCH preparation time for UE processing capability 1 assuming  corresponds to the smallest SCS configuration between the SCS configuration of the PDCCH order and the SCS configuration of the corresponding PRACH transmission and is specified in table 6.4-1 in 38.214 [26].NT,2N2μ

-= 0, = 0, = 0TBWPswitchDelayTswitch∆RF/BB preparation

-= 0.25 ms∆Delay

-, where  is first SSB occasion, after 1 slot from the end of the slot of the PDCCH, and  = 2 ms, which is the time for SSB processing.TSSB= Tfirst-SSB_RACH + TSSB-procTfirst-SSB_RACH TSSB-proc

During T2, interruption on Cell 1 UL shall not happen outside the overlapped slot to transmit PRACH and  symbols from the last or first symbol of PRACH occasion as defined in clause 8.1 in 38.213 [3], where N=4. During T2, interruption on Cell 1 DL shall not occur outside the overlapped slot to transmit PRACH.N

The test equipment will verify that the timing of PRACH transmission on Cell 2 is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB of Cell 2.

-The NTA_offset value (in Tc units) is 13792.

-The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.3.2.4.2PDCCH-order RACH on inter-frequency neighbor cell in FR2

A.7.3.2.4.2.1Test Purpose and Environment

This test is to verify the requirement for PDCCH-order RACH on neighbour cell in FR2 when RACH bandwidth is outside any configured UL BWP specified in clause 8.1 in 38.213 [3], UE transmit timing in clause 7.1 and interruption in clause 8.2.2.2.20 for UE supporting rach-EarlyTA-Measurement-r18, pdcch-RACH-PrepTime-TargetBandList-r18 and pdcch-RACH-Switching-TargetBandTimeList-r18.

A.7.3.2.4.2.2Test Parameters

In this test, there are two cells: NR Cell 1 as PCell in FR2 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR2 on NR RF channel 2. Test configurations are given in table A.7.3.2.4.2.2-1. Both PDCCH order RACH delay, transmit timing requirement and the interruption requirements are tested by using the parameters in table A.7.3.2.4.2.2-2, and A.7.3.2.4.2.2-3.

The test consists of two successive time periods, with time durations of T1 and T2 respectively.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is provided with LTM-Candidate-r18 for Cell 2.

-A measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A4 is used.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

-The UE has reported L3 measurement results and performed SSB based L1-RSRP measurement on Cell 2.

T1 starts from UE transmitting a valid L1 report on Cell 2. After T1, test equipment sends PDCCH order to trigger RACH transmission. The start of T2 is the instant when PDCCH order to trigger PRACH transmission on Cell 2 is received.

Table A.7.3.2.4.2.2-1: PDCCH order RACH on inter-frequency neighbor cell in FR2 test configurations

Table A.7.3.2.4.2.2-2: General test parameters for PDCCH order RACH in FR2

Table A.7.3.2.4.2.2-3: Cell specific test parameters for PDCCH order RACH test case

A.7.3.2.4.2.3Test Requirements

The UE shall transmit the PRACH to Cell 2 in the first available PRACH occasion after  + 0.25 ms +  +  from the beginning of time period T2. After transmitting PRACH on Cell 2, UE shall be back to Cell 1.NT,2 TSSB∆RF/BB preparation

NOTE:The PDCCH order RACH delay can be expressed as: , where:NT,2+TBWPswitchDelay+∆Delay+Tswitch+TSSB+∆RF/BB preparation

- is a time duration of  symbols corresponding to a PUSCH preparation time for UE processing capability 1 assuming  corresponds to the smallest SCS configuration between the SCS configuration of the PDCCH order and the SCS configuration of the corresponding PRACH transmission and is specified in table 6.4-1 in 38.214 [26].NT,2N2μ

-= 0, = 0TBWPswitchDelayTswitch

- is reported in pdcch-RACH-PrepTime-TargetBandList-r18∆RF/BB preparation

-= 0.25 ms∆Delay

-, where is the time to first SSB occasion overlapped with MGL after 2 ms and 1 slot from the end of the slot that UE receives PDCCH-order, and  = 2 ms, which is the time for SSB processing.TSSB= Tfirst-SSB_RACH + TSSB-procTfirst-SSB_RACHTSSB-proc

During T2, interruption on Cell 1 shall not happen outside ceil (Y/NR Slot length) +1 slots before and after PRACH transmission and the same slot of PRACH, where Y as reported in pdcch-RACH-Switching-TargetBandTimeList-r18,

The test equipment will verify that the timing of PRACH transmission on Cell 2 is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB of Cell 2.

-The NTA_offset value (in Tc units) is 13792.

-The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.3.3Conditional Handover

## A.7.3.3.1Intra-frequency conditional handover from FR2 to FR2

## A.7.3.3.1.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 intra frequency conditional handover requirements specified in clause 6.1.4.4.

## A.7.3.3.1.2Test Parameters

Supported test configurations are shown in table A.7.3.3.2.2-1. Both handover delay and interruption length are tested by using the parameters in table A.7.3.3.2.2-2, and A.7.3.3.2.2-3.

The test scenario comprises of two cells. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. NR shall configure a condition implying handover to cell 2 during T1, at a time earlier than TRRC before the beginning of T2. Starting T2, cell 2 becomes detectable.

Table A.7.3.3.1.2-1: Intra-frequency conditional handover from FR2 to FR2 test configurations

Table A.7.3.3.1.2-2: General test parameters for conditional Intra-frequency handover from FR2 to FR2

Table A.7.3.3.1.2-3: Cell specific test parameters for NR FR2-FR2 conditional Intra frequency handover test case

## A.7.3.3.1.2.3Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution =1600+62+10=1672 ms (power class 1) or 1080+62+10 =1152 ms (power classes 2,3 and 4) from the start of T2 and the interruption during T2 shall not exceeed Tinterrupt=Tprocessing + TIU + T∆ + Tmargin =40+20+2 = 62 ms excluding any transmissions which do not occur due to scheduling restrictions.

## A.7.3.3.2Inter-frequency conditional handover from FR2 to FR2; unknown target cell

## A.7.3.3.2.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 inter frequency conditional handover requirements specified in clause 6.1.4.4.

## A.7.3.3.2.2Test Parameters

Supported test configurations are shown in table A.7.3.3.3.2-1. Both conditional handover delay and interruption length are tested by using the parameters in tables A.7.3.3.3.2-2, and A.7.3.3.3.2-3.

The test scenario comprises of two carriers and one cell on each carrier. Gap pattern ID gp0 is configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. NR shall configure a condition implying handover to cell 2 during T1, at a time earlier than TRRC before the beginning of T2. At the start of T2, cell 2 becomes detectable and meets the handover condition.

Table A.7.3.3.2.2-1: Inter-frequency conditional handover from FR2 to FR2 test configurations

Table A.7.3.3.2.2-2: General test parameters Inter-frequency conditional handover from FR2 to FR2

Table A.7.3.3.2.2-3: Cell specific test parameters for NR FR2-FR2 Inter frequency conditional handover test case

## A.7.3.3.2.3Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution = 6720+62+10 ms=6792 ms (power class 1) or 4160+62+10 ms =4232 ms (power classes 2,3 and 4) from the start of T2 and the interruption during T2 shall not exceeed Tinterrupt=Tprocessing + TIU + T∆ + Tmargin =40+20+2 = 62 ms excluding any transmissions which do not occur due to scheduling restrictions.

## A.7.3.3.3NES triggering intra-frequency target CHO delay From FR2 to FR2

## A.7.3.3.3.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 intra frequency NES triggering conditional handover requirements specified in clause 6.1.4.4.

## A.7.3.3.3.2Test Parameters

Supported test configurations are shown in table A.7.3.3.3.2-1. Both handover delay and interruption length are tested by using the parameters in table A.7.3.3.3.2-2 and A.7.3.3.3.2-3.

The test scenario comprises of two cells. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. NR shall configure a condition implying NES triggering handover to cell 2 during T1, at a time earlier than TRRC before the beginning of T2.

Starting T2, cell 2 becomes detectable and DCI-2-9 command with including NES-mode indication as ‘1’ is sent at a time earlier than UE realizes the RSRP condition of CHO is met

Table A.7.3.3.3.2-1: Intra-frequency NES triggering conditional handover from FR2 to FR2 test configurations

Table A.7.3.3.3.2-2: General test parameters for NES triggering conditional Intra-frequency handover from FR2 to FR2

Table A.7.3.3.3.2-3: Cell specific test parameters for NR FR2-FR2 NES triggering conditional Intra frequency handover test case

## A.7.3.3.3.2.3Test Requirements

TRRC + TEvent_DU occurs during T1 as the NES triggering handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution =1600+62+10=1672 ms (power class 1) or 1080+62+10 =1152 ms (power classes 2,3 and 4) from the start of T2 and the interruption during T2 shall not exceeed Tinterrupt=Tprocessing + TIU + T∆ + Tmargin =40+20+2 = 62 ms excluding any transmissions which do not occur due to scheduling restrictions.

## A.7.3.3.4NES triggering inter-frequency conditional handover from FR2 to FR1

## A.7.3.3.4.1Test Purpose and Environment

This test is to verify the requirement for the NES triggering NR FR2-NR FR1 inter frequency conditional handover requirements specified in clause 6.1.4.3.

## A.7.3.3.4.2Test Parameters

Supported test configurations are shown in table A.7.3.3.4.2-1. Both conditional handover delay and interruption length are tested by using the parameters in tables A.7.3.3.4.2-2, A.7.3.3.4.2-3 and A.7.3.3.4.2-4.

The test scenario comprises of two carriers and one cell on each carrier. Measurement gap is configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. NR shall configure a NES based CHO condition implying handover to cell 2 during T1, at a time earlier than TRRC before the beginning of T2.  At the start of T2, cell 2 becomes detectable and meets the NES-based handover condition. In this test, UE is not indicated to report SSB based RRM measurement result with the associated SSB index for carrier of cell 2, and DCI 2-9 command of ‘1’ value for indicating NES-specific CHO execution condition is transmitted to UE at 950 ms from the start of T2, i.e. UE is expected to decode the DCI command 2-9 later than the time when the NES condition is considered met.

Table A.7.3.3.4.2-1: Inter-frequency conditional handover from FR2 to FR1 test configurations

Table A.7.3.3.4.2-2: General test parameters Inter-frequency conditional handover from FR2 to FR1

Table A.7.3.3.4.2-3: Cell specific test parameters for NR FR2-FR1 Inter frequency conditional handover test case

Table A.7.3.3.4.2-4: OTA related test parameters for NR FR2-FR1 Inter frequency conditional handover test case

## A.7.3.3.4.3Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution = 1022 ms from the start of T2 and the interruption during T2 shall not exceeed Tinterrupt=Tprocessing + TIU + T∆ + Tmargin = 62 ms excluding any transmissions which do not occur due to measurement gaps.

## A.7.3.3.5NR conditional handover including target MCG and target SCG from FR1-FR2 NR-DC to FR1-FR2 NR-DC

## A.7.3.3.5.1Test Purpose and Environment

This test is to verify the requirement for the requirements of CHO including target MCG and target SCG in NR-DC requirements specified in clause 6.1.6.2. inter-frequency conditional handover from NR FR1 to NR FR1 and intra-frequency PSCell change from NR-FR2 to NR FR2 are tested independently in the same test, with different end points.

The supported test configurations are given in table A.7.3.3.5.1-1. The test scenario comprises four NR cells, source PCell(Cell 1) and source PSCell(Cell 2), target PCell(Cell 3), target PSCell(Cell 4).

Cell 1 and Cell 3 are on radio channel 1 in FR1.Cell 2 and Cell 4 are on radio channel 2 in FR2. Test parameters are given in tables A.7.3.3.5.1-2, A.7.3.3.5.1-3, A.7.3.3.5.1-4 and A.7.3.3.5.1-5 below. Gap pattern ID gp0 is configured for PCell FR1-FR1 Inter frequency conditional handover in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of cell 2. NR shall configure a message implying conditional handover including target MCG in FR1 and target SCG in FR2 to Cell 3 during T1, at a time earlier than TRRC before the beginning of T2.  At the start of T2, cell 2 becomes detectable and meets the handover condition.

Table A.7.3.3.5.1-1: Supported test configurations for CHO with PSCell change from NR-DC to NR-DC

Table A.7.3.3.5.1-2: General test parameters for PCell FR1-FR1 Inter frequency conditional handover

Table A.7.3.3.5.1-3: Cell specific test parameters for PCell FR1-FR1 Inter frequency conditional handover

Table A.7.3.3.5.1-4: General test parameters Intra-frequency FR2-FR2 PSCell change (known cell)

Table A.7.3.3.5.1-5: Cell specific test parameters for Intra-frequency FR2-FR2 PSCell change (known cell)

## A.7.3.3.5.2Test Requirements

## A.7.3.3.5.2.1Test Requirements for NR conditional handover

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 3 less than Tmeasure + Tinterrupt + TCHO_execution = 1040+67+10 ms=1117 ms  from the start of T2 and the interruption during T2 shall not exceed Tinterrupt=Tprocessing + TIU + T∆ + Tmargin =25+20+20+2 = 67 ms excluding any transmissions which do not occur due to scheduling restrictions. excluding any transmissions which do not occur due to scheduling restrictions.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

## A.7.3.3.5.2.2Test Requirements for NR PSCell change

The UE shall start to transmit the PRACH to Cell 4 less than Tmeasure + TCHO_execution + Tprocessing + Tsearch_PCell_Conditional + Tsearch_PSCell + T∆_PSCell + TPSCell_ DU + 2 =1040+10+25+20+20 +2ms=1117 msfrom the start of T2.

## A.7.3.3.6NR conditional Handover including target MCG and candidate SCG from FR1-FR2 NR-DC to FR1-FR2 NR-DC

## A.7.3.3.6.1Test Purpose and Environment

This test is to verify the requirements for conditional handover including target MCG and candidate SCG in NR-DC: from FR1-FR2 NR-DC to FR1-FR2 NR-DC specified in clause 6.1.7.2. This test verifies the requirements for inter-frequency FR1-FR1 conditional handover and intra-frequency FR2-FR2 conditional PSCell change.

## A.7.3.3.6.2Test Parameters

The supported test configurations are given in table A.7.3.3.6.1-1. The test scenario comprises four NR cells, source PCell (Cell 1) and source PSCell (Cell 2), target PCell (Cell 3), and target PSCell (Cell 4).

Cell 1 is on radio channel 1 in FR1. Cell 3 is on radio channel 2 in FR1, Cell 2 and Cell 4 are on radio channel 3 in FR2. The event-triggered reporting with Event A3 is used for handover condition. Test parameters are given in tables A.7.3.3.6.1-2, A.7.3.3.6.1-3, and A.7.3.3.6.1-4 below. Gap pattern ID gp0 is configured for PCell FR1-FR1 Inter frequency conditional handover in the test case. The test consists of three successive time periods, with time durations of T1, T2 and T3, respectively.

At the start of T1, the UE shall be connected to Cell 1 on radio channel 1 and Cell 2 on radio channel 3. UE is not aware of Cell 3 and Cell 4. TE shall configure a condition implying conditional handover to Cell 3 with a condition implying conditional PSCell change to cell 4 during T1, at a time earlier than TRRC before the beginning of T2.

At the start of T2, cell 3 becomes detectable. At the start of T3, cell 4 becomes detectable. The condition for conditional handover and the condition for conditional PSCell change is met during T3.

Table A.7.3.3.6.1-1: Supported test configurations for Conditional Handover including target MCG and candidate SCG from NR-DC to NR-DC

Table A.7.3.3.6.1-2: General test parameters for FR1-FR1 inter frequency conditional handover with target MCG and FR2-FR2 intra-frequency conditional PSCell change with candidate SCG

Table A.7.3.3.6.1-3: Cell specific test parameters for PCell FR1-FR1 Inter frequency handover with target MCG

Table A.7.3.3.6.1-4: Cell specific test parameters for conditionaly intra-frequency FR2-FR2 PSCell change with candidate SCG

## A.7.3.3.6.3 Test Requirements

TRRC + TEvent_DU occurs during T1 and T2, as the conditional handover condition for cell 3 becomes satisfied from the start of T2, and the conditional PSCell change condition for cell 4 becomes satisfied from the start of T3. The test shall verify that there are no interruptions during T1 and T2. The UE shall not start the transmission of the new uplink PRACH channel of the target PCell before T3.

In this test, the UE shall start to transmit the PRACH to Cell 3 less than 1677 ms (power class 1) or 1157 ms (power classes 2,3 and 4)Note1 from the beginning of time period T3.

The UE shall transmit the PRACH to Cell 4 at latest 1677 ms (power class 1) or 1157 ms (power classes 2,3 and 4)Note2 from the beginning of time period T3.

The rate of correct observed delay in conditional handover including target MCG and candidate SCG during repeated tests shall be at least 90 %.

NOTE 1:The PCell conditional handover delay can be expressed as specified in clause 6.1.7.2.1:

DCHOwithCPC_PCell = TRRC_delay + TEvent_DU + max (Tmeasure_PCell, Tmeasure_PSCell) + TUE_preparation + Tprocessing + TΔ_PCell + TPCell_DU + 2 ms,

Where:

max (Tmeasure_PCell, Tmeasure_PSCell) = 1600 ms (power class 1) or 1080 ms (power classes 2, 3 and 4)

TUE_preparation = 10 ms

Tprocessing = 25 ms

TΔ_PSCell = 20 ms

TPCell_ DU = 20 ms

NOTE 2:The PSCell conditional change delay can be expressed as follows as specified in clause 6.1.7.2.2:

DCHOwithCPC_PSCell = TRRC_delay + TEvent_DU + max (Tmeasure_PCell, Tmeasure_PSCell) + TUE_preparation + Tprocessing + TΔ_PSCell + TPSCell_DU + 2 ms

Where:

max (Tmeasure_PCell, Tmeasure_PSCell) = 1600 ms (power class 1) or 1080 ms (power classes 2, 3 and 4)

TUE_preparation = 10 ms

Tprocessing = 25 ms

TΔ_PSCell = 20 msTPSCell_ DU = 20 ms

## A.7.3.4LTM PCell Switch

## A.7.3.4.1RACH based Intra-frequency PCell switch from FR2 to FR2

## A.7.3.4.1.1Test Purpose and Environment

This test is to verify the intra frequency RACH based LTM PCell switch requirements from NR FR2 to NR FR2 specified in clause 6.3.1 for both with and without early TCI state activation.

## A.7.3.4.1.2Test Parameters

Two cells are deployed in the test, which are FR2 PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. Test configurations are given in table A.7.3.4.1.2-1. Both cell switch delay and interruption length are tested by using the parameters in table A.7.3.4.1.2-2 and A.7.3.4.1.2-3.

The test consists of 4 tests, and UE is required to pass one among Test 1A, Test 1B, Test 2A and Test 2B.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18 and/or ltm-MAC-CE-SeparateTCI-r18

-Test 1A: for a UE supporting ltm-MAC-CE-JointTCI-r18.

-Test 1B: for a UE supporting ltm-MAC-CE-SeparateTCI-r18 and does not support ltm-MAC-CE-JointTCI-r18.

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18 and ltm-MAC-CE-SeparateTCI-r18

-Test 2A: for a UE supporting ltm-BeamIndicationJointTCI-r18.

-Test 2B: for a UE supporting ltm-BeamIndicationSeparateTCI-r18 and does not support ltm-BeamIndicationJointTCI-r18.

The test consists of four successive time periods, with time durations of T1, T2, T3 and T4, respectively. No gap patterns are configured in the test case.

During T1, for Test 1A, 1B, 2A and 2B:

-A measurement object is configured for the frequency of the Cell 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-T1 ends with UE reporting an L3 measurement result of Cell 2 to Cell 1.

During T2, for Test 1A, 1B, 2A and 2B:

-At the start of T2, UE is provided with LTM-Candidate-r18 for Cell 2

-Joint TCI state configuration as defined in table A.7.3.4.1.2-2 for Test 1A and Test 2A are provided.

-Separate TCI state configuration as defined in table A.7.3.4.1.2-2 for Test 1B and Test 2B are provided.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

-T2 ends with UE reporting a valid L1-RSRP result of Cell 2.

During T3, for Test 1A and 1B:

-At the start of T3, UE receives candidate cell TCI state activation MAC CE for Cell 2.

-In Test 1A, CandidateTCI-State#1 is activated.

-In Test 1B, CandidateTCI-State#1 and CandidateTCI-UL-State#1 is activated.

-T3 ends 50 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2A and 2B, T3 is skipped.

During T4, for Test 1A, 1B, 2A and 2B:

-The start of T4 is the instant when the last TTI containing LTM cell switch command MAC CE is sent by Cell 1 to the UE.

-In the cell switch command, Cell 2 is the target cell. Contention-Free Random-Access Resources are indicated. The field of Timing Advance Command is set to FFF.

-In test 1A, CandidateTCI-State#2 is indicated.

-In test 1B, CandidateTCI-State#2 and CandidateTCI-UL-State#1 are indicated.

-In test 2A, CandidateTCI-State#1 is indicated.

-In test 2B, CandidateTCI-State#1 and CandidateTCI-UL-State#1 are indicated.

-T4 ends upon the reception of PRACH at Cell 2.

Table A.7.3.4.1.2-1: Intra-frequency cell switch from FR2 to FR2 test configurations

Table A.7.3.4.1.2-2: General test parameters for Intra-frequency cell switch from FR2 to FR2

Table A.7.3.4.1.2-3: Cell specific test parameters for NR FR2-FR2 Intra frequency cell switch test case

## A.7.3.4.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 in no later than DLTM from the beginning of time period T4.

The rate of correct cell switches observed during repeated tests shall be at least 90 %.

NOTE:The cell switch delay can be expressed as DLTM (= Tcmd + TLTM-interrupt), where:

Tcmd = THARQ + 3 ms and is specified in clause 6.3.1.2,

TLTM-interrupt = TLTM-RRC-processing + TLTM-processing + Tfirst-RS + TRS-proc + TLTM-IU ms, as stated in clause 6.3.1.3

-Tfirst-RS + TRS-proc= 0 ms for Test 1A and 1B, Tfirst-RS + TRS-proc= 22 ms for Test 2A and 2B

-TLTM-IU = 20 ms

-TLTM-RRC-processing = 10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TLTM-RRC-processing =0 ms

-TLTM-processing = 10 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 10 ms for FR2-to-FR2 cell switch in the capability

-TLTM-processing = 15 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 15 ms for FR2-to-FR2 cell switch in the capability

-TLTM-processing = 20 ms if the UE does not support ltm-FastUE-Processing-r18 capability.

## A.7.3.4.2RACH-less Intra-frequency PCell switch from FR2 to FR2

## A.7.3.4.2.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 RACH-less intra frequency PCell switch specified in clause 6.3.1 for both with and without early TCI state activation.

## A.7.3.4.2.2Test Parameters

Two cells are deployed in the test, which are FR2 PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. Test configurations are given in table A.7.3.4.2.2-1. Both cell switch delay and interruption length are tested by using the parameters in table A.7.3.4.2.2-2 and A.7.3.4.2.2-3.

The test consists of 4 tests, and UE is required to pass one among Test 1A, Test 1B, Test 2A and Test 2B.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18 and/or ltm-MAC-CE-SeparateTCI-r18

-Test 1A: for a UE supporting ltm-MAC-CE-JointTCI-r18.

-Test 1B: for a UE supporting ltm-MAC-CE-SeparateTCI-r18 and does not support ltm-MAC-CE-JointTCI-r18.

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18 and ltm-MAC-CE-SeparateTCI-r18

-Test 2A: for a UE supporting ltm-BeamIndicationJointTCI-r18.

-Test 2B: for a UE supporting ltm-BeamIndicationSeparateTCI-r18 and does not support ltm-BeamIndicationJointTCI-r18.

The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5, respectively. No gap patterns are configured in the test case.

During T1, for Test 1A, 1B, 2A and 2B:

-A measurement object is configured for the frequency of the Cell 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-T1 ends with UE reporting an L3 measurement result of Cell 2 to Cell 1.

During T2, for Test 1A, 1B, 2A and 2B:

-At the start of T2, UE is provided with LTM-Candidate-r18 for Cell 2

-Joint TCI state configuration as defined in table A.7.3.4.2.2-2 for Test 1A and Test 2A are provided.

-Separate TCI state configuration as defined in table A.7.3.4.2.2-2 for Test 1B and Test 2B are provided.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

-T2 ends with UE reporting a valid L1-RSRP result of Cell 2.

During T3, for Test 1A and 1B:

-At the start of T3, UE receives candidate cell TCI state activation MAC CE for Cell 2.

-In Test 1A, CandidateTCI-State#1 is activated.

-In Test 1B, CandidateTCI-State#1 and CandidateTCI-UL-State#1 is activated.

-T3 ends 50 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2A and 2B, T3 is skipped.

During T4, for Test 1A, 1B, 2A and 2B:

-At the start of T4, UE receives PDCCH order to trigger PRACH transmission on Cell 2.

-T4 ends 5 ms after the UE transmits the PRACH to Cell 2.

-For UE incapable of rach-EarlyTA-Measurement-r18, T4 is skipped.

During T5, for Test 1A, 1B, 2A and 2B:

-The start of T5 is the last TTI containing LTM cell switch command MAC CE is sent by Cell 1 to the UE.

-In the cell switch command, Cell 2 is the target cell and the field of Timing Advance Command is set to 0.

-In test 1A, CandidateTCI-State#2 is indicated.

-In test 1B, CandidateTCI-State#2 and CandidateTCI-UL-State#1 are indicated.

-In test 2A, CandidateTCI-State#1 is indicated.

-In test 2B, CandidateTCI-State#1 and CandidateTCI-UL-State#1 are indicated.

-Cell 2 continuously schedules PUSCH for the UE.

-T5 ends either at the UL slot of PUSCH scheduled by Cell 2 at the fist DL slot not earlier than (Tcmd + TLTM-RRC-processing + TLTM-processing + Tfirst-RS + TRS-proc) after the beginning of T5 or upon the reception of PUSCH at Cell 2, whichever is earlier.

-The values of Tcmd, TLTM-RRC-processing TLTM-processing, Tfirst-RS and TRS-proc are specified in A.7.3.4.2.3.

Table A.7.3.4.2.2-1: Intra-frequency cell switch from FR2 to FR2 test configurations

Table A.7.3.4.2.2-2: General test parameters for Intra-frequency cell switch from FR2 to FR2

Table A.7.3.4.2.2-3: Cell specific test parameters for NR FR2-FR2 Intra frequency cell switch test case

## A.7.3.4.2.3Test Requirements

The UE shall start to transmit PUSCH to Cell 2 in no later than DLTM from the beginning of time period T5.

The rate of correct cell switches observed during repeated tests shall be at least 90 %.

NOTE:The cell switch delay can be expressed as DLTM (= Tcmd + TLTM-interrupt), where:

Tcmd = THARQ + 3 ms and is specified in clause 6.3.1.2, TLTM-interrupt is defined in clause 6.3.1.3 as TLTM-RRC-processing + TLTM-processing + Tfirst-RS + TRS-proc + TLTM-IU,

-Tfirst-RS + TRS-proc= 0 ms for Test 1A and 1B, Tfirst-RS + TRS-proc= 22 ms for Test 2A and 2B,

-TLTM-IU is the uncertainty on transmitting the first uplink transmission on Cell 2.

-TLTM-RRC-processing = 10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TLTM-RRC-processing =0 ms

-TLTM-processing = 10 ms if the UE supports ltm-FastProcessingConfig-r18 capability and UE reports 10 ms for FR2-to-FR2 cell switch in the capability

-TLTM-processing = 15 ms if the UE supports ltm-FastProcessingConfig-r18 capability and UE reports 15 ms for FR2-to-FR2 cell switch in the capability

-TLTM-processing = 20 ms if the UE does not support ltm-FastProcessingConfig-r18 capability.

## A.7.3.4.3RACH-based Inter-frequency LTM PCell switch from FR2 to FR2

## A.7.3.4.3.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 RACH-based inter-frequency PCell switch specified in clause 6.3.1 for both with and without early TCI state activation.

## A.7.3.4.3.2Test Parameters

Two cells are deployed in the test, which are FR2 PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on a different frequency than the PCell. Test configurations are given in table A.7.3.4.3.2-1. Both cell switch delay and interruption length are tested by using the parameters in table A.7.3.4.3.2-2 and A.7.3.4.3.2-3.

The test consists of 4 tests, and UE is required to pass one among Test 1A, Test 1B, Test 2A and Test 2B.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18 and/or ltm-MAC-CE-SeparateTCI-r18

-Test 1A: for a UE supporting ltm-MAC-CE-JointTCI-r18.

-Test 1B: for a UE supporting ltm-MAC-CE-SeparateTCI-r18 and does not support ltm-MAC-CE-JointTCI-r18.

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18 and ltm-MAC-CE-SeparateTCI-r18

-Test 2A: for a UE supporting ltm-BeamIndicationJointTCI-r18.

-Test 2B: for a UE supporting ltm-BeamIndicationSeparateTCI-r18 and does not support ltm-BeamIndicationJointTCI-r18.

The test consists of five successive time periods, with time durations of T1, T2, T3, and T4, respectively. Measurement gap pattern gp0 is configured.

During T1, for Test 1A, 1B,2A and 2B:

-A measurement object is configured for the frequency of the Cell 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-T1 ends with UE reporting an L3 measurement result of Cell 2 to Cell 1.

During T2, for Test 1A, 1B, 2A and 2B:

-At the start of T2, UE is provided with LTM-Candidate-r18 for Cell 2

-Joint TCI state configuration as defined in table A.7.3.4.3.2-2 for Test 1A and Test 2A are provided.

-Separate TCI state configuration as defined in table A.7.3.4.3.2-2 for Test 1B and Test 2B are provided.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

-T2 ends with UE reporting a valid L1-RSRP result of Cell 2.

During T3, for Test 1A and 1B:

-At the start of T3, UE receives candidate cell TCI state activation MAC CE for Cell 2.

-In Test 1A, CandidateTCI-State#1 is activated.

-In Test 1B, CandidateTCI-State#1 and CandidateTCI-UL-State#1 is activated.

-T3 ends 100 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2A and 2B, T3 is skipped.

During T4, for Test 1A, 1B, 2A and 2B:

-The start of T4 is the last TTI containing LTM cell switch command MAC CE is sent by Cell 1 to the UE.

-In the cell switch command, Cell 2 is the target cell and the field of Timing Advance Command is set to FFF.

-In test 1A, CandidateTCI-State#2 is indicated.

-In test 1B, CandidateTCI-State#2 and CandidateTCI-UL-State#1 are indicated.

-In test 2A, CandidateTCI-State#1 is indicated.

-In test 2B, CandidateTCI-State#1 and CandidateTCI-UL-State#1 are indicated.

-T4 ends upon the reception of PRACH at Cell 2.

Table A.7.3.4.3.2-1: Inter-frequency cell switch from FR2 to FR2 test configurations

Table A.7.3.4.3.2-2: General test parameters for Inter-frequency cell switch from FR2 to FR2

Table A.7.3.4.3.2-3: Cell specific test parameters for NR FR2-FR2 Inter frequency cell switch test case

## A.7.3.4.3.3Test Requirements

The UE shall start to transmit RACH to Cell 2 in no later than DLTM from the beginning of time period T4.

The rate of correct cell switches observed during repeated tests shall be at least 90 %.

NOTE:The cell switch delay can be expressed as DLTM (= Tcmd + TLTM-interrupt), where:

Tcmd = THARQ + 3 ms and is specified in clause 6.3.1.2, TLTM-interrupt is defined in clause 6.3.1.3 as TLTM-RRC-processing + TLTM-processing + Tfirst-RS + TRS-proc + TLTM-IU,

-Tfirst-RS + TRS-proc= 0 ms for Test 1A and 1B, Tfirst-RS + TRS-proc= 22 ms for Test 2A and 2B,

-TLTM-IU = 20 ms.

-TLTM-RRC-processing = 10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TLTM-RRC-processing =0 ms

-TLTM-processing = 10 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 10 ms for FR2-to-FR2 cell switch in the capability

-TLTM-processing = 15 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 15 ms for FR2-to-FR2 cell switch in the capability

-TLTM-processing = 20 ms if the UE does not support ltm-FastUE-Processing-r18 capability.

## A.7.3.4.4RACH-less Intra-frequency CLTM PCell switch from FR2 to FR2 triggered by SSB based L1-RSRP measurement

## A.7.3.4.4.1Test Purpose and Environment

This test is to verify the requirement for the NR FR2-NR FR2 RACH-less intra frequency PCell switch specified triggered by SSB based L1-RSRP measurement in clause 6.3.2 for both with and without early TCI state activation, for UE supporting cltm-EarlyTA-Indication-r19 and supporting intraFreqL1-MeasConfig-r18.

## A.7.3.4.4.2Test Parameters

Two cells are deployed in the test, which are FR2 PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. Test configurations are given in table A.7.3.4.4.2-1. Both cell switch delay and interruption length are tested by using the parameters in table A.7.3.4.4.2-2 and A.7.3.4.4.2-3.

The test consists of 4 tests, and UE is required to pass one among Test 1A, Test 1B, Test 2A and Test 2B.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18 and/or ltm-MAC-CE-SeparateTCI-r18

-Test 1A: for a UE supporting ltm-MAC-CE-JointTCI-r18.

-Test 1B: for a UE supporting ltm-MAC-CE-SeparateTCI-r18 and does not support ltm-MAC-CE-JointTCI-r18.

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18 and ltm-MAC-CE-SeparateTCI-r18

-Test 2A: for a UE supporting ltm-BeamIndicationJointTCI-r18.

-Test 2B: for a UE supporting ltm-BeamIndicationSeparateTCI-r18 and does not support ltm-BeamIndicationJointTCI-r18.

The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5, respectively. No gap patterns are configured in the test case.

During T1, for Test 1A, 1B, 2A and 2B:

-A measurement object is configured for the frequency of the Cell 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-T1 ends with UE reporting an L3 measurement result of Cell 2 to Cell 1.

During T2, for Test 1A, 1B, 2A and 2B:

-At the start of T2, UE is provided with LTM-Candidate-r18 for Cell 2

-Joint TCI state configuration as defined in table A.7.3.4.4.2-2 for Test 1A and Test 2A are provided.

-Separate TCI state configuration as defined in table A.7.3.4.4.2-2 for Test 1B and Test 2B are provided.

-LTM-Candidate-r18 includes the L1 condition implying cell switch to Cell 2 in ltm-ExecutionCondition-r19.

-Event LTM3 is used in the CLTM execution condition as defined in table A.7.3.4.4.2-2.

-UE is configured with SSB-based L1-RSRP measurements.

During T3, for Test 1A and 1B:

-At the start of T3, UE receives candidate cell TCI state activation MAC CE for Cell 2.

-In Test 1A, CandidateTCI-State#1 is activated.

-In Test 1B, CandidateTCI-State#1 and CandidateTCI-UL-State#1 is activated.

-T3 ends 50 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2A and 2B, T3 is skipped.

During T4, for Test 1A, 1B, 2A and 2B:

-At the start of T4, UE receives PDCCH order to trigger PRACH transmission on Cell 2.

-T4 ends 5 ms after the UE transmits the PRACH to Cell 2.

-For UE incapable of rach-EarlyTA-Measurement-r18, T4 is skipped.

During T5, for Test 1A, 1B, 2A and 2B:

-The start of T5 is the condition in ltm-ExecutionCondition-r19 becomes satisfied.

-Cell 2 is the target cell and the field of Timing Advance Command is set to 0.

-Cell 2 continuously schedules PUSCH for the UE.

-T5 ends either at the UL slot of PUSCH scheduled by Cell 2 at the first DL slot not earlier than (TRRC + TEvent_DU + Tmeasure + TCLTM-RRC-processing + TLTM-processing + Tfirst-RS + TRS-proc ) after the beginning of T5 or upon the reception of PUSCH at Cell 2, whichever is earlier.

-The values of TRRC, TEvent_DU, Tmeasure , TCLTM-RRC-processing TLTM-processing, Tfirst-RS and TRS-proc are specified in A.7.3.4.4.3.

Table A.7.3.4.4.2-1: Intra-frequency cell switch from FR2 to FR2 test configurations

Table A.7.3.4.4.2-2: General test parameters for Intra-frequency L1 triggered CLTM cell switch from FR2 to FR2

Table A.7.3.4.4.2-3: Cell specific test parameters for NR FR2-FR2 Intra frequency L1 triggered CLTM cell switch test case

## A.7.3.4.4.3Test Requirements

The UE shall start to transmit PUSCH to Cell 2 in no later than DLTM from the beginning of time period T5.

The rate of correct cell switches observed during repeated tests shall be at least 90 %.

NOTE:The cell switch delay can be expressed as DCLTM (= TRRC + TEvent_DU + Tmeasure + TCLTM-RRC-processing + TCLTM-interrupt), where:

TRRC is the RRC procedure delay defined in clause 12 in TS 38.331[2].

TEvent_DU is the delay uncertainty.

Tmeasure = 1080 +960 ms= 2040ms.

TCLTM-RRC-processing = 10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TCLTM-RRC-processing =0 ms

TCLTM-interrupt = TLTM-processing + Tfirst-RS + TRS-proc + TCLTM-IU ms, as stated in clause 6.3.2.2.3.

-TLTM-processing = 10 ms if the UE supports ltm-FastUE-Processing-r18capability and UE reports 10 ms for FR2-to-FR2 cell switch in the capability

-TLTM-processing = 15 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 15 ms for FR2-to-FR2 cell switch in the capability

-TLTM-processing = 20 ms if the UE does not support ltm-FastUE-Processing-r18 capability

-Tfirst-RS + TRS-proc= 0 ms for Test 1,Tfirst-RS + TRS-proc= 22 ms for Test 2

-TCLTM-IU = 20 ms

## A.7.3.4.5RACH-based Intra-frequency CLTM PCell switch from FR2 to FR2 triggered by SSB based L1-RSRP measurement

## A.7.3.4.5.1Test Purpose and Environment

This test is to verify the intra-frequency RACH based conditional LTM PCell switch requirements from NR FR2 to NR FR2 triggered by SSB based L1-RSRP measurement specified in clause 6.3.2 for both with and without early TCI state activation, for UE supporting intraFreqL1-MeasConfig-r18 and not supporting cltm-EarlyTA-Indication-r19 and ltm-InterFreqMeasGap-r18.

## A.7.3.4.5.2Test Parameters

Two cells are deployed in the test, which are FR2 PCell (Cell 1) and a FR2 neighbour cell (Cell 2) on the same frequency as the PCell. Test configurations are given in table A.7.3.4.5.2-1. Both cell switch delay and interruption length are tested by using the parameters in table A.7.3.4.5.2-2 and A.7.3.4.5.2-3.

The test consists of 4 tests, and UE is required to pass one among Test 1A, Test 1B, Test 2A and Test 2B.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18 and/or ltm-MAC-CE-SeparateTCI-r18

-Test 1A: for a UE supporting ltm-MAC-CE-JointTCI-r18.

-Test 1B: for a UE supporting ltm-MAC-CE-SeparateTCI-r18 and does not support ltm-MAC-CE-JointTCI-r18.

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18 and ltm-MAC-CE-SeparateTCI-r18

-Test 2A: for a UE supporting ltm-BeamIndicationJointTCI-r18.

-Test 2B: for a UE supporting ltm-BeamIndicationSeparateTCI-r18 and does not support ltm-BeamIndicationJointTCI-r18.

The test consists of four successive time periods, with time durations of T1, T2, T3 and T4, respectively. No gap patterns are configured in the test case.

During T1, for Test 1A, 1B, 2A and 2B:

-A measurement object is configured for the frequency of the Cell 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-T1 ends with UE reporting an L3 measurement result of Cell 2 to Cell 1.

During T2, for Test 1A, 1B, 2A and 2B:

-At the start of T2, UE is provided with LTM-Candidate-r18 for Cell 2

-Joint TCI state configuration as defined in table A.7.3.4.5.2-2 for Test 1A and Test 2A are provided.

-Separate TCI state configuration as defined in table A.7.3.4.5.2-2 for Test 1B and Test 2B are provided.

-LTM-Candidate-r18 includes the L1 condition implying cell switch to Cell 2 in ltm-ExecutionCondition-r19.

-Event LTM3 is used in the CLTM execution condition as defined in table A.7.3.4.5.2-2.

-UE is configured with SSB-based L1-RSRP measurements.

During T3, for Test 1A and 1B:

-At the start of T3, UE receives candidate cell TCI state activation MAC CE for Cell 2.

-In Test 1A, CandidateTCI-State#1 is activated.

-In Test 1B, CandidateTCI-State#1 and CandidateTCI-UL-State#1 is activated.

-T3 ends 50 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2A and 2B, T3 is skipped.

During T4, for Test 1A, 1B, 2A and 2B:

-The start of T4 is the condition in ltm-ExecutionCondition-r19 becomes satisfied, Cell 2 is the target cell.

-T4 ends upon the reception of PRACH at Cell 2.

Table A.7.3.4.5.2-1: Intra-frequency cell switch from FR2 to FR2 test configurations

Table A.7.3.4.5.2-2: General test parameters for Intra-frequency cell switch from FR2 to FR2

Table A.7.3.4.5.2-3: Cell specific test parameters for NR FR2-FR2 Intra frequency cell switch test case

## A.7.3.4.5.3Test Requirements

TRRC + TEvent_DU occurs during T1 as the cell switch condition becomes satisfied at the start of T2.

The UE shall start to transmit the PRACH to Cell 2 in no later than Tmeasure + TCLTM-RRC-processing + TCLTM-interrupt from the beginning of time period T2 .

The rate of correct cell switches observed during repeated tests shall be at least 90 %.

NOTE:The conditional LTM cell switch delay can be expressed as DcLTM (= TRRC + TEvent_DU + Tmeasure + TCLTM-RRC-processing + TCLTM-interrupt), where:

TRRC is the RRC procedure delay defined in clause 12 in TS 38.331 [2].

TEvent_DU is the delay uncertainty.

Tmeasure =1080+960=2040 ms.

TCLTM-RRC-processing = 10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TCLTM-RRC-processing =0 ms.

TCLTM-interrupt = TLTM-processing + Tfirst-RS + TRS-proc + TCLTM-IU ms, as stated in clause 6.3.2.2.3.

-TLTM-processing = 10 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 10 ms for FR2-to-FR2 cell switch in the capability

-TLTM-processing = 15 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 15 ms for FR2-to-FR2 cell switch in the capability

-TLTM-processing = 20 ms if the UE does not support ltm-FastUE-Processing-r18 capability.

-Tfirst-RS + TRS-proc= 0 ms for Test 1, Tfirst-RS + TRS-proc= 22 ms  for Test 2

-TCLTM-IU = 20 ms

## A.7.3.5LTM PSCell Switch

## A.7.3.5.1RACH-based Intra-frequency LTM PSCell switch from FR2 to FR2

## A.7.3.5.1.1Test Purpose and Environment

This test is to verify RACH-based LTM PSCell Switch requirements for the NR FR2-NR FR2 intra frequency cell switch specified in clause 8.20 for both with and without early TCI state activation.

## A.7.3.5.1.2Test Parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), source FR2 PSCell (Cell 2) and target FR2 PSCell (Cell 3) on the same frequency as the PSCell. Test configurations are given in table A.7.3.5.1.2-1. Both PSCell switch delay and interruption length are tested by using the parameters in table A.7.3.5.1.2-2, A.7.3.5.1.2-3 and A.7.3.5.1.2-4.

The test consists of 4 tests, and UE is required to pass one among Test 1A, Test 1B, Test 2A and Test 2B.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18 and/or ltm-MAC-CE-SeparateTCI-r18

-Test 1A: for a UE supporting ltm-MAC-CE-JointTCI-r18.

-Test 1B: for a UE supporting ltm-MAC-CE-SeparateTCI-r18 and does not support ltm-MAC-CE-JointTCI-r18.

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18 and ltm-MAC-CE-SeparateTCI-r18

-Test 2A: for a UE supporting ltm-BeamIndicationJointTCI-r18.

-Test 2B: for a UE supporting ltm-BeamIndicationSeparateTCI-r18 and does not support ltm-BeamIndicationJointTCI-r18.

The test consists of four successive time periods, with time durations of T1, T2, T3 and T4, respectively. No gap patterns are configured in the test case.

During T1, for Test 1A, 1B, 2A and 2B:

-A measurement object is configured for the frequency of the Cell 3, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-T1 ends with UE reporting an L3 measurement result of Cell 3 to Cell 1.

During T2, for Test 1A, 1B, 2A and 2B:

-At the start of T2, UE is provided with LTM-Candidate-r18 for Cell 3

-Joint TCI state configuration as defined in table A.7.3.5.1.2-2 for Test 1A and Test 2A are provided.

-Separate TCI state configuration as defined in table A.7.3.5.1.2-2 for Test 1B and Test 2B are provided.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 3) in PUCCH format 2.

-T2 ends with UE reporting a valid L1-RSRP result of Cell 3.

During T3, for Test 1A and 1B:

-At the start of T3, UE receives candidate cell TCI state activation MAC CE for Cell 3.

-In Test 1A, CandidateTCI-State#1 is activated.

-In Test 1B, CandidateTCI-State#1 and CandidateTCI-UL-State#1 is activated.

-T3 ends 50 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2A and 2B, T3 is skipped.

During T4, for Test 1A, 1B, 2A and 2B:

-The start of T4 is the instant when the last TTI containing LTM cell switch command MAC CE is sent by Cell 2 to the UE.

-In the cell switch command, Cell 3 is the target cell for PSCell switch. Contention-Free Random-Access Resources are indicated and the field of Timing Advance Command is set to FFF.

-In test 1A, CandidateTCI-State#2 is indicated.

-In test 1B, CandidateTCI-State#2 and CandidateTCI-UL-State#1 are indicated.

-In test 2A, CandidateTCI-State#1 is indicated.

-In test 2B, CandidateTCI-State#1 and CandidateTCI-UL-State#1 are indicated.

-T4 ends upon the reception of PRACH at Cell 3.

Table A.7.3.5.1.2-1: Intra-frequency PSCell switch from FR2 to FR2 test configurations

Table A.7.3.5.1.2-2: General test parameters for Intra-frequency cell switch from FR2 to FR2

Table A.7.3.5.1.2-3: Cell specific test parameters for PCell (Cell 1)

Table A.7.3.5.1.2-4: Cell specific test parameters for NR FR2-FR2 Intra frequency cell switch test case

## A.7.3.5.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 3 in no later than DLTM from the beginning of time period T4.

The rate of correct cell switches observed during repeated tests shall be at least 90 %.

NOTE:The cell switch delay can be expressed as DLTM (= Tcmd + TLTM-interrupt), where:

Tcmd = THARQ + 3 ms and is specified in clause 6.3.1.2, TLTM-interrupt is defined in clause 8.20.3 as TLTM-interrupt  = TLTM-RRC-processing + TLTM-processing + Tfirst-RS + TRS-proc + TLTM-IU ms.

-Tfirst-RS + TRS-proc= 0 ms for Test 1A and 1B, Tfirst-RS + TRS-proc= 22 ms for Test 2A and 2B

-TLTM-IU=20 ms,

-TLTM-RRC-processing = 10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TLTM-RRC-processing =0 ms

-TLTM-processing = 10 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 10 ms for FR2-to-FR2 cell switch in the capability

-TLTM-processing = 15 ms if the UE supports ltm-FastUE-Processing-r18] capability and UE reports 15 ms for FR2-to-FR2 cell switch in the capability

-TLTM-processing = 20 ms if the UE does not support ltm-FastUE-Processing-r18 capability.

## A.7.4Timing

## A.7.4.1UE transmit timing

## A.7.4.1.1NR UE Transmit Timing Test for FR2

## A.7.4.1.1.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeb and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. highSpeedMeasFlagFR2-r17 is broadcast to UE supporting power class 6. This test will verify the requirements in clause 7.1.2.

Supported test configurations are shown in table 7.4.1.1.1-1.

Table A.7.4.1.1.1-1: Supported test configurations for FR2 PCell

For this test a single NR cell is used. Tables A.7.4.1.1.1-2 and A.7.4.1.1.1-2A define the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.7.4.1.1.1-3.

Table A.7.4.1.1.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.7.4.1.1.1-2A: OTA related test parameters

Table A.7.4.1.1.1-3: SRS Configuration for Timing Accuracy Test

Table A.7.4.1.1.1-4: Void

## A.7.4.1.1.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test:

1)Setup NR PCell according to parameters given in table A.7.4.1.1.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB.

a.The NTA offset value (in Tc units) is 13792

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.7.4.1.1.2-1

Table A.7.4.1.1.2-1 Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first path (in time) of DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna.  Skip this step for test 2 with DRX confiured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first path (in time) of DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.4.1.2NR UE Transmit Timing Test for FR2-2

## A.7.4.1.2.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeb and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1.2.

Supported test configurations are shown in table A.7.4.1.2.1-1.

Table A.7.4.1.2.1-1: Supported test configurations for FR2 PCell

For this test a single NR cell is used. Tables A.7.4.1.2.1-2 and A.7.4.1.2.1-2A define the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.7.4.1.2.1-3.

Table A.7.4.1.2.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.7.4.1.2.1-2A: OTA related test parameters

Table A.7.4.1.2.1-3: SRS Configuration for Timing Accuracy Test

## A.7.4.1.2.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test:

1)Setup NR PCell according to parameters given in table A.7.4.1.2.2-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB.

a.The NTA offset value (in Tc units) is 13792

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.7.4.1.2.2-1

Table A.7.4.1.2.2-1 Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first detected path (in time) of DL SSB.  Skip this step for test 2 with DRX configured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

The rate of correct transmit timing observed during repeated tests shall be at least 90 %.

## A.7.4.1.3NR UE Transmit Timing Test with 2-TA for FR2 UE supporting multiDCI-IntraCellMultiTRP-TwoTA-r18

## A.7.4.1.3.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeb and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits, for UE supporting multiDCI-IntraCellMultiTRP-TwoTA-r18 and is configured with 2 TAGs for multi-DCI multi-TRP operation. UE is also configured with dl-OrJointTCI-StateList or ul-TCI-State-List. This test will verify the requirements in clause 7.1.2.

Supported test configurations are shown in table A.7.4.1.3.1-1.

Table A.7.4.1.3.1-1: Supported test configurations for FR2 PCell

For this test a single NR cell is used. Tables A.7.4.1.3.1-2 and A.7.4.1.3.1-2A define the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.7.4.1.3.1-3.

For UE not support the capability of “rxTimingDiff-r18”, the UE is only required to be tested in Test1 and Test3.

For UE supports the capability of “rxTimingDiff-r18”, the UE is only required to be tested in Test2 and Test4.

Table A.7.4.1.3.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.7.4.1.3.1-2A: OTA related test parameters

Table A.7.4.1.3.1-3: SRS Configuration for Timing Accuracy Test

Table A.7.4.1.3.1-4: Void

## A.7.4.1.3.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test:

1)Setup NR PCell according to parameters given in table A.7.4.1.3.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB for each TAG.

a.The NTA offset value (in Tc units) is 13792

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.7.4.1.3.2-1 for only TRP#1. The timing of the DL path of TRP#2 is not changed.

Table A.7.4.1.3.2-1 Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first path (in time) of DL SSB of each TAG used by the UE to determine downlink timing is received from the reference cell at the UE antenna. For TRP#2, the test system shall verify there is no adjustment. Skip this step for Test 3 and Test 4 with DRX confiured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first path (in time) of DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna. For Test 3 and Test 4 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.4.1.4NR UE Transmit Timing Test with 2-TA for FR2 UE supporting single DCI

## A.7.4.1.4.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeb and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits, for UE not configured PL offset and is configured with 2 TAGs for

single-DCI multi-TRP operation. UE is also configured with dl-OrJointTCI-StateList. This test will verify the requirements in clause 7.1.2.

Supported test configurations are shown in table A.7.4.1.4.1-1.

Table A.7.4.1.4.1-1: Supported test configurations for FR2 PCell

For this test a single NR cell is used. Tables A.7.4.1.4.1-2 and A.7.4.1.4.1-2A define the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.7.4.1.4.1-3.

Table A.7.4.1.4.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.7.4.1.4.1-2A: OTA related test parameters

Table A.7.4.1.4.1-3: SRS Configuration for Timing Accuracy Test

## A.7.4.1.4.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test:

1)Setup NR PCell according to parameters given in table A.7.4.1.4.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected corresponding path of DL SSB (TRP#1) for each TAG and detected another path of DL SSB (TRP#2).

a.The NTA offset value (in Tc units) is 13792

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.7.4.1.4.2-1 for only TRP#1. The timing of the DL path of TRP#2 is not changed.

Table A.7.4.1.4.2-1 Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first path (in time) of corresponding DL SSB (TRP#1) of each TAG used by the UE to determine downlink timing is received from the reference cell at the UE antenna. For TRP#2, the test system shall verify there is adjusted as well. Skip this step for Test 2 with DRX configured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first path (in time) of DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.7.4.2UE timer accuracy

## A.7.4.3Timing advance

## A.7.4.3.1SA FR2 timing advance adjustment accuracy

## A.7.4.3.1.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3.

## A.7.4.3.1.2Test Parameters

Supported test configurations are shown in table A.7.4.3.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.7.4.3.1.2-2, A.7.4.3.1.2-3 and A.7.4.3.1.2-4.

In all test cases, single cell is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.7.4.3.1.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.4.3.1.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in Clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k+1 for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.7.4.3.1.2-1: Timing advance supported test configurations

Table A.7.4.3.1.2-2: General test parameters for timing advance

Table A.7.4.3.1.2-3: Cell specific test parameters for timing advance

Table A.7.4.3.1.2-3A: OTA related test parameters

Table A.7.4.3.1.2-4: Sounding Reference Symbol Configuration for timing advance

## A.7.4.3.1.3 Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k = 11.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.7.4.3.2SA FR2-2 timing advance adjustment accuracy

## A.7.4.3.2.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3.

## A.7.4.3.2.2Test Parameters

Supported test configurations are shown in table A.7.4.3.2.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.7.4.3.2.2-2, A.7.4.3.2.2-3 and A.7.4.3.2.2-4.

In all test cases, single cell is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.7.4.3.2.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.4.3.2.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in Clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.7.4.3.2.2-1: Timing advance supported test configurations

Table A.7.4.3.2.2-2: General test parameters for timing advance

Table A.7.4.3.2.2-3: Cell specific test parameters for timing advance

Table A.7.4.3.2.2-3A: OTA related test parameters

Table A.7.4.3.2.2-4: Sounding Reference Symbol Configuration for timing advance

## A.7.4.3.2.3Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.7.4.3.3SA FR2 timing advance adjustment accuracy for asymmetric DL sTRP/UL mTRP deployment with two TAs

## A.7.4.3.3.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3 for asymmetric DL sTRP/UL mTRP deployment with two TAs when PL-offset is configured joint/UL TCI state(s).

## A.7.4.3.3.2Test Parameters

Supported test configurations are shown in table A.7.4.3.3.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.7.4.3.3.2-2, A.7.4.3.3.2-3 and A.7.4.3.3.2-4.

In all test cases, single cell is used. The cell is configured with two TRPs in the test. UE is also configured with tag2 in ServingCellConfig. Two SRS resource sets are configured and associated to different TAGs via TCI state configuration. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.7.4.3.3.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.7.4.3.3.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS for both TAGs sent from the UE.

As specified in Clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k+1 for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in Clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.7.4.3.3.2-1: Timing advance supported test configurations

Table A.7.4.3.3.2-2: General test parameters for timing advance

Table A.7.4.3.3.2-3: Cell specific test parameters for timing advance

Table A.7.4.3.3.2-3A: OTA related test parameters

Table A.7.4.3.3.2-4: Sounding Reference Symbol Configuration for timing advance

A.7.4.3.3.3Test Requirements

For TRP1 the UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k = 11. For TRP2 there shall be no change in the uplink timing.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.
