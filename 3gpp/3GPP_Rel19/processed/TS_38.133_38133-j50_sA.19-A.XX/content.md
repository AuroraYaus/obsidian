---
type: spec
aliases:
  - 38.133_38133-j50_sA.19-A.XX
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.19-A.XX/content.md"
---
# TS 38.133 38133-j50_sA.19-A.XX

## A.19NR standalone tests for ATG

## A.19.1RRC_IDLE state mobility

## A.19.1.1Cell reselection to FR1 intra-frequency NR case

## A.19.1.1.1Test Purpose and Environment

This test is to verify the requirement for the intra frequency NR cell reselection requirements for ATG specified in clause 4.2D.2.3.

## A.19.1.1.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells, supported test configurations are shown in table A.19.1.1.2-1. The test parameters from table A.6.1.1.1.2-2 and table A.6.1.1.1.2-3 are used except those described in the tables A.19.1.1.2-2 and A.19.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.1.1.2-1: Supported test configurations

Table A.19.1.1.2-2: General test parameters for intra frequency NR cell re-selection test case

Table A.19.1.1.2-3: Cell specific test parameters for intra frequency NR cell re-selection test case

## A.19.1.1.3Test Requirements

For UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Intra + TSI-NR, and to an already detected cell can be expressed as: Tevaluate, NR_ intra + TSI-NR,

Where:

Tdetect, NR_IntraSee Table 4.2D.2.3-1 in clause 4.2D.2.3

Tevaluate, NR_ intraSee Table 4.2D.2.3-1 in clause 4.2D.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB22 are scheduled with 20 ms period and 80 ms period, respectively.

For the cell re-selection delay to a newly detectable cell, Tdetect, NR_ intra + TSI-NR = 33.28 s, allow 34 s.

For the cell re-selection delay to an already detected cell in the test case, Tevaluate, NR_Intra + TSI-NR = 7.68 s, allow 8 s.

## A.19.1.2Cell reselection to FR1 inter-frequency NR case

## A.19.1.2.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for ATG specified in clause 4.2D.2.4.

## A.19.1.2.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.19.1.2.2-1, A.19.1.2.2-2 and A.19.1.2.2-3. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.1.2.2-1: Supported test configurations

Table A.19.1.2.2-2: General test parameters for FR1 inter frequency NR cell re-selection test case

Table A.19.1.2.2-3: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case

## A.19.1.2.3Test Requirements

For UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 34 s.

The cell reselection delay to an already detected cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on Cell 1, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 1.

The cell re-selection delay to an already detected cell shall be less than 8 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Inter + TSI-NR, and to an already detected cell can be expressed as: Tevaluate, NR_ intrer+ TSI-NR,

Where:

Tdetect, NR_InterSee Table 4.2D.2.4-1 in clause 4.2D.2.4

Tevaluate, NR_ interSee Table 4.2D.2.4-1 in clause 4.2D.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB22 are scheduled with 20 ms period and 80 ms period, respectively.

For the cell re-selection delay to a newly detectable cell, Tdetect, NR_ inter + TSI-NR = 33.28 s, allow 34 s.

For the cell re-selection delay to an already detected cell in the test case, Tevaluate, NR_Inter + TSI-NR = 7.68 s, allow 8 s.

## A.19.1.3Cell reselection to FR1 inter-frequency NR case for UE configured with hs-ATG-cellReselectionSet-r18

## A.19.1.3.1Test Purpose and Environment

This test is to verify the requirement for the inter frequency NR cell reselection requirements for ATG UE configured with hs-ATG-cellReselectionSet-r18 and for ATG UE supporting the feature for enhanced RRM requirements (Enhanced RRM requirements for measurements in IDLE and INACTIVE modes for ATG) specified in clause 4.2D.2.4.

## A.19.1.3.2Test Parameters

The test scenario comprises of 2 cells on 2 different NR carriers respectively as given in tables A.19.1.3.2-1, A.19.1.3.2-2 and A.19.1.3.2-3. The test consists of two successive time periods, with time duration of T1 and T2. Only Cell 1 is already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.1.3.2-1: Supported test configurations

Table A.19.1.3.2-2: General test parameters for FR1 inter frequency NR cell re-selection test case

Table A.19.1.3.2-3: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case

## A.19.1.3.3Test Requirements

For UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The cell reselection delay to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration update on Cell 2.

The cell re-selection delay to a newly detectable cell shall be less than 12 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a newly detectable cell can be expressed as: Tdetect, NR_Inter_enh + TSI-NR

Where:

Tdetect, NR_Inter_enhSee Table 4.2D.2.4-2 in clause 4.2D.2.4

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case provided that SIB1 and SIB22 are scheduled with 20 ms period and 80 ms period, respectively.

For the cell re-selection delay to a newly detectable cell, Tdetect, NR_ inter_enh + TSI-NR = 11.52 s, allow 12 s.

## A.19.2RRC_CONNECTED state mobility

## A.19.2.1Handover

## A.19.2.1.1Intra-frequency handover from FR1 to FR1; known target cell

## A19.2.1.1.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 intra frequency handover requirements for ATG specified in clause 6.1E.1.2.

## A.19.2.1.1.2Test Parameters

Supported test configurations are shown in table A.19.2.1.1.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.1.2-2 and table A.6.3.1.1.2-3 except those described in the table A.19.2.1.1.2-2 and A.19.2.1.1.2-3.

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2.

NR shall send a RRC message implying handover to Cell 2. The RRC message implying handover shall be sent to the UE during period T2, after the UE has reported Event A3. T3 is defined as the end of the last TTI containing the RRC message implying handover.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.1.1.2-1: Intra-frequency handover from FR1 to FR1 test configurations

Table A.19.2.1.1.2-2: General test parameters Intra-frequency handover from FR1 to FR1

Table A.19.2.1.1.2-3: Cell specific test parameters for NR FR1-FR1 Intra frequency handover test case

## A.19.2.1.2.3Test Requirements

For UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The UE shall start to transmit the PRACH to Cell 2 less than 72 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 62 ms in the test. Tinterrupt is defined in clause 6.1E.1.2.2.

## A.19.2.1.2Inter-frequency handover from FR1 to FR1; unknown target cell

## A.19.2.1.2.1Test Purpose and Environment

This test is to verify the requirement for the NR FR1-NR FR1 inter frequency handover requirements for ATG specified in clause 6.1E.1.2.

## A.19.2.1.2.2Test Parameters

Supported test configurations are shown in table A.19.2.1.2.2-1. Both handover delay and interruption length are tested by using the parameters in table A.6.3.1.3.2-2 and table A.6.3.1.3.2-3 except those described in the table A.19.2.1.2.2-2 and A.19.2.1.2.2-3.

The test scenario comprises of two carriers and one cell on each carrier. No gap patterns are configured in the test case. The test consists of two successive time periods, with time durations of T1, T2 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE receives a RRC handover command from the network. The start of T2 is the instant when the last TTI containing the RRC message implying handover is sent to the UE.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.1.2.2-1: Inter-frequency handover from FR1 to FR1 test configurations

Table A.19.2.1.2.2-2: General test parameters Inter-frequency handover from FR1 to FR1

Table A.19.2.1.2.2-3: Cell specific test parameters for NR FR1-FR1 Inter frequency handover test case

## A.19.2.1.2.3Test Requirements

For UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The UE shall start to transmit the PRACH to Cell 2 less than 132 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 10 ms and is specified in clause 12 in TS 38.331 [2].

Tinterrupt = 122 ms in the test. Tinterrupt is defined in clause 6.1E.1.2.2.

This gives a total of 132 ms.

## A.19.2.2Conditional Handover

## A.19.2.2.1Intra-frequency distance-based conditional Handover from FR1 to FR1

## A.19.2.2.1.1Test Purpose and Environment

This test is to verify the requirement for intra-frequency distance-based conditional handover from FR1 to FR1 for ATG specified in clause 6.1E.2.

## A.19.2.2.1.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in table A.19.2.2.1.2-1, and A.19.2.2.1.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure intra-frequency neighbour cell. The RRC message implying distance-based handover to Cell 2 with Event D1 shall be sent to UE, at a time earlier than TRRC (10 ms) before the beginning of T2.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and location condition event condEventD1-r17 is fulfilled.

The specific gNB reference location is emulated by test system.

Table A.19.2.2.1.2-1: Supported test configurations

Table A.19.2.2.1.2-2: General test parameters for Intra-frequency distance-based conditional handover from FR1 to FR1

Table A.19.2.2.1.2-3: Cell specific test parameters for Intra-frequency distance-based conditional handover from FR1 to FR1

## A.19.2.2.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 872 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay is defined in clause 6.1E.2, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

At start of T2,

distance to source cell reference location is   = 10057.8m, and D1-1 = 10000m(3000)2+(1200*1000/3600*15-(-4600))2

distance to target cell reference location is   = 9942.4m, and D1-2 = 10000m(3000)2+(1200*1000/3600*15-(14479))2

i.e. D1-1 and D1-2 conditions are fulfilled at start of T2 with >=50m location margin.

Tmeasure = max(600 + 200 ms, 0) = 800 ms;

Tinterrupt = 62 ms; TCHO_execution = 10 ms.

This gives a total of 800 ms + 62 ms + 10 ms = 872 ms.

## A.19.2.2.2Inter-frequency distance-based conditional Handover from FR1 to FR1

## A.19.2.2.2.1Test Purpose and Environment

This test is to verify the requirement for inter-frequency distance-based conditional handover from FR1 to FR1 for ATG specified in clause 6.1E.2.

## A.19.2.2.2.2Test Parameters

The test scenario comprises of 2 NR carrier and one cell on each carrier as given in table A.19.2.2.2.2-1, and A.19.2.2.2.2-2. Both handover delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure inter-frequency neighbour cell and Gap pattern ID gp0. The RRC message implying distance-based handover to Cell 2 with Event D1 shall be sent to UE, at a time earlier than TRRC (10 ms) before the beginning of T2.

Starting T2, Cell 2 becomes detectable and offset better than Cell 1 and after 9976 ms of T2, location condition event condEventD1-r17 is fulfilled.

The specific gNB reference location is emulated by test system.

Table A.19.2.2.2.2-1: Supported test configurations

Table A.19.2.2.2.2-2: General test parameters for Inter-frequency distance-based conditional handover from FR1 to FR1

Table A.19.2.2.2.2-3: Cell specific test parameters for Inter-frequency distance-based conditional handover from FR1 to FR1

## A.19.2.2.2.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 later than 9976 ms and less than 10048 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay is defined in clause 6.1E.2, can be expressed as:

DCHO = TRRC + TEvent_DU + Tmeasure + Tinterrupt + TCHO_execution

where:

RRC procedure delay TRRC = 10 ms and is specified in clause 12 in TS 38.331 [2].

TEvent_DU = start of T2

At 9976 ms after start of T2,

distance to source cell reference location is   = 10050.2m, and D1-1 = 10000m(3000)2+(1200*1000/3600*14.976-(-4600))2

distance to target cell reference location is   = 9949.08m, and D1-2 = 10000m(3000)2+(1200*1000/3600*14.976-(14479))2

i.e. D1-1 and D1-2 conditions are fulfilled at start of T2 with >=50m location margin.

Tmeasure = max(600 + 200 ms, 9976 ms) = 9976 ms;

Tinterrupt = 62 ms; TCHO_execution = 10 ms.

This gives a total of 9976 ms + 62 ms + 10 ms = 10048 ms.

## A.19.2.3RRC Connection Mobility Control

## A.19.2.3.1SA: RRC Re-establishment

## A.19.2.3.1.1Intra-frequency RRC Re-establishment in FR1 for ATG

## A.19.2.3.1.1.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR1 with known target cell is within the specified limits for ATG. These tests will verify the requirements in clause 6.2D.1.

The test configurations are given in table A.19.2.3.1.1.1-1, and the test parameters are given in table A.6.3.2.1.1.1-2 and table A.6.3.2.1.1.1-3, except those described in the table A.19.2.3.1.1.1-2. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.3.1.1.1-1: Supported test configurations for ATG

Table A.19.2.3.1.1.1-2: Modified test parameters for ATG for UE with omnidirectional antenna

## A.19.2.3.1.1.2 Test Requirements

For ATG UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The test requirements of this test case are the same as those defined in clause A.6.3.2.1.1.2.

## A.19.2.3.1.2Inter-frequency RRC Re-establishment in FR1 with unknown target cell without serving cell timing for ATG

## A.19.2.3.1.2.1Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR1 with unknown target cell and without serving cell timing are within the specified limits. These tests will verify the requirements in clause 6.2D.1.

The test parameters are given in table A.19.2.3.1.2.1-1, table A.19.2.3.1.2.1-2 and table A.19.2.3.1.2.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.3.1.2.1-1: Supported test configurations

Table A.19.2.3.1.2.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1

Table A.19.2.3.1.2.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1

## A.19.2.3.1.2.2Test Requirements

For UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell without serving cell timing shall be less than 3 s.

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

## A.19.2.3.2Random Access for ATG UE

A.19.2.3.2.14-step RA type contention based random access test in FR1 for NR standalone

## A.19.2.3.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2D.2.2 and clause 7.1D.2 in an AWGN with constant residual doppler model.

For this test one cell is used and configured as PCell in FR1. Supported test configurations are shown in table A.19.2.3.2.1.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.6.3.2.2.1.1-2, except those described in the Table A.19.2.3.2.1.1-2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.3.2.1.1-1: Supported test configurations for contention based random access test in FR1 for NR standalone

Table A.19.2.3.2.1.1-2: General test parameters for contention based random access test in FR1 for NR Standalone

## A.19.2.3.2.1.2Test Requirements

The test requirements defined in clause A.6.3.2.2.1.2 shall apply for ATG.

A.19.2.3.2.24-step RA type non-contention based random access test in FR1 for NR standalone

## A.19.2.3.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2D.2.2 and clause 7.1D.2 in an AWGN with constant residual doppler model.

For this test one cell is used and configured as PCell in FR1. Supported test configurations are shown in table A.19.2.3.2.2.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.6.3.2.2.2.1-2 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2), except those described in the Table A.19.2.3.2.2.1-2. Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.3.2.2.1-1: Supported test configurations for non-contention based random access test in FR1 for NR standalone

Table A.19.2.3.2.2.1-2: General test parameters for non-contention based random access test in FR1 for NR Standalone

## A.19.2.3.2.2.2Test Requirements

The test requirements defined in clause A.6.3.2.2.2.2 shall apply for ATG.

## A.19.2.3.2.32-step RA type contention based random access test in FR1 for NR standalone

## A.19.2.3.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the 2-step RA type random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2D.2.3 and clause 7.1D.2 in an AWGN with constant residual doppler model.

For this test one cell is used and configured as PCell in FR1. Supported test configurations are shown in table A.19.2.3.2.3.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.6.3.2.2.3.1-2, except those described in the Table A.19.2.3.2.3.1-2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.3.2.3.1-1: Supported test configurations for 2-step RA type contention based random access with successRAR test in FR1 for NR standalone

Table A.19.2.3.2.3.1-2: General test parameters for 2-step RA type contention based random access with successRAR test in FR1 for NR standalone

## A.19.2.3.2.3.2Test Requirements

The test requirements defined in clause A.6.3.2.2.3.2 shall apply for ATG.

## A.19.2.3.2.42-step RA type non-contention based test in FR1 for NR standalone

## A.19.2.3.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the MsgA PRACH, MsgA PUSCH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2D.2.3 and clause 7.1D.2 in an AWGN with constant residual doppler model.

For this test one cell is used and configured as PCell in FR1. Supported test configurations are shown in table A.19.2.3.2.4.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.6.3.2.2.4.1-2, except those described in the Table A.19.2.3.2.4.1-2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.2.3.2.4.1-1: Supported test configurations for non-contention based random access test in FR1 for NR standalone

Table A.19.2.3.2.4.1-2: General test parameters for non-contention based random access test in FR1 for NR Standalone

## A.19.2.3.2.4.2Test Requirements

The test requirements defined in clause A.6.3.2.2.4.2 shall apply for ATG.

A.19.2.3.3SA: RRC Connection Release with Redirection for ATG UE

A.19.2.3.3.1Redirection from NR in FR1 to NR in FR1

## A.19.2.3.3.1.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements specified in clause 6.2D.3.2.1.

## A.19.2.3.3.1.2Test Parameters

Supported test configurations are shown in table A.19.2.3.3.1.2-1. The time delay is tested by using the parameters in table A.6.3.2.3.1.2-2 and table A.6.3.2.3.1.2-3, except those described in the Table A.19.2.3.3.1.2-2 and table A.19.2.3.3.1.2-3.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2. Cell 1 and Cell 2 belong to different tracking areas.

Table A.19.2.3.3.1.2-1: Redirection from NR to NR test configurations

Table A.19.2.3.3.1.2-2: General test parameters for Redirection from NR to NR test case

Table A.19.2.3.3.1.2-3: Cell specific test parameters for Redirection from NR to NR test case

## A.19.2.3.3.1.3Test Requirements

For UEs that don’t support antennaArrayType-r18 and UEs that support antennaArrayType-18:

The UE shall start to transmit the PRACH to Cell 2 less than 2240 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_NR = TRRC_procedure_delay + Tidentify-NR + TSI-NR + TRACH,

where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR = 680 ms in the test.

TSI-NR = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH = 170 ms in the test.

## A.19.3Timing

## A.19.3.1UE transmit timing

## A.19.3.1.1ATG UE Transmit Timing Test for FR1

## A.19.3.1.1.1Test Purpose and environment

The purpose of this test is to verify that the UE can follow frame timing change of the connected gNodeb and that the UE initial transmit timing accuracy, maximum amount of timing change in one adjustment, minimum and maximum adjustment rate are within the specified limits. This test will verify the requirements in clause 7.1D.2.

Supported test configurations refer to Table A.6.4.1.1.1-1.

A single NR cell is used during the test. Table A.19.3.1.1.1-1 defines the parameters to be configured and strength of the transmitted signals. The transmit timing is verified by the UE transmitting SRS using the configuration SRSconfig.1 defined in table A.6.4.1.1.1-3.

Changed UE location with the mobility assumption of 1200km/h, the specific UE location should be emulated by test system and provided to UE by AT command or GNSS simulator.

The specific gNB reference location is emulated by test system.

Table A.19.3.1.1.1-1: Cell Specific Test Parameters for UL Transmit Timing test

## A.19.3.1.1.2Test requirements

The test sequence shall be carried out in RRC_CONNECTED for every test case.

Following will be the test sequence for this test

1) Setup NR PCell according to parameters given in table A.19.3.1.1.1-1.

2)After connection set up with the cell, the test equipment will verify that the timing of the NR cell is within (NTA + NTA_offset+) ×Tc ± Te_ATG of the first detected path of DL SSB.NTA,adjUE

a.The NTA offset value (in Tc units) is 25600

b.The Te_ATG values depend on the DL and UL SCS for which the test is being run and are given in table 7.1D.2-1

c.The  value is computed by the UE based on UE position and BS location.NTA,adjUE

3)The test system shall adjust the timing of the DL path by values given in table A.19.3.1.1.2-1

Table A.19.3.1.1.2-1: Adjustment Value for DL Timing

4)The test system shall verify that the adjustment step size and the adjustment rate shall be according to requirements specified in clause 7.1D.2 Table 7.1D.2.1-1 until the UE transmit timing offset is within (NTA + NTA_offset+) ×Tc ± Te_ATG respective to the first path (in time) of DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna.NTA,adjUE

5)The test system shall verify that the UE transmit timing offset stays within (NTA + NTA_offset+) ×Tc ± Te_ATG of the first path (in time) of DL SSB used by the UE to determine downlink timing is received from the reference cell at the UE antenna.NTA,adjUE

## A.19.3.2UE timer accuracy

## A.19.3.3Timing advance

## A.19.3.3.1SA FR1 timing advance adjustment accuracy

## A.19.3.3.1.1Test Purpose and Environment

The purpose of the test is to verify UE Timing Advance adjustment delay and accuracy requirement defined in clause 7.3D.

## A.19.3.3.1.2Test Parameters

Supported test configurations refer to table A.6.4.3.1.2-1. Both timing advance adjustment delay and accuracy are tested by using the parameters in table A.6.4.3.1.2-2, A.6.4.3.1.2-3 and A.6.4.3.1.2-4, except those defined in table A.19.3.3.1.2-1.

In all test cases, single cell is used. Each test consists of two successive time periods, with time duration of T1 and T2 respectively. In each time period, timing advance commands are sent to the UE and Sounding Reference Signals (SRS), as specified in table A.6.4.3.1.2-3, are sent from the UE and received by the test equipment. By measuring the reception of the SRS, the transmit timing, and hence the timing advance adjustment accuracy, can be measured.

During time period T1, the test equipment shall send one message with a Timing Advance Command MAC Control Element, as specified in clause 6.1.3.4 in TS 38.321 [7]. The Timing Advance Command value shall be set to 31, which according to clause 4.2 in TS 38.213 [3] results in zero adjustment of the Timing Advance. In this way, a reference value for the timing advance used by the UE is established.

During time period T2, the test equipment shall send a sequence of messages with Timing Advance Command MAC Control Elements, with Timing Advance Command value specified in table A.6.4.3.1.2-2. This value shall result in changes of the timing advance used by the UE, and the accuracy of the change shall then be measured, using the SRS sent from the UE.

As specified in clause 7.3D.2.1, the UE adjusts its uplink timing at slot n+k+2µ  for a timing advance command received in slot n. This delay must be taken into account when measuring the timing advance adjustment accuracy, via the SRS sent from the UE.∙Koffset

The UE Time Alignment Timer, described in clause 5.2 in TS 38.321 [7], shall be configured so that it does not expire in the duration of the test.

Changed UE location with the mobility assumption of 1200km/h, the specific UE location should be emulated by test system and provided to UE by AT command or GNSS simulator.

The specific gNB reference location is emulated by test system.

Table A.19.3.3.1.2-1 Cell specific test parameters for timing advance

## A.19.3.3.1.3Test Requirements

The UE shall apply the signalled Timing Advance value to the transmission timing at the designated activation time i.e. k+1+2µ  slots after the reception of the timing advance command, where k=5.∙Koffset

The Timing Advance adjustment accuracy shall be within the limits specified in clause 7.3D.2.2.

The rate of correct Timing Advance adjustments observed during repeated tests shall be at least 90 %.

## A.19.4Signalling characteristics

## A.19.4.1Radio link Monitoring

In the following clause, any uplink signal transmitted by the UE is used for detecting the In-/Out-of-Sync state of the UE. In terms of measurement, the uplink signal is verified on the basis of the UE output power:

For UE with multiple transmit antennas, transmit OFF power is measured as the mean power at each transmit connector.

-UE output power higher than Transmit OFF power -50 dBm (as defined in TS 38.101-1 [18]) means uplink signal

-UE output power equal to or less than Transmit OFF power -50 dBm (as defined in TS 38.101-1 [18]) means no uplink signal.

## A.19.4.1.1Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode

## A.19.4.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1D.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.19.4.1.1.1-1. The test parameters are given in tables A.19.4.1.1.1-2, A.19.4.1.1.1-3, and A.19.4.1.1.1-4 below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.19.4.1.1.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. The UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.1.1.1-1: Supported test configurations for FR1 PCell

Table A.19.4.1.1.1-2: General test parameters for FR1 out-of-sync testing in non-DRX mode

Table A.19.4.1.1.1-3: Cell specific test parameters for FR1 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode

Table A.19.4.1.1.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

