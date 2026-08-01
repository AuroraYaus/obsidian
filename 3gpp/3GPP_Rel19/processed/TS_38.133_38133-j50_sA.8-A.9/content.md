---
type: spec
aliases:
  - 38.133_38133-j50_sA.8-A.9
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.8-A.9/content.md"
---
# TS 38.133 38133-j50_sA.8-A.9

## A.8E-UTRA standalone tests for NR RRM

Editor notes: All NR RRM tests under E-UTRA standalone operations are included in this annex. All EN-DC related NR RRM tests are in A.4 and A.5.

## A.8.1Void

## A.8.2RRC_IDLE state mobility

## A.8.2.1Inter-RAT NR Cell re-selection

## A.8.2.1.1E-UTRA Cell reselection to higher priority NR target Cell in FR1

## A.8.2.1.1.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN to NR inter-RAT cell reselection requirements specified in clause 4.2.2.5.6 in TS 36.133 [15].

The test scenario comprises of 1 E-UTRA cell and 1 NR cell as given in tables A.8.2.1.1.1-1, A.8.2.1.1.1-2, A.8.2.1.1.1-3 and A.8.2.1.1.1-4. The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. E-UTRA cell 1 is already identified by the UE prior to the start of the test. Cell 2 is of higher priority than cell 1.

Table A.8.2.1.1.1-1: Supported test configurations

Table A.8.2.1.1.1-2: General test parameters for E-UTRA cell re-selection FR1 NR cell test case

Table A.8.2.1.1.1-3: Cell specific test parameters for NR cell 2

Table A.8.2.1.1.1-4: Cell specific test parameters for E-UTRA cell 1

## A.8.2.1.1.2Test Requirements

The cell reselection delay to a higher priority NR cell is defined as the time from the beginning of time period T3, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRCSetupRequest message to perform a Registration procedure for mobility and periodic registration updateon cell 2.

The cell re-selection delay to a higher priority cell shall be less than 68 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a higher priority cell can be expressed as: Thigher_priority_search + Tevaluate, NR + TSI-NR, and to a lower priority cell can be expressed as: Tevaluate, EUTRAN+ TSI-EUTRA,

Where:

Thigher_priority_searchSee clause 4.2.2 in TS 36.133 [15]

Tevaluate, NRSee Table 4.2.2.5.6-1 in clause 4.2.2.5.6 in TS 36.133 [15]

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

Tevaluate, EUTRANSee Table 4.2.2.5-1 in clause 4.2.2.5

TSI-EUTRAMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 67.68 s, allow 68 s for the cell re-selection delay to a higher priority NR cell and 7.68 s for the cell re-selection delay to a lower priority cell in the test case, which we allow 8 s.

## A.8.2.1.2E-UTRA Cell reselection to lower priority NR target Cell in FR1 for UE configured with highSpeedInterRAT-NR-r16

## A.8.2.1.2.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN to NR inter-RAT cell reselection requirements specified in clause 4.2.2.5.6 in 36.133 [15].

The test scenario comprises of 1 E-UTRA cell and 1 NR cell as given in tables A.8.2.1.2.1-1, A.8.2.1.2.1-2, A.8.2.1.2.1-3 and A.8.2.1.2.1-4. In SIB of the E-UTRA cell, highSpeedInterRAT-NR-r16 is configured and the carrier of NR cell is configured with highSpeedCarrierNR-r16. The test consists of two time periods, with time duration of T1 and T2 respectively. Both E-UTRA cell 1 and NR cell 2 are already identified by the UE prior to the start of the test. NR cell 2 is of lower priority than E-UTRA cell 1.

Table A.8.2.1.2.1-1: Supported test configurations for UE configured with highSpeedInterRAT-NR-r16

Table A.8.2.1.2.1-2: General test parameters in E-UTRA cell re-selection FR1 NR cell test case for UE configured with highSpeedInterRAT-NR-r16

Table A.8.2.1.2.1-3: Cell specific test parameters for NR cell 2 in E-UTRA cell re-selection FR1 NR cell test case for UE configured with highSpeedInterRAT-NR-r16

Table A.8.2.1.2.1-4: Cell specific test parameters for E-UTRA cell 1 in E-UTRA cell re-selection FR1 NR cell test case for UE configured with highSpeedInterRAT-NR-r16

## A.8.2.1.2.2Test Requirements

The cell reselection delay to a lower priority NR cell is defined as the time from the beginning of time period T1, to the moment when the UE camps on cell 2, and starts to send preambles on the PRACH for sending the RRC CONNECTION REQUEST message to perform a Tracking Area Update procedure on cell 2.

The cell re-selection delay to a lower priority cell shall be less than 3 s.

The rate of correct cell reselections observed during repeated tests shall be at least 90 %.

NOTE:The cell re-selection delay to a lower priority cell can be expressed as: Tevaluate, NR_HST + TSI-NR,

Where:

Tevaluate, NR_HSTSee Table 4.2.2.5.6-2 in clause 4.2.2.5.6 in [15]

TSI-NRMaximum repetition period of relevant system info blocks that needs to be received by the UE to camp on a cell; 1280 ms is assumed in this test case.

This gives a total of 2.24 s, allow 3 s for the cell re-selection delay to a lower priority NR cell.

## A.8.2.2E-UTRA – NR Inter-RAT Early Measruement Reporting

## A.8.2.2.1E-UTRA – NR Early Measurement Reporting for NR in FR1

## A.8.2.2.1.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN to NR inter-RAT Idle mode DC measurement requirements specified in clause 4.9.2.4 in TS 36.133 [15]. This test is also to verify the accuracy requirement for the E-UTRAN to NR inter-RAT Idle mode DC measurement requirements specified in clause 9.11.1A and 9.11.2A in TS 36.133 [15]. Supported test configurations are shown in table A.8.2.2.1.1-1.

Table A.8.2.2.1.1-1: Supported test configurations

The test scenario comprises of 1 E-UTRA cell (Cell 1) and 1 NR cell (Cell 2). The the test parameters and applicability for the E-UTRAN cell are defined in table A.8.2.2.1.1-4. The general test parameters and the cell specific test parameters for the NR cell are specified in table A.8.2.2.1.1-2 and table A.8.2.2.1.1-3, respectively.

The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Prior to the start of the time duration T1, the UE shall be connected to Cell 1. During T1, Cell 2 shall be powered off. At the end of T1, the RRC connection to Cell 1 is released and UE is configured Idle mode DC measurement on the carrier frequency of Cell 2. Time duration T2 starts when the RRC connection is released, and during the T2 UE is in Idle mode. Cell 2 shall be powered on from the beginning of T2. At beginning of T3 the UE is paged for connection setup and requested by the network to send idle mode measurements.

Table A.8.2.2.1.1-2: General test parameters

Table A.8.2.2.1.1-3: Cell specific test parameters for NR cell 2

Table A.8.2.2.1.1-4: Cell specific test parameters for E-UTRA cell 1

## A.8.2.2.1.2Test Requirements

At the beginning of the time-period T2 the connection is released, and UE enters idle mode. During the time period T2 the UE is in Idle mode and Cell 2 is active. The UE shall not perform reselection. The UE shall perform Idle Mode DC measurement according to clause 4.9.2.4 in TS 36.133 [15]. UE shall be able to detect, acqure the SSB index and measure the SS-RSRP and SS-RSRQ from Cell 2 for Idle mode DC measurement during T2.

NOTE:The Idle mode DC measurement period for the test setup can be expressed as: Thigher_priority_search + TSSB_index,NR + Tevaluate, NR.

Where:

Thigher_priority_searchSee clause 4.2.2 in TS 36.133 [15]

TSSB_index,NRSee Table 4.9.2.4-1 in clause 4.9.2.4 in TS 36.133 [15]

Tevaluate, NRSee Table 4.2.2.5.6-1 in clause 4.2.2.5.6 in TS 36.133 [15]

This gives a total of 70.24 s, allow 71 s for the T2.

At the start of T3 the UE is paged for connection setup. During the connection setup the UE is requested to transmit early measurement report. The UE shall send early measurement report to the PCell.

After receiving the requested early measurement report, the test equipment verifies the accuracy of measurement reported for serving Cell 1 and Cell 2 meets the requirements in section 9.1.2B in TS 36.133 [15] and section 9.1.3B, respectively and test ends.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.8.2.2.2E-UTRA – NR Early Measurement Reporting for NR in FR2

## A.8.2.2.2.1Test Purpose and Environment

This test is to verify the requirement for the E-UTRAN to NR inter-RAT Idle mode DC measurement requirements specified in clause 4.9.2.4 in TS 36.133 [15]. This test is also to verify the accuracy requirement for the E-UTRAN to NR inter-RAT Idle mode DC measurement requirements specified in clause 9.11.1A and 9.11.2A in TS 36.133 [15]. Supported test configurations are shown in table A.8.2.2.2.1-1.

Table A.8.2.2.2.1-1: Supported test configurations

The test scenario comprises of 1 E-UTRA cell (Cell 1) and 1 NR cell (Cell 2). The the test parameters and applicability for the E-UTRAN cell are defined in table A.8.2.2.2.1-4. The general test parameters and the cell specific test parameters for the NR cell are speficied in table A.8.2.2.2.1-2 and table A.8.2.2.2.1-3, respectively.

The test consists of three successive time periods, with time duration of T1, T2, and T3 respectively. Prior to the start of the time duration T1, the UE shall be connected to Cell 1. During T1, Cell 2 shall be powered off. At the end of T1, the RRC connection to Cell 1 is released and UE is configured Idle mode DC measurement on the carrier frequency of Cell 2. Time duration T2 starts when the RRC connection is released, and during the T2 UE is in Idle mode. Cell 2 shall be powered on from the beginning of T2. At beginning of T3 the UE is paged for connection setup and requested by the network to send idle mode measurements.

Table A.8.2.2.2.1-2: General test parameters

Table A.8.2.2.2.1-3: Cell specific test parameters for NR cell 2

Table A.8.2.2.2.1-4: Cell specific test parameters for E-UTRA cell 1

## A.8.2.2.2.2Test Requirements

At the beginning of the time-period T2 the connection is released, and UE enters idle mode. During the time period T2 the UE is in Idle mode and Cell 2 is active. The UE shall not perform reselection. The UE shall perform Idle Mode DC measurement according to clause 4.9.2.4 in TS 36.133 [15]. UE shall be able to detect, acqure the SSB index and measure the SS-RSRP and SS-RSRQ from Cell 2 for Idle mode DC measurement during T2.

NOTE:The Idle mode DC measurement period for the test setup can be expressed as: Tdetect, NR.

Where:

Tdetect, NRSee Table 4.2.2.5.6-1 in clause 4.2.2.5.6 in TS 36.133 [15]

This gives a total of 128 s, allow 128 s for the T2.

At the start of T3 the UE is paged for connection setup. During the connection setup the UE is requested to transmit early measurement report. The UE shall send early measurement report to the PCell.

After receiving the requested early measurement report, the test equipment verifies the accuracy of measurement reported for serving Cell 1 and Cell 2 meets the requirements in section 9.1.2B in TS 36.133 [15] and section 9.1.3B, respectively and test ends.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.8.3RRC_CONNECTED state mobility

## A.8.3.1Handover

## A.8.3.1.1E-UTRAN - NR handover in FR1

## A.8.3.1.1.1Test Purpose and Environment

This test shall verify the E-UTRAN to NR FR1 handover requirements as specified in clause 6.1.2.1 specified in clause 5.3.4 in TS 36.133 [15].

The test comprises of one E-UTRA carrier and one NR carrier. There are two cells and one cell on each carrier. Cell 1 is the E-UTRAN and Cell 2 is an inter-RAT NR neighbour cell. The test consists of three successive time periods, with time durations of T1, T2 and T3 respectively. At the start of time duration T1, the UE does not have any timing information of Cell 2. Starting T2, Cell 2 becomes detectable and the UE is expected to detect and send a measurement report. Gap pattern configuration with id #0 as specified in table 8.1.2.1-1 of TS 36.133 [15] is configured before T2 begins to enable inter-RAT frequency monitoring.

A RRC message implying handover shall be sent to the UE during period T2 after the UE has reported Event B2. The start of T3 is the instant when the last TTI containing the RRC message implying handover is sent to the UE. The handover message shall contain Cell 2 as the target cell.

Supported test configurations are shown in table A.8.3.1.1-1. General test parameters are provided in table A.8.3.1.1-2. Cell specific test parameters for Cell 1 and Cell 2 are provided in tables A.8.3.1.1-3 and A.8.3.1.1-4 respectively.

Table A.8.3.1.1-1: Supported test configurations for E-UTRAN inter-RAT NR handover

Table A.8.3.1.1-2: General test parameters for E-UTRAN inter-RAT NR handover

Table A.8.3.1.1-3: Cell specific test parameters for E-UTRAN inter-RAT NR handover (Cell 1)

Table A.8.3.1.1-4: Cell specific test parameters E-UTRAN inter-RAT NR handover (Cell 2)

## A.8.3.1.1.2Test Requirements

The UE shall start to transmit the PRACH to Cell 2 less than 112 ms from the beginning of time period T3.

The rate of correct handovers observed during repeated tests shall be at least 90 %.

NOTE:The handover delay can be expressed as: RRC procedure delay + Tinterrupt, where:

RRC procedure delay = 50 ms and is specified in TS36.133.

Tinterrupt = 62 ms in the test; Tinterrupt is defined in TS36.133 clause 5.3.4.3.

This gives a total of 112 ms.

## A.8.4Measurement procedure

## A.8.4.1E-UTRA – NR Inter-RAT SFTD Measurement Delay

## A.8.4.1.1E-UTRA – NR Inter-RAT SFTD Measurement Delay in non-DRX

## A.8.4.1.1.1Test Purpose and Environment

The purpose of this test is to partly verify that measurement reporting delay for SFTD between E-UTRA PCell and inter-RAT NR neighbour cell in FR1 is within the requirements stated in clauses 8.1.2.4.25 and 8.1.2.4.26 of TS 36.133 [15] for E-UTRA FDD and TDD, respectively, when no measurement gaps are provided and no DRX is configured.

The tests consist of a single time period of duration T1. Two carriers are used in the tests: one E-UTRA carrier with the PCell (Cell 1), and one NR carrier with the NR neighbour cell (Cell 2).

Prior to the start of time duration T1, the UE is connected to Cell 1 and configured to carry out intra-frequency measurements only. The point in time at which the UE receives, at the UE antenna connector(s), a RRC message containing a measurement configuration for SFTD measurements on RF channel 1 defines the start of time duration T1. Following the start of T1 the UE shall detect Cell 2, determine the SFN and frame time difference of Cell 2 relative to Cell 1, and send a measurement report.

The supported test configurations are listed in table A.8.4.1.1.1-1 below. Test parameters and cell-specific parameters for the NR cell are provided in tables A.8.4.1.1.1-2 and A.8.4.1.1.1-3 below, respectively. Cell-specific parameters for the E-UTRA cell are provided in table A.3.7.2.1-1 in clause A.3.7.2.1.

Table A.8.4.1.1.1-1: Applicable E-UTRA and NR configurations for inter-RAT SFTD measurement delay test

Table A.8.4.1.1.1-2: Applicable E-UTRA and NR configurations for inter-RAT SFTD measurement delay test

Table A.8.4.1.1.1-3: Cell specific test parameters for Cell 2 in inter-RAT SFTD measurement delay test

## A.8.4.1.1.2Test Requirements

Following the start of T1, the UE shall detect Cell 2 and determine the relative time difference between Cell 1 and Cell 2. At latest at TRRC_procedure_delay + Tmeasure_SFTD1 after the beginning of time duration T1, the UE shall send a measurement report on SFTD between Cell 1 and Cell 2.

