---
type: spec
aliases:
  - 38.133_38133-j50_sA.705-A.705
tags:
  - 3gpp
  - rel19
  - processed
  - protocol-text
source_spec: "3GPP_Rel19/processed/TS_38.133_38133-j50_sA.705-A.705/content.md"
---
# TS 38.133 38133-j50_sA.705-A.705

## A.7.5Signaling characteristics

## A.7.5.1Radio link Monitoring

In the following clause, any uplink signal transmitted by the UE is used for detecting the In-/Out-of-Sync state of the UE. In terms of measurement, the uplink signal is verified on the basis of the UE output power:

Editor note: The metric for the detection of the UE UL transmitted signal by the TE is FFS.

## A.7.5.1.1Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode

## A.7.5.1.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.7.5.1.1.1-1. The test parameters are given in Tables A.7.5.1.1.1-2, A.7.5.1.1.1-3, and A.7.5.1.1.1-4 below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.5.1.1.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states, and Figure A.7.5.1.1.1-2 shows the Time multiplexed downlink transmissions from each Angle of Arrival. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In addition to RLM-RS radio link monitoring using SSB index 0 and SSB index 1, the UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

Table A.7.5.1.1.1-1: Supported test configurations for FR2 PCell

Table A.7.5.1.1.1-2: General test parameters for FR2 out-of-sync testing in non-DRX mode

Table A.7.5.1.1.1-3: OTA related cell specific test parameters for FR2 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode

Table A.7.5.1.1.1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

Figure A.7.5.1.1.1-1: SNR variation for out-of-sync testing

Figure A.7.5.1.1.1-2: Time multiplexed downlink transmissions

## A.7.5.1.1.2Test Requirements

The UE behavior in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.1.2Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode

## A.7.5.1.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.7.5.1.2.1-1.The test parameters are given in Tables A.7.5.1.2.1-2, and A.7.5.1.2.1-3 below. There is one cell (Cell 1), which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.1.2.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states, and Figure A.7.5.1.2.1-2 shows the Time multiplexed downlink transmissions from each Angle of Arrival. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms.

Table A.7.5.1.2.1-1: Supported test configurations for FR2 PCell

Table A.7.5.1.2.1-2: General test parameters for FR2 in-sync testing in non-DRX mode

Table A.7.5.1.2.1-3: OTA related cell specific test parameters for FR2 (Cell 1) for in-sync radio link monitoring tests in non-DRX mode

Table A.7.5.1.2.1-4: Void

Figure A.7.5.1.2.1-1: SNR variation for in-sync testing

Figure A.7.5.1.2.1-2: Time multiplexed downlink transmissions

## A.7.5.1.2.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.1.3Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode

## A.7.5.1.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.7.5.1.3.1-1. The test parameters are given in Tables A.7.5.1.3.1-2, and A.7.5.1.3.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.5.1.3.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.5.1.3.1-1: Supported test configurations for FR2 PCell

Table A.7.5.1.3.1-2: General test parameters for FR2 out-of-sync testing in DRX mode

Table A.7.5.1.3.1-3: OTA related cell specific test parameters for FR2 (Cell 1) for out-of-sync radio link monitoring tests in DRX mode

Table A.7.5.1.3.1-4: Void

Table A.7.5.1.3.1-5: Void

Figure A.7.5.1.3.1-1: SNR variation for out-of-sync testing

## A.7.5.1.3.2Test Requirements

The UE behavior in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.1.4Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode

## A.7.5.1.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when DRX is used. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.7.5.1.4.1-1. The test parameters are given in Tables A.7.5.1.4.1-2, and A.7.5.1.4.1-3. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.1.4.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CSI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.5.1.4.1-1: Supported test configurations for FR2 PCell

Table A.7.5.1.4.1-2: General test parameters for FR2 in-sync testing in DRX mode

Table A.7.5.1.4.1-3: OTA related cell specific test parameters for FR2 (Cell 1) for in-sync radio link monitoring test in DRX mode

Table A.7.5.1.4.1-4: Void

Table A.7.5.1.4.1-5: Void

Figure A.7.5.1.4.1-1: SNR variation for in-sync testing

## A.7.5.1.4.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.1.5Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode

## A.7.5.1.5.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used. This test will partly verify the FR2 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in Tables A.7.5.1.5.1-1, A.7.5.1.5.1-2, A.7.5.1.5.1-3 and A.7.5.1.5.1-4 below. There is one cell, cell 1 which is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.5.1.5.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 10 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40ms) in test. In the test, SSB0 and SSB1 are configured as BFD-RS and are not same as RLM-RS to avoid triggering the beam failure during the RLM test.

Table A.7.5.1.5.1-1: Supported test configurations for FR2 PCell

Table A.7.5.1.5.1-2: General test parameters for FR2 PCell for CSI-RS out-of-sync testing in non-DRX mode

Table A.7.5.1.5.1-3: Cell specific test parameters for FR2 for CSI-RS out-of-sync radio link monitoring in non-DRX mode

Table A.7.5.1.5.1-4: Measurement gap configuration for FR2 CSI-RS out-of-sync radio link monitoring in non-DRX mode

Figure A.7.5.1.5.1-1: SNR variation for CSI-RS out-of-sync testing

## A.7.5.1.5.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 no later than time point C (D1 second after the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.1.6Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode

## A.7.5.1.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used. This test will partly verify the FR2 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in Tables A.7.5.1.6.1-1, A.7.5.1.6.1-2 and A.7.5.1.6.1-3 below. There is one cells, cell 1which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.1.6.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 10 ms. In the test, DRX configuration is not enabled. In the test, SSB0 and SSB1 are configured as BFD-RS and are not same as RLM-RS to avoid triggering the beam failure during the RLM test.

Table A.7.5.1.6.1-1: Supported test configurations for FR2 PCell

Table A.7.5.1.6.1-2: General test parameters for FR2 PCell for CSI-RS in-sync testing in non-DRX mode

Table A.7.5.1.6.1-3: Cell specific test parameters for FR2 for CSI-RS in-sync radio link monitoring in non-DRX mode

Figure A.7.5.1.6.1-1: SNR variation for CSI-RS in-sync testing

## A.7.5.1.6.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.1.7Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode

## A.7.5.1.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when DRX is used. This test will partly verify the FR2 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in Tables A.7.5.1.7.1-1, A.7.5.1.7.1-2, and A.7.5.1.7.1-3 below. There is one cell, cell 1 is the PCell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.5.1.7.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 10 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test. In the test, SSB0 and SSB1 are configured as BFD-RS and are not same as RLM-RS to avoid triggering the beam failure during the RLM test.

Table A.7.5.1.7.1-1: Supported test configurations for FR2 PCell

Table A.7.5.1.7.1-2: General test parameters for FR2 PCell for CSI-RS out-of-sync testing in DRX mode

Table A.7.5.1.7.1-3: Cell specific test parameters for FR2 for CSI-RS out-of-sync radio link monitoring in DRX mode

Figure A.7.5.1.7.1-1: SNR variation for CSI-RS out-of-sync testing

## A.7.5.1.7.2Test Requirements

The UE behaviour during time durations T1, T2, and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 (PCell) at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

The UE shall stop transmitting uplink signal in Cell 1 (PCell) no later than time point C (D1 secondafter the start of the time duration T3) on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.1.8Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode

## A.7.5.1.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when DRX is used. This test will partly verify the FR2 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in Tables A.7.5.1.8.1-1, A.7.5.1.8.1-2, A.7.5.1.8.1-3 and A.7.5.1.8.1-4 below. There is one cells, cell 1which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.1.8.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 10 ms. The UE is configured to perform inter-frequency measurements using GP ID #0 (40ms) in test. In the test, SSB0 and SSB1 are configured as BFD-RS and are not same as RLM-RS to avoid triggering the beam failure during the RLM test.

Table A.7.5.1.8.1-1: Supported test configurations for FR2 PSCell

Table A.7.5.1.8.1-2: General test parameters for FR2 PCell for CSI-RS in-sync testing in non-DRX mode

Table A.7.5.1.8.1-3: Cell specific test parameters for FR2 for CSI-RS in-sync radio link monitoring in non-DRX mode

Table A.7.5.1.8.1-4: Measurement gap configuration for FR2 CSI-RS in-sync radio link monitoring in non-DRX mode

Figure A.7.5.1.8.1-1: SNR variation for CSI-RS in-sync testing

## A.7.5.1.8.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.1.9UE Radio Link Monitoring Scheduling Restrictions on FR2

## A.7.5.1.9.1Test Purpose and Environment

The purpose is to verify that the NR UE correctly follows the RLM scheduling restrictions requirements defined in clause 8.1.7. This test verifies that the UE correctly receive the PDCCH scheduled on the symbols right before the RLM SSB symbols without overlap so that it sends ACK/NACK correctly. The test case is only applicable to UE which supports pdcch-MonitoringAnyOccasions or pdcch-MonitoringAnyOccasionsWithSpanGap.

The test parameters are given in table A.7.5.1.9.1-1, table A.7.5.1.9.1-2 and table A.7.5.1.9.1-3 below. The UE is required during time period T1 to transmit ACK/NACK correctly upon scheduling of PDSCH.

Table A.7.5.1.9.1-1: Supported test configurations

Table A.7.5.1.9.1-2: General test parameters for NR RLM scheduling restriction test case in FR2

Table A.7.5.1.9.1-3: Cell specific test parameters for NR RLM scheduling restriction test case in FR2

Figure A.7.5.1.9.1-1: Time multiplexed downlink transmissions

## A.7.5.1.9.2Test Requirements

The UE behaviour follows the requirements defined in clause 8.1.7.3.

The UE shall be continuously scheduled by PDCCH on the symbols right before each SSB which is not covered by SMTC during the entire length of T1. The UE shall transmit ACK/NACK for every scheduled PDCCH during the time duration T1.

## A.7.5.1.10Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode for UE supporting fast beam sweeping in multi-Rx

## A.7.5.1.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.7.5.1.10.1-1. The test parameters are given in Tables A.7.5.1.10.1-2, and A.7.5.1.10.1-3below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.5.1.10.1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states, and Figure A.7.5.1.10.1-2 shows the Time multiplexed downlink transmissions from each Angle of Arrival. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In addition to RLM-RS radio link monitoring using SSB index 0 and SSB index 1.

Table A.7.5.1.10.1-1: Supported test configurations for FR2 PCell

Table A.7.5.1.10.1-2: General test parameters for FR2 out-of-sync testing in non-DRX mode

Table A.7.5.1.10.1-3: OTA related cell specific test parameters for FR2 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode

Table A.7.5.1.10.1-4: Void

Figure A.7.5.1.10.1-1: SNR variation for out-of-sync testing

Figure A.7.5.1.10.1-2: Time multiplexed downlink transmissions

## A.7.5.1.10.2Test Requirements

The UE behavior in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.1.11Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP

## A.7.5.1.11.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when no DRX is used and when CD-SSB is outside active BWP. This test will partly verify the FR2 PCell CSI-RS Out-of-sync radio link monitoring requirements in clause 8.1.

The test is for UE supporting rlm-BM-BFD-CSI-RS-OutsideActiveBWP-r18 and the UE is not required past legacy test in A.7.5.1.5.

The test environment is the same as in A.7.5.1.5.

NOTE:The starting PRB index of the SSB can be any possible PRB index of the RF channel BW occurring after the last PRB of the DL active BWP.

The test requirements are the same as in A.7.5.1.5.2.

## A.7.5.1.12Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP

## A.7.5.1.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting bwpOperationMeasWithoutInterrupt-r18 properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell when CD-SSB is outside active BWP. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.

The test environment is the same as in A.7.5.1.1 with following exceptions in Table A.7.5.1.1.1-2.

## A.7.5.1.12.2Test Requirements

The test requirements are the same as in A.7.5.1.1.2.

## A.7.5.1.13Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP

## A.7.5.1.13.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects the out of sync and in sync for the purpose of monitoring downlink radio link quality of the PCell. This test will partly verify the FR2 radio link monitoring requirements in clause 8.1.

In the test, UE is configured to perform RLM on SSB, with detectionResource included in RadioLinkMonitoringRS set to SSB#0 and SSB#1, and purpose set to ‘rlf’. Supported test configurations are shown in table A.7.5.1.13 .1-1. The test parameters are given in Tables A.7.5.1.13 .1-2, A.7.5.1.13 .1-3, and A.7.5.1.13 .1-4 below. There is one cell (Cell 1), which is the active NR cell, in the test. The test consists of three successive time periods, with time duration of T1, T2 and T3 respectively. Figure A.7.5.1.13 .1-1 shows the variation of the downlink SNR in the active cell to emulate out-of-sync and in-sync states, and Figure A.7.5.1.13 .1-2 shows the Time multiplexed downlink transmissions from each Angle of Arrival. Prior to the start of the time duration T1, the UE shall be fully synchronized to Cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In addition to RLM-RS radio link monitoring using SSB index 0 and SSB index 1, the UE is configured to perform inter-frequency measurements using Gap Pattern ID #0 (40 ms) in test 1.

Table A.7.5.1.13 .1-1: Supported test configurations for FR2 PCell

Table A.7.5.1.13 .1-2: General test parameters for FR2 out-of-sync testing in non-DRX mode

Table A.7.5.1.13 .1-3: OTA related cell specific test parameters for FR2 (Cell 1) for out-of-sync radio link monitoring tests in non-DRX mode

Table A.7.5.1.13 .1-4: Measurement gap configuration for out-of-sync tests in non-DRX mode

Figure A.7.5.1.13 .1-1: SNR variation for out-of-sync testing

Figure A.7.5.1.13 .1-2: Time multiplexed downlink transmissions

## A.7.5.1.13.2Test Requirements

The UE behavior in each test during time durations T1, T2 and T3 shall be as follows:

During the period from time point A to time point B the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting.

The UE shall stop transmitting uplink signal no later than time point C (D1 second after the start of the time duration T3).

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.1.14Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode  for a UE operating with SBFD

## A.7.5.1.14.1Test Purpose and Environment

The purpose of this test is to verify that when the UE supports supportSBFD and SBFD is configured by the network, the UE properly detects the in sync for the purpose of monitoring downlink CSI-RS based radio link quality of the PCell when there are overlapping between occasions of the CSI-RS resource for RLM and dynamic UL transmission on SBFD symbols. This test will partly verify the FR2 PCell CSI-RS In-sync radio link monitoring requirements in clause 8.1.

The test parameters are given in Tables A.7.5.1.14.1-1, A.7.5.1.14.1-2, A.7.5.1.14.1-3 and A.7.5.1.14.1-4 below. There is one cells, cell 1which is the PCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.1.14.1-1 shows the variation of the downlink SNR in the PCell to emulate out-of-sync and in-sync states. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 10 ms. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test. In the test, SSB0 and SSB1 are configured as BFD-RS.

CSI-RS resource for RLM are on SBFD symbols. During T5, there is overlapping between occasions of the CSI-RS resource for RLM and dynamic UL transmission on SBFD symbols, as specified in A.3.

Table A.7.5.1.14.1-1: Supported test configurations for FR2 PSCell

Table A.7.5.1.14.1-2: General test parameters for FR2 PCell for CSI-RS in-sync testing in DRX mode

Table A.7.5.1.14.1-3: Cell specific test parameters for FR2 for CSI-RS in-sync radio link monitoring in DRX mode

Table A.7.5.1.14.1-4: Measurement gap configuration for FR2 CSI-RS in-sync radio link monitoring in DRX mode

Figure A.7.5.1.14.1-1: SNR variation for CSI-RS in-sync testing

## A.7.5.1.14.2Test Requirements

The UE behaviour in each test during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the period from time point A to time point F (D1 second after the start of time duration T5) the UE shall transmit uplink signal at least in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting on the PCell.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.2Interruption

## A.7.5.2.1Interruptions during measurements on deactivated NR SCC in FR2

## A.7.5.2.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE missed ACK/NACK rate does not exceed the limits at NR PSCell interruptions during the measurement on the deactivated NR SCC. This test will verify the missed ACK/NACK rate for PCell in standalone NR specified in clause 8.2.2.2. Supported test configurations are shown in table A.7.5.2.1.1-1.

The general test parameters and NR cell specific test parameters are given in Table A.7.5.2.1.1-2 and A.7.5.2.1.1-3 below. In the test there are two cells: Cell 1 and Cell 2. Cell 1 is PCell, Cell 2 is an NR deactivated SCell. Cell 1 shall be configured as PCell and Cell 2 shall be configured as SCell.

The test consists of one time period, with duration of T1. Prior to the start of the time duration T1, the UE is connected to Cell 1 and Cell 2. The point in time at which the RRC message including measCycleSCell or allowInterruptions for the deactivated NR SCells is received at the UE antenna connector, defines the start of time period T1. During T1, PCell is continuously scheduled in DL.

Table A.7.5.2.1.1-1: Interruptions during measurements on deactivated NR SCC supported test configurations

Table A.7.5.2.1.1-2: General test parameters for interruptions during measurements on deactivated NR SCC in standalone NR

Table A.7.5.2.1.1-3: NR cell specific test parameters for interruptions during measurements on deactivated NR SCC in standalone NR

Table A.7.5.2.1.1-4: OTA related test parameters for interruptions during measurements on deactivated NR SCC in standalone NR

## A.7.5.2.1.2Test Requirements

The UE shall be continuously scheduled on PCell during the entire length of T1. During the time duration T1 the UE shall transmit at least 99.5 % of ACK/NACK on PCell.

If the NR PCell is not in the same band as the deactivated SCell, the UE is only allowed to cause interruptions on NR PCell immediately before and immediately after an SMTC. Each interruption on NR PCell shall not exceed the value defined in Table A.7.5.2.1.2-1.

If the NR PCell is in the same band as the deactivated SCell, the UE is only allowed to cause an interruption on PCell no earlier than 4 slots before an SMTC and no later than 4 slots after the SMTC. the interruption on NR PCell shall not exceed the value defined in Table A.7.5.2.1.2-2.

Table A.7.5.2.1.2-1: Interruption duration if the PCell is not in the same band as the deactivated SCell

Table A.7.5.2.1.2-2: Interruption duration if the PCell is in the same band as the deactivated SCell

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.2.2SA interruptions at NR SRS carrier-based switching

## A.7.5.2.2.1Test Purpose and Environment

The purpose of this test is to verify that when a UE needs to transmit aperiodic SRS, the UE can perform SRS carrier-based switching to a carrier not configured for PUCCH/PUSCH transmission from a carrier with PUCCH/PUSCH transmission. The test will partly verify the interruption requirements on PCell in clause 8.2.2.2.9.

## A.7.5.2.2.2Test Parameters

In each test there are two cells: Cell 1 and Cell 2. Cell 1 is the FR2 PCell. Cell 2 is an activated FR2 SCell on the TDD SCC which operats in downlink without PUCCH/PUSCH. The UE is configured with the SRS switching between PCell and SCell.The test parameters for PCell and SCell are given in Tables A.7.5.2.2.2-2, A.7.5.2.2.2-3, and A.7.5.2.2.2-4 below. The test consists of two successive time periods, with duration of T1 and T2, respectively. Immediately at the beginning of T2, the UE is triggered for SRS switching by DCI 2_3 scheduling. After T2, the UE is expected to transmit aperiodic SRS on a special slot in the configured TDD UL/DL configuration, as scheduled by DCI 2_3. The UE shall be scheduled on PCell continuously throughout the test.

The test equipment verifies that potential interruption is carried out correctly by monitoring ACK/NACK sent in PCell.

Table A.7.5.2.2.2-1: Supported test configurations

Table A.7.5.2.2.2-2: General test parameters for SA interruptions at NR SRS carrier-based switching

Table A.7.5.2.2.2-3: Cell-specific test parameters for SA interruptions at NR SRS carrier-based switching

Table A.7.5.2.2.2-4: OTA related test parameters

## A.7.5.2.2.3Test Requirements

During T2, interruption on PCell due to SRS carrier-based switching between Cell 1 and Cell 2 shall not exceed the required values specified in clause 8.2.2.2.9.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.3SCell Activation and Deactivation Delay

## A.7.5.3.1SCell Activation and deactivation for SCell in FR2 intra-band in non-DRX

## A.7.5.3.1.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.6.5.3.1.1 except the PCell and SCell are in FR2 intra-band.

The supported test configurations are shown in table A.7.5.3.1.1-1 below. The general test parameters are the same as defined in Table A.6.5.3.1.1-2 except those described in Tables A.7.5.3.1.1-2, and cell specific test parameters are described in Tables A.7.5.3.1.1-3. OTA related test parameters are shown in table A.7.5.3.1.1-4 below.

Table A.7.5.3.1.1-1: Supported test configurations for FR2 SCell activation case

Table A.7.5.3.1.1-2: General test parameters for FR2 SCell activation case

Table A.7.5.3.1.1-3: Cell specific test parameters for FR2 SCell activation case

Table A.7.5.3.1.1-4: OTA related test parameters for FR2 SCell activation case

## A.7.5.3.1.2Test Requirements

The test requirements defined in clause A.6.5.3.1.2 shall apply to this test case, except Tactivation_time will be replaced with the value TFirstSSB + 5 ms as defined in clause 8.3.

## A.7.5.3.2SCell Activation and deactivation for FR1+FR2 inter-band with target SCell in FR2

## A.7.5.3.2.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.7.5.3.1.1 except the PCell is in FR1 and SCell is in FR2.

The supported test configurations are defined in Table A.7.5.3.2.1-1. The general test parameters are the same as defined in Table A.6.5.3.1.1-2 except that the length of T2 is 2 s. And cell specific test parameters are described in Tables A.7.5.3.2.1-2. OTA related test parameters are defined in Table A.7.5.3.2.1-3.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on NR. During T1 the SCell is powered off and UE is not aware of SCell.

A MAC message for activation of SCell is sent by the test equipment 100 ms after the RRC message, in a slot # denoted m. The point in time at which the MAC message for activation of SCell is received at the UE antenna connector defines the start of time period T2.

During T2, the test equipment monitors the L1-RSRP measurement reporting for the SCell. The time when test equipment receives a valid L1-RSRP report is denoted as slot m+TL1-RSRP. In the next DL slot after slot m+TL1-RSRP, the test equipment sends a MAC message for the activation of the TCI state of the RMC CORESET of the SCell. In the same slot, the test equipment also sends an RRC message to configure the CSI-RS resources for SCell.

Time period T3 starts when a MAC message for deactivation of the SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell and PCell during activation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell 1 deactivation command is sent until CSI reporting for SCell 1 is discontinued.

Table A.7.5.3.2.1-1: Supported test configurations for FR2 SCell activation case

Table A.7.5.3.2.1-2: Cell specific test parameters for FR2 SCell activation case

Table A.7.5.3.2.1-3: OTA related test parameters for FR1 PCell activation case with FR2 SCell

## A.7.5.3.2.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in 5.2.2.5 in [26], and reporting after slot (m+k). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.  Whether CSI report in a slot was interrupted is checked by monitoring ACK/NACK sent in PCell in the slot.

During T2 the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than

## 3 ms + TFirstSSB_MAX + 15*TSMTC_MAX + 8*Trs + TL1-RSRP, measure + TL1-RSRP, report

as defined in clause 8.3.2. For this test case, TFirstSSB_MAX=TSMTC_MAX=Trs=20 ms; TL1-RSRP, measure=160 ms and TL1-RSRP, report=5 ms, which allows TL1-RSRP 680 ms.

During T2 the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

- THARQ is defined in Table A.5.5.3.1.1-2

- Tactivation_time = 3 ms + TFirstSSB_MAX + 15*TSMTC_MAX + 8*Trs + TL1-RSRP, measure + TL1-RSRP, report + max {(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)}, which allows 710 ms

- TCSI_Reporting = 10 ms

- NR slot length is 0.125 ms for this test case.

During T3 the UE shall stop sending CSI reports for both SCells no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

During T2 interruption of PCell during SCell activation shall not happen outside the slot   to , as defined in clause 8.3, where TX =20 ms. m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

The interruption of PCell due to activation of SCell shall not be more than the values specified for SA in Clause 8.2.2.2.7.

## A.7.5.3.3SCell Activation and deactivation for SCell in FR2 inter-band in non-DRX

## A.7.5.3.3.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.7.5.3.1.1 except the PCell and SCell are in FR2 inter-band.

The supported test configurations are shown in table A.7.5.3.3.1-1 below. The general test parameters are described in Tables A.7.5.3.3.1-2, and cell specific test parameters are described in Tables A.7.5.3.3.1-3. OTA related test parameters are shown in table A.7.5.3.3.1-4 below.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on NR. During T1 the SCell is powered off and UE is not aware of SCell. A MAC message for activation of SCell is sent by the test equipment 100 ms after the RRC message, in a slot # denoted m.

The point in time at which the MAC message for activation of SCell is received at the UE antenna connector defines the start of time period T2. Immediately at beginning of T2 the transmission power of Cell 2 is increased to same level as for PCell. During T2, the test equipment monitors the L1-RSRP measurement reporting for the SCell. The time when test equipment receives a valid L1-RSRP report is denoted as slot m+TL1-RSRP. In the next DL slot after slot m+TL1-RSRP, the test equipment sends a MAC message for the activation of the TCI state of the RMC CORESET of the SCell. In the same slot, the test equipment also sends an RRC message to configure the CSI-RS resources for SCell.

Time period T3 starts when a MAC message for deactivation of the SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell 1 deactivation command is sent until CSI reporting for SCell is discontinued.

Table A.7.5.3.3.1-1: Supported test configurations for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.3.1-2: General test parameters for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.3.1-3: Cell specific test parameters for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.3.1-4: OTA related test parameters for FR2 SCell activation in FR2 inter-band

## A.7.5.3.3.2Test Requirements

During T2 the UE shall start sending CSI report for the SCell in the configured slots for CSI reporting after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k). UE shall send the first CSI report for SCell after receiving at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k), or in the next available uplink resource for CSI reporting if the slot was subject to interruption. Whether CSI report in a slot was interrupted is checked by monitoring ACK/NACK sent in PCell in the slot.

During T2, the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than 3 ms + TFirstSSB_MAX + 15*TSMTC_MAX + 8*Trs + TL1-RSRP, measure + TL1-RSRP, report as defined in clause 8.3.2. For this test case, TFirstSSB_MAX=TSMTC_MAX=Trs=20 ms; TL1-RSRP, measure=480 ms and TL1-RSRP, report=5 ms, which allows TL1-RSRP =1000 ms.

During T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

-THARQ is defined in Table A.7.5.3.3.1-2

-Tactivation_time = 3 ms + TFirstSSB_MAX + 15*TSMTC_MAX + 8*Trs + TL1-RSRP, measure + TL1-RSRP, report + max {(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)}, which allows 1030 ms

-TCSI_Reporting = 10 ms

-NR slot length is 0.125 ms for this test case.

During T2, the interruption of PCell during SCell activation shall not happen outside the slot   to , where TX =20 ms. m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length

During T3, the UE shall stop sending CSI reports for SCell no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

During T3, the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to  as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

## A.7.5.3.4Direct SCell activation at SCell addition of known SCell in FR2

## A.7.5.3.4.1Test Purpose and Environment

The purpose of this test is to verify that the delay and interruption for direct SCell activation delay at SCell addition are within the requirements stated in clause 8.3.4.

The supported test configurations are shown in Table A.7.5.3.4.1-1 below. The general test parameters are given in Table A.7.5.3.4.1-2 and cell-specific test parameters in Table A.7.5.3.4.1-3. OTA related test parameters are shown in Table A.7.5.3.4.1-4.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two FR2 carriers and two NR cells. Before the test starts the UE is connected to Cell 1 (PCell) on carrier #1, but is not aware of Cell 2 on NR carrier #2. Cell 1 and Cell 2 have constant signal levels throughout the test. The UE is monitoring the PCell. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the Cell 2 is monitored by the UE. During T1, Cell 2 should be detected and measured by the UE such that it meets the condition for known cell defined in clause 8.3.4 for direct SCell activation.

Time period T2 starts when the RRCReconfiguration message for the configuration and activation of Cell 2 (the SCell), which is sent from the test equipment, is received at the UE antenna connector in a slot # denoted m. The test equipment shall set the parameter sCellState to activated for the SCell, which causes Cell 2 to become configured and activated.

Time period T3 starts at (m + Ndirect), at which point UE shall be reporting a valid CQI for both PCell and SCell.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during the activation of SCell. The test equipment verifies the activation time by counting the slots from the time when the SCell activation message is sent until a CQI report with other than CQI index 0 is received.

Table A.7.5.3.4.1-1: Supported test configurations

Table A.7.5.3.4.1-2: General test parameters

Table A.7.5.3.4.1-3: Cell specific test parameters

Table A.7.5.3.4.1-4: OTA related test parameters

## A.7.5.3.4.2Test Requirements

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

## A.7.5.3.5Direct SCell activation at handover with known SCell in FR2

## A.7.5.3.5.1Test Purpose and Environment

This test is to verify the requirements specified in sub clause 8.3.5 for the FR2 intra-frequency handover with direct SCell activation.

The test scenario comprises of three FR2 cells, one source PCell (Cell 1), one target PCell (Cell 2) and one SCell (Cell 3). The test consists of three successive time periods, with time durations of T1, T2, and T3 respectively.

At the start of time duration T1, the UE is in connected mode with PCell (Cell 1). Both Cell 2 and Cell 3 are known to UE and UE is reporting CQI for all Cell 1.

Time period T2 starts when UE receives a handover command that initiate handover of UE to Cell 2 and also activates Cell 3. This is done using an RRCConnectionReconfiguration message with parameter sCellState set to activated for the Cell 3. The message is sent from the test equipment to the UE and is received in a slot number n at the UE antenna connector. The UE shall accomplish the handover, addition and activation of the SCell no later than slot (n +). NdirectNR slot length

Time period T3 starts at (n +), at which point UE shall be reporting a valid CSI for both Cell 2 and Cell 3 as given in tables A.7.5.3.5.1-1 and A.7.5.3.5.1-2.NdirectNR slot length

Table A.7.5.3.5.1-1: Supported test configurations for FR2 handover with direct SCell activation case

Table A.7.5.3.5.1-2: General test parameters for FR2 handover with direct SCell activation case

Table A.7.5.3.5.1-3: Cell specific test parameters for FR2 SCell activation case

Table A.7.5.3.5.1-4: OTA related test parameters for FR2 SCell activation case

## A.7.5.3.5.2Test Requirements

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

## A.7.5.3.6PUCCH SCell activation and deactivation for FR1+FR2 inter-band with target SCell in FR2 and known

## A.7.5.3.6.1Test Purpose and Environment

The purpose of this test is to verify that the PUCCH SCell activation and deactivation times are within the requirements stated in clause 8.3.12 and 8.3.14, when the PUCCH SCell in FR2 is known by the UE at the time of activation.

The supported test configurations are shown in table A.7.5.3.6.1-1 below. The test parameters are given in Tables A.7.5.3.6.1-2 and cell-specific parameters in A.7.5.3.6.1-3 below. The test consists of four successive time periods, with duration of T1, T2 T3, and T4 respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the PUCCH SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the PUCCH SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI for the activated PUCCH SCell at latest in slotn+ , and report valid CSI for the activated DL SCell at latest in slotn+, as defined in clause 8.3.13. In this test case, both valid TA and invalid TA cases shall be tested. THARQ+Tdelay_multiple_SCells_PUCCH_SCellNR slot length THARQ+Tdelay_multiple_SCells_other_SCellNR slot length

Test for case when UE has valid TA: the TimeAlignmentTimer [2] associated with the TAG containing the PUCCH SCell is running, and Tdelay_multiple_SCells_PUCCH_SCell = Tactivation_time_multiple_scells + [X]*Ttarget_PL_RS + TCSI_Reporting.

Test for case when UE do not have valid TA: Tdelay_multiple_SCells_PUCCH_SCell = Tactivation_time_multiple_scells + max ((TFirst_available_CSI + TCSI_processing), [X]*Ttarget_PL_RS, (T1+T2+T3)) + TCSI_reporting_after

Tactivation_time_multiple_scells is the target SCell activation delay in millisecond in multiple SCell activation scenario as specified in clause 8.3.7

Any PCell interruption due to activation of PUCCH SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of PUCCH SCell abd DL SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3.14and the starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.14.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of PUCCH SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.7.5.3.6.1-1: Supported test configurations for FR2 SCell activation case

Table A.7.5.3.6.1-2: Cell specific test parameters for FR2 SCell activation case

Table A.7.5.3.6.1-3: OTA related test parameters for FR2 SCell with FR1 PCell

## A.7.5.3.6.2Test Requirements

By end of T2 the UE shall finish the DL activation for the PUCCH SCell. Assuming the periodic CSI reporting is used and assuming periodic CSI activation and TCI state is sent along with SCell activation MAC CE, UE shall finish the DL activation by slot n+ 10 ms + THARQ + TFineTiming

With SSB periodicity of 20 ms, UE shall complete DL activation of PUCCH SCell with in 30 ms after transmitting HARQ message for SCell activation command.