Figure A.19.4.1.1.1-1: SNR variation for out-of-sync testing

## A.19.4.1.1.2Test Requirements

The UE behaviour in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.19.4.1.2Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode

## A.19.4.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR1 radio link monitoring requirements in clause 8.1D.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0, and purpose set to ‘rlf’. Supported test configurations are shown in table A.19.4.1.2.1-1. The test parameters are given in tables A.19.4.1.2.1-2, and A.19.4.1.2.1-3 below. There is one cell (Cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.19.4.1.2.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.1.2.1-1: Supported test configurations for FR1 PCell

Table A.19.4.1.2.1-2: General test parameters for FR1 in-sync testing in non-DRX mode

Table A.19.4.1.2.1-3: Cell specific test parameters for FR1 (Cell 1) for in-sync radio link monitoring tests in non-DRX mode

Table A.19.4.1.2.1-4: Void

Figure A.19.4.1.2.1-1: SNR variation for in-sync testing

## A.19.4.1.2.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.19.4.1.3Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode

## A.19.4.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used. This test will partly verify the FR1 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1D.

The test parameters are given in tables A.19.4.1.3.1-1, A.19.4.1.3.1-2, A.19.4.1.3.1-3, and A.19.4.1.3.1-3A below. There is one cell, Cell 1 which is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.19.4.1.3.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting of 5 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 is configured as the BFD-RS.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.1.3.1-1: Supported test configurations for FR1 PCell

Table A.19.4.1.3.1-2: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in non-DRX mode

Table A.19.4.1.3.1-3: Cell specific test parameters for FR1 for CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.19.4.1.3.1-3A: Measurement gap configuration for FR1 CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.19.4.1.3.1-4: Void

Figure A.19.4.1.3.1-1: SNR variation for CSI-RS out-of-sync testing

## A.19.4.1.3.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 no later than time point C (D1 ms after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.19.4.1.4Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode

## A.19.4.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used. This test will partly verify the FR1 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1D.

The test parameters are given in tables A.19.4.1.4.1-1, A.19.4.1.4.1-2, and A.19.4.1.4.1-3 below. There is one cell (Cell 1), which is the PCell in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.19.4.1.4.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled. In the test, SSB0 is configured as the BFD-RS.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.1.4.1-1: Supported test configurations for FR1 PCell

Table A.19.4.1.4.1-2: General test parameters for FR1 PCell for CSI-RS in-sync testing in non-DRX mode

Table A.19.4.1.4.1-3: Cell specific test parameters for FR1 for CSI-RS in-sync radio link monitoring in non-DRX mode

Table A.19.4.1.4.1-4: Void

Figure A.19.4.1.4.1-1: SNR variation for CSI-RS in-sync testing

## A.19.4.1.4.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (T6 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.19.4.2Beam Failure Detection and Link recovery procedures

## A.19.4.2.1Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode

## A.19.4.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5D.

The test parameters are given in tables A.19.4.2.1.1-1, A.19.4.2.1.1-2, A.19.4.2.1.1-3 and A.19.4.2.1.1-4 below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.19.4.2.1.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.19.4.2.1.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.2.1.1-1: Supported test configurations for FR1 PCell

Table A.19.4.2.1.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.19.4.2.1.1-3: Cell specific test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.19.4.2.1.1-4: Void

Figure A.19.4.2.1.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.19.4.2.1.1-2: L1-RSRP level variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.19.4.2.1.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 120+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.19.4.2.2Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode

## A.19.4.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5D.

The test parameters are given in tables A.19.4.2.2.1-1, A.19.4.2.2.1-2, and below. There is one cell, Cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.19.4.2.2.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.19.4.2.2.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.2.2.1-1: Supported test configurations for FR1 PCell

Table A.19.4.2.2.1-2: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.19.4.2.2.1-3: Cell specific test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.19.4.2.2.1-4: Void

Table A.19.4.2.2.1-5: Void

Figure A.19.4.2.2.1-1: SNR variation for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Figure A.19.4.2.2.1-2: L1-RSRP level variation for CSI-RS based beam failure detection and link recovery testing in non-DRX mode

## A.19.4.2.2.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 30+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.19.4.2.3Beam Failure Detection and Link Recovery Test for FR1 SCell configured with with CSI-RS-based BFD and SSB-based LR in non-DRX mode

## A.19.4.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP without schedulingRequestID-BFR-SCell-r16 configuration, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the beam failure detection and link recovery for an FR1 serving cell requirements in clause 8.5D.

The test parameters are given in table A.19.4.2.3.1-1 below. The test parameters for PCell and SCell refer to Table A.6.5.5.5.1-2 and A.6.5.5.5.1-3 except those described in the table A.19.4.2.3.1-2.

There are two cells, Cell 1 is the PCell and Cell 2 is the SCell, in the test. UE is not provided by schedulingRequestID-BFR-SCell-r16, i.e., no configuration for PUCCH transmission resources, and UE shall perform the random access procedure to recover the beam failure. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.19.4.2.1.1-1 shows the SNR of the CSI-RS in set q0 in the active SCell to emulate beam failure. Figure A.19.4.2.1.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery.

Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1 and Cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.2.3.1-1: Supported test configurations for FR1 PCell and SCell

Table A.19.4.2.3.1-2: Cell specific test parameters for FR1 SCell for beam failure detection and link recovery testing in non-DRX mode

## A.19.4.2.3.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 120+10 ms after the start of T5, the UE shall transmit preamble for UL-SCH resource application, followed by MAC-CE on the assigned uplink resources containing a beam associated with the candidate beam set q1. The UE shall not transmit preamble earlier than time point B.

During T5, the System Simulator shall transmit a Random Access Response to UE after the System Simulator receives the preamble from UE. The UE shall transmit the msg.3 containing candidate beam set q1 for SCell BFR if UE receives the Random Access Response.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.19.4.3Active BWP switch

## A.19.4.3.1DCI-based and Timer-based Active BWP Switch

## A.19.4.3.1.1NR FR1 DL active BWP switch with non-DRX in SA

A.19.4.3.1.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6D.

The supported test configurations are shown in table A.19.4.3.1.1.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.19.4.3.1.1.1-2. Cell-specific parameters of the cell are specified in table A.19.4.3.1.1.1-3 below.

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

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.3.1.1.1-1: DL BWP switch supported test configurations

Table A.19.4.3.1.1.1-2: General test parameters for DL BWP switch in SA

Table A.19.4.3.1.1.1-3: NR Cell specific test parameters for DL BWP switch in SA

A.19.4.3.1.1.2Test Requirements