The observed rate of successful SFTD reports in repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2×TTIDCCH longer than the measurement reporting delays above due to TTI insertion uncertainty of the measurement report in DCCH.

## A.8.4.1.2E-UTRA – NR Inter-RAT SFTD Measurement Delay in DRX

## A.8.4.1.2.1Test Purpose and Environment

The purpose of this test is to partly verify that measurement reporting delay for SFTD between E-UTRA PCell and inter-RAT NR neighbour cell in FR1 is within the requirements stated in clauses 8.1.2.4.25 and 8.1.2.4.26 of TS 36.133 [15] for E-UTRA FDD and TDD, respectively, when no measurement gaps are provided and DRX is configured.

The tests consist of a single time period of duration T1. Two carriers are used in the tests: one E-UTRA carrier with the PCell (Cell 1), and one NR carrier with the NR neighbour cell (Cell 2).

Prior to the start of time duration T1, the UE is connected to Cell 1 and configured to carry out intra-frequency measurements only. The point in time at which the UE receives, at the UE antenna connector(s), a RRC message containing a measurement configuration for SFTD measurements on RF channel 1 defines the start of time duration T1. Following the start of T1 the UE shall detect Cell 2, determine the SFN and frame time difference of Cell 2 relative to Cell 1, and send a measurement report.

The supported test configurations are listed in table A.8.4.1.2.1-1 below. Test parameters are provided in tables A.8.4.1.2.1-2 below. Cell-specific parameters for the E-UTRA and NR cells are provided in table A.3.7.2.1-1 in clause A.3.7.2.1, and table A.8.4.1.1.1-3 in clause A.8.4.1.1.1, respectively.

Table A.8.4.1.2.1-1: Applicable E-UTRA and NR configurations for inter-RAT SFTD measurement delay test in DRX

Table A.8.4.1.2.1-2: Applicable E-UTRA and NR configurations for inter-RAT SFTD measurement delay test in DRX

## A.8.4.1.2.2Test Requirements

Following the start of T1, the UE shall detect Cell 2 and determine the relative time difference between Cell 1 and Cell 2. At latest at the earliest DRX activity time following upon  TRRC_procedure_delay + Tmeasure_SFTD1 from the beginning of time duration T1, the UE shall send a measurement report on SFTD between Cell 1 and Cell 2.

The observed rate of successful SFTD reports in repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2×TTIDCCH longer than the measurement reporting delays above due to TTI insertion uncertainty of the measurement report in DCCH.

## A.8.4.2E-UTRA – NR Inter-RAT Measurements

## A.8.4.2.1NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used

## A.8.4.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA cell 1 as PCell on E-UTRA RF channel 1 and NR cell 2 as neighbour cell in FR1 on NR RF channel 1. The test parameters are given in tables A.8.4.2.1.1-1, A.8.4.2.1.1-2, A.8.4.2.1.1-3 and A.8.4.2.1.1-4.

Measurement gap pattern configuration is defined in table A.8.4.2.1.1-2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Table A.8.4.2.1.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

Table A.8.4.2.1.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

Table A.8.4.2.1.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

Table A.8.4.2.1.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

## A.8.4.2.1.2Test Requirements

The UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 920 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.8.4.2.2NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used

## A.8.4.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA cell 1 as PCell on E-UTRA RF channel 1 and NR cell 2 as neighbour cell in FR1 on NR RF channel 1. The test parameters are given in tables A.8.4.2.2.1-1, A.8.4.2.2.1-2, A.8.4.2.2.1-3 and A.8.4.2.2.1-4.

In tests 1 and 2, measurement gap pattern configuration is defined in table A.8.4.2.2.1-2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Table A.8.4.2.2.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

Table A.8.4.2.2.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

Table A.8.4.2.2.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

Table A.8.4.2.2.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

## A.8.4.2.2.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 1080 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 10240 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is not required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.8.4.2.3NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used

## A.8.4.2.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA cell 1 as PCell on E-UTRA RF channel 1 and NR cell 2 as neighbour cell in FR1 on NR RF channel 1.  The test parameters are given in tables A.8.4.2.3.1-1, A.8.4.2.3.1-2, A.8.4.2.3.1-3 and A.8.4.2.3.1-4.

Measurement gap pattern configuration is defined in table A.8.4.2.3.1-2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Table A.8.4.2.3.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

Table A.8.4.2.3.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

Table A.8.4.2.3.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

Table A.8.4.2.3.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

## A.8.4.2.3.2Test Requirements

The UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 1040 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.8.4.2.4NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used

## A.8.4.2.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA cell 1 as PCell on E-UTRA RF channel 1 and NR cell 2 as neighbour cell in FR1 on NR RF channel 1. The test parameters are given in tables A.8.4.2.4.1-1, A.8.4.2.4.1-2, A.8.4.2.4.1-3 and A.8.4.2.4.1-4.

In tests 1 and 2, measurement gap pattern configuration is defined in table A.8.4.2.4.1-2.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Table A.8.4.2.4.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR1

Table A.8.4.2.4.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

Table A.8.4.2.4.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neigbour cell in FR1 without SSB time index detection

Table A.8.4.2.4.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

## A.8.4.2.4.2Test Requirements

In test 1 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 1280 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2 with per-UE gap, the UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 12160 ms from the beginning of time period T2. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.8.4.2.5NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is not used

## A.8.4.2.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA cell 1 as PCell on E-UTRA RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 1. The test parameters are given in tables A.8.4.2.5.1-1, A.8.4.2.5.1-2 and A.8.4.2.5.1-3.

The cell specific test parameters for E-UTRA Cell 1 as PCell are defined in clause A.3.7.2.2.

Measurement gap pattern configuration defined in table A.8.4.2.5.1-2 is provided for a UE that does not support per-FR gap, and no gap pattern (Gap Pattern Id and Measurement gap offset) is configured for a UE capable of per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B1 (Inter RAT neighbour becomes better than threshold) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have timing information of NR cell 2.

Table A.8.4.2.5.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR2 in non-DRX

Table A.8.4.2.5.1-2: General test parameters for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in non-DRX

Table A.8.4.2.5.1-3: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in non-DRX

## A.8.4.2.5.2Test Requirements

The UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D1 ms and D2 ms from the beginning of time period T2 for a UE incapable of per-FR gap and for a UE capable of per-FR gap, respectively. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is not required to report SSB time index.

Table A.8.4.2.5.2-1: Test requirements for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in non-DRX

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.8.4.2.6NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is used

## A.8.4.2.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA cell 1 as PCell on E-UTRA RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 1.  The test parameters are given in tables A.8.4.2.6.1-1, A.8.4.2.6.1-2 and A.8.4.2.6.1-3.

The cell specific test parameters for E-UTRA Cell 1 as PCell are defined in clause A.3.7.2.2.

Measurement gap pattern configuration defined in table A.8.4.2.6.1-2 is provided for a UE that does not support per-FR gap, and no gap pattern (Gap Pattern Id and Measurement gap offset) is configured for a UE capable of per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B1 (Inter RAT neighbour becomes better than threshold) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have timing information of NR cell 2.

Table A.8.4.2.6.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR2 in DRX

Table A.8.4.2.6.1-2: General test parameters for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in DRX

Table A.8.4.2.6.1-3: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in DRX

## A.8.4.2.6.2Test Requirements

In test 1, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D1 ms and D3 ms from the beginning of time period T2 for a UE incapable of per-FR gap and for a UE capable of per-FR gap, respectively. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D2 ms and D4 ms from the beginning of time period T2 for a UE incapable of per-FR gap and for a UE capable of per-FR gap, respectively. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is not required to report SSB time index.

Table A.8.4.2.6.2-1: Test requirements for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in DRX

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.8.4.2.7NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is not used

## A.8.4.2.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA cell 1 as PCell on E-UTRA RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 1. The test parameters are given in tables A.8.4.2.7.1-1, A.8.4.2.7.1-2 and A.8.4.2.7.1-3.

The cell specific test parameters for E-UTRA Cell 1 as PCell are defined in clause A.3.7.2.2.

Measurement gap pattern configuration defined in table A.8.4.2.7.1-2 is provided for a UE that does not support per-FR gap, and no gap pattern (Gap Pattern Id and Measurement gap offset) is configured for a UE capable of per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B1 (Inter RAT neighbour becomes better than threshold) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Table A.8.4.2.7.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR2 in non-DRX

Table A.8.4.2.7.1-2: General test parameters for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in non-DRX

Table A.8.4.2.7.1-3: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in non-DRX

## A.8.4.2.7.2Test Requirements

the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D1 ms and D2 ms from the beginning of time period T2 for a UE incapable of per-FR gap and for a UE capable of per-FR gap, respectively. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

The UE is required to report SSB time index.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

Table A.8.4.2.7.2-1: Test requirements for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in non-DRX

## A.8.4.2.8NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is used

## A.8.4.2.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

In this test, there are two cells: E-UTRA cell 1 as PCell on E-UTRA RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 1. The test parameters are given in tables A.8.4.2.8.1-1, A.8.4.2.8.1-2 and A.8.4.2.8.1-3.

The cell specific test parameters for E-UTRA Cell 1 as PCell are defined in clause A.3.7.2.2.

Measurement gap pattern configuration defined in table A.8.4.2.8.1-2 is provided for a UE that does not support per-FR gap, and no gap pattern (Gap Pattern Id and Measurement gap offset) is configured for a UE capable of per-FR gap.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B1 (Inter RAT neighbour becomes better than threshold) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Table A.8.4.2.8.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR2 in DRX

Table A.8.4.2.8.1-2: General test parameters for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in DRX

Table A.8.4.2.8.1-3: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR2 with SSB time index detection

## A.8.4.2.8.2Test Requirements

In test 1, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D1 ms and D3 ms from the beginning of time period T2 for a UE incapable of per-FR gap and for a UE capable of per-FR gap, respectively. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In test 2, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D2 ms from the beginning of time period T2 for a UE incapable of per-FR gap and for a UE capable of per-FR gap, respectively. The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled. The rate of correct events observed during repeated tests shall be at least 90 %.

In tests 1 and 2, the UE is required to report SSB time index.

Table A.8.4.2.8.2-1: Test requirements for NR inter-RAT event triggered reporting for FR2 with SSB time index detection in DRX

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.8.4.2.9NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection in DRX for UE configured with highSpeedInterRAT-NR-r16

## A.8.4.2.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.21of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.22 of TS 36.133 [15] for E-UTRAN TDD-NR measurements when UE is configured with highSpeedInterRAT-NR-r16.

In this test, there are two cells: E-UTRA cell 1 as PCell on E-UTRA RF channel 1 and NR cell 2 as neighbour cell in FR1 on NR RF channel 1. The test parameters are given in tables A.8.4.2.9.1-1, A.8.4.2.9.1-2, A.8.4.2.9.1-3 and A.8.4.2.9.1-4.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B2 (PCell becomes worse than threshold1 and inter RAT neighbour becomes better than threshold2) [16] is used. In the measurement configuration the UE shall be indicated to report the SSB index of the identified NR cell. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Table A.8.4.2.9.1-1: NR inter-RAT event triggered reporting tests with SSB index reading for FR1 for UE configured with highSpeedInterRAT-NR-r16

Table A.8.4.2.9.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection for UE configured with highSpeedInterRAT-NR-r16

Table A.8.4.2.9.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting with NR neigbour cell in FR1 with SSB time index detection for UE configured with highSpeedInterRAT-NR-r16

Table A.8.4.2.9.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 with SSB time index detection for UE configured with highSpeedInterRAT-NR-r16

## A.8.4.2.9.2Test Requirements

The UE shall send one Event B2 triggered measurement report, with a measurement reporting delay less than 4.8 s from the beginning of time period T2. The UE is required to read the neighbour cell SSB index and report the acquired SSB index in this test.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.8.4.3E-UTRAN - NR Inter-RAT event-triggered without measurement gaps

## A.8.4.3.1NR Inter-RAT event triggered reporting tests for FR2 without MG nor DRX

## A.8.4.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.29 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.30 of TS 36.133 [15] for E-UTRAN TDD-NR measurements, as well as the interruption requriements in clause 7.8.2.22.

In this test, there are two cells: E-UTRA cell 1 as PCell on E-UTRA RF channel 1 and NR cell 2 as neighbour cell in FR2 on NR RF channel 1. The test parameters are given in tables A.8.4.3.1.1-1, A.8.4.3.1.1-2 and A.8.4.3.1.1-3.

The cell specific test parameters for E-UTRA Cell 1 as PCell are defined in clause A.3.7.2.2.

No measurement gap is configured for the test. UE is continuously scheduled in DL in LTE PCell during the test.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B1 (Inter RAT neighbour becomes better than threshold) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have timing information of NR cell 2.

Table A.8.4.3.1.1-1: NR inter-RAT event triggered reporting tests without SSB index reading for FR2 in non-DRX

Table A.8.4.3.1.1-2: General test parameters for NR inter-RAT event triggered reporting for FR2 without MG nor DRX

Table A.8.4.3.1.1-3: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR2 without SSB time index detection in non-DRX

## A.8.4.3.1.2Test Requirements

In the test, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D1 ms from the beginning of time period T2, where D1 = 12.8 s for UE power class 3.

During the test, the interruption ratio (number of interrupted subframes over the number of total subframes) in LTE PCell shall be less than 1.25 %, and each interruption shall not exceed 1 subframe.

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

In the test, the UE is not required to report SSB time index.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.8.4.3.2NR Inter-RAT event triggered reporting tests for FR1 without gaps when DRX is not used

## A.8.4.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE makes correct reporting of an event when performing inter-RAT NR measurements without gaps and with or without interruptions. This test will partly verify the NR inter-RAT cell search requirements in clause 8.1.2.4.29 of TS 36.133 [15] for E-UTRAN FDD-NR measurements and clause 8.1.2.4.30 of TS 36.133 [15] for E-UTRAN TDD-NR measurements.

The purpose of this test is also to verify that the interruption ratio does not exceed the limits for the LTE PCell during the inter-RAT NR measurement without gaps and with interruptions. This test will verify the interruption ratio for LTE PCell in standalone LTE specified in clause 7.8.2.22.

In this test, there are two cells: E-UTRA cell 1 as PCell on E-UTRA RF channel 1 and NR cell 2 as neighbour cell in FR1 on NR RF channel 1. The test parameters are given in tables A.8.4.3.2.1-1, A.8.4.3.2.1-2, A.8.4.3.2.1-3 and A.8.4.3.2.1-4.

The serving frequency should be selected for this test case should be one in which the UE reports UE capabilities interRAT-NeedForGapsNR-r16=FALSE and interRAT-NeedForInterruptionNR-r18=’nogap-interruption’ or interRAT-NeedForInterruptionNR-r18=’nogap-nointerruption’.

No measurement gap is configured for the test. UE is continuously scheduled in DL in LTE PCell during the test.

In the measurement control information, it is indicated to the UE that event-triggered reporting with Event B1 Inter RAT neighbour becomes better than threshold) [16] is used. The test consists of two successive time periods, with time duration of T1, and T2 respectively. During time duration T1, the UE shall not have any timing information of NR cell 2.

Table A.8.4.3.2.1-1: NR inter-RAT event triggered reporting tests without gaps and with interruptions

Table A.8.4.3.2.1-2: General test parameters for NR inter-RAT event triggered reporting for FR1 without gaps and with interruptions

Table A.8.4.3.2.1-3: E-UTRAN PCell specific test parameters for NR inter-RAT event triggered reporting in non-DRX with NR neighbour cell in FR1 without gaps and with interruptions

