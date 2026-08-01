---
type: spec
aliases:
  - 38.133_38133-j50_sA.6-A.605
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.6-A.605/content.md"
---
# TS 38.133 38133-j50_sA.6-A.605

## A.6NR standalone tests with all NR cells in FR1

## A.6.1SA: RRC_IDLE state mobility

## A.6.1.1Cell re-selection to NR

## A.6.1.1.1Cell reselection to FR1 intra-frequency NR case

## A.6.1.1.1.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell reselection requirements specified in clause 4.2.2.3.

## A.6.1.1.1.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.6.1.1.1.2-1, A.6.1.1.1.2-2 and A.6.1.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.6.1.1.1.2-1: Supported test configurations

Table A.6.1.1.1.2-2: General test parameters for intra-frequency NR cell re-selection test case

Table A.6.1.1.1.2-3: Cell specific test parameters for intra-frequency NR cell re-selection test case in AWGN

## A.6.1.1.1.3Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_IntraSee table 4.2.2.3-1 in clause 4.2.2.3

Tevaluate, NR_ intraSee table 4.2.2.3-1 in clause 4.2.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 33.28 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 7.68 s for the cell re-selection delay to an already detected cell in the test case, which we allow 8 s.

## A.6.1.1.2Cell reselection to FR1 inter-frequency NR case

## A.6.1.1.2.1Test Purpose and Environment

This test is to verify the requirement for the inter-frequency NR cell reselection requirements specified in clause 4.2.2.4.

## A.6.1.1.2.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.6.1.1.2.2-1, A.6.1.1.2.2-2 and A.6.1.1.2.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

Table A.6.1.1.2.2-1: Supported test configurations

Table A.6.1.1.2.2-2: General test parameters for FR1 inter-frequency NR cell re-selection test case

Table A.6.1.1.2.2-3: Cell specific test parameters for FR1 inter-frequency NR cell re-selection test case in AWGN

## A.6.1.1.2.3Test Requirements

The cell reselection delay to a higher priority cell is defined as the time from the beginning of time period T3, to the moment when the UE camps again on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The cell reselection delay to a lower priority cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to a lower priority cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR_ inter + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Thigher_priority_searchSee clause 4.2.2.7

Tevaluate, NR_ interSee table 4.2.2.4-1 in clause 4.2.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority cell and 7.68 s for the cell re-selection delay to a lower priority cell in the test case, which we allow 8 s.

## A.6.1.1.3Cell reselection to FR1 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion

## A.6.1.1.3.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell reselection requirements for UE fulfilling low mobility criterion specified in clause 4.2.2.9.2

## A.6.1.1.3.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.6.1.1.3.2-1, A.6.1.1.3.2-2 and A.6.1.1.3.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.6.1.1.3.2-1: Supported test configurations

Table A.6.1.1.3.2-2: General test parameters for FR1 intra-frequency NR cell re-selection test case for UE fulfilling low mobility criterion

Table A.6.1.1.3.2-3: Cell specific test parameters for FR1 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling low mobility criterion

## A.6.1.1.3.3Test Requirements

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected cell shall be less than 17 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 17 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to an already detected cell can be expressed as: Tevaluate,NR_Intra + TSI-NR,

Where:

Tevaluate,NR_IntraSee table 4.2.2.9.2-1 in clause 4.2.2.9.2 for reselection to Cell 2 during T1 with UE fulfilling low mobility criterion. 15.36 s.

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 16.64 s, allow 17 s for the cell re-selection delay to an already detected cell for UE fulfilling low mobility criterion in the test case.

## A.6.1.1.4Cell reselection to FR1 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion

## A.6.1.1.4.1Test Purpose and Environment

This test is to verify the relaxed cell re-selection requirement for UEs configured with not-at-cell edge criterion specified in clause 4.2.2.9.3.

## A.6.1.1.4.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.6.1.1.4.2-1, A.6.1.1.4.2-2 and A.6.1.1.4.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas.

Table A.6.1.1.4.2-1: Supported test configurations

Table A.6.1.1.4.2-2: General test parameters for FR1 intra-frequency NR cell re-selection test case for UE fulfilling not-at-cell edge criterion

Table A.6.1.1.4.2-3: Cell specific test parameters for FR1 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling not-at-cell edge criterion

## A.6.1.1.4.3Test Requirements

The cell re-selection delay to an already detected cell for UE configured with cellEdgeEvaluation criterion is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected cell for UE configured with cellEdgeEvaluation criterion shall be less than 17 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to an already detected cell for UE configured with relaxed measurement criterion can be expressed as: Tevaluate,NR_Intra + TSI-NR,

Where:

Tevaluate,NR_IntraSee table 4.2.2.9.3-1 for UE fulfilling not-at-cell edge criterion in clause 4.2.2.9.3.

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a Cell; 1280 ms is assumed in this test case.

This gives a total of 16.64 s, allow 17 s for the cell re-selection delay to an already detected cell for UE fulfilling not-at-cell edge criterion in the test case.

## A.6.1.1.5Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion

## A.6.1.1.5.1Test Purpose and Environment

This test is to verify the requirement for the inter-frequency NR cell reselection requirements specified in clause 4.2.2.10.2, for UE fulfilling low mobility relaxed measurement criterion.

## A.6.1.1.5.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.6.1.1.5.2-1, A.6.1.1.5.2-2 and A.6.1.1.5.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

As specified in the Test Purpose, the UE is configured with the relaxed measurement criterion for UE with low mobility defined in clause 5.2.4.9.1 in [1]. So, Cell 2 and Cell 1 configure the UE as follows:

lowMobilityEvalutation [2] criterion is configured according to the parameters listed in table A.6.1.1.5.2-3;

cellEdgeEvaluation [2] criterion is not configured;

combineRelaxedMeasCondition [2] is not configured;

Table A.6.1.1.5.2-1: Supported test configurations

Table A.6.1.1.5.2-2: General test parameters for FR1 inter-frequency NR cell re-selection test case for UE fulfilling low mobility criterion

Table A.6.1.1.5.2-3: Cell specific test parameters for FR1 inter-frequency NR cell re-selection test case in AWGN for UE fulfilling low mobility criterion

## A.6.1.1.5.3Test Requirements

The cell reselection delay to an already detected lower priority cell for UE fulfilling low mobility relaxed measurements is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to a lower priority cell for UE fulfilling low mobility relaxed measurements shall be less than 17 s.

The cell reselection delay to an already detected higher priority cell for UE fulfilling low mobility relaxed measurements is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected higher priority cell for UE fulfilling low mobility relaxed measurements shall be less than 17 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a known lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Tevaluate, NR_ interSee table 4.2.2.10.2-1 in clause 4.2.2.10.2

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 16.64 s, allow 17 s  for the cell re-selection delay to an already detected lower priority cell and 16.64 s for the cell re-selection delay to an already detected higher priority cell, which we allow 17 s for UE fulfilling low mobility relaxed measurements in the test case.

## A.6.1.1.6Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion

## A.6.1.1.6.1Test Purpose and Environment

This test is to verify the requirement for the inter-frequency NR cell reselection requirements specified in clause 4.2.2.10.3, for UE fulfilling not-at-cell edge relaxed measurement criterion.

## A.6.1.1.6.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.6.1.1.6.2-1, A.6.1.1.6.2-2 and A.6.1.1.6.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

As specified in the Test Purpose, the UE is configured with the relaxed measurement criterion for UE not-at-cell edge as defined in clause 5.2.4.9.2 in TS 38.304 [1]. So, Cell 2 and Cell 1configures the UE as follows:

cellEdgeEvaluation [2] criterion is configured according to the parameters listed in table A.6.1.1.5.2-3;

lowMobilityEvalutation [2] criterion is not configured;

combineRelaxedMeasCondition [2] is not configured;

Table A.6.1.1.6.2-1: Supported test configurations

Table A.6.1.1.6.2-2: General test parameters for FR1 inter-frequency NR cell re-selection test case for UE fulfilling not-at-cell edge criterion

Table A.6.1.1.6.2-3: Cell specific test parameters for FR1 inter-frequency NR cell re-selection test case in AWGN for UE fulfilling not-at-cell edge criterion

## A.6.1.1.6.3Test Requirements

The cell reselection delay to an already detected lower priority cell for UE fulfilling not-at-cell edge relaxed measurements is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected lower priority cell for UE fulfilling not-at-cell edge relaxed measurements shall be less than 17 s.

The cell reselection delay to an already detected higher priority cell for UE fulfilling not-at-cell-edge relaxed measurements is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to an already detected higher priority cell for UE fulfilling not-at-cell-edge  relaxed measurements shall be less than 17 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, NR_ inter + TSI-NR,

Where:

Tevaluate, NR_ interSee table 4.2.2.10.3-1 in clause 4.2.2.10

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 16.64 s , allow 17 s for the cell re-selection delay to an already detected lower priority cell and 16.64 s for the cell re-selection delay to an already higher priority cell, which we allow 17 s  for UE fulfilling not-at-cell edge relaxed measurements in the test case.

## A.6.1.1.7Cell reselection to FR1 intra-frequency NR case for UE configured with highSpeedMeasFlag-r16

## A.6.1.1.7.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell reselection requirements for UE configured with highSpeedMeasFlag-r16 specified in clause 4.2.2.3.

## A.6.1.1.7.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.6.1.1.7.2-1, A.6.1.1.7.2-2 and A.6.1.1.7.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. highSpeedMeasFlag-r16 is broadcasted to UE.

Table A.6.1.1.7.2-1: Supported test configurations

Table A.6.1.1.7.2-2: General test parameters for intra-frequency NR cell re-selection test case for UE configured with highSpeedMeasFlag-r16

Table A.6.1.1.7.2-3: Cell specific test parameters for intra-frequency NR cell re-selection test case for UE configured with highSpeedMeasFlag-r16

## A.6.1.1.7.3Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 4 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 3 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_IntraSee table 4.2.2.3-2 in clause 4.2.2.3

Tevaluate, NR_ intraSee table 4.2.2.3-2 in clause 4.2.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 3.84 s, allow 4 s for the cell re-selection delay to a newly detectable cell and 2.24 s for the cell re-selection delay to an already detected cell in the test case, which we allow 3 s.

## A.6.1.1.8Cell reselection to FR1 inter-frequency NR case for UE configured with highSpeedMeasInterFreq-r17

## A.6.1.1.8.1Test Purpose and Environment

This test is to verify the requirement for the inter-frequency NR cell reselection requirements for UE configured with highSpeedMeasInterFreq-r17 specified in clause 4.2.2.4.

## A.6.1.1.8.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.6.1.1.8.2-1, A.6.1.1.8.2-2 and A.6.1.1.8.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas and Cell 2 is of higher priority than Cell 1.

Table A.6.1.1.8.2-1: Supported test configurations

Table A.6.1.1.8.2-2: General test parameters for FR1 inter-frequency NR cell re-selection test case

Table A.6.1.1.8.2-3: Cell specific test parameters for FR1 inter-frequency NR cell re-selection test case in AWGN

## A.6.1.1.8.3Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 5 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 3 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect,NR_Inter_HST + TSI-NR, and to an already detected cell can be expressed as: Tevaluate,NR_Inter_HST + TSI-NR,

Where:

Tdetect,NR_Inter_HST See table 4.2.2.4-2 in clause 4.2.2.4

Tevaluate,NR_Inter_HST See table 4.2.2.4-2 in clause 4.2.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 4.48 s, allow 5 s for the cell re-selection delay to a newly detectable cell and 2.24 s for the cell re-selection delay to an already detected cell in the test case, which we allow 3 s.

## A.6.1.1.9Cell reselection to FR1 intra-frequency NR case for UE operating on a cell with less than 5 MHz BW

## A.6.1.1.9.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell reselection requirements specified in clause 4.2.2.3. for UE capable of operating on a cell with less than 5 MHz BW.

## A.6.1.1.9.2Test Parameters

Supported test configurations are specified in table A.6.1.1.9.2-1. General test parameters as specified in table A.6.1.1.1.2-2 with config 1 apply except those specified in table A.6.1.1.9.2-2. Cell specific test parameters as specified in table A.6.1.1.1.2-3 with config 1 apply except those specified in table A.6.1.1.9.2-3. The test procedure specified in clause A.6.1.1.1.2 applies to this test.

Table A.6.1.1.9.2-1: Supported test configurations

Table A.6.1.1.9.2-2: General test parameters for intra-frequency NR cell re-selection test case

Table A.6.1.1.9.2-3: Cell specific test parameters for intra-frequency NR cell re-selection test case

## A.6.1.1.9.3Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s for UE operating on a cell with less than 5 MHz BW.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 8 s for UE operating on a cell with less than 5 MHz BW.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_Intra + 40 ms See table 4.2.2.3-1 in clause 4.2.2.3

Tevaluate, NR_ intra See table 4.2.2.3-1 in clause 4.2.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1320 ms is assumed in this test case.

This gives a total of 33.32 s, allow 34 s for the cell re-selection delay to a newly detectable cell and 7.72 s for the cell re-selection delay to an already detected cell in the test case, which we allow 8 s.

## A.6.1.1.10Cell reselection to FR1 intra-frequency NR cell supporting OD-SIB1

## A.6.1.1.10.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell reselection requirements specified in clause 4.2.2.3.

## A.6.1.1.10.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.6.1.1.10.2-1, A.6.1.1.10.2-2 and A.6.1.1.10.2-3. The test consists of one time period with time duration of T1. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. Cell2 is an NES Cell with OD-SIB1, and OD-SIB1-Config of Cell2 is provided in SIB26 of Cell1.

Table A.6.1.1.10.2-1: Supported test configurations

Table A.6.1.1.10.2-2: General test parameters for intra-frequency NR cell re-selection test case

Table A.6.1.1.10.2-3: Cell specific test parameters for intra-frequency NR cell re-selection test case in AWGN

## A.6.1.1.10.3Test Requirements

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on cell 2.

The cell re-selection delay to an already detected cell shall be less than Tevaluate, NR_Intra + TSI-NR + TOD-SIB1.

Tevaluate, NR_IntraSee table 4.2.2.3-1 in clause 4.2.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

TOD-SIB1 is the time for OD-SIB1 acuqisition, whichi is assumed to be [1] second in the test case.

This gives a total of 8.68 s for the cell re-selection delay to an already detected cell in the test case.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

## A.6.1.1.11Cell reselection to FR1 inter-frequency NR cell supporting OD-SIB1

## A.6.1.1.11.1Test Purpose and Environment

This test is to verify the requirement for the inter-frequency NR cell reselection requirements specified in clause 4.2.2.3.

## A.6.1.1.11.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.6.1.1.11.2-1, A.6.1.1.11.2-2 and A.6.1.1.11.2-3. The test consists of one time period with time duration of T1. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. Cell2 is an NES Cell with OD-SIB1, and OD-SIB1-Config of Cell2 is provided in SIB26 of Cell1.

Table A.6.1.1.11.2-1: Supported test configurations

Table A.6.1.1.11.2-2: General test parameters for inter-frequency NR cell re-selection test case

Table A.6.1.1.11.2-3: Cell specific test parameters for inter-frequency NR cell re-selection test case in AWGN

## A.6.1.1.11.3Test Requirements

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on cell 2.

The cell re-selection delay to an already detected cell shall be less than Tevaluate, NR_Inter + TSI-NR + TOD-SIB1.

Tevaluate, NR_InterSee table 4.2.2.4-1 in clause 4.2.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

TOD-SIB1 is the time for OD-SIB1 acuqisition, whichi is assumed to be [1] second in the test case.

This gives a total of 8.68 s for the cell re-selection delay to an already detected cell in the test case.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

## A.6.1.2Inter-RAT E-UTRAN cell re-selection

## A.6.1.2.1Cell reselection to higher priority E-UTRAN

## A.6.1.2.1.1Test Purpose and Environment

This test is to verify the requirement for the NR to E-UTRAN inter-RAT cell reselection requirements specified in clause 4.2.2.5 when the E-UTRAN cell is of higher priority.

## A.6.1.2.1.2Test Parameters

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A.6.1.2.1.2-1, A.6.1.2.1.2-2, A.6.1.2.1.2-3 and A.6.1.2.1.2-4. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. NR Cell 1 is already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of higher priority than Cell 1.

Table A.6.1.2.1.2-1: Supported test configurations

Table A.6.1.2.1.2-2: General test parameters for NR to E-UTRAN cell re-selection test case

Table A.6.1.2.1.2-3: Cell specific test parameters for NR Cell 1

Table A.6.1.2.1.2-4: Cell specific test parameters for E-UTRA Cell 2

## A.6.1.2.1.3Test Requirements

The cell reselection delay to a higher priority E-UTRAN cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, E-UTRAN + TSI-E-UTRA,

Where:

Thigher_priority_searchSee clause 4.2.2.7

Tevaluate, E-UTRANSee table 4.2.2.5-1 in clause 4.2.2.5

TSI-E-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority E-UTRAN cell.

## A.6.1.2.2Cell reselection to lower priority E-UTRAN

## A.6.1.2.2.1Test Purpose and Environment

This test is to verify the requirement for the NR to E-UTRAN inter-RAT cell reselection requirements specified in clause 4.2.2.5 when the E-UTRAN cell is of lower priority.

## A.6.1.2.2.2Test Parameters

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A.6.1.2.2.2-1, A.6.1.2.2.2-2, A.6.1.2.2.2-3 and A.6.1.2.2.2-4. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both NR Cell 1 and E-UTRAN Cell 2 are already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of lower priority than Cell 1.

Table A.6.1.2.2.2-1: Supported test configurations

Table A.6.1.2.2.2-2: General test parameters for NR to E-UTRAN cell re-selection test case

Table A.6.1.2.2.2-3: Cell specific test parameters for NR Cell 1

Table A.6.1.2.2.2-4: Cell specific test parameters for E-UTRA Cell 2

## A.6.1.2.2.3Test Requirements

The cell reselection delay to a lower priority E-UTRAN cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a lower priority cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, E-UTRAN + TSI-E-UTRA,

Where:

Tevaluate, E-UTRANSee table 4.2.2.5-1 in clause 4.2.2.5

TSI-E-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 7.68 s, allow 8 s for the cell re-selection delay to a lower priority E-UTRAN cell.

## A.6.1.2.3Cell reselection to lower priority E-UTRAN for UE fulfilling low mobility relaxed measurement criterion

## A.6.1.2.3.1Test Purpose and Environment

This test is to verify the requirement for the NR to E-UTRAN inter-RAT cell reselection when UE fulfills the low mobility criterion specified in clause 4.2.2.11.2 and the E-UTRAN cell is of lower priority.

## A.6.1.2.3.2Test Parameters

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A.6.1.2.3.2-1, A.6.1.2.3.2-2, A.6.1.2.3.2-3 and A.6.1.2.3.2-4. The test consists of two successive time periods, with time duration of T1 and T2, respectively. Both NR Cell 1 and E-UTRAN Cell 2 are already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of lower priority than Cell 1.

As specified in the test purpose, the UE is configured with the relaxed measurement criterion for UE with low mobility defined in clause 5.2.4.9.1 in TS 38.304 [1]. So, Cell 1 configures the UE as follows:

-lowMobilityEvalutation [2] criterion is configured according to the parameters listed in table A.6.1.2.3.2-3;

-cellEdgeEvaluation [2] criterion is not configured;

-combineRelaxedMeasCondition [2] is not configured

Table A.6.1.2.3.2-1: Supported test configurations

Table A.6.1.2.3.2-2: General test parameters for NR to E-UTRAN cell re-selection test case for UE fulfilling low mobility criterion

Table A.6.1.2.3.2-3: Cell specific test parameters for NR Cell 1

Table A.6.1.2.3.2-4: Cell specific test parameters for E-UTRA Cell 2

## A.6.1.2.3.3Test Requirements

The cell reselection delay to a lower priority E-UTRAN cell with UE fulfilling low mobility criterion is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCConnectionRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a lower priority cell shall be less than 17  s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, E-UTRAN + TSI-E-UTRA,

Where:

Tevaluate, E-UTRANSee table 4.2.2.11.2-1 in clause 4.2.2.11.2

TSI-E-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 15.36 (Tevaluate, E-UTRAN) + 1.28 (TSI-E-UTRA) = 16.64 s, allow 17 s for the cell re-selection delay to a lower priority E-UTRAN cell for UE fulfilling low mobility criterion.

## A.6.1.2.4Cell reselection to lower priority E-UTRAN for UE fulfilling not-at-cell edge relaxed measurement criterion

## A.6.1.2.4.1Test Purpose and Environment

This test is to verify the requirement for the NR to E-UTRAN inter-RAT cell reselection requirements when UE fulfills  not-at-cell edge criterion specified in clause 4.2.2.11.3 when the E-UTRAN cell is of lower priority.

## A.6.1.2.4.2Test Parameters

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A.6.1.2.4.2-1, A.6.1.2.4.2-2, A.6.1.2.4.2-3 and A.6.1.2.4.2-4. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both NR Cell 1 and E-UTRAN Cell 2 are already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of lower priority than Cell 1.

As specified in the Test Purpose, the UE is configured with the relaxed measurement criterion for UE with not-at-cell edge defined in clause 5.2.4.9.2 in [1]. So, Cell 1 configures the UE as follows:

-lowMobilityEvalutation [2] criterion is not configured;

-cellEdgeEvaluation [2] criterion is configured according to the parameters listed in table A.6.1.2.4.2-3;

-combineRelaxedMeasCondition [2] is not configured

Table A.6.1.2.4.2-1: Supported test configurations

Table A.6.1.2.4.2-2: General test parameters for NR to E-UTRAN cell re-selection test case for UE fulfilling not-at-cell edge criterion

Table A.6.1.2.4.2-3: Cell specific test parameters for NR Cell 1

Table A.6.1.2.4.2-4: Cell specific test parameters for E-UTRA Cell 2

## A.6.1.2.4.3Test Requirements

The cell reselection delay to a lower priority E-UTRAN cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCConnectionRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a lower priority cell shall be less than 17 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, E-UTRAN + TSI-E-UTRA,

Where:

Tevaluate, E-UTRANSee table 4.2.2.11.3-1 in clause 4.2.2.11.3

TSI-E-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 16.64 s, allow 17 s for the cell re-selection delay to a lower priority E-UTRAN cell for UE fulfilling not-at-cell edge criterion.

## A.6.1.2.5Cell reselection to lower priority E-UTRAN cell for UE configured with highSpeedMeasFlag-r16

## A.6.1.2.5.1Test Purpose and Environment

This test is to verify the requirement for the NR to E-UTRAN inter-RAT cell reselection requirements for UE configured with highSpeedMeasFlag-r16 specified in clause 4.2.2.5 when the E-UTRAN cell is of lower priority.

## A.6.1.2.5.2Test Parameters

The test scenario comprises of one NR cell and one E-UTRAN cell as given in tables A.6.1.2.5.2-1, A.6.1.2.5.2-2, A.6.1.2.5.2-3 and A.6.1.2.5.2-4. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both NR Cell 1 and E-UTRAN Cell 2 are already identified by the UE prior to the start of the test. E-UTRAN Cell 2 is of lower priority than Cell 1. The E-UTRAN Cell 2 is indicated by NR Cell 1 as an HST cell.

Table A.6.1.2.5.2-1: Supported test configurations

Table A.6.1.2.5.2-2: General test parameters for NR to E-UTRAN cell re-selection test case

Table A.6.1.2.5.2-3: Cell specific test parameters for NR Cell 1

Table A.6.1.2.5.2-4: Cell specific test parameters for E-UTRA Cell 2

## A.6.1.2.5.3Test Requirements

The cell reselection delay to a lower priority E-UTRAN cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The cell re-selection delay to a lower priority cell shall be less than 3 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, E-UTRAN_HST + TSI-E-UTRA,

Where:

Tevaluate, E-UTRAN_HSTSee table 4.2.2.5-2 in clause 4.2.2.5

TSI-E-UTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 2.24 s, allow 3 s for the cell re-selection delay to a lower priority E-UTRAN cell.

## A.6.1.1.7Void

## A.6.2SA: RRC_INACTIVE state mobility

## A.6.2.1Configured Grant based Small Data Transmissions (CG-SDT)

## A.6.2.1.1Test purpose and Environment

The purpose of this test is to partly verify that the UE properly perform TA validation for CG-SDT transmission in clause 5.5.3. The test includes two sub-tests, Sub-test#1 for testing valid TA where UE can initiat CG-SDT transmission, and Sub-test#2 for testing invalid TA where UE does not initiate CG-SDT transmission. Subtest#2 is only tested if Sub-test#1 is passed. For each sub-test, UE is configured with CG-SDT configurations when entering RRC Inactive state. Sub-test#1 consists of four successive time periods, with time duration of T1, T2, T3 and T4 repectively. Sub-test#2 consists of two successive time periods, with time duration of T5 and T6 repectively. There is one cell, which is the active NR cell in FR1. Figure A.6.2.1.1-1 shows the variation of the RSRP over the duration of Sub-test#1, and figure A.6.2.1.1-2 shows the variation of the RSRP over the duration of Sub-test#2.

In Sub-test#1:

-Prior to the time point TA, the UE shall be fully synchronized to PCell (Cell 1), be registered to the cell and have entered RRC connected mode.

-At time point TB, RSRP is changed from P0 to P1.

-At time point TC, which is W1 after time point TB, UE expect to receive RRC release with CG SDT configuration and RRC status is changed to INACTIVE status.

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

W1 equals to 640 ms and W2 equals to 640 ms based on requirements in clause 5.5.3. W3 is 860 ms.

Figure A.6.2.1.1-1: RSRP variation model for CG-SDT Sub-test#1.

Figure A.6.2.1.1-2: RSRP variation model for CG-SDT Sub-test#2.

## A.6.2.1.2Test Parameters

There is one cells in the test, the FR1 PCell. The test parameters for the PCell are given in table A.6.2.1.2-1, table A.6.2.1.2-2, and table A.6.2.1.2-3.

Table A.6.2.1.2-1: NR configuration for FR1 SSB

Table A.6.2.1.2-2 : General test parameters

Table A.6.2.1.2-3: SSB specific test parameters

## A.6.2.1.3Test requirements

The UE behaviour in each test during time durations shall be as follows:

During Sub-test#1, UE shall transmit PUSCH at CG-SDT resource within 860 ms after time point TF.

During Sub-test#2, after passing Sub-test#1, UE shall not transmit PUSCH at CG-SDT resources after TF until the end of the test at time point TG.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.2.2Cell reselection for positioning

## A.6.2.2.1Cell reselection to FR1 intra-frequency NR case with RRC_ INACTIVE eDRX and positioning SRS

## A.6.2.2.1.1Test Purpose and Environment

This test is to verify the requirement for the intra-frequency NR cell reselection requirements specified in clause 5.6.1A.2, when UE is in RRC_INACTIVE and configured with eDRX and to transmit SRS for positioning.

## A.6.2.2.1.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.6.2.2.1.2-1, A.6.2.2.1.2-2 and A.6.2.2.1.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2. UE is configured with transmit SRS for positioning in Cell 1.

Table A.6.2.2.1.2-1: Supported test configurations

Table A.6.2.2.1.2-2: General test parameters for intra frequency NR cell re-selection test case

Table A.6.2.2.1.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case in AWGN

## A.6.2.2.1.3Test Requirements

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 119 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90%.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra + TSI-NR,

Where:

Tdetect, NR_IntraSee table 5.6.1A.2-1 in clause 5.6.1A.2

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280ms is assumed in this test case.

This gives a total of 119.04 s, allow 120 s for the cell re-selection delay to a newly detectable cell.

## A.6.3RRC_CONNECTED state mobility

## A.6.3.1Handover

## A.6.3.1.1Intra-frequency handover from FR1 to FR1; known target cell

## A.6.3.1.1.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-frequency handover requirements specified in clause 6.1.1.2.

## A.6.3.1.1.2Test Parameters

Supported test configurations are shown in table A.6.3.1.1.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.1.2-2, and A.6.3.1.1.2-3.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

NR shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

Table A.6.3.1.1.2-1: Intra-frequency handover from FR1 to FR1 test configurations

Table A.6.3.1.1.2-2: General test parameters Intra-frequency handover from FR1 to FR1

Table A.6.3.1.1.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency handover test case

## A.6.3.1.1.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 62 ms in the test. Tinterrupt is defined in clause 6.1.1.2.2.

This gives a total of 72 ms.

## A.6.3.1.2Intra-frequency handover from FR1 to FR1; unknown target cell

## A.6.3.1.2.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-frequency handover requirements specified in clause 6.1.1.2.

## A.6.3.1.2.2Test Parameters

Supported test configurations are shown in table A.6.3.1.2.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.2.2-2, and A.6.3.1.2.2-3.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2, respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.6.3.1.2.2-1: Intra-frequency handover from FR1 to FR1 test configurations

Table A.6.3.1.2.2-2: General test parameters Intra-frequency handover from FR1 to FR1

Table A.6.3.1.2.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency handover test case

## A.6.3.1.2.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 92 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 82 ms in the test. Tinterrupt is defined in clause 6.1.1.2.2.

This gives a total of 92 ms.

## A.6.3.1.3Inter-frequency handover from FR1 to FR1; unknown target cell

## A.6.3.1.3.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 inter-frequency handover requirements specified in clause 6.1.1.2.

## A.6.3.1.3.2Test Parameters

Supported test configurations are shown in table A.6.3.1.3.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.3.2-2, and A.6.3.1.3.2-3.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.6.3.1.3.2-1: Inter-frequency handover from FR1 to FR1 test configurations

Table A.6.3.1.3.2-2: General test parameters Inter-frequency handover from FR1 to FR1

Table A.6.3.1.3.2-3: Cell specific test parameters for NR FR1-FR1 Inter-frequency handover test case

## A.6.3.1.3.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 132 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 122 ms in the test. Tinterrupt is defined in clause 6.1.1.2.2.

This gives a total of 132 ms.

## A.6.3.1.4SA NR - E-UTRAN handover

## A.6.3.1.4.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE can make correct inter-RAT E-UTRAN handover when operating in standalone (SA) operation with PCell in FR1. This test shall verify the NR to E-UTRAN handover requirements as specified in clause 6.1.2.1.

The test comprises of one NR carrier and one E-UTRA carrier. There are two cells and one cell on each carrier. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in table 9.1.2-1 is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2 after the UE has reported Event B2. The start of T3 is the next instant after the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.6.3.1.4-1. General test parameters are provided in table A.6.3.1.4-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.6.3.1.4-3 and A.6.3.1.4-4 respectively.

Table A.6.3.1.4-1: Supported test configurations for SA inter-RAT E-UTRAN handover tests

Table A.6.3.1.4-2: General test parameters for SA inter-RAT E-UTRAN handover

Table A.6.3.1.4-3: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 1)

Table A.6.3.1.4-4: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 2)

## A.6.3.1.4.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 85 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and is specified in clause 6.1.2.1.

Tinterrupt = 35 ms in the test; Tinterrupt is defined in clause 6.1.2.1.

This gives a total of 85 ms.

## A.6.3.1.5SA NR - E-UTRAN handover with unknown target cell

## A.6.3.1.5.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE can make correct inter-RAT E-UTRAN handover when operating in standalone (SA) operation with PCell in FR1. This test shall verify the NR to E-UTRAN handover requirements for the case when the target E-UTRAN cell is unknown as specified in clause 6.1.2.1.

The test comprises of one NR carrier and one E-UTRA carrier. There are two cells and one cell on each carrier. Cell 1 is the NR PCell and Cell 2 is an inter-RAT E-UTRAN neighbour cell. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable. No gap pattern shall be configured.

A RRC message implying handover shall be sent to the UE during period T1. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.6.3.1.5-1. General test parameters are provided in table A.6.3.1.5-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.6.3.1.5-3 and A.6.3.1.5-4 respectively.

Table A.6.3.1.5-1: Supported test configurations for SA inter-RAT E-UTRAN handover tests

Table A.6.3.1.5-2: General test parameters for SA inter-RAT E-UTRAN handover

Table A.6.3.1.5-3: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 1)

Table A.6.3.1.5-4: Cell specific test parameters for SA inter-RAT E-UTRA handover (Cell 2)

## A.6.3.1.5.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 165 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and is specified in clause 6.1.2.1.

Tinterrupt = 115 ms in the test; Tinterrupt is defined in clause 6.1.2.1.

This gives a total of 165 ms.

## A.6.3.1.6 SA NR - UTRAN FDD handover

## A.6.3.1.6.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE can make correct inter-RAT UTRAN FDD handover when operating in standalone (SA) operation with PCell in FR1. This test shall verify the NR to UTRAN FDD handover requirements as specified in clause 6.1.2.2.1.

The test comprises of one NR carrier and one UTRA FDD carrier. There are two cells and one cell on each carrier. Cell 1 is the NR PCell and Cell 2 is an inter-RAT UTRAN FDD neighbour cell. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in table 9.1.2-1 is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2 after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.6.3.1.6-1. General test parameters are provided in table A.6.3.1.6-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.6.3.1.6-3 and A.6.3.1.6-4 respectively.

Table A.6.3.1.6-1: Supported test configurations for SA inter-RAT UTRAN FDD handover tests

Table A.6.3.1.6-2: General test parameters for SA inter-RAT UTRAN FDD handover

Table A.6.3.1.6-3: Cell specific test parameters for SA inter-RAT UTRAN FDD handover (Cell 1)

Table A.6.3.1.6-4: Cell specific test parameters for SA inter-RAT UTRAN FDD handover (Cell 2)

## A.6.3.1.6.2Test Requirements

The UE shall start to transmit the UL DPCCH to Cell 2 less than 190 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms, which is specified in clause 5.3.1.1.1.

Tinterrupt = 140 ms in the test; Tinterrupt is defined in clause 5.3.1.1.2. This gives a total of 190 ms.

## A.6.3.1.7Intra-frequency synchronous DAPS handover in FR1

## A.6.3.1.7.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-frequency DAPS handover requirements in synchronous scenario specified in clause 6.1.3.2.

## A.6.3.1.7.2Test Parameters

Supported test configurations are shown in table A.6.3.1.7.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.7.2-2, and A.6.3.1.7.2-3.The test consists of five successive time periods, with time durations of T1, T2, T3, T4, and T5 respectively.

Before the start of T1, the UE is connected to the cell1 and not aware of the cell2. The UE shall be configured with periodic CSI reporting for cell1. During T1, the UE does not have any timing information of the cell2.

Starting T2, the cell2 becomes detectable. During T2, the UE performs cell detection and measurements on the cell2 and shall send event report to the network. After receiving the event report A3, the network sends a RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the last TTI containing DAPS handover command is sent to the UE. During T3, UE shall be able to perform random access, DL reception or UL transmission in the cell2 while the DL scheduling and UL feedback in the cell1 shall be avoided. After successful RACH procedure of the cell2, UE is scheduled with PDSCH from cell1 and cell2 in alternative TTIs where both cell1 and cell2 belong to the same TAG. In the end the network sends a RRC message implying cell1 release to the UE. During T3, the handover delay Dhandover1 for target cell addition need to be verified.

The start of T4 is the instant when the last TTI containing cell1 release command is sent to the UE. During T4, the UE shall accomplish the release actions within Dhandover2.

Starting T5, the UE stops sending the periodical CSI report to the cell1.

Table A.6.3.1.7.2-1: Intra-frequency DAPS handover in FR1 test configurations

Table A.6.3.1.7.2-2: General test parameters synchronous Intra-frequency DAPS handover in FR1

Table A.6.3.1.7.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency DAPS handover test case

## A.6.3.1.7.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The target cell add delay Dhandover1 can be expressed as: TRRC_procedure + Tsearch + TIU + Tprocessing + T∆ + Tmargin, where:

TRRC_procedure  = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tsearch, TIU, Tprocessing, T∆ and Tmargin are defined in clause 6.1.1.2.2.

If the target cell is known, then Tsearch = 0 ms

TIU = 20 ms in the test. TIU is defined in clause 6.1.1.2.2.

T∆ = 20 ms in the test. T∆ is defined in clause 6.1.1.2.2.

Tprocessing = 20 ms in the test. Tprocessing is defined in clause 6.1.1.2.2.

Tmargin = 2 ms in the test. Tmargin is defined in clause 6.1.1.2.2.

This gives a total of 72 ms.

After successful RACH to Cell 2 and until the start of time period T4, UE shall be able to receive PDSCH alternatively from Cell 1 and Cell 2. UE is not expected to transmit UL to both Cell 1 and Cell 2 in the same TTI.

The UE shall release Cell 1 less than Dhandover2 = (TRRC_procedure + Tinterrupt2) from the beginning of time period T4.

NOTE:Dhandover2 is defined in clause 6.1.3.2.1.

TRRC_procedure  = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt2 is defined in clause 6.1.3.2.2.

UE shall not report CSI to Cell 1 during T5.

## A.6.3.1.8Intra-frequency asynchronous DAPS handover in FR1

## A.6.3.1.8.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-frequency DAPS handover requirements in asynchronous scenario specified in clause 6.1.3.2.

## A.6.3.1.8.2Test Parameters

Supported test configurations are shown in table A.6.3.1.8.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.8.2-2, and A.6.3.1.8.2-3.

The test consists of five successive time periods, with time durations of T1, T2, T3, T4, and T5 respectively.

Before the start of T1, the UE is connected to the cell1 and not aware of the cell2. The UE shall be configured with periodic CSI reporting for cell1. During T1, the UE does not have any timing information of the cell2.

Starting T2, the cell2 becomes detectable. During T2, the UE performs cell detection and measurements on the cell2 and shall send event report to the network. After receiving the event report A3, the network sends a RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the last TTI containing DAPS handover command is sent to the UE. During T3, UE shall be able to perform random access, DL reception or UL transmission in the cell2 while the DL scheduling and UL feedback in the cell1 shall be avoided. After successful RACH procedure of the cell2, UE is scheduled with PDSCH from cell1 and cell2 in alternative TTIs where both cell1 and cell2 belong to the same TAG. In the end the network sends a RRC message implying cell1 release to the UE. During T3, the handover delay Dhandover1 for target cell addition needs to be verified.

The start of T4 is the instant when the last TTI containing cell1 release command is sent to the UE by cell2. During T4, the UE shall accomplish the release actions within Dhandover2.

Starting T5, the UE stops sending the periodical CSI report to the cell1.

Table A.6.3.1.8.2-1: Intra-frequency DAPS handover in FR1 test configurations

Table A.6.3.1.8.2-2: General test parameters Intra-frequency asynchronous DAPS handover in FR1

Table A.6.3.1.8.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency DAPS handover test case

## A.6.3.1.8.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The target cell add delay Dhandover1 can be expressed as: TRRC_procedure + Tsearch + TIU + Tprocessing + T∆ + Tmargin, where:

TRRC_procedure  = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tsearch, TIU, Tprocessing, T∆ and Tmargin are defined in clause 6.1.1.2.2.

If the target cell is known, then Tsearch = 0 ms

TIU = 20 ms in the test. TIU is defined in clause 6.1.1.2.2.

T∆ = 20 ms in the test. T∆ is defined in clause 6.1.1.2.2.

Tprocessing = 20 ms in the test. Tprocessing is defined in clause 6.1.1.2.2.

Tmargin = 2 ms in the test. Tmargin is defined in clause 6.1.1.2.2.

This gives a total of 72 ms.

After successful RACH to Cell 2 and until the start of time period T4, UE shall be able to receive PDSCH alternatively from Cell 1 and Cell 2. UE is not expected to transmit UL to both Cell 1 and Cell 2 in the same TTI.

The UE shall release Cell 1 less than Dhandover2 = (TRRC_procedure + Tinterrupt2) from the beginning of time period T4.

NOTE:Dhandover2 is defined in clause 6.1.3.2.1.

TRRC_procedure  = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt2 is defined in clause 6.1.3.2.2.

UE shall not report CSI to Cell 1 during T5.

## A.6.3.1.9Intra-band inter-frequency synchronous DAPS handover test in SA for FR1

## A.6.3.1.9.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-band inter-frequency synchronous DAPS handover requirements specified in clause 6.1.3.2.

## A.6.3.1.9.2Test Parameters

Supported test configurations are shown in table A.6.3.1.9.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.9.2-2, and A.6.3.1.9.2-3.

The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. The UE shall be configured with periodic CSI reporting for cell1. The test scenario comprises of two carriers and one cell on each carrier. Gap pattern with ID 0 as specified in table 9.1.2-1 is configured before T2 in the test case.

Starting T2, Cell 2 becomes known to the UE. During T2, the UE shall report Event A3. After receiving the Event A3, the test system shall send a RRC message implying DAPS handover to the UE.

T3 is defined as the end of the last TTI containing the RRC message implying DAPS handover. During T3 UE shall be able to perform random access to Cell 2. Cell 1 is continuously scheduled in DL during T3. DL schedule and UL feedback to Cell 1 shall be avoided when UE is required to perform DL reception or UL transmission in PRACH procedure in Cell 2, except preamble transmission. At the end of T3 Cell 2 shall send an RRC message implying Cell 1 release command.

T4 is defined as the end of the last TTI containing the RRC message implying DAPS handover. Cell 2 is continuously scheduled in DL during T4. During T4, the UE shall perform source cell release.

Starting T5, the UE shall stop sending CSI report to the source cell. And the test system shall observe the periodic reporting of CSI for Cell 1 during T5.

Table A.6.3.1.9.2-1: Intra-band inter-frequency synchronous DAPS handover in SA for FR1 test configurations

Table A.6.3.1.9.2-2: General test parameters for intra-band inter-frequency synchronous DAPS  handover test in SA for FR1

Table A.6.3.1.9.2-3: Cell specific test parameters for intra-band inter-frequency synchronous DAPS handover test in SA for FR1

## A.6.3.1.9.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T3.

During T3 UE is allowed to cause Tinterrupt1 interruption to Cell 1. Tinterrupt1 is defined in clause 6.1.3.2.2 table 6.1.3.2.2-2. When UE is transmitting PRACH preamble to Cell 2, interruption to Cell 1 is allowed.

During T4 UE is allowed to cause Tinterrupt2 interruption to Cell 1. Tinterrupt2 is defined in clause 6.1.3.2.2 table 6.1.3.2.2-5.

UE shall finish Cell 1 release in T4 and shall not send any CSI reports to Cell 1 during T5.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

## A.6.3.1.10Intra-band inter-frequency asynchronous DAPS handover test in SA for FR1

## A.6.3.1.10.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-band inter-frequency asynchronous DAPS handover requirements specified in clause 6.1.3.2.

## A.6.3.1.10.2Test Parameters

Supported test configurations are shown in table A.6.3.1.10.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.10.2-2, and A.6.3.1.10.2-3.

The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. The UE shall be configured with periodic CSI reporting for cell1. The test scenario comprises of two carriers and one cell on each carrier. Gap pattern ID gp0 as specified in table 9.1.2-1 is configured before T2 in the test case.

Starting T2, Cell 2 becomes known to the UE. During T2, the UE shall report Event A3. After receiving the Event A3, the test system shall send a RRC message implying DAPS handover to the UE.

T3 is defined as the end of the last TTI containing the RRC message implying DAPS handover.During T3 UE shall be able to perform random access to Cell 2. Cell 1 is continuously scheduled in DL during T3. DL schedule and UL feedback to Cell 1 shall be avoided when UE is required to perfrom DL reception or UL transmission in PRACH procedure in Cell 2, except preamble transmission. At the end of T3 Cell 2 shall send an RRC message implying Cell 1 release command.

T4 is defined as the end of the last TTI containing the RRC message implying DAPS handover. Cell 2 is continuously scheduled in DL during T4. During T4, the UE shall perform source cell release.

Starting T5, the UE shall stop sending CSI report to the source cell. And the test system shall observe the periodic reporting of CSI for Cell 1 during T5.

Table A.6.3.1.10.2-1: Intra-band inter-frequency asynchronous DAPS handover in SA for FR1 test configurations

Table A.6.3.1.10.2-2: General test parameters for intra-band inter-frequency asynchronous DAPS  handover test in SA for FR1

Table A.6.3.1.10.2-3: Cell specific test parameters for intra-band inter-frequency asynchronous DAPS  handover test in SA for FR1

## A.6.3.1.10.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T3.

During T3 UE is allowed to cause Tinterrupt1 interruption to Cell 1. Tinterrupt1 is defined in clause 6.1.3.2.2 table 6.1.3.2.2-2. When UE is transmitting PRACH preamble to Cell 2, interruption to Cell 1 is allowed.

During T4 UE is allowed to cause Tinterrupt2 interruption to Cell 1. Tinterrupt2 is defined in clause 6.1.3.2.2 table 6.1.3.2.2-6.

UE shall finish Cell 1 release in T4 and shall not send any CSI reports to Cell 1 during T5.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

## A.6.3.1.11Inter-band inter-frequency synchronous DAPS handover from FR1 to FR1

## A.6.3.1.11.1Test Purpose and Environment

This test is to verify the requirement for the FR1-to-FR1 inter-band inter-frequency synchronous DAPS handover requirements specified in clause 6.1.3.2.

## A.6.3.1.11.2Test Parameters

Supported test configurations are shown in table A.6.3.1.11.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.11.2-2, A.6.3.1.11.2-3 and A.6.3.1.11.2-4.

The test scenario comprises of two bands each with one cell. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively.

Before the start of T1, the UE is connected to Cell 1 (source PCell) on radio channel 1 but is not aware of Cell 2 (neighbour cell) on radio channel 2. The UE shall be configured with periodic CSI reporting for cell1. During T1, the UE shall not have any timing information of Cell 2.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event A3 is configured for neighbour cell (Cell 2), and the UE is configured with the measurement gaps (gap pattern ID # 0). Starting T2, Cell 2 becomes known to the UE. During T2, the UE shall report Event A3. After receiving the Event A3, the test system shall send a RRC m`essage implying DAPS handover to the UE.

The start of T3 is the instant when the last TTI containing the RRC message implying DAPS handover to Cell 2 (target PCell) is sent to the UE. During T3, the UE shall be able to perform random access to Cell 2. DL schedule and UL feedback to Cell 1 shall be avoided when UE is required to perform DL reception or UL transmission in PRACH procedure in Cell 2, except preamble transmission. After the RACH procedure is completed, the test system shall send a RRC message to the UE to release Cell 1 (source cell) on radio channel 1.

The start of T4 is the instant when the last TTI containing the RRC message implying source cell release is sent to the UE. During T4, the UE shall perform source cell release.

Starting T5, the UE shall stop sending CSI report to the source cell.

Table A.6.3.1.11.2-1: Inter-band inter-frequency synchronous DAPS handover from FR1 to FR1 test configurations

Table A.6.3.1.11.2-2: General test parameters for inter-band inter-frequency synchronous DAPS handover from FR1 to FR1

Table A.6.3.1.11.2-3: Cell specific test parameters for inter-band inter-frequency synchronous DAPS handover from FR1 to FR1 (Cell 1)

Table A.6.3.1.11.2-4: Cell specific test parameters for inter-band inter-frequency synchronous DAPS handover from FR1 to FR1 (Cell 2)

## A.6.3.1.11.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T3. During Dhandover1, the interruption on Cell 1 shall not exceed Tinterrupt1 as defined in table 6.1.3.2.2-3 for synchronous DAPS HO.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay Dhandover1 can be expressed as: TRRC_procedure + TIU + Tprocessing + T∆ + Tmargin, where:

TRRC_procedure = 10 ms and is specified in clause 12 in TS 38.331 [2].

TIU = 20 ms in the test. TIU is defined in clause 6.1.1.2.2.

T∆ = 20 ms in the test. T∆ is defined in clause 6.1.1.2.2.

Tprocessing = 20 ms in the test. Tprocessing is defined in clause 6.1.1.2.2.

Tmargin = 2 ms in the test. Tmargin is defined in clause 6.1.1.2.2.

This gives a total of 72 ms.

The UE shall complete to release Cell 1 less than (10 ms + Tinterrupt2) from the beginning of time period T4. During Dhandover2, the interruption on Cell 2 shall not exceed Tinterrupt2 as defined in table 6.1.3.2.2-7 for synchronous DAPS HO.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay Dhandover2 can be expressed as: TRRC_procedure + Tinterrupt2, where:

TRRC_procedure = 10 ms and is specified in clause 12 in TS 38.331 [2].

## A.6.3.1.12Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR1

## A.6.3.1.12.1Test Purpose and Environment

This test is to verify the requirement for the FR1-to-FR1 inter-band inter-frequency asynchronous DAPS handover requirements specified in clause 6.1.3.2.

## A.6.3.1.12.2Test Parameters

Supported test configurations are shown in table A.6.3.1.12.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.12.2-2, A.6.3.1.12.2-3 and A.6.3.1.12.2-4.

The test scenario comprises of two bands each with one cell. The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5 respectively.

Before the start of T1, the UE is connected to Cell 1 (source PCell) on radio channel 1 but is not aware of Cell 2 (neighbour cell) on radio channel 2. The UE shall be configured with periodic CSI reporting for cell1. During T1, the UE shall not have any timing information of Cell 2.

Before the start of T2, the UE in the measurement control information that event-triggered reporting with Event A3 is configured for neighbour cell (Cell 2), and the UE is configured with the measurement gaps (gap pattern ID # 0). Starting T2, Cell 2 becomes known to the UE. During T2, the UE shall report Event A3. After receiving the Event A3, the test system shall send a RRC message implying DAPS handover to the UE.

The start of T3 is the instant when the last TTI containing the RRC message implying DAPS handover to Cell 2 (target PCell) is sent to the UE. During T3, the UE shall be able to perform random access to Cell 2. DL schedule and UL feedback to Cell 1 shall be avoided when UE is required to perform DL reception or UL transmission in PRACH procedure in Cell 2, except preamble transmission. After the RACH procedure is completed, the test system shall send a RRC message to the UE to release Cell 1 (source cell) on radio channel 1.

The start of T4 is the instant when the last TTI containing the RRC message implying source cell release is sent to the UE. During T4, the UE shall perform source cell release.

Starting T5, the UE shall stop sending CSI report to the source cell.

Table A.6.3.1.12.2-1: Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR1 test configurations

Table A.6.3.1.12.2-2: General test parameters for inter-band inter-frequency asynchronous DAPS handover from FR1 to FR1

Table A.6.3.1.12.2-3: Cell specific test parameters for inter-band inter-frequency asynchronous DAPS handover from FR1 to FR1 (Cell 1)

Table A.6.3.1.12.2-4: Cell specific test parameters for inter-band inter-frequency asynchronous DAPS handover from FR1 to FR1 (Cell 2)

## A.6.3.1.12.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T3. During Dhandover1, the interruption on Cell 1 shall not exceed Tinterrupt1 as defined in table 6.1.3.2.2-3 for asynchronous DAPS HO.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay Dhandover1 can be expressed as: TRRC_procedure + TIU + Tprocessing + T∆ + Tmargin, where:

TRRC_procedure = 10 ms and is specified in clause 12 in TS 38.331 [2].

TIU = 20 ms in the test. TIU is defined in clause 6.1.1.2.2.

T∆ = 20 ms in the test. T∆ is defined in clause 6.1.1.2.2.

Tprocessing = 20 ms in the test. Tprocessing is defined in clause 6.1.1.2.2.

Tmargin = 2 ms in the test. Tmargin is defined in clause 6.1.1.2.2.

This gives a total of 72 ms.

The UE shall complete to release Cell 1 less than (10 ms + Tinterrupt2) from the beginning of time period T4. During Dhandover2, the interruption on Cell 2 shall not exceed Tinterrupt2 as defined in table 6.1.3.2.2-7 for asynchronous DAPS HO.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay Dhandover2 can be expressed as: TRRC_procedure + Tinterrupt2, where:

TRRC_procedure = 10 ms and is specified in clause 12 in TS 38.331 [2].

## A.6.3.1.13SA NR - E-UTRAN with NR PSCell addition in FR1

## A.6.3.1.13.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE can make correct inter-RAT E-UTRAN handover with PSCell addition when operating in standalone (SA) operation with PCell in FR1 where target PCell and target PSCell are unknown. This test shall verify the Handover with PSCell from NR SA to EN-DC requirements as specified in clause 6.1.5.2.

The test comprises of two NR carrier and one E-UTRA carrier. There are three cells and one cell on each carrier. Cell 1 is the NR PCell, Cell 2 is an inter-RAT E-UTRAN neighbour cell and Cell 3 is an NR neighbour cell. The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2 and Cell 3. Starting T2, Cell 2 and Cell 3 becomes detectable

A RRC message implying handover with PSCell shall be sent to the UE during period T1. The start of T2 is the instant when the last TTI containing the RRC message implying handover with PSCell is sent to the UE.Before T2, the UE does not have any information of Cell 3. The handover with PSCell message shall contain Cell 2 and Cell 3 as the target cells and the SMTC for Cell 3 is configured in RRCConnectionReconfiguration.

Supported test configurations are shown in table A.6.3.1.13.1-1. General test parameters are provided in table A.6.3.1.13.1-2. Cell specific test parameters for Cell 1, Cell 2 and Cell 3 are provided in tables A.6.3.1.13.1-3, A.6.3.1.13.1-4 and A.6.3.1.13.1-5 respectively.

Table A.6.3.1.13.1-1: Supported test configurations for SA inter-RAT E-UTRAN handover tests

Table A.6.3.1.13.1-2: General test parameters for Handover with PSCell from NR SA to EN-DC

Table A.6.3.1.13.1-3: Cell specific test parameters for Handover with PSCell from NR SA to EN-DC (Cell 1)

Table A.6.3.1.13.1-4: Cell specific test parameters for Handover with PSCell from NR SA to EN-DC (Cell 2)

Table A.6.3.1.13.1-5: Cell specific test parameters for Handover with PSCell from NR SA to EN-DC (Cell 3)

## A.6.3.1.13.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 175 ms from the beginning of time period T2.

The UE shall start to transmit the PRACH to Cell 3 less than 270 ms from the beginning of time period T2.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and is specified in clause 6.1.5.2.

Tinterrupt = 125 ms in the test; Tinterrupt is defined in clause 6.1.5.2.

The PSCell addition time can be expressed as: TRRC_delay + Tprocessing + Tsearch_HO + Tsearch_PSCell + T∆ + TPSCell_ DU + 2 ms which is defined in clause 6.1.5.2.

The rate of correct handovers observed during repeated tests shall be at least 90%.

## A.6.3.1.14SA NR - E-UTRAN handover with NR FR1 PSCell addition

## A.6.3.1.14.1Test Purpose and Environment

The purpose of this set of tests is to verify that the UE can make correct SA inter-RAT handover from NR to E-UTRAN with FR1 PSCell addition when operating in standalone (SA) operation with PCell in FR1, for the case where the PSCell is known to the UE at the time of addition and SMTC of target known PSCell is not present in RRCConnectionReconfiguration. This test shall verify delay requirements of inter-RAT handover from NR to E-UTRAN and FR1 PSCell addition as specified in clause 6.1.5.

The test comprises of two NR cells and one E-UTRA cell. Cell 1 is the NR PCell, Cell 2 is an inter-RAT E-UTRAN neighbour cell and Cell 3 is the target NR PSCell, on radio channel 1 in FR1, radio channel 2 in E-UTRAN and radio channel 3 in FR1, respectively.

In this test, inter-RAT handover from NR to E-UTRAN and FR1 PSCell addition are performed in parallel processing. The test consists of successive time periods for inter-RAT handover and FR1 PSCell addition with time durations of T1, T2 and T3 respectively.

At the start of time duration T1, the UE does not have any timing information of Cell 2 and Cell 3, and the UE is only monitoring Cell 1. During T1, only Cell 1 is known to the UE.

Before the start of T2, the test system shall send measurement control information including measurement gap configuration and event-triggered reporting configuration with event B2 for neighbour Cell 2 and event A3 for Cell 3. Gap pattern configuration with id #0 as specified in Table 9.1.2-1 is configured before T2 begins.

Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report, and the Cell 3 (PSCell-to-be) on radio channel 3 becomes known to the UE at the time of addition. The RRC message implying handover with PSCell shall be sent to the UE during period T2 after the UE has reported Event B2 and Event A3. After receiving both Event B2 and Event A3 the test system shall send a RRC message to the UE to release the measurement gaps.

The point in time at which the RRC message implying handover with PSCell is received at the UE antenna connector defines the start of period T3 and T3’. The handover with PSCell message shall contain Cell 2 as the target cell and Cell 3 as PSCell-to-be added. The RRC message (to add PSCell) also includes a request for the UE to start periodic CSI reporting for the PSCell after the PSCell has been successfully added.

During T3, the UE shall carry out random access (i.e., transmit the PRACH) towards the Cell 2. Reception by the test system of the PRACH preamble defines the end of T3.

During T3’, the UE shall carry out random access (i.e., transmit the PRACH) towards the Cell 3. Reception by the test system of the PRACH preamble defines the start of period T4’.

During T4’, the UE shall send periodic CSI reports in PSCell and the test system shall observe the periodic reporting of CSI for PSCell.

Supported test configurations are shown in table A.6.3.1.14.1-1. General test parameters are provided in table A.6.3.1.14.1-2. Cell specific test parameters for NR Cell 1, E-UTRAN PCell Cell 2 and NR PSCell Cell 3 are provided in tables A.6.3.1.14.1-3, A.6.3.1.14.1-4 and A.6.3.1.14.1-5 respectively.

Table A.6.3.1.14.1-1: Supported test configurations for SA inter-RAT E-UTRAN handover with FR1 PSCell addition tests

Table A.6.3.1.14.1-2: General test parameters for SA inter-RAT E-UTRAN handover with FR1 PSCell addition

Table A.6.3.1.14.1-3: Cell specific test parameters for SA inter-RAT E-UTRA handover with FR1 PSCell addition (NR Cell 1)

Table A.6.3.1.14.1-4: Cell specific test parameters for SA inter-RAT E-UTRA handover with FR1 PSCell addition (E-UTRA Cell 2)

Table A.6.3.1.14.1-5: Cell specific test parameters for SA inter-RAT E-UTRA handover with FR1 PSCell addition (NR Cell 3)

## A.6.3.1.14.2Test Requirements

In this test, the UE shall start to transmit the PRACH to E-UTRA Cell 2 less than 85 ms Note1 from the beginning of time period T3.

The UE shall transmit the PRACH to PSCell no later than 117 ms Note2 from the start of T3’. The UE shall send at least one CSI report for PSCell with non-zero CQI index during T4’. The UE shall periodically send CSI reports for PSCell after the UE has sent first CQI report with non-zero CQI index during T4’.

The above test requirements shall be fulfilled in order of T1, T2, T3 for the observed inter-RAT handover delay from NR to E-UTRAN to be counted as correct, and in order of T1, T2, T3‘, T4‘ for the observed PSCell addition delay to be counted as correct.

The rate of correct handovers and correct PSCell addition delay during repeated tests shall be at least 90 %.

NOTE1:The handover delay can be expressed as specified in clause 6.1.5.2:

DHOwithPSCell_PCell = RRC procedure delay + Tinterrupt,

Where RRC procedure delay = 50 ms, Tinterrupt = Tsearch_HO + TIU + Tprocessing is defined in clause 6.1.5.2.1, where

Tsearch = 0 ms

TIU = 10 ms,

Tprocessing = 25 ms

Note2: The PSCell addition delay can be expressed as follows as specified in clause 6.1.5.2.2:

DHOwithPSCell_PSCell = TRRC_delay + Tprocessing + Tsearch_HO + Tsearch_PSCell + T∆ + TPSCell_ DU + 2 ms

Where:

TRRC_delay = 50 ms

Tprocessing = 25 ms

Tsearch_HO  = 0

Tsearch_PSCell = 0

T∆ = 20 ms

TPSCell_ DU = 1*10+10 = 20 ms

## A.6.3.1.15Intra-frequency handover from FR1 to FR1; known target cell configured with NCD-SSB

## A.6.3.1.15.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-frequency handover requirements specified in clause 6.1.1.2, when the target cell is configured with NCD-SSB.

## A.6.3.1.15.2Test Parameters

Supported test configurations are shown in table A.6.3.1.15.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.15.2-2, and A.6.3.1.15.2-3.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

Before the test starts,

-UE is connected to Cell 1 with active DL BWP and active UL BWP;

-UE is configured with nonCellDefiningSSB-r17 under BWP-DownlinkDedicated, and NCD-SSB serves as the reference SSB for the serving cell, and is contained in the active DL BWP.

During T2, Cell 2 is switched ON, and transmits two SSBs, i.e. CD-SSB at SSB frequency 1 and NCD-SSB at SSB frequency 2. Before the test, UE is configured to measure SSB frequency 2. The test equipment shall send an RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3.

The start of T3 is defined as the end of the last TTI containing the RRC message implying handover. The handover command indicates the UE to handover to Cell 2 with firstActiveDownlinkBWP-Id configured to BWP-1. The UE then performs handover from Cell 1’s active DL-BWP associated with the NCD-SSB of Cell 1 to Cell 2’s BWP-1 which is associated with NCD-SSB of Cell 2.

Table A.6.3.1.15.2-1: Intra-frequency handover from FR1 to FR1 test configurations

Table A.6.3.1.15.2-2: General test parameters Intra-frequency handover from FR1 to FR1

Table A.6.3.1.15.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency handover test case

## A.6.3.1.15.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 132  ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 122 ms in the test. Tinterrupt is defined in clause 6.1.1.2.2.

This gives a total of 132 ms.

## A.6.3.1.16Inter-frequency handover from FR1 to FR1; known target cell configured with NCD-SSB

## A.6.3.1.16.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 inter-frequency handover requirements specified in clause 6.1.1.2, when the target cell is configured with NCD-SSB.

## A.6.3.1.16.2Test Parameters

Supported test configurations are shown in table A.6.3.1.16.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.16.2-2 and A.6.3.1.16.2-3.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

Before the test starts,

-UE is connected to Cell 1 with active DL BWP and active UL BWP;

-UE is not configured with nonCellDefiningSSB-r17 under BWP-DownlinkDedicated, and CD-SSB serves as the reference SSB for the serving cell, and is contained in the active DL BWP.

During T2, Cell 2 is switched ON, and transmits two SSBs, i.e. CD-SSB at SSB frequency 1 and NCD-SSB at SSB frequency 2. Before the test, UE is configured to measure SSB frequency 1. The test equipment shall send an RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3.

The start of T3 is defined as the end of the last TTI containing the RRC message implying handover. The handover command indicates the UE to handover to Cell 2 with firstActiveDownlinkBWP-Id configured to BWP-1. The UE then performs handover from Cell 1’s active DL-BWP associated with the CD-SSB of Cell 1 to Cell 2’s BWP-1 which is associated with NCD-SSB of Cell 2.

Table A.6.3.1.16.2-1: Inter-frequency handover from FR1 to FR1 test configurations

Table A.6.3.1.16.2-2: General test parameters Inter-frequency handover from FR1 to FR1

Table A.6.3.1.16.2-3: Cell specific test parameters for NR FR1-FR1 Inter-frequency handover test case

## A.6.3.1.16.3 Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 212 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 202 ms in the test. Tinterrupt is defined in clause 6.1.1.2.2.

This gives a total of 212 ms.

## A.6.3.1.17Handover with PSCell change delay from NR-DC (FR1-FR1) to NR-DC (FR1-FR1)

## A.6.3.1.17.1Test Purpose and Environment

The purpose of this test is to verify the handover delay requirements and PSCell change delay requirements in HO with PSCell from NR-DC (FR1-FR1) to NR-DC (FR1-FR1) defined in clauses 6.1.5.4. The requirements are applicable to NR FR1-FR1 intra-frequency PCell handover and NR FR1-FR1 intra-frequency PSCell change.

The supported test configurations are given in table A.6.3.1.17.1-1. The test scenario comprises four NR cells, source PCell(Cell 1) and source PSCell(Cell 2), target PCell(Cell 3), target PSCell(Cell 4).

Cell 1 and Cell 3 are on radio channel 1 in FR1. Cell 2 and Cell 4 are on radio channel 2 in FR1. Test parameters are given in Tables A.6.3.1.17.1-2, A.6.3.1.17.1-3, A.6.3.1.17.1-4 and A.6.3.1.17.1-5 below. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of T1, the UE shall be connected to Cell 1 on radio channel 1 and Cell 2 on radio channel 2. UE is not aware of Cell 3 and Cell 4. Starting T2, Cell 3 and Cell 4 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

Table A.6.3.1.17.1-1: Supported test configurations for HO with PSCell from NR-DC to NR-DC

Table A.6.3.1.17.1-2: General test parameters for PCell FR1-FR1 Intra-frequency handover

Table A.6.3.1.17.1-3: Cell specific test parameters for PCell FR1-FR1 Inter-frequency handover

Table A.6.3.1.17.1-4: General test parameters Intra-frequency FR1-FR1 PSCell change

Table A.6.3.1.17.1-5: Cell specific test parameters for Intra-frequency FR1-FR1 PSCell change

## A.6.3.1.17.2Test Requirements

In this test, the UE shall start to transmit the PRACH to target PCell (Cell 3) less than 93 ms from the beginning of time period T2.

The UE shall transmit the PRACH to target PSCell (Cell 4) no later than 103 ms from the beginning of time period T2.

The rate of correct handovers and correct PSCell change delay during repeated tests shall be at least 90 %.

NOTE:The handover with PSCell change delay is defined in clause 6.1.5.4.1 as

DHOwithPSCell_PCell = RRC procedure delay + Tinterrupt, whereTinterrupt = Tsearch + TIU + Tprocessing  + T∆ + Tmargin

PSCell change delay during handover is defined in clause 6.1.5.4.2 as

DHOwithPSCell_PSCell = TRRC_delay + Tprocessing + Tsearch_HO + Tsearch_PSCell + T∆ + TPSCell_ DU + 2 ms.

In this test the definition of each components are specified as followings :

TRRC_delay = 16 ms and is specified in clause 12 in TS 38.331 [2],

Tprocessing = 25 ms,

Tsearch = 20 ms,

Tsearch_HO  = 0,

Tsearch_PSCell = 20 ms,

TIU = 10 ms,

T∆ = 20 ms,

Tmargin = 2 ms,

TPSCell_ DU = 1*10+10 = 20 ms

## A.6.3.1.18Intra-frequency handover from FR1 to FR1; unknown target cell operating with 12 PRB SSB bandwidth

A.6.3.1.18.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-frequency handover requirements for unknown target cell operating with 12 PRB SSB bandwidth specified in clause 6.1.1.2.

## A.6.3.1.18.2Test Parameters

Supported test configurations are shown in table A.6.3.1.18.2-1. General test parameters as specified in table A.6.3.1.2.2-2 with config 1 apply except those specified in table A.6.3.1.18.2-2. Cell specific test parameters as specified in table A.6.3.1.2.2-3 with config 1 apply except those specified in table A.6.3.1.18.2-3.

The test procedure specified in clause A.6.3.1.2.2 applies to this test. The Cell 2 is the unknown target cell operating with 12 PRB SSB bandwidth.

Table A.6.3.1.18.2-1: Intra-frequency handover from FR1 to FR1 test configurations

Table A.6.3.1.18.2-2: General test parameters Intra-frequency handover from FR1 to FR1

Table A.6.3.1.18.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency handover test case

## A.6.3.1.18.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 132 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 122 ms in the test. Tinterrupt is defined in clause 6.1.1.2.2.

This gives a total of 132 ms.

## A.6.3.1.19Handover with PSCell change delay where target PSCell is with 12PRB SSB bandwidth

## A.6.3.1.19.1Test Purpose and Environment

The purpose of this test is to verify the handover delay requirements and PSCell change/addition delay requirements in HO with PSCell from NR-DC (FR1-FR1) to NR-DC (FR1-FR1) defined in clauses 6.1.5.4. The requirements are applicable to NR FR1-FR1 intra-frequency PCell handover and NR FR1-FR1 intra-frequency PSCell change/addition. The requirements are only applicable when the target PSCell is configured with 12PRB SSB bandwidth.

## A.6.3.1.19.2Test Parameters

The supported test configurations are given in table A.6.3.1.19.2-1. Only 15kHz FDD cases are considered. The test scenario comprises 3 NR cells, source PCell(Cell 1), target PCell(Cell 2), target PSCell(Cell 3).

Cell 1 and Cell 2 are on radio channel 1 in FR1. Cell 3 is on radio channel 2 in FR1. Test parameters are given in Tables A.6.3.1.19.2-2, A.6.3.1.19.2-3, and A.6.3.1.19.2-4 below. Note that for Cell 3 the SSB configuration refers to SSB pattern 13 in FR1: SSB allocation for SSB SCS=15kHz in 3 MHz. In the test, the SSB is configured with 12PRB bandwidth.

The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of T1, the UE shall be connected to Cell 1 on radio channel 1. UE is not aware of Cell 2 and Cell 3. Starting T2, Cell 2 and Cell 3 becomes detectable to the UE and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

The UE is required to successfully handover from Cell 1 to Cell 2 and at the same time in time period T2 add Cell 3 as PSCell attached to Cell 2. This test case verifies the delay starting from the start of T2 to time points where the UE finishes handover to Cell 2 and where the UE finishes addition of Cell 3. Test cases delay requirements are specified.

Table A.6.3.1.19.2-1: Supported test configurations for HO with PSCell with 12PRB SSB bandwidth

Table A.6.3.1.19.2-2: General test parameters for HO with PSCell with 12PRB SSB bandwidth

Table A.6.3.1.19.2-3: Cell specific test parameters for Intra-frequency handover

Table A.6.3.1.19.2-4: Cell specific test parameters for Intra-frequency FR1-FR1 PSCell change/addition

## A.6.3.1.19.3Test Requirements

Handover to PCell delay requirements

In this test, the UE shall start to transmit the PRACH to target PCell (Cell 2) less than [98] ms from the beginning of time period T2.

The handover delay is defined as

DHOwithPSCell_PCell = RRC procedure delay + Tinterrupt, where

Tinterrupt = Tsearch + TIU + Tprocessing + T∆ + Tmargin

The UE is required to follow the below parameters according to derivation from the test setup specified:

-RRC procedure delay = 16 ms,

-Tsearch = 20 ms,

-TIU = 20 ms where PRACH association period should be configured as 1,

-Tprocessing = 20 ms,

-T∆ = 20 ms,

-Tmargin = 2ms.

That sums up to 98ms exactly.

PSCell change/addition delay requirements

The UE shall transmit the PRACH to target PSCell (Cell 3) no later than [178] ms from the beginning of time period T2.

PSCell change delay during handover is defined as

DHOwithPSCell_PSCell = TRRC_delay + Tprocessing + Tsearch_PCell + Tsearch_PSCell + T∆ + TPSCell_ DU + 2 ms.

In this test the UE is required to follow the below parameters according to derivation from the test setup specified:

-TRRC_delay = 16ms,

-Tprocessing = 20 ms,

-Tsearch_PCell = 0,

-Tsearch_PSCell = 60 ms,

-T∆ = 60 ms,

-TPSCell_ DU = 1*10+10 = 20 ms where PRACH association period should be configured as 1.

That sums up to 178ms exactly.

The test is considered successful only when both requirements are correctly verified, and the success rate during repeated tests shall be at least 90 %.

## A.6.3.2RRC Connection Mobility Control

## A.6.3.2.1SA: RRC Re-establishment

## A.6.3.2.1.1Intra-frequency RRC Re-establishment in FR1

A.6.3.2.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the NR intra-frequency RRC re-establishment delay in FR1 with known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1.

The test parameters are given in table A.6.3.2.1.1.1-1, table A.6.3.2.1.1.1-2 and table A.6.3.2.1.1.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.6.3.2.1.1.1-1: Supported test configurations

Table A.6.3.2.1.1.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR1

Table A.6.3.2.1.1.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR1

A.6.3.2.1.1.2Test Requirements

The RRC re-establishment delay is defined as the time from the moment UE declares RLF, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to a known NR intra-frequency cell shall be less than 1.6 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant  is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 1

Tidentify_intra_NR = 200 ms

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 [2] for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1545 ms for RRC re-establishment delay, allow 1840 ms (240 ms + 1.6 s) from the beginning of T2 in the test case.

## A.6.3.2.1.2Inter-frequency RRC Re-establishment in FR1

A.6.3.2.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the NR inter-frequency RRC re-establishment delay in FR1 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2.1.

The test parameters are given in table A.6.3.2.1.2.1-1, table A.6.3.2.1.2.1-2 and table A.6.3.2.1.2.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

Table A.6.3.2.1.2.1-1: Supported test configurations

Table A.6.3.2.1.2.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1

Table A.6.3.2.1.2.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1

A.6.3.2.1.2.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter-frequency cell shall be less than 3 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant  is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 2.

Tidentify_intra_NR = 800 ms.

Tidentify_inter_NR = 800 ms.

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 [2] for the target inter-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 2945 ms, allow 3 s in the test case.

## A.6.3.2.1.3Intra-frequency RRC Re-establishment in FR1 without serving cell timing

A.6.3.2.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the NR intra-frequency RRC re-establishment delay in FR1 without serving cell timing is within the specified limits. These tests will verify the requirements in clause 6.2.1.

The test parameters are given in table A.6.3.2.1.3.1-1, table A.6.3.2.1.3.1-2 and table A.6.3.2.1.3.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

Table A.6.3.2.1.3.1-1: Supported test configurations

Table A.6.3.2.1.3.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR1

Table A.6.3.2.1.3.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR1

A.6.3.2.1.3.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR intra-frequency cell without serving cell timing shall be less than 2.2 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant  is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

.TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 1.

Tidentify_intra_NR = 800 ms.

TSI = 1280 ms; it is the time required for receiving all the relevant system information as defined in TS 38.331 [2] for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 2145 ms, allow 2.2 s in the test case.

## A.6.3.2.2Random Access

## A.6.3.2.2.14-step RA type contention based random access test in FR1 for NR standalone

A.6.3.2.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.2 and clause 7.1.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.6.3.2.2.1.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.6.3.2.2.1.1-2.

Table A.6.3.2.2.1.1-1: Supported test configurations for contention based random access test in FR1 for NR standalone

Table A.6.3.2.2.1.1-2: General test parameters for contention based random access test in FR1 for NR Standalone

A.6.3.2.2.1.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.6.3.2.2.1.2.1Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2.2.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 22  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.6.3.2.2.1.2.2Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 22  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.6.3.2.2.1.2.3No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 22  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.6.3.2.2.1.2.4Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2.2.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

A.6.3.2.2.1.2.5Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A. 6.3.2.2.1.2.6Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.6.3.2.2.1.2.7Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.6.3.2.2.24-step RA type non-contention based random access test in FR1 for NR standalone

A.6.3.2.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.2 and clause 7.1.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.6.3.2.2.2.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.6.3.2.2.2.1-2 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2). Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

Table A.6.3.2.2.2.1-1: Supported test configurations for non-contention based random access test in FR1 for NR standalone

Table A.6.3.2.2.2.1-2: General test parameters for non-contention based random access test in FR1 for NR Standalone

A.6.3.2.2.2.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.6.3.2.2.2.2.1SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2.2.2.2.1 for SSB-based Random Access Preamble transmsission, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 22  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.6.3.2.2.2.2.2CSI-RS-based Random Access Preamble Transmission

In Test-2, to test the UE behavior specified in clause 6.2.2.2.2.1 for CSI-RS-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with CSI-RSs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the CSI-RS configured.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the CSI-RS configured, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given by the ra-OccasionList.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 22  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.6.3.2.2.2.2.3Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 22  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

A.6.3.2.2.2.2.4No Random Access Response Reception

To test the UE behavior specified in clause 6.2.2.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.2. The power of the first preamble shall be 22  dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1.2.

## A.6.3.2.2.32-step RA type contention based random access test in FR1 for NR standalone

A.6.3.2.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the 2-step RA type random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.3 and clause 7.1.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.6.3.2.2.3.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.6.3.2.2.3.1-2.

Table A.6.3.2.2.3.1-1: Supported test configurations for 2-step RA type contention based random access with successRAR test in FR1 for NR standalone

Table A.6.3.2.2.3.1-2: General test parameters for 2-step RA type contention based random access with successRAR test in FR1 for NR standalone

A.6.3.2.2.3.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.6.3.2.2.3.2.1MsgA Transmission

To test the UE behavior specified in clause 6.2.2.3.1.1 the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured msgA-RSRP-ThresholdSSB.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first MsgA preamble transmission shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be 3dB lower than the first MsgA PRACH power for test configuration 1 and equal to the first MsgA PRACH power for test configuration 2 & 3 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

A.6.3.2.2.3.2.2MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.1.2 the System Simulator shall transmit a MsgB containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB(s) and shall transmit an ACK if the MsgB with a successRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble and if the Contention Resolution is successful.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB(s) contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be 3dB lower than the first MsgA PRACH power for test configuration 1 and equal to the first MsgA PRACH power for test configuration 2 & 3 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

A.6.3.2.2.3.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.1.3 the System Simulator shall transmit a MsgB containing a successRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if no MsgB  is received within the MsgB Response window.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be 3dB lower than the first MsgA PRACH power for test configuration 1 and equal to the first MsgA PRACH power for test configuration 2 & 3 with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.6.3.2.2.42-step RA type non-contention based test in FR1 for NR standalone

A.6.3.2.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2.2.3 and clause 7.1.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.6.3.2.2.4.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.6.3.2.2.4.1-2.

Table A.6.3.2.2.4.1-1: Supported test configurations for non-contention based random access test in FR1 for NR standalone

Table A.6.3.2.2.4.1-2: General test parameters for non-contention based random access test in FR1 for NR Standalone

A.6.3.2.2.4.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.6.3.2.2.4.2.1MsgA Transmission

To test the UE behavior specified in clause 6.2.2.3.2.1, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the MsgA with a preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0.

In addition, the System Simulator shall receive the MsgA PRACH on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occasions permitted by the restrictions given first by the msgA-SSB-SharedRO-MaskIndex if configured, or next by the ra-ssb-OccasionMaskIndex if configured.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

A.6.3.2.2.4.2.2MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.2 the System Simulator shall transmit a MsgB containing a fallbackRAR containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a MsgB not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for MsgB(s) and shall transmit the msg3 containing the payload of MsgA PUSCH if the MsgB with a fallbackRAR contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble. The UE shall monitor contention resolution as described in clause 8.2A in TS 38.213 [3].

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA PRACH and MsgA PUSCH transmission power when the backoff time expires if all received MsgB’s contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA and msg3 transmissions shall be within the accuracy specified in clause 7.1.2.

A.6.3.2.2.4.2.3No MsgB Reception

To test the UE behavior specified in clause 6.2.2.3.2.3 the System Simulator shall transmit a MsgB containing a successRAR message and a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2a in TS 38.321 [7], and transmit with the calculated MsgA transmission power when the backoff time expires if no MsgB  is received within the MsgB Response window.

In addition, the power applied to all MsgA transmissions shall be in accordance with what is specified in clause 6.2.2.3. The power of the first preamble shall be -22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The power of the first MsgA PUSCH transmission shall be same as the first MsgA PRACH power with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional MsgA transmissions shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all MsgA transmissions shall be within the accuracy specified in clause 7.1.2.

## A.6.3.2.3SA: RRC Connection Release with Redirection

## A.6.3.2.3.1Redirection from NR in FR1 to NR in FR1

A.6.3.2.3.1.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements specified in clause 6.2.3.2.1.

A.6.3.2.3.1.2Test Parameters

Supported test configurations are shown in table A.6.3.2.3.1.2-1. The time delay is tested by using the parameters in table A.6.3.2.3.1.2-2, and A.6.3.2.3.1.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2. Cell 1 and Cell 2 belong to different tracking areas.

Table A.6.3.2.3.1.2-1: Redirection from NR to NR test configurations

Table A.6.3.2.3.1.2-2: General test parameters for Redirection from NR to NR test case

Table A.6.3.2.3.1.2-3: Cell specific test parameters for Redirection from NR to NR test case

A.6.3.2.3.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2240 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_NR = TRRC_procedure_delay + Tidentify-NR + TSI-NR + TRACH,

where:

TRRC_procedure_delay = 110 msin the test.

Tidentify-NR = 680 ms in the test.

TSI-NR = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331[2] for the target NR cell.

TRACH = 170 ms in the test.

This gives a total of 2240 ms.

## A.6.3.2.3.2Redirection from NR in FR1 to E-UTRAN

A.6.3.2.3.2.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to E-UTRAN requirements specified in clause 6.2.3.2.2.

A.6.3.2.3.2.2Test Parameters

Supported test configurations are shown in table A.6.3.2.3.2.2-1. The time delay is tested by using the parameters in table A.6.3.2.3.2.2-2, A.6.3.2.3.2.2-3 and A.6.3.2.3.2.2-4.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2.

Table A.6.3.2.3.2.2-1: Redirection from NR to E-UTRAN test configurations

Table A.6.3.2.3.2.2-2: General test parameters for Redirection from NR to E-UTRAN test case

Table A.6.3.2.3.2.2-3: Cell specific test parameters for Redirection from NR to E-UTRAN (Cell 1)

Table A.6.3.2.3.2.2-4: Cell specific test parameters for Redirection from NR to E-UTRAN (Cell 2)

A.6.3.2.3.2.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2205 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to E-UTRAN observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_E-UTRA = TRRC_procedure_delay + Tidentify-E-UTRA + TSI-E-UTRA + TRACH,

where:

TRRC_procedure_delay = 110 ms  in the test.

Tidentify-E-UTRA = 800 ms in the test.

TSI-E-UTRA = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 36.331 [2] for the target E-UTRA cell.

TRACH = 15 ms in the test.

This gives a total of 2205 ms.

## A.6.3.2.4LTM PDCCH-order Random Access

## A.6.3.2.4.1PDCCH-order RACH on neighbor cell in FR1 when RACH BW is within active UL BWP

A.6.3.2.4.1.1Test Purpose and Environment

This test is to verify the requirement for PDCCH-order RACH on neighbour cell in FR1 when RACH BW is within active UL BWP specified in clause 8.1 in TS 38.213 [3] and UE transmit timing in clause 7.1 for UE supporting rach-EarlyTA-Measurement-r18.

A.6.3.2.4.1.2Test Parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. Test configurations are given in table A.6.3.2.4.1.2-1. Both PDCCH order RACH delay, transmit timing requirement and the interruption requirements are tested by using the parameters in table A.6.3.2.4.1.2-2 and A.6.3.2.4.1.2-3.

This test contains 2 tests (test 1, and 2) and UE may have to pass one of the tests based on the conditions defined in this clause.

In test 1, joint TCI state configuration as defined in table A.6.3.2.4.1.2-2 is provided.

In test 2, no candidate TCI state configurations are configured as in table A.6.3.2.4.1.2-2.

If a UE supports ltm-MAC-CE-JointTCI-r18, it is only required to pass test 1. If a UE does not support ltm-MAC-CE-JointTCI-r18, it is only required to pass test 2.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. No gap patterns are configured in the test case.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is provided with LTM-Candidate-r18 for Cell 2.

-A measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

-For tests 1, 2, the UE has reported L3 measurement results and performed SSB based L1-RSRP measurement on Cell 2.

In test 1 and 2, T1 starts from UE transmitting a valid L1 report on Cell 2.

In test 1, after receiving the first L1 report on Cell 2 during T1, the test equipment sends TCI state activation MAC CE to active TCI state of Cell 2 no later than 100 ms after receiving the L1 report.

-In test 1, CandidateTCI-State#1 is activated.

-In test 2, test equipment shall not send TCI state activation MAC CE to active TCI state of Cell 2.

The start of T2 is the instant when PDCCH order to trigger PRACH transmission on Cell 2 is sent to the UE.

Table A.6.3.2.4.1.2-1: PDCCH order RACH on neighbor cell in FR1 test configurations

Table A.6.3.2.4.1.2-2: General test parameters for PDCCH order RACH in FR1

Table A.6.3.2.4.1.2-3: Cell specific test parameters for PDCCH order RACH test case

A.6.3.2.4.1.3Test Requirements

The UE shall transmit the PRACH preamble to Cell 2 in the first available PRACH occasion after  + 0.5 ms +  from the beginning of time period T2. After transmitting PRACH on Cell 2, UE shall retune back to Cell 1.NT,2 TSSB

NOTE:The PDCCH order RACH delay can be expressed as: , where:NT,2+TBWPswitchDelay+∆Delay+Tswitch+TSSB+∆RF/BB preparation

- is a time duration of  symbols corresponding to a PUSCH preparation time for UE processing capability 1 assuming  corresponds to the smallest SCS configuration between the SCS configuration of the PDCCH order and the SCS configuration of the corresponding PRACH transmission and is specified in table 6.4-1 in TS 38.214 [26].NT,2N2μ

-= 0, = 0, = 0TBWPswitchDelayTswitch∆RF/BB preparation

-= 0.5 ms∆Delay

-= 0 for UE supporting ltm-MAC-CE-JointTCI-r18 and/or ltm-MAC-CE-SeparateTCI-r18, otherwise , where  is the time to first SSB after 1 slot from the end of the slot that UE receives PDCCH-order, and  = 2 ms, which is the time for SSB processing.TSSBTSSB= Tfirst-SSB_RACH + TSSB-procTfirst-SSB_RACHTSSB-proc

During T2, interruption on Cell 1 UL shall not happen outside the overlapped slot to transmit PRACH and  symbols before and after the PRACH occasion as defined in clause 8.1 in 38.213 [3], where N=2. During T2, interruption on Cell 1 DL shall not occur outside the overlapped slot to transmit PRACH.N

The test equipment will verify that the timing of PRACH transmission on Cell 2 is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB of Cell 2.

-The NTA_offset value (in Tc units) is 25600

-The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.3.2.4.2PDCCH-ordered RACH to an inter-frequency candidate cell in FR1 for LTM

A.6.3.2.4.2.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 PDCCH-ordered RACH to an inter-frequency candidate cell in FR1 for LTM. The Te requirements are specified in 7.1. The interruption requirements specified in clause 8.2.2.2.20. This test is for UE supporting PDCCH-ordered RACH to an inter-frequency candidate cell, whose SSB is outside active BWPs of the UE.

A.6.3.2.4.2.2Test Parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency from the PCell. Test configurations are given in table A.6.3.2.4.2.2-1. Both interruption length and Te requirements for the first uplink transmission are tested by using the parameters in table A.6.3.2.4.2.2-2 and A.6.3.2.4.2.2-3.

The test consists of 2 tests, and UE is required to pass one among Test 1, Test 2.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18

The test consists of two successive time periods, with time durations of T1 and T2, respectively. Measurement gap patterns are configured in the test case and the SSB of Cell 2 is outside the active BWP of Cell 1. The PCell is continuously scheduled during the whole test.

Before T1, for Test 1, 2:

-Cell 1 and Cell 2 on radio channel 1 are powered on.

-UE establishes a connection with the Cell 1.

-A measurement object is configured for the frequency of the Cell 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used. UE has reported an L3 measurement result of Cell 2 to Cell 1.

-UE is provided with LTM-Candidate-r18 for Cell 2

-Joint TCI state configuration as defined in table A.6.3.2.4.2.2-2 for Test 1 is provided.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2, and UE has already reported a valid L1-RSRP result of Cell 2.

During T1, for Test 1:

-At the start of T1, UE receives candidate cell TCI state activation MAC CE for Cell 2.

-In Test 1, CandidateTCI-State#1 is activated.

-T1 ends 100 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2, T1 is skipped.

During T2, for Test 1, 2:

-At the start of T2, UE receives PDCCH order to trigger PRACH transmission on Cell 2.

Note: PDCCH order is not expected on the frame with SFN mod 8 =3.

-T2 ends with UE back to Cell 1 after transmitting PRACH to Cell 2.

-The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during the transmission of PDCCH ordered RACH.

-The test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB.

-The NTA offset value (in Tc units) is 25600

-The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

Table A.6.3.2.4.2.2-1: Inter-frequency PDCCH-ordered RACH from FR1 to FR1 test configurations

Table A.6.3.2.4.2.2-2: General test parameters for Inter-frequency PDCCH-ordered RACH test from FR1 to FR1 from FR1 to FR1

Table A.6.3.2.4.2.2-3: Cell specific test parameters for NR FR1-FR1 Inter-frequency PDCCH-ordered RACH test

A.6.3.2.4.2.3Test Requirements

The UE shall transmit the PRACH preamble to Cell 2 in the first available PRACH occasion after  + 0.5 ms +  from the beginning of time period T2. After transmitting PRACH on Cell 2, UE shall retune back to Cell 1.NT,2 TSSB

NOTE:The PDCCH order RACH delay can be expressed as: , where:NT,2+TBWPswitchDelay+∆Delay+Tswitch+TSSB+∆RF/BB preparation

- is a time duration of  symbols corresponding to a PUSCH preparation time for UE processing capability 1 assuming  corresponds to the smallest SCS configuration between the SCS configuration of the PDCCH order and the SCS configuration of the corresponding PRACH transmission and is specified in table 6.4-1 in TS 38.214 [26].NT,2N2μ

-= 0, = 0TBWPswitchDelayTswitch

-= 0.5 ms∆Delay

-is defined in clause 6.2.2C∆RF/BB preparation

-= 0 for UE supporting ltm-MAC-CE-JointTCI-r18 and/or ltm-MAC-CE-SeparateTCI-r18, otherwise , where  is the time to first SSB occasion overlapped with MGL after 2ms and 1 slot from the end of the slot that UE receives PDCCH-order, and  = 2 ms, which is the time for SSB processing.TSSBTSSB= Tfirst-SSB_RACH + TSSB-procTfirst-SSB_RACHTSSB-proc

During T2, interruption on Cell 1 UL shall not happen outside ceil (Y/NR Slot length) +1 slots before and after PRACH transmission and the same slot of PRACH, where Y as reported in pdcch-RACH-Switching-TargetBandTimeList-r18.

The test equipment will verify that the timing of PRACH transmission on Cell 2 is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB of Cell 2.

-The NTA_offset value (in Tc units) is 25600

-The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.3.2.4.3PDCCH-order RACH on neighbor cell without L1-RSRP measurement in FR1 when RACH BW is within active UL BWP

A.6.3.2.4.3.1Test Purpose and Environment

This test is to verify the requirement for PDCCH-order RACH on neighbour cell without L1-RSRP measurement in FR1 when RACH BW is within active UL BWP specified in clause 8.1 in 38.213 [3] and UE transmit timing in clause 7.1 for UE supporting rach-EarlyTA-Measurement-r18.

A.6.3.2.4.3.2Test Parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. Test configurations are given in table A.6.3.2.4.3.2-1. Both PDCCH order RACH delay, transmit timing requirement and the interruption requirements are tested by using the parameters in table A.6.3.2.4.3.2-2 and A.6.3.2.4.3.2-3.

This test contains 2 tests (test 1 and 2) and UE may have to pass one of the tests based on the conditions defined in this clause.

-In test 1, joint TCI state configuration as defined in table A.6.3.2.4.3.2-2 is provided.

-In test 2, no candidate TCI state configurations are configured as in table A.6.3.2.4.3.2-2.

If a UE supports ltm-MAC-CE-JointTCI-r18, it is only required to pass test 1. If a UE does not support ltm-MAC-CE-JointTCI-r18, it is only required to pass test 2. The test consists of two successive time periods, with time durations of T1 and T2 respectively. No gap patterns are configured in the test case.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is provided with LTM-Candidate-r18 for Cell 2.

-A measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

In test 1 and 2, T1 starts from UE transmitting a L3 report on Cell 2. In test 1, after receiving the L3 report on Cell 2 during T1, the test equipment sends TCI state activation MAC CE to active TCI state of Cell 2 no later than 100 ms after receiving the L3 report.

-In test 1, CandidateTCI-State#1 is activated.

-In test 2, test equipment shall not send TCI state activation MAC CE to active TCI state of Cell 2.

The start of T2 is the instant when PDCCH order to trigger PRACH transmission on Cell 2 is sent to the UE.

Table A.6.3.2.4.3.2-1: PDCCH order RACH on neighbor cell in FR1 test configurations

Table A.6.3.2.4.3.2-2: General test parameters for PDCCH order RACH in FR1

Table A.6.3.2.4.3.2-3: Cell specific test parameters for PDCCH order RACH test case

A.6.3.2.4.3.3Test Requirements

The UE shall transmit the PRACH preamble to Cell 2 in the first available PRACH occasion after  + 0.5 ms +  from the beginning of time period T2. After transmitting PRACH on Cell 2, UE shall retune back to Cell 1.NT,2 TSSB

NOTE:The PDCCH order RACH delay can be expressed as: , where:NT,2+TBWPswitchDelay+∆Delay+Tswitch+TSSB+∆RF/BB preparation

- is a time duration of  symbols corresponding to a PUSCH preparation time for UE processing capability 1 assuming  corresponds to the smallest SCS configuration between the SCS configuration of the PDCCH order and the SCS configuration of the corresponding PRACH transmission and is specified in table 6.4-1 in TS 38.214 [26].NT,2N2μ

-= 0, = 0, = 0TBWPswitchDelayTswitch∆RF/BB preparation

-= 0.5 ms∆Delay

- is the time to first SSB occasion, after 1 slot from the end of the slot of the PDCCH plus 2 ms (SSB processing time) .TSSB

During T2, interruption on Cell 1 UL shall not happen outside the overlapped slot to transmit PRACH and  symbols before and after the PRACH occasion as defined in clause 8.1 in TS 38.213 [3], where N=2. During T2, interruption on Cell 1 DL shall not occur outside the overlapped slot to transmit PRACH.N

The test equipment will verify that the timing of PRACH transmission on Cell 2 is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB of Cell 2.

-The NTA_offset value (in Tc units) is 25600

-The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.3.3Conditional handover

## A.6.3.3.1Intra-frequency conditional handover from FR1 to FR1

## A.6.3.3.1.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-frequency conditional handover requirements specified in clause 6.1.4.2.

## A.6.3.3.1.2Test Parameters

Supported test configurations are shown in table A.6.3.3.1.2-1. Both conditional handover delay and interruption length are tested by using the parameters in table A.6.3.3.1.2-2 and A.6.3.3.1.2-3.

The test consists of two successive time periods, with time durations of T1 and  T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

NR shall configure a condition implying handover to Cell 2 during T1, at a time earlier than TRRC before the beginning of T2.

Table A.6.3.3.1.2-1: Intra-frequency conditional handover from FR1 to FR1 test configurations

Table A.6.3.3.1.2-2: General test parameters Intra-frequency conditional handover from FR1 to FR1

Table A.6.3.3.1.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency conditional handover test case

## A.6.3.3.1.3Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution = 800 +62 +10=872 ms from the start of T2 and the interruption during T2 shall not exceeed Tinterrupt=Tprocessing + TIU + T∆ + Tmargin =40+20+2 = 62 ms

## A.6.3.3.2Inter-frequency conditional handover from FR1 to FR1

## A.6.3.3.2.1Test Purpose and Environment

This test is to verify the requirement for the NR conditional FR1-NR FR1 inter-frequency conditional handover requirements specified in clause 6.1.4.2.

## A.6.3.3.2.2Test Parameters

Supported test configurations are shown in table A.6.3.3.2.2-1. Both conditional handover delay and interruption length are tested by using the parameters in table A.6.3.3.2.2-2 and A.6.3.3.2.2-3.

The test scenario comprises of two carriers and one cell on each carrier Gap pattern ID gp0 is configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. NR shall configure a condition implying handover to Cell 2 during T1, at a time earlier than TRRC before the beginning of T2.  At the start of T2, Cell 2 becomes detectable and meets the handover condition.

Table A.6.3.3.2.2-1: Inter-frequency handover from FR1 to FR1 test configurations

Table A.6.3.3.2.2-2: General test parameters Inter-frequency handover from FR1 to FR1

Table A.6.3.3.2.2-3: Cell specific test parameters for NR FR1-FR1 Inter-frequency handover test case

## A.6.3.3.2.3Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution =920 +62 +10=992 ms from the start of T2 and the interruption during T2 shall not exceeed Tinterrupt=Tprocessing + TIU + T∆ + Tmargin =40+20+2 = 62 ms excluding any transmissions which do not occur due to measurement gaps.

## A.6.3.3.3NR conditional handover including target MCG and target SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC

## A.6.3.3.3.1Test Purpose and Environment

The purpose of this test is to verify that UE can make correct NR-RC to NR-DC conditional handover including target MCG in FR1 and target SCG in FR1 as specified in clauses 6.1.6.1.

The supported test configurations are given in table A.6.3.3.3.1-1. The test scenario comprises four NR cells, source PCell (Cell 1) and source PSCell (Cell 2), target PCell (Cell 3), and target PSCell (Cell 4). Cell 1 and Cell 3 are on radio channel 1 in FR1. Cell 2 and Cell 4 are on radio channel 2 in FR1.

Test parameters are given in tables A.6.3.3.3.1-2, A.6.3.3.3.1-3, A.6.3.3.3.1-4 and A.6.3.3.3.1-5 below.

The test consists of two successive time periods, with time durations of T1, T2 respectively.

At the start of T1, the UE shall be connected to Cell 1 on radio channel 1 and Cell 2 on radio channel 2. UE is not aware of Cell 3 and Cell 4.  NR shall configure a condition implying handover to Cell 3 and Cell 4 during T1, at a time earlier than TRRC before the beginning of T2.

At the start of T2, Cell 3 and Cell 4 become detectable. The condition for conditional PCell handover is met during T2.

Table A.6.3.3.3.1-1: Supported test configurations for NR conditional handover including target MCG and target SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC

Table A.6.3.3.3.1-2: General test parameters for PCell handover at conditional handover including target MCG and target SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC

Table A.6.3.3.3.1-3: Cell specific test parameters for PCell handover at conditional handover including target MCG and target SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC

Table A.6.3.3.3.1-4: General test parameters for PSCell change at conditional handover including target MCG and target SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC

Table A.6.3.3.3.1-5: Cell specific test parameters for PSCell change at conditional handover including target MCG and target SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC

## A.6.3.3.3.2Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 3 less than Tmeasure + Tinterrupt + TCHO_execution =920 +57 +10=987 ms from the start of T2, and the interruption during T2 shall not exceeed TIU + Tprocessing  + T∆ + Tmargin=10+25+20+2=57 ms.

The UE shall start to transmit the PRACH to Cell 4 less than Tmeasure + TCHO_execution + Tprocessing + Tsearch_PCell_Conditional + Tsearch_PSCell + T∆_PSCell + TPSCell_ DU + 2 ms =920+10+25+0+ (3*20)+ 20+2=1037 ms from the start of T2, excluding any transmissions which do not occur due to measurement gaps.

The rate of correct conditional handovers observed during repeated tests shall be at least 90 %.

Note1:The PCell conditional handover delay can be expressed as specified in clause 6.1.6.1:

DCHOwithPSCell_PCell = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

The interruption time is the time between when the UE starts to execute the conditional handover to the target cell and the time the UE starts transmission of the new PRACH as specified in clause 6.1.6.1.1

Tinterrupt = TIU + Tprocessing  + T∆ + Tmargin ms

The PSCell conditional handover delay can be expressed as specified in clause 6.1.6.1.2:

DCHOwithPSCell_PSCell = TRRC + TEvent_DU + Tmeasure + TCHO_execution + Tprocessing + Tsearch_PCell_Conditional + Tsearch_PSCell + T∆_PSCell + TPSCell_DU + 2 ms

## A.6.3.3.4NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC

## A.6.3.3.4.1Test Purpose and Environment

This test is to verify the requirement for conditional handover including target MCG and candidate SCG for CPC in FR1 NR-DC specified in clause 6.1.7.1. This test verifies the requirements for PCell conditional handover delay in section 6.1.7.1.1 and PSCell conditional change delay in section 6.1.7.1.2 for FR1-FR1 NR-DC to FR1-FR1 NR-DC CHO with CPC.

## A.6.3.3.4.2Test Parameters

Supported test configurations are shown in table A.6.3.3.4.2-1. Conditional handover delay and interruption length are tested by using the parameters in table A.6.3.3.4.2-2 and A.6.3.3.4.2-3. Conditional PSCell change delay and interruption length are tested by using the parameters in tables A.6.3.3.4.2-2 and A.6.3.3.4.2-4.

The test consists of three successive time periods, with time durations of T1, T2, and T3, respectively.

At the start of time duration T1, the UE is connected to Cell 1 (source PCell) and Cell 2 (source PSCell). The UE may not have any timing information of Cell 3 (target PCell) and Cell 4 (target PSCell).

TE shall configure a condition implying conditional handover to Cell 3 with a condition implying conditional PSCell change to Cell 4 during T1, at a time earlier than TRRC before the beginning of T2.

At the start of T2, Cell 3 becomes detectable. At the start of T3, Cell 4 becomes detectable. UE meets the handover condition and meets the PSCell change condition during T3.

Table A.6.3.3.4.2-1: Supported test configurations for NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC

Table A.6.3.3.4.2-2: General test parameters for NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC

Table A.6.3.3.4.2-3: Cell specific test parameters for NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC (Cell 1 and Cell 3)

Table A.6.3.3.4.2-4: Cell specific test parameters for NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC (Cell 2 and Cell 4)

## A.6.3.3.4.3Test Requirements

TRRC + TEvent_DU occurs during T1 and T2, as the conditional handover condition for Cell 3 becomes satisfied at the start of T2, and the conditional PSCell change condition for Cell 4 becomes satisfied at the start of T3. The test shall verify that there are no interruptions during T1 and T2. The UE shall not send PRACH to Cell 3 before the end of T3. The UE shall not send PRACH to Cell 4 before the end of T3.

The UE shall start to transmit PRACH to Cell 3 less than max (Tmeasure_PCell, Tmeasure_PSCell) + TUE_preparation + Tprocessing + T∆_PCell + TPCell_DU + 2 ms = (800 + 10 + 25 + 20 + 20 + 2) ms = 877 ms from the start of T3 and the interruption during T3 shall not exceeed Tprocessing + T∆_PCell + TPCell_DU + 2 ms = (25 + 20 + 20 + 2) ms = 67 ms.

The UE shall start to transmit PRACH to Cell 4 less than max (Tmeasure_PCell, Tmeasure_PSCell) + TUE_preparation + Tprocessing + T∆_PSCell + TPSCell_DU + 2 ms = (800 + 10 + 25 + 20 + 20 + 2) ms = 877 ms from the start of T3. The interruption during T3 shall not exceed Tprocessing + T∆_PSCell + TPSCell_DU + 2 ms = 25 ms + 20 + 20 ms + 2 ms = 67 ms.

## A.6.3.3.5NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC with complementary conditional handover configuration

## A.6.3.3.5.1Test Purpose and Environment

This test verifies the requirement for conditional handover when the UE is configured with target MCG and candidate SCG for CPC in FR1 NR-DC and additionally configured with a complementary CHO only configuration in FR1. The test verifies that the UE makes the correct decision to proceed with CHO without CPC in case CHO condition is met without CPC condition being met, meanwhile verifying the conditional handover delay requirement in section 6.1.4.2.

For UE which can pass test case defined in clause A.6.3.3.5, test case defined in clause A.6.3.3.1 can be skipped and corresponding test requirements are deemed to be fulfilled.

## A.6.3.3.5.2Test Parameters

Supported test configurations are shown in table A.6.3.3.5.2-1. Both conditional handover delay and interruption length are tested by using the parameters in table A.6.3.3.5.2-2 and A.6.3.3.5.2-3.

The test consists of two successive time periods, with time durations of T1 and T2 respectively.

At the start of time duration T1, the UE is connected to Cell 1 (source PCell) and Cell 2 (source PSCell). The UE may not have any timing information of Cell 3 (target PCell) and Cell 4 (target PSCell).

TE shall configure a condition implying conditional handover to Cell 3 with a condition implying conditional PSCell change to Cell 4 during T1, at a time earlier than TRRC before the beginning of T2. Additionally, the TE shall configure a complementary condition only implying conditional handover to Cell 3.

At the start of T2, Cell 3 becomes detectable. UE meets the handover condition during T2.

Table A.6.3.3.5.2-1: Supported test configurations for NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC with complementary conditional handover configuration

Table A.6.3.3.5.2-2: General test parameters NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC with complementary conditional handover configuration

Table A.6.3.3.5.2-3: Cell specific test parameters for NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC with complementary conditional handover configuration (Cell 1 and Cell 3)

Table A.6.3.3.5.2-4: Cell specific test parameters for NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC with complementary conditional handover configuration (Cell 2 and Cell 4)

## A.6.3.3.5.3Test Requirements

TRRC + TEvent_DU occurs during T1 as the conditional handover condition for cell becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 3 less than Tmeasure + Tinterrupt + TCHO_execution = 800 +62 +10=872 ms from the start of T2 and the interruption during T2 shall not exceeed Tinterrupt=Tprocessing + TIU + T∆ + Tmargin =40+20+2 = 62 ms.

The UE shall not send PRACH to Cell 4.

## A.6.3.3.6NES triggering intra-frequency conditional handover from FR1 to FR1

## A.6.3.3.6.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-frequency NES-based conditional handover requirements specified in clause 6.1.4.2.

## A.6.3.3.6.2Test Parameters

Supported test configurations are shown in table A.6.3.3.6.2-1. Both NES-based conditional handover delay and interruption length are tested by using the parameters in table A.6.3.3.6.2-2 and A.6.3.3.6.2-3.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

NR shall configure the NES-based condition implying handover to Cell 2 firstly, and then configure DCI 2-9 with NES-mode indication during T1, at a time earlier than TRRC before the beginning of T2. In the RRC signaling, one conditional execution condition with condEventA3 should be configured, that nesEvent set as true and A3-offset set as 0 dB.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and NES-based event is fulfilled.

Table A.6.3.3.6.2-1: NES triggering Intra-frequency conditional handover from FR1 to FR1 test configurations

Table A.6.3.3.6.2-2: General test parameters for NES triggering Intra-frequency conditional handover from FR1 to FR1

Table A.6.3.3.6.2-3: Cell specific test parameters for NR FR1-FR1 NES triggering Intra-frequency conditional handover test case

## A.6.3.3.6.3Test Requirements

TRRC + TEvent_DU occurs during T1 as the NES-based handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution = 800 +62 +10=872ms from the start of T2 and the interruption during T2 shall not exceed Tinterrupt=Tprocessing + TIU + T∆ + Tmargin =40+20+2 = 62ms.

## A.6.3.3.7NES-based Inter-frequency conditional handover from FR1 to FR1

## A.6.3.3.7.1Test Purpose and Environment

This test is to verify the requirement for the NES-based NR FR1-NR FR1 inter-frequency conditional handover requirements specified in clause 6.1.4.2.

## A.6.3.3.7.2Test Parameters

Supported test configurations are shown in table A.6.3.3.7.2-1. Both conditional handover delay and interruption length are tested by using the parameters in table A.6.3.3.7.2-2 and A.6.3.3.7.2-3.

The test scenario comprises of two carriers and one cell on each carrier. Gap pattern ID gp0 is configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. NR shall configure a condition implying handover to Cell 2 during T1, at a time earlier than TRRC before the beginning of T2.  At the start of T2, Cell 2 becomes detectable and meets the NES-based handover condition. In this test, UE is not indicated to report SSB based RRM measurement result with the associated SSB index for carrier of Cell 2, and DCI 2-9 command of ‘1’ value for indicating NES-specific CHO execution condition is transmitted to UE at 950 ms from the start of T2, i.e., UE receives DCI 2-9 command later than the time at the end of TEvent_DU + Tidentify_inter_without_index.

Table A.6.3.3.7.2-1: NES-based inter-frequency conditional handover from FR1 to FR1 test configurations

Table A.6.3.3.7.2-2: General test parameters for NES-based inter-frequency conditional handover from FR1 to FR1

Table A.6.3.3.7.2-3: Cell specific test parameters for NES-based NR FR1-FR1 inter-frequency conditional handover test case

## A.6.3.3.7.3Test Requirements

TRRC + TEvent_DU occurs during T1 as the handover condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + Tinterrupt + TCHO_execution =950 +62 +10=1022 ms from the start of T2 and the interruption during T2 shall not exceeed Tinterrupt=Tprocessing + TIU + T∆ + Tmargin =40+20+2 = 62 ms excluding any transmissions which do not occur due to measurement gaps.

## A.6.3.4LTM PCell Switch

## A.6.3.4.1RACH-based Intra-frequency PCell switch from FR1 to FR1

## A.6.3.4.1.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 RACH-based intra-frequency PCell switch specified in clause 6.3.1 for both with and without early TCI state activation.

## A.6.3.4.1.2Test Parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. Test configurations are given in table A.6.3.4.1.2-1. Both cell switch delay and interruption length are tested by using the parameters in table A.6.3.4.1.2-2 and A.6.3.4.1.2-3.

The test consists of 2 tests, and UE is required to pass one among Test 1, Test 2.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18

The test consists of four successive time periods, with time durations of T1 to T4 respectively. No gap patterns are configured in the test case.

During T1, for Test 1 and 2:

-A measurement object is configured for the frequency of the Cell 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-T1 ends with UE reporting an L3 measurement result of Cell 2 to Cell 1.

During T2, for Test 1 and 2:

-At the start of T2, UE is provided with LTM-Candidate-r18 for Cell 2

-In Test 1 and Test 2, joint TCI state configurations as defined in table A.6.3.4.1.2-2 are provided.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

-T2 ends with UE reporting a valid L1-RSRP result of Cell 2.

During T3, for Test 1:

-At the start of T3, UE receives candidate cell TCI state activation MAC CE for Cell 2.

-In Test 1, CandidateTCI-State#1 is activated.

-T3 ends 50 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2, T3 is skipped.

During T4, for Test 1 and 2:

-The start of T4 is the last TTI containing LTM cell switch command MAC CE is sent by Cell 1 to the UE.

-In the cell switch command, Cell 2 is the target cell. Contention-Free Random-Access Resources are indicated and the field of Timing Advance Command is set to FFF.

-In test 1, CandidateTCI-State#2 is indicated.

-In test 2, CandidateTCI-State#1 is indicated.

-T4 ends upon the reception of PRACH at Cell 2.

Table A.6.3.4.1.2-1: Intra-frequency cell switch from FR1 to FR1 test configurations

Table A.6.3.4.1.2-2: General test parameters for Intra-frequency cell switch from FR1 to FR1

Table A.6.3.4.1.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency cell switch test case

## A.6.3.4.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 in no later than DLTM from the beginning of time period T4. The rate of correct cell switches observed during repeated tests shall be at least 90 %.

NOTE:The cell switch delay can be expressed as DLTM (= Tcmd + TLTM-interrupt), where:

Tcmd = THARQ + 3 ms and is specified in clause 6.3.1.2. TLTM-interrupt = TLTM-RRC-processing + TLTM-processing + Tfirst-RS + TRS-proc + TLTM-IU ms and is specified in clause 6.3.1.2.1

-Tfirst-RS + TRS-proc= 0 ms for Test 1, Tfirst-RS + TRS-proc= 22 ms for Test 2

-TLTM-IU_=20 ms

-TLTM-RRC-processing =10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TLTM-RRC-processing =0 ms

-TLTM-processing =10 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 10 ms for FR1-to-FR1 cell switch in the capability

-TLTM-processing =15 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 15 ms for FR1-to-FR1 cell switch in the capability

-TLTM-processing =20 ms if the UE does not support ltm-FastUE-Processing-r18 capability.

## A.6.3.4.2RACH based Inter-frequency LTM PCell switch from FR1 to FR1

## A.6.3.4.2.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 inter-frequency LTM RACH based cell switch delay requirements specified in clause 6.3.1 for both with and without early TCI state activation.

## A.6.3.4.2.2Test Parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency from the PCell. Test configurations are given in table A.6.3.4.2.2-1. Both cell switch delay and interruption length are tested by using the parameters in table A.6.3.4.2.2-2 and A.6.3.4.2.2-3.

The test consists of 2 tests, and UE is required to pass one among Test 1, Test 2.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18

The test consists of four successive time periods, with time durations of T1, T2, T3 and T4, respectively.

During T1, for Test 1, 2:

-A measurement object is configured for the frequency of the Cell 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-T1 ends with UE reporting an L3 measurement result of Cell 2 to Cell 1.

During T2, for Test 1, 2:

-At the start of T2, UE is provided with LTM-Candidate-r18 for Cell 2

-In Test 1 and Test 2 joint TCI state configurations as defined in table A.6.3.4.2.2-2 are provided.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

-T2 ends with UE reporting a valid L1-RSRP result of Cell 2.

During T3, for Test 1:

-At the start of T3, UE receives candidate cell TCI state activation MAC CE for Cell 2.

-In Test 1, CandidateTCI-State#1 is activated.

-T3 ends 100 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2, T3 is skipped.

During T4, for Test 1 and 2:

-The start of T4 is the instant when the last TTI containing LTM cell switch command MAC CE is sent by Cell 2 to the UE.

-In the cell switch command, Cell 2 is the target cell for PCell switch. Contention-Free Random-Access Resources are indicated and the field of Timing Advance Command is set to FFF.

-In test 1, CandidateTCI-State#2 is indicated.

-In test 2, CandidateTCI-State#1 is indicated.

-T4 ends upon the reception of PRACH at Cell 2.

Table A.6.3.4.2.2-1: Inter-frequency RACH based cell switch from FR1 to FR1 test configurations

Table A.6.3.4.2.2-2: General test parameters Inter-frequency RACH based cell switch from FR1 to FR1

Table A.6.3.4.2.2-3: Cell specific test parameters for NR FR1-FR1 Inter-frequency RACH-based cell switch test case

## A.6.3.4.2.3Test Requirements

The UE shall start to transmit PRACH to Cell 2 in no later than DLTM from the beginning of time period T4.

The rate of correct cell switches observed during repeated tests shall be at least 90 %.

NOTE:The cell switch delay can be expressed as DLTM (= Tcmd + TLTM-interrupt), where:

Tcmd = THARQ + 3 ms and is specified in clause 6.3.1.2, TLTM-interrupt is defined in clause 6.3.1.3 as TLTM-RRC-processing + TLTM-processing + Tfirst-RS + TRS-proc + TLTM-IU,

-Tfirst-RS + TRS-proc= 0 ms for Test 1, Tfirst-RS + TRS-proc= 22 ms for Test 2,

-TLTM-IU_= 20 ms.

-TLTM-RRC-processing =10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TLTM-RRC-processing = 0 ms

-TLTM-processing = 10 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 10 ms for FR1-to-FR1 cell switch in the capability

-TLTM-processing = 15 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 15 ms for FR1-to-FR1 cell switch in the capability

-TLTM-processing = 20 ms if the UE does not support ltm-FastUE-Processing-r18 capability.

## A.6.3.4.3RACH-less Intra-frequency PCell switch from FR1 to FR1

## A.6.3.4.3.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 RACH-less intra-frequency PCell switch specified in clause 6.3.1 for both with and without early TCI state activation.

## A.6.3.4.3.2Test Parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. Supported test configurations are shown in table A.6.3.4.3.2-1. Both cell switch delay and interruption length are tested by using the parameters in table A.6.3.4.3.2-2 and A.6.3.4.3.2-3.

The test consists of 2 tests, and UE is required to pass one among Test 1, Test 2.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18 8

The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5, respectively. No gap patterns are configured in the test case.

During T1, for Test 1, 2:

-A measurement object is configured for the frequency of the Cell 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-T1 ends with UE reporting an L3 measurement result of Cell 2 to Cell 1.

During T2, for Test 1, 2:

-At the start of T2, UE is provided with LTM-Candidate-r18 for Cell 2

-Joint TCI state configuration as defined in table A.6.3.4.3.2-2 for Test 1 are provided.

-Separate TCI state configuration as defined in table A.6.3.4.3.2-2 for Test 1 are provided.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports on candidate cell (Cell 2) in PUCCH format 2.

-T2 ends with UE reporting a valid L1-RSRP result of Cell 2.

During T3, for Test 1:

-At the start of T3, UE receives candidate cell TCI state activation MAC CE for Cell 2.

-In Test 1, CandidateTCI-State#1 is activated.

-T3 ends 50 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2, T3 is skipped.

During T4, for Test 1, 2:

-At the start of T4, UE receives PDCCH order to trigger PRACH transmission on Cell 2.

-T4 ends 5 ms after the UE transmits the PRACH to Cell 2.

-For UE incapable of rach-EarlyTA-Measurement-r18, T4 is skipped.

During T5, for Test 1, 2:

-The start of T5 is the last TTI containing LTM cell switch command MAC CE is sent by Cell 1 to the UE.

-In the cell switch command, Cell 2 is the target cell and the field of Timing Advance Command is set to 0.

-In test 1, CandidateTCI-State#2 is indicated.

-In test 2, CandidateTCI-State#1 is indicated.

-Cell 2 continuously schedules PUSCH for the UE.

-T5 ends either at the UL slot of PUSCH scheduled by Cell 2 at the first DL slot not earlier than (Tcmd + TLTM-RRC-processing + TLTM-processing + Tfirst-RS + TRS-proc) after the beginning of T5 or upon the reception of PUSCH at Cell 2, whichever is earlier.

-The values of Tcmd, TLTM-RRC-processing TLTM-processing,Tfirst-RS and TRS-proc are specified in clause A.6.3.4.3.3.

Table A.6.3.4.3.2-1: Intra-frequency cell switch from FR1 to FR1 test configurations

Table A.6.3.4.3.2-2: General test parameters Intra-frequency cell switch from FR1 to FR1

Table A.6.3.4.3.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency cell switch test case

## A.6.3.4.3.3Test Requirements

The UE shall start to transmit PUSCH to Cell 2 in no later than DLTM from the beginning of time period T5.

The rate of correct cell switches observed during repeated tests shall be at least 90 %.

NOTE:The cell switch delay can be expressed as DLTM (= Tcmd + TLTM-interrupt), where:

Tcmd = THARQ + 3 ms and is specified in clause 6.3.1.2.

TLTM-interrupt is defined in clause 6.3.1.3 as TLTM-RRC-processing + TLTM-processing + Tfirst-RS + TRS-proc + TLTM-IU. Tfirst-RS + TRS-proc=0 for Test 1, Tfirst-RS + TRS-proc=22 ms for Test 2, and TLTM-IU_is the uncertainty on transmitting the first uplink transmission on Cell 2.

-TLTM-RRC-processing = 10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TLTM-RRC-processing =0 ms

-TLTM-processing = 10 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 10 ms for FR1-to-FR1 cell switch in the capability

-TLTM-processing = 15 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 15 ms for FR1-to-FR1 cell switch in the capability

-TLTM-processing = 20 ms if the UE does not support ltm-FastUE-Processing-r18 capability.

## A.6.3.4.4RACH-less Intra-frequency PCell switch from FR1 to FR1 without L1-RSRP measurement

## A.6.3.4.4.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 RACH-less intra-frequency PCell switch specified in clause 6.3.1 without L1-RSRP measurement and measurement reporting.

## A.6.3.4.4.2Test Parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. Supported test configurations are shown in table A.6.3.4.4.2-1. Both cell switch delay and interruption length are tested by using the parameters in table A.6.3.4.4.2-2 and A.6.3.4.4.2-3.

The test consists of 2 tests, and UE is required to pass one among Test 1, Test 2.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18

The test consists of five successive time periods, with time durations of T1, T2, T3, T4 and T5, respectively. No gap patterns are configured in the test case.

During T1, for Test 1, 2

-A measurement object is configured for the frequency of the Cell 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-T1 ends with UE reporting an L3 measurement result of Cell 2 to Cell 1.

During T2, for Test 1, 2:

-At the start of T2, UE is provided with LTM-Candidate-r18 for Cell 2

-Joint TCI state configuration as defined in table A.6.3.4.4.2-2 for Test 1 are provided.

During T3, for Test 1:

-At the start of T3, UE receives candidate cell TCI state activation MAC CE for Cell 2.

-In Test 1, CandidateTCI-State#1 is activated.

-T3 ends 50 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2, T3 is skipped.

During T4, for Test 1, 2:

-At the start of T4, UE receives PDCCH order to trigger PRACH transmission on Cell 2.

-T4 ends 5 ms after the UE transmits the PRACH to Cell 2.

-For UE incapable of rach-EarlyTA-Measurement-r18, T4 is skipped.

During T5, for Test 1, 2:

-The start of T5 is the last TTI containing LTM cell switch command MAC CE is sent by Cell 1 to the UE.

-In the cell switch command, Cell 2 is the target cell and the field of Timing Advance Command is set to 0.

-In test 1, CandidateTCI-State#2 is indicated.

-In test 2, CandidateTCI-State#1 is indicated.

-Cell 2 continuously schedules PUSCH for the UE.

-T5 ends either at the UL slot of PUSCH scheduled by Cell 2 at the first DL slot not earlier than (Tcmd + TLTM-RRC-processing + TLTM-processing + Tfirst-RS + TRS-proc) after the beginning of T5 or upon the reception of PUSCH at Cell 2, whichever is earlier.

-The values of Tcmd, TLTM-RRC-processing TLTM-processing,Tfirst-RS and TRS-proc are specified in clause A.6.3.4.3.3.

Table A.6.3.4.4.2-1: Intra-frequency cell switch from FR1 to FR1 test configurations

Table A.6.3.4.4.2-2: General test parameters Intra-frequency cell switch from FR1 to FR1

Table A.6.3.4.4.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency cell switch test case

## A.6.3.4.4.3Test Requirements

The UE shall start to transmit PUSCH to Cell 2 in no later than DLTM from the beginning of time period T5.

The rate of correct cell switches observed during repeated tests shall be at least 90 %.

NOTE:The cell switch delay can be expressed as DLTM (= Tcmd + TLTM-interrupt), where:

Tcmd = THARQ + 3 ms and is specified in clause 6.3.1.2.

TLTM-interrupt is defined in clause 6.3.1.3 as TLTM-RRC-processing + TLTM-processing + Tfirst-RS + TRS-proc + TLTM-IU. Tfirst-RS + TRS-proc=0 for Test 1, Tfirst-RS + TRS-proc=22 ms for Test 2, and TLTM-IU_is the uncertainty on transmitting the first uplink transmission on Cell 2.

-TLTM-RRC-processing = 10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TLTM-RRC-processing =0 ms

-TLTM-processing = 10 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 10 ms for FR1-to-FR1 cell switch in the capability

-TLTM-processing = 15 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 15 ms for FR1-to-FR1 cell switch in the capability

-TLTM-processing = 20 ms if the UE does not support ltm-FastUE-Processing-r18 capability.

## A.6.3.5LTM PSCell Switch

## A.6.3.5.1 RACH-based intra-frequency LTM PSCell switch from FR1 to FR1

## A.6.3.5.1.1Test Purpose and Environment

This test is to verify the intra-frequency RACH based LTM PSCell switch requirements from NR FR1 to NR FR1 specified in clause 8.20 for both with and without early TCI state activation.

## A.6.3.5.1.2Test Parameters

Three cells are deployed in the test, which are FR1 PCell (Cell 1), FR1 PSCell (Cell 2) and a FR1 neighbour cell (Cell 3) on the same frequency as the PSCell. The test configurations of PCell and PSCell are given in table A.6.3.5.1.2-1 and table A.6.3.5.1.2-1A. Both cell switch delay and interruption length are tested by using the parameters in table A.6.3.5.1.2-2 and table A.6.3.5.1.2-3.

The test consists of 2 tests, and UE is required to pass one among Test 1, Test 2.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18

The test consists of four successive time periods, with time durations of T1, T2, T3 and T4, respectively.

During T1, for Test 1 and 2:

-A measurement object is configured for the frequency of the Cell 3, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-T1 ends with UE reporting an L3 measurement result of Cell 3 to Cell 2.

During T2, for Test 1 and 2:

-At the start of T2, UE is provided with LTM-Candidate-r18 for Cell 3

-Joint TCI state configuration as defined in table A.6.3.5.1.2-2 for Test 1 are provided.

-UE is configured with SSB-based L1-RSRP measurements and periodic L1-RSRP measurement reports for candidate cell (Cell 3) in PUCCH format 2.

-T2 ends with UE reporting a valid L1-RSRP result of Cell 3.

During T3, for Test 1:

-At the start of T3, UE receives candidate cell TCI state activation MAC CE for Cell 3.

-In Test 1, CandidateTCI-State#1 is activated.

-T3 ends 50 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2, T3 is skipped.

During T4, for Test 1 and 2:

-The start of T4 is the instant when the last TTI containing LTM cell switch command MAC CE is sent by Cell 2 to the UE.

-In the cell switch command, Cell 3 is the target cell for PSCell switch. Contention-Free Random-Access Resources are indicated and the field of Timing Advance Command is set to FFF.

-In test 1, CandidateTCI-State#2 is indicated.

-In test 2, CandidateTCI-State#1 is indicated.

-T4 ends upon the reception of PRACH at Cell 3.

Table A.6.3.5.1.2-1: Supported PCell test configurations for intra-frequency PSCell cell switch from FR1 to FR1

Table A.6.3.5.1.2-1A: Supported PSCell test configurations for intra-frequency PSCell cell switch from FR1 to FR1

Table A.6.3.5.1.2-2: General test parameters for Intra-frequency cell switch from FR1 to FR1

Table A.6.3.5.1.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency cell switch test case

## A.6.3.5.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 3 in no later than DLTM from the beginning of time period T4.

The rate of correct cell switches observed during repeated tests shall be at least 90 %.

NOTE:The cell switch delay can be expressed as DLTM (= Tcmd + TLTM-RRC-processing + TLTM-processing + Tfirst-RS + TRS-proc + TLTM-IU), where:

Tcmd = THARQ + 3 ms and is specified in clause 6.3.1.2

-Tfirst-RS + TRS-proc= 0 ms for Test 1, Tfirst-RS + TRS-proc= 22 ms for Test 2

-TLTM-IU = 20 ms

-TLTM-RRC-processing = 10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TLTM-RRC-processing =0 ms

-TLTM-processing = 10 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 10 ms for FR1-to-FR1 cell switch in the capability

-TLTM-processing = 15 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 15 ms for FR1-to-FR1 cell switch in the capability

-TLTM-processing = 20 ms if the UE does not support ltm-FastUE-Processing-r18 capability.

## A.6.3.6CLTM PCell Switch

## A.6.3.6.1RACH-based intra-frequency CLTM PCell switch from FR1 to FR1 triggered by SSB based L1-RSRP measurement

## A.6.3.6.1.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 RACH-based intra-frequency CLTM PCell switch triggered by SSB-based L1-RSRP measurement specified in clause 6.3.2 for both with and without early TCI state activation, for UE supporting intraFreqL1-MeasConfig-r18 and not supporting cltm-EarlyTA-Indication-r19 and ltm-InterFreqMeasGap-r18.

## A.6.3.6.1.2Test Parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. Test configurations are given in table A.6.3.6.1.2-1. Both cell switch delay and interruption length are tested by using the parameters in table A.6.3.6.1.2-2 and A.6.3.6.1.2-3.

The test consists of 2 tests, and UE is required to pass one among Test 1, Test 2.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18

The test consists of four successive time periods, with time durations of T1 to T4 respectively. No gap patterns are configured in the test case.

During T1, for Test 1 and 2:

-A measurement object is configured for the frequency of the Cell 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-T1 ends with UE reporting an L3 measurement result of Cell 2 to Cell 1.

During T2, for Test 1 and 2:

-At the start of T2, UE is provided with LTM-Candidate-r18 for Cell 2

-In Test 1 and Test 2, joint TCI state configurations as defined in table A.6.3.6.1.2-2 are provided.

-LTM-Candidate-r18 includes the L1 condition implying cell switch to Cell 2 in ltm-ExecutionCondition-r19.

-Event LTM3 is used in the CLTM execution condition as defined in table A.6.3.6.1.2-2.

-UE is configured with SSB-based L1-RSRP measurements.

During T3, for Test 1:

-At the start of T3, UE receives candidate cell TCI state activation MAC CE for Cell 2.

-In Test 1, CandidateTCI-State#1 is activated.

-T3 ends 50 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2, T3 is skipped.

During T4, for Test 1 and 2:

-The start of T4 is the condition in ltm-ExecutionCondition-r19 becomes satisfied, Cell 2 is the target cell.

-T4 ends upon the reception of PRACH at Cell 2.

Table A.6.3.6.1.2-1: Intra-frequency cell switch from FR1 to FR1 test configurations

Table A.6.3.6.1.2-2: General test parameters for Intra-frequency cell switch from FR1 to FR1

Table A.6.3.6.1.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency cell switch test case

## A.6.3.6.1.3Test Requirements

TRRC + TEvent_DU occurs during T2 and T3 as the cell switch condition becomes satisfied at the start of T4.

The UE shall start to transmit the PRACH to Cell 2 in no later than Tmeasure + TCLTM-RRC-processing + TCLTM-interrupt from the beginning of time period T4 and the interruption during T4 shall not exceed TCLTM-interrupt. The rate of correct cell switches observed during repeated tests shall be at least 90 %.

NOTE:The cell switch delay can be expressed as DCLTM = TRRC + TEvent_DU + Tmeasure + TCLTM-RRC-processing + TCLTM-interrupt and is specified in clause 6.3.2.2, where:

-Tmeasure = 20ms.

-TCLTM-RRC-processing =10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TCLTM-RRC-processing =0 ms.

NOTE:TCLTM-interrupt = TLTM-processing + Tfirst-RS + TRS-proc + TCLTM-IU and is specified in clause 6.3.2.2.3, where:

-Tfirst-RS + TRS-proc= 0 ms for Test 1, Tfirst-RS + TRS-proc= 22 ms for Test 2

-TCLTM-IU_=20 ms

-TLTM-processing =10 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 10 ms for FR1-to-FR1 cell switch in the capability

-TLTM-processing =15 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 15 ms for FR1-to-FR1 cell switch in the capability

-TLTM-processing =20 ms if the UE does not support ltm-FastUE-Processing-r18 capability.

## A.6.3.6.2RACH-based inter-frequency CLTM PCell switch from FR1 to FR1 triggered by SSB based L1-RSRP measurement

## A.6.3.6.2.1Test Purpose and Environment

This test is to verify the requirement for the NR conditional FR1-NR FR1 inter-frequency conditional LTM cell switch requirements specified in clause 6.3.2.2 for both with and without early TCI state activation, for UE not supporting cltm-EarlyTA-Indication-r19 and supporting ltm-InterFreqMeasGap-r18.

## A.6.3.6.2.2Test Parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency from the PCell. Test configurations are given in table A.6.3.6.2.2-1. Both cell switch delay and interruption length are tested by using the parameters in table A.6.3.6.2.2-2 and A.6.3.6.2.2-3.

The test consists of 2 tests, and UE is required to pass one among Test 1, Test 2.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18

The test consists of four successive time periods, with time durations of T1, T2, T3 and T4, respectively.

During T1, for Test 1, 2:

-A measurement object is configured for the frequency of the Cell 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-T1 ends with UE reporting an L3 measurement result of Cell 2 to Cell 1.

During T2, for Test 1, 2:

-At the start of T2, UE is provided with LTM-Candidate-r18 for Cell 2

-In Test 1 and Test 2 joint TCI state configurations as defined in table A.6.3.6.2.2-2 are provided.

-LTM-Candidate-r18 includes the L1 condition implying cell switch to Cell 2 in ltm-ExecutionCondition-r19.

-Event LTM3 is used in the CLTM execution condition as defined in table A.6.3.6.2.2-2.

-UE is configured with SSB-based L1-RSRP measurements.

During T3, for Test 1:

-At the start of T3, UE receives candidate cell TCI state activation MAC CE for Cell 2.

-In Test 1, CandidateTCI-State#1 is activated.

-T3 ends 100 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2, T3 is skipped.

During T4, for Test 1 and 2:

-The start of T4 is the condition in ltm-ExecutionCondition-r19 becomes satisfied, Cell 2 is the target cell.

-T4 ends upon the reception of PRACH at Cell 2.

Table A.6.3.6.2.2-1: Inter-frequency RACH based CLTM cell switch from FR1 to FR1 test configurations

Table A.6.3.6.2.2-2: General test parameters Inter-frequency RACH based CLTM cell switch from FR1 to FR1

Table A.6.3.6.2.2-3: Cell specific test parameters for NR FR1-FR1 Inter-frequency CLTM RACH-based cell switch test case

## A.6.3.6.2.3Test Requirements

TRRC + TEvent_DU occurs during T3 as the CLTM condition becomes satisfied at the start of T4.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + TCLTM-RRC-processing + TCLTM-interrupt from the start of T4 and the interruption during T4 shall not exceeed TCLTM-interrupt =TLTM-processing + Tfirst-RS + TRS-proc + TCLTM-IU excluding any transmissions which do not occur due to measurement gaps, where:

-Tmeasure= TL1-RSRP_Measurement_Period_SSB_inter =20ms in the test,

-TCLTM-RRC-processing=10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TLTM-RRC-processing = 0 ms

-TCLTM-interrupt =TLTM-processing + Tfirst-RS + TRS-proc + TCLTM-IU, where

-TLTM-RRC-processing =10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TLTM-RRC-processing = 0 ms

-TLTM-processing = 10 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 10 ms for FR1-to-FR1 cell switch in the capability

-TLTM-processing = 15 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 15 ms for FR1-to-FR1 cell switch in the capability

-TLTM-processing = 20 ms if the UE does not support ltm-FastUE-Processing-r18 capability.

-Tfirst-RS + TRS-proc= 0 ms for Test 1, Tfirst-RS + TRS-proc= 22 ms for Test 2,

-TCLTM-IU_= 20 ms.

The rate of correct cell switches observed during repeated tests shall be at least 90 %.

## A.6.3.6.3RACH-less intra-frequency CLTM PCell switch from FR1 to FR1 triggered by SSB-based L1-RSRP measurement

## A.6.3.6.3.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 RACH-less intra-frequency CLTM PCell switch triggered by SSB-based L1-RSRP measurement specified in clause 6.3.2 for both with and without early TCI state activation, for UE supporting cltm-EarlyTA-Indication-r19 and intraFreqL1-MeasConfig-r18.

## A.6.3.6.3.2Test Parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. Supported test configurations are shown in table A.6.3.6.3.2-1. Both cell switch delay and interruption length are tested by using the parameters in tables A.6.3.6.3.2-2 and A.6.3.6.3.2-3.

The test consists of 2 tests, and UE is required to pass one among Test 1, Test 2.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18

The test consists of five successive time periods, with time durations of T1, T2, T3, T4, and T5 respectively. No gap patterns are configured in the test case.

During T1, for Test 1, 2:

-A measurement object is configured for the frequency of the Cell 2, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-T1 ends with UE reporting L3 measurement results of Cell 2 to Cell 1.

During T2, for Test 1, 2:

-At the start of T2, UE is provided with LTM-Candidate-r18 for Cell 2.

-In Test 1 and Test 2, joint TCI state configurations as defined in table A.6.3.6.3.2-1 are provided.

-LTM-Candidate-r18 includes the L1 condition implying cell switch to Cell 2 in ltm-ExecutionCondition-r19.

-Event LTM3 is used in the CLTM execution condition as defined in table A.6.3.6.3.2-1.

-UE is configured with SSB-based L1-RSRP measurements.

During T3, for Test 1:

-At the start of T3, UE receives candidate cell TCI state activation MAC CE for Cell 2.

-In Test 1, CandidateTCI-State#1 is activated.

T3 ends 50 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2, T3 is skipped.

During T4, for Test 1, 2:

-At the start of T4, UE receives PDCCH order to trigger PRACH transmission on Cell 2.

-T4 ends 5 ms after the UE transmits the PRACH to Cell 2.

During T5, for Test 1, 2:

-At the start of T5, Cell 2 meets the CLTM execution condition in ltm-ExecutionCondition-r19.

-Cell 2 continuously schedules PUSCH for the UE.

-T5 ends at the reception of PUSCH at Cell 2.

Table A.6.3.6.3.2-1: Intra-frequency cell switch from FR1 to FR1 test configurations

Table A.6.3.6.3.2-2: General test parameters for intra-frequency CLTM cell switch from FR1 to FR1

Table A.6.3.6.3.2-3: Cell specific test parameters for intra-frequency CLTM cell switch from FR1 to FR1

## A.6.3.6.3.3Test Requirements

The UE shall start to transmit PUSCH to Cell 2 in no later than Tmeasure + TCLTM-RRC-processing + TCLTM-interrupt from the start of T5 and the interruption during T5 shall not exceed TCLTM-interrupt= TLTM-processing + Tfirst-RS + TRS-proc + TCLTM-IU, where:

-Tmeasure = 20 ms.

-TCLTM-RRC-processing = 10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TCLTM-RRC-processing = 0 ms.

-TLTM-processing = 10 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 10 ms for FR1-to-FR1 cell switch in the capability.

-TLTM-processing = 15 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 15 ms for FR1-to-FR1 cell switch in the capability.

-TLTM-processing = 20 ms if the UE does not support ltm-FastUE-Processing-r18 capability.

-Tfirst-RS + TRS-proc = 0 ms for Test 1, Tfirst-RS + TRS-proc = 22 ms for Test 2.

-TCLTM-IU is the uncertainty on transmitting the new uplink transmission on Cell 2.

The rate of correct cell switches observed during repeated tests shall be at least 90 %.

## A.6.3.6.4RACH-less intra-frequency CLTM Pcell switch from FR1 to FR1 triggered by SSB-based L3-RSRP measurement

## A.6.3.6.4.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra-frequency conditional LTM Pcell switch requirements specified in clause 6.3.2 for both with and without early TCI state activation. For UE supporting cltm-EarlyTA-Indication-r19 and not supporting intraFreqL1-MeasConfig-r18.

## A.6.3.6.4.2Test Parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and two FR1 neighbour cells (Cell 2 and Cell 3) on the same frequency as the PCell. Supported test configurations are shown in table A.6.3.6.4.2-1. Both cell switch delay and interruption length are tested by using the parameters in table A.6.3.6.4.2-2 and A.6.3.6.4.2-3.

The test consists of 2 tests, and UE is required to pass one among Test 1, Test 2.

-Test 1: for a UE supporting ltm-MAC-CE-JointTCI-r18

-Test 2: for a UE not supporting ltm-MAC-CE-JointTCI-r18

No gap patterns are configured in the test case.

The test consists of six successive time periods, with time durations of T1, T2, T3, T4, T5, and T6 respectively. During T3, the UE peforms initial CLTM cell switch from Cell 1 to Cell 2, while subsequent CLTM cell switch from Cell 2 to Cell 3 is performed during T6.

During T1, for Test 1, 2:

A measurement object is configured for the frequency of the Cell 2 and Cell 3, and it is indicated to the UE that event-triggered reporting with Event A3 is used.

-UE is configured with SSB-based L3 measurement reports on candidate cell (Cell 2) in PUCCH format 2.

-T1 ends with UE reporting L3 measurement results of Cell 2 and Cell 3 to Cell 1.

During T2, for Test 1, 2:

-At the start of T2,  UE is provided with LTM-Candidate-r18 for Cell 2 and Cell 3.

In Test 1 and Test 2, joint TCI state configurations as defined in table A.6.3.6.4.2-1 are provided.

LTM-Candidate-r18 includes the L3 conditions implying cell switches to Cell 2 and Cell 3.

Event LTM3 is used in the CLTM execution conditions as defined in table A.6.3.6.4.2-1.

-UE is configured with SSB-based L1-RSRP measurements.

During T3, for Test 1 and 2:

-At the start of T3, Cell 2 meets the CLTM condition.

-T3 ends at the reception of RRCReconfigurationComplete message at Cell 2.

During T4, for Test 1, 2:

-At the start of T4, UE receives candidate cell TCI state activation MAC CE for Cell 3.

-In Test 1, CandidateTCI-State#1 is activated.

-T4 ends 50 ms after the candidate cell TCI state activation MAC CE transmission.

-In Test 2, T4 is skipped.

During T5, for Test 1, 2:

-At the start of T5, UE receives PDCCH order to trigger PRACH transmission on Cell 3.

-T5 ends 5 ms after the UE transmits the PRACH to Cell 3.

During T6, for Test 1, 2:

-At the start of T6, Cell 3 meets the CLTM condition.

-Cell 3 continuously schedules PUSCH for the UE.

-T6 ends at the reception of PUSCH at Cell 3.

Table A.6.3.6.4.2-1: Intra-frequency conditional handover from FR1 to FR1 test configurations

Table A.6.3.6.4.2-2: General test parameters Intra-frequency CLTM switch from FR1 to FR1

Table A.6.3.6.4.2-3: Cell specific test parameters for NR FR1-FR1 Intra-frequency CLTM test case

## A.6.3.6.4.3Test Requirements

The UE shall start to transmit PUSCH to Cell 3 in no later than Tmeasure + TCLTM-RRC-processing + TCLTM-interrupt from the start of T6 and the interruption during T6 shall not exceeed TCLTM-interrupt= TLTM-processing + Tfirst-RS + TRS-proc + TCLTM-IU, where:

-Tmeasure = 20 ms.

-TCLTM-RRC-processing = 10 ms if UE does not support ltm-FastProcessingConfig-r18, otherwise TCLTM-RRC-processing =0 ms.

-TLTM-processing = 10 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 10 ms for FR1-to-FR1 cell switch in the capability.

-TLTM-processing = 15 ms if the UE supports ltm-FastUE-Processing-r18 capability and UE reports 15 ms for FR1-to-FR1 cell switch in the capability.

-TLTM-processing = 20 ms if the UE does not support ltm-FastUE-Processing-r18 capability.

-Tfirst-RS + TRS-proc = 0 ms for Test 1, Tfirst-RS + TRS-proc = 22 ms for Test 2.

-TCLTM-IUis the uncertainty on transmitting the new uplink transmission on Cell 3.

The rate of correct cell switches observed during repeated tests shall be at least 90 %.

## A.6.4Timing

## A.6.4.1UE transmit timing

## A.6.4.1.1NR UE Transmit Timing Test for FR1

## A.6.4.1.1.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNB and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1.2.

Supported test configurations are shown in table A.6.4.1.1.1-1.

Table A.6.4.1.1.1-1: Supported test configurations for FR1 PCell

For this test a single NR cell is used. Table A.6.4.1.1.1-2 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.6.4.1.1.1-3.

Table A.6.4.1.1.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.6.4.1.1.1-3: SRS Configuration for Timing Accuracy Test

Table A.6.4.1.1.1-4: Void

## A.6.4.1.1.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1) Setup NR PCell according to parameters given in table A.6.4.1.1.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB.

a.The NTA offset value (in Tc units) is 25600

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.6.4.1.1.2-1

Table A.6.4.1.1.2-1: Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 Table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first path (in time) of DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna.  Skip this step for test 2 with DRX configured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first path (in time) of DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment

## A.6.4.1.2NR UE Transmit Timing Test for two TRPs in FR1

## A.6.4.1.2.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNB and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits for both TRPs. The test is configured with two TRPs in NR PCell. This test will verify the requirements in clause 7.1.2.

Supported test configurations are shown in table A.6.4.1.1.1-1.

Table A.6.4.1.2.1-1: Supported test configurations for FR1 PCell

For this test a single NR cell is used. Table A.6.4.1.2.1-2 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.6.4.1.2.1-3.

For UE not supporting the capability of “rxTimingDiff-r18”, the UE is only required to be tested in Test1 and Test3.

For UE supports the capability of “rxTimingDiff-r18”, the UE is only required to be tested in Test2 and Test4.

Table A.6.4.1.2.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.6.4.1.2.1-3: SRS Configuration for Timing Accuracy Test

## A.6.4.1.2.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1) Setup NR PCell according to parameters given in table A.6.4.1.1.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected path of DL SSB of TRP#1 and TRP#2.

a.The NTA offset value (in Tc units) is 25600

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.6.4.1.2.2-1 for only TRP#1. The timing of the DL path of TRP#2 is not changed.

Table A.6.4.1.2.2-1: Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 Table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first path (in time) of DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna for TRP#1. For TRP#2, the test system shall verify there is no adjustment. Skip this step for test 3&4 with DRX configured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first path (in time) of DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna of TRP#1. For Test 3&4 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.6.4.1.3NR UE Transmit Timing Test with 2-TA and two TRPs for FR1 UE supporting single DCI

## A.6.4.1.3.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNB and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits for UE not configured PL offset and is configured with 2 TAGs for

single-DCI multi-TRP operation. The test is configured with two TRPs in NR PCell. This test will verify the requirements in clause 7.1.2.

Supported test configurations are shown in table A.6.4.1.1.1-1.

Table A.6.4.1.3.1-1: Supported test configurations for FR1 PCell

For this test a single NR cell is used. Table A.6.4.1.3.1-2 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration defined in table A.6.4.1.3.1-3.

Table A.6.4.1.3.1-2: Cell Specific Test Parameters for UL Transmit Timing test

Table A.6.4.1.3.1-3: SRS Configuration for Timing Accuracy Test

## A.6.4.1.3.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1)Setup NR PCell according to parameters given in table A.6.4.1.1.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset) ×Tc ± Te of the first detected corresponding path of DL SSB (index 0) for each TAG and detected another path of DL SSB (index 1).

a.The NTA offset value (in Tc units) is 25600

b.The Te values depend on the DL and UL SCS for which the test is being run and are given in table 7.1.2-1

3)The test system shall adjust the timing of the DL path by values given in table A.6.4.1.3.2-1 for only TRP#1. The timing of the DL path of TRP#2 is not changed.

Table A.6.4.1.3.2-1: Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1.2 Table 7.1.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset) ×Tc ± Te respective to the first path (in time) of corresponding DL SSB (TRP#1) of each TAG used by the UE to determine downlink timing is received from the reference cell at UE antenna. For TRP#2, the test system shall verify there is adjusted as well. Skip this step for test 2 with DRX configured.

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset) ×Tc ± Te of the first path (in time) of corresponding DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna of TRP#1 for each TAG. For Test 2 the UE transmit timing offset shall be verified for the first transmission in the DRX cycle immediately after DL timing adjustment.

## A.6.4.2UE timer accuracy

## A.6.4.3Timing advance

## A.6.4.3.1SA FR1 timing advance adjustment accuracy

## A.6.4.3.1.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3.

## A.6.4.3.1.2Test Parameters

Supported test configurations are shown in table A.6.4.3.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.6.4.3.1.2-2, A.6.4.3.1.2-3 and A.6.4.3.1.2-4.

In all test cases, single cell is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.6.4.3.1.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to and clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.6.4.3.1.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k+1 for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.6.4.3.1.2-1: Timing advance supported test configurations

Table A.6.4.3.1.2-2: General test parameters for timing advance

Table A.6.4.3.1.2-3: Cell specific test parameters for timing advance

Table A.6.4.3.1.2-4: Sounding Reference Symbol Configuration for timing advance

## A.6.4.3.1.3Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k=5.

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.6.4.3.2SA FR1 timing advance adjustment accuracy for asymmetric DL sTRP/UL mTRP deployment with two TAs

## A.6.4.3.2.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3 for asymmetric DL sTRP/UL mTRP deployment with two TAs when PL-offset is configured joint/UL TCI state(s).

## A.6.4.3.2.2Test Parameters

Supported test configurations are shown in table A.6.4.3.2.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.6.4.3.2.2-2, A.6.4.3.2.2-3 and A.6.4.3.2.2-4.

In all test cases, single cell is used. The cell is configured with two TRPs in the test. UE is also configured with tag2 in ServingCellConfig. Two SRS resource sets are configured and associated to different TAGs via TCI state configuration. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands for two TRP are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.6.4.3.2.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured for each TRP.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31 and 16 respectively for TRP1 and TRP2, which according to and clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance for TRP1 and TRP2 used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements for both TRPs, with Timing Advance Command value specified in table A.6.4.3.2.2-2. This value shall result in changes of the timing advance for TRP1 and TRP2 used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE for both TRPs.

As specified in clause 7.3.2.1, the UE adjusts its uplink timing at slot n+k+1 for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Table A.6.4.3.2.2-1: Timing advance supported test configurations

Table A.6.4.3.2.2-2: General test parameters for timing advance

Table A.6.4.3.2.2-3: Cell specific test parameters for timing advance

Table A.6.4.3.2.2-4: Sounding Reference Symbol Configuration for timing advance

## A.6.4.3.2.3Test Requirements

The UE shall apply the signalled Timing Advance value for TRP1 and TRP2 to the transmission timing at the designated activation time i.e. k+1 slots after the reception of the timing advance command, where k=5.

The Timing Advance adjustment accuracy for TRP1 and TRP2 shall be within the limits specified in clause 7.3.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.6.5Signalling characteristics

## A.6.5.1Radio link Monitoring

In the following clause, any uplink signal transmitted by the UE is used for detecting the In-/Out-of-Sync state of the UE. In terms of measurement, the uplink signal is verified on the basis of the UE output power:

For intra-band contiguous carrier aggregation, transmit OFF power is measured as the mean power per component carrier.

For UE with multiple transmit antennas, transmit OFF power is measured as the mean power at each transmit connector.

-UE output power higher than Transmit OFF power -50 dBm (as defined in TS 38.101-1 [18]) means uplink signal

-UE output power equal to or less than Transmit OFF power -50 dBm (as defined in TS 38.101-1 [18]) means no uplink signal.

## A.6.5.1.1Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode

## A.6.5.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.6.5.1.1.1-1. The test parameters are given in tables A.6.5.1.1.1-2, A.6.5.1.1.1-3, and A.6.5.1.1.1-4 below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.6.5.1.1.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

Table A.6.5.1.1.1-1: Supported test configurations for FR1 PCell

Table A.6.5.1.1.1-2: General test parameters for FR1 out-of-sync testing in non-DRX mode

Table A.6.5.1.1.1-3: Cell specific test parameters for FR1 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode

Table A.6.5.1.1.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

Figure A.6.5.1.1.1-1: SNR variation for out-of-sync testing

## A.6.5.1.1.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.1.2Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode

## A.6.5.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.6.5.1.2.1-1. The test parameters are given in tables A.6.5.1.2.1-2, and A.6.5.1.2.1-3 below. There is one cell (Cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.6.5.1.2.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

Table A.6.5.1.2.1-1: Supported test configurations for FR1 PCell

Table A.6.5.1.2.1-2: General test parameters for FR1 in-sync testing in non-DRX mode

Table A.6.5.1.2.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in non-DRX mode

Table A.6.5.1.2.1-4: Void

Figure A.6.5.1.2.1-1: SNR variation for in-sync testing

## A.6.5.1.2.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.1.3Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode

## A.6.5.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.6.5.1.3.1-1. The test parameters are given in tables A.6.5.1.3.1-2, and A.6.5.1.3.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.6.5.1.3.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.6.5.1.3.1-1: Supported test configurations for FR1 PCell

Table A.6.5.1.3.1-2: General test parameters for FR1 out-of-sync testing in DRX mode

Table A.6.5.1.3.1-3: Cell specific test parameters for FR1 (Cell 1) for out-of-sync radio link monitoring tests in DRX mode

Table A.6.5.1.3.1-4: Void

Table A.6.5.1.3.1-5: Void

Table A.6.5.1.3.1-6: Void

Figure A.6.5.1.3.1-1: SNR variation for out-of-sync testing

## A.6.5.1.3.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.1.4Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode

## A.6.5.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.6.5.1.4.1-1. The test parameters are given in tables A.6.5.1.4.1-2, and A.6.5.1.4.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.6.5.1.4.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.6.5.1.4.1-1: Supported test configurations for FR1 PCell

Table A.6.5.1.4.1-2: General test parameters for FR1 in-sync testing in DRX mode

Table A.6.5.1.4.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in DRX mode

Table A.6.5.1.4.1-4: Void

Table A.6.5.1.4.1-5: Void

Figure A.6.5.1.4.1-1: SNR variation for in-sync testing.

## A.6.5.1.4.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.1.5Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode

## A.6.5.1.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used. This test will partly verify the FR1 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in tables A.6.5.1.5.1-1, A.6.5.1.5.1-2, A.6.5.1.5.1-3, and A.6.5.1.5.1-3A below. There is one cell, Cell 1 which is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.6.5.1.5.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting of 5 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 is configured as the BFD-RS.

Table A.6.5.1.5.1-1: Supported test configurations for FR1 PCell

Table A.6.5.1.5.1-2: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in non-DRX mode

Table A.6.5.1.5.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.6.5.1.5.1-3A: Measurement gap configuration for FR1 CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.6.5.1.5.1-4: Void

Figure A.6.5.1.5.1-1: SNR variation for CSI-RS out-of-sync testing

## A.6.5.1.5.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 no later than time point C (D1 ms after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.1.6Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode

## A.6.5.1.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used. This test will partly verify the FR1 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in tables A.6.5.1.6.1-1, A.6.5.1.6.1-2, and A.6.5.1.6.1-3 below. There is one cells, Cell 1which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.6.5.1.6.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled. In the test, SSB0 is configured as the BFD-RS.

Table A.6.5.1.6.1-1: Supported test configurations for FR1 PCell

Table A.6.5.1.6.1-2: General test parameters for FR1 PCell for CSI-RS in-sync testing in non-DRX mode

Table A.6.5.1.6.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in non-DRX mode

Table A.6.5.1.6.1-4: Void

Figure A.6.5.1.6.1-1: SNR variation for CSI-RS in-sync testing

## A.6.5.1.6.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.1.7Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode

## A.6.5.1.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when DRX is used. This test will partly verify the FR1 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in tables A.6.5.1.7.1-1, A.6.5.1.7.1-2, and A.6.5.1.7.1-3 below. There is one cell, Cell 1 is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.6.5.1.7.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test. In the test, SSB0 is configured as the BFD-RS.

Table A.6.5.1.7.1-1: Supported test configurations for FR1 PCell

Table A.6.5.1.7.1-2: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in DRX mode

Table A.6.5.1.7.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in DRX mode

Table A.6.5.1.7.1-4: Void

Table A.6.5.1.7.1-5: Void

Table A.6.5.1.7.1-6: Void

Figure A.6.5.1.7.1-1: SNR variation for CSI-RS out-of-sync testing

## A.6.5.1.7.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 (PCell) at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 (PCell) no later than time point C (D1 ms after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.1.8Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode

## A.6.5.1.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when DRX is used. This test will partly verify the FR1 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in tables A.6.5.1.8.1-1, A.6.5.1.81-2, A.6.5.1.8.1-3 and A.6.5.1.8.1-3A below. There is one cells, Cell 1which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.6.5.1.8.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 is configured as the BFD-RS.

Table A.6.5.1.8.1-1: Supported test configurations for FR1 PSCell

Table A.6.5.1.8.1-2: General test parameters for FR1 PCell for CSI-RS in-sync testing in non-DRX mode

Table A.6.5.1.8.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in non-DRX mode

Table A.6.5.1.8.1-3A: Measurement gap configuration for FR1 CSI-RS in-sync radio link monitoring in non-DRX mode

Table A.6.5.1.8.1-4: Void

Table A.6.5.1.8.1-5: Void

Table A.6.5.1.8.1-6: Void

Figure A.6.5.1.8.1-1: SNR variation for CSI-RS in-sync testing

## A.6.5.1.8.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.1.9Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM for UE fulfilling relaxed measurement criterion

## A.6.5.1.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when DRX is used. This test will partly verify the FR1 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1.3.4 for UE fulfilling good serving cell quality criterion.

The test parameters are given in tables A.6.5.1.9.1-1, A.6.5.1.9.1-2, and A.6.5.1.9.1-3 below. There is one cell, Cell 1 is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.6.5.1.9.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test. In the test, SSB0 is configured as the BFD-RS.

Table A.6.5.1.9.1-1: Supported test configurations for FR1 PCell

Table A.6.5.1.9.1-2: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in DRX mode

Table A.6.5.1.9.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in DRX mode

Figure A.6.5.1.9.1-1: SNR variation for CSI-RS out-of-sync testing

## A.6.5.1.9.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 (PCell) at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 (PCell) no later than time point C (D1 ms after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.1.10Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP

## A.6.5.1.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used and when CD-SSB is outside active BWP. This test will partly verify the FR1 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1.

The test is for UE supporting rlm-BM-BFD-CSI-RS-OutsideActiveBWP-r18 and the UE is not required past legacy test in clause A.6.5.1.5.

The test environment is the same as in clause A.6.5.1.5 with following exceptions in Table A.6.5.1.5.1-2.

The value of parameter “DL dedicated BWP configuration” is DLBWP.1.2. The value of parameter “UL dedicated BWP configuration” is ULBWP.1.2.

NOTE: The starting PRB index of the SSB can be any possible PRB index of the RF channel BW occurring after the last PRB of the DL active BWP.

The test requirements are the same as for A.6.5.1.5.2.

## A.6.5.1.11Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP

## A.6.5.1.11.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting bwpOperationMeasWithoutInterrupt-r18 properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when CD-SSB is outside active BWP. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1.

The test environment is the same as in clause A.6.5.1.1 with following exceptions in table A.6.5.1.1.1-2.

## A.6.5.1.11.2Test Requirements

The test requirements are the same as in clause A.6.5.1.1.2.

## A.6.5.1.12Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP

## A.6.5.1.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell for UE supporting FG 53-3. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.6.5.1.12.1-1. The test parameters are given in tables A.6.5.1.12.1-2, A.6.5.1.12.1-3, and A.6.5.1.12.1-4 below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.6.5.1.12.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

Table A.6.5.1.12.1-1: Supported test configurations for FR1 PCell for UE supporting FG NCD-SSB based measurement outside active BWP

Table A.6.5.1.12.1-2: General test parameters for FR1 out-of-sync testing in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP

Table A.6.5.1.12.1-3: Cell specific test parameters for FR1 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP

Table A.6.5.1.12.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

Figure A.6.5.1.12.1-1: SNR variation for out-of-sync testing

## A.6.5.1.12.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.1.13Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for UE operating on a cell with less than 5 MHz BW

## A.6.5.1.13.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting support3MHz-ChannelBW-Symmetric-r18 properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell operating on a 3 MHz channel bandwidth. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1.

Supported test configurations are specified in table A.6.5.1.13.1-1. General test parameters as specified in table A.6.5.1.3.1-2 with config 1 apply except those specified in table A.6.5.1.13.1-2. Cell specific test parameters as specified in table A.6.5.1.3.1-3 apply except those specified in table A.6.5.1.13.1-3.

The test procedure specified in clause A.6.5.1.3.1 applies to this test.

Table A.6.5.1.13.1-1: Supported test configurations for FR1 PCell

Table A.6.5.1.13.1-2: General test parameters for FR1 OOS 12 PRB in DRX mode

Table A.6.5.1.13.1-3: Cell specific test parameters for FR1 OOS 12 PRB in DRX mode

## A.6.5.1.13.2Test Requirements

Test requirements specified in clause A.6.5.1.3.2 apply to this test.

## A.6.5.1.14Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for UE operating on a cell with less than 5 MHz BW

## A.6.5.1.14.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting support3MHz-ChannelBW-Symmetric-r18 properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell operating on a 3 MHz channel bandwidth. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1.

Supported test configurations are specified in table A.6.5.1.14.1-1. General test parameters as specified in table A.6.5.1.1.1-2 with config 1 apply except those specified in table A.6.5.1.14.1-2. Cell specific test parameters as specified in table A.6.5.1.1.1-3 apply except those specified in table A.6.5.1.14.1-3.

The test procedure specified in clause A.6.5.1.1.1 applies to this test.

Table A.6.5.1.14.1-1: Supported test configurations for FR1 PCell

Table A.6.5.1.14.1-2: General test parameters for FR1 OOS 15 PRB in DRX mode

Table A.6.5.1.14.1-3: Cell specific test parameters for FR1 PCell

## A.6.5.1.14.2Test Requirements

Test requirements specified in clause A.6.5.1.1.2 apply to this test.

## A.6.5.1.15Radio Link Monitoring In-sync Test for FR1 PCell with 3 MHz Channel Bandwidth configured with SSB-based RLM RS in non-DRX mode

## A.6.5.1.15.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting support3MHz-ChannelBW-Symmetric-r18 properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell operating on a 3 MHz channel bandwidth. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1.

Supported test configurations are specified in table A.6.5.1.15.1-1. General test parameters as specified in table A.6.5.1.2.1-2 with config 1 apply to this test for both config 1 and 2, except those specified in table A.6.5.1.15.1-2. Cell specific test parameters as specified in table A.6.5.1.2.1-3 apply except those specified in table A.6.5.1.15.1-3.

The test procedure specified in clause A.6.5.1.2.1 applies to this test.

Table A.6.5.1.15.1-1: Supported test configurations for FR1 PCell

Table A.6.5.1.15.1-2: General test parameters for FR1 in-sync testing in non-DRX mode

Table A.6.5.1.15.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in non-DRX mode

## A.6.5.1.15.2Test Requirements

Test requirements specified in clause A.6.5.1.2.2 apply to this test.

## A.6.5.1.16Radio Link Monitoring In-sync Test for FR1 PCell with 3MHz Channel Bandwidth configured with SSB-based RLM RS in DRX mode

## A.6.5.1.16.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting support3MHz-ChannelBW-Symmetric-r18 properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell operating on a 3MHz channel bandwidth. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1.

Supported test configurations are specified in Table A.6.5.1.16.1-1. General test parameters as specified in Table A.6.5.1.4.1- with config 1 apply to this test, except those specified in Table A.6.5.1.16.1-2. Cell specific test parameters as specified in Table A.6.5.1.4.1-3 apply except those specified in Table A.6.5.1.16.1-3.

The test procedure specified in A.6.5.1.4.1 applies to this test.

Table A.6.5.1.16.1-1: Supported test configurations for FR1 PCell

Table A.6.5.1.16.1-2: General test parameters for FR1 in-sync testing in non-DRX mode

Table A.6.5.1.16.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in non-DRX mode

## A.6.5.1.16.2Test Requirements

## Test requirements specified in Clause A.6.5.1.4.2 apply to this test.A.6.5.1.17Radio Link Monitoring Out-of-sync Test for FR1 PCell with LowBandCA-Switching-r19 configured with SSB-based RLM RS in non-DRX mode

## A.6.5.1.17.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting featureSetCombinationLowBandSwitching-r19 properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.6.5.1.17.1-1. The test parameters are given in tables A.6.5.1.17.1-2 and A.6.5.1.17.1-3 below. There are two cells, Cell 1 is the FDD PCell and Cell 2 is the SDL SCell, in the test. The PCell and SCell are co-located deployed and synchronized with 3us MRTD. The frequencies of PCell and SCell are lower than 1GHz. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.6.5.1.17.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

Table A.6.5.1.17.1-1: Supported test configurations for FR1 PCell and SCell

Table A.6.5.1.17.1-2: General test parameters for FR1 out-of-sync testing in non-DRX mode

Table A.6.5.1.17.1-3: Cell specific test parameters for FR1 (Cell 1 and Cell 2) for out-of-sync radio link monitoring tests in non-DRX mode

Figure A.6.5.1.17.1-1: SNR variation for out-of-sync testing

## A.6.5.1.17.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting and overlapped with FDD PCell ON duration corresponding to the LB CA switching pattern.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.1.18Radio Link Monitoring In-sync Test for FR1 PCell with LowBandCA-Switching-r19 configured with SSB-based RLM RS in non-DRX mode

## A.6.5.1.18.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting featureSetCombinationLowBandSwitching-r19 properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.6.5.1.18.1-1. The test parameters are given in tables A.6.5.1.18.1-2, and A.6.5.1.18.1-3 below. There are two cells, Cell 1 is the FDD PCell and Cell 2 is the SDL SCell, in the test. The PCell and SCell are co-located deployed and synchronized with 3us MRTD. The frequencies of PCell and SCell are lower than 1GHz. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.6.5.1.18.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

Table A.6.5.1.18.1-1: Supported test configurations for FR1 PCell

Table A.6.5.1.18.1-2: General test parameters for FR1 in-sync testing in non-DRX mode

Table A.6.5.1.18.1-3: Cell specific test parameters for FR1 (Cell 1 and Cell 2) for in-sync radio link monitoring tests in non-DRX mode

Figure A.6.5.1.18.1-1: SNR variation for in-sync testing

## A.6.5.1.18.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting and overlapped with FDD PCell ON duration corresponding to the LB CA switching pattern.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.1.19Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for a UE operating with SBFD

## A.6.5.1.19.1Test Purpose and Environment

The purpose of this test is to verify that when the UE supports supportSBFD and SBFD is configured by the network, the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when there are overlapping between occasions of the CSI-RS resource for RLM and dynamic UL transmission on SBFD symbols. This test will partly verify the FR1 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in tables A.6.5.1.19.1-1, A.6.5.1.19.1-2, A.6.5.1.19.1-3 and A.6.5.1.19.1-4 below. There is one cells, Cell 1which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.6.5.1.19.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 is configured as the BFD-RS.

CSI-RS resource for RLM are on SBFD symbols. During T5, there is overlapping between occasions of the CSI-RS resource for RLM and dynamic UL transmission on SBFD symbols, as specified in A.3.

Table A.6.5.1.19.1-1: Supported test configurations for FR1 PSCell

Table A.6.5.1.19.1-2: General test parameters for FR1 PCell for CSI-RS in-sync testing in DRX mode

Table A.6.5.1.19.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in DRX mode

Table A.6.5.1.19.1-4: Measurement gap configuration for FR1 CSI-RS in-sync radio link monitoring in DRX mode

Figure A.6.5.1.19.1-1: SNR variation for CSI-RS in-sync testing

## A.6.5.1.19.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.2Interruption

## A.6.5.2.1Interruptions during measurements on deactivated NR SCC in FR1

## A.6.5.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE missed ACK/NACK rate does not exceed the limits at NR PCell interruptions during the measurement on the deactivated NR SCC. This test will verify the missed ACK/NACK rate for PCell in standalone NR specified in clause 8.2.2.2.3. Supported test configurations for NR PCell are shown in table A.6.5.2.1.1-1. Supported test configurations for NR SCell are shown in table A.6.5.2.1.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently.

The general test parameters and NR cell specific test parameters are given in Table A.6.5.2.1.1-2, A.6.5.2.1.1-3 and A.6.5.2.1.1-4 below. In the test there are two cells: Cell1 and Cell2. Cell1 is PCell, Cell2 is an NR deactivated SCell. Cell1 shall be configured as PCell and Cell2 shall be configured as SCell.

The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE is connected to Cell1 and Cell2 and the RRC message including measCycleSCell or allowInterruptions for the deactivated NR SCell is received at the UE antenna connector. During T1, PCell is continuously scheduled in DL.

Table A.6.5.2.1.1-1: Interruptions during measurements on deactivated NR SCC supported test configurations for NR PCell

Table A.6.5.2.1.1-1A: Interruptions during measurements on deactivated NR SCC supported test configurations for NR SCell

Table A.6.5.2.1.1-2: General test parameters for interruptions during measurements on deactivated NR SCC in standalone NR

Table A.6.5.2.1.1-3: NR cell specific test parameters for NR PCell for interruptions during measurements on deactivated NR SCC in standalone NR

Table A.6.5.2.1.1-4: NR cell specific test parameters for NR SCell for interruptions during measurements on deactivated NR SCC in standalone NR

## A.6.5.2.1.2Test Requirements

The UE shall be continuously scheduled on PCell during the entire length of T1. During the time duration T1 the UE shall transmit at least 99.5 % of ACK/NACK on PCell.

If the NR PCell is not in the same band as the deactivated SCell, the UE is only allowed to cause interruptions on NR PCell immediately before and immediately after an SMTC. Each interruption on NR PCell shall not exceed the value defined in table A.6.5.2.1.2-1.

If the NR PCell is non-contiguous to the deactivated SCell in the same band and UE is capable of intraBandNRCA-NonCollocated-r18 on this FR1 bnad and nonCollocatedTypeNR-CA-r18 is not provided, the UE is only allowed to cause interruptions on NR PCell immediately before and immediately after an SMTC. Each interruption on NR PCell shall not exceed the value defined in table A.6.5.2.1.2-1.

If the NR PCell is non-contiguous to the deactivated SCell in the same band, when UE is not capable of intraBandNRCA-NonCollocated-r18 or when UE is capable ofintraBandNRCA-NonCollocated-r18 and provided with nonCollocatedTypeNR-CA-r18, the UE is only allowed to cause an interruption on PCell no earlier than 1 slot before an SMTC and no later than 1 slot after the SMTC. The interruption on NR PCell shall not exceed the value defined in table A.6.5.2.1.2-2.

If the NR PCell is contiguous to the deactivated SCell in the same band, the UE is only allowed to cause an interruption on PCell no earlier than 1 slot before an SMTC and no later than 1 slot after the SMTC. The interruption on NR PCell shall not exceed the value defined in table A.6.5.2.1.2-2.

Table A.6.5.2.1.2-1: Interruption duration if the PCell is not in the same band as the deactivated SCell

Table A.6.5.2.1.2-2: Interruption duration if the PCell is in the same band as the deactivated SCell

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.2.1AInterruptions during measurements on deactivated NR SCC in FR1 for UE supporting intraBandNR-CA-non-collocated-r19

## A.6.5.2.1A.1Test Purpose and Environment

The purpose of this test is to verify that the UE missed ACK/NACK rate does not exceed the limits at NR PSCell interruptions during the measurement on the deactivated NR SCC for UE supporting intraBandNR-CA-non-collocated-r19. This test will verify the missed ACK/NACK rate for PCell in standalone NR specified in clause 8.2.2.2. Supported test configurations for NR PCell are shown in table A.6.5.2.1A.1-1. Supported test configurations for NR SCell are shown in table A.6.5.2.1A.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently.

The general test parameters and NR cell specific test parameters are given in table A.6.5.2.1A.1-2, A.6.5.2.1A.1-3 and A.6.5.2.1A.1-4 below. In the test there are two cells: Cell 1 and Cell 2. Cell 1 is PCell, Cell 2 is an NR deactivated SCell. Cell 1 shall be configured as PCell and Cell 2 shall be configured as SCell.

There are four sub tests in this section.

In test 1, the UE is configured with maxMIMO-Layers with value equal to 4, and nonCollocatedTypeNR-CA-v1900 is presented with “type 4”.

In test 2, the UE is configured with maxMIMO-Layers with value equal to 4, and nonCollocatedTypeNR-CA-v1900 is presented with “type 1”.

In test 3, the UE is configured with maxMIMO-Layers with value equal to 4, and nonCollocatedTypeNR-CA-v1900 is not provided.

In test 4, the UE is configured with maxMIMO-Layers with value equal to 2.

The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell 2 and the RRC message including measCycleSCell or allowInterruptions for the deactivated NR SCells is received at the UE antenna connector. During T1, PCell is continuously scheduled in DL.

Table A.6.5.2.1A.1-1: Interruptions during measurements on deactivated NR SCC supported test configurations for NR PCell

Table A.6.5.2.1A.1-1A: Interruptions during measurements on deactivated NR SCC supported test configurations for NR SCell

Table A.6.5.2.1A.1-2: General test parameters for interruptions during measurements on deactivated NR SCC in standalone NR

Table A.6.5.2.1A.1-3: NR cell specific test parameters for NR PCell for interruptions during measurements on deactivated NR SCC in standalone NR

Table A.6.5.2.1A.1-4: NR cell specific test parameters for NR SCell for interruptions during measurements on deactivated NR SCC in standalone NR

## A.6.5.2.1A.2Test Requirements

The NR PCell is non-contiguous to the deactivated SCell in the same band, and the UE is capable of intraBandNR-CA-non-collocated-r19. The UE shall be continuously scheduled on PCell during the entire length of T1. During the time duration T1 the UE shall transmit at least 99.5 % of ACK/NACK on PCell.

For test 1, the UE is only allowed to cause interruptions on NR PCell immediately before and immediately after an SMTC. Each interruption on NR PCell shall not exceed the value defined in table A.6.5.2.1.2-1.

For test 2 and test 3, the UE is only allowed to cause an interruption on PCell no earlier than 1 slot before an SMTC and no later than 1 slot after the SMTC. The interruption on NR PCell shall not exceed the value defined in table A.6.5.2.1.2-2.

For test 4, if nonCollocatedTypeNR-CA-r18 is not provided, the UE is only allowed to cause interruptions on NR PCell immediately before and immediately after an SMTC. Each interruption on NR PCell shall not exceed the value defined in table A.6.5.2.1.2-1. If nonCollocatedTypeNR-CA-r18 is provided, the UE is only allowed to cause an interruption on PCell no earlier than 1 slot before an SMTC and no later than 1 slot after the SMTC. The interruption on NR PCell shall not exceed the value defined in table A.6.5.2.1.2-2.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.2.2SA interruptions at NR SRS carrier based switching

## A.6.5.2.2.1Test Purpose and Environment

The purpose of this test is to verify that when a UE needs to transmit aperiodic SRS, the UE can perform carrier based switching to one carrier not configured for PUCCH/PUSCH transmission from a carrier with PUCCH/PUSCH transmission. The test will partly verify the UE missed ACK/NACK does not exceed the interruption requirements on PCell in clause 8.2.2.2.9.

## A.6.5.2.2.2Test Parameters

which operates in downlink without PUCCH/PUSCH. The UE is configured with the SRS switching between PCell and SCell. The test parameters for PCell and SCell are given in table A.6.5.2.2.2-2 and A.6.5.2.2.2-3 below. The test consists of two successive time periods, with duration of T1 and T2, respectively. Immediately at the beginning of T2, the UE is triggered for SRS switching by DCI 2_3 scheduling. After T2, the UE is expected to transmit aperiodic SRS on a special slot in the configured TDD UL/DL configuration, as scheduled by DCI 2_3.

The test equipment verifies that potential interruption is carried out correctly by monitoring ACK/NACK sent in PCell.

Table A.6.5.2.2.2-1: Supported test configurations

Table A.6.5.2.2.2-2: General test parameters for SA interruptions at NR SRS carrier based switching

Table A.6.5.2.2.2-3: Cell specific test parameters for SA interruptions at NR SRS carrier based switching

Table A.6.5.2.2.2-4: Void

## A.6.5.2.2.3Test Requirements

The UE shall be scheduled on PCell continuously throughout the test. During the time duration T2, the missed ACK/NACK interruption on PCell shall not be more than the values specified for SA in clause 8.2.2.2.9.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.2.3SA interruptions at NR SRS antenna port switching with 1 SRS symbol in a slot in NR-CA

## A.6.5.2.3.1Test Purpose and Environment

The purpose of this test is to verify that when a UE performs SRS antenna port switching, i.e. transmits SRS on the antenna port(s) not used for PUCCH/PUSCH transmission and on the antenna port(s) used for PUCCH/PUSCH transmission at different SRS transmission occasions. The test will partly verify the interruption requirements on PCell and SCell in clause 8.2.2.2.16. The interruption requirement is defined based on the band combination capability reported by UE, i.e., based on txSwitchImpactToRx or txSwitchWithAnotherBand as specified in requirement applicability in clause 8.2.2.2.16.

## A.6.5.2.3.2Test Parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the FR1 PCell and Cell 2 is activated SCell. Only PCC may be configured with more than 1 SRS resources in each SRS resource set with usage set to ‘antennaSwitching’. The test parameters for PCell and SCell are given in Table A.6.5.2.3.2-2 and A.6.5.2.3.2-3 below. The test consists of two successive time periods, with duration of T1 and T2, respectively. Immediately at the beginning of T2, the UE is configured with periodic SRS for antenna port switching via RRC reconfiguration. Note that the RRC reconfiguration message should be sent to UE at the time 50ms before the beginning of T2.

The test equipment verifies that potential interruption is carried out correctly by monitoring ACK/NACK sent in SCell.

Table A.6.5.2.3.2-1: Supported test configurations

Table A.6.5.2.3.2-2: General test parameters for SA interruptions at NR SRS antenna switching

Table A.6.5.2.3.2-3: Cell specific test parameters for SA interruptions at NR SRS antenna switching

Table A.6.5.2.3.2-4: SRSConf.1 Specific Sounding Reference Symbol Configuration for xTyR configuration

Table A.6.5.2.3.2-5: SRSConf.2 Specific Sounding Reference Symbol Configuration for xTyR configuration

## A.6.5.2.3.3Test Requirements

The UE shall be scheduled on SCell continuously throughout the test.

During the time duration T2, the DL interruption on NR SCell during the SRS antenna switching in each SRS transmission slot on NR PCell shall not exceed 1 slot if SCell is indicated in txSwitchImpactToRx.

During the time duration T2, the UL interruption on NR SCell during the SRS antenna switching in each SRS transmission slot on NR PCell shall not exceed 1 slot if SCell is indicated in txSwitchWithAnotherBand.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.2.4SA interruptions at NR SRS antenna port switching

## A.6.5.2.4.1Test Purpose and Environment

The purpose of this test is to verify the interruption requirement on victim CC during SRS antenna port switching with more than 1 SRS symbols on aggressor CC defined in clause 8.2.2.2.16. The interruption requirement is defined based on the band combination capability reported by UE, i.e., based on txSwitchImpactToRx or txSwitchWithAnotherBand as specified in requirement applicability in clause 8.2.2.2.16.

## A.6.5.2.4.2Test Parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the FR1 PCell and Cell 2 is FR1 SCell. The UE is configured with the SRS antenna port in FR1 PCell. The test parameters for PCell and SCell are given in table A.6.5.2.4.2-2 and A.6.5.2.4.2-3 below. Common SRS configuration is given in clause A.3.24. Dedicated SRS configuration which is dependent on reported SRS capability supportedSRS-TxPortSwitch, is given in table A.6.5.2.4.2-4. The test consists of two successive time periods, with duration of T1 and T2, respectively. Immediately at the beginning of T2, the UE is triggered for SRS antenna port switching.

The test equipment verifies that potential interruption is carried out correctly by monitoring ACK/NACK sent in PCell.

Table A.6.5.2.4.2-1: Supported test configurations

Table A.6.5.2.4.2-2: General test parameters for SA interruptions at NR SRS antenna port switching

Table A.6.5.2.4.2-3: Cell specific test parameters for SA interruptions at NR SRS antenna port switching

Table A.6.5.2.4.2-4: SRSConf.1 Dedicated Sounding Reference Symbol Configuration for xTyR configuration

Table A.6.5.2.4.2-5: SRSConf.2 Dedicated Sounding Reference Symbol Configuration for xTyR configuration

## A.6.5.2.4.3Test Requirements

The UE shall be scheduled on PCell continuously throughout the test. During the time duration T2, the interruption on SCell shall not be more than the values specified in table 8.2.1.2.18-3 in clause 8.2.1.2.18 for each SRS transmission slot.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.2.5Interruptions during measurements on deactivated NR SCC in FR1

## A.6.5.2.5.1Test Purpose and Environment

The purpose of this test is to verify that a UE supporting LBCA-SwitchingPattern performs correct interruption requirements on PCell, where the UE missed ACK/NACK rate does not exceed the limits at NR PSCell interruptions during the measurement on the deactivated NR SCC. This test will verify the missed ACK/NACK rate for PCell in standalone NR specified in clause 8.2.2.2. Supported test configurations for NR PCell are shown in table A.6.5.2.5.1-1. Supported test configurations for NR SCell are shown in table A.6.5.2.5.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently.

The general test parameters and NR cell specific test parameters are given in table A.6.5.2.5.1-2, A.6.5.2.5.1-3 and A.6.5.2.5.1-4 below. In the test there are two cells: Cell 1 and Cell 2. Cell 1 is PCell, Cell 2 is an NR deactivated SCell. Cell 1 shall be configured as PCell and Cell 2 shall be configured as SCell.

The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell 2 and the RRC message including measCycleSCell or allowInterruptions for the deactivated NR SCells is received at the UE antenna connector. During T1, PCell is continuously scheduled in DL.

Table A.6.5.2.5.1-1: Interruptions during measurements on deactivated NR SCC supported test configurations for NR PCell

Table A.6.5.2.5.1-2: General test parameters for interruptions during measurements on deactivated NR SCC in standalone NR

Table A.6.5.2.5.1-3: NR cell specific test parameters for NR PCell for interruptions during measurements on deactivated NR SCC in standalone NR

Table A.6.5.2.5.1-4: NR cell specific test parameters for NR SCell for interruptions during measurements on deactivated NR SCC in standalone NR

## A.6.5.2.5.2Test Requirements

The UE shall be continuously scheduled on PCell during the entire length of T1. During the time duration T1 the UE shall transmit at least 99.5 % of ACK/NACK on PCell.

The UE is only allowed to cause interruptions on NR PCell immediately before and immediately after an SMTC. Each interruption on NR PCell shall not exceed the value defined in table A.6.5.2.5.2-1.

Table A.6.5.2.5.2-1: Interruption duration if the PCell is in the same band as the deactivated SCell

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.3SCell Activation and Deactivation Delay

## A.6.5.3.1SCell Activation and deactivation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle

## A.6.5.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3, when the SCell in FR1 is known by the UE at the time of activation.

The supported test configurations for NR PCell are shown in table A.6.5.3.1.1-1 below. Supported test configurations for NR SCell are shown in table A.6.5.3.1.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently. The test parameters are given in tables A.6.5.3.1.1-2 and cell-specific parameters in tables A.6.5.3.1.1-3 and A.6.5.3.1.1-4 below. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in 5.2.2.5 in [26], and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3, and The starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.6.5.3.1.1-1: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR PCell

Table A.6.5.3.1.1-1A: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR SCell

Table A.6.5.3.1.1-2: General test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.6.5.3.1.1-3: Cell specific test parameters for NR PCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.6.5.3.1.1-4: Cell specific test parameters for NR SCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

## A.6.5.3.1.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in clause 5.2.2.5 in TS 38.214 [26], and reporting after slot (). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.n+1+THARQ+3 msNR slot length

During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , Tactivation_time = TFirstSSB+ 5ms, as defined in clause 8.3.n+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

During T3 the UE shall stop sending CSI reports for SCell at latest in a slot , as defined in clause 8.3.m+THARQ+3 msNR slot length

During T2 interruption of PCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.6.5.3.2SCell Activation and deactivation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle

## A.6.5.3.2.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.6.5.3.1.1. The supported test configurations are the same as defined in clause A.6.5.3.1.1. The test parameters are the same except those described in the following clause. The listed parameter values in tables A.6.5.3.2.1-1 will replace the values of corresponding parameters in tables A.6.5.3.1.1-1.

Table A.6.5.3.2.1-1: General test parameters for known FR1 SCell activation case, 640 ms SCell measurement cycle

## A.6.5.3.2.2Test Requirements

The test requirements defined in clause A.6.5.3.1.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstSSB_MAX + Trs + 5 ms.

## A.6.5.3.3SCell Activation and deactivation of unknown SCell in FR1 in non-DRX

## A.6.5.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3, when the SCell in FR1 is known by the UE at the time of activation.

The supported test configurations are shown in table A.6.5.3.1.1-1 and table A.6.5.3.1.1-1A. The test parameters are given in table A.6.5.3.1.1-2 and cell-specific parameters in table A.6.5.3.1.1-3. The listed parameter values in table A.6.5.3.3.1-1 will replace the values of corresponding parameters in table A.6.5.3.1.1-2. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in 5.2.2.5 in [26], and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3, and The starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.6.5.3.3.1-1: General test parameters for unknown FR1 SCell activation case, 160 ms SCell measurement cycle

## A.6.5.3.3.2Test Requirements

The test requirements defined in clause A.6.5.3.1.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstSSB_MAX + TSMTC_MAX + 2*Trs + 5 ms as defined in clause 8.3.

## A.6.5.3.4Direct SCell activation at SCell addition of known SCell in FR1

## A.6.5.3.4.1Test Purpose and Environment

The purpose of this test is to verify fulfillment of direct SCell activation delay and interruption requirements at SCell addition as defined in clause 8.3.4 and 8.2.2, respectively. The supported test configurations for NR PCell are shown in table A.6.5.3.4.1-1. The supported test configurations for NR SCell are shown in table A.6.5.3.4.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently.

The test scenario comprises one PCell (Cell 1) and one SCell (Cell 2) as outlined in table A.6.5.3.4.1-2. Cell-specific parameters are provided in table A.6.5.3.4.1-3 and table A.6.5.3.4.1-4.

The test consists of two successive time periods with duration T1 and T2, respectively. There are two carriers, each with one cell. Cell 1 (PCell) is on RF channel 1 (PCC), and Cell 2 (SCell) is on RF channel 2 (SCC). Cell 1 and Cell 2 both operate according to one of the configurations in table A.6.5.3.4.1-1 and table A.6.5.3.4.1-1A respectively.

Before the test starts the UE is connected to Cell 1 on RF channel 1. The UE is only monitoring RF channel 1 and is not aware of Cell 2 on RF channel 2.

The UE is continuously scheduled in PCell throughout the test.

At the beginning of T1 the UE is configured to measure RF channel 2 in measurement gaps. During T1, the UE detects and measures Cell 2 on RF channel 2, and sends a measurement report containing Cell 2 to the test equipment. After having received a measurement report containing Cell 2, the test equipment deconfigures the measurement gaps and thereafter sends a RRC connection reconfiguration message to the UE by which it configures the SCell (Cell 2) in activated state (sCellState is set to activated). The time between reception of the last measurement report carrying SCell and transmission of the RRC connection reconfiguration message directly activating SCell is kept short enough to allow the SCell to remain known to the UE.

Time period T2 starts when the UE receives the RRC connection reconfiguration message at the UE antenna connector. The corresponding slot at which the message is received at the UE antenna connector is denoted n. The UE shall complete activation of the SCell no later than in slot n + , as specified in clause 8.3.4. From slot n+  and onwards the UE shall report valid CSI both for PCell and SCell.NdirectNR slot lengthNdirectNR slot length

The test equipment verifies the activation time by counting the slots between the RRC connection reconfiguration message is sent and until CSI report with non-zero CQI for both PCell and SCell is received.

The test equipment verifies that interruptions on other serving cells are within the requirements by counting ACK/NACKs transmitted in PCell.

Table A.6.5.3.4.1-1: Supported test configurations

Table A.6.5.3.4.1-1A: Supported test configurations for NR SCell

Table A.6.5.3.4.1-2: General test parameters

Table A.6.5.3.4.1-3: NR Cell specific test parameters

Table A.6.5.3.4.1-4: NR Cell specific test parameters for NR Scell

## A.6.5.3.4.2Test Requirements

The UE shall complete the direct activation of the SCell no later than at slot n + . NdirectNR slot length

The UE shall report non-zero CQI for SCell from slot n +  and onwards throughout time period T2.NdirectNR slot length

The interruption on PCell during direct activation of the SCell shall occur within the interruption window specified in clause 8.3.4 and shall not exceed the length specified in clause 8.2.2.2.11.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.3.5Direct SCell activation at handover with known SCell in FR1

## A.6.5.3.5.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD and TDD-TDD intra-frequency handover with direct SCell activation requirements specified in subclause 8.3.5.

Supported test configurations for NR PCell are shown in table A.6.5.3.5.1-1. Supported test configurations for NR SCell are shown in table A.6.5.3.5.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently. Both handover with direct SCell activation requirements are tested by using the parameters in table A.6.5.3.5.1-2, A.6.5.3.5.1-3 and A.6.5.3.5.1-4.

The test scenario comprises of two NR carriers and 3 cells as given in tables A.6.5.3.5.1-1 and A.6.5.3.5.1-2. The test consists of three successive time periods, with time durations of T1, T2, and T3 respectively.

At the start of time duration T1, the UE is in connected mode with PCell and SCell 1 (Cell 2) is in activated state and UE is reporting CQI for both PCell and SCell 1.

Time period T2 starts when UE receives a handover command to Cell 3 that also activates SCell 1 (Cell 2). This is done using an RRCReconfiguration message with parameter sCellState set to activated for the SCell 1 (Cell 2). The message is sent from the test equipment to the UE and is received in a subframe # denoted n at the UE antenna connector. The UE shall accomplish the activation of the SCell no later than subframe (n + Ndirect).

Time period T3 starts at (n + Ndirect), at which point UE shall be reporting a valid CQI for both PCell and SCell 1.

Table A.6.5.3.5.1-1: Intra-frequency handover with direct SCell activation from FR1 to FR1 test configurations for NR PCell

Table A.6.5.3.5.1-1A: Intra-frequency handover with direct SCell activation from FR1 to FR1 test configurations for NR SCell

Table A.6.5.3.5.1-2: General test parameters Intra-frequency handover with direct SCell activation from FR1 to FR1

Table A.6.5.3.5.1-3: Cell specific test parameters for NR PCell for NR FR1-FR1 Intra-frequency handover with direct SCell activation test case

Table A.6.5.3.5.1-4: Cell specific test parameters for NR SCell for NR FR1-FR1 Intra-frequency handover with direct SCell activation test case

## A.6.5.3.5.2Test Requirements

The UE shall be capable to transmit valid CSI report for the directly activated SCell 1 no later than in subframe n+Ndirect.

The rate of correct observed SCell 1 direct activation delay during repeated tests shall be at least 90 %.

NOTE:The SCell activation delay, Ndirect, can be expressed as: Ndirect = TRRC_process + Tinterrupt + T2 + T3 + Tactivation_time + TCSI_Reporting - 3 ms, where:

TRRC_Process: RRC procedure delay defined in clause 12 of TS 38.331 [2],

Tinterrupt: Interruption time during handover as specified in clause 6.1.1,

T2: Delay from slot  until UE has obtained a valid TA command for the target PCell,n+TRRC_Process+TinterruptNR slot length

T3: Delay for applying the received TA for uplink transmission in the target PCell, and greater than or equal to k+1 slot, where k is defined in clause 4.2 in TS 38.213,

Tactivation_time and TCSI_Reporting are specified in clause 8.3.2, where the following definitions of TFirstSSB and TFirstSSB_MAX as defined in section 8.3.5 shall apply:

-TFirstSSB: the time to the end of the first complete SSB burst indicated by the SMTC after slot n + (𝑇𝑅𝑅𝐶_𝑃𝑟𝑜𝑐𝑒𝑠𝑠+𝑇𝑖𝑛𝑡𝑒𝑟𝑟𝑢𝑝𝑡+𝑇2+𝑇3)/(N𝑅 𝑠𝑙𝑜𝑡 𝑙𝑒𝑛𝑔𝑡ℎ)

-TFirstSSB_MAX: the time to the end of the first complete SSB burst indicated by the SMTC after slot n + (𝑇𝑅𝑅𝐶𝑃𝑟𝑜𝑐𝑒𝑠𝑠+𝑇𝑖𝑛𝑡𝑒𝑟𝑟𝑢𝑝𝑡+𝑇2+𝑇3)/(N𝑅 𝑠𝑙𝑜𝑡 𝑙𝑒𝑛𝑔𝑡ℎ)

This gives a total of Ndirect = 10 + 52 + TIU + T2 + T3 + Tactivation_time + TCSI_Reporting - 3 ms = 62 + 10 + 13 + 6 + 20 + 2 - 3 = 94 ms for test configurations 1 and 2.

This gives a total of Ndirect = 10 + 52 + TIU + T2 + T3 + Tactivation_time + TCSI_Reporting - 3 ms = 62 + 10 + 13 + 6 + 20 + 2 - 3 = 94 ms for test configuration 3.

During T3 the UE shall send valid CSI reports for PCell and SCell 1 with non-zero CQI index and continue to send CSI reports for PCell and SCell 1 (Cell 2) with non-zero CQI index until the end of T3.

All of the above test requirements shall be fulfilled in order for the observed SCell 1 direct activation delay to be counted as correct.

## A.6.5.3.6PUCCH SCell Activation and deactivation of known SCell in FR1

## A.6.5.3.6.1Test Purpose and Environment

The purpose of this test is to verify that the PUCCH SCell activation and deactivation times are within the requirements stated in clause 8.3, when the PUCCH SCell in FR1 is known by the UE at the time of activation.

The supported test configurations are shown in table A.6.5.3.6.1-1 below. The test parameters are given in tables A.6.5.3.6.1-2 and cell-specific parameters in table A.6.5.3.6.1-3 below. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Cell 1 is the PCell in primary Timing Advance Group (pTAG) and Cell 2 is the PUCCH SCell in the secondary Timing Advance Group (sTAG). Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

The test consists of two sub tests. In Test 1, UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment for sTAG. In Test 2, the TimeAlignmentTimer of sTAG expires before receiving the activation command.

At the beginning of T1 the UE receives an RRC message by which the PUCCH SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the PUCCH SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. In Test 1, the UE shall be able to report valid CSI on for the activated PUCCH SCell on PUCCH SCell at latest in slot n+, as defined in clause 8.3. In Test 2, the UE shall be able to report valid CSI for the activated PUCCH SCell on PUCCH SCell at latest in slot , as defined in clause 8.3.THARQ+Tactivation_time+max ((TFirst_available_CSI +TCSI_processing),   3*Ttarget_PL-RS)+TCSI_Reporting_afterNR slot lengthn+THARQ+Tdelay_PUCCH_SCellNR slot length

Any PCell interruption due to activation of PUCCH SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of PUCCH SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the PUCCH SCell in a slot , as defined in clause 8.3, and The starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of PUCCH SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the PUCCH SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the PUCCH SCell deactivation command is sent until CQI reporting for PUCCH SCell is discontinued.

Table A.6.5.3.6.1-1: known FR1 SCell activation test configurations

Table A.6.5.3.6.1-2: General test parameters for known FR1 SCell activation case

Table A.6.5.3.6.1-3: Cell specific test parameters for known FR1 SCell activation case

## A.6.5.3.6.2Test Requirements

In Test1，during T2 the UE shall start sending CSI reports for PUCCH SCell with non-zero CQI index at latest in a slot n+, Tactivation_time = TFirstSSB+ 5ms, as defined in clause 8.3. In Test2，during T2 the UE shall start sending CSI reports for PUCCH SCell with non-zero CQI index at latest in a slot , Tactivation_time = TFirstSSB+ 5ms, as defined in clause 8.3.THARQ+Tactivation_time+max ((TFirst_available_CSI +TCSI_processing),   3*Ttarget_PL-RS)+TCSI_Reporting_afterNR slot lengthn+THARQ+Tdelay_PUCCH_SCellNR slot length

During T3 the UE shall stop sending CSI reports for PUCCH SCell at latest in a slot , as defined in clause 8.3.m+THARQ+3 msNR slot length

During T2 interruption of PCell / PSCell during PUCCH SCell activation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

During T3 the starting point of interruption of PCell during PUCCH SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.18.

All of the above test requirements shall be fulfilled in order for the observed PUCCH SCell activation delay and PUCCH SCell deactivation delay to be counted as correct. The rate of correct observed PUCCH SCell activation delay and PUCCH SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in slot n+ in Test 1 or in slot  in Test 2 as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivation_time+max ((TFirst_available_CSI +TCSI_processing),   3*Ttarget_PL-RS)+TCSI_Reporting_afterNR slot lengthn+THARQ+Tdelay_PUCCH_SCellNR slot length

## A.6.5.3.7SCell Activation and deactivation of unknown SCell in FR1 in non-DRX

## A.6.5.3.7.1Test Purpose and Environment

The purpose of this test is to verify that the PUCCH SCell activation and deactivation times are within the requirements stated in clause 8.3, when the PUCCH SCell in FR1 is unknown by the UE at the time of activation. In this test, UE shall support cross PUCCH group CSI reporting capability csi-ReportingCrossPUCCH-Grp-r16.

The supported test configurations are shown in table A.6.5.3.7.1-1 below. The test parameters are given in table A.6.5.3.7.1-2 and cell-specific parameters in table A.6.5.3.7.1-3 below. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two NR carriers, each with one cell. Cell 1 is the PCell in primary Timing Advance Group (pTAG) and Cell 2 is the PUCCH SCell in the secondary Timing Advance Group (sTAG). Both cells have constant signal levels throughout the test.

There are two sub tests in this section.

For Test 1 (valid TA case), UE is provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment for sTAG.

For Test 2 (invalid TA case), TimeAlignmentTimer of sTAG expires before UE receives the activation command

Before the test starts the UE is connected to PCell, but is not aware of PUCCH SCell. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the PUCCH SCell becomes configured on NR. During T1 the PUCCH SCell is powered off and UE is not aware of PUCCH SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI on PUCCH SCell for the activated PUCCH SCell at latest in

slot n+ for Test 1, orTHARQ+Tactivation_time+max ((TFirst_available_CSI +TCSI_processing),   3*Ttarget_PL-RS)+TCSI_Reporting_afterNR slot length

slot   for Test 2n+THARQ+Tdelay_PUCCH_SCellNR slot length

Note: Tdelay_PUCCH_SCell = Tactivation_time + max ((TFirst_available_CSI + TCSI_processing), (T1+T2+T3), 3*Ttarget_PL-RS) + TCSI_reporting_after, as defined in clause 8.3,

Any PCell interruption due to activation of PUCCH SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+1+THARQNR slot lengthn+1+THARQ+3ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of PUCCH SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the PUCCH SCell in a slot , as defined in clause 8.3, and the starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of PUCCH SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the PUCCH SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the PUCCH SCell deactivation command is sent until CQI reporting for PUCCH SCell is discontinued.

Table A.6.5.3.7.1-1: unknown FR1 PUCCH SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations

Table A.6.5.3.7.1-2: General test parameters for unknown FR1 PUCCH SCell activation case, 160 ms SCell measurement cycle

Table A.6.5.3.7.1-3: Cell specific test parameters for unknown FR1 PUCCH SCell activation case, 160 ms SCell measurement cycle

## A.6.5.3.7.2Test Requirements

During T2, as defined in clause 8.3, the UE shall start sending CSI reports for PUCCH SCell on PUCCH SCell with non-zero CQI index at latest in

a slot n+ for Test 1. Tactivation_time = TFirstSSB_MAX + TSMTC_MAX + 2*Trs + 5ms.THARQ+Tactivation_time+max ((TFirst_available_CSI +TCSI_processing),   3*Ttarget_PL-RS)+TCSI_Reporting_afterNR slot length

a slot   for Test 2.n+THARQ+Tdelay_PUCCH_SCellNR slot length

During T3 the UE shall stop sending CSI reports for PUCCH SCell at latest in a slot , as defined in clause 8.3.m+THARQ+3 msNR slot length

During T2 interruption of PCell during PUCCH SCell activation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

During T3 the starting point of interruption of PCell during PUCCH SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.18.

All of the above test requirements shall be fulfilled in order for the observed PUCCH SCell activation delay and PUCCH SCell deactivation delay to be counted as correct. The rate of correct observed PUCCH SCell activation delay and PUCCH SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  n+  and in a slot for Test 1 and Test 2, respectively, as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivation_time+max ((TFirst_available_CSI +TCSI_processing),   3*Ttarget_PL-RS)+TCSI_Reporting_afterNR slot lengthn+THARQ+Tdelay_PUCCH_SCellNR slot length

## A.6.5.3.8SCell Activation and Deactivation of one FR1 known PUCCH SCell and one FR1 unknown SCell with single activation/deactivation command

## A.6.5.3.8.1Test Purpose and Environment

The purpose of this test is to verify the SCell activation and deactivation delay requirements for PUCCH SCell with multiple SCells specified in clause 8.3.13 and 8.3.15, when one configured deactivated known PUCCH SCells in FR1 and one configured unknown SCell in FR1 by the UE at the time of activation.

The supported test configurations are defined in table A.6.5.3.8.1-1 below. The test parameters are given in table A.6.5.3.8.1-2 and cell-specific parameters in table A.6.5.3.8.1-3 below.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are three NR carriers. All Cells has constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCC), but is not aware of Cell 2 (PUCCH SCell) and Cell 3(SCell). The UE is monitoring the Cell 1 (PCC). The UE shall be continuously scheduled in the Cell 1 throughout the whole test. PCC, SCC of Cell 2 and SCC of Cell 3 are on different FR1 bands.

At the beginning of T1 the UE receives an RRC message by which the PUCCH SCell (Cell 2) and SCell (Cell 3) become configured on radio channel 2 and 3 respectively.

A MAC message for activation of PUCCH SCell (Cell 2) and SCell (Cell 3) is sent by the test equipment 100 ms after the RRC message, in a slot # denoted m. The point in time at which the MAC message for activation of PUCCH SCell (Cell 2) and SCell (Cell 3) is received at the UE antenna connector defines the start of time period T2. Immediately at beginning of T2 the transmission power of Cell 2 and Cell 3 are increased to same level as for Cell 1. The UE shall be able to report valid CSI on PCell for the activated PUCCH SCell (Cell 2) at latest in slot   and be able to report valid CSI on PCell for the activated SCell  (Cell 3) at latest in slot  as defined in clause 8.3.13 provided the PUCCH SCell can be successfully detected on the first attempt.m+THARQ+Tdelay_multiple_SCells_PUCCH_SCellNR slot lengthm+THARQ+Tdelay_multiple_SCells_other_SCellNR slot length

For Cell 2 activtion, the UE shall start reporting CSI in PCell in slot  and shall report CQI index 0 (out-of-range) until the PUCCH SCell activation has been completed. For Cell 3 activtion, the UE shall start reporting CSI in PCell in slot  and shall report CQI index 0 (out-of-range) until the DL SCell activation has been completed.n+THARQ+3 msNR slot lengthn+THARQ+3 msNR slot length

Any PCell interruption due to activation of SCells (including one SCell configured with PUCCH) shall occur in the slot  to slot, as defined in clause 8.3, where  is the interruption length given in section 8.2. m+1+THARQNR slot length m+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of the SCells (Cell 2 and Cell 3), sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector. The UE shall carry out deactivation of the SCells (Cell 2 and Cell 3) at latest in slot   as defined in clause 8.3. The starting point of PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3. n+THARQ+3msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of PUCCH SCell and DL SCell, respectively.

The test equipment verifies the PUCCH SCell activation time by counting the slots from the time when the PUCCH SCell activation command is sent until a CSI report with other than CQI index 0 is received. The test equipment verifies the DL SCell activation time by counting the slots from the time when the DL SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the PUCCH SCell deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for PUCCH SCell is discontinued. The test equipment verifies the DL SCell deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for DL SCell is discontinued.

Table A.6.5.3.8.1-1: Supported test configurations

Table A.6.5.3.8.1-2: General test parameters for unknown FR1 SCell activation case with 2 deactivated SCells, 160 ms SCell measurement cycle

Table A.6.5.3.8.1-3: Cell specific test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

## A.6.5.3.8.2Test Requirements

During T2, the UE shall send the first CSI report for SCell in the first available uplink resource after slot (m+k). UE is allowed to postpone CSI report to next available uplink resource if an available uplink resource is subject to interruption.  Whether CSI report in slot (m+k) was interrupted is checked by monitoring ACK/NACK sent in PCell in slot (m+k). And the UE shall be able to report valid CSI for the activated PUCCH SCell (Cell 2) at latest in slot  and report valid CSI for the activated SCell (Cell 3) at latest in slot  as defined in clause 8.3.13. And the PCell interruption due to activation of SCells (including one SCell configured with PUCCH) shall occur in the slot  to slot, as defined in clause 8.3, where is the interruption length given in section 8.2. m+THARQ+Tdelay_multiple_SCells_PUCCH_SCellNR slot lengthm+THARQ+Tdelay_multiple_SCells_other_SCellNR slot lengthm+1+THARQNR slot length m+1+THARQ+3ms+TXNR slot length+NinterruptionNinterruption

During T3, the UE shall carry out deactivation of the the SCells (including one SCell configured with PUCCH) at latest in slot   as defined in clause 8.3. And the starting point of PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.n+THARQ+3msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3msNR slot length

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90 %.

## A.6.5.3.9SCell Activation and deactivation of unknown PUCCH SCell and unknown DL SCell in FR1 in non-DRX

## A.6.5.3.9.1Test Purpose and Environment

The purpose of this test is to verify that the PUCCH SCell and DL SCell activation and deactivation times are within the requirements stated in clause 8.3.13 and clause 8.3.15, when the PUCCH SCell in FR1 and DL SCell in FR1 is unknown to the UE at the time of activation.

The supported test configurations are shown in table A.6.5.3.9.1-1 below. The test parameters are given in table A.6.5.3.9.1-2 and cell-specific parameters in table A.6.5.3.9.1-3 below. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are three NR carriers, each with one cell. All cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2 (PUCCH SCell) and Cell 3(DL SCell). The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test. PCC, SCC of Cell 2 and SCC of Cell 3 are on different bands. The primary PUCCH group contain Cell 1 and the secondary PUCCH group contains Cell 2 and Cell 3.

At the beginning of T1 the UE receives an RRC message by which the PUCCH SCell (Cell 2) and DL SCell (Cell 3) becomes configured on radio channel 2 and 3 respectively. The UE starts monitoring the SCC1(Cell 2 CC) and SCC2(Cell 3 CC). The test equipment sends a MAC message for activation of the PUCCH SCell and DL SCell simultaneously.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated PUCCH SCell at latest in slotn+ , and report valid CSI in PCell for the activated DL SCell at latest in slotn+, as defined in clause 8.3.13. In this test case, both valid TA and invalid TA cases shall be tested. THARQ+Tdelay_multiple_SCells_PUCCH_SCellNR slot length THARQ+Tdelay_multiple_SCells_other_SCellNR slot length

Test for case when UE has valid TA: the TimeAlignmentTimer [2] associated with the TAG containing the PUCCH SCell is running, and Tdelay_multiple_SCells_PUCCH_SCell = Tdelay_multiple_SCells_PUCCH_SCell = Tactivation_time_multiple_scells + max ((TFirst_available_CSI + TCSI_processing), 3*Ttarget_PL-RS) + TCSI_reporting_after.

Test for case when UE do not have valid TA: Tdelay_multiple_SCells_PUCCH_SCell = Tactivation_time_multiple_scells + max ((TFirst_available_CSI + TCSI_processing), (T1+T2+T3), 3*Ttarget_PL-RS) + TCSI_reporting_after.

Tdelay_multiple_SCells_other_SCell   = Tactivation_time_multiple_scells +TCSI_Reporting.

Tactivation_time_multiple_scells is the target SCell activation delay in millisecond in multiple SCell activation scenario as specified in section 8.3.7

For Cell 2 activtion, the UE shall start reporting CSI in PCell in slot  and shall report CQI index 0 (out-of-range) until the PUCCH SCell activation has been completed. For Cell 3 activtion, the UE shall start reporting CSI in PCell in slot  and shall report CQI index 0 (out-of-range) until the DL SCell activation has been completed.n+THARQ+3 msNR slot lengthn+THARQ+3 msNR slot length

Any PCell interruption due to activation of PUCCH SCell or DL SCell shall occur in the slot  to , as defined in clause 8.3.13, where  is the interruption length given in clause 8.2.2.2.7.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of PUCCH SCell abd DL SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3.15, and the starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.15.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of PUCCH SCell and DL SCell, respectively.

The test equipment verifies the PUCCH SCell activation time by counting the slots from the time when the PUCCH SCell activation command is sent until a CSI report with other than CQI index 0 is received. The test equipment verifies the DL SCell activation time by counting the slots from the time when the DL SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the PUCCH SCell deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for PUCCH SCell is discontinued. The test equipment verifies the DL SCell deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for DL SCell is discontinued.

Table A.6.5.3.9.1-1: unknown FR1 PUCCH SCell and DL SCell activation test configurations

Table A.6.5.3.9.1-2: General test parameters for unknown FR1 PUCCH SCell and DL SCell activation case

Table A.6.5.3.9.1-3: Cell specific test parameters for unknown FR1 PUCCH SCell and DL SCell activation case

## A.6.5.3.9.2Test Requirements

The test requirements defined in clause A.6.5.3.8.2 shall apply to this test case.

## A.6.5.3.10Fast SCell Activation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle

## A.6.5.3.10.1Test Purpose and Environment

The purpose of this test is to verify that the fast SCell activation and deactivation times are within the requirements stated in clause 8.3.16, when the SCell in FR1 is known by the UE at the time of activation.

The supported test configurations are shown in table A.6.5.3.10.1-1 below. The test parameters are given in tables A.6.5.3.10.1-2 and cell-specific parameters in table A.6.5.3.10.1-3 below. The test consists of two successive time periods, with duration of T1and T2, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell and triggering the aperiodic CSI-RS for fast SCell activation.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n (where n mode 20=1), defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.6.5.3.10.1-1: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations

Table A.6.5.3.10.1-2: General test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.6.5.3.10.1-3: Cell specific test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

## A.6.5.3.10.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , Tactivation_time = TFirstATRS + 5 ms, as defined in clause 8.3.16.n+1+THARQ+3 msNR slot lengthn+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

During T2 interruption of PCell / PSCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.16.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.6.5.3.11SCell Activation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle

## A.6.5.3.11.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.6.5.3.10.1. The supported test configurations are the same as defined in clause A.6.5.3.10.1. The test parameters are the same except those described in the following clause. The listed parameter values in table A.6.5.3.11.1-1 will replace the values of corresponding parameters in tables A.6.5.3.10.1-2 and the listed parameter values in table A.6.5.3.11.1-2 will replace the values of corresponding parameters in tables A.6.5.3.10.1-3.

Table A.6.5.3.11.1-1: General test parameters for known FR1 SCell activation case, 640 ms SCell measurement cycle

Table A.6.5.3.11.1-2: Cell specific test parameters for known FR1 SCell activation case, 640 ms SCell measurement cycle

## A.6.5.3.11.2Test Requirements

The test requirements defined in clause A.6.5.3.10.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstATRS + Tgap + TATRS + 5 ms.

## A.6.5.3.12SCell Activation and deactivation of unknown SCell in FR1 in DRX for UE capable of short measurement interval

## A.6.5.3.12.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clauses 8.3.2 and 8.3.3, respectively, when the SCell in FR1 is unknown by the UE at the time of activation and when UE supports shortMeasInterval-r18 capability.

The supported test configurations are shown in table A.6.5.3.12.1-1 below. The test parameters are given in table A.6.5.3.12.1-2 and cell-specific parameters in table A.6.5.3.12.1-3 below. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3.2. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3, and The starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.6.5.3.12.1-1: unknown FR1 SCell activation in DRX for 160 ms SCell measurement cycle supported test configurations

Table A.6.5.3.12.1-2: General test parameters for unknown FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.6.5.3.12.1-3: Cell specific test parameters for unknown FR1 SCell activation case, 160 ms SCell measurement cycle

## A.6.5.3.12.2Test Requirements

The test requirements defined in clause A.6.5.3.1.2 shall apply to this test case, except Tactivation_time will be replaced with the value below as defined in clause 8.3.2 when UE supports shortMeasInterval-r18 capability:

Tactivation_time = 3 ms + TFirstSSB_MAX, enhanced + TSMTC_MAX, enhanced + Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP ,report + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay), for which TFirstSSB_MAX, enhanced = TSMTC_MAX, enhanced = Trs, enhanced =20 ms; TL1-RSRP, enhanced_measure = 60 ms and TL1-RSRP, report=5 ms.

## A.6.5.3.13SCell Activation of multiple unknown SCells in FR1 with L3 reporting with single activation/deactivation commandin non-DRX

## A.6.5.3.13.1Test Purpose and Environment

The purpose of this test is to verify that the multiple SCells activation times are within the requirements stated in clause 8.3.18, when all the multiple SCells in the same FR1 band are unknown to the UE at the time of activation.

The supported test configurations are shown in table A.6.5.3.13.1-1 below. The test parameters are given in tables A.6.5.3.13.1-2. The cell-specific parameters for NR PCell and NR SCell are given in tables A.6.5.3.13.1-3 and A.6.5.3.13.1-4 below. The test consists of two successive time periods, with duration of T1 and T2, respectively. There are three NR carriers, each with one cell. All cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1(PCell), but is not aware of Cell 2 (DL SCell) and Cell 3(DL SCell). The UE is only monitoring the PCC. TE continuously schedules the downlink data to UE on PCell throughout the whole test. PCC and SCC of Cell 2, Cell 3 are on different bands. SCC of Cell 2 and SCC of Cell 3 are on same band.

The test consists of two sub tests. The slot at which the MAC message is received at the UE antenna connector, is denoted slot #n.

At the beginning of T1 the UE receives an RRC message by which the Cell 2 and Cell 3 becomes configured on radio channel 2 and 3 respectively. The UE starts monitoring the SCC1(Cell 2 CC) and SCC2(Cell 3 CC). The test equipment sends a MAC message for activation of the Cell 2 and Cell 3 simultaneously.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2.

In sub test 1, TE shall transmit DCI 0-1 on PCell to schedule the PUSCH at slot , and the UE shall be able to transmit L3 measurement report of SCells at slot , where k2 = 1. n+THARQ+7 ms NR slot lengthn+THARQ+7 ms+k2 NR slot length

In sub test 2, TE shall transmit DCI 0-1 on PCell to schedule the PUSCH at slot , where M is defined in clause 8.3.17 and k2 = 1, and the UE shall be able to transmit L3 measurement report of SCells at slot . For sub test 2, TE will send TCI activation command after receiving L3 measurement report of the SCell.n+THARQ+3ms+M-k2 NR slot lengthn+THARQ+3ms+M NR slot length

The UE shall be able to report valid CSI in PCell for the activated DL SCells at latest in slot as defined in clause 8.3.18.  n+THARQ+Tactivation_time_multiple_scells+TCSI_ReportingNR slot length,

The UE shall start reporting CSI in PCell for the activated SCells(Cell 2 and Cell 3) after at least one CSI-RS transmission occasion for channel measurement and reporting after slot  and shall report CQI index 0 (out-of-range) until the multiple DL SCell activation has been completed.n+THARQ+3 msNR slot length

Any PCell interruption due to activation DL SCell shall occur in the slot  to , as defined in clause 8.3.18, where  is the interruption length given in clause 8.2.2.2.2.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

The test equipment verifies the activation time for Cell 2 by counting the slots from the time when the SCell activation command is sent until CSI report of acticated Cell 2 with other than CQI index 0 is received.

The test equipment verifies the activation time for Cell 3 by counting the slots from the time when the SCell activation command is sent until CSI report of acticated Cell 3 with other than CQI index 0 is received.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation of multiple DL SCells.

The test equipment verifies the multiple DL SCell activation time by counting the slots from the time when the multiple DL SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.6.5.3.13.1-1: Supported test configurations

Table A.6.5.3.13.1-2: General test parameters for multiple unknown FR1 DL SCell activation case

Table A.6.5.3.13.1-3: Cell specific test parameters for NR PCell for multiple unknown FR1 SCell activation case

Table A.6.5.3.13.1-4: Cell specific test parameters for NR SCell for multiple unknown FR1 SCell activation case

## A.6.5.3.13.2Test Requirements

During T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where as defined in clause 8.3.18, in sub test 1,    Tactivation_time_multiple_scells = 7 ms  +  + max (THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay), where = 1 ms for Config 1 and 2, and 0.5 ms for config 3. n+THARQ+Tactivation_time_multiple_scells+TCSI_ReportingNR slot lengthk2NR slot lengthk2NR slot length

In sub test 2, Tactivation_time_multiple_scells = 3 ms + M  + max (THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay).

## A.6.5.3.14SCell Activation of unknown SCell with valid L3 measurement results in FR1 in non-DRX for 160 ms SCell measurement cycle

## A.6.5.3.14.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation time are within the requirements stated in clause 8.3.17, when the SCell in FR1 is unknown by the UE at the time of activation, but UE has valid L3 measurement results of the SCell.

The supported test configurations for NR PCell are shown in table A.6.5.3.14.1-1 below. Supported test configurations for NR SCell are shown in table A.6.5.3.14.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently. The test parameters are given in Tables A.6.5.3.14.1-2 and cell-specific parameters in tables A.6.5.3.14.1-3 and A.6.5.3.14.1-4 below. The test consists of three successive time periods, with duration of T1, T2 and T3 respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC.

The test consists of three sub tests. The slot at which the MAC message is received at the UE antenna connector, is denoted slot #n. TE continuously schedules the downlink data to UE on PCell. In Sub-test 1, TE shall schedule DCI format 0_1 at slot n + . In Sub-test 2, TE shall schedule DCI format 0_1 at slot n + , where M is defined in clause 8.3.17 and k2 = 1. In Sub-test 3, UE shall tranmsit scheduling request on the first SR resource by 7ms+ THARQ + TSR_Periodicity to obtain the UL grant for L3 report transmission.THARQ+7msNR slot lengthTHARQ+3ms+M-k2NR slot length

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. T1 is sufficiently long enough so that UE is able to complete the L3 detection and measurements on the SCell to be activated. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. UE is expected to report L3 measurement result at the first PUSCH scheduled by TE.

The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3.17. TE also indicates the TCI, based on L3 report of the UE. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after the slot that UE sends the L3 reports and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. n+THARQ+Tactivation_time+TCSI_ReportingNR slot length

During T2, any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3.17, where  is the interruption length given in clause 8.2.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

At the beginning of T3, the SCell de-activation command is sent. T3 shall be long enough to ensure UE completes the SCell de-activation.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation of SCell.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.6.5.3.14.1-1: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR PCell

Table A.6.5.3.14.1-1A: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR SCell

Table A.6.5.3.14.1-2: General test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.6.5.3.14.1-3: Cell specific test parameters for NR PCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.6.5.3.14.1-4: Cell specific test parameters for NR SCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.6.5.3.14.1-5: Scheduling request parameters

## A.6.5.3.14.2Test Requirements

During T2, the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption. During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot .n+1+THARQ+3 msNR slot lengthn+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

For Sub-test 1, Tactivation_time = 7 ms + k2/SCS + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3.17, where k2/SCS is 1 ms for config 1,2 and 0.5 ms for config 3.

For Sub-test 2, Tactivation_time = 3 ms + M + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3.17.

For Sub-test 3, Tactivation_time = 7ms + Tuncertainity_ULgrant + max (THARQ + Tuncertainty_MAC + 5ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3.17. Where, Tuncertainity_ULgrant is uncertainty in acquiring UL grant after sending scheduling request.

During T2, interruption of PCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.17.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and L3 measurement reporting to be counted as correct. The rate of correct observed SCell activation delay and L3 measurement reporting during repeated tests shall be at least 90 %.

NOTE:During T2, if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.6.5.3.15TRS based SCell Activation of SSB-less SCell in FR1 inter-band CA in non-DRX

## A.6.5.3.15.1Test Purpose and Environment

The purpose of this test is to verify that the SSB-less SCell activation delay is within the requirements stated in clause 8.3.2, when the to be activated SCell in FR1 is provided with periodic CSI-RS for tracking instead of SSB. SCell does not provide neighther SSB configuration (absoluteFrequencySSB) nor SMTC configuration.

The supported test configurations are shown in table A.6.5.3.15.1-1A and A.6.5.3.15.1-1B below. The test parameters are given in Tables A.6.5.3.15.1-2 and cell-specific parameters in tables A.6.5.3.15.1-3 and A.6.5.3.15.1-4 below. The test consists of two successive time periods, with duration of T1 and T2, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1(PCell), but is not aware of Cell 2(SCell). Cell 1 and Cell 2 are in different bands. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. At the same time, UE also receives the indication of reference serving cell in the same RRC message. The Cell 1 is indicated as the reference cell of Cell 2. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n (where n mod 20=1), defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.6.5.3.15.1-1A: FR1 inter-band SSB-less SCell activation based on TRS for NR PCell in non-DRX for 160 ms SCell measurement cycle supported test configurations

Table A.6.5.3.15.1-1B: FR1 inter-band SSB-less SCell activation based on TRS for NR SCell in non-DRX for 160 ms SCell measurement cycle supported test configurations

Table A.6.5.3.15.1-2: General test parameters for TRS based SCell activation of SSB-less SCell in FR1 inter-band CA in non-DRX for 160 ms SCell measurement cycle

Table A.6.5.3.15.1-3: PCell test configuration parameters for TRS based SCell activation of SSB-less SCell in FR1 inter-band CA in non-DRX for 160 ms measurement cycle

Table A.6.5.3.15.1-4: SCell test configuration parameters for TRS based SCell activation of SSB-less SCell in FR1 inter-band CA in non-DRX for 160 ms measurement cycle

## A.6.5.3.15.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption. During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , Tactivation_time  is n+1+THARQ+3 msNR slot lengthn+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

-Tfirst_TRS + TTRS + 5 ms, when the the EPRE difference (ΔEPRE) is 12 dB

-Tfirst_TRS + 2*TTRS +5 ms, when the EPRE difference (ΔEPRE) is 30 dB

During T2 interruption of PCell / PSCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.2.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.6.5.3.16Inter-band SSB-less SCell Activation based on A-TRS

## A.6.5.3.16.1Test Purpose and Environment

The purpose of this test is to verify that the inter-band SSB-less SCell activation times are within the requirements stated in clause 8.3.2.

The supported test configurations are shown in table A.6.5.3.16.1-1A and A.6.5.3.16.1-1B below. The test parameters are given in Tables A.6.5.3.16.1-2 and cell-specific parameters in tables A.6.5.3.16.1-3 below. The test consists of two successive time periods, with duration of T1and T2, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to PCell Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The test equipment sends a MAC message for activation of the SCell and triggering the aperiodic CSI-RS for SCell activation.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n (where n mod 20=1), defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.6.5.3.16.1-1A: Inter-band SSB-less SCell Activation based on A-TRS for NR PCell

Table A.6.5.3.16.1-1B: Inter-band SSB-less SCell Activation based on A-TRS for NR SCell

Table A.6.5.3.16.1-2: General test parameters for Inter-band SSB-less SCell Activation based on A-TRS

Table A.6.5.3.16.1-3: PCell test parameters for Inter-band SSB-less SCell Activation based on A-TRS

Table A.6.5.3.16.1-4: SCell parameters for Inter-band SSB-less SCell Activation based on A-TRS

## A.6.5.3.16.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.n+1+THARQ+3 msNR slot length

During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , Tactivation_time = Tfirst_ATRS + Tgap + TATRS + 5 ms, as defined in clause 8.3.2.n+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

During T2 interruption of PCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.2.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

A.6.5.3.17SCell Activation and deactivation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle with less than 5MHz BW

## A.6.5.3.17.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3, when the SCell in FR1 is known by the UE at the time of activation, and the SCell operate with a bandwidth of less than 5 MHz. Supported test configurations are specified in Table A.6.5.3.17.1-1 below. General test parameters for known Scell activation case are specified in Table A.6.5.3.1.1-2. Supported Cell specific test parameters for NR PCell specified in Table A.6.5.3.1.1-3. Supported Cell specific test parameters for NR SCell specified in Table A.6.5.3.1.1-4 apply except those specified in Table A.6.5.3.17.1-2.

The test procedure specified in A.6.5.3.1 applies to this test.

Table A.6.5.3.17.1-1: Supported test configurations

Table A.6.5.3.17.1-2: Cell specific test parameters for NR SCell

## A.6.5.3.17.2Test Requirements

Test requirements specified in Clause A.6.5.3.1.2 apply to this test except Tactivation_time will be replaced with TFirstSSB+ T∆ + 5ms.

## A.6.5.3.18OD-SSB based SCell Activation and deactivation of unknown SCell in FR1 in DRX (OD-SSB Case 1)

## A.6.5.3.18.1Test Purpose and Environment

The purpose of this test is to verify that the OD-SSB based SCell activation and deactivation times are within the requirements stated in clause 8.3, when the SCell in FR1 is unknown by the UE at the time of activation.

The supported test configurations for NR PCell are shown in table A.6.5.3.18.1-1 below. Supported test configurations for unknown NR SCell are shown in table A.6.5.3.18.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently. The test parameters are given in tables A.6.5.3.18.1-2 and cell-specific parameters in tables A.6.5.3.18.1-3 and A.6.5.3.18.1-4 below. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell and the related OD-SSB transmission on the SCell. The point in time at which the MAC message which includes both OD-SSB activation and SCell activation commands is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in 5.2.2.5 in [26], and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of SCell and deactivation of OD-SSB transmission, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell and deactivation of OD-SSB transmission in a slot , as defined in clause 8.3, and The starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.6.5.3.18.1-1: unknown FR1 SCell activation in DRX for 160 ms SCell measurement cycle supported test configurations for NR PCell

Table A.6.5.3.18.1-1A: unknown FR1 SCell activation in DRX for 160 ms SCell measurement cycle supported test configurations for NR SCell

Table A.6.5.3.18.1-2: General test parameters for unknown FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.6.5.3.18.1-3: Cell specific test parameters for NR PCell for unknown FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.6.5.3.18.1-4: Cell specific test parameters for NR SCell for unknown FR1 SCell activation case, 160 ms SCell measurement cycle

## A.6.5.3.18.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in clause 5.2.2.5 in TS 38.214 [26], and reporting after slot (). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.n+1+THARQ+3 msNR slot length

During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , Tactivation_time = TFirst, OD-SSB + 3*Trs, OD-SSB + 5 ms, as defined in clause 8.3.n+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

During T3 the UE shall stop sending CSI reports for SCell at latest in a slot , as defined in clause 8.3.m+THARQ+3 msNR slot length

During T2 interruption of PCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.6.5.3.19OD-SSB based SCell Activation and deactivation of unknown SCell in FR1 DRX mode(OD-SSB Case 2, Alt Time-C1)

## A.6.5.3.19.1Test Purpose and Environment

The purpose of this test is to verify that the OD-SSB based SCell activation and deactivation times are within the requirements stated in clause 8.3, when the SCell in FR1 is unknown by the UE at the time of activation.

The supported test configurations are shown in table A.6.5.3.19.1-1 below. The test parameters are given in table A.6.5.3.19.1-2 and cell-specific parameters in table A.6.5.3.19.1-3 below.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell and the related OD-SSB transmission in the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in 5.2.2.5 in [26], and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3, and The starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.6.5.3.19.1-1: unknown FR1 SCell activation in DRX for 160 ms SCell measurement cycle supported test configurations for NR PCell

Table A.6.5.3.19.1-1A: unknown FR1 SCell activation in DRX for 160 ms SCell measurement cycle supported test configurations for NR SCell

Table A.6.5.3.19.1-2: General test parameters for unknown FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.6.5.3.19.1-3: Cell specific test parameters for NR PCell for unknown FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.6.5.3.19.1-4: Cell specific test parameters for NR SCell for unknown FR1 SCell activation case, 160 ms SCell measurement cycle

## A.6.5.3.19.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in clause 5.2.2.5 in TS 38.214 [26], and reporting after slot (). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.n+1+THARQ+3 msNR slot length

During T3 the UE shall stop sending CSI reports for SCell at latest in a slot , as defined in clause 8.3.m+THARQ+3 msNR slot length

During T2 interruption of PCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.6.5.3.20OD-SSB based SCell Activation and deactivation of known SCell in FR1 non-DRX mode(OD-SSB Case 2, Alt Time-C1)

## A.6.5.3.20.1Test Purpose and Environment

The purpose of this test is to verify that the OD-SSB based SCell activation and deactivation times are within the requirements stated in clause 8.3, when the SCell in FR1 is known by the UE at the time of activation.

The supported test configurations for NR PCell are shown in table A.6.5.3.20.1-1 below. Supported test configurations for NR SCell are shown in table A.6.5.3.20.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently. The test parameters are given in tables A.6.5.3.20.1-2 and cell-specific parameters in tables A.6.5.3.20.1-3 and A.6.5.3.20.1-4 below. The test consists of three successive time periods, with duration of T1 and T2, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell and the related OD-SSB transmission in the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in 5.2.2.5 in [26], and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.6.5.3.20.1-1: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR PCell

Table A.6.5.3.20.1-1A: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR SCell

Table A.6.5.3.20.1-2: General test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.6.5.3.20.1-3: Cell specific test parameters for NR PCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.6.5.3.20.1-4: Cell specific test parameters for NR SCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

## A.6.5.3.20.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in clause 5.2.2.5 in TS 38.214 [26], and reporting after slot (). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.n+1+THARQ+3 msNR slot length

During T2 interruption of PCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.6.5.3.21OD-SSB based Direct SCell activation at SCell addition in FR1(OD-SSB Case 2)

## A.6.5.3.21.1Test Purpose and Environment

The purpose of this test is to verify fulfillment of OD-SSB based direct SCell activation delay and interruption requirements at SCell addition as defined in clause 8.3.21 and 8.2.2, respectively. The supported test configurations for NR PCell are shown in table A.6.5.3.18.1-1. The supported test configurations for NR SCell are shown in table A.6.5.3.18.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently.

The test scenario comprises one PCell (Cell 1) and one SCell (Cell 2) as outlined in table A.6.5.3.21.1-1. Cell-specific parameters are provided in table A.6.5.3.21.1-2 and table A.6.5.3.21.1-3.

The test consists of two successive time periods with duration T1 and T2, respectively. There are two carriers, each with one cell. Cell 1 (PCell) is on RF channel 1 (PCC), and Cell 2 (SCell) is on RF channel 2 (SCC). Cell 1 and Cell 2 both operate according to one of the configurations in table A.6.5.3.18.1-1 and table A.6.5.3.18.1-1A respectively.

Before the test starts the UE is connected to Cell 1 on RF channel 1. The UE is only monitoring RF channel 1 and is not aware of Cell 2 on RF channel 2.

The UE is continuously scheduled in PCell throughout the test.

At the beginning of T1 the UE is configured to measure RF channel 2 in measurement gaps. During T1, the UE detects and measures Cell 2 on RF channel 2, and sends a measurement report containing Cell 2 to the test equipment. After having received a measurement report containing Cell 2, the test equipment deconfigures the measurement gaps and thereafter sends a RRC connection reconfiguration message to the UE by which it configures the SCell (Cell 2) in activated state (sCellState is set to activated) and OD-SSB configurations. The time between reception of the last measurement report carrying SCell and transmission of the RRC connection reconfiguration message directly activating SCell is kept short enough to allow the SCell to remain known to the UE.

Time period T2 starts when the UE receives the RRC connection reconfiguration message at the UE antenna connector. The corresponding slot at which the message is received at the UE antenna connector is denoted n. The UE shall complete activation of the SCell no later than in slot n + , as specified in clause 8.3.21. From slot n+  and onwards the UE shall report valid CSI both for PCell and SCell.NdirectNR slot lengthNdirectNR slot length

The test equipment verifies the activation time by counting the slots between the RRC connection reconfiguration message is sent and until CSI report with non-zero CQI for both PCell and SCell is received.

The test equipment verifies that interruptions on other serving cells are within the requirements by counting ACK/NACKs transmitted in PCell.

Table A.6.5.3.21.1-1: General test parameters

Table A.6.5.3.21.1-2: Cell specific test parameters for NR PCell

Table A.6.5.3.21.1-3: Cell specific test parameters for NR SCell

## A.6.5.3.21.2Test Requirements

The UE shall complete the direct activation of the SCell no later than at slot n + . NdirectNR slot length

Ndirect = TRRC_Process + T1 + THARQ + Tactivation_time + TCSI_Reporting

TRRC_Process and T1 are defined in Clause 8.3.21.

Tactivation_time = TFirst, OD-SSB+ 5 ms

The UE shall report non-zero CQI for SCell from slot n +  and onwards throughout time period T2.NdirectNR slot length

The interruption on PCell during direct activation of the SCell shall occur within the interruption window specified in clause 8.3.21 and shall not exceed the length specified in clause 8.2.2.2.11.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.5.3.22OD-SSB based Direct SCell activation at SCell addition in FR1 without first SSB transmission

## A.6.5.3.22.1Test Purpose and Environment

The purpose of this test is to verify fulfillment of OD-SSB based direct SCell activation delay and interruption requirements at SCell addition as defined in clause 8.3.21 and 8.2.2, respectively. The supported test configurations for NR PCell are shown in table A.6.5.3.22.1-1. The supported test configurations for NR SCell are shown in table A.6.5.3.22.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently.

The test scenario comprises one PCell (Cell 1) and one SCell (Cell 2) as outlined in table A.6.5.3.22.1-1. Cell-specific parameters are provided in table A.6.5.3.22.1-2 and table A.6.5.3.22.1-3.

The test consists one time period with duration T1. There are two carriers, each with one cell. Cell 1 (PCell) is on RF channel 1 (PCC), and Cell 2 (SCell) is on RF channel 2 (SCC). Cell 1 and Cell 2 both operate according to one of the configurations in table A.6.5.3.22.1-1 and table A.6.5.3.22.1-1A respectively.

Before the test starts the UE is connected to Cell 1 on RF channel 1. The UE is only monitoring RF channel 1 and is not aware of Cell 2 on RF channel 2.

The UE is continuously scheduled in PCell throughout the test.

Time period T1 starts when the UE receives the RRC connection reconfiguration message at the UE antenna connector, by which it configures the SCell (Cell 2) in activated state (sCellState is set to activated) and OD-SSB configuration in activated state. The corresponding slot at which the message is received at the UE antenna connector is denoted n. The UE shall complete activation of the SCell no later than in slot n + , as specified in clause 8.3.21. From slot n+  and onwards the UE shall report valid CSI both for PCell and SCell.NdirectNR slot lengthNdirectNR slot length

The test equipment verifies the activation time by counting the slots between the RRC connection reconfiguration message is sent and until CSI report with non-zero CQI for both PCell and SCell is received.

The test equipment verifies that interruptions on other serving cells are within the requirements by counting ACK/NACKs transmitted in PCell.

Table A.6.5.3.22.1-1: General test parameters

Table A.6.5.3.22.1-2: Cell specific test parameters for NR PCell

Table A.6.5.3.22.1-3: Cell specific test parameters for NR SCell

## A.6.5.3.22.2Test Requirements

The UE shall complete the direct activation of the SCell no later than at slot n + . NdirectNR slot length

Ndirect = TRRC_Process + T1 + THARQ + Tactivation_time + TCSI_Reporting

TRRC_Process and T1 are defined in Clause 8.3.21

Tactivation_time = TFirst, OD-SSB + Trs, OD-SSB + 5 ms

The UE shall report non-zero CQI for SCell from slot n +  and onwards throughout time period T1.NdirectNR slot length

The interruption on PCell during direct activation of the SCell shall occur within the interruption window specified in clause 8.3.21 and shall not exceed the length specified in clause 8.2.2.2.11.

The rate of correct events observed during repeated tests shall be at least 90%.

## A.6.5.3.23SDL SCell Activation and deactivation of unknown SCell in FR1 for LBCA

## A.6.5.3.23.1Test Purpose and Environment

The purpose of this test is to verify that the SDL SCell activation and deactivation times are within the requirements stated in clause 8.3.2, when the SDL SCell in FR1 is unknown by the UE at the time of activation, and the UE supporting LB-CA via switching is configured with switchingPattern-r19. The test verifies SCell activation delay when SDL SCell reference signals are partially overlapped with SCell active periods according to the switching pattern.

The supported test configuration for PCell and SCell is Config 1 as shown in table A.6.5.3.23.1-1. The test parameters are given in table A.6.5.3.1.1-2, except for the parameters specific for this test case, which are given in table A.6.5.3.23.1-2 below. Cell-specific parameters are given in table A.6.5.3.1.1-3 and A.6.5.3.1.1-4.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two NR carriers, each with one cell. Both radio channels in this test are at frequency lower than 1GHz. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. Also the LBCA switching pattern is configured in this RRC message. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in 5.2.2.5 in [26], and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. n+THARQ+TLBCA+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 ms+TLBCANR slot length

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3.2.m+THARQ+3ms+TLBCANR slot length

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.6.5.3.23.1-1: Supported test configuration for SDL SCell activation

Table A.6.5.3.23.1-2: General test parameters for unknown FR1 SDL SCell activation case for LBCA

## A.6.5.3.23.2Test Requirements

The test requirements defined in clause A.6.5.3.1.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstSSB_MAX + TSMTC_MAX + 2*Trs + 5 ms as defined in clause 8.3.2 for the case when LowBandCA-Switching-r19 is configured.

## A.6.5.3.24Direct SCell activation at SCell addition of known SCell in FR1 for LBCA

## A.6.5.3.24.1Test Purpose and Environment

The purpose of this test is to verify fulfillment of direct SCell activation delay and interruption requirements at SCell addition as defined in clause 8.3.4 and 8.2.2, respectively, when the UE supporting LB-CA via switching and directSCellActivation-r19 is configured with switchingPattern-r19. The test verifies SCell activation delay when SDL SCell reference signals are partially overlapped with SCell active periods according to the switching pattern.

The supported test configuration for PCell and SCell is Config 1 as shown in table A.6.5.3.24.1-1.

The test parameters are given in tables A.6.5.3.4.1-2, except for the parameters specific for this test case, which are given in table A.6.5.3.24.1-2 below.

The test scenario comprises one PCell (Cell 1) and one SCell (Cell 2) as outlined in table A.6.5.3.4.1-2. Cell-specific parameters are provided in table A.6.5.3.4.1-3 and table A.6.5.3.4.1-4.

The test consists of two successive time periods with duration T1 and T2, respectively. There are two carriers, each with one cell. Cell 1 (PCell) is on RF channel 1 (PCC), and Cell 2 (SCell) is on RF channel 2 (SCC).

Before the test starts the UE is connected to Cell 1 on RF channel 1. The UE is only monitoring RF channel 1 and is not aware of Cell 2 on RF channel 2.

The UE is continuously scheduled in PCell throughout the test.

At the beginning of T1, the UE is configured to measure RF channel 2 in measurement gaps. During T1, the UE detects and measures Cell 2 on RF channel 2 and sends a measurement report containing Cell 2 to the test equipment. After having received a measurement report containing Cell 2, the test equipment deconfigures the measurement gaps and thereafter sends a RRC connection reconfiguration message to the UE by which it configures the SCell (Cell 2) in activated state (sCellState is set to activated). The time between reception of the last measurement report carrying SCell and transmission of the RRC connection reconfiguration message directly activating SCell is kept short enough to allow the SCell to remain known to the UE.

Time period T2 starts when the UE receives the RRC connection reconfiguration message at the UE antenna connector. The corresponding slot at which the message is received at the UE antenna connector is denoted n. The UE shall complete activation of the SCell no later than in slot n + , as specified in clause 8.3.4. From slot n+  and onwards the UE shall report valid CSI both for PCell and SCell.NdirectNR slot lengthNdirectNR slot length

The test equipment verifies the activation time by counting the slots between the RRC connection reconfiguration message is sent and until CSI report with non-zero CQI for both PCell and SCell is received.

The test equipment verifies that interruptions on other serving cells are within the requirements by counting ACK/NACKs transmitted in PCell.

Table A.6.5.3.24.1-1: Supported test configuration for direct SDL SCell activation

Table A.6.5.3.24.1-2: General test parameters for unknown FR1 SDL SCell activation case for LBCA

## A.6.5.3.24.2Test Requirements

The UE shall complete the direct activation of the SCell no later than at slot n + . NdirectNR slot length

The UE shall report non-zero CQI for SCell from slot n +  and onwards throughout time period T2.NdirectNR slot length

The interruption on PCell during direct activation of the SCell shall occur within the interruption window specified in clause 8.3.4 and shall not exceed the length specified in clause 8.2.2.2.11.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.3.25PUCCH SCell Activation and deactivation for UE supporting EMR in FR1

## A.6.5.3.25.1Test Purpose and Environment

The purpose of this test is to verify that EMR (early measurement reporting) based SCell activationis done within the required time period defined in clause 8.3.12, when PUCCH for a being activated SCell is configured on the NR FR1 SCell. The PCell and SCell are in different FR1 bands. The SCell is unknown by the UE and the UE does not have valid TA for a sTAG which the SCell belongs to at the time of activation. Supported test configurations are shown in table A.6.5.3.25.1-1.

The general test parameters and NR cell specific test parameters are given in Table A.6.5.3.25.1-2 and A.6.5.3.25.1-3 below.

In the test there are two cells: Cell 1 and Cell 2. Cell 1 is PCell, Cell 2 is the PUCCH SCell being activated. The test consists of six successive time periods with duration of T1, T2, T3, T4, T5 and T6, respectively. The UE shall be continuously scheduled in Cell 1 (PCell) throughout the test.

During T1, the UE is connected to the PCell (Cell 1) on NR radio channel 1 (PCC), but is not aware of SCell (Cell 2) on NR radio channel 2 (SCC). The PCell is in the pTAGs and the SCell is in a sTAG. The UE is only monitoring the PCC and configured with inter-frequency measurement reporting for Cell 2 in:

measIdleCarrierListNR-r16 for UE supporting measValidationReportEMR-r18

or idleInactiveNR-MeasReport-r16 only,

or measReselectionCarrierListNR-r18 for UE supporting measValidationReportReselectionMeasurements.

Beam level reporting for early measurements is configured when UE receives RRC_Release message from the TE defines the starting point of T2.

At the beginning of T2, Cell 2 becomes detectable however cell reselection shall not be performed. During T2, UE will perform the inter-frequency measurement with the configuration with SCC. Signal level of Cell 2 is set to the value given in table A.6.5.3.25.1-3.

At the beginning of T3, the signal level of the neighbour cell is set to turned off.  The duration of the T3 equals to measIdleValidityDuration-r18 or measReselectionValidityDuration-r18.

During the T2 and T3 the UE is in the RRC_IDLE mode.

The time when TE sends the paging message is defined as the starting point of T4. DuringT4, the UE shall send a valid measurement report with SSB index of Cell2 to the PCell. UE needs to send a valid early measurement report. The time when TE receives the EMR report denote as the end of the T4.

At the beginning of T5 the UE receives an RRC message by which the SCell(Cell2) becomes configured on radio channel 2. UE is only monitoring the PCC and shall be continuously scheduled in the PCell when UE is connected to PCell. Then the test equipment sends a MAC message for activation of the SCell.

The TE will send an MAC CE message to activate the PUCCH SCell (SCC).The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T6.

During T6, the test equipment should send a PDCCH order to the UE to initiate RA procedure on the PUCCH SCell at slot n+ as defined in clause 8.3.12 after UE reports on PCell.THARQ+Tactivation_time+max ((TFirst_available_CSI +TCSI_processing),   3*Ttarget_PL-RS)+TCSI_Reporting_afterNR slot length

The test equipment verifies the activation time by counting the slots from the time when the PUCCH SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.6.5.3.25.1-1: unknown FR1 PCell and SCell activation test configurations

Table A.6.5.3.25.1-2: General test parameters for unknown FR1 PCell and SCell activation case

Table A.6.5.3.25.1-3: Cell specific test parameters for known FR1 PCell and SCell activation case

## A.6.5.3.25.2Test Requirements

During the time period T3 the UE is in Idle mode and the signal level of Cell 2 is changed. The UE shall not perform reselection. The UE shall perform Idle Mode CA measurement according to section 4.4.

At the end of T4, UE is requested to transmit early measurement report for Cell 2 to the PCell.

After receiving the requested early measurement report, the test equipment verifies the slot n+. The is defined in clause 8.3.2A.THARQ+Tactivation_time+max ((TFirst_available_CSI +TCSI_processing),   3*Ttarget_PL-RS)+TCSI_Reporting_afterNR slot lengthTactivation_time

The rate of correct events observed during repeated tests shall be at least 90%. UE needs to report SSB index.

## A.6.5.3.26EMR based SCell activation of unknown SCell in FR1

## A.6.5.3.26.1Test Purpose and Environment

The purpose of this test is to verify that the EMR (early measurement reporting) based SCell activation delay is within the requirements stated in clause 8.3.2A, when the SCell in FR1 is unknown by the UE at the time of activation.

In the test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as SCell in FR1 on NR RF channel 2. The supported test configurations for PCell and SCell are provided in table A.6.5.3.26.1-1 and table A.6.5.3.26.1-1A respectively. The general test parameters are given in table A.6.5.3.26.1-2 and cell-specific parameters for PCell and SCell are given in table A.6.5.3.26.1-3 and table A.6.5.3.26.1-4 respectively.

Table A.6.5.3.26.1-1: supported test configurations for NR PCell

Table A.6.5.3.26.1-1A: supported test configurations for NR SCell

The test consists of 6 successive time periods, with time duration of T1, T2, T3, T4, T5 and T6 respectively.

During T1, the UE is connected to Cell 1 (PCell) only and shall not have any timing information of Cell 2. UE is configured with inter-frequency measurement reporting for Cell 2 in:

measIdleCarrierListNR-r16 for UE supporting measValidationReportEMR-r18 or idleInactiveNR-MeasReport-r16 only, or

measReselectionCarrierListNR-r18 for UE supporting measValidationReportReselectionMeasurements.

Beam level reporting for early measurements is configured. The time point when UE receives RRC_Release message from the TE defines the starting point of T2.

At the beginning of T2, Cell 2 becomes detectable however cell reselection shall not be performed. Signal level of Cell 2 is set to the value given in table A.6.5.3.26.1-4. The duration of T2 is set to a fixed value according to the table A.6.5.3.26.1-2.

At the beginning of T3, the signal level of the Cell 2 is set to another value according to the table A.6.5.3.26.1-4. The duration of the T3 equals to measIdleValidityDuration-r18 or measReselectionValidityDuration-r18 depending on the UE capabilities of the UE under test.

During T2 and T3, UE is in RRC_IDLE mode.

The time when TE sends the paging message is defined as the starting point of T4. During T4, the UE shall send a valid measurement report with SSB index of Cell 2 to the PCell.

At the beginning of T5 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. UE is only monitoring the PCC and shall be continuously scheduled in the PCell when UE is connected to PCell. Then the test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T6. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot, as defined in clause 8.3.2A. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in 5.2.2.5 in [26], and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed.  n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot length

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.6.5.3.26.1-2: General test parameters

Table A.6.5.3.26.1-3: Cell specific test parameters for NR PCell

Table A.6.5.3.26.1-4: Cell specific test parameters for NR SCell

## A.6.5.3.26.2Test Requirements

The UE shall complete the SCell activation no later than at slot.  n+THARQ+Tactivation_time+TCSI_ReportingNR slot length

The UE shall report non-zero CQI for SCell from slot n +  and onwards throughout time period T6.THARQ+Tactivation_time+TCSI_ReportingNR slot length

is defined in clause 8.3.2A in TS 38.133 for FR1 SCell as Tactivation_time is TFirstSSB_MAX + Trs + 5ms. Tactivation_time

The observed SCell activation delay fulfilling the SCell activation delay requirements specified in clause 8.3.2A in TS 38.133 is counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

## A.6.5.3.27EMR based Direct SCell activation at SCell addition of unknown SCell in FR1

## A.6.5.3.27.1Test Purpose and Environment

The purpose of this test is to verify that the EMR (early measurement reporting) based direct SCell activation delay as defined in clause 8.3.4, when the SCell in FR1 is unknown by the UE at the time of activation.

The supported test configurations for NR PCell are shown in table A.6.5.3.27.1-1. The supported test configurations for NR SCell are shown in table A.6.5.3.27.1-1A. Test configurations for NR PCell and test configurations for NR SCell are chosen independently.

The test scenario comprises one PCell (Cell 1) and one SCell (Cell 2) as outlined in table A.6.5.3.27.1-2. Cell-specific parameters for PCell and SCell are provided in table A.6.5.3.27.1-3 and table A.6.5.3.27.1-4, respectively.

There are two carriers, each with one cell. Cell 1 (PCell) is on RF channel 1 (PCC), and Cell 2 (SCell) is on RF channel 2 (SCC). Cell 1 and Cell 2 both operate according to one of the configurations in table A.6.5.3.27.1-1 and table A.6.5.3.27.1-1A respectively.

Before the test starts the UE is connected to Cell 1 on RF channel 1. The UE is only monitoring RF channel 1 and is not aware of Cell 2 on RF channel 2.

The test consists of 5 successive time periods, with time duration of T1, T2, T3, T4, and T5 respectively.

During T1, the UE is connected to Cell 1 only and shall not have any timing information of Cell 2. UE is configured with early measurement reporting for Cell 2 in

measIdleCarrierListNR-r16 for UE supporting measValidationReportEMR-r18 or

idleInactiveNR-MeasReport-r16 only, or

measReselectionCarrierListNR-r18 for UE supporting measValidationReportReselectionMeasurements-r18.

Beam level reporting for early measurements is configured. The time point when UE receives RRC_Release message from the TE defines the starting point of T2.

During T2 and T3 the UE is in idle mode.

At the beginning of T2, Cell 2 becomes detectable however cell reselection shall not be performed. Signal level of Cell 2 is set to the value given in table A.6.5.3.27.1-4. The time when T331 timer expires defines the ending point of T2.

At the beginning of T3, the signal level of the neighbour cell is set to turned off. The duration of the T3 equals to measIdleValidityDuration-r18 or measReselectionValidityDuration-r18 depending on the UE capabilities of the UE under test.

The time when TE sends the paging message is defined as the starting point of T4. During T4, in this test the UE shall send measurement report with SSB index of Cell 2 to the PCell.

At the beginning of T5 the UE receives the RRC connection reconfiguration message at the UE antenna connector. The corresponding slot at which the message is received at the UE antenna connector is denoted n. The UE shall complete activation of the SCell no later than in slot , as specified in clause 8.3.4 and in  is defined in clause 8.3.2A. From slot  and onwards the UE shall report valid CSI both for PCell and SCell.n+NdirectNR slot lengthTactivation_time  Ndirectn+NdirectNR slot length

The test equipment verifies the activation time by counting the slots between the RRC connection reconfiguration message is sent and until CSI report with non-zero CQI for both PCell and SCell is received.

Table A.6.5.3.27.1-1: Supported test configurations for NR PCell

Table A.6.5.3.27.1-1A: Supported test configurations for NR SCell

Table A.6.5.3.27.1-2: General test parameters

Table A.6.5.3.27.1-3: NR Cell specific test parameters for NR PCell

Table A.6.5.3.27.1-4: NR Cell specific test parameters for NR SCell

## A.6.5.3.27.2Test Requirements

The UE shall complete the SCell activation no later than at slot . n+NdirectNR slot length

The UE shall report non-zero CQI for SCell from slot  and onwards throughout time period T5.n+NdirectNR slot length

in  is defined in clause 8.3.2A in TS 38.133 for FR1 SCell as  is TFirstSSB_MAX + Trs + 5ms. Tactivation_time  NdirectTactivation_time

The observed SCell activation delay fulfilling the SCell activation delay requirements specified in clause 8.3.4 in TS 38.133 is counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90%.

## A.6.5.4UE UL carrier RRC reconfiguration Delay

## A.6.5.4.1UE UL carrier RRC reconfiguration Delay

Table A.6.5.4.1-1 - Table A.6.5.4.1-4 : Void

## A.6.5.4.1.1Test Purpose and Environment

The purpose of this test is to verify that when the UE receives a RRC message implying NR UL or Supplementary UL carrier configuration, the UE shall be ready to start transmission on the newly configured carrier within the time limits specified in clause 8.4.2 and 8.4.3 for configuring and deconfiguring, respectively.

There is one cell with two UL carriers: FR1 PCell and FR1 SUL. Both NR uplink and supplementary uplink are broadcast by ServingCellConfigCommonSIB. The test parameters for PCell and SUL are given in Table A. 6.5.4.1.1-1, Table A.6.5.4.1.1-2, Table A.6.5.4.1.1-3 and Table A.6.5.4.1.1-4 below.  The test consists of three time periods, with duration of T1, T2 and T3 respectively. During time duration T1, only NR uplink of PCell is configured to UE. At the start of T2, a supplementary uplink is configured to UE through RRCReconfiguration, then UE shall start transmission on the supplementary uplink. At the start of T3, the supplementary uplink is released through RRCReconfiguration.

Table A.6.5.4.1.1-1: Supported test configurations

Table A.6.5.4.1.1-2: General test parameters for NR standalone UE UL carrier RRC reconfiguration Delay on Pcell

Table A.6.5.4.1.1-3: NR Cell specific test parameters for NR standalone UE UL carrier RRC reconfiguration Delay on PCell

## A.6.5.4.1.2Test Requirements

The UE shall be ready to start transmission on the supplementary uplink carrier on SUL within 20ms from the start of T2.

The UE shall stop the transmission on the supplementary uplink carrier on SUL within 20ms from the start of T3.

All of the above test requirements shall be fulfilled in order for the observed UE UL carrier configuration delay and UE UL carrier release delay to be counted as correct. The rate of correct observed UE UL carrier configuration delay and UE UL carrier release delay during repeated tests shall be at least 90%.

## A.6.5.4.2Void

## A.6.5.5Beam Failure Detection and Link recovery procedures

## A.6.5.5.1Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode

## A.6.5.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.6.5.5.1.1-1, A.6.5.5.1.1-2, A.6.5.5.1.1-3 and A.6.5.5.1.1-4 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.6.5.5.1.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.6.5.5.1.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

Table A.6.5.5.1.1-1: Supported test configurations for FR1 PCell

Table A.6.5.5.1.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.6.5.5.1.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.6.5.5.1.1-4: Void

Figure A.6.5.5.1.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.6.5.5.1.1-2: L1-RSRP level variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.6.5.5.1.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 120+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.5.2Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode

## A.6.5.5.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.6.5.5.2.1-1, A.6.5.5.2.1-2, A.6.5.5.2.1-3, A.6.5.5.2.1-4 and A.6.5.5.2.1-5 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.6.5.5.2.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.6.5.5.2.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.6.5.5.2.1-1: Supported test configurations for FR1 PCell

Table A.6.5.5.2.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.6.5.5.2.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.6.5.5.2.1-4: Void

Table A.6.5.5.2.1-5: Void

Figure A.6.5.5.2.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in DRX mode

Figure A.6.5.5.2.1-2: L1-RSRP level variation for SSB-based beam failure detection and link recovery testing in DRX mode

## A.6.5.5.2.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 1920+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.5.3Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode

## A.6.5.5.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.6.5.5.3.1-1, A.6.5.5.3.1-2, and below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.6.5.5.3.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.6.5.5.3.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

Table A.6.5.5.3.1-1: Supported test configurations for FR1 PCell

Table A.6.5.5.3.1-2: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.6.5.5.3.1-3: Cell specific test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.6.5.5.3.1-4: Void

Table A.6.5.5.3.1-5: Void

Figure A.6.5.5.3.1-1: SNR variation for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Figure A.6.5.5.3.1-2: L1-RSRP level variation for CSI-RS based beam failure detection and link recovery testing in non-DRX mode

## A.6.5.5.3.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 30+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.5.4Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode

## A.6.5.5.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.6.5.5.4.1-1, A.6.5.5.4.1-2, A.6.5.5.4.1-3, and A.6.5.5.4.1-4 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.6.5.5.4.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.6.5.5.4.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.6.5.5.4.1-1: Supported test configurations for FR1 PCell

Table A.6.5.5.4.1-2: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.6.5.5.4.1-3: Cell specific test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.6.5.5.4.1-4: Void

Table A.6.5.5.4.1-5: Void

Table A.6.5.5.4.1-6: Void

Figure A.6.5.5.4.1-1: SNR variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Figure A.6.5.5.4.1-2: L1-RSRP level variation for CSI-RS based beam failure detection and link recovery testing in DRX mode

## A.6.5.5.4.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 1920+20 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.5.5Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode

## A.6.5.5.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP without schedulingRequestID-BFR-SCell-r16 configuration, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in tables A.6.5.5.5.1-1, A.6.5.5.5.1-2, and below. There are two cells, Cell 1 is the PCell and Cell 2 is the SCell, in the test. UE is not provided by schedulingRequestID-BFR-SCell-r16, i.e., no configuration for PUCCH transmission resources, and UE shall perform the random access procedure to recover the beam failure. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.6.5.5.5.1-1 shows the SNR of the CSI-RS in set q0 in the active SCell to emulate beam failure. Figure A.6.5.5.5.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery.  Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

Table A.6.5.5.5.1-1: Supported test configurations for FR1 PCell and SCell

Table A.6.5.5.5.1-2: General test parameters for FR1 SCell for beam failure detection and link recovery testing in non-DRX mode

Table A.6.5.5.5.1-3: Cell specific test parameters for FR1 SCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Figure A.6.5.5.5.1-1: SNR variation for beam failure detection and link recovery testing in for SCell non-DRX mode

Figure A.6.5.5.5.1-2: L1-RSRP level variation for beam failure detection and link recovery testing for SCell in non-DRX mode

## A.6.5.5.5.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 120+10 ms after the start of T5, the UE shall transmit preamble for UL-SCH resource application, followed by MAC-CE on the assigned uplink resources containing  a beam associated with the candidate beam set q1. The UE shall not transmit preamble earlier than time point B.

During T5, the System Simulator shall transmit a Random Access Response to UE after the System Simulator receives the preamble from UE. The UE shall transmit the msg.3 containing candidate beam set q1 for SCell BFR if UE receives the Random Access Response.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.5.6Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in DRX mode

## A.6.5.5.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based  beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP without schedulingRequestID-BFR-SCell-r16 configuration, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

The test parameters are given in Tables A.6.5.5.6.1-1, A.6.5.5.6.1-2, and A.6.5.5.6.1-3 below. There are two cells, Cell 1 is the PCell and Cell 2 is the SCell, in the test. UE is not provided by schedulingRequestID-BFR-SCell-r16, i.e., no configuration for PUCCH transmission resources, and UE shall perform the random access procedure to recover the beam failure. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.6.5.5.6.1-1 shows the SNR of the CSI-RS in set q0 in the active SCell to emulate beam failure. Figure A.6.5.5.6.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in SCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.6.5.5.6.1-1: Supported test configurations for FR1 PCell and SCell

Table A.6.5.5.6.1-2: General test parameters for FR1 SCell for beam failure detection and link recovery testing in DRX mode

Table A.6.5.5.6.1-3: Cell specific test parameters for FR1 SCell for beam failure detection and link recovery testing in DRX mode

Figure A.6.5.5.6.1-1: SNR variation for beam failure detection and link recovery testing for SCell in DRX mode

Figure A.6.5.5.6.1-2: L1-RSRP level variation for beam failure detection and link recovery testing for SCell in DRX mode

## A.6.5.5.6.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 120+10 ms after the start of T5, the UE shall transmit preamble for UL-SCH resource application, followed by MAC-CE on the assigned uplink resources containing  a beam associated with the candidate beam set q1. The UE shall not transmit preamble earlier than time point B.

During T5, the System Simulator shall transmit a Random Access Response to UE after the System Simulator receives the preamble from UE. The UE shall transmit the msg.3 containing candidate beam set q1 for SCell BFR if UE receives the Random Access Response.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.5.7TRP Specific Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode

## A.6.5.5.7.1Test Purpose and Environment

The test scenario is NR configured in the test contains two TRPs (i.e., TRP0 and TRP1). Each TRP is configured with different CSI-RS for beam failure detection and candidate beam detection. CSI-RS is configured as BFD-RS and CBD-RS.

The purpose of this test is to verify that the UE properly detects TRP specific CSI-RS-based beam failure in the sets q0,0  for TRP0  configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candidate set q1,0. The purpose is to test the downlink monitoring for beam failure detection on TRP0 within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based TRP specific beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.18 with schedulingRequestID-BFR-r17 configured.

The test parameters are given in Tables A.6.5.5.7.1-1, A.6.5.5.7.1-2, and A.6.5.5.7.1-3 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.6.5.5.7.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0,0  and q0,1  for TRP0 and TRP1 respectively to emulate CSI-RS based beam failure on TRP0. Figure A.6.5.5.7.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1,0 and q1,1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.6.5.5.7.1-1: Supported test configurations for FR1 PCell

Table A.6.5.5.7.1-2: General test parameters for FR1 PCell for CSI-RS-based TRP specific beam failure detection and link recovery testing in DRX mode

Table A.6.5.5.7.1-3: Cell specific test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Figure A.6.5.5.7.1-1: SNR variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Figure A.6.5.5.7.1-2: L1-RSRP level variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

## A.6.5.5.7.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1,0.

No later than time point F occurring no later than D1 = 1920+10 ms after the start of T5, the UE shall transmit PUCCH with LRR, followed by BFR MAC CE containing a beam associated with the candidate beam set q1,0. The UE shall not transmit PUCCH with an LRR with the candidate beam set q1,0 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.5.8Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode for a UE operating on a cell with less than 5 MHz BW

## A.6.5.5.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting support3MHz-ChannelBW-Symmetric-r18 properly detects SSB-based beam failure in the set q0 configured for a serving cell operating on a less than 5 MHz bandwidth, and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

Supported test configurations are specified in table A.6.5.5.8.1-1. General test parameters as specified in table A.6.5.5.1.1-2 with config 1 apply except those specified in table A.6.5.5.8.1-2. Cell specific test parameters as specified in table A.6.5.5.1.1-3 apply except those specified in table A.6.5.5.8.1-3.

The test procedure specified in clause A.6.5.5.1.1 applies to this test.

Table A.6.5.5.8.1-1: Supported test configurations for FR1 PCell

Table A.6.5.5.8.1-2: General test parameters for FR1 PCell

Table A.6.5.5.8.1-3: Cell specific test parameters for FR1 PCell

## A.6.5.5.8.2Test Requirements

Test requirements specified in clause A.6.5.5.1.2 apply to this test.

## A.6.5.5.9Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode for a UE operating with SBFD

## A.6.5.5.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting supportSBFD properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell operating on SBFD, and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the DL subband of UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5.

Supported test configurations are specified in Table A.6.5.5.9.1-1. General test parameters as specified in Table A.6.5.5.3.1-2 with config 3 apply except those specified in Table A.6.5.5.9.1-2. Cell specific test parameters as specified in Table A.6.5.5.3.1-3 apply except those specified in Table A.6.5.5.9.1-3.

The test procedure specified in clause A.6.5.5.3.1 applies to this test. In addition, during T3 and T5, there is overlapping between occasions of the CSI-RS resource for BFD (q0) and dynamic UL transmission on SBFD symbols, as specified in A.3.

Table A.6.5.5.9.1-1: Supported test configurations for FR1 PCell

Table A.6.5.5.9.1-2: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.6.5.5.9.1-3: Cell specific test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

## A.6.5.5.9.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 30+20+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.6Active BWP switch

## A.6.5.6.1DCI-based and Timer-based Active BWP Switch

## A.6.5.6.1.1NR FR1- NR FR1 DL active BWP switch of SCell with non-DRX in SA

A.6.5.6.1.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6, and interruption requirement on other active serving cell defined in clause 8.2.2.2.5.

The supported test configurations for PCell are shown in table A.6.5.6.1.1.1-1 below. Supported test configurations for NR SCell are shown in table A.6.5.6.1.1.1-1A below. Test configuration for NR PCell and test configuration for NR SCell are chosen independently. The test scenario comprises of one NR PCell (Cell 1) and one SCell (Cell 2) as given in table A.6.5.6.1.1.1-2. NR Cell-specific parameters are specified in table A.6.5.6.1.1.1-3 and table A.6.5.6.1.1.1-4 below.

PDCCHs indicating new transmissions shall be sent continuously on SCell (Cell 2) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 2 and the time duration of T2.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (SCell) on radio channel 2 (SCC).

-UE is configured with 2 different UE-specific downlink bandwidth parts for SCell, BWP-1 and BWP-2, in Cell 2 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is configured with 1 UE-specific downlink bandwidth parts the same as initial BWP for PCell, BWP-0 in Cell 1 before starting the test.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in SCell.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in PCell.

-UE is configured with a bwp-InactivityTimer timer value for SCell.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for SCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in SCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH no later than the first DL slot that occurs after the beginning of SCell’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the SCell on PCell no later than the first UL slot that occurs after the beginning of slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on SCell’s BWP-2 no later than the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).

The starting time of PCell (Cell 1) interruption due to BWP switch on SCell shall occur within the BWP switch delay.

During T2, the test equipment will not transmit DCI format for PDSCH reception on SCell (Cell 2).

During T3,

The time period T3 starts from the slot #j, where j is the first  slot of the subframe immediately after bwp-InactivityTimer timer expires. The UE should switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH no later than the first DL slot that occurs after the beginning of SCell’s slot (j+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the SCell on PCell at latest on the first UL slot that occurs after the beginning of slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on SCell’s BWP-1 no later than the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

The starting time of PCell (Cell 1) interruption due to BWP switch of SCell shall occur within the BWP switch delay.

The test equipment verifies the DL BWP switch time in SCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK/NACK is received.

The test equipment verifies that potential interruption to PCell is carried out in the correct time span by monitoring ACK/NACK sent in PCell during BWP switch of SCell, respectively.

Table A.6.5.6.1.1.1-1: DL BWP switch supported test configurations for NR PCell

Table A.6.5.6.1.1.1-1A: DL BWP switch supported test configurations for NR SCell

Table A.6.5.6.1.1.1-2: General test parameters for DL BWP switch in SA

Table A.6.5.6.1.1.1-3: NR Cell specific test parameters for NR PCell for DL BWP switch in SA

Table A.6.5.6.1.1.1-4: NR Cell specific test parameters for NR SCell for DL BWP switch in SA

A.6.5.6.1.1.2Test Requirements

During T1, the UE shall start to send the ACK/NACK for SCell on PCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for SCell on PCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in TS 38.321 [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed SCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

During T1 and T3, the start time of PCell interruption during SCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PCell shall not be longer than the interruption duration specified for active BWP switch in clause 8.2.2.2.5.

All of the above test requirements shall be fulfilled in order for the observed SCell active BWP switch interruption to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first DL slot that occurs after the beginning of DL slot (i+ TBWPswitchDelay+k1), (j+ TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

## A.6.5.6.1.2NR FR1 DL active BWP switch with non-DRX in SA

A.6.5.6.1.2.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6.

The supported test configurations are shown in table A.6.5.6.1.2.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.6.5.6.1.2.1-2. Cell-specific parameters of the cell are specified in table A.6.5.6.1.2.1-3 below.

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

During T2, the test equipment will not transmit DCI format for PDSCH reception on Cell 1.

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the subframe immediately after bwp-InactivityTimer timer expires. The UE shall switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s slot (j+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the Cell 1 at latest on the first UL slot that occurs after the beginning of slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on Cell 1’s BWP-1 starting from the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

The test equipment verifies the DL BWP switch time by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK/NACK is received.

Table A.6.5.6.1.2.1-1: DL BWP switch supported test configurations

Table A.6.5.6.1.2.1-2: General test parameters for DL BWP switch in SA

Table A.6.5.6.1.2.1-3: NR Cell specific test parameters for DL BWP switch in SA

A.6.5.6.1.2.2Test Requirements

During T1, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in TS 38.321 [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed Cell 1 active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first UL slot that occurs after beginning of DL slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

## A.6.5.6.2RRC-based Active BWP Switch

## A.6.5.6.2.1NR FR1 DL active BWP switch of Cell with non-DRX in SA

A.6.5.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6.

The supported test configurations are shown in table A.6.5.6.2.1.1-1. The test scenario comprises of one Cell (Cell 1) as given in table A.6.5.6.2.1.1-2. Cell-specific parameters of Cell are specified in table A.6.5.6.2.1.1-3 below.

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

Table A.6.5.6.2.1.1-1: DL BWP switch supported test configurations in SA scenario

Table A.6.5.6.2.1.1-2: General test parameters for DL BWP switch in SA scenario

Table A.6.5.6.2.1.1-3: NR Cell specific test parameters for DL BWP switch in SA scenario

A.6.5.6.2.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the Cell from the first DL slot that occurs right after the begining of slot  and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot. i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in TS 38.321 [7].

All of the above test requirements shall be fulfilled in order for the observed Cell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs

## A.6.5.6.3.1NR FR1- NR FR1 DL active BWP switch on multiple CCs with non-DRX in SA

A.6.5.6.3.1.1Test Purpose and Environment

The purpose of this test is to verify requirements on the DL BWP switch delay on multiple CCs and interruption requirement for NR victim cell, both defined in clause 8.6.

The supported test configurations for NR PCell are shown in table A.6.5.6.3.1.1-1 below. The supported test configurations for NR SCells are shown in table A.6.5.6.3.1.1-1A below. Test configuration for NR PCell and test configuration for NR SCells are chosen independently. Test configuration for two NR SCells are chosen independently. The test scenario comprises of one NR PCell (Cell 1) and two NR SCells (Cell 2 and Cell 3) as given in table A.6.5.6.3.1.1-2. NR Cell-specific parameters are specified in table A.6.5.6.3.1.1-3, table A.6.5.6.3.1.1-4 and table A.6.5.6.3.1.1-5 below.

PDCCHs indicating new transmissions shall be sent continuously on SCell (Cell 2) and SCell (Cell 3) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 2 and Cell 3 and the time duration of T2.

PDCCHs indicating new transmissions shall be sent continuously on SCell (Cell 3) to ensure that the UE will have ACK/NACK sending.Before the test starts,

-UE is connected to PCell (Cell 1) on radio channel 1 (PCC), and SCell (Cell 2) on radio channel 2 (SCC) and SCell (Cell 3) on radio channel 3(SCC).

-UE is configured with 2 different UE-specific downlink bandwidth parts for SCell (Cell 2) and SCell (Cell 3), BWP-1 and BWP-2, in Cell 2 and Cell 3 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is configured with a single UE-specific downlink bandwidth part, BWP-0, for PCell (Cell 1). BWP-0 includes the bandwidth of the initial DL BWP and SSB.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in SCell (Cell 2) and SCell (Cell 3).

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in PCell (Cell 1).

-UE is configured with a bwp-InactivityTimer timer value for SCell (Cell 2) and SCell (Cell 3).

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for both SCell (Cell 2) and SCell (Cell 3) DL BWP switch, sent from the test equipment to the UE, is received at the UE side in both SCell (Cell 2)’s and SCell (Cell 3)’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2 at both SCell (Cell 2) and SCell (Cell 3).

The UE shall be able to receive PDSCH no later than the first DL slot that occurs after the beginning of SCell (Cell 2)’s and SCell (Cell 3)’s DL slot (i+ TMultipleBWPswitchDelay) as defined in clause 8.6.2A.1 and starts to report valid ACK/NACK for the both SCell (Cell 2) and SCell (Cell 3) no later than the first UL slot that occurs after the beginning of slot (i+ TMultipleBWPswitchDelay +k1). The UE shall be continuously scheduled on both SCell (Cell 2)’s and SCell (Cell 3)’s BWP-2 no later than the first DL slot that occurs after the beginning of slot (i+ TMultipleBWPswitchDelay).

The starting time of PCell interruption due to BWP switch on SCell (Cell 2) and SCell (Cell 3) shall occur within the BWP switch delay.

During T2, the test equipment will not transmit DCI format for PDSCH reception on SCell (Cell 2) and SCell (Cell 3).

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the subframe immediately after bwp-InactivityTimer timer expires. The UE should switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1 on both SCell (Cell 2) and SCell (Cell 3).

The UE shall be able to receive PDSCH no later than the first DL slot that occurs after the beginning of SCell (Cell 2)’s an SCell (Cell 3)’s slot (j+ TMultipleBWPswitchDelay) as defined in clause 8.6.2A.1 and starts to report valid ACK/NACK for the SCell (Cell 2) and SCell (Cell 3) no later than the first UL slot that occurs after the beginning of slot (j+ TMultipleBWPswitchDelay +k1). The UE shall be continuously scheduled on SCell (Cell 2)’s and SCell (Cell 3)’s BWP-1 no later than the first DL slot that occurs after the beginning of slot (j+ TMultipleBWPswitchDelay).

The starting time of PCell interruption due to BWP switch of SCell (Cell 2) and SCell (Cell 3) shall occur within the BWP switch delay.

The test equipment verifies the DL BWP switch time in SCells by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK/NACK is received.

The test equipment verifies that potential interruption to PCell is carried out in the correct time span by monitoring ACK/NACK sent in PCell during BWP switch of SCells, respectively.

Table A.6.5.6.3.1.1-1: DL BWP switch supported test configurations for NR PCell

Table A.6.5.6.3.1.1-1A: DL BWP switch supported test configurations for NR SCells

Table A.6.5.6.3.1.1-2: General test parameters for DL BWP switch in SA

Table A.6.5.6.3.1.1-3: NR Cell specific test parameters for NR PCell for DL BWP switch in SA

Table A.6.5.6.3.1.1-4: NR Cell specific test parameters for SCell (NR Cell 2) for DL BWP switch in SA

Table A.6.5.6.3.1.1-5: NR Cell specific test parameters for SCell (NR Cell 3) for DL BWP switch in SA

A.6.5.6.3.1.2Test Requirements

During T1, the UE shall start to send the ACK/NACK for both SCell (Cell 2) and SCell (Cell 3) from the first UL slot that occurs after the beginning of DL slot (i+ TMultipleBWPswitchDelay +k1).

During T3, the UE shall start to send the ACK/NACK for both SCell (Cell 2) and SCell (Cell 3) from the first UL slot that occurs after the beginning of DL slot (j+ TMultipleBWPswitchDelay +k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in TS 38.321 [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TMultipleBWPswitchDelay defined in 8.6.2A.1.

All of the above test requirements shall be fulfilled in order for the observed Cell 2 and Cell 3 active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

During T1 and T3, the start time of PCell interruption during SCell (Cell 2) and SCell (Cell 3) active BWP switch shall not happen outside the BWP switch delay.

The interruption of PCell shall not be longer than the interruption duration specified for active BWP switch in clause 8.2.2.2.5.

All of the above test requirements shall be fulfilled in order for the observed SCell (Cell 2) and SCell (Cell 3) active BWP switch interruption to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first UL slot that occurs after beginning of DL slot (i+ TMultipleBWPswitchDelay +k1), (j+ TMultipleBWPswitchDelay +k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

## A.6.5.6.4SCell dormancy switch

## A.6.5.6.4.1NR FR1 PCell SCell dormancy switch of single FR1 SCell outside active time

## A.6.5.6.4.1.1Test Purpose and Environment

The purpose of this test is to verify the SCell dormancy switch delay requirements defined in clause 8.6 when the UE is triggered to switch between dormancy to non-dormancy and non-dormancy to dormancy outside the DRX active time. Further the test purpose is to verify the interruption rate on other serving cells when the UE performing CSI and RRM measurements on dormant SCell(s) as defined in clause 8.2.2.2.12 and also to verify the interruption requirement on other active serving cell defined in clause 8.2.2.2.5.

In the test scenario UE is connected to one PCell (Cell 1) in FR1 and one SCell in FR1. In the test the SCell is switched from non-dormancy to dormancy, and vice versa, at a point in time before start of onDuration. The UE is configured to monitor PDCCH for DCI format 2_6 at ps-Offset before the start of onDuration. Two tests are specified, where a UE that only supports triggering within the first three OFDM symbols of a slot shall undergo Test1 only, and a UE that supports triggering also in remaining OFDM symbols of a slot shall undergo both Test1 and Test2. In the tested scenario, ps-Offset is selected to correspond to the dormancy switching time specified in clause 8.6.

The supported test configurations for NR PCell are shown in table A.6.5.6.4.1.1-1, The supported test configurations for NR SCell are shown in table A.6.5.6.4.1.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently. The general test parameters are given in table A.6.5.6.4.1.1-2. NR Cell-specific parameters are specified in table A.6.5.6.4.1.1-3 and table A.6.5.6.4.1.1-4.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (SCell) on radio channel 2 (SCC).

-UE is configured with 1 UE-specific downlink bandwidth parts the same as initial BWP for PCell, BWP-0 in Cell 1 before starting the test.

-UE is configured with 2 different UE-specific downlink bandwidth parts for SCell, BWP-1 and BWP-2, in Cell 2 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in PCell.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in SCell.

-UE is indicated in dormantBWP -Id that the active DL BWP is BWP-2 in the SCell.

-UE is configured with DRX.

-UE is configured to monitor DCI format 2_6, and to be active during onDuration even when no DCI format 2_6 is detected (ps-WakeUp).

All cells have constant signal levels throughout the test.

The test consists of 4 successive time periods, with durations of T1, T2, T3 and T4, respectively.

During T1,

Time period T1 starts when a DCI format 2_6 command intended for dormant BWP switch in a SCell from non-dormancy to dormancy, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i (at ps-Offset before onDuration). Upon reception of the PDCCH indicating entering dormant BWP in PCell (i.e. through cross-carrier scheduling), UE shall switch the DL BWP-1 to DL BWP-2 in SCell, i.e., switching from non-dormant BWP to dormant BWP and the UE shall complete the switching before the start of onDuration.

The UE shall be able to receive PDCCH on PCell no later than the first DL slot that occurs after the beginning of PCell’s DL slot (i+ TdormantBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK on the PCell no later than the first UL slot that occurs after the beginning of slot (i+N) as defined in clause 10.3 in TS38.213. The UE shall be continuously scheduled on PCell’s BWP-0 no later than the first DL slot that occurs after the beginning of slot (i+ TdormantBWPswitchDelay).

The starting time of PCell (Cell 1) interruption due to dormancy switching on SCell shall occur within the dormant BWP switch delay, i.e. before start of onDuration.

The UE shall not transmit signals on SCell after the beginning of PCell’s DL slot (i+ TdormantBWPswitchDelay) as defined in clause 8.6. The UE shall not be scheduled on SCells BWP-1 no later than the first DL slot that occurs after the beginning of slot (i+ TdormantBWPswitchDelay).

Time period T2 starts when T1 is completed. During T2, the test equipment continues to schedule the UE continuously in PCell. The UE shall carry out CSI and RRM measurements on the dormant SCells. The UE shall report ACK/NACK in PCell in response to scheduled PDSCH, with the maximum loss of transmitted ACK/NACKs fulfilling the requirement in clause 8.2.2.2.12. The test equipment verifies that the loss of ACK/NACKs is no larger than 1.5 %.

Time period T3 starts when T2 is completed. During T3, the test equipment does not schedule the UE, by which the inactivity timer expires and the UE stops monitoring PDCCH except for signalling using DCI format 2_6 at wake-up signalling occasions.

During T4,

Time period T4 starts when a DCI format 2_6 command for leaving dormant BWP in SCell, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted j (at ps-Offset before onDuration). Upon reception of the PDCCH indicating leaving dormant BWP in PCell (i.e. through cross-carrier scheduling), UE shall switch the DL BWP-2 to DL BWP-1 in SCell, i.e., switching from dormant BWP to non-dormant BWP.

The UE shall be able to receive PDSCH on PCell and SCell no later than the first DL slot that occurs after the beginning of PCell’s DL slot (j+ TdormantBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK on the PCell (for both PCell and SCell) no later than the first UL slot that occurs after the beginning of slot (j+N) as defined in clause 10.3 in TS 38.213. The UE shall be continuously scheduled on PCell’s BWP-0 no later than the first DL slot that occurs after the beginning of slot (j+ TdormantBWPswitchDelay).

The starting time of PCell (Cell 1) interruption due to dormancy switching on SCell shall occur within the dormant BWP switch delay.

The UE shall be ready to transmit signals on SCell no later than the first DL slot that occurs after the beginning of PCell’s DL slot (j+ TdormantBWPswitchDelay) as defined in clause 8.6. The UE shall be ready to continuously scheduled on SCell’s BWP-1 no later than the first DL slot that occurs after the beginning of slot (j+ TdormantBWPswitchDelay).

The test equipment verifies the DL dormant BWP switch time in SCell by counting the slots from the time when the dormant BWP switch command is received till an ACK/NACK on PCell is received.

The test equipment verifies that potential interruption to PCell is carried out in the correct time span by monitoring ACK/NACK sent in PCell during dormant BWP switch of SCell (i.e. before start of onDuration), respectively.

Table A.6.5.6.4.1.1-1A: SCell dormancy switch supported test configurations for NR SCell

Table A.6.5.6.4.1.1-2: General test parameters for SCell dormancy switch in SA

Table A.6.5.6.4.1.1-3: NR Cell specific test parameters for NR PCell for SCell dormancy switch in SA

Table A.6.5.6.4.1.1-4: NR Cell specific test parameters for NR SCell for SCell dormancy switch in SA

## A.6.5.6.4.1.2Test Requirements

During T1, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (i+N) (i.e. from the start of onDuration).

During time period T2, the UE shall transmit ACK/NACKs in response to scheduling in PCell and the rate of missed ACK/NACKs shall be no more than 1.5 %.

During T4, the UE shall start to send the ACK/NACK for PCell and SCell from the first UL slot that occurs after the beginning of DL slot (j+N) (i.e. from the start of onDuration).

Where, N is the timing that UE provide HARQ-ACK information in response to a detection of a DCI format 2_6 indicating SCell dormancy as specified in [3].

All of the above test requirements shall be fulfilled in order for the observed SCell dormant BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

During T1 and T4, the start time of PCell interruption during SCell dormant BWP switch shall not happen outside the dormant BWP switch delay.

The interruption of PCell shall not be longer than the interruption duration specified for dormant BWP switch in clause 8.6.

NOTE:During T1, T4 if there are no uplink resources for reporting the ACK/NACK in the first DL slot that occurs after the beginning of DL slot (i+ N), (j+ N), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

## A.6.5.6.4.2NR FR1 PCell SCell dormancy switch of two FR1 SCells inside active time

## A.6.5.6.4.2.1Test Purpose and Environment

The purpose of this test is to verify fulfillment of SCell dormancy switching delay requirements in clause 8.6.2A, requirements on interruptions due to SCell dormancy switching in clause 8.2.2.2.12.1, and requirements on interruptions due to CSI and RRM measurements on dormant SCells in clauses 8.2.2.2.12.2 and 8.2.2.2.12.3, respectively. In the tested scenario, the UE is connected to PCell and two SCells in FR1, and the SCells are switched from non-dormancy to dormancy, and back, during active time. Depending on UE capability on whether DCI for dormancy switching can be received also later than within the initial three OFDM symbols of a slot, the UE may have to undergo one or two sets of tests. A UE that only supports triggering during within the first three OFDM symbols of a slot shall only undergo Test1 and Test2, whereas a UE that supports triggering also in remaining OFDM symbols of a slot shall undergo Test1 through Test4.

The supported test configurations for NR PCell are provided in table A.6.5.6.4.2.1-1 below. The supported test configurations for NR SCells are provided in table A.6.5.6.4.2.1-1A below. Test configuration for NR PCell and test configuration for NR SCells are chosen independently. Test configurations for two NR SCells are chosen independently. General test parameters are provided in table A.6.5.6.4.2.1-2, and cell-specific parameters are provided in table A.6.5.6.4.2.1-3, table A.6.5.6.4.2.1-4 and table A.6.5.6.4.2.1-5 below.

The tests consist of three consecutive time periods T1, T2, and T3, respectively.

Three carriers are used in the test, each within FR1 and each with one cell. Cell 1 (PCell) is on RF channel 1 (PCC), Cell 2 (SCell 1) is on RF channel 2 (SCC1), and Cell 3 (SCell2) is on RF channel 3 (SCC2). All three cells have constant signal levels throughout the test. The UE is continuously scheduled in PCell throughout the test.

Before the test starts,

-UE is connected to Cell 1 (PCell), Cell 2 (SCell 1) and Cell 3 (SCell2).

-UE is configured with a single UE-specific downlink bandwidth part, BWP-0, for Cell 1. BWP-0 includes the bandwidth of the initial DL BWP and SSB.

-UE is configured with one non-dormant and one dormant UE-specific downlink bandwidth part, BWP-0 and BWP-1, respectively, for Cell 2 and Cell 3. BWP-0 includes the bandwidth of the initial DL BWP and SSB.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP in Cell 1 is BWP-0.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP in Cell 2 is BWP-0.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP in Cell 3 is BWP-0.

-UE is continuously scheduled in PCell, SCell 1 and SCell2.

T1 starts at the point in time at which the UE receives a DCI with dormancy indication on PDCCH in PCell at the antenna connector, in a slot # denoted m, pertaining to dormancy indication for switching SCell 1 and SCell2 from non-dormancy to dormancy. The UE shall complete switching of the SCells to dormancy by the end of slot m + ceil(TMultipleBWPswitchDelay/NR slot length) + 1 in Test1 and Test2, and slot m + ceil(TMultipleBWPswitchDelay/NR slot length) + 2 in Test3 and Test4, as specified in clause 8.6.2A. Any PCell interruptions due to the switching between non-dormant and dormant BWPs shall fulfill requirements in clause 8.2.2.2.12.1. The test equipment verifies that interruptions due to switching from non-dormancy to dormancy are within the requirements by analysing HARQ feedback transmitted in PCell for PCell.

During T2, the UE is carrying out CSI and RRM measurements on dormant SCell 1 and SCell2. Any PCell interruptions due to CSI and RRM measurements shall fulfill requirements in clauses 8.2.2.2.12.2 and 8.2.2.2.12.3, respectively. The test equipment verifies that the interruptions are within the allowed percentages by counting ACK/NACKs in PCell. At the end of T2, the test equipment transmits a DCI with dormancy indication on PDCCH in PCell carrying a dormany indication for switching SCell 1 and SCell2 from dormancy to non-dormancy.

T3 starts at the point in time at which the UE receives a DCI with dormancy indication on PDCCH in PCell at the antenna connector, in a slot # denoted n, pertaining to dormancy indication for switching SCell 1 and SCell2 from dormancy to non-dormancy. The UE shall complete switching of the SCells to non-dormancy by the end of slot n + ceil(TMultipleBWPswitchDelay/NR slot length) + 1 in Test1 and Test2, and slot n + ceil(TMultipleBWPswitchDelay/NR slot length) + 2 in Test3 and test4, as specified in clause 8.6.2A. Any PCell interruptions due to the switching between dormant and non-dormant BWPs shall fulfill requirements in clause 8.2.2.2.12.1. The test equipment verifies that interruptions due to switching from dormancy to non-dormancy are within the requirements by analysing HARQ feedback transmitted in PCell for PCell. The test equipment verifies the switching delay by analysing HARQ feedback transmitted in PCell for SCells.

Table A.6.5.6.4.2.1-1: Supported test configurations for NR PCell

Table A.6.5.6.4.2.1-1A: Supported test configurations for NR SCells

Table A.6.5.6.4.2.1-2: General test parameters

Table A.6.5.6.4.2.1-3: NR Cell specific test parameters for NR Pcell

Table A.6.5.6.4.2.1-4: NR Cell specific test parameters for NR SCell (Cell 2)

Table A.6.5.6.4.2.1-5: NR Cell specific test parameters for NR SCell (Cell 3)

## A.6.5.6.4.2.2Test Requirements

During T1, any interruption on PCell due to dormancy switching of SCells shall be within the requirement specified in clause 8.2.2.2.12.1.

During T2, interruptions on PCell due to CSI and RRM measurements on dormant SCells shall be within the interruption rate requirements specified in clauses 8.2.2.2.12.2 and 8.2.2.2.12.3, respectively.

During T3, any interruption on PCell due to dormancy switching of SCells shall be within the requirement specified in clause 8.2.2.2.12.1. Monitoring of PDCCH for SCell in SCell shall be resumed within the dormancy switching time specified in clause 8.6.2A.

For an event to be considered to be correct, all requirements above have to be fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.6.5Simultaneous RRC-based Active BWP Switch on multiple CCs

## A.6.5.6.5.1NR FR1- NR FR1 DL active BWP switch on multiple CCs with non-DRX in SA

A.6.5.6.5.1.1Test Purpose and Environment

The purpose of this test is to verify requirements on the RRC-based DL BWP switch delay on multiple CCs defined in clause 8.6.

The supported test configurations for NR PCell are shown in table A.6.5.6.5.1.1-1 below. The supported test configurations for NR SCell are shown in table A.6.5.6.5.1.1-1A below. Test configuration for NR PCell and test configuration for NR SCell are chosen independently. The test scenario comprises of one NR PCell (Cell 1) and one NR SCell (Cell 2) as given in table A.6.5.6.5.1.1-2. NR Cell-specific parameters are specified in table A.6.5.6.5.1.1-3 and A.6.5.6.5.1.1-4 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) and SCell (Cell 2) to ensure that the UE would have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), Cell 2 (SCell) on radio channel 2 (SCC).

-UE has bandwidth part BWP-1 in its RRC-configuration for PCell and SCell (Cell 2).

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PCell and SCell (Cell 2).

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration for both PCell and SCell (Cell 2), sent from the test equipment to the UE, is completely received at the UE side in PCell’s and SCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition for both PCell and SCell (Cell 2).

The UE shall be able to receive PDSCH on PCell and SCell (Cell 2) from the first DL slot that occurs after the beginning of DL slot as defined in clause 8.6.3A.1 and starts to report valid ACK/NACK for the PCell and SCell (Cell 2) from the first UL slot that occurs after the beginning of DL slot on BWP-1 of final condition. The UE shall be continuously scheduled on PCell’s and SCell (Cell 2)’s BWP-1 of final condition starting from the first DL slot right after slot . i+TRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot length i+TRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot length+k1i+TRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot length

TRRCprocessingDelay, TBWPswitchDelayRRC and DRRC are defined in clause 8.6.3A.1, N=2 in this test case.

The test equipment verifies the DL BWP switch time in PCell and SCell by counting the slots from the time when the RRC Reconfiguration message including updated BWP configuration is sent till the time when a vaild ACK/NACK is received.

Table A.6.5.6.5.1.1-1: DL BWP switch supported test configurations for NR PCell

Table A.6.5.6.5.1.1-1A: DL BWP switch supported test configurations for NR SCell

Table A.6.5.6.5.1.1-2: General test parameters for DL BWP switch in SA

Table A.6.5.6.5.1.1-3: NR Cell specific test parameters for NR PCell for DL BWP switch in SA

Table A.6.5.6.5.1.1-4: NR Cell specific test parameters for NR SCell for DL BWP switch in SA

A.6.5.6.5.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for both PCell and SCell (Cell 2) from the first DL slot that occurs right after the begining of slot  and starts to report valid ACK/NACK for both PCell and SCell (Cell 2) from the first UL slot that occurs after the beginning of DL slot. (i+TRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot length) (i+ TRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot length+k1)

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch on PCell and SCell (Cell 2) within the time duration  defined in 8.6.3A.1.TRRCprocessingDelay+TBWPswitchDelayRRC+DRRC

All of the above test requirements shall be fulfilled in order for the observed PCell and SCell (Cell 2) active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1 if there are no uplink resources for reporting the ACK/NACK in the first UL slot that occurs after beginning of DL slot (i+ +k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.TRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot length

## A.6.5.7DL interruptions at switching between two uplink carriers

## A.6.5.7.1DL interruptions at switching between two uplink carriers in FDD-TDD CA

## A.6.5.7.1.1Test Purpose and Environment

The purpose of this test is to verify DL interruption requirements during UE dynamic switching between two uplink carriers defined in clause 8.2.2.2.10. The test case is applicable for an uplink band pair of an inter-band FDD-TDD CA configuration when the capability uplinkTxSwitchingPeriod is present.

There are two cells: FR1 FDD PCell (Cell 1), FR1 TDD SCell (Cell 2). The test parameters for the two cells are given in table A.6.5.7.1.1-1, table A.6.5.7.1.1-2 and table A.6.5.7.1.1-3 below.

For NR FDD carrier (Cell 1), aperiodic CSI-RS for L1-RSRP reporting is triggered with power boosting 6 dB on the following symbol in the slot overlapping with the 1 st special slot of every radio frame of the NR TDD carrier (Cell 2):

symbol#12 if UE does not report uplinkTxSwitching-DL-Interruption-r16;

otherwise,

symbol #8 if UE capability uplinkTxSwitchingPeriod is 210 us or

symbol #9 if UE capability uplinkTxSwitchingPeriod is 140 us or

symbol #10 if UE capability uplinkTxSwitchingPeriod is 35 us.

For NR TDD carrier (Cell 2), aperiodic CSI-RS for L1-RSRP reporting is configured with power boosting 6 dB on the following symbol in the 2nd special slot of every radio frame:

symbol#9 if UE does not report uplinkTxSwitching-DL-Interruption-r16;

otherwise,

symbol #2 if UE capability uplinkTxSwitchingPeriod is 210 us or

symbol #3 if UE capability uplinkTxSwitchingPeriod is 140 us or

symbol #6 if UE capability uplinkTxSwitchingPeriod is 35 us.

This test verifies that the UE correctly report the L1-RSRP reporting. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, uplinkTxSwitching is indicated to UE.

Table A.6.5.7.1.1-1: Supported test configurations

Table A.6.5.7.1.1-2: General test parameters for DL interruptions at switching between two uplink carriers in FDD-TDD CA

Table A.6.5.7.1.1-3: Cell specific test parameters for DL interruptions at switching between two uplink carriers in FDD-TDD CA

## A.6.5.7.1.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.2.2.2.10.

UE shall send L1-RSRP report while meeting the accuracy requirements defined in clause 10.1.19.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.7.2DL interruptions at switching between two uplink carriers in TDD-TDD CA

## A.6.5.7.2.1Test Purpose and Environment

The purpose of this test is to verify DL interruption requirements during UE dynamic switching between two uplink carriers defined in clause 8.2.2.2.10. The test case is applicable for an uplink band pair of an inter-band TDD-TDD CA configuration when the capability uplinkTxSwitchingPeriod is present.

There are two cells: FR1 TDD PCell (Cell 1), FR1 TDD SCell (Cell 2). The test parameters for the two cells are given in table A.6.5.7.2.1-1, table A.6.5.7.2.1-2 and table A.6.5.7.2.1-3 below.

For NR TDD PCell (Cell 1), aperiodic CSI-RS for L1-RSRP reporting is triggered with power boosting 6 dB on the following symbol in the 1 st special slot of every even radio frame:

symbol#10 if UE does not report uplinkTxSwitching-DL-Interruption-r16;

otherwise,

symbol #4 if UE capability uplinkTxSwitchingPeriod is 210 us or

symbol #5 if UE capability uplinkTxSwitchingPeriod is 140 us or

symbol #8 if UE capability uplinkTxSwitchingPeriod is 35 us.

For NR TDD SCell (Cell 2), aperiodic CSI-RS for L1-RSRP reporting is configured with power boosting 6 dB on the following symbol on the 2nd special slot of every even radio frame:

symbol#10 if UE does not report uplinkTxSwitching-DL-Interruption-r16;

otherwise,

symbol #4 if UE capability uplinkTxSwitchingPeriod is 210 us or

symbol #5 if UE capability uplinkTxSwitchingPeriod is 140 us or

symbol #8 if UE capability uplinkTxSwitchingPeriod is 35 us.

This test verifies that the UE correctly report the L1-RSRP reporting. The test case is only applicable to UE which supports simultaneousRxTxInterBandCA.

The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, uplinkTxSwitching is indicated to UE.

Table A.6.5.7.2.1-1: Supported test configurations

Table A.6.5.7.2.1-2: General test parameters for DL interruptions at switching between two uplink carriers in TDD-TDD CA

Table A.6.5.7.2.1-3: Cell specific test parameters for DL interruptions at switching between two uplink carriers in TDD-TDD CA

## A.6.5.7.2.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.2.2.2.10.

UE shall send L1-RSRP report while meeting the accuracy requirements defined in clause 10.1.19.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.7ADL interruptions at switching between two uplink carriers with two transmit antenna connectors

## A.6.5.7A.1DL interruptions at switching between two uplink carriers in FDD-TDD CA

## A.6.5.7A.1.1Test Purpose and Environment

The purpose of this test is to verify DL interruption requirements during UE dynamic switching between two uplink carriers defined in clause 8.2.2.2.10A. The test case is applicable for an uplink band pair of an inter-band FDD-TDD CA configuration when the capability uplinkTxSwitchingPeriod2T2T is present, where NR UL carrier 1 is capable of two transmit antenna connectors and NR UL carrier 2 is capable of two transmit antenna connectors, and the two uplink carriers are in different bands with different carrier frequencies.

There are two cells: FR1 FDD PCell (Cell 1), FR1 TDD SCell (Cell 2). The test parameters for the two cells are given in table A.6.5.7A.1.1-1, table A.6.5.7A.1.1-2 and table A.6.5.7A.1.1-3 below.

For NR FDD carrier (Cell 1), aperiodic CSI-RS for L1-RSRP reporting is triggered with power boosting 6dB on the following symbol in the slot overlapping with the 1st special slot of every radio frame of the NR TDD carrier (Cell 2):

-symbol#12 if UE does not report uplinkTxSwitching-DL-Interruption-r16;

-otherwise,

-symbol #8 if UE capability uplinkTxSwitchingPeriod2T2T is 210 us or

-symbol #9 if UE capability uplinkTxSwitchingPeriod2T2T is 140 us or

-symbol #10 if UE capability uplinkTxSwitchingPeriod2T2T is 35 us.

For NR TDD carrier (Cell 2), aperiodic CSI-RS for L1-RSRP reporting is configured with power boosting 6dB on the following symbol in the 2nd special slot of every radio frame:

-symbol#9 if UE does not report uplinkTxSwitching-DL-Interruption-r16;

-otherwise,

-symbol #2 if UE capability uplinkTxSwitchingPeriod2T2T is 210 us or

-symbol #3 if UE capability uplinkTxSwitchingPeriod2T2T is 140 us or

-symbol #6 if UE capability uplinkTxSwitchingPeriod2T2T is 35 us.

This test verifies that the UE correctly report the L1-RSRP reporting. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, uplinkTxSwitching is indicated to UE.

Table A.6.5.7A.1.1-1: Supported test configurations

Table A.6.5.7A.1.1-2: General test parameters for DL interruptions at switching between two uplink carriers in FDD-TDD CA

Table A.6.5.7A.1.1-3: Cell specific test parameters for DL interruptions at switching between two uplink carriers in FDD-TDD CA

## A.6.5.7A.1.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.2.2.2.10A.

UE shall send L1-RSRP report while meeting the accuracy requirements defined in clause 10.1.19.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.7A.2DL interruptions at switching between two uplink carriers in TDD-TDD CA

## A.6.5.7A.2.1Test Purpose and Environment

The purpose of this test is to verify DL interruption requirements during UE dynamic switching between two uplink carriers defined in clause 8.2.2.2.10A. The test case is applicable for an uplink band pair of an inter-band TDD-TDD CA configuration when the capability uplinkTxSwitchingPeriod2T2T is present, where NR UL carrier 1 is capable of two transmit antenna connectors and NR UL carrier 2 is capable of two transmit antenna connectors, and the two uplink carriers are in different bands with different carrier frequencies.

There are two cells: FR1 TDD PCell (Cell 1), FR1 TDD SCell (Cell 2). The test parameters for the two cells are given in table A.6.5.7A.2.1-1, table A.6.5.7A.2.1-2 and table A.6.5.7A.2.1-3 below.

For NR TDD PCell (Cell 1), aperiodic CSI-RS for L1-RSRP reporting is triggered with power boosting 6dB on the following symbol in the 1st special slot of every even radio frame:

-symbol#10 if UE does not report uplinkTxSwitching-DL-Interruption-r16;

-otherwise,

-symbol #4 if UE capability uplinkTxSwitchingPeriod2T2T is 210 us or

-symbol #5 if UE capability uplinkTxSwitchingPeriod2T2T is 140 us or

-symbol #8 if UE capability uplinkTxSwitchingPeriod2T2T is 35 us.

For NR TDD SCell (Cell 2), aperiodic CSI-RS for L1-RSRP reporting is configured with power boosting 6dB on the following symbol on the 2nd special slot of every even radio frame:

-symbol#10 if UE does not report uplinkTxSwitching-DL-Interruption-r16;

-otherwise,

-symbol #4 if UE capability uplinkTxSwitchingPeriod2T2T is 210 us or

-symbol #5 if UE capability uplinkTxSwitchingPeriod2T2T is 140 us or

-symbol #8 if UE capability uplinkTxSwitchingPeriod2T2T is 35 us.

This test verifies that the UE correctly report the L1-RSRP reporting. The test case is only applicable to UE which supports simultaneousRxTxInterBandCA.

The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, uplinkTxSwitching is indicated to UE.

Table A.6.5.7A.2.1-1: Supported test configurations

Table A.6.5.7A.2.1-2: General test parameters for DL interruptions at switching between two uplink carriers in TDD-TDD CA

Table A.6.5.7A.2.1-3: Cell specific test parameters for DL interruptions at switching between two uplink carriers in TDD-TDD CA

## A.6.5.7A.2.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.2.2.2.10A.

UE shall send L1-RSRP report while meeting the accuracy requirements defined in clause 10.1.19.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.7BDL interruptions at switching between one uplink band with one transmit antenna connector and one uplink band with two transmit antenna connectors

## A.6.5.7B.1DL interruptions at switching between two uplink bands in FDD-TDD CA

## A.6.5.7B.1.1Test Purpose and Environment

The purpose of this test is to verify DL interruption requirements during UE dynamic switching between two uplink bands defined in clause 8.2.2.2.10B. The test case is applicable for an uplink band pair of an inter-band UL CA configuration when the capability uplinkTxSwitchingPeriod is present, where NR UL carrier 1 in band A is capable of one transmit antenna connector, NR UL carrier 2 and carrier 3 in band B are capable of two transmit antenna connectors. NR UL carrier 2 and carrier 3 are two contiguous aggregated carriers, and band A and band B are different bands with different carrier frequencies.

There are three cells: FR1 FDD PCell (Cell 1), FR1 TDD SCell (Cell 2) and FR1 TDD SCell (Cell 3) where Cell 1 in band A is with 1TX, cell2 and Cell 3 in band B with 2Tx, cell2 and cell3 are two contiguous aggregated carriers. The test parameters for the three cells are given in table A.6.5.7B.1.1-1, table A.6.5.7B.1.1-2 and table A.6.5.7B.1.1-3 below.

For NR FDD carrier (Cell 1), aperiodic CSI-RS for L1-RSRP reporting is triggered with power boosting 6 dB on the following symbol in the slot overlapping with the 1 st special slot of every radio frame of the NR TDD carrier (Cell 2):

-symbol#12 if UE does not report uplinkTxSwitching-DL-Interruption-r16;

-otherwise,

-symbol #8 if UE capability uplinkTxSwitchingPeriod is 210 us or

-symbol #9 if UE capability uplinkTxSwitchingPeriod is 140 us or

-symbol #10 if UE capability uplinkTxSwitchingPeriod is 35 us.

For NR TDD Cell 2 and NR TDD Cell 3, aperiodic CSI-RS for L1-RSRP reporting is configured with power boosting 6 dB on the following symbol in the 2nd special slot of every radio frame:

-symbol#9 if UE does not report uplinkTxSwitching-DL-Interruption-r16;

-otherwise,

-symbol #2 if UE capability uplinkTxSwitchingPeriod is 210 us or

-symbol #3 if UE capability uplinkTxSwitchingPeriod is 140 us or

-symbol #6 if UE capability uplinkTxSwitchingPeriod is 35 us.

This test verifies that the UE correctly report the L1-RSRP reporting. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, uplinkTxSwitching is indicated to UE.

Table A.6.5.7B.1.1-1: Supported test configurations

Table A.6.5.7B.1.1-2: General test parameters for DL interruptions at switching between two uplink bands in FDD-TDD CA

Table A.6.5.7B.1.1-3: Cell specific test parameters for DL interruptions at switching between two uplink bands in FDD-TDD CA

## A.6.5.7B.1.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.2.2.2.10B.

UE shall send L1-RSRP report while meeting the accuracy requirements defined in clause 10.1.19.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.7B.2DL interruptions at switching between two uplink bands in TDD-TDD CA

## A.6.5.7B.2.1Test Purpose and Environment

The purpose of this test is to verify DL interruption requirements during UE dynamic switching between two uplink bands defined in clause 8.2.2.2.10B. The test case is applicable for an uplink band pair of an inter-band UL CA configuration when the capability uplinkTxSwitchingPeriod is present, where NR UL carrier 1 in band A is capable of one transmit antenna connector, NR UL carrier 2 and carrier 3 in band B are capable of two transmit antenna connectors. NR UL carrier 2 and carrier 3 are two contiguous aggregated carriers, and band A and band B are different bands with different carrier frequencies.

There are three cells: FR1 TDD PCell (Cell 1), FR1 TDD SCell (Cell 2) and FR1 TDD SCell (Cell 3) where Cell 1 in band A is with 1TX, cell2 and Cell 3 in band B with 2Tx, cell2 and cell3 are two contiguous aggregated carriers.The test parameters for the three cells are given in table A.6.5.7B.2.1-1, table A.6.5.7B.2.1-2 and table A.6.5.7B.2.1-3 below.

For NR TDD PCell (Cell 1), aperiodic CSI-RS for L1-RSRP reporting is triggered with power boosting 6 dB on the following symbol in the 1 st special slot of every even radio frame:

-symbol#10 if UE does not report uplinkTxSwitching-DL-Interruption-r16;

-otherwise,

-symbol #4 if UE capability uplinkTxSwitchingPeriod is 210 us or

-symbol #5 if UE capability uplinkTxSwitchingPeriod is 140 us or

-symbol #8 if UE capability uplinkTxSwitchingPeriod is 35 us.

For NR TDD Cell 2 and NR TDD Cell 3, aperiodic CSI-RS for L1-RSRP reporting is configured with power boosting 6 dB on the following symbol on the 2nd special slot of every even radio frame:

-symbol#10 if UE does not report uplinkTxSwitching-DL-Interruption-r16;

-otherwise,

-symbol #4 if UE capability uplinkTxSwitchingPeriod is 210 us or

-symbol #5 if UE capability uplinkTxSwitchingPeriod is 140 us or

-symbol #8 if UE capability uplinkTxSwitchingPeriod is 35 us.

This test verifies that the UE correctly report the L1-RSRP reporting. The test case is only applicable to UE which supports simultaneousRxTxInterBandCA.

The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, uplinkTxSwitching is indicated to UE.

Table A.6.5.7B.2.1-1: Supported test configurations

Table A.6.5.7B.2.1-2: General test parameters for DL interruptions at switching between two uplink bands in TDD-TDD CA

Table A.6.5.7B.2.1-3: Cell specific test parameters for DL interruptions at switching between two uplink bands in TDD-TDD CA

## A.6.5.7B.2.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.2.2.2.10B.

UE shall send L1-RSRP report while meeting the accuracy requirements defined in clause 10.1.19.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.7CDL interruptions at switching between two uplink bands with two transmit antenna connectors

## A.6.5.7C.1DL interruptions at switching between two uplink bands with two transmit antenna connectors in FDD-TDD CA

## A.6.5.7C.1.1Test Purpose and Environment

The purpose of this test is to verify DL interruption requirements during UE dynamic switching between two uplink bands with two transmit antenna connectors defined in clause 8.2.2.2.10C. The test case is applicable for an uplink band pair of an inter-band FDD-TDD CA configuration when the capability uplinkTxSwitchingPeriod2T2T is present, where NR UL carrier 1 in band A is capable of two transmit antenna connector, NR UL carrier 2 and carrier 3 in band B are capable of two transmit antenna connectors. NR UL carrier 2 and carrier 3 are two contiguous aggregated carriers, and band A and band B are different bands with different carrier frequencies.

There are three cells: FR1 FDD PCell (Cell 1), FR1 TDD SCell (Cell 2) and FR1 TDD SCell (Cell 3) where Cell 1 in band A is with 2Tx, cell2 and Cell 3 in band B with 2Tx, cell2 and cell3 are two contiguous aggregated carriers. The test parameters for the three cells are given in table A.6.5.7C.1.1-1, table A.6.5.7C.1.1-2 and table A.6.5.7C.1.1-3 below.

For NR FDD carrier (Cell 1), aperiodic CSI-RS for L1-RSRP reporting is triggered with power boosting 6dB on the following symbol in the slot overlapping with the 1st special slot of every radio frame of the NR TDD carrier (Cell 2) and NR TDD carrier (Cell 3):

-symbol#12 if UE does not report uplinkTxSwitching-DL-Interruption;

-otherwise,

-symbol #8 if UE capability uplinkTxSwitchingPeriod2T2T  is 210us or

-symbol #9 if UE capability uplinkTxSwitchingPeriod2T2T is 140us or

-symbol #10 if UE capability uplinkTxSwitchingPeriod2T2T is 35us.

For NR TDD carrier (Cell 2) and NR TDD carrier (Cell 3), aperiodic CSI-RS for L1-RSRP reporting is configured with power boosting 6dB on the following symbol in the 2nd special slot of every radio frame:

-symbol#9 if UE does not report [uplinkTxSwitching-DL-Interruption];

-otherwise,

-symbol #2 if UE capability uplinkTxSwitchingPeriod2T2T is 210us or

-symbol #3 if UE capability uplinkTxSwitchingPeriod2T2T is 140us or

-symbol #6 if UE capability uplinkTxSwitchingPeriod2T2T is 35us.

This test verifies that the UE correctly report the L1-RSRP reporting. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, uplinkTxSwitchingPeriod2T2T is indicated to UE.

Table A.6.5.7C.1.1-1: Supported test configurations

Table A.6.5.7C.1.1-2: General test parameters for DL interruptions at switching between two uplink bands with two transmit antenna connectors in FDD-TDD CA

Table A.6.5.7C.1.1-3: Cell specific test parameters for DL interruptions at switching between two uplink bands with two transmit antenna connectors in FDD-TDD CA

## A.6.5.7C.1.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.2.2.2.10C.

UE shall send L1-RSRP report while meeting the accuracy requirements defined in clause 10.1.19.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.7C.2DL interruptions at switching between two uplink bands with two transmit antenna connectors in TDD-TDD CA

## A.6.5.7C.2.1Test Purpose and Environment

The purpose of this test is to verify DL interruption requirements during UE dynamic switching between two uplink carriers defined in clause 8.2.2.2.10C. The test case is applicable for an uplink band pair of an inter-band TDD-TDD CA configuration when the capability uplinkTxSwitchingPeriod2T2T is present, , where NR UL carrier 1 in band A is capable of two transmit antenna connector, NR UL carrier 2 and carrier 3 in band B are capable of two transmit antenna connectors. NR UL carrier 2 and carrier 3 are two contiguous aggregated carriers, and band A and band B are different bands with different carrier frequencies.

There are three cells: FR1 TDD PCell (Cell 1), FR1 TDD SCell (Cell 2) and FR1 TDD SCell (Cell 3) where cell 1 in band A is with 2Tx, cell2 and cell 3 in band B with 2Tx, cell2 and cell3 are two contiguous aggregated carriers. The test parameters for the three cells are given in Table A.6.5.7C.2.1-1, Table A.6.5.7C.2.1-2 and Table A.6.5.7C.2.1-3 below.

For NR TDD PCell (Cell 1), aperiodic CSI-RS for L1-RSRP reporting is triggered with power boosting 6dB on the following symbol in the 1st special slot of every even radio frame:

-symbol#10 if UE does not report uplinkTxSwitching-DL-Interruption;

-otherwise,

-symbol #4 if UE capability uplinkTxSwitchingPeriod2T2T is 210us or

-symbol #5 if UE capability uplinkTxSwitchingPeriod2T2T is 140us or

-symbol #8 if UE capability uplinkTxSwitchingPeriod2T2T is 35us.

For NR TDD SCell (Cell 2) and NR TDD SCell (Cell 3), aperiodic CSI-RS for L1-RSRP reporting is configured with power boosting 6dB on the following symbol on the 2nd special slot of every even radio frame:

-symbol#10 if UE does not report uplinkTxSwitching-DL-Interruption;

-otherwise,

-symbol #4 if UE capability uplinkTxSwitchingPeriod2T2T is 210us or

-symbol #5 if UE capability uplinkTxSwitchingPeriod2T2T is 140us or

-symbol #8 if UE capability uplinkTxSwitchingPeriod2T2T is 35us.

This test verifies that the UE correctly report the L1-RSRP reporting. The test case is only applicable to UE which supports simultaneousRxTxInterBandCA.

The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, uplinkTxSwitchingPeriod2T2T is indicated to UE.

Table A.6.5.7C.2.1-1: Supported test configurations

Table A.6.5.7C.2.1-2: General test parameters for DL interruptions at switching between two uplink bands with two transmit antenna connectors in TDD-TDD CA

Table A.6.5.7C.2.1-3: Cell specific test parameters for DL interruptions at switching between two uplink bands with two transmit antenna connectors in TDD-TDD CA

## A.6.5.7C.2.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.2.2.2.10C.

UE shall send L1-RSRP report while meeting the accuracy requirements defined in clause 10.1.19.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.7DDL interruptions at UE switching across three or four uplink bands

## A.6.5.7D.1DL interruptions at switching across three uplink bands in TDD-TDD CA for single TAG

## A.6.5.7D.1.1Test Purpose and Environment

The purpose of this test is to verify DL interruption requirements during UE dynamic switching across three uplink bands for single TAG defined in clause 8.2.2.2.10D. The test case is applicable for an inter-band TDD-TDD CA configuration when the capability BandCombination-UplinkTxSwitch-v1800 is present, where NR UL carrier 1 in band A is capable of one transmit antenna connector, NR UL carrier 2 in band B is capable of one transmit antenna connector and NR UL carrier 3 in band C is capable of two transmit antenna connectors. NR UL carrier 1, carrier 2 and carrier 3 in band A, band B and band C, respectively, are different bands with different carrier frequencies. All cells belong to the same TAG.

There are three cells: FR1 TDD PCell (Cell 1), FR1 TDD SCell (Cell 2) and FR1 TDD SCell (Cell 3) where Cell 1 with 1TX is on band A, Cell 2 with 1TX is on band B, and Cell 3 with 2TX is on band C. The test parameters for the three cells are given in table A.6.5.7D.1.1-1, table A.6.5.7D.1.1-2 and table A.6.5.7D.1.1-3 below. TX switching is from band A and band B to band C.

For NR TDD PCell (Cell 1) and NR TDD SCell (Cell 2), aperiodic CSI-RS for L1-RSRP reporting is triggered with power boosting 6 dB on the following symbol in the 1 st special slot of every even radio frame:

-symbol#10 if UE does not report uplinkTxSwitching-DL-Interruption-r18;

-otherwise,

-symbol #4 if UE capability uplink Tx switching period is 210 s or

-symbol #5 if UE capability uplink Tx switching period is 140 s or

-symbol #8 if UE capability uplink Tx switching period is 35 s.

For NR TDD SCell (Cell 3), aperiodic CSI-RS for L1-RSRP reporting is configured with power boosting 6dB on the following symbol on the 2nd special slot of every even radio frame:

-symbol#10 if UE does not report uplinkTxSwitching-DL-Interruption-r18;

-otherwise,

-symbol #4 if UE capability uplink Tx switching period is 210 s  or

-symbol #5 if UE capability uplink Tx switching period is 140 s  or

-symbol #8 if UE capability uplink Tx switching period is 35 s .

This test verifies that the UE correctly report the L1-RSRP reporting. The test case is only applicable to UE which supports simultaneousRxTxInterBandCA.

The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, UplinkTxSwitchingMoreBands-r18 is indicated to UE.

Table A.6.5.7D.1.1-1: Supported test configurations

Table A.6.5.7D.1.1-2: General test parameters for DL interruptions at switching across three uplink bands in TDD-TDD CA

Table A.6.5.7D.1.1-3: Cell specific test parameters for DL interruptions at switching across three uplink bands in TDD-TDD CA

## A.6.5.7D.1.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.2.2.2.10D.

UE shall send L1-RSRP report while meeting the accuracy requirements defined in clause 10.1.19.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.7D.2DL interruptions at switching across four uplink bands in FDD-TDD CA for single TAG

## A.6.5.7D.2.1Test Purpose and Environment

The purpose of this test is to verify DL interruption requirements during UE dynamic switching across four uplink bands for single TAG defined in clause 8.2.2.2.10D. The test case is applicable an NR inter-band CA configuration when the capability BandCombination-UplinkTxSwitch-v1800 is present, where NR UL carrier 1 in band A, NR UL carrier 2 in band B, NR UL carrier 3 in band C and NR UL carrier 4 in band D are capable of one transmit antenna connector respectively. All cells belong to the same TAG.

There are four cells: FR1 FDD PCell (Cell 1), FR1 FDD SCell (Cell 2), FR1 TDD SCell (Cell 3) and FR1 TDD SCell (Cell 4) where Cell 1 in band A is with 1TX, Cell 2 in band B is with 1TX, Cell 3 in band C is with 1TX and Cell 4 in band D is with 1TX. The test parameters for the four cells are given in table A.6.5.7D.2.1-1, table A.6.5.7D.2.1-2 and table A.6.5.7D.2.1-3 below. TX switching is from band A and band B to band C and band D.

For NR FDD carrier Cell 1 and NR FDD carrier Cell2, aperiodic CSI-RS for L1-RSRP reporting is triggered with power boosting 6 dB on the following symbol in the slot overlapping with the 1 st special slot of every radio frame of the NR TDD carrier (Cell 3):

-symbol#12 if UE does not report uplinkTxSwitching-DL-Interruption-r18;

-otherwise,

-symbol #8 if UE indicated uplink Tx switching period is 210 s or

-symbol #9 if UE indicated uplink Tx switching period is 140 s or

-symbol #10 if UE indicated uplink Tx switching period is 35 s.

For NR TDD Cell 3 and NR TDD Cell 4, aperiodic CSI-RS for L1-RSRP reporting is configured with power boosting 6 dB on the following symbol in the 2nd special slot of every radio frame:

-symbol#9 if UE does not report uplinkTxSwitching-DL-Interruption-r18;

-otherwise,

-symbol #2 if UE indicated uplink Tx switching period is 210 s or

-symbol #3 if UE indicated uplink Tx switching period is 140 s or

-symbol #6 if UE indicated uplink Tx switching period is 35 s.

This test verifies that the UE correctly report the L1-RSRP reporting. The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, UplinkTxSwitchingMoreBands-r18 is indicated to UE.

Table A.6.5.7D.2.1-1: Supported test configurations

Table A.6.5.7D.2.1-2: General test parameters for DL interruptions at switching across four uplink bands in FDD-TDD CA

Table A.6.5.7D.2.1-3: Cell specific test parameters for DL interruptions at switching across four uplink bands in FDD-TDD CA

## A.6.5.7D.2.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.2.2.2.10D.

UE shall send L1-RSRP report while meeting the accuracy requirements defined in clause 10.1.19.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.7D.3DL interruptions at switching across three uplink bands in FDD-TDD CA for two TAGs

## A.6.5.7D.3.1Test Purpose and Environment

The purpose of this test is to verify DL interruption requirements during UE dynamic switching across 3 bands with one or two transmit antenna connectors defined in clause 8.2.2.2.10D for two TAGs. The test case is applicable for an NR inter-band CA configuration when the capability BandCombination-UplinkTxSwitch-v1800 is present, where in NR inter-band CA configuration, the number of NR uplink bands with different carrier frequencies is three. NR UL carrier(s) in each of the three uplink bands are capable of one or two transmit antenna connector(s), according to the UE capability. Cell 1 and Cell 2 belong to one TAG, and Cell 3 belongs to the other TAG.

There are three cells: FR1 FDD PCell (Cell 1), FR1 FDD SCell (Cell 2) and FR1 TDD SCell (Cell 3) where Cell 1 with 1TX is on band A, Cell 2 with 1TX is on band B, and Cell 3 with 2TX is on band C. The test parameters for the three cells are given in table A.6.5.7D.3.1-1, table A.6.5.7D.3.1-2 and table A.6.5.7D.3.1-3 below. TX switching is from band A and band B to band C.

For NR FDD carrier Cell 1 and NR FDD carrier Cell2, aperiodic CSI-RS for L1-RSRP reporting is triggered with power boosting 6 dB on the following symbol in slot overlapping with the 1 st special slot of every radio frame of the NR TDD carrier (Cell 3):

-symbol#12 if UE does not report uplinkTxSwitching-DL-Interruption-r18;

-otherwise,

-symbol #8 if UE indicated uplink Tx switching period is 210 s  or

-symbol #9 if UE indicated uplink Tx switching period is 140 s  or

-symbol #10 indicated uplink Tx switching period is 35 s .

For NR TDD carrier (Cell 3), aperiodic CSI-RS for L1-RSRP reporting is configured with power boosting 6 dB on the following symbol in the 2nd special slot of every radio frame:

-symbol#9 if UE does not report uplinkTxSwitching-DL-Interruption-r18;

-otherwise,

-symbol #1 if UE indicated uplink Tx switching period is 210 s or

-symbol #3 if UE indicated uplink Tx switching period is 140 s or

-symbol #6 if UE indicated uplink Tx switching period is 35 s.

This test verifies that the UE correctly report the L1-RSRP reporting. The test case is only applicable to UE which supports simultaneousRxTxInterBandCA.

The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, UplinkTxSwitchingMoreBands-r18 is indicated to UE.

Table A.6.5.7D.3.1-1: Supported test configurations

Table A.6.5.7D.3.1-2: General test parameters for DL interruptions at switching across 3 bands with one or two transmit antenna connectors in FDD-TDD CA

Table A.6.5.7D.3.1-3: Cell specific test parameters for DL interruptions at switching across 3 bands with one or two transmit antenna connectors in FDD-TDD CA

## A.6.5.7D.3.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.2.2.2.10D for two TAGs case and provided in table 8.2.2.2.10D-2.

UE shall send L1-RSRP report while meeting the accuracy requirements defined in clause 10.1.19.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.7D.4DL interruptions at switching across four uplink bands in TDD-TDD CA for two TAGs

## A.6.5.7D.4.1Test Purpose and Environment

The purpose of this test is to verify DL interruption requirements during UE dynamic across four bands with one or two transmit antenna connectors defined in clause 8.2.2.2.10D for two TAGs. The test cases are applicable for an NR inter-band CA configuration when the capability BandCombination-UplinkTxSwitch-v1800 is present, where in NR inter-band CA configuration, the number of NR uplink bands with different carrier frequencies is four. NR UL carrier(s) in each of the four uplink bands are capable of one transmit antenna connector(s), according to the UE capability. Cell 1 and Cell 2 belong to one TAG, and Cell 3 and Cell 4 belong to the other TAG.

There are four cells: FR1 TDD PCell (Cell 1), FR1 TDD SCell (Cell 2), FR1 TDD SCell (Cell 3) and FR1 TDD SCell (Cell 4) where Cell 1 in band A is with 1TX, Cell 2 in band B is with 1TX, Cell 3 in band C is with 1TX and Cell 4 in band D is with 1TX. The test parameters for the four cells are given in table A.6.5.7D.4.1-1, table A.6.5.7D.4.1-2 and table A.6.5.7D.4.1-3 below. TX switching is from band A and band B to band C and band D.

For NR TDD PCell (Cell 1) and NR TDD SCell (Cell 2), aperiodic CSI-RS for L1-RSRP reporting is triggered with power boosting 6 dB on the following symbol in the 1 st special slot of every even radio frame:

-symbol#10 if UE does not report uplinkTxSwitching-DL-Interruption-r18;

-otherwise,

-symbol #3 if UE capability uplink Tx switching period is 210 s  or

-symbol #5 if UE capability uplink Tx switching period is 140 s  or

-symbol #8 if UE capability uplink Tx switching period is 35 s .

For NR TDD SCell (Cell 3) and NR TDD SCell (Cell 4), aperiodic CSI-RS for L1-RSRP reporting is configured with power boosting 6dB on the following symbol on the 2nd special slot of every even radio frame:

-symbol#10 if UE does not report uplinkTxSwitching-DL-Interruption-r18;

-otherwise,

-symbol #3 if UE capability uplink Tx switching period is 210 s  or

-symbol #5 if UE capability uplink Tx switching period is 140 s  or

-symbol #8 if UE capability uplink Tx switching period is 35 s .

This test verifies that the UE correctly report the L1-RSRP reporting. The test case is only applicable to UE which supports simultaneousRxTxInterBandCA.

The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, UplinkTxSwitchingMoreBands-r18 is indicated to UE.

Table A.6.5.7D.4.1-1: Supported test configurations

Table A.6.5.7D.4.1-2: General test parameters for DL interruptions at switching across 4 bands with one or two transmit antenna connectors in TDD-TDD CA

Table A.6.5.7D.7.1-3: Cell specific test parameters for DL interruptions at switching across 4 bands with one or two transmit antenna connectors in TDD-TDD CA

## A.6.5.7D.7.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.2.2.2.10D for two TAGs case and provided in table 8.2.2.2.10D-2.

UE shall send L1-RSRP report while meeting the accuracy requirements defined in clause 10.1.19.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.8UE specific CBW change

## A.6.5.8.1UE specific CBW change on PCell in FR1 in non-DRX

## A.6.5.8.1.1Test Purpose and Environment

The purpose of this test is to verify the UE specific CBW change delay requirement defined in clause 8.13.

The supported test configurations are shown in table A.6.5.8.1.1-1. The test scenario comprises of one Cell (Cell 1), which is PCell as given in table A.6.5.8.1.1-2. Cell-specific parameters are specified in table A.6.5.8.1.1-3.

PDCCHs indicating new transmissions shall be sent continuously on Cell 1 to ensure that the UE sends ACK/NACK during the test.

Before the test starts:

-UE is connected to Cell 1 (PCell) on radio channel 1.

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1 (PCell).

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PCell.

-UE has been configured with UE specific CBW (CBW-1).

-UE is indicated in SCS-SpecificCarrier [2] that the UE specific CBW is CBW-1 as the initial condition in Cell 1 (PCell).

Cell 1 (PCell) has constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration containing SCS-SpecificCarrier with updated UE specific CBW, sent from the test equipment to the UE, is completely received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its UE specific CBW with the updated CBW-2 for the final condition.

The UE shall be able to receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot as defined in clause 8.13 and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot on the PCell’s BWP-1 on CBW-2 for the final condition. The UE shall be continuously scheduled on the PCell’s BWP-1 on CBW-2  for the final condition starting from the first DL slot right after slot . i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length+k1i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length

and  are defined in clause 8.13.TRRCprocessingDelayTCBWchangeDelayRRC

The test equipment verifies the UE specific CBW switching delay in PCell by estimating the time from the moment the RRC Reconfiguration message including updated UE specific CBW configuration is sent until the moment a vaild ACK/NACK is received.

Table A.6.5.8.1.1-1: Supported test configurations for UE specific CBW change in SA scenario

Table A.6.5.8.1.1-2: General test parameters for UE specific CBW change in SA scenario

Table A.6.5.8.1.1-3: NR Cell specific test parameters for UE specific CBW change in SA scenario

## A.6.5.8.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the PCell from the first DL slot that occurs right after the begining of slot  and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot.i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in TS 38.321 [7].

All of the above test requirements shall be fulfilled in order for the observed UE specific CBW change delay on the PCell to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.9Pathloss reference signal switching delay

## A.6.5.9.1MAC-CE based pathloss reference signal switch delay

## A.6.5.9.1.1Test Purpose and Environment

The purpose of this test is to verify the MAC-CE based pathloss reference signal switch delay requirement defined in clause 8.14.

The supported test configurations are shown in table A.6.5.9.1.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.6.5.9.1.1-2. Cell-specific parameters of the cell are specified in table A.6.5.9.1.1-3 below.

The test consists of 3 successive time periods, with duration of T1, T2 and T3, respectively.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 on radio channel 1.

-UE shall be fully synchronized to SSB #0.

During T1,

-The UE shall track SSB #1 so that SSB #1 as a pathloss reference signal is known to the UE.

Time period T2 starts when the UE is configured of the power headroom reporting functionality by upper layers by the test equipment and the UE shall transmit a PHR during T2.

During T2,

-UE is configured with a phr-ProhibitTimer timer value for Cell 1.

-UE is configured with a phr-Tx-PowerFactorChange value for Cell 1.

During T3,

Time period T3 starts when a PDSCH carrying MAC-CE activation for pathloss reference signal switch, sent from the test equipment to the UE to swicth the pathloss reference signal from SSB 0 to SSB 1, is received at the UE side in Cell 1’s slot # denoted i. The UE shall switch its pathloss reference signal to the target one and send PHR.

The UE shall be able to apply the target pathloss reference signal of the serving cell on which pathloss reference signal switch occurs no later than the slot i + +  as defined in clause 8.14.  The UE shall be able to apply old pathloss reference signals until the slot i + +  as defined in clause 8.14.THARQ3 ms + 5*Ttarget_PL-RS + 2 msNR slot lengthTHARQ3Nslotsubframe,µ

The test equipment verifies the pathloss RS switch time by counting the slots from the time when the pathloss RS switch command is transmitted till a PHR is received during T3.

Table A.6.5.9.1.1-1: MAC-CE based pathloss reference signal switch supported test configurations

Table A.6.5.9.1.1-2: General test parameters for MAC-CE based pathloss reference signal switch in SA

Table A.6.5.9.1.1-3: NR Cell specific test parameters for MAC-CE based pathloss reference signal switch in SA

## A.6.5.9.1.2Test Requirements

During T3, the UE shall start to send the PHR for PCell no later than the slot i + + .THARQ3 ms + 5*Ttarget_PL-RS + 2 msNR slot length

During T3, the UE shall start to send the PHR for PCell no earlier than the slot i + + .THARQ3Nslotsubframe,µ

Where,  is the timing between pathloss reference MAC-CE activation command and acknowledgement as specified in TS 38.321 [7],  is the periodicity of the target pathloss reference signal which is SSB in this test.THARQTtarget_PL-RS

During T3, UE shall send L1-RSRP report with measurement results for both SSB0 and SSB1.

All of the above test requirements shall be fulfilled in order for the observed pathloss RS switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The UE shall be given proper uplink transmission grant during T2 and T3.

## A.6.5.9.2MAC-CE based pathloss reference signal switch delay  for LB CA

## A.6.5.9.2.1Test Purpose and Environment

The purpose of this test is to verify the MAC-CE based pathloss reference signal switch delay requirement defined in clause 8.14 for the UE supporting featureSetCombinationLowBandSwitching-r19 and switchingPeriodForFDD-SDL-r19 is configured with switchingPattern-r19. The test verifies pathloss reference signal switch delay in PCell when PCell reference signals are partially overlapped with PCell active periods according to the switching pattern.

The supported test configurations are shown in table A.6.5.9.1.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.6.5.9.1.1-2. Cell-specific parameters of the cell are specified in table A.6.5.9.1.1-3, except for the parameters specific for this test case, which are defined in table A.6.5.9.2.1-1.

Table A.6.5.9.2.1-1: General test parameters for known pathloss reference signal switch case in PCell for LBCA

The test consists of 3 successive time periods, with duration of T1, T2 and T3, respectively.

Prior to the start of the time duration T1,

-UE is connected to Cell 1 on radio channel 1.

-UE shall be fully synchronized to SSB #0.

During T1,

-The UE shall track SSB #1 so that SSB #1 as a pathloss reference signal is known to the UE.

Time period T2 starts when the UE is configured of the power headroom reporting functionality by upper layers by the test equipment and the UE shall transmit a PHR during T2.

During T2,

-UE is configured with a phr-ProhibitTimer timer value for Cell 1.

-UE is configured with a phr-Tx-PowerFactorChange value for Cell 1.

During T3,

Time period T3 starts when a PDSCH carrying MAC-CE activation for pathloss reference signal switch, sent from the test equipment to the UE to swicth the pathloss reference signal from SSB 0 to SSB 1, is received at the UE side in Cell 1’s slot # denoted i. The UE shall switch its pathloss reference signal to the target one and send PHR.

The UE shall be able to apply the target pathloss reference signal of the serving cell on which pathloss reference signal switch occurs no later than the slot i + +  as defined in clause 8.14.  The UE shall be able to apply old pathloss reference signals until the slot i + +  as defined in clause 8.14.THARQ3 ms + 5*Kp*Ttarget_PL-RS + 2 msNR slot lengthTHARQ3Nslotsubframe,µ

The test equipment verifies the pathloss RS switch time by counting the slots from the time when the pathloss RS switch command is transmitted till a PHR is received during T3.

## A.6.5.9.2.2Test Requirements

During T3, the UE shall start to send the PHR for PCell no later than the slot i + + .THARQ3 ms + 5*Kp*Ttarget_PL-RS + 2 msNR slot length

During T3, the UE shall start to send the PHR for PCell no earlier than the slot i + + .THARQ3Nslotsubframe,µ

Where,  is the timing between pathloss reference MAC-CE activation command and acknowledgement as specified in TS 38.321 [7],  is the periodicity of the target pathloss reference signal which is SSB in this test. Kp is the scaling factor for the pathloss reference signal of PCell to be measured for LB_CA via switching.THARQTtarget_PL-RS

During T3, UE shall send L1-RSRP report with measurement results for both SSB0 and SSB1.

All of the above test requirements shall be fulfilled in order for the observed pathloss RS switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The UE shall be given proper uplink transmission grant during T2 and T3.

## A.6.5.10Conditional PSCell addition and release delay (FR1 NR-DC)

## A.6.5.10.1Conditional PSCell Addition and Release Delay

## A.6.5.10.1.1Test purpose and environment

The purpose of this test is to verify that the NR conditional PSCell addition and release delay under NR-DC is within the requirements stated in clause 8.9A.2.

## A.6.5.10.1.2Test Parameters

Supported test configurations are shown in clause A.6.5.10.1.2-1. The test scenario comprises two NR cells, Cell 1 and Cell 2, on radio channel 1 in FR1 and radio channel 2 in FR1, respectively. Test parameters are given in Tables A.6.5.10.1.2-2 below.

The test parameters for NR cell are given in Tables A.6.5.10.1.2-2 and cell-specific parameters in table A.6.5.10.1.2-3 below. The test consists of four successive time periods with duration of T1, T2, T3 and T4 respectively. There are two carriers each with one cell. Before the test starts the UE is connected to Cell 1 (NR PCell) on radio channel 1 (PCC) but is not aware of Cell 2 (NR PSCell) on radio channel 2. The UE is only monitoring the PCC. During T1 only Cell1 is known to the UE.

At the start of time duration T1, the UE does not have any timing information of Cell 2. The network shall configure a condition and the target PSCell configuration implying addition to Cell 2 during T1, at a time earlier than TRRC_delay before the beginning of T2.

At the start of T2, Cell 2 becomes detectable and meets the addition condition. UE shall be able to measure and detect that the condition is fulfilled during time Tmeasure. After which it will transmit the PRACH preamble. Reception by the test system of the PRACH preamble defines the start of T3.

During T3, the UE shall send periodic CSI reports in PSCell. After having received at least one such report, the test system shall send an RRC message instructing the UE to release the PSCell. Reception by the UE of the RRC message defines the start of T4.

During T4, the UE shall release the PSCell.

Table A.6.5.10.1.2-1: Supported test configurations for FR1 PSCell

Table A.6.5.10.1.2-2: General Test Parameters for Conditional PSCell Addition and Release

Table A.6.5.10.1.2-3: Cell Specific Parameters for Conditional PSCell Addition and Release

## A.6.5.10.1.3Test Requirements

TRRC_delay + TEvent_DU occurs during T1 as the addition condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms = 920+10+20+20+20+2 ms=992 ms from the start of T2.

The UE shall transmit at least one periodic CSI report for PSCell during T3.

The UE shall stop transmitting CSI reports for PSCell at latest 20 ms into T4.

All of the above test requirements shall be fulfilled in order for the observed conditional PSCell addition and release delay to be counted as correct. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.11PSCell addition and release delay

## A.6.5.11.1Addition and Release Delay of unknown NR FR1 PSCell

## A.6.5.11.1.1Test purpose and environment

The purpose of this test is to verify that the NR PSCell addition and release delay requirements under NR-DC defined in clauses 8.9.2 and 8.9.3 respectively, for the case where the PSCell is unknown to the UE at the time of addition.

The supported test configurations are shown in table A.6.5.11.1.1-1. The test scenario comprises two NR cells, Cell 1 and Cell 2, on radio channel 1 and radio channel 2 in FR1, respectively. Test parameters are given in Tables A.6.5.11.1.1-2 and A.6.5.11.1.1-3 below. The test consists of six successive time periods with duration of T1, T2, T3 and T4 respectively. Cell 1 is the NR PCell, Cell 2 is an NR neighbour cell. The Cell 1 once set up is not changed across time.

At the start of T1, the UE shall be connected to Cell 1 (PCell) on radio channel 1 (PCC) and shall only monitor PCC and hence be unaware of Cell 2 (PSCell-to-be) on radio channel 2. the UE does not have any timing information of Cell 2. At the end of T1, the test system shall send a RRC message instructing the UE to add PSCell (Cell 2), and further instructing the UE to report CSI periodically in the PSCell once it has been added. Reception by the UE of this RRC message defines the start of T2.

During T2, the UE shall identify PSCell (Cell 2) and carry out random access towards the PSCell (Cell 2). Reception by the test system of the PRACH preamble defines the start of T3.

During T3, the UE shall send periodic CSI reports in PSCell (Cell 2). After having received at least one such report, the test system shall send a RRC message instructing the UE to release the PSCell (Cell 2). Reception by the UE of the RRC message defines the start of T4.

During T4, the UE shall release the PSCell (Cell 2).

Table A.6.5.11.1.1-1: Supported test configurations for FR1 PSCell Addition and Release

Table A.6.5.11.1.1-2: General Test Parameters for FR1 PSCell Addition and Release

Table A.6.5.11.1.1-3: Cell Specific Parameters for FR1 PSCell Addition and Release

## A.6.5.11.1.2Test Requirements

The UE shall transmit the PRACH preamble to PSCell no later than 172 msNote1 from the start of T2.

The UE shall send at least one CSI report for PSCell with non-zero CQI index during T3.

The UE shall periodically send CSI reports for PSCell after the UE has sent first CQI report with non-zero CQI index during T3.

The UE shall stop sending CSI reports for PSCell no later than 20 ms from the start of T4.

All the above test requirements shall be fulfilled in order for the observed PSCell addition delay and PSCell release delay to be counted as correct. The rate of correct observed PSCell addition delay and PSCell release delay during repeated tests shall be at least 90 %.

Note1:The PSCell addition delay can be expressed as follows as specified in clause 8.9.2:

Tconfig_PSCell = TRRC_delay + Tprocessing + Tsearch + T∆ + TPSCell_ DU + 2 ms

Where:

TRRC_delay = 50 ms

Tprocessing = 20 ms

Tsearch = 60 ms

T∆ = 20 ms

TPSCell_ DU = 1*10+10 = 20 ms

## A.6.5.11.2Addition and Release Delay of unknown NR FR1 PSCell with less than 5 MHz

## A.6.5.11.2.1Test purpose and environment

The purpose of this test is to verify that the NR PSCell addition and release delay under NR-DC with a bandwidth of less than 5 MHz meets the requirements defined in Clauses 8.9.2 and 8.9.3, where the PSCell is unknown to the UE at the time of addition.

Supported test configurations are shown in Table A.6.5.11.2.1-1. The test scenario comprises two NR cells, Cell 1 and Cell 2, on radio channel 1 and radio channel 2 in FR1, respectively. Test parameters are given in Table A.6.5.11.1.1-2. The cell-specific parameters as specified in Table A.6.5.11.1.1-3 with config 1 apply except those specified in Table A.6.5.11.2.1-2.

The test procedure specified in A.6.5.11.1 applies to this test.

Table A.6.5.11.2.1-1: Supported test configurations for FR1 PSCell Addition and Release with less than 5 MHz

Table A.6.5.11.2.1-2: Cell Specific Parameters for FR1 PSCell Addition and Release with less than 5 MHz

## A.6.5.11.2.2Test Requirements

The UE shall transmit the PRACH preamble to PSCell no later than 212msNote1 with 12 PRB SSB bandwidth from the start of T2.

The UE shall send at least one CSI report for PSCell with non-zero CQI index during T3.

The UE shall periodically send CSI reports for PSCell after the UE has sent first CQI report with non-zero CQI index during T3.

The UE shall stop sending CSI reports for PSCell no later than 20 ms from the start of T4.

All the above test requirements shall be fulfilled in order for the observed PSCell addition delay and PSCell release delay to be counted as correct. The rate of correct observed PSCell addition delay and PSCell release delay during repeated tests shall be at least 90 %.

Note1:The PSCell addition delay can be expressed as follows as specified in clause 8.9.2:

Tconfig_PSCell = TRRC_delay + Tprocessing + Tsearch + T∆ + TPSCell_ DU + 2 ms with 12 PRB SSB bandwidth.

Where:

TRRC_delay = 50 ms

Tprocessing = 20 ms

Tsearch = 60 ms

T∆ = 60 ms

TPSCell_ DU = 1*10+10 = 20 ms

## A.6.5.12Subsequent conditional PSCell addition/change

## A.6.5.12.1Intra-frequency subsequent CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC

## A.6.5.12.1.1Test purpose and environment

The purpose of this test is to verify that the subsequent conditional NR PSCell change under NR-DC is within the requirements stated in clause 8.11E.2.

For UE supporting subsequent conditional PSCell addition/change, UE only needs to pass either intra-frequency CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC defined in clause A.6.5.12.1 or intra-frequency CPC from FR1-FR2 NR-DC to FR1-FR2 NR-DC defined in clause A.7.5.18.1.

For UE which can pass this test, test of conditional PSCell addition and release delay defined in clauseA.6.5.10 can be skipped.

## A.6.5.12.1.2Test Parameters

Supported test configurations are shown in table A.6.5.12.1.2-1. The test scenario comprises three NR cells, Cell 1, Cell 2 and Cell 3. Cell1 is on radio channel 1 in FR1. Cell 2 and 3 are on radio channel 2 in FR1. Test parameters are given in Tables A.6.5.12.1.2-2 and A.6.5.12.1.2-3 below.

The test consists of three successive time periods with duration of T1, T2, and T3 respectively. Before the test starts the UE is connected to Cell 1 (NR PCell) on radio channel 1 (PCC) but is not aware of Cell 2 (NR PSCell) on radio channel 2. The UE is only monitoring the PCC. During T1 only Cell 1 is known to the UE.

At the start of time duration T1, the UE does not have any timing information of Cell 2. The TE shall configure subsequent conditional PSCell addition/change with Cell 2 and Cell 3 as target PSCells during T1, at a time earlier than TRRC_delay before the beginning of T2.

At the start of T2, Cell 2 becomes detectable and meets the PSCell addition condition. UE shall be able to measure and detect that the condition is fulfilled, after which it will transmit the PRACH preamble to Cell 2. Upon PSCell addition complete (UE transmits SN RRCReconfigurationcomplete message), T3 starts.

At the start of T3, Cell 3 becomes detectable and meets the PSCell change condition. UE shall be able to measure and detect that the condition is fulfilled, after which it will transmit the PRACH preamble to Cell 3.

Table A.6.5.12.1.2-1: Supported test configurations for Intra-frequency CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC

Table A.6.5.12.1.2-2: General Test Parameters for Intra-frequency CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC

Table A.6.5.12.1.2-3: Cell Specific Parameters for Intra-frequency CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC

## A.6.5.12.1.3Test Requirements

TRRC_delay + TEvent_DU for PSCell addition (Cell 2) occurs during T1 as the addition condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms = 920+10+62 ms=992 ms from the start of T2.

The UE shall start to transmit the PRACH to Cell 3 less than TEvent_DU + Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms = 0+920+10+62 ms=992 ms from the start of T3.

All of the above test requirements shall be fulfilled in order for the observed conditional PSCell addition and release delay to be counted as correct. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.12.2Inter-frequency subsequent CPA from FR1-FR1 NR-DC to FR1-FR1 NR-DC

## A.6.5.12.2.1Test purpose and environment

The purpose of this test is to verify that the subsequent conditional NR PSCell addition under NR-DC is within the requirements stated in clause 8.9C.2.

For UE supporting subsequent conditional PSCell addition/change, UE only needs to pass either inter-frequency CPA from FR1-FR1 NR-DC to FR1-FR1 NR-DC defined in clause A.6.5.12.2 or inter-frequency CPA from FR1-FR2 NR-DC to FR1-FR2 NR-DC defined in clause A.7.5.18.2.

For UE which can pass this test, test of conditional PSCell addition and release delay defined in clause A.6.5.10 can be skipped.

## A.6.5.12.2.2Test Parameters

Supported test configurations are shown in table A.6.5.12.2.2-1. The test scenario comprises three NR cells, Cell 1, Cell 2 and Cell 3. Cell 1 is on radio channel 1 in FR1. Cell 2 is on radio channel 2 in FR1. Cell 3 is on radio channel 3 in FR1.

The test parameters for NR Cell 2 and Cell 3 are given in Tables A.6.5.12.2.2-2 and cell-specific parameters in table A.6.5.12.2.2-3 below.

The test consists of four successive time periods with duration of T1, T2, T3 and T4 respectively. Before the test starts the UE is connected to Cell 1 (NR PCell) on radio channel 1 (PCC) but is not aware of Cell 2 (NR PSCell) on radio channel 2. The UE is only monitoring the PCC. During T1 only Cell 1 is known to the UE.

At the start of time duration T1, the UE does not have any timing information of Cell 2. The TE shall configure subsequent conditional PSCell addition with Cell 2 and Cell 3 as target PSCells during T1, at a time earlier than TRRC_delay before the beginning of T2.

At the start of T2, Cell 2 becomes detectable and meets the PSCell addition condition. UE shall be able to measure and detect that the condition is fulfilled, after which it will transmit the PRACH preamble to Cell 2. Upon PSCell addition complete (UE transmits SN RRCReconfigurationcomplete message), T3 starts.

At the start of T3, the test system shall send a RRCRconfiguration message to the UE to release PSCell (Cell 2) on radio channel 2. Upon PSCell release complete (UE transmits SN RRCReconfigurationcomplete message), T4 starts.

At the start of T4, Cell 3 becomes detectable and meets the subsequent PSCell addition condition. UE shall be able to measure and detect that the condition is fulfilled during time Tmeasure, after which it will transmit the PRACH preamble to Cell 3.

Table A.6.5.12.2.2-1: Supported test configurations for Inter-frequency Subsequent CPA from FR1-FR1 NR-DC to FR1-FR1 NR-DC

Table A.6.5.12.2.2-2: General Test Parameters for Subsequent Conditional PSCell Addition and Release

Table A.6.5.12.2.2-3: Cell Specific Parameters for Subsequent Conditional PSCell Addition and Release

## A.6.5.12.2.3Test Requirements

TRRC_delay + TEvent_DU for PSCell addition (Cell 2) occurs during T1 as the addition condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms = 1040+10+62 ms=1112 ms from the start of T2.

The UE shall start to transmit the PRACH to Cell 3 less than TEvent_DU + Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms = 0+1040+10+62 ms=1112 ms from the start of T4.

All of the above test requirements shall be fulfilled in order for the observed conditional PSCell addition and release delay to be counted as correct. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.12.3Intra-frequency subsequent CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC with 12 PRB SSB bandwidth

## A.6.5.12.3.1Test purpose and environment

The purpose of this test is to verify that the subsequent conditional NR PSCell change with 12 PRB SSB bandwidth under NR-DC is within the requirements stated in clause 8.11E.2.

For UE supporting subsequent conditional PSCell addition/change, UE only needs to pass one of addition and release delay of PSCell with 12 PRB SSB bandwidth defined in clause A.6.5.11.2 and  intra-frequency subsequent CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC with 12 PRB SSB bandwidth defined in clause A.6.5.12.3 and inter-frequency subsequent CPA from FR1-FR1 NR-DC to FR1-FR1 NR-DC with 12 PRB SSB bandwidth defined in clause A.6.5.12.4 and handover with PSCell delay defined in clause A.6.3.1.19.

## A.6.5.12.3.2Test Parameters

Supported test configurations are shown in table A.6.5.12.3.2-1. The test scenario comprises three NR cells, Cell 1, Cell 2 and Cell 3. Cell1 is on radio channel 1 in FR1. Cell 2 and 3 are on radio channel 2 in FR1. General test parameters as specified in table A.6.5.12.1.2-2 with config 1 apply except those specified in table A.6.5.12.3.2-2. Cell specific test parameters as specified in table A.6.5.12.1.2-3 with config 1 apply except those specified in table A.6.5.12.3.2-3.

The test procedure specified in clause A.6.5.12.1.2 applies to this test. The Cell 3 is the target cell operating with 12 PRB SSB bandwidth.

Table A.6.5.12.3.2-1: Supported test configurations for Intra-frequency CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC

Table A.6.5.12.3.2-2: General Test Parameters for Intra-frequency CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC

Table A.6.5.12.3.2-3: Cell Specific Parameters for Intra-frequency CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC

## A.6.5.12.3.3Test Requirements

TRRC_delay + TEvent_DU for PSCell addition (Cell 2) occurs during T1 as the addition condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms = 920+10+102 ms=1032 ms from the start of T2.

The UE shall start to transmit the PRACH to Cell 3 less than TEvent_DU + Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms = 0+920+10+102 ms=1032 ms from the start of T3.

All of the above test requirements shall be fulfilled in order for the observed conditional PSCell addition and release delay to be counted as correct. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.12.4Inter-frequency subsequent CPA from FR1-FR1 NR-DC to FR1-FR1 NR-DC with 12 PRB SSB bandwidth

## A.6.5.12.4.1Test purpose and environment

The purpose of this test is to verify that the subsequent conditional NR PSCell addition with 12 PRB SSB bandwidth under NR-DC is within the requirements stated in clause 8.9C.2.

For UE supporting subsequent conditional PSCell addition/change, UE only needs to pass one of addition and release delay of PSCell with 12 PRB SSB bandwidth defined in clause A.6.5.11.2 and intra-frequency subsequent CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC with 12 PRB SSB bandwidth in clause A.6.5.12.3 and inter-frequency subsequent CPA from FR1-FR1 NR-DC to FR1-FR1 NR-DC with 12 PRB SSB bandwidth defined in clause A.6.5.12.4 and handover with PSCell delay defined in clause A.6.3.1.19.

## A.6.5.12.4.2Test Parameters

Supported test configurations are shown in table A.6.5.12.4.2-1. The test scenario comprises three NR cells, Cell 1, Cell 2 and Cell 3. Cell 1 is on radio channel 1 in FR1. Cell 2 is on radio channel 2 in FR1. Cell 3 is on radio channel 3 in FR1.

General test parameters as specified in table A.6.5.12.2.2-2 with config 1 apply except those specified in table A.6.5.12.4.2-2. Cell specific test parameters as specified in table A.6.5.12.2.2-3 with config 1 apply except those specified in table A.6.5.12.4.2-3.

The test procedure specified in clause A.6.5.12.2.2 applies to this test. The Cell 3 is the target cell operating with 12 PRB SSB bandwidth.

Table A.6.5.12.4.2-1: Supported test configurations for Inter-frequency Subsequent CPA from FR1-FR1 NR-DC to FR1-FR1 NR-DC

Table A.6.5.12.4.2-2: General Test Parameters for Subsequent Conditional PSCell Addition and Release

Table A.6.5.12.4.2-3: Cell Specific Parameters for Subsequent Conditional PSCell Addition and Release

## A.6.5.12.4.3Test Requirements

TRRC_delay + TEvent_DU for PSCell addition (Cell 2) occurs during T1 as the addition condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms = 1040+10+102 ms=1152 ms from the start of T2.

The UE shall start to transmit the PRACH to Cell 3 less than TEvent_DU + Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms = 0+1040+10+102 ms=1152 ms from the start of T4.

All of the above test requirements shall be fulfilled in order for the observed conditional PSCell addition and release delay to be counted as correct. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.6.5.13Active TCI state switch delay

## A.6.5.13.1MAC-CE based joint TCI state switch for mDCI with two TA when RTD is larger than CP

## A.6.5.13.1.1Test Purpose and Environment

The purpose of this test is to verify the active TCI state switch delay requirement defined in clause 8.22.3. Supported test configuration is shown in table A.6.5.13.1.1-1.

The test scenario comprises of one NR PCell (Cell 1) containing two TRPs (i.e., TRP 0 and TRP 1) belonging to two TAGs as given in table A.6.5.13.1.1-2. Cell-specific parameters of NR PCell are specified in table A.6.5.13.1.1-3 below.

PDCCHs associated with corsetPoolIndex 0 and 1 indicating new transmissions shall be sent continuously on PCell to ensure that the UE would have ACK/NACK sending on PUCCH associated with TRP 0.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is configured with 1 TCI stats associated with coresetPoolIndex 0 for PCell, PDCCH TCI state 0 (QCL’d to SSB0), in Cell 1 before starting the test. UE is configured with 2 TCI states associated with coresetPoolIndex 1 for PCell, PDCCH TCI state 0 (QCL’d to SSB2) and TCIstate 1 (QCL’d to SSB3),.

-UE is indicated in TCI state 0 as the active PDCCH TCI state for PDCCH associated with coresetPoolIndex 0, and UE is indicated in TCI state 0 as the active PDCCH TCI state for PDCCH associated with coresetPoolIndex 1.

-Target TCI state is not in the active TCI state list.

The test consists of two time periods, T1 and T2. During T1 only SSB0 and SSB2 are transmitted. At the beginning of T2, the SSB3 corresponding to TCI state 1 starts transmitting. The UE is configured to provide periodic L1-RSRP reports. In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB2 and SSB3, UE receives a MAC-CE command indicating a switch to TCI state 1 for PDCCH associated with coresetPoolIndex 1. tci-PresentInDCI is not configured in the PDSCH configuration, i.e. TCI state for the PDSCH is identical to the PDCCH TCI state.

The test equipment verifies that UE can be scheduled on PCell on TCI state 0 associated with coresetPoolIndex 1  till n+ THARQ +3 ms. The test equipment also verifies the TCI state switch time in PCell by scheduling the UE on TCI state 1 associated with coresetPoolIndex 1  after n+ THARQ +3 ms + (Tfirst-SSB + TSSB-proc).

Table A.6.5.13.1.1-1: Supported test configurations

Table A.6.5.13.1.1-2: General test parameters for TCI state switch

Table A.6.5.13.1.1-3: NR Cell specific test parameters for TCI state switch

## A.6.5.13.1.2Test Requirements

During T2, UE shall send L1-RSRP report with results for both SSB0 and SSB1.

After receiving MAC-CE command in slot n, UE shall be able to continue receive on TRP 0, and for TRP 1, UE shall:

-be able to continue to receive on TCI state 0 till   n+ THARQ +3 ms

-be able to start receiving on TCI state 1 after n+ THARQ +5 ms + Tfirst-SSB

The rate of correct events observed during repeated tests shall be at least 90 %.