During T2 the UE shall start sending PRACH preamble to TE and shall obtain the TA command from TA and shall be ready to send valid CSI report to the TE. CSI report shall be transmitted within 30 ms + [X=0] + max ((TFirst_available_CSI + TCSI_processing), (T1+T2+T3)) + TCSI_reporting_after from the transmission of HARQ feedback of SCell activation command as specified in the 8.3.12.

During T3 the UE shall stop sending CSI reports for both SCells no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

During T2 interruption of PCell during SCell activation shall not happen outside the slot   to , as defined in clause 8.3, where TX =20 ms. m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

The interruption of PCell due to activation of SCell shall not be more than the values specified for SA in Clause 8.2.2.2.7.

## A.7.5.3.7PUCCH SCell activation and deactivation delay requirements of FR2 unknown cell with FR1 PCell

## A.7.5.3.7.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.7.5.3.7.1 except the PUCCH SCell in FR2 is unknown.

The supported test configurations and the general test parameters are defined in Table A.7.5.3.7.1-1 and Table A.7.5.3.7.1-2, respectively. And cell specific test parameters are described in Tables A.7.5.3.7.1-3. OTA related test parameters are defined in Table A.7.5.3.7.1-4. In all test cases, two cells are used. Cell 1 is the FR1 PCell in the primary Timing Advance Group (pTAG) and cell 2 is the FR2 PUCCH SCell in the secondary Timing Advance Group (sTAG).

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on NR. During T1 the SCell is powered off and UE is not aware of SCell.

A MAC message for activation of SCell is sent by the test equipment T1 after the RRC message, in a slot # denoted m. The point in time at which the MAC message for activation of SCell is received at the UE antenna connector defines the start of time period T2. At the time of T2, the UE does not have a valid TA for the SCell in sTAG. Immediately at the beginning of T2 the transmission power of Cell 2 is increased to same level as for cell 2

During T2, the test equipment monitors the L1-RSRP measurement result for the SCell reported on the PCell. The time when test equipment receives a valid L1-RSRP report is denoted as slot m+TL1-RSRP. In the next DL slot after slot m+TL1-RSRP, the test equipment sends a MAC message for the activation of the TCI state of the RMC CORESET of the SCell and PUCCH-SpatialRelation of the SCell. In the same slot, the test equipment also sends an RRC message to configure the CSI-RS resources for SCell. THARQ + Tactivation_time after slot m, the UE shall be able to monitor PDCCH on the SCell that triggers PDCCH order-based contention-free PRACH. The test equipment receives the PRACH and sends random access response with Timing Advance Command MAC Control Elements for sTAG, with Timing Advance Command value estimated from the PRACH. The UE shall start reporting CSI of the SCell with non-zero CQI index via PUCCH on the SCell no later than slot m + (THARQ + Tdelay_PUCCH_SCell)/NR slot length. Here, Tactivation_time is the SCell activation delay defined in 8.3.2 for FR2 unknown SCell with periodic CSI-RS used for CSI reporting, and Tdelay_PUCCH_SCell is the PUCCH SCell activation delay defined in 8.3.12 for an invalid TA scenario.

Time period T3 starts when a MAC message for deactivation of the SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during the activation of the SCell.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CSI reporting on the SCell is discontinued.

Table A.7.5.3.7.11: Supported test configurations for FR2 SCell activation case

Table A.7.5.3.7.1-2: General test parameters for unknown FR2 PUCCH SCell activation case

Table A.7.5.3.7.1-3: Cell specific test parameters for FR2 PUCCH SCell activation case

Table A.7.5.3.7.1-4: OTA related test parameters for FR2 PUCCH SCell activation

## A.7.5.3.7.2Test Requirements

During T2 the UE shall start sending a valid L1-RSRP report of the SCell to the PCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than 3 ms + TFirstSSB_MAX + 15*TSMTC_MAX + 8*Trs + TL1-RSRP, measure + TL1-RSRP, report as defined in clause 8.3.2.

During T2 the UE shall start sending CSI reports of the SCell with non-zero CQI index via PUCCH on the SCell in the configured slots for CSI reporting no later than slot  as defined in clause 8.3.12.m+THARQ+Tdelay_PUCCH_SCellNR slot length

During T3 the UE shall stop sending CSI reports on the SCell no later than slot , as defined in clause 8.3.14.n+THARQ+3 msNR slot length

During T2 interruption of PCell during the SCell activation shall not happen outside the slot   to , as defined in clause 8.3, where TX =20 ms. If the UE is not capable of parallelTxPRACH-SRS-PUCCH-PUSCH additional interruption can be allowed as defined in Clause 8.2.2.2.18.m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.14.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

The interruption of PCell due to activation of SCell shall not be more than the values specified for SA in Clause 8.2.2.2.18.

## A.7.5.3.8SCell Activation and deactivation for known PUCCH SCell in FR2 inter-band in non-DRX

## A.7.5.3.8.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements specified in clause 8.3, when PUCCH for a being activated SCell is configured on the SCell. The PCell and SCell are inter-band in FR2 and the SCell is known by a UE. The test shall be performed for the cases respectively where UE has valid TA and where UE does not have valid TA for an sTAG which the SCell belongs to at the time of activation.

The supported test configurations are shown in table A.7.5.3.8.11-1 below. The general test parameters are described in Tables A.7.5.3.8.1-2, and cell specific test parameters are described in Tables A.7.5.3.8.1-3. OTA related test parameters are shown in table A.7.5.3.8.1-4 below.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. The UE shall be continuously scheduled in the PCell (Cell 1) throughout the whole test.

Before the test starts, the UE is connected to the Cell 1 (PCell) on radio channel 1 but is not aware of Cell 2 (SCell) on radio channel 2. The PCell is in the pTAG and the SCell is in an sTAG. The UE is only monitoring the PCell.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured with PUCCH on radio channel 2. The UE now starts monitoring the Cell 2. During T1, Cell 2 should be detected and measured by the UE such that it meets the condition for known cell defined in clause 8.3.2 for SCell activation.

A MAC message for activation of SCell is sent by the test equipment in a slot # denoted m. The point in time at which the MAC message for activation of SCell is received at the UE antenna connector defines the start of time period T2.

During T2,

-When the UE has a valid TA, the UE shall be able to report valid CSI for the activated SCell no later than in slot n+,  as defined in clause 8.3.12. THARQ+Tactivation_time+X*Ttarget_PL-RS+TCSI_ReportingNR slot length

-When the UE does not have a valid TA, the test equipment should send a PDCCH order to the UE to initiate RA procedure on the PUCCH SCell no later than in slot n+,  and the UE shall be able to report valid CSI for the activated SCell no later than in slot , as defined in clause 8.3.12. THARQ+Tactivation_timeNR slot lengthn+THARQ+Tdelay_PUCCH_SCellNR slot length

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3, and the starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.n+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and the deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received from the PUCCH SCell.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting from the PUCCH SCell is discontinued.

Table A.7.5.3.8.1-1: Supported test configurations for FR2 PUCCH SCell activation in FR2 inter-band

Table A.7.5.3.8.1-2: General test parameters for known PUCCH SCell activation in FR2 inter-band

Table A.7.5.3.8.1-3: Cell specific test parameters for FR2 PUCCH SCell activation in FR2 inter-band

Table A.7.5.3.8.1-4: OTA related test parameters for FR2 SCell activation in FR2 inter-band

## A.7.5.3.8.2Test Requirements

During T2, when the UE has valid TA, the UE shall start sending CSI report for the SCell with non-zero CQI index on the PUCCH SCell no later than in slot n+,  where Tactivation_time is max(Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay-THARQ) as defined in clause 8.3.2, which allows 5 ms.THARQ+Tactivation_time+X*Ttarget_PL-RS+TCSI_ReportingNR slot length

If the UE has a valid TA for transmitting on the SCell, during T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting on PUCCH SCell no later than slot , where m+THARQ+Tactivtion_time+X*Ttarget_PL-RS+TCSI_ReportingNR slot length

-THARQ is defined in Table A.4.5.3.1.1-2

-Tactivation_time = max(Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay-THARQ), which allows 5 ms

-TCSI_Reporting = 10 ms

-NR slot length is 0.125 ms for this test case.

If the UE does not have a valid TA for transmitting on the SCell, during T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tdelay_PUCCH_SCellNR slot length

-THARQ is defined in Table A.4.5.3.1.1-2

-Tdelay_PUCCH_SCell = Tactivation_time + max ((TFirst_available_CSI + TCSI_processing), (T1+T2+T3), [X]*Ttarget_PL-RS) + TCSI_reporting_after

-FFS the value of T1+T2+T3 and TCSI_reporting_after

-NR slot length is 0.125 ms for this test case.

During T2 interruption of PCell / PSCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length+Ninterruption

During T3 the UE shall stop sending CSI reports for SCell at latest in a slot n, as defined in clause 8.3.+THARQ+3 msNR slot length

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

## A.7.5.3.9PUCCH SCell Activation and deactivation of unknown SCell in FR2

## A.7.5.3.9.1Test Purpose and Environment

The purpose of this test is to verify that SCell activation and deactivation are done within the required time period defined in clause 8.3.12, when PUCCH for a being activated SCell is configured on the NR FR2 SCell. The PCell and SCell are in different FR2 band. The SCell is unknown by the UE and the UE does not have valid TA for a sTAG which the SCell belongs to at the time of activation. Supported test configurations are shown in table A.7.5.3.9.1-1.

The general test parameters and NR cell specific test parameters are given in Table A.7.5.3.9.1-2 and A.7.5.3.9.1-3 below. OTA related test parameters are shown in table A.7.5.3.9.1-4 below.

In the test there are two cells: Cell 1 and Cell 2. Cell 1 is PCell, Cell 2 is the PUCCH SCell being activated and deactivated. The test consists of three successive time periods with duration of T1, T2 and T3, respectively. The UE shall be continuously scheduled in Cell 1 (PCell) throughout the test.

Before the test starts, the UE is connected to the PCell (Cell 1) on NR radio channel 1 (PCC), but is not aware of SCell (Cell 2) on NR radio channel 2 (SCC). The PCell is in the pTAGs and the SCell is in a sTAG. The UE is only monitoring the PCC.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) gets configured with PUCCH on NR radio channel 2 (SCC). The UE now starts monitoring the SCC2 also. Test equipment sends a MAC message for activation of the SCell. The MAC message for the activation is received at the UE antenna connector at slot # denoted m, which is defined as the start of time period T2.

Immediately at beginning of T2 the transmission power of Cell 2 is increased to same level as for Cell 1. During T2, the test equipment monitors the L1-RSRP measurement reporting for the SCell. The time when test equipment receives a valid L1-RSRP report is denoted as slot m+TL1-RSRP. In the next DL slot after slot m+TL1-RSRP, the test equipment sends a MAC message for the activation of the TCI state of the RMC CORESET of the SCell. In the same slot, the test equipment also sends an RRC message to configure the CSI-RS resources for SCell. During T2, the test equipment should send a PDCCH order to the UE to initiate RA procedure on the PUCCH SCell at slot (m+) after UE report on PCell.THARQ+Tactivation_timeNR slot length

Time period T3 starts when a MAC message for deactivation of the PUCCH SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CSI reporting for SCell is discontinued.

Table A.7.5.3.9.1-1: PUCCH SCell Activation and deactivation test configurations in FR2 inter-band

Table A.7.5.3.9.1-2: General test parameters for PUCCH SCell activation and deactivation in FR2 inter-band

Table A.7.5.3.9.1-3: NR Cell specific test parameters for PUCCH SCell activation and deactivation in FR2 inter-band

Table A.7.5.3.9.1-4: OTA related test parameters for PUCCH SCell activation and deactivation in FR2 inter-band

## A.7.5.3.9.2Test Requirements

During T2, the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than 3 ms + TFirstSSB_MAX + 15*TSMTC_MAX + 8*Trs + TL1-RSRP, measure + TL1-RSRP, report as defined in clause 8.3.12. For this test case, TFirstSSB_MAX=TSMTC_MAX=Trs=20 ms; TL1-RSRP, measure=480 ms and TL1-RSRP, report=5 ms, which allows TL1-RSRP =1000 ms.

During T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tdelay_PUCCH_SCellNR slot length

-THARQ is defined in Table A.7.5.3.3.1-2

-Tdelay_PUCCH_SCell = Tactivation_time + max ((TFirst_available_CSI + TCSI_processing), (T1+T2+T3), Tmeas) + TCSI_reporting_after

-Tactivation_time = 3 ms + TFirstSSB_MAX + 15*TSMTC_MAX + 8*Trs + TL1-RSRP, measure + TL1-RSRP, report + max {(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)}, which allows 1030 ms

-Tmeas = 5* Trs = 100 ms

-NR slot length is 0.125 ms for this test case.

During T2, the interruption of PCell during SCell activation shall not happen outside the slot  to , where TX =20 ms. m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length

During T3, the UE shall stop sending CSI reports for SCell no later than slot , as defined in clause 8.3.14.n+THARQ+3 msNR slot length

During T3, the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to  as defined in clause 8.3.14.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

## A.7.5.3.10SCell Activation and deactivation of FR2 known PUCCH SCell and one FR2 unknown SCell with FR2 PCell

## A.7.5.3.10.1Test Purpose and Environment

The purpose of this test is to verify that when a PUCCH SCell and DL SCell are activated using the same MAC CE command, the PUCCH SCell, and DL SCell activation and deactivation delays are within the requirements stated in clause 8.3.13 and 8.3.15. When UE receive the MAC CE activation command, PUCCH SCell in FR2 is known to UE and DL SCell in FR2 is unknown to the UE.

The supported test configurations are provided in table A.7.5.3.10.1-1 below. The general test parameters are given in Tables A.7.5.3.10.1-2 and cell-specific test parameters are given in A.7.5.3.10.1-3. OTA related test parameters are given in A.7.5.3.10.1-4.

The test consists of two sub tests, one with valid timing advance (TA), and other with invalid TA. The test consists of six successive time periods, with duration of T1, T2, and T3 respectively. There are two NR carriers, and PCC has two cell and SCC has one cells. All cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 but is not aware of Cell 2 (PUCCH SCell) and Cell 3 (DL SCell). Cell 1 and Cell 3 are configured on primary timing advance group (pTAG). Cell 2 is on different band than Cell 1 and Cell 3. For valid TA case, Cell 1, Cell 2 and Cell 3 are on same TAG.  For invalid TA case Cell 2 is on different TAG than Cell 1 and Cell 3. At the start of the test, the UE is monitoring PCC and not SCC.

At the beginning of T1, the UE receives an RRC message by which the PUCCH SCell (Cell 2) and DL SCell (Cell 3) becomes configured on radio channel 2 and 1 respectively. In T1, the UE starts measuring PUCCH SCell 1 and DL SCell is not detectable. During the duration of T1, the time alignment timer is running on and pTAG, and the TA is maintained on PCell. At the end of T1, the test equipment sends a MAC CE message for activation of the PUCCH SCell and DL SCell simultaneously.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI for the activated PUCCH SCell at latest in slotn1+ , and report valid CSI for the activated DL SCell at latest in slotn1+, as defined in clause 8.3.13. In this test case, both valid TA and invalid TA cases shall be tested. THARQ+Tdelay_multiple_SCells_PUCCH_SCellNR slot length THARQ+Tdelay_multiple_SCells_other_SCellNR slot length

Test for case when UE has valid TA (i.e., the TimeAlignmentTimer [2] associated with the TAG containing the PUCCH SCell is running), Tdelay_multiple_SCells_PUCCH_SCell = Tactivation_time_multiple_scells + [X]*Ttarget_PL_RS + TCSI_Reporting.

Test for case when UE do not have valid TA: Tdelay_multiple_SCells_PUCCH_SCell = Tactivation_time_multiple_scells + max ((TFirst_available_CSI + TCSI_processing), [X]*Ttarget_PL_RS, (T1+T2+T3)) + TCSI_reporting_after

Tactivation_time_multiple_scells is the target SCell activation delay in millisecond in multiple SCell activation scenario as specified in clause 8.3.7

In case of valid TA, for Cell 2 activation, the UE shall start reporting CSI in PUCCH SCell in slot  and shall report CQI index 0 (out-of-range) until the PUCCH SCell activation has been completed. n1+THARQ+3 msNR slot length

For Cell 3 activation, the UE shall start reporting CSI in PCell in slot  and shall report CQI index 0 (out-of-range) until the DL SCell activation has been completed.n1+THARQ+3 msNR slot length

Any PCell interruption due to activation of PUCCH SCell or DL SCell shall occur in the slot  to , as defined in clause 8.3.13, where  is the interruption length given in clause 8.2.2.2.7.n1+1+THARQNR slot lengthn1+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of PUCCH SCell and DL SCell, sent from the test equipment to the UE in a slot # denoted n2, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3.15, and the starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.15.n2+THARQ+3msNR slot lengthn2+1+THARQNR slot lengthn2+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of PUCCH SCell and DL SCell, respectively.

The test equipment verifies the PUCCH SCell activation time by counting the slots from the time when the PUCCH SCell activation command is sent until a CSI report with other than CQI index 0 is received. The test equipment verifies the DL SCell activation time by counting the slots from the time when the DL SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the PUCCH SCell deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for PUCCH SCell is discontinued. The test equipment verifies the DL SCell deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for DL SCell is discontinued.

Table A.7.5.3.10.1-1: Supported test configurations for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.10.1-2: General test parameters for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.10.1-3: Cell specific test parameters for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.10.1-4: OTA related test parameters for FR2 SCell activation in FR2 inter-band

## A.7.5.3.10.2Test Requirements

When UE receive SCell activation command at slot n1, during T2 the UE shall start sending CSI reports for SCell 2 with non-zero CQI index in the configured slots for CSI reporting no later than slot , where n1+THARQ+Tdelay_multiple_SCells_PUCCH_SCellNR slot length

- THARQ is defined in Table A.5.5.3.x6.1-2

- Tdelay_multiple_SCells_PUCCH_SCell is defined in clause 8.13.13.1. In this test case, both valid TA and invalid TA cases shall be tested.

- Test for case when UE has valid TA: the TimeAlignmentTimer [2] associated with the TAG containing the PUCCH SCell is running, and Tdelay_multiple_SCells_PUCCH_SCell = Tactivation_time_multiple_scells + [X]*Ttarget_PL_RS + TCSI_Reporting.

- Test for case when UE do not have valid TA: Tdelay_multiple_SCells_PUCCH_SCell = Tactivation_time_multiple_scells + max ((TFirst_available_CSI + TCSI_processing), [X]*Ttarget_PL_RS, (T1+T2+T3)) + TCSI_reporting_after.

- Tactivation_time_multiple_scells is the target SCell activation delay in millisecond in multiple SCell activation scenario as specified in clause 8.3.7.

- TCSI_Reporting = 10 ms

- NR slot length is 0.125 ms.

During T2 the UE shall start sending CSI reports for SCell 3 with non-zero CQI index in the configured slots for CSI reporting no later than slot where n1+THARQ+Tdelay_multiple_SCells_other_SCellNR slot length

- THARQ is defined in Table A.5.5.3.x6.1-2

- Tdelay_multiple_SCells_other_SCell   = Tactivation_time_multiple_scells +TCSI_Reporting.

- Tactivation_time_multiple_scells is the target SCell activation delay in millisecond in multiple SCell activation scenario as specified in clause 8.3.7

- TCSI_Reporting = 10 ms

- NR slot length is 0.125 ms.

Any PCell interruption due to activation of PUCCH SCell or DL SCell shall occur in the slot  to , as defined in clause 8.3.13, where  is the interruption length given in clause 8.2.2.2.7.n1+1+THARQNR slot lengthn1+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

During T3, when UE receives deactivation MAC CE at n2 slot, the UE shall stop sending CSI reports for both PUCCH SCell and DL SCell no later than slot , as defined in clause 8.3. The starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.15.n2+THARQ+3 msNR slot lengthn2+1+THARQNR slot lengthn2+1+THARQ+3 msNR slot length

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot ,  as defined in clause 8.3.13 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.n1+THARQ+Tdelay_multiple_SCells_PUCCH_SCellNR slot length

## A.7.5.3.11PUCCH SCell activation and deactivation delay requirements of FR2 unknown cell with FR2 PCell

## A.7.5.3.11.1PUCCH SCell activation with non-PUCCH SCell in a secondary PUCCH Group

## A.7.5.3.11.1.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.7.5.3.11 except the PUCCH SCell in FR2 is unknown and another to-be-activated FR2 non-PUCCH SCell in parallel with the PUCCH SCell belongs to the secondary PUCCH group.

The supported test configurations and the general test parameters are defined in Table A.7.5.3.11.1.1-1 and Table A.7.5.3.11.1.1-2, respectively. And cell specific test parameters are described in Tables A.7.5.3.11.1.1-3. OTA related test parameters are defined in Table A.7.5.3.11.1.1-4. In all test cases, three cells are used. Cell 1 is the FR2 PCell, and Cell 2 and Cell 3 are SCells in a different band from Cell 1. Cell 2 is PUCCH SCell and Cell 3 is non-PUCCH SCell belonging to the secondary PUCCH group.

In the test configuration 1, the UE is configured with a single Timingi Advance Group (TAG) for all cells, whereas UE is configured with a primary TAG (pTAG) for Cell 1 and a secondary TAG (sTAG) for Cell 2 and Cell 3 in the test configuration 2. The test configuration 1 and 2 are to verify the UE performance for the case where the UE has a valid TA for the PUCCH SCell and the case where the UE does not have a valid TA for the PUCCH SCell, respectively.

At the beginning of T1 the UE receives an RRC message by which the PUCCH SCell (Cell) and the non-PUCCH SCell (Cell 3) become configured on NR. During T1 the SCells are powered off and UE is not aware of the SCells.

A MAC message for activation of SCells is sent by the test equipment T1 after the RRC message, in a slot # denoted m. The point in time at which the MAC message for activation of SCells is received at the UE antenna connector defines the start of time period T2. Immediately at the beginning of T2 the transmission power of Cell 2 is increased to same level as for cell 2 At the time of T2, the UE has a valid TA in the test configuration 1 while the UE does not have a valid TA for the SCell in sTAG in the test configuration 2. During the test for the test configuration 1, the UE needs to be provided with a new Timing Advance Command MAC control element at least once during each time alignment timer period.

During T2, the test equipment monitors the L1-RSRP measurement result for the PUCCH SCell reported on the PCell. The time when test equipment receives a valid L1-RSRP report is denoted as slot m+TL1-RSRP. In the next DL slot after slot m+TL1-RSRP, the test equipment sends a MAC message for the activation of the TCI state of the RMC CORESET of the SCells and PUCCH-SpatialRelation of the PUCCH SCell. In the same slot, the test equipment also sends an RRC message to configure the CSI-RS resources for the SCells.

During the test for the test configuration 1, the UE shall start reporting CSI of the PUCCH SCell (Cell 2) and the non-PUCCH SCell (Cell 3) with non-zero CQI index via PUCCH on the SCell no later than slot m + (THARQ + Tdelay_multiple_SCells_PUCCH_SCell)/NR slot length and slot m + (THARQ + Tdelay_multiple_SCells_other_SCell)/NR slot length, respectively. Here, Tdelay_multiple_SCells_PUCCH_SCell and Tdelay_multiple_SCells_other_SCell are the PUCCH SCell activation delay and other SCell activation delay defined in 8.3.13 for a valid TA scenario.

During the test for the test configuration 2, THARQ + Tactivation_time after slot m, the UE shall be able to monitor PDCCH on the PUCCH SCell that triggers PDCCH order-based contention-free PRACH. The test equipment receives the PRACH and sends random access response with Timing Advance Command MAC Control Elements for sTAG, with Timing Advance Command value estimated from the PRACH. The UE shall start reporting CSI of the PUCCH SCell (Cell 2) and the non-PUCCH SCell (Cell 3) with non-zero CQI index via PUCCH on the SCell no later than slot m + (THARQ + Tdelay_multiple_SCells_PUCCH_SCell)/NR slot length and slot m + (THARQ + Tdelay_multiple_SCells_other_SCell)/NR slot length, respectively. Here, Tactivation_time is the SCell activation delay defined in 8.3.2 for FR2 unknown SCell with periodic CSI-RS used for CSI reporting, and Tdelay_multiple_SCells_PUCCH_SCell and Tdelay_multiple_SCells_other_SCell are the PUCCH SCell activation delay and other SCell activation delay defined in 8.3.13 for an invalid TA scenario.

Time period T3 starts when a MAC message for deactivation of the SCells, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during the activation of the SCells.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CSI reporting on the PUCCH SCell is discontinued.

Table A.7.5.3.11.1.1-1: Supported test configurations for FR2 SCell activation case

Table A.7.5.3.11.1.1-2: General test parameters for unknown FR2 PUCCH SCell activation case

Table A.7.5.3.11.1.1-3: Cell specific test parameters for FR2 PUCCH SCell activation case

Table A.7.5.3.11.1.1-4: OTA related test parameters for FR2 PUCCH SCell activation

## A.7.5.3.11.1.2Test Requirements

During T2 the UE shall start sending a valid L1-RSRP report of the SCell to the PCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than 3 ms + TFirstSSB_MAX + 15*TSMTC_MAX + 8*Trs + TL1-RSRP, measure + TL1-RSRP, report as defined in clause 8.3.2.

During T2, if the test is based on the test configuration 1, the UE shall start sending CSI reports of the PUCCH SCell (Cell 2) and the non-PUCCH SCell (Cell 3) with non-zero CQI index via PUCCH on the SCell no later than slot m + (THARQ + Tdelay_multiple_SCells_PUCCH_SCell)/NR slot length and slot m + (THARQ + Tdelay_multiple_SCells_other_SCell)/NR slot length, respectively. Here, Tdelay_multiple_SCells_PUCCH_SCell and Tdelay_multiple_SCells_other_SCell are the PUCCH SCell activation delay and other SCell activation delay defined in 8.3.13 for a valid TA scenario.

During T2, if the test is based on the test configuration 2, the UE shall start sending CSI reports of the PUCCH SCell (Cell 2) and the non-PUCCH SCell (Cell 3) with non-zero CQI index via PUCCH on the SCell (Cell 2) no later than slot m + (THARQ + Tdelay_multiple_SCells_PUCCH_SCell)/NR slot length and slot m + (THARQ + Tdelay_multiple_SCells_other_SCell)/NR slot length, respectively. Here, Tdelay_multiple_SCells_PUCCH_SCell and Tdelay_multiple_SCells_other_SCell are the PUCCH SCell activation delay and other SCell activation delay defined in 8.3.13 for an invalid TA scenario.

During T3 the UE shall stop sending CSI reports on the PUCCH SCell no later than slot , as defined in clause 8.3.15.n+THARQ+3 msNR slot length

During T2 interruption of PCell during the SCell activation shall not happen outside the slot   to , as defined in clause 8.3, where TX =20 ms. If the UE is not capable of parallelTxPRACH-SRS-PUCCH-PUSCH additional interruption can be allowed as defined in Clause 8.2.2.2.18.m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.15.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

The interruption of PCell due to activation of SCells shall not be more than the values specified for SA in Clause 8.2.2.2.18.

## A.7.5.3.11.2PUCCH SCell activation with non-PUCCH SCell in a primary PUCCH Group

## A.7.5.3.11.2.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.7.5.3.11 except the PUCCH SCell in FR2 is unknown and another to-be-activated FR2 non-PUCCH SCell in parallel with the PUCCH SCell belongs to the primary PUCCH group.

The supported test configurations and the general test parameters are defined in Table A.7.5.3.11.2.1-1 and Table A.7.5.3.11.2.1-2, respectively. And cell specific test parameters are described in Tables A.7.5.3.11.2.1-3. OTA related test parameters are defined in Table A.7.5.3.11.2.1-4. In all test cases, three cells are used. Cell 1 and Cell 3 are FR2 PCell and FR2 non-PUCCH SCell in the same band, respectively, and Cell 2 is PUCCH SCells in a different band from Cell 1 and Cell 3. Cell 3 belongs to the primary PUCCH group.

In the test configuration 1, the UE is configured with a single Timingi Advance Group (TAG) for all cells, whereas UE is configured with a primary TAG (pTAG) for Cell 1 and a secondary TAG (sTAG) for Cell 2 and Cell 3 in the test configuration 2. The test configuration 1 and 2 are to verify the UE performance for the case where the UE has a valid TA for the PUCCH SCell and the case where the UE does not have a valid TA for the PUCCH SCell, respectively.

At the beginning of T1 the UE receives an RRC message by which the PUCCH SCell (Cell) and the non-PUCCH SCell (Cell 3) become configured on NR. During T1 the SCells are powered off and UE is not aware of the SCells.

A MAC message for activation of SCells is sent by the test equipment T1 after the RRC message, in a slot # denoted m. The point in time at which the MAC message for activation of SCells is received at the UE antenna connector defines the start of time period T2. Immediately at the beginning of T2 the transmission power of Cell 2 is increased to same level as for cell 2 At the time of T2, the UE has a valid TA in the test configuration 1 while the UE does not have a valid TA for the SCell in sTAG in the test configuration 2. During the test for the test configuration 1, the UE needs to be provided with a new Timing Advance Command MAC control element at least once during each time alignment timer period.

During T2, the test equipment monitors the L1-RSRP measurement result for the PUCCH SCell reported on the PCell. The time when test equipment receives a valid L1-RSRP report is denoted as slot m+TL1-RSRP. In the next DL slot after slot m+TL1-RSRP, the test equipment sends a MAC message for the activation of the TCI state of the RMC CORESET of the SCells and PUCCH-SpatialRelation of the PUCCH SCell. In the same slot, the test equipment also sends an RRC message to configure the CSI-RS resources for the SCells.

During the test for the test configuration 1, the UE shall start reporting CSI of the PUCCH SCell (Cell 2) and the non-PUCCH SCell (Cell 3) with non-zero CQI index via PUCCH on the PUCCH SCell (Cell 2) and PCell (Cell 1), respectively, no later than slot m + (THARQ + Tdelay_multiple_SCells_PUCCH_SCell)/NR slot length and slot m + (THARQ + Tdelay_multiple_SCells_other_SCell)/NR slot length, respectively. Here, Tdelay_multiple_SCells_PUCCH_SCell and Tdelay_multiple_SCells_other_SCell are the PUCCH SCell activation delay and other SCell activation delay defined in 8.3.13 for a valid TA scenario.

During the test for the test configuration 2, THARQ + Tactivation_time after slot m, the UE shall be able to monitor PDCCH on the PUCCH SCell that triggers PDCCH order-based contention-free PRACH. The test equipment receives the PRACH and sends random access response with Timing Advance Command MAC Control Elements for sTAG, with Timing Advance Command value estimated from the PRACH. The UE shall start reporting CSI of the PUCCH SCell (Cell 2) and the non-PUCCH SCell (Cell 3) with non-zero CQI index via PUCCH on the PUCCH SCell (Cell 2) and PCell (Cell 1), respectively, no later than slot m + (THARQ + Tdelay_multiple_SCells_PUCCH_SCell)/NR slot length and slot m + (THARQ + Tdelay_multiple_SCells_other_SCell)/NR slot length, respectively. Here, Tactivation_time is the SCell activation delay defined in 8.3.2 for FR2 unknown SCell with periodic CSI-RS used for CSI reporting, and Tdelay_multiple_SCells_PUCCH_SCell and Tdelay_multiple_SCells_other_SCell are the PUCCH SCell activation delay and other SCell activation delay defined in 8.3.13 for an invalid TA scenario.

Time period T3 starts when a MAC message for deactivation of the SCells, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during the activation of the SCells.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CSI reporting on the PUCCH SCell is discontinued.

Table A.7.5.3.11.2.1-1: Supported test configurations for FR2 SCell activation case

Table A.7.5.3.11.2.1-2: General test parameters for unknown FR2 PUCCH SCell activation case

Table A.7.5.3.11.2.1-3: Cell specific test parameters for FR2 PUCCH SCell activation case

Table A.7.5.3.11.2.1-4: OTA related test parameters for FR2 PUCCH SCell activation

## A.7.5.3.11.2.2Test Requirements

During T2 the UE shall start sending a valid L1-RSRP report of the SCell to the PCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than 3 ms + TFirstSSB_MAX + 15*TSMTC_MAX + 8*Trs + TL1-RSRP, measure + TL1-RSRP, report as defined in clause 8.3.2.

During T2, if the test is based on the test configuration 1, the UE shall start sending CSI reports of the PUCCH SCell (Cell 2) and the non-PUCCH SCell (Cell 3) with non-zero CQI index via PUCCH on the PUCCH SCell (Cell 2) and PCell (Cell 1), respectively, no later than slot m + (THARQ + Tdelay_multiple_SCells_PUCCH_SCell)/NR slot length and slot m + (THARQ + Tdelay_multiple_SCells_other_SCell)/NR slot length, respectively. Here, Tdelay_multiple_SCells_PUCCH_SCell and Tdelay_multiple_SCells_other_SCell are the PUCCH SCell activation delay and other SCell activation delay defined in 8.3.13 for a valid TA scenario.