Table A.8.4.3.2.1-4: NR neighbour cell specific test parameters for NR inter-RAT event triggered reporting for FR1 without SSB time index detection

## A.8.4.3.2.2Test Requirements

The UE shall be continuously scheduled on PCell during the entire length of T1 and T2. During both time durations the interruption ratio should not exceed 2.5 %.

In the test, the UE shall send one Event B1 triggered measurement report, with a measurement reporting delay less than D1 ms from the beginning of time period T2.

D1 = 1280 for a UE that supports interRAT-NeedForInterruptionNR-r18=’nogap-interruption’

D1 = 800 for a UE that supports interRAT-NeedForInterruptionNR-r18=’nogap-nointerruption’

The UE shall not send event triggered measurement reports, as long as the reporting criteria are not fulfilled.

The UE is not required to report SSB time index.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the measurement reporting delays above because of TTI insertion uncertainty of the measurement report in DCCH.

## A.8.5Measurement performance

## A.8.5.1SFTD accuracy

## A.8.5.1.1SFTD accuracy

## A.8.5.1.1.1Test Purpose

The purpose of this set of tests is to verify that the SFTD measurement accuracy is within the specified limits. This test will verify the requirements as specified in clause 9.1.27 in TS 36.133 [15] for inter-RAT FR1 SFTD measurements.

## A.8.5.1.1.2Test Environment

Supported test configurations are shown in table A.8.5.1.1.2-1. In this set of test cases there are two cells on different carriers. Cell 1 is E-UTRAN PCell and Cell 2 is inter-RAT NR FR1 target cell. The test parameters of cell 1 are given in clause A.8.5.1.1.2-2. The test parameters of cell 2 are given in table A.8.5.1.1.2-3. The SFTD between PCell and target cell shall be set by the test equipment to one of the time differences in table A.8.5.1.1.2-4.

Table A.8.5.1.1.2-1: Supported test configurations for SFTD accuracy

Table A.8.5.1.1.2-2: Test parameters for SFTD accuracy (Cell 1)

Table A.8.5.1.1.2-3: Test parameters for SFTD accuracy (Cell 2)

Table A.8.5.1.1.2-4: Timing offsets for SFTD accuracy test

## A.8.5.1.1.3Test Requirements

The SFTD reported by the UE consists of 2 elements, SFN offset and frame boundary offset between PCell and inter-RAT NR target cell. The reported SFTD accuracy shall fulfil the requirement in clause 9.1.27 in TS 36.133 [15].

## A.8.5.2E-UTRA – NR Inter-RAT Measurement Performance requirements

A.8.5.2.1SS-RSRP

## A.8.5.2.1.1E-UTRAN – NR inter-RAT measurements with FR1 target cell

A.8.5.2.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.11.1 in TS 36.133 [15] for inter-RAT FR1 SS-RSRP measurements.

A.8.5.2.1.1.2Test Parameters

Supported test configurations are shown in table A.8.5.2.1.1.2-1. In this test case there are two cells on different carriers. Cell 1 is the E-UTRA cell which specific test parameters for this test case are specified in table A.3.7.2.1-1. Cell 2 is the inter-RAT NR FR1 target cell. The absolute accuracy requirements of SS-RSRP inter-RAT measurement is tested by using test parameters in table A.8.5.2.1.1.2-2.

Table A.8.5.2.1.1.2-1: SS-RSRP Inter-RAT SS-RSRP supported test configurations

Table A.8.5.2.1.1.2-2: SS-RSRP inter-RAT test parameters

A.8.5.2.1.1.3Test Requirements

The SS-RSRP measurement accuracy for Cell 2 shall fulfil the requirement in clause 9.11.1 in TS 36.133 [15].

## A.8.5.2.1.2E-UTRAN – NR inter-RAT measurements with FR2 target cell

## A.8.5.2.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRP measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.11.1 in TS 36.133 [15] for inter-RAT FR2 SS-RSRP measurements.

## A.8.5.2.1.2.2Test Parameters

Supported test configurations are shown in table A.8.5.2.1.2.2-1. In this test case there are two cells on different carriers. Absolute accuracy requirements of SS-RSRP inter-RAT measurement are tested by using test setup in table A.8.5.2.1.2.2-2 and table A.8.5.2.1.2.2-3. In all test cases, Cell 2 is target cell. Cell 1 is the E-UTRA cell which specific test parameters for this test case are specified in table A.3.7.2.1-1.

Table A.8.5.2.1.2.2-1: SS-RSRP Inter-RAT SS-RSRP supported test configurations

Table A.8.5.2.1.2.2-2: SS-RSRP Inter-RAT general test parameters

Table A.8.5.2.1.2.2-3: SS-RSRP Inter-RAT OTA related test parameters

## A.8.5.2.1.2.3Test Requirements

The SS-RSRP measurement accuracy for Cell 2 shall fulfil the requirement in clause 9.11.1 in TS 36.133 [15].

## A.8.5.2.2SS-RSRQ

## A.8.5.2.2.1E-UTRAN – NR inter-RAT measurements with FR1 target cell

A.8.5.2.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.11.2 in TS 36.133 [15] for inter-RAT FR1 SS-RSRQ measurements.

A.8.5.2.2.1.2Test Parameters

Supported test configurations are shown in table A.8.5.2.2.1.2-1. In this test case there are two cells on different carriers. Cell 1 is the E-UTRA cell which specific test parameters for this test case are specified in table A.3.7.2.1-1. Cell 2 is the inter-RAT NR FR1 target cell. The absolute accuracy requirements of SS-RSRP inter-RAT measurement is tested by using test parameters in table A.8.5.2.2.1.2-2.

Table A.8.5.2.2.1.2-1: SS-RSRQ Inter-RAT SS-RSRQ supported test configurations

Table A.8.5.2.2.1.2-2: SS-RSRQ inter-RAT test parameters

A.8.5.2.2.1.3Test Requirements

The SS-RSRQ measurement accuracy for Cell 2 shall fulfil the requirement in clause 9.11.2 in TS 36.133 [15].

## A.8.5.2.2.2E-UTRAN – NR inter-RAT measurements with FR2 target cell

## A.8.5.2.2.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS-RSRQ measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.11.2 in TS 36.133 [15] for inter-RAT FR2 SS-RSRQ measurements.

## A.8.5.2.2.2.2Test Parameters

Supported test configurations are shown in table A.8.5.2.2.2.2-1. In this test case there are two cells on different carriers. Absolute accuracy requirements of SS-RSRQ inter-RAT measurement are tested by using test setup in table A.8.5.2.2.2.2-2 and table A.8.5.2.2.2.2-3. In all test cases, Cell 2 is target cell. Cell 1 is the E-UTRA cell which specific test parameters for this test case are specified in table A.3.7.2.1-1.

Table A.8.5.2.2.2.2-1: SS-RSRQ Inter-RAT SS-RSRQ supported test configurations

Table A.8.5.2.2.2.2-2: SS-RSRQ Inter-RAT general test parameters

Table A.8.5.2.2.2.2-3: SS-RSRQ Inter-RAT OTA related test parameters

## A.8.5.2.2.2.3Test Requirements

The SS-RSRQ measurement accuracy for Cell 2 shall fulfil the requirement in clause 9.11.2 in TS 36.133 [15].

In this test case there are two cells on different carriers and measurement gaps are provided

## A.8.5.2.3SS-SINR

## A.8.5.2.3.1E-UTRAN – NR inter-RAT measurements with FR1 target cell

A.8.5.2.3.1.1Test Purpose and Environment

The purpose of this test is to verify that the SS- SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.11.3 in TS 36.133 [15] for inter-RAT FR1 SS-SINR measurements.

A.8.5.2.3.1.2Test Parameters

Supported test configurations are shown in table A.8.5.2.3.1.2-1. In this test case there are two cells on different carriers. Cell 1 is the E-UTRA cell which specific test parameters for this test case are specified in table A.3.7.2.1-1. Cell 2 is the inter-RAT NR FR1 target cell. The absolute accuracy requirements of SS-RSRP inter-RAT measurement is tested by using test parameters in table A.8.5.2.3.1.2-2.

Table A.8.5.2.3.1.2-1: SS- SINR Inter-RAT SS- SINR supported test configurations

Table A.8.5.2.3.1.2-2: SS-SINR inter-RAT test parameters

A.8.5.2.3.1.3Test Requirements

The SS-SINR measurement accuracy for Cell 2 shall fulfil the requirement in clause 9.11.3 in TS 36.133 [15].

## A.8.5.2.3.2E-UTRAN – NR inter-RAT measurements with FR2 target cell

## A.8.5.2.3.2.1Test Purpose and Environment

The purpose of this test is to verify that the SS- SINR measurement accuracy is within the specified limits. This test will verify the requirements in clause 9.11.3 in TS 36.133 [15] for inter-RAT FR2 SS-SINR measurements.

## A.8.5.2.3.2.2Test Parameters

Supported test configurations are shown in table A.8.5.2.3.2.2-1. In this test case there are two cells on different carriers. Absolute accuracy requirements of SS-SINR inter-RAT measurement are tested by using test setup in table A.8.5.2.3.2.2-2 and A.8.5.2.3.2.2-3. In all test cases, Cell 2 is target cell. Cell 1 is the E-UTRA cell which specific test parameters for this test case are specified in table A.3.7.2.1-1.

Table A.8.5.2.3.2.2-1: SS-SINR Inter-RAT SS-SINR supported test configurations

Table A.8.5.2.3.2.2-2: SS-SINR Inter-RAT general test parameters

Table A.8.5.2.3.2.2-3: SS-SINR Inter-RAT OTA related test parameters

## A.8.5.2.3.2.3Test Requirements

The SS-SINR measurement accuracy for Cell 2 shall fulfil the requirement in clause 9.11.3 in TS 36.133 [15].

## A.9V2X Tests

## A.9.1V2X Tests in FR1

## A.9.1.1Test for V2X UE Transmit Timing

## A.9.1.1.1 Test for GNSS as Synchronization Reference Source

## A.9.1.1.1.1Test Purpose and Environment

The purpose of this test is to verify the UE timing requirements as specified in clause 12.2.2, when the GNSS is used as timing reference. For this test, the UE is triggered by the test loop function to transmit for V2X sidelink communication.

Table A.9.1.1.1.1-1 defines test parameters for UE transmit timing accuracy tests for V2X. There is one GNSS based synchronization source during the test. The test system can emulate and send the GNSS signal to the test UE. The test parameters for GNSS signals are defined in B.4.1.

Table A.9.1.1.1.1-1: V2X Sidelink Test Parameters for UE Transmit Timing Tests for GNSS as Timing Reference

## A.9.1.1.1.2Test requirements

For parameters specified in tables A.9.1.1.1-1, the timing accuracy for V2X sidelink transmission shall be within the limits defined in clause 12.2.2. The timing accuracy is verified by using PSSCH transmissions.

## A.9.1.1.2Test for SyncRef UE as Synchronization Reference Source

## A.9.1.1.2.1Test Purpose and Environment

The purpose of this test is to verify the timing requirements for V2X sidelink transmissions specified in clause 12.2.5, when SyncRef UE is used as timing reference. For this test, the UE is triggered by the test loop function to transmit for V2X sidelink communication.

Table A.9.1.1.2.1-1 defines test parameters for UE transmit timing accuracy tests for V2X sidelink Communication. There is one active SyncRef UE in this test without either serving cell and or GNSS signals. Before the test starts, the UE has been synchronized to the SyncRef UE. The transmit timing accuracy is verified by using the transmission timing of PSSCH transmissions.

Table A.9.1.1.2.1-1: General Test Parameters for V2X UE Transmit Timing Test for SyncRef UE as Timing Reference

## A.9.1.1.2.2Test requirements

For parameters specified in tables A.9.1.1.2.1-1, the timing accuracy for V2X sidelink transmission shall be within the limits defined in clause 12.2.5. The timing accuracy is verified by using PSSCH transmissions.

## A.9.1.1.3Test for FR1 NR Cell as Synchronization Reference Source

## A.9.1.1.3.1Test Purpose and Environment

The purpose of this test is to verify the timing requirements for V2X sidelink transmissions specified in clause 12.2.3, when the downlink timing of the serving cell (RRC_IDLE) or PCell (RRC_CONNECTED) on a non-V2X sidelink carrier is used as timing reference. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X sidelink communication.

This test is applicable for V2X sidelink communication capable UEs that support NR Uu and sidelink operation.

Table A.9.1.1.3.1-1, A.9.1.1.3.1-2 and A.9.1.1.3.1-3 define test parameters for UE transmit timing accuracy tests for V2X sidelink Communication. There is one active cell (PCell) in this test. The transmit timing accuracy is verified by using the transmission timing of PSSCH transmissions.

Table A.9.1.1.3.1-1: Supported test configurations for FR1 PCell

Table A.9.1.1.3.1-2: V2X Sidelink Test Parameters for V2X UE Transmit Timing Accuracy Test for gNB as Timing Reference

Table A.9.1.1.3.1-3: Cell Test Parameters for V2X UE Transmit Timing Accuracy Test for gNB as Timing Reference

## A.9.1.1.3.2Test requirements

For parameters specified in tables A.9.1.1.3.1-1 A.9.1.1.3.1-2 and A.9.1.1.3.1-3, the timing accuracy for V2X sidelink transmission shall be within the limits defined in clause 12.2.3. The timing accuracy is verified by using PSSCH transmissions.

## A.9.1.2Test for Initiation/Cease of S-SSB Transmission with V2X Sidelink Communication

## A.9.1.2.1Test for FR1 NR Cell as synchronization reference source without gap under non-DRX

## A.9.1.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the V2X UE meets the requirements related to the maximum evaluation time allowed to initiate and cease S-SSB transmissions defined in clause 12.3.1.1, when the reference timing used for sidelink transmissions is a NR serving cell in FR1 on a non-V2X sidelink carrier.

This test is applicable for V2X sidelink communication capable UEs that support NR Uu and sidelink operation.

Supported test configurations for FR1 NR cell are shown in table A.9.1.2.1.1-1.

Table A.9.1.2.1.1-1: Supported Test Configurations for FR1 NR cell as synchronization reference source

The test parameters are given in table A.9.1.2.1.1-2 and table A.9.1.2.1.1-3 below. There is one active cell in this test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively.

During T1, the SS-RSRP of the PCell is above syncTxThreshIC and the UE is not expected to be transmitting S-SSB.

During T2, the SS-RSRP of the PCell is lowered below syncTxThreshIC and the UE is expected to initiate S-SSB transmissions.

During T3, the SS-RSRP of the PCell is increased back to be above syncTxThreshIC and the UE is expected to cease S-SSB transmissions.

Table A.9.1.2.1.1-2: Test Parameters for Initiation/Cease of S-SSB Transmission Test for FR1 NR cell as synchronization reference source

Table A.9.1.2.1.1-3: FR1 NR Cell Specific Test Parameters for Initiation/Cease of S-SSB Transmission Test for FR1 NR cell as synchronization reference source

## A.9.1.2.1.2Test Requirements

The S-SSB transmission initiation delay is defined as the time from the beginning of time period T2 up to the moment when the UE initiates the S-SSB transmission.

The S-SSB transmission initiation delay shall be less than 0.56 s.

The S-SSB transmission cease delay is defined as the time from the beginning of time period T3 up to the moment when the UE ceases the S-SSB transmission.

The S-SSB transmission cease delay shall be less than 0.56 s.

The rate of correct initiation/cease delay of S-SSB transmissions observed during repeated tests shall be at least 90 %.

NOTE:The initiation/cease delay of S-SSB transmissions can be expressed as: Tevaluate,SLSS + S-SSB period,

Where:

Tevaluate,SLSS = 0.4 sec (as specified in clause 12.3.1.1);

S-SSB period = 160 ms.

## A.9.1.2.2Test for SyncRef UE as synchronization reference source

## A.9.1.2.2.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to the evaluation time allowed to initiate and cease S-SSB transmissions defined in clause 12.3.1.4, when the reference timing used for sidelink transmissions is a SyncRef UE.

The test parameters are given in table A.9.1.2.2.1-1 and table A.9.1.2.2.1-2 below. There are neither active cells nor GNSS signals in this test. There is one active SyncRef UE (SyncRef UE 1) in this test. The test system shall emulate SyncRef UE 1 to transmit S-SSB every synchronization period.

Prior to start of test, test system is required to ensure that the V2X UE is synchronized to the SyncRef UE 1 and is transmitting S-SSB as derived from the S-SSB of SyncRef UE 1 as per clause 5.8.5.3 of TS 38.331[2]. For the test configuration, the SLSSID used by the V2X UE shall be 30 with inCoverage IE in MIB-SL set as FALSE. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively.

During T1, the PSBCH-RSRP of SyncRef UE 1 is above syncTxThreshOOC and the UE is not expected to be transmitting S-SSB.

During T2, the PSBCH-RSRP of SyncRef UE 1 is lowered below syncTxThreshOOC and the UE is expected to initiate S-SSB transmissions.

During T3, the PSBCH-RSRP of SyncRef UE 1 is increased back to be above syncTxThreshOOC and the UE is expected to cease S-SSB transmissions.

Table A.9.1.2.2.1-1: Test Parameters for Initiation/Cease of S-SSB Transmission Test for SyncRef UE as synchronization reference source

Table A.9.1.2.2.1-2: SyncRef UE Specific Test Parameters for Initiation/Cease of S-SSB Transmission Test for SyncRef UE as synchronization reference source

## A.9.1.2.2.2Test Requirements

The S-SSB transmission initiation delay is defined as the time from the beginning of time period T2 up to the moment when the UE initiates the S-SSB transmission.

The S-SSB transmission initiation delay shall be less than 0.8 s.

The S-SSB transmission cease delay is defined as the time from the beginning of time period T3 up to the moment when the UE ceases the S-SSB transmission.

The S-SSB transmission cease delay shall be less than 0.8 s.

The rate of correct initiation/cease delay of S-SSB transmissions observed during repeated tests shall be at least 90 %.

NOTE:The initiation/cease delay of S-SSB transmissions can be expressed as: Tevaluate,SLSS + S-SSB period,

Where:

-Tevaluate,SLSS = 0.64 sec (as specified in clause 12.3.1.4);

-S-SSB period = 160 ms.

## A.9.1.2.3Test for SyncRef UE as synchronization reference source when SL-DRX is used

## A.9.1.2.3.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to the evaluation time allowed to initiate and cease S-SSB transmissions defined in clause 12.3.1.4, when the reference timing used for sidelink transmissions is a SyncRef UE and SL-DRX is used.

The test parameters are given in table A.9.1.2.3.1-1 and table A.9.1.2.3.1-2 below. There are neither active cells nor GNSS signals in this test. There is one active SyncRef UE (SyncRef UE 1) in this test. The test system shall emulate SyncRef UE 1 to transmit S-SSB every synchronization period.

Prior to start of test, test system is required to ensure that the V2X UE is synchronized to the SyncRef UE 1 and is transmitting S-SSB as derived from the S-SSB of SyncRef UE 1 as per clause 5.8.5.3 of TS 38.331[2]. For the test configuration, the SLSSID used by the V2X UE shall be 30 with inCoverage IE in MIB-SL set as FALSE. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively.

During T1, the PSBCH-RSRP of SyncRef UE 1 is above syncTxThreshOOC and the UE is not expected to be transmitting S-SSB.

During T2, the PSBCH-RSRP of SyncRef UE 1 is lowered below syncTxThreshOOC and the UE is expected to initiate S-SSB transmissions.

During T3, the PSBCH-RSRP of SyncRef UE 1 is increased back to be above syncTxThreshOOC and the UE is expected to cease S-SSB transmissions.

Table A.9.1.2.3.1-1: Test Parameters for Initiation/Cease of S-SSB Transmission Test for SyncRef UE as synchronization reference source when SL-DRX is used

Table A.9.1.2.3.1-2: SyncRef UE Specific Test Parameters for Initiation/Cease of SLSS Transmission Test for SyncRef UE as synchronization reference source when SL-DRX is used

## A.9.1.2.3.2Test Requirements

The S-SSB transmission initiation delay is defined as the time from the beginning of time period T2 up to the moment when the UE initiates the S-SSB transmission.

The S-SSB transmission initiation delay shall be less than 1.44 s.

The S-SSB transmission cease delay is defined as the time from the beginning of time period T3 up to the moment when the UE ceases the S-SSB transmission.

The S-SSB transmission cease delay shall be less than 1.44 s.

The rate of correct initiation/cease delay of S-SSB transmissions observed during repeated tests shall be at least 90 %.

NOTE:The initiation/cease delay of S-SSB transmissions can be expressed as: Tevaluate,SLSS + S-SSB period,

Where:

-Tevaluate,SLSS = 1.28 sec (as specified in clause 12.3.1.4);

-S-SSB period = 160 ms.

## A.9.1.2.4Test for SyncRef UE as synchronization reference source with CCA

## A.9.1.2.4.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to the evaluation time allowed to initiate and cease S-SSB transmissions defined in clause 12.3A.1.4, when the reference timing used for sidelink transmissions is a SyncRef UE.

The test parameters are given in table A.9.1.2.4.1-1 and table A.9.1.2.4.1-2 below. There are neither active cells nor GNSS signals in this test. There is one active SyncRef UE (SyncRef UE 1) in this test. The test system shall emulate SyncRef UE 1 to transmit S-SSB every synchronization period.

Prior to start of test, test system is required to ensure that the sidelink UE is synchronized to the SyncRef UE 1 and is transmitting S-SSB as derived from the S-SSB of SyncRef UE 1 as per clause 5.8.5.3 of TS 38.331[2]. For the test configuration, the SLSSID used by the sidelink UE shall be 30 with inCoverage IE in MIB-SL set as FALSE. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Two counters, lCCA_2 and lCCA_3, as defined in A.3.26.4.1 will be used with time duration of T2 and T3 respectively.

During T1, the PSBCH-RSRP of SyncRef UE 1 is above syncTxThreshOOC and the UE is not expected to be transmitting S-SSB.

During T2, the PSBCH-RSRP of SyncRef UE 1 is lowered below syncTxThreshOOC and the UE is expected to initiate S-SSB transmissions. The counter lCCA_2 is initialized as 0 at the beginning of T2 and tracks the number of unavailable SSB periods as defined in A.3.26.4.1 until the end of T2.

During T3, the PSBCH-RSRP of SyncRef UE 1 is increased back to be above syncTxThreshOOC and the UE is expected to cease S-SSB transmissions. The counter lCCA_3 is initialized as 0 at the beginning of T3 and tracks the number of unavailable SSB periods as defined in A.3.26.4.1 until the end of T3.

Table A.9.1.2.4.1-1: Test Parameters for Initiation/Cease of S-SSB Transmission Test for SyncRef UE as synchronization reference source with CCA

Table A.9.1.2.4.1-2: SyncRef UE Specific Test Parameters for Initiation/Cease of S-SSB Transmission Test for SyncRef UE as synchronization reference source with CCA

## A.9.1.2.4.2Test Requirements

The S-SSB transmission initiation delay is defined as the time from the beginning of time period T2 up to the moment when the UE initiates the S-SSB transmission.

The S-SSB transmission initiation delay shall be less than Tevaluate,SLSS_CCA + S-SSB period.

The S-SSB transmission cease delay is defined as the time from the beginning of time period T3 up to the moment when the UE ceases the S-SSB transmission.

The S-SSB transmission cease delay shall be less than Tevaluate,SLSS_CCA + S-SSB period.

Where:

-Tevaluate,SLSS_CCA = (4+LSLSS)×S-SSB periods [ms] (as specified in clause 12.3A.1.4) and LSLSS = lCCA_2 or lCCA_3, is the number of unavailable S-SSB period during time duration of T2 and T3 respectively;

-S-SSB period = 160 ms.

The rate of correct initiation/cease delay of S-SSB transmissions observed during repeated tests shall be at least 90 %.

## A.9.1.3 Test for V2X Synchronization Reference Selection/Reselection

## A.9.1.3.1 Test for GNSS configured as the highest priority

## A.9.1.3.1.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to SyncRef UE selection / reselection defined in clause 12.4, when GNSS is configured as the highest priority. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

The test parameters are given in table A.9.1.3.1.1-1and A.9.1.3.1.1-2 below. There are no GNSS signals in this test. There are three active SyncRef UEs (SyncRef UE 1, SyncRef UE 2 and SyncRef UE 3) in this test. The test system shall emulate SyncRef UE 1, SyncRef UE 2 and SyncRef UE 3 to transmit S-SSB every S-SSB period.

The test system can verify the selection / reselection of SyncRef UE by monitoring the SLSS ID used by the V2X UE for its S-SSB transmissions. When the V2X UE is not synchronized to any SyncRef UE, then the V2X UE shall use the SLSS ID belonging to set id_oon. When the V2X UE is synchronized to a SyncRef UE, the V2X UE shall derive its SLSS ID from the SLSS ID of the SyncRef UE as per clause 5.8.5.3 of TS 38.331[2].

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. SyncRef UE 1, SyncRef UE 2 and SyncRef UE 3 are all powered off before starting the test. During T1, SyncRef UE 1 is powered ON and the V2X UE will select SyncRef UE 1 as synchronization source. During T2, SyncRef UE 2 is powered ON and the V2X UE will select SyncRef UE 2 as the synchronization source. During T3, SyncRef UE 3 is powered ON and the V2X UE will reselect to SyncRef UE 3 as the synchronization source.

Table A.9.1.3.1.1-1: Test Parameters for V2X Synchronization Reference Selection/Reselection Tests for GNSS configured as the highest priority

Table A.9.1.3.1.1-2: SyncRef UE Specific Test Parameters for V2X Synchronization Reference Selection/Reselection Tests for GNSS configured as the highest priority

## A.9.1.3.1.2Test Requirements

During T1, SyncRef UE selection delay is defined as the time from the beginning of T1 to the time UE is synchronized to SyncRef UE 1, and changes its S-SSB transmissions timing and SLSS ID to follow SyncRef UE 1 as the synchronization source. For the test configuration, the SLSS ID will be changed to 30 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE selection delay from start of T1.

The SyncRef UE selection delay shall be less than 8.8 sec. The SyncRef UE selection delay can be expressed as:

SyncRef UE selection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + S-SSB period

Where

-Tdetect,SyncRef UE = 8 sec (as specified in sub-clause 12.4)

-Tevaluate,SLSS = 0.64 sec (as specified in sub-clause 12.3)

-S-SSB period = 160 ms

This gives a total of 8.8 seconds.

2) During T2, SyncRef UE reselection delay is defined as the time from the beginning of T2 to the time UE changes its synchronization source from SyncRef UE 1 to SyncRef UE 2 and changes its S-SSB transmissions timing and SLSS ID to follow SyncRef UE 2 as the synchronization source. For the test configuration, the SLSS ID will be changed to 336 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE reselection delay from start of T2.

The SyncRef UE reselection delay shall be less than 8.8 sec. The SyncRef UE reselection delay can be expressed as:

SyncRef UE reselection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + S-SSB period

Where

-Tdetect,SyncRef UE = 8 sec (as specified in sub-clause 12.4)

-Tevaluate,SLSS = 0.64 (as specified in sub-clause 12.3)

-S-SSB period = 160 ms

This gives a total of 8.8 seconds.

3) During T3, SyncRef UE reselection delay is defined as the time from the beginning of T3 to the time UE changes its synchronization source from SyncRef UE 2 to SyncRef UE 3, and changes its S-SSB transmissions timing and SLSS ID to follow SyncRef UE 3 as the synchronization source. For the test configuration, the SLSS ID will still be 0 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE reselection delay from start of T3.

The SyncRef UE reselection delay shall be less than 2.4 sec. The SyncRef UE reselection delay can be expressed as:

SyncRef UE reselection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + S-SSB period

Where

-Tdetect,SyncRef UE = 1.6 sec (as specified in sub-clause 12.4)

-Tevaluate,SLSS = 0.64 (as specified in sub-clause 12.3)

-S-SSB period = 160 ms

This gives a total of 2.4 seconds.

The test system will verify that the V2X UE does not drop or delay more than 6 % of its V2X data and S-SSB transmissions during the duration of T2, and does not drop or delay more than 30 % of its S-SSB transmissions during the duration of T3.

The rate of correct SyncRef UE selection / reselection observed during repeated tests shall be at least 90 %.

## A.9.1.3.2 Test for FR1 NR Cell configured as the highest priority

## A.9.1.3.2.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to SyncRef UE selection / reselection defined in clause 12.4, when gNB is configured as the highest priority. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

This test is applicable for V2X sidelink communication capable UEs that support gNB as synchronization source and sidelink operation.

Table A.9.1.3.2.1-1: Void

The test parameters are given in table A.9.1.3.2.1-2 and A.9.1.3.2.1-3 below. There are no active cells and GNSS is reliable during the whole test. The test system can emulate and send the GNSS signal to the test UE. The test parameters for GNSS signals are defined in B.4.1. There are two active SyncRef UEs (SyncRef UE 1 and SyncRef UE 2) in this test. The test system shall emulate SyncRef UE 1 and SyncRef UE 2 to transmit S-SSB every S-SSB period.

The test system can verify the selection / reselection of SyncRef UE by monitoring the SLSS ID used by the V2X UE for its S-SSB transmissions. When the V2X UE is synchronized to a SyncRef UE, the V2X UE shall derive its SLSS ID from the SLSS ID of the SyncRef UE as per clause 5.8.5.3 of TS 38.331[2].

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. During T1, both SyncRef UE 1 and SyncRef UE 2 are powered off and the V2X UE will select GNSS as synchronization source. During T2, SyncRef UE 1 is powered ON and the V2X UE will select SyncRef UE 1 as the synchronization source. During T3, a higher priority SyncRef UE 2 is additionally powered ON and the V2X UE will reselect to the higher priority SyncRef UE 2 as the synchronization source.

Table A.9.1.3.2.1-2: Test Parameters for V2X Synchronization Reference Selection/Reselection Tests for FR1 NR Cell configured as the highest priority

Table A.9.1.3.2.1-3: SyncRef UE Specific Test Parameters for V2X Synchronization Reference Selection/Reselection Tests for FR1 NR Cell configured as the highest priority

## A.9.1.3.2.2Test Requirements

1) During T2, SyncRef UE selection delay is defined as the time from the beginning of T2 to the time UE is synchronized to SyncRef UE 1 and changes its S-SSB transmissions timing and SLSS ID to follow SyncRef UE 1 as the synchronization source. For the test configuration, the SLSS ID will be changed to 336+59 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE selection delay from start of T2.

The SyncRef UE selection delay shall be less than 8.8 sec. The SyncRef UE selection/reselection delay can be expressed as:

SyncRef UE selection/reselection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + S-SSB period

Where

-Tdetect,SyncRef UE = 8 sec (as specified in sub-clause 12.4)

-Tevaluate,SLSS = 0.64 sec (as specified in sub-clause 12.3)

-S-SSB period = 160 ms

This gives a total of 8.8 seconds.