During T1, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed Cell 1 active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first UL slot that occurs after beginning of DL slot (i+TBWPswitchDelay+k1), (j+TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

## A.19.4.3.2RRC-based Active BWP Switch

## A.19.4.3.2.1NR FR1 DL active BWP switch of Cell with non-DRX in SA

A.19.4.3.2.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6D.

The supported test configurations are shown in table A.19.4.3.2.1.1-1. The test scenario comprises of one Cell (Cell 1) as given in table A.19.4.3.2.1.1-2. Cell-specific parameters of Cell are specified in table A.19.4.3.2.1.1-3 below.

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

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.3.2.1.1-1: DL BWP switch supported test configurations in SA scenario

Table A.19.4.3.2.1.1-2: General test parameters for DL BWP switch in SA scenario

Table A.19.4.3.2.1.1-3: NR Cell specific test parameters for DL BWP switch in SA scenario

A.19.4.3.2.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the Cell from the first DL slot that occurs right after the begining of slot  and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot. i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed Cell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.19.4.4UE specific CBW change

## A19.4.4.1UE specific CBW change on PCell in FR1 in non-DRX

## A19.4.4.1.1Test Purpose and Environment

The purpose of this test is to verify the UE specific CBW change delay requirement defined in clause 8.13D.

The supported test configurations are shown in table A.19.4.4.1.1-1. The test scenario comprises of one Cell (Cell 1), which is PCell as given in table A.19.4.4.1.1-2. Cell-specific parameters are specified in table A.19.4.4.1.1-3.

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

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.4.1.1-1: Supported test configurations for UE specific CBW change in SA scenario

Table A.19.4.4.1.1-2: General test parameters for UE specific CBW change in SA scenario

Table A.19.4.4.1.1-3: NR Cell specific test parameters for UE specific CBW change in SA scenario

## A.19.4.4.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for the PCell from the first DL slot that occurs right after the begining of slot  and starts to report valid ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot.i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed UE specific CBW change delay on the PCell to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.19.4.5Pathloss reference signal switching delay

## A.19.4.5.1MAC-CE based pathloss reference signal switch delay

## A.19.4.5.1.1Test Purpose and Environment

The purpose of this test is to verify the MAC-CE based pathloss reference signal switch delay requirement defined in clause 8.14D.

The supported test configurations are shown in table A.19.4.5.1.1-1. The test scenario comprises of one cell (Cell 1) as given in table A.19.4.5.1.1-2. Cell-specific parameters of the cell are specified in table A.19.4.5.1.1-3 below.

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

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.5.1.1-1: MAC-CE based pathloss reference signal switch supported test configurations

Table A.19.4.5.1.1-2: General test parameters for MAC-CE based pathloss reference signal switch in SA

Table A.19.4.5.1.1-3: NR Cell specific test parameters for MAC-CE based pathloss reference signal switch in SA

## A.19.4.5.1.2Test Requirements

During T3, the UE shall start to send the PHR for PCell no later than the slot i + + .THARQ3 ms + 5*Ttarget_PL-RS + 2 msNR slot length

During T3, the UE shall start to send the PHR for PCell no earlier than the slot i + + .THARQ3Nslotsubframe,µ

Where,  is the timing between pathloss reference MAC-CE activation command and acknowledgement as specified in [7],  is the periodicity of the target pathloss reference signal which is SSB in this test.THARQTtarget_PL-RS

During T3, UE shall send L1-RSRP report with measurement results for both SSB0 and SSB1.

All of the above test requirements shall be fulfilled in order for the observed pathloss RS switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The UE shall be given proper uplink transmission grant during T2 and T3.

## A.19.4.6Interruption

## A.19.4.6.1SA interruptions at NR SRS antenna port switching with 1 SRS symbol in a slot in NR-CA

## A.19.4.6.1.1Test Purpose and Environment

The purpose of this test is to verify that when a ATG UE performs SRS antenna port switching, i.e. transmits SRS on the antenna port(s) not used for PUCCH/PUSCH transmission and on the antenna port(s) used for PUCCH/PUSCH transmission at different SRS transmission occasions. The test will partly verify the interruption requirements on PCell and SCell in clause 8.2D.1.2.10.

## A.19.4.6.1.2Test Parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the FR1 PCell and Cell 2 is activated SCell on the TDD PCC. Only PCC is configured with 1 SRS resources in each SRS resource set with usage set to ‘antennaSwitching’. The test parameters for PCell and SCell are given in table A.19.4.6.1.2-2 and A.19.4.6.1.2-3 below. The test consists of two successive time periods, with duration of T1 and T2, respectively. Immediately at the beginning of T2, the UE is configured with periodic SRS for antenna port switching via RRC reconfiguration. Note that the RRC reconfiguration message should be sent to UE at the time 50 ms before the beginning of T2.

The test equipment verifies that potential interruption is carried out correctly by monitoring ACK/NACK sent in PCell.

Table A.19.4.6.1.2-1: Supported test configurations

Table A.19.4.6.1.2-2: General test parameters for SA interruptions at NR SRS antenna switching

Table A.19.4.6.1.2-3: Cell specific test parameters for SA interruptions at NR SRS antenna switching

Table A.19.4.6.1.2-4: Specific Sounding Reference Symbol Configuration for xTyR configuration

## A.19.4.6.1.3Test Requirements

The UE shall be scheduled on SCell continuously throughout the test.

During the time duration T2, the DL interruption on NR SCell during the SRS antenna switching in each SRS transmission slot on NR PCell shall not exceed 1 slot if SCell is indicated in txSwitchImpactToRx.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.19.4.6.2SA interruptions at NR SRS antenna port switching with more than 1 SRS symbol in a slot in NR-CA

## A.19.4.6.2.1Test Purpose and Environment

The purpose of this test is to verify that when a ATG UE performs SRS antenna port switching with more than 1 SRS symbols on aggressor CC defined in clause 8.2D.1.2.10. The interruption requirement is defined based on the band combination capability reported by UE, i.e., based on txSwitchImpactToRx as specified in requirement applicability in clause 8.2D.1.2.10.

## A.19.4.6.2.2Test Parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the FR1 PCell and Cell 2 is FR1 SCell. The UE is configured with the SRS antenna port in FR1 PCell. The test parameters for PCell and SCell are given in table A.19.4.6.2.2-2 and A.19.4.6.2.2-3 below. Common SRS configuration is given in clause A.3.24. Dedicated SRS configuration which is dependent on reported SRS capability supportedSRS-TxPortSwitch, is given in table A.19.4.6.2.2-4. The test consists of two successive time periods, with duration of T1 and T2, respectively. Immediately at the beginning of T2, the UE is triggered for SRS antenna port switching.

The test equipment verifies that potential interruption is carried out correctly by monitoring ACK/NACK sent in PCell.

Table A.19.4.6.2.2-1: Supported test configurations

Table A.19.4.6.2.2-2: General test parameters for SA interruptions at NR SRS antenna switching

Table A.19.4.6.2.2-3: Cell specific test parameters for SA interruptions at NR SRS antenna switching

Table A.19.4.6.2.2-4: Specific Sounding Reference Symbol Configuration for xTyR configuration

## A.19.4.6.2.3Test Requirements

The UE shall be scheduled on PCell continuously throughout the test. During the time duration T2, the interruption on SCell shall not be more than the values specified in table 8.2D.1.2.10-2 in clause 8.2D.1.2.10 for each SRS transmission slot.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.19.4.7SCell Activation and Deactivation Delay for ATG

## A.19.4.7.1SCell Activation and deactivation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle

## A.19.4.7.1.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3D, when the SCell in FR1 is known by the UE at the time of activation. Besides, the interruption on PCell due to SCell activation and deactivation is also verified in this test.

The supported test configurations for NR PCell are shown in table A.19.4.7.1.1-1 below. Supported test configurations for NR SCell are shown in table A.19.4.7.1.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently. The test parameters are given in tables A.19.4.7.1.1-2 and cell-specific parameters in tables A.19.4.7.1.1-3 and A.19.4.7.1.1-4 below. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3D. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in 5.2.2.5 in [26], and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3D, where  is the interruption length given in clause 8.2D.n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3D, and The starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3D.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.19.4.7.1.1-1: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR PCell

Table A.19.4.7.1.1-1A: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR SCell

Table A.19.4.7.1.1-2: General test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.19.4.7.1.1-3: Cell specific test parameters for NR PCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.19.4.7.1.1-4: Cell specific test parameters for NR SCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

## A.19.4.7.1.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in clause 5.2.2.5 in TS 38.214 [26], and reporting after slot (). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.n+1+THARQ+3 msNR slot length

During T3 the UE shall stop sending CSI reports for SCell at latest in a slot , as defined in clause 8.3D.m+THARQ+3 msNR slot length

During T2 interruption of PCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3D.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3D.m+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2D.1.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3D then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.19.4.7.2SCell Activation and deactivation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle

## A.19.4.7.2.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.19.4.7.1.1. The supported test configurations are the same as defined in clause A.19.4.7.1.1. The test parameters are the same except those described in the following clause. The listed parameter values in tables A.19.4.7.2.1-1 will replace the values of corresponding parameters in tables A.19.4.7.1.1-1.

Table A.19.4.7.2.1-1: General test parameters for known FR1 SCell activation case, 640 ms SCell measurement cycle

## A.19.4.7.2.2Test Requirements

The test requirements defined in clause A.19.4.7.1.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstSSB_MAX + Trs + 5 ms.

## A.19.4.7.3SCell Activation and deactivation of unknown SCell in FR1 in non-DRX

## A.19.4.7.3.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3D, when the SCell in FR1 is unknown by the UE at the time of activation. and both the PCell and SCell are co-located in an ATG NR SA configuration. The test also verifies that any PCell interruption occurring due to SCell activation or deactivation remains within the limits defined in clause 8.2D.

The supported test configurations are shown in table A.6.5.3.1.1-1 and table A.6.5.3.1.1-1A. The test parameters are given in table A.6.5.3.1.1-2 and cell-specific parameters in table A.6.5.3.1.1-3, except the parameters that are defined in A.19.4.7.3.1-1. The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3D. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in 5.2.2.5 in [26], and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3D, where  is the interruption length given in clause 8.2D.n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3D, and The starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3D.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.19.4.7.3.1-1: General test parameters for unknown FR1 SCell activation case, 160 ms SCell measurement cycle

## A.19.4.7.3.2Test Requirements

The test requirements defined in clause A.6.5.3.3.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstSSB_MAX + TSMTC_MAX + 2*Trs + 5 ms as defined in clause 8.3D.

## A.19.4.7.4Direct SCell activation at SCell addition of known SCell in FR1

## A.19.4.7.4.1Test Purpose and Environment

The purpose of this test is to verify fulfillment of direct SCell activation delay and interruption requirements at SCell addition as defined in clause 8.3D.4 and 8.2D.1, respectively. The supported test configurations for NR PCell are shown in table A.19.4.7.4.1-1. The supported test configurations for NR SCell are shown in table A.19.4.7.4.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently.

The test scenario comprises one PCell (Cell 1) and one SCell (Cell 2) as outlined in table A.19.4.7.4.1-2. Cell-specific parameters are provided in table A.19.4.7.4.1-3 and table A.19.4.7.4.1-4.

The test consists of two successive time periods with duration T1 and T2, respectively. There are two carriers, each with one cell. Cell 1 (PCell) is on RF channel 1 (PCC), and Cell 2 (SCell) is on RF channel 2 (SCC). Cell 1 and Cell 2 both operate according to one of the configurations in table A.19.4.7.4.1-1 and table A.19.4.7.4.1-1A respectively.

Before the test starts the UE is connected to Cell 1 on RF channel 1. The UE is only monitoring RF channel 1 and is not aware of Cell 2 on RF channel 2.

The UE is continuously scheduled in PCell throughout the test.

At the beginning of T1 the UE is configured to measure RF channel 2 in measurement gaps. During T1, the UE detects and measures Cell 2 on RF channel 2, and sends a measurement report containing Cell 2 to the test equipment. After having received a measurement report containing Cell 2, the test equipment deconfigures the measurement gaps and thereafter sends a RRC connection reconfiguration message to the UE by which it configures the SCell (Cell 2) in activated state (sCellState is set to activated). The time between reception of the last measurement report carrying SCell and transmission of the RRC connection reconfiguration message directly activating SCell is kept short enough to allow the SCell to remain known to the UE.

Time period T2 starts when the UE receives the RRC connection reconfiguration message at the UE antenna connector. The corresponding slot at which the message is received at the UE antenna connector is denoted n. The UE shall complete activation of the SCell no later than in slot n + , as specified in clause 8.3D.4. From slot n+  and onwards the UE shall report valid CSI both for PCell and SCell.NdirectNR slot lengthNdirectNR slot length

The test equipment verifies the activation time by counting the slots between the RRC connection reconfiguration message is sent and until CSI report with non-zero CQI for both PCell and SCell is received.

The test equipment verifies that interruptions on other serving cells are within the requirements by counting ACK/NACKs transmitted in PCell.

Table A.19.4.7.4.1-1: Supported test configurations

Table A.19.4.7.4.1-1A: Supported test configurations for NR SCell

Table A.19.4.7.4.1-2: General test parameters

Table A.19.4.7.4.1-3: NR Cell specific test parameters

Table A.19.4.7.4.1-4: NR Cell specific test parameters for NR Scell

## A.19.4.7.4.2Test Requirements

The UE shall complete the direct activation of the SCell no later than at slot n + . NdirectNR slot length

The UE shall report non-zero CQI for SCell from slot n +  and onwards throughout time period T2.NdirectNR slot length

The interruption on PCell during direct activation of the SCell shall occur within the interruption window specified in clause 8.3D.4 and shall not exceed the length specified in clause 8.2D.1.2.4.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.19.4.7.5Direct SCell activation at handover with known SCell in FR1

## A.19.4.7.5.1Test Purpose and Environment

This test is to verify the requirement for the FDD-FDD and TDD-TDD intra-frequency handover with direct SCell activation requirements specified in subclause 8.3D.5.

Supported test configurations for NR PCell are shown in table A.19.4.7.5.1-1. Supported test configurations for NR SCell are shown in table A.19.4.7.5.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently. Both handover with direct SCell activation requirements are tested by using the parameters in table A.19.4.7.5.1-2, A.19.4.7.5.1-3 and A.19.4.7.5.1-4.

The test scenario comprises of two NR carriers and 3 cells as given in tables A.19.4.7.5.1-3 and A.19.4.7.5.1-4. The test consists of three successive time periods, with time durations of T1, T2, and T3 respectively.

At the start of time duration T1, the UE is in connected mode with PCell (Cell 1) and UE is reporting CQI for PCell. The UE is configured to measure RF channel 2 in measurement gaps. During T1, the UE detects and measures Cell 2 on RF channel 2 and sends a measurement report containing Cell 2 to the test equipment. After having received a measurement report containing Cell 2, the test equipment deconfigures the measurement gaps and thereafter sends a RRC connection reconfiguration message to the UE. The time between reception of the last measurement report carrying SCell and transmission of the RRC connection reconfiguration message directly activating SCell is kept short enough to allow the SCell to remain known to the UE.

Time period T2 starts when UE receives a handover command to PCell (Cell 3) that also activates SCell 1 (Cell 2). This is done using an RRCReconfiguration message with parameter sCellState set to activated for the SCell 1 (Cell 2). The message is sent from the test equipment to the UE and is received in a subframe # denoted n at the UE antenna connector. The UE shall accomplish the activation of the SCell no later than subframe (n + Ndirect).

Time period T3 starts at (n + Ndirect), at which point UE shall be reporting a valid CQI for both PCell (Cell 3) and SCell 1.

Table A.19.4.7.5.1-1: Intra-frequency handover with direct SCell activation from FR1 to FR1 test configurations for NR PCell

Table A.19.4.7.5.1-1A: Intra-frequency handover with direct SCell activation from FR1 to FR1 test configurations for NR SCell

Table A.19.4.7.5.1-2: General test parameters Intra-frequency handover with direct SCell activation from FR1 to FR1

Table A.19.4.7.5.1-3: Cell specific test parameters for NR PCell for NR FR1-FR1 Intra-frequency handover with direct SCell activation test case

Table A.19.4.7.5.1-4: Cell specific test parameters for NR SCell for NR FR1-FR1 Intra-frequency handover with direct SCell activation test case

## A.19.4.7.5.2Test Requirements

The UE shall be capable to transmit valid CSI report for the directly activated SCell 1 no later than in subframe n+Ndirect.

The rate of correct observed SCell 1 direct activation delay during repeated tests shall be at least 90 %.

NOTE:The SCell activation delay, Ndirect, can be expressed as: Ndirect = TRRC_process + Tinterrupt + T2 + T3 + Tactivation_time + TCSI_Reporting - 3 ms, where:

TRRC_Process: RRC procedure delay defined in clause 12 of TS 38.331 [2],

Tinterrupt: Interruption time during handover as specified in clause 6.1E.1,

T2: Delay from slot  until UE has obtained a valid TA command for the target PCell,n+TRRC_Process+TinterruptNR slot length

T3: Delay for applying the received TA for uplink transmission in the target PCell, and greater than or equal to k+1 slot, where k is defined in clause 4.2 in TS 38.213,

Tactivation_time and TCSI_Reporting are specified in clause 8.3D.2, where the following definitions of TFirstSSB and TFirstSSB_MAX as defined in section 8.3D.5 shall apply:

-TFirstSSB: the time to the end of the first complete SSB burst indicated by the SMTC after slot n + (𝑇𝑅𝑅𝐶_𝑃𝑟𝑜𝑐𝑒𝑠𝑠+𝑇𝑖𝑛𝑡𝑒𝑟𝑟𝑢𝑝𝑡+𝑇2+𝑇3)/(N𝑅 𝑠𝑙𝑜𝑡 𝑙𝑒𝑛𝑔𝑡ℎ)

-TFirstSSB_MAX: the time to the end of the first complete SSB burst indicated by the SMTC after slot n + (𝑇𝑅𝑅𝐶𝑃𝑟𝑜𝑐𝑒𝑠𝑠+𝑇𝑖𝑛𝑡𝑒𝑟𝑟𝑢𝑝𝑡+𝑇2+𝑇3)/(N𝑅 𝑠𝑙𝑜𝑡 𝑙𝑒𝑛𝑔𝑡ℎ)

This gives a total of Ndirect = 10 + 52 + TIU + T2 + T3 + Tactivation_time + TCSI_Reporting - 3 ms = 62 + 10 + 13 + 6 + 20 + 2 - 3 = 94 ms for test configurations 1 and 2.

This gives a total of Ndirect = 10 + 52 + TIU + T2 + T3 + Tactivation_time + TCSI_Reporting - 3 ms = 62 + 10 + 13 + 6 + 20 + 2 - 3 = 94 ms for test configuration 3.

During T3 the UE shall send valid CSI reports for PCell and SCell 1 with non-zero CQI index and continue to send CSI reports for PCell and SCell 1 (Cell 2) with non-zero CQI index until the end of T3.

All of the above test requirements shall be fulfilled in order for the observed SCell 1 direct activation delay to be counted as correct.

## A.19.4.7.6Fast SCell Activation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle

## A.19.4.7.6.1Test Purpose and Environment

The purpose of this test is to verify that the fast SCell activation and deactivation times are within the requirements stated in clause 8.3D.7, when the SCell in FR1 is known by the UE at the time of activation.

The supported test configurations are shown in table A.19.4.7.6.1-1 below. The test parameters refer to Table A.6.5.3.10.1-2 and A.6.5.3.10.1-3 except those described in the Table A.19.4.7.6.1-2. The test consists of two successive time periods, with duration of T1and T2, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell and triggering the aperiodic CSI-RS for fast SCell activation.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n (where n mode 20=1), defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3D. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3D, where  is the interruption length given in clause 8.2D.n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.4.7.6.1-1: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations

Table A.19.4.7.6.1-2: Cell specific test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

## A.19.4.7.6.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption. During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , Tactivation_time = TFirstATRS + 5 ms, as defined in clause 8.3D.7.n+1+THARQ+3 msNR slot lengthn+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

During T2 interruption of PCell / PSCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3D.7.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

The interruption on any activated serving cell shall not be more than the values specified in clause 8.2D.1.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3D then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.19.4.7.7Fast SCell Activation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle

## A.19.4.7.7.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.19.4.7.6.1. The supported test configurations are the same as defined in clause A.19.4.7.6.1. The test parameters refer to Table A.6.5.3.10.1-2 and A.6.5.3.10.1-3 except those described in the Table A.19.4.7.7.1-1 and A.19.4.7.7.1-2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system

Table A.19.4.7.7.1-1: General test parameters for known FR1 SCell activation case, 640 ms SCell measurement cycle

Table A.19.4.7.7.1-2: Cell specific test parameters for known FR1 SCell activation case, 640 ms SCell measurement cycle

## A.19.4.7.7.2Test Requirements

The test requirements defined in clause A.19.4.7.6.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstATRS + Tgap + TATRS + 5 ms.

## A.19.4.7.8SCell Activation of unknown SCell with valid L3 measurement results in FR1 in non-DRX for 160 ms SCell measurement cycle

## A.19.4.7.8.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation time are within the requirements stated in clause 8.3D.8, when the target SCell in FR1 is unknown to the UE at the time of activation, but UE has valid L3 measurement results of the SCell.

The supported test configurations for NR PCell are shown in table A.19.4.7.8.1-1 below. Supported test configurations for NR SCell are shown in table A.19.4.7.8.1-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently. The test parameters are given in Tables A.19.4.7.8.1-2 and cell-specific parameters in tables A.19.4.7.8.1-3 and A.19.4.7.8.1-4 below. The test consists of three successive time periods, with duration of T1, T2 and T3 respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC.

The test consists of three sub tests. The slot at which the MAC message is received at the UE antenna connector, is denoted slot #n. TE continuously schedules the downlink data to UE on PCell. In Sub-test 1, TE shall schedule DCI format 0_1 at slot n + . In Sub-test 2, TE shall schedule DCI format 0_1 at slot n + , where M is defined in clause 8.3D.8 and k2 = 1. In Sub-test 3, UE shall tranmsit scheduling request on the first SR resource by 7ms+ THARQ + TSR_Periodicity to obtain the UL grant for L3 report transmission.THARQ+7msNR slot lengthTHARQ+3ms+M-k2NR slot length

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE then starts monitoring the SCC. T1 is sufficiently long so that UE is able to complete the L3 detection and measurements on the SCell to be activated. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. UE is expected to report L3 measurement result at the first PUSCH scheduled by TE.

The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3D.8. TE also indicates the TCI, based on L3 report of the UE. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after the slot that UE sends the L3 reports and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. n+THARQ+Tactivation_time+TCSI_ReportingNR slot length

During T2, any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3D.8, where  is the interruption length given in clause 8.2D.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

At the beginning of T3, the SCell de-activation command is sent. T3 shall be sufficiently long to ensure UE completes the SCell de-activation.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation of SCell.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.19.4.7.8.1-1: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR PCell

Table A.19.4.7.8.1-1A: known FR1 SCell activation in non-DRX for 160 ms SCell measurement cycle supported test configurations for NR SCell

Table A.19.4.7.8.1-2: General test parameters for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.19.4.7.8.1-3: Cell specific test parameters for NR PCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.19.4.7.8.1-4: Cell specific test parameters for NR SCell for known FR1 SCell activation case, 160 ms SCell measurement cycle

Table A.19.4.7.8.1-5: Scheduling request parameters

## A.19.4.7.8.2Test Requirements

During T2, the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption. During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot .n+1+THARQ+3 msNR slot lengthn+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

For Sub-test 1, Tactivation_time = 7 ms + k2/SCS + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3D.8, where k2/SCS is 1 ms for config 1,2 and 0.5 ms for config 3.

For Sub-test 2, Tactivation_time = 3 ms + M + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3D.8.

For Sub-test 3, Tactivation_time = 7ms + Tuncertainity_ULgrant + max (THARQ + Tuncertainty_MAC + 5ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3D.8. Where, Tuncertainity_ULgrant is uncertainty in acquiring UL grant after sending scheduling request.

During T2, interruption of PCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3D.8.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and L3 measurement reporting to be counted as correct. The rate of correct observed SCell activation delay and L3 measurement reporting during repeated tests shall be at least 90 %.

NOTE:During T2, if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3D then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.19.4.7.9TRS based SCell Activation of SSB-less SCell in FR1 inter-band CA in non-DRX for ATG

## A.19.4.7.9.1Test Purpose and Environment

The purpose of this test is to verify that the SSB-less SCell activation delay is within the requirements stated in clause 8.3D.2, when the to be activated SCell in FR1 is provided with periodic CSI-RS for tracking instead of SSB. SCell does not provide neither SSB configuration (absoluteFrequencySSB) nor SMTC configuration.

The supported test configurations are shown in table A.19.4.7.9.1-1A and A.19.4.7.9.1-1B below. The test parameters for PCell and SCell refer to Table A.6.5.3.15.1-2, A.6.6.1.1.1.2-3 and A.6.6.1.1.1.2-4 except those described in the table A.19.4.7.9.1-2. The test consists of two successive time periods, with duration of T1 and T2, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1(PCell), but is not aware of Cell 2(SCell). Cell 1 and Cell 2 are in different bands. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. At the same time, UE also receives the indication of reference serving cell in the same RRC message. The Cell 1 is indicated as the reference cell of Cell 2. The test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n (where n mod 20=1), defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3D. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3D, where  is the interruption length given in clause 8.2D.n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

This test case is only applicable to ATG UE capable of one common Rx beam between PCC band and SCC band.

Table A.19.4.7.9.1-1A: FR1 inter-band SSB-less SCell activation based on TRS for NR PCell in non-DRX for 160 ms SCell measurement cycle supported test configurations

Table A.19.4.7.9.1-1B: FR1 inter-band SSB-less SCell activation based on TRS for NR SCell in non-DRX for 160 ms SCell measurement cycle supported test configurations

Table A.19.4.7.9.1-2: PCell and SCell test configuration parameters for TRS based SCell activation of SSB-less SCell in FR1 inter-band CA in non-DRX for 160 ms measurement cycle

## A.19.4.7.9.2Test Requirements

During T2 the ATG UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption. During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , Tactivation_time  is n+1+THARQ+3 msNR slot lengthn+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

-Tfirst_TRS + TTRS + 5 ms, if aperiodic CSI-RS resources are not configured for SCell activation or UE do not support aperiodicCSI-RS-FastScellActivation-r17, when the the EPRE difference (ΔEPRE) is 12 dB

-Tfirst_TRS + 2*TTRS +5 ms, when the EPRE difference (ΔEPRE) is 30 dB

During T2 interruption of PCell / PSCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3D.2.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2D.1.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3D then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.19.5Measurement procedure

## A.19.5.1Intra-frequency Measurements

## A.19.5.1.1SA event triggered reporting tests without gap without SSB index reading under non-DRX

## A.19.5.1.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2D.5.1 and 9.2D.5.2.

## A.19.5.1.1.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test configurations are given in the Table A.19.5.1.1.2-1, the test parameters for PCell and neighbour cell refer to Table A.6.6.1.1.1.2-2 and A.6.6.1.1.1.2-3 except those described in the table A.19.5.1.1.2-2. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.5.1.1.2-1: Supported test configurations

Table A.19.5.1.1.2-2: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

## A.19.5.1.1.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.19.5.1.2SA event triggered reporting tests with per-UE gaps under non-DRX

## A.19.5.1.2.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2D.6.2 and 9.2D.6.3.

## A.19.5.1.2.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test configuration refer to Table A.6.6.1.3.2-1, the test parameters refer to Table A.6.6.1.3.2-2 and A.6.6.1.3.2-3, except those described in the table A.19.5.1.2.2-1. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.5.1.2.2-1: NR Cell specific test parameters for SA intra-frequency event triggered reporting with per-UE gaps for PCell in FR

## A.19.5.1.2.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.19.5.1.3SA event triggered reporting tests without gap under non-DRX with SSB index reading

## A.19.5.1.3.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2D.5.1 and 9.2D.5.2.

## A.19.5.1.3.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test configuration refer to Table A.6.6.1.5.2-1, the test parameters for FDD PCell and neighbour cell refer to Table A.6.6.1.5.2-2 and A.6.6.1.5.2-3 except those described in the table A.19.5.1.3.2-1. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.5.1.3.2-1: NR Cell specific test parameters for SA intra-frequency event triggered reporting without gap for FR1

## A.19.5.1.3.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.19.5.1.4SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading

## A.19.5.1.4.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the  intra-frequency cell search requirements in clause 9.2D.6.2 and 9.2D.6.3.

## A.19.5.1.4.2Test parameters

Two cells are deployed in the test, which are FR1 PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on the same frequency as the PCell. The test configuration refer to Table A.6.6.1.6.2-1, the test parameters refer to Table A.6.6.1.6.2-2 and A.6.6.1.6.2-3 except those described in the table A.19.5.1.4.2-1. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of Cell 2.

There are two BWPs configured in Cell 1, BWP1 which contains the cell defining SSB, and BWP2 which does not contain any SSB of Cell 1. During the whole test, BWP2 is always scheduled as the active BWP for the UE.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.5.1.4.2-1: NR Cell specific test parameters for SA intra-frequency event triggered reporting with gap for FDD PCell in FR1 with SSB index reading

## A.19.5.1.4.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.19.5.1.5Event triggered reporting tests on SCC with deactivated SCell under non-DRX with measurement cycle of 640ms

## A.19.5.1.5.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event when measuring the CC with deactivated SCell. This test will partly verify the intra-frequency cell search requirements in clause 9.2D.5.1 and 9.2D.5.2, and verify that the UE missed ACK/NACK rate does not exceed the limits at NR PCell interruptions during the measurement on the deactivated NR SCC as specified in 8.2D.1.2.3.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system. The specific gNB reference location is emulated by test system.

## A.19.5.1.5.2Test parameters

Supported test configurations for NR PCell are shown in table A.19.5.1.5.2-1. Supported test configurations for NR SCell are shown in table A.19.5.1.5.2-1A. Test configuration for NR PCell and test configuration for NR SCell are chosen independently.

Three cells are deployed in the test, which are FR1 PCell (Cell 1), a FR1 deactivated SCell (Cell 2) and a FR1 neighbour cell (Cell 3) on the same frequency as the SCell (Cell 2). The test parameters are given in table A.19.5.1.5.2-2 and A.19.5.1.5.2-3 below. In the measurement control information, a measurement object is configured for the frequency of the SCell, and it is indicated to the UE that event-triggered reporting with Event A6 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell 2 and the RRC message including measCycleSCell or allowInterruptions for the deactivated NR SCells is received at the UE antenna connector. During time duration T1, PCell is continuously scheduled in DL, the UE shall not have any timing information of Cell 3.

UE needs to be provided with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment.

Table A.19.5.1.5.2-1: Supported PCell test configurations

Table A.19.5.1.5.2-1A: Supported SCell test configurations

Table A.19.5.1.5.2-2: General test parameters for intra-frequency event triggered reporting without gap for SCC with deactivated SCell in FR1 with non-DRX

Table A.19.5.1.5.2-3: Cell specific test parameters for intra-frequency event triggered reporting without gap for SCC with deactivated SCell in FR1 with non-DRX

## A.19.5.1.5.3Test Requirements

The UE shall send one Event A6 triggered measurement report, with a measurement reporting delay less than 6400 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The UE shall be continuously scheduled on PCell during the entire length of T1. During the time duration T1, the UE shall transmit at least 99.5 % of ACK/NACK on PCell.

If the NR PCell is not in the same band as the deactivated SCell, the UE is only allowed to cause interruptions on NR PCell immediately before and immediately after an SMTC. Each interruption on NR PCell shall not exceed the value defined in table A.19.5.1.5.3-1.

If the NR PCell is contiguous to the deactivated SCell in the same band, the UE is only allowed to cause an interruption on PCell no earlier than 1 slot before an SMTC and no later than 1 slot after the SMTC. The interruption on NR PCell shall not exceed the value defined in table A.19.5.1.5.3-2.

Table A.19.5.1.5.3-1: Interruption duration if the PCell is not in the same band as the deactivated SCell

Table  A.19.5.1.5.3-2: Interruption duration if the PCell is in the same band as the deactivated SCell

The rate of correct events observed during repeated tests shall be at least 90%.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.19.5.2Inter-frequency Measurements

A.19.5.2.1SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used

A.19.5.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3D.4.

## A.19.5.2.1.2Test parameters

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test configuration refer to Table A.6.6.1.3.2-1. The general test parameters are given in table A.19.5.2.1.2-1. The cell specific test parameters refer to A.6.6.2.2.1-3, except those described in the table A.19.5.2.1.2-2.The DRX configuration is given in table A.19.5.2.1.2-3. The TimeAlignmentTimer configuration refers to Table A.6.6.2.2.1-5.

Measurement gap pattern configuration defined in table A.19.5.2.1.2-1 is per-UE gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE needs to be provided  with new Timing Advance Command MAC control element at least once during each time alignment timer period to maintain uplink time alignment. Furthermore, UE is allocated with PUSCH resource at every DRX cycle.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.5.2.1.2-1: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.19.5.2.1.2-2: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

Table A.19.5.2.1.2-3: DRX-Configuration for SA inter-frequency event triggered reporting without SSB time index detection

## A.19.5.2.1.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1080 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 10240 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

A.19.5.2.2SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used

A.19.5.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3D.4 and 9.3D.5.

## A.19.5.2.2.2Test parameters

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2. The test configurations refer to Tables A.6.6.2.5.1-1. The test parameters refer to Table A.6.6.2.5.1-2 and A.6.6.2.5.1-3 except those described in table A.19.5.2.2.2-1.

Measurement gap pattern configuration defined in table A.6.6.2.5.1-2 is per-UE gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.5.2.2.2-1: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 with SSB time index detection

A.19.5.2.2.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1040 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

A.19.5.2.3SA event triggered reporting tests for FR1 without gap when DRX is not used

A.19.5.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clause 9.3D.9.

## A.19.5.2.3.2Test parameters

In this test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as neighbour cell in FR1 on NR RF channel 2.  The SSB of Cell 2 is completely within UE’s active BWP BW. The RBs containing SSB from Cell 1 and Cell 2 should be different in frequency location within the cell bandwidth. The test configuration refer to Table A.6.6.2.11.1-1. The test parameters refer to Tables A.6.6.2.11.1-2 and A.6.6.2.11.1-3 except those described in table A.19.5.2.3.2-1.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event A3 is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR Cell 2.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.5.2.3.2-1: Cell specific test parameters for SA inter-frequency event triggered reporting for FR1 without gap

## A.19.5.2.3.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 800 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.19.5.3L1-RSRP measurement for beam reporting for ATG

## A.19.5.3.1SSB based L1-RSRP measurement when DRX is not used

## A.19.5.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5D.4.1, with the testing configurations for NR ATG cells in table A.19.5.3.1.1-1.

Table A.19.5.3.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test for ATG

## A.19.5.3.1.2Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). The test parameters from Table A.6.6.4.1.2-1 and table A.6.6.4.1.2-2 are used except those described in table A.19.5.3.1.2-1.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.19.5.3.1.2-1: General test parameters

## A.19.5.3.1.3Test Requirements

The test requirements of this test case are the same as those defined in clause A.6.6.4.1.3.

## A.19.5.3.2CSI-RS based L1-RSRP measurement when DRX is not used

## A.19.5.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5D.4.2, with the testing configurations for NR ATG cells in table A.19.5.3.2.1-1.

Table A.19.5.3.2.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test for ATG

## A.19.5.3.2.2Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). The test parameters from Table A.6.6.4.3.2-1 and table A.6.6.4.3.2-2 are used except those described in table A.19.5.3.2.2-1.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (0 for Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.6.6.4.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.19.5.3.2.2-1: General test parameters

## A.19.5.3.2.3Test Requirements

The test requirements of this test case are the same as those defined in clause A.6.6.4.3.3.

## A.19.5.4L1-SINR measurement for beam reporting for ATG

## A.19.5.4.1L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured when DRX is not used

A.19.5.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements in clause 9.8D.4.1, with the testing configurations for NR ATG cells in table A.19.5.4.1.1-1.

Table A.19.5.4.1.1-1: Applicable NR configurations for FR1 CSI-RS based L1-SINR test for ATG

A.19.5.4.1.2Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). The test parameters from Table A.6.6.8.1.2-1 and table A.6.6.8.1.2-2 are used except those described in table A.19.5.4.1.2-1.

In the CSI-RS measurement configuration, UE is indicated to perform L1-SINR measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-SINR on aperiodic CSI-RS resources. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (1 Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.6.6.8.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.19.5.4.1.2-1: General test parameters

## A.19.5.4.1.3Test Requirements

The test requirements of this test case are the same as those defined in clause A.6.6.8.1.3.

## A.19.5.4.2L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used

## A.19.5.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements in clause 9.8D.4.2, with the testing configurations for NR ATG cells in table A.19.5.4.2.1-1.

Table A.19.5.4.2.1-1: Applicable NR configurations for FR1 L1-SINR measurement test with SSB based CMR and CSI-RS based IMR for ATG

## A.19.5.4.2.2Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). The test parameters from Table A.6.6.8.2.2-1, table A.6.6.8.2.2-2, and table A.6.6.8.2.2-3 are used except those described in table A.19.5.4.2.2-1.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the SSBs and the associated CSI-RS resources, and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD measurements based on the SSBs, and UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-RS resources as IMR.

Table A.19.5.4.2.2-1: General test parameters

## A.19.5.4.2.3Test Requirements

The test requirements of this test case are the same as those defined in clause A.6.6.8.2.3.

## A.19.5.4.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used

## A.19.5.4.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-SINR measurement. This test will partly verify the L1-SINR measurement requirements with CSI-RS based CMR and dedicated IMR configured in clause 9.8D.4.3, with the testing configurations for NR ATG cells in table A.19.5.4.3.1-1.

Table A.19.5.4.3.1-1: Applicable NR configurations for FR1 L1-SINR test with CMR and dedicated IMR for ATG

## A.19.5.4.3.2Test parameters

There is one cell in the test, the FR1 PCell (Cell 1). The test parameters from Table A.6.6.8.3.2-1 and table A.6.6.8.3.2-2 are used except those described in table A.19.5.4.3.2-1.

In CSI measurement configuration, UE is indicated to perform L1-SINR measurement on the configured CSI-RS as CMR and an associated CSI-IM as IMR, and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-SINR on aperiodic CSI-RS resources. UE is also configured to measure L1-SINR based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (1 Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.6.6.8.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs, and UE is configured to perform L1-SINR measurement based on the CSI-RS as CMR and the CSI-IM as IMR.

Table A.19.5.4.3.2-1: General test parameters

## A.19.5.4.3.3Test Requirements

The test requirements of this test case are the same as those defined in clause A.6.6.8.3.3

## A.19.5.5NR measurements with autonomous gaps for ATG

## A.19.5.5.1SA intra-frequency CGI identification of NR neighbor cell in FR1

## A.19.5.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of intra-frequency CGI identification of an NR neighbour ATG cell in FR1 with autonomous gaps. This test shall partly verify the measurement requirements in clause 9.11D, with the testing configurations for NR ATG cells in table A.19.5.5.1.1-1

Table A.19.5.5.1.1-1: Supported test configurations for ATG

## A.19.5.5.1.2Test Parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the FR1 PCell and Cell 2 is an FR1 neighbour cell on the same frequency as the PCell. The test parameters from Table A.6.6.7.1.2-2 and table A.6.6.7.1.2-3 are used except those described in A.19.5.5.1.2-1.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable.  A measurement object is configured for the frequency of the PCell and it is indicated to the UE that event-triggered reporting with Event A3 is used. The UE is expected to detect and send a measurement report with Event A3.

A new RRC message triggering CGI identification shall be sent to the UE during period T2, after the UE has reported Event A3. The RRC message shall create a measurement report configuration with purpose reportCGI and useAutonomousGaps set to TRUE. The start of T3 is the instant when the last TTI containing the RRC message implying CGI identification is sent to the UE.

The test equipment verifies that potential interruption is carried out correctly by monitoring ACK/NACK sent in PCell during T3 until a measurement report with CGI is sent.

Table A.19.5.5.1.2-1: NR Cell specific test parameters for SA intra-frequency CGI identification of NR neighbor cell in FR1

## A.19.5.5.1.3Test Requirements

The test requirements of this test case are the same as those defined in clause A.6.6.7.1.3

## A.19.6Measurement Performance requirements

Unless explicitly stated otherwise:

-Reported measurements shall be within defined range of accuracy limits defined in clause 10 for at least 90 % of the reported cases. If multiple measurement performance requirements are verified in the same test, the reported measurements for each requirement shall be within defined range of accuracy limits of the corresponding requirement defined in clause 10 for at least 90 % of the reported cases.

-Measurements are performed in RRC_CONNECTED state.

-The reference channels assume transmission of PDSCH with a maximum number of 5 HARQ transmissions unless otherwise specified.

## A.19.6.1SS-RSRP for ATG UE

## A.19.6.1.1SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

## A.19.6.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.2.1.1 and 10.1.2.1.2 for intra-frequency measurements.

## A.19.6.1.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.19.6.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in table A.6.7.1.1.2-2, except those described in the Table A.19.6.1.1.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.1.1.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

Table A.19.6.1.1.2-2: SS-RSRP Intra frequency test parameters

## A.19.6.1.1.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.2.1.1 and relative requirement in clause 10.1.2.1.2.

## A.19.6.1.2SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

## A.19.6.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.4.1.1 and 10.1.4.1.2 for inter-frequency measurements with the testing configurations for NR cells in table A.19.6.1.2.1-1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.1.2.1-1: Applicable NR configurations for FR1 inter-frequency SS-RSRP accuracy test

## A.19.6.1.2.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.19.6.1.2.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.6.7.1.2.2-1, except those described in the Table A.19.6.1.2.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.19.6.1.2.2-1: SS-RSRP inter-frequency test parameters

## A.19.6.1.2.3Test Requirements

The SS-RSRP measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.4.1.1 and relative requirement in clause 10.1.4.1.2.

## A.19.6.2SS-RSRQ for ATG UE

## A.19.6.2.1SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.19.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.7.1.1.

## A.19.6.2.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configuration are shown in table A.19.6.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.6.7.2.1.2-2, except those described in the given in table A.19.6.2.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

Table A.19.6.2.1.2-2: SS-RSRQ Intra frequency test parameters

## A.19.6.2.1.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.7.1.1.

## A.19.6.2.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.19.6.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.9.1.1 and 10.1.9.1.2.

## A.19.6.2.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.19.6.2.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.6.7.2.2.2-2 except those described in the Table A.19.6.2.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.2.2.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

Table A.19.6.2.2.2-2: SS-RSRQ Inter frequency test parameters

## A.19.6.2.2.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.9.1.1 and 10.1.9.1.2.

## A.19.6.3SS-SINR for ATG UE

## A.19.6.3.1SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.19.6.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.12.1.1.

## A.19.6.3.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.19.6.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.6.7.3.1.2-2, except those described in the Table A.19.6.3.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

Table A.19.6.3.1.2-2: SS-SINR Intra frequency test parameters

## A.19.6.3.1.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.12.1.1.

## A.19.6.3.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.19.6.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.14.1.1 and 10.1.14.1.2.

## A.19.6.3.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.19.6.3.2.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.6.7.3.2.2-2, except those described in the Table A.19.6.3.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.3.2.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

Table A.19.6.3.2.2-2: SS-SINR Inter frequency test parameters

## A.19.6.3.2.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirements in clause 10.1.14.1.1 and 10.1.14.1.2.

## A.19.6.4L1-RSRP measurement for beam reporting for ATG UE

## A.19.6.4.1SSB based L1-RSRP measurement

## A.19.6.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.5D.2 and clause 10.1.19.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.19.6.4.1.1-1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.19.6.4.1.2Test parameters

In this set of test cases there one cell in the test, PCell (Cell 1).. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.6.7.4.1.2-1, except those described in the Table A.19.6.4.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.19.6.4.1.2-1: FR1 SSB based L1-RSRP test parameters

## A.19.6.4.1.3Test Requirements

The L1-RSRP measurement accuracy for SSB resource reported by UE in L1-RSRP report (SSB#0 or SSB#1) of Cell 2 shall fulfil the requirements in clauses 10.1.19.1.

## A.19.6.4.2CSI-RS based L1-RSRP measurement on resource set with repetition off

## A.19.6.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.5D.3 and clause 10.1.19.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.19.6.4.2.1-1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.4.2.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.19.6.4.2.2Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1). The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.6.7.4.2.2-2 is used except those described in the Table A.19.6.4.2.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.19.6.4.2.2-1: FR1 CSI-RS based L1-RSRP test parameters

## A.19.6.4.2.3Test Requirements

The L1-RSRP measurement accuracy for CSI-RS resource reported by UE in L1-RSRP report (CSI-RS#0 or CSI-RS#1) of Cell 1 shall fulfil the requirements in clause 10.1.19.2.

## A.19.6.5L1-SINR measurement for beam reporting based CMR for ATG UE

## A.19.6.5.1L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured and CSI-RS resource set with repetition off

## A.19.6.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.8D.4.1 and clause 10.1.27.1 for L1-SINR measurements based on CSI-RS with the testing configurations for NR cells in table A.19.6.5.1.1-1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.5.1.1-1: Applicable NR configurations for FR1 L1-SINR test with CSI-RS based CMR and no dedicated IMR configured

## A.19.6.5.1.2Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1).The absolute and relative accuracy of L1-SINR measurements are tested by using the parameters in table A.6.7.9.1.2-1 except those described in table A.19.6.5.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.19.6.5.1.2-1: FR1 CSI-RS based L1-SINR test parameters

## A.19.6.5.1.3Test Requirements

The L1-SINR measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirements in clause 10.1.27.1.

## A.19.6.5.2L1-SINR measurement with SSB based CMR and dedicated IMR

## A.19.6.5.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.8D.4.2 and clause 10.1.27.2 for L1-SINR measurements with SSB based CMR and dedicated CSI-RS based IMR, with the testing configurations for NR cells in table A.19.6.5.2.1-1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.5.2.1-1: Applicable NR configurations for FR1 L1-SINR measurement test with SSB based CMR and CSI-RS based IMR

## A.19.6.5.2.2Test parameters

In this set of test cases there one cell in the test, PCell (Cell 1). The absolute accuracy of L1-SINR measurements are tested by using the parameters in table A.6.7.9.2.2-1 except those described in the Table A.19.6.5.2.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources and one CSI-RS resource set with two CSI-RS resource. UE is configured to perform RLM and BFD measurement based on the SSB resources 0 and 1. UE is configured to perform L1-SINR measurement based on the SSBs as CMR and the CSI-RS resources as IMR.

Table A.19.6.5.2.2-1: FR1 SSB based L1-SINR test parameters

## A.19.6.5.2.3Test Requirements

The L1-SINR measurement accuracy for SSB#0+CSI-RS#0 and SSB#1+CSI-RS#1 of Cell 1 shall fulfil the requirements in clauses 10.1.27.2.

## A.19.6.5.3L1-SINR measurement with CSI-RS based CMR and dedicated IMR

## A.19.6.5.3.1Test Purpose and Environment

The purpose of this test is to verify that the L1-SINR measurement accuracy is within the specified limits. This test will partly verify the requirements in clauses 9.8D.4.3 and clause 10.1.27.3 for L1-SINR measurements based on CSI-RS as CMR and CSI-IM as IMR with the testing configurations for NR cells in table A.19.6.5.3.1-1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.5.3.1-1: Applicable NR configurations for FR1 L1-SINR measurement test with CSI-RS based CMR and CSI-IM based IMR

## A.19.6.5.3.2Test parameters

In this set of test cases there are one cell in the test, PCell (Cell 1). The absolute and relative accuracy of L1-SINR measurements are tested by using the parameters in table A.6.7.9.3.2-1 except those described in table A.19.6.5.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources and one CSI-IM resource set with two CSI-IM resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB. UE is configured to perform L1-SINR measurement based on the configured CSI-RS as CMR and CSI-IM as IMR.

Table A.19.6.5.3.2-1: FR1 L1-SINR measurement test with CSI-RS based CMR and CSI-IM based IMR

## A.19.6.5.3.3Test Requirements

The L1-SINR measurement accuracy for CSI-RS#0+CSI-IM#0 and CSI-RS#1+CSI-IM# of Cell 1 shall fulfil the requirements in clause 10.1.27.3.

## A.19.6.6CSI-RSRP for ATG UE

## A.19.6.6.1SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

## A.19.6.6.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.2.3.1 and 10.1.2.3.2 for CSI-RS intra-frequency measurements.

## A.19.6.6.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.19.6.6.1.2-1. Both absolute and relative accuracy of CSI-RSRP intra-frequency measurements are tested by using the parameters in table A.6.7.10.1.2-2, except those described in the Table A.19.6.6.1.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.6.1.2-1: CSI-RSRP intra frequency supported test configurations

Table A.19.6.6.1.2-2: CSI-RSRP intra frequency test parameters

## A.19.6.6.1.3Test Requirements

The CSI-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.2.3.1 and relative requirement in clause 10.1.2.3.2.

## A.19.6.6.2SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell

## A.19.6.6.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.4.3.1 and 10.1.4.3.2 for CSI-RS inter-frequency measurements with the testing configurations for NR cells in table A.19.6.6.2.1-1.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.6.2.1-1: Applicable NR configurations for FR1 inter-frequency CSI-RSRP accuracy test

## A.19.6.6.2.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency than the PCell. Both absolute and relative accuracy of CSI-RSRP inter-frequency measurements are tested by using the parameters in table A.6.7.10.2.2-1, except those described in the Table A.19.6.6.2.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.19.6.6.2.2-1: CSI-RSRP inter-frequency test parameters

## A.19.6.6.2.3Test Requirements

The CSI-RSRP measurement accuracy for Cell 2 shall fulfil the absolute requirement in clause 10.1.4.3.1 and relative requirement in clause 10.1.4.3.2.

## A.19.6.7CSI-RSRQ for ATG UE

## A.19.6.7.1SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.19.6.7.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.7.2.

## A.19.6.7.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.19.6.7.1.2-1. The absolute accuracy of CSI-RSRQ intra-frequency measurement is tested by using the parameters in table A.6.7.11.1.2-2, except those described in the Table A.19.6.7.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.7.1.2-1: Intra frequency CSI-RSRQ supported test configurations

Table A.19.6.7.1.2-2: CSI-RSRQ Intra frequency test parameters

## A.19.6.7.1.3Test Requirements

The CSI-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.7.2.

## A.19.6.7.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.19.6.7.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.9.2.1 and 10.1.9.2.2.

## A.19.6.7.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.19.6.7.2.2-1. Both absolute accuracy and relative accuracy requirements of CSI-RSRQ inter-frequency measurement are tested by using test parameters in table A.6.7.11.2.2-2, except those described in the Table A.19.6.7.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.7.2.2-1: CSI-RSRQ Inter frequency CSI-RSRQ supported test configurations

Table A.19.6.7.2.2-2: CSI-RSRQ Inter frequency test parameters

## A.19.6.7.2.3Test Requirements

The CSI-RSRQ measurement accuracy shall fulfil the requirements in clause 10.1.9.2.1 and 10.1.9.2.2.

## A.19.6.8CSI-SINR for ATG UE

## A.19.6.8.1SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.19.6.8.1.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 10.1.12.2.1.

## A.19.6.8.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.19.6.8.1.2-1. The absolute accuracy of CSI-SINR intra-frequency measurement is tested by using the parameters in table A.6.7.12.1.2-2, except those described in the Table A.19.6.8.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.8.1.2-1: CSI-SINR Intra frequency CSI-SINR supported test configurations

Table A.19.6.8.1.2-2: CSI-SINR Intra frequency test parameters

## A.19.6.8.1.3Test Requirements

The CSI-SINR measurement accuracy shall fulfil the requirements in clause 10.1.12.2.1.

## A.19.6.8.2SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell

## A.19.6.8.2.1Test Purpose and Environment

The purpose of this test is to verify that the CSI-SINR measurement accuracy is within the specified limits. This test will verify the requirements in clauses 10.1.14.2.1 and 10.1.14.2.2.

## A.19.6.8.2.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.19.6.8.2.2-1. Both absolute accuracy and relative accuracy requirements of CSI-SINR inter-frequency measurement are tested by using test parameters in table A.6.7.12.2.2-2, except those described in the Table A.19.6.8.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

UE positioning and UE speed are set by AT command. UE speed is 0km/h, UE specific positioning is emulated by test system.

The specific gNB reference location is emulated by test system.

Table A.19.6.8.2.2-1: CSI-SINR Inter frequency CSI-SINR supported test configurations

Table A.19.6.8.2.2-2: CSI-SINR Inter frequency test parameters

## A.19.6.8.2.3Test Requirements

The CSI-SINR measurement accuracy shall fulfil the requirements in clause 10.1.14.2.1 and 10.1.14.2.2.

## A.20NR standalone tests for RedCap UE with Satellite Access

## A.20.1RRC_IDLE state mobility

## A.20.1.1Cell reselection to FR1 intra-frequency NR case for 1Rx RedCap UE

## A.20.1.1.1Test Purpose and Environment

Test purpose and environment in clause A.14.1.1.1 shall apply for 1Rx RedCap UE.

## A.20.1.1.2Test Parameters

Test parameters in clause A.14.1.1.2 shall apply except that:

-Table A.14.1.1.2-1 is replaced with A.20.1.1.2-1, and

-NR cell specific test parameters in Table A.20.1.1.2-2 replace the corresponding parameters in Table A.14.1.1.2-3, and

-Table A.14.1.1.2-2 and Table A.14.1.1.2-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.1.1.2-1: Supported test configurations

Table A.20.1.1.2-2: Cell specific test parameters for intra frequency NR cell re-selection test case

## A.20.1.1.3Test Requirements

Test requirements in clause A.14.1.1.3 shall apply for 1Rx RedCap UEs.

## A.20.1.2Cell reselection to FR1 intra-frequency NR case  for 2Rx RedCap UE

## A.20.1.2.1Test Purpose and Environment

Test purpose and environment in clause A.14.1.1.1 shall apply for 2Rx RedCap UE.

## A.20.1.2.2Test Parameters

Test parameters in clause A.14.1.1.2 shall apply except that:

-Table A.14.1.1.2-1 is replaced with A.20.1.1.2-1, and

-NR cell specific test parameters in Table A.20.1.1.2-2 replace the corresponding parameters in Table A.14.1.1.2-3, and

-Table A.14.1.2.2-2 and Table A.14.1.2.2-3 shall apply to configurations 1, 2, 3 and 4.

## A.20.1.2.3Test Requirements

Test requirements in clause A.14.1.1.3 shall apply for 2Rx RedCap UEs.

## A.20.1.3Cell reselection to FR1 intra-frequency NR cell for 1Rx RedCap UE configured with the feature for enhanced requirements

## A.20.1.3.1Test Purpose and Environment

Test purpose and environment in clause A.14.1.2.1 shall apply for 1Rx RedCap UE.

## A.20.1.3.2Test Parameters

Test parameters in clause A.14.1.2.2 shall apply except that:

-Table A.14.1.2.2-1 is replaced with A.20.1.1.2-1, and

-NR cell specific test parameters in Table A.20.1.3.2-1 replace the corresponding parameters in Table A.14.1.2.2-3, and

-Table A.14.1.2.2-2 and Table A.14.1.2.2-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.1.3.2-1: Cell specific test parameters for intra frequency NR cell re-selection test case

## A.20.1.3.3Test Requirements

Test requirements in clause A.14.1.2.3 shall apply for 1Rx RedCap UEs.

## A.20.1.4Cell reselection to FR1 intra-frequency NR cell for 2Rx RedCap UE configured with the feature for enhanced requirements

## A.20.1.4.1Test Purpose and Environment

Test purpose and environment in clause A.14.1.2.1 shall apply for 2Rx RedCap UE.

## A.20.1.4.2Test Parameters

Test parameters in clause A.14.1.2.2 shallapply except that:

Table A.14.1.2.2-1 is replaced with A.20.1.1.2-1, and

NR cell specific test parameters in Table A.20.1.3.2-1 replace the corresponding parameters in Table A.14.1.2.2-3, and

-Table A.14.1.2.2-2 and Table A.14.1.2.2-3 shall apply to configurations 1, 2, 3 and 4.

## A.20.1.4.3Test Requirements

Test requirements in clause A.14.1.2.3 shall apply for 2Rx RedCap UEs.

## A.20.1.5Time-based measurement initiation to FR1 intra-frequency NR cell reselection for 1Rx RedCap UE

## A.20.1.5.1Test Purpose and Environment

Test purpose and environment in clause A.14.1.3.1 shall apply for 1Rx RedCap UE.

## A.20.1.5.2Test Parameters

Test parameters in clause A.14.1.3.2 shall apply except that:

Table A.14.1.3.2-1 is replaced with A.20.1.1.2-1, and

NR cell specific test parameters in Table A.20.1.5.2-1 replace the corresponding parameters in Table A.14.1.2.2-3, and

Table A.14.1.3.2-2 and Table A.14.1.3.2-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.1.5.2-1: Cell specific test parameters for intra frequency NR cell re-selection test case

## A.20.1.5.3Test Requirements

Test requirements in clause A.14.1.3.3 shall apply for 1Rx RedCap UEs.

## A.20.1.6Time-based measurement initiation to FR1 intra-frequency NR cell reselection for 2Rx RedCap UE

## A.20.1.6.1Test Purpose and Environment

Test purpose and environment in clause A.14.1.3.1 shall apply for 2Rx RedCap UE.

## A.20.1.6.2Test Parameters

Test parameters in clause A.14.1.3.2 shall apply except that:

Table A.14.1.3.2-1 is replaced with A.20.1.1.2-1, and

NR cell specific test parameters in Table A.20.1.5.2-1 replace the corresponding parameters in Table A.14.1.3.2-3, and

-Table A.14.1.3.2-2 and Table A.14.1.3.2-3 shall apply to configurations 1, 2, 3 and 4.

## A.20.1.6.3Test Requirements

Test requirements in clause A.14.1.3.3 shall apply for 2Rx RedCap UEs.

## A.20.1.7Location-based measurement initiation to FR1 inter-frequency NR cell reselection for 1Rx RedCap UE

## A.20.1.7.1Test Purpose and Environment

Test purpose and environment in clause A.14.1.8.1 shall apply for 1Rx RedCap UE.

## A.20.1.7.2Test Parameters

Test parameters in clause A.14.1.8.2 shall apply except that:

Table A.14.1.8.2-1 is replaced with A.20.1.1.2-1, and

NR cell specific test parameters in Table A.20.1.7.2-1 replace the corresponding parameters in Table A.14.1.3.2-3, and

Table A.14.1.8.2-2 and Table A.14.1.8.2-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.1.7.2-1: Cell specific test parameters for inter frequency NR cell re-selection test case

## A.20.1.7.3Test Requirements

Test requirements in clause A.14.1.8.3 shall apply for 1Rx RedCap UEs.

## A.20.1.8Location-based measurement initiation to FR1 inter-frequency NR cell reselection for 2Rx RedCap UE

## A.20.1.8.1Test Purpose and Environment

Test purpose and environment in clause A.14.1.8.1 shall apply for 2Rx RedCap UE.

## A.20.1.8.2Test Parameters

Test parameters in clause A.14.1.8.2 shall apply except that:

Table A.14.1.8.2-1 is replaced with A.20.1.1.2-1, and

NR cell specific test parameters in Table A.20.1.7.2-1 replace the corresponding parameters in Table A.14.1.3.2-3, and

-Table A.14.1.8.2-2 and Table A.14.1.8.2-3 shall apply to configurations 1, 2, 3 and 4.

## A.20.1.8.3Test Requirements

Test requirements in clause A.14.1.8.3 shall apply for 2Rx RedCap UEs.

## A.20.1.9Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion for 1Rx RedCap UE

## A.20.1.9.1Test Purpose and Environment

Test purpose and environment in clause A.14.1.9.1 shall apply for 1Rx RedCap UE.

## A.20.1.9.2Test Parameters

Test parameters in clause A.14.1.9.2 shall apply except that:

Table A.14.1.9.2-1 is replaced with A.20.1.1.2-1, and

Table A.14.1.9.2-2 is replaced with A.20.1.9.2-1, and,

Table A.14.1.9.2-3 is replaced with A.20.1.9.2-2.

Table A.20.1.9.2-1: General test parameters for FR1 inter frequency NR cell re-selection test case for UE fulfilling low mobility criterion

Table A.20.1.9.2-2: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case in AWGN for UE fulfilling low mobility criterion

## A.20.1.9.3Test Requirements

Test requirements in clause A.14.1.9.3 shall apply for 1Rx RedCap UEs.

## A.20.1.10Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion for 2Rx RedCap UE

## A.20.1.10.1Test Purpose and Environment

Test purpose and environment in clause A.14.1.9.1 shall apply for 2Rx RedCap UE.

## A.20.1.10.2Test Parameters

Test parameters in clause A.14.1.9.2 shall apply except that:

Table A.14.1.9.2-1 is replaced with A.20.1.1.2-1, and

Table A.14.1.9.2-2 is replaced with A.20.1.9.2-1, and,

-Table A.14.1.9.2-3 is replaced with A.20.1.9.2-2.

## A.20.1.10.3Test Requirements

Test requirements in clause A.14.1.9.3 shall apply for 2Rx RedCap UEs.

## A.20.1.11Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion for 1Rx RedCap UEs

## A.20.1.11.1Test Purpose and Environment

Test purpose and environment in clause A.14.1.10.1 shall apply for 1Rx RedCap UE.

## A.20.1.11.2Test Parameters

Test parameters in clause A.14.1.10.2 shall apply except that:

Table A.14.1.3.2-1 is replaced with A.20.1.1.2-1, and

Table A.14.1.10.2-2 is replaced with A.20.1.11.2-1, and,

Table A.14.1.10.2-3 is replaced with A.20.1.11.2-2.

Table A.20.1.11.2-1: General test parameters for FR1 inter frequency NR cell re-selection test case for UE fulfilling not-at-cell edge criterion

Table A.20.1.11.2-2: Cell specific test parameters for FR1 inter frequency NR cell re-selection test case in AWGN for UE fulfilling not-at-cell edge criterion

## A.20.1.11.3Test Requirements

Test requirements in clause A.14.1.10.3 shall apply for 1Rx RedCap UEs.

## A.20.1.12Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion for 2Rx RedCap UEs

## A.20.1.12.1Test Purpose and Environment

Test purpose and environment in clause A.14.1.10.1 shall apply for 2Rx RedCap UE.

## A.20.1.12.2Test Parameters

Test parameters in clause A.14.1.10.2 shall apply except that:

Table A.14.1.3.2-1 is replaced with A.20.1.1.2-1, and

Table A.14.1.10.2-2 is replaced with A.20.1.11.2-1, and,

-Table A.14.1.10.2-3 is replaced with A.20.1.11.2-2.

## A.20.1.12.3Test Requirements

Test requirements in clause A.14.1.10.3 shall apply for 2Rx RedCap UEs.

## A.20.1.13Cell reselection to FR1 inter-RAT for NR NTN carrier for 1Rx RedCap UE

## A.20.1.13.1Test purpose and Environment

Test purpose and environment in clause A.14.1.11.1 shall apply for 1Rx RedCap UE.

## A.20.1.13.2Test Parameters

-Table A.14.1.11.2-1 is replaced with A.20.1.13.2-1, and

-Table A.14.1.11.2-2 is replaced with A.20.1.13.2-2, and,

-Table A.14.1.11.2-3 is replaced with A.20.1.13.2-3, and,

-Table A.14.1.11.2-4 is replaced with A.20.1.13.2-4.

A.20.1.13.2-1: Supported test configurations

Table A.20.1.13.2-2: General test parameters for NR to E-UTRAN cell re-selection test case

Table A.20.1.13.2-3: Cell specific test parameters for NR Cell 1

Table A.20.1.13.2-4: Cell specific test parameters for E-UTRA Cell 2

## A.20.1.13.3Test requirements

Test requirements in clause A.14.1.11.3 shall apply for 1Rx RedCap UEs.

## A.20.1.14Cell reselection to FR1 inter-RAT for NR NTN carrier for 2Rx RedCap UE

## A.20.1.14.1Test purpose and Environment

Test purpose and environment in clause A.14.1.11.1 shall apply for 2Rx RedCap UE.

## A.20.1.14.2Test Parameters

-Table A.14.1.11.2-1 is replaced with A.20.1.13.2-1, and

-Table A.14.1.11.2-2 is replaced with A.20.1.13.2-2, and,

-Table A.14.1.11.2-3 is replaced with A.20.1.13.2-3, and,

-Table A.14.1.11.2-4 is replaced with A.20.1.13.2-4.

## A.20.1.14.3Test requirements

Test requirements in clause A.14.1.11.3 shall apply for 2Rx RedCap UEs.

## A.20.1.15Cell re-selection to FR1 inter-frequency NR case with TN carrier for 1Rx RedCap UE

## A.20.1.15.1Test purpose and Environment

Test purpose and environment in clause A.14.1.12.1 shall apply for 1Rx RedCap UE.

## A.20.1.15.2Test parameters

-Table A.14.1.12.2-1 is replaced with A.20.1.15.2-1, and

-Table A.14.1.12.2-2 is replaced with A.20.1.15.2-2, and,

-Table A.14.1.12.2-3 is replaced with A.20.1.15.2-3.

Table A.20.1.15.2-1: Supported test configurations

Table A.20.1.15.2-2: General test parameters for inter frequency NR cell re-selection test case

Table A.20.1.15.2-3: Cell specific test parameters for inter frequency NR cell re-selection test case

## A.20.1.15.3Test requirements

Test requirements in clause A.14.1.12.3 shall apply for 1Rx RedCap UEs.

## A.20.1.16Cell re-selection to FR1 inter-frequency NR case with TN carrier for 2Rx RedCap UE

## A.20.1.16.1Test purpose and Environment

Test purpose and environment in clause A.14.1.12.1 shall apply for 2Rx RedCap UE.

## A.20.1.16.2Test parameters

-Table A.14.1.12.2-1 is replaced with A.20.1.15.2-1, and

-Table A.14.1.12.2-2 is replaced with A.20.1.15.2-2, and,

-Table A.14.1.12.2-3 is replaced with A.20.1.15.2-3.

## A.20.1.16.3Test requirements

Test requirements in clause A.14.1.12.3 shall apply for 2Rx RedCap UEs.

## A.20.2RRC_CONNECTED state mobility

## A.20.2.1Handover

## A.20.2.1.1Intra-frequency SAN Handover from FR1 to FR1 for 1Rx RedCap UE

## A.20.2.1.1.1Test Purpose and Environment

This test is to verify the requirement for Intra-frequency SAN Handover from FR1 to FR1 specified in clause 6.1F.1 for 1Rx RedCap UE.

## A.20.2.1.1.2Test Parameters

Test parameters in clause A.14.2.1.1.2 shall apply except that the supported test configurations are defined in table A.20.2.1.1.2-1, and NR Cell specific test parameters in Table A.20.2.1.1.2-2 replace the corresponding parameters in Table A.14.2.1.1.2-3. Other parameters in Table A.14.2.1.1.2-2 and Table A.14.2.1.1.2-3 shall apply to test configurations 1, 2, 3 and 4.

In the test, the target cell is known by the UE and carries only CD-SSB.

Table A.20.2.1.1.2-1: Supported test configurations

Table A.20.2.1.1.2-2: Cell specific test parameters for Intra frequency SAN handover test case

## A.20.2.1.1.3Test Requirements

Test requirements in clause A.14.2.1.1.3 shall apply for 1Rx RedCap UEs.

## A.20.2.1.2Intra-frequency SAN Handover from FR1 to FR1 for 2Rx RedCap UE

## A.20.2.1.2.1Test Purpose and Environment

This test is to verify the requirement for Intra-frequency SAN Handover from FR1 to FR1 specified in clause 6.1F.1 for 2Rx RedCap UE.

## A.20.2.1.2.2Test Parameters

Test parameters in clause A.20.2.1.1.2 shall apply. The antenna configuration for 2Rx RedCap UE is 1x2.

## A.20.2.1.2.3Test Requirements

Test requirements in clause A.14.2.1.1.3 shall apply for 2Rx RedCap UEs.

## A.20.2.1.3Inter-frequency SAN Handover from FR1 to FR1 for 1Rx RedCap UE

## A.20.2.1.3.1Test Purpose and Environment

This test is to verify the requirement for Inter-frequency SAN Handover from FR1 to FR1 specified in clause 6.1F.1 for 1Rx RedCap UE.

## A.20.2.1.3.2Test Parameters

Test parameters in clause A.14.2.1.2.2 shall apply except that the supported test configurations are defined in table A.20.2.1.1.2-1, and NR Cell specific test parameters in Table A.20.2.1.1.2-2 replace the corresponding parameters in Table A.14.2.1.2.2-3. Other parameters in Table A.14.2.1.2.2-2 and Table A.14.2.1.2.2-3 shall apply to test configurations 1, 2, 3 and 4.

In the test, the target cell is known by the UE and carries only CD-SSB. The antenna configuration for 1Rx RedCap UE is 1x1.

## A.20.2.1.3.3Test Requirements

Test requirements in clause A.14.2.1.2.3 shall apply for 1Rx RedCap UEs.

## A.20.2.1.4Inter-frequency SAN Handover from FR1 to FR1 for 2Rx RedCap UE

## A.20.2.1.4.1Test Purpose and Environment

This test is to verify the requirement for Inter-frequency SAN Handover from FR1 to FR1 specified in clause 6.1F.1 for 2Rx RedCap UE.

## A.20.2.1.4.2Test Parameters

Test parameters in clause A.20.2.1.3.2 shall apply. The antenna configuration for 2Rx RedCap UE is 1x2.

## A.20.2.1.4.3Test Requirements

Test requirements in clause A.14.2.1.2.3 shall apply for 2Rx RedCap UEs.

## A.20.2.1.5Intra-frequency SAN RACH-less Handover from FR1 to FR1 for 1Rx RedCap UE

## A.20.2.1.5.1Test Purpose and Environment

This test is to verify the requirement for Intra-frequency SAN RACH-less Handover from FR1 to FR1 specified in clause 6.1F.1 for 1Rx RedCap UE.

## A.20.2.1.5.2Test Parameters

Test parameters in clause A.14.2.1.8.2 shall apply except that the supported test configurations are defined in table A.20.2.1.1.2-1, and NR Cell specific test parameters in Table A.20.2.1.1.2-2 replace the corresponding parameters in Table A.14.2.1.8.2-3. Other parameters in Table A.14.2.1.8.2-2 and Table A.14.2.1.8.2-3 shall apply to test configurations 1, 2, 3 and 4.

In the test, the target cell is known by the UE and carries only CD-SSB. The antenna configuration for 1Rx RedCap UE is 1x1.

## A.20.2.1.5.3Test Requirements

Test requirements in clause A.14.2.1.8.3 shall apply for 1Rx RedCap UE.

## A.20.2.1.6Intra-frequency SAN RACH-less Handover from FR1 to FR1 for 2Rx RedCap UE

## A.20.2.1.6.1Test Purpose and Environment

This test is to verify the requirement for Intra-frequency SAN RACH-less Handover from FR1 to FR1 specified in clause 6.1F.1 for 2Rx RedCap UE.

## A.20.2.1.6.2Test Parameters

Test parameters in clause A.20.2.1.5.2 shall apply. The antenna configuration for 2Rx RedCap UE is 1x2.

## A.20.2.1.6.3Test Requirements

Test requirements in clause A.14.2.1.8.3 shall apply for 2Rx RedCap UE.

## A.20.2.1.7Intra-frequency SAN time-based conditional Handover from FR1 to FR1 for 1Rx RedCap UE

## A.20.2.1.7.1Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN time-based conditional handover from FR1 to FR1 specified in clause 6.1F.2 for 1Rx RedCap UE.

## A.20.2.1.7.2Test Parameters

Test parameters in clause A.14.2.1.3.2 shall apply except that the supported test configurations are defined in table A.20.2.1.7.2-1, and NR Cell specific test parameters in Table A.20.2.1.7.2-2 replace the corresponding parameters in Table A.14.2.1.3.2-3. Other parameters in Table A.14.2.1.3.2-2 and Table A.14.2.1.3.2-3 shall apply to test configurations 1, 2, 3 and 4.

In the test, the target cell is known by the UE and carries only CD-SSB.

Table A.20.2.1.7.2-1: Supported test configurations

Table A.20.2.1.7.2-2: Cell specific test parameters for Intra-frequency SAN time-based conditional handover from FR1 to FR1

## A.20.2.1.7.3Test Requirements

Test requirements in clause A.14.2.1.3.3 shall apply for 1Rx RedCap UE.

## A.20.2.1.8Intra-frequency SAN time-based conditional Handover from FR1 to FR1 for 2Rx RedCap UE

## A.20.2.1.8.1Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN time-based conditional handover from FR1 to FR1 specified in clause 6.1F.2 for 2Rx RedCap UE.

## A.20.2.1.8.2Test Parameters

Test parameters in clause A.20.2.1.7.2 shall apply. The antenna configuration for 2Rx RedCap UE is 1x2.

## A.20.2.1.8.3Test Requirements

Test requirements in clause A.14.2.1.3.3 shall apply for 2Rx RedCap UE.

## A.20.2.1.9Inter-frequency SAN distance-based conditional Handover from FR1 to FR1 for 1Rx RedCap UE

## A.20.2.1.9.1Test Purpose and Environment

This test is to verify the requirement for inter-frequency SAN distance-based conditional handover from FR1 to FR1 specified in clause 6.1F.2 for 1Rx RedCap UE.

## A.20.2.1.9.2Test Parameters

Test parameters in clause A.14.2.1.6.2 shall apply except that the supported test configurations are defined in table A.20.2.1.7.2-1, and NR Cell specific test parameters in Table A.20.2.1.7.2-2 replace the corresponding parameters in Table A.14.2.1.6.2-3. Other parameters in Table A.14.2.1.6.2-2 and Table A.14.2.1.6.2-3 shall apply to test configurations 1, 2, 3 and 4.

In the test, the target cell is known by the UE and carries only CD-SSB. The antenna configuration for 1Rx RedCap UE is 1x1.

## A.20.2.1.9.3Test Requirements

Test requirements in clause A.14.2.1.6.3 shall apply for 1Rx RedCap UE.

## A.20.2.1.10Inter-frequency SAN distance-based conditional Handover from FR1 to FR1 for 2Rx RedCap UE

## A.20.2.1.10.1Test Purpose and Environment

This test is to verify the requirement for inter-frequency SAN distance-based conditional handover from FR1 to FR1 specified in clause 6.1F.2 for 2Rx RedCap UE.

## A.20.2.1.10.2Test Parameters

Test parameters in clause A.20.2.1.9.2 shall apply. The antenna configuration for 2Rx RedCap UE is 1x2.

## A.20.2.1.10.3Test Requirements

Test requirements in clause A.14.2.1.6.3 shall apply for 2Rx RedCap UE.

## A.20.2.1.11Intra-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 1Rx RedCap UE

## A.20.2.1.11.1Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN time-based conditional handover without L3 measurement criteria from FR1 to FR1 specified in clause 6.1F.2.3 for 1Rx RedCap UE.

## A.20.2.1.11.2Test Parameters

Test parameters in clause A.14.2.3.2 shall apply except that the supported test configurations are defined in table A.20.2.1.11.2-1. Parameters in Table A.14.2.3.2-2 and Table A.14.2.3.2-3 shall apply to test configurations 1 and 2.

In the test, the target cell is known by the UE and carries only CD-SSB. The antenna configuration for 1Rx RedCap UE is 1x1.

Table A.20.2.1.11.2-1: Supported test configurations

## A.20.2.1.11.3Test Requirements

Test requirements in clause A.14.2.3.3 shall apply for 1Rx RedCap UE.

## A.20.2.1.12Intra-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 2Rx RedCap UE

## A.20.2.1.12.1Test Purpose and Environment

This test is to verify the requirement for intra-frequency SAN time-based conditional handover without L3 measurement criteria from FR1 to FR1 specified in clause 6.1F.2.3 for 2Rx RedCap UE.

## A.20.2.1.12.2Test Parameters

Test parameters in clause A.20.2.1.11.2 shall apply. The antenna configuration for 2Rx RedCap UE is 1x2.

## A.20.2.1.12.3Test Requirements

Test requirements in clause A.14.2.3.3 shall apply for 2Rx RedCap UE.

## A.20.2.1.13Inter-frequency SAN distance-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 1Rx RedCap UE

## A.20.2.1.13.1Test Purpose and Environment

This test is to verify the requirement for inter-frequency SAN distance-based conditional handover without L3 measurement criteria from FR1 to FR1 specified in clause 6.1F.2.3 for 1Rx RedCap UE.

## A.20.2.1.13.2Test Parameters

Test parameters in clause A.14.2.1.6.2 shall apply except that the supported test configurations are defined in table A.20.2.1.11.2-1 and except that general test parameters are defined in A.20.2.1.13.2-1; NR Cell specific test parameters in Table A.20.2.1.13.2-2 replace the corresponding parameters in Table A.14.2.1.6.2-3. Other parameters in Table A.14.2.1.6.2-3 shall apply to test configurations 1 and 2.

The test scenario comprises of 2 NR FDD carriers and one cell on each carrier. Both handover delay and interruption length are tested. The target cell is known by the UE and carries only CD-SSB.

The test consists of two successive time periods, with time durations of T1 and T2 respectively. At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, the UE is configured to measure inter-frequency neighbour cell with Gap pattern ID gp0. The RRC message implying distance-based handover to Cell 2 with Event D1 shall be sent to UE, at a time earlier than TRRC (10 ms) before the beginning of T2.

Starting T2, Cell 2 becomes detectable and after 11670 ms of T2, location condition event condEventD1-r17 is fulfilled.

Table A.20.2.1.13.2-1: General test parameters for Inter-frequency SAN distance-based conditional handover without L3 measurement criteria from FR1 to FR1

Table A.20.2.1.13.2-2: Cell specific test parameters for Inter-frequency SAN distance-based conditional handover without L3 measurement criteria from FR1 to FR1

## A.20.2.1.13.3Test Requirements

Test requirements in clause A.14.2.1.6.3 shall apply for 1Rx RedCap UE.

## A.20.2.1.14Inter-frequency SAN distance-based conditional Handover without L3 measurement criteria from FR1 to FR1 for 2Rx RedCap UE

## A.20.2.1.14.1Test Purpose and Environment

This test is to verify the requirement for inter-frequency SAN distance-based conditional handover without L3 measurement criteria from FR1 to FR1 specified in clause 6.1F.2.3 for 2Rx RedCap UE.

## A.20.2.1.14.2Test Parameters

Test parameters in clause A.20.2.1.Y7.2 shall apply. The antenna configuration for 2Rx RedCap UE is 1x2.

## A.20.2.1.14.3Test Requirements

Test requirements in clause A.14.2.1.6.3 shall apply for 2Rx RedCap UE.

## A.20.2.2RRC Connection Mobility Control

## A.20.2.2.1SA: RRC Re-establishment for SAN

## A.20.2.2.1.1Intra-frequency RRC Re-establishment in FR1 for 1 Rx RedCap UE

A.20.2.2.1.1.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR1 with known target cell is within the specified limits. These tests will verify the requirements in clause 6.2E.1.

The test parameters are given in table A.20.2.2.1.1.1-1, table A.20.2.2.1.1.1-2 and table A.20.2.2.1.1.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.2.2.1.1.1-1: Supported test configurations

Table A.20.2.2.1.1.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR1 for 1 Rx RedCap UE

Table A.20.2.2.1.1.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR1

A.20.2.2.1.1.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to a known NR intra frequency cell shall be less than 1.6 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 1

Tidentify_intra_NR = 200 ms

TSI = 1280 ms, provided that SIB1 and SIB19 are scheduled with 20 ms period; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1545 ms, allow 1.6 s in the test case.

## A.20.2.2.1.2Intra-frequency RRC Re-establishment in FR1 for 2 Rx RedCap UE

A.20.2.2.1.2.1Test Purpose and Environment

The purpose is to verify that the NR intra-frequency RRC re-establishment delay in FR1 with known target cell is within the specified limits. These tests will verify the requirements in clause 6.2E.1.

The test parameters are given in table A.20.2.2.1.2.1-1, table A.20.2.2.1.2.1-2 and table A.20.2.2.1.2.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, is deactivated. The time period T3 starts after the occurrence of the radio link failure.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.2.2.1.2.1-1: Supported test configurations

Table A.20.2.2.1.2.1-2: General test parameters for NR intra-frequency RRC Re-establishment test case in FR1 for 2 Rx RedCap UE

Table A.20.2.2.1.2.1-3: Cell specific test parameters for NR intra-frequency RRC Re-establishment test case in FR1 for 2 Rx RedCap UE

A.20.2.2.1.2.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to a known NR intra frequency cell shall be less than 1.6 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 1

Tidentify_intra_NR = 200 ms

TSI = 1280 ms, provided that SIB1 and SIB19 are scheduled with 20 ms period; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target intra-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 1545 ms, allow 1.6 s in the test case.

## A.20.2.2.1.3Inter-frequency RRC Re-establishment in FR1 for 1 Rx RedCap UE

A.20.2.2.1.3.1Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR1 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2E.1.

The test parameters are given in table A.20.2.2.1.3.1-1, table A.20.2.2.1.3.1-2 and table A.20.2.2.1.3.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.2.2.1.3.1-1: Supported test configurations

Table A.20.2.2.1.3.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1 for 1 Rx RedCap UE

Table A.20.2.2.1.3.1-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1 for 1 Rx RedCap UE

A.20.2.2.1.3.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell shall be less than 3 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 2

Tidentify_intra_NR = 800 ms

Tidentify_inter_NR = 800 ms

TSI = 1280 ms, provided that SIB1 and SIB19 are scheduled with 20 ms period; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 2945 ms, allow 3 s in the test case.

## A.20.2.2.1.4Inter-frequency RRC Re-establishment in FR1 for 2 Rx RedCap UE

A.20.2.2.1.4.1Test Purpose and Environment

The purpose is to verify that the NR inter-frequency RRC re-establishment delay in FR1 without known target cell is within the specified limits. These tests will verify the requirements in clause 6.2E.1.

The test parameters are given in table A.20.2.2.1.4.1-1, table A.20.2.2.1.4.1-2 and table A.20.2.2.1.4.1-3 below. The test consists of 3 successive time periods, with time duration of T1, T2 and T3 respectively. At the start of time period T2, Cell 1, which is the active cell, becomes inactive. The time period T3 starts after the occurrence of the radio link failure. During T1, the UE shall be configured with the carrier frequency of Cell 2 (with RF Channel Number #2) to ensure that the UE has the context of the carrier frequency of Cell 2 by the end of T1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.2.2.1.4.1-1: Supported test configurations

Table A.20.2.2.1.4.1-2: General test parameters for NR inter-frequency RRC Re-establishment test case in FR1 for 2 Rx RedCap UE

Table A.20.2.2.1.4-3: Cell specific test parameters for NR inter-frequency RRC Re-establishment test case in FR1 for 2 Rx RedCap UE

A.20.2.2.1.4.2Test Requirements

The RRC re-establishment delay is defined as the time from the start of time period T3, to the moment when the UE starts to send PRACH preambles to Cell 2 for sending the RRCReestablishmentRequest message to Cell 2.

The RRC re-establishment delay to an unknown NR inter frequency cell shall be less than 3 s.

The rate of correct RRC re-establishments observed during repeated tests shall be at least 90 %.

NOTE:The RRC re-establishment delay in the test is derived from the following expression:

Tre-establish_delay= TUL_grant + TUE_re-establish_delay.

Where:

TUL_grant = It is the time required to acquire and process uplink grant from the target cell. The PRACH reception at the system simulator is used as a trigger for the completion of the test; hence TUL_grant is not used.

TUE_re-establish_delay=50 ms+Tidentify_intra_NR+i=1Nfreq-1Tidentify_inter_NR,i+TSI-NR+TPRACH

Nfreq = 2

Tidentify_intra_NR = 800 ms

Tidentify_inter_NR = 800 ms

TSI = 1280 ms, provided that SIB1 and SIB19 are scheduled with 20 ms period; it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target inter-frequency NR cell.

TPRACH = 15 ms; it is the additional delay caused by the random access procedure.

This gives a total of 2945 ms, allow 3 s in the test case.

## A.20.2.2.2Random Access

## A.20.2.2.2.14-step RA type contention based random access test in FR1 for NR standalone for 1 Rx RedCap UE

A.20.2.2.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2C.2.2 and clause 7.1E.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.20.2.2.2.1.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.20.2.2.2.1.1-2.

Table A.20.2.2.2.1.1-1: Supported test configurations for contention based random access test for satellite access

Table A.20.2.2.2.1.1-2: General test parameters for contention based random access test for satellite access for 1 Rx RedCap UE

A.20.2.2.2.1.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.20.2.2.2.1.2.1Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2C.2.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB+1 dB.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.1.2.2Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.1.2.3No Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.1.2.4Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2C.2.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

A.20.2.2.2.1.2.5Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2C.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.20.2.2.2.1.2.6Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2C.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.20.2.2.2.1.2.7Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2C.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.20.2.2.2.24-step RA type contention based random access test in FR1 for NR standalone for 2 Rx RedCap UE

A.20.2.2.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2C.2.2 and clause 7.1E.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.20.2.2.2.2.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.20.2.2.2.2.1-2.

Table A.20.2.2.2.2.1-1: Supported test configurations for contention based random access test for satellite access

Table A.20.2.2.2.2.1-2: General test parameters for contention based random access test for satellite access

A.20.2.2.2.2.2Test Requirements

Contention based random access is triggered by not explicitly assigning a random access preamble via dedicated signalling in the downlink.

A.20.2.2.2.2.2.1Random Access Preamble Transmission

To test the UE behavior specified in clause 6.2C.2.2.1.1 the System Simulator shall receive the Random Access Preamble which belongs to one of the Random Access Preambles associated with the SSB with index 0, which has SS-RSRP above the configured rsrp-ThresholdSSB.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.2.2.2Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.1.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) and shall transmit the msg3 if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.2.2.3No Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.1.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.2.2.4Receiving an UL grant for msg3 retransmission

To test the UE behavior specified in clause 6.2C.2.2.1.4 the System Simulator shall provide an UL grant for msg3 retransmission following a successful Random Access Response.

The UE shall re-transmit the msg3 upon the reception of an UL grant for msg3 retransmission.

A.20.2.2.2.2.2.5Reception of an Incorrect Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2C.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element not matching the CCCH SDU transmitted in msg3 uplink message.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires unless the received message includes a UE Contention Resolution Identity MAC control element and the UE Contention Resolution Identity included in the MAC control element matches the CCCH SDU transmitted in the uplink message.

A.20.2.2.2.2.2.6Reception of a Correct Message over Temporary C-RNTI

To test the UE behavior specified in clause 6.2C.2.2.1.5 the System Simulator shall send a message addressed to the temporary C-RNTI with a UE Contention Resolution Identity included in the MAC control element matching the CCCH SDU transmitted in the msg3 uplink message.

The UE shall send ACK if the Contention Resolution is successful.

A.20.2.2.2.2.2.7Contention Resolution Timer expiry

To test the UE behavior specified in clause 6.2C.2.2.1.6 the System Simulator shall not send a response to a msg3.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if the Contention Resolution Timer expires.

## A.20.2.2.2.34-step RA type non-contention based random access test in FR1 for NR standalone for 1 Rx RedCap UE

A.20.2.2.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2C.2.2 and clause 7.1E.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.20.2.2.2.3.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.20.2.2.2.3.1-2 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2). Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

Table A.20.2.2.2.3.1-1: Supported test configurations for non-contention based random access test for satellite access

Table A.20.2.2.2.3.1-2: General test parameters for non-contention based random access test satellite access

A.20.2.2.2.3.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.20.2.2.2.3.2.1SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2C.2.2.2.1 for SSB-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.3.2.2CSI-RS-based Random Access Preamble Transmission

In Test-2, to test the UE behavior specified in clause 6.2C.2.2.2.1 for CSI-RS-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with CSI-RSs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the CSI-RS configured.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the CSI-RS configured, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-OccasionList.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.3.2.3Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.3.2.4No Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

## A.20.2.2.2.44-step RA type non-contention based random access test in FR1 for NR standalone for 2 Rx RedCap UE

A.20.2.2.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the behavior of the random access procedure is according to the requirements and that the PRACH power settings and timing are within specified limits. This test will verify the requirements in clause 6.2C.2.2 and clause 7.1E.2 in an AWGN model.

For this test one cell is used and configured as PCell in FR1. Supported test parameters are shown in table A.20.2.2.2.4.1-1. UE capable of SA with PCell in FR1 needs to be tested by using the parameters in table A.20.2.2.2.4.1-2 for SSB-based non-contention based random access test (Test 1) and CSI-RS-based non-contention based random access test (Test 2). Test 2 is only applicable to UE which supports csi-RSRP-AndRSRQ-MeasWithSSB or csi-RSRP-AndRSRQ-MeasWithoutSSB.

Table A.20.2.2.2.4.1-1: Supported test configurations for non-contention based random access test for satellite access

Table A.20.2.2.2.4.1-2: General test parameters for non-contention based random access test satellite access

A.20.2.2.2.4.2Test Requirements

Non-Contention based random access is triggered by explicitly assigning a random access preamble via dedicated signalling in the downlink. In the test, the non-contention based random access procedure is not initialized for Other SI requested from UE or beam failure recovery.

A.20.2.2.2.4.2.1SSB-based Random Access Preamble Transmission

In Test-1, to test the UE behavior specified in clause 6.2C.2.2.2.1 for SSB-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with SSBs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the SSB with index 0.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the SSB with index 0, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-ssb-OccasionMaskIndex.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.4.2.2CSI-RS-based Random Access Preamble Transmission

In Test-2, to test the UE behavior specified in clause 6.2C.2.2.2.1 for CSI-RS-based Random Access Preamble tranmsision, with the contention-free Random Access Resources and the contention-free PRACH occasions associated with CSI-RSs configured, the System Simulator shall receive the Random Access Preamble which has the Preamble Index associated with the CSI-RS configured.

In addition, the System Simulator shall receive the Random Access Preamble on the PRACH occasion which belongs to the PRACH occasions corresponding to the CSI-RS configured, and the selected PRACH occasion shall belongs to the PRACH occassions permitted by the restrictions given by the ra-OccasionList.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.4.2.3Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.2.2 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. In response to the first 4 preambles, the System Simulator shall transmit a Random Access Response not corresponding to the transmitted Random Access Preamble.

The UE may stop monitoring for Random Access Response(s) if the Random Access Response contains a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power if all received Random Access Responses contain Random Access Preamble identifiers that do not match the transmitted Random Access Preamble.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

A.20.2.2.2.4.2.4No Random Access Response Reception

To test the UE behavior specified in clause 6.2C.2.2.2.3 the System Simulator shall transmit a Random Access Response containing a Random Access Preamble identifier corresponding to the transmitted Random Access Preamble after 5 preambles have been received by the System Simulator. The System Simulator shall not respond to the first 4 preambles.

The UE shall again perform the Random Access Resource selection procedure specified in clause 5.1.2 in TS 38.321 [7], and transmit with the calculated PRACH transmission power when the backoff time expires if no Random Access Response is received within the RA Response window configured in RACH-ConfigCommon.

In addition, the power applied to all preambles shall be in accordance with what is specified in clause 6.2C.2.2. The power of the first preamble shall be 22 dBm with an accuracy specified in clause 6.3.4.2 of TS 38.101-1 [18]. The relative power applied to additional preambles shall have an accuracy specified in clause 6.3.4.3 of TS 38.101-1 [18].

The transmit timing of all PRACH transmissions shall be within the accuracy specified in clause 7.1E.2.

## A.20.2.2.3RRC Connection Release with Redirection

## A.20.2.2.3.1Redirection from NR in FR1 to NR in FR1 for 1 Rx RedCap UE

A.20.2.2.3.1.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements specified in clause 6.2E.3.2.1.

A.20.2.2.3.1.2Test Parameters

Supported test configurations are shown in table A.20.2.2.3.1.2-1. The time delay is tested by using the parameters in table A.20.2.2.3.1.2-2, and A.20.2.2.3.1.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2. Cell 1 and Cell 2 belong to different tracking areas.

Table A.20.2.2.3.1.2-1: Redirection from NR to NR test configurations

Table A.20.2.2.3.1.2-2: General test parameters for Redirection from NR to NR test case

Table A.20.2.2.3.1.2-3: Cell specific test parameters for Redirection from NR to NR test case

A.20.2.2.3.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2240 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_NR = TRRC_procedure_delay + Tidentify-NR + TSI-NR + TRACH,

Where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR = 680 ms in the test.

TSI-NR = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH = 170 ms in the test.

This gives a total of 2240 ms.

## A.20.2.2.3.2Redirection from NR in FR1 to NR in FR1 for 2 Rx RedCap UE

A.20.2.2.3.2.1Test Purpose and Environment

This test is to verify RRC connection release with redirection from NR to NR requirements specified in clause 6.2E.3.2.1.

A.20.2.2.3.2.2Test Parameters

Supported test configurations are shown in table A.20.2.2.3.2.2-1. The time delay is tested by using the parameters in table A.20.2.2.3.2.2-2, and A.20.2.2.3.2.2-3.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. The RRCRelease message shall be sent to the UE during period T1 and the start of T2 is the instant when the last TTI containing the RRC message is sent to the UE. Prior to time duration T2, the UE shall not have any timing information of Cell 2. Cell 2 is powered up at the beginning of the T2. Cell 1 and Cell 2 belong to different tracking areas.

Table A.20.2.2.3.2.2-1: Redirection from NR to NR test configurations

Table A.20.2.2.3.2.2-2: General test parameters for Redirection from NR to NR test case

Table A.20.2.2.3.2.2-3: Cell specific test parameters for Redirection from NR to NR test case

A.20.2.2.3.2.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 2240 ms from the beginning of time period T2.

The rate of correct RRC connection release redirection to NR observed during repeated tests shall be at least 90 %.

NOTE:The redirection delay can be expressed as:

Tconnection_release_redirect_NR = TRRC_procedure_delay + Tidentify-NR + TSI-NR + TRACH,

Where:

TRRC_procedure_delay = 110 ms in the test.

Tidentify-NR = 680 ms in the test.

TSI-NR = 1280 ms, it is the time required for receiving all the relevant system information as defined in TS 38.331 for the target NR cell.

TRACH = 170 ms in the test.

This gives a total of 2240 ms.

## A.20.2.3Satellite switching with re-synchronization from FR1 to FR1 for RedCap UE with Satellite Access

## A.20.2.3.1RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 for RedCap UEs with 2Rx RedCap UE

## A.20.2.3.1.1Test Purpose and Environment

This test is to verify the requirement for RACH-based hard satellite switching with re-synchronization from SAN FR1 to SAN FR1 for RedCap UEs, which is specified in clause 6.1F.3. The test is applicable for UEs that support RedCap operation in NTN. The test procedure is applicable for UEs supporting 2 Rx Antenna.

## A.20.2.3.1.2Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells with same PCI as given in table A.20.2.3.1.2-1, A.20.2.3.1.2-2, A.20.2.3.1.2-3 and A.20.2.3.1.2-4. Both satellite switching delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively.

At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, The SIB19 implying t-service-r17 and target satellite configuration SatSwitchWithReSync-r18 shall be sent to UE. The target satellite configuration is in table A.20.2.3.1.2-3.

At the start of time duration T2, Cell 2 becomes detectable and t-service-r17 of Cell 1 is fulfilled.

Table A.20.2.3.1.2-1: Supported test configurations

Table A.20.2.3.1.2-2: General test parameters for RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1

Table A.20.2.3.1.2-3: Target Satellite configuration pattern for hard satellite switching scenario

Table A.20.2.3.1.2-4: Cell specific test parameters for RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 test case

## A.20.2.3.1.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 52.5 ms from the beginning of time period T2.

The rate of correct satellite switch observed during repeated tests shall be at least 90 %.

NOTE:The hard satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tinterrupt, where:

Tinterrupt is defined in clause 6.1C.3.2.2.

Dswitch_unchangedPCI = Tinterrupt = Tsearch + Tprocessing  + T∆ + Tmargin ms

Here: Tprocessing = 10ms; T∆ = 20ms; Tmargin = 2ms. And Tsearch is equal to Tfirst_SSB = 10.5ms, for UEs with 2Rx;

Besides, interruption uncertainty TIU = 20ms in acquiring the first PRACH transmission resource is needed.

This gives a total of 42.5 ms.

## A.20.2.3.2RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 for RedCap UEs with 1 Rx RedCap UE

## A.20.2.3.2.1Test Purpose and Environment

This test is to verify the requirement for RACH-based hard satellite switching with re-synchronization from SAN FR1 to SAN FR1 for RedCap UEs, which is specified in clause 6.1F.3. The test is applicable for UEs that support RedCap operation in NTN. The test procedure is applicable for UEs supporting 1 Rx Antenna.

## A.20.2.3.2.2Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells with same PCI as given in tables A.20.2.3.2.2-1, A.20.2.3.2.2-2, A.20.2.3.2.2-3 and A.20.2.3.2.2-4. Both satellite switching delay and interruption length are tested.

The test consists of two successive time periods, with time durations of T1 and T2 respectively.

At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, The SIB19 implying t-service-r17 and target satellite configuration SatSwitchWithReSync-r18 shall be sent to UE. The target satellite configuration is in table A.20.2.3.2.2-3.

At the start of time duration T2, Cell 2 becomes detectable and t-service-r17 of Cell 1 is fulfilled.

Table A.20.2.3.2.2-1: Supported test configurations

Table A.20.2.3.2.2-2: General test parameters for RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1

Table A.20.2.3.2.2-3: Target Satellite configuration pattern for hard satellite switching scenario

Table A.20.2.3.2.2-4: Cell specific test parameters for RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1 test case

## A.20.2.3.2.3Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 52.5 ms from the beginning of time period T2.

The rate of correct satellite switch observed during repeated tests shall be at least 90 %.

NOTE:The hard satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tinterrupt, where:

Tinterrupt is defined in clause 6.1C.3.2.2.

Dswitch_unchangedPCI = Tinterrupt = Tsearch + Tprocessing  + T∆ + Tmargin ms

Here: Tprocessing = 10ms; T∆ = 20ms; Tmargin = 2ms. And Tsearch is equal to 2*Trs = 40 ms, for UEs with 1 Rx;

Besides, interruption uncertainty TIU = 20ms in acquiring the first PRACH transmission resource is needed.

This gives a total of 72 ms.

## A.20.2.3.3RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1 for 2Rx RedCap UEs

## A.20.2.3.3.1Test Purpose and Environment

This test is to verify the requirement for RACH-less soft satellite switching with re-synchronization from SAN FR1 to SAN FR1 for RedCap UEs which is specified in clause 6.1F.3. The test is applicable for UEs that support RedCap operation in NTN. The test procedure is applicable for UEs supporting 2 Rx Antenna. The requirements to be met depend on the number of supported Rx Antenna at UE side.

## A.20.2.3.3.2Test Parameters

The test scenario comprises of 1 NR FDD carrier and 2 cells with same PCI as given in tables A.20.2.3.3.2-1, A.20.2.3.3.2-2, A.20.2.3.3.2-3 and A.20.2.3.3.2-4. Satellite switching delay is tested.

The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively.

At the start of time duration T1, the UE may not have any timing information of Cell 2. During T1, The SIB19 implying t-service-r17 and target satellite configuration SatSwitchWithReSync-r18 shall be sent to UE. The target satellite configuration is in table A.20.2.3.3.2-3. The configured grant PUSCH transmission in the Cell 2 is configured in the RRC message from Cell 1.

At the start of time duration T2, Cell 2 becomes detectable and t-ServiceStart-r18 is fulfilled.

At the start of time duration T3, t-service-r17 of Cell 1 is fulfilled.

Table A.20.2.3.3.2-1: Supported test configurations

Table A.20.2.3.3.2-2: General test parameters for RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1

Table A.20.2.3.3.2-3: Target Satellite configuration pattern for soft satellite switching scenario

Table A.20.2.3.3.2-4: Cell specific test parameters for Inter frequency SAN handover test case

## A.20.2.3.3.3Test Requirements

The UE shall start to transmit the PUSCH to Cell 2 less than 130 ms from the beginning of time period T2.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The satellite switch with re-sync delay Dswitch_unchangedPCI can be expressed as: Tsoft_switch, where:

Tsoft_switch = max(t-service-t-seviceStart, Tsearch + T∆ + Tmargin) + TIU + Tprocessing  ms

Here: t-service-t-seviceStart= 100ms; Tsearch = 10.5ms; T∆ = 20ms; Tmargin = 2ms, Tprocessing = 10ms.

Besides, interruption uncertainty TIU = 20ms in acquiring the first configured grant based PUSCH transmission resource is needed.

This gives a total of 130 ms.

## A.20.2.3.4RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1 for 1Rx RedCap UEs

## A.20.2.3.4.1Test Purpose and Environment

This test is to verify the requirement for RACH-less soft satellite switching with re-synchronization from SAN FR1 to SAN FR1 for RedCap UEs which is specified in clause 6.1F.3. The test is applicable for UEs that support RedCap operation in NTN. The test procedure is applicable for UEs supporting 1 Rx Antenna. The requirements to be met depend on the number of supported Rx Antenna at UE side.

## A.20.2.3.4.2Test Parameters

The test parameters defined in A.20.2.3.3.2 for 2Rx RedCap UE shall apply for 1Rx RedCap UE.

## A.20.2.3.4.3Test Requirements

The test requirements defined in A.20.2.3.3.3 for 2Rx RedCap UE shall apply for 1Rx RedCap UE.

## A.20.3Timing for RedCap UE with Satellite Access

## A.20.3.1UE transmit timing for RedCap UE with Satellite Access

## A.20.3.1.1NR UE Transmit Timing Test for FR1

## A.20.3.1.1.1Test Purpose and environment

Test purpose and environment in clause A.14.3.1.1.1 apply for RedCap UE except that:

-Table A.14.3.1.1.1-1 is replaced with A.20.3.1.1.1-1, and,

-Table A.14.3.1.1.1-2 is replaced with A.20.3.1.1.1-2.

Table A.20.3.1.1.1-1: Supported test configurations for FR1 PCell

Table A.20.3.1.1.1-2: Cell Specific Test Parameters for UL Transmit Timing test

## A.20.3.1.1.2Test requirements

Test requirements in clause A.14.3.1.1.2 apply for RedCap UEs.

## A.20.3.2Timing advance for RedCap UE with Satellite Access

## A.20.3.2.1SA FR1 timing advance adjustment accuracy for RedCap UE

## A.20.3.2.1.1Test Purpose and Environment

The test purpose and environment in clause A.14.3.2.1.1 shall apply for RedCap UE.

## A.20.3.2.1.2Test Parameters

The test parameters in clause A.14.3.2.1.2 shall apply for RedCap UE except that:

-Table A.14.3.2.1.2-1 is replaced with A.20.3.2.1.2-1, and,

-Table A.14.3.2.1.2-3 is replaced with A.20.3.2.1.2-2, and,

-Table A.14.3.2.1.2-4 is replaced with A.20.3.2.1.2-3,

-Table A.14.3.2.1.2-2 shall apply to configurations 1, 2, 3 and 4.

Table A.20.3.2.1.2-1: Timing advance supported test configurations

Table A.20.3.2.1.2-2: Cell specific test parameters for timing advance

Table A.20.3.2.1.2-3: Sounding Reference Symbol Configuration for timing advance

## A.20.3.2.1.3Test Requirements

Test requirements in clause A.14.3.2.1.3 apply for RedCap UEs with NTN.

## A.20.4Signalling characteristics for RedCap UE with Satellite Access

## A.20.4.1Radio link Monitoring

## A.20.4.1.1Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode for 2Rx RedCap UE with NTN

## A.20.4.1.1.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.1.1 shall apply for 2Rx RedCap UE except that:

-Table A.14.4.1.1.1-1 is replaced with A.20.4.1.1.1-1, and

-Table A.14.4.1.1.1-2, Table A.14.4.1.1.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.4.1.1.1-1: Supported test configurations for FR1 PCell

## A.20.4.1.1.2Test Requirements

The test requirement in clause A.14.4.1.1.2 shall apply for RedCap.

## A.20.4.1.2Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode for 1Rx RedCap UE with NTN

## A.20.4.1.2.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.1.1 shall apply for 1Rx RedCap UE except that:

-Table A.14.4.1.1.1-1 is replaced with A.20.4.1.1.1-1, and

-Table A.14.4.1.1.1-2 is replaced with A.20.4.1.2.1-1, and

-Table A.14.4.1.1.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.4.1.2.1-1: General test parameters for FR1 out-of-sync testing in non-DRX mode for 1Rx RedCap UE

## A.20.4.1.2.2Test Requirements

The test requirement in clause A.14.4.1.1.2 shall apply for 1Rx RedCap UE.

## A.20.4.1.3Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode for 2Rx RedCap UE with NTN

## A.20.4.1.3.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.4.1 shall apply for 2Rx RedCap UE except that:

-Table A.14.4.1.4.1-1 is replaced with A.20.4.1.1.1-1, and

- Table A.14.4.1.4.1-2, Table A.14.4.1.1.1-3 shall apply to configurations 1, 2, 3 and 4.

## A.20.4.1.3.2Test Requirements

The test requirement in clause A.14.4.1.4.2 shall apply for 2Rx RedCap UE.

## A.20.4.1.4Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode for 1Rx RedCap UE with NTN

## A.20.4.1.4.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.4.1 shall apply for 1Rx RedCap UE except that:

-Table A.14.4.1.4.1-1 is replaced with A.20.4.1.1.1-1, and

-Table A.14.4.1.4.1-2 is replaced with A.20.4.1.4.1-1, and

-Table A.14.4.1.1.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.4.1.4.1-1: General test parameters for FR1 in-sync testing in DRX mode

## A.20.4.1.4.2Test Requirements

The test requirement in clause A.14.4.1.4.2 shall apply for 1Rx RedCap UE.

## A.20.4.1.5Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode for 2Rx RedCap UE with NTN

## A.20.4.1.5.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.5.1 shall apply for 2Rx RedCap UE except that:

-Table A.14.4.1.5.1-1 is replaced with A.20.4.1.1.1-1, and

-Table A.14.4.1.5.1-2, Table A.14.4.1.5.1-3 shall apply to configurations 1, 2, 3 and 4.

## A.20.4.1.5.2Test Requirements

The test requirement in clause A.14.4.1.5.2 shall apply for 2Rx RedCap UE.

## A.20.4.1.6Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode for 1Rx RedCap UE with NTN

## A.20.4.1.6.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.5.1 shall apply for 1Rx RedCap UE except that:

-Table A.14.4.1.5.1-1 is replaced with A.20.4.1.1.1-1, and

-Table A.14.4.1.5.1-2 is replaced with A.20.4.1.6.1-1, and

-Table A.14.4.1.5.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.4.1.6.1-1: General test parameters for FR1 PCell for CSI-RS out-of-sync testing in non-DRX mode

## A.20.4.1.6.2Test Requirements

The test requirement in clause A.14.4.1.5.2 shall apply for 1Rx RedCap UE.

## A.20.4.1.7Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode for 2Rx RedCap UE with NTN

## A.20.4.1.7.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.8.1 shall apply for 2Rx RedCap UE except that:

-Table A.14.4.1.8.1-1 is replaced with A.20.4.1.1.1-1, and

-Table A.14.4.1.5.1-2, Table A.14.4.1.5.1-3 shall apply to configurations 1, 2, 3 and 4.

## A.20.4.1.7.2Test Requirements

The test requirement in clause A.14.4.1.8.2 shall apply for 2Rx RedCap UE.

## A.20.4.1.8Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode for 1Rx RedCap UE with NTN

## A.20.4.1.8.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.1.8.1 shall apply for 1Rx RedCap UE except that:

-Table A.14.4.1.8.1-1 is replaced with A.20.4.1.1.1-1, and

-Table A.14.4.1.8.1-2 is replaced with A.20.4.1.8.1-1, and

-Table A.14.4.1.8.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.4.1.8.1-1: General test parameters for FR1 PCell for CSI-RS in-sync testing in non-DRX mode

## A.20.4.1.8.2Test Requirements

The test requirement in clause A.14.4.1.8.2 shall apply for 1Rx RedCap UE with NTN.

## A.20.4.2Beam Failure Detection and Link recovery procedures for RedCap UE with satellite access

## A.20.4.2.1Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode for 1Rx RedCap UE

## A.20.4.2.1.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.1.1 shall apply for 1Rx RedCap UE except that:

-Clause 8.5 is replaced with clause 8.5E

-Table A.14.4.2.1.1-1 is replaced with A.20.4.2.1.1-1

-Table A.14.4.2.1.1-2, Table A.14.4.2.1.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.1.1-2.

Table A.20.4.2.1.1-1: Supported test configurations for FR1 PCell

Table A.20.4.2.1.1-2: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.20.4.2.1.2Test Requirements

The test requirements defined in A.14.4.2.1.2 are reused for 1Rx RedCap UE with NTN.

## A.20.4.2.2Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode for 2Rx RedCap UE

## A.20.4.2.2.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.1.1 shall apply for 2Rx RedCap UE except that:

-Clause 8.5 is replaced with clause 8.5E

-Table A.14.4.2.1.1-1 is replaced with A.20.4.2.1.1-1

-Table A.14.4.2.1.1-2, Table A.14.4.2.1.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.2.1-1.

Table A.20.4.2.2.1-1: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.20.4.2.2.2Test Requirements

The test requirements defined in A.14.4.2.1.2 are reused for 2Rx RedCap UE with NTN.

## A.20.4.2.3Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in DRX mode for 1Rx RedCap UE

## A.20.4.2.3.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.2.1 shall apply for 1Rx RedCap UE except that:

-Clause 8.5 is replaced with clause 8.5E

-Table A.14.4.2.2.1-1 is replaced with A.20.4.2.1.1-1

-Table A.14.4.2.2.1-2, Table A.14.4.2.2.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.3.1-1.

Table A.20.4.2.3.1-1: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

## A.20.4.2.3.2Test Requirements

The test requirements defined in A.14.4.2.2.2 are reused for 1Rx RedCap UE with NTN.

## A.20.4.2.4Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in DRX mode for 2Rx RedCap UE

## A.20.4.2.4.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.2.1 shall apply for 2Rx RedCap UE except that:

-Clause 8.5 is replaced with clause 8.5E,

-Table A.14.4.2.2.1-1 is replaced with A.20.4.2.1.1-1,

-Table A.14.4.2.2.1-2, Table A.14.4.2.2.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.4.1-1.

Table A.20.4.2.4.1-1: General test parameters for FR1 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

## A.20.4.2.4.2Test Requirements

The test requirements defined in A.14.4.2.2.2 are reused for 2Rx RedCap UE with NTN.

## A.20.4.2.5Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in non-DRX mode for 1Rx RedCap UE

## A.20.4.2.5.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.3.1 shall apply for 1Rx RedCap UE except that:

-Clause 8.5 is replaced with clause 8.5E,

-Table A.14.4.2.3.1-1 is replaced with A.20.4.2.1.1-1,

-Table A.14.4.2.3.1-2, Table A.14.4.2.3.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.5.1-1.

Table A.20.4.2.5.1-1: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

## A.20.4.2.5.2Test Requirements

The test requirements defined in A.14.4.2.3.2 are reused for 1Rx RedCap UE with NTN.

## A.20.4.2.6Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in non-DRX mode for 2Rx RedCap UE

## A.20.4.2.6.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.3.1 shall apply for 2Rx RedCap UE except that:

-Clause 8.5 is replaced with clause 8.5E,

-Table A.14.4.2.3.1-1 is replaced with A.20.4.2.1.1-1,

-Table A.14.4.2.3.1-2, Table A.14.4.2.3.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.6.1-1.

Table A.20.4.2.6.1-1: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

## A.20.4.2.6.2Test Requirements

The test requirements defined in A.14.4.2.3.2 are reused for 2Rx RedCap UE with NTN.

## A.20.4.2.7Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in DRX mode for 1Rx RedCap UE

## A.20.4.2.7.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.4.1 shall apply for 1Rx RedCap UE except that:

-Clause 8.5 is replaced with clause 8.5E,

-Table A.14.4.2.4.1-1 is replaced with A.20.4.2.1.1-1,

-Table A.14.4.2.4.1-2, Table A.14.4.2.4.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.7.1-1.

Table A.20.4.2.7.1-1: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

## A.20.4.2.7.2Test Requirements

The test requirements defined in A.14.4.2.4.2 are reused for 1Rx RedCap UE with NTN.

## A.20.4.2.8Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in DRX mode for 2Rx RedCap UE

## A.20.4.2.8.1Test Purpose and Environment

The test purpose and environment in clause A.14.4.2.4.1 shall apply for 2Rx RedCap UE except that:

-Clause 8.5 is replaced with clause 8.5E

-Table A.14.4.2.4.1-1 is replaced with A.20.4.2.1.1-1

-Table A.14.4.2.4.1-2, Table A.14.4.2.4.1-3 shall apply to configurations 1, 2, 3 and 4, except those described in the tables A.20.4.2.8.1-1.

Table A.20.4.2.8.1-1: General test parameters for FR1 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

## A.20.4.2.8.2Test Requirements

The test requirements defined in A.14.4.2.4.2 are reused for 2Rx RedCap UE with NTN.

## A.20.4.3Active BWP switch for RedCap UE with Satellite Access

## A.20.4.3.1DCI-based and Timer-based Active BWP Switch

## A.20.4.3.1.1NR FR1 DL active BWP switch with non-DRX in SA

A.20.4.3.1.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6E.

The supported test configurations are shown in table A.20.4.3.1.1.1-1 below.

The test procedure and environment in clause A.14.4.3.1.1.1 shall apply.

Table A.20.4.3.1.1.1-1: DL BWP switch supported test configurations

A.20.4.3.1.1.2Test Requirements

The test requirements in clause A.14.4.3.1.1.2 shall apply.

## A.20.4.3.2RRC-based Active BWP Switch

## A.20.4.3.2.1NR FR1 DL active BWP switch of Cell with non-DRX in SA

A.20.4.3.2.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6E.

The supported test configurations are shown in table A.20.4.3.2.1.1-1 below.

The test procedure and environment in clause A.14.4.3.2.1.1 shall apply.

Table A.20.4.3.2.1.1-1: DL BWP switch supported test configurations in SA scenario

## A.20.4.3.2.1.2Test Requirements

The test requirements in clause A.14.4.3.1.1.2 shall apply.

## A.20.4.4UE specific CBW change for RedCap UE with Satellite Access

## A.20.4.4.1UE specific CBW change on PCell in FR1 in non-DRX

## A.20.4.4.1.1Test Purpose and Environment

The purpose of this test is to verify the UE specific CBW change delay requirement defined in clause 8.13E.

The supported test configurations are shown in table A.20.4.4.1.1-1. The test scenario comprises of one Cell (Cell 1), which is PCell as given in table A.20.4.4.1.1-2. Cell-specific parameters are specified in table A.20.4.4.1.1-3.

The test procedure in clause A.14.4.4.1.1.1 shall apply.

Table A.20.4.4.1.1-1: Supported test configurations for UE specific CBW change in SA scenario

Table A.20.4.4.1.1-2: General test parameters for UE specific CBW change in SA scenario

Table A.20.4.4.1.1-3: NR Cell specific test parameters for UE specific CBW change in SA scenario

## A.20.4.4.1.2Test Requirements

The test requirements in clause A.14.4.4.1.2 shall apply.

## A.20.4.5Pathloss reference signal switching delay for RedCap UE with Satellite Access

## A.20.4.5.1MAC-CE based pathloss reference signal switch delay

## A.20.4.5.1.1Test Purpose and Environment

The purpose of this test is to verify the MAC-CE based pathloss reference signal switch delay requirement defined in clause 8.14E.

The supported test configurations are shown in table A.20.4.5.1.1-1 below.

The test procedure and environment in clause A.14.4.5.1.1 shall apply.

Table A.20.4.5.1.1-1: MAC-CE based pathloss reference signal switch supported test configurations

## A.20.4.5.1.2Test Requirements

The test requirements in clause A.14.4.5.1.2 shall apply.

## A.20.5Measurement procedure

## A.20.5.1Intra-frequency Measurements

## A.20.5.1.1SA event triggered reporting tests without gap under non-DRX for 1Rx RedCap UE

## A.20.5.1.1.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2E.5.1 and 9.2E.5.2.

## A.20.5.1.1.2Test parameters

The test parameters and procedure in clause A.14.5.1.1.2 apply, except that the supported test configurtions are defined in table A.20.5.1.1.2-1, and NR Cell specific test parameters in Table A.20.5.1.1.2-2 replace the corresponding parameters in Table A.14.5.1.1.2-3. Other parameters in Table A.14.5.1.1.2-2 and Table A.14.5.1.1.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.1.2-1: Supported test configurations

Table A.20.5.1.1.2-2: Cell specific test parameters

## A.20.5.1.1.3Test Requirements

The test requirements in clause A.14.5.1.1.3 apply for this test.

## A.20.5.1.2SA event triggered reporting tests without gap under non-DRX for 2Rx RedCap UE

## A.20.5.1.2.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2E.5.1 and 9.2E.5.2.

## A.20.5.1.2.2Test parameters

The test parameters and procedure in clause A.14.5.1.1.2 apply, except that the supported test configurtions are defined in table A.20.5.1.2.2-1, and NR Cell specific test parameters in Table A.20.5.1.2.2-2 replace the corresponding parameters in Table A.14.5.1.1.2-3. Other parameters in Table A.14.5.1.1.2-2 and Table A.14.5.1.1.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.2.2-1: Supported test configurations

Table A.20.5.1.2.2-2: Cell specific test parameters

## A.20.5.1.2.3Test Requirements

The test requirements in clause A.14.5.1.1.3 apply for this test.

## A.20.5.1.3SA event triggered reporting tests without gap under DRX for 1Rx RedCap UE

## A.20.5.1.3.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2E.5.1 and 9.2E.5.2.

## A.20.5.1.3.2Test parameters

The test parameters and procedure in clause A.14.5.1.2.2 apply, except that the supported test configurtions are defined in table A.20.5.1.3.2-1, and NR Cell specific test parameters in Table A.20.5.1.3.2-2 replace the corresponding parameters in Table A.14.5.1.2.2-3. Other parameters in Table A.14.5.1.2.2-2 and Table A.14.5.1.2.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.3.2-1: Supported test configurations

Table A.20.5.1.3.2-2: Cell specific test parameters

## A.20.5.1.3.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. X=1520 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise X=920.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Y ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. Y=15360 for test configuration 2 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise Y=7680.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.5.1.4SA event triggered reporting tests without gap under DRX for 2Rx RedCap UE

## A.20.5.1.4.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clauses 9.2E.5.1 and 9.2E.5.2.

## A.20.5.1.4.2Test parameters

The test parameters and procedure in clause A.14.5.1.2.2 apply, except that the supported test configurtions are defined in table A.20.5.1.4.2-1, and NR Cell specific test parameters in Table A.20.5.1.4.2-2 replace the corresponding parameters in Table A.14.5.1.2.2-3. Other parameters in Table A.14.5.1.2.2-2 and Table A.14.5.1.2.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.4.2-1: Supported test configurations

Table A.20.5.1.4.2-2: Cell specific test parameters

## A.20.5.1.4.3Test Requirements

The test requirements in clause A.14.5.1.2.3 apply for this test.

## A.20.5.1.5SA event triggered reporting tests without gap under non-DRX with SSB index reading for 1Rx RedCap UE

## A.20.5.1.5.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2E.5.1 and 9.2E.5.2.

## A.20.5.1.5.2Test parameters

The test parameters and procedure in clause A.14.5.1.3.2 apply, except that the supported test configurtions are defined in table A.20.5.1.5.2-1, and NR Cell specific test parameters in Table A.20.5.1.5.2-2 replace the corresponding parameters in Table A.14.5.1.3.2-3. Other parameters in Table A.14.5.1.3.2-2 and Table A.14.5.1.3.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.5.2-1: Supported test configurations

Table A.20.5.1.5.2-2: Cell specific test parameters

## A.20.5.1.5.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X = 1040 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.5.1.6SA event triggered reporting tests without gap under non-DRX with SSB index reading for 2Rx RedCap UE

## A.20.5.1.6.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2E.5.1 and 9.2E.5.2.

## A.20.5.1.6.2Test parameters

The test parameters and procedure in clause A.14.5.1.3.2 apply, except that the supported test configurtions are defined in table A.20.5.1.6.2-1, and NR Cell specific test parameters in Table A.20.5.1.6.2-2 replace the corresponding parameters in Table A.14.5.1.3.2-3. Other parameters in Table A.14.5.1.3.2-2 and Table A.14.5.1.3.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.6.2-1: Supported test configurations

Table A.20.5.1.6.2-2: Cell specific test parameters

## A.20.5.1.6.3Test Requirements

The test requirements in clause A.14.5.1.3.3 apply for this test.

## A.20.5.1.7SA event triggered reporting tests with single measurement gap under non-DRX for satellite access for 1Rx RedCap UE

## A.20.5.1.7.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2E.6.1 and 9.2E.6.2.

## A.20.5.1.7.2Test parameters

The test parameters and procedure in clause A.14.5.1.4.2 apply, except that the supported test configurtions are defined in table A.20.5.1.7.2-1, and NR Cell specific test parameters in Table A.20.5.1.7.2-2 replace the corresponding parameters in Table A.14.5.1.4.2-3. Other parameters in Table A.14.5.1.4.2-2 and Table A.14.5.1.4.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.7.2-1: Supported test configurations

Table A.20.5.1.7.2-2: Cell specific test parameters

## A.20.5.1.7.3Test Requirements

The test requirements in clause A.14.5.1.4.3 apply for this test.

## A.20.5.1.8SA event triggered reporting tests with single measurement gap under non-DRX for satellite access for 2Rx RedCap UE

## A.20.5.1.8.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2E.6.1 and 9.2E.6.2.

## A.20.5.1.8.2Test parameters

The test parameters and procedure in clause A.14.5.1.4.2 apply, except that the supported test configurtions are defined in table A.20.5.1.8.2-1, and NR Cell specific test parameters in Table A.20.5.1.8.2-2 replace the corresponding parameters in Table A.14.5.1.4.2-3. Other parameters in Table A.14.5.1.4.2-2 and Table A.14.5.1.4.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.8.2-1: Supported test configurations

Table A.20.5.1.8.2-2: Cell specific test parameters

## A.20.5.1.8.3Test Requirements

The test requirements in clause A.14.5.1.4.3 apply for this test.

## A.20.5.1.9SA event triggered reporting tests with FNO concurrent gaps under DRX for satellite access for 1Rx RedCap UE

## A.20.5.1.9.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2E.6.1 and 9.2E.6.2.

## A.20.5.1.9.2Test parameters

The test parameters and procedure in clause A.14.5.1.5.2 apply, except that the supported test configurtions are defined in table A.20.5.1.9.2-1, and NR Cell specific test parameters in Table A.20.5.1.9.2-2 replace the corresponding parameters in Table A.14.5.1.5.2-3. Other parameters in Table A.14.5.1.5.2-2 and Table A.14.5.1.5.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.9.2-1: Supported test configurations

Table A.20.5.1.9.2-2: Cell specific test parameters

## A.20.5.1.9.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 7680 ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.5.1.10SA event triggered reporting tests with FNO concurrent gaps under DRX for satellite access for 2Rx RedCap UE

## A.20.5.1.10.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the intra-frequency cell search requirements in clause 9.2E.6.1 and 9.2E.6.2.

## A.20.5.1.10.2Test parameters

The test parameters and procedure in clause A.14.5.1.5.2 apply, except that the supported test configurtions are defined in table A.20.5.1.10.2-1, and NR Cell specific test parameters in Table A.20.5.1.10.2-2 replace the corresponding parameters in Table A.14.5.1.5.2-3. Other parameters in Table A.14.5.1.5.2-2 and Table A.14.5.1.5.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.10.2-1: Supported test configurations

Table A.20.5.1.10.2-2: Cell specific test parameters

## A.20.5.1.10.3Test Requirements

The test requirements in clause A.14.5.1.5.3 apply for this test.

## A.20.5.1.11SA event triggered reporting tests with PPO concurrent gaps under non-DRX with SSB index reading for satellite access for 1Rx RedCap UE

## A.20.5.1.11.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2E.6.1 and 9.2E.6.2.

## A.20.5.1.11.2Test parameters

The test parameters and procedure in clause A.14.5.1.6.2 apply, except that the supported test configurtions are defined in table A.20.5.1.11.2-1, and NR Cell specific test parameters in Table A.20.5.1.11.2-2 replace the corresponding parameters in Table A.14.5.1.6.2-3. Other parameters in Table A.14.5.1.6.2-2 and Table A.14.5.1.6.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.11.2-1: Supported test configurations

Table A.20.5.1.11.2-2: Cell specific test parameters

## A.20.5.1.11.3Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1480 ms from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.5.1.12SA event triggered reporting tests with PPO concurrent gaps under non-DRX with SSB index reading for satellite access for 2Rx RedCap UE

## A.20.5.1.12.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the FDD intra-frequency cell search requirements in clause 9.2E.6.1 and 9.2E.6.2.

## A.20.5.1.12.2Test parameters

The test parameters and procedure in clause A.14.5.1.6.2 apply, except that the supported test configurtions are defined in table A.20.5.1.12.2-1, and NR Cell specific test parameters in Table A.20.5.1.12.2-2 replace the corresponding parameters in Table A.14.5.1.6.2-3. Other parameters in Table A.14.5.1.6.2-2 and Table A.14.5.1.6.2-3 shall apply to test configurations 1, 2, 3 and 4.

Table A.20.5.1.12.2-1: Supported test configurations

Table A.20.5.1.12.2-2: Cell specific test parameters

## A.20.5.1.12.3Test Requirements

The test requirements in clause A.14.5.1.5.3 apply for this test.

## A.20.5.2Inter-frequency Measurements

## A.20.5.2.1SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used with single gap for 2Rx RedCap UE with satellite access

## A.20.5.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.2.1 shall apply for 2Rx RedCap UE except that:

-Table A.14.5.2.2.1-1 is replaced with A.20.5.2.1.1-1, and

-Table A.14.5.2.2.1-2, Table A.14.5.2.2.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.5.2.1.1-1: SA event triggered reporting tests without SSB index reading for FR1-FR1

## A.20.5.2.1.2Test Requirements

The test requirement in clause A.14.5.2.2.2 shall apply for 2Rx RedCap UE with NTN.

## A.20.5.2.2SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used with single gap for 1Rx RedCap UE with satellite access

## A.20.5.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.2.1 shall apply for 1Rx RedCap UE except that:

-Table A.14.5.2.2.1-1 is replaced with A.20.5.2.1.1-1, and

-Table A.14.5.2.2.1-2 is replaced with A.20.5.2.2.1-1, and

-Table A.14.5.2.2.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.5.2.2.1-1: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

## A.20.5.2.2.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1080 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 11520 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 and 2 UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.5.2.3SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used with single gap for 2Rx RedCap UE with satellite access

## A.20.5.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.3.1 shall apply for 2Rx RedCap UE except that:

-Table A.14.5.2.3.1-1 is replaced with A.20.5.2.1.1-1, and

-Table A.14.5.2.3.1-2, Table A.14.5.2.3.1-3 shall apply to configurations 1, 2, 3 and 4.

## A.20.5.2.3.2Test Requirements

The test requirement in clause A.14.5.2.3.2 shall apply for 2Rx RedCap UE with NTN.

## A.20.5.2.4SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used with single gap for 1Rx RedCap UE with satellite access

## A.20.5.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.3.1 shall apply for 1Rx RedCap UE except that:

-Table A.14.5.2.3.1-1 is replaced with A.20.5.2.1.1-1, and

-Table A.14.5.2.3.1-2 is replaced with A.20.5.2.4.1-1, and

-Table A.14.5.2.3.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.5.2.4.1-1: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

## A.20.5.2.4.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1240 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.5.2.5SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in fully non-overlapped for 2Rx RedCap UE with satellite access

## A.20.5.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.4.1 shall apply for 2Rx RedCap UE except that:

-Table A.14.5.2.4.1-1 is replaced with A.20.5.2.1.1-1, and

-Table A.14.5.2.4.1-2, Table A.14.5.2.4.1-3 shall apply to configurations 1, 2, 3 and 4.

## A.20.5.2.5.2Test Requirements

The test requirement in clause A.14.5.2.4.2 shall apply for 2Rx RedCap UE with NTN.

## A.20.5.2.6SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in fully non-overlapped for 1Rx RedCap UE with satellite access

## A.20.5.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.4.1 shall apply for 1Rx RedCap UE except that:

-Table A.14.5.2.4.1-1 is replaced with A.20.5.2.1.1-1, and

-Table A.14.5.2.4.1-2 is replaced with A.20.5.2.6.1-1, and

-Table A.14.5.2.4.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.5.2.6.1-1: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

## A.20.5.2.6.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1000 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 1 UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.5.2.7SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in partially partial overalpping for 2Rx RedCap UE with satellite access

## A.20.5.2.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.6.1 shall apply for 2Rx RedCap UE except that:

-Table A.14.5.2.6.1-1 is replaced with A.20.5.2.1.1-1, and

-Table A.14.5.2.6.1-2, Table A.14.5.2.6.1-3 shall apply to configurations 1, 2, 3 and 4.

## A.20.5.2.7.2Test Requirements

The test requirement in clause A.14.5.2.6.2 shall apply for RedCap.

## A.20.5.2.8SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in partially partial overalpping for 1Rx RedCap UE with satellite access

## A.20.5.2.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the SA inter-frequency NR cell search requirements in clauses 9.3E.4 and 9.3E.5.

The test environment in clause A.14.5.2.6.1 shall apply for 1Rx RedCap UE except that:

-Table A.14.5.2.6.1-1 is replaced with A.20.5.2.1.1-1, and

-Table A.14.5.2.6.1-2 is replaced with A.20.5.2.8.1-1, and

-Table A.14.5.2.6.1-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.5.2.8.1-1: General test parameters for SA inter-frequency event triggered reporting for FR1 without SSB time index detection

## A.20.5.2.8.2Test Requirements

The UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than 1440 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.5.2.9Event triggered reporting test without gap under non-DRX for 2Rx RedCap UE with satellite access

## A.20.5.2.9.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the inter-frequency cell search requirements in clause 9.3E.7.

## A.20.5.2.9.2Test parameters

The test environment in clause A.14.5.2.7.1 shall apply for 2Rx RedCap UE except that:

-Table A.14.5.2.7.2-1 is replaced with A.20.5.2.1.1-1, and

-Table A.14.5.2.7.2-2, Table A.14.5.2.7.2-3 shall apply to configurations 1, 2, 3 and 4.

## A.20.5.2.9.3Test Requirements

The test requirement in clause A.14.5.2.7.3 shall apply for 2Rx RedCap UE with NTN.

## A.20.5.2.10Event triggered reporting test without gap under non-DRX for 1Rx RedCap UE with satellite access

## A.20.5.2.10.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the inter-frequency cell search requirements in clause 9.3E.7.

## A.20.5.2.10.2Test parameters

The test environment in clause A.14.5.2.7.2 shall apply for 1Rx RedCap UE except that:

-Table A.14.5.2.7.2-1 is replaced with A.20.5.2.1.1-1, and

-Table A.14.5.2.7.2-2, Table A.14.5.2.7.2-3 shall apply to configurations 1, 2, 3 and 4.

## A.20.5.2.10.3Test Requirements

The test requirement in clause A.14.5.2.7.3 shall apply for 1Rx RedCap UE with NTN.

## A.20.5.2.11Event triggered reporting tests without gap under DRX for 2Rx RedCap UE with satellite access

## A.20.5.2.11.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the inter-frequency cell search requirements in clauses 9.3E.7.

## A.20.5.2.11.2Test parameters

The test environment in clause A.14.5.2.8.2 shall apply for 2Rx RedCap UE except that:

-Table A.14.5.2.8.2-1 is replaced with A.20.5.2.1.1-1, and

-Table A.14.5.2.8.2-2, Table A.14.5.2.8.2-3 shall apply to configurations 1, 2, 3 and 4.

## A.20.5.2.11.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. X=1280 for test configuration 2,4 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise X=920.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Y ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. Y=12800 for test configuration 2, 4 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise Y=6400.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.5.2.12Event triggered reporting tests without gap under DRX for 1Rx RedCap UE with satellite access

## A.20.5.2.12.1Test purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the inter-frequency cell search requirements in clause 9.3E.7.

## A.20.5.2.12.2Test parameters

The test environment in clause A.14.5.2.8.2 shall apply for 1Rx RedCap UE except that:

-Table A.14.5.2.8.2-1 is replaced with A.20.5.2.1.1-1, and

-Table A.14.5.2.8.2-2 is replaced with A.20.5.2.12.2-1, and

-Table A.14.5.2.8.2-3 shall apply to configurations 1, 2, 3 and 4.

Table A.20.5.2.12.2-1: General test parameters for inter-frequency event triggered reporting without gap for PCell in FR1 with DRX

## A.20.5.2.12.3Test Requirements

In test 1, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than X ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. X=1520 for test configuration 2,4 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise X=920.

In test 2, the UE shall send one Event A3 triggered measurement report, with a measurement reporting delay less than Y ms from the beginning of time period T2. The UE is not required to read the neighbour cell SSB index in this test. Y=15360 for test configuration 2,4 and if UE indicates ‘n1’ for maxNumber-NGSO-SatellitesWithinOneSMTC, otherwise Y=7680.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.5.3L1-RSRP measurement for beam reporting for (e)RedCap UE with Satellite Access

## A.20.5.3.1SSB based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is not used for 1Rx (e)RedCap UE with NTN

## A.20.5.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5E.4.1, with the testing configurations for NR cells served by satellite access node (SAN) in Table A.20.5.3.1.1-1.

Table A.20.5.3.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test for satellite access

## A.20.5.3.1.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.20.5.3.1.2-1 and table A.20.5.3.1.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.20.5.3.1.2-1: General test parameters

Table A.20.5.3.1.2-2: SSB specific test parameters

## A.20.5.3.1.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19F.1.1 and relative accuracy requirement in clause 10.1.19F.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.5.3.2SSB based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is not used for 2Rx (e)RedCap UE with NTN

## A.20.5.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5E.4.1, with the testing configurations for NR cells served by satellite access node (SAN) in table A.20.5.3.2.1-1.

Table A.20.5.3.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test for satellite access

## A.20.5.3.2.2Test parameters

There is one cell in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.20.5.3.2.2-1 and table A.20.5.3.2.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the SSBs and report periodically. The test consists of two successive time periods, with time duration of T1 and T2 respectively. The test has higher layer parameter timeRestrictionForChannelMeasurements configured.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSBs.

Table A.20.5.3.2.2-1: General test parameters

Table A.20.5.3.2.2-2: SSB specific test parameters

## A.20.5.3.2.3Test Requirements

The UE shall send L1-RSRP report every 80 slots. No later than 640 ms plus 80 slots from the beginning of time period T2, UE shall send L1-RSRP report including results of both SSB0 and SSB1 while meeting the absolute accuracy requirement in clause 10.1.19F.1.1 and relative accuracy requirement in clause 10.1.19F.1.2. The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.5.3.3CSI-RS based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is used for 1Rx (e)RedCap UE with NTN

## A.20.5.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5E.4.2, with the testing configurations for NR cells served by satellite access node (SAN)  in table A.20.5.3.3.1-1.

Table A.20.5.3.3.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test for satellite access

## A.20.5.3.3.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.20.5.3.3.2-1 and table A.20.5.3.3.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (0 for Config 1, 2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.20.5.3.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.20.5.3.3.2-1: General test parameters

Table A.20.5.3.3.2-2: CSI-RS specific test parameters

## A.20.5.3.3.3Test Requirements

After 80ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.19F.1.1 and relative accuracy requirement in clause 10.1.19F.1.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.5.3.4CSI-RS based L1-RSRP measurement for (e)RedCap UE with satellite access when DRX is used for 2Rx (e)RedCap UE with NTN

## A.20.5.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of L1-RSRP measurement. This test will partly verify the L1-RSRP measurement requirements in clause 9.5E.4.2, with the testing configurations for NR cells served by satellite access node (SAN) in table A.20.5.3.4.1-1.

Table A.20.5.3.4.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test for satellite access

## A.20.5.3.4.2Test parameters

There is one cells in the test, the FR1 PCell (Cell 1) which is served by satellite access node (SAN). The test parameters for the Cell 1 are given in table A.20.5.3.4.2-1 and table A.20.5.3.4.2-2 below.

In CSI measurement configuration, UE is indicated to perform L1-RSRP measurement on the CSI-RS and report aperiodically. The test consists of a single time period T1, during which the UE is triggered via DCI to report L1-RSRP on aperiodic CSI-RS resources. UE is also configured to measure L1-RSRP based on SSB. After 80 ms from the beginning of the test, the DCI trigger comes in slot n (0 for Config 1,2 and 8 for Config 3) of a frame and UE provides the report back based on the reporting configuration as defined in table A.20.5.3.4.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured to perform RLM and BFD based on the SSBs.

Table A.20.5.3.4.2-1: General test parameters

Table A.20.5.3.4.2-2: CSI-RS specific test parameters

## A.20.5.3.4.3Test Requirements

After 80ms from the beginning of the test, the UE shall send L1-RSRP report at slot 8  from the reception of DCI triggering the L1-RSRP measurement. The L1-RSRP report shall include the results for both CSI-RS#0 and CSI-RS#1 while meeting the absolute accuracy requirement in clause 10.1.19F.1.1 and relative accuracy requirement in clause 10.1.19F.1.2.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.20.6Measurement Performance requirements

## A.20.6.1SS-RSRP for SAN

## A.20.6.1.1SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE

## A.20.6.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clauses 10.1.2D.1.1 and 10.1.2D.1.2 for intra-frequency measurements.

## A.20.6.1.1.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.20.6.1.1.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.20.6.1.1.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.6.1.1.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

Table A.20.6.1.1.2-2: SS-RSRP Intra frequency test parameters

## A.20.6.1.1.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.2D.1.1 and relative requirement in clause 10.1D.2.1.2 for 1Rx (e)RedCap UE.

## A.20.6.1.2SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE

## A.20.6.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clauses 10.1.2D.1.1 and 10.1.2D.1.2 for intra-frequency measurements.

## A.20.6.1.2.2Test parameters

In this set of test cases all cells are on the same carrier frequency. Supported test configurations are shown in table A.20.6.1.2.2-1. Both absolute and relative accuracy of SS-RSRP intra-frequency measurements are tested by using the parameters in A.20.6.1.2.2-2. In all test cases, Cell 1 is the PCell, and Cell 2 is the target cell.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.6.1.2.2-1: SS-RSRP Intra frequency SS-RSRP supported test configurations

Table A.20.6.1.2.2-2: SS-RSRP Intra frequency test parameters

## A.20.6.1.2.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.2D.1.1 and relative requirement in clause 10.1.2D.1.2 for 2Rx (e)RedCap UE.

## A.20.6.1.3SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE

## A.20.6.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clauses 10.1.4D.1.1 and 10.1.4D.1.2 for inter-frequency measurements with the testing configurations for NR cells in table A.20.6.1.3.1-1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.6.1.3.1-1: Applicable NR configurations for FR1 inter-frequency SS-RSRP accuracy test

## A.20.6.1.3.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.20.6.1.3.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.20.6.1.3.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.20.6.1.3.2-1: SS-RSRP inter-frequency test parameters

## A.20.6.1.3.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.4D.1.1 and relative requirement in clause 10.1.4D.1.2 for 1Rx (e)RedCap UE.

## A.20.6.1.4SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE

## A.20.6.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clauses 10.1.4D.1.1 and 10.1.4D.1.2 for inter-frequency measurements with the testing configurations for NR cells in table A.20.6.1.4.1-1.

The UE shall be provided with the valid information about the SAN serving the each cell in the test before the test.

Table A.20.6.1.4.1-1: Applicable NR configurations for FR1 inter-frequency SS-RSRP accuracy test

## A.20.6.1.4.2Test parameters

In this set of test cases there are two cells in the test, PCell (Cell 1) and a FR1 neighbour cell (Cell 2) on a different frequency than the PCell. The test parameters for the Cell 1 and Cell 2 are given in table A.20.6.1.4.2-1 below. Both absolute and relative accuracy of RSRP inter-frequency measurements are tested by using the parameters in table A.20.6.1.4.2-1. The inter-frequency measurements are supported by a measurement gap.

Table A.20.6.1.4.2-1: SS-RSRP inter-frequency test parameters

## A.20.6.1.4.3Test Requirements

The SS-RSRP measurement accuracy for Cell 1 and Cell 2 shall fulfil absolute requirement in clause 10.1.4D.1.1 and relative requirement in clause 10.1.4D.1.2 for 2Rx (e)RedCap UE.

## A.20.6.2SS-RSRQ

## A.20.6.2.1SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 1Rx RedCap UE

## A.20.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 10.1.7D.

## A.20.6.2.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.20.6.2.1.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.20.6.2.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.20.6.2.1.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

Table A.20.6.2.1.2-2: SS-RSRQ Intra frequency test parameters

## A.20.6.2.1.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirement in clause 10.1.7D.1.1 for 1Rx (e)RedCap UE.

## A.20.6.2.2SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 2Rx RedCap UE

## A.20.6.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 10.1.7D.

## A.20.6.2.2.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.20.6.2.2.2-1. The absolute accuracy of SS-RSRQ intra-frequency measurement is tested by using the parameters in table A.20.6.2.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.20.6.2.2.2-1: SS-RSRQ Intra frequency SS-RSRQ supported test configurations

Table A.20.6.2.2.2-2: SS-RSRQ Intra frequency test parameters

## A.20.6.2.2.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil the requirement in clause 10.1.7D.1.1 for 2Rx (e)RedCap UE.

## A.20.6.2.3SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 1Rx RedCap UE

## A.20.6.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 10.1.7D.

## A.20.6.2.3.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.20.6.2.3.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.20.6.2.3.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.20.6.2.3.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

Table A.20.6.2.3.2-2: SS-RSRQ Inter frequency test parameters

## A.20.6.2.3.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil absolute requirement in clause 10.1.9D.1.1 and relative requirement in clause 10.1.9D.1.2 for 1Rx (e)RedCap UE.

## A.20.6.2.4SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access for 2Rx RedCap UE

## A.20.6.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 10.1.7D.

## A.20.6.2.4.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.20.6.2.4.2-1. Both absolute accuracy and relative accuracy requirements of SS-RSRQ inter-frequency measurement are tested by using test parameters in table A.20.6.2.4.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.20.6.2.4.2-1: SS-RSRQ Inter frequency SS-RSRQ supported test configurations

Table A.20.6.2.4.2-2: SS-RSRQ Inter frequency test parameters

## A.20.6.2.4.3Test Requirements

The SS-RSRQ measurement accuracy shall fulfil absolute requirement in clause 10.1.9D.1.1 and relative requirement in clause 10.1.9D.1.2 for 2Rx (e)RedCap UE.

## A.20.6.3SS-SINR

## A.20.6.3.1SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE

## A.20.6.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 10.1.12D.1.1.

## A.20.6.3.1.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.20.6.3.1.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.20.6.3.1.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.20.6.3.1.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

Table A.20.6.3.1.2-2: SS-SINR Intra frequency test parameters

## A.20.6.3.1.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirement in clause 10.1.12D.1.1-1 for 1Rx (e)RedCap UE.

## A.20.6.3.2SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE

## A.20.6.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 10.1.12D.1.1.

## A.20.6.3.2.2Test Parameters

In this test case all cells are on the same carrier frequency. Supported test configurations are shown in table A.20.6.3.2.2-1. The absolute accuracy of SS-SINR intra-frequency measurement is tested by using the parameters in table A.20.6.3.2.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is the target cell.

Table A.20.6.3.2.2-1: SS-SINR Intra frequency SS-SINR supported test configurations

Table A.20.6.3.2.2-2: SS-SINR Intra frequency test parameters

## A.20.6.3.2.3Test Requirements

The SS-SINR measurement accuracy shall fulfil the requirement in clause 10.1.12D.1.1 for 2Rx (e)RedCap UE.

## A.20.6.3.3SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1Rx RedCap UE

## A.20.6.3.3.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clauses 10.1.14D.1.1 and 10.1.14D.1.2.

## A.20.6.3.3.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.20.6.3.3.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.20.6.3.3.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.20.6.3.3.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

Table A.20.6.3.3.2-2: SS-SINR Inter frequency test parameters

## A.20.6.3.3.3Test Requirements

The SS-SINR measurement accuracy shall fulfil absolute requirement in clause 10.1.14D.1.1-1 and relative requirement in clause 10.1.14D.1.2-1 for 1Rx (e)RedCap UE.

## A.20.6.3.4SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx RedCap UE

## A.20.6.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the SS-SINR measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clauses 10.1.14D.1.1 and 10.1.14D.1.2.

## A.20.6.3.4.2Test Parameters

In this test case the two cells (i.e., Cell 1 and Cell 2) are on different carrier frequencies and measurement gaps are provided. Supported test configurations are shown in table A.20.6.3.4.2-1. Both absolute accuracy and relative accuracy requirements of SS-SINR inter-frequency measurement are tested by using test parameters in table A.20.6.3.4.2-2. In all test cases, Cell 1 is the PCell and Cell 2 is target cell.

Table A.20.6.3.4.2-1: SS-SINR Inter frequency SS-SINR supported test configurations

Table A.20.6.3.4.2-2: SS-SINR Inter frequency test parameters

## A.20.6.3.4.3Test Requirements

The SS-SINR measurement accuracy shall fulfil absolute requirement in clause 10.1.14D.1.1 and relative requirement in clause 10.1.14D.1.2 for 2Rx (e)RedCap UE.

## A.20.6.4L1-RSRP measurement for beam reporting

## A.20.6.4.1SSB based L1-RSRP measurement for 1Rx RedCap UE

## A.20.6.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 9.5E.4 and clause 10.1.19F.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.20.6.4.1.1-1.

Table A.20.6.4.1.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.20.6.4.1.2Test parameters

In this set of test cases, there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.20.6.4.1.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.20.6.4.1.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.20.6.4.1.2-1: FR1 SSB based L1-RSRP test parameters

## A.20.6.4.1.3Test Requirements

The L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 1 shall fulfil the requirement in clause 10.1.19F.1 for 1Rx (e)RedCap UE.

## A.20.6.4.2SSB based L1-RSRP measurement for 2Rx RedCap UE

## A.20.6.4.2.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 9.5E.4 and clause 10.1.19F.1 for L1-RSRP measurements based on SSB with the testing configurations for NR cells in table A.20.6.4.2.1-1.

Table A.20.6.4.2.1-1: Applicable NR configurations for FR1 SSB based L1-RSRP test

## A.20.6.4.2.2Test parameters

In this set of test cases, there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.20.6.4.2.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.20.6.4.2.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one SSB resource set with two SSB resources. UE is configured to perform RLM, BFD and L1-RSRP measurement based on the SSB resources 0 and 1.

Table A.20.6.4.2.2-1: FR1 SSB based L1-RSRP test parameters

## A.20.6.4.2.3Test Requirements

The L1-RSRP measurement accuracy for SSB#0 and SSB#1 of Cell 1 shall fulfil the requirement in clause 10.1.19F.1 for 2Rx (e)RedCap UE.

## A.20.6.4.3CSI-RS based L1-RSRP measurement on resource set with repetition off for 1Rx RedCap UE

## A.20.6.4.3.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy for 1Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 9.5E.4 and clause 10.1.19F.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.20.6.4.3.1-1.

Table A.20.6.4.3.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.20.6.4.3.2Test parameters

In this set of test cases, there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.20.6.4.3.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.20.6.4.3.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.20.6.4.3.2-1: FR1 CSI-RS based L1-RSRP test parameters

## A.20.6.4.3.3Test Requirements

The L1-RSRP measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirement in clause 10.1.19F.2 for 1Rx (e)RedCap UE.

## A.20.6.4.4CSI-RS based L1-RSRP measurement on resource set with repetition off for 2Rx RedCap UE

## A.20.6.4.4.1Test Purpose and Environment

The purpose of this test is to verify that the L1-RSRP measurement accuracy for 2Rx RedCap UE with satellite access is within the specified limits. This test will verify the requirements in clause 9.5E.4 and clause 10.1.19F.2 for L1-RSRP measurements based on CSI-RS with the testing configurations for NR cells in table A.20.6.4.4.1-1.

Table A.20.6.4.4.1-1: Applicable NR configurations for FR1 CSI-RS based L1-RSRP test

## A.20.6.4.4.2Test parameters

In this set of test cases, there is one cell in the test, PCell (Cell 1). The test parameters for the Cell 1 are given in table A.20.6.4.4.2-1 below. The absolute and relative accuracy of L1-RSRP measurements are tested by using the parameters in table A.20.6.4.4.2-1.

There is no measurement gap configured in the test. Before the test, UE is configured one CSI-RS resource set with two CSI-RS resources. UE is configured to perform RLM and BFD based on SSB 0 and 1. CSI-RS is not transmitted in the same OFDM symbols as SSB.

Table A.20.6.4.4.2-1: FR1 CSI-RS based L1-RSRP test parameters

## A.20.6.4.4.3Test Requirements

The L1-RSRP measurement accuracy for CSI-RS#0 and CSI-RS#1 of Cell 1 shall fulfil the requirement in clause 10.1.19F.2 for 2Rx (e)RedCap UE.

## A.21NR standalone tests for LP-WUR

## A.21.1RRC_IDLE state mobility

## A.21.1.1UE exits offloading mode to legacy mode with LR using LP-SS signal

## A.21.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE correctly exists from offloading mode to legacy mode based on the evaluation requirement defined in clause 4.8.2.2.3 with LR using LP-SS signal.

## A.21.1.1.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.21.1.1.2-1, A.21.1.1.2-2 and A.21.1.1.2-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

The LP-SS configuration 1 in is A.3.X.1 will be used in the test.

Table A.21.1.1.2-1: Supported test configurations

Table A.21.1.1.2-2: General test parameters for FR1 UE exit from offloading mode to legacy with LP-SS based LR

Table A.21.1.1.2-3: Cell specific test parameters for FR1 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling low mobility criterion

## A.21.1.1.3Test Requirements

The duration for a UE exiting the offloading mode to the legacy mode and performing a cell reselection to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The total delay till to reslect to a newly detectable cell shall be the same or less than 36 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The total delay from a UE exits offloading mode till cell re-selection delay to a newly detectable cell can be expressed as: Tevaluate-LP-WUR-LP-SS + 800ms + Tdetect, NR_Intra + TSI-NR

Where:

Tevaluate-LP-WUR-LP-SSSee Table 4.8.2.3-1 in clause 4.8.2.2.3

800ms is the MR wake up duration

Tdetect, NR_IntraSee table 4.2.2.3-1 in clause 4.2.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 36s from exiting the offloading mode till the cell re-selection delay to a newly detectable cell.

## A.21.1.2UE exits from relaxed measurement mode with LR using PSS/SSS in FR1

## A.21.1.2.1Test Procedure and Environment

The purpose of this test is to verify that the UE correctly exits from relaxation mode to legacy mode based on the evaluation requirements defined in clause 4.8.2.2.2 with LR using PSS/SSS signal.

## A.21.1.2.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.21.1.2.2-1, A.21.1.2.2-2 and A.21.1.2.2-3. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. Furthermore, UE has not registered with network for the tracking area containing Cell 2.

Table A.21.1.2.2-1: Supported test configurations

Table A.21.1.2.2-2: General test parameters for FR1 UE exit from relaxation mode to legacy with PSS/SSS based LR

Table A.21.1.2.2-3: Cell specific test parameters for FR1 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling low mobility criterion

## A.21.1.2.3Test Requirements

The duration for a UE exiting the relaxation mode to the legacy mode and performing a cell reselection to a newly detectable cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a registration procedure for mobility and periodic registration update on Cell 2.

The total delay till to reslect to a newly detectable cell shall be the same or less than 32.64 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The total delay from a UE exits offloading mode till cell re-selection delay to a newly detectable cell can be expressed as: Tevaluate-LP-WUR-PSS/SSS + 800ms + Tdetect, NR_Intra + TSI-NR

Where:

Tevaluate-LP-WUR-PSS/SSSSee Table 4.8.2.2-1 in clause 4.8.2.2.2

800ms is the MR wake up duration

Tdetect, NR_IntraSee table 4.2.2.3-1 in clause 4.2.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 32.64 from exiting the relaxation mode till the cell re-selection delay to a newly detectable cell.

## A.21.1.3UE exits relaxed measurement mode to legacy mode with LR using LP-SS signal

## A.21.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE correctly exists the relaxed measurement mode to legacy mode with LR using LP-SS signal. This test will verify the evaluation requirement for the exit condition of RRM relaxation based on LP-SS for UEs configured with relaxed measurement criterion specified in clause 4.8.2.2.3.

## A.21.1.3.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.21.1.3.2-1, A.21.1.3.2-2 and A.21.1.3.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both Cell 1 and Cell 2 are already identified by the UE prior to the start of the test. Cell 1 and Cell 2 belong to different tracking areas. The LP-SS configuration 2 in A.3.X.2 will be used for LP-SS configuration.

Table A.21.1.3.2-1: Supported test configurations

Table A.21.1.3.2-2: General test parameters for FR1 intra-frequency NR cell re-selection test case for UE fulfilling not-at-cell edge criterion

Table A.21.1.3.2-3: Cell specific test parameters for FR1 intra-frequency NR cell re-selection test case in AWGN for UE fulfilling not-at-cell edge criterion

## A.21.1.3.3Test Requirements

The delay for a UE existing the relaxed measurement mode to the legacy mode and performing cell re-selection to an already detected cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The delay for a UE existing the relaxed measurement mode to the legacy mode and performing cell re-selection to an already detected cell shall be less than 10 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to an already detected cell for UE fulfilling with relaxed measurement criterion can be expressed as: 800ms + Tevaluate-LP-WUR-LP-SS + Tevaluate,NR_Intra + TSI-NR,

Where:

Tevaluate-LP-WUR-LP-SSSee table 4.8.2.3-1 in clause 4.8.2.2.3

Tevaluate,NR_IntraSee table 4.2.2.3-1 in clause 4.2.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a Cell; 1280 ms is assumed in this test case.

This gives a total of 9.6 s, allow 10 s for the cell re-selection delay to an already detected cell for UE fulfilling not-at-cell edge criterion in the test case.

## A.21.1.4UE exit from relaxed measurement mode with LR using PSS/SSS in FR2

## A.21.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE correctly exits from the relaxed measurement mode to legacy mode in FR2 based on the evaluation requirement for the exit condition for PSS/SSS specified in clause 4.8.2.2.2.

## A.21.1.4.2Test Parameters

The test scenario comprises of 1 NR carrier and 2 cells as given in tables A.21.1.4.2-1, A.21.1.4.2-2 and A.21.1.4.2-3. The test consists of two successive time periods, with time duration of T1 and T2 respectively. Both cell 1 and cell 2 are already identified by the UE prior to the start of the test. Cell 1 and cell 2 belong to different tracking areas. During T1 and T2, entry/exit conditions for RRM measurement relaxation is configured but the conditions are met only during T1. UE has not registered with network for the tracking area containing Cell 2.

Table A.21.1.4.2-1: Supported test configurations

Table A.21.1.4.2-2: General test parameters

Table A.21.1.4.2-3: Cell specific test parameters

## A.21.1.4.3Test Requirements

The delay for a UE exiting the relaxed measurement mode to the legacy mode and performing cell re-selection to an already detected cell is defined as the time from the beginning of time period T2, to the moment when the UE camps on Cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Tracking Area Update procedure on Cell 2.

The delay for a UE exiting the relaxed measurement mode to the legacy mode and performing cell re-selection to an already detected cell shall be less than 40 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to an already detected cell for UE fulfilling with relaxed measurement criterion can be expressed as: Tevaluate-LP-WUR-PSS/SSS + Tevaluate,NR_Intra + TSI-NR,

Where:

Tevaluate-LP-WUR-PSS/SSSSee table 4.8.2.2-1 in clause 4.8.2.2.2

Tevaluate,NR_IntraSee table 4.2.2.3-1 in clause 4.2.2.3

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a Cell; 1280 ms is assumed in this test case.

This gives a total of 12.8+25.6+1.28 = 39.68s, allow 40 s for the cell re-selection delay to an already detected cell for UE fulfilling not-at-cell edge criterion in the test case.