During T2, if the test is based on the test configuration 2, the UE shall start sending CSI reports of the PUCCH SCell (Cell 2) and the non-PUCCH SCell (Cell 3) with non-zero CQI index via PUCCH on the PUCCH SCell (Cell 2) and PCell (Cell 1), respectively, no later than slot m + (THARQ + Tdelay_multiple_SCells_PUCCH_SCell)/NR slot length and slot m + (THARQ + Tdelay_multiple_SCells_other_SCell)/NR slot length, respectively. Here, Tdelay_multiple_SCells_PUCCH_SCell and Tdelay_multiple_SCells_other_SCell are the PUCCH SCell activation delay and other SCell activation delay defined in 8.3.13 for an invalid TA scenario.

During T3 the UE shall stop sending CSI reports on the PUCCH SCell no later than slot , as defined in clause 8.3.15.n+THARQ+3 msNR slot length

During T2 interruption of PCell during the SCell activation shall not happen outside the slot   to , as defined in clause 8.3, where TX =20 ms. If the UE is not capable of parallelTxPRACH-SRS-PUCCH-PUSCH additional interruption can be allowed as defined in Clause 8.2.2.2.18.m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.15.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

The interruption of PCell due to activation of SCells shall not be more than the values specified for SA in Clause 8.2.2.2.18.

## A.7.5.3.12Void

## A.7.5.3.13SCell Activation for SCell in FR2 intra-band in non-DRX

## A.7.5.3.13.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.5.5.3.8.1, PCell and SCell are in FR2 intra-band.

The supported test configurations are shown in table A.5.5.3.8.1-1 below. The general test parameters are the same as defined in Table A.5.5.3.8.1-2 except those described in Tables A.7.5.3.13.1-2, and cell specific test parameters are described in Tables A.7.5.3.13.1-3. OTA related test parameters are shown in table A.7.5.3.13.1-4 below.

Table A.7.5.3.13.1-1: Supported test configurations for FR2 SCell activation case

Table A.7.5.3.13.1-2: General test parameters for FR2 SCell activation case

Table A.7.5.3.13.1-3: Cell specific test parameters for FR2 SCell activation case

Table A.7.5.3.13.1-4: OTA related test parameters for FR2 SCell activation case

## A.7.5.3.13.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption. During T2 the UE shall start sending CSI reports for SCell with non-zero CQI index at latest in a slot , Tactivation_time = TFirstATRS + 5 ms, as defined in TS 38.133 [6] clause 8.3.16.n+1+THARQ+3 msNR slot lengthn+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

During T2 interruption of PCell / PSCell during SCell activation shall not happen outside the slot  to , as defined in TS 38.133 [6] clause 8.3.16.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

The interruption on any activated serving cell shall not be more than the values specified for SA in TS 38.133 [6] clause 8.2.2.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in TS 38.133 [6] clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.7.5.3.14SCell Activation for known SCell in FR2 inter-band

## A.7.5.3.14.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.7.5.3.13.1 except the PCell and SCell are in FR2 inter-band, when the SCell in FR2 is known by the UE at the time of activation.

The supported test configurations are shown in table A.7.5.3.14.1-1 below. The general test parameters are described in Tables A.7.5.3.14.1-2, and cell specific test parameters are described in Tables A.7.5.3.14.1-3. OTA related test parameters A.7.5.3.14.1 are shown in table A.7.5.3.14.1-4 below.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on NR. The UE now starts monitoring the SCell. The test equipment sends a MAC message for activation of the SCell triggering the aperiodic CSI-RS for fast SCell activation.

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m (where m mode 20=1), defines the start of time period T2. The UE shall be able to report valid CSI in PSCell for the activated SCell at latest in slot , as defined in clause 8.3.6. The UE shall start reporting CSI in PSCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k) and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PSCell interruption due to activation of SCell shall occur in the slot  to slot , as defined in clause 8.3, where  is the interruption length given in clause 8.2m+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell and PSCell during activation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.7.5.3.14.1-1: Supported test configurations for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.14.1-2: General test parameters for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.14.1-3: Cell specific test parameters for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.14.1-4: OTA related test parameters for FR2 SCell activation in FR2 inter-band

## A.7.5.3.14.2Test Requirements

During T2 the UE shall start sending CSI report for the SCell in the configured slots for CSI reporting after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k). UE shall send the first CSI report for SCell after receiving at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k), or in the next available uplink resource for CSI reporting if the slot was subject to interruption. Whether CSI report in a slot was interrupted is checked by monitoring ACK/NACK sent in PCell in the slot.

During T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

-THARQ is defined in Table A.7.5.3.14.1-2

-Tactivation_time = max(TFirstATRS + 5 ms, Tuncertainty_RRC + TRRC_delay-THARQ)

-TCSI_Reporting = 10 ms

-NR slot length is 0.125 ms for this test case.

During T2, the interruption of PCell during SCell activation shall not happen outside the slot   to , where TX =4 ms. m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length

## A.7.5.3.15PUCCH SCell activation and deactivation with FR1 PCell based on L3 reporting after SCell activation command

## A.7.5.3.15.1Test Purpose and Environment

The purpose of this test is to verify that the PUCCH SCell activation and deactivation times are within the requirements stated in clause 8.3.12 for UE capable of l3-MeasUnknownSCellActivation-r18.

The supported test configurations are shown in table A.7.5.3.15.1-1 below. The test parameters are given in Tables A.7.5.3.15.1-2 and cell-specific parameters in A.7.5.3.15.1-3 and A.7.5.3.15.1-4 below. The test consists of Three successive time periods, with duration of T1, T2 and T3 respectively. There are three NR carriers, each with one cell. Before the test starts the UE is connected to Cell 1 and Cell 2 but is not aware of Cell 3, and UE is configured with MeasObjectNR on carriers of Cell 1 and Cell 2. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the PUCCH SCell (Cell 3) becomes configured on radio channel 3, and one measID is associated with reportOnActivation. The UE now starts monitoring the Cell 3. The test equipment sends a MAC message for activation of the PUCCH SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI for the activated PUCCH SCell at latest in slotn+ , as defined in clause 8.3.12.  THARQ+Tdelay_PUCCH_SCellNR slot length

There are two sub-tests in the test. In sub-test 1, TE shall transmit DCI 0-1 to PSCell at slot , and the UE shall be able to send L3 measurements report of the SCell at slot , where k2 =1. In sub-test 2, TE shall transmit DCI 0-1 to PSCell at slot , where k2=1 and M is defined in 8.3.12. The UE shall be able to send L3 measurements report of the SCell at.n+THARQ+7 ms NR slot lengthn+THARQ+7 ms+k2 NR slot lengthn+THARQ+7 ms+M-k2 NR slot length+THARQ+7 ms+M NR slot length

Any PCell interruption due to activation of PUCCH SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of PUCCH SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3.14and the starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.14.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of PUCCH SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.7.5.3.15.1-1: Supported test configurations for FR2 SCell activation case

Table A. A.7.5.3.15.1-2: General test parameters for FR2 SCell activation case

Table A.7.5.3.15.1-3: Cell specific test parameters for FR2 SCell activation case: Cell 1 and Cell 2

Table A.7.5.3.15.1-4: Cell specific test parameters for FR2 SCell activation case: Cell 3

Table A.7.5.3.15.1-4: OTA related test parameters for FR2 SCell with FR1 PCell

## A.7.5.3.15.2Test Requirements

By end of T2 the UE shall finish the DL activation for the PUCCH SCell. Assuming the periodic CSI reporting is used and assuming periodic CSI activation and TCI state is sent along with SCell activation MAC CE, UE shall finish the DL activation by slot n+  as defined in clause 8.3.12.THARQ+Tactivation_timeNR slot length

During T2 the UE shall start sending PRACH preamble to TE and shall obtain the TA command from TE and shall be ready to send valid CSI report to the TE. CSI report shall be transmitted within  Tactivation_time + Max ((TFirst_available_CSI + TCSI_processing), (T1+T2+T3)) + TCSI_reporting_after from the transmission of HARQ feedback of SCell activation command as specified in the 8.3.12.

In sub-test 1, Tactivation_time = 7 ms + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3.12.

In sub-test 2, Tactivation_time = 7 ms + M+ max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3.12.

During T3 the UE shall stop sending CSI reports for both SCells no later than slot , as defined in clause 8.3.m+THARQ+3 msNR slot length

During T2 interruption of PCell during SCell activation shall not happen outside the slot   to , as defined in clause 8.3, where TX =20 ms. n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The interruption of PCell due to activation of SCell shall not be more than the values specified for SA in Clause 8.2.2.2.7.

## A.7.5.3.16PUCCH SCell activation and deactivation with FR2 PCell based on L3 reporting after SCell activation command

## A.7.5.3.16.1Test Purpose and Environment

The purpose of this test is to verify that the PUCCH SCell activation and deactivation times are within the requirements stated in clause 8.3.12 for UE capable of l3-MeasUnknownSCellActivation-r18.

The supported test configurations are shown in table A.7.5.3.16.1-1 below. The test parameters are given in Tables A.7.5.3.16.1-2 and cell-specific parameters in A.7.5.3.16.1-3 below. The test consists of Three successive time periods, with duration of T1, T2 and T2 respectively. There are two NR carriers, each with one cell. Before the test starts the UE is connected to Cell 1 but is not aware of Cell 2, and UE is configured with MeasObjectNR on carrier of Cell 1 and Cell 2. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the PUCCH SCell (Cell 2) becomes configured on radio channel 2, and one measID is associated with reportOnActivation. The UE now starts monitoring the Cell 2. The test equipment sends a MAC message for activation of the PUCCH SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI for the activated PUCCH SCell at latest in slotn+ , as defined in clause 8.3.12.  THARQ+Tdelay_PUCCH_SCellNR slot length

There are two sub-tests in the test. In sub-test 1, TE shall transmit DCI 0-1 to PSCell at slot , and the UE shall be able to send L3 measurements report of the SCell at slot , where k2 =1. In sub-test 2, TE shall transmit DCI 0-1 to PSCell at slot , where k2=1 and M is defined in 8.3.12. The UE shall be able to send L3 measurements report of the SCell at.n+THARQ+7 ms NR slot lengthn+THARQ+7 ms+k2 NR slot lengthn+THARQ+7 ms+M-k2 NR slot length+THARQ+7 ms+M NR slot length

Any PCell interruption due to activation of PUCCH SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of PUCCH SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3.14and the starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.14.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of PUCCH SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.7.5.3.16.1-1: Supported test configurations for FR2 SCell activation case

Table A. A.7.5.3.16.1-2: General test parameters for FR2 SCell activation case

Table A.7.5.3.16.1-2: Cell specific test parameters for FR2 SCell activation case: Cell 1 and Cell 2

Table A.7.5.3.16.1-4: OTA related test parameters for FR2 SCell with FR2 PCell

## A.7.5.3.16.2Test Requirements

By end of T2 the UE shall finish the DL activation for the PUCCH SCell. Assuming the periodic CSI reporting is used and assuming periodic CSI activation and TCI state is sent along with SCell activation MAC CE, UE shall finish the DL activation by slot n+  as defined in clause 8.3.12.THARQ+Tactivation_timeNR slot length

During T2 the UE shall start sending PRACH preamble to TE and shall obtain the TA command from TE and shall be ready to send valid CSI report to the TE. CSI report shall be transmitted within Tactivation_time + Max ((TFirst_available_CSI + TCSI_processing), (T1+T2+T3)) + TCSI_reporting_after from the transmission of HARQ feedback of SCell activation command as specified in the 8.3.12.

In sub-test 1, Tactivation_time = 7 ms + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3.12.

In sub-test 2, Tactivation_time = 7 ms + M+ max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay) as defined in clause 8.3.12.

During T3 the UE shall stop sending CSI reports for both SCells no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

During T2 interruption of PCell during SCell activation shall not happen outside the slot   to , as defined in clause 8.3, where TX =20 ms. m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

The interruption of PCell due to activation of SCell shall not be more than the values specified for SA in Clause 8.2.2.2.7.

## A.7.5.3.17SCell Activation and deactivation for SCell in FR2 inter-band in DRX for UE capable of small beam sweeping factors and/or short measurement interval

## A.7.5.3.17.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.7.5.3.1.1 except the PCell (Cell 1) and SCell (Cell 2) are in FR2 inter-band. The test will also verify that the SSB-based L1-RSRP measurement accuracy is within the specified limits as stated in clause 10.1.20.1.

The supported test configurations are shown in table A.7.5.3.17.1-1 below. The general test parameters are described in Tables A.7.5.3.17.1-2, and cell specific test parameters are described in Tables A.7.5.3.17.1-3. OTA related test parameters are shown in table A.7.5.3.17.1-4 below.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on NR. During T1 the SCell is powered off and UE is not aware of SCell. A MAC message for activation of SCell is sent by the test equipment 100 ms after the RRC message, in a slot # denoted m. The UE shall be continuously scheduled within on-duration based on DRX configuration in the PCell throughout the whole test. The point in time at which the MAC message for activation of SCell is received at the UE antenna connector defines the start of time period T2. Immediately at beginning of T2 the transmission power of Cell 2 is increased to same level as for Cell 1. During T2, the test equipment monitors the L1-RSRP measurement reporting for the SCell. The time when test equipment receives a valid L1-RSRP report is denoted as slot m+TL1-RSRP. In the next DL slot after slot m+TL1-RSRP, the test equipment sends a MAC message for the activation of the TCI state of the RMC CORESET of the SCell. In the same slot, the test equipment also sends an RRC message to configure the CSI-RS resources for SCell.

Time period T3 starts when a MAC message for deactivation of the SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received. In this test the allowed time for SCell activation depends on the UE reported capabilities regarding small beam sweeping factors (beamSweepingFactorReduction-r18) and short measurement intervals (shortMeasInterval-r18).

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CSI reporting for SCell is discontinued.

The test equipment verifies the absolute accuracy of SSB-based L1-RSRP measurements during T2 by using the parameters in Table A.7.5.3.17.1-3 and Table A.7.5.3.17.1-4.

Table A.7.5.3.17.1-1: Supported test configurations for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.17.1-2: General test parameters for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.17.1-3: Cell specific test parameters for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.17.1-4: OTA related test parameters for FR2 SCell activation in FR2 inter-band

## A.7.5.3.17.2Test Requirements

During T2 the UE shall start sending CSI report for the SCell in the configured slots for CSI reporting after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k). UE shall send the first CSI report for SCell after receiving at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k), or in the next available uplink resource for CSI reporting if the slot was subject to interruption. Whether CSI report in a slot was interrupted is checked by monitoring ACK/NACK sent in PCell in the slot.

For UE capable of beamSweepingFactorReduction-r18 and shortMeasInterval-r18 capabilities:

During T2, the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than:

## 3 ms + TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + X1*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report