2) During T3, SyncRef UE reselection delay is defined as the time from the beginning of T3 to the time UE changes its synchronization source from SyncRef UE 1 to SyncRef UE 2, and changes its S-SSB transmissions timing and SLSS ID to follow SyncRef UE 2 as the synchronization source. For the test configuration, the SLSS ID will be changed to 30 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE selection delay from start of T3.

The SyncRef UE reselection delay shall be less than 8.8 sec. The SyncRef UE selection/reselection delay can be expressed as:

SyncRef UE selection/reselection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + S-SSB period

Where

-Tdetect,SyncRef UE = 8 sec (as specified in sub-clause 12.4)

-Tevaluate,SLSS = 0.64 sec (as specified in sub-clause 12.3)

-S-SSB period = 160 ms

This gives a total of 8.8 seconds.

The test system will verify that the V2X UE does not drop or delay more than 6 % of its V2X data and S-SSB transmissions during the duration of T2 and T3.

The rate of correct SyncRef UE selection / reselection observed during repeated tests shall be at least 90 %.

## A.9.1.3.3Test for GNSS configured as the highest priority under SL-DRX

## A.9.1.3.3.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to SyncRef UE selection / reselection defined in clause 12.4, when GNSS is configured as the highest priority and SL-DRX is configured. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

The test parameters are given in table A.9.1.3.3.1-1and A.9.1.3.3.1-2 below. There are no GNSS signals in this test. There are three active SyncRef UEs (SyncRef UE 1, SyncRef UE 2 and SyncRef UE 3) in this test. The test system shall emulate SyncRef UE 1, SyncRef UE 2 and SyncRef UE 3 to transmit S-SSB every S-SSB period.

The test system can verify the selection / reselection of SyncRef UE by monitoring the SLSS ID used by the V2X UE for its S-SSB transmissions. When the V2X UE is not synchronized to any SyncRef UE, then the V2X UE shall use the SLSS ID belonging to set id_oon. When the V2X UE is synchronized to a SyncRef UE, the V2X UE shall derive its SLSS ID from the SLSS ID of the SyncRef UE as per clause 5.8.5.3 of TS 38.331[2].

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. SyncRef UE 1, SyncRef UE 2 and SyncRef UE 3 are all powered off before starting the test. During T1, SyncRef UE 1 is powered ON and the V2X UE will select SyncRef UE 1 as synchronization source. During T2, SyncRef UE 2 is powered ON and the V2X UE will select SyncRef UE 2 as the synchronization source. During T3, SyncRef UE 3 is powered ON and the V2X UE will reselect to SyncRef UE 3 as the synchronization source. SL-DRX is configured during the entire test period.

Table A.9.1.3.3.1-1: Test Parameters for V2X Synchronization Reference Selection/Reselection Tests for GNSS configured as the highest priority

Table A.9.1.3.3.1-2: SyncRef UE Specific Test Parameters for V2X Synchronization Reference Selection/Reselection Tests for GNSS configured as the highest priority

## A.9.1.3.3.2Test Requirements

During T1, SyncRef UE selection delay is defined as the time from the beginning of T1 to the time UE is synchronized to SyncRef UE 1, and changes its S-SSB transmissions timing and SLSS ID to follow SyncRef UE 1 as the synchronization source. For the test configuration, the SLSS ID will be changed to 30 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE selection delay from start of T1.

The SyncRef UE selection delay shall be less than 8.8 sec. The SyncRef UE selection delay can be expressed as:

SyncRef UE selection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + S-SSB period

Where

-Tdetect,SyncRef UE = 8 sec (as specified in sub-clause 12.4)

-Tevaluate,SLSS = 0.64 sec (as specified in sub-clause 12.3)

-S-SSB period = 160 ms

This gives a total of 8.8 seconds.

2) During T2, SyncRef UE reselection delay is defined as the time from the beginning of T2 to the time UE changes its synchronization source from SyncRef UE 1 to SyncRef UE 2 and changes its S-SSB transmissions timing and SLSS ID to follow SyncRef UE 2 as the synchronization source. For the test configuration, the SLSS ID will be changed to 336 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE reselection delay from start of T2.

The SyncRef UE reselection delay shall be less than 8.8 sec. The SyncRef UE reselection delay can be expressed as:

SyncRef UE reselection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + S-SSB period

Where

-Tdetect,SyncRef UE = 8 sec (as specified in sub-clause 12.4)

-Tevaluate,SLSS = 0.64 (as specified in sub-clause 12.3)

-S-SSB period = 160 ms

This gives a total of 8.8 seconds.

3) During T3, SyncRef UE reselection delay is defined as the time from the beginning of T3 to the time UE changes its synchronization source from SyncRef UE 2 to SyncRef UE 3, and changes its S-SSB transmissions timing and SLSS ID to follow SyncRef UE 3 as the synchronization source. For the test configuration, the SLSS ID will still be 0 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE reselection delay from start of T3.

The SyncRef UE reselection delay shall be less than 2.4 sec. The SyncRef UE reselection delay can be expressed as:

SyncRef UE reselection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + S-SSB period

Where

-Tdetect,SyncRef UE = 1.6 sec (as specified in sub-clause 12.4)

-Tevaluate,SLSS = 0.64 (as specified in sub-clause 12.3)

-S-SSB period = 160 ms

This gives a total of 2.4 seconds.

The test system will verify that the V2X UE does not drop its V2X data and SLSS transmissions at most in an aggregated window of 480 ms during the duration of T2, and does not drop or delay at most an aggregated window of 24 ms of its S-SSB transmissions during the duration of T3.

The rate of correct SyncRef UE selection / reselection observed during repeated tests shall be at least 90 %.

## A.9.1.3.4Test for FR1 NR Cell configured as the highest priority under SL-DRX

## A.9.1.3.4.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to SyncRef UE selection / reselection defined in clause 12.4, when gNB is configured as the highest priority and SL-DRX is configured. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

This test is applicable for V2X sidelink communication capable UEs that support gNB as synchronization source and sidelink operation.

The test parameters are given in table A.9.1.3.4.1-1 and A.9.1.3.4.1-2 below. There are no active cells and GNSS is reliable during the whole test. The test system can emulate and send the GNSS signal to the test UE. The test parameters for GNSS signals are defined in B.4.1. There are two active SyncRef UEs (SyncRef UE 1 and SyncRef UE 2) in this test. The test system shall emulate SyncRef UE 1 and SyncRef UE 2 to transmit S-SSB every S-SSB period.

The test system can verify the selection / reselection of SyncRef UE by monitoring the SLSS ID used by the V2X UE for its S-SSB transmissions. When the V2X UE is synchronized to a SyncRef UE, the V2X UE shall derive its SLSS ID from the SLSS ID of the SyncRef UE as per clause 5.8.5.3 of TS 38.331[2].

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. During T1, both SyncRef UE 1 and SyncRef UE 2 are powered off and the V2X UE will select GNSS as synchronization source. During T2, SyncRef UE 1 is powered ON and the V2X UE will select SyncRef UE 1 as the synchronization source. During T3, a higher priority SyncRef UE 2 is additionally powered ON and the V2X UE will reselect to the higher priority SyncRef UE 2 as the synchronization source. SL-DRX is configured during the entire test period.

Table A.9.1.3.4.1-1: Test Parameters for V2X Synchronization Reference Selection/Reselection Tests for FR1 NR Cell configured as the highest priority

Table A.9.1.3.4.1-2: SyncRef UE Specific Test Parameters for V2X Synchronization Reference Selection/Reselection Tests for FR1 NR Cell configured as the highest priority

## A.9.1.3.4.2Test Requirements

1) During T2, SyncRef UE selection delay is defined as the time from the beginning of T2 to the time UE is synchronized to SyncRef UE 1 and changes its S-SSB transmissions timing and SLSS ID to follow SyncRef UE 1 as the synchronization source. For the test configuration, the SLSS ID will be changed to 336+59 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE selection delay from start of T2.

The SyncRef UE selection delay shall be less than 8.8 sec. The SyncRef UE selection/reselection delay can be expressed as:

SyncRef UE selection/reselection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + S-SSB period

Where

-Tdetect,SyncRef UE = 8 sec (as specified in sub-clause 12.4)

-Tevaluate,SLSS = 0.64 sec (as specified in sub-clause 12.3)

-S-SSB period = 160 ms

This gives a total of 8.8 seconds.

2) During T3, SyncRef UE reselection delay is defined as the time from the beginning of T3 to the time UE changes its synchronization source from SyncRef UE 1 to SyncRef UE 2, and changes its S-SSB transmissions timing and SLSS ID to follow SyncRef UE 2 as the synchronization source. For the test configuration, the SLSS ID will be changed to 30 (with in-coverage IE in MIB-SL set to FALSE) after SyncRef UE selection delay from start of T3.

The SyncRef UE reselection delay shall be less than 8.8 sec. The SyncRef UE selection/reselection delay can be expressed as:

SyncRef UE selection/reselection delay = Tdetect,SyncRef UE + Tevaluate,SLSS + S-SSB period

Where

-Tdetect,SyncRef UE = 8 sec (as specified in sub-clause 12.4)

-Tevaluate,SLSS = 0.64 sec (as specified in sub-clause 12.3)

-S-SSB period = 160 ms

This gives a total of 8.8 seconds.

The test system will verify that the V2X UE does not drop or delay its V2X data and SLSS transmissions at most in an aggregated window of 480 ms during the duration of T2 and T3.

The rate of correct SyncRef UE selection / reselection observed during repeated tests shall be at least 90 %.

## A.9.1.4Test for L1 SL-RSRP Measurement

## A.9.1.4.1Test for V2X UE Autonomous Resource Selection/Reselection

## A.9.1.4.1.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to autonomous resource selection / reselection for V2X UE in mode 2 defined in clause 12.5. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

The test parameters are given in table A.9.1.4.1.1-1and A. 9.1.4.1.1-2 below. There are 50 active V2X sidelink UEs (UE0~UE49) in this test. Both the UE under test and active V2X sidelink UEs select GNSS as synchronization reference source. The test system can emulate and send the GNSS signal to the test UE and active V2X sidelink UEs. The test parameters for GNSS signals are defined in B.4.1. The test system shall emulate the active V2X sidelink UEs to transmit PSCCH/PSSCH every 5 ms. At the beginning of whole test, the test equipment shall send one AT command to trigger the UE under test continuously transmits PSCCH/PSSCH.

The test consists of two duration T1 and T2. During T1, the signal from Test Equipement are configured such that

-he measured PSSCH-RSRP for 20 active V2X sidelink UEs(UE10~UE29) is above the measurement threshold, and the resource occupied by the 20 active V2X sidelink UEs is expected to be excluded in the resource selection procedure and,

-the measured PSSCH-RSRP for other 30 active V2X sidelink UEs(UE0~UE9, UE30~UE49) is low the measurement threshold, and the resource occupied by the 30 active V2X sidelink UEs is expected to be included in the resource selection procedureDuring T2, the signal from Test Equipement are configured such that

-the measured PSSCH-RSRP or the 20 active V2X sidelink UEs(UE10~UE29) is below the measurement threshold, and the resource occupied by the 20 active V2X sidelink UEs is expected to be included in the resource selection procedure and,

-the measured PSSCH-RSRP for other 30 active V2X sidelink UEs(UE0~UE9, UE30~UE49) is above the measurement threshold, and the resource occupied by the 30 active V2X sidelink UEs is expected to be excluded in the resource selection procedure.

Table A. 9.1.4.1.1-1: Test Parameters for V2X UE Autonomous Resource Selection/Reselection Tests for PSSCH-RSRP measurements

Table A.9.1.4.1.1-2: Active Sidelink UE Specific Test Parameters for V2X UE Autonomous Resource Selection/Reselection Tests for PSSCH-RSRP measurements

## A.9.1.4.1.2Test Requirements

The test time  T1 and T2 should be long enough. The rate of PSSCH transmissions on the resources on subchannel #1 or #2 shall be less than 10 % during T1. The rate of PSSCH transmissions on the resources on subchannel #1 or #2 shall be more than 90 % during T2.

## A.9.1.4.2Test for V2X UE Resource Pre-emption

## A.9.1.4.2.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to autonomous resource pre-emption for V2X UE in mode 2 defined in clause 12.5. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

The test parameters are given in table A. 9.1.4.2.1-1and A.12. 9.1.4.1-2 below. There is one active V2X sidelink UE in this test. Both the UE under test and the active V2X sidelink UE select GNSS as synchronization reference source. The test system can emulate and send the GNSS signal to the test UE and active V2X sidelink UEs. The test parameters for GNSS signals are defined in B.4.1. At the beginning of whole test, the test equipment shall send one message with a SL-SCH MAC PDU as specified in clause 6.1.6 in TS 38.321[7], in order to make sure that the UE under test needs continuously transmit PSCCH/PSSCH.

The test consists of two duration T1 and T2. During T1, the signal from Test Equipement are configured such that the active V2X sidelink UE is not transmitting. The UE under test shall transmit SL data and reserve future resources. The resource reservation is decoded by the active V2X sidelink UE. The point in time at which resource reservation from the UE under test is decoded by the active V2X sidelink UE defines the start of time period T2. During T2, the active V2X sidelink UE reserves the same resource as the UE under test with high priority data no later than slot n- Tpre-empt.

Table A.9.1.4.2.1-1: Test Parameters for V2X UE Resource Pre-emption Tests for PSSCH-RSRP measurements

Table A.9.1.4.2.1-2: Active Sidelink UE Specific Test Parameters for V2X UE Resource Pre-emption Tests for PSSCH-RSRP measurements

## A.9.1.4.2.2Test Requirements

The test time T1 and T2 should be long enough. The UE under test is required to trigger resource reselection and not to transmit on the reserved resource at slot n when the high priority reservation is transmitted by the active V2X sidelink UE before n-Tpre-empt, where

Tpre-empt = T3+Tproc,0

T3 = 5 slots and Tproc,0= 1 slot for FR1.

The rate of PSSCH transmissions on the resources at slot n shall be less than 10 % during repeated tests.

## A.9.1.4.3 Test for V2X UE Resource Re-evaluation

## A.9.1.4.3.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to autonomous resource re-evaluation for V2X UE in mode 2 defined in clause 12.5. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

The test parameters are given in table A.9.1.4.3.1-1, A.9.1.4.3.1-2 and A.9.1.4.3.1-3 below. There are 130 active V2X sidelink UEs in this test. The first 100 active V2X sidelink UEs are scheduled with 50 ms periodicity. The last 30 active V2X sidelink Ues are aperiodic service UE with retransmission reservation period equaling 15 ms.

Both the UE under test and active V2X sidelink Ues select GNSS as synchronization reference source. The test system can emulate and send the GNSS signal to the test UE and active V2X sidelink Ues. The test parameters for GNSS signals are defined in B.4.1.

The test consists of three duration T0, T1, T2.

During T0, the signal from Test Equipement are configured. The resource occupied by the active V2X sidelink UEs is expected to be excluded in the resource selection procedure such that the measured PSSCH-RSRP is above the measurement threshold. The test equipment shall just configure the resource pool for the test UE without the MAC PDU for transmission channel configuration.

During T1, the signal from Test Equipement are configured. Some of the resource occupied by the active V2X sidelink Ues is expected to be excluded in the resource selection procedure such that the measured PSSCH-RSRP is above the measurement threshold and some of the resource occupied by the active V2X sidelink Ues is expected to be included in the resource selection procedure such that the measured PSSCH-RSRP is below the measurement threshold. The test system shall emulate the active V2X sidelink Ues to transmit PSCCH/PSSCH every 50 ms according to the RSRP level specified in the Table A. 9.1.4.3.1-2, but UE #0~29 will be silent during T2.

At the end of T1, where slot index mod 100 = 99, the test equipment shall send one message with a SL-SCH MAC PDU as specified in clause 6.1.6 in TS 38.321[7], in order to make sure that the UE under test shall be scheduled to periodically transmit PSCCH/PSSCH.

During T2, the additional aperiodic active V2X sidelink UEs from Test Equipement are configured in the beginning 30 slots, and the resource occupied by these active V2X sidelink UEs is expected to be excluded in the resource re-evaluation procedure such that the measured PSSCH-RSRP is above the measurement threshold shown in table A. 9.1.4.3.1-2. The test system shall emulate the active V2X sidelink UEs to transmit PSCCH/PSSCH with the maximum number of reserved PSCCH/PSSCH resources equalling n2 and time resource assignment interval as 15 ms.

During T2, the test UE is expeted to reselect the resources and transmit the PSCCH/PSSCH in the newly re-evaluated resources.

Table A.9.1.4.3.1-1: Test Parameters for V2X UE Resource Selection Tests for Re-evaluation

Table A.9.1.4.3.1-2: Active Sidelink UE Specific Test Parameters for V2X UE Resource Selection Tests for Re-evaluation (UE #0...99)

Table A.9.1.4.3.1-3: Active Sidelink UE Specific Test Parameters for V2X UE Resource Selection Tests for Re-evaluation (UE #100…129)

## A.9.1.4.3.2Test Requirements

The rate of PSSCH transmissions on the resources of the subchannels which are occupied by UE #65-84 shall be more than 90 % during T2.

## A.9.1.4.4Test for V2X UE Autonomous Resource Selection/Reselection with Periodic Sensing

## A.9.1.4.4.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to autonomous resource selection / reselection for V2X UE in mode 2 with partial sensing support defined in clause 12.5. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

The test parameters are given in table A.9.1.4.4.1-1and A. 9.1.4.4.1-2 below. There are 100 active V2X sidelink UEs (UE0~UE99) in this test. Both the UE under test and active V2X sidelink UEs select GNSS as synchronization reference source. The test system can emulate and send the GNSS signal to the test UE and active V2X sidelink UEs. The test parameters for GNSS signals are defined in B.4.1. The test system shall emulate the active V2X sidelink UEs to transmit PSCCH/PSSCH every 10 ms. At the beginning of whole test, the test equipment shall send one message with a SL-SCH MAC PDU as specified in clause 6.1.6 in TS 38.321[7] and ensure that the UE under test needs to continuously transmit PSCCH/PSSCH with 10 ms period. Upon receiving the MAC PDU, UE starts resource selection to transmit PSCCH/PSSCH based on the available sensing results.

The test consists of two duration T1 and T2. During T1, the signals from Test Equipment are configured such that

-the measured PSSCH-RSRP for 40 active V2X sidelink UEs(UE20~UE59) is above the measurement threshold, and the resource occupied by the 40 active V2X sidelink UEs is expected to be excluded in the resource selection procedure and,

-the measured PSSCH-RSRP for other 60 active V2X sidelink UEs(UE0~UE19, UE60~UE99) is low the measurement threshold, and the resource occupied by the 60 active V2X sidelink UEs is expected to be included in the resource selection procedure.

During T2, the signals from Test Equipment are configured such that

-the measured PSSCH-RSRP for the 40 active V2X sidelink UEs(UE20~UE59) is below the measurement threshold, and the resource occupied by the 40 active V2X sidelink UEs is expected to be included in the resource selection procedure and,

-the measured PSSCH-RSRP for other 60 active V2X sidelink UEs(UE0~UE19, UE60~UE99) is above the measurement threshold, and the resource occupied by the 60 active V2X sidelink UEs is expected to be excluded in the resource selection procedure.

Table A.9.1.4.4.1-1: Test Parameters for V2X UE Autonomous Resource Selection/Reselection Tests with Periodic Sensing

Table A.9.1.4.4.1-2: Active Sidelink UE Specific Test Parameters for V2X UE Autonomous Resource Selection/Reselection Tests with Periodic Sensing

## A.9.1.4.4.2Test Requirements

The test time T1 and T2 should be long enough. The rate of PSSCH transmissions on the resources on subchannel #1 or #2 shall be less than 10 % during T1. The rate of PSSCH transmissions on the resources on subchannel #1 or #2 shall be more than 90 % during T2.

## A.9.1.4.5Test for V2X UE Autonomous Resource Selection/Reselection with Contiguous Sensing

## A.9.1.4.5.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to autonomous resource selection / reselection for V2X UE in mode 2 performing contiguous sensing configured with M=31 defined in clause 12.5. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

The test parameters are given in table A.9.1.4.5.1-1and A. 9.1.4.5.1-2 below. There are 50 active V2X sidelink UEs (UE0~UE49) in this test. Both the UE under test and active V2X sidelink UEs select GNSS as synchronization reference source. The test system can emulate and send the GNSS signal to the test UE and active V2X sidelink UEs. The test parameters for GNSS signals are defined in B.4.1. The test system shall emulate the active V2X sidelink UEs to transmit PSCCH/PSSCH every 5 ms. Starting from the beginning of whole test, the test equipment shall send a message with a SL-SCH MAC PDU every 5 ms as specified in clause 6.1.6 in TS 38.321[7] to schedule an aperiodic transmission and ensure that the UE under test needs continuously transmit PSCCH/PSSCH every 5 ms.

The test consists of two duration T1 and T2. During T1, the signal from Test Equipment are configured such that

-the measured PSSCH-RSRP for 20 active V2X sidelink UEs (UE10~UE29) is above the measurement threshold, and the resource occupied by the 20 active V2X sidelink UEs is expected to be excluded in the resource selection procedure and,

-the measured PSSCH-RSRP for other 30 active V2X sidelink UEs(UE0~UE9, UE30~UE49) is low the measurement threshold, and the resource occupied by the 30 active V2X sidelink UEs is expected to be included in the resource selection procedure.

During T2, the signal from Test Equipment are configured such that

-the measured PSSCH-RSRP for the 20 active V2X sidelink UEs(UE10~UE29) is below the measurement threshold, and the resource occupied by the 20 active V2X sidelink UEs is expected to be included in the resource selection procedure and,

-the measured PSSCH-RSRP for other 30 active V2X sidelink UEs(UE0~UE9, UE30~UE49) is above the measurement threshold, and the resource occupied by the 30 active V2X sidelink UEs is expected to be excluded in the resource selection procedure.

Table A.9.1.4.5.1-1: Test Parameters for V2X UE Autonomous Resource Selection/Reselection Tests with Contiguous Sensing

Table A.9.1.4.5.1-2: Active Sidelink UE Specific Test Parameters for V2X UE Autonomous Resource Selection/Reselection Tests with Contiguous Sensing

## A.9.1.4.5.2Test Requirements

The test time T1 and T2 should be long enough. The rate of PSSCH transmissions on the resources on subchannel #1 or #2 shall be less than 10 % during T1. The rate of PSSCH transmissions on the resources on subchannel #1 or #2 shall be more than 90 % during T2.

## A.9.1.4.6Test for V2X UE Autonomous Resource Selection/Reselection in SL-DRX

## A.9.1.4.6.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to autonomous resource selection / reselection for V2X UE in mode 2 defined in clause 12.5. For this test, the UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

The test parameters are given in table A.9.1.4.6.1-1and A. 9.1.4.6.1-2 below. There are 50 active V2X sidelink UEs (UE0~UE49) and another V2X sidelink UE as the receiver for the UE under test in this test. The UE under test, the receiver UE and active V2X sidelink UEs select GNSS as synchronization reference source. The test system can emulate and send the GNSS signal to the test UE, the receiver V2X sidelink UE and active V2X sidelink UEs. The test parameters for GNSS signals are defined in B.4.1. The test system shall emulate the active V2X sidelink UEs to transmit PSCCH/PSSCH every 5 ms. At the beginning of whole test, the test equipment shall send one message with a SL-SCH MAC PDU as specified in clause 6.1.6 in TS 38.321[7] and ensure that the UE under test needs continuously transmit PSCCH/PSSCH to the receiver SL UE.

The receiver UE runs one DRX cycle with 40 ms cycle length and 10 ms on time, 0 ms inactivity timer, and 10 ms offset. The UE under test and the 50 active UEs are in non-DRX mode.

The test consists of two duration T1 and T2. During T1, the signals from Test Equipment are configured such that

-the measured PSSCH-RSRP for 20 active V2X sidelink UEs(UE10~UE29) is above the measurement threshold, and the resource occupied by the 20 active V2X sidelink UEs is expected to be excluded in the resource selection procedure and,

-the measured PSSCH-RSRP for other 30 active V2X sidelink UEs(UE0~UE9, UE30~UE49) is low the measurement threshold, and the resource occupied by the 30 active V2X sidelink UEs is expected to be included in the resource selection procedure.

During T2, the signals from Test Equipment are configured such that

-the measured PSSCH-RSRP for the 20 active V2X sidelink UEs(UE20~UE29) is below the measurement threshold, and the resource occupied by the 20 active V2X sidelink UEs is expected to be included in the resource selection procedure and,

-the measured PSSCH-RSRP for other 30 active V2X sidelink UEs(UE0~UE9, UE30~UE49) is above the measurement threshold, and the resource occupied by the 30 active V2X sidelink UEs is expected to be excluded in the resource selection procedure.

Table A.9.1.4.6.1-1: Test Parameters for V2X UE Autonomous Resource Selection/Reselection Tests in SL-DRX

Table A.9.1.4.6.1-2: Active Sidelink UE Specific Test Parameters for V2X UE Autonomous Resource Selection/Reselection Tests in SL-DRX

## A.9.1.4.6.2Test Requirements

The test time T1 and T2 should be long enough. The rate of PSSCH transmissions on the resources on subchannel #1 or #2 shall be less than 10 % during T1. The rate of PSSCH transmissions on the resources on subchannel #1 or #2 shall be more than 90 % during T2. The PSSCH transmission should happen only in the receiver SL UE SL-DRX active time.

## A.9.1.5Test for Congestion Control Measurement

## A.9.1.5.1Test Purpose and Environment

The purpose of this test is to verify the congestion control measurement requirements in section 12.6. For UE supporting NR Uu and sidelink operation, this test will also verify that V2X UE makes correct reporting of an event.

The test parameters are given in table A.9.1.5.1-1,  Table A.9.1.5.1-2 , A.9.1.5.1-3 and A.9.1.5.1-4 below. There are 4 active V2X sidelink UEs in this test. The test system shall emulate the active sidelink UE to transmit PSCCH/PSSCH every 50 ms. Additionally, For UE supporting NR Uu and sidelink operation, there is an active Cell (Cell 1) in this test. For UE only supporting NR sidelink, There are no active cell and GNSS is reliable during the whole test. The test system can emulate and send the GNSS signal to the test UE. The test parameters for GNSS signals are defined in B.4.1.

The test consists of two successive time periods, with time duration of T1, and T2 respectively. During T1, all of active V2X sidelink UEs are configured to transmit PSCCH/PSSCH with lower transmission power every 50 ms. During T2, all of active V2X sidelink UEs are configured to transmit PSCCH/PSSCH with higher transmission power every 50 ms.

For UE supporting NR Uu and sidelink operation, the UE under test and all active sidelink UEs select PCell as synchonization source In the measurement control information it is indicated to the V2X UE that event-triggered reporting with Event C1 is used.

For UE only supporting NR sidelink, the UE under test and all active sidelink UEs select GNSS as synchonization source. The UE is triggered by the test loop function or the upper layers to transmit for V2X Sidelink Communication.

For UE supporting NR Uu and sidelink operation, Supported test configurations for FR1 NR cell are shown in table A.9.1.5.1.1-1.

Table A.9.1.5.1.1-1: Supported Test Configurations for FR1 NR cell (only for UE supporting both NR Uu and sidelink operation)

Table A.9.1.5.1-2: General test parameters for Congestion Control Measurement Test for V2X UE

Table A.9.1.5.1-3: Active sidelink UE specific test parameters for Congestion Control Measurement Test for V2X UE

Table A.9.1.5.1-4: Cell Test Parameters for Congestion Control Measurement Test for V2X UE (only for UE supporting both NR Uu and sidelink operation)

## A.9.1.5.2Test Requirements

For UEs that support NR Uu and sidelink operation, the UEs shall not send event C1 triggered measurement reports during T1 and shall send event C1 triggered measurement reports during T2.

For UEs that support sidelink operation only, the UE channel occupancy ratio shall be larger than 0.001 during T1, and the UE channel occupancy ratio shall be smaller than 0.001 curing T2.

The rate of correct events observed during repeated tests shall be at least 98 %.

## A.9.1.6Test for Interruption

## A.9.1.6.1Test for Interruption to WAN due to V2X Sidelink Communication

## A.9.1.6.1.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to interruptions due to V2X sidelink communication defined in clause 12.7.1 under the following additional conditions:

-The UE is out of coverage on the V2X sidelink carrier and is associated with a serving cell on a non-V2X sidelink carrier

This test is applicable for V2X sidelink communication capable UEs that support inter-band concurrent V2X sidelink operation.

For this test, the UE is triggered by the test loop function or the upper layers to monitor V2X sidelink communication.

The test parameters are given in table A.9.1.6.1.1-1, table A.9.1.6.1.1-2, table A.9.1.6.1.1-3 and table A.9.1.6.1.1-4. The test consists of one active cell (PCell) on the serving RF channel 1, and there are no active cells on RF channel 2. On RF channel 2, the test consists of 8 active Sidelink UEs in this test transmitting V2X sidelink communication. The UE under test and all active sidelink UEs select the active cell as synchonization source.

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively.

During T1, the UE is in RRC_IDLE and monitoring the V2X sidelink communication transmission from other active Sidelink UEs on the V2X sidelink communication resources.

During T2, the test system establishes a RRC connection with the UE. No PDSCH traffic is scheduled for UE, and the UE is expected to transmit SidelinkUEInformationNR indicating sl-RxInterestedFreqList. On reception of SidelinkUEInformationNR, the test system shall send RRC reconfiguration message to the UE and wait for the UE to respond with RRC reconfiguration complete message before transitioning to T3. If the UE does not transmit SidelinkUEInformationNR for up to 2 second, the test system shall transition to T3.

During T3, the UE is scheduled with PDSCH traffic on PCell downlink. The test system will count the missed ACK/NACKs during T3 to verify the allowed interruptions during V2X sidelink communication.

Table A.9.1.6.1.1-1: Supported test configurations for FR1 PCell

Table A.9.1.6.1.1-2: Test Parameters for Interruptions due to V2X Sidelink Communication

Table A.9.1.6.1.1-3: Sidelink Communication Configuration for Interruptions due to V2X Sidelink Communication

Table A.9.1.6.1.1-4: Cell specific test parameters for interruptions due to V2X slidelink communication

## A.9.1.6.1.2Test Requirements

The UE shall be continuously scheduled on PCell on RF channel 1 during T3. During T3, the interruption on PCell shall not be more than the values specified in clause 12.7.1..

## A.9.1.6.2Test for interruption to WAN at transitions between active and non-active during SL-DRX in asynchronous case

## A.9.1.6.2.1Test Purpose and Environment

The purpose of this test is to verify that when V2X sidelink is in SL-DRX and NR PCell is in non-DRX, NR PCell interruptions due to transitions of V2X sidelink UE from active to non-active and from non-active to active do not exceed the limits in terms of missing ACK/NACK. This test will verify the missing ACK/NACK rate on NR PCell in clause 12.7.4 under the following additional conditions:

-The UE is out of coverage on the V2X sidelink carrier and is associated with a serving cell on a non-V2X sidelink carrier.

-The UE is in sidelink resource allocation mode 1.

This test is applicable for V2X sidelink communication capable UEs that support inter-band concurrent V2X sidelink operation.

For this test, the UE is triggered by the test loop function or the upper layers to monitor V2X sidelink communication.

The test parameters are given in table A.9.1.6.2.1-1, table A.9.1.6.2.1-2, and table A.9.1.6.2.1-3. The test consists of one active cell (PCell) on the serving RF channel 1, and there are no active cells on RF channel 2. The UE under test selects GNSS as the synchonization source.

The test consists of one time period, with duration of T1. During T1, NR PCell is continuously scheduled in DL while V2X sidelink is not scheduled and has SL-DRX configured. Prior to start of T1 the SL-DRX inactivity timer for the V2X sidelink has already expired. PDCCH indicating a new transmission on PCell shall be sent continuously during the entire time duration to ensure UE would not enter DRX state on PCell.

Table A.9.1.6.2.1-1: Supported test configurations for FR1 PCell

Table A.9.1.6.2.1-2: Test Parameters for Interruptions at transitions between active and non-active during SL-DRX in asynchronous case

Table A.9.1.6.2.1-3: Cell specific test parameters for interruptions at transitions between active and non-active during SL-DRX in asynchronous case

## A.9.1.6.2.2Test Requirements

The UE shall be continuously scheduled on PCell on RF channel 1 during the entire length of T1. UE shall not be scheduled in V2X sidelink during T1. During the time duration T1 the UE shall transmit at least 99.375 % of ACK/NACK on NR PCell.

Interruption on NR PCell shall not exceed X as defined in table A.9.1.6.2.2-1.

Table A.9.1.6.2.2-1: Interruption length X at transition between active and non-active during SL-DRX

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.9.1.6.3Test for Interruption at NR Sidelink Diccovery Configuration

## A.9.1.6.3.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to interruptions due to NR sidelink discovery configuration defined in clause 12.7.8 under the following additional conditions:

-The UE is out of coverage on the NR sidelink carrier and is associated with a serving cell on a NR non-sidelink carrier

This test is applicable for NR sidelink discovery capable UEs that support inter-band concurrent sidelink operation.

For this test, the UE is triggered by the test loop function or the upper layers to monitor NR sidelink discovery.

The test parameters are given in table A.9.1.6.3.1-1, table A.9.1.6.3.1-2, table A.9.1.6.3.1-3 and table A.9.1.6.3.1-4. The test consists of one active cell (PCell) on the serving RF channel 1, and there are no active cells on RF channel 2. On RF channel 2, the test consists of 8 active Sidelink UEs in this test transmitting sidelink discovery. The UE under test and all active sidelink UEs select the active cell as synchonization source.

The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively.

During T1, the UE is in RRC_IDLE and monitoring NR sidelink discovery announcements from other active Sidelink UEs on NR sidelink discovery resources.

During T2, the test system establishes a RRC connection with the UE. No PDSCH traffic is scheduled for UE, and the UE is expected to transmit SidelinkUEInformationNR indicating sl-RxInterestedFreqListDisc. On reception of SidelinkUEInformationNR, the test system shall send RRC reconfiguration message to the UE and wait for the UE to respond with RRC reconfiguration complete message before transitioning to T3. If the UE does not transmit SidelinkUEInformationNR for up to 2 second, the test system shall transition to T3.

During T3, the UE is scheduled with PDSCH traffic on PCell downlink. The test system will count the missed ACK/NACKs during T3 to verify the allowed interruptions during NR sidelink discovery.

Table A.9.1.6.3.1-1: Supported test configurations for FR1 PCell

Table A.9.1.6.3.1-2: Test Parameters for Interruptions at NR Sidelink Discovery Configuration

Table A.9.1.6.3.1-3: Sidelink Discovery Configuration for Interruptions at NR Sidelink Discovery Configuration

Table A.9.1.6.3.1-4: Cell specific test parameters for interruptions at NR Sidelink Discovery Configuration

## A.9.1.6.3.2Test Requirements

The UE shall be continuously scheduled on PCell on RF channel 1 during T3. During T3, the interruption on PCell shall not be more than the values specified in clause 12.7.8.

## A.9.1.7Selection / Reselection of relay UE

## A.9.1.7.1Test Purpose and Environment

The purpose of this test is to verify the requirements related to selection / reselection of relay UE defined in clauses 12.10. In the test, the UE under test is configured with PCell or an Sidelink UE but not both, based on the scenarios (U2N or U2U relay) UE supported, and is configured with resource pools for NR sidelink discovery message as required for remote UE operation.

This test is applicable to UEs capable of NR sidelink communication and sidelink discovery, and further support the optional feature of sidelink remote UE operation.

The test parameters are given in table A.9.1.7.1.1-0, table A.9.1.7.1.1-1, table A.9.1.7.1-2, table A.9.1.7.1-3, table A.9.1.7.1-4, table A.9.1.7.1-5, and table A.9.1.7.1-6 below. The test consists of one active serving cell (cell 1, configured as Table A.9.1.7.1-5) or an Sidelink UE (Sidelink UE 1, configured as Table A.9.1.7.1-6), one remote UE and two active Sidelink relay UEs (Sidelink Relay UE 1, Sidelink Relay UE 2). The relay UEs are configured in mode 2 to be transmitting relay discovery messages every discovery period, which is determined by resource reservation period indicated by sl-ResourceReservePeriodList.

The test system shall ensure that the remote UE under test has transmitted SidelinkUEInformationNR message and has been configured with the sidelink discovery resource pool and sidelink communication resource pool respectively for relay operation prior to the start of the test.

The tests consist of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively.

During T1, RSRP of cell 1 or SL-RSRP of Sidelink UE 1 is kept higher than threshHighRemote (within sl-remoteUE-Config), and the remote UE is not required to perform relay UE selection.

During T2, RSRP of cell 1 or SL-RSRP of Sidelink UE 1 is configured to be lower than threshHighRemote. The UE is expected to start looking for relay UE. The test system shall ensure that the UE under test has been configured the resource pool prior to end of T2 duration. During T2, the SD-RSRP of Sidelink Relay UE 1 and Sidelink Relay UE 2 is configured to be lower than the detection threshold and no relay UE will be available for the remote UE under test.

During T3, the SD-RSRP of Sidelink Relay UE 1 is raised above the threshold sl-RSRP-Thresh and the UE is expected to perform relay selection to Sidelink Relay UE 1. The test system can determine that the remote UE has selected a relay by monitoring the configured sidelink communication resource for the ProSe direct link establishment request message to the relay UE.

During T4, the UE is expected to complete the sidelink connection establishment with the relay UE. Note that the RSRP of the serving cell (cell 1) or SL-RSRP of Sidelink UE 1 and the SD-RSRP of sidelink relay UEs are kept unchanged during T3 and T4. The period T4 ends when Sidelink Relay UE1 sends the sidelink communication response message back to the remote UE.

During T5, SD-RSRP of Sidelink Relay UEs are modified such that the remote UE is expected to reselect to Sidelink Relay UE2.

Table A.9.1.7.1-0: Supported test configurations for FR1 PCell

Table A.9.1.7.1-1: Test parameters for selection / reselection of relay UE test for NR FR1

Table A.9.1.7.1-2: Sidelink discovery configuration for selection / reselection of relay UE test for NR FR1

Table A.9.1.7.1-3: Sidelink Communication configuration for selection / reselection of relay UE test

Table A.9.1.7.1-4: Sidelink Relay UE specific test parameters for selection / reselection of relay UE test for NR FR1

Table A.9.1.7.1-5: Cell specific test parameters for selection / reselection of relay UE test for NR FR1

Table A.9.1.7.1-6: Sidelink UE specific test parameters for selection / reselection of relay UE test for NR FR1

## A.9.1.7.2Test Requirements

Sidelink relay UE selection delay is defined as the time from the beginning of time period T3 to the moment when the UE selects the Sidelink Relay UE1 and transmits the PC5-SP direct communication setup message using Sidelink Communications.

The test system shall verify that the sidelink relay UE selection delay is less than 680 ms.

NOTE:The sidelink relay UE selection delay can be expressed as (Tevaluate, SL_Relay_Intra + 40 ms).

Sidelink relay UE reselection time is defined as the time from the beginning of time period T5 to the moment when the UE reselects to Sidelink relay UE2 and transmits the direct communication setup message using Sidelink Communications.

The test system shall verify that the sidelink relay UE reselection delay is less than 840 ms.

NOTE:The sidelink relay UE reselection delay can be expressed as (Tmeasure, SL_Relay_Intra + Tevaluate, SL_Relay_Intra + 40 ms).

## A.9ATests for NR Sidelink Measurements for Positioning

## A.9A.1Tests for NR Sidelink Measurements for Positioning in FR1

## A.9A.1.1Measurement delay tests

## A.9A.1.1.1NR SL RSTD measurement reporting delay test case in FR1 SA

## A.9A.1.1.1.1Test Purpose and Environment

The purpose of the test is to verify that the SL RSTD measurement meets the requirements specified in clause 12A.2 in an environment with AWGN propagation conditions in FR1 in standalone NR scenario, with additionally configured single frequency layer for SL positioning.

This test is applicable for UEs supporting NR Uu and V2X or 5G ProSe operation, which are capable of performing SL RSTD measurements.

The supported NR Uu test configurations are specified in table A.9A.1.1.1.1-1.

Table A.9A.1.1.1.1-1: Supported test configurations for FR1 NR Cell 1

The supported NR SL test configurations are specified in table A.9A.1.1.1.1-2.

Table A.9A.1.1.1.1-2: Supported test configurations for NR SL UEs

In the test, there is one target UE receiving SL-PRS and performing SL RSTD measurements and three anchor UEs (anchor UE 1, anchor UE 2, and anchor UE 3) transmitting SL-PRS for the SL RSTD measurements on NR SL RF channel 2. Anchor UE 1 is the reference anchor UE for the measurements. The target UE and all the anchor UEs are in RRC_CONNECTED state, with Cell 1 as their PCell in FR1 on NR Uu RF channel 1. Cell 1 is also the synchronization source of the target UE and all anchor UEs in the test.

The test consists of two consecutive time intervals, with duration of T1 and T2. Before T2 starts, the UEs have been synchronized to Cell 1. During time duration T1, the target UE shall not have any timing information of anchor UE 2 and anchor UE 3. All three anchor UEs transmit SL-PRS during T2.

The SL-TDOA-ProvideAssistanceData and SL-TDOA-RequestLocationInformation as defined in TS 38.355 [37, clause 6.9], shall be provided to the target UE via Cell 1 during T1. The last TTI containing the two messages shall be provided to the target UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the SL-TDOA assistance data and location information request.

The general test parameters are listed in table A.9A.1.1.1.1-3. NR Uu specific test parameters for Cell 1 and NR Uu UE-specific test parameters for all UEs in the test are listed in table A.9A.1.1.1.1-4 and A.9A.1.1.1.1-5, respectively. Anchor UE specific test parameters for SL RSTD measurement reporting delay during T1 and T2 are listed in table A.9A.1.1.1.1-6.

Table A.9A.1.1.1.1-3: General test parameters for SL RSTD measurement reporting delay

Table A.9A.1.1.1.1-5: NR Uu UE-specific test parameters for UE 0, UE 1, UE 2, and UE 3

Table A.9A.1.1.1.1-6: Anchor UEs specific test parameters on the SL carrier

## A.9A.1.1.1.2Test Requirements

The SL RSTD measurement time fulfils the requirements specified in clause 12A.2.5.

The UE shall perform and report to LMF the SL RSTD measurements for anchor UE 2 and anchor UE 3 with respect to the reference anchor UE 1, within the time duration specified in clause 12A.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each anchor UE observed during repeated tests shall be at least 90%, where the reported SL RSTD measurement for each correct event shall be within the SL RSTD reporting range specified in clause 10.4A.2.1.1, i.e., between SL_RSTD_000000 and SL_RSTD_492513.

## A.9A.1.1.2SLRx-Tx measurement delay tests

## A.9A.1.1.2.1Test Purpose and Environment

The purpose of the test is to verify that the SL Rx-Tx measurement meets the requirements specified in clause 12A.2 in an environment with AWGN propagation conditions in FR1 in standalone NR scenario, with additionally configured single frequency layer for SL positioning.

This test is applicable for UEs supporting NR Uu and V2X or 5G ProSe operation, which are capable of performing SL Rx-Tx measurements.

The supported NR Uu test configurations in FR1 are shown in table A.9A.1.1.2.1-1.

Table A.9A.1.1.2.1-1: Supported Test Configurations for FR1 NR cell

The supported NR SL test configurations are specified in table A.9A.1.1.2.1-2.

Table A.9A.1.1.2.1-2: Supported test configurations for NR SL UEs

There is one NR active cell (Cell 1) and three active UEs (one target UE and two anchor UEs for SL positioning measurement) in this test. The target UE receives SL-PRS and performs the SL Rx-Tx time difference measurement. The two anchor UEs transmit the SL-PRS for the SL Rx-Tx time difference measurement on NR SL RF channel 2. The target UE and all anchor UEs are in RRC_CONNECTED state, with Cell 1 as their PCell in FR1 on NR Uu RF channel 1.

The test consists of two successive time periods, with time duration of T1 and T2 respectively. Before T2 starts, the UEs have been synchronized to the NR serving cell. And during T2, two anchor UEs transmit SL-PRS for positioning measurements.

The SL-RTT-ProvideAssistanceData and SL-RTT-RequestLocationInformation as defined in TS 38.355 [37, clause 6.9], shall be provided to the target UE via Cell 1 during T1. The last TTI containing the two messages shall be provided to the target UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the SL RTT assistance data and location information request.

The test parameters are given in table A.9A.1.1.2.1-3, A.9A.1.1.2.1-4, A.9A.1.1.2.1-5 and table A.9A.1.1.2.1-6 below.

Table A.9A.1.1.2.1-3: General Test Parameters for SL Rx-Tx measurement reporting delay

Table A.9A.1.1.2.1-4: NR Uu specific test parameters for Cell 1

Table A.9A.1.1.2.1-5: NR Uu UE-specific test parameters for UE 0, UE 1 and UE 2

Table A.9A.1.1.2.1-6: Anchor V2X UE specific test parameters for SL Rx-Tx measurement

## A.9A.1.1.2.2Test Requirements

The SL Rx-Tx time difference measurement time fulfils the requirements specified in clause 12A.4.5.

The UE shall perform and report the SL Rx-Tx time difference measurements for anchor UE 1 and anchor UE 2 within the specified SL Rx-Tx time difference measurement time starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each anchor UE observed during repeated tests shall be at least 90%, where the reported SL Rx-Tx measurement for each correct event shall be within the SL Rx-Tx reporting range specified in clause 10.4A.4.1.

## A.9A.1.1.3NR SL AoA measurements reporting delay test in FR1 SA

## A.9A.1.1.3.1Test Purpose and Environment

The purpose of the test is to verify that the SL AoA measurement meets the requirements specified in clause 12A.6 in an environment with AWGN propagation conditions in FR1 in NR Uu standalone scenario, when a single frequency layer is configured for SL positioning.

The test is applicable for UEs supporting NR Uu and V2X or 5G ProSe operation, which are capable of performing SL AoA measurements.

The supported NR Uu test configurations are specified in table A.9A.1.1.3.1-1.

The supported NR SL test configurations are specified in table A.9A.1.1.3.1-2.

Table A.9A.1.1.3.1-1: Supported Test Configurations for FR1 NR cell

Table A.9A.1.1.3.1-2: Supported test configurations for NR SL UEs

In the test there is one target UE receiving SL-PRS and performing SL AoA measurements and two anchor UEs (anchor UE 1, anchor UE 2) transmitting SL-PRS for the SL AoA measurements. The target UE and all the anchor UEs are in RRC_CONNECTED state, with Cell 1 as their PCell in FR1. Cell 1 is also the synchronization source of the target UE and all anchor UEs in the test.

The test consists of two consecutive time intervals, with the duration of T1 and T2. During the duration T1, the target UE shall not have any timing information of anchor UE 1 and anchor UE 2. All two anchor UEs transmit SL-PRS during T2.

The SL-AOA-ProvideAssistanceData and SL-AOA-RequestLocationInformation as defined in TS 38.355 [37], shall be provided to the target UE via Cell 1 during T1. The last TTI containing the two messages shall be provided to the target UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the SL-AOA assistance data and location information request.

The general test parameters are listed in table A.9A.1.1.3.1-3. NR Uu specific test parameters for Cell 1 and NR Uu UE-specific test parameters for all UEs in the test are listed in table A.9A.1.1.3.1-4 and A.9A.1.1.3.1-5, respectively. Anchor UE specific test parameters for SL AoA measurement reporting delay during T1 and T2 are listed in table A.9A.1.1.3.1-6.

Table A.9A.1.1.3.1-3: General test parameters for SL AoA measurement reporting delay

Table A.9A.1.1.3.1-4: NR Uu specific test parameters for Cell 1

Table A.9A.1.1.3.1-5: NR Uu UE-specific test parameters for UE 0, UE 1, and UE 2

Table A.9A.1.1.3.1-6: Anchor UE specific test parameters on the SL carrier

## A.9A.1.1.3.2Test Requirements

The SL AoA measurement time fulfils the requirements specified in clause 12A.6.5.

The UE shall perform and report to LMF the SL AoA measurements for the anchor UE 1 and anchor UE 2, within the time duration specified in clause 12A.6.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each anchor UE observed during repeated tests shall be at least 90%, where the reported SL AoA measurement for each correct event shall be within the SL AoA reporting range specified in clause 10.4A.6.1.1, i.e., between A_AoA_0 and SL_AoA_3599, and between Z_AoA_0 and Z_AoA_1799.

## A.9A.1.1.4NR SL RTOA measurements reporting delay test in FR1 SA

## A.9A.1.1.4.1Test Purpose and Environment

The purpose of the test is to verify that the SL RTOA measurement meets the requirements specified in clause 12A.7 in an environment with AWGN propagation conditions in FR1 in NR Uu standalone scenario, when a single frequency layer is configured for SL positioning.

The test is applicable for UEs supporting NR Uu and V2X or 5G ProSe operation, which are capable of performing SL AoA measurements.

The supported NR Uu test configurations are specified in table A.9A.1.1.4.1-1.

The supported NR SL test configurations are specified in table A.9A.1.1.4.1-2.

Table A.9A.1.1.4.1-1: Supported test configurations for FR1 NR Cell 1

Table A.9A.1.1.4.1-2: Supported test configurations for NR SL UEs

In the test there is one target UE transmitting SL-PRS and performing SL RTOA measurements and one anchor UE (anchor UE 1) receiving SL-PRS for the SL RTOA measurements. The target UE and all the anchor UEs are in RRC_CONNECTED state, with Cell 1 as their PCell in FR1. Cell 1 is also the synchronization source of the target UE and all anchor UEs in the test.

The test consists of two consecutive time intervals, with the duration of T1 and T2. During the duration T1, the target UE shall not have any timing information of anchor UE 1 and anchor UE 2. All two anchor UEs transmit SL-PRS during T2.

The SL-TOA-ProvideAssistanceData and SL-TOA-RequestLocationInformation as defined in TS 38.355 [37], shall be provided to the target UE via Cell 1 during T1. The last TTI containing the two messages shall be provided to the target UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the SL-TOA assistance data and location information request.

The general test parameters are listed in table A.9A.1.1.4.1-3. NR Uu specific test parameters for Cell 1 and NR Uu UE-specific test parameters for all UEs in the test are listed in table A.9A.1.1.4.1-4 and A.9A.1.1.4.1-5, respectively. Anchor UE specific test parameters for SL RTOA measurement reporting delay during T1 and T2 are listed in table A.9A.1.1.4.1-6.

Table A.9A.1.1.4.1-3: General test parameters for SL RTOA measurement reporting delay

Table A.9A.1.1.4.1-4: NR Uu specific test parameters for Cell 1

Table A.9A.1.1.4.1-5: NR Uu UE-specific test parameters for UE 0 and UE 1

Table A.9A.1.1.4.1-6: Anchor UE specific test parameters on the SL carrier

## A.9A.1.1.4.2Test Requirements

The SL RTOA measurement time fulfils the requirements specified in clause 12A.7.5.

The UE shall perform and report to LMF the SL RTOA measurements for the anchor UE 1, within the time duration specified in clause 12A.7.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each anchor UE observed during repeated tests shall be at least 90%, where the reported SL RTOA measurement for each correct event shall be within the SL RTOA reporting range specified in clause 10.4A.7.1.1, i.e., between SL_RTOA_0 and SL_RTOA_985024.

## A.9A.1.1.5NR SL PRS-RSRP measurement reporting delay test case in FR1 SA

## A.9A.1.1.5.1Test Purpose and Environment

The purpose of the test is to verify that the measurement time of both SL PRS PRS-RSRP and SL PRS RSTD measurements meet the requirements specified in clause 12A.3.5and 12A.2.5 respectively in an environment with AWGN propagation conditions in FR1 in standalone NR scenario, with additionally configured single frequency layer for SL positioning.

The test environment and configurations refer to A.9A.1.1.1. And if UE passes this test case, then UE does not need to take the reporting delay test with RSTD measurement only defined in A.9A.1.1.1.

## A.9A.1.1.5.2Test Requirements

The SL PRS-RSRP and SL RSTD measurement times fulfil the requirements specified in clause 12A.3.5 and 12A.2.5 respectively.

The UE shall perform and report to LMF the SL PRS-RSRP measurements for anchor UE 2 and anchor UE 3 within the time duration specified in clause 12A.3.5 starting from the beginning of time interval T2. UE also performs and report to LMF the SL RSTD measurements for anchor UE 2 and anchor UE 3 with respect to the reference anchor UE 1, within the time duration specified in clause 12A.2.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each anchor UE observed during repeated tests shall be at least 90%, where the reported SL PRS-RSRP measurement for each correct event shall be within the SL PRS-RSRP reporting range specified in clause 10.4A.3.1.1, i.e., between SL_PRS_RSRP_0 and SL_PRS_RSRP_126, and the reported SL RSTD measurement for each correct event shall be within the SL RSTD reporting range specified in clause 10.4A.2.1.1.

## A.9A.1.1.6NR SL PRS-RSRPP measurement reporting delay test case in FR1 SA

## A.9A.1.1.6.1Test Purpose and Environment

The purpose of the test is to verify that the measurement time of both SL PRS PRS-RSRPP and SL Rx-Tx measurements meet the requirements specified in clause 12A.5.5 and 12A.4.5 respectively in an environment with two-tap propagation conditions in FR1 in standalone NR scenario, with additionally configured single frequency layer for SL positioning.

The test environment and configurations refer to A.9A.1.1.2, except that the propagation shall be two-tap channel. And if UE passes this test case, then UE does not need to take the reporting delay test case with SL Rx-Tx measurement only defined in A.9A.1.1.2.

## A.9A.1.1.6.2Test Requirements

The SL PRS-RSRPP and SL Rx-Tx measurement times fulfil the requirements specified in clause 12A.5.5 and 12A.4.5, respectively.

The UE shall perform and report to LMF the SL PRS-RSRPP measurements for anchor UE 2 and anchor UE 3 within the time duration specified in clause 12A.5.5 starting from the beginning of time interval T2. UE also performs and report to LMF the SL Rx-Tx measurements for anchor UE 2 and anchor UE 3 within the time duration specified in clause 12A.4.5 starting from the beginning of time interval T2.

NOTE:The actual overall delays measured in the test may be up to 2xTTIDCCH higher than the time duration above because of TTI insertion uncertainty of the measurement report in DCCH.

The rate of the correct events for each anchor UE observed during repeated tests shall be at least 90%, where the reported SL PRS-RSRPP measurement for each correct event shall be within the SL PRS-RSRPP reporting range specified in clause 10.4A.5.1.1, i.e., between SL_PRS_RSRPP_0 and SL_PRS_RSRPP_126, and the reported SL Rx-Tx measurement for each correct event shall be within the SL Rx-Tx reporting range specified in clause 10.4A.4.1.1.

## A.9A.1.2Measurement Accuracy Tests

## A.9A.1.2.1NR SL RSTD measurement accuracy test case in FR1 SA

## A.9A.1.2.1.1Test Purpose and Environment

The purpose of the test is to verify that the SL RSTD measurement meets the accuracy requirements specified in clause 10.4A.2 in an environment with AWGN propagation conditions in FR1 in standalone NR scenario, with additionally configured single frequency layer for SL positioning.

This test is applicable for UEs supporting NR Uu and V2X or 5G ProSe operation, which are capable of performing SL RSTD measurements.

The supported NR Uu test configurations are specified in table A.9A.1.2.1.1-1.

Table A.9A.1.2.1.1-1: Supported test configurations for FR1 NR Cell 1

The supported NR SL test configurations are specified in table A.9A.1.2.1.1-2.

Table A.9A.1.2.1.1-2: Supported test configurations for NR SL UEs

In the test, there is one target UE receiving SL-PRS and performing SL RSTD measurements and two anchor UEs (anchor UE 1 and anchor UE 2) transmitting SL-PRS for the SL RSTD measurements on NR SL RF channel 2. Anchor UE 1 is the reference anchor UE for the measurements. The target UE and all the anchor UEs are in RRC_CONNECTED state, with Cell 1 as their PCell in FR1 on NR Uu RF channel 1. Cell 1 is also the synchronization source of the target UE and all anchor UEs in the test.

The test consists of two consecutive time intervals, with duration of T1 and T2. Before T2 starts, the UEs have been synchronized to Cell 1. During time duration T1, the target UE shall not have any timing information of anchor UE 2. All two anchor UEs transmit SL-PRS during T2.

The SL-TDOA-ProvideAssistanceData and SL-TDOA-RequestLocationInformation as defined in TS 38.355 [37, clause 6.9], shall be provided to the target UE via Cell 1 during T1. The last TTI containing the two messages shall be provided to the target UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the SL-TDOA assistance data and location information request.

The general test parameters are listed in table A.9A.1.2.1.1-3. NR Uu specific test parameters for Cell 1 and NR Uu UE-specific test parameters for all UEs in the test are listed in table A.9A.1.2.1.1-4 and A.9A.1.2.1.1-5, respectively. Anchor UE specific test parameters for SL RSTD measurement accuracy during T1 and T2 are listed in table A.9A.1.2.1.1-6.

Table A.9A.1.2.1.1-3: General test parameters for SL RSTD measurement accuracy test

Table A.9A.1.2.1.1-4: NR Uu specific test parameters for Cell 1

Table A.9A.1.2.1.1-5: NR Uu UE-specific test parameters for UE 0, UE 1, and UE 2

Table A.9A.1.2.1.1-6: Anchor UE specific test parameters on the SL carrier

## A.9A.1.2.1.2Test Requirements

In each test, the SL RSTD measurement for anchor UE 2 shall fulfil the absolute accuracy requirement in clause 10.4A.2.2.

## A.9A.1.2.2SL Rx-Tx measurement accuracy test case in FR1

## A.9A.1.2.2.1Test Purpose and Environment

The purpose of the test is to verify that the SL Rx-Tx measurement meets the accuracy requirements specified in clause 10.4A.4 in an environment with AWGN propagation conditions in FR1 in standalone NR scenario, with additionally configured single frequency layer for SL positioning.

This test is applicable for UEs supporting NR Uu and V2X or 5G ProSe operation, which are capable of performing SL Rx-Tx measurements.

The supported NR Uu test configurations in FR1 are shown in table A.9A.1.2.2.1-1.

Table A.9A.1.2.2.1-1: Supported Test Configurations for FR1 NR cell

The supported NR SL test configurations are specified in table A.9A.1.2.2.1-2.

Table A.9A.1.2.2.1-2: Supported test configurations for NR SL UEs

There is one NR active cell (Cell 1) and three active UEs (one target UE and two anchor UEs for SL positioning measurement) in this test. The target UE receives SL-PRS and performs the SL Rx-Tx time difference measurement. The two anchor UEs transmit the SL-PRS for the SL Rx-Tx time difference measurement on NR SL RF channel 2. The target UE and all anchor UEs are in RRC_CONNECTED state, with Cell 1 as their PCell in FR1 on NR Uu RF channel 1.

The test consists of two successive time periods, with time duration of T1 and T2 respectively. Before T2 starts, the UEs have been synchronized to the NR serving cell. And during T2, two anchor UEs transmit SL-PRS for positioning measurements.

The SL-RTT-ProvideAssistanceData and SL-RTT-RequestLocationInformation as defined in TS 38.355 [37, clause 6.9], shall be provided to the target UE via Cell 1 during T1. The last TTI containing the two messages shall be provided to the target UE T ms before the start of T2, where T = 50 ms is the maximum processing time of the SL-RTT assistance data and location information request.

The test parameters are given in table A.9A.1.2.2.1-3, A.9A.1.2.2.1-4, A.9A.1.2.2.1-5 and table A.9A.1.2.2.1-6 below.

Table A.9A.1.2.2.1-3: General Test Parameters for SL Rx-Tx measurement reporting delay

Table A.9A.1.2.2.1-4: NR Uu specific test parameters for Cell 1

Table A.9A.1.2.2.1-5: NR Uu UE-specific test parameters for UE 0, UE 1 and UE 2

Table A.9A.1.2.2.1-6: Anchor V2X UE specific test parameters for SL Rx-Tx measurement

## A.9A.1.2.2.2Test Requirements

The SL Rx-Tx time difference measurement fulfils the UE Rx-Tx measurement accuracy requirements specified in clause 10.4A.4.2 for both anchor UE 1 and anchor UE 2.

## A.9A.1.2.3NR SL PRS-RSRP measurement accuracy test case in FR1 SA

## A.9A.1.2.3.1Test Purpose and Environment

The purpose of the test is to verify that the SL PRS PRS-RSRP measurement accuracy meets the requirements specified in clause 10.4A.3.2 in an environment with AWGN propagation conditions in FR1 in standalone NR scenario, with additionally configured single frequency layer for SL positioning.

The test environment and configurations refer to A.9A.1.2.1. During the test, both SL RSTD and SL PRS-RSRP measurements are requested by LMF.

## A.9A.1.2.3.2Test Requirements

In each test, the PRS-RSRP measurement accuracies shall fulfil the accuracy requirement defined in clause 10.4A.3.2.

## A.9A.1.2.4NR SL PRS-RSRPP measurement accuracy test case in FR1 SA

## A.9A.1.2.4.1Test Purpose and Environment

The purpose of the test is to verify that the SL PRS PRS-RSRPP measurement accuracy meets the requirements specified in clause 10.4A.5.2 in an environment with two-tap propagation conditions in FR1 in standalone NR scenario, with additionally configured single frequency layer for SL positioning.

The test environment and configurations refer to A.9A.1.2.2, except that the propagation shall be two-tap channel. During the test, both SL Rx-Tx and SL PRS-RSRPP measurements are requested by LMF.

## A.9A.1.2.4.2Test Requirements

In each test, the PRS-RSRPP measurement accuracies shall fulfil the accuracy requirement defined in clause 10.4A.5.2.