as defined in clause 8.3.2. For this test case, UE supports short measurement interval hence TFirstSSB_MAX, enhanced =TSMTC_MAX, enhanced =Trs, enhanced =TSSB=20 ms; TL1-RSRP, enhanced measure=X2/8 *480 ms and TL1-RSRP, report=5 ms, which allows TL1-RSRP according to table A.7.5.17.2-1. TL1-RSRP =968 ms if X1 and X2 use the default value and a minimum of 348 ms for the case with X1=1, X2=0 (for other values of X1/X2 capability corresponding value of TL1-RSRP shall be adopted from table A.7.5.17.2-1:

Table A.7.5.3.17.2-1: TL1-RSRP for different X1/X2 capabilities (ms)

During T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tctivation_time+TCSI_ReportingNR slot length

-THARQ is defined in table A.7.5.3.3.1-2

-Tactivation_time = 3 ms TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + X1*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report + max {(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)}, which allows 1000 ms in case of no X1/X2 capability and a minimum of 380 ms for the case with X1=1, X2=0 (for other values of X1/X2 capability corresponding value of TL1-RSRP shall be adopted.

For UE capable of beamSweepingFactorReduction-r18 but not shortMeasInterval-r18 capabilities, the cell specific test parameters are described in table A.7.5.3.17.1-3 except that SMTC value is SMTC.1:

During T2, the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than:

## 3 ms + TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + X1*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report

as defined in clause 8.3.2. For this test case, UE supports short measurement interval hence TFirstSSB_MAX, enhanced =TSMTC_MAX, enhanced =Trs, enhanced =20 ms; TL1-RSRP, enhanced measure=X2/8 *11520 ms and TL1-RSRP, report=5 ms, which allows TL1-RSRP = 12008 ms if X1 and X2 are absent. Value of TL1-RSRP for various X1/X2 capabilities is obtained from table A.7.53.17.2-2.

Table A.7.5.3.17.2-2: TL1-RSRP for different X1/X2 capabilities (ms)

During T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

-THARQ is defined in table A.7.5.3.3.1-2

-Tactivation_time = 3 ms TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + X1*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report + max {(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)}, which allows 12040 ms in case of no X1/X2 capability and a minimum of 380 ms for the case with X1=1, X2=0 (for other values of X1/X2 capability corresponding value of TL1-RSRP shall be adopted.

For UE capable of shortMeasInterval-r18 but not beamSweepingFactorReduction-r18 capabilities, the general test parameters are described in table A.7.5.3.17.1-2, except that the default value for X1=X2=8 is chosen.

During T2, the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than:

## 3 ms + TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + 8*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report

as defined in clause 8.3.2. For this test case, UE supports short measurement interval hence TFirstSSB_MAX, enhanced =TSMTC_MAX, enhanced =Trs, enhanced =TSSB=20 ms; TL1-RSRP, enhanced measure=480 ms and TL1-RSRP, report=5 ms, which allows TL1-RSRP =968 ms.

During T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

-THARQ is defined in table A.7.5.3.3.1-2

-Tactivation_time = 3 ms TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + 8*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report + max {(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)}, which allows 1000 ms.

-TCSI_Reporting = 10 ms

-NR slot length is 0.125 ms for this test case.

The L1-RSRP measurement accuracy for SSB resource reported by UE in L1-RSRP report (SSB#0 or SSB#1) of Cell 3 shall fulfil the accuracy requirements in clauses 10.1.20.1 provided the side condition is -2 dB as defined in clause 8.3.2.

During T3, the UE shall stop sending CSI reports for SCell no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

## A.7.5.3.18SCell Activation and deactivation for FR1+FR2 inter-band with target SCell in FR2, in DRX, for UE capable of small beam sweeping factors and/or short measurement interval

## A.7.5.3.18.1Test Purpose and Environment

The purpose of this test case is the same as for the test defined in clause A.7.5.3.1.1 except the PCell is in FR1 and SCell is in FR2.

The supported test configurations are defined in table A.7.5.3.18.1-1. The general test parameters are the same as defined in table A.7.5.3.18.1-2. And cell specific test parameters are described in Tables A.7.5.3.18.1-2. OTA related test parameters are defined in table A.7.5.3.18.1-3. The test will also verify that the SSB-based L1-RSRP measurement accuracy is within the specified limits as stated in clause 10.1.20.1.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on NR. During T1 the SCell is powered off and UE is not aware of SCell.

A MAC message for activation of SCell is sent by the test equipment 100 ms after the RRC message, in a slot # denoted m. The UE shall be continuously scheduled within on-duration based on DRX configuration in the PCell throughout the whole test. The point in time at which the MAC message for activation of SCell is received at the UE antenna connector defines the start of time period T2.

During T2, the test equipment monitors the L1-RSRP measurement reporting for the SCell. The time when test equipment receives a valid L1-RSRP report is denoted as slot m+TL1-RSRP. In the next DL slot after slot m+TL1-RSRP, the test equipment sends a MAC message for the activation of the TCI state of the RMC CORESET of the SCell. In the same slot, the test equipment also sends an RRC message to configure the CSI-RS resources for SCell.

Time period T3 starts when a MAC message for deactivation of the SCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE antenna connector.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell 1 deactivation command is sent until CSI reporting for SCell 1 is discontinued.

The test equipment verifies the absolute accuracy of SSB-based L1-RSRP measurements during T2 by using the parameters in table A.7.5.3.18.1-3 and table A.7.5.3.18.1-4.

Table A.7.5.3.18.1-1: Supported test configurations for FR2 SCell activation case

Table A.7.5.3.18.1-2: General test parameters for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.18.1-3: Cell specific test parameters for FR2 SCell activation case

Table A.7.5.3.18.1-4: OTA related test parameters for FR2 SCell activation case with FR1 PCell

## A.7.5.3.18.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.  Whether CSI report in a slot was interrupted is checked by monitoring ACK/NACK sent in PCell in the slot.

For UE capable of beamSweepingFactorReduction-r18 and shortMeasInterval-r18 capabilities:

During T2 the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than

## 3 ms + TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + X1*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report

as defined in clause 8.3.2. For this test case, TFirstSSB_MAX, enhanced =TSMTC_MAX, enhanced =Trs, enhanced = TSSB=20 ms; TL1-RSRP, enhanced_measure= (X2/8)*160 ms and TL1-RSRP,reprt=5 ms, which allows TL1-RSRP = 680 ms if X1 and X2 use the default value. Value of TL1-RSRP for various X1/X2 capabilities is obtained from table A.7.5.3.18.2-1.

During T2 the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

- THARQ is defined in table A.7.5.3.18.1-2

- Tactivation_time = 3 ms TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + X1*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report + max {(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)}, which allows 710 ms in case of no X1/X2 capability and a minimum of 380 ms for the case with X1=1, X2=0 (for other values of X1/X2 capability corresponding value of TL1-RSRP shall be adopted from table A.7.5.3.18.2-1.

Table A.7.5.3.18.2-1: TL1-RSRP for different X1/X2 capabilities (ms)

For UE capable of beamSweepingFactorReduction-r18 but not shortMeasInterval-r18 capabilities, the cell specific test parameters are described in table A.7.5.3.18.1-3 except that SMTC value is SMTC.1:

During T2 the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than

## 3 ms + TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + X1*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report

as defined in clause 8.3.2. For this test case, TFirstSSB_MAX, enhanced =TSMTC_MAX, enhanced =Trs, enhanced = TSSB=20 ms; TL1-RSRP, enhanced_measure= (X2/8)*3840 ms and TL1-RSRP,ctiva=5 ms, which allows TL1-RSRP = 4328 ms if X1 and X2 use the default value. Value of TL1-RSRP for various X1/X2 capabilities is obtained from table A.7.5.3.18.2-2.

During T2 the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tctivation_time+TCSI_ReportingNR slot length

- THARQ is defined in table A.5.5.3.1.1-2

- Tactivation_time = 3 ms TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + X1*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report + max {(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)}, which allows 4360 ms in case of no X1/X2 capability and a minimum of 380 ms for the case with X1=1, X2=0 (for other values of X1/X2 capability corresponding value of TL1-RSRP shall be adopted from table A.7.5.3.18.2-2.

Table A.7.5.3.18.2-2: TL1-RSRP for different X1/X2 capabilities (ms)

For UE capable of shortMeasInterval-r18 but not beamSweepingFactorReduction-r18 capabilities, the general test parameters are described in table A.7.5.3.18.1-2, except that the default value for X1=X2=8 is chosen.

During T2, the UE shall start sending valid L1-RSRP report for the SCell in the configured slots for CSI reporting after slot (m+TL1-RSRP), where TL1-RSRP is no larger than:

## 3 ms + TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + 8*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report

as defined in clause 8.3.2. For this test case, UE supports short measurement interval hence TFirstSSB_MAX, enhanced =TSMTC_MAX, enhanced =Trs, enhanced =TSSB=20 ms; TL1-RSRP, enhanced measure=160 ms and TL1-RSRP, report=5 ms, which allows TL1-RSRP =680 ms.

During T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

-THARQ is defined in table A.7.5.3.3.1-2

-Tactivation_time = 3 ms TFirstSSB_MAX, enhanced + 15*TSMTC_MAX, enhanced + 8*Trs, enhanced + TL1-RSRP, enhanced_measure + TL1-RSRP, report + max {(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming), (Tuncertainty_RRC + TRRC_delay)}, which allows 710 ms.

- TCSI_Reporting = 10 ms

- NR slot length is 0.125 ms for this test case.

The L1-RSRP measurement accuracy for SSB resource reported by UE in L1-RSRP report (SSB#0 or SSB#1) of Cell 3 shall fulfil the accuracy requirements in clauses 10.1.20.1 provided the side condition is -2 dB as defined in clause 8.3.2.

During T3 the UE shall stop sending CSI reports for both SCells no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

## A.7.5.3.19SCell Activation and deactivation of FR2 unknown SCell with FR1 PCell in non-DRX with L3 reporting during activation

## A.7.5.3.19.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3.17, when the SCell is unknown in FR2 by the UE at the time of activation. In this test, UE shall perform two sub-tests where two different UL resource locations are configured.

The supported test configurations are shown in table A.7.5.3.19.1-1 below. The test parameters are the same as in clause A.4.5.3.3.1 except those described in the following clause. The general test parameters are given in table A.7.5.3.19.1-2 and cell-specific test parameters in table A.7.5.3.19.1-3 below. In this case, OTA related test parameters are shown in table A.7.5.3.19.1-4 below.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two carriers, PCell (Cell 1) in FR1 and SCell (Cell 2) in FR2. Cell 1 have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) but is not aware of Cell 2 (SCell). The UE is monitoring the PCell. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. In the measurement control information for Cell 2, it is indicated to the UE that event-triggered reporting with Event A2 and reportOnActivation is used. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell activation.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n (where n mode 20=1), defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3. n+THARQ+Tactivation_time+TCSI_ReportingNR slot length

In sub-test1, TE shall transmit DCI 0-1 to PCell at slot .  The UE shall be able to send L3 measurements report of the SCell at slot  for sub-test 1.In sub-test2, TE shall transmit DCI 0-1 to PCell at slot  The UE shall be able to send L3 measurements report of the SCell at slot  for sub-test 2. TE will send TCI activation command after receiving L3 measurement report of the SCell. n+THARQ+7 ms NR slot lengthn+THARQ+7 ms+0.125 ms NR slot lengthn+THARQ+3 ms+M-0.125 ms NR slot length.n+THARQ+7 ms+ M NR slot length

The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of the SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell and PSCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CSI reporting for SCell is discontinued.

Table A.7.5.3.19.1-1: Supported test configurations for FR2 SCell activation case

Table A.7.5.3.19.1-2: General test parameters for FR2 SCell activation case with FR1 PSCell

Table A.7.5.3.19.1-3: Cell specific test parameters for FR2 SCell activation case with FR1 active PCell

Table A.7.5.3.19.1-4: OTA related test parameters for FR2 SCell activation case with FR1 PCell

## A.7.5.3.19.2Test Requirements

During T2, the UE shall be able to send a valid L3-RSRP report for the SCell in the configured slots for CSI reporting at slot  for sub-test 1. For sub-test2, the UE shall be able to send a valid L3-RSRP for the SCell at slot  . The UE is not required to send L3-RSRP report after slot , where M is defined in 8.3.17.n+THARQ+7ms+0.125msNR slot lengthn+THARQ+7ms+MNR slot lengthn+THARQ+3ms+MNR slot length

During T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where n+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

-THARQ and TCSI_Reporting are defined in table A.7.5.3.16.1-2.

-In this case, TSSB=TSMTC = 20 ms and TL1-RSRP,report = 5 ms.

-For sub-test1, Tactivation_time = 7 ms + 0.125 ms + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay).

-For sub-test2, Tactivation_time = 3 ms + M  + max (THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay)

-NR slot length is 0.125 ms for this test case.

During T3 the UE shall stop sending CSI reports for SCell no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

During T2 interruption of PCell / PSCell during SCell activation shall not happen outside the slot   to , as defined in clause 8.3, where TX =20 ms. m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length

During T3 interruption of PCell / PSCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.7.5.3.20SCell Activation and Deactivation of FR2 unkown SCell with FR2 PCell in non-DRX with L3 reporting during activation

## A.7.5.3.20.1Test Purpose and Environment

The purpose of this test is to verify that the SCell activation and deactivation times are within the requirements stated in clause 8.3.17, when the SCell is unknown in FR2 by the UE at the time of activation. In this test, UE shall perform two sub-tests where two different UL resource locations are configured.

The supported test configurations are shown in table A.7.5.3.20.1-1 below. The test parameters are the same as in clause A.4.5.3.3.1 except those described in the following clause. The general test parameters are given in table A.7.5.3.20.1-2 and cell-specific test parameters in table A.7.5.3.20.1-3 below. In this case, OTA related test parameters are shown in table A.7.5.3.20.1-4 below.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two carriers, PCell (Cell 1) in FR2 and SCell (Cell 2) in FR2. Cell 1 has constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) but is not aware of Cell 2 (SCell). The UE is monitoring the PCell. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. In the measurement control information for Cell 2, it is indicated to the UE that event-triggered reporting with Event A2 and reportOnActivation is used. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell activation.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n (where n mode 20=1), defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3. n+THARQ+Tactivation_time+TCSI_ReportingNR slot length

In sub-test1, TE shall transmit DCI 0-1 to PCell at slot .  The UE shall be able to send L3 measurements report of the SCell at slot  for sub-test 1.In sub-test2, TE shall transmit DCI 0-1 to PCell at slot  The UE shall be able to send L3 measurements report of the SCell at slot  for sub-test 2. TE will send TCI activation command after receiving L3 measurement report of the SCell. n+THARQ+7 ms NR slot lengthn+THARQ+7 ms+0.125 ms NR slot lengthn+THARQ+3 ms+M-0.125 ms NR slot length.n+THARQ+7 ms+ M NR slot length

The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of the SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell and PSCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CSI reporting for SCell is discontinued.

Table A.7.5.3.20.1-1: Supported test configurations for FR2 SCell activation case

Table A.7.5.3.20.1-2: General test parameters for FR2 SCell activation case with FR2 PCell

Table A.7.5.3.20.1-3: Cell specific test parameters for FR2 SCell activation case with FR2 active PCell

Table A.7.5.3.20.1-4: OTA related test parameters for FR2 SCell activation case with FR2 PCell

## A.7.5.3.20.2Test Requirements

During T2, the UE shall be able to send a valid L3-RSRP report for the SCell in the configured slots for CSI reporting at slot  for sub-test 1. For sub-test2, the UE shall be able to send a valid L3-RSRP for the SCell at slot  . The UE is not required to send L3-RSRP report after slot , where M is defined in 8.3.17.n+THARQ+7ms+0.125msNR slot lengthn+THARQ+7ms+MNR slot lengthn+THARQ+3ms+MNR slot length

During T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where n+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

-THARQ and TCSI_Reporting are defined in table A.7.5.3.16.1-2.

-In this case, TSSB=TSMTC = 20 ms and TL1-RSRP,report = 5 ms.

-For sub-test1, Tactivation_time = 7 ms + 0.125 ms + max(THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay).

-For sub-test2, Tactivation_time = 3 ms + M  + max (THARQ + Tuncertainty_MAC + 5 ms + TFineTiming, Tuncertainty_RRC + TRRC_delay)

-NR slot length is 0.125 ms for this test case.

During T3 the UE shall stop sending CSI reports for SCell no later than slot , as defined in clause 8.3.n+THARQ+3 msNR slot length

During T2 interruption of PCell / PSCell during SCell activation shall not happen outside the slot   to , as defined in clause 8.3, where TX =20 ms. m+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length

During T3 interruption of PCell / PSCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 msNR slot length

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.7.5.3.21OD-SSB based SCell Activation and deactivation of unknown SCell in FR2 DRX mode(OD-SSB Case 1)

## A.7.5.3.21.1Test Purpose and Environment

The purpose of this test is to verify that the OD-SSB based SCell activation and deactivation times are within the requirements stated in clause 8.3, when the SCell in FR2 is unknown by the UE at the time of activation.

The supported test configurations are shown in table A.7.5.3.21.1-1 and table A.7.5.3.21.1-1A below. The test parameters are given in table A.7.5.3.21.1-2 and cell-specific parameters in table A.7.5.3.21.1-3 below. OTA related test parameters are defined in Table A.7.5.3.21.1-4.

The test consists of three successive time periods, with duration of T1, T2 and T3, respectively. There are two NR carriers, each with one cell. Both cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1, but is not aware of Cell 2. The UE is only monitoring the PCC. The UE shall be continuously scheduled in the PCell throughout the whole test.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. The UE now starts monitoring the SCC. The test equipment sends a MAC message for activation of the SCell and the related OD-SSB transmission in the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T2. The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot , as defined in clause 8.3. The UE shall start reporting CSI in PCell after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in 5.2.2.5 in [26], and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PCell interruption due to activation of SCell shall occur in the slot  to , as defined in clause 8.3, where  is the interruption length given in clause 8.2.n+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthn+THARQ+3 msNR slot lengthn+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

Time period T3 starts when a MAC message for deactivation of SCell, sent from the test equipment to the UE in a slot # denoted m, is received at the UE antenna connector. The UE shall carry out deactivation of the SCell in a slot , as defined in clause 8.3, and The starting point of any PCell interruption due to the deactivation shall occur in the slot  to , as defined in clause 8.3.m+THARQ+3msNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

The test equipment verifies the deactivation time by counting the slots from the time when the SCell deactivation command is sent until CQI reporting for SCell is discontinued.

Table A.7.5.3.21.1-1: unknown FR2 SCell activation test configurations for NR PCell

Table A.7.5.3.21.1-1A: unknown FR2 SCell activation test configurations for NR SCell

Table A.7.5.3.21.1-2: General test parameters for unknown FR2 SCell activation case

Table A.7.5.3.21.1-3: Cell specific test parameters for NR PCell for unknown FR2 SCell activation case

Table A.7.5.3.21.1-4: OTA related test parameters for unknown FR2 SCell activation case

## A.7.5.3.21.2Test Requirements

During T2 the UE shall send the first CSI report for SCell in the first available uplink resource after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in clause 5.2.2.5 in TS 38.214 [26], and reporting after slot (). UE is allowed to postpone CSI report to next available UL resource if an available uplink resource is subject to interruption.n+1+THARQ+3 msNR slot length

During T3 the UE shall stop sending CSI reports for SCell at latest in a slot , as defined in clause 8.3.m+THARQ+3 msNR slot length

During T2 interruption of PCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

During T3 the starting point of interruption of PCell during SCell deactivation shall not happen outside the slot  to , as defined in clause 8.3.m+1+THARQNR slot lengthm+1+THARQ+3 msNR slot length

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90 %.

NOTE:During T2 if there are no uplink resources for reporting the valid CSI in a slot  as defined in clause 8.3 then the UE shall use the next available uplink resource for reporting the corresponding valid CSI.THARQ+Tactivtion_time+TCSI_ReportingNR slot length

## A.7.5.3.22OD-SSB based SCell Activation for known SCell in FR2 inter-band

## A.7.5.3.22.1Test Purpose and Environment

The purpose of this test is to verify that the OD-SSB based SCell activation and deactivation times are within the requirements stated in clause 8.3, when the SCell in FR2 is known by the UE at the time of activation.

The supported test configurations are shown in table A.7.5.3.22.1-1 below. The general test parameters are described in Tables A.7.5.3.22.1-2, and cell specific test parameters are described in Tables A.7.5.3.22.1-3. OTA related test parameters A.7.5.3.22.1 are shown in table A.7.5.3.22.1-4 below.

At the beginning of T1 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on NR. The UE now starts monitoring the SCell. The test equipment sends a MAC message for activation of the SCell and the related OD-SSB transmission in the SCell..

The point in time at which the MAC message is received at the UE antenna connector, in a slot # denoted m (where m mode 20=1), defines the start of time period T2. The UE shall be able to report valid CSI in PSCell for the activated SCell at latest in slot , as defined in clause 8.3.x. The UE shall start reporting CSI in PSCell after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k) and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. Any PSCell interruption due to activation of SCell shall occur in the slot  to slot , as defined in clause 8.3, where  is the interruption length given in clause 8.2m+THARQ+Tactivation_time+TCSI_ReportingNR slot lengthm+1+THARQNR slot lengthm+1+THARQ+3 ms+TXNR slot length+NinterruptionNinterruption

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell and PSCell during activation of SCell, respectively.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.7.5.3.22.1-1: Supported test configurations for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.22.1-2: General test parameters for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.22.1-3: Cell specific test parameters for FR2 SCell activation in FR2 inter-band

Table A.7.5.3.22.1-4: OTA related test parameters for FR2 SCell activation in FR2 inter-band

## A.7.5.3.22.2Test Requirements

During T2 the UE shall start sending CSI report for the SCell in the configured slots for CSI reporting after at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k). UE shall send the first CSI report for SCell after receiving at least one CSI-RS transmission occasion for channel measurement and reporting after slot (m+k), or in the next available uplink resource for CSI reporting if the slot was subject to interruption. Whether CSI report in a slot was interrupted is checked by monitoring ACK/NACK sent in PCell in the slot.

During T2, the UE shall start sending CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot , where m+THARQ+Tactivtion_time+TCSI_ReportingNR slot length

-THARQ is defined in Table A.7.5.3.14.1-2

-Tactivation_time = max(TFirstATRS + 5 ms, Tuncertainty_RRC + TRRC_delay-THARQ)

-TCSI_Reporting = 10 ms

-NR slot length is 0.125 ms for this test case.

During T2 interruption of PCell during SCell activation shall not happen outside the slot  to , as defined in clause 8.3.n+1+THARQNR slot lengthn+1+THARQ+3 ms+TXNR slot length+Ninterruption

The interruption on any activated serving cell shall not be more than the values specified for SA in clause 8.2.2.2.2.

All of the above test requirements shall be fulfilled in order for the observed SCell activation delay and SCell deactivation delay to be counted as correct. The rate of correct observed SCell activation delay and SCell deactivation delay during repeated tests shall be at least 90 %.

## A.7.5.3.23EMR based SCell activation of unknown SCell in FR2

## A.7.5.3.23.1Test Purpose and Environment

The purpose of this test is to verify that the EMR (early measurement reporting) based SCell activation delay is within the requirements stated in clause 8.3.2A for the UE supporting fastSCellActivationEarlyMeas-r19, when the SCell in FR2 is unknown by the UE at the time of activation.

In the test, there are two cells: NR Cell 1 as PCell in FR2 on NR RF channel 1 and NR Cell 2 as SCell in FR2 on NR RF channel 2. The supported test configurations are shown in table A.7.5.3.23.1-1 below. The general test parameters are described in Tables A.7.5.3.23.1-2, and cell specific test parameters are described in Tables A.7.5.3.23.1-3. OTA related test parameters are shown in table A.7.5.3.23.1-4 below.

The test consists of 6 successive time periods, with time duration of T1, T2, T3, T4, T5 and T6 respectively.

During T1, the UE is connected to Cell 1 (PCell) only and shall not have any timing information of Cell 2. UE is configured with early measurement reporting for Cell 2 in:

measIdleCarrierListNR-r16 for UE supporting measValidationReportEMR-r18 or idleInactiveNR-MeasReport-r16 only, or

measReselectionCarrierListNR-r18 for UE supporting measValidationReportReselectionMeasurements.

Beam level reporting for early measurements is configured. The time point when UE receives RRC_Release message from the TE defines as the starting point of T2.

At the beginning of T2, Cell 2 becomes detectable however no cell reselection is being performed. Signal level of Cell 2 is set to fixed value according to Table A.7.5.3.23.1-4. The duration of T2 is set to fixed value according to the Table A.7.5.3.23.1-2.

At the beginning of T3, the signal level of the Cell 2 is set to another value according to the table A.7.5.3.23.1-4. The duration of the T3 equals to measIdleValidityDuration-r18 or measReselectionValidityDuration-r18 depending on the UE capabilities of the UE under test.

During T2 and T3, UE is in RRC_IDLE mode.

The time when TE sends the paging message is defined as the starting point of T4. During T4, the UE shall send a valid measurement report with SSB index of Cell 2 to the PCell.

At the beginning of T5 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2. UE is only monitoring the PCC and shall be continuously scheduled in the PCell when UE is connected to PCell. Then the test equipment sends a MAC message for activation of the SCell.

The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T6.

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.7.5.3.23.1-1: Supported test configurations for EMR based SCell activation in FR2

Table A.7.5.3.23.1-2: General test parameters for EMR based SCell activation in FR2

Table A.7.5.3.23.1-3: Cell specific test parameters in Idle and Connected mode for EMR based SCell activation in FR2

Table A.7.5.3.23.1-4: OTA related test parameters for EMR based SCell activation in FR2

## A.7.5.3.23.2Test Requirements

During T6, the UE shall start reporting CSI after at least one CSI-RS transmission occasion for channel measurement plus nCSI_ref  slots, as defined in 5.2.2.5 in [26], and reporting after slot  and shall report CQI index 0 (out-of-range) until the SCell activation has been completed. n+THARQ+3 msNR slot length

During T6, the UE shall be able to send CSI reports for the SCell with non-zero CQI index in the configured slots for CSI reporting no later than slot  as defined in clause 8.3.2A, where n+THARQ+Tactivation_time+TCSI_ReportingNR slot length

-THARQ is defined in Table A.7.5.3.23.1-2

-Tactivation_time = TFirstSSB_MAX + 15*TSMTC_MAX + max(Tuncertainty_MAC + 5ms + TFineTiming, Tuncertainty_RRC + TRRC_delay-THARQ), which allows 345 ms.

For this test case, TFirstSSB_MAX=TSMTC_MAX=TFineTiming=Trs=20 ms.

-TCSI_Reporting = 10 ms

-NR slot length is 0.125 ms for this test case.

The observed SCell activation delay fulfilling the SCell activation delay requirements specified in clause 8.3.2A in TS 38.133 is counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

## A.7.5.3.24EMR based SCell activation of unknown SCell in FR2 in RRC Inactive

## A.7.5.3.24.1Test Purpose and Environment

The purpose of this test is to verify that the EMR (early measurement reporting) based direct SCell activation delay is within the requirements stated in clause 8.3.2A, when the SCell in FR2 is unknown by the UE but the EMR measurements are available at the time of activation.

In the test, there are two cells: NR Cell 1 as PCell in FR1 on NR RF channel 1 and NR Cell 2 as SCell in FR2 on NR RF channel 2. The supported test configurations for PCell and SCell are provided in table A.7.5.3.24.1-1 and table A.7.5.3.24.1-1A respectively. The general test parameters are given in table A.7.5.3.24.1-2 and cell-specific parameters for PCell and SCell are given in table A.7.5.3.24.1-3 and table A.7.5.3.24.1-4 respectively.

Table A.7.5.3.24.1-1: supported test configurations for NR PCell

Table A.7.5.3.24.1-1A: supported test configurations for NR SCell

The test consists of 5 successive time periods, with time duration of T1, T2, T3, T4, and T5 respectively.

During T1, the UE is connected to Cell 1 (PCell) only and shall not have any timing information of Cell 2. UE is configured with inter-frequency measurement reporting for Cell 2 in:

-measIdleCarrierListNR-r16 for UE supporting measValidationReportEMR-r18 or idleInactiveNR-MeasReport-r16 only, or

-measReselectionCarrierListNR-r18 for UE supporting measValidationReportReselectionMeasurements.

-The UE is configured with beam level reporting for early measurements.

The time point when UE receives RRC_Release message from the TE defines the starting point of T2.

At the beginning of T2, Cell 2 becomes detectable but the cell reselection threshold is not occurring. Signal level of Cell 2 is set to the value given in table A.7.5.3.24.1-4. The duration of T2 is set to a fixed value according to the table A.7.5.3.24.1-2.

At the beginning of T3, the signal level of the Cell 2 is set to a value according to the table A.7.5.3.24.1-4.

The duration of the T3 equals to measIdleValidityDuration-r18 or measReselectionValidityDuration-r18 depending on the UE capabilities of the UE under test.

During T2 and T3, UE is in RRC_IDLE mode.

The time when TE sends the paging message is defined as the starting point of T4.

During T4, the UE shall send a valid measurement report with SSB index of Cell 2 to the PCell in RRCResumeComplete message

At the beginning of T5 the UE receives an RRC message by which the SCell (Cell 2) becomes configured on radio channel 2.

T5: At the beginning of T5, the UE receives RRC message for direct addition and activation of the SCell (Cell 2). The point in time at which the RRC message is received at the UE antenna connector is denoted as slot #n.

The UE shall be able to report valid CSI in PCell for the activated SCell at latest in slot n+Ndirect/(NR slot length) where Ndirect = TRRC_Process + T1 + Tactivation_time + TCSI_Reporting - 3 ms (TCI state is not indicated within Tactivation_time) or

Ndirect = TRRC_Process + T1 + THARQ + Tactivation_time + TCSI_Reporting (TCI state is not indicated within Tactivation_time).

Table A.7.5.3.24.1-2: General test parameters

Table A.7.5.3.24.1-3: Cell specific test parameters for NR PCell

Table A.7.5.3.24.1-4: Cell specific test parameters for NR SCell

A.7.5.3.24.2Test Requirements

The UE shall complete the SCell activation no later than at slot.  n+THARQ+Tactivation_time+TCSI_ReportingNR slot length

The UE shall report non-zero CQI for SCell from slot n +  and onwards throughout time period T5.THARQ+Tactivation_time+TCSI_ReportingNR slot length

is defined in clause 8.3.2A in TS 38.133 for FR2 SCell as Tactivation_time is TFirstSSB_MAX + 15*TSMTC_MAX + 5msTactivation_time

The observed SCell activation delay fulfilling the SCell activation delay requirements specified in clause 8.3.2A in TS 38.133 is counted as correct. The rate of correct observed SCell activation delay during repeated tests shall be at least 90 %.

## A.7.5.3.25PUCCH SCell Activation of unknown SCell for UE supporting EMR in FR2

## A.7.5.3.25.1Test Purpose and Environment

The purpose of this test is to verify that EMR (early measurement reporting) based SCell activation is done within the required time period defined in clause 8.3.12, when PUCCH for a being activated SCell is configured on the NR FR2 SCell. The PCell and SCell are in different FR2 bands. The SCell is unknown by the UE and the UE does not have valid TA for a sTAG which the SCell belongs to at the time of activation. Supported test configurations are shown in table A.7.5.3.25.1-1.

The general test parameters and NR cell specific test parameters are given in Table A.7.5.3.25.1-2 and A.7.5.3.25.1-3 below. OTA related test parameters are shown in table A.7.5.3.25.1-4 below.

In the test there are two cells: Cell 1 and Cell 2. Cell 1 is PCell, Cell 2 is the PUCCH SCell being activated. The test consists of five successive time periods with duration of T1, T2, T3, T4 and T5, respectively. The UE shall be continuously scheduled in Cell 1 (PCell) throughout the test.

During T1, the UE is connected to the PCell (Cell 1) on NR radio channel 1 (PCC), but is not aware of SCell (Cell 2) on NR radio channel 2 (SCC). The PCell is in the pTAGs and the SCell is in a sTAG. The UE is only monitoring the PCC and configured with inter-frequency measurement reporting for Cell 2 in:

measIdleCarrierListNR-r16 for UE supporting measValidationReportEMR-r18, or

idleInactiveNR-MeasReport-r16 only, or

measReselectionCarrierListNR-r18 for UE supporting measValidationReportReselectionMeasurements.

Beam level reporting for early measurements is configured when UE receives RRC_Release message from the TE defines the starting point of T2.

At the beginning of T2, Cell 2 becomes detectable however cell reselection shall not be performed. During T2, UE will perform the inter-frequency measurement with the configuration with SCC. Signal level of Cell 2 is set to the value given in table A.7.5.3.25.1-3.

At the beginning of T3, the signal level of the neighbour cell is set to turned off. The duration of the T3 equals to measIdleValidityDuration-r18 or measReselectionValidityDuration-r18.

During the T2 and T3 the UE is in the RRC_IDLE mode.

The time when UE receive paging from the TE denoted as the starting time of T4. During T4 UE needs to send a valid early measurement report. The time when TE receives the EMR report denote as the end of the T4.

At the beginning of T5 the UE receives an RRC message by which the SCell(Cell2) becomes configured on radio channel 2. UE is only monitoring the PCC and shall be continuously scheduled in the PCell when UE is connected to PCell.

The TE will send an MAC CE message to activate the PUCCH SCell (SCC).The point in time at which the MAC message is received at the UE antenna connector, in slot # denoted n, defines the start of time period T6. During T6, the test equipment should send a PDCCH order to the UE to initiate RA procedure on the PUCCH SCell at slot n+  as defined in clause 8.3.12 after UE report on PCell.THARQ+Tactivation_time+max ((TFirst_available_CSI +TCSI_processing),   3*Ttarget_PL-RS)+TCSI_Reporting_afterNR slot length

The test equipment verifies the activation time by counting the slots from the time when the SCell activation command is sent until a CSI report with other than CQI index 0 is received.

Table A.7.5.3.25.1-1: PCell and PUCCH SCell Activation test configurations in FR2 inter-band

Table A.7.5.3.25.1-2: General test parameters for PCell and PUCCH SCell activation in FR2 inter-band

Table A.7.5.3.25.1-3: NR Cell specific test parameters for PCell and PUCCH SCell activation in FR2 inter-band

Table A.7.5.3.25.1-4: OTA related test parameters for PCell and PUCCH SCell activation in FR2 inter-band

## A.7.5.3.25.2Test Requirements

During the time period T3 the UE is in Idle mode and the signal level of Cell 2 is changed. The UE shall not perform reselection. The UE shall perform Idle Mode CA measurement according to section 4.4.

At the end of T4, UE is requested to transmit early measurement report for Cell 2 to the PCell.

After receiving the requested early measurement report, the test equipment verifies the slot n+. The is defined in clause 8.3.2A.THARQ+Tactivation_time+max ((TFirst_available_CSI +TCSI_processing),   3*Ttarget_PL-RS)+TCSI_Reporting_afterNR slot lengthTactivation_time

The rate of correct events observed during repeated tests shall be at least 90%. UE needs to report SSB index.

## A.7.5.4Void

## A.7.5.5Beam Failure Detection and Link recovery procedures

## A.7.5.5.1Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode

## A.7.5.5.1.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5.

The test parameters are given in Tables A.7.5.5.1.1-1, A.7.5.5.1.1-2, A.7.5.5.1.1-3 and A.7.5.5.1.1-4 below. There is one cell, cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.5.1.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.7.5.5.1.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

Table A.7.5.5.1.1-1: Supported test configurations for FR2 PCell

Table A.7.5.5.1.1-2: General test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.7.5.5.1.1-3: Cell specific test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.7.5.5.1.1-4: Void

Figure A.7.5.5.1.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.7.5.5.1.1-2: SSB_RP level variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.7.5.5.1.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 960+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.5.2Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in DRX mode

## A.7.5.5.2.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects SSB-based beam failure in the set q0 configured for a serving cell and that the UE performs correct SSB-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the SSB based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5.

The test parameters are given in Tables A.7.5.5.2.1-1, A.7.5.5.2.1-2, A.7.5.5.2.1-3, A.7.5.5.2.1-4 and A.7.5.5.2.1-5 below. There is one cell, cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.5.2.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.7.5.5.2.1-2 shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.5.5.2.1-1: Supported test configurations for FR2 PCell

Table A.7.5.5.2.1-2: General test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.7.5.5.2.1-3: Cell specific test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in DRX mode

Table A.7.5.5.2.1-4: Void

Table A.7.5.5.2.1-5: Void

Figure A.7.5.5.2.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in DRX mode

Figure A.7.5.5.2.1-2: SSB_RP level variation for SSB-based beam failure detection and link recovery testing in DRX mode

## A.7.5.5.2.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiate link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 560+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.5.3Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode

## A.7.5.5.3.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5.

The test parameters are given in Tables A.7.5.5.3.1-1, A.7.5.5.3.1-2, and A.7.5.5.3.1-3 below. There is one cell, cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.5.3.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.7.5.5.3.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

Table A.7.5.5.3.1-1: Supported test configurations for FR2 PCell

Table A.7.5.5.3.1-2: General test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.7.5.5.3.1-3: Cell specific test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.7.5.5.3.1-4: Void

Table A.7.5.5.3.1-5: Void

Figure A.7.5.5.3.1-1: SNR variation for CSI-RS based beam failure detection and link recovery testing in non-DRX mode

Figure A.7.5.5.3.1-2: CSI-RS_RP level variation for CSI-RS based beam failure detection and link recovery testing in non-DRX mode

## A.7.5.5.3.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.5.4Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode

## A.7.5.5.4.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5.

The test parameters are given in Tables A.7.5.5.4.1-1, A.7.5.5.4.1-2, A.7.5.5.4.1-3, and A.7.5.5.4.1-4 below. There is one cell, cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.5.4.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.7.5.5.4.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.5.5.4.1-1: Supported test configurations for FR2 PCell

Table A.7.5.5.4.1-2: General test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.7.5.5.4.1-3: Cell specific test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.7.5.5.4.1-4: Void

Table A.7.5.5.4.1-5: Void

Table A.7.5.5.4.1-6: Void

Figure A.7.5.5.4.1-1: SNR variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Figure A.7.5.5.4.1-2: CSI-RS_RP level variation for CSI-RS based beam failure detection and link recovery testing in DRX mode

## A.7.5.5.4.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.5.5Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode

## A.7.5.5.5.1Test Purpose and Environment

The purpose is to test scheduling availability restrictions when the UE is performing beam failure detection or when the UE is performing L1-RSRP measurement for candidate beam detection, when no DRX is used. This test will verify the scheduling availability restriction requirements in clause 8.5.7 and 8.5.8.

The test parameters are given in Tables A.7.5.5.5.1-1, A.7.5.5.5.1-2 and A.7.5.5.5.1-3 below. There is one cell, cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.5.5.1-1 shows the variation of the downlink SNR of the SSB index 0 in the active cell to emulate SSB based beam failure. Figure A.7.5.5.5.1-2 shows the variation of the downlink L1-RSRP of the SSB index 1 used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. This test will focus on the scheduling availability during beam failure detection) and candidate beam detection. In the test, DRX configuration is not enabled. Test is to test the scheduling availability restriction of UE performing beam failure detection and candidate beam detection when SSB RS configured for Beam failure detection and candidate beam detection. During the test the UE is scheduled to transmit continuously in UL.

Table A.7.5.5.5.1-1: Supported test configurations for FR2 PCell

Table A.7.5.5.5.1-2: General test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.7.5.5.5.1-3: Cell specific test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.7.5.5.5.1-1: SNR variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.7.5.5.5.1-2: SSB_RP level variation for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.7.5.5.5.2Test Requirements

The UE behaviour during time duration T3 follows the requirements defined in clause 8.5.7.3:

-The UE is not expected to transmit PUCCH/PUSCH/SRS or receive PDCCH/PDSCH/CSI-RS for tracking/CSI-RS for CQI on BFD-RS symbols to be measured for beam failure detection.

The UE behaviour during time durations T4 and T5 follows the requirements defined in clause 8.5.8.3:

-The UE is not expected to transmit PUCCH/PUSCH or receive PDCCH/PDSCH on reference symbols to be measured for candidate beam detection.

## A.7.5.5.6Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in non-DRX mode

## A.7.5.5.6.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for an active SCell and that the UE performs correct CSI-RS-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the SCell with schedulingRequestID-BFR-SCell-r16 configuration, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 SCell requirements in clause 8.5.

The test parameters are given in Tables A.7.5.5.6.1-1, A.7.5.5.6.1-2 and A.7.5.5.6.1-3. There are two cells, cell 1 is the active PCell and cell 2 is the active SCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.5.6.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active SCell to emulate CSI-RS based beam failure. Figure A.7.5.5.6.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

Table A.7.5.5.6.1-1: Supported test configurations for FR2 PCell and SCell

Table A.7.5.5.6.1-2: General test parameters for FR2 SCell for beam failure detection and link recovery testing in non-DRX mode

Table A.7.5.5.6.1-3: Cell specific test parameters for FR2 SCell for beam failure detection and link recovery testing in non-DRX mode

Figure A.7.5.5.6.1-1: SNR variation for beam failure detection and link recovery testing for SCell in non-DRX mode

Figure A.7.5.5.6.1-2: CSI-RS_RP level variation for CSI-RS based beam failure detection and link recovery testing for SCell in non-DRX mode

## A.7.5.5.6.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 in A.7.5.5.6.1 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initial link recovery. During T4 and T5 the UE measures and evaluates beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit PUCCH with LRR, followed by BFR MAC CE containing a beam associated with the candidate beam set q1. The UE shall not transmit PUCCH with an LRR with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.5.7Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode

## A.7.5.5.7.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for an active SCell and that the UE performs correct CSI-RS-based link recovery based on beam candidate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP of the SCell with schedulingRequestID-BFR-SCell-r16 configuration, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 SCell requirements in clause 8.5.

The test parameters are given in Tables A.7.5.5.7.1-1, A.7.5.5.7.1-2 and A.7.5.5.7.1-3. There are two cell, cell 1 is the active PCell and cell 2 is the active SCell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.5.7.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active SCell to emulate CSI-RS based beam failure. Figure A.7.5.5.7.1-2 shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.5.5.7.1-1: Supported test configurations for FR2 PCell and SCell

Table A.7.5.5.7.1-2: General test parameters for FR2 SCell for beam failure detection and link recovery testing in DRX mode

Table A.7.5.5.7.1-3: Cell specific test parameters for FR2 SCell for beam failure detection and link recovery testing in DRX mode

Figure A.7.5.5.7.1-1: SNR variation for beam failure detection and link recovery testing for SCell in DRX mode

Figure A.7.5.5.7.1-2: CSI-RS_RP level variation for CSI-RS based beam failure detection and link recovery testing for SCell in DRX mode

## A.7.5.5.7.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 in A.7.5.5.7.1 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initial link recovery. During T4 and T5 the UE measures and evaluates beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit PUCCH with LRR, followed by BFR MAC CE containing a beam associated with the candidate beam set q1. The UE shall not transmit PUCCH with an LRR with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.5.8Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode for UE fulfilling relaxed measurement criterion

## A.7.5.5.8.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5.3.4 for UE fulfilling good serving cell quality relaxed measurement criteria. The test parameters are given in Tables A.7.5.5.8.1-1, A.7.5.5.8.1-2, A.7.5.5.8.1-3, and A.7.5.5.8.1-4 below. There is one cell, cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.5.8.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.7.5.5.8.1-1 additionally shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

As specified in the Test Purpose, the UE is configured with the relaxed measurement criterion for both low mobility and good serving cell quality defined in clause 5.7.13.2 in TS 38.331 [2]. At the beginning of T1, the UE has fulfilled the good serving cell quality relaxation measurements criterion and is performing relaxed measurements for beam failure detection.

-goodServingCellEvaluationBFD [2] criterion is configured according to the parameters listed in table A.7.5.5.8.1-2;

-lowMobilityEvalutationcConnected [2] criterion is configured according to the parameters listed in table A.7.5.5.8.1-2.

Table A.7.5.5.8.1-1: Supported test configurations for FR2 PCell

Table A.7.5.5.8.1-2: General test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.7.5.5.8.1-3: Cell specific test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Figure A.7.5.5.8.1-1: SNR and L1-RSRP variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

## A.7.5.5.8.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiat link recovery, and exit from relaxed measurements. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.5.9TRP specific Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode

## A.7.5.5.9.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects TRP specific CSI-RS-based beam failure and link recovery in the sets  and  for TRP0 when DRX is used for an FR2 active SCell requirements in clause 8.18.q0,0q1,0

The test parameters are given in Tables A.7.5.5.9.1-1, A.7.5.5.9.1-2 and A.7.5.5.9.1-3. There are two cell, cell 1 is the active PCell and cell 2 is the active SCell, in the test. SCell is configured with two TRPs. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.5.9.1-1 shows the variation of the downlink SNR of the CSI-RS in set  and  in the active SCell for TRP0 and TRP1 respectively. Figure A.7.5.5.9.11-1additionally shows the variation of the downlink L1-RSRP of the CSI-RS in   for TPR0. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1 and cell 2. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 2 ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.q0,0q0,1q1,0

Table A.7.5.5.9.1-1: Supported test configurations for FR2 PCell and SCell

Table A.7.5.5.9.1-2: General test parameters for FR2 SCell for beam failure detection and link recovery testing in DRX mode

Table A.7.5.5.9.1-3: Cell specific test parameters for FR2 SCell for beam failure detection and link recovery testing in DRX mode

Figure A.7.5.5.9.1-1: SNR and L1-RSRP variation for beam failure detection and link recovery testing for SCell in DRX mode

## A.7.5.5.9.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 in A.7.5.5.9.1 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1 for TRP1 and TRP2.

During the period from time point A to time point B the UE shall transmit uplink signal in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3, T4, T5, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1 for TRP2.

During T3 the UE shall detect beam failure and initiate link recovery for TRP1. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q0,1.

No later than time point F occurring no later than D1 = [520]+10 ms after the start of T5, the UE shall transmit PUCCH with LRR, followed by BFR MAC CE containing a beam associated with the candidate beam set q0,1. The UE shall not transmit PUCCH with an LRR with the candidate beam set q0,1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.5.10TRP specific Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode

## A.7.5.5.10.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects TRP specific SSB-based beam failure and link recovery in the sets  and  for TRP1 with schedulingRequestID-BFR-r17 configured, when no DRX is used for an FR2 serving cell requirements in clause 8.18.q0,0q0,1

The test parameters are given in Tables A.7.5.5.10.1-1, A.7.5.5.10.1-2, A.7.5.5.10.1-3 and A.7.5.5.10.1-4 below. There is one active serving cell configured with two TRPs in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.5.10.1-1 shows the variation of the downlink SNR of the SSB in set  and  for TRP1 and TRP2 respectively. Figure A.7.5.5.10.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set   for TPR1.q0,0q1,0q0,1

Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled. The UE is configured to perform inter-frequency measurements using GP ID #0 (40 ms) in test 1.

Table A.7.5.5.10.1-1: Supported test configurations for FR2 PCell

Table A.7.5.5.10.1-2: General test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.7.5.5.10.13: Cell specific test parameters for FR2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.7.5.5.10.1-4: Void

Figure A.7.5.5.10.1-1: SNR and L1-RSRP variation SSB for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.7.5.5.10.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1 for TRP 0 and TRP1.

During the period from time point A to time point B the UE shall transmit uplink signal for TRP 0 and TRP1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3, T4, T5, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission for TRP 1.

During T3 the UE shall detect beam failure and initiate link recovery for TRP 0. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1,0.

No later than time point F occurring no later than D1 = 960+10 ms after the start of T5, the UE shall transmit PUCCH with LRR, followed by BFR MAC CE containing a beam associated with the candidate beam set q1,0. The UE shall not transmit PUCCH with an LRR with the candidate beam set q1,0 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.5.11Beam Failure Detection and Link Recovery Test for FR2-2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode

## A.7.5.5.11.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2-2 serving cell requirements in clause 8.5.

The test parameters are given in Tables A.7.5.5.11.1-1, A.7.5.5.11.1-2, and A.7.5.5.11.1-3 below. There is one cell, cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.5.11.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.7.5.5.11.1-1 additionally shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. In the test, DRX configuration is not enabled.

Table A.7.5.5.11.1-1: Supported test configurations for FR2-2 PCell

Table A.7.5.5.11.1-2: General test parameters for FR2-2 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.7.5.5.11.1-3: Cell specific test parameters for FR2-2 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.7.5.5.11.1-4: Void

Table A.7.5.5.11.1-5: Void

Figure A.7.5.5.11.1-1: SNR and L1-RSRP variation for CSI-RS based beam failure detection and link recovery testing in non-DRX mode

## A.7.5.5.11.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.5.12Beam Failure Detection and Link Recovery Test for FR2-2 PCell configured with CSI-RS-based BFD and LR in DRX mode

## A.7.5.5.12.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the UEs active DL BWP, during the evaluation period, and link recovery, when DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2-2 serving cell requirements in clause 8.5.

The test parameters are given in Tables A.7.5.5.12.1-1, A.7.5.5.12.1-2, A.7.5.5.12.1-3, and A.7.5.5.12.1-4 below. There is one cell, cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.5.12.1-1 shows the variation of the downlink SNR of the CSI-RS in set q0 in the active cell to emulate CSI-RS based beam failure. Figure A.7.5.5.12.1-1 additionally shows the variation of the downlink L1-RSRP of the CSI-RS in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5  ms. In the test, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.5.5.12.1-1: Supported test configurations for FR2-2 PCell

Table A.7.5.5.12.1-2: General test parameters for FR2-2 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.7.5.5.12.1-3: Cell specific test parameters for FR2-2 PCell for CSI-RS-based beam failure detection and link recovery testing in DRX mode

Table A.7.5.5.12.1-4: Void

Table A.7.5.5.12.1-5: Void

Table A.7.5.5.12.1-6: Void

Figure A.7.5.5.12.1-1: SNR and L1-RSRP variation for CSI-RS-based beam failure detection and link recovery testing in DRX mode

## A.7.5.5.12.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the UE shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.5.13Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2-2 PCell configured with SSB-based BFD and LR in non-DRX mode

## A.7.5.5.13.1Test Purpose and Environment

The purpose is to test scheduling availability restrictions when the UE is performing beam failure detection or when the UE is performing L1-RSRP measurement for candidate beam detection, when no DRX is used. This test will verify the scheduling availability restriction requirements in clause 8.5.7 and 8.5.8.

The test parameters are given in Tables A.7.5.5.13.1-1, A.7.5.5.13.1-2 and A.7.5.5.13.1-3 below. There is one cell, cell 1 which is the active cell, in the test. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.5.13.1-1 shows the variation of the downlink SNR of the SSB in set q0 in the active cell to emulate SSB based beam failure. Figure A.7.5.5.13.1-1 additionally shows the variation of the downlink L1-RSRP of the SSB in set q1 of the candidate beam used for link recovery. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 5 ms. This test will focus on the scheduling availability during beam failure detection) and candidate beam detection. In the test, DRX configuration is not enabled. Test is to test the scheduling availability restriction of UE performing beam failure detection and candidate beam detection when SSB RS configured for Beam failure detection and candidate beam detection. During the test the UE is scheduled to transmit continuously in UL.

Table A.7.5.513.1-1: Supported test configurations for FR2-2 PCell

Table A.7.5.5.13.1-2: General test parameters for FR2-2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Table A.7.5.5.13.1-3: Cell specific test parameters for FR2-2 PCell for SSB-based beam failure detection and link recovery testing in non-DRX mode

Figure A.7.5.5.13.1-1: SNR and L1-RSRP variation SSB for SSB-based beam failure detection and link recovery testing in non-DRX mode

## A.7.5.5.13.2Test Requirements

The UE behaviour during time duration T3 follows the requirements defined in clause 8.5.7.3:

-The UE is not expected to transmit PUCCH/PUSCH/SRS or receive PDCCH/PDSCH/CSI-RS for tracking/CSI-RS for CQI on BFD-RS symbols to be measured for beam failure detection.

The UE behaviour during time durations T4 and T5 follows the requirements defined in clause 8.5.8.3:

-The UE is not expected to transmit PUCCH/PUSCH or receive PDCCH/PDSCH on reference symbols to be measured for candidate beam detection.

## A.7.5.5.14TRP specific Beam Failure Detection and Link Recovery for FR2 PCell configured with CSI-RS-based BFD and LR and multi-Rx operation in DRX mode

## A.7.5.5.14.1Test Purpose and Environment

The purpose of this test is to verify that the UE properly detects TRP specific CSI-RS-based beam failure and link recovery in the sets  and  for TRP0 and sets  and  for TRP1 when DRX is used for an FR2 PCell requirements in clause 8.18.q0,0q1,0q0,1q1,1

The test parameters are given in Tables A.7.5.5.14.1-1, A.7.5.5.14.1-2 and A.7.5.5.14.1-3. Cell 1 is the active PCell in the test. PCell is configured with two TRPs. The test consists of five successive time periods, with time duration of T1, T2, T3, T4 and T5 respectively. Figure A.7.5.5.14.1-3 shows the variation of the downlink SNR of the CSI-RS in set  and  in the PCell for TRP0 and TRP1 respectively. Figure A.7.5.5.14.1-3 additionally shows the variation of the downlink L1-RSRP of the CSI-RS in   for TPR0. Prior to the start of the time duration T1, the UE shall be fully synchronized to cell 1. The UE shall be configured for periodic CSI reporting with a reporting periodicity of 2 ms. q0,0q0,1q1,0

In the test, UE is capable of multi-Rx operation and configured with group-based beam reporting (GBBR) on the cell 1.  During T1, UE shall be able to report via beam pair associated with sets  for TRP0 and  for TRP1. After T5, UE shall be able to report via new beam pair associated with sets  for TRP0 and  for TRP1q0,0q0,1q1,0q0,1

During T2 and T3, for beam failure detection, CSI-RS resources in the two sets  for TRP0 and  for TRP1 are overlapped on the same OFDM symbol according to CSI-RS configuration in table A.7.5.5.14.1-2 and A.3.14.2-3, and the conditions in clause 8.18.3.2 are met, at least including:q0,0q0,1

-Both CSI-RSs are not in any CSI-RS resource set with repetition ON

-The CSI-RS in set  has same QCL source as the active TCI state of one PDSCH, and the CSI-RS in set  has same QCL source as the active TCI state of the other PDSCHq0,0q0,1

-Resources of the active TCI states for the two PDSCHs have been reported as a resource group in Rel-17 group-based RSRP report.

During T4 and T5, for candidate beam detection, CSI-RS resources in the two sets  for TRP0 and  for TRP1 are also overlapped according to CSI-RS configuration in table A.7.5.5.14.1-2 and and A.3.14.2-3.q1,0q0,1

In addition, DRX configuration is enabled in PCell and DRX inactivity timer has already been expired, i.e. UE tries to decode PDCCH and to send periodic CQI during the period when On-duration timer is running. Time alignment timers shall be set to “infinity” so that UL timing alignment is maintained during the test.

Table A.7.5.5.14.1-1: Supported test configurations for FR2 PCell

Table A.7.5.5.14.1-2: General test parameters for FR2 PCell for beam failure detection and link recovery testing in DRX mode

Table A.7.5.5.14.1-3: Cell specific test parameters for FR2 PCell for beam failure detection and link recovery testing in DRX mode

Figure A.7.5.5.14.1-1: SNR and L1-RSRP variation for beam failure detection and link recovery testing for PCell in DRX mode

## A.7.5.5.14.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 in A.7.5.5.14.1 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1 with sets  for TRP0 and sets  for TRP1. During T1, UE reports via beam pair assoiated with sets  for TRP0 and  for TRP1.q0,0q0,1q0,0q0,1

During the period from time point A to time point B the UE shall transmit uplink signal in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3, T4, T5, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1 with sets  for TRP1.q0,1

During T3 the UE shall detect beam failure and initiate link recovery for TRP0. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate sets  for TRP0 and  for TRP1.q1,0q0,1

No later than time point F occurring no later than D1 after the start of T5, the UE shall transmit PUCCH with LRR, followed by BFR MAC CE containing beam associated with the candidate beam with sets  for TRP0. The UE shall not transmit PUCCH with an LRR with candidate beam set   for TRP0 earlier than time point B. q1,0q1,0

After T5, UE shall be able to report via new beam pair associated with sets  for TRP0 and  for TRP1.q1,0q0,1

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.5.15Beam Failure Detection and Link Recovery Test for FR2 Pcell configured with CSI-RS-based BFD and LR in non-DRX mode for a UE operating with SBFD

## A.7.5.5.15.1Test Purpose and Environment

The purpose of this test is to verify that the UE supporting supportSBFD properly detects CSI-RS-based beam failure in the set q0 configured for a serving cell operating on SBFD, and that the UE performs correct CSI-RS-based link recovery based on beam candicate set q1. The purpose is to test the downlink monitoring for beam failure detection within the Ues active DL BWP, during the evaluation period, and link recovery, when no DRX is used. This test will partly verify the CSI-RS based beam failure detection and link recovery for an FR2 serving cell requirements in clause 8.5.

Supported test configurations are specified in Table A.7.5.5.15.1-1. General test parameters as specified in Table A.7.5.5.3.1-2 apply except those specified in Table A.7.5.5.15.1-2. Cell specific test parameters as specified in Table A.7.5.5.3.1-3 apply except those specified in table A.7.5.5.15.1-3.

The test procedure specified in clause A.7.5.5.3.1 applies to this test. In addition, during T3 and T5, there is overlapping between occasions of the CSI-RS resource for BFD (q0) and dynamic UL transmission on SBFD symbols, as specified in A.3.

Table A.7.5.5.15.1-1: Supported test configurations for FR2 Pcell

Table A.7.5.5.15.1-2: General test parameters for FR2 Pcell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

Table A.7.5.5.15.1-3: Cell specific test parameters for FR2 PCell for CSI-RS-based beam failure detection and link recovery testing in non-DRX mode

## A.7.5.5.15.2Test Requirements

The UE behaviour during time durations T1, T2, T3, T4 and T5 shall be as follows:

During the time duration T1 and T2, the UE shall transmit uplink signal at least in all subframes configured for CSI transmission on Cell 1.

During the period from time point A to time point B the UE shall transmit uplink signal in Cell 1 in all uplink slots configured for CSI transmission according to the configured periodic CSI reporting for Cell 1.

During T3 the shall detect beam failure and initiat link recovery. During T4 and T5 the UE measures and evaluate beam candidate from beam candidate set q1.

No later than time point F occurring no later than D1 = 260+10+80 ms after the start of T5, the UE shall transmit preamble on a beam associated with the candidate beam set q1. The UE shall not transmit preamble on a beam associated with the candidate beam set q1 earlier than time point B.

Test is concluded once the test equipment has received the initial preamble transmission from the UE. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.6Active BWP switch

## A.7.5.6.1DCI-based and Timer-based Active BWP Switch

## A.7.5.6.1.1NR FR2- NR FR2 DL active BWP switch of SCell with non-DRX in SA

A.7.5.6.1.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6, and interruption requirement on other active serving cell defined in clause 8.2.2.2.5.

The supported test configurations are shown in table A.7.5.6.1.1.1-1 below. The test scenario comprises of one PCell (Cell 1) and one SCell (Cell 2) as given in table A.7.5.6.1.1.1-2. NR Cell-specific parameters are specified in table A.7.5.6.1.1.1-3 below. OTA related test parameters are shown in table A.7.5.6.1.1.1-4 below.

PDCCHs indicating new transmissions shall be sent continuously on SCell (Cell 2) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 2 and the time duration of T2.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (SCell) on radio channel 2 (SCC).

UE is configured with 2 different UE-specific downlink bandwidth parts for SCell, BWP-1 and BWP-2, in Cell 2 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

UE is configured with 1 UE-specific downlink bandwidth parts the same as initial BWP for PSCell, BWP-0 in Cell 1 before starting the test.

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in SCell.

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in PCell.

UE is configured with a bwp-InactivityTimer timer value for SCell.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for SCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in SCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH no later than the first DL slot that occurs after the beginning of SCell’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the SCell on PCell no later than the first UL slot that occurs after the beginning of slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on SCell’s BWP-2 no later than the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).

The starting time of PCell (Cell 1) interruption due to BWP switch on SCell shall occur within the BWP switch delay.

During T2, the test equipment won’t transmit DCI format for PDSCH reception on SCell(Cell 2).

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the half subframe immediately after bwp-InactivityTimer timer expires. The UE should switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH no later than the first DL slot that occurs after the beginning of SCell’s DL slot (j+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the SCell on PCell at latest on the first UL slot that occurs after the beginning of slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on SCell’s BWP-1 no later than the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

The starting time of PCell (Cell 1) interruption due to BWP switch of SCell shall occur within the BWP switch delay.

The test equipment verifies the DL BWP switch time in SCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK/NACK is received.

The test equipment verifies that potential interruption to PCell is carried out in the correct time span by monitoring ACK/NACK sent in PCell during BWP switch of SCell, respectively.

Table A.7.5.6.1.1.1-1: DL BWP switch supported test configurations

Table A.7.5.6.1.1.1-2: General test parameters for DL BWP switch in SA

Table A.7.5.6.1.1.1-3: NR Cell specific test parameters for DL BWP switch in SA

Table A.7.5.6.1.1.1-4: OTA related test parameters for BWP switching test case

A.7.5.6.1.1.2Test Requirements

During T1, the UE shall start to send the ACK/NACK for SCell on PCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for SCell on PCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed SCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

During T1 and T3, the start time of PCell interruption during SCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PCell shall not be longer than the interruption duration specified for active BWP switch in clause 8.2.2.2.5.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch interruption to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK in the first UL slot that occurs after the beginning of DL slot (i+ TBWPswitchDelay+k1), (j+ TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK.

## A.7.5.6.1.2NR FR1- NR FR2 DL active BWP switch of SCell with non-DRX in SA

A.7.5.6.1.2.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6, and interruption requirement on other active serving cell defined in clause 8.2.2.2.5.

The supported test configurations are shown in table A.7.5.6.1.2.1-1 below. The test scenario comprises of one NR PCell (Cell 1) and one NR SCell (Cell 2). The general parameters are given in table A.7.5.6.1.2.1-2. NR Cell-specific parameters are specified in table A.7.5.6.1.2.1-3 below. OTA related test parameters are shown in table A.7.5.6.1.2.1-4 below.

PDCCHs indicating new transmissions shall be sent continuously on SCell (Cell 2) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 2 and the time duration of T2.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (SCell) on radio channel 2 (SCC).

UE is configured with 2 different UE-specific downlink bandwidth parts for SCell, BWP-1 and BWP-2, in Cell 2 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

UE is configured with 1 UE-specific downlink bandwidth parts the same as initial BWP for PCell, BWP-0 in Cell 1 before starting the test.

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in SCell.

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in PCell.

UE is configured with a bwp-InactivityTimer timer value for SCell.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for SCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in SCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH no later than the first DL slot that occurs after the beginning of SCell’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the SCell on PCell no later than the first UL slot that occurs after the begining of slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on SCell’s BWP-2 no later than the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).

The starting time of PCell (Cell 1) interruption due to BWP switch on SCell shall occur within the BWP switch delay if the UE doesn’t support per-FR gap, otherwise no interruption due to BWP switch on PCell is allowed.

During T2, the test equipment won’t transmit DCI format for PDSCH reception on SCell (Cell 2).

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the half subframe immediately after bwp-InactivityTimer timer expires. The UE should switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH no later than the first DL slot that occurs after the beginning of SCell’s DL slot (j+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the SCell on PCell at latest on the first UL slot that occurs after the beginning of slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on SCell’s BWP-1 no later than the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

The starting time of PCell (Cell 1) interruption due to BWP switch of SCell shall occur within the BWP switch delay if the UE doesn’t support per-FR gap, otherwise no interruption due to BWP switch on PCell is allowed.

The test equipment verifies the DL BWP switch time in SCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK/NACK is received.

The test equipment verifies that potential interruption to PCell is carried out in the correct time span by monitoring ACK/NACK sent in PCell during BWP switch of SCell, respectively.

Table A.7.5.6.1.2.1-1: DL BWP switch supported test configurations

Table A.7.5.6.1.2.1-2: General test parameters for DL BWP switch in SA

Table A.7.5.6.1.2.1-3: NR Cell specific test parameters for DL BWP switch in SA

Table A.7.5.6.1.2.1-4: OTA related test parameters for BWP switching test case

A.7.5.6.1.2.2Test Requirements

During T1, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

If the UE doesn’t support per-FR gap,

-During T1 and T3, the start time of SCell interruption during PCell active BWP switch shall not happen outside the BWP switch delay.

-The interruption of SCell shall not be longer than the interruption duration specified for active BWP switch in clause 8.2.2.2.5.

Otherwise no interruption due to BWP switch on SCell is allowed.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch interruption to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first UL slot that occurs after the beginning of DL slot (i+ TBWPswitchDelay+k1), (j+ TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

## A.7.5.6.1.3NR FR2 DL active BWP switch with non-DRX in SA

## A.7.5.6.1.3.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6. Supported test configurations are shown in table A.7.5.6.1.3.1-1.

The test scenario comprises of one cell (Cell 1) as given in table A.7.5.6.1.3.1-2. Cell-specific parameters of NR PCell is specified in table A.7.5.6.1.3.1-3 below. The OTA related test parameters for FR2 is shown in table A.7.5.6.1.3.1-4.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE is configured with 2 different UE-specific downlink bandwidth parts, BWP-1 and BWP-2 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1.

-UE is configured with a bwp-InactivityTimer timer value for Cell 1.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for DL BWP switch, sent from the test equipment to the UE, is received at the UE side in Cell 1’s slot # denoted i. The UE should switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the Cell 1 no later than the first UL slot that occurs after the beginning of slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on Cell 1’s BWP-2 starting from the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).

During T2, the test equipment won’t transmit DCI format for PDSCH reception on Cell 1.

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the half subframe immediately after bwp-InactivityTimer timer expires. The UE should switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH on the first DL slot that occurs after the beginning of Cell 1’s DL slot (j+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the Cell 1 at latest on the first UL slot that occurs after the beginning of slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on Cell 1’s BWP-1 starting from the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

The test equipment verifies the DL BWP switch time by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK is received.

Table A.7.5.6.1.3.1-1: DL BWP switch supported test configurations

Table A.7.5.6.1.3.1-2: General test parameters for DL BWP switch in SA

Table A.7.5.6.1.3.1-3: NR Cell specific test parameters for DL BWP switch in SA

Table A.7.5.6.1.3.1-4: OTA related test parameters for DL BWP switch in SA

## A.7.5.6.1.3.2Test Requirements

During T1, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for PCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK/NACK in the first UL slot that occurs after the beginning of DL slot (i+ TBWPswitchDelay+k1), (j+ TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK/NACK.

## A.7.5.6.1.4NR FR2-2- NR FR2-2 DL active BWP switch of SCell with non-DRX in SA

## A.7.5.6.1.4.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement defined in clause 8.6, and interruption requirement on other active serving cell defined in clause 8.2.2.2.5.

The supported test configurations are shown in table A.7.5.6.1.4.1-1 below. The test scenario comprises of one PCell (Cell 1) and one SCell (Cell 2) as given in table A.7.5.6.1.4.1-2. NR Cell-specific parameters are specified in table A.7.5.6.1.4.1-3 below. OTA related test parameters are shown in table A.7.5.6.1.4.1-4 below.

PDCCHs indicating new transmissions shall be sent continuously on SCell (Cell 2) to ensure that the UE would have ACK/NACK sending except for the time duration when BWP is switching on Cell 2 and the time duration of T2.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), and Cell 2 (SCell) on radio channel 2 (SCC).

UE is configured with 2 different UE-specific downlink bandwidth parts for SCell, BWP-1 and BWP-2, in Cell 2 before starting the test. BWP-1 and BWP-2 always include bandwidth of the initial DL BWP and SSB.

UE is configured with 1 UE-specific downlink bandwidth parts the same as initial BWP for PSCell, BWP-0 in Cell 1 before starting the test.

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in SCell.

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in PCell.

UE is configured with a bwp-InactivityTimer timer value for SCell.

All cells have constant signal levels throughout the test.

The test consists of 3 successive time periods, with durations of T1, T2, and T3, respectively.

During T1,

Time period T1 starts when a DCI format 1_1 command for SCell DL BWP switch, sent from the test equipment to the UE, is received at the UE side in SCell’s slot # denoted i. The UE shall switch its bandwidth part from BWP-1 to BWP-2.

The UE shall be able to receive PDSCH no later than the first DL slot that occurs after the beginning of SCell’s DL slot (i+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the SCell on PCell no later than the first UL slot that occurs after the beginning of slot (i+TBWPswitchDelay+k1). The UE shall be continuously scheduled on SCell’s BWP-2 no later than the first DL slot that occurs after the beginning of slot (i+TBWPswitchDelay).

The starting time of PCell (Cell 1) interruption due to BWP switch on SCell shall occur within the BWP switch delay.

During T2, the test equipment won’t transmit DCI format for PDSCH reception on SCell(Cell 2).

During T3,

The time period T3 starts from the slot #j, where j is the first slot of the half subframe immediately after bwp-InactivityTimer timer expires. The UE should switch its bandwidth part from BWP-2 back to the default bandwidth part – BWP-1.

The UE shall be able to receive PDSCH no later than the first DL slot that occurs after the beginning of SCell’s DL slot (j+TBWPswitchDelay) as defined in clause 8.6 and starts to report valid ACK/NACK for the SCell on PCell at latest on the first UL slot that occurs after the beginning of slot (j+TBWPswitchDelay+k1). The UE shall be continuously scheduled on SCell’s BWP-1 no later than the first DL slot that occurs after the beginning of slot (j+TBWPswitchDelay).

The starting time of PCell (Cell 1) interruption due to BWP switch of SCell shall occur within the BWP switch delay.

The test equipment verifies the DL BWP switch time in SCell by counting the slots from the time when the BWP switch command is received or bwp-InactivityTimer timer expires till an ACK/NACK is received.

The test equipment verifies that potential interruption to PCell is carried out in the correct time span by monitoring ACK/NACK sent in PCell during BWP switch of SCell, respectively.

Table A.7.5.6.1.4.1-1: DL BWP switch supported test configurations

Table A.7.5.6.1.4.1-2: General test parameters for DL BWP switch in SA

Table A.7.5.6.1.4.1-3: NR Cell specific test parameters for DL BWP switch in SA

Table A.7.5.6.1.4.1-4: OTA related test parameters for BWP switching test case

## A.7.5.6.1.4.2Test Requirements

During T1, the UE shall start to send the ACK/NACK for SCell on PCell from the first UL slot that occurs after the beginning of DL slot (i+TBWPswitchDelay+k1).

During T3, the UE shall start to send the ACK/NACK for SCell on PCell from the first UL slot that occurs after the beginning of DL slot (j+TBWPswitchDelay+k1).

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

Depending on UE capability bwp-SwitchingDelay [2], UE shall finish BWP switch within the time duration TBWPswitchDelay defined in table 8.6.2-1.

All of the above test requirements shall be fulfilled in order for the observed SCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

During T1 and T3, the start time of PCell interruption during SCell active BWP switch shall not happen outside the BWP switch delay.

The interruption of PCell shall not be longer than the interruption duration specified for active BWP switch in clause 8.2.2.2.5.

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch interruption to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

NOTE:During T1, T3 if there are no uplink resources for reporting the ACK in the first UL slot that occurs after the beginning of DL slot (i+ TBWPswitchDelay+k1), (j+ TBWPswitchDelay+k1), then the UE shall use the next available uplink resource for reporting the corresponding ACK.

## A.7.5.6.2RRC-based Active BWP Switch

A.7.5.6.2.1NR FR2 DL active BWP switch of PCell with non-DRX in SA

## A.7.5.6.2.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6.3. Supported test configurations are shown in table A.7.5.6.2.1.1-1.

The test scenario comprises of one PCell (Cell 1) as given in table A.7.5.6.2.1.1-2. Cell-specific parameters of PCell are specified in table A.7.5.6.2.1.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1 (PCell).

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PCell.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition.

The UE shall be able to completely receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot  as defined in clause 8.6.3 and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot. The UE shall be continuously scheduled on PCell’s BWP-1 starting from the first DL slot that occurs after the beginning of DL slot .i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length

TRRCprocessingDelay and TBWPswitchDelayRRC are defined in clause 8.6.3.

The test equipment verifies the DL BWP switch time in PCell by counting the time from the time when the RRC Reconfiguration message including updated BWP configurationis sent till the time when RRC Reconfiguration Complete message is received.

Table A.7.5.6.2.1.1-1: DL BWP switch supported test configurations

Table A.7.5.6.2.1.1-2: General test parameters for DL BWP switch in SA

Table A.7.5.6.2.1.1-3: NR Cell specific test parameters for DL BWP switch in SA

Table A.7.5.6.2.1.1-4: OTA related test parameters for BWP switching test case

## A.7.5.6.2.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PCell from the first DL slot that occurs after the beginning of slot  and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot.i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.6.2.2NR FR2-2 DL active BWP switch of PCell with non-DRX in SA

## A.7.5.6.2.2.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for RRC-based BWP switch defined in clause 8.6.3. Supported test configurations are shown in table A.7.5.6.2.2.1-1.

The test scenario comprises of one PCell (Cell 1) as given in table A.7.5.6.2.2.1-2. Cell-specific parameters of PCell are specified in table A.7.5.6.2.2.1-3 below.

PDCCHs indicating new transmissions shall be sent continuously on PCell (Cell 1) to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1 (PCell).

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition in PCell.

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration, sent from the test equipment to the UE, is received at the UE side in PSCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition.

The UE shall be able to completely receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot  as defined in clause 8.6.3 and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot. The UE shall be continuously scheduled on PSCell’s BWP-1 starting from the first DL slot that occurs after the beginning of DL slot .i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length

TRRCprocessingDelay and TBWPswitchDelayRRC are defined in clause 8.6.3.

The test equipment verifies the DL BWP switch time in PSCell by counting the time from the time when the RRC Reconfiguration message including updated BWP configurationis sent till the time when RRC Reconfiguration Complete message is received.

Table A.7.5.6.2.2.1-1: DL BWP switch supported test configurations

Table A.7.5.6.2.2.1-2: General test parameters for DL BWP switch in SA

Table A.7.5.6.2.2.1-3: NR Cell specific test parameters for DL BWP switch in SA

Table A.7.5.6.2.2.1-4: OTA related test parameters for BWP switching test case

## A.7.5.6.2.2.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PCell from the first DL slot that occurs after the beginning of slot  and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot.i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length i+TRRCprocessingDelay+TBWPswitchDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed PCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.6.3Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs

A.7.5.6.3.1Active BWP switch on multiple SCells with non-DRX in SA

## A.7.5.6.3.1.1Test Purpose and Environment

The purpose of this test is to verify fulfillment of DL BWP switch delay requirement defined in clauses 8.6.2A.1 and 8.6.2B.1, and interruption requirement on other active serving cell defined in clause 8.2.2.2.5.

The supported test configurations are shown in table A.7.5.6.3.1.1-1 below. The test scenario comprises one PCell (Cell 1) and two SCells (Cell 2 and Cell 3) as given in table A.7.5.6.3.1.1-2. NR cell-specific parameters are provided in table A.7.5.6.3.1.1-3, and OTA related test parameters in table A.7.5.6.3.1.1-4 below.

The test consists of three consecutive time periods with durations T1, T2 and T3, respectively.

PDCCHs indicating new transmissions shall be transmitted in PCell, SCell 1 and SCell 2 throughout time periods T1 and T3 to ensure that UE sends ACK/NACKs for PDSCH reception in PCell, SCell 1 and SCell 2. During T2, there shall be scheduling on PDSCH in PCell only.

Before the test starts,

UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), Cell 2 (SCell 1) on radio channel 2 (SCC1), and Cell 3 (SCell 2) on radio channel 3 (SCC2).

UE is configured with a single UE-specific downlink bandwidth part, BWP-0, for Cell 1 (PCell). BWP-0 includes the bandwidth of the initial DL BWP and SSB.

UE is configured with two different UE-specific downlink bandwidth parts, BWP-1 and BWP-2, for Cell 2 (SCell 1). BWP-1 and BWP-2 include the bandwidth of the initial DL BWP and SSB.

UE is configured with two different UE-specific downlink bandwidth parts, BWP-3 and BWP-4, for Cell 3 (SCell 2). BWP-3 and BWP-4 include the bandwidth of the initial DL BWP and SSB.

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-0 in PCell.

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 in SCell 1.

UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-3 in SCell 2.

UE is configured with a bwp-InactivityTimer timer value for SCell 1 and SCell 2, respectively.

All cells have constant signal levels throughout the test.

Time period T1 starts when the UE simultaneously receives DCI format 1_1 commands for DL BWP switch in SCell 1 and SCell 2, respectively, in a slot # denoted m. The UE shall switch its SCell 1 bandwidth part from BWP-1 to BWP-2, and its SCell 2 bandwidth part from BWP-3 to BWP-4. The UE shall be able to receive PDSCH in SCell 1 and SCell 2 starting from the first DL slot that occurs after slot (m+TMultipleBWPswitchDelay) as defined in clause 8.6.2A.1, and to transmit ACK/NACKs in SCell 1 and SCell 2 from the first UL slot that occurs after (m+TBWPswitchDelay+k1) where k1 is specified in [7]. The UE shall be continuously scheduled in SCell 1 BWP-2 and SCell 2 BWP-4 no later than in the first DL slot that occurs after slot (m+TMultipleBWPswitchDelay). The starting time of any interruption on PCell due to DL BWP switching of SCell 1 and SCell 2 shall occur within the BWP switching delay. The length of any interruption on PCell due to DL BWP switching of SCell 1 and SCell 2 shall fulfill requirements in clause 8.2.2.2.5.

Time period T2 starts when the test equipment ceases to schedule the UE on PDSCH in SCell 1 and SCell 2, thereby causing the bwp-InactivityTimer timers for SCell 1 and SCell 2 to be running until expiry.

Time period T3 starts at the beginning of the first DL half-subframe immediately after the earliest of the bwp-InactivityTimer timers expires, in a slot # denoted n. The UE shall switch its SCell 1 bandwidth part from BWP-2 to BWP-1, and its SCell 2 bandwidth part from BWP-4 to BWP-3. The UE shall be able to receive PDSCH in SCell 1 and SCell 2 starting from the first DL slot that occurs after slot (n+TMultipleBWPswitchDelay) as defined in clause 8.6.2B.1, and to transmit ACK/NACKs in SCell 1 and SCell 2 from the first UL slot that occurs after slot (n+TMultipleBWPswitchDelay+k1). The UE shall be continuously scheduled in SCell 1 BWP-1 and SCell 2 BWP-3 no later than in the first DL slot that occurs after slot (n+TMultipleBWPswitchDelay). The starting time of any interruption on PCell due to DL BWP switching of SCell 1 and SCell 2 shall occur within the BWP switching delay. The length of any interruption on PCell due to DL BWP switching of SCell 1 and SCell 2 shall fulfill requirements in clause 8.2.2.2.5.

The test equipment verifies the DL BWP switch time by counting the slots from the time when the BWP switch commands are received or bwp-InactivityTimer timers expire until ACK/NACKs are sent in SCell 1 and SCell 2, respectively.

The test equipment verifies that potential interruptions of PCell due to DL BWP switching on SCell 1 and SCell 2 are carried out within the correct time span, and are within the correct length, by monitoring ACK/NACKs sent in PCell for PCell.

Table A.7.5.6.3.1.1-1: DL BWP switch supported test configurations

Table A.7.5.6.3.1.1-2: General test parameters for DL BWP switch in SA

Table A.7.5.6.3.1.1-3: NR Cell specific test parameters for DL BWP switch in SA

Table A.7.5.6.3.1.1-4: OTA related test parameters for BWP switching test case

## A.7.5.6.3.1.2Test Requirements

During T1, the UE shall start to send ACK/NACKs in SCell 1 and SCell 2 from the first UL slot that occurs after the beginning of DL slot (m+TMultipleBWPswitchDelay+k1).

During T3, the UE shall start to send ACK/NACKs in SCell 1 and SCell 2 from the first UL slot that occurs after the beginning of DL slot (n+TMultipleBWPswitchDelay+k1).

During T1 and T3, the start of any interruption on PCell due to active BWP switching on SCell 1 and SCell 2 shall not happen outside the BWP switching delay TMultipleBWPswitchDelay, and the length of any interruption shall not exceed the length specified in clause 8.2.2.2.5.

All of the above test requirements shall be fulfilled in order for the observed active BWP switch delays in SCell 1 and SCell 2 to be considered correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.6.4SCell dormancy switch

## A.7.5.6.4.1NR FR2 PCell SCell dormancy switch of single FR2 SCell inside active time

## A.7.5.6.4.1.1Test Purpose and Environment

The purpose of this test is to verify that the Dormant SCell BWP switch delay requirements are within the requirements stated in clause 8.6 for UE configured with a single downlink SCell, when the dormancy indication is received in any of the first 3 OFDM symbols or is received after the first 3 OFDM symbols.

The Supported test configurations are given in table A.7.5.6.4.1.1-1. The test parameters are given in Tables A.7.5.6.4.1.1-2 and cell-specific parameters in A.7.5.6.4.1.1-3 below. In the measurement control information, a measurement object is configured for the frequency of the PCell, and it is indicated to the UE that event-triggered reporting with Event A6 is used The test consists of four successive time periods, with duration of T1, T2, T3 and T4, respectively. There are two carriers both in FR2, with one cell on the PCC and 2 cells on SCC. Cell 1, Cell 2 and Cell 3 operate in either FDD or TDD duplex mode according to test configuration. All cells have constant signal levels throughout the test. Before the test starts the UE is connected to Cell 1 (PCell) on radio channel 1 (PCC) with configured and activated SCell (SCell 1) on radio channel 2 (SCC1). The UE is not aware of Cell 3 on radio channel 2 (SCC1). The UE is reporting CSI and shall not report CQI index 0 (out-of-range) in the available uplink resources to report CQI for the SCell. The UE shall be continuously scheduled in the PCell throughout the whole test.

The UE receives a DCI-based BWP switch command by which the SCell 1 (Cell 2) is requested to switch the active BWP to the dormant BWP.

The point in time at which the DCI message is received at the UE antenna connector, in a subframe # denoted n, defines the start of time period T1. The UE shall accomplish the BWP switch to the dormant BWP latest in subframe (n + TBWPswitchDelay + X). The UE shall continue to shall report valid CQI if the UE has available uplink resources to report CQI for the dormant SCell. The UE shall continue to shall report L1-RSRP if the UE has available uplink resources to report L1-RSRP for the Dormant SCell. Any PCell interruption due to BWP switch on the SCell shall occur in the subframes n to (n+ TBWPswitchDelay + X).

Time T2 start at T1 + (TBWPswitchDelay + X). During T2 the UE shall continue to measure and report CQI and L1-RSRP in the available uplink resources to report CQI and L1-RSRP for the SCell.

Time T3 starts at T2 + 500 ms. During T3 the UE shall continue to measure and report CQI and L1-RSRP in the available uplink resources to report CQI and L1-RSRP for the SCell.

Starting at T4 = T3 + 500 ms, Cell 3 becomes detectable. During T3 the UE shall continue to measure and report CQI and L1-RSRP in the available uplink resources to report CQI and L1-RSRP for the SCell. The UE shall send one Event A6 triggered measurement report, with a measurement reporting delay less than 1000 ms from the beginning of time period T4. The UE is not required to read the neighbour cell SSB index in this test.

At time T5 starting at T4 + 1500 ms a a DCI-based BWP switch command by which the SCell 1 (Cell 2) is requested to switch the active BWP to the non-dormant BWP.

The point in time at which the DCI message is received at the UE antenna connector, in a subframe # denoted n, defines the start of time period T6. The UE shall accomplish the BWP switch to the non-dormant BWP latest in subframe (n + TBWPswitchDelay + X). The UE shall continue to shall report valid CQI if the UE has available uplink resources to report CQI for the non-dormant SCell. The UE shall continue to shall report L1-RSRP if the UE has available uplink resources to report L1-RSRP for the non-dormant SCell. Any PCell interruption due to BWP switch on the SCell shall occur in the subframes n to (n+ TBWPswitchDelay + X).

During T2, T3 and T4 the total rate of ACK/NACK feedback loss on any non-dormant serving cell resulting from CQI measurements and RRM measurements, clause 8.2.2.2.12.3, on dormant SCells, shall not exceed [0.5]%.

During T2, T3 and T4 the total rate of ACK/NACK feedback loss on any non-dormant serving cell resulting from L1-RSRP measurements and RRM measurements, clause 8.2.2.2.12.3, on dormant SCells, shall not exceed [0.5]%.

During T2, T3 and T4 the total rate of ACK/NACK feedback loss on any non-dormant serving cell resulting from RRM measurements and RRM measurements, clause 8.2.2.2.12.3, on dormant SCells, shall not exceed [0.5]%

During T1, T2, T3, T4, T5 and T6, the UE shall be continuously scheduled in the SCell 1.

Table A.7.5.6.4.1.1-1: Supported test configurations

Table A.7.5.6.4.1.1-2: General test parameters for dormancy SCell in NR SA with PCell and SCell in FR2

Table A.7.5.6.4.1.1-3: NR Cell specific test parameters for dormancy SCell in NR SA with PCell and SCell in FR2

## A.7.5.6.4.1.2Test Requirements

During T1 the UE shall switch to the dormant BWP.

During T2, T3, T4 and T5 the UE shall not send ACK/NACK for the PDSCH data scheduled on the SCell.

During T2, T3, T4 and T5 the UE shall continue to send CSI reports for SCell 1 with non-zero CQI index.

During T2, T3, T4 and T5 the UE shall continue to send L1-RSRP reports for SCell.

During T4 the UE shall send one Event A6 triggered measurement report, with a measurement reporting delay less than 1000 ms from the beginning of time period T4.

During T2, T3, T4 and T5, the missing ACK/NACK sent in PCell shall be less than 1.5 % of the total number of the expected ACK/NACK.

During T6, the UE shall send ACK/NACK for the PDSCH data scheduled after subframe (n+ TBWPswitchDelay + X) for the SCell 1.

All of the above test requirements shall be fulfilled in order for the observed SCell 1 BWP switch delays, PCell interruption rate, correct CSI and L1-RSRP reporting and event triggeres reporting. The rate of correct observed SCell 1 hibernation delay, activation delay and SCell 1 deactivation delay during repeated tests shall be at least 90 %.

## A.7.5.6.4.2NR FR1 PCell SCell dormancy switch of two FR2 SCells outside active time

## A.7.5.6.4.2.1Test Purpose and Environment

The purpose of this test is to verify fulfillment of SCell dormancy switching delay requirements in clause 8.6.2A when the UE is triggered to switch between non-dormancy and dormancy outside DRX active time. In the tested scenario, the UE is connected to PCell in FR1and two SCells in FR2, and the SCells are switched from non-dormancy to dormancy, and vice versa, at a point in time before start of onDuration. The UE is configured to monitor PDCCH for DCI format 2_6 at ps-Offset before the start of onDuration. Two tests are specified, where a UE that only supports triggering within the first three OFDM symbols of a slot shall undergo Test1 only, and a UE that supports triggering also in remaining OFDM symbols of a slot shall undergo both Test1 and Test2. In the tested scenario, ps-Offset is selected to correspond to the dormancy switching time specified in clause 8.6.2A.

The supported test configurations are provided in table A.7.5.6.4.2.1-1 below. General test parameters are provided in table A.7.5.6.4.2.1-2, and cell-specific parameters are provided in table A.7.5.6.4.2.1-3 below. OTA-related test parameters are provided in table A.7.5.6.4.2.1-4.

The tests consist of four consecutive time periods, T1, T2, T3 and T4, respectively.

Three carriers are used in the test. Cell 1 (PCell) is on RF channel 1 (PCC) in FR1, and Cell 2 (SCell 1) and Cell 3 (SCell 2) are on RF channels 2 (SCC1) and 3 (SCC2) in FR2, respectively. All three cells have constant signal levels throughout the test.

Before the test starts,

-UE is connected to Cell 1 (PCell), Cell 2 (SCell 1) and Cell 3 (SCell 2).

-UE is configured with a single UE-specific downlink bandwidth part, BWP-0, for Cell 1. BWP-0 includes the bandwidth of the initial DL BWP and SSB.

-UE is configured with one non-dormant and one dormant UE-specific downlink bandwidth part, BWP-0 and BWP-1, respectively, for Cell 2 and Cell 3. BWP-0 includes the bandwidth of the initial DL BWP and SSB.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP in Cell 1 is BWP-0.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP in Cell 2 is BWP-0.

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP in Cell 3 is BWP-0.

-UE is configured with DRX.

-UE is configured to monitor DCI format 2_6, and to be active during onDuration even when no DCI format 2_6 is detected (ps-WakeUp).

Time period T1 starts when the UE at ps-Offset before onDuration detects a DCI format 2_6 carrying dormancy indication that indicates that SCell 1 and SCell 2 are to be switched from non-dormancy to dormancy. The UE shall switch active bandwidth parts for SCell 1 and SCell 2, respectively, from non-dormant BWP-0 to dormant BWP-1. The UE shall complete the switching before the start of onDuration. The test equipment schedules the UE continuously with new data indications in PCell starting from beginning of onDuration. The test equipment verifies that the UE is transmitting HARQ feedback for PCell from the beginning of onDuration and thus verifies that the UE has completed interruptions due to dormancy switching before the start of onDuration.

Time period T2 starts when T1 is completed. The test equipment continues to schedule the UE continuously in PCell. The UE shall carry out CSI and RRM measurements on the dormant SCells. The UE shall report ACK/NACK in PCell in response to scheduled PDSCH, with the maximum loss of transmitted ACK/NACKs fulfilling the requirement in clause 8.2.2.2.12. The test equipment verifies that the loss of ACK/NACKs is no larger than 1.5 %.

Time period T3 starts when T2 is completed. During T3, the test equipment does not schedule the UE, by which the inactivity timer expires and the UE stops monitoring PDCCH except for signalling using DCI format 2_6 at wake-up signalling occasions.

Time period T4 starts when the UE at ps-Offset before onDuration detects a DCI format 2_6 carrying dormancy indication that indicates that SCell 1 and SCell 2 are to be switched from dormancy to non-dormancy. The UE shall switch active bandwidth parts for SCell 1 and SCell 2, respectively, from dormant BWP-1 to non-dormant BWP-0. The UE shall complete the switching before the start of onDuration. The test equipment schedules the UE with new data indication in PCell, SCell 1 and SCell 2 during onDuration. The UE shall receive in PCell, SCell 1 and SCell 2 and send HARQ feedback for PCell, SCell 1 and SCell 2 via PCell. The test equipment verifies that the UE is transmitting HARQ feedback for PCell, SCell 1 and SCell 2 from the beginning of onDuration, and thus verifies that the UE has completed interruptions due to dormancy switching before the start of onDuration.

Table A.7.5.6.4.2.1-1: Supported test configurations

Table A.7.5.6.4.2.1-2: General test parameters

Table A.7.5.6.4.2.1-3: Cell specific test parameters

Table A.7.5.6.4.2.1: OTA related test parameters

## A.7.5.6.4.2.2Test Requirements

Starting from onDuration in time period T1, the UE shall transmit ACK/NACK in response to scheduling in PCell. There shall be no loss of ACK/NACK.

During time period T2, the UE shall transmit ACK/NACKs in response to scheduling in PCell and the rate of missed ACK/NACKs shall be no more than 1.5 %.

Starting from onDuration in time period T4, the UE shall transmit ACK/NACK in response to scheduling in PCell, SCell 1 and SCell 2. There shall be no loss of ACK/NACK.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.6.5Simultaneous RRC-based Active BWP Switch on multiple CCs

## A.7.5.6.5.1Active BWP switch on multiple SCells with non-DRX in SA

A.7.5.6.5.1.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for simultaneous RRC-based BWP switch on multiple CCs defined in clause 8.6.3A.

The supported test configurations are shown in table A.7.5.6.5.1.1-1. The test scenario comprises one PCell (Cell 1) and one SCell (Cell 2) as given in table A.7.5.6.5.1.1-2. NR cell-specific parameters are provided in table A.7.5.6.5.1.1-3, and OTA related test parameters in table A.7.5.6.5.1.1-4.

PDCCHs indicating new transmissions shall be transmitted in PCell and SCell throughout to ensure that UE sends ACK/NACKs for PDSCH reception in PCell, SCell.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), to Cell 2 (SCell) on radio channel 2 (SCC).

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1 (PCell), Cell 2 (SCell).

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition on Cell 1 (PCell), Cell 2 (SCell).

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration in Cell 1 and Cell 2, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition in Cell 1 and Cell 2.

The UE shall be able to receive PDSCH on Cell 1 and Cell 2 at the beginning of the DL slot right after PCell’s DL slot (i+) as defined in clause 8.6.3A and be ready for the reception of uplink grant for the PCell no later than at the beginning of the DL slot right after slot (i+). The UE shall be continuously scheduled on Cell 1’s BWP-1and Cell 2’s BWP-1 starting from the beginning of the DL slot right after slot (i+).TRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot lengthTRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot lengthTRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot length

TRRCprocessingDelay , TBWPswitchDelayRRC and DRRC are defined in clause 8.6.3A.

The test equipment verifies the DL BWP switch time in Cell 1 and Cell 2 by counting the time from the time when the RRC Reconfiguration message including updated BWP configuration is sent till the time when RRC Reconfiguration Complete message is received.

Table A.7.5.6.5.1.1-1: DL BWP switch supported test configurations

Table A.7.5.6.5.1.1-2: General test parameters for DL BWP switch in SA

Table A.7.5.6.5.1.1-3: NR Cell specific test parameters for DL BWP switch in SA

Table A.7.5.6.5.1.1-4: OTA related test parameters for BWP switching test case

A.7.5.6.5.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PCell and SCell in the beginning of the DL slot right after slot (i+).TRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot length

All of the above test requirements shall be fulfilled in order for the observed PCell and SCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.6.5.2NR FR2-2 Active BWP switch on multiple SCells with non-DRX in SA

## A.7.5.6.5.2.1Test Purpose and Environment

The purpose of this test is to verify the DL BWP switch delay requirement for simultaneous RRC-based BWP switch on multiple CCs defined in clause 8.6.3A.

The supported test configurations are shown in table A.7.5.6.5.2.1-1. The test scenario comprises one PCell (Cell 1) and one SCell (Cell 2) as given in table A.7.5.6.5.2.1-2. NR cell-specific parameters are provided in table A.7.5.6.5.2.1-3, and OTA related test parameters in table A.7.5.6.5.2.1-4.

PDCCHs indicating new transmissions shall be transmitted in PCell and SCell throughout to ensure that UE sends ACK/NACKs for PDSCH reception in PCell, SCell.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC), to Cell 2 (SCell) on radio channel 2 (SCC).

-UE has bandwidth part BWP-1 in its RRC-configuration for Cell 1 (PCell), Cell 2 (SCell).

-UE is indicated in firstActiveDownlinkBWP-Id that the active DL BWP is BWP-1 of initial condition on Cell 1 (PCell), Cell 2 (SCell).

All cells have constant signal levels throughout the test.

The test consists of 1 time period, with duration of T1.

During T1,

Time period T1 starts when a RRCReconfiguration with updated bandwidth part configuration in Cell 1 and Cell 2, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its bandwidth part with the updated bandwidth part BWP-1 of final condition in Cell 1 and Cell 2.

The UE shall be able to receive PDSCH on Cell 1 and Cell 2 at the beginning of the DL slot right after PCell’s DL slot (i+) as defined in clause 8.6.3A and be ready for the reception of uplink grant for the PCell no later than at the beginning of the DL slot right after slot (i+). The UE shall be continuously scheduled on Cell 1’s BWP-1and Cell 2’s BWP-1 starting from the beginning of the DL slot right after slot (i+).TRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot lengthTRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot lengthTRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot length

TRRCprocessingDelay , TBWPswitchDelayRRC and DRRC are defined in clause 8.6.3A.

The test equipment verifies the DL BWP switch time in Cell 1 and Cell 2 by counting the time from the time when the RRC Reconfiguration message including updated BWP configuration is sent till the time when RRC Reconfiguration Complete message is received.

Table A.7.5.6.5.2.1-1: DL BWP switch supported test configurations

Table A.7.5.6.5.2.1-2: General test parameters for DL BWP switch in SA

Table A.7.5.6.5.2.1-3: NR Cell specific test parameters for DL BWP switch in SA

Table A.7.5.6.5.2.1-4: OTA related test parameters for BWP switching test case

## A.7.5.6.5.2.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PCell and SCell in the beginning of the DL slot right after slot (i+).TRRCprocessingDelay+TBWPswitchDelayRRC+DRRCNR slot length

All of the above test requirements shall be fulfilled in order for the observed PCell and SCell active BWP switch delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.7PSCell addition and release delay

## A.7.5.7.1Addition and Release Delay of known NR PSCell

## A.7.5.7.1.1Test Purpose and Environment

The purpose of this test is to verify the PSCell addition and release delay requirements defined in clauses 8.9.2 and 8.9.3, respectively, for the case where the PSCell is known to the UE at the time of addition.

The supported test configurations are given in table A.7.5.7.1.1-1. The test scenario comprises two NR cells, Cell 1 and Cell 2, on radio channel 1 in FR1 and radio channel 2 in FR2, respectively. Test parameters are given in Tables A.7.5.7.1.1-2, A.7.5.7.1.1-3 and A.7.5.7.1.1-4 below. The test consists of six time periods with durations T1, T2, T3, T4, T5 and T6, respectively.

At the start of T1, the UE shall be connected to Cell 1 (PCell) on radio channel 1 (PCC) and shall only monitor PCC and hence be unaware of Cell 2 (PSCell-to-be) on radio channel 2. Before the start of T2, the test system shall send measurement control information including measurement gap configuration and event-triggered reporting configuration for measurements on radio channel 2.

During T2, the Cell 2 becomes known to the UE. Therefore, during T2 the UE shall report Event triggered report.

The point in time at which the RRC message to release measurement gap is transmitted from the test system defines the start of period T3. During T3, after measurement gap is released, the test system transmits the RRC message to the UE to add PSCell on radio channel 2. The RRC message (to add PSCell) also includes a request for the UE to start periodic CSI reporting for the PSCell after the PSCell has been successfully added.

The point in time at which the RRC message to add PSCell (Cell 2) is received at the UE antenna connector defines the start of period T4.

During T4, the UE shall carry out random access towards the PSCell. Reception by the test system of the PRACH preamble defines the start of T5.

During T5, the UE shall send periodic CSI reports in PSCell. After having received at least one such report, the test system shall send a RRC message instructing the UE to release the PSCell. Reception by the UE of the RRC message defines the start of T6.

During T6, the UE shall release the PSCell.

Table A.7.5.7.1.1-1: Supported test configurations for FR2 PSCell

Table A.7.5.7.1.1-2: General test parameters for PSCell addition and release delay

Table A.7.5.7.1.1-3: NR Cell specific test parameters for PSCell addition and release delay

Table A.7.5.7.1.1-4: OTA related test parameters for PSCell addition and release delay

## A.7.5.7.1.2Test Requirements

The UE shall transmit the PRACH preamble to PSCell at latest 112 ms into T4.

The UE shall transmit at least one periodic CSI report for PSCell during T5.

The UE shall stop transmitting CSI reports for PSCell at latest 20 ms into T6.

All of the above test requirements shall be fulfilled in order for the observed PSCell addition and release delay to be counted as correct. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.7.2Addition and Release Delay of unknown NR PSCell in

## A.7.5.7.2.1Test Purpose and Environment

The purpose of this test is to verify the PSCell addition and release delay requirements defined in clauses 8.9.2 and 8.9.3, respectively, for the case where the PSCell is unknown to the UE at the time of addition.

The supported test configurations are given in table A.7.5.7.2.1-1. The test scenario comprises two NR cells, Cell 1 and Cell 2, on radio channel 1 in FR1 and radio channel 2 in FR2, respectively. Test parameters are given in Tables A.7.5.7.2.1-2, A.7.5.7.2.1-3 and A.7.5.7.2.1-4 below. The test consists of four time periods with durations T1, T2, T3 and T4, respectively.

At the start of T1, the UE shall be connected to Cell 1 (PCell) on radio channel 1 (PCC) and shall only monitor PCC and hence be unaware of Cell 2 (PSCell-to-be) on radio channel 2. At the end of T1, the test system shall send a RRC message instructing the UE to add PSCell (Cell 2), and further instructing the UE to report CSI periodically in the PSCell once it has been added. Reception by the UE of this RRC message defines the start of T2.

During T2, the UE shall identify PSCell and carry out random access towards the PSCell. Reception by the test system of the PRACH preamble defines the start of T3.

During T3, the UE shall send periodic CSI reports in PSCell. After having received at least one such report, the test system shall send a RRC message instructing the UE to release the PSCell. Reception by the UE of the RRC message defines the start of T4.

During T4, the UE shall release the PSCell.

Table A.7.5.7.2.1-1: Supported test configurations for FR2 PSCell

Table A.7.5.7.2.1-2: General test parameters for PSCell addition and release delay

Table A.7.5.7.2.1-3: NR Cell specific test parameters for PSCell addition and release delay

Table A.7.5.7.2.1-4: OTA related test parameters for PSCell addition and release delay

## A.7.5.7.2.2Test Requirements

The UE shall transmit the PRACH preamble to PSCell at latest 572 ms into T2.

The UE shall transmit at least one periodic CSI report for PSCell during T3.

The UE shall stop transmitting CSI reports for PSCell at latest 20 ms into T4.

All of the above test requirements shall be fulfilled in order for the observed PSCell addition and release delay to be counted as correct. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.7.3Addition and Release Delay of known NR PSCell in FR2-2

## A.7.5.7.3.1Test Purpose and Environment

The purpose of this test is to verify the PSCell addition and release delay requirements defined in clauses 8.9.2 and 8.9.3, respectively, for the case where the PSCell is known to the UE at the time of addition.

The supported test configurations are given in table A.7.5.7.3.1-1. The test scenario comprises two NR cells, Cell 1 and Cell 2, on radio channel 1 in FR1 and radio channel 2 in FR2-2, respectively. Test parameters are given in Tables A.7.5.7.3.1-2, A.7.5.7.3.1-3 and A.7.5.7.3.1-4 below. The test consists of five time periods with durations T1, T2, T3, T4 and T5, respectively.

At the start of T1, the UE shall be connected to Cell 1 (PCell) on radio channel 1 (PCC) and shall only monitor PCC and hence be unaware of Cell 2 (PSCell-to-be) on radio channel 2. Before the start of T2, the test system shall send measurement control information including measurement gap configuration and event-triggered reporting configuration for measurements on radio channel 2.

During T2, the Cell 2 becomes known to the UE. Therefore, during T2 the UE shall report Event triggered report.

The point in time at which the RRC message to release measurement gap is transmitted from the test system defines the start of period T3. During T3, after measurement gap is released, the test system transmits the RRC message to the UE to add PSCell on radio channel 2. The RRC message (to add PSCell) also includes a request for the UE to start periodic CSI reporting for the PSCell after the PSCell has been successfully added.

The point in time at which the RRC message to add PSCell (Cell 2) is received at the UE antenna connector defines the start of period T4.

During T4, the UE shall carry out random access towards the PSCell. Reception by the test system of the PRACH preamble defines the start of T4.

During T5, the UE shall send periodic CSI reports in PSCell. After having received at least one such report, the test system shall send a RRC message instructing the UE to release the PSCell. Reception by the UE of the RRC message defines the start of T6

During T6, the UE shall release the PSCell.

Table A.7.5.7.3.1-1: Supported test configurations for FR2-2 PSCell

Table A.7.5.7.3.1-2: General test parameters for PSCell addition and release delay

Table A.7.5.7.3.1-3: NR Cell specific test parameters for PSCell addition and release delay

Table A.7.5.7.3.1-4: OTA related test parameters for PSCell addition and release delay

## A.7.5.7.3.2Test Requirements

The UE shall transmit the PRACH preamble to PSCell at latest TBD ms into T3.

The UE shall transmit at least one periodic CSI report for PSCell during T4.

The UE shall stop transmitting CSI reports for PSCell at latest 20 ms into T5.

All of the above test requirements shall be fulfilled in order for the observed PSCell addition and release delay to be counted as correct. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.7.4Addition and Release Delay of unknown NR PSCell in FR2-2

## A.7.5.7.4.1Test Purpose and Environment

The purpose of this test is to verify the PSCell addition and release delay requirements defined in clauses 8.9.2 and 8.9.3, respectively, for the case where the PSCell is unknown to the UE at the time of addition.

The supported test configurations are given in table A.7.5.7.4.1-1. The test scenario comprises two NR cells, Cell 1 and Cell 2, on radio channel 1 in FR1 and radio channel 2 in FR2-2, respectively. Test parameters are given in Tables A.7.5.7.4.1-2, A.7.5.7.4.1-3 and A.7.5.7.4.1-4 below. The test consists of four time periods with durations T1, T2, T3 and T4, respectively.

At the start of T1, the UE shall be connected to Cell 1 (PCell) on radio channel 1 (PCC) and shall only monitor PCC and hence be unaware of Cell 2 (PSCell-to-be) on radio channel 2. At the end of T1, the test system shall send a RRC message instructing the UE to add PSCell (Cell 2), and further instructing the UE to report CSI periodically in the PSCell once it has been added. Reception by the UE of this RRC message defines the start of T2.

During T2, the UE shall identify PSCell and carry out random access towards the PSCell. Reception by the test system of the PRACH preamble defines the start of T3.

During T3, the UE shall send periodic CSI reports in PSCell. After having received at least one such report, the test system shall send a RRC message instructing the UE to release the PSCell. Reception by the UE of the RRC message defines the start of T4.

During T4, the UE shall release the PSCell.

Table A.7.5.7.4.1-1: Supported test configurations for FR2-2 PSCell

Table A.7.5.7.4.1-2: General test parameters for PSCell addition and release delay

Table A.7.5.7.4.1-3: NR Cell specific test parameters for PSCell addition and release delay

Table A.7.5.7.4.1-4: OTA related test parameters for PSCell addition and release delay

## A.7.5.7.4.2Test Requirements

The UE shall transmit the PRACH preamble to PSCell at latest TBD ms into T2.

The UE shall transmit at least one periodic CSI report for PSCell during T3.

The UE shall stop transmitting CSI reports for PSCell at latest 20 ms into T4.

All of the above test requirements shall be fulfilled in order for the observed PSCell addition and release delay to be counted as correct. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.8Active TCI state switch delay

## A.7.5.8.1MAC-CE based active TCI state switch

A.7.5.8.1.1NR PCell FR2 active TCI state switch for a known TCI state

A.7.5.8.1.1.1Test Purpose and Environment

The purpose of this test is to verify the active TCI state switch delay requirement defined in clause 8.10.3. Supported test configuration is shown in table A.7.5.8.1.1.1-1.

The test scenario comprises of one NR PCell (Cell 1) as given in table A.7.5.8.1.1.1-2. Cell-specific parameters of NR PCell are specified in table A.7.5.8.1.1.1-3 below. The OTA related test parameters for FR2 are shown in table A.7.5.8.1.1.1-4.

PDCCHs indicating new transmissions shall be sent continuously on PCell to ensure that the UE would have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is configured with 2 different TCI states for PCell, PDCCH TCI state 0 (QCL’d to SSB0) and TCIstate 1 (QCL’d to SSB1), in Cell 1 before starting the test.

-UE is indicated in TCI state 0 as the active PDCCH TCI state

-Target TCI state is not in the active TCI state list.

The test consists of two time periods, T1 and T2. Figure A.7.5.8.1.1.1-1 and Figure A.7.5.8.1.1.1-2 show the Time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival. During T1 only SSB to which PDCCH-TCI-state0 is QCL’d is transmitted. At the beginning of T2, the SSB corresponding to TCI state 1 starts transmitting. The UE is configured to provide periodic L1-RSRP reports. In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 and SSB1, UE receives a MAC-CE command indicating a switch to TCI state 1. tci-PresentInDCI is not configured in the PDSCH configuration, i.e. TCI state for the PDSCH is identical to the PDCCH TCI state.

The test equipment verifies that UE can be scheduled on PCell on TCI state 0 till slot n+ THARQ +. The test equipment also verifies the TCI state switch time in PCell by scheduling the UE on TCI state 1 after slot n+ THARQ + + (Tfirst-SSB + TSSB-proc)/NR slot length.3Nslotsubframe,µ3Nslotsubframe,µ

Table A.7.5.8.1.1.1-1: Supported test configurations

Table A.7.5.8.1.1.1-2: General test parameters for TCI state switch

Table A.7.5.8.1.1.1-3: NR Cell specific test parameters for TCI state switch

Table A.7.5.8.1.1.1-4: OTA related test parameters for TCI state switch

Figure A.7.5.8.1.1.1-1: Time multiplexed downlink transmissions during T1

Figure A.7.5.8.1.1.1-2: Time multiplexed downlink transmissions during T2

A.7.5.8.1.1.2Test Requirements

During T2, UE shall send L1-RSRP report with results for both SSB0 and SSB1.

After receiving MAC-CE command in slot n, UE shall:

-be able to continue to receive on TCI state 0 till slot n+ THARQ +3Nslotsubframe,µ

-be able to start receiving on TCI state 1 after slot n+ THARQ + + Tfirst-SSB/NR slot length5Nslotsubframe,µ

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.8.2RRC based active TCI state switch

A.7.5.8.2.1NR PCell FR2 active TCI state switch for a known TCI state

A.7.5.8.2.1.1Test Purpose and Environment

The purpose of this test is to verify the active TCI state switch delay requirement defined in clause 8.10.3. Supported test configuration is shown in table A.7.5.8.2.1.1-1.

The test scenario comprises of one NR PCell as given in table A.7.5.8.2.1.1-2. Cell-specific parameters of NR PCell is specified in table A.7.5.8.2.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.7.5.8.2.1.1-4.

PDCCHs indicating new transmissions shall be sent continuously on PCell to ensure that the UE would have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is configured with 1 TCI state for PCell, PDCCH-TCI-state0 (QCL’d to SSB0)

-UE is indicated in TCI state0 as the active TCI state

The test consists of two time periods, T1 and T2. Figure A.7.5.8.2.1.1-1 and Figure A.7.5.8.2.1.1-2 show the Time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival. During T1 only SSB to which TCI-state0 is QCL’d is transmitted. At the beginning of T2, the SSB corresponding to TCI-state1 starts transmitting. The UE is configured to provide periodic L1-RSRP reports.  In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 and SSB1, UE receives a RRC command indicating a switch to TCI-state1.

The test equipment verifies the TCI state switch time in PCell by scheduling the UE on TCI state 1 after slot n+ (TRRC_processing  + Tfirst-SSB)/NR slot length + .2Nslotsubframe,µ

Table A.7.5.8.2.1.1-1: Supported test configurations

Table A.7.5.8.2.1.1-2: General test parameters for TCI state switch

Table A.7.5.8.2.1.1-3: NR Cell specific test parameters for TCI state switch

Table A.7.5.8.2.1.1-4: OTA related test parameters for TCI state switch

Figure A.7.5.8.2.1.1-1: Time multiplexed downlink transmissions during T1

Figure A.7.5.8.2.1.1-2: Time multiplexed downlink transmissions during T2

A.7.5.8.2.1.2Test Requirements

During T2, UE shall send L1-RSRP report with both SSB0 and SSB1.

After receiving RRC command in slot n, UE shall be able to start receiving on TCI state 1 after slot n+ (TRRC_processing  + Tfirst-SSB) / NR slot length + .2Nslotsubframe,µ

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.8.3MAC-CE based active TCI state switch for HST FR2 scenario

## A.7.5.8.3.1NR PCell FR2 HST active TCI state switch for a known TCI state

## A.7.5.8.3.1.1Test Purpose and Environment

The purpose of this test is to verify the active TCI state switch delay requirement defined in clause 8.10.3A for FR2 power class 6 UE. Supported test configuration is shown in table A.7.5.8.3.1.1-1. Furthermore, the purpose of this test is also to verify the one shot large timing adjustment requirement specified in clause 7.1.2.3 provided highSpeedMeasFlagFR2-r17 is configured and highSpeedLargeOneStepUL-TimingFR2-r17 is enabled for UE supporting FR2 power class 6 and largeOneStepUL-timingFR2-r17 capability.

The test scenario comprises of one NR PCell (Cell 1) as given in table A.7.5.8.3.1.1-2. Cell-specific parameters of NR PCell are specified in table A.7.5.8.3.1.1-3 below. The OTA related test parameters for FR2 are shown in table A.7.5.8.3.1.1-4. During the test, highSpeedMeasFlagFR2-r17 is configured to be set2 and broadcast to UE.

PDCCHs indicating new transmissions shall be sent continuously on PCell to ensure that the UE would have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is configured with 2 different TCI states for PCell, PDCCH TCI state 0 (QCL’d to SSB0) and TCI state 1 (QCL’d to SSB1), in Cell 1 before starting the test.

-UE is indicated in TCI state 0 as the active PDCCH TCI state

The test consists of two time periods, T1 and T2. Figure A.7.5.8.3.1.1-1 and Figure A.7.5.8.3.1.1-2 show the Time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival. During T1 only SSB to which PDCCH-TCI-state0 is QCL’d is transmitted. At the beginning of T2, the SSB corresponding to TCI state 1 starts transmitting, which has the relative timing delay compared to TCI state 0 by the absolute value of the one-way differential propagation time . The UE is configured to provide periodic L1-RSRP reports. In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 and SSB1, UE receives a MAC-CE command indicating a switch to TCI state 1. tci-PresentInDCI is not configured in the PDSCH configuration, i.e. TCI state for the PDSCH is identical to the PDCCH TCI state. After the TCI state switch, the UE transmit timing accuracy shall be measured by the test equipment by using the SRS defined in table A.7.5.8.3.1-5.Told-Tnew=2.33 μs

The test equipment verifies that

-UE can be scheduled on PCell on TCI state 0 till n+ THARQ +3 ms.

-the TCI state switch time in PCell by scheduling the UE on TCI state 1 after slot n + THARQ + 3 ms + Tfirst-SSB + TSSB-proc + Trs + Trs-proc.

-the UE transmission timing immediately after TCI state switch shall follow the requirements as specified in clause 7.1.2.3.

Table A.7.5.8.3.1.1-1: Supported test configurations

Table A.7.5.8.3.1.1-2: General test parameters for TCI state switch

Table A.7.5.8.3.1.1-3: NR Cell specific test parameters for TCI state switch

Table A.7.5.8.3.1.1-4: OTA related test parameters for TCI state switch

Table A.7.5.8.3.1.1-5: Sounding Reference Symbol Configuration

Figure A.7.5.8.3.1.1-1: Time multiplexed downlink transmissions during T1

Figure A.7.5.8.3.1.1-2: Time multiplexed downlink transmissions during T2

## A.7.5.8.3.1.2Test Requirements

During T2, UE shall send L1-RSRP report with results for both SSB0 and SSB1.

After the TCI state switch, the UE transmission timing immediately after TCI state switch shall follow the requirements as specified in clause 7.1.2.3.

After receiving MAC-CE command in slot n, UE shall:

-be able to continue to receive on TCI state 0 till n + THARQ + 3 ms

-be able to start receiving on TCI state 1 after n + THARQ + 7 ms + Tfirst-SSB + Trs

## A.7.5.8.3.2NR PCell FR2 HST active TCI state switch for PC6 UE supporting tciStateSwitchIndr18 for a known TCI state

## A.7.5.8.3.2.1Test Purpose and Environment

The purpose of this test is to verify the active TCI state switch delay requirement defined in clause 8.10.3 applicable for FR2 power class 6 UE. Supported test configuration is shown in table A.7.5.8.3.2.1-1. Furthermore, the purpose of this test is also to verify the timing adjustment requirement specified in clause 7.1.2.3. In the test, highSpeedMeasFlagFR2-r17 is configured and cross-RRH TCI state indicator for UE-specific PDCCH MAC CE as specified in Clause 6.1.3.77 of TS 38.321 [7] is set to ‘0’ for the TCI state switch for FR2 power class 6 UE supporting tciStateSwitchIndr18 capability.

The test scenario comprises of one NR PCell (Cell 1) and the general test parameters are specified in table A.7.5.8.3.2.1-2. Cell-specific parameters of NR PCell are specified in table A.7.5.8.3.2.1-3 below. The OTA related test parameters for FR2 are specified in table A.7.5.8.3.2.1-4. During the test, highSpeedMeasFlagFR2-r17 is configured to be set2.

PDCCHs indicating new transmissions shall be sent continuously on PCell to ensure that the UE would have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is configured with 2 different TCI states for PCell: PDCCH TCI state 0 (QCL’d to SSB0) and TCI state 1 (QCL’d to SSB1), and TCI state 0 is indicated as the active PDCCH TCI state.

The test consists of two time periods: T1 and T2. Figure A.7.5.8.3.2.1-1 and A.7.5.8.3.2.1-2 show the time multiplexed (allocation in frequency is symbolic) downlink transmissions from each Angle of Arrival. During T1 only SSB to which PDCCH-TCI-state0 is QCL’d is transmitted. From the beginning of T2, the SSB corresponding to TCI state 1 is transmitted. The UE is configured to provide periodic L1-RSRP reports. In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 and SSB1, UE receives a MAC-CE command indicating a switch to TCI state 1 with cross-RRH TCI state indicator for UE-specific PDCCH MAC CE set as ‘0’. tci-PresentInDCI is not configured in the PDSCH configuration, i.e. TCI state for the PDSCH is identical to the PDCCH TCI state. After the TCI state switch, the UE transmit timing accuracy shall be measured by the test equipment by using the SRS defined in table A.7.5.8.3.2-5. TCI state 1 has relative timing delay of 4*64*Tc compared to TCI state 0.

The test equipment verifies that

-UE can be scheduled on PCell on TCI state 0 till n+ THARQ +3 ms.

-the TCI state switch time in PCell by scheduling the UE on TCI state 1 after slot n + THARQ + 3 ms + Tfirst-SSB + TSSB-proc.

-the UE transmission timing immediately after TCI state switch shall follow the requirements as specified in clause 7.1.2.3.

Table A.7.5.8.3.1.1-1: Supported test configurations

Table A.7.5.8.3.2.1-2: General test parameters for TCI state switch

Table A.7.5.8.3.2.1-3: NR Cell specific test parameters for TCI state switch

Table A.7.5.8.3.2.1-4: OTA related test parameters for TCI state switch

Table A.7.5.8.3.2.1-5: Sounding Reference Symbol Configuration

Figure A.7.5.8.3.2.1-1: Time multiplexed downlink transmissions during T1

Figure A.7.5.8.3.2.1-2: Time multiplexed downlink transmissions during T2

## A.7.5.8.3.2.2Test Requirements

During T2, UE shall send L1-RSRP report with results for both SSB0 and SSB1.

After the TCI state switch, the UE transmission timing immediately after TCI state switch shall follow the requirements as specified in clause 7.1.2.3.

After receiving TCI state switch command with cross-RRH TCI state indicator for UE-specific PDCCH MAC CE set to ‘0’ in slot n, UE shall:

-be able to continue to receive on TCI state 0 till n+ THARQ +3 ms

-be able to start receiving on TCI state 1 after n+ THARQ +5 ms + Tfirst-SSB.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.8.4DCI based active TCI state switch with m-DCI for simultaneous reception

## A.7.5.8.4.1Test Purpose and Environment

The purpose of this test is to verify the active TCI state switch delay requirement defined in clause 8.10E.4.2. Supported test configuration is shown in table A.7.5.8.4.1-1.

The test scenario comprises of one NR PCell (Cell 1) as given in table A.7.5.8.4.1-2. Cell-specific parameters of NR PCell are specified in table A.7.5.8.4.1-3 below. The OTA related test parameters for FR2 are shown in table A.7.5.8.4.1-4.

PDCCHs indicating new transmissions shall be sent continuously on PCell to ensure that the UE would have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-The UE is configured with the following TCI states: TCI state 0 (QCL’d to SSB0), TCI state 1 (QCL’d to SSB1), TCI state 2 (QCL’d to SSB2) and TCI state 3 (QCL’d to SSB3).

-UE is indicated with the following TCI states for Cell 1 (PCell):

-PDCCH TCI state 0 (QCL’d to SSB0), PDSCH TCI state 0 (QCL’d to SSB0) for CORESETPoolIndex 0, and

-PDCCH TCIstate 1 (QCL’d to SSB1), PDSCH TCI state 1 (QCL’d to SSB1) for CORESETPoolIndex 1.

-UE is configured with groupBasedBeamReporting-r17 for SSB index 2 and SSB index 3.

-tci-PresentInDCI is configured in the PDSCH configuration.

The test consists of two time periods, T1 and T2. During T1, the time multiplexed (allocation in Frequency is symbolic) downlink transmissions are scheduled from each Angle of Arrival (AoA1, AoA2 and AoA3) as shown in Figure A.7.5.8.4.1-1. UE is configured to transmit periodic L1-RSRP group-based beam reports on SSB index 2 and SSB index 3. After UE transmits the first L1-RSRP group-based beam report with SSB index 2 and SSB index 3 as a beam pair, TE sends TCI state activation MAC-CEs to activate TCI state 2 and TCI state 3 for PDSCHs.

T2 starts at a time that is not earlier than active TCI state list update delay (as defined in section 8.10E.6.2) from the time UE has received the TCI state activation MAC-CEs. At the beginning of T2, at slot n, UE receives DCI to switch PDSCH TCI state on CORESETPoolIndex 0 for indicating the TCI state switch of PDSCH to TCI state 3. At slot n+1, UE receives DCI to switch PDSCH TCI state on CORESETPoolIndex 1 for indicating the TCI state switch of PDSCH to TCI state 2. During T2, the time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival is shown in Figure A.7.5.8.4.1-2.

The test equipment verifies the TCI state switch time in PCell by scheduling the UE on TCI state 2 and TCI state 3 simultaneously after slot n + 1 + timeDurationForQCL

Table A.7.5.8.4.1-1: Supported test configurations

Table A.7.5.8.4.1-2: General test parameters for TCI state switch

Table A.7.5.8.4.1-3: NR Cell specific test parameters for TCI state switch

Table A.7.5.8.4.1-4: OTA related test parameters for TCI state switch

Figure A.7.5.8.4.1-1: Time multiplexed downlink transmissions during T1

Figure A.7.5.8.4.1-2: Time multiplexed downlink transmissions during T2

## A.7.5.8.4.2Test Requirements

After receiving two DCIs in slot n and slot n+1 during T2, UE shall:

-be able to start receiving on TCI state 2 and TCI state 3 simultaneously after slot n + timeDurationForQCL

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.8.5Single-DCI FR2 DCI based active TCI state switch with known target TCI states for simultaneous reception

## A.7.5.8.5.1Test Purpose and Environment

The purpose of this test is to verify the DCI based active TCI state switch delay requirement defined for sDCI in clause 8.10E.4.1 for simultaneous reception in DL, while also verifying that the UE can complete active TCI state list update within the delay requirement defined in 8.10E.6.1. Supported test configuration is shown in table A.7.5.8.5.1-1.

The test scenario comprises of one NR PCell (Cell 1) in FR2-1 as given in table A.7.5.8.5.1-2. Cell-specific parameters of NR PCell are specified in table A.7.5.8.5.1-3 below. The OTA related test parameters for FR2 are shown in table A.7.5.8.5.1-4.

PDCCH indicating new transmissions shall be sent continuously on PCell to ensure that the UE will have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is configured with groupBasedBeamReporting-r17 for SSB index 0 and SSB index 1

-UE is configured with 3 different TCI states for PCell in Cell 1 before starting the test:

-PDCCH TCI state 0 (QCL’d to SSB0),

-PDSCH TCI state 0 (QCL’d to SSB0),

-PDSCH TCI state 1 (QCL’d to SSB1)

-UE is indicated TCI state 0 as the active PDCCH and PDSCH TCI state at the beginning of the test.

-TCI state 1, which is one of the target TCI states, is not in the active TCI state list.

The test consists of two time periods, T1 and T2.

During T1, only SSBs to which PDCCH TCI state 0 and PDSCH TCI state 0 are QCL’d is transmitted (SSB0). During T1, SSB0 is transmitted on AoA1.

At the beginning of T2, the SSB corresponding to PDSCH TCI state 1 starts transmitting on AoA2. The UE is configured with groupBasedBeamReporting-r17 to provide periodic group-based L1-RSRP reports for SSB0 and SSB1. In slot n, which is within 1280 ms of UE providing group-based L1-RSRP report with results for SSB0 and SSB1 as a beam pair, UE receives a MAC-CE command indicating activation of TCI state 0 and TCI state 1 in a single codepoint. Tci-PresentInDCI is configured as enabled in the PDSCH configuration.

After a time that equals to the active TCI state list update delay defined in section 8.10F.6.1 for sDCI, UE receives a DCI indicating TCI state 0 and TCI state 1 for PDSCH scheduling. The TE verifies that the UE can start receiving PDSCH with TCI state 0 (in AoA1) and TCI state 1 (in AoA2) simultaneously after timeDurationForQCL from receiving the DCI.

Table A.7.5.8.5.1-1: Supported test configurations

Table A.7.5.8.5.1-2: General test parameters for TCI state switch

Table A.7.5.8.5.1-3: NR Cell specific test parameters for TCI state switch

Table A.7.5.8.5.1-4: OTA related test parameters for TCI state switch

## A.7.5.8.5.1.2Test Requirements

During T2, UE shall send group-based L1-RSRP report with results for SSB0 and SSB1.

After receiving DCI indicating TCI state 0 and TCI state 1 for PDSCH in slot n, UE shall be able to start receiving TCI state 0 and TCI state 1 simultaneously after n + timeDurationForQCL.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.9Uplink spatial relation switch delay

A.7.5.9.1MAC-CE based Spatial Relation switch

A.7.5.9.1.1NR PCell FR2 spatial relation associated with known DL-RS

## A.7.5.9.1.1.1Test Purpose and Environment

The purpose of this test is to verify fulfillment of the uplink spatial relation switch delay requirement defined in clause 8.12.3 by a UE capable of beam correspondence without the need for UL beam sweeping. The supported test configurations are shown in table A.7.5.9.1.1.1-1.

The test scenario comprises one PCell (Cell 1) as outlined in table A.7.5.9.1.1.1-2. Cell-specific parameters are provided in table A.7.5.9.1.1.1-3. OTA-related test parameters are provided in table A.7.5.9.1.1.1-4.

Throughout the test, PDCCH indicating new transmissions shall ge sent continuously on PCell to ensure that the UE will send ACK/NACKs on PUCCH.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE is configured with a single TCI state, TCI State-0, which is QCLed with SSB0.

-UE is configured with two spatial relation information configurations Spatial Relation Info-0 and Spatial Relation Info-1 for PUCCH, each associated with SSB0 and SSB1, respectively.

-UE is indicated via MAC-CE activation of PUCCH-SpatialRelationInfoId corresponding to Spatial Relation Info-0

-UE is configured with a CSI measurement configuration indicating L1-RSRP measurements on SSB0 and SSB1 with periodic reporting. The L1-RSRP measurement period is influenced by the following: the higher layer parameter timeRestrictionForChannelMeasurement is configured, measured SSBs are fully overlapping with SMTC window, and there are no conflicts with measurement gaps.

The test consists of two time periods, T1 and T2. During T1 only the SSB associated with PDCCH TCI state-0 and PUCCH Spatial Relation Info-0 is transmitted. At the beginning of T2, transmission of the SSB associated with PUCCH Spatial Relation Info-1 starts. The UE conducts periodic L1-RSRP measurements and SSB-Index-RSRP reporting for SSB0 and SSB1. In slot n, which is within 1280 ms after UE receiving both SSB0 and SSB1, and after reporting valid results for both the SSB0 and the SSB1, the UE receives a MAC-CE indicating a switch of spatial relation to PUCCH Spatial Relation Info 1.

The test equipment verifies that the UE transmits according to PUCCH Spatial Relation Info 0 up until slot n + THARQ/NR slot length + , and according to PUCCH Spatial Relation Info 1 from slot n + THARQ/NR slot length +  + 1 and onwards.3Nslotsubframe,µ3Nslotsubframe,µ

Table A.7.5.9.1.1.1-1: Supported test configurations

Table A.7.5.9.1.1.1-2: General test parameters

Table A.7.5.9.1.1.1-3: NR Cell specific test parameters

Table A.7.5.9.1.1.1-4: OTA related test parameters

## A.7.5.9.1.1.2Test Requirements

During T2, the UE shall send L1-RSRP report with results for SSB0 and SSB1.

After receiving MAC-CE command in slot n, the UE shall:

-Continue transmitting using PUCCH spatial relation associated with SSB0 up to and including slot n + THARQ/NR slot length + 3Nslotsubframe,µ

-Start transmitting using PUCCH spatial relation associated with SSB1 from slot n + THARQ/NR slot length +  + 1 and onwards.3Nslotsubframe,µ

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.9.2RRC based spatial relation switch

## A.7.5.9.2.1NR PCell FR2 spatial relation switch associated with a known DL-RS

## A.7.5.9.2.1.1Test Purpose and Environment

The purpose of this test is to verify the RRC based spatial relation switch delay requirement defined in clause 8.12.5 by a UE capable of beam correspondence without the need for UL beam sweeping. In the test the higher layer parameter timeRestrictionForChannelMeasurements is configured. Supported test configuration is shown in table A.7.5.9.2.1.1-1.

The test scenario comprises of one PCell (Cell 1) as given in table A.7.5.9.2.1.1-2. Cell-specific parameters of PCell is specified in table A.7.5.9.2.1.1-3 below. The OTA related test parameters for FR2 is shown in table A.7.5.9.2.1.1-4.

Periodic SRS is transmitted on PCell (Cell 1), and the SRS configuration is SRSConf.1 given in table A.5.4.1.1.1-3.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is configured with 1 SRS-SpatialRelation0 associated with SSB0.

-UE is indicated SRS-SpatialRelation0 as the active SRS spatial relation.

The test consists of two time periods, T1 and T2. During T1 only SSB0 to which SRS-SpatialRelation0 associated is transmitted. UE shall transmit periodic SRS with SRS-SpatialRelation0 on the UL of the PCell.

T2 start when the tester initiates transmission of SSB1 corresponding to SRS-SpatialRelation1. The UE is configured to transmit periodic L1-RSRP reports.

In slot n, which is within 1280ms of UE providing the L1-RSRP report with results for both SSB0 and SSB1, the UE receives an RRC command indicating a switch to transmit periodic SRS with target SRS-SpatialRelation1. The UE shall be able to transmit periodic SRS with target spatial relation (SRS-SpatialRelation1) on PCell in slot n + TRRC_processing/NR slot length +1.

Table A.7.5.9.2.1.1-1: Supported test configurations

Table A.7.5.9.2.1.1-2: General test parameters for spatial relation switch associated with a known DL-RS

Table A.7.5.9.2.1.1-3: NR Cell specific test parameters for spatial relation switch associated with a known DL-RS

Table A.7.5.9.2.1.1-4: OTA related test parameters for spatial relation switch associated with a known DL-RS

## A.7.5.9.2.1.2Test Requirements

During T1 UE shall send L1-RSRP report with SSB0 to which SRS-SpatialRelation0 is associated. During T2, UE shall send L1-RSRP report with SSB1 to which SRS-SpatialRelation1 is associated.

After receiving RRC command in slot n, UE shall be able to transmit target periodic SRS with SRS-SpatialRelation1 on the PCell in the slot n +  TRRC_processing/NR slot length + 1.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.10UE specific CBW change

## A.7.5.10.1NR FR2 UE specific CBW change of PCell with non-DRX in SA

## A.7.5.10.1.1Test Purpose and Environment

The purpose of this test is to verify the UE specific CBW change delay requirement defined in clause 8.13. Supported test configurations are shown in table A.7.5.10.1.1-1.

The test scenario comprises of one PCell (Cell 1) as given in table A.7.5.10.1.1-2. Cell-specific parameters of PCell are specified in table A.7.5.10.1.1-3 below.

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

Time period T1 starts when a RRCReconfiguration with updated CBW configuration, sent from the test equipment to the UE, is received at the UE side in PCell’s slot # denoted i. The UE shall reconfigure its CBW with the updated CBW of final condition (CBW-2).

The UE shall be able to completely receive PDSCH on PCell from the first DL slot that occurs after the beginning of DL slot  as defined in clause 8.13.2 and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot. The UE shall be continuously scheduled on PCell’s BWP-1 on CBW-2 starting from the first DL slot that occurs after the beginning of DL slot .i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length+k1i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length

TRRCprocessingDelay and TCBWchangeDelayRRC are defined in clause 8.13.

The test equipment verifies the UE specific CBW switch time in PCell by counting the time from the time when the RRC Reconfiguration message including updated CBW configurations sent till the time when RRC Reconfiguration Complete message is received.

Table A.7.5.10.1.1-1: UE specific CBW change supported test configurations

Table A.7.5.10.1.1-2: General test parameters for UE specific CBW change in NR SA

Table A.7.5.10.1.1-3: NR Cell specific test parameters for UE specific CBW change in NR SA

Table A.7.5.10.1.1-4: OTA related test parameters for UE specific CBW change test case

## A.7.5.10.1.2Test Requirements

During T1, the UE shall be ready for the reception of uplink grant for PCell from the first DL slot that occurs after the beginning of slot  and starts to report valid ACK/NACK for the PCell from the first UL slot that occurs after the beginning of DL slot.i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length i+TRRCprocessingDelay+TCBWchangeDelayRRCNR Slot length+k1

Where, k1 is the timing between DL data receiving and acknowledgement as specified in [7].

All of the above test requirements shall be fulfilled in order for the observed PCell UE specific CBW change delay to be counted as correct.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.11UE UL carrier RRC reconfiguration Delay

## A.7.5.11.1UE UL carrier RRC reconfiguration Delay

## A.7.5.11.1.1Test Purpose and Environment

The purpose of this test is to verify that when the UE receives a RRC message implying NR UL carrier configuration, the UE shall be ready to start transmission on the newly configured carrier within the time limits specified in clause 8.4.2 and 8.4.3 for configuring and deconfiguring, respectively. The test will also verify the interruption at UL carrier configuration requirements on PCell in clause 8.2.2.2.4.

There are two cells: FR2 PCell (Cell 1) on NR RF channel 1 and FR2 SCell (Cell 2) on NR RF channel 2. NR uplink is broadcast by ServingCellConfigCommonSIB. The test parameters for PCell and SCell are given in table A.7.5.11.1.1-1, table A.7.5.11.1.1-2 and table A.7.5.11.1.1-3 below.  The test consists of three time periods, with duration of T1, T2 and T3 respectively. During time duration T1, NR uplink of Cell 2 is not configured to UE. At the start of T2, a NR uplink of Cell 2 is configured to UE through RRCReconfiguration, then UE shall start transmission on the NR uplink of Cell 2. At the start of T3, the NR uplink is released through RRCReconfiguration.

The test equipment also verifies that potential interruption of PCell due to UL carrier configuration on SCell is carried out within the correct time span and within the correct length by monitoring ACK/NACK sent in PCell.

Table A.7.5.11.1.1-1: Supported test configurations

Table A.7.5.11.1.1-2: General test parameters for SA UE UL carrier RRC reconfiguration Delay for FR2

Table A.7.5.11.1.1-3: NR Cell specific test parameters for SA UE UL carrier RRC reconfiguration Delay for FR2

## A.7.5.11.1.2Test Requirements

The UE shall be ready to start transmission on the NR uplink carrier on SCell within 20 ms from the start of T2.

The UE shall stop the transmission on the NR uplink carrier on SCell within 20 ms from the start of T3.

During T2 and T3, the start of interruption of PCell due to UL carrier configuration or de-configuration on SCell shall not happen outside the UL carrier configuration delay which is 20 ms in this test, and the length of interruption shall not exceed the length specified in clause 8.2.2.2.4.

All of the above test requirements shall be fulfilled in order for the observed UE UL carrier configuration delay and UE UL carrier release delay to be counted as correct. The rate of correct observed UE UL carrier configuration delay and UE UL carrier release delay during repeated tests shall be at least 90 %.

## A.7.5.12Conditional PSCell addition and release delay (FR2 SA)

## A.7.5.12.1Addition and Release Delay of PSCell

## A.7.5.12.1.1Test purpose and environment

The purpose of this test is to verify that the conditional PSCell addition and release delays under SA are within the requirements stated in clause 8.9A.2.

## A.7.5.12.1.2Test Parameters

The supported test configurations are given in table A.7.5.12.1.2-1. The test scenario comprises two NR cells, Cell 1 and Cell 2, on radio channel 1 in FR1 and radio channel 2 in FR2, respectively. Test parameters are given in Tables A.7.5.12.1.2-2 and A.7.5.12.1.2-3 below. The test consists of four successive time periods, with time durations of T1, T2, T3, T4, respectively.

At the start of time duration T1, the UE does not have any timing information of cell 2. NR shall configure a condition implying addition to cell 2 during T1, at a time earlier than TRRC before the beginning of T2.

At the start of T2, cell 2 becomes detectable and meets the addition condition. Reception by the test system of the PRACH preamble defines the start of T3.

During T3, the UE shall send periodic CSI reports in PSCell. After having received at least one such report, the test system shall send an RRC message instructing the UE to release the PSCell. Reception by the UE of the RRC message defines the start of T4.

During T4, the UE shall release the PSCell.

Table A.7.5.12.1.2-1: Supported test configurations for FR2 PSCell

Table A.7.5.12.1.2-2: General test parameters for conditional PSCell addition and release delay

Table A.7.5.12.1.2-3: NR Cell specific test parameters for conditional PSCell addition and release delay

Table A.7.5.12.1.2-4: OTA related test parameters for conditional PSCell addition and release delay

## A.7.5.12.1.3Test Requirements

TRRC_delay + TEvent_DU occurs during T1 as the addition condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms = 6720+10+62 ms=6792 ms (power class 1) or 4160+10+62 ms =4232 ms (power classes 2,3 and 4) from the start of T2.

The UE shall transmit at least one periodic CSI report for PSCell during T3.

The UE shall stop transmitting CSI reports for PSCell at latest 20 ms into T4.

All of the above test requirements shall be fulfilled in order for the observed conditional PSCell addition and release delay to be counted as correct. The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.13Unified TCI state switching delay

## A.7.5.13.1MAC-CE based active joint TCI state switching

## A.7.5.13.1.1NR PCell FR2 active joint TCI state switch for a known TCI state

## A.7.5.13.1.1.1Test Purpose and Environment

The purpose of this test is to verify both active downlink and uplinke TCI state switch delay requirement defined in clause 8.15 and 8.16, respectively, by using joint TCI state of unified TCI state switch framework. In this test, the target TCI state is not in the active TCI state list for PDSCH/PDCCH, and UE is capable of beam correspondence without the need for UL beam sweeping, i.e. beamCorrespondenceWithoutUL-BeamSweeping is set to 1. Supported test configuration is shown in table A.7.5.13.1.1.1-1.

The test scenario comprises of one NR PCell (Cell 1) as given in table A.7.5.13.1.1.1-2. Cell-specific parameters of NR PCell are specified in table A.7.5.13.1.1.1-1 below. The OTA related test parameters for FR2 are shown in table A.7.5.13.1.1.1-2.

Table A.7.5.13.1.1.1-1: Supported test configurations

Table A.7.5.13.1.1.1-2: General test parameters for TCI state switch

## A.7.5.13.1.1.2Test parameters

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-PDCCHs indicating new transmissions shall be sent continuously on PCell to ensure that the UE would have ACK/NACK sending.

-UE is provided with dl-OrJoint-TCIStateList-r17 and UE’s higher layer signalling unifiedTCI-StateType-r17 in IE MIMOParam-r17 is set to joint;

-UE is configured with 2 different joint TCI states for PCell, TCI state 0 (QCL’d to SSB0) and TCI state 1 (QCL’d to SSB1), and the TCI state 1 is not in the active TCI state list for PDSCH/PDCCH.

-UE is indicated TCI state 0 as the active PDCCH TCI state

The test consists of two time periods, T1 and T2. During T1 only source RS in TCI state 0 is transmitted. At the beginning of T2, source RS in TCI state 1 start transmitting. The UE is configured to provide periodic L1-RSRP reports. In slot n which is within 1280 ms after the slot in which UE provides L1-RSRP report with results for both source RSs in TCI state 0 and 1, UE receives a MAC-CE command indicating a switch to TCI state 1. tci-PresentInDCI is not configured in the PDSCH configuration, i.e. TCI state for the PDSCH is identical to the PDCCH TCI state.

The test equipment verifies the following UE behavior for joint TCI state switch:

-UE shall be able to receive and transmit with TCI state 0 until slot slot n + THARQ + , and3Nslotsubframe,µ

-receive and transmit with TCI state 1 from slot n+THARQ +  + (Tfirst_target-PL-RS + 4*Ttarget_PL-RS + 2 ms) / NR slot length3Nslotsubframe,µ

Table A.7.5.13.1.1.2-1: NR Cell specific test parameters for TCI state switch

Table A.7.5.13.1.1.2-2: OTA related test parameters for TCI state switch

## A.7.5.13.1.1.3Test Requirements

The test verifies that UE can be scheduled by PCell on TCI state 0 and TCI state 1.

During T2, UE shall send L1-RSRP report with results for source RSs in both TCI state 0 and 1.

After receiving MAC-CE command in slot n, UE shall:

-be able to receive and transmit with TCI state 0 until  slot n + THARQ + 3Nslotsubframe,µ

-be able to start receiving and transmitting with TCI state 1 after slot n + THARQ + 3 + (Tfirst_target-PL-RS + 4*Ttarget_PL-RS + 2 ms) / NR slot lengthNslotsubframe,µ

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.13.2MAC-CE based active uplink TCI state switch

## A.7.5.13.2.1NR FR2 PCell uplink TCI state switch for a known TCI state

## A.7.5.13.2.1.1Test Purpose and Environment

The purpose of this test is to verify fulfillment of the uplink TCI switch delay requirement defined in clause 8.16.3 by a UE capable of beam correspondence without the need for UL beam sweeping. The test scenario comprises one PCell (Cell 1).

Throughout the test, PDCCH indicating new transmissions shall be sent continuously on PCell to ensure that the UE will send ACK/NACKs on PUCCH.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE is configured with a unified DL TCI state, TCI State-0, and SSB0 is configured as QCL source for the TCI state. At the start of test UE is connected to DL TCI state 0.

-UE is configured with 2 UL TCI states, UL TCI state 0 and UL TCI state 1. QCL info to UL TCI state 0 and 1 is provided by SSB0 and SSB1, respectively. Initially only UL TCI 0 is in the active TCI states.

-PL-RS is configured for each of the UL TCI states. CSI-RS 0 and CSI-RS 1 are associated with UL TCI state 0 and 1 respectively as PL-RS.

-AT the start of the test UE connected to DL TCI state 0 and UL TCI state 0.

Index of CSI-RS#1 is configured for UE as PUSCH-PathlossReferenceRS-Id-r17 which is indicated in TCI-UL-State-r17 of uplink TCI state 1. CSI-RS#1 is QCLed typeD with SSB#1. UE does not maintain CSI-RS#1 as pathloss RS before the uplink TCI state switching.

The test consists of two time periods, T1 and T2. During T1, only the SSB associated with DL TCI state-0 and UL TCI state 0 is transmitted. At the beginning of T2, transmission of the SSB 1 associated with UL TCI state 1 starts. The UE conducts periodic L1-RSRP (i.e., SSB-Index-RSRP) reporting for SSB0 and SSB1. In slot n, which is within 1280 ms after UE receiving both SSB0 and SSB1, and after reporting valid results for both the SSB0 and the SSB1, the UE receives a MAC-CE indicating a TCI state switch to UL TCI state 1.

The test equipment verifies that the UE transmits according to UL TCI state 0 up until slot n + THARQ + , and according to UL TCI state 1 from slot n + THARQ +  + NM* (Tfirst_target-PL-RS + 4*Ttarget_PL-RS + 2 ms) / NR slot length and onwards. NM is equal to 1. Where, THARQ (in slot) is the timing between DL data transmission and acknowledgement as specified in TS 38.213 [3].3Nslotsubframe,µ3Nslotsubframe,µ

## A.7.5.13.2.1.2Test parameters

The supported test configurations are provided in table A.7.5.13.2.1.2-1.

General test parameters are provided in table A.7.5.13.2.1.2-2.

Cell-specific parameters are provided in table A.7.5.13.2.1.2-3.

OTA-related test parameters are provided in table A.7.5.13.2.1.2-4.

Table A.7.5.13.2.1.2-1: Supported test configurations

Table A.7.5.13.2.1.2-2: General test parameters

Table A.7.5.13.2.1.2-3: NR Cell specific test parameters

Table A.7.5.13.2.1.2-4: OTA related test parameters

## A.7.5.13.2.1.3Test Requirements

During T2, the UE shall send L1-RSRP report with results for SSB0 and SSB1.

After receiving MAC-CE command in slot n, the UE shall:

-Continue transmitting using UL TCI state 0 up to and including slot n + THARQ + 3Nslotsubframe,µ

-Start transmitting using UL TCI state 1, from slot n + THARQ +  + (Tfirst_target-PL-RS + 4*Ttarget_PL-RS + 2 ms) / NR slot length and onwards.3Nslotsubframe,µ

The rate of correct events observed during repeated tests shall be at least 90 %

## A.7.5.13.3MAC-CE based active downlink TCI state switch

## A.7.5.13.3.1NR PCell FR2 active downlink TCI state switch to cell with additional PCI for a known TCI state

## A.7.5.13.3.1.1Test Purpose and Environment

The purpose of this test is to verify the MAC-CE based active downlink TCI state switch delay requirement defined in clause 8.15.3. Supported test configuration is shown in table A.7.5.13.3.1.1-1.

Table A.7.5.13.3.1.1-1: Supported test configurations

## A.7.5.13.3.1.2Test Parameters

The test scenario comprises of one NR PCell (Cell 1) and one NR cell as the cell with additional PCI (Cell 2), as given in table A.7.5.13.3.1.2-1. Cell-specific parameters of NR PCell and the cell with additional PCI are specified in table A.7.5.13.3.1.2-2 below. The OTA related test parameters for FR2 are shown in table A.7.5.13.3.1.2-3.

PDCCHs indicating new transmissions shall be sent continuously on PCell to ensure that the UE would have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is provided with dl-OrJoint-TCIStateList-r17 and UE’s higher layer signalling unifiedTCI-StateType-r17 in IE MIMOParam-r17 is set to separate.

-UE is configured with SSB-based L1-RSRP measurements on cell with additional PCI (Cell 2)

-UE is configured with 2 different TCI states for PCell, TCI state 0 (QCL’d to TRS resource set 1, TCI state of which is QCLed to SSB0 of Cell 1) and TCI state 1 (QCL’d to TRS resource set 2, TCI state of which is QCLed to SSB1 of Cell 2), in Cell 1 before starting the test.

-UE is indicated in TCI state 0 as the active TCI state

The test consists of two time periods, T1 and T2. Figure A.7.5.13.3.1.2-1 and Figure A.7.5.13.3.1.2-2 show the Time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival. During T1 only SSB to which TCI-state0 is QCL’d is transmitted. At the beginning of T2, the SSB corresponding to TCI state 1 starts transmitting. The UE is configured to provide periodic L1-RSRP reports. In slot n which is within 1280 ms of UE providing L1-RSRP report with results for both SSB0 of Cell 1 and SSB1 of Cell 2, UE receives a MAC-CE command indicating a switch to TCI state 1. tci-PresentInDCI is not configured in the PDSCH configuration, i.e. TCI state for the PDSCH is identical to the PDCCH TCI state.

The test equipment verifies that UE can be scheduled on PCell on TCI state 0 till slot n+ THARQ +. The test equipment also verifies the TCI state switch time in PCell by scheduling the UE on TCI state 1 after slot n+ THARQ + + (Tfirst-SSB + TSSB-proc)/NR slot length.3Nslotsubframe,µ3Nslotsubframe,µ

Table A.7.5.13.3.1.2-1: General test parameters for TCI state switch

Table A.7.5.13.3.1.2-2: NR Cell specific test parameters for TCI state switch to a cell with additional PCI

Table A.7.5.13.3.1.2-3: OTA related test parameters for TCI state switch to a cell with additional PCI

Figure A.7.5.13.3.1.2-1: Time multiplexed downlink transmissions during T1

Figure A.7.5.13.3.1.2-2: Time multiplexed downlink transmissions during T2

## A.7.5.13.3.1.3Test Requirements

During T2, UE shall send L1-RSRP report with results for both SSB0 of Cell 1 and SSB1 of Cell 2.

After receiving MAC-CE command in slot n, UE shall:

-be able to continue to receive on DL TCI state 0 till slot n+ THARQ +3Nslotsubframe,µ

-be able to start receiving on DL TCI state 1 after slot n+ THARQ + (5 ms + Tfirst-SSB) / NR slot length

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.13.4sDCI MAC-CE based joint TCI state switching

## A.7.5.13.4.1NR PCell FR2 dual downlink and uplink TCI state switch in sDCI for known case

## A.7.5.13.4.1.1Test Purpose and Environment

The purpose of this test is to verify both active downlink and uplink TCI state switch delay requirement defined in clause 8.21 and 8.23, respectively, by using joint TCI state of unified TCI state switch framework when tci-JointTCI-UpdateSingleActiveTCI-PerCC-r18 is supported and when tci-SeparateTCI-UpdateSingleActiveTCI-PerCC-r18 is not supported. Supported test configuration is shown in table A.7.5.13.4.1.1-1.

Table A.7.5.13.4.1.1-1: Supported test configurations

Table A.7.5.13.4.1.1-2: General test parameters for dual TCI state switch

## A.7.5.13.4.1.2Test parameters

The test scenario comprises of one NR PCell (Cell 1) as given in table A.7.5.13.4.1.2-1. Cell-specific parameters of NR PCell are specified in table A.7.5.13.4.1.2-2 below. The OTA related test parameters for FR2 are shown in table A.7.5.13.4.1.2-3.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-PDCCHs indicating new transmissions shall be sent continuously on Pcell to ensure that the UE would have ACK/NACK sending.

-UE is provided with dl-OrJoint-TCIStateList-r17 and UE’s higher layer signalling unifiedTCI-StateType-r17 in IE MIMOParam-r17 is set to joint.

-applyIndicatedTCI-State-r18 is set as {first} for TRP0 (CORESET index p associated with Joint TCI state 0 and Joint TCI state 1) and as {second} for TRP1 (CORESET index q associated with Joint TCI state 2 and Joint TCI state 3).

-tci-SelectionPresentInDCI-r18 is configured in the BWP configuration, i.e. TCI state for the PDSCH is indicated by DCI format 1_1 and PDSCHs on two TRPs are scheduled in TDM manner.

-UE is configured with two joint TCI states (TCI state 0 and TCI state 1) for TRP0 and two joint TCI states (TCI state 2 and TCI state 3) for TRP1. QCL info to Joint TCI state 0,1,2 and 3 are provided by SSB0, SSB1, SSB2 and SSB3, respectively.

-UE is indicated in TCI state 0 and TCI state 2 as the active TCI state for TRP0 and TRP1.

The test consists of two time periods, T1 and T2. During T1, SSB0 in joint TCI state 0 and SSB2 in joint TCI state 2 are transmitted.

At the beginning of T2, SSB1 in joint TCI state 1 and SSB3 in joint TCI state 3 start transmitting. The UE is configured to provide periodic L1-RSRP reports. In slot n which is within 1280 ms after the slot in which UE provides L1-RSRP report with results for SSB1 and SSB3 in joint TCI state 1 and joint TCI state 3, UE receives a MAC-CE command indicating a switch to dual joint TCI state 1 and TCI state 3 for two TRPs.

The test equipment verifies that UE can be scheduled by two TRPs on joint TCI state 0 and joint TCI state 2 till slot n+ THARQ +. The test equipment also verifies the TCI state switch time for two TRPs by scheduling the UE on joint TCI state 1 and joint TCI state 3 after slot n+THARQ +  + max{NM1* (Tfirst_target-PL-RS1 + 4*Ttarget_PL-RS1 + 2 ms), NM2* (Tfirst_target-PL-RS2 + 4*Ttarget_PL-RS 2+ 2 ms) }/ NR slot length.3Nslotsubframe,µ3Nslotsubframe,µ

Table A.7.5.13.4.1.2-1: Void

Table A.7.5.13.4.1.2-2: NR Cell specific test parameters for dual TCI state switch

Table A.7.5.13.4.1.2-3: OTA related test parameters for dual TCI state switch

## A.7.5.13.4.1.3Test Requirements

During T2, the test verifies that UE can be scheduled by two TRPs on joint TCI state 1 and joint TCI state 3.

After receiving MAC-CE command in slot n, UE shall:

-be able to continue to receive and transmit with joint TCI state 0 and joint TCI state 2 till slot n+ THARQ +3Nslotsubframe,µ

-be able to start receiving and transmitting with joint TCI state 1 and joint TCI state 3 after slot n+THARQ +  + max{NM1* (Tfirst_target-PL-RS1 + 4*Ttarget_PL-RS1 + 2 ms), NM2* (Tfirst_target-PL-RS2 + 4*Ttarget_PL-RS 2+ 2 ms) }/ NR slot length.3Nslotsubframe,µ

-where NM1=1, NM2=1.

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.13.5MAC-CE based dual downlink TCI state switching delay for unified TCI for single-DCI mTRP

## A.7.5.13.5.1NR PCell FR2 dual downlink TCI state switch in sDCI for known case

## A.7.5.13.5.1.1Test Purpose and Environment

The purpose of this test is to verify the MAC-CE based dual downlink TCI state switch delay requirement defined in clause 8.21.3 when tci-SeparateTCI-UpdateSingleActiveTCI-PerCC-r18 is supported. Supported test configuration is shown in table A.7.5.13.5.1.1-1.

Table A.7.5.13.5.1.1-1: Supported test configurations

## A.7.5.13.5.1.2Test Parameters

There is one active serving cell (Cell 1) configured with two TRPs in the test. Cell-specific parameters of Cell 1 are specified in table A.7.5.13.5.1.2-2 below. The OTA related test parameters for FR2 are shown in table A.7.5.13.5.1.2-3.

PDCCHs indicating new transmissions shall be sent continuously on TRP0 to ensure that the UE would have ACK/NACK sending.

Before the test starts,

-UE is connected to Cell 1  on radio channel 1 (PCC).

-UE is provided with dl-OrJoint-TCIStateList-r17 and UE’s higher layer signalling unifiedTCI-StateType-r17 in IE MIMOParam-r17 is set to separate.

-UE is configured with SSB-based L1-RSRP measurements on Cell 1

-applyIndicatedTCI-State-r18 is set as {first} for TRP0 (CORESET index p associated with Joint TCI state 0 and Joint TCI state 1) and as {second} for TRP1 (CORESET index q associated with Joint TCI state 2 and Joint TCI state 3).

-tci-SelectionPresentInDCI-r18 is configured in the BWP configuration, i.e. TCI state for the PDSCH is indicated by DCI format 1_1 and PDSCHs on two TRPs are scheduled in TDM manner.

-UE is configured with two TCI states (TCI state 0 and TCI state 1) for TRP0 and two TCI states(TCI state 2 and TCI state 3) for TRP1. QCL info to DL TCI state 0, 1 , 2 and 3 are provided by SSB0, SSB1, SSB2 and SSB3, respectively.

-UE is indicated in TCI state 0 and TCI state 1 as the active TCI state for TRP0 and TRP1

The test consists of two time periods, T1 and T2. During T1, source RS in TCI state 0 and TCI state 2 are transmitted. At the beginning of T2, source RS in TCI state 1 and source RS in TCI state 3 start transmitting. The UE is configured to provide periodic L1-RSRP reports. In slot n which is within 1280 ms after the slot in which UE provides L1-RSRP report with results for source RSs in TCI state 1 and 3, UE receives a MAC-CE command indicating a switch to TCI state 1 and 3 for two TRPs. tci-PresentInDCI is not configured in the PDSCH configuration, i.e. TCI state for the PDSCH is identical to the PDCCH TCI state.

The test equipment verifies that UE can be scheduled by two TRPs on TCI state 0 and TCI state 2 till slot n+ THARQ +. The test equipment also verifies the TCI state switch time for two TRPs by scheduling the UE on TCI state 1 and TCI state 3 after slot after slot n+ THARQ + + max{TOk1*(Tfirst-SSB1 + AD1*TSSB1  + TSSB-proc), TOk2*(Tfirst-SSB2 + AD2*TSSB2 + TSSB-proc)} / NR slot length.3Nslotsubframe,µ3Nslotsubframe,µ

Table A.7.5.13.5.1.2-1: General test parameters for TCI state switch

Table A.7.5.13.5.1.2-2: NR Cell specific test parameters

Table A.7.5.13.5.1.2-3: OTA related test parameters for TCI state switch

## A.7.5.13.5.1.3Test Requirements

During T2, the test verifies that UE can be scheduled by two TRPs on TCI state 1 and TCI state 3.

After receiving MAC-CE command in slot n, UE shall:

-be able to continue to receive on DL TCI state 0 and DL TCI state 2 till slot n+ THARQ +3Nslotsubframe,µ

-be able to start receiving on DL TCI state 1 and DL TCI state 3  after slot n+ THARQ + + max{TOk1*(Tfirst-SSB1 + AD1*TSSB1  + TSSB-proc), TOk2*(Tfirst-SSB2 + AD2*TSSB2 + TSSB-proc)} / NR slot length3Nslotsubframe,µ

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.13.6MAC-CE based active uplink TCI state switch for single-DCI mTRP

## A.7.5.13.6.1NR FR2 PCell uplink TCI state switch for two known TCI states

## A.7.5.13.6.1.1Test Purpose and Environment

The purpose of this test is to verify fulfillment of the uplink TCI switch delay requirement defined in clause 8.23.3 by a UE capable of beam correspondence without the need for UL beam sweeping when tci-SeparateTCI-UpdateSingleActiveTCI-PerCC-r18 is supported. The test scenario comprises one PCell (Cell 1) with two TRPs.

Throughout the test, PDCCH indicating new transmissions shall be sent continuously on PCell to ensure that the UE will send ACK/NACKs on PUCCH.

Before the test starts,

-UE is connected to Cell 1 on radio channel 1.

-UE is configured with a unified DL TCI state, TCI State-0, and SSB0 is configured as QCL source for the TCI state. At the start of test UE is connected to DL TCI state 0.

-UE is configured with 4 UL TCI states, UL TCI state 0, UL TCI state 1, UL TCI state 2, and UL TCI state 3. QCL info to UL TCI state 0, 1, 2, and 3 is provided by SSB0, SSB1, SSB2, and SSB3, respectively. Initially only UL TCI 0 is in the active TCI state list.

-PL-RS is configured for each of the UL TCI states. CSI-RS 0, CSI-RS 1, CSI-RS 2, and CSI-RS 3 are associated with UL TCI state 0, 1, 2, and 3 respectively as PL-RS.

-At the start of the test UE is connected to DL TCI state 0, UL TCI state 0, and UL TCI state 1.

Index of CSI-RS#1 is configured for UE as PUSCH-PathlossReferenceRS-Id-r17 which is indicated in TCI-UL-State-r17 of uplink TCI state 1. CSI-RS#1 is QCLed typeD with SSB#1. UE does not maintain CSI-RS#1 as pathloss RS before the uplink TCI state switching.

Index of CSI-RS#2 is configured for UE as PUSCH-PathlossReferenceRS-Id-r17 which is indicated in TCI-UL-State-r17 of uplink TCI state 2. CSI-RS#2 is QCLed typeD with SSB#2. UE does not maintain CSI-RS#2 as pathloss RS before the uplink TCI state switching.

The test consists of two time periods, T1 and T2. During T1, only the SSBs associated with DL TCI state-0, UL TCI state 0, and UL TCI state 1 are transmitted. At the beginning of T2, transmission of the SSB 2 associated with UL TCI state 2 and transmission of the SSB 3 associated with UL TCI state 3 start. The UE conducts periodic L1-RSRP (i.e., SSB-Index-RSRP) reporting for SSB0, SSB1, SSB2, and SSB3. In slot n, which is within 1280 ms after UE receiving SSB0, SSB1, SSB2, and SSB3, and after reporting valid results for the SSB0, the SSB1, the SSB2 and the SSB3, the UE receives a MAC-CE indicating a TCI state switch to UL TCI state 2 and to UL TCI state 3.

The test equipment verifies that the UE transmits according to UL TCI state 0 and UL TCI state 1 up until slot n + THARQ + , and according to UL TCI state 2 and to UL TCI state 3 from slot n + THARQ +  + max{NM1* (Tfirst_target-PL-RS1 + 4*Ttarget_PL-RS1 + 2 ms), NM2* (Tfirst_target-PL-RS2 + 4*Ttarget_PL-RS2 + 2 ms)} / NR slot length and onwards. NM1 is equal to 1. NM2 is equal to 1. Where, THARQ (in slot) is the timing between DL data transmission and acknowledgement as specified in TS 38.213 [3].3Nslotsubframe,µ3Nslotsubframe,µ

## A.7.5.13.6.1.2Test parameters

The supported test configurations are provided in table A.7.5.13.6.1.2-1.

General test parameters are provided in table A.7.5.13.6.1.2-2.

Cell-specific parameters are provided in table A.7.5.13.6.1.2-3.

OTA-related test parameters are provided in table A.7.5.13.6.1.2-4.

Table A.7.5.13.6.1.2-1: Supported test configurations

Table A.7.5.13.6.1.2-2: General test parameters

Table A.7.5.13.6.1.2-3: NR Cell specific test parameters

Table A.7.5.13.6.1.2-4: OTA related test parameters

## A.7.5.13.6.1.3Test Requirements

During T2, the UE shall send L1-RSRP report with results for SSB0 and SSB1.

After receiving MAC-CE command in slot n, the UE shall:

-Continue transmitting using UL TCI state 0 and UL TCI state 1 up to and including slot n + THARQ + 3Nslotsubframe,µ

-Start transmitting using UL TCI state 2 and UL TCI state 3, from slot n + THARQ +  + max{Tfirst_target-PL-RS1 + 4*Ttarget_PL-RS1 + 2 ms, Tfirst_target-PL-RS2 + 4*Ttarget_PL-RS2 + 2 ms} / NR slot length and onwards.3Nslotsubframe,µ

The rate of correct events observed during repeated tests shall be at least 90 %.

## A.7.5.14PSCell RACH-less based Activation and deactivation for FR1+FR2 inter-band with target PSCell in FR2

## A.7.5.14.1Test Purpose and Environment

The purpose of this test case is to test the activation PSCell delay for a UE configured with one deactivated SCG in NR-DC and when PSCell in one SCG is being activated. The test also tests the deactivation delay. The test case tests the requirements within which the UE shall be able to activate the deactivated SCG in clause 8.17.2 for RACH-less based conditions when PSCell and TCI state are known. The PCell is in NR FR1 and the PSCell is in NR FR2.

The supported test configurations are defined in table A.7.5.14.1-1. The test parameters for NR cell are given in Tables A.7.5.14.1-2. And cell specific test parameters are described in Tables A.7.5.14.1-3. OTA related test parameters are defined in table A.7.5.14.1-4.

At the beginning of T1 the UE is configured with a PSCell which is activated. At T1 the PSCell is deactivated. PSCell is configured with bfd-and-RLM with value true.

An RRC message for activation of PSCell is sent by the test equipment 1 s after the RRC message deactivating the PSCell, in a slot # denoted m. The point in time at which the RRC message for activation of PSCell is received at the UE defines the start of time period T2.

During T2, the test equipment monitors for SR from the UE on the PSCell. The time when test equipment receives a scheduling request from the UE is denoted as slot T3.

Time period T4 starts when a RRC message for deactivation of the PSCell, sent from the test equipment to the UE in a slot # denoted n, is received at the UE.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of the PSCell, respectively.

The test equipment verifies the activation time by when the SR from the UE is received in the activated PSCell.

The test equipment verifies the deactivation time by counting the slots from the time when the PSCell deactivation command is sent until UL transmission from the PSCell is discontinued.

Table A.7.5.14.1-1: Supported test configurations for FR2 PSCell activation case

Table A.7.5.14.1-2: General Test Parameters for FR2 PSCell activation and deactivation

TBD

Table A.7.5.14.1-3: Cell specific test parameters for FR2 PSCell activation case

Table A.7.5.14.1-4: OTA related test parameters for FR1 PCell with FR2 PSCell activation case

## A.7.5.14.2Test Requirements

During T2 the UE shall send the first SR on PSCell in the first available uplink SR resource no later than T3 which is:

TRRC_delay + Tprocessing + Tsearch + T∆ + TIU + 2 ms

as defined on clause 8.17.2. In this test case:

Tprocessing = 5 ms (no RRC parameter has been modified),

Tsearch = 0 ms (RACH-less based PSCell activation, with RLM and BFD are configured, PSCell and TCI state are known), and

T∆ = 20 ms.

This allows T3 of [TRRC_delay + TIU + 27]ms

During T4 the UE shall stop all transmissions on the PSCell no later than in slot  as defined in 8.17.3.n+TRRC_delayNR slot length

During T2 the interruption of PCell during PSCell activation shall not happen outside the slot m + TRRC_delay.

During T4 the interruption of PCell during PSCell deactivation shall not happen outside the slot n + TRRC_delay.

The interruption duration on PCell due to activation and deactivation of PSCell shall not be more than the values specified for in Clause 8.17.2 and 8.17.3.

## A.7.5.15Void

## A.7.5.16UE L1-RSRP Scheduling and Measurement Restrictions on FR2-1

## A.7.5.16.1Test Purpose and Environment

The purpose of this test is to verify that the NR UE correctly follows the L1-RSRP scheduling restrictions requirements defined in clause 9.5.6.3 and measurement restrictions defined in clause 9.5.5.2.

There is no measurement gap and no DRX configured in the test. The test has higher layer parameter timeRestrictionForChannelMeasurements configured. The test is for sDCI based sceneriao and consists of two time periods, T1 and T2.

Before the test starts,

-UE is connected to Cell 1 (PCell) on radio channel 1 (PCC).

-UE is configured with groupBasedBeamReporting-r17 for SSB index 0 and SSB index 1.

-UE is configured with 2 different TCI states for PCell, PDCCH TCI state 0 (QCL-ed to SSB0) and TCI state 1 (QCL-ed to SSB1).

-tci-PresentInDCI is not configured in the PDSCH configuration, i.e. TCI state for the PDSCH is identical to the PDCCH TCI state.During T1, the time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival (AoA1 and AoA2) is shown in Figure A.7.5.16.1-1. UE transmits periodic L1-RSRP group-based beam reports for SSB index 0 and SSB index 1. After UE transmits first valid L1-RSRP group-based beam report, TCI state 0 and TCI state 1 are activated for CORESET index p and CORSET index q which indicates for 2 PDSCH reception.

During T2, the time multiplexed (allocation in Frequency is symbolic) downlink transmissions from each Angle of Arrival is shown in Figure A.7.5.16.1-2. At the beginning of T2, the CSI-RS resource index 0 and CSI-RS resource index 1 are configured for measurement resources for L1-RSRP. CSI-RS resource 0 is QCL-ed to SSB index 0, and CSI-RS resource 1 is QCL-ed to SSB index 1. During T2, CSI-RS resource 0 is transmitted on AoA1 and CSI-RS resource 1 is transmitted on AoA2. During T2, after the CSI-RS configuration, PDSCH is always scheduled on the symbols overlapping with CSI-RS resource symbols.

For scheduling restriction relaxation, the UE is required to receive both PDSCHs on the symbols overlapped with CSI-RS configured for L1-RSRP and sends ACK correctly.

For measurement restriction relaxation, the UE is required to measure both CSI-RS resource index 0 and CSI-RS resource index 1 at the same time from the beginning of T2.

The test parameters are given in table A.7.5.16.1-1, table A.7.5.16.1-2, table A.7.5.16.1-3 and table A.7.5.16.1-4 below.

Table A.7.5.16.1-1: Supported test configurations

Table A.7.5.16.1-2: General test parameters for NR L1-RSRP scheduling and measurement restriction test case in FR2

Table A.7.5.16.1-3: Cell specific test parameters for NR L1-RSRP scheduling and measurement restriction test case in FR2

Table A.7.5.16.1-4: NR OTA test parameters for NR L1-RSRP scheduling and measurement restriction test case in FR2

Figure A.7.5.16.1-1: Time multiplexed downlink transmissions during T1

Figure A.7.5.16.1-2: Time multiplexed downlink transmissions during T2

## A.7.5.16.2Test Requirements

The UE behaviour follows the requirements defined in clause 9.5.6.3 and 9.5.5.2.

During T2,

-UE is required to receive both PDSCHs and send ACK correctly.

-No later than Y + 80 slot from the beginning of time period T2, UE shall send L1-RSRP report including the valid results for both CSI-RS resource 0 and CSI-RS resource 1 while meeting the accuracy requirements defined in clause 10.1.20.

-Y is the RRC processing delay, which is 10 ms

## A.7.5.17SCG Activation and deactivation for FR1+FR1 inter-band with target PSCell in FR1

## A.7.5.17.1Test Purpose and Environment

The purpose of this test case is to test the PSCell activation delay for a UE configured with one deactivated SCG in NR-DC and when PSCell in one SCG is being activated. The test also tests the deactivation delay. The test case tests the requirements within which the UE shall be able to activate the deactivated SCG in clause 8.17.2 for when PSCell is known and TCI state is known. The PCell is in NR FR1 and the PSCell is in NR FR1.

The supported test configurations are defined in table A.7.5.17.1-1. The test parameters for NR cell are given in Tables A.7.5.17.1-2. And cell specific test parameters are described in Tables A.7.5.17.1-3.

During T1 the PSCell is configured in deactivated state. The TE ensures that the deactivated PSCell remain known until the PSCell is activated.

At T2 an RRC message for activation of PSCell is sent by the test equipment.The point in time at which the RRC message, for activating of the PSCell , is received at the UE in slot n defines as the starting point of T2

During T2, the test equipment monitors for PRACH preamble from the UE on the PSCell. The time when TE receives a preamble from the UE is denoted as starting point of T3.

During T3 the TE monitoris the msg3,and after sending the msg4, the TE sends the RRC deactivation command to the UE. The point in time at which the RRC message for deactivating the PSCell is received at the UE in slot n defines the starting time of T4.

During the time period T4, the UE is configured with measCyclePscell , bfd-and-RLM with value true . And the TE sends the 2nd RRC activation command.

The time when UE receives the 2nd RRC activation command in slot n , defines as the starting time of T5.

During T5, the test equipment monitors for SR from the UE on the PSCell. The time when test equipment receives a scheduling request from the UE is denoted as the ending point of the test.

The test equipment verifies that potential interruption is carried out in the correct time span by monitoring ACK/NACK sent in PCell during activation and deactivation of the PSCell, respectively.

For 1 st time activation during T2, the test equipment verifies the activation time by when the Random Access preamble from the UE is received in the activated PSCell.

During T4 and T5 the TE ensures that that TCI state is known.

For the 2nd time activation during T5, the test equipment verifies the activation time by when the SR from the UE is received in the activated PSCell. The TE verifies the deactivation time by counting the slots from the time when the PSCell deactivation command is sent until UL transmission from the PSCell is discontinued.

Table A.7.5.17.1-1: Supported test configurations for FR1 PSCell activation case

Table A.7.5.17.1-2: General Test Parameters for FR1FR1 PSCell activation and deactivation

Table A.7.5.17.1-3: Cell specific test parameters for FR1-FR1 PSCell activation case

## A.7.5.17.2Test Requirements

RRC message for activation of the PSCell is received in slot n at the UE and denotes the starting point of T2. During T2 the UE shall send the first preamble on PSCell in the first available PRACH occation no later than:

Tactivation_time = TRRC_delay + Tprocessing + Tsearch + T∆ + TIU + 2 ms

After T2 as defined on clause 8.17.2.

In this test case:

Tprocessing = 5 ms

Tsearch = 0 ms PSCell and TCI state are known, and

T∆ = 20 ms.

Tiu = 10 ms.

This allows T2 of Tactivation_time = TRRC_delay + 37 ms

The UE shall stop all transmissions on the PSCell no later than in slot n +  after T4, as defined in 8.17.3.TRRC_delayNR slot length

The 2nd RRC activation command is received in slot n at the UE as the starting time of T5. During T5 the UE shall send the first SR on PSCell in the first available uplink SR resource no later than T5 which is :

Tactivation_time = TRRC_delay + Tprocessing + Tsearch + T∆ + TIU + 2 ms

as defined on clause 8.17.2. In this test case:

Tprocessing = 5 ms (no RRC parameter has been modified)

Tsearch = 0 ms (RACH-less activation PSCell and TCI state are known), and

T∆ = 20 ms.

Tiu = 10 ms.

This allows T5 PSCell activation time of Tactivation_time = TRRC_delay + 37 ms

During T2 and T5 the interruption of PCell during PSCell activation shall not happen outside the slot m + TRRC_delay.

During T4 the interruption of PCell during PSCell deactivation shall not happen outside the slot n + TRRC_delay.

The interruption duration on PCell due to activation and deactivation of PSCell shall not be more than the values specified for in Clause 8.17.2 and 8.17.3.

## A.7.5.18Subsequent conditional PSCell addition/change

## A.7.5.18.1Intra-frequency subsequent CPC from FR1-FR2 NR-DC to FR1-FR2 NR-DC

## A.7.5.18.1.1Test purpose and environment

The purpose of this test is to verify that the subsequent conditional NR PSCell change under NR-DC is within the requirements stated in clause 8.11E.2.

For UE supporting subsequent conditional PSCell addition/change, UE only needs to pass either intra-frequency CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC defined in clause A.6.5.12.1. or intra-frequency CPC from FR1-FR2 NR-DC to FR1-FR2 NR-DC defined in clause A.7.5.18.1.1.

For UE which can pass this test, test of conditional PSCell addition and release delay defined in A.7.5.12 can be skipped.

Supported test configurations are shown in A.7.5.18.1.1-1. The test scenario comprises three NR cells, Cell 1, Cell 2 and Cell 3. Cell 1 is on radio channel 1 in FR1. Cell 2 and Cell 3 are on radio channel 2 in FR2. The test parameters for the NR Cell 1 are given in table A.3.7A. The NR Cell 1 once set up is not changed across time. The test parameters for NR Cell 2 and Cell 3 are given in Tables A.7.5.18.1.1-2, cell-specific parameters in A.7.5.18.1.1-3 and OTA parameters in A.7.5.18.1.1-4 below.

The test consists of three successive time periods with duration of T1, T2, and T3 respectively. There are two carriers each with one cell. Before the test starts the UE is connected to Cell 1 (NR PCell) on radio channel 1 (PCC) but is not aware of Cell 2 (NR PSCell 1) and Cell 3 (NR PSCell 2) on radio channel 2. The UE is only monitoring the PCC. During T1 only Cell 1 is known to the UE.

At the start of time duration T1, the UE does not have any timing information of Cell 2. The TE shall configure subsequent conditional PSCell addition/change with Cell 2 and Cell 3 as target PSCells during T1, at a time earlier than TRRC_delay before the beginning of T2.

At the start of T2, Cell 2 becomes detectable and meets the PSCell addition condition. UE shall be able to measure and detect that the condition is fulfilled, after which it will transmit the PRACH preamble to Cell 2 during T2.

Upon PSCell addition complete (UE transmits SN RRCReconfigurationcomplete message), T3 starts. At the start of T3, Cell 3 becomes detectable and meets the PSCell change condition. UE shall be able to measure and detect that the condition is fulfilled, after which it will transmit the PRACH preamble to Cell 3 during T3.

Table A.7.5.18.1.1-1: Supported test configurations for Intra-frequency Subsequent CPC from FR1-FR2 NR-DC to FR1-FR2 NR-DC

Table A.7.5.18.1.1-2: General Test Parameters for subsequent CPC from FR1-FR2 NR-DC to FR1-FR2 NR-DC

Table A.7.5.18.1.1-3: Cell Specific Parameters for subsequent CPC from FR1-FR2 NR-DC to FR1-FR2 NR-DC (Cell 2, Cell 3)

Table A.7.5.18.1.1-4: OTA related test parameters for subsequent CPC from FR1-FR2 NR-DC to FR1-FR2 NR-DC (Cell 2, Cell 3)

## A.7.5.18.1.2Test Requirements

TRRC_delay +TEvent_DU for PSCell addition (Cell 2) occurs during T1 as the PSCell addition condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall start to transmit the PRACH to Cell 2 less than Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms from the start of T2.

The UE shall transmit the PRACH to Cell 3 less than Tconfig_PSCell_Subsequent_Change_Conditional Note1 from the start of T3.

All the above test requirements shall be fulfilled for the observed PSCell change delay to be counted as correct. The rate of correct observed PSCell change delay during repeated tests shall be at least 90 %.

NOTE 1:The subsequent Conditional PSCell change delay during T3 can be expressed as follows:

Tconfig_PSCell_Subsequent_Change_Conditional = TEvent_DU +Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms

Where:

TEvent_DU  = 0 ms

Tmeasure = 6720 ms for power class 1 or 4160 for power class 2/3/4

TUE_preparation = 10 ms

Tprocessing = 40 ms

T∆ = 20 ms

TPSCell_ DU = 1*10+10 = 20 ms

## A.7.5.18.2Inter-frequency subsequent CPA from FR1-FR2 NR-DC to FR1-FR2 NR-DC

## A.7.5.18.2.1Test Purpose and Environment

The purpose of this test is to verify that the subsequent conditional NR PSCell addition under NR-DC is within the requirements stated in clause 8.9C.2.

For UE supporting subsequent conditional PSCell addition/change, UE only needs to pass either inter-frequency CPA from FR1-FR1 NR-DC to FR1-FR1 NR-DC defined in clause A.6.5.12.2 or inter-frequency CPA from FR1-FR2 NR-DC to FR1-FR2 NR-DC defined in clause A.7.5.18.2.

For UE which can pass this test, test of conditional PSCell addition and release delay defined in A.7.5.12 can be skipped.

Supported test configurations are shown in A.7.5.18.2.1-1. The test parameters for the NR cell 1 are given in table A.3.7A. The NR cell 1 once set up is not changed across time.

The test parameters for NR cell 2, NR cell 3 are given in Tables A.7.5.18.2.1-2, cell-specific parameters in A.7.5.18.2.1-3 and OTA parameters in A.7.5.18.2.1-4 below.  The test comprises of three NR carrier. There are three cells and one cell on each carrier. Before the test starts the UE is connected to Cell 1 (NR PCell) on radio channel 1, but is not aware of Cell 2 (NR candidate NR PSCell 1) on radio channel 2 and Cell 3 (NR candidate PSCell 2) on radio channel 3. The test consists of  four successive time periods with duration of T1, T2, T3, T4.

During T1, the UE does not have any timing information of Cell 2 and Cell 3.  The TE shall configure subsequent conditional PSCell addition/change with Cell 2 and Cell 3 as target PSCells during T1, at a time earlier than TRRC_delay before the beginning of T2.

At the start of T2, Cell 2 becomes detectable and meets the PSCell addition condition. UE shall be able to measure and detect that the condition is fulfilled, after which the UE shall transmit the PRACH preamble to Cell 2. Upon PSCell addition complete (UE transmits SN RRCReconfigurationcomplete message), T3 starts.

During T3, the TE shall send a RRCRconfiguration message to the UE to release PSCell (Cell 2) on radio channel 2. Upon PSCell release complete (UE transmits SN RRCReconfigurationcomplete message), T4 starts.

At the start of T4, Cell 3 becomes detectable and meets the addition condition. UE shall be able to measure and detect that the condition is fulfilled, after which UE shall send PRACH to the PSCell (Cell 3).

Table A.7.5.18.2.1-1: Supported test configurations for Inter-frequency Subsequent CPA from FR1-FR2 NR-DC to FR1-FR2 NR-DC

Table A.7.5.18.2.1-2: General Test Parameters for subsequent CPA

Table A.7.5.18.2.1-3: Cell Specific Parameters for subsequent CPA (cell 2, cell 3)

Table A.7.5.18.2.1-4: OTA related test parameters

## A.7.5.18.2.2Test Requirements

TRRC_delay + TEvent_DU for PSCell addition (Cell 2) occurs during T1 as the PSCell addition condition becomes satisfied at the start of T2. The test shall verify that there are no interruptions during T1.

The UE shall transmit the PRACH to PSCell (Cell 2) less than Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 msfrom the start of T2.

The UE shall transmit the PRACH to PSCell (Cell 3) less than Tconfig_PSCell_Addition_Conditional Note1 from the start of T4.

All the above test requirements shall be fulfilled for the observed PSCell addition delay and PSCell release delay to be counted as correct. The rate of correct observed PSCell addition delay and PSCell release delay during repeated tests shall be at least 90 %.

NOTE 1:The PSCell addition delay during T2 can be expressed as follows:

Tconfig_PSCell_Addition_Conditional = TEvent_DU +  Tmeasure + TUE_preparation + Tprocessing + T∆ + TPSCell_ DU + 2 ms

Where:

TEvent_DU = 0

Tmeasure = 6720 ms for power class 1 or 4160 for power class 2/3/4

TUE_preparation = 10 ms

Tprocessing = 40 ms

T∆ = 20 ms

TPSCell_ DU = 1*10+10 = 20 ms
